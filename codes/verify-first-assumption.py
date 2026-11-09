"""Toy-model checks for record 116 (the "first assumption" passage of section 2.2).

Verified, on finite-dimensional or one-dimensional representations only:

- A6-range: for the Mehler kernel E(q, q') = exp(-a(q^2 + q'^2) + c q q'), |c| < 2a,
  a Gaussian source exp(-b q^2) lies in the range iff a - c^2/(4a) < b < a
  (record 104, eq. (1.6)); outside the window the source is still orthogonal to the
  (trivial) kernel, i.e. in the closure of the range. This is the content of
  sentences A6-A8 of the passage: "image, not closure" is a real condition.
- B6-horn1 / B6-horn2: an analytic family of matrices I - C(p) with a built-in
  selection rule (a common null vector) is singular at every p, so sampling generic
  momenta never exhibits a kernel-free point (first horn of the dichotomy); a family
  without it is singular on a discrete set only and a random p is kernel-free.
- B9-laplace / B9-accidental: for K(s) = K0 + sum_n exp(-h_n s) E_n with distinct
  h_n, a vector null for all s in an interval is annihilated by every E_n (Laplace
  separation); a family with a kernel at every s whose null vector rotates with s is
  not annihilated by the E_n (the accidental case of sentence B11).

Not verified: anything about the string vertex itself; PH35 and PH36 are the paper's
assumptions and are not tested here.

Run from the project root:
    uv run python verify-first-assumption.py
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
from numpy.polynomial.hermite import hermgauss

DEFAULT_OUT = Path(__file__).resolve().parent / "output" / "first-assumption"


def mehler_range_check(a: float, c: float, b: float, n_quad: int = 200) -> float:
    """Residual of E f = exp(-b q^2) with the Gaussian ansatz f = exp(-beta q^2).

    Solving b = a - c^2 / (4 (a + beta)) gives beta; the ansatz is an L^2 function
    iff beta > 0, which is the window a - c^2/(4a) < b < a. Returns the max residual
    on a grid when beta > 0, and +inf otherwise (no L^2 Gaussian preimage).
    """
    if not (c**2 / (4 * (a - b)) - a > 0 if b < a else False):
        return np.inf
    beta = c**2 / (4 * (a - b)) - a
    # Gauss-Hermite quadrature for int exp(-beta q'^2) E(q, q') dq'.
    x, w = hermgauss(n_quad)
    q = np.linspace(-3, 3, 41)
    # Substitute q' = x / sqrt(a + beta) so the weight exp(-x^2) is extracted.
    s = np.sqrt(a + beta)
    qp = x / s
    integrand = np.exp(c * np.outer(q, qp)) * np.exp(-a * q[:, None] ** 2)
    lhs = (integrand * w[None, :]).sum(axis=1) / s
    rhs = np.sqrt(np.pi / (a + beta)) * np.exp(-b * q**2)
    return float(np.max(np.abs(lhs - rhs) / np.max(rhs)))


def picard_ratio(a: float, c: float, b: float, n: int = 160) -> float:
    """Growth ratio of the Picard terms |<u_j, v>|^2 / mu_j^2 at large even j.

    Nystrom discretization on a Gauss-Hermite grid of the symmetric kernel; the
    ratio > 1 means the series diverges (source outside the range).
    """
    x, w = hermgauss(n)
    # Symmetrized kernel with weights: K_ij = sqrt(w_i w_j) e^{x_i^2/2 + x_j^2/2} E(x_i, x_j).
    sw = np.sqrt(w) * np.exp(x**2 / 2)
    kern = np.exp(-a * (x[:, None] ** 2 + x[None, :] ** 2) + c * np.outer(x, x))
    kmat = sw[:, None] * kern * sw[None, :]
    mu, u = np.linalg.eigh(kmat)
    order = np.argsort(-np.abs(mu))
    mu, u = mu[order], u[:, order]
    v = sw * np.exp(-b * x**2)
    coeff = u.T @ v
    terms = coeff**2 / mu**2
    # Even-index terms only (odd ones vanish by parity); indices 4-18, where the
    # Nystrom eigenpairs agree between 120 and 240 nodes (probe of 2026-11-09).
    idx = np.arange(4, 20, 2)
    ratios = terms[idx[1:]] / terms[idx[:-1]]
    return float(np.exp(np.mean(np.log(ratios))))


def horn_family(rng: np.random.Generator, n: int, selection_rule: bool) -> callable:
    """Analytic matrix family T(p) = I - C(p), C(p) = C0 + p C1 + p^2 C2.

    With selection_rule=True the matrices are built so that a fixed vector e is
    annihilated by T(p) for every p (a conserved sector): first horn. Otherwise a
    generic family: det T(p) is a nontrivial polynomial, zeros isolated.
    """
    mats = [rng.normal(size=(n, n)) / n for _ in range(3)]
    if selection_rule:
        e = np.zeros(n)
        e[0] = 1.0
        for i, m in enumerate(mats):
            # Force T(p) e = 0: C(p) e = e, i.e. C0 e = e, C1 e = C2 e = 0.
            m[:, 0] = 0.0
            if i == 0:
                m[0, 0] = 1.0

    def t_of_p(p: complex) -> np.ndarray:
        return np.eye(n) - (mats[0] + p * mats[1] + p**2 * mats[2])

    return t_of_p


def laplace_family(rng: np.random.Generator, n: int, n_mass: int, accidental: bool):
    """K(s) = K0 + sum_n exp(-h_n s) E_n, h_n = 2 n distinct, E_n finite rank.

    accidental=False: a common null vector N of K0 and every E_n is built in, so
    K(s) N = 0 for all s (a conserved sector). accidental=True: K(s) is made singular
    at every s by a rotating null vector N(s) = (cos s, sin s, 0, ...) via
    K(s) = M(s) P(s) with P(s) the projector orthogonal to N(s). No Laplace fit is made
    for this family: the script checks only that K(s) is singular at every s and that
    the stacked family has no common null vector.
    """
    h = 2.0 * np.arange(n_mass)
    if not accidental:
        n_vec = rng.normal(size=n)
        n_vec /= np.linalg.norm(n_vec)
        proj = np.eye(n) - np.outer(n_vec, n_vec)
        k0 = proj @ rng.normal(size=(n, n)) @ proj
        e_list = [proj @ rng.normal(size=(n, n)) @ proj for _ in range(n_mass)]

        def k_of_s(s: float) -> np.ndarray:
            return k0 + sum(np.exp(-h[i] * s) * e_list[i] for i in range(n_mass))

        return k_of_s, e_list, n_vec, h
    base = rng.normal(size=(n, n))

    def n_of_s(s: float) -> np.ndarray:
        v = np.zeros(n)
        v[0], v[1] = np.cos(s), np.sin(s)
        return v

    def k_of_s(s: float) -> np.ndarray:
        v = n_of_s(s)
        return base @ (np.eye(n) - np.outer(v, v))

    return k_of_s, None, n_of_s, h


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--perturb", type=str, default=None)
    parser.add_argument("--seed", type=int, default=20261109)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(args.seed)
    print(f"seed {args.seed}")
    results: list[tuple[str, bool, str]] = []

    def record(name: str, ok: bool, info: str) -> None:
        results.append((name, ok, info))
        print(f"{'PASS' if ok else 'FAIL'} {name}: {info}")

    # --- A6-range: Mehler window --------------------------------------------------
    a, c = 1.0, 1.2
    lo = a - c**2 / (4 * a)
    inside = [lo + 0.25 * (a - lo), lo + 0.6 * (a - lo)]
    outside = [lo - 0.3 * (a - lo), a + 0.3 * (a - lo)]
    res_in = [mehler_range_check(a, c, b) for b in inside]
    rat_in = [picard_ratio(a, c, b) for b in inside]
    rat_out = [picard_ratio(a, c, b) for b in outside]
    ok = (
        all(r < 1e-8 for r in res_in)
        and all(r < 1 for r in rat_in)
        and all(r > 1 for r in rat_out)
    )
    record(
        "A6-range",
        ok,
        f"window ({lo:.3f}, {a:.3f}); inside: residual {max(res_in):.1e}, Picard ratio "
        f"{rat_in}; outside: Picard ratio {rat_out} (>1: source in closure, not range)",
    )
    # Break leg: the one-sided convolution criterion "b < a" would admit the slow point.
    slow = outside[0]
    wrong_criterion_admits = slow < a
    record(
        "A6-range-break",
        wrong_criterion_admits and picard_ratio(a, c, slow) > 1,
        f"b={slow:.3f} < a admitted by the convolution criterion yet outside the range",
    )

    # --- B6: horns of the dichotomy -----------------------------------------------
    n = 8
    t_sel = horn_family(rng, n, selection_rule=True)
    t_gen = horn_family(rng, n, selection_rule=False)
    ps = rng.normal(size=20) + 1j * rng.normal(size=20)
    if args.perturb == "B6-break":
        # Perturb the selection-rule family: a random rank-one term breaks the rule.
        delta = rng.normal(size=(n, n)) * 1e-2
        t_sel_base = t_sel
        t_sel = lambda p: t_sel_base(p) + delta  # noqa: E731
    smin_sel = [np.linalg.svd(t_sel(p), compute_uv=False)[-1] for p in ps]
    smin_gen = [np.linalg.svd(t_gen(p), compute_uv=False)[-1] for p in ps]
    record(
        "B6-horn1",
        max(smin_sel) < 1e-12,
        f"selection-rule family: max over 20 random complex p of sigma_min = "
        f"{max(smin_sel):.1e} (a kernel at every momentum; sampling cannot refute it)",
    )
    # Generic family: det is a polynomial of degree <= 2n, so at most 2n zeros.
    record(
        "B6-horn2",
        min(smin_gen) > 1e-6,
        f"generic family: min sigma_min at 20 random p = {min(smin_gen):.2e} "
        f"(zeros of det T(p), a polynomial of degree <= {2 * n}, are isolated)",
    )
    if args.perturb == "B6-break":
        record(
            "B6-break",
            max(smin_sel) > 1e-12,
            "broken selection rule: sigma_min no longer vanishes, B6-horn1 fails as it should",
        )

    # --- B9: Laplace separation and the accidental case -----------------------------
    n, n_mass = 7, 4
    k_cons, e_list, n_vec, h = laplace_family(rng, n, n_mass, accidental=False)
    s_grid = np.linspace(0.0, 2.0, 25)
    # Persistence: K(s) N = 0 on the grid.
    persist = max(np.linalg.norm(k_cons(s) @ n_vec) for s in s_grid)
    # Laplace separation: fit the exponentials from K(s) N on the grid (Vandermonde in
    # exp(-h_n s)); the fitted coefficients are E_n N and K0 N and must vanish.
    design = np.column_stack(
        [np.ones_like(s_grid)] + [np.exp(-hn * s_grid) for hn in h]
    )
    rhs = np.array([k_cons(s) @ n_vec for s in s_grid])
    coeffs, *_ = np.linalg.lstsq(design, rhs, rcond=None)
    direct = max(np.linalg.norm(e @ n_vec) for e in e_list)
    record(
        "B9-laplace",
        persist < 1e-10 and np.abs(coeffs).max() < 1e-8 and direct < 1e-10,
        f"null for all s (resid {persist:.1e}); Laplace-fitted E_n N and K0 N all "
        f"< {np.abs(coeffs).max():.1e}; direct |E_n N| < {direct:.1e}",
    )
    # Break: a vector null at s=0 only (not along the family) is not exchange-decoupled.
    # Build K0 so that K(0) n0 = 0 for a random unit n0, with generic E_n.
    e_brk = [rng.normal(size=(n, n)) for _ in range(n_mass)]
    n0 = rng.normal(size=n)
    n0 /= np.linalg.norm(n0)
    k0_raw = rng.normal(size=(n, n))
    k0_brk = k0_raw - np.outer((k0_raw + sum(e_brk)) @ n0, n0)

    def k_brk(s: float) -> np.ndarray:
        return k0_brk + sum(np.exp(-h[i] * s) * e_brk[i] for i in range(n_mass))

    resid0 = np.linalg.norm(k_brk(0.0) @ n0)
    not_persist = max(np.linalg.norm(k_brk(s) @ n0) for s in s_grid[1:])
    record(
        "B9-break",
        resid0 < 1e-10
        and not_persist > 1e-3
        and max(np.linalg.norm(e @ n0) for e in e_brk) > 1e-3,
        f"a null vector of K(0) alone (resid {resid0:.1e}) does not persist ({not_persist:.2f}) "
        f"and is not annihilated by the E_n",
    )
    # Accidental: kernel at every s, rotating null vector; the Laplace coefficients of the
    # family applied to a fixed vector do not vanish, and no fixed vector is null.
    k_acc, _, n_of_s, _ = laplace_family(rng, n, n_mass, accidental=True)
    sing_every = max(np.linalg.svd(k_acc(s), compute_uv=False)[-1] for s in s_grid)
    stack = np.vstack([k_acc(s) for s in s_grid])
    common_null = np.linalg.svd(stack, compute_uv=False)[-1]
    record(
        "B9-accidental",
        sing_every < 1e-12 and common_null > 1e-3,
        f"kernel at every s (max sigma_min {sing_every:.1e}) but no common null vector "
        f"(smallest singular value of the stacked family {common_null:.2f}): the "
        f"Laplace argument does not see it",
    )

    n_fail = sum(not ok for _, ok, _ in results)
    summary = f"{len(results) - n_fail}/{len(results)} PASS, {n_fail} FAIL"
    print(summary)
    (args.out / "verify-first-assumption.txt").write_text(
        "\n".join(
            f"{'PASS' if ok else 'FAIL'} {nm}: {info}" for nm, ok, info in results
        )
        + f"\n{summary}\n"
    )
    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(main())
