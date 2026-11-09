"""
Verify record 061 (PH2 (a)): the nested kernels of R26's dressed tower at g = 0.

Finite model of the algebraic layer (record 019, R26): H_0 = Q^2, Sym^k H_0 with the
symmetrised basis E_alpha = Sym(e_I) (alpha a multiset), exact rational arithmetic
(sympy). Parents: T_4 = V_4, T_5 = V_5 (totally symmetric), T_6 (level-3 kinetic and
source), T_7 (level-3 odd coupling), T_8, T_9 (level 4). Tower truncated at K = 3 or 4.

Jacobi operator (019 (1.1)):  A_kk = a_k Mhat_k,  Mhat_k = Mt_k - g/(2k+1) T_{2k+1}(.,.,Psi),
A_{k,k-1} = -a_k L_k(Psi),  a_k = g^(2k-2)/(2k)!.
Nested kernels (019 (1.2)):  H_K = Mhat_K,  H_k = Mhat_k - g^2 c_k L_{k+1}^T H_{k+1}^{-1} L_{k+1},
c_k = (2k)!/(2k+2)!.

What is verified (each check is named after the claim-tree node of record 061):
  C1.1  H_k(g, Psi) = H_k(1, g Psi) exactly (scaling), break: wrong Schur power.
  C1.2  det H_k(g) -> det Mt_k as g -> 0: Taylor coefficients of det H_k from the
        nilpotent-g recursion (truncated series, g^(N+1) = 0) equal, exactly, those of
        the full Jacobi determinant route det A_{k..K} / (a_k^{d_k} det A_{k+1..K})
        (no Schur recursion); order 0 = det Mt_k, order 1 = Jacobi formula; exact
        convergence rate at small rational g. Breaks: perturbed c_2, flipped odd sign.
  C1.3  descent leg: a kernel n of Mt_3 in the joint kernel (T_7(n,.,Psi) = 0,
        L_3^T n = 0): det H_3 = 0 identically on Sym^3 (kernel stable in g), H_2 on the
        quotient complement-independent. Break: T_7(n,.,Psi) != 0 -> complement-dependent.
  C1.4  on the quotient: [g^0] det H_3|_Q = det Mt_3|_Q != 0 and H_2(0) = V_4.
  C1.5  smallest |g| zero of det H_k(g) (fixed Psi) is > 0, k = 2..4.
  C1.6  without D1 the kernel moves: H_3(g) n != 0 for g != 0.
  C1.7  missed terms, level-3 kernel off the quotient: block-symmetric parent keeps
        [g^0] H_2 = V_4 and [g^1] H_2 = -V_5 Psi/5 (pole order 2); a non-block-symmetric
        source (l = L_3^T n != 0) gives the predicted missed O(g) term (pole order 1)
        and the predicted missed O(g^0) term (pole order 2), direction dependent.
  C1.8  break leg: PH1 holds (det V_4 != 0, Jacobi operator invertible at small g != 0)
        while det H_3 has a zero at g = 0: PH2 strictly extends PH1.
  C1.9  factorisation L_k = Mt_k J_k(Psi) for a totally symmetric parent (tensor
        contraction vs matrix product), k = 3, 4; fails for a non-block-symmetric parent.

  Fix pass 1 (critic-061 #7, #12):
  C1.10 first entry of a level-3 kernel n into the value S = ... + (g^2/4!) u_2^T H_2^-1 u_2,
        block parent (l = 0). Pole order 2 (T_7(n,n,.) = 0, the C1.7-protected
        configuration): [g^2]H_2 = -c_2 (J^T Mt_3 J + u u^T/alpha_2), and
        [g^4]S - (collapse value) = -T_7(n,P_3,Psi)^2/(6! T_7(n,.,Psi)^T Mt_3^+ T_7(n,.,Psi)),
        rational (non-constant reduced denominator), homogeneous of degree 6. Pole order 1:
        [g^2]H_2 regular (invisible at n = 6), [g^3]H_2 = c_2 J^T A_3 J - c_2 J^T w w^T J/alpha_1,
        [g^5]S - regular = -T_7(n,P_3,Psi)^2/(7! T_7(n,n,Psi)). Breaks: singular part dropped,
        sign flipped, rationality detector on the polynomial T_6(Psi^6).
  C1.4  (3.5) leg, ker V_4 = span(m) != 0, K = 3: with V_5(m,.,Psi) = 0 and
        T_6(._3; m, Psi) = 0 (dense parent built by exact projection), H_2(g) m = 0 and the
        quotient value is complement-independent. Breaks: V_5(m,.,.) != 0 (R38 clause);
        block T_6 (L_3 m = Mt_3 J_3 m != 0, the new clause), where H_2 m = O(g^2) with the
        predicted Schur coefficient. K = 2 limit: descent iff the R38 clause.
  C1.3  D2 leg, K = 4, level-3 kernel n with L_4(Psi) n = 0: H_3(g) n = 0 including the
        level-4 Schur term; H_2 on the level-3 quotient complement-independent.
        Break: block T_8 (L_4 n = Mt_4 J_4 n != 0).

Checks true by construction (they confirm the model is set up as stated, not a claim):
C1.3-stable-kernel, C1.3-descent-D3, C1.6-kernel-moves, C1.4-quotient-det,
C1.4-H2-at-0, C1.2-coeff0-k2..k4, C1.5-radius-k2..k4, C1.2-limit and its break,
C1.8-break-PH1-holds, C1.8-break-level3-fails (an existence example).

What is NOT verified: the forced-diagonal values of the parents (irrelevant to the
reduction, which holds for any parents in the shared-parent class); anything about the
string vertices (level truncation limit, momenta, PH1's level stability, the level-0 M_3
of PH2 (b)); pole orders 3, 4 (one-line consequences of (4.4), not run); the general-k
form of C1.10 (k = 3 only); dimension n = 2 only.
"""

from __future__ import annotations

import itertools
import random
import sys
from math import factorial

import sympy as sp

SEED = int(sys.argv[1]) if len(sys.argv) > 1 else 20260926
NDIM = 2
ORDER = 4  # nilpotent-g truncation: g^(ORDER+1) = 0
g = sp.Symbol("g")

RESULTS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, info: str = "") -> None:
    """Record and print one named PASS/FAIL check."""
    RESULTS.append((name, bool(ok), info))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {info}")


def expect_fail(name: str, ok: bool, info: str = "") -> None:
    """A break leg: the perturbed statement must FAIL; PASS here means it did."""
    check(name + " (break leg fails as it must)", not ok, info)


# ---------------------------------------------------------------- symmetric basis
def msets(k: int) -> list[tuple[int, ...]]:
    return list(itertools.combinations_with_replacement(range(NDIM), k))


def orbit(alpha: tuple[int, ...]) -> list[tuple[int, ...]]:
    return sorted(set(itertools.permutations(alpha)))


def al(idx: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sorted(idx))


def dim(k: int) -> int:
    return len(msets(k))


def rnd(rng: random.Random, lo: int = -6, hi: int = 6) -> sp.Rational:
    v = 0
    while v == 0:
        v = rng.randint(lo, hi)
    return sp.Rational(v)


def sym_tensor(m: int, rng: random.Random):
    """Totally symmetric m-tensor: value depends only on the multiset."""
    f = {a: rnd(rng) for a in msets(m)}
    return lambda idx: f[al(idx)]


def restrict_kk(T, k: int) -> sp.Matrix:
    """(k|k) restriction: M[a,b] = T(E_a, E_b)."""
    B = msets(k)
    M = sp.zeros(len(B), len(B))
    for i, a in enumerate(B):
        for j, b in enumerate(B):
            oa, ob = orbit(a), orbit(b)
            s = sum(T(I + J) for I in oa for J in ob)
            M[i, j] = sp.Rational(s) / (len(oa) * len(ob))
    return M


def restrict_odd(T, k: int, psi) -> sp.Matrix:
    """T_{2k+1}(E_a, E_b, Psi)."""
    B = msets(k)
    M = sp.zeros(len(B), len(B))
    for i, a in enumerate(B):
        for j, b in enumerate(B):
            oa, ob = orbit(a), orbit(b)
            s = sum(psi[c] * T(I + J + (c,)) for I in oa for J in ob for c in range(NDIM))
            M[i, j] = sp.nsimplify(s) / (len(oa) * len(ob))
    return M


def source(T, k: int, psi) -> sp.Matrix:
    """L_k(Psi)[a,b] = T_{2k}(E_a ; E_b, Psi), a in Sym^k, b in Sym^(k-1)."""
    Bk, Bl = msets(k), msets(k - 1)
    M = sp.zeros(len(Bk), len(Bl))
    for i, a in enumerate(Bk):
        for j, b in enumerate(Bl):
            oa, ob = orbit(a), orbit(b)
            s = sum(psi[c] * T(I + J + (c,)) for I in oa for J in ob for c in range(NDIM))
            M[i, j] = sp.nsimplify(s) / (len(oa) * len(ob))
    return M


def u2(V4, psi) -> sp.Matrix:
    B = msets(2)
    v = sp.zeros(len(B), 1)
    for i, a in enumerate(B):
        oa = orbit(a)
        v[i] = sum(psi[c] * psi[d] * V4(I + (c, d)) for I in oa
                   for c in range(NDIM) for d in range(NDIM)) / len(oa)
    return v


def J_raise(k: int, psi) -> sp.Matrix:
    """J_k(Psi): coordinates (E basis of Sym^k) of Sym(E_b (x) Psi), b in Sym^(k-1)."""
    Bk, Bl = msets(k), msets(k - 1)
    M = sp.zeros(len(Bk), len(Bl))
    for j, b in enumerate(Bl):
        nb = len(orbit(b))
        for i, gam in enumerate(Bk):
            s = sum(psi[I[-1]] for I in orbit(gam) if al(I[:-1]) == b)
            M[i, j] = sp.nsimplify(s) / nb
    return M


def block_parent(Bmat: sp.Matrix, k: int, X=None):
    """Parent T_{2k}(I,J) = B[al(I), al(J)] (+ X): symmetric in each block of k slots."""
    pos = {a: i for i, a in enumerate(msets(k))}

    def T(idx):
        v = Bmat[pos[al(idx[:k])], pos[al(idx[k:])]]
        return v + (X(idx) if X else 0)
    return T


def block_odd(Amats: list[sp.Matrix], k: int):
    """Odd coupling T_{2k+1}(I,J,c) = A_c[al(I), al(J)]."""
    pos = {a: i for i, a in enumerate(msets(k))}
    return lambda idx: Amats[idx[-1]][pos[al(idx[:k])], pos[al(idx[k:2 * k])]]


def rand_sym(d: int, rng: random.Random) -> sp.Matrix:
    R = sp.Matrix(d, d, lambda i, j: rnd(rng))
    return R + R.T


# ---------------------------------------------------------------- nilpotent-g series
class TS:
    """Truncated matrix power series in g: coefficients c[0..ORDER], g^(ORDER+1) = 0."""

    def __init__(self, c: list[sp.Matrix]) -> None:
        self.c = c + [sp.zeros(*c[0].shape)] * (ORDER + 1 - len(c))

    def __add__(self, o: TS) -> TS:
        return TS([a + b for a, b in zip(self.c, o.c, strict=True)])

    def __sub__(self, o: TS) -> TS:
        return TS([a - b for a, b in zip(self.c, o.c, strict=True)])

    def __matmul__(self, o: TS) -> TS:
        return TS([sum((self.c[i] * o.c[m - i] for i in range(m + 1)),
                       sp.zeros(self.c[0].rows, o.c[0].cols)) for m in range(ORDER + 1)])

    def scale(self, s) -> TS:
        return TS([s * a for a in self.c])

    def shift(self, p: int) -> TS:
        """Multiply by g^p."""
        z = sp.zeros(*self.c[0].shape)
        return TS([z] * p + self.c[: ORDER + 1 - p])

    @property
    def T(self) -> TS:
        return TS([a.T for a in self.c])

    def inv(self) -> TS:
        X0 = self.c[0].inv()
        X = [X0]
        for m in range(1, ORDER + 1):
            acc = sum((self.c[j] * X[m - j] for j in range(1, m + 1)),
                      sp.zeros(*X0.shape))
            X.append(-X0 * acc)
        return TS(X)

    def det(self) -> list[sp.Rational]:
        """Taylor coefficients of det via det(H0) exp(tr log(1 + H0^{-1}(H - H0)))."""
        H0 = self.c[0]
        X = TS([sp.zeros(*H0.shape)] + [H0.inv() * a for a in self.c[1:]])
        logd = [sp.Integer(0)] * (ORDER + 1)
        P = X
        for m in range(1, ORDER + 1):
            for j in range(ORDER + 1):
                logd[j] += sp.Rational((-1) ** (m + 1), m) * P.c[j].trace()
            P = P @ X
        ex = sp.series(sp.exp(sum(logd[j] * g ** j for j in range(ORDER + 1))),
                       g, 0, ORDER + 1).removeO()
        return [H0.det() * ex.coeff(g, j) for j in range(ORDER + 1)]


def const(M: sp.Matrix) -> TS:
    return TS([M])


def lin(M0: sp.Matrix, M1: sp.Matrix) -> TS:
    return TS([M0, M1])


def ck(k: int) -> sp.Rational:
    return sp.Rational(factorial(2 * k), factorial(2 * k + 2))


def ak(k: int):
    return g ** (2 * k - 2) / factorial(2 * k)


# ---------------------------------------------------------------- tower data
def tower_blocks(par: dict, K: int, psi) -> dict:
    """Mt_k, A_k = -T_{2k+1}(.,.,Psi)/(2k+1), L_k(Psi) from the parent tensors."""
    out = {}
    for k in range(2, K + 1):
        out[("M", k)] = restrict_kk(par[2 * k], k)
        out[("A", k)] = -restrict_odd(par[2 * k + 1], k, psi) / (2 * k + 1)
        if k >= 3:
            out[("L", k)] = source(par[2 * k], k, psi)
    return out


def nested_series(bl: dict, K: int, cfac=None) -> dict[int, TS]:
    """Nilpotent-g recursion (019 (1.2)); cfac overrides c_k (break legs)."""
    cfac = cfac or ck
    H = {K: lin(bl[("M", K)], bl[("A", K)])}
    for k in range(K - 1, 1, -1):
        Lk = const(bl[("L", k + 1)])
        schur = (Lk.T @ H[k + 1].inv() @ Lk).shift(2).scale(cfac(k))
        H[k] = lin(bl[("M", k)], bl[("A", k)]) - schur
    return H


def nested_symbolic(bl: dict, K: int, gpow: int = 2) -> dict[int, sp.Matrix]:
    """Exact rational-in-g nested kernels (for singular top levels)."""
    H = {K: bl[("M", K)] + g * bl[("A", K)]}
    for k in range(K - 1, 1, -1):
        Lk = bl[("L", k + 1)]
        Hin = H[k + 1].adjugate() / H[k + 1].det()
        H[k] = bl[("M", k)] + g * bl[("A", k)] - g ** gpow * ck(k) * Lk.T * Hin * Lk
    return H


def nested_at(bl: dict, K: int, gval, gpow: int = 2) -> dict[int, sp.Matrix]:
    """Nested kernels at an exact rational g (019 (1.2)); gpow != 2 is a break leg."""
    H = {K: bl[("M", K)] + gval * bl[("A", K)]}
    for k in range(K - 1, 1, -1):
        Lk = bl[("L", k + 1)]
        H[k] = bl[("M", k)] + gval * bl[("A", k)] - gval ** gpow * ck(k) * Lk.T * H[
            k + 1].inv() * Lk
    return H


def jacobi(bl: dict, K: int, kmin: int = 2) -> sp.Matrix:
    """Full Jacobi operator on levels kmin..K (019 (1.1)), no Schur recursion."""
    dims = [bl[("M", k)].rows for k in range(kmin, K + 1)]
    off = [sum(dims[:i]) for i in range(len(dims))]
    A = sp.zeros(sum(dims), sum(dims))
    for i, k in enumerate(range(kmin, K + 1)):
        A[off[i]:off[i] + dims[i], off[i]:off[i] + dims[i]] = ak(k) * (
            bl[("M", k)] + g * bl[("A", k)])
        if k > kmin:
            Lk = -ak(k) * bl[("L", k)]
            A[off[i]:off[i] + dims[i], off[i - 1]:off[i - 1] + dims[i - 1]] = Lk
            A[off[i - 1]:off[i - 1] + dims[i - 1], off[i]:off[i] + dims[i]] = Lk.T
    return A


def jacobi_scaled(bl: dict, K: int, kmin: int = 2) -> sp.Matrix:
    """diag(1/a_k) times the Jacobi operator: blocks Mhat_k, -L_k, -g^2 c_{k-1} L_k^T.

    det = det A / prod_k a_k^{d_k}; its lower-right Schur complements are the H_k, so
    det = prod_{k>=kmin} det H_k, computed here without the recursion.
    """
    dims = [bl[("M", k)].rows for k in range(kmin, K + 1)]
    off = [sum(dims[:i]) for i in range(len(dims))]
    A = sp.zeros(sum(dims), sum(dims))
    for i, k in enumerate(range(kmin, K + 1)):
        A[off[i]:off[i] + dims[i], off[i]:off[i] + dims[i]] = bl[("M", k)] + g * bl[("A", k)]
        if k > kmin:
            A[off[i]:off[i] + dims[i], off[i - 1]:off[i - 1] + dims[i - 1]] = -bl[("L", k)]
            A[off[i - 1]:off[i - 1] + dims[i - 1], off[i]:off[i] + dims[i]] = (
                -g ** 2 * ck(k - 1) * bl[("L", k)].T)
    return A


def poly_det(A: sp.Matrix) -> sp.Expr:
    """Exact det of a polynomial matrix in g (entries of degree <= 2) by interpolation."""
    deg = 2 * A.rows
    pts = [(x, A.subs(g, x).det()) for x in range(deg + 1)]
    return sp.expand(sp.interpolate(pts, g))


def taylor(expr, n: int = ORDER) -> list:
    """Exact Taylor coefficients at g = 0 of a rational function (series division)."""
    num, den = sp.fraction(sp.together(expr))
    P = sp.Poly(sp.expand(num), g).all_coeffs()[::-1]
    Q = sp.Poly(sp.expand(den), g).all_coeffs()[::-1]
    v = next(i for i, q in enumerate(Q) if q != 0)
    if any(P[i] != 0 for i in range(min(v, len(P)))):
        raise ValueError("pole at g = 0")
    P, Q = P[v:], Q[v:]
    out = []
    for m in range(n + 1):
        pm = P[m] if m < len(P) else 0
        acc = pm - sum(Q[j] * out[m - j] for j in range(1, min(m, len(Q) - 1) + 1))
        out.append(sp.nsimplify(acc / Q[0]))
    return out


def mat_taylor(M: sp.Matrix, n: int) -> list[sp.Matrix]:
    coeffs = [[taylor(M[i, j], n) for j in range(M.cols)] for i in range(M.rows)]
    return [sp.Matrix(M.rows, M.cols, lambda i, j, m=m: coeffs[i][j][m]) for m in range(n + 1)]


def p_vec(k: int, psi) -> sp.Matrix:
    """E-basis coordinates of P_k = Psi^(x)k in Sym^k, built as J_k(Psi) ... J_2(Psi) Psi."""
    v = sp.Matrix(psi)
    for j in range(2, k + 1):
        v = J_raise(j, psi) * v
    return v


def constrained_parent(k: int, Bmat: sp.Matrix, kill: sp.Matrix, rng: random.Random):
    """Dense parent T_{2k} with T|_(k|k) = Bmat and L_k(e_c) kill = 0 for every c.

    The components t_I (I in [NDIM]^(2k)) are a random rational vector projected, exactly,
    onto the affine space {C t = d} of the two linear constraints (minimal-norm
    correction t = t_r + C^T (C C^T)^(-1) (d - C t_r)). kill is a vector of Sym^(k-1).
    """
    tuples = list(itertools.product(range(NDIM), repeat=2 * k))
    pos = {t: i for i, t in enumerate(tuples)}
    rows, rhs = [], []
    Bk, Bl = msets(k), msets(k - 1)
    for i, a in enumerate(Bk):      # (k|k) restriction = Bmat
        for j, b in enumerate(Bk):
            oa, ob = orbit(a), orbit(b)
            r = [sp.Integer(0)] * len(tuples)
            for I in oa:
                for J in ob:
                    r[pos[I + J]] += sp.Rational(1, len(oa) * len(ob))
            rows.append(r)
            rhs.append(Bmat[i, j])
    for c in range(NDIM):          # (L_k(e_c) kill)[a] = 0
        for a in Bk:
            oa = orbit(a)
            r = [sp.Integer(0)] * len(tuples)
            for j, b in enumerate(Bl):
                ob = orbit(b)
                for I in oa:
                    for J in ob:
                        r[pos[I + J + (c,)]] += kill[j] * sp.Rational(1, len(oa) * len(ob))
            rows.append(r)
            rhs.append(sp.Integer(0))
    C = sp.Matrix(rows)
    d = sp.Matrix(rhs)
    t_r = sp.Matrix([rnd(rng) for _ in tuples])
    t = t_r + C.T * (C * C.T).LUsolve(d - C * t_r)
    return lambda idx: t[pos[tuple(idx)]]


def quotient_value(H2: sp.Matrix, u2v: sp.Matrix, Cb: sp.Matrix):
    """Gaussian value u^T H^{-1} u on a complement Cb of the level-2 quotient."""
    Hc = Cb.T * H2 * Cb
    uc = Cb.T * u2v
    return sp.cancel((uc.T * (Hc.adjugate() / Hc.det()) * uc)[0])


def quotient_H2_lvl3(M2, A2, L3, H3, Cb: sp.Matrix) -> sp.Matrix:
    """H_2 with the level-3 Schur term taken on a complement Cb of the level-3 quotient."""
    H3c = Cb.T * H3 * Cb
    L3c = Cb.T * L3
    H2 = M2 + g * A2 - g ** 2 * ck(2) * L3c.T * (H3c.adjugate() / H3c.det()) * L3c
    return H2.applyfunc(sp.cancel)


def is_zero(M: sp.Matrix) -> bool:
    return M.applyfunc(sp.cancel) == sp.zeros(*M.shape)


def nonpolynomial(expr, xs) -> bool:
    """True iff the rational function expr of xs has a non-constant reduced denominator."""
    den = sp.denom(sp.cancel(sp.together(expr)))
    return sp.Poly(den, *xs).total_degree() > 0


# ---------------------------------------------------------------- main
def main() -> int:
    rng = random.Random(SEED)
    print(f"seed = {SEED}, NDIM = {NDIM}, ORDER = {ORDER}")
    psi = [rnd(rng), rnd(rng)]
    par = {m: sym_tensor(m, rng) for m in range(4, 10)}  # totally symmetric parents
    K = 4
    bl = tower_blocks(par, K, psi)
    for k in range(2, K + 1):
        assert bl[("M", k)].det() != 0, "generic draw must be non-degenerate"

    # ---- C1.8 factorisation L_k = Mt_k J_k for a totally symmetric parent
    for k in (3, 4):
        diff = bl[("L", k)] - bl[("M", k)] * J_raise(k, psi)
        check(f"C1.9-factor-k{k}", diff == sp.zeros(*diff.shape),
              "L_k(Psi) from the tensor == Mt_k J_k(Psi)")

    # ---- C1.1 scaling H_k(g,Psi) = H_k(1, g Psi), exact at a rational point
    g0 = sp.Rational(3, 7)
    blg = tower_blocks(par, K, [g0 * p for p in psi])
    Hs = nested_at(bl, K, g0)
    H1 = nested_at(blg, K, 1)
    ok = all(Hs[k] - H1[k] == sp.zeros(*Hs[k].shape) for k in range(2, K + 1))
    check("C1.1-scaling", ok, f"H_k(g,Psi) == H_k(1,g Psi) for k=2..{K}, g={g0}")
    Hbad = nested_at(bl, K, g0, gpow=1)
    Hbad1 = nested_at(blg, K, 1, gpow=1)
    okb = Hbad[2] - Hbad1[2] == sp.zeros(3, 3)
    expect_fail("C1.1-scaling-break", okb, "Schur term with g^1 instead of g^2")

    # ---- C1.2 det H_k Taylor coefficients: nilpotent route vs full Jacobi route
    Hser = nested_series(bl, K)
    dets_jac = {}
    P = {k: poly_det(jacobi_scaled(bl, K, k)) for k in range(2, K + 1)}
    P[K + 1] = sp.Integer(1)
    for k in range(2, K + 1):
        dets_jac[k] = P[k] / P[k + 1]
    # the rescaling is exact: det A(g0) = prod a_k(g0)^{d_k} det A'(g0)
    gq = sp.Rational(2, 9)
    lhs = jacobi(bl, K).subs(g, gq).det()
    rhs = P[2].subs(g, gq) * sp.prod([ak(k).subs(g, gq) ** bl[("M", k)].rows
                                      for k in range(2, K + 1)])
    check("C1.2-jacobi-rescaling", lhs == rhs and lhs != 0,
          "det A(g) = prod a_k^{d_k} det A'(g) at g = 2/9 (A' = diag(1/a_k) A)")
    for k in range(2, K + 1):
        c_nil = Hser[k].det()
        c_jac = taylor(dets_jac[k])
        check(f"C1.2-series-k{k}", all(sp.simplify(a - b) == 0 for a, b in zip(c_nil, c_jac, strict=True)),
              f"det H_{k}: coefficients 0..{ORDER} nilpotent == full-Jacobi; c0 = {c_jac[0]}")
        Mk = bl[("M", k)]
        check(f"C1.2-coeff0-k{k}", c_jac[0] == Mk.det(),
              f"[g^0] det H_{k} (full Jacobi) == det Mt_{k} = {Mk.det()}")
        c1 = Mk.det() * (Mk.inv() * bl[("A", k)]).trace()
        check(f"C1.2-coeff1-k{k}", sp.simplify(c_jac[1] - c1) == 0,
              "[g^1] det H_k == det Mt_k tr(Mt_k^-1 A_k) (Jacobi formula)")
        c1bad = Mk.det() * (Mk.inv() * (-bl[("A", k)])).trace()
        expect_fail(f"C1.2-coeff1-k{k}-break", sp.simplify(c_jac[1] - c1bad) == 0,
                    "sign of the odd coupling flipped")
    # break: perturbed c_2 in the nilpotent route
    Hbad = nested_series(bl, K, cfac=lambda k: ck(k) * (2 if k == 2 else 1))
    cb = Hbad[2].det()
    cj = taylor(dets_jac[2])
    expect_fail("C1.2-series-break", all(sp.simplify(a - b) == 0 for a, b in zip(cb, cj, strict=True)),
                "c_2 -> 2 c_2 in the Schur recursion")
    # exact convergence det H_2(g) -> det Mt_2 and remainder scaling of the Taylor
    # polynomial through g^ORDER: |det H_2(g) - sum_j c_j g^j| ~ |c_{ORDER+1}| g^(ORDER+1)
    d0 = bl[("M", 2)].det()
    gs = (sp.Rational(1, 10 ** 4), sp.Rational(1, 10 ** 6))
    close = abs(dets_jac[2].subs(g, gs[1]) - d0) < abs(d0) * sp.Rational(1, 10 ** 4)
    rem = [abs(dets_jac[2].subs(g, x) - sum(cj[j] * x ** j for j in range(ORDER + 1)))
           for x in gs]
    ratio = sp.N(rem[0] / rem[1], 12)
    check("C1.2-limit", close and abs(ratio / 10 ** (2 * (ORDER + 1)) - 1) < sp.Rational(1, 100),
          f"det H_2(1e-6) within 1e-4 rel of det Mt_2; remainder ratio g=1e-4 vs 1e-6: "
          f"{ratio:.6e} (expected 1e{2 * (ORDER + 1)})")
    cjb = list(cj)
    cjb[ORDER] = cjb[ORDER] * 2
    remb = [abs(dets_jac[2].subs(g, x) - sum(cjb[j] * x ** j for j in range(ORDER + 1)))
            for x in gs]
    ratiob = sp.N(remb[0] / remb[1], 12)
    expect_fail("C1.2-limit-break", abs(ratiob / 10 ** (2 * (ORDER + 1)) - 1) < sp.Rational(1, 100),
                f"[g^{ORDER}] doubled: remainder ratio {ratiob:.3e}")

    # ---- C1.4 neighbourhood: smallest zero of det H_k(g) in |g|, level by level
    for k in range(2, K + 1):
        numer = sp.Poly(sp.numer(sp.cancel(dets_jac[k])), g)
        roots = [abs(complex(r)) for r in numer.nroots(n=15)]
        r = min(roots) if roots else float("inf")
        check(f"C1.5-radius-k{k}", r > 0, f"smallest |g| zero of det H_{k}: {r:.4g} (Psi fixed)")

    # ---- level-3 kernel legs (K = 3): block parents with prescribed kernel n
    K3 = 3
    d3 = dim(3)
    n_vec = sp.Matrix([1, -2, 1, 3])  # kernel vector (E-basis coordinates)
    Pn = sp.eye(d3) - n_vec * n_vec.T / (n_vec.T * n_vec)[0]
    Bsing = Pn * rand_sym(d3, rng) * Pn  # symmetric, B n = 0
    assert Bsing * n_vec == sp.zeros(d3, 1) and Bsing.rank() == d3 - 1

    def odd_mats(mode: str) -> list[sp.Matrix]:
        out = []
        for _ in range(NDIM):
            R = rand_sym(d3, rng)
            if mode == "annihilate":      # D1: T_7(n,.,Psi) = 0
                R = Pn * R * Pn
            elif mode == "isotropic":     # T_7(n,n,Psi) = 0, T_7(n,.,Psi) != 0
                R = R - (n_vec.T * R * n_vec)[0] / (n_vec.T * n_vec)[0] ** 2 * n_vec * n_vec.T
            out.append(R)
        return out

    def X_nonblock():
        """6-linear X, zero on Sym^3 in the last block, nonzero on Sym^2 (x) Psi."""
        C = {(a, J): rnd(rng) for a in msets(3)
             for J in itertools.product(range(NDIM), repeat=3)}

        def X(idx):
            a, J = al(idx[:3]), tuple(idx[3:])
            ob = orbit(al(J))
            return C[(a, J)] - sum(C[(a, Jp)] for Jp in ob) / len(ob)
        return X

    def level3(odd_mode: str, nonblock: bool, psi_):
        p = dict(par)
        p[6] = block_parent(Bsing, 3, X_nonblock() if nonblock else None)
        p[7] = block_odd(odd_mats(odd_mode), 3)
        return p

    # C1.3 descent: kernel in the joint kernel
    pD = level3("annihilate", False, psi)
    blD = tower_blocks(pD, K3, psi)
    check("C1.3-descent-D3", (n_vec.T * blD[("L", 3)]) == sp.zeros(1, dim(2)),
          "block parent: n^T L_3(Psi) = 0 automatically")
    H3 = blD[("M", 3)] + g * blD[("A", 3)]
    check("C1.3-stable-kernel", sp.expand(H3.det()) == 0 and H3 * n_vec == sp.zeros(d3, 1),
          "det H_3(g) = 0 identically and H_3(g) n = 0: kernel stable in g")

    def quotient_H2(blx, Cbasis: sp.Matrix) -> sp.Matrix:
        H3c = Cbasis.T * (blx[("M", 3)] + g * blx[("A", 3)]) * Cbasis
        L3c = Cbasis.T * blx[("L", 3)]
        H2 = blx[("M", 2)] + g * blx[("A", 2)] - g ** 2 * ck(2) * L3c.T * (
            H3c.adjugate() / H3c.det()) * L3c
        return H2.applyfunc(sp.cancel)

    C1 = sp.Matrix.hstack(*[sp.eye(d3)[:, i] for i in range(1, d3)])  # drop e_0
    C2 = sp.Matrix.hstack(*[sp.eye(d3)[:, i] + (i + 1) * n_vec / 7 for i in (0, 1, 3)])
    for Cb in (C1, C2):
        assert sp.Matrix.hstack(Cb, n_vec).rank() == d3
    H2a, H2b = quotient_H2(blD, C1), quotient_H2(blD, C2)
    check("C1.3-complement-indep", (H2a - H2b).applyfunc(sp.cancel) == sp.zeros(3, 3),
          "H_2 on the quotient identical for two complements of span(n)")
    qdet = taylor((C1.T * H3 * C1).det(), 2)
    check("C1.4-quotient-det", qdet[0] == (C1.T * Bsing * C1).det() and qdet[0] != 0,
          f"[g^0] det H_3|_Q = det Mt_3|_Q = {qdet[0]} != 0")
    check("C1.4-H2-at-0", H2a.subs(g, 0) == blD[("M", 2)], "H_2(0) on the quotient == V_4")
    # break: D1 violated -> complement dependence
    pN = level3("generic", False, psi)
    blN = tower_blocks(pN, K3, psi)
    diffc = (quotient_H2(blN, C1) - quotient_H2(blN, C2)).applyfunc(sp.cancel)
    expect_fail("C1.3-complement-indep-break", diffc == sp.zeros(3, 3),
                "T_7(n,.,Psi) != 0: the quotient is inconsistent")
    # C1.5 kernel moves without D1
    Hn = (blN[("M", 3)] + g * blN[("A", 3)]) * n_vec
    check("C1.6-kernel-moves", Hn != sp.zeros(d3, 1),
          "T_7(n,.,Psi) != 0 => H_3(g) n = g A n != 0 for g != 0")

    # ---- C1.7 break leg: PH1 holds, level 3 fails at g = 0
    detV4 = blN[("M", 2)].det()
    detJ = jacobi(blN, K3).subs(g, sp.Rational(1, 100)).det()
    c3 = taylor((blN[("M", 3)] + g * blN[("A", 3)]).det(), 2)
    check("C1.8-break-PH1-holds", detV4 != 0 and detJ != 0,
          f"det V_4 = {detV4} != 0; det Jacobi(g=1/100) != 0")
    check("C1.8-break-level3-fails", c3[0] == 0 and c3[1] != 0,
          f"det H_3: [g^0] = {c3[0]}, [g^1] = {c3[1]} (simple zero at g = 0)")

    # ---- C1.6 missed terms
    def H2_series(blx, n=1):
        return mat_taylor(nested_symbolic(blx, K3)[2], n)

    V5A = bl[("A", 2)]  # -V_5(.,.,Psi)/5, shared by all legs (same V_4, V_5)
    # (i) block-symmetric parent, pole order 2: [g^0], [g^1] protected
    pI = level3("isotropic", False, psi)
    blI = tower_blocks(pI, K3, psi)
    sI = H2_series(blI, 1)
    check("C1.7-protected", sI[0] == bl[("M", 2)] and sI[1] == V5A,
          "block parent, Mt_3 singular (pole order 2): [g^0]H_2 = V_4, [g^1]H_2 = -V_5Psi/5")
    # (ii) non-block source, pole order 1: missed O(g) term
    pX1 = level3("generic", True, psi)
    blX1 = tower_blocks(pX1, K3, psi)
    ell = blX1[("L", 3)].T * n_vec
    alpha1 = (n_vec.T * blX1[("A", 3)] * n_vec)[0]
    sX1 = H2_series(blX1, 1)
    pred1 = V5A - ck(2) * ell * ell.T / alpha1
    check("C1.7-missed-g1", sX1[0] == bl[("M", 2)] and
          (sX1[1] - pred1).applyfunc(sp.simplify) == sp.zeros(3, 3) and ell != sp.zeros(3, 1),
          "[g^0]H_2 = V_4; [g^1]H_2 = -V_5Psi/5 - c_2 l l^T/alpha_1 (l = L_3^T n != 0)")
    # (iii) non-block source, pole order 2: missed O(g^0) term, direction dependent
    pX2 = level3("isotropic", True, psi)

    def missed0(psi_):
        blx = tower_blocks(pX2, K3, psi_)
        w = blx[("A", 3)] * n_vec
        alpha2 = -(w.T * Bsing.pinv() * w)[0]
        l_ = blx[("L", 3)].T * n_vec
        pred = bl[("M", 2)] - ck(2) * l_ * l_.T / alpha2
        return mat_taylor(nested_symbolic(blx, K3)[2], 0)[0], pred

    got, pred = missed0(psi)
    check("C1.7-missed-g0", (got - pred).applyfunc(sp.simplify) == sp.zeros(3, 3)
          and got != bl[("M", 2)],
          "[g^0]H_2 = V_4 - c_2 l l^T/alpha_2 != V_4 (alpha_2 = -w^T Mt_3^+ w, w = A n)")
    got2, _ = missed0([psi[0] + 1, psi[1] - 2])
    check("C1.7-direction", (got - got2).applyfunc(sp.simplify) != sp.zeros(3, 3),
          "H_2(g->0) depends on the direction of Psi: H_2(phi) discontinuous at phi = 0")
    # factorisation break: non-block parent violates L_3 = Mt_3 J_3
    diffX = blX1[("L", 3)] - blX1[("M", 3)] * J_raise(3, psi)
    expect_fail("C1.9-factor-break", diffX == sp.zeros(*diffX.shape),
                "non-block-symmetric parent")

    # ---- C1.10 first entry of a level-3 kernel into the value (fix pass 1, #7)
    J3 = J_raise(3, psi)
    p2, p3 = p_vec(2, psi), p_vec(3, psi)
    u2v = u2(par[4], psi)
    assert bl[("M", 2)] * p2 == u2v and J3 * p2 == p3  # u_2 = V_4 P_2, J_3 P_2 = P_3

    def value_coeffs(Hcoef: list[sp.Matrix], uvec: sp.Matrix) -> dict[int, sp.Expr]:
        """[g^m] of (g^2/4!) u^T H^{-1} u, m = 2..ORDER+1, from the Taylor coefficients of H."""
        Hi = TS(list(Hcoef)).inv()
        return {j + 2: sp.Rational(1, 24) * (uvec.T * Hi.c[j] * uvec)[0] for j in range(ORDER)}

    # (i) pole order 2: the C1.7-protected configuration (block parent, T_7(n,n,.) = 0)
    M3I, A3I = blI[("M", 3)], blI[("A", 3)]
    R7I = restrict_odd(pI[7], 3, psi)                 # T_7(E_a, E_b, Psi)
    wI = A3I * n_vec                                   # w = A(n, .) = -T_7(n,.,Psi)/7
    assert (n_vec.T * wI)[0] == 0 and R7I * n_vec == -7 * wI
    a2I = -(wI.T * M3I.pinv() * wI)[0]                # alpha_2 (K = 3: B = 0)
    uI = -J3.T * wI                                    # u = -J_3(Psi)^T w
    cI = mat_taylor(nested_symbolic(blI, K3)[2], 3)   # exact Taylor coefficients of H_2
    regI = -ck(2) * J3.T * M3I * J3                    # generalised-inverse reading
    predI = regI - ck(2) * uI * uI.T / a2I
    check("C1.10-order2-g2", is_zero(cI[2] - predI) and uI != sp.zeros(dim(2), 1),
          "pole order 2: [g^2]H_2 = -c_2 (J^T Mt_3 J + u u^T/alpha_2), u = -J_3^T A_3 n")
    expect_fail("C1.10-order2-g2-break", is_zero(cI[2] - regI),
                "generalised-inverse reading (singular part dropped)")
    vI = value_coeffs(cI, u2v)
    vIreg = value_coeffs([cI[0], cI[1], regI], u2v)
    collapse = (sp.Rational(1, 24) * (p2.T * bl[("A", 2)] * bl[("M", 2)].inv() * bl[("A", 2)]
                                       * p2)[0] + sp.Rational(1, 720) * (p3.T * M3I * p3)[0])
    t7I = R7I * n_vec                                  # T_7(n, ., Psi)
    deltaI = -((t7I.T * p3)[0]) ** 2 / (720 * (t7I.T * M3I.pinv() * t7I)[0])
    check("C1.10-order2-collapse", vIreg[4] == collapse,
          "regular part of [g^4]S = p2^T A2 V4^-1 A2 p2/4! + T_6(Psi^6)/6! (any generalised inverse)")
    check("C1.10-order2-value-n6", vI[4] - vIreg[4] == deltaI and deltaI != 0,
          f"[g^4]S - regular = -T_7(n,P_3,Psi)^2/(6! T_7(n,.,Psi)^T Mt_3^+ T_7(n,.,Psi)) = {deltaI}")
    expect_fail("C1.10-order2-value-n6-break", vI[4] == vIreg[4],
                "old 4 remark: a kernel of Mt_3 invisible at n = 6")
    expect_fail("C1.10-order2-value-n6-sign-break", vI[4] - vIreg[4] == -deltaI,
                "sign of the n = 6 term flipped")
    xs = sp.symbols("x y")
    t7s = restrict_odd(pI[7], 3, list(xs)) * n_vec
    p3s = p_vec(3, list(xs))
    delta_s = -((t7s.T * p3s)[0]) ** 2 / (720 * (t7s.T * M3I.pinv() * t7s)[0])
    tt = sp.Symbol("t")
    hom = sp.cancel(delta_s.subs({xs[0]: tt * xs[0], xs[1]: tt * xs[1]}, simultaneous=True)
                    - tt ** 6 * delta_s) == 0
    atpsi = sp.cancel(delta_s.subs({xs[0]: psi[0], xs[1]: psi[1]}) - deltaI) == 0
    check("C1.10-order2-rational", nonpolynomial(delta_s, xs) and hom and atpsi,
          "the n = 6 term is rational, not polynomial, in Psi, homogeneous of degree 6")
    T6s = sp.expand((p3s.T * M3I * p3s)[0])
    expect_fail("C1.10-order2-rational-control", nonpolynomial(T6s, xs),
                "detector on the polynomial T_6(Psi^6)")

    # (ii) pole order 1: block parent, generic T_7 (the C1.8 configuration)
    M3N, A3N = blN[("M", 3)], blN[("A", 3)]
    wN = A3N * n_vec
    a1N = (n_vec.T * wN)[0]
    assert a1N != 0
    cN = mat_taylor(nested_symbolic(blN, K3)[2], 3)
    regN2 = -ck(2) * J3.T * M3N * J3
    regN3 = ck(2) * J3.T * A3N * J3
    predN3 = regN3 - ck(2) * J3.T * wN * wN.T * J3 / a1N
    check("C1.10-order1-g2", is_zero(cN[2] - regN2),
          "simple pole: [g^2]H_2 = -c_2 J^T Mt_3 J (singular part absent at g^2)")
    check("C1.10-order1-g3", is_zero(cN[3] - predN3),
          "simple pole: [g^3]H_2 = c_2 J^T A_3 J - c_2 J^T w w^T J/alpha_1")
    expect_fail("C1.10-order1-g3-break", is_zero(cN[3] - regN3), "singular part dropped at [g^3]")
    vN = value_coeffs(cN, u2v)
    vNreg = value_coeffs([cN[0], cN[1], regN2, regN3], u2v)
    t7N = restrict_odd(pN[7], 3, psi) * n_vec
    delta5 = -((t7N.T * p3)[0]) ** 2 / (5040 * (n_vec.T * t7N)[0])
    check("C1.10-order1-value", vN[4] == vNreg[4] and vN[5] - vNreg[5] == delta5 and delta5 != 0,
          f"simple pole: [g^4]S regular; [g^5]S - regular = -T_7(n,P_3,Psi)^2/(7! T_7(n,n,Psi))"
          f" = {delta5}")
    expect_fail("C1.10-order1-value-break", vN[5] == vNreg[5], "kernel invisible at n = 7 too")

    # ---- (3.5) leg: ker V_4 = span(m) != 0 (fix pass 1, #12)
    d2 = dim(2)
    m_vec = sp.Matrix([2, -1, 3])
    Pm = sp.eye(d2) - m_vec * m_vec.T / (m_vec.T * m_vec)[0]
    B2s = Pm * rand_sym(d2, rng) * Pm
    assert B2s * m_vec == sp.zeros(d2, 1) and B2s.rank() == d2 - 1
    V4k = block_parent(B2s, 2)
    V5ok = block_odd([Pm * rand_sym(d2, rng) * Pm for _ in range(NDIM)], 2)  # R38 clause
    V5bad = block_odd([rand_sym(d2, rng) for _ in range(NDIM)], 2)
    B3 = rand_sym(d3, rng)
    assert B3.det() != 0
    T6ok = constrained_parent(3, B3, m_vec, rng)      # T_6(._3; m, Psi) = 0, Mt_3 = B_3
    T6blk = block_parent(B3, 3)                        # L_3 = B_3 J_3: L_3 m != 0
    T7g = block_odd([rand_sym(d3, rng) for _ in range(NDIM)], 3)
    u2A = u2(V4k, psi)
    D1 = sp.Matrix.hstack(sp.eye(d2)[:, 1], sp.eye(d2)[:, 2])
    D2 = sp.Matrix.hstack(sp.eye(d2)[:, 1] + m_vec / 5, sp.eye(d2)[:, 2] - 2 * m_vec / 7)
    for Db in (D1, D2):
        assert sp.Matrix.hstack(Db, m_vec).rank() == d2

    def legA(V5, T6, Kx: int = 3):
        blx = tower_blocks({4: V4k, 5: V5, 6: T6, 7: T7g}, Kx, psi)
        return blx, nested_symbolic(blx, Kx)[2].applyfunc(sp.cancel)

    def descends(H2: sp.Matrix) -> bool:
        same = sp.cancel(quotient_value(H2, u2A, D1) - quotient_value(H2, u2A, D2)) == 0
        return is_zero(H2 * m_vec) and same

    blA, HA = legA(V5ok, T6ok)
    assert is_zero(blA[("L", 3)] * m_vec) and blA[("M", 3)] == B3
    check("C1.4-kerV4-descent", descends(HA) and (D1.T * B2s * D1).det() != 0,
          "V_5(m,.,Psi) = 0 and T_6(._3; m, Psi) = 0: H_2(g) m = 0, quotient value "
          "complement-independent, V_4 non-degenerate on the quotient")
    _, HR = legA(V5bad, T6ok)
    expect_fail("C1.4-kerV4-R38-break", descends(HR), "V_5(m,.,Psi) != 0 (R38 clause violated)")
    blT, HT = legA(V5ok, T6blk)
    expect_fail("C1.4-kerV4-T6-break", descends(HT),
                "block T_6: T_6(._3; m, Psi) = (Mt_3 J_3 m) != 0 (new clause violated)")
    cT = mat_taylor(HT * m_vec, 2)
    L3m = blT[("L", 3)] * m_vec
    predT = -ck(2) * blT[("L", 3)].T * B3.inv() * L3m
    check("C1.4-kerV4-T6-order", cT[0] == sp.zeros(d2, 1) and cT[1] == sp.zeros(d2, 1)
          and cT[2] == predT and predT != sp.zeros(d2, 1),
          "T_6 clause violated: H_2 m = O(g^2), [g^2] = -c_2 L_3^T Mt_3^-1 L_3 m (Schur term)")
    _, HK2 = legA(V5ok, T6blk, Kx=2)
    _, HK2b = legA(V5bad, T6blk, Kx=2)
    check("C1.4-K2-limit", descends(HK2) and not descends(HK2b),
          "K = 2: H_2 = V_4 - g V_5/5 descends iff V_5(m,.,Psi) = 0 (R38 exactly)")

    # ---- D2 leg: K = 4, kernel n at level 3, L_4(Psi) n = 0 (fix pass 1, #12)
    d4 = dim(4)
    B4 = rand_sym(d4, rng)
    assert B4.det() != 0
    T8ok = constrained_parent(4, B4, n_vec, rng)       # T_8(._4; n, Psi) = 0, Mt_4 = B_4
    T8blk = block_parent(B4, 4)                         # L_4 = B_4 J_4: L_4 n != 0
    T9g = block_odd([rand_sym(d4, rng) for _ in range(NDIM)], 4)
    T7ann = block_odd(odd_mats("annihilate"), 3)

    def legB(T8):
        parB = {4: par[4], 5: par[5], 6: block_parent(Bsing, 3), 7: T7ann, 8: T8, 9: T9g}
        blx = tower_blocks(parB, 4, psi)
        H4 = blx[("M", 4)] + g * blx[("A", 4)]
        H3 = blx[("M", 3)] + g * blx[("A", 3)] - g ** 2 * ck(3) * blx[("L", 4)].T * (
            H4.adjugate() / H4.det()) * blx[("L", 4)]
        return blx, H3.applyfunc(sp.cancel)

    def descends3(blx, H3) -> bool:
        if not is_zero(H3 * n_vec):
            return False
        Ha = quotient_H2_lvl3(blx[("M", 2)], blx[("A", 2)], blx[("L", 3)], H3, C1)
        Hb = quotient_H2_lvl3(blx[("M", 2)], blx[("A", 2)], blx[("L", 3)], H3, C2)
        return is_zero(Ha - Hb)

    blB, H3B = legB(T8ok)
    assert is_zero(blB[("L", 4)] * n_vec) and blB[("M", 4)] == B4
    check("C1.3-descent-D2", descends3(blB, H3B),
          "K = 4, level-3 kernel n with T_7(n,.,Psi) = 0 and L_4(Psi) n = 0: H_3(g) n = 0 with "
          "the level-4 Schur term, H_2 on the level-3 quotient complement-independent")
    blB2, H3B2 = legB(T8blk)
    expect_fail("C1.3-descent-D2-break", descends3(blB2, H3B2),
                "block T_8: L_4 n = Mt_4 J_4 n != 0 (upward clause violated)")

    nfail = sum(1 for _, ok, _ in RESULTS if not ok)
    print(f"\nSUMMARY: {len(RESULTS) - nfail}/{len(RESULTS)} PASS, {nfail} FAIL (seed {SEED})")
    return 1 if nfail else 0


if __name__ == "__main__":
    sys.exit(main())
