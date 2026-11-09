"""
Verify the k = 4 truncated classical BV master equation in the finite cyclic L_infty
model of ``verify-bv-master-equation.py`` (record 058 §7, addendum node C5.4).

Reuses the model, the tree-level transfer, the Grassmann algebra and the antibracket
matrix P = om^{-1} diag((-1)^deg) of the k <= 3 script unchanged; only the nilpotency
order is raised to g^6 = 0 (M_ORDER = 5) so that S_7 (the transferred l_6) is kept
and the g^5 coefficient of the truncated bracket can be compared with the lemma.

Checks (named after the addendum nodes of record 058 §7.2):
  C5.4-B1            untruncated S_eff: [g^m](S,S) = 0 for m <= 5 (independent).
  C5.4-B1-nontrivial S_7 != 0 (the g^5 remainder has a source).
  C5.4-B2-vanish     k = 4: [g^m](S^(4),S^(4)) = 0 for m <= 4        (bookkeeping).
  C5.4-B2-rem        k = 4: [g^5](S^(4),S^(4)) = -2 (S_2,S_7)         (bookkeeping;
                     the kept-vertex form 2(S_3,S_6)+2(S_4,S_5) is the definition of
                     the left-hand side and is not a separate check); -nonzero,
                     -break (coefficient -1 fails).
  C5.4-B3            two constant-coefficient pairs (Y2, Y2+) at g^2 and (Y3, Y3+) at
                     g^4: (S_BV,S_BV) = (S^(4),S^(4)) through g^5 (056 lemma (e));
                     -mixing: a Psi-INDEPENDENT, antifield-free Y2 Y3 cross term
                     leaves the identity intact (lemma (e) needs the auxiliary
                     sector antifield-free AND Psi-independent). The actual source
                     coupling u(Sigma_2).Sigma_3 is Psi-dependent; it is removed by
                     the exact Sigma_3 shift, not by an irrelevance argument, so this
                     check does not test it;
                     -break-mixing-psi: a Psi-DEPENDENT antifield-free cross term
                     g^3 psi_even Y2 Y3 (psi_even: a field whose antifield occurs in
                     S^(4)) spoils it -- break leg, must FAIL;
                     -break-Y2+, -break-Y3+: a psi-dependent antifield term of either
                     pair spoils it (one break leg per pair).
                     The tolerance is relative to max|(S^(4),S^(4))| (floored at 1e-300).
  Break legs of B1 within the k = 4 truncation (must FAIL): S_6 -> -S_6 (g^4);
  S_6 -> 0 (l_5^tr -> 0, the arity-5 relation, g^4); antifield-number-two monomials
  dropped from S_5 or S_6 (g^3 or g^4).

Independent content vs bookkeeping: as in the k <= 3 script — B1 and its break legs
are the independent content; B2-* and B3-* are rearrangements of the same coefficient
table (B2-rem is B1 at m = 5; B2-rem-break is implied by B2-rem and B2-rem-nonzero)
and 056's lemma (e) on toy pairs. C5.4-B1-nontrivial is a precondition (S_7 != 0),
counted apart: per seed 1 independent (B1) + 1 precondition + 7 falsifiers (4 break
legs of B1, B3-break-Y2+, -Y3+, -mixing-psi) + 6 bookkeeping.

Not verified: the string vertices (PH27), the F^(7) term (a function of the
ghost-number-2 field, absent from the model), properness. Arithmetic: float64 with
per-order relative scales as in the parent script (the brief's exact/40-digit clause
is not met by the reused code; reported).

Run: OMP_NUM_THREADS=1 .venv/bin/python codes/verify-bv-master-k4.py
"""

from __future__ import annotations

import importlib.util
import pathlib
import sys
import time

import numpy as np

_here = pathlib.Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location(
    "bv", _here / "verify-bv-master-equation.py"
)
bv = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(bv)

bv.M_ORDER = 5  # keep S_n through n = 7; GP reads the module global at call time
M = bv.M_ORDER
GP, TOL = bv.GP, bv.TOL
K4 = 4


def kind_of(name: str) -> str:
    if "B1-nontrivial" in name:
        return "precondition"
    if "B2-rem-break" in name:  # implied by B2-rem and B2-rem-nonzero
        return "bookkeeping"
    if "break" in name or "control" in name:
        return "falsifier"
    if "-B2" in name or "-B3" in name:
        return "bookkeeping"
    return "independent"


failures: list[str] = []
tally = {"independent": 0, "precondition": 0, "falsifier": 0, "bookkeeping": 0}


def report(name: str, ok: bool, detail: str = "") -> None:
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""))
    tally[kind_of(name)] += 1
    if not ok:
        failures.append(name)


def S_by_n(S: GP) -> dict[int, GP]:
    out = {}
    for m in range(M + 1):
        Sm = S.gpart(m)
        Sm_h = GP({(0, k[1], k[2]): v for k, v in Sm.t.items()})
        if Sm_h.t and any(len(k[1]) + len(k[2]) != m + 2 for k in Sm_h.t):
            raise ValueError("S_eff not homogeneous of degree gpow + 2")
        out[m + 2] = Sm_h
    return out


def pair_table(Sn, P, nk, nmax):
    tab = {}
    for a in range(2, nmax + 1):
        for b in range(2, nmax + 1):
            if a + b - 4 <= M and a in Sn and b in Sn:
                tab[(a, b)] = bv.antibracket(Sn[a], Sn[b], P, nk)
    return tab


def scale_of(Sn, P, m):
    pmax = np.abs(P).max()
    vals = [Sn[a].maxabs() * Sn[b].maxabs() * pmax
            for a in Sn for b in Sn if a + b - 4 == m]
    return max(vals + [1e-300])


def rel(x: GP, sc: float) -> float:
    return x.maxabs() / sc


def one_seed(seed: int, wdeg: list[int], cut: tuple[int, ...]) -> None:
    t0 = time.time()
    print(f"\n=== seed {seed}: W degrees {wdeg}, integrated-out C'' degrees {cut}, "
          f"g^{M + 1} = 0")
    mod = bv.run_model(seed, wdeg, cut)
    nk = mod["nk"]
    Sn = S_by_n(bv.effective_action(mod))
    P = bv.bv_poisson(mod["om"], mod["kdeg"])
    print(f"    retract dim {nk}; |S_n| = "
          + ", ".join(f"{n}:{Sn[n].maxabs():.2e}" for n in sorted(Sn))
          + f"  [{time.time() - t0:.0f}s]")
    report(f"C5.4-B1-nontrivial seed {seed}: transferred S_7 != 0 (l_6^tr != 0)",
           Sn[7].maxabs() > 1e-8, f"|S_7| = {Sn[7].maxabs():.2e}")
    tab = pair_table(Sn, P, nk, M + 2)
    print(f"    pair table done [{time.time() - t0:.0f}s]")
    r1 = [rel(bv.J(tab, m), scale_of(Sn, P, m)) for m in range(M + 1)]
    report(f"C5.4-B1 seed {seed}: untruncated [g^m](S,S)=0, m<={M}",
           max(r1) < TOL, "rel = " + ", ".join(f"{x:.1e}" for x in r1))
    # ---- B2 truncation lemma at k = 4
    k = K4
    keep = lambda a, b: a <= k + 2 and b <= k + 2  # noqa: E731
    rk = [rel(bv.J(tab, m, keep), scale_of(Sn, P, m)) for m in range(k + 1)]
    report(f"C5.4-B2-vanish k={k} seed {seed}: [g^m](S^(4),S^(4))=0 for m<=4",
           max(rk) < TOL, "rel = " + ", ".join(f"{x:.1e}" for x in rk))
    lhs = bv.J(tab, k + 1, keep)  # = 2(S_3,S_6) + 2(S_4,S_5) by construction
    rhs = (tab[(2, 7)] + tab[(7, 2)]).scale(-1.0)
    sc = scale_of(Sn, P, k + 1)
    report(f"C5.4-B2-rem k={k} seed {seed}: [g^5](S^(4),S^(4)) = -2(S_2,S_7)",
           rel(lhs + rhs.scale(-1.0), sc) < TOL,
           f"|remainder| rel = {rel(lhs, sc):.2e}, mismatch = "
           f"{rel(lhs + rhs.scale(-1.0), sc):.1e}")
    if Sn[7].maxabs() > 1e-12:
        report(f"C5.4-B2-rem-nonzero k={k} seed {seed}: remainder != 0 (S_7 != 0)",
               rel(lhs, sc) > 1e-6, f"rel {rel(lhs, sc):.2e}")
        report(f"C5.4-B2-rem-break k={k} seed {seed}: coefficient -1 instead of -2 fails",
               rel(lhs + rhs.scale(-0.5), sc) > 1e-6)
    else:
        print(f"    [n/a] seed {seed}: tower terminates (S_7 = 0), remainder 0 as predicted")
    # ---- break legs of B1 within the k = 4 truncation
    def trunc_J(Sb: dict, m: int) -> float:
        tb = pair_table(Sb, P, nk, 6)
        return rel(bv.J(tb, m, keep), scale_of(Sb, P, m))

    Sb = dict(Sn); Sb[6] = Sn[6].scale(-1.0)
    x = trunc_J(Sb, 4)
    report(f"C5.4-break-sign seed {seed}: S_6 -> -S_6 fails at g^4", x > 1e-6, f"rel {x:.2e}")
    Sb = dict(Sn); Sb[6] = GP()
    x = trunc_J(Sb, 4)
    report(f"C5.4-break-l5 seed {seed}: S_6 -> 0 (l_5^tr -> 0) fails at g^4 (arity-5 relation)",
           x > 1e-6, f"rel {x:.2e}")
    anti = {a for a in range(nk) if mod["kdeg"][a] >= 2}

    def n_anti(k_: tuple) -> int:
        return sum(1 for a in k_[1] + k_[2] if a in anti)

    for n2 in (5, 6):
        quad = [k_ for k_ in Sn[n2].t if n_anti(k_) == 2 and abs(Sn[n2].t[k_]) > 1e-12]
        if not quad:
            print(f"    [n/a] S_{n2} has no antifield-number-two monomials")
            continue
        Sb = dict(Sn)
        Sb[n2] = GP({k_: c for k_, c in Sn[n2].t.items() if n_anti(k_) != 2})
        x = trunc_J(Sb, n2 - 2)
        report(f"C5.4-break-antifield2 seed {seed}: {len(quad)} antifield-number-two "
               f"monomials dropped from S_{n2} fail at g^{n2 - 2}", x > 1e-6, f"rel {x:.2e}")
    # ---- B3: two constant-coefficient pairs, (Y2,Y2+) at g^2 and (Y3,Y3+) at g^4
    rng = np.random.default_rng(seed + 2000)
    ny = 2  # per pair
    # variables: nk psi | Y2 (ny even) | Y3 (ny even) | Y2+ (ny odd) | Y3+ (ny odd)
    GP.par = GP.par[:nk] + [0] * (2 * ny) + [1] * (2 * ny)
    ntot = nk + 4 * ny
    PY = np.zeros((ntot, ntot)); PY[:nk, :nk] = P
    for i in range(2 * ny):  # C2: P^{Y Y+} = 1, P^{Y+ Y} = -1
        PY[nk + i, nk + 2 * ny + i] = 1.0
        PY[nk + 2 * ny + i, nk + i] = -1.0
    def quad_form(off: int, coef: float) -> GP:
        Kf = rng.standard_normal((ny, ny)); Kf = Kf + Kf.T
        out = GP()
        for i in range(ny):
            for j in range(ny):
                out = out + (GP.var(nk + off + i) * GP.var(nk + off + j)).scale(coef * Kf[i, j])
        return out
    S4 = GP()
    for n in range(2, k + 3):
        S4 = S4 + Sn[n].gshift(n - 2)
    SBV = S4 + quad_form(0, -1.0 / 24.0).gshift(2) + quad_form(ny, -1.0 / 720.0).gshift(4)
    base = bv.antibracket(S4, S4, PY, ntot)
    sc = max(base.maxabs(), 1e-300)  # relative tolerance (was absolute: max(., 1.0))
    def mismatch(Sx: GP) -> float:
        return (bv.antibracket(Sx, Sx, PY, ntot) + base.scale(-1.0)).maxabs() / sc
    report(f"C5.4-B3 k={k} seed {seed}: (S_BV,S_BV) = (S^(4),S^(4)) with the two pairs through g^{M}",
           mismatch(SBV) < TOL, f"mismatch {mismatch(SBV):.1e}")
    mix = GP()
    for i in range(ny):
        for j in range(ny):
            mix = mix + (GP.var(nk + i) * GP.var(nk + ny + j)).scale(rng.standard_normal())
    odd_psi = next(a for a in range(nk) if GP.par[a] == 1)
    Smix = SBV + mix.gshift(3)
    report(f"C5.4-B3-mixing k={k} seed {seed}: a Psi-independent antifield-free g^3 Y2 Y3 cross term leaves it intact",
           mismatch(Smix) < TOL, f"mismatch {mismatch(Smix):.1e}")
    # Psi-dependent cross term: psi_even Y2 Y3 with psi_even's antifield present in S^(4)
    used = {i for kk in S4.t for i in kk[1] + kk[2]}
    even_psi = next(a for a in range(nk) if GP.par[a] == 0
                    and any(abs(P[a, b]) > 0 and b in used for b in range(nk)))
    mixpsi = GP()
    for i in range(ny):
        for j in range(ny):
            mixpsi = mixpsi + (GP.var(even_psi) * GP.var(nk + i) * GP.var(nk + ny + j)).scale(rng.standard_normal())
    Smp = SBV + mixpsi.gshift(3)
    report(f"C5.4-B3-break-mixing-psi k={k} seed {seed}: a Psi-dependent antifield-free g^3 psi Y2 Y3 term spoils it",
           mismatch(Smp) > 1e-6, f"mismatch {mismatch(Smp):.1e}")
    bad2 = SBV + (GP.var(nk + 2 * ny) * GP.var(odd_psi)).gshift(2)
    report(f"C5.4-B3-break-Y2+ k={k} seed {seed}: a psi-dependent g^2 Y2+ term spoils it",
           mismatch(bad2) > 1e-6, f"mismatch {mismatch(bad2):.1e}")
    bad3 = SBV + (GP.var(nk + 3 * ny) * GP.var(odd_psi)).gshift(4)
    report(f"C5.4-B3-break-Y3+ k={k} seed {seed}: a psi-dependent g^4 Y3+ term spoils it",
           mismatch(bad3) > 1e-6, f"mismatch {mismatch(bad3):.1e}")
    print(f"    seed {seed} done [{time.time() - t0:.0f}s]")


if __name__ == "__main__":
    seeds = [int(s) for s in sys.argv[1:]] or [11, 12, 13]
    print(f"seeds {seeds}; model W degrees [0,1,2], cut (-1,3) (retract 14); M_ORDER = {M}")
    for seed in seeds:
        one_seed(seed, [0, 1, 2], (-1, 3))
    ntot = sum(tally.values())
    print(f"\nchecks: {ntot} total = {tally['independent']} independent + "
          f"{tally['precondition']} preconditions + {tally['falsifier']} falsifiers (break legs) + "
          f"{tally['bookkeeping']} bookkeeping (B2, B3)")
    print(f"SUMMARY: {len(failures)} failure(s)" + (f": {failures}" if failures else ""))
    sys.exit(1 if failures else 0)
