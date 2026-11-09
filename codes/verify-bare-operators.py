#!/usr/bin/env python3
"""verify-bare-operators.py — companion checks for derivation 115.

Question: does the quadratic form of Sigma_k in the cubic action `eq:all:action`
receive Psi-independent contributions beyond the order g^{2k-2} at which Sigma_k
enters, i.e. can the bare operator be written w_{k,k} without an order label?

Model: reused from ``codes/verify-all-orders-eom.py`` (record 100), imported, not
copied: H = R^3, Sigma_k in Sym^k(R^3) in an orthonormal basis, the action
``action(g, psi, Sig, K, odd_top, W)`` of that script, and its dressed tower
``dressed_tower(VN)`` (W_6..W_9 fixed by the diagonal rule `eq:hs7:deficit`).
The Hessian of the action in the tower is taken by exact polarization of that
``action`` function (the action is quadratic in the tower), not rebuilt from
the formulas of the record.  k_eff of Sigma_k after eliminating a set E of the
other auxiliary fields is the Schur complement divided by -2 a_k,
a_k = g^{2k-2}/(2k)!.

Checks (named after the claim-tree nodes of agent/derivations/115-...md):
  N1-psi0-block-diagonal   Hessian at Psi = 0 is blockdiag(-2 a_k W_{2k}).
  N1-psi-couplings-nonzero at Psi != 0 the off-diagonal blocks and the odd
                           dressing are nonzero (non-vacuity of N1).
  N2-psi0-k<k>             k_eff(g, Psi=0) = W_{2k} for every elimination set E
                           of the other fields, K = 4, two values of g.
  N2-gpsi-k<k>             k_eff(g, Psi) = k_eff(g t, Psi / t) for every E.
  N2-g0-k<k>               [g^0] k_eff(g, Psi) at fixed Psi != 0 = W_{2k}
                           (Cauchy contour coefficients), every E.
  N2-dressing-nonzero      k_eff(g, Psi) - W_{2k} = O(g Psi) is nonzero.
  N4-scaling-k2, -k3       [g^1], [g^2] of the nested operator (E = all higher
                           fields, K = 4 octic truncation) equal
                           `eq:hs8:scaling`: -W_{2k+1}(.,.,Psi)/(2k+1),
                           -W_{2k+2}(Psi x .,Psi x .)/((2k+1)(2k+2)).
  N4-nested-octic          the Schur complements equal `eq:hs8:dressed-3`
                           and `eq:hs8:dressed-2` at finite g.
  N4-K-dependence          the nested operator of Sigma_2 for K = 3 and K = 4
                           (odd top) agrees through g^3 and differs at g^4:
                           the label on the nested operator is informative.
  N3-closure-W6-fixed      with W_4, W_6 fixed at their own order, the value
                           matches the target through g^6 (K = 4, even top).
  N3-representative        W_6 -> W_6 + Delta with Delta Veronese-null
                           (Delta(Psi^3, Psi^3) = 0): W_7, W_8 rebuilt by the
                           diagonal rule close through g^6; w_{3,3} changes by
                           Delta, a choice made once at order g^4.
Break legs (-break suffix, also selectable with --perturb <name>):
  N2-break     a Psi-free coupling eps g^4 <Sigma_3, X Sigma_2> added to the
               action must make N2-psi0-k2 and N2-gpsi-k2 fail.
  N4-break     1/30 -> 1/31 in `eq:hs8:dressed-2` must fail N4-nested-octic.
  N3-break     W_6 + Delta with the old W_7, W_8 must miss the target.

Not tested: anything the finite model lacks (Grassmann signs, ghost numbers,
kernels of w_{k,k}: every W_{2k} is invertible here; the string-vertex origin
of the forms; convergence at K = infinity).

Usage, from the project root:
  uv run --no-project --with numpy python codes/verify-bare-operators.py \
      [--seed N] [--out DIR] [--perturb NAME]
(the project .venv has no numpy as of 2026-11-07; ~90 s, ~50 MB.)
Run of 2026-11-07, seed 20261107: 21/21 PASS (18 checks + 3 break legs);
--perturb N2-break fails 6 checks, as it must.
Exit code = number of failed checks.
"""

from __future__ import annotations

import argparse
import importlib.util
import itertools
import sys
from pathlib import Path

import numpy as np

parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
parser.add_argument("--seed", type=int, default=20261107)
parser.add_argument("--out", type=str, default=None, help="unused: writes nothing")
parser.add_argument(
    "--perturb", type=str, default=None, choices=["N2-break", "N4-break", "N3-break"]
)
ARGS = parser.parse_args()

# Import the record-100 model with its own seed taken from ours.
_path = Path(__file__).resolve().parent / "verify-all-orders-eom.py"
_argv = sys.argv
sys.argv = [str(_path), str(ARGS.seed)]
_spec = importlib.util.spec_from_file_location("allorders", _path)
M = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(M)
sys.argv = _argv

N, DIM, fact, Lmap, odd_op = M.N, M.DIM, M.fact, M.Lmap, M.odd_op
rng = np.random.default_rng(ARGS.seed + 1)
TOL = 1e-8
failures: list[str] = []


def report(name: str, ok: bool, detail: str = "") -> None:
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    if not ok:
        failures.append(name)


def rel(a, b) -> float:
    return float(np.max(np.abs(a - b)) / max(1.0, np.max(np.abs(a)), np.max(np.abs(b))))


# ------------------------------------------------------------ the action
XPERT = rng.standard_normal((DIM[3], DIM[2]))  # Psi-free coupling for N2-break


def action(g, psi, Sig, K, odd_top, W, psi_free=0.0):
    """Record-100 action, plus optionally eps g^4 <Sigma_3, X Sigma_2> (break leg)."""
    S = M.action(g, psi, Sig, K, odd_top, W)
    if psi_free and K >= 3:
        S = S + psi_free * g**4 * (Sig[3] @ XPERT @ Sig[2])
    return S


def hessian(g, psi, K, odd_top, W, psi_free=0.0, rescaled=False):
    """Hessian of the action in (Sigma_2..Sigma_K), by exact polarization.

    With ``rescaled`` the Hessian is taken in the fields g^{k-1} Sigma_k
    (`eq:all:rescaled`), whose blocks are O(1): this avoids the cancellation
    of O(g^{2k-2}) increments against the O(1) Psi part of the action.

    """
    dims = [DIM[k] for k in range(2, K + 1)]
    off = np.cumsum([0] + dims)
    D = off[-1]
    scale = {k: (g ** (-(k - 1)) if rescaled else 1.0) for k in range(2, K + 1)}

    def unpack(v):
        return {k: scale[k] * v[off[k - 2] : off[k - 1]] for k in range(2, K + 1)}

    def S(v):
        return action(g, psi, unpack(v), K, odd_top, W, psi_free)

    z = np.zeros(D, dtype=complex)
    S0 = S(z)
    E = np.eye(D)
    Si = np.array([S(E[i].astype(complex)) for i in range(D)])
    H = np.zeros((D, D), dtype=complex)
    for i in range(D):
        for j in range(i + 1, D):
            H[i, j] = H[j, i] = S((E[i] + E[j]).astype(complex)) - Si[i] - Si[j] + S0
    # diagonal: S(e) - S0 = h/2 + lin, S(-e) - S0 = h/2 - lin  =>  h = sum
    for i in range(D):
        H[i, i] = Si[i] + S(-E[i].astype(complex)) - 2 * S0
    return H, off


def k_eff(g, psi, K, odd_top, W, k, elim, psi_free=0.0):
    """Operator of Sigma_k after eliminating the levels in `elim` (Schur), / (-2 a_k)."""
    H, off = hessian(g, psi, K, odd_top, W, psi_free, rescaled=True)

    def idx(levels):
        return np.concatenate([np.arange(off[l - 2], off[l - 1]) for l in levels])

    r = idx([k])
    if elim:
        e = idx(list(elim))
        Hk = H[np.ix_(r, r)] - H[np.ix_(r, e)] @ np.linalg.solve(
            H[np.ix_(e, e)], H[np.ix_(e, r)]
        )
    else:
        Hk = H[np.ix_(r, r)]
    # Schur complements commute with the diagonal rescaling: the true block is
    # Hk g^{2k-2}, and dividing by -2 a_k = -2 g^{2k-2}/(2k)! leaves Hk (2k)!/(-2).
    return Hk * fact(2 * k) / (-2.0)


def taylor(fun, nmax, r=0.05, n=40):
    """Taylor coefficients [g^m] fun(g), m = 0..nmax, by the Cauchy formula.

    Used only for the octic truncation (no odd coupling of Sigma_4): the fitted
    W_9 of the dressed tower has entries ~2e3, which puts a pole of the nested
    operators at |g| ~ 7e-3 for |Psi| ~ 1 when W_9 is kept, inside any usable
    contour (record 115, step 3).  The exact checks N2-psi0 and N2-gpsi keep W_9.

    """
    zs = r * np.exp(2j * np.pi * np.arange(n) / n)
    vals = [fun(z) for z in zs]
    return [sum(v * z ** (-m) for v, z in zip(vals, zs)) / n for m in range(nmax + 1)]


# ------------------------------------------------------------ data
W = M.dressed_tower(M.VN)
psi = rng.standard_normal(N)
print(f"seed = {ARGS.seed}, N = {N}, dims = {[DIM[k] for k in (2, 3, 4)]}")
pf = 0.7 if ARGS.perturb == "N2-break" else 0.0

# ------------------------------------------------------------ N1
K = 4
H0, off = hessian(0.37, np.zeros(N), K, True, W)
blk = np.zeros_like(H0)
for k in range(2, K + 1):
    s = slice(off[k - 2], off[k - 1])
    blk[s, s] = -2 * 0.37 ** (2 * k - 2) / fact(2 * k) * W[2 * k]
report("N1-psi0-block-diagonal", rel(H0, blk) < TOL, f"rel {rel(H0, blk):.1e}")
H1, _ = hessian(0.37, psi, K, True, W)
s2, s3 = slice(off[0], off[1]), slice(off[1], off[2])
nz = np.max(np.abs(H1[s3, s2])) > 1e-6 and rel(H1[s2, s2], H0[s2, s2]) > 1e-6
report("N1-psi-couplings-nonzero", nz)

# ------------------------------------------------------------ N2
for k in (2, 3, 4):
    others = [l for l in (2, 3, 4) if l != k]
    subsets = [
        c for r_ in range(len(others) + 1) for c in itertools.combinations(others, r_)
    ]
    e0 = max(
        rel(k_eff(g, np.zeros(N), K, True, W, k, E, pf), W[2 * k])
        for E in subsets
        for g in (0.37, 1.3)
    )
    report(f"N2-psi0-k{k}", e0 < TOL, f"max rel over {len(subsets)} sets {e0:.1e}")
    t = 1.7
    es = max(
        rel(
            k_eff(0.4, psi, K, True, W, k, E, pf),
            k_eff(0.4 * t, psi / t, K, True, W, k, E, pf),
        )
        for E in subsets
    )
    report(f"N2-gpsi-k{k}", es < TOL, f"max rel {es:.1e}")
    egs = {
        E: rel(taylor(lambda g: k_eff(g, psi, K, False, W, k, E, pf), 0)[0], W[2 * k])
        for E in subsets
    }
    eg = max(egs.values())
    report(
        f"N2-g0-k{k}",
        eg < 1e-7,
        "rel per set " + ", ".join(f"{E}: {v:.0e}" for E, v in egs.items()),
    )
dn = rel(k_eff(0.4, psi, K, True, W, 2, (3, 4)), W[4])
report("N2-dressing-nonzero", dn > 1e-4, f"rel {dn:.1e}")

# ------------------------------------------------------------ N4
# octic truncation: K = 4, no odd coupling of Sigma_4 (`eq:hs8:dressed-*`).
L3, L4 = Lmap(psi, 3), Lmap(psi, 4)
for k in (2, 3):
    elim = tuple(range(k + 1, 5))
    c = taylor(lambda g: k_eff(g, psi, 4, False, W, k, elim), 2)
    Lk1 = Lmap(psi, k + 1)
    c1 = -odd_op(W, k, psi) / (2 * k + 1)
    c2 = -Lk1.T @ W[2 * k + 2] @ Lk1 / ((2 * k + 1) * (2 * k + 2))
    e = max(rel(c[0], W[2 * k]), rel(c[1], c1), rel(c[2], c2))
    report(f"N4-scaling-k{k}", e < 1e-7, f"max rel {e:.1e}")

g = 0.3
c30 = 31.0 if ARGS.perturb == "N4-break" else 30.0
M3 = W[6] - g / 7 * odd_op(W, 3, psi) - g**2 / 56 * L4.T @ W[8] @ L4
M2 = (
    W[4]
    - g / 5 * odd_op(W, 2, psi)
    - g**2 / c30 * L3.T @ W[6] @ np.linalg.solve(M3, W[6] @ L3)
)
e = max(
    rel(k_eff(g, psi, 4, False, W, 3, (4,)), M3),
    rel(k_eff(g, psi, 4, False, W, 2, (3, 4)), M2),
)
report("N4-nested-octic", e < TOL, f"max rel {e:.1e}")

c3 = taylor(lambda g: k_eff(g, psi, 3, True, W, 2, (3,)), 4)
c4 = taylor(lambda g: k_eff(g, psi, 4, False, W, 2, (3, 4)), 4)
rels = [rel(c3[m], c4[m]) for m in range(5)]
same, diff = max(rels[:4]), rels[4]
report(
    "N4-K-dependence",
    same < 1e-7 and diff > 1e-4,
    "rel per m " + ", ".join(f"{m}: {v:.0e}" for m, v in enumerate(rels)),
)

# ------------------------------------------------------------ N3
target = [0.5 * psi @ M.Q @ psi] + [
    M.vdiag(M.VN[n], psi) / fact(n) for n in range(3, 9)
]


def value(Wd, K=4, odd=False, mmax=6):
    return M.value_series(psi, M.solve_series(psi, K, odd, Wd, mmax), K, odd, Wd, mmax)


v = value(W)
e = max(abs(v[m] - target[m]) for m in range(7))
report("N3-closure-W6-fixed", e < 1e-7, f"max |diff| through g^6 {e:.1e}")

# Veronese-null Delta on Sym^3: symmetric D x D matrix with Delta(Psi^3, Psi^3) = 0.
D3 = DIM[3]
iu = np.triu_indices(D3)
pts = rng.standard_normal((120, N))
rows = []
for p in pts:
    x = M.coords_of_power(p, 3)
    Xo = np.outer(x, x)
    rows.append((Xo + Xo.T - np.diag(np.diag(Xo)))[iu])
_, sv, Vt = np.linalg.svd(np.array(rows))
null = Vt[np.sum(sv > 1e-9 * sv[0]) :]
coef = rng.standard_normal(len(null)) @ null
Delta = np.zeros((D3, D3))
Delta[iu] = coef
Delta = Delta + Delta.T - np.diag(np.diag(Delta))
Delta *= 0.3 / np.max(np.abs(Delta))
xt = M.coords_of_power(rng.standard_normal(N), 3)
print(
    f"  Veronese-null space on Sym^3: dim {len(null)}; Delta(Psi^3,Psi^3) = {xt @ Delta @ xt:.1e}"
)

Wp = {4: W[4], 5: W[5], 6: W[6] + Delta}
for n, Kn, odd in [(7, 3, False), (8, 3, True)]:
    m = n - 2

    def mismatch(p, Kn=Kn, odd=odd, m=m):
        allS = M.solve_series(p, Kn, odd, Wp, m)
        A = M.value_series(p, allS, Kn, odd, Wp, m)[m]
        return M.vdiag(M.VN[n], p) - fact(n) * A

    T = M.fit_polarize(mismatch, n)
    Wp[n] = M.even_form(T, n // 2) if n % 2 == 0 else M.odd_form(T, n // 2)
if ARGS.perturb == "N3-break":
    Wp[7], Wp[8] = W[7], W[8]
vp = value(Wp)
e = max(abs(vp[m] - target[m]) for m in range(7))
dw = rel(Wp[6], W[6])
report(
    "N3-representative",
    e < 1e-7 and dw > 1e-3,
    f"max |diff| {e:.1e}, w33 change rel {dw:.1e}",
)

# ------------------------------------------------------------ break legs
if ARGS.perturb is None:
    print("--- break legs (each must FAIL its target check) ---")
    # N2-break
    e0 = rel(k_eff(0.37, np.zeros(N), 4, True, W, 2, (3,), 0.7), W[4])
    es = rel(
        k_eff(0.4, psi, 4, True, W, 2, (3,), 0.7),
        k_eff(0.68, psi / 1.7, 4, True, W, 2, (3,), 0.7),
    )
    report("N2-break", e0 > 1e-4 and es > 1e-4, f"psi0 rel {e0:.1e}, gpsi rel {es:.1e}")
    M2b = M2 + g**2 * (1 / 30 - 1 / 31) * L3.T @ W[6] @ np.linalg.solve(M3, W[6] @ L3)
    eb = rel(k_eff(g, psi, 4, False, W, 2, (3, 4)), M2b)
    report("N4-break", eb > 1e-4, f"rel {eb:.1e}")
    Wb = dict(Wp)
    Wb[7], Wb[8] = W[7], W[8]
    vb = value(Wb)
    eb = max(abs(vb[m] - target[m]) for m in range(7))
    report("N3-break", eb > 1e-6, f"max |diff| {eb:.1e}")

print(f"summary: {len(failures)} failures" + (f": {failures}" if failures else ""))
sys.exit(len(failures))
