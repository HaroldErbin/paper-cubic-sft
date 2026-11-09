"""Companion checks for derivation record 105 (the six-point Sigma_2 exchange at real momenta).

What is verified (each check named after the claim-tree node it tests, with two
exceptions noted after record 105's last review: C2-hoelder and C2-hoelder-break test
the Cauchy-Schwarz step of C3.3, and C3.5-expconvex runs on the slab model and is
evidence for C5 only, not for the theorem C3.5 about the actual exchange; C5-multiple
tests only the disjoint case b < tau, the overlap clause b > tau of C5 is derived,
not checked):

- C2-bmodes (bookkeeping, critic #23: it transcribes the anticommutators and b_n|0> = 0
  that eq. (2.1) uses, so it can fail only through a mis-built representation; the
  substantive steps of C2, the n >= -1 restriction of the Schiffer vectors and the
  cancellation of f_i'(0), are not machine-checked): in a finite fermionic Fock representation of the ghost modes
  {b_{-1}, b_0, b_1, c_{-1}, c_0, c_1} and their antiholomorphic copies, the tachyon
  state c_1 cbar_1 |0> is annihilated by b_n, bbar_n for n = 0, 1 and mapped by b_{-1}
  to cbar_1 |0> (up to sign); the result does not use the on-shell condition, which
  is the step behind C2 and C2' (only the translation modes of the Schiffer vectors
  survive on a tachyon). Break leg: the state c_0 c_1 |0> is not annihilated by b_0.
- C2-hoelder (bookkeeping: Cauchy-Schwarz on random positive input, an identity valid for
  any input; not evidence for C3.3): the Laplace transform F(x) = sum_k w_k exp(<l_k, x>) of a random
  positive measure on R^2 satisfies the midpoint inequality F((x+y)/2)^2 <= F(x) F(y)
  at seeded random pairs (Hoelder / Cauchy-Schwarz, the T3 step), and the Hankel
  matrices [F((x_a+x_b)/2)] are positive semi-definite (the T3+ step).
- C2-hoelder-break: the signed measure delta_0 - (1/2) delta_1, whose transform
  1 - e^{x}/2 has concave logarithm on x < ln 2, violates the midpoint inequality
  at a printed triple (the check can fail).
- C3.5-crossratio-fibre: with (z_1, z_2, z_3) = (0, 1, infinity), the nine absolute
  cross-ratios |z_j|, |1 - z_j| (j = 4, 5, 6), |z_45|, |z_46|, |z_56| determine
  (z_4, z_5, z_6) up to the global conjugation: the reconstruction from the nine
  numbers returns exactly the two conjugate points at seeded random configurations.
- C5-single, C5-multiple, C5-generic, C5-generic-wide, C5-break, C3.5-expconvex:
  the fixed-halves slab model of R80 C4 with cutoff tau and slab widths (a, b);
  composite neck measure mu_C(S) = sum_{n>=1} d/dS (1_{[-a,0]} * 1_{[-b,0]})(S - n tau),
  Laplace transform (convention of codes/verify-circle-gluing-inverse.py: a slab [-x,0]
  has f_x(h) = (e^{x h} - 1)/h, the tower gives h/(e^{tau h} - 1))
  mu_hat(h) = f_a(h) f_b(h) h / (e^{tau h} - 1), on the convergence half-line h > 0.
  Single slab (a = tau): closed form against quadrature of the truncated tower, log-convexity
  on a grid, Hankel PSD, T4 exponents (b as h -> +inf, 0 as h -> -inf on the continuation);
  the growth exponents are read after removing the 1/h prefactor; the ratio mu_hat / f_b = 1 is printed as bookkeeping and excluded from the exit code.
  Compact support (a = k tau): exact identity mu_hat = f_b sum_{j<k} e^{j tau h} (sympy),
  pointwise positivity of the telescoped measure evaluated in floating point on a grid (the
  identity itself is exact in sympy), log-convexity and Hankel PSD
  (the verdict the record derives before the run: PASS).
  Generic (a, b, tau) = (1/2, 1/2, 3/4): (log mu_hat)''(0+) = (a^2 + b^2 - tau^2)/12 exactly
  (sympy series), negative here, so the midpoint inequality fails at printed small h;
  the Hankel matrix has a negative eigenvalue at printed points; the pole of the closed form
  at h = 2 pi i / tau is reported as a property (numerator non-zero there), not as the reason.
  Generic wide (0.7, 0.7, 0.75), a^2 + b^2 > tau^2: exploratory scan of (log mu_hat)'' on
  h in (0, 40] and a Hankel search; printed, excluded from the exit code.
  Break: in the single-slab case the sign of the n = 1 term of the telescoping sum is flipped
  (mu -> mu - 2 T_1), the transform f_b (2 e^{-tau h} - 1) has a real zero, and the midpoint
  inequality on |mu_hat| must FAIL at a printed triple.

What is not verified: anything about the actual vertices (C1, C1.1, C3.2', C4, C6 are
arguments, definitions or hypotheses); C3.1 (T1), C3.2 (T2), C3.4 (T4) and C3.5 (iii)
(the converse with the symmetrised density), which are arguments; the exponential-convexity
theorem itself (cited); the record's hypotheses H-C1, H-C2, H-C2' (i)-(iii), H-C4, H-C5.
"""

from __future__ import annotations

import sys
from itertools import product
from pathlib import Path

import numpy as np
import sympy as sp

SEED = 20261018
rng = np.random.default_rng(SEED)
RESULTS: list[tuple[str, bool, bool]] = []  # name, ok, counts_for_exit


def report(name: str, ok: bool, info: str = "", counts: bool = True) -> None:
    tag = "PASS" if ok else "FAIL"
    if not counts:
        tag += " (informative)"
    print(f"[{tag}] {name}: {info}")
    RESULTS.append((name, ok, counts))


# ---------------------------------------------------------------------------
# C2-bmodes: ghost zero modes on the tachyon state
# ---------------------------------------------------------------------------
def fock_ops(n_modes: int) -> list[np.ndarray]:
    """Jordan-Wigner annihilation operators for n_modes fermionic modes."""
    a1 = np.array([[0.0, 1.0], [0.0, 0.0]])  # annihilation on (|0>, |1>)
    par = np.diag([1.0, -1.0])
    eye2 = np.eye(2)
    ops = []
    for k in range(n_modes):
        mats = [par] * k + [a1] + [eye2] * (n_modes - k - 1)
        m = mats[0]
        for x in mats[1:]:
            m = np.kron(m, x)
        ops.append(m)
    return ops


def check_c2_bmodes() -> None:
    # modes: 0: (b_{-1}, c_1), 1: (b_0, c_0), 2: (b_1, c_{-1}); 3-5 the antiholomorphic copies.
    # Creator c_{1-k} = annihilator-dagger of mode k; b_{k-1} = annihilator of mode k:
    # {b_m, c_n} = delta_{m+n,0}, and b_n |0> = 0 for n >= -1, c_n |0> = 0 for n >= 2.
    ann = fock_ops(6)
    b = {-1: ann[0], 0: ann[1], 1: ann[2]}
    c = {1: ann[0].T, 0: ann[1].T, -1: ann[2].T}
    bb = {-1: ann[3], 0: ann[4], 1: ann[5]}
    cb = {1: ann[3].T, 0: ann[4].T, -1: ann[5].T}
    dim = 2**6
    vac = np.zeros(dim)
    vac[0] = 1.0
    tach = c[1] @ cb[1] @ vac
    ok = True
    info = []
    for n in (0, 1):
        for name, op in (("b", b[n]), ("bbar", bb[n])):
            v = op @ tach
            ok &= np.allclose(v, 0)
            info.append(f"{name}_{n} T = 0: {np.allclose(v, 0)}")
    v = b[-1] @ tach
    target = cb[1] @ vac
    rel = abs(abs(v @ target) - 1.0) < 1e-12 and np.allclose(
        v - (v @ target) * target, 0
    )
    ok &= rel
    info.append(f"b_-1 T = +-cbar_1|0>: {rel}")
    v = bb[-1] @ tach
    target = c[1] @ vac
    rel = abs(abs(v @ target) - 1.0) < 1e-12 and np.allclose(
        v - (v @ target) * target, 0
    )
    ok &= rel
    info.append(f"bbar_-1 T = +-c_1|0>: {rel}")
    # anticommutators as a transcription check
    for m in (-1, 0, 1):
        for n in (-1, 0, 1):
            ac = b[m] @ c[n] + c[n] @ b[m]
            ok &= np.allclose(ac, np.eye(dim) if m + n == 0 else 0)
    report("C2-bmodes", ok, "(bookkeeping) " + "; ".join(info))
    # break leg: c_0 c_1 |0> (ghost-number-3 state) is not annihilated by b_0
    st = c[0] @ c[1] @ vac
    broken = not np.allclose(b[0] @ st, 0)
    report("C2-bmodes-break", broken, "b_0 (c_0 c_1|0>) != 0: %s" % broken)


# ---------------------------------------------------------------------------
# C2-hoelder: Laplace transform of a positive measure is log-convex / exponentially convex
# ---------------------------------------------------------------------------
def check_c2_hoelder() -> None:
    n_atoms = 12
    locs = rng.normal(size=(n_atoms, 2))
    wts = rng.uniform(0.1, 2.0, size=n_atoms)

    def F(x: np.ndarray) -> float:
        return float(np.sum(wts * np.exp(locs @ x)))

    ok = True
    worst = -np.inf
    for _ in range(200):
        x, y = rng.normal(scale=1.5, size=2), rng.normal(scale=1.5, size=2)
        m = 0.5 * (x + y)
        gap = np.log(F(x)) + np.log(F(y)) - 2 * np.log(F(m))
        worst = max(worst, -gap)
        ok &= gap >= -1e-12
    # Hankel matrices
    min_eig = np.inf
    for _ in range(50):
        pts = rng.normal(scale=1.5, size=(4, 2))
        H = np.array([[F(0.5 * (pts[i] + pts[j])) for j in range(4)] for i in range(4)])
        ev = np.linalg.eigvalsh(H)
        min_eig = min(min_eig, ev[0] / ev[-1])
        ok &= ev[0] >= -1e-10 * ev[-1]
    report(
        "C2-hoelder",
        ok,
        f"(bookkeeping) 200 midpoint triples, worst violation {worst:.2e} (<= 0 means none); "
        f"50 Hankel 4x4, min relative eigenvalue {min_eig:.2e}",
    )
    # break leg: delta_0 - (1/2) delta_1, F(x) = 1 - e^x / 2 on x < ln 2
    Fb = lambda x: 1.0 - 0.5 * np.exp(x)  # noqa: E731
    x, y = -1.0, 0.5
    m = 0.5 * (x + y)
    gap = np.log(Fb(x)) + np.log(Fb(y)) - 2 * np.log(Fb(m))
    report(
        "C2-hoelder-break",
        gap < 0,
        f"delta_0 - delta_1/2 at (x, y) = ({x}, {y}): log F(x) + log F(y) - 2 log F(m) = {gap:.4f} < 0",
    )


# ---------------------------------------------------------------------------
# C3.5-crossratio-fibre
# ---------------------------------------------------------------------------
def circle_pts(r1: float, r2: float) -> list[complex]:
    """Intersections of |z| = r1 and |z - 1| = r2."""
    x = (1.0 + r1**2 - r2**2) / 2.0
    y2 = r1**2 - x**2
    if y2 < -1e-12:
        return []
    y = np.sqrt(max(y2, 0.0))
    return [complex(x, y), complex(x, -y)]


def check_c35_fibre() -> None:
    ok = True
    counts = []
    for _ in range(100):
        z = rng.normal(size=3) + 1j * rng.normal(size=3)
        if min(abs(z.imag)) < 0.05:
            continue
        data = {
            "r": [(abs(zj), abs(1 - zj)) for zj in z],
            "d": {(i, j): abs(z[i] - z[j]) for i in range(3) for j in range(i + 1, 3)},
        }
        cands = [circle_pts(*data["r"][j]) for j in range(3)]
        sols = []
        for choice in product(*cands):
            if all(
                abs(abs(choice[i] - choice[j]) - data["d"][(i, j)]) < 1e-8
                for (i, j) in data["d"]
            ):
                sols.append(choice)
        counts.append(len(sols))
        good = len(sols) == 2 and all(
            (np.allclose(s, z) or np.allclose(s, np.conj(z))) for s in sols
        )
        ok &= good
    report(
        "C3.5-crossratio-fibre",
        ok,
        f"{len(counts)} seeded configurations, fibre sizes {sorted(set(counts))} (expected {{2}}: z and zbar)",
    )


# ---------------------------------------------------------------------------
# C5: the slab model of R80 C4 (conventions of codes/verify-circle-gluing-inverse.py)
# ---------------------------------------------------------------------------
H = sp.symbols("h")


def f_slab(x, h=H):
    """Laplace transform of the slab 1_{[-x,0]}: int_{-x}^0 e^{-hS} dS = (e^{xh}-1)/h."""
    return (sp.exp(x * h) - 1) / h


def mu_hat_expr(a, b, tau):
    """Closed form of the composite's transform, h/(e^{tau h}-1) the tower sum_{n>=1} h e^{-n tau h}."""
    return f_slab(a) * f_slab(b) * H / (sp.exp(tau * H) - 1)


def tower_term(
    a: float, b: float, tau: float, n: int, S: np.ndarray, sign: float = 1.0
) -> np.ndarray:
    """n-th term of mu_C: d/dS(1_{[-a,0]} * 1_{[-b,0]})(S - n tau) = 1_{[ntau-a-b, ntau-a]} - 1_{[ntau-b, ntau]}."""
    t = S - n * tau
    return sign * (
        ((t >= -a - b) & (t < -a)).astype(float) - ((t >= -b) & (t < 0)).astype(float)
    )


def mu_measure(
    a: float, b: float, tau: float, S: np.ndarray, nmax: int, flip: int | None = None
) -> np.ndarray:
    out = np.zeros_like(S)
    for n in range(1, nmax + 1):
        out += tower_term(a, b, tau, n, S, sign=-1.0 if n == flip else 1.0)
    return out


def laplace_quadrature(
    a: float, b: float, tau: float, h: float, nmax: int, flip: int | None = None
) -> float:
    """Transform of the truncated tower measure by exact integration of piecewise constants."""
    # breakpoints
    pts = {0.0}
    for n in range(1, nmax + 1):
        for p in (n * tau - a - b, n * tau - a, n * tau - b, n * tau):
            pts.add(p)
    pts = sorted(pts)
    total = 0.0
    for lo, hi in zip(pts[:-1], pts[1:]):
        mid = np.array([0.5 * (lo + hi)])
        val = mu_measure(a, b, tau, mid, nmax, flip)[0]
        if val != 0.0:
            total += val * (np.exp(-h * lo) - np.exp(-h * hi)) / h
    return total


def logconvex_gap(F, x: float, y: float) -> float:
    """log F(x) + log F(y) - 2 log F((x+y)/2); >= 0 for a log-convex F."""
    return float(np.log(F(x)) + np.log(F(y)) - 2.0 * np.log(F(0.5 * (x + y))))


def hankel_min_eig(F, pts: np.ndarray) -> float:
    M = np.array([[F(0.5 * (p + q)) for q in pts] for p in pts])
    ev = np.linalg.eigvalsh(M)
    return float(ev[0] / max(abs(ev[-1]), 1e-300))


def second_log_derivative(expr, hval: float) -> float:
    d2 = sp.diff(sp.log(expr), H, 2)
    return float(d2.subs(H, sp.Float(hval, 30)).evalf(30))


def check_c5_single() -> None:
    a = tau = sp.Rational(3, 4)
    b = sp.Rational(1, 2)
    expr = mu_hat_expr(a, b, tau)
    Fn = sp.lambdify(H, expr, "numpy")
    F = lambda h: float(Fn(h))  # noqa: E731
    af, bf, tf = float(a), float(b), float(tau)
    # closed form against quadrature of the truncated tower (converges for h > 0)
    ok = True
    errs = []
    for h in (0.3, 1.1, 2.7):
        q = laplace_quadrature(af, bf, tf, h, nmax=120)
        errs.append(abs(q - F(h)) / abs(F(h)))
    ok &= max(errs) < 1e-10
    # log-convexity on a grid of triples in (0, 30], and Hankel PSD
    worst = -np.inf
    for _ in range(300):
        x, y = rng.uniform(0.05, 30.0, size=2)
        worst = max(worst, -logconvex_gap(F, x, y))
    ok &= worst <= 1e-12
    min_eig = min(
        hankel_min_eig(F, np.sort(rng.uniform(0.05, 20.0, size=4))) for _ in range(100)
    )
    ok &= min_eig >= -1e-10
    # T4: exponents b (h -> +inf) and 0 (h -> -inf, continuation) against the support [-b, 0]
    # the 1/h prefactor of a slab's transform is removed before reading the exponent
    slope_plus = (np.log(60.0 * F(60.0)) - np.log(50.0 * F(50.0))) / 10.0
    slope_minus = (np.log(60.0 * abs(F(-60.0))) - np.log(50.0 * abs(F(-50.0)))) / (
        -10.0
    )
    ok &= abs(slope_plus - bf) < 1e-9 and abs(slope_minus - 0.0) < 1e-9
    report(
        "C5-single",
        ok,
        f"closed form vs quadrature rel. err {max(errs):.1e}; worst log-convexity violation {worst:.1e}; "
        f"min Hankel rel. eigenvalue {min_eig:.1e}; T4 exponents {slope_plus:.4f} (expected b = {bf}), "
        f"{slope_minus:.4f} (expected 0)",
    )
    # bookkeeping: the ratio to the other width's slab is 1 (restates the closed form)
    ratio = sp.simplify(expr / f_slab(b))
    report(
        "C5-single-ratio",
        ratio == 1,
        f"mu_hat / f_b = {ratio} (bookkeeping)",
        counts=False,
    )


def check_c5_multiple() -> None:
    k = 3
    tau = sp.Rational(3, 4)
    a = k * tau
    b = sp.Rational(1, 2)
    expr = mu_hat_expr(a, b, tau)
    target = f_slab(b) * sum(sp.exp(j * tau * H) for j in range(k))
    exact = sp.simplify(sp.expand(expr - target).rewrite(sp.exp)) == 0
    # numerical confirmation of the identity at generic complex points
    pts = [0.7 + 0.3j, 1.3 - 0.4j, 0.2 + 0.9j]
    num = max(abs(complex(expr.subs(H, p)) - complex(target.subs(H, p))) for p in pts)
    # pointwise positivity of the measure on a fine grid (exact telescoping to k shifted slabs)
    S = np.linspace(-float(a + b) - 1, 40.0, 20001)
    mu = mu_measure(float(a), float(b), float(tau), S, nmax=120)
    pos = bool(np.all(mu >= -1e-12))
    expected = sum(
        ((S >= -float(b) - j * float(tau)) & (S < -j * float(tau))).astype(float)
        for j in range(k)
    )
    matches = bool(np.all(np.abs(mu - expected) < 1e-12))
    Fn = sp.lambdify(H, expr, "numpy")
    F = lambda h: float(Fn(h))  # noqa: E731
    worst = max(-logconvex_gap(F, *rng.uniform(0.05, 30.0, size=2)) for _ in range(300))
    min_eig = min(
        hankel_min_eig(F, np.sort(rng.uniform(0.05, 20.0, size=4))) for _ in range(100)
    )
    ok = (
        exact
        and num < 1e-12
        and pos
        and matches
        and worst <= 1e-12
        and min_eig >= -1e-10
    )
    report(
        "C5-multiple",
        ok,
        f"a = {k} tau: identity mu_hat = f_b sum_j e^(j tau h) exact {exact} (num {num:.1e}); measure >= 0: {pos}, "
        f"equals the {k} shifted slabs: {matches}; worst log-convexity violation {worst:.1e}; "
        f"min Hankel rel. eigenvalue {min_eig:.1e} (derived verdict: PASS)",
    )


def check_c5_generic() -> None:
    a, b, tau = sp.Rational(1, 2), sp.Rational(1, 2), sp.Rational(3, 4)
    expr = mu_hat_expr(a, b, tau)
    # (log mu_hat)''(0+) = (a^2 + b^2 - tau^2)/12, exact by series
    d2 = sp.series(sp.diff(sp.log(expr), H, 2), H, 0, 1).removeO()
    d2_0 = sp.simplify(d2)
    formula = (a**2 + b**2 - tau**2) / 12
    exact = sp.simplify(d2_0 - formula) == 0
    # symbolic version with free widths
    A, B, T = sp.symbols("a b tau", positive=True)
    e_sym = f_slab(A) * f_slab(B) * H / (sp.exp(T * H) - 1)
    d2_sym = sp.simplify(sp.series(sp.diff(sp.log(e_sym), H, 2), H, 0, 1).removeO())
    exact_sym = sp.simplify(d2_sym - (A**2 + B**2 - T**2) / 12) == 0
    Fn = sp.lambdify(H, expr, "numpy")
    F = lambda h: float(Fn(h))  # noqa: E731
    # failure of the midpoint inequality at small h
    triples = [(0.05, 0.45), (0.1, 0.6), (0.2, 0.8)]
    gaps = [(x, y, logconvex_gap(F, x, y)) for x, y in triples]
    fails = [g for g in gaps if g[2] < 0]
    # Hankel failure
    pts = np.array([0.05, 0.25, 0.45, 0.65])
    me = hankel_min_eig(F, pts)
    # the pole at h = 2 pi i / tau: numerator non-zero, denominator zero (a property, not the reason)
    h0 = 2 * sp.pi * sp.I / tau
    numer = complex((f_slab(a) * f_slab(b) * H).subs(H, h0))
    denom = complex((sp.exp(tau * H) - 1).subs(H, h0))
    pole = abs(numer) > 1e-12 and abs(denom) < 1e-12
    ok = (
        exact
        and exact_sym
        and float(formula) < 0
        and len(fails) == len(triples)
        and me < -1e-8
        and pole
    )
    report(
        "C5-generic",
        ok,
        f"(a,b,tau) = (1/2,1/2,3/4): (log mu_hat)''(0+) = {d2_0} = (a^2+b^2-tau^2)/12 exact {exact} "
        f"(free widths: {exact_sym}); midpoint gaps at (x,y) = "
        + ", ".join(f"({x},{y}): {g:.3e}" for x, y, g in gaps)
        + f" (all < 0: {len(fails) == len(triples)}); Hankel min rel. eigenvalue at {pts.tolist()}: {me:.3e}; "
        f"pole at 2 pi i / tau (numerator {abs(numer):.3f}, denominator {abs(denom):.1e}): {pole}",
    )


def check_c5_generic_wide() -> None:
    """Exploratory: a^2 + b^2 > tau^2, where the small-h criterion does not fire."""
    a, b, tau = sp.Rational(7, 10), sp.Rational(7, 10), sp.Rational(3, 4)
    expr = mu_hat_expr(a, b, tau)
    Fn = sp.lambdify(H, expr, "numpy")
    F = lambda h: float(Fn(h))  # noqa: E731
    d2f = sp.lambdify(H, sp.diff(sp.log(expr), H, 2), "mpmath")
    grid = np.linspace(0.02, 40.0, 2000)
    d2 = np.array([float(d2f(float(h))) for h in grid])
    neg = grid[d2 < 0]
    # Hankel search on (0, 20]
    best = np.inf
    best_pts = None
    for _ in range(400):
        pts = np.sort(rng.uniform(0.02, 20.0, size=4))
        me = hankel_min_eig(F, pts)
        if me < best:
            best, best_pts = me, pts
    report(
        "C5-generic-wide",
        best < -1e-10,
        f"(a,b,tau) = (0.7,0.7,0.75), a^2+b^2-tau^2 = {float(a**2 + b**2 - tau**2):.4f} > 0: (log mu_hat)'' < 0 on "
        f"{'no grid point' if len(neg) == 0 else f'h in [{neg.min():.3f}, {neg.max():.3f}]'} of (0, 40]; "
        f"Hankel 4x4 search min rel. eigenvalue {best:.3e} at {None if best_pts is None else np.round(best_pts, 3).tolist()} "
        f"(exploratory; T3+ failure exists by uniqueness of the representing measure, record §5)",
        counts=False,
    )


def check_c5_break() -> None:
    """Single-slab case with the sign of the n = 1 tower term flipped: convexity must FAIL."""
    a = tau = sp.Rational(3, 4)
    b = sp.Rational(1, 2)
    af, bf, tf = float(a), float(b), float(tau)
    # closed form: mu - 2 T_1 with T_1 = 1_{[-b,0]} - 1_{[tau-b,tau]}  ->  f_b (2 e^{-tau h} - 1)
    expr = f_slab(b) * (2 * sp.exp(-tau * H) - 1)
    Fn = sp.lambdify(H, expr, "numpy")
    F = lambda h: abs(float(Fn(h)))  # noqa: E731
    # transcription: the flipped measure's quadrature agrees with the closed form
    err = max(
        abs(laplace_quadrature(af, bf, tf, h, 120, flip=1) - float(Fn(h)))
        / abs(float(Fn(h)))
        for h in (0.3, 1.1, 2.7)
    )
    h0 = np.log(2.0) / tf  # real zero of the transform
    x, y = h0 + 0.05, h0 + 0.45
    gap = logconvex_gap(F, x, y)
    report(
        "C5-break",
        err < 1e-10 and gap < 0,
        f"n = 1 term flipped: transform f_b (2 e^(-tau h) - 1), quadrature rel. err {err:.1e}, real zero at h = {h0:.4f}; "
        f"midpoint gap of log|mu_hat| at ({x:.3f}, {y:.3f}) = {gap:.3f} < 0 (convexity FAILS, as it must)",
    )


def check_c35_expconvex() -> None:
    """T3+ Hankel 3x3 and 4x4 on the three slab cases, points and midpoints in h > 0."""
    cases = {
        "single (a = tau)": (
            sp.Rational(3, 4),
            sp.Rational(1, 2),
            sp.Rational(3, 4),
            True,
        ),
        "compact (a = 3 tau)": (
            sp.Rational(9, 4),
            sp.Rational(1, 2),
            sp.Rational(3, 4),
            True,
        ),
        "generic (1/2, 1/2, 3/4)": (
            sp.Rational(1, 2),
            sp.Rational(1, 2),
            sp.Rational(3, 4),
            False,
        ),
    }
    ok_all = True
    infos = []
    for name, (a, b, tau, expect_psd) in cases.items():
        Fn = sp.lambdify(H, mu_hat_expr(a, b, tau), "numpy")
        F = lambda h, Fn=Fn: float(Fn(h))  # noqa: E731
        worst = np.inf
        worst_pts = None
        for size in (3, 4):
            for _ in range(150):
                pts = np.sort(rng.uniform(0.02, 15.0, size=size))
                me = hankel_min_eig(F, pts)
                if me < worst:
                    worst, worst_pts = me, pts
        # also the deterministic small-h set for the generic case
        me_small = hankel_min_eig(F, np.array([0.05, 0.25, 0.45, 0.65]))
        worst = min(worst, me_small)
        verdict = worst >= -1e-10
        ok_all &= verdict == expect_psd
        infos.append(
            f"{name}: min rel. eigenvalue {worst:.2e} at {np.round(worst_pts, 3).tolist()} -> {'PSD' if verdict else 'not PSD'} (expected {'PSD' if expect_psd else 'not PSD'})"
        )
    report("C3.5-expconvex", ok_all, "; ".join(infos))


def main() -> int:
    print(f"seed = {SEED}")
    check_c2_bmodes()
    check_c2_hoelder()
    check_c35_fibre()
    check_c5_single()
    check_c5_multiple()
    check_c5_generic()
    check_c5_generic_wide()
    check_c5_break()
    check_c35_expconvex()
    n_pass = sum(1 for _, ok, c in RESULTS if ok and c)
    n_fail = sum(1 for _, ok, c in RESULTS if (not ok) and c)
    n_info = sum(1 for _, _, c in RESULTS if not c)
    print(
        f"summary: {n_pass} PASS, {n_fail} FAIL, {n_info} informative (excluded from exit code)"
    )
    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(main())
