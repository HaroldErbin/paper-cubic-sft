"""
Task 19c: the coupling c g_s V_3(Sigma_2, Psi) required by the Maurer-Cartan components.

Record: agent/derivations/109-mc-cubic-coupling.md (claim-tree nodes in brackets).

Setting.  S' = S + c g_s V_3(Sigma_2, Psi), S the cubic action of the quartic section,
  S = 1/2 V_2(Psi, Psi) + g_s/3! V_3(Psi^3) + 2 g_s^2/4! V_4(Sigma_2, Psi^2)
      - g_s^2/4! V_4(Sigma_2, Sigma_2),
evaluated by tensor contraction of the model's vertices on the ghost-2 sector; the
Maurer-Cartan components (MC.5), (MC.7) of record 103 are computed by 103's literal CFL
path (mc_block), the raised operations p_{1,2}, p_{2,2}, l_n by raise_family (engine of
codes/verify-ibl-generating-sign.py), neither edited.

Checks (each named after the node it tests):
  C1    [C1]  (1.7): S_MC(Psi, Sigma/6), built from the vertices on e^{Psi + Psi_2} in the
              symmetric algebra, minus S'(Psi, Sigma) at c = 1/6 equals S_4 + g^2/18
              V_4(Sigma, Sigma), at three g.  -break: Psi_2 = Sigma (alpha = 1); the
              difference without S_4.
  C2    [C2]  (1.5), (1.6): the gradients of S' (exact finite differences of the action
              polynomial) equal the literal components with Psi_2 = Sigma/6 plus the
              predicted residuals -g^2/6 l3(Psi^3) and -g^2/9 p22(Sigma) (raised
              operations), at c = 1/6, three g.  -break: c = 1/3; residuals dropped.
  C3    [C3.1, C3.2]  elimination: exact linear solve of the Sigma equation at six g,
              Laurent coefficients g^-2..g^3 extracted; g^-2, g^-1, g^3 vanish; g^0 = S_2 +
              6 c^2 W with W = <X, y>_2, y = p12(Psi) (3,3) part, p22(X) = y (raised
              operations); g^1 = (1 + 6c) V_3/6; g^2 = V_4/24; the g^0 excess scales as
              t^2 under Psi -> t Psi.  -break: 3 c^2 W; quartic scaling t^4.
  C3.3  [C3.3] kernel model (V_4 on the ghost-2 sector replaced by a sum of two fourth
              powers, K of rank 2 on Sym^2): N in ker K nonzero; S'(Sigma + lam N) -
              S'(Sigma) = lam c g V_3(N, Psi) != 0; Sigma equation inconsistent for generic
              Psi, consistent on V_3(N, Psi) = 0 and at c = 0 (control).
  C4.4  [C4.4] S' - 6c^2 W - 6c S_3 eliminates to S_<=4 exactly (Laurent coefficients),
              and its g^0 Psi equation differs from that of (MC.5) (= Q_B Psi, literal) by
              -12 c^2 D Psi != 0.  -break: the counterterm -3 c^2 W does not restore it.
  C4.5  [C4.5] W(Psi) != 0 and D Psi != 0 at random Psi.
  C5    [C5]  free model (V_2(gh1, gh3) = 0, V_2 of rank 1 on the ghost-2 sector): Q^2 = 0,
              Q kills nothing exact at ghost 2 (Q from ghost 1 is zero), rank B_Q = 1;
              rank(B_Q + 12 c^2 B_W) = 2 at c = 1/6, W(psi_0) != 0 on ker B_Q.
              -control: c = 0 gives equal ranks (no break leg: the claim is a rank
              count in one model).
NOT verified: H-W for the closed-string vertices (finite models only); the L-infinity
relations (not imposed: the identities checked are algebraic and do not use them, except
the meaning of C5, whose model has Q^2 = 0 but random V_3, V_4); gauge invariance
(step 3, not done: stop condition); genus >= 1; Sigma_2 strands other than (2, 2).
Method: exact Fractions; model and fields of record 103's Data (seeds 20261018, 20261019).

Usage:  uv run --no-sync python codes/verify-mc-cubic-coupling.py
"""

from __future__ import annotations

import copy
import importlib.util
import itertools
import random
import sys
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location(
    "mc103", ROOT / "verify-ibl-mc-conventions.py"
)
mc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mc)
iblgen = mc.iblgen

SEEDS = (20261018, 20261019)
RESULTS: list[tuple[str, bool]] = []
C = F(1, 6)  # fixed by S_MC (record block 1), never fitted


def check(name: str, ok: bool, detail: str = "") -> None:
    """Record and print one named PASS/FAIL check."""
    RESULTS.append((name, bool(ok)))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}")


# ---------------------------------------------------------------- action level
def vcon(M, n: int, tensors: list) -> F:
    """V_n contracted with tensors (dicts {index tuple: value}), ranks summing to n."""
    Vn = M.V.get(n, {})
    tot = F(0)
    for combo in itertools.product(*[list(T.items()) for T in tensors]):
        idx = sum((k for k, _ in combo), ())
        v = Vn.get(idx, 0)
        if v:
            w = F(v)
            for _, x in combo:
                w *= x
            tot += w
    return tot


def outer(a: dict, b: dict) -> dict:
    return {ka + kb: va * vb for ka, va in a.items() for kb, vb in b.items()}


def tadd(A: dict, B: dict, c=1) -> dict:
    out = dict(A)
    for k, v in B.items():
        out[k] = out.get(k, 0) + c * v
    return {k: v for k, v in out.items() if v != 0}


def tscale(A: dict, c) -> dict:
    return {k: c * v for k, v in A.items() if c * v != 0}


def action(M, psi: dict, sig: dict, g, c=C, sig_quad=F(-1, 24), mix=F(1, 12)) -> F:
    """S' of (1.2) by tensor contraction (all strands even: no signs)."""
    pp = outer(psi, psi)
    return (
        F(1, 2) * vcon(M, 2, [psi, psi])
        + g / 6 * vcon(M, 3, [psi, psi, psi])
        + c * g * vcon(M, 3, [sig, psi])
        + mix * g**2 * vcon(M, 4, [sig, pp])
        + sig_quad * g**2 * vcon(M, 4, [sig, sig])
    )


def deriv(fun):
    """Exact first derivative at 0 of a polynomial of degree <= 4."""
    return (fun(-2) - 8 * fun(-1) + 8 * fun(1) - fun(2)) / 12


def gh2(M) -> list[int]:
    return [a for a in range(M.N) if M.gh[a] == 2]


def sym_basis(M) -> list[dict]:
    """Basis E_ab (a <= b) of symmetric tensors with (2, 2) strands."""
    idx = gh2(M)
    out = []
    for i, a in enumerate(idx):
        for b in idx[i:]:
            out.append({(a, b): F(1), (b, a): F(1)} if a != b else {(a, a): F(1)})
    return out


def eliminate(M, psi: dict, g, c=C, extra=None):
    """Stationary value of S' in Sigma (exact solve); (consistent, value, Sigma*)."""
    E = sym_basis(M)
    pp = outer(psi, psi)
    A = [[g**2 / 12 * vcon(M, 4, [Ei, Ej]) for Ej in E] for Ei in E]
    L = [c * g * vcon(M, 3, [Ei, psi]) + g**2 / 12 * vcon(M, 4, [Ei, pp]) for Ei in E]
    ok, s = mc.gauss_consistent(A, L)
    if not ok:
        return False, None, None
    sig = {}
    for si, Ei in zip(s, E):
        sig = tadd(sig, Ei, si)
    val = action(M, psi, sig, g, c)
    if extra is not None:
        val += extra(g)
    # value from the completed square, an internal consistency leg
    val2 = (
        F(1, 2) * vcon(M, 2, [psi, psi])
        + g / 6 * vcon(M, 3, [psi, psi, psi])
        + sum(F(1, 2) * li * si for li, si in zip(L, s))
    )
    if extra is not None:
        val2 += extra(g)
    if val != val2:
        raise RuntimeError("completed-square value disagrees with the direct one")
    return True, val, sig


def laurent(points: list, values: list, pmin: int, pmax: int) -> dict:
    """Exact Laurent coefficients from as many points as powers."""
    rows = [[x**p for p in range(pmin, pmax + 1)] for x in points]
    ok, sol = mc.gauss_consistent(rows, values)
    if not ok:
        raise RuntimeError("Laurent fit inconsistent")
    return dict(zip(range(pmin, pmax + 1), sol))


G_PTS = [F(1, 2), F(2, 3), F(-3, 4), F(5, 3), F(-2), F(7, 5)]


# ---------------------------------------------------------------- raised side
def pair2(M, A: dict, T: dict) -> F:
    """<A, T>_2 = sum A^{pq} T^{c1 c2} g_{p c1} g_{q c2} (A with even strands)."""
    return sum(
        (
            av * tv * M.g.get((p, c1), 0) * M.g.get((q, c2), 0)
            for (p, q), av in A.items()
            for (c1, c2), tv in T.items()
        ),
        F(0),
    )


def part33(M, T: dict) -> dict:
    return {k: v for k, v in T.items() if all(M.gh[i] == 3 for i in k)}


def W_raised(M, fam: dict, psi_a: dict, psi_b: dict) -> F:
    """W(a, b) = <X_a, y_b>_2, y = p12(psi) (3,3) part, p22(X_a) = y_a on (3,3)."""
    E = sym_basis(M)
    ya = part33(M, mc.feed(M, fam[(1, 2)], [(psi_a, 1)]))
    yb = part33(M, mc.feed(M, fam[(1, 2)], [(psi_b, 1)]))
    cols = [part33(M, mc.feed(M, fam[(2, 2)], [(Ei, 2)])) for Ei in E]
    keys = sorted(set().union(*cols, ya))
    rows = [[col.get(k, 0) for col in cols] for k in keys]
    ok, s = mc.gauss_consistent(rows, [ya.get(k, 0) for k in keys])
    if not ok:
        raise RuntimeError("p22 not invertible on the (2,2) sector")
    X = {}
    for si, Ei in zip(s, E):
        X = tadd(X, Ei, si)
    return pair2(M, X, yb)


def families(M) -> dict:
    return {
        (k, l): iblgen.raise_family(M, k, l, "g")
        for k in range(1, 4)
        for l in range(1, 4)
        if k + l <= 4
    }


def literal_M1(D, P: dict, S6: dict, g) -> dict:
    """(MC.5) by 103's literal path, Psi_2 = S6 (symmetric-algebra element)."""
    eps = D.M.eps
    m = mc.s_add(P, S6)
    out = {}
    for k in (1, 2, 3):
        out = mc.s_add(out, mc.mc_block(eps, D.fam["g"][(k, 1)], k, m)[1], g ** (k - 1))
    return out


def literal_M26(D, P: dict, S6: dict, g) -> dict:
    """(MC.7) by 103's literal path (two-output blocks, shifted output parity)."""
    M = D.M
    m = mc.s_add(P, S6)
    out = {}
    for k in (1, 2):
        blk = mc.mc_block(M.eps, D.fam["g"][(k, 2)], k, m, mc.eps_out(M, 2))[2]
        out = mc.s_add(out, blk, g**k)
    return out


# ---------------------------------------------------------------- checks
def run(seed: int) -> None:
    print(f"--- seed {seed}")
    D = mc.Data(seed)
    M = D.M
    eps = M.eps
    psi, sig = D.psi1, D.psi2_22
    P, S = mc.to_sym(eps, psi), mc.to_sym(eps, sig)
    S6 = {w: x / 6 for w, x in S.items()}
    fam = D.fam["g"]
    gs3 = (F(3, 7), F(-5, 2), F(4, 3))

    # C1: action level (1.7)
    def s_mc(Pp, Ss, g):
        E = mc.s_exp(eps, mc.s_add(Pp, Ss))
        tot = F(0)
        for n in (2, 3, 4):
            Vn = M.V.get(n, {})
            vn = sum((x * Vn.get(w, 0) for w, x in E.items() if len(w) == n), F(0))
            if n == 2:
                V2 = M.V.get(2, {})
                vn -= sum((x * V2.get(w, 0) for w, x in Ss.items()), F(0))
            tot += g ** (n - 2) * vn
        return tot

    def diff17(g, alpha, with_s4=True):
        Sa = {w: alpha * x for w, x in S.items()}
        pred = g**2 / 18 * vcon(M, 4, [sig, sig])
        if with_s4:
            pred += g**2 / 24 * vcon(M, 4, [psi, psi, psi, psi])
        return s_mc(P, Sa, g) - action(M, psi, sig, g) == pred and pred != 0

    ok1 = all(diff17(g, F(1, 6)) for g in gs3)
    br1a = all(diff17(g, F(1)) for g in gs3)
    br1b = all(diff17(g, F(1, 6), with_s4=False) for g in gs3)
    check(
        f"C1 (seed {seed})",
        ok1 and not br1a and not br1b,
        "S_MC(Psi, Sigma/6) - S'(Psi, Sigma) = S_4 + g^2/18 V_4(Sigma, Sigma) at c = 1/6,"
        f" three g: {ok1}; break legs FAIL as expected (alpha = 1: {not br1a};"
        f" without S_4: {not br1b})",
    )

    # C2: gradients of S' vs literal components plus predicted residuals
    def c2(g, c, resid=True):
        okk = True
        M1 = literal_M1(D, P, S6, g)
        l3psi3 = mc.feed(M, fam[(3, 1)], [(psi, 1)] * 3)
        l2sig = mc.feed(M, fam[(2, 1)], [(sig, 2)])
        for x in gh2(M):
            ex = {(x,): F(1)}
            lhs = deriv(lambda t: action(M, tadd(psi, ex, t), sig, g, c))
            rhs = sum((M.g.get((x, w[0]), 0) * v for w, v in M1.items()), F(0))
            if resid:
                rhs += (
                    -(g**2)
                    / 6
                    * sum((M.g.get((x, w[0]), 0) * v for w, v in l3psi3.items()), F(0))
                )
                rhs += (
                    (c - C)
                    * g
                    * sum((M.g.get((x, w[0]), 0) * v for w, v in l2sig.items()), F(0))
                )
            okk &= lhs == rhs
        # E_2: tensor form of (MC.7) at Psi_2 = Sigma/6, tied to the literal path
        p12 = mc.feed(M, fam[(1, 2)], [(psi, 1)])
        p22pp = mc.feed(M, fam[(2, 2)], [(psi, 1), (psi, 1)])
        p22s = mc.feed(M, fam[(2, 2)], [(sig, 2)])
        T6 = tadd(tadd(tscale(p12, g), p22pp, g**2 / 2), p22s, g**2 / 6)
        okk &= mc.to_sym(mc.eps_out(M, 2), T6) == literal_M26(D, P, S6, g)
        for AB in sym_basis(M):
            lhs = deriv(lambda t: action(M, psi, tadd(sig, AB, t), g, c))
            rhs = pair2(M, AB, T6) / 6
            if resid:
                rhs += (c - C) * g * pair2(M, AB, p12) - g**2 / 9 * pair2(M, AB, p22s)
            okk &= lhs == rhs
        return okk

    ok2 = all(c2(g, C) for g in gs3)
    br2a = all(c2(g, F(1, 3), resid=False) for g in gs3)
    br2b = all(c2(g, C, resid=False) for g in gs3)
    check(
        f"C2 (seed {seed})",
        ok2 and not br2a and not br2b,
        "delta S' = literal (MC.5), (1/6)(MC.7) at Psi_2 = Sigma/6 plus -g^2/6 l3(Psi^3)"
        " (M-e) and -g^2/9 p22(Sigma) (M-c), c = 1/6, three g, the tensor (MC.7) equal to"
        f" the literal block: {ok2}; break legs FAIL as expected (c = 1/3: {not br2a};"
        f" residuals dropped: {not br2b})",
    )

    # C3: elimination, Laurent coefficients
    def coeffs(ps, c=C, extra=None):
        vals = []
        for g in G_PTS:
            okc, v, _ = eliminate(M, ps, g, c, extra)
            if not okc:
                raise RuntimeError("Sigma equation inconsistent in the generic model")
            vals.append(v)
        return laurent(G_PTS, vals, -2, 3)

    a = coeffs(psi)
    S2 = F(1, 2) * vcon(M, 2, [psi, psi])
    V3 = vcon(M, 3, [psi, psi, psi])
    V4 = vcon(M, 4, [psi, psi, psi, psi])
    W = W_raised(M, fam, psi, psi)
    ok3 = (
        a[-2] == 0
        and a[-1] == 0
        and a[3] == 0
        and a[0] == S2 + 6 * C**2 * W
        and a[1] == (1 + 6 * C) * V3 / 6
        and a[2] == V4 / 24
        and W != 0
    )
    psi2x = tscale(psi, 2)
    a2 = coeffs(psi2x)
    S2x = F(1, 2) * vcon(M, 2, [psi2x, psi2x])
    quad = (a2[0] - S2x) == 4 * (a[0] - S2)
    br3a = a[0] == S2 + 3 * C**2 * W
    br3b = (a2[0] - S2x) == 16 * (a[0] - S2)
    check(
        f"C3 (seed {seed})",
        ok3 and quad and not br3a and not br3b,
        "eliminated S'[Psi] = S_2 + 6c^2 W + (1 + 6c) S_3 + S_4, no g^-2, g^-1, g^3;"
        f" W (raised p12, p22) = {W}; g^0 excess quadratic under Psi -> 2 Psi: {quad};"
        f" break legs FAIL as expected (3c^2 W: {not br3a}; quartic scaling: {not br3b})",
    )

    # C4.5: W and its gradient nonzero
    Dpsi = [W_raised(M, fam, {(x,): F(1)}, psi) for x in gh2(M)]
    check(
        f"C4.5 (seed {seed})",
        W != 0 and any(v != 0 for v in Dpsi),
        f"W(Psi) = {W}, <e_x, D Psi> = {Dpsi}",
    )

    # C4.4: counterterms restore S_<=4, but change the g^0 Psi equation
    def ct(g, ps=psi):
        return -6 * C**2 * W_raised(M, fam, ps, ps) - C * g * vcon(M, 3, [ps, ps, ps])

    def ct_half(g, ps=psi):
        return -3 * C**2 * W_raised(M, fam, ps, ps) - C * g * vcon(M, 3, [ps, ps, ps])

    def is_s4(a4):
        return (
            a4[-2] == 0
            and a4[-1] == 0
            and a4[3] == 0
            and a4[0] == S2
            and a4[1] == V3 / 6
            and a4[2] == V4 / 24
        )

    restored = is_s4(coeffs(psi, extra=ct))
    br44 = is_s4(coeffs(psi, extra=ct_half))
    M1_0 = literal_M1(D, P, S6, F(0))  # g^0 part of (MC.5): Q_B Psi
    okq = True
    shift = []
    for i, x in enumerate(gh2(M)):
        ex = {(x,): F(1)}
        # g^0 Psi equation of S' - 6c^2 W at Sigma fixed: <e_x, Q Psi> - 12 c^2 <e_x, D Psi>
        lhs = deriv(
            lambda t: (
                F(1, 2) * vcon(M, 2, [tadd(psi, ex, t)] * 2)
                - 6 * C**2 * W_raised(M, fam, tadd(psi, ex, t), tadd(psi, ex, t))
            )
        )
        q = sum((M.g.get((x, w[0]), 0) * v for w, v in M1_0.items()), F(0))
        okq &= lhs == q - 12 * C**2 * Dpsi[i]
        shift.append(lhs - q)
    check(
        f"C4.4 (seed {seed})",
        restored and okq and any(s != 0 for s in shift) and not br44,
        f"S' - 6c^2 W - 6c S_3 eliminates to S_<=4: {restored}; its g^0 Psi equation is"
        f" Q_B Psi (literal (MC.5) at g = 0) - 12 c^2 D Psi: {okq}; shift {shift} != 0;"
        f" break leg (counterterm -3c^2 W) FAILs as expected: {not br44}",
    )

    # C3.3: kernel model
    MK = copy.deepcopy(M)
    rng = random.Random(seed + 11)
    idx = gh2(MK)
    us = [[F(rng.choice([-3, -2, -1, 1, 2, 3])) for _ in idx] for _ in range(2)]
    lam = [F(rng.choice([-2, -1, 1, 2])) for _ in range(2)]
    for key in list(MK.V[4]):
        if all(MK.gh[i] == 2 for i in key):
            del MK.V[4][key]
    for key in itertools.product(idx, repeat=4):
        v = sum(
            lam[r]
            * us[r][idx.index(key[0])]
            * us[r][idx.index(key[1])]
            * us[r][idx.index(key[2])]
            * us[r][idx.index(key[3])]
            for r in range(2)
        )
        if v:
            MK.V[4][key] = v
    E = sym_basis(MK)
    Kmat = [[vcon(MK, 4, [Ei, Ej]) for Ej in E] for Ei in E]
    # null vector of K: solve K n = 0 with the last coordinate set to 1
    okn, nsol = mc.gauss_consistent(
        [row[:-1] for row in Kmat], [-row[-1] for row in Kmat]
    )
    N = {}
    if okn:
        for si, Ei in zip(nsol + [F(1)], E):
            N = tadd(N, Ei, si)
    kerok = okn and bool(N) and all(vcon(MK, 4, [N, Ej]) == 0 for Ej in E)
    g = F(3, 7)
    v3n = vcon(MK, 3, [N, psi])
    shift_ok = all(
        action(MK, psi, tadd(sig, N, lm), g) - action(MK, psi, sig, g)
        == lm * C * g * v3n
        for lm in (F(2), F(-1, 3))
    )
    inc = not eliminate(MK, psi, g)[0]
    # constraint surface: psi' with V_3(N, psi') = 0
    lin = [vcon(MK, 3, [N, {(x,): F(1)}]) for x in idx]
    psic = {(idx[0],): lin[1], (idx[1],): -lin[0]}
    on_surface = vcon(MK, 3, [N, psic]) == 0 and bool(psic)
    cons = eliminate(MK, psic, g)[0]
    control = eliminate(MK, psi, g, c=F(0))[0]
    check(
        f"C3.3 (seed {seed})",
        kerok and v3n != 0 and shift_ok and inc and on_surface and cons and control,
        f"N in ker V_4 nonzero: {kerok}; V_3(N, Psi) = {v3n}; S'(Sigma + lam N) - S' ="
        f" lam c g V_3(N, Psi): {shift_ok}; Sigma equation inconsistent: {inc};"
        f" consistent on V_3(N, Psi) = 0: {cons}; consistent at c = 0: {control}",
    )

    # C5: free model with Q^2 = 0 and a physical-state kernel at ghost 2
    MF = copy.deepcopy(M)
    for key in list(MF.V[2]):
        if sorted(MF.gh[i] for i in key) == [1, 3]:
            del MF.V[2][key]
    u = [F(rng.choice([-3, -2, -1, 1, 2, 3])) for _ in idx]
    lq = F(rng.choice([-2, -1, 1, 2]))
    for a_, b_ in itertools.product(idx, repeat=2):
        MF.V[2][(a_, b_)] = lq * u[idx.index(a_)] * u[idx.index(b_)]
    famF = families(MF)
    Q = famF[(1, 1)]
    q2 = all(
        not mc.feed(MF, Q, [(mc.feed(MF, Q, [({(x,): F(1)}, 1)]), 1)])
        for x in range(MF.N)
    )
    q1 = not any(
        MF.gh[k[0]] == 2
        for x in range(MF.N)
        if MF.gh[x] == 1
        for k in mc.feed(MF, Q, [({(x,): F(1)}, 1)])
    )
    BQ = [[F(MF.V[2].get((x, y), 0)) for y in idx] for x in idx]
    BW = [[W_raised(MF, famF, {(x,): F(1)}, {(y,): F(1)}) for y in idx] for x in idx]

    def rank2(B):
        det = B[0][0] * B[1][1] - B[0][1] * B[1][0]
        return 2 if det != 0 else (1 if any(v != 0 for r in B for v in r) else 0)

    def total(c):
        return [[BQ[i][j] + 12 * c**2 * BW[i][j] for j in range(2)] for i in range(2)]

    psi0 = {(idx[0],): u[1], (idx[1],): -u[0]}
    w0 = W_raised(MF, famF, psi0, psi0)
    rq, rt, r0 = rank2(BQ), rank2(total(C)), rank2(total(F(0)))
    check(
        f"C5 (seed {seed})",
        q2 and q1 and rq == 1 and rt == 2 and w0 != 0 and r0 == rq,
        f"Q^2 = 0: {q2}; Q(ghost 1) = 0 at ghost 2: {q1}; rank B_Q = {rq}; rank(B_Q +"
        f" 12 c^2 B_W) = {rt} at c = 1/6; W(psi_0) = {w0} on ker B_Q; control c = 0:"
        f" rank {r0} = rank B_Q",
    )


def main() -> int:
    for seed in SEEDS:
        print(f"seed {seed}")
        run(seed)
    n_fail = sum(1 for _, ok in RESULTS if not ok)
    print(f"\n{len(RESULTS) - n_fail}/{len(RESULTS)} PASS")
    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(main())
