"""Verify record 028 (agent/derivations/028-reality-tower.md): reality of the auxiliary tower.

Finite-dimensional toy: H_0 = C^N with an antilinear involution  x^‡ = J conj(x), J a real
orthogonal involution (so ‡ is not plain conjugation and the ‡-real subspace is not the
coordinate one). "Real" (‡-equivariant) symmetric tensors V_n satisfy
V_n(x_1^‡..x_n^‡) = conj V_n(x_1..x_n); the pairing is omega_1(x,y) = x^T y (bilinear, real).

Verified:
  part 1 (tower, record §2): the Jacobi-form tower action with generic real parents
    T_4..T_7 is real off-shell for ‡-real (Psi, Sigma_2, Sigma_3); the saddle Sigma* is ‡-real,
    also for a degenerate kinetic form (minimum-norm class representative); break legs: a
    non-equivariant component in T_5, and a relative phase Sigma_2 -> i Sigma_2.
  part 2 (chi, record §3): S_chi real for chi ‡-real with real (a,b); chi^‡ = -chi with real
    (a,b) is NOT real (coupling imaginary); chi^‡ = -chi with imaginary b IS real and equals the
    real-field theory with kinetic sign flipped, the ratio b^2/a invariant; on-shell chi* real.
  part 3 (multipliers, record §4): omega_k(lambda, C) real for all ‡-real C iff lambda ‡-real
    (componentwise convention), k = 1, 2, 3; break leg with a ‡-imaginary lambda.
  part 4 (record 039, agent/derivations/039-reality-ogs3.md): the O(g_s^3) statement, in two
    sectors. INVERTIBLE sector (ker V_4 = 0): p22, p32 ‡-real operators (C2.1); the composites
    P = p22^{-1}p32 and R = K_Psi^{-1}p22 of the record's eqs. (1.7)/(1.8) ‡-real, through their
    characterising identities (C2.1-P, C2.1-R); ‡ commutes with p22^{-1} at GENERIC COMPLEX A
    (C2.3); truncated and exact (K_Psi^{-1}) saddles ‡-real and agreeing to O(g^2) by a
    Richardson ratio (C3.1, C3.2); each term of the gauge law ‡-real in both symmetrisation
    readings, as is the exact law 011 (B.9) (C4.1-C4.3). DEGENERATE sector (ker V_4 != 0 with a
    V_5 annihilating ker V_4 ⊙ H_0, i.e. the PH5/R38 condition imposed by construction, C2.R38):
    ker V_4 ‡-stable (C2.2); the genuine class statements on W_q = Sym^2/ker V_4 — ‡ well posed
    on classes and the commutation holding mod ker and NOT as a vector identity (C2.3-quotient),
    P ‡-real as a class (C2.1-P-deg), both saddles (C3.1-deg, C3.2-deg) and the gauge law with
    term (c) independent of the representative of Sigma_2 (C4.1-deg).
  Break legs (10): non-equivariant V_4 (non-real p22; non-‡-stable kernel; ‡ ill defined on
    classes), non-equivariant V_5 (non-real P; non-real exact saddle), complex rescaling of p22,
    complex 1/5 and 3/5 (weak: these test only that the reality test detects an i), ‡-non-real
    Psi / delta-Psi / variation direction (substantive: they test the dependence on A4), and
    break-R38 (without V_5(ker V_4,.,.) = 0 the O(g^3) objects do NOT descend to W_q).
  part 5 (Step 2.1, record 028): the untested polarisation step itself. A real ‡-equivariant
    ground-truth symmetric tensor C generates a polynomial A(Psi) = C(Psi^{⊗6}); the finite-
    difference polarisation formula Pol(A)(v_1..v_6) = (1/6!) sum_S (-1)^{6-|S|} A(sum_{i in S} v_i)
    reconstructs T_6 = -6! Pol(A) from scalar evaluations of A alone (never touching C): T_6 is
    ‡-real and symmetric, reconstructs -6! C exactly, satisfies the diagonal identity
    T_6(Psi^{⊗6}) = -6! A(Psi) at a random point off the construction grid, and is ‡-equivariant
    at complex arguments; break legs: a complex perturbation of one coefficient of A breaks both
    reality and equivariance of T_6, a wrong normalisation (n-1)! breaks the diagonal identity.
NOT verified: the CFT hypothesis (H_R) (reality of the worldsheet vertices); PH1/PH2 (the
level-truncation invertibility package); PH7, the ‡-square on Grassmann-odd states, and the
reversal-sign convention for odd strands — the toy has NO Grassmann layer and no ghost grading,
so p22's +2 ghost shift and its odd-strand target are invisible in it, and none of the three
odd-sector questions of the record can fail here. The toy is a faithful representation of the
UNGRADED linear algebra of the record's clauses and of nothing more.

Run: .venv/bin/python codes/verify-reality-tower.py
"""
import itertools
import math
import os
import sys

import numpy as np

# Default seed of the original run; a second seed is available for a re-run without replacing it:
#     VERIFY_SEED=20260922 .venv/bin/python codes/verify-reality-tower.py
SEED = int(os.environ.get("VERIFY_SEED", 20260914))
rng = np.random.default_rng(SEED)
RESULTS = []
TOL = 1e-10
N = 3  # dim H_0


def check(name, ok):
    RESULTS.append((name, bool(ok)))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")


# ---------------------------------------------------------------- involution and reality
# J: real orthogonal involution, not the identity (a reflection in a random real plane).
_v = rng.normal(size=N)
_v /= np.linalg.norm(_v)
J = np.eye(N) - 2 * np.outer(_v, _v)
assert np.allclose(J @ J, np.eye(N)) and np.allclose(J, J.T)


def Jk(k):
    M = np.array([[1.0]])
    for _ in range(k):
        M = np.kron(M, J)
    return M


def dag(x):
    """‡ on H^{⊗k}, componentwise: J^{⊗k} conj(x). x is a flat vector of length N^k."""
    k = round(math.log(x.size, N))
    return Jk(k) @ np.conj(x)


def is_real(x, tol=TOL):
    return np.linalg.norm(dag(x) - x) < tol * max(1.0, np.linalg.norm(x))


def real_vec(k):
    """Random ‡-real vector in H^{⊗k}."""
    y = rng.normal(size=N**k) + 1j * rng.normal(size=N**k)
    return 0.5 * (y + dag(y))


def sym_basis(k):
    """Orthonormal real basis (columns) of Sym^k H inside H^{⊗k}; J^{⊗k}-stable."""
    idx = list(itertools.product(range(N), repeat=k))
    seen = {}
    cols = []
    for t in idx:
        key = tuple(sorted(t))
        if key in seen:
            continue
        seen[key] = True
        v = np.zeros(N**k)
        for p in set(itertools.permutations(t)):
            v[np.ravel_multi_index(p, (N,) * k)] = 1.0
        cols.append(v / np.linalg.norm(v))
    return np.array(cols).T


def real_sym_tensor(n):
    """Random symmetric tensor of order n, ‡-equivariant: conj(T) = J^{⊗n} T (flat)."""
    T = rng.normal(size=(N,) * n) + 1j * rng.normal(size=(N,) * n)
    S = np.zeros_like(T)
    for p in itertools.permutations(range(n)):
        S += np.transpose(T, p)
    S /= math.factorial(n)
    flat = S.reshape(-1)
    flat = 0.5 * (flat + Jk(n) @ np.conj(flat))
    return flat.reshape((N,) * n)


def contract(T, *vecs):
    """Contract the first len(vecs) legs of T with flat vectors (each of length N^k_i)."""
    out = T
    for v in vecs:
        k = round(math.log(v.size, N))
        out = np.tensordot(out, v.reshape((N,) * k), axes=(list(range(k)), list(range(k))))
    return out


def form_matrix(T, ka, kb, *fixed):
    """Matrix of the bilinear form (x,y) -> T(x, y, fixed...) with x in H^{⊗ka}, y in H^{⊗kb}."""
    R = contract(np.moveaxis(T, list(range(ka + kb, T.ndim)), list(range(T.ndim - ka - kb))), *fixed) \
        if fixed else T
    return R.reshape(N**ka, N**kb)


# ---------------------------------------------------------------- part 1: the tower
def part1():
    T4, T5, T6, T7 = (real_sym_tensor(n) for n in (4, 5, 6, 7))
    # 1.1 equivariance of the constructed tensors (falsifiable: fails for a generic complex T)
    x = [rng.normal(size=N) + 1j * rng.normal(size=N) for _ in range(5)]
    lhs = contract(T5, *x)
    rhs = np.conj(contract(T5, *[dag(xi) for xi in x]))
    check("1.1 constructed V_5 is ‡-equivariant at a random complex point", abs(lhs - rhs) < TOL)
    Tbad = rng.normal(size=(N,) * 5) + 1j * rng.normal(size=(N,) * 5)
    check("1.1b break: a generic complex tensor is NOT equivariant",
          abs(contract(Tbad, *x) - np.conj(contract(Tbad, *[dag(xi) for xi in x]))) > 1e-3)

    B2, B3 = sym_basis(2), sym_basis(3)

    def tower(Psi, T5_=T5, g=0.37):
        """Return (A, b, S) for S(s) = -s^T A s + 2 b^T s in Sym^2 ⊕ Sym^3 coordinates."""
        a2, a3 = g**2 / 24, g**4 / 720
        PP = np.kron(Psi, Psi)
        M2 = B2.T @ form_matrix(T4, 2, 2) @ B2
        M3 = B3.T @ form_matrix(T6, 3, 3) @ B3
        C5 = B2.T @ form_matrix(T5_, 2, 2, Psi) @ B2          # T5(., ., Psi)
        C7 = B3.T @ form_matrix(T7, 3, 3, Psi) @ B3
        L3 = B3.T @ form_matrix(T6, 3, 2, Psi) @ B2            # T6(., ., Psi): Sym^2 -> Sym^3
        u2 = B2.T @ (form_matrix(T4, 2, 2) @ PP)
        H2 = M2 - g / 5 * C5
        H3 = M3 - g / 7 * C7
        A = np.block([[a2 * H2, -a3 * L3.T], [-a3 * L3, a3 * H3]])
        b = np.concatenate([a2 * u2, np.zeros(B3.shape[1])])

        def S(s2, s3):
            s = np.concatenate([s2, s3])
            return -s @ A @ s + 2 * b @ s

        return A, b, S

    Psi = real_vec(1)
    A, b, S = tower(Psi)
    s2 = B2.T @ real_vec(2)
    s3 = B3.T @ real_vec(3)
    # coordinates of a ‡-real symmetric tensor: B real & J-stable -> the tensor B s is real
    check("1.2 tower action real off-shell at ‡-real (Psi, Sigma_2, Sigma_3), real g",
          abs(S(s2, s3).imag) < TOL and abs(S(s2, s3).real) > 1e-6)
    s = np.linalg.solve(A, b)
    d2 = B2.shape[1]
    check("1.3 saddle Sigma_2*, Sigma_3* are ‡-real",
          is_real(B2 @ s[:d2]) and is_real(B3 @ s[d2:]))
    check("1.3b on-shell action value real", abs(S(s[:d2], s[d2:]).imag) < TOL)
    # 1.4 degenerate kinetic form: project T4 onto a ‡-stable hyperplane of Sym^2 ⊕ Sym^3
    #   by killing one ‡-real direction of A (rank drop), source in the image.
    w = np.concatenate([B2.T @ real_vec(2), B3.T @ real_vec(3)])
    # omega-orthogonal projector (bilinear, not Hermitian): omega(w,w) is real for real w, so Pw is real
    Pw = np.eye(A.shape[0]) - np.outer(w, w) / (w @ w)
    Adeg = Pw @ A @ Pw
    bdeg = Adeg @ np.concatenate([s2, s3])            # some real preimage exists
    sdeg = np.linalg.lstsq(Adeg, bdeg, rcond=None)[0]
    check("1.4 degenerate kernel: minimum-norm saddle solves the system and is ‡-real",
          np.linalg.norm(Adeg @ sdeg - bdeg) < 1e-8 * np.linalg.norm(bdeg)
          and is_real(B2 @ sdeg[:d2], 1e-8) and is_real(B3 @ sdeg[d2:], 1e-8)
          and np.linalg.matrix_rank(Adeg) == A.shape[0] - 1)
    check("1.4b degenerate kernel is ‡-stable (kernel vector w is ‡-real up to scale)",
          is_real(B2 @ w[:d2], 1e-8) and is_real(B3 @ w[d2:], 1e-8)
          and np.linalg.norm(Adeg @ w) < 1e-10)
    # 1.5 break: non-equivariant component in T5 -> action and saddle non-real
    T5bad = T5 + 1j * np.real(real_sym_tensor(5))
    Ab, bb, Sb = tower(Psi, T5_=T5bad)
    sb = np.linalg.solve(Ab, bb)
    check("1.5 break: non-real V_5 component -> action non-real and saddle non-real",
          abs(Sb(s2, s3).imag) > 1e-6 and not is_real(B2 @ sb[:d2]))
    # 1.6 break: relative phase Sigma_2 -> i Sigma_2 (Sigma_2^‡ = -Sigma_2) -> source imaginary
    check("1.6 break: Sigma_2 -> i Sigma_2 makes the action non-real (source term)",
          abs(S(1j * s2, s3).imag) > 1e-6)
    return T4, T5


# ---------------------------------------------------------------- part 2: chi
def part2(T4, T5):
    g = 0.37
    Psi, Sig, chi = real_vec(1), real_vec(2), real_vec(2)
    B2 = sym_basis(2)
    Sig, chi = B2 @ (B2.T @ Sig), B2 @ (B2.T @ chi)  # symmetric parts (still ‡-real)
    V4 = B2.T @ form_matrix(T4, 2, 2) @ B2          # kinetic form on Sym^2 (non-degenerate there)
    v = B2.T @ (form_matrix(T5, 2, 2, Psi) @ Sig)   # v = T5(., Sigma, Psi) restricted to Sym^2
    chi = B2.T @ chi

    def Schi(chi, a, b):
        return g**2 / 24 * a * (chi @ V4 @ chi) + g**3 / 120 * b * (chi @ v)

    check("2.1 S_chi real for chi ‡-real, (a,b) = (1,2) real",
          abs(Schi(chi, 1, 2).imag) < TOL and abs(Schi(chi, 1, 2).real) > 1e-8)
    check("2.2 chi^‡ = -chi with real (a,b): kinetic real, coupling imaginary -> S_chi NOT real",
          abs((1j * chi) @ V4 @ (1j * chi) - (-(chi @ V4 @ chi))) < TOL
          and abs(Schi(1j * chi, 1, 2).imag) > 1e-8)
    # 2.3 chi^‡ = -chi with imaginary b is the real-field theory with flipped kinetic sign
    a, b = 1.0, 2j
    check("2.3 chi^‡ = -chi, b imaginary: real, equals real-field theory with (a_r,b_r)=(-a, ib); b^2/a invariant",
          abs(Schi(1j * chi, a, b).imag) < TOL
          and abs(Schi(1j * chi, a, b) - Schi(chi, -a, 1j * b)) < TOL
          and abs((1j * b)**2 / (-a) - b**2 / a) < TOL)
    # 2.4 on-shell chi* = -(g/10)(b/a) V4^{-1} v is ‡-real for real (a,b)
    chistar = -(g / 10) * (2 / 1) * np.linalg.solve(V4, v)
    check("2.4 on-shell chi* ‡-real for real (a,b)", is_real(B2 @ chistar))
    check("2.4b break: chi* with imaginary b is ‡-imaginary, not ‡-real",
          not is_real(B2 @ (1j * chistar)) and is_real(B2 @ (1j * 1j * chistar)))
    # 2.5 stationarity of Schi at chistar (falsifiable: derivative vanishes)
    grad = g**2 / 12 * V4 @ chistar + g**3 / 120 * 2 * v
    check("2.5 chi* is the stationary point of S_chi", np.linalg.norm(grad) < 1e-10)


# ---------------------------------------------------------------- part 3: multipliers
def part3():
    for k in (1, 2, 3):
        lam = real_vec(k)
        Cs = [real_vec(k) for _ in range(N**k)]
        ok_real = all(abs(lam @ C).imag < TOL for C in Cs)
        lam_bad = lam + 1j * real_vec(k)                      # ‡-imaginary part added
        ok_break = any(abs((lam_bad @ C).imag) > 1e-8 for C in Cs)
        # uniqueness: the set {lambda: Im omega(lambda, C) = 0 for all real C} is exactly the
        # ‡-real subspace (dimension N^k over R): rank of the real-linear map lam -> Im(lam . C_j)
        # over a real basis of ‡-real C's, acting on lam in R^{2 N^k} (Re, Im coordinates)
        Bk = np.array([0.5 * (e + dag(e)) for e in np.eye(N**k)]
                      + [0.5 * (1j * e + dag(1j * e)) for e in np.eye(N**k)])  # spans the ‡-real subspace
        rows = []
        for C in Bk:
            # Im((x + i y) . C) = x . Im C + y . Re C
            rows.append(np.concatenate([C.imag, C.real]))
        rank = np.linalg.matrix_rank(np.array(rows), tol=1e-10)
        check(f"3.{k} k={k}: omega_k(lambda, C) real for all ‡-real C iff lambda ‡-real "
              f"(real: {ok_real}; break: {ok_break}; solution space dim = {2*N**k - rank} = {N**k})",
              ok_real and ok_break and rank == N**k)


# ---------------------------------------------------------------- part 4: O(g_s^3) reality
def part4():
    """Record 039: reality of Sigma_2 at O(g_s^3) — clauses C2 (inverse), C3 (saddle), C4 (gauge law).

    Notation (project): V_4(A,B) = <A, p22 B>, V_5(A,C) = <A, p32 C> with A,B in Sym^2 H_0,
    C in Sym^3 H_0 and <.,.> = omega_1^{⊗2}. Dressed kernel K_Psi = p22 - (g/5) V_5(.,.,Psi).

    Two sectors are run:
      (a) the INVERTIBLE sector (ker V_4 = 0), which is the toy's default;
      (b) the DEGENERATE sector (ker V_4 != 0) built with a V_5 that annihilates ker V_4 —
          the condition PH5/R38 of the ledger's 2026-09-19 annotation, without which the
          O(g_s^3) objects do not descend to Sym^2/ker V_4 at all.
    Sector (b) is what the first run of this part never exercised (the documented trap of the
    R17 annotation: "every O(g_s^{>=3}) toy with a generic invertible V_4 never saw this").
    """
    g = 0.37
    T4, T5 = real_sym_tensor(4), real_sym_tensor(5)
    B2, B3 = sym_basis(2), sym_basis(3)
    # ‡ in Sym^k coordinates: x -> Jt_k conj(x); Jt_k is real orthogonal and involutive.
    Jt2, Jt3 = B2.T @ Jk(2) @ B2, B3.T @ Jk(3) @ B3

    def dag2(x):
        return Jt2 @ np.conj(x)

    def dag3(x):
        return Jt3 @ np.conj(x)

    def real2(x, tol=1e-9):
        return np.linalg.norm(dag2(x) - x) < tol * max(1.0, np.linalg.norm(x))

    def to2(v):  # H^{⊗2} -> Sym^2 coordinates
        return B2.T @ v

    def to3(v):
        return B3.T @ v

    p22 = to2(form_matrix(T4, 2, 2) @ B2)          # Sym^2 -> Sym^2
    p32 = to2(form_matrix(T5, 2, 3) @ B3)          # Sym^3 -> Sym^2
    n2 = B2.shape[1]

    def odot_map(psi):
        """Matrix of B -> psi ⊙ B, Sym^2 -> Sym^3 (used to build V_5(.,.,psi) = p32 @ odot)."""
        return np.column_stack([to3(np.kron(B2[:, j], psi)) for j in range(n2)])

    # ---- C2.1: p22 and p32 are real operators:  p Jt = Jt conj(p)  (the remark C2.5 route,
    # which in the graded theory needs the odd-strand ‡ convention and PH7; kept because the
    # toy is ungraded and it is the cheapest transcription check of PH6 -> real operator).
    e22 = np.linalg.norm(p22 @ Jt2 - Jt2 @ np.conj(p22))
    e32 = np.linalg.norm(p32 @ Jt3 - Jt2 @ np.conj(p32))
    check(f"C2.1 p22, p32 are ‡-real operators (||p J - J conj p|| = {e22:.2e}, {e32:.2e})",
          e22 < TOL and e32 < TOL)
    T4bad = T4 + 1j * np.real(real_sym_tensor(4))
    p22bad = to2(form_matrix(T4bad, 2, 2) @ B2)
    check("break-C2.1 a non-equivariant V_4 gives a NON-real p22",
          np.linalg.norm(p22bad @ Jt2 - Jt2 @ np.conj(p22bad)) > 1e-3)

    # ---- C2.1-P / C2.1-R: the composites of eq. (1.7)/(1.8), which is the route the record
    # actually takes.  Tested through their CHARACTERISING identities
    #   V_4(A, P C) = V_5(A, C)        and     V_4^Psi(A, R B) = V_4(A, B),
    # i.e. never conjugating an odd-strand object: P = p22^{-1} p32, R = K_Psi^{-1} p22.
    inv22 = np.linalg.inv(p22)
    Pcomp = inv22 @ p32                                       # Sym^3 -> Sym^2
    Cg = rng.normal(size=B3.shape[1]) + 1j * rng.normal(size=B3.shape[1])   # generic complex
    resP = np.linalg.norm(Pcomp @ dag3(Cg) - dag2(Pcomp @ Cg))
    check(f"C2.1-P composite P = p22^-1 p32 is ‡-real at generic complex C (residual {resP:.2e}; "
          f"||C^‡ - C|| = {np.linalg.norm(dag3(Cg) - Cg):.2f})",
          resP < 1e-9 * max(1.0, np.linalg.norm(Pcomp @ Cg))
          and np.linalg.norm(dag3(Cg) - Cg) > 1e-3)
    T5bad0 = T5 + 1j * np.real(real_sym_tensor(5))
    Pbad = inv22 @ to2(form_matrix(T5bad0, 2, 3) @ B3)
    check("break-C2.1-P a non-equivariant V_5 makes the composite P NON-real",
          np.linalg.norm(Pbad @ dag3(Cg) - dag2(Pbad @ Cg)) > 1e-3)

    Psi = real_vec(1)
    KPsi = p22 - g / 5 * (p32 @ odot_map(Psi))
    Rcomp = np.linalg.solve(KPsi, p22)                        # Sym^2 -> Sym^2
    Bg = rng.normal(size=n2) + 1j * rng.normal(size=n2)
    resR = np.linalg.norm(Rcomp @ dag2(Bg) - dag2(Rcomp @ Bg))
    check(f"C2.1-R composite R = K_Psi^-1 p22 is ‡-real at generic complex B (residual {resR:.2e})",
          resR < 1e-9 * max(1.0, np.linalg.norm(Rcomp @ Bg))
          and np.linalg.norm(dag2(Bg) - Bg) > 1e-3)
    check("break-C2.1-R a non-‡-real Psi in the dressing makes R NON-real",
          np.linalg.norm(
              (lambda Rb: Rb @ dag2(Bg) - dag2(Rb @ Bg))(
                  np.linalg.solve(p22 - g / 5 * (p32 @ odot_map(Psi + 0.7j * real_vec(1))), p22))
          ) > 1e-3)

    # ---- C2.2: ker V_4 = ker p22 is ‡-stable (eq. (1.5)).  Degenerate p22 by projecting out a
    # ‡-real direction w (omega-orthogonal projector, so the degenerate form stays equivariant).
    y = rng.normal(size=n2) + 1j * rng.normal(size=n2)
    w = 0.5 * (y + dag2(y))
    Pw = np.eye(n2) - np.outer(w, w) / (w @ w)
    p22deg = Pw @ p22 @ Pw
    _, s, Vh = np.linalg.svd(p22deg)
    null = Vh[s < 1e-9 * s[0]].conj().T          # columns span ker p22deg (orthonormal)
    stable = all(np.linalg.norm(p22deg @ dag2(null[:, j])) < 1e-9 for j in range(null.shape[1]))
    check(f"C2.2 ker V_4 (dim {null.shape[1]}) is ‡-stable for an equivariant degenerate V_4",
          null.shape[1] >= 1 and stable)
    # break: degenerate along a NON-‡-real direction -> the form is not equivariant and the kernel
    # is not ‡-stable.
    wb = y
    Pwb = np.eye(n2) - np.outer(wb, wb) / (wb @ wb)
    p22degb = Pwb @ p22 @ Pwb
    check("break-C2.2 a non-equivariant degenerate V_4 has a NON-‡-stable kernel",
          np.linalg.norm(p22degb @ dag2(wb)) > 1e-3 * np.linalg.norm(p22degb) * np.linalg.norm(wb))

    # class machinery on W_q = Sym^2 / ker p22deg
    Pker = null @ null.conj().T                  # Hermitian projector onto ker
    Pout = np.eye(n2) - Pker

    def same_class(x, z, tol=1e-8):
        """x = z in Sym^2/ker p22deg ?"""
        return np.linalg.norm(Pout @ (x - z)) < tol * max(1.0, np.linalg.norm(x))

    def real_cls(x, tol=1e-8):
        return same_class(dag2(x), x, tol)

    # ---- C2.3: ‡ commutes with p22^{-1} (eq. (1.6)), tested at GENERIC COMPLEX A (at ‡-real A
    # both sides coincide trivially and the check would be vacuous).
    e_inv = np.linalg.norm(inv22 @ Jt2 - Jt2 @ np.conj(inv22))
    A = rng.normal(size=n2) + 1j * rng.normal(size=n2)
    e_pt = np.linalg.norm(dag2(inv22 @ A) - inv22 @ dag2(A))
    check(f"C2.3 (p22^-1 A)^‡ = p22^-1(A^‡) at generic complex A (residual {e_pt:.2e})",
          e_inv < 1e-9 and e_pt < 1e-9 and np.linalg.norm(dag2(A) - A) > 1e-3)
    p22c = np.exp(0.3j) * p22
    check("break-C2.3 a complex rescaling of p22 breaks the commutation",
          np.linalg.norm(np.linalg.inv(p22c) @ Jt2 - Jt2 @ np.conj(np.linalg.inv(p22c))) > 1e-3)

    # ---- C2.3-quotient: the genuine CLASS statement on W_q, in two parts.
    #   (i) well-posedness: two representatives differing by a kernel element have ‡-images in
    #       the SAME class (this is eq. (1.5) doing its work, not the operator reality of p22);
    #  (ii) the commutation holds MODULO the kernel and NOT as a vector identity — the residual
    #       lies in ker and is nonzero, so the statement is genuinely about classes.
    kap = null @ (rng.normal(size=null.shape[1]) + 1j * rng.normal(size=null.shape[1]))
    Xc = np.linalg.pinv(p22deg) @ (p22deg @ A)
    wellposed = (same_class(dag2(Xc + kap), dag2(Xc))
                 and np.linalg.norm(dag2(Xc + kap) - dag2(Xc)) > 1e-3)
    diff = np.linalg.pinv(p22deg) @ dag2(p22deg @ A) - dag2(np.linalg.pinv(p22deg) @ (p22deg @ A))
    in_ker = np.linalg.norm(Pout @ diff) < 1e-8 * max(1.0, np.linalg.norm(diff))
    check(f"C2.3-quotient class statement on Sym^2/ker V_4: ‡ well posed on classes "
          f"(||‡(X+k) - ‡X|| = {np.linalg.norm(dag2(Xc + kap) - dag2(Xc)):.2f}) and the "
          f"commutation holds mod ker (out-of-ker part {np.linalg.norm(Pout @ diff):.2e}, "
          f"in-ker part {np.linalg.norm(Pker @ diff):.2e})",
          wellposed and in_ker)
    # break: with the NON-equivariant degenerate V_4 the kernel is not ‡-stable, so ‡ is not even
    # well defined on classes and the commutation residual leaves the kernel.
    _, sb, Vhb = np.linalg.svd(p22degb)
    nullb = Vhb[sb < 1e-9 * sb[0]].conj().T
    Poutb = np.eye(n2) - nullb @ nullb.conj().T
    kapb = nullb @ (rng.normal(size=nullb.shape[1]) + 1j * rng.normal(size=nullb.shape[1]))
    Xb = np.linalg.pinv(p22degb) @ (p22degb @ A)
    check("break-C2.3-quotient a non-‡-stable kernel makes ‡ ILL defined on classes",
          np.linalg.norm(Poutb @ (dag2(Xb + kapb) - dag2(Xb))) > 1e-3)

    # ---- the PH5/R38 sector: a degenerate V_4 together with a V_5 annihilating ker V_4.
    # Project Sym^3 along the ‡-stable subspace ker ⊙ H_0 with the omega-orthogonal projector
    # (bilinear, so equivariance is preserved), then p32r := p32 @ Q kills ker ⊙ H_0.
    cols = [to3(np.kron(B2 @ null[:, j], np.eye(N)[:, i]))
            for j in range(null.shape[1]) for i in range(N)]
    Vsub = np.column_stack(cols)
    Q = np.eye(B3.shape[1]) - Vsub @ np.linalg.solve(Vsub.T @ Vsub, Vsub.T)
    p32r = p32 @ Q
    r38 = max(np.linalg.norm(p32r @ Vsub[:, c]) for c in range(Vsub.shape[1]))
    r38_bad = max(np.linalg.norm(p32 @ Vsub[:, c]) for c in range(Vsub.shape[1]))
    check(f"C2.R38 the constructed V_5 annihilates ker V_4 ⊙ H_0 (max ||p32r(k⊙e)|| = {r38:.2e}) "
          f"and stays ‡-equivariant",
          r38 < 1e-9 and np.linalg.norm(p32r @ Jt3 - Jt2 @ np.conj(p32r)) < 1e-9)
    check(f"break-R38 WITHOUT the condition the O(g^3) objects do NOT descend to W_q "
          f"(max ||p32(k⊙e)|| = {r38_bad:.2e}; class of P(k⊙e) nonzero: "
          f"{np.linalg.norm(Pout @ (np.linalg.pinv(p22deg) @ (p32 @ Vsub[:, 0]))):.2e})",
          r38_bad > 1e-3
          and np.linalg.norm(Pout @ (np.linalg.pinv(p22deg) @ (p32 @ Vsub[:, 0]))) > 1e-6)

    Pdeg = np.linalg.pinv(p22deg) @ p32r                      # P on the quotient
    check(f"C2.1-P-deg the composite P is ‡-real AS A CLASS on W_q with ker V_4 != 0 "
          f"(out-of-ker residual "
          f"{np.linalg.norm(Pout @ (Pdeg @ dag3(Cg) - dag2(Pdeg @ Cg))):.2e})",
          np.linalg.norm(Pout @ (Pdeg @ dag3(Cg) - dag2(Pdeg @ Cg)))
          < 1e-8 * max(1.0, np.linalg.norm(Pdeg @ Cg)))

    # ---- C3: the corrected saddle
    PP2 = to2(np.kron(Psi, Psi))
    PP3 = to3(np.kron(np.kron(Psi, Psi), Psi))

    def sigma_trunc(c=0.2):
        """Psi^{⊗2} + c g p22^{-1} p32(Psi^{⊗3}); c = 1/5 is the derived coefficient."""
        return PP2 + c * g * (inv22 @ (p32 @ PP3))

    check("C3.1 truncated saddle Sigma_2* = Psi^2 + (g/5) p22^-1 p32(Psi^3) is ‡-real",
          real2(sigma_trunc()) and np.linalg.norm(sigma_trunc() - PP2) > 1e-6)
    check("break-C3.1 a complex coefficient (1/5 -> i/5) makes the truncated saddle non-real",
          not real2(sigma_trunc(c=0.2j)))
    # stronger leg: the reality of the saddle is a statement about REAL data (A4), not only
    # about the coefficient — a ‡-non-real Psi must break it.
    Psi_bad = Psi + 0.6j * real_vec(1)
    check("break-C3.1b a ‡-non-real Psi makes the truncated saddle non-real (reality uses A4, "
          "not only the rationality of 1/5)",
          not real2(to2(np.kron(Psi_bad, Psi_bad))
                    + 0.2 * g * (inv22 @ (p32 @ to3(np.kron(np.kron(Psi_bad, Psi_bad), Psi_bad))))))

    def K_of(gs, Psi_=Psi, T5_=T5):
        W = to2(form_matrix(T5_, 2, 2, Psi_) @ B2)     # V_5(.,.,Psi): Sym^2 -> Sym^2
        return p22 - gs / 5 * W

    def sigma_exact(gs, Psi_=Psi, T5_=T5):
        return np.linalg.solve(K_of(gs, Psi_, T5_), p22 @ to2(np.kron(Psi_, Psi_)))

    se = sigma_exact(g)
    # Richardson ratio, taken at a small g where the O(g^3) remainder is negligible: the
    # deviation of the exact saddle from the O(g) truncation must scale as g^2.
    gr = 0.05
    d1 = np.linalg.norm(sigma_exact(gr) - (PP2 + 0.2 * gr * (inv22 @ (p32 @ PP3))))
    d2h = np.linalg.norm(sigma_exact(gr / 2) - (PP2 + 0.2 * (gr / 2) * (inv22 @ (p32 @ PP3))))
    check(f"C3.2 exact saddle K_Psi^-1 p22 Psi^2 is ‡-real, and agrees with the truncation to "
          f"O(g^2) (Richardson ratio {d1 / d2h:.2f} ~ 4 at g = {gr})",
          real2(se) and abs(d1 / d2h - 4.0) < 0.3 and d1 > 1e-8)
    T5bad = T5 + 1j * np.real(real_sym_tensor(5))
    check("break-C3.2 a non-equivariant V_5 makes the exact saddle non-real",
          not real2(sigma_exact(g, T5_=T5bad)))
    # break-C3.2b: the ratio half of C3.2 had no break leg (only reality was perturbed above).
    # Perturb the truncation coefficient 1/5 -> 0.25 (exact saddle sigma_exact unchanged), so the
    # deviation from the exact saddle is O(g) instead of O(g^2) and the Richardson ratio moves
    # away from 4, failing |r-4|<0.3.
    d1_wc = np.linalg.norm(sigma_exact(gr) - (PP2 + 0.25 * gr * (inv22 @ (p32 @ PP3))))
    d2h_wc = np.linalg.norm(sigma_exact(gr / 2) - (PP2 + 0.25 * (gr / 2) * (inv22 @ (p32 @ PP3))))
    check(f"break-C3.2b a wrong coefficient (1/5 -> 0.25) in the truncation makes the Richardson "
          f"ratio fail |r-4|<0.3 (r = {d1_wc / d2h_wc:.2f})",
          abs(d1_wc / d2h_wc - 4.0) > 0.3)

    # ---- clauses 2 and 3 re-run in the DEGENERATE sector (ker V_4 != 0, PH5/R38 imposed).
    sig_tr_deg = PP2 + 0.2 * g * (Pdeg @ PP3)
    check(f"C3.1-deg truncated saddle is ‡-real AS A CLASS with ker V_4 != 0 "
          f"(out-of-ker residual {np.linalg.norm(Pout @ (dag2(sig_tr_deg) - sig_tr_deg)):.2e}, "
          f"||‡S - S|| = {np.linalg.norm(dag2(sig_tr_deg) - sig_tr_deg):.2e})",
          real_cls(sig_tr_deg) and np.linalg.norm(Pout @ (sig_tr_deg - PP2)) > 1e-6)

    Wdeg = p32r @ odot_map(Psi)                       # V_5(.,.,Psi) with the R38 condition
    Kdeg = p22deg - g / 5 * Wdeg
    sig_ex_deg = np.linalg.pinv(Kdeg) @ (p22deg @ PP2)
    sig_ex_deg_r = np.linalg.pinv(p22deg - gr / 5 * Wdeg) @ (p22deg @ PP2)
    d1d = np.linalg.norm(Pout @ (sig_ex_deg_r - (PP2 + 0.2 * gr * (Pdeg @ PP3))))
    sig_ex_deg_h = np.linalg.pinv(p22deg - (gr / 2) / 5 * Wdeg) @ (p22deg @ PP2)
    d2d = np.linalg.norm(Pout @ (sig_ex_deg_h - (PP2 + 0.2 * (gr / 2) * (Pdeg @ PP3))))
    check(f"C3.2-deg exact saddle K_Psi^-1 p22 Psi^2 is ‡-real AS A CLASS with ker V_4 != 0, and "
          f"agrees with the truncation to O(g^2) (Richardson ratio {d1d / d2d:.2f} ~ 4)",
          real_cls(sig_ex_deg) and abs(d1d / d2d - 4.0) < 0.3 and d1d > 1e-10)

    # ---- C4: the gauge law
    dPsi = real_vec(1)
    Sig = 0.5 * (to2(real_vec(2)) + dag2(to2(real_vec(2))))   # a ‡-real element of Sym^2
    Sig = 0.5 * (Sig + dag2(Sig))
    X = Sig - PP2

    a_sym = to2(np.kron(dPsi, Psi) + np.kron(Psi, dPsi))
    a_unsym = 2 * np.kron(dPsi, Psi)                          # in H^{⊗2}, not in Sym^2

    def term_b(c=0.6):
        return c * g * (inv22 @ (p32 @ to3(np.kron(np.kron(dPsi, Psi), Psi))))

    term_c = 0.1 * g * (inv22 @ (p32 @ to3(np.kron(B2 @ X, dPsi))))
    check("C4.1 each term of the O(g_s^3) gauge law is separately ‡-real",
          real2(a_sym) and real2(term_b()) and real2(term_c)
          and min(np.linalg.norm(t) for t in (a_sym, term_b(), term_c)) > 1e-8)
    check("break-C4.1 a complex coefficient (3/5 -> 3i/5) makes the law non-real",
          not real2(term_b(c=0.6j)))
    check("break-C4.1b a ‡-non-real delta-Psi makes the law non-real (reality uses A4, not only "
          "the rationality of 3/5)",
          not real2(0.6 * g * (inv22 @ (p32 @ to3(
              np.kron(np.kron(dPsi + 0.5j * real_vec(1), Psi), Psi))))))
    check("C4.2 both symmetrisation readings of 2 dPsi⊗Psi are ‡-real and agree inside Sym^2",
          is_real(a_unsym) and real2(a_sym)
          and np.linalg.norm(to2(a_unsym) - a_sym) < 1e-10 * np.linalg.norm(a_sym))

    # clause 3 in the degenerate sector: term (c) is the one that needs PH5/R38, because
    # Sigma_2 - Psi^{⊗2} is only a CLASS.
    Xd = Sig + null @ (rng.normal(size=null.shape[1])
                       + 1j * rng.normal(size=null.shape[1])) - PP2   # another representative
    term_b_deg = 0.6 * g * (Pdeg @ to3(np.kron(np.kron(dPsi, Psi), Psi)))
    term_c_deg = 0.1 * g * (Pdeg @ to3(np.kron(B2 @ (Sig - PP2), dPsi)))
    term_c_deg2 = 0.1 * g * (Pdeg @ to3(np.kron(B2 @ Xd, dPsi)))
    check(f"C4.1-deg each term of the gauge law is ‡-real AS A CLASS with ker V_4 != 0, and "
          f"term (c) is independent of the representative of Sigma_2 "
          f"(||X' - X|| = {np.linalg.norm(Xd - (Sig - PP2)):.2f})",
          real_cls(a_sym) and real_cls(term_b_deg) and real_cls(term_c_deg)
          and same_class(term_c_deg2, term_c_deg)
          and np.linalg.norm(Xd - (Sig - PP2)) > 1e-3
          and np.linalg.norm(Pout @ term_c_deg) > 1e-8)

    # exact law (3.6): reality of the saddle variation along a real direction + the rotation term
    eps = 1e-5
    dsig = (sigma_exact(g, Psi_=Psi + eps * dPsi) - sigma_exact(g, Psi_=Psi - eps * dPsi)) / (2 * eps)
    Xt = Sig - se
    rot = 0.1 * g * (np.linalg.solve(K_of(g), p32 @ to3(np.kron(B2 @ Xt, dPsi))))
    check("C4.3 exact law (011 B.9): saddle variation and rotation term are both ‡-real",
          real2(dsig, 1e-6) and real2(rot) and np.linalg.norm(rot) > 1e-8)
    check("break-C4.3 a ‡-non-real variation direction makes the saddle variation non-real",
          not real2((sigma_exact(g, Psi_=Psi + eps * 1j * dPsi)
                     - sigma_exact(g, Psi_=Psi - eps * 1j * dPsi)) / (2 * eps), 1e-6))

# ---------------------------------------------------------------- part 5: polarisation (Step 2.1)
def part5():
    """Record 028 Step 2.1: T_n = -n! Pol(A_{n-2}) for the parents at n >= 6.

    Exercises the untested step itself (rigor-audit carve-out): given a real, ‡-equivariant
    homogeneous degree-n polynomial A(Psi) = C(Psi^{⊗n}) built from a KNOWN ‡-real symmetric
    tensor C (ground truth, generated exactly as in part1's real_sym_tensor), recover the
    symmetric tensor T_n = -n! Pol(A) by the standard finite-difference polarisation formula

        Pol(A)(v_1,...,v_n) = (1/n!) sum_{S subset [n]} (-1)^{n-|S|} A(sum_{i in S} v_i),

    using ONLY scalar evaluations of A (the polarisation routine never sees C directly — it is
    a black-box reconstruction, exactly the operation Step 2.1 performs on A_{n-2}). n = 6 (a
    genuine higher parent, not T_4/T_5 which are geometric by (H_R) directly).
    """
    n = 6
    Ctrue = real_sym_tensor(n)  # ground truth: ‡-real, permutation-symmetric (independent of Pol)

    def Afunc(v, C=Ctrue):
        out = v
        for _ in range(n - 1):
            out = np.multiply.outer(out, v)
        return complex(np.sum(C * out))

    def polarize(Afunc_, n_=n, N_=N):
        """Reconstruct the symmetric n-tensor T with T(x,..,x) = Afunc_(x) from scalar evals."""
        T = np.zeros((N_,) * n_, dtype=complex)
        basis = np.eye(N_)
        for idx in itertools.combinations_with_replacement(range(N_), n_):
            vecs = [basis[i] for i in idx]
            total = 0j
            for mask in range(2**n_):
                bits = [(mask >> k) & 1 for k in range(n_)]
                v = np.zeros(N_)
                for bit, vec in zip(bits, vecs):
                    if bit:
                        v = v + vec
                total += ((-1) ** (n_ - sum(bits))) * Afunc_(v)
            val = total / math.factorial(n_)
            for p in set(itertools.permutations(idx)):
                T[p] = val
        return T

    def is_symmetric(T, n_=n, tol=TOL):
        return all(np.allclose(np.transpose(T, p), T, atol=tol) for p in itertools.permutations(range(n_)))

    Tn = -math.factorial(n) * polarize(Afunc)

    # 5.1 reality of the reconstructed T_n (‡-equivariance, the content of Step 2.1's claim)
    check("5.1 T_6 = -6! Pol(A) is ‡-real (Step 2.1, parent reality)",
          is_real(Tn.reshape(-1)))
    # 5.2 symmetry of the reconstructed tensor (Pol always outputs a symmetric tensor)
    check("5.2 T_6 is a symmetric tensor (permutation-invariant)", is_symmetric(Tn))
    # 5.3 reconstruction identity: Pol recovers the ground-truth tensor exactly (-6! Ctrue)
    check(f"5.3 -6! Pol(A) reconstructs -6! C exactly (||T_6 - (-6!)C|| = "
          f"{np.linalg.norm(Tn - (-math.factorial(n) * Ctrue)):.2e})",
          np.linalg.norm(Tn - (-math.factorial(n) * Ctrue)) < 1e-8)
    # 5.4 the defining diagonal identity T_n(Psi^{⊗n}) = -n! A(Psi) at a random real Psi NOT among
    # the 0/1 basis combinations used to build T_n (genuine independent evaluation point)
    Psi = rng.normal(size=N)  # generic real point, off the 0/1 construction grid
    lhs54 = contract(Tn, *([Psi] * n))
    rhs54 = -math.factorial(n) * Afunc(Psi)
    check(f"5.4 T_6(Psi^⊗6) = -6! A(Psi) at random real Psi off the construction grid "
          f"(|lhs-rhs| = {abs(lhs54 - rhs54):.2e})",
          abs(lhs54 - rhs54) < 1e-8 * max(1.0, abs(rhs54)))
    # 5.5 equivariance at generic complex arguments (H_R's carried consequence, (1.4))
    xs = [rng.normal(size=N) + 1j * rng.normal(size=N) for _ in range(n)]
    lhs55 = contract(Tn, *xs)
    rhs55 = np.conj(contract(Tn, *[dag(xi) for xi in xs]))
    check(f"5.5 T_6 is ‡-equivariant at a random complex point (|lhs-rhs| = {abs(lhs55 - rhs55):.2e})",
          abs(lhs55 - rhs55) < TOL)

    # ---- break legs
    # break-5.1/5.5: perturb ONE coefficient of A (one permutation-symmetric orbit of C) by an
    # imaginary amount; keeps A permutation-symmetric (Pol still returns a symmetric tensor) but
    # breaks ‡-equivariance of A, hence of Pol(A).
    idx0 = tuple(int(i) for i in rng.integers(0, N, size=n))
    Cbad = Ctrue.copy()
    eps = 0.53
    for p in set(itertools.permutations(idx0)):
        Cbad[p] += 1j * eps
    Tn_bad = -math.factorial(n) * polarize(lambda v, C=Cbad: Afunc(v, C=C))
    lhs55b = contract(Tn_bad, *xs)
    rhs55b = np.conj(contract(Tn_bad, *[dag(xi) for xi in xs]))
    check(f"break-5.1/5.5 a complex perturbation of one coefficient of A makes T_6 non-real "
          f"(‖T‡-T‖ = {np.linalg.norm(dag(Tn_bad.reshape(-1)) - Tn_bad.reshape(-1)):.2e}) and "
          f"non-equivariant (|lhs-rhs| = {abs(lhs55b - rhs55b):.2e})",
          not is_real(Tn_bad.reshape(-1)) and abs(lhs55b - rhs55b) > 1e-3
          and is_symmetric(Tn_bad))
    # break-5.4: wrong normalisation (n-1)! instead of n! -> the diagonal identity fails by a
    # factor n = 6, well outside tolerance
    Tn_wrongnorm = -math.factorial(n - 1) * polarize(Afunc)
    lhs54w = contract(Tn_wrongnorm, *([Psi] * n))
    check(f"break-5.4 wrong normalisation (n-1)! in place of n! breaks the diagonal identity by "
          f"a factor {abs(rhs54 / lhs54w) if lhs54w != 0 else float('inf'):.3f} (~ n = {n})",
          abs(lhs54w - rhs54) > 0.1 * abs(rhs54))


def main():
    print(f"seed = {SEED}, N = {N}")
    T4, T5 = part1()
    part2(T4, T5)
    part3()
    part4()
    part5()
    npass = sum(ok for _, ok in RESULTS)
    print(f"summary: {npass}/{len(RESULTS)} PASS")
    sys.exit(0 if npass == len(RESULTS) else 1)


if __name__ == "__main__":
    main()
