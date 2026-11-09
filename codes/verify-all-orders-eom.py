#!/usr/bin/env python3
"""verify-all-orders-eom.py — companion checks for derivation 100.

Finite-dimensional model of the cubic action `eq:all:action` of the paper
(`03-all-orders.tex`): H = R^N with the Euclidean pairing, Sigma_k in Sym^k(R^N)
in an orthonormal basis (so every multi-string pairing is a dot product, the
even-field case of `eq:conv:pairing-n`), V_2 = Q_B a random symmetric matrix,
V_3, V_4, V_5 random fully symmetric tensors, and dressed forms W_{2k} (random
symmetric matrices on Sym^k) and W_{2k+1} (random arrays symmetric in the two
Sym^k slots) — exactly the block symmetry assumed in record 100, A2.  The action

  S~ = 1/2 <Psi, Q Psi> + g/3! V3(Psi^3)
       + sum_k [ -a_k <S_k, W_{2k} S_k> + 2 a_k <S_k, W_{2k}(Psi (x) S_{k-1})>
                 + b_k W_{2k+1}(S_k, S_k, Psi) ],
  a_k = g^{2k-2}/(2k)!,  b_k = g^{2k-1}/(2k+1)!,  S_1 = Psi,

through K = 4, with or without the odd coupling of the top level.

Checks (named after the claim-tree nodes of agent/derivations/100-...md):
  C1.1  the order-by-order form (1.2) of the action equals the level sum.
  C1.3  stabilization in K of the series coefficients of Sigma_2* and of the
        value (equal through g^3 resp. g^5 between K = 3 and K = 4, different
        at g^4 resp. g^6).
  C3.1  the stated Psi equation (2.4) equals the complex-step gradient of the
        action with respect to Psi, for K = 2, 3, 4 and both truncations.
  C3.2  the stated Sigma_k equation (2.5), times 2 a_k, equals the gradient
        with respect to Sigma_k; break legs: 1/56 -> 1/55, exchange sign,
        the factor 2 of the k = 2 term of the Psi equation.
  C3.4  eliminating the top field with its stated equation reproduces
        `eq:all:eliminate-top`.
  C3.5  the order-by-order recursion (2.7), summed at small g, equals the
        exact stationary point of the action (a linear solve built from the
        action's gradient alone).
  C4    the septic instance (3.1)-(3.4); C5 the octic instance (4.1)-(4.4).
  C6    the octic equations solved order by order and substituted reproduce
        [g^m] S for m <= 6 (and m = 7 with W_9), with W_6, W_7, W_8 (W_9)
        fixed by the diagonal rule `eq:all:diagonal`; break legs (W_8
        undressed, 1/56 -> 1/55); top-first elimination equals joint solve.

Not tested: anything the model lacks — ghost numbers and Grassmann signs
(all fields even here), the kernel condition (every W_{2k} is invertible),
the string-vertex origin of the forms, the convergence of the series.

Usage: from the project root, ``uv run --no-sync python codes/verify-all-orders-eom.py [seed]``.
Exit code = number of failed checks.
"""

from __future__ import annotations

import itertools
import math
import sys

import numpy as np

SEED = int(sys.argv[1]) if len(sys.argv) > 1 else 20261018
rng = np.random.default_rng(SEED)
N = 3
KMAX = 4
TOL = 1e-9
failures: list[str] = []


def report(name: str, ok: bool, detail: str = "") -> None:
    """Print one PASS/FAIL line and record a failure."""
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name}" + (f" — {detail}" if detail else ""))
    if not ok:
        failures.append(name)


def fact(n: int) -> float:
    return float(math.factorial(n))


# ------------------------------------------------------------------ bases
def sym_basis(k: int) -> np.ndarray:
    """Orthonormal basis of Sym^k(R^N) as symmetric tensors (disjoint supports)."""
    elems = []
    for combo in itertools.combinations_with_replacement(range(N), k):
        M = np.zeros((N,) * k)
        for perm in set(itertools.permutations(combo)):
            M[perm] += 1.0
        M /= np.linalg.norm(M)
        elems.append(M)
    return np.array(elems)


LAM = {k: sym_basis(k) for k in range(1, KMAX + 2)}
LF = {k: LAM[k].reshape(len(LAM[k]), -1) for k in LAM}
DIM = {k: len(LAM[k]) for k in LAM}


def symmetrize_first(T: np.ndarray) -> np.ndarray:
    """Symmetrize a tensor whose axes 1.. are already symmetric over axis 0."""
    k = T.ndim
    return sum(np.moveaxis(T, 0, j) for j in range(k)) / k


def Lmap(psi: np.ndarray, k: int) -> np.ndarray:
    """Matrix (D_k, D_{k-1}) of Sigma_{k-1} -> Psi (x) Sigma_{k-1} (symmetrized)."""
    cols = []
    for J in range(DIM[k - 1]):
        T = symmetrize_first(np.multiply.outer(psi, LAM[k - 1][J]))
        cols.append(LF[k] @ T.reshape(-1))
    return np.array(cols).T


def Lmap_psi_slot(sig_coords: np.ndarray, k: int) -> np.ndarray:
    """Matrix (D_k, N) of C -> C (x) Sigma_{k-1} for fixed Sigma_{k-1} (coords)."""
    T = np.tensordot(sig_coords, LAM[k - 1], axes=([0], [0]))
    cols = []
    for a in range(N):
        e = np.zeros(N, dtype=T.dtype)
        e[a] = 1.0
        cols.append(LF[k] @ symmetrize_first(np.multiply.outer(e, T)).reshape(-1))
    return np.array(cols).T


def to_tensor(coords: np.ndarray, k: int) -> np.ndarray:
    return np.tensordot(coords, LAM[k], axes=([0], [0]))


def coords_of_power(psi: np.ndarray, k: int) -> np.ndarray:
    T = np.array(1.0)
    for _ in range(k):
        T = np.multiply.outer(T, psi)
    return LF[k] @ T.reshape(-1)


# --------------------------------------------------------------- vertices
def sym_tensor_perm(n: int) -> np.ndarray:
    T = rng.standard_normal((N,) * n)
    S = np.zeros_like(T)
    for perm in itertools.permutations(range(n)):
        S += np.transpose(T, perm)
    return S / fact(n)


def sym_tensor_rank1(n: int, terms: int) -> np.ndarray:
    S = np.zeros((N,) * n)
    for _ in range(terms):
        a = rng.standard_normal(N)
        a /= np.linalg.norm(a)
        c = rng.standard_normal()
        out = np.array(c)
        for _ in range(n):
            out = np.multiply.outer(out, a)
        S += out
    return S


Q = sym_tensor_perm(2)
V3 = sym_tensor_perm(3)
V4 = sym_tensor_perm(4)
V5 = sym_tensor_perm(5)
V6 = sym_tensor_perm(6)
VN = {2: Q, 3: V3, 4: V4, 5: V5, 6: V6}
VN[7] = sym_tensor_rank1(7, 80)
VN[8] = sym_tensor_rank1(8, 100)
VN[9] = sym_tensor_rank1(9, 130)


def vdiag(T: np.ndarray, psi: np.ndarray) -> float:
    out = T
    for _ in range(T.ndim):
        out = np.tensordot(out, psi, axes=([0], [0]))
    return float(out)


def even_form(T: np.ndarray, k: int) -> np.ndarray:
    """Matrix of a 2k-tensor as a bilinear form on Sym^k (coords)."""
    return LF[k] @ T.reshape(N**k, N**k) @ LF[k].T


def odd_form(T: np.ndarray, k: int) -> np.ndarray:
    """Array (D_k, D_k, N) of a (2k+1)-tensor read with slots (k, k, 1)."""
    return np.einsum("xyz,Ix,Jy->IJz", T.reshape(N**k, N**k, N), LF[k], LF[k])


def random_even_form(k: int) -> np.ndarray:
    A = rng.standard_normal((DIM[k], DIM[k]))
    return A + A.T


def random_odd_form(k: int) -> np.ndarray:
    A = rng.standard_normal((DIM[k], DIM[k], N))
    return A + A.transpose(1, 0, 2)


# Generic block-symmetric forms for the equation-of-motion checks (part A).
W_GEN = {4: even_form(V4, 2), 5: odd_form(V5, 2)}
for kk in range(3, KMAX + 1):
    W_GEN[2 * kk] = random_even_form(kk)
    W_GEN[2 * kk + 1] = random_odd_form(kk)


# ------------------------------------------------------------------ action
def odd_op(W: dict, k: int, psi: np.ndarray) -> np.ndarray:
    """O_k(Psi)_{IJ} = W_{2k+1}(Lambda_I, Lambda_J, Psi)."""
    return np.tensordot(W[2 * k + 1], psi, axes=([2], [0]))


def action(
    g: complex,
    psi: np.ndarray,
    Sig: dict[int, np.ndarray],
    K: int,
    odd_top: bool,
    W: dict,
) -> complex:
    """The cubic action `eq:all:action`, level sum, tower Sigma_2..Sigma_K."""
    S = 0.5 * psi @ Q @ psi + g / 6.0 * np.einsum("abc,a,b,c", V3, psi, psi, psi)
    fields = {1: psi, **Sig}
    for k in range(2, K + 1):
        a_k = g ** (2 * k - 2) / fact(2 * k)
        b_k = g ** (2 * k - 1) / fact(2 * k + 1)
        Sk, Skm = fields[k], fields[k - 1]
        src = W[2 * k] @ (Lmap(psi, k) @ Skm)
        S += -a_k * (Sk @ W[2 * k] @ Sk) + 2 * a_k * (Sk @ src)
        if k < K or odd_top:
            S += b_k * np.einsum("IJa,I,J,a", W[2 * k + 1], Sk, Sk, psi)
    return S


def action_by_orders(g, psi, Sig, K, odd_top, W) -> complex:
    """The same action from the coefficients (1.2) of record 100, sum_m g^m S_[m]."""
    fields = {1: psi, **Sig}
    coeff = {0: 0.5 * psi @ Q @ psi, 1: np.einsum("abc,a,b,c", V3, psi, psi, psi) / 6.0}
    for k in range(2, K + 1):
        Sk, Skm = fields[k], fields[k - 1]
        coeff[2 * k - 2] = (
            -(Sk @ W[2 * k] @ Sk) + 2 * (Sk @ W[2 * k] @ (Lmap(psi, k) @ Skm))
        ) / fact(2 * k)
        if k < K or odd_top:
            coeff[2 * k - 1] = np.einsum("IJa,I,J,a", W[2 * k + 1], Sk, Sk, psi) / fact(
                2 * k + 1
            )
    return sum(g**m * c for m, c in coeff.items())


def gradient(g, psi, Sig, K, odd_top, W) -> tuple[np.ndarray, dict]:
    """Complex-step gradient of the action with respect to every coordinate."""
    h = 1e-30

    def f(psi_, Sig_):
        return action(g, psi_, Sig_, K, odd_top, W)

    gpsi = np.zeros(N)
    for a in range(N):
        p = psi.astype(complex)
        p[a] += 1j * h
        gpsi[a] = f(p, {k: v.astype(complex) for k, v in Sig.items()}).imag / h
    gsig = {}
    for k in range(2, K + 1):
        gk = np.zeros(DIM[k])
        for I in range(DIM[k]):
            S_ = {kk: v.astype(complex) for kk, v in Sig.items()}
            S_[k][I] += 1j * h
            gk[I] = f(psi.astype(complex), S_).imag / h
        gsig[k] = gk
    return gpsi, gsig


# ------------------------------------------------- stated equations of motion
def eom_psi(g, psi, Sig, K, odd_top, W, brk: str | None = None) -> np.ndarray:
    """Equation (2.4) of record 100."""
    S2 = to_tensor(Sig[2], 2)
    E = Q @ psi + g / 2.0 * np.einsum("abc,b,c->a", V3, psi, psi)
    c3 = g**2 / 6.0 if brk != "factor2" else 2 * g**2 / 24.0
    E = E + c3 * np.einsum("abcd,b,cd->a", V4, psi, S2)
    if K > 2 or odd_top:  # the quintic coupling is absent from the quartic action
        E = E + g**3 / 120.0 * np.einsum("abcde,bc,de->a", V5, S2, S2)
    fields = {1: psi, **Sig}
    for k in range(3, K + 1):
        a_k = g ** (2 * k - 2) / fact(2 * k)
        b_k = g ** (2 * k - 1) / fact(2 * k + 1)
        E = E + 2 * a_k * Lmap_psi_slot(fields[k - 1], k).T @ (W[2 * k] @ fields[k])
        if k < K or odd_top:
            E = E + b_k * np.einsum("IJa,I,J->a", W[2 * k + 1], fields[k], fields[k])
    return E


def eom_sigma(k, g, psi, Sig, K, odd_top, W, brk: str | None = None) -> np.ndarray:
    """Equation (2.5) of record 100, normalized as in A3 (divided by 2 a_k)."""
    fields = {1: psi, **Sig}
    E = W[2 * k] @ (Lmap(psi, k) @ fields[k - 1]) - W[2 * k] @ fields[k]
    if k < K or odd_top:
        E = E + g / (2 * k + 1) * odd_op(W, k, psi) @ fields[k]
    if k < K:
        c = g**2 / ((2 * k + 1) * (2 * k + 2))
        if brk == "coef56" and k == 3:
            c = g**2 / 55.0
        if brk == "sign":
            c = -c
        E = E + c * Lmap(psi, k + 1).T @ (W[2 * k + 2] @ fields[k + 1])
    return E


# ------------------------------------------------------- series machinery
def solve_series(psi, K, odd_top, W, M, brk: str | None = None) -> dict:
    """Order-by-order solution (2.7): Sig[k][m] = [g^m] Sigma_k*, m = 0..M."""
    Sig = {k: np.zeros((M + 1, DIM[k])) for k in range(2, K + 1)}
    Sig1 = np.zeros((M + 1, N))
    Sig1[0] = psi
    allS = {1: Sig1, **Sig}
    Winv = {k: np.linalg.inv(W[2 * k]) for k in range(2, K + 1)}
    L = {k: Lmap(psi, k) for k in range(2, K + 2)}
    for m in range(M + 1):
        for k in range(2, K + 1):
            rhs = W[2 * k] @ (L[k] @ allS[k - 1][m])
            if m >= 1 and (k < K or odd_top):
                rhs = rhs + odd_op(W, k, psi) @ allS[k][m - 1] / (2 * k + 1)
            if m >= 2 and k < K:
                c = 1.0 / ((2 * k + 1) * (2 * k + 2))
                if brk == "coef56" and k == 3:
                    c = 1.0 / 55.0
                rhs = rhs + c * (L[k + 1].T @ (W[2 * k + 2] @ allS[k + 1][m - 2]))
            allS[k][m] = Winv[k] @ rhs
    return allS


def conv(A: np.ndarray, X: np.ndarray, Y: np.ndarray, shift: int, M: int) -> np.ndarray:
    """[g^m] of g^shift * X(g)^T A Y(g) for series X, Y (arrays (M+1, dim))."""
    out = np.zeros(M + 1)
    for m in range(shift, M + 1):
        for i in range(m - shift + 1):
            out[m] += X[i] @ A @ Y[m - shift - i]
    return out


def value_series(psi, allS, K, odd_top, W, M) -> np.ndarray:
    """[g^m] of the full action evaluated on the series solution, m = 0..M."""
    out = np.zeros(M + 1)
    out[0] = 0.5 * psi @ Q @ psi
    out[1] = np.einsum("abc,a,b,c", V3, psi, psi, psi) / 6.0
    for k in range(2, K + 1):
        Sk, Skm = allS[k], allS[k - 1]
        out += -conv(W[2 * k], Sk, Sk, 2 * k - 2, M) / fact(2 * k)
        out += 2 * conv(W[2 * k] @ Lmap(psi, k), Sk, Skm, 2 * k - 2, M) / fact(2 * k)
        if k < K or odd_top:
            out += conv(odd_op(W, k, psi), Sk, Sk, 2 * k - 1, M) / fact(2 * k + 1)
    return out


# ------------------------------------------------ polynomial fit, polarization
def monomials(n: int) -> list[tuple[int, ...]]:
    return [a for a in itertools.product(range(n + 1), repeat=N) if sum(a) == n]


def fit_polarize(fun, n: int) -> np.ndarray:
    """Symmetric n-tensor T with T(Psi^n) = fun(Psi), fun homogeneous of degree n."""
    mons = monomials(n)
    P = 3 * len(mons)
    pts = rng.standard_normal((P, N))
    A = np.array([[np.prod(p ** np.array(a)) for a in mons] for p in pts])
    y = np.array([fun(p) for p in pts])
    c, *_ = np.linalg.lstsq(A, y, rcond=None)
    resid = np.linalg.norm(A @ c - y) / max(1.0, np.linalg.norm(y))
    if resid > 1e-8:
        raise RuntimeError(f"polynomial fit of degree {n} failed, resid {resid}")
    T = np.zeros((N,) * n)
    for idx in itertools.product(range(N), repeat=n):
        a = tuple(idx.count(i) for i in range(N))
        multi = fact(n) / np.prod([fact(ai) for ai in a])
        T[idx] = c[mons.index(a)] / multi
    return T


def dressed_tower(target: dict, M: int = 8) -> dict:
    """Build W_6..W_9 by the diagonal rule `eq:all:diagonal` from V_n = target."""
    W = {4: even_form(target[4], 2), 5: odd_form(target[5], 2)}
    steps = [(6, 2, True), (7, 3, False), (8, 3, True), (9, 4, False)]
    for n, K, odd in steps:
        m = n - 2

        def mismatch(psi, W=W, K=K, odd=odd, m=m):
            allS = solve_series(psi, K, odd, W, m)
            A = value_series(psi, allS, K, odd, W, m)[m]
            return vdiag(target[n], psi) - fact(n) * A

        T = fit_polarize(mismatch, n)
        if n % 2 == 0:
            W[n] = even_form(T, n // 2)
        else:
            W[n] = odd_form(T, n // 2)
    return W


# ---------------------------------------------------------------- checks
def rel(a, b) -> float:
    return float(np.linalg.norm(a - b) / max(1.0, np.linalg.norm(a), np.linalg.norm(b)))


def random_fields(K: int) -> tuple[np.ndarray, dict]:
    psi = rng.standard_normal(N)
    Sig = {k: rng.standard_normal(DIM[k]) for k in range(2, K + 1)}
    return psi, Sig


def part_A() -> None:
    print("--- part A: equations of motion against the gradient (generic W) ---")
    W = W_GEN
    for K in (2, 3, 4):
        for odd_top in (True, False):
            tag = f"K{K}-{'odd' if odd_top else 'even'}"
            psi, Sig = random_fields(K)
            g = rng.uniform(0.3, 0.9)
            s1 = action(g, psi, Sig, K, odd_top, W)
            s2 = action_by_orders(g, psi, Sig, K, odd_top, W)
            report(
                f"C1.1-series-equals-level-sum-{tag}",
                abs(s1 - s2) < TOL,
                f"{abs(s1 - s2):.1e}",
            )
            gpsi, gsig = gradient(g, psi, Sig, K, odd_top, W)
            e = rel(gpsi, eom_psi(g, psi, Sig, K, odd_top, W))
            report(f"C3.1-psi-{tag}", e < TOL, f"rel {e:.1e}")
            for k in range(2, K + 1):
                a_k = g ** (2 * k - 2) / fact(2 * k)
                e = rel(gsig[k] / (2 * a_k), eom_sigma(k, g, psi, Sig, K, odd_top, W))
                report(f"C3.2-sigma{k}-{tag}", e < TOL, f"rel {e:.1e}")
    # instances named after the paper's sections
    for K, odd_top, name in ((3, True, "C4-septic"), (4, False, "C5-octic")):
        psi, Sig = random_fields(K)
        g = rng.uniform(0.3, 0.9)
        gpsi, gsig = gradient(g, psi, Sig, K, odd_top, W)
        report(f"{name}-psi", rel(gpsi, eom_psi(g, psi, Sig, K, odd_top, W)) < TOL)
        for k in range(2, K + 1):
            a_k = g ** (2 * k - 2) / fact(2 * k)
            ok = (
                rel(gsig[k] / (2 * a_k), eom_sigma(k, g, psi, Sig, K, odd_top, W)) < TOL
            )
            report(f"{name}-sigma{k}", ok)
    # break legs (must FAIL to agree)
    K, odd_top = 4, False
    psi, Sig = random_fields(K)
    g = 0.7
    gpsi, gsig = gradient(g, psi, Sig, K, odd_top, W)
    a3 = g**4 / fact(6)
    e = rel(gsig[3] / (2 * a3), eom_sigma(3, g, psi, Sig, K, odd_top, W, brk="coef56"))
    report("C3.2-break-coef56-detected", e > 1e-6, f"rel {e:.1e}")
    e = rel(gsig[3] / (2 * a3), eom_sigma(3, g, psi, Sig, K, odd_top, W, brk="sign"))
    report("C3.2-break-sign-detected", e > 1e-6, f"rel {e:.1e}")
    e = rel(gpsi, eom_psi(g, psi, Sig, K, odd_top, W, brk="factor2"))
    report("C3.1-break-factor2-detected", e > 1e-6, f"rel {e:.1e}")
    # C3.4: eliminate the top field with its stated equation
    for K in (3, 4):
        psi, Sig = random_fields(K)
        g = rng.uniform(0.3, 0.9)
        a_K = g ** (2 * K - 2) / fact(2 * K)
        Mhat = W[2 * K] - g / (2 * K + 1) * odd_op(W, K, psi)
        u = W[2 * K] @ (Lmap(psi, K) @ Sig[K - 1])
        SigStar = dict(Sig)
        SigStar[K] = np.linalg.solve(Mhat, u)
        e_top = eom_sigma(K, g, psi, SigStar, K, True, W)
        lhs = action(g, psi, SigStar, K, True, W)
        lower = {k: v for k, v in Sig.items() if k < K}
        rhs = action(g, psi, lower, K - 1, True, W) + a_K * (
            u @ np.linalg.solve(Mhat, u)
        )
        ok = np.linalg.norm(e_top) < TOL and abs(lhs - rhs) < TOL
        report(
            f"C3.4-eliminate-top-K{K}",
            ok,
            f"|E_top| {np.linalg.norm(e_top):.1e}, diff {abs(lhs - rhs):.1e}",
        )


def exact_tower_solve(g, psi, K, odd_top, W) -> dict:
    """Stationary tower from the action's gradient alone (affine in the tower)."""
    dims = [DIM[k] for k in range(2, K + 1)]
    offs = np.cumsum([0] + dims)
    zero = {k: np.zeros(DIM[k]) for k in range(2, K + 1)}
    _, g0 = gradient(g, psi, zero, K, odd_top, W)
    b = np.concatenate([g0[k] for k in range(2, K + 1)])
    H = np.zeros((offs[-1], offs[-1]))
    for k in range(2, K + 1):
        for I in range(DIM[k]):
            S_ = {kk: np.zeros(DIM[kk]) for kk in range(2, K + 1)}
            S_[k][I] = 1.0
            _, gI = gradient(g, psi, S_, K, odd_top, W)
            H[:, offs[k - 2] + I] = (
                np.concatenate([gI[kk] for kk in range(2, K + 1)]) - b
            )
    x = np.linalg.solve(H, -b)
    return {k: x[offs[k - 2] : offs[k - 1]] for k in range(2, K + 1)}


def part_B() -> None:
    print("--- part B: order-by-order solution, closure, triangular structure ---")
    W = W_GEN
    # C3.5: recursion summed at small g == exact stationary point
    K, odd_top, g, M = 4, True, 0.01, 14
    psi = rng.standard_normal(N)
    allS = solve_series(psi, K, odd_top, W, M)
    summed = {k: sum(g**m * allS[k][m] for m in range(M + 1)) for k in range(2, K + 1)}
    exact = exact_tower_solve(g, psi, K, odd_top, W)
    e = max(rel(summed[k], exact[k]) for k in range(2, K + 1))
    report("C3.5-order-by-order", e < TOL, f"rel {e:.1e}")
    ok = all(rel(allS[k][0], coords_of_power(psi, k)) < TOL for k in range(2, K + 1))
    report("C3.5-leading-order-diagonal", ok)
    # C6-top-first: solve the octic equations from the top at fixed g
    K, odd_top, g = 4, False, 0.3
    psi = rng.standard_normal(N)
    exact = exact_tower_solve(g, psi, K, odd_top, W)
    S4 = Lmap(psi, 4) @ exact[3]  # (4.4): Sigma_4 = Psi (x) Sigma_3
    M3 = (
        W[6]
        - g / 7 * odd_op(W, 3, psi)
        - g**2 / 56 * Lmap(psi, 4).T @ W[8] @ Lmap(psi, 4)
    )
    S3 = np.linalg.solve(
        M3, W[6] @ (Lmap(psi, 3) @ exact[2])
    )  # (4.3) with Sigma_4 eliminated
    M2 = (
        W[4]
        - g / 5 * odd_op(W, 2, psi)
        - g**2 / 30 * Lmap(psi, 3).T @ W[6] @ np.linalg.solve(M3, W[6] @ Lmap(psi, 3))
    )  # `eq:hs8:dressed-2`: the Sigma_3 line carries M3^{-1} between two sources W6 L3
    S2 = np.linalg.solve(
        M2, W[4] @ coords_of_power(psi, 2)
    )  # (4.2) with Sigma_3, Sigma_4 eliminated
    e = max(rel(S2, exact[2]), rel(S3, exact[3]), rel(S4, exact[4]))
    report("C6-top-first", e < TOL, f"rel {e:.1e}")
    # C4-sigma-first-order: (3.4) against the series
    K, odd_top = 3, True
    psi = rng.standard_normal(N)
    allS = solve_series(psi, K, odd_top, W, 2)
    P2, P3 = coords_of_power(psi, 2), coords_of_power(psi, 3)
    W4inv, W6inv = np.linalg.inv(W[4]), np.linalg.inv(W[6])
    s2_1 = W4inv @ odd_op(W, 2, psi) @ P2 / 5
    s3_1 = Lmap(psi, 3) @ s2_1 + W6inv @ odd_op(W, 3, psi) @ P3 / 7
    D = W4inv @ odd_op(W, 2, psi)
    s2_2 = D @ D @ P2 / 25 + W4inv @ Lmap(psi, 3).T @ W[6] @ P3 / 30
    e = max(rel(allS[2][1], s2_1), rel(allS[3][1], s3_1), rel(allS[2][2], s2_2))
    report("C4-sigma-first-order", e < TOL, f"rel {e:.1e}")
    # C1.3: stabilization between K = 3 (odd) and K = 4 (even)
    psi = rng.standard_normal(N)
    S3o = solve_series(psi, 3, True, W, 6)
    S4e = solve_series(psi, 4, False, W, 6)
    v3 = value_series(psi, S3o, 3, True, W, 6)
    v4 = value_series(psi, S4e, 4, False, W, 6)
    same = all(rel(S3o[2][m], S4e[2][m]) < TOL for m in range(4)) and all(
        abs(v3[m] - v4[m]) < TOL for m in range(6)
    )
    diff = rel(S3o[2][4], S4e[2][4]) > 1e-6 and abs(v3[6] - v4[6]) > 1e-6
    report(
        "C1.3-stabilization",
        same and diff,
        f"Sigma_2 g^4 rel {rel(S3o[2][4], S4e[2][4]):.1e}, value g^6 {abs(v3[6] - v4[6]):.1e}",
    )

    # C6 / C2.2: closure with the dressed tower built by the diagonal rule
    Wd = dressed_tower(VN)
    psi = rng.standard_normal(N)
    target = [0.5 * psi @ Q @ psi] + [vdiag(VN[n], psi) / fact(n) for n in range(3, 10)]
    allS = solve_series(psi, 4, False, Wd, 7)
    v = value_series(psi, allS, 4, False, Wd, 7)
    for m in range(7):
        report(
            f"C6-closure-g{m}",
            abs(v[m] - target[m]) < 1e-7,
            f"{v[m]:.6f} vs {target[m]:.6f}",
        )
    report(
        "C6-remainder-g7-nonzero-without-W9",
        abs(v[7] - target[7]) > 1e-6,
        f"{abs(v[7] - target[7]):.1e}",
    )
    allS9 = solve_series(psi, 4, True, Wd, 7)
    v9 = value_series(psi, allS9, 4, True, Wd, 7)
    report(
        "C2.2-closure-g7-with-W9",
        all(abs(v9[m] - target[m]) < 1e-7 for m in range(8)),
        f"g^7 diff {abs(v9[7] - target[7]):.1e}",
    )
    # break legs
    Wu = dict(Wd)
    Wu[8] = even_form(VN[8], 4)
    vu = value_series(psi, solve_series(psi, 4, False, Wu, 6), 4, False, Wu, 6)
    ok = (
        all(abs(vu[m] - target[m]) < 1e-7 for m in range(6))
        and abs(vu[6] - target[6]) > 1e-6
    )
    report("C6-break-undressed-W8", ok, f"g^6 diff {abs(vu[6] - target[6]):.1e}")
    # A wrong coefficient in the Sigma_3 equation changes the solution at [g^2]
    # Sigma_3 but, by stationarity, the value only at O(g^8): the value is a
    # weak test of the equations (the equations are tested in part A, C3.*).
    Sb = solve_series(psi, 4, False, Wd, 6, brk="coef56")
    vb = value_series(psi, Sb, 4, False, Wd, 6)
    ok = (
        rel(Sb[3][2], allS[3][2]) > 1e-6
        and max(abs(vb[m] - target[m]) for m in range(7)) < 1e-7
    )
    report(
        "C6-break-coefficient-solution-not-value",
        ok,
        f"[g^2]Sigma_3 rel {rel(Sb[3][2], allS[3][2]):.1e}, g^6 diff {abs(vb[6] - target[6]):.1e}",
    )
    # The collapse coefficient 1/n! of the diagonal rule: halving it breaks g^6.
    Wh = dict(Wd)

    def mismatch_half(p):
        aS = solve_series(p, 3, True, Wd, 6)
        return vdiag(VN[8], p) - fact(8) / 2 * value_series(p, aS, 3, True, Wd, 6)[6]

    Wh[8] = even_form(fit_polarize(mismatch_half, 8), 4)
    vh = value_series(psi, solve_series(psi, 4, False, Wh, 6), 4, False, Wh, 6)
    ok = (
        all(abs(vh[m] - target[m]) < 1e-7 for m in range(6))
        and abs(vh[6] - target[6]) > 1e-6
    )
    report("C6-break-diagonal-rule", ok, f"g^6 diff {abs(vh[6] - target[6]):.1e}")


def main() -> int:
    print(f"seed = {SEED}, N = {N}, dims = {dict((k, DIM[k]) for k in range(1, 5))}")
    part_A()
    part_B()
    print(f"summary: {len(failures)} failures" + (f": {failures}" if failures else ""))
    return len(failures)


if __name__ == "__main__":
    sys.exit(main())
