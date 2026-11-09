"""
Companion checks of record 072 (momentum-space auxiliary fields).

Verified here (record ``agent/derivations/072-momentum-space-auxiliaries.md``):
    C1.2-jacobian  Jacobi change of variables k -> (P, q_1..q_{n-1}), eq. (1.3),
                   at n = 2, 3, 4: E^T E = 1, E^T 1 = 0, |det M| = sqrt(n) per
                   spacetime component (so d^{nd}k = n^{-d/2} d^dP prod d^dq,
                   eq. (1.4)), sum_i k_i^2 = P^2/n + sum_j q_j^2 (eq. (1.4));
                   at n = 2, q_1 = -sqrt(2) ell with ell = (k_1 - k_2)/2 of
                   049 A2 and the (P, ell) map has unit Jacobian.
    C1.2-S3        the symmetric group S_3 acts on (q_1, q_2) by
                   D(pi) = E^T Pi(pi) E, eq. (1.5): orthogonal, a homomorphism,
                   transpositions of determinant -1, the two matrices of
                   eq. (1.6), and q(Pi k) = D(pi) q(k) for generic symbolic k
                   (the defining property of D, which uses that P is fixed).
    C4.2-matrix    finite-dimensional stand-in for (4.2)-(4.3): a random positive
                   symmetric matrix K for the action-side kernel, S(sigma) =
                   -g^2/4! s.K.s + 2 g^2/4! s.K.v with v = (t t) stand-in: the
                   stationary point is s = v, the on-shell value is
                   +g^2/4! v.K.v, the eigen-mode decomposition reproduces S, and
                   the Gaussian propagator of a mode is 12/(g^2 mu) (weight e^S).
    C3-toy         one-dimensional toy of eq. (3.1): a configuration
                   sigma(k_1, k_2) = delta(k_1 + k_2) s(ell) has a position-space
                   coefficient depending on x_1 - x_2 only.
Not verified: the level-0 kernel K_P and everything transcribed from R51-R55;
the diagonality claim C2 (a delta-function identity with no machine content);
the sign of K_P^book (a convention, conv. C5); C4.2-matrix tests the algebra of
(4.2)-(4.3) on a stand-in matrix, not the physical kernel. The script uses no
randomness except the seeded matrix of C4.2-matrix (seed printed).
Each check prints PASS/FAIL and is followed by a break leg (a deliberate
perturbation that must FAIL); the script exits nonzero on any FAIL.
"""

from __future__ import annotations

import itertools
import sys

import numpy as np
import sympy as sp

SEED = 20261001
FAILED: list[str] = []


def report(name: str, ok: bool, detail: str = "") -> None:
    """Print one named PASS/FAIL line and record failures."""
    print(f"{'PASS' if ok else 'FAIL'}  {name}  {detail}")
    if not ok:
        FAILED.append(name)


def jacobi_matrix(n: int, normalised: bool = True) -> sp.Matrix:
    """
    Jacobi matrix E (n x (n-1)), columns e_j of record 072 eq. (1.3).

    e_j = sqrt(j/(j+1)) (-1/j, ..., -1/j, 1, 0, ..., 0) with j entries -1/j.
    With ``normalised=False`` the prefactor is dropped (break leg).
    """
    cols = []
    for j in range(1, n):
        pref = sp.sqrt(sp.Rational(j, j + 1)) if normalised else sp.Integer(1)
        col = [-sp.Rational(1, j)] * j + [sp.Integer(1)] + [sp.Integer(0)] * (n - j - 1)
        cols.append(pref * sp.Matrix(col))
    return sp.Matrix.hstack(*cols)


def check_jacobian(n: int, normalised: bool = True) -> bool:
    """E^T E = 1, E^T 1 = 0, |det M| = sqrt(n), and the k^2 identity of (1.4)."""
    e_mat = jacobi_matrix(n, normalised)
    ones = sp.ones(n, 1)
    m_mat = sp.Matrix.vstack(ones.T, e_mat.T)
    ok = sp.simplify(e_mat.T * e_mat - sp.eye(n - 1)) == sp.zeros(n - 1, n - 1)
    ok &= sp.simplify(e_mat.T * ones) == sp.zeros(n - 1, 1)
    ok &= sp.simplify(sp.Abs(m_mat.det()) - sp.sqrt(n)) == 0
    k = sp.Matrix(sp.symbols(f"k1:{n + 1}", real=True))
    pq = m_mat * k
    total = pq[0]
    q = pq[1:, 0]
    ok &= (
        sp.simplify(sum(ki**2 for ki in k) - total**2 / n - sum(qj**2 for qj in q)) == 0
    )
    return bool(ok)


def check_s3(normalised: bool = True) -> tuple[bool, str]:
    """D(pi) = E^T Pi E for S_3: orthogonal, homomorphism, (1.6), P fixed."""
    n = 3
    e_mat = jacobi_matrix(n, normalised)
    perms = [
        sp.combinatorics.Permutation(list(p)) for p in itertools.permutations(range(n))
    ]

    def pi_mat(p: sp.combinatorics.Permutation) -> sp.Matrix:
        mat = sp.zeros(n, n)
        for i in range(n):
            mat[p(i), i] = 1
        return mat

    def d_of(p: sp.combinatorics.Permutation) -> sp.Matrix:
        return sp.simplify(e_mat.T * pi_mat(p) * e_mat)

    ok = True
    detail = []
    for p in perms:
        d = d_of(p)
        ok &= sp.simplify(d.T * d - sp.eye(n - 1)) == sp.zeros(n - 1, n - 1)
        # defining property of D: q(Pi k) = D q(k) for generic symbolic k
        k = sp.Matrix(sp.symbols(f"k1:{n + 1}", real=True))
        ok &= sp.simplify(e_mat.T * pi_mat(p) * k - d * (e_mat.T * k)) == sp.zeros(
            n - 1, 1
        )
    # sympy composes left to right, (p*q)(i) = q(p(i)); with Pi(p) e_i = e_{p(i)}
    # one has Pi(p) Pi(q) = Pi(q*p), hence the homomorphism reads D(q*p) = D(p) D(q).
    for p in perms:
        for p2 in perms:
            ok &= sp.simplify(d_of(p2 * p) - d_of(p) * d_of(p2)) == sp.zeros(
                n - 1, n - 1
            )
    # the explicit matrices of (1.6):
    t12 = sp.combinatorics.Permutation([1, 0, 2])
    t23 = sp.combinatorics.Permutation([0, 2, 1])
    d12 = d_of(t12)
    d23 = d_of(t23)
    exp12 = sp.Matrix([[-1, 0], [0, 1]])
    exp23 = sp.Matrix(
        [[sp.Rational(1, 2), sp.sqrt(3) / 2], [sp.sqrt(3) / 2, -sp.Rational(1, 2)]]
    )
    ok &= sp.simplify(d12 - exp12) == sp.zeros(2, 2)
    ok &= sp.simplify(d23 - exp23) == sp.zeros(2, 2)
    ok &= d12.det() == -1 and d23.det() == -1
    detail.append(f"D((12))={d12.tolist()}, D((23))={d23.tolist()}")
    return bool(ok), "; ".join(detail)


def check_matrix(prop_factor: int = 12) -> bool:
    """
    Finite stand-in for (4.2)-(4.3): S(s) = -g^2/4! s.K.s + 2 g^2/4! s.K.v.

    Checks stationarity at s = v, on-shell value g^2/4! v.K.v, the eigen-mode
    decomposition of S, and the propagator <x^2> = prop_factor/(g^2 mu) of one
    mode with weight e^S (true value prop_factor = 12).
    """
    rng = np.random.default_rng(SEED)
    dim = 5
    a = rng.normal(size=(dim, dim))
    kmat = a @ a.T + dim * np.eye(dim)  # positive definite
    v = rng.normal(size=dim)
    g = 0.7

    def action(s):
        return -(g**2 / 24) * s @ kmat @ s + 2 * (g**2 / 24) * s @ kmat @ v

    s0 = rng.normal(size=dim)

    def fd_grad(s):
        """Central finite-difference gradient of the action (independent of K.s)."""
        h = 1e-5
        return np.array(
            [(action(s + h * e) - action(s - h * e)) / (2 * h) for e in np.eye(dim)]
        )

    # EOM (4.3): stationary at s = v, not at a displaced point (check can fail)
    ok = bool(np.allclose(fd_grad(v), 0, atol=1e-6))
    ok &= bool(np.linalg.norm(fd_grad(s0)) > 1e-3)
    ok &= bool(np.isclose(action(v), (g**2 / 24) * v @ kmat @ v))
    mu, lam = np.linalg.eigh(kmat)
    sh, wh = lam.T @ s0, lam.T @ v
    ok &= bool(
        np.isclose(
            action(s0), np.sum(mu * (-(g**2 / 24) * sh**2 + 2 * (g**2 / 24) * sh * wh))
        )
    )
    # Gaussian propagator of one mode, exact: int x^2 e^{-A x^2} / int e^{-A x^2}
    x = sp.symbols("x", real=True)
    cap = sp.symbols("A", positive=True)
    var = sp.integrate(x**2 * sp.exp(-cap * x**2), (x, -sp.oo, sp.oo)) / sp.integrate(
        sp.exp(-cap * x**2), (x, -sp.oo, sp.oo)
    )
    gs, ms = sp.symbols("g mu", positive=True)
    var_mode = sp.simplify(var.subs(cap, gs**2 * ms / 24))
    ok &= sp.simplify(var_mode - sp.Rational(prop_factor) / (gs**2 * ms)) == 0
    return ok


def check_toy(delta_sign: int = 1) -> bool:
    """1D toy: sigma = delta(k1 + delta_sign*k2) s((k1-k2)/2) -> depends on x1-x2 only."""
    k1, k2, x1, x2, a = sp.symbols("k1 k2 x1 x2 a", real=True)
    s = sp.Function("s")
    integrand = (
        sp.DiracDelta(k1 + delta_sign * k2)
        * sp.exp(sp.I * (k1 * x1 + k2 * x2))
        * s((k1 - k2) / 2)
    )
    inner = sp.integrate(integrand, (k2, -sp.oo, sp.oo))
    # translation invariance: shift both coordinates by a
    shifted = inner.subs({x1: x1 + a, x2: x2 + a}, simultaneous=True)
    return sp.simplify(shifted - inner) == 0


def main() -> int:
    """Run every named check and its break leg; return 1 on any FAIL."""
    print(f"seed {SEED} (used by C4.2-matrix only)")
    for n in (2, 3, 4):
        report(f"C1.2-jacobian n={n}", check_jacobian(n))
    report(
        "C1.2-jacobian-break (unnormalised Jacobi vectors must FAIL)",
        not check_jacobian(3, normalised=False),
    )
    # n = 2: q_1 = -sqrt(2) ell and unit Jacobian of (P, ell)
    k1, k2 = sp.symbols("k1 k2", real=True)
    e2 = jacobi_matrix(2)
    q1 = (e2.T * sp.Matrix([k1, k2]))[0]
    ell = (k1 - k2) / 2
    m_pl = sp.Matrix([[1, 1], [sp.Rational(1, 2), -sp.Rational(1, 2)]])
    report(
        "C1.2-jacobian n=2 ell",
        sp.simplify(q1 + sp.sqrt(2) * ell) == 0 and sp.Abs(m_pl.det()) == 1,
    )
    ok, detail = check_s3()
    report("C1.2-S3", ok, detail)
    ok_b, _ = check_s3(normalised=False)
    report("C1.2-S3-break (non-orthonormal frame must FAIL)", not ok_b)
    report("C4.2-matrix", check_matrix())
    report("C4.2-matrix-break (propagator 4!/(g^2 mu) must FAIL)", not check_matrix(24))
    report("C3-toy", check_toy(+1))
    report("C3-toy-break (delta(k1-k2) must FAIL)", not check_toy(-1))
    n_fail = len(FAILED)
    print(f"summary: {n_fail} FAIL" + (f" ({', '.join(FAILED)})" if FAILED else ""))
    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(main())
