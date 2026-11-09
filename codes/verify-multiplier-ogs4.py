#!/usr/bin/env python3
r"""
verify-multiplier-ogs4.py — record 068: the multiplier remedy on ker V4 at O(g_s^4).

Finite model (record 068 A1–A5): U = Q^n, S = Sym^2 U in the basis E_aa, E_ab + E_ba
(no inner product used), V4 symmetric on S with dim ker V4 = r, V5 on S x S x U
symmetric in the S slots and violating R38 (V5(Xi, ., .) != 0), V6 symmetric trilinear
on S, all exact rationals.  Reduced action S~ := S_4 / g^2,

    S~(Sigma) = -V4(Sigma,Sigma)/24 + V4(Sigma,P)/12 + g V5(Sigma,Sigma,Psi)/120
                + g^2 W6(Sigma,Sigma,Sigma)/720,       P = Psi (x) Psi,

    S~_eff   = V4(P,P)/24 + g V5(P,P,Psi)/120 + g^2 V6(P,P,P)/720   (013/R19, C4).

The multiplier pair on the kernel (034 (3.1)) restricts Sigma to the affine slice
P + C, C = ker mu a complement of N = ker V4 (mu: S -> N, mu|_N = id).  The saddle over
C is computed as an exact truncated power series in g (fixed-point iteration, one order
per step), so every Taylor coefficient of the eliminated action F_*^{(C)}(Psi) is exact.
Index k of a reduced series is the absolute order g^{k+2}.

Checks (named after the claim-tree nodes of record 068; each has a break leg that must
FAIL, printed as <name>-break with PASS meaning "the break was detected"):
  C1     the full (Sigma, lambda) stationarity system is solved by the restricted saddle:
         the Sigma-EOM residual with lambda = -Xi^T grad (1.3) vanishes to all orders.
         The constraint half mu(Sigma - P) = 0 holds by construction (Sigma = P + B y,
         B = ker mu) and the restricted saddle itself is the assert inside `eliminate`,
         so C1 tests the lambda formula (1.3); break: Sigma = P is not a solution at O(g).
  C1-lambda  lambda_* = -(g/60) v_N + O(g^2) (no g^0 term; nonzero iff v_N != 0).
  C2     g^2, g^3 coefficients of F_* - S_eff vanish in every complement (R38's remedy);
         break: without the multiplier (linear slice Sigma in C) the g^3 coefficient is
         -(1/120)[V5(P,P,Psi) - V5(pi_C P, pi_C P, Psi)], 034 (1.4), nonzero.
  C3.1   G_C = B (B^T V4 B)^{-1} B^T is the symmetric reflexive generalised inverse with
         image C and kernel the annihilator C^0 = row(mu);
         <w, G_{C_L} w'> = (w_C0 + L^T w_N)^T (V4^{C0C0})^{-1} (w'_C0 + L^T w'_N).
  C3.2   with W6 = V6 the g^4 coefficient of F_* - S_eff is (1/600) <v, G_C v>.
  C3.3   that coefficient differs between two complements, is quadratic in L, and is
         L-independent once V5 is replaced by an R38-satisfying V5.
  C3.4   with W6 = V6 - (6/5) C^{(C)} the g^4 coefficient vanishes in every complement
         (two random ones, a one-parameter family); breaks: theta = 1, theta = 0,
         the composite of another complement, the Moore-Penrose composite, and no
         multiplier (g^3 fails).
  C3.5   under R38 the full composite tensor C^{(C)} is complement-independent; break:
         with the R38-violating V5 it is not.
  C3.6   <v, (G_C - G_{C'}) v> != 0 at sampled Psi: no single W6 serves both complements
         *with the constraint undeformed and V5(Sigma,Sigma,Psi) the only O(g^3) coupling*.
  C3.6-relax        the weakest relaxation (critic-068 #1): add g^3 <lambda, Z(Sigma,Psi)>,
         Z linear in Sigma with values in N, so the lambda-EOM is mu(Sigma-P) + g Z = 0
         (solved exactly: Sigma = R(g)(P + B y), R = 1 - g Xi (1 + g M Xi)^{-1} M, Z = M Sigma).
         With Z_L = (1/10) L A_a (2 B_a + Xi L)^T V5(., Sigma, Psi) the fixed vertex
         W6^{(C_a)} gives g^2..g^4 coefficients zero in C_L, C_2L and C_b (L_b = -mu_b B_a).
  C3.6-relax-shift  for a random Z (random M): g^2, g^3 coefficients unchanged and the g^4
         coefficient shifted by exactly -(1/60) v_N^T Z(P, Psi), nonzero.
  C3.6-relax-break  the same complements with W6^{(C_a)} and Z = 0: g^4 coefficient nonzero.
  C4     the g^5 coefficient with W6^{(C)} equals 013's A5 with V4^{-1} -> G_C; break:
         the factor 1/2 replaced by 1.
  C5-*   the same at corank 2.
  C3.4-r0  r = 0 limit (ker V4 = 0, C = S): G_C = V4^{-1} and W6 = V6 - (6/5) C[V4^{-1}]
         (R19's vertex verbatim) gives g^2..g^4 zero; break: V6 alone leaves <v,V4^{-1}v>/600.

C1, C3.1, C3.3, C3.5, C3.6 are identity/inequality checks on G_C, lambda and the
constraint; C2, C3.2, C3.4, C3.6-relax, C4 compare exact Taylor coefficients of the
eliminated action against independently written formulas.  The new legs (C1-lambda,
C3.6-relax-*, C3.4-r0) draw from separate seeded generators, so the data of the
original 42 checks are unchanged.

Not verified: anything outside the finite model (the string vertices, PH1/PH14, R13
regularity), the gauge law of the hybrid action, orders beyond g^5.

Usage: ``.venv/bin/python codes/verify-multiplier-ogs4.py``; exit code = #failures.
"""

from __future__ import annotations

import itertools
import random
import sys
import time
from collections.abc import Callable
from fractions import Fraction as Fr

import numpy as np
import sympy as sp

SEED = 20261001
ORDER = 3  # reduced order: keep g^0..g^3 of S~, i.e. absolute O(g^5)
failures: list[str] = []
t0 = time.time()


def report(name: str, ok: bool, detail: str = "") -> None:
    print(
        f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""),
        flush=True,
    )
    if not ok:
        failures.append(name)


# ------------------------------------------------------------ exact arrays
def zeros(shape: tuple[int, ...]) -> np.ndarray:
    return np.full(shape, Fr(0), dtype=object)


def rand_arr(shape: tuple[int, ...], rng: random.Random) -> np.ndarray:
    a = zeros(shape)
    for idx in itertools.product(*[range(s) for s in shape]):
        a[idx] = Fr(rng.randint(-9, 9), rng.randint(1, 4))
    return a


def to_sp(a: np.ndarray) -> sp.Matrix:
    return sp.Matrix(
        a.shape[0],
        a.shape[1],
        [sp.Rational(x.numerator, x.denominator) for x in a.flat],
    )


def from_sp(m: sp.Matrix) -> np.ndarray:
    a = zeros((m.rows, m.cols))
    for i in range(m.rows):
        for j in range(m.cols):
            q = sp.Rational(m[i, j])
            a[i, j] = Fr(int(q.p), int(q.q))
    return a


def inv(a: np.ndarray) -> np.ndarray:
    return from_sp(to_sp(a).inv())


def nullspace(a: np.ndarray) -> np.ndarray:
    cols = to_sp(a).nullspace()
    return from_sp(sp.Matrix.hstack(*cols))


def rank(a: np.ndarray) -> int:
    return to_sp(a).rank()


def is_zero(a: np.ndarray) -> bool:
    return all(x == 0 for x in np.asarray(a, dtype=object).flat)


# ------------------------------------------------------------ truncated series
Series = list  # list of ORDER+1 object arrays of a common shape


def s_const(x: np.ndarray) -> Series:
    return [np.array(x, dtype=object)] + [zeros(np.shape(x)) for _ in range(ORDER)]


def s_zero(shape: tuple[int, ...]) -> Series:
    return [zeros(shape) for _ in range(ORDER + 1)]


def s_add(*ss: Series) -> Series:
    return [sum(s[k] for s in ss) for k in range(ORDER + 1)]


def s_scale(s: Series, c: Fr) -> Series:
    return [c * x for x in s]


def s_shift(s: Series, k: int) -> Series:
    return [zeros(np.shape(s[0])) for _ in range(k)] + s[: ORDER + 1 - k]


def s_lin(f: Callable, s: Series) -> Series:
    return [f(x) for x in s]


def s_bil(f: Callable, a: Series, b: Series) -> Series:
    shape = np.shape(f(a[0], b[0]))
    out = [zeros(shape) for _ in range(ORDER + 1)]
    for i in range(ORDER + 1):
        for j in range(ORDER + 1 - i):
            out[i + j] = out[i + j] + f(a[i], b[j])
    return out


def s_tri(f: Callable, a: Series, b: Series, c: Series) -> Series:
    shape = np.shape(f(a[0], b[0], c[0]))
    out = [zeros(shape) for _ in range(ORDER + 1)]
    for i in range(ORDER + 1):
        for j in range(ORDER + 1 - i):
            for k in range(ORDER + 1 - i - j):
                out[i + j + k] = out[i + j + k] + f(a[i], b[j], c[k])
    return out


def s_matvec(R: Series, x: Series, transpose: bool = False) -> Series:
    """Convolution of a matrix series with a vector series: (R x)_k = sum_i R_i x_{k-i}."""
    shape = np.shape(x[0])
    out = [zeros(shape) for _ in range(ORDER + 1)]
    for i in range(ORDER + 1):
        Ri = R[i].T if transpose else R[i]
        for j in range(ORDER + 1 - i):
            out[i + j] = out[i + j] + Ri @ x[j]
    return out


def s_is_zero(s: Series, upto: int = ORDER) -> bool:
    return all(is_zero(x) for x in s[: upto + 1])


# ------------------------------------------------------------ model
def sym_basis(n: int) -> list[np.ndarray]:
    """Basis matrices Lambda_K^{ef} of Sym^2 U: E_aa, then E_ab + E_ba (a < b)."""
    lam = []
    for a in range(n):
        E = zeros((n, n))
        E[a, a] = Fr(1)
        lam.append(E)
    for a in range(n):
        for b in range(a + 1, n):
            E = zeros((n, n))
            E[a, b] = Fr(1)
            E[b, a] = Fr(1)
            lam.append(E)
    return lam


def identity(D: int) -> np.ndarray:
    """Exact D x D identity (Fraction entries)."""
    out = zeros((D, D))
    for i in range(D):
        out[i, i] = Fr(1)
    return out


class Model:
    """V4 (D,D) with kernel span(Xi), V5 (D,D,n) sym in (I,J), V6 (D,D,D) sym, basis Lam."""

    def __init__(self, n: int, r: int, rng: random.Random) -> None:
        self.n, self.r = n, r
        D = n * (n + 1) // 2
        self.D = D
        self.Lam = sym_basis(n)  # basis matrices Lambda_K^{ef}
        # kernel basis and a reference complement
        while True:
            Xi = rand_arr((D, r), rng)
            if rank(Xi) == r:
                break
        self.Xi = Xi
        self.mu0 = self.random_mu(rng)
        Q = (
            np.identity(D, dtype=object) * Fr(1) - Xi @ self.mu0
        )  # projector on C0 along N
        Bsym = rand_arr((D, D), rng)
        Bsym = Bsym + Bsym.T
        self.V4 = Q.T @ Bsym @ Q
        assert rank(self.V4) == D - r and is_zero(self.V4 @ Xi)
        ker = nullspace(self.V4)
        assert rank(np.concatenate([ker, Xi], axis=1)) == r, "ker V4 != span Xi"
        V5 = rand_arr((D, D, n), rng)
        self.V5 = (V5 + V5.transpose(1, 0, 2)) * Fr(1, 2)
        V6 = rand_arr((D, D, D), rng)
        self.V6 = sum(V6.transpose(p) for p in itertools.permutations(range(3))) * Fr(
            1, 6
        )
        # R38-satisfying variant of V5: project both S slots onto C0 along N
        V5p = zeros((D, D, n))
        for e in range(n):
            V5p[:, :, e] = Q.T @ self.V5[:, :, e] @ Q
        self.V5_R38 = V5p
        assert all(is_zero(Xi.T @ V5p[:, :, e]) for e in range(n))
        assert not all(is_zero(Xi.T @ self.V5[:, :, e]) for e in range(n)), (
            "V5 must violate R38"
        )

    def random_mu(self, rng: random.Random) -> np.ndarray:
        while True:
            M = rand_arr((self.r, self.D), rng)
            if rank(M @ self.Xi) == self.r:
                return inv(M @ self.Xi) @ M

    # ----- coordinates
    def pvec(self, psi: np.ndarray) -> np.ndarray:
        """Coordinates of P = psi (x) psi in the basis Lam: P_aa = psi_a^2, P_ab = psi_a psi_b."""
        n = self.n
        out = [psi[a] * psi[a] for a in range(n)]
        out += [psi[a] * psi[b] for a in range(n) for b in range(a + 1, n)]
        return np.array(out, dtype=object)

    def W(self, psi: np.ndarray) -> np.ndarray:
        """W_Psi[I,J] = V5[I,J,e] psi_e."""
        return sum(self.V5[:, :, e] * psi[e] for e in range(self.n))

    # ----- multilinear contractions (object arrays: use @ and tensordot only)
    @staticmethod
    def bil(M: np.ndarray, a: np.ndarray, b: np.ndarray):
        return a @ M @ b

    @staticmethod
    def tri(T: np.ndarray, a: np.ndarray, b: np.ndarray, c: np.ndarray):
        return np.tensordot(np.tensordot(T, c, axes=([2], [0])), b, axes=([1], [0])) @ a

    @staticmethod
    def tri_vec(T: np.ndarray, b: np.ndarray, c: np.ndarray) -> np.ndarray:
        """T(., b, c) as a covector."""
        return np.tensordot(np.tensordot(T, c, axes=([2], [0])), b, axes=([1], [0]))

    def composite(self, G: np.ndarray, V5: np.ndarray | None = None) -> np.ndarray:
        """R19's Sigma-channel composite with V4^{-1} -> G:
        C[I,J,K] = sym_{IJK} sum_{ef} Lam_K^{ef} V5[M,I,e] G[M,M'] V5[M',J,f]."""
        V5 = self.V5 if V5 is None else V5
        D, n = self.D, self.n
        raw = zeros((D, D, D))
        GV = [G @ V5[:, :, f] for f in range(n)]  # (D,D): [M', J] -> [M, J]
        for K in range(D):
            LK = self.Lam[K]
            acc = zeros((D, D))
            for e in range(n):
                for f in range(n):
                    if LK[e, f] != 0:
                        acc = acc + LK[e, f] * (V5[:, :, e].T @ GV[f])
            raw[:, :, K] = acc
        return sum(raw.transpose(p) for p in itertools.permutations(range(3))) * Fr(
            1, 6
        )


def G_of(m: Model, B: np.ndarray) -> np.ndarray:
    """Symmetric reflexive generalised inverse with image C = col(B), kernel C^0."""
    return B @ inv(B.T @ m.V4 @ B) @ B.T


# ------------------------------------------------------------ elimination
def eliminate(
    m: Model,
    psi: np.ndarray,
    B: np.ndarray,
    T: np.ndarray,
    affine: bool = True,
    R: Series | None = None,
):
    """Saddle of S~ over Sigma = R(g)(shift + B y) (shift = P if affine else 0), exact series.

    R = None is R = 1 (the undeformed slice).  A matrix series R with Xi^T V4 = 0 on the
    left of its g-corrections (R_k = Xi (...) for k >= 1) parametrises the deformed
    constraint surface of C3.6-relax; then V4 R = V4, R^T V4 = V4, and the tangent
    directions are the columns of R(g) B.

    Returns (Sigma_* series, F_* series, grad series) with grad = dS~/dSigma at Sigma_*.
    """
    P = m.pvec(psi)
    W = m.W(psi)
    V4 = m.V4
    Bt = B.T
    A = inv(Bt @ V4 @ B)
    shift = P if affine else zeros((m.D,))
    Rs = R if R is not None else s_const(identity(m.D))

    def embed(y: Series) -> Series:
        return s_matvec(Rs, s_add(s_const(shift), s_lin(lambda v: B @ v, y)))

    def project(cov: Series) -> Series:  # (R B)^T cov
        return s_lin(lambda v: Bt @ v, s_matvec(Rs, cov, transpose=True))

    m_ = B.shape[1]
    y = s_zero((m_,))
    lin_src = s_const(Fr(1, 12) * (V4 @ (P - shift)))
    for _ in range(ORDER + 2):
        sig = embed(y)
        rhs = s_add(
            lin_src,
            s_shift(s_lin(lambda v: Fr(1, 60) * (W @ v), sig), 1),
            s_shift(
                s_lin(
                    lambda v: Fr(1, 240) * v,
                    s_bil(lambda a, b: m.tri_vec(T, a, b), sig, sig),
                ),
                2,
            ),
        )
        y = s_lin(lambda v: 12 * (A @ v), project(rhs))
    sig = embed(y)
    grad = s_add(
        s_lin(lambda v: Fr(-1, 12) * (V4 @ v), sig),
        s_const(Fr(1, 12) * (V4 @ P)),
        s_shift(s_lin(lambda v: Fr(1, 60) * (W @ v), sig), 1),
        s_shift(
            s_lin(
                lambda v: Fr(1, 240) * v,
                s_bil(lambda a, b: m.tri_vec(T, a, b), sig, sig),
            ),
            2,
        ),
    )
    assert s_is_zero(project(grad)), "restricted saddle not converged"
    F = s_add(
        s_scale(s_bil(lambda a, b: m.bil(V4, a, b), sig, sig), Fr(-1, 24)),
        s_lin(lambda v: Fr(1, 12) * m.bil(V4, v, P), sig),
        s_shift(s_scale(s_bil(lambda a, b: m.bil(W, a, b), sig, sig), Fr(1, 120)), 1),
        s_shift(
            s_scale(
                s_tri(lambda a, b, c: m.tri(T, a, b, c), sig, sig, sig), Fr(1, 720)
            ),
            2,
        ),
    )
    return sig, F, grad


def seff(m: Model, psi: np.ndarray) -> Series:
    P = m.pvec(psi)
    s = s_zero(())
    s[0] = np.array(Fr(1, 24) * m.bil(m.V4, P, P), dtype=object)
    s[1] = np.array(Fr(1, 120) * m.bil(m.W(psi), P, P), dtype=object)
    s[2] = np.array(Fr(1, 720) * m.tri(m.V6, P, P, P), dtype=object)
    return s


def mismatch(
    m: Model,
    psi: np.ndarray,
    B: np.ndarray,
    T: np.ndarray,
    affine: bool = True,
    R: Series | None = None,
) -> Series:
    _, F, _ = eliminate(m, psi, B, T, affine, R)
    return s_add(F, s_scale(seff(m, psi), Fr(-1)))


def coef(s: Series, k: int) -> Fr:
    return Fr(np.asarray(s[k], dtype=object).item())


# ------------------------------------------------------------ main
def run(n: int, r: int, tag: str, rng: random.Random) -> None:
    m = Model(n, r, rng)
    D = m.D
    print(f"--- model {tag}: n={n}, D={D}, corank r={r}")
    mu_a, mu_b = m.random_mu(rng), m.random_mu(rng)
    B_a, B_b = nullspace(mu_a), nullspace(mu_b)
    G_a, G_b = G_of(m, B_a), G_of(m, B_b)
    psis = [rand_arr((n,), rng) for _ in range(2)]
    W6_a = m.V6 - Fr(6, 5) * m.composite(G_a)
    W6_b = m.V6 - Fr(6, 5) * m.composite(G_b)
    pre = f"{tag}" if tag else ""

    # ---- C1: full multiplier system solved by the restricted saddle
    ok, ok_break, ok_lam = True, True, True
    for psi in psis:
        for mu, B in ((mu_a, B_a), (mu_b, B_b)):
            sig, F, grad = eliminate(m, psi, B, W6_a)
            lam = s_lin(lambda v: -(m.Xi.T @ v), grad)
            resid = s_add(grad, s_lin(lambda v: mu.T @ v, lam))
            cons = s_add(s_lin(lambda v: mu @ v, sig), s_const(-(mu @ m.pvec(psi))))
            ok &= s_is_zero(resid) and s_is_zero(cons)
            # (critic-068 #13) lambda_* = -(g/60) v_N + O(g^2): series index k = order g^k
            vN = m.Xi.T @ (m.W(psi) @ m.pvec(psi))
            ok_lam &= (
                is_zero(lam[0]) and is_zero(lam[1] + Fr(1, 60) * vN) and not is_zero(vN)
            )
            # break: Sigma = P (no O(g) correction) is not stationary on C at O(g)
            P = m.pvec(psi)
            gradP = Fr(1, 60) * (B.T @ (m.W(psi) @ P))
            ok_break &= not is_zero(gradP)
    report(
        f"{pre}C1",
        ok,
        "Sigma-EOM residual zero to all orders with lambda of (1.3) (constraint holds by construction)",
    )
    report(f"{pre}C1-break", ok_break, "Sigma = P fails the restricted EOM at O(g)")
    report(
        f"{pre}C1-lambda",
        ok_lam,
        "lambda_* = -(g/60) v_N + O(g^2), no g^0 term, v_N != 0",
    )

    # ---- C2: O(g^3) reproduction, and 034 (1.4) without the multiplier
    ok, ok_break = True, True
    for psi in psis:
        P = m.pvec(psi)
        for mu, B in ((mu_a, B_a), (mu_b, B_b)):
            d = mismatch(m, psi, B, m.V6)
            ok &= coef(d, 0) == 0 and coef(d, 1) == 0
            d_lin = mismatch(m, psi, B, m.V6, affine=False)
            piC_P = P - m.Xi @ (mu @ P)
            pred = -Fr(1, 120) * (m.bil(m.W(psi), P, P) - m.bil(m.W(psi), piC_P, piC_P))
            ok_break &= coef(d_lin, 0) == 0 and coef(d_lin, 1) == pred and pred != 0
    report(
        f"{pre}C2", ok, "g^2, g^3 coefficients of F_* - S_eff vanish, both complements"
    )
    report(
        f"{pre}C2-break", ok_break, "linear slice: g^3 mismatch = 034 (1.4), nonzero"
    )

    # ---- C3.1: G_C properties and the L-formula
    ok = True
    for G, mu in ((G_a, mu_a), (G_b, mu_b)):
        ok &= (
            is_zero(m.V4 @ G @ m.V4 - m.V4)
            and is_zero(G @ m.V4 @ G - G)
            and is_zero(mu @ G)
        )
        # (critic-068 #5) symmetric, kernel = C^0 = row(mu) (rank D - r fixes the dimension)
        ok &= is_zero(G - G.T) and is_zero(G @ mu.T) and rank(G) == D - r
    L = rand_arr((r, D - r), rng)
    B_L = B_a + m.Xi @ L
    G_L = G_of(m, B_L)
    A0 = inv(B_a.T @ m.V4 @ B_a)
    w, w2 = rand_arr((D,), rng), rand_arr((D,), rng)
    lhs = w @ G_L @ w2
    rhs = (B_a.T @ w + L.T @ (m.Xi.T @ w)) @ A0 @ (B_a.T @ w2 + L.T @ (m.Xi.T @ w2))
    ok &= lhs == rhs
    ok_break = (w @ G_a @ w2) != rhs  # the L = 0 inverse differs from the L-formula
    report(
        f"{pre}C3.1",
        ok,
        "V4 G V4 = V4, G V4 G = G, im G = C, G = G^T, ker G = C^0; <w,G_L w'> = L-formula",
    )
    report(f"{pre}C3.1-break", ok_break, "G_{C_0} != G_{C_L} on generic covectors")

    # ---- C3.2: undressed g^4 coefficient = (1/600) <v, G_C v>
    ok, ok_break = True, True
    for psi in psis:
        P = m.pvec(psi)
        v = m.W(psi) @ P
        for G, B in ((G_a, B_a), (G_b, B_b)):
            d = mismatch(m, psi, B, m.V6)
            ok &= coef(d, 2) == Fr(1, 600) * (v @ G @ v)
            ok_break &= coef(d, 2) != Fr(1, 720) * (v @ G @ v)
    report(f"{pre}C3.2", ok, "g^4 coefficient with W6 = V6 equals <v,G_C v>/600")
    report(f"{pre}C3.2-break", ok_break, "…and not <v,G_C v>/720")

    # ---- C3.3: complement dependence; quadratic in L; constant under R38
    ok = True
    psi = psis[0]
    P = m.pvec(psi)
    v = m.W(psi) @ P
    ok &= (v @ G_a @ v) != (v @ G_b @ v)
    vals = []
    for t in range(4):
        Bt = B_a + m.Xi @ (t * L)
        vals.append(v @ G_of(m, Bt) @ v)
    third = vals[3] - 3 * vals[2] + 3 * vals[1] - vals[0]
    second = vals[2] - 2 * vals[1] + vals[0]
    ok &= third == 0 and second != 0
    # R38-satisfying V5: v_N = 0, so <v, G_C v> is complement-independent
    vR = sum(m.V5_R38[:, :, e] * psi[e] for e in range(n)) @ P
    ok &= is_zero(m.Xi.T @ vR) and (vR @ G_a @ vR) == (vR @ G_b @ vR) == (vR @ G_L @ vR)
    report(
        f"{pre}C3.3",
        ok,
        "<v,G_C v> differs between complements, quadratic in L, constant iff v_N = 0",
    )
    report(
        f"{pre}C3.3-break", not is_zero(m.Xi.T @ v), "the R38-violating v has v_N != 0"
    )

    # ---- C3.4: absorption by W6^{(C)}; breaks
    ok = True
    for psi in psis:
        for B, W6 in ((B_a, W6_a), (B_b, W6_b)):
            d = mismatch(m, psi, B, W6)
            ok &= coef(d, 0) == 0 and coef(d, 1) == 0 and coef(d, 2) == 0
        for t in (1, 2, 5):
            Bt = B_a + m.Xi @ (t * L)
            W6_t = m.V6 - Fr(6, 5) * m.composite(G_of(m, Bt))
            d = mismatch(m, psi, Bt, W6_t)
            ok &= coef(d, 0) == 0 and coef(d, 1) == 0 and coef(d, 2) == 0
    report(
        f"{pre}C3.4",
        ok,
        "g^2..g^4 coefficients vanish with W6^{(C)} in C_a, C_b and the family C_{tL}",
    )
    psi = psis[0]
    d = mismatch(m, psi, B_a, m.V6 - Fr(1) * m.composite(G_a))
    report(f"{pre}C3.4-break-theta", coef(d, 2) != 0, "theta = 1 leaves a g^4 mismatch")
    d = mismatch(m, psi, B_a, m.V6)
    report(f"{pre}C3.4-break-V6alone", coef(d, 2) != 0, "V6 alone leaves <v,G_C v>/600")
    d = mismatch(m, psi, B_a, W6_b)
    report(
        f"{pre}C3.4-break-otherC",
        coef(d, 2) != 0,
        "composite of C_b in complement C_a fails",
    )
    B_perp = nullspace(m.Xi.T)  # coordinate-orthogonal complement: Moore-Penrose
    G_mp = G_of(m, B_perp)
    d = mismatch(m, psi, B_a, m.V6 - Fr(6, 5) * m.composite(G_mp))
    report(
        f"{pre}C3.4-break-MoorePenrose",
        coef(d, 2) != 0,
        "pinv composite in a non-orthogonal complement fails",
    )
    d = mismatch(m, psi, B_a, W6_a, affine=False)
    report(
        f"{pre}C3.4-break-nomultiplier",
        coef(d, 1) != 0,
        "without the multiplier the g^3 order fails even with W6^{(C)}",
    )

    # ---- C3.5: under R38 the composite tensor is complement-independent
    Ca, Cb, CL = (m.composite(G, m.V5_R38) for G in (G_a, G_b, G_L))
    report(
        f"{pre}C3.5",
        is_zero(Ca - Cb) and is_zero(Ca - CL),
        "C^{(C)} tensor equal for C_a, C_b, C_L under R38",
    )
    report(
        f"{pre}C3.5-break",
        not is_zero(m.composite(G_a) - m.composite(G_b)),
        "…and differs for the R38-violating V5",
    )

    # ---- C3.6: no complement-independent W6
    ok = all(
        (m.W(p) @ m.pvec(p)) @ (G_a - G_b) @ (m.W(p) @ m.pvec(p)) != 0 for p in psis
    )
    report(
        f"{pre}C3.6",
        ok,
        "<v,(G_a - G_b) v> != 0 at both Psi: W6(P^3) would need two values",
    )

    # ---- C4: g^5 residual = 013's A5 with G_C
    ok, ok_break = True, True
    for psi in psis:
        P = m.pvec(psi)
        W = m.W(psi)
        v = W @ P
        for B, G, W6 in ((B_a, G_a, W6_a), (B_b, G_b, W6_b)):
            d = mismatch(m, psi, B, W6)
            Gv = G @ v
            A5 = Fr(1, 600) * (
                Fr(1, 2) * m.tri(W6, Gv, P, P) + Fr(1, 5) * (v @ G @ W @ Gv)
            )
            A5_bad = Fr(1, 600) * (m.tri(W6, Gv, P, P) + Fr(1, 5) * (v @ G @ W @ Gv))
            ok &= coef(d, 3) == A5
            ok_break &= coef(d, 3) != A5_bad
    report(
        f"{pre}C4",
        ok,
        "g^5 coefficient = A5[G_C] = (1/600)[T(G v,P,P)/2 + <v,G W G v>/5]",
    )
    report(f"{pre}C4-break", ok_break, "factor 1/2 -> 1 fails")

    # ---- C3.6-relax (critic-068 #1): the O(g^3) composite coupling g^3 <lambda, Z(Sigma,Psi)>
    # deforms the lambda-EOM to mu(Sigma - P) + g Z(Sigma) = 0.  For Z = M Sigma (M: S -> N,
    # r x D) the surface is Sigma = R(g)(P + B y), R = 1 - g Xi (1 + g M Xi)^{-1} M, with
    # C = col(B) = ker mu; nothing else in the elimination changes (V4 Xi = 0).
    rng_x = random.Random(
        SEED * 10 + r
    )  # separate stream: the draws above are unchanged
    A_a = inv(B_a.T @ m.V4 @ B_a)

    def R_of(M: np.ndarray) -> Series:
        Rs = s_zero((D, D))
        Rs[0] = identity(D)
        pw = identity(r)
        for k in range(1, ORDER + 1):
            Rs[k] = (-1) ** k * (m.Xi @ pw @ M)  # R_k = (-1)^k Xi (M Xi)^{k-1} M
            pw = pw @ (M @ m.Xi)
        return Rs

    fam = [
        L,
        2 * L,
        -(mu_b @ B_a),
    ]  # C_L, C_2L, and C_b = col(B_a + Xi L_b), L_b = -mu_b B_a
    ok, ok_shift, ok_break = True, True, True
    for psi in psis:
        P = m.pvec(psi)
        W = m.W(psi)
        vN = m.Xi.T @ (W @ P)
        for Lx in fam:
            BL = B_a + m.Xi @ Lx
            assert rank(BL) == D - r
            M_L = Fr(1, 10) * (
                Lx @ A_a @ (2 * B_a + m.Xi @ Lx).T @ W
            )  # Z_L = M_L Sigma
            d = mismatch(m, psi, BL, W6_a, R=R_of(M_L))
            ok &= coef(d, 0) == 0 and coef(d, 1) == 0 and coef(d, 2) == 0
            d0 = mismatch(m, psi, BL, W6_a)
            ok_break &= coef(d0, 2) != 0
        # general shift formula, arbitrary Z = M Sigma
        Mr = rand_arr((r, D), rng_x)
        ZP = Mr @ P
        for B in (B_a, B_b):
            dz = mismatch(m, psi, B, W6_a, R=R_of(Mr))
            d0 = mismatch(m, psi, B, W6_a)
            ok_shift &= coef(dz, 0) == coef(d0, 0) and coef(dz, 1) == coef(d0, 1)
            ok_shift &= (
                coef(dz, 2) - coef(d0, 2) == -Fr(1, 60) * (vN @ ZP) and (vN @ ZP) != 0
            )
    report(
        f"{pre}C3.6-relax",
        ok,
        "with Z_L, the fixed vertex W6^{(C_a)} matches g^2..g^4 in C_L, C_2L, C_b",
    )
    report(
        f"{pre}C3.6-relax-shift",
        ok_shift,
        "random Z: g^2, g^3 unchanged, [g^4] shifted by -(1/60) v_N^T Z(P)",
    )
    report(
        f"{pre}C3.6-relax-break",
        ok_break,
        "same complements, W6^{(C_a)}, Z = 0: g^4 mismatch nonzero",
    )


def run_r0(n: int, rng: random.Random) -> None:
    """Check the r = 0 limit (critic-068 #4): ker V4 = 0, C = S, G_C = V4^{-1}; R19."""
    m = Model.__new__(Model)
    m.n, m.r, m.D = n, 0, n * (n + 1) // 2
    D = m.D
    m.Lam = sym_basis(n)
    while True:
        V4 = rand_arr((D, D), rng)
        V4 = V4 + V4.T
        if rank(V4) == D:
            break
    m.V4 = V4
    V5 = rand_arr((D, D, n), rng)
    m.V5 = (V5 + V5.transpose(1, 0, 2)) * Fr(1, 2)
    V6 = rand_arr((D, D, D), rng)
    m.V6 = sum(V6.transpose(p) for p in itertools.permutations(range(3))) * Fr(1, 6)
    print(f"--- model r0: n={n}, D={D}, corank r=0")
    Id = identity(D)
    V4inv = inv(V4)
    ok = is_zero(G_of(m, Id) - V4inv)
    W6 = m.V6 - Fr(6, 5) * m.composite(V4inv)  # R19's W6 verbatim
    ok_break = True
    for _ in range(2):
        psi = rand_arr((n,), rng)
        v = m.W(psi) @ m.pvec(psi)
        d = mismatch(m, psi, Id, W6)
        ok &= coef(d, 0) == 0 and coef(d, 1) == 0 and coef(d, 2) == 0
        d0 = mismatch(m, psi, Id, m.V6)
        ok_break &= coef(d0, 2) == Fr(1, 600) * (v @ V4inv @ v) != 0
    report("C3.4-r0", ok, "r = 0: G_C = V4^{-1}; R19's W6 gives g^2..g^4 zero")
    report("C3.4-r0-break", ok_break, "r = 0, V6 alone: g^4 = <v,V4^{-1} v>/600 != 0")


if __name__ == "__main__":
    print(f"seed = {SEED}, reduced ORDER = {ORDER} (absolute O(g^{ORDER + 2}))")
    rng = random.Random(SEED)
    run(3, 1, "", rng)
    run(3, 2, "C5-", rng)
    run_r0(3, random.Random(SEED * 10))
    print(f"\n{len(failures)} failure(s): {failures}  [{time.time() - t0:.1f} s]")
    sys.exit(len(failures))
