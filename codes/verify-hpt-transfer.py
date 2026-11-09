"""
Homological-perturbation transfer of the Sigma sector of the cubic (HS) theory
(record 037, brief computator-037).

Finite-dimensional model of record 029 sec. 3 (same graded toy data as
codes/verify-morphism-check.py): H_0 with N_gh = (1,2,2,3,3,4), odd
graded-antisymmetric omega_1 saturating N_gh = 5, Delta = omega_1^{-1},
Q = Delta K (K rank one on the gh-2 block), ell_2 = Delta V_3,
ell_3 = Delta V_4, m_2 = Delta^{(x)2} V_4.

Classical complex (record 037 A2, repaired form): truncate H_0 FIRST, then
take the symmetric square.
    W^0 = H_0 at gh 2,           W^1 = H_0 at gh 3
    S^4 = Sym^2(H_0 at gh 2),    S^6 = Sym^2(H_0 at gh 3)
    V = (H_0 at gh {2,3}) (+) (S^4 (+) S^6),  degrees {0,1}.
Differential Ltilde_1 = Q (+) (-g^2/12 m_2cl) with m_2cl = Pi_2 m_2|_{S^4} the
PROJECTED quartic kernel (m_2 itself leaves the truncation: it has components
in (gh 2) (x) (gh 4)).  Contraction (p, i, h) with
    h|_{S^6} = -(12/g^2) m_2cl^{-1},  h = 0 elsewhere      (037 eq. (1.5)).
Neither S^4 nor S^6 is defined through m_2, so bijectivity of m_2cl is a
statement about V_4 (037 C1.0), not a definition.

VERIFIED
  C1.0-dual    omega_2 identifies S^6 = (S^4)^*, and the matrix of m_2cl in the
               S^4/S^6 bases equals Omega_2^{-1} V_4|_{S^4} (037 eq. (1.2)):
               m_2cl IS the quartic form on S^4.
  C1-rank      m_2cl : S^4 -> S^6 is injective, i.e. V_4 non-degenerate on S^4
               (the injectivity half of PH1, R9); dim S^4 = dim S^6 here, so in
               this finite-dimensional model that is bijectivity -- beyond it,
               closed range and a bounded inverse are PH1's extra content (R10)
               and are NOT checked.  Break leg C1-rank' makes V_4|_{S^4}
               degenerate and must FAIL.
  C1.5-span    m_2 S^4 is NOT S^6 (the projector Pi_2 is not vacuous).
  C1-sidecond  the five contraction relations (037 eq. (1.6)); break leg
               C1-sidecond' rescales h by 2 and must FAIL.
  C1-rank/unique  NOT a separate check: the uniqueness of h reduces by an
               argument (037 sec. 1) to the injectivity C1-rank already
               reports; the line restates that datum and is not counted.
  C1-acyclic   the cohomology of (V, Ltilde_1) COMPUTED from the explicit
               matrix of Ltilde_1 on V (ranks and kernels, nothing hard-coded)
               equals H(W, Q) in each degree; break legs C1-acyclic' (V_4 made
               degenerate on S^4) and C1-acyclic'' (one column of the
               differential removed) must FAIL.
  C2.1-C2.4    the transferred brackets obtained by running the fixed-point
               recursion F = i psi - h P B(F) NUMERICALLY (not by substituting
               the closed form) and extracting the Taylor coefficients of
               L^tr(t psi) = p Ltilde(F(t psi)) equal (Q, g ell_2, g^2 ell_3, 0)
               = the brackets of T.  Break legs C2.3' (h rescaled by 2) and
               C2.3'' (h sign flipped) must FAIL.
  C2-V3zero    limiting case ell_2 = 0: ell_3^tr is unchanged.
  C2-gscale    the transferred brackets recomputed at four values of g; the
               exponents fitted from log|ell_n^tr| vs log g are n - 1, so the
               g^{-2} of h does cancel the g^2 of the Sym^2-valued bracket
               (037 sec. 1, commentary (1.5)).
  C3.1         F^(2) = psi^{(x)2} and F^(3) = 0 (so phi_2 = (.)^{(x)2},
               phi_{n>=3} = 0 are derived, not assumed).
  C4.1         the morphism defect Ltilde(F) - dF[L^tr], with dF computed by
               finite differences of the recursion, vanishes on the classical
               complex; computed again with no truncation anywhere it is
               NONZERO and supported at N_gh = 5 only (029 check D0,
               C4.1-nonvac / C4.1-supp).  Break leg C4.1' rescales phi_2 to
               1.3 (.)^{(x)2} and must FAIL.
  C4.2         the same identity at a generic superposition of four gh-2
               vectors, ten times: a genericity test of the same polynomial
               identity as C4.1, NOT an arity-resolved test.
  C4.4         h is cyclic with respect to omega_2 (inherited from the graded
               symmetry of V_4, R7/R8); break leg C4.4' composes h with a
               non-symmetric map on S^4 and must FAIL.
  C4.5         SECOND METHOD for cyclicity: the primitive in t of
               omega_1(psi, L^tr(t psi)) equals S_eff(t psi) assembled from the
               raw vertices, 1/2 omega_1 Q + g/3! V_3 + g^2/4! V_4 (029 eq.
               (1.3)) -- neither L_trunc nor the closed forms of sec. 2 enter
               the right-hand side.  Break leg C4.5' rescales the quartic
               vertex by 1.5 and must FAIL.
  C5.1         the grading system (037 eq. (4.1)) has no solution over Z or
               Z_2 once gh-1 states are admitted; break leg C5.1' shows the
               same system restricted to the classical complex is solvable.

NOT VERIFIED: anything about the actual CFT V_4 (generic random tensors only);
  odd-input suspension signs; gradings of Sym^2 that are not functions of the
  total ghost number; the existence of the ghost-number-(-1) factorisation
  m_2 = B m' proposed in 037 sec. 4 as the weakest relaxation.

Conditional on PH1 (bounded inverse of m_2 on Sym^2 H_0 / ker V_4); in this
finite-dimensional model PH1 is checked, not assumed (C1-acyclic).
"""

from __future__ import annotations

import sys
from itertools import combinations_with_replacement, permutations

import numpy as np

SEED = int(sys.argv[1]) if len(sys.argv) > 1 else 2037
rng = np.random.default_rng(SEED)
print(f"[info] seed = {SEED}")
TOL = 1e-8
FAILS = 0
TOTAL = 0


def report(name: str, ok: bool, detail: str = "") -> None:
    global FAILS, TOTAL
    TOTAL += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
    if not ok:
        FAILS += 1


# --------------------------------------------------------------------------
# 1. Toy data (identical construction to codes/verify-morphism-check.py)
# --------------------------------------------------------------------------
NGH = np.array([1, 2, 2, 3, 3, 4])
N = len(NGH)
PAR = NGH % 2
GH2 = np.where(NGH == 2)[0]
GH3 = np.where(NGH == 3)[0]

omega = np.zeros((N, N))
for a in range(N):
    for b in range(N):
        if NGH[a] + NGH[b] == 5 and a < b:
            x = rng.standard_normal() + 1.0
            omega[a, b] = x
            omega[b, a] = -((-1) ** (PAR[a] * PAR[b])) * x
Delta = np.linalg.inv(omega)


def koszul_perm(idx, perm) -> float:
    s = 1.0
    for i in range(len(perm)):
        for j in range(i + 1, len(perm)):
            if perm[i] > perm[j] and PAR[idx[perm[i]]] and PAR[idx[perm[j]]]:
                s = -s
    return s


def sym_unit(idx):
    r = len(idx)
    T = np.zeros((N,) * r)
    for perm in permutations(range(r)):
        pidx = tuple(idx[perm[t]] for t in range(r))
        T[pidx] += koszul_perm(idx, perm)
    return None if np.abs(T).max() < 1e-12 else T / np.abs(T).max()


def rand_vertex(rank, target):
    basis = []
    for idx in combinations_with_replacement(range(N), rank):
        if sum(NGH[list(idx)]) != target:
            continue
        T = sym_unit(idx)
        if T is not None:
            basis.append(T)
    return sum(c * T for c, T in zip(rng.standard_normal(len(basis)), basis))


u = rng.standard_normal(2)
K = np.zeros((N, N))
K[np.ix_(GH2, GH2)] = np.outer(u, u)
Q = Delta @ K
V3 = rand_vertex(3, 6)
V4 = rand_vertex(4, 8)
L2 = np.einsum("ea,abc->ebc", Delta, V3)
L3 = np.einsum("ea,abcd->ebcd", Delta, V4)
M2 = np.einsum("ea,fb,abcd->efcd", Delta, Delta, V4)

g = 0.7


def ell2(a, b):
    return np.einsum("ebc,b,c->e", L2, a, b)


def ell3_sig(sig, a):
    """ell_3 with two slots filled by the strands of the Sym^2 element sig."""
    return np.einsum("ebcd,bc,d->e", L3, sig, a)


def m2(sig):
    return np.einsum("efcd,cd->ef", M2, sig)


def omega2(A, B):
    return np.einsum("ab,ae,bf,ef->", A, omega, omega, B)


def odot(a, b):
    return np.outer(a, b) + np.outer(b, a)


# --------------------------------------------------------------------------
# 2. Classical complex, projector, contraction (037 sec. 1)
# --------------------------------------------------------------------------
def sym2_basis(idx_set):
    """Basis of Sym^2 of the span of the basis vectors listed in idx_set."""
    out = []
    for i in range(len(idx_set)):
        for j in range(i, len(idx_set)):
            e_i = np.zeros(N); e_i[idx_set[i]] = 1.0
            e_j = np.zeros(N); e_j[idx_set[j]] = 1.0
            out.append(odot(e_i, e_j) / (2.0 if i == j else 1.0))
    return out


# 037 A2 (repaired): S^4 and S^6 are the symmetric squares of the TRUNCATED
# H_0 blocks; neither is defined through m_2.
S4_basis = sym2_basis(GH2)
S6_basis = sym2_basis(GH3)
S4_mat = np.array([b.ravel() for b in S4_basis]).T          # N^2 x 3
S6_mat = np.array([b.ravel() for b in S6_basis]).T          # N^2 x 3
dimS4, dimS6 = len(S4_basis), len(S6_basis)


def coeffs_S6(x):
    """Coefficients of the S^6 part of the Sym^2 element x in S6_basis.

    S6_basis is supported on the (gh 3, gh 3) entries only, so the
    Frobenius-orthogonal least-squares projection used here IS the ghost-block
    projector Pi_2 of 037 A2.
    """
    c, *_ = np.linalg.lstsq(S6_mat, x.ravel(), rcond=None)
    return c


# Matrix of m_2cl = Pi_2 m_2|_{S^4} in the bases S4_basis -> S6_basis.
def build_Mcl(V4_local=None):
    V4l = V4 if V4_local is None else V4_local
    M2l = np.einsum("ea,fb,abcd->efcd", Delta, Delta, V4l)
    cols = [coeffs_S6(np.einsum("efcd,cd->ef", M2l, b)) for b in S4_basis]
    return np.array(cols).T                                  # dimS6 x dimS4


Mcl = build_Mcl()
Mcl_inv = np.linalg.pinv(Mcl)
sv = np.linalg.svd(Mcl, compute_uv=False)


def proj_span(mat, x):
    """Orthogonal (Frobenius) projection of the matrix x on the span of mat's columns."""
    v = x.ravel()
    c, *_ = np.linalg.lstsq(mat, v, rcond=None)
    return (mat @ c).reshape(N, N)


H0_KEEP = np.zeros(N)
H0_KEEP[GH2] = 1.0
H0_KEEP[GH3] = 1.0


def P_V(phi, extra=None):
    """Projector on the classical complex; `extra` adds further Sym^2 columns."""
    psi, sig = phi
    mat = S4_mat if extra is None else np.hstack([S4_mat, extra])
    mat = np.hstack([mat, S6_mat])
    return H0_KEEP * psi, proj_span(mat, sig)


def h_map(phi, scale=1.0, twist=None):
    """h of eq. (1.5): kills H_0 and S^4, inverts m_2cl on S^6.

    `twist` (a dimS4 x dimS4 matrix) post-composes h with a linear map on the
    S^4 coefficients; used by the break leg C4.4'.
    """
    _, sig = phi
    c = Mcl_inv @ coeffs_S6(sig)
    if twist is not None:
        c = twist @ c
    pre = sum(ci * b for ci, b in zip(c, S4_basis))
    return np.zeros(N), scale * (-12.0 / g**2) * pre


S46_mat = np.hstack([S4_mat, S6_mat])


def m2_cl(sig):
    """Pi_2 m_2 on Sym^2: the Sigma-sector operator of the classical complex.

    The projection on S^4 (+) S^6 kills the (gh 2)(x)(gh 4) and gh-8 debris of
    the untruncated m_2 (037 sec. 1, 'Why the projector is needed').
    """
    return proj_span(S46_mat, m2(sig))


def ell1t(phi):
    """Differential of the classical complex: Q (+) (-g^2/12 m_2cl)."""
    psi, sig = phi
    return H0_KEEP * (Q @ psi), -(g**2) / 12.0 * m2_cl(sig)


def ell2t(phi1, phi2):
    p1, s1 = phi1
    p2, s2 = phi2
    h0 = g * ell2(p1, p2) + g**2 / 6.0 * (ell3_sig(s1, p2) + ell3_sig(s2, p1))
    s = g**2 / 12.0 * m2(odot(p1, p2))
    return h0, s


def B_op(phi):
    a, b = ell2t(phi, phi)
    return 0.5 * a, 0.5 * b


def Ltilde(phi):
    a1, b1 = ell1t(phi)
    a2, b2 = B_op(phi)
    return a1 + a2, b1 + b2


def Ltilde_full(phi):
    """Same EOM with the UNTRUNCATED differential (-g^2/12 m_2, no projector).

    Used only by defect_untruncated, which reproduces 029 check D0 on the full
    Sym^2 H_0 and must therefore not see the classical-complex projector.
    """
    psi, sig = phi
    a2, b2 = B_op(phi)
    return Q @ psi + a2, -(g**2) / 12.0 * m2(sig) + b2


def L_trunc(psi):
    """EOM of T (029 eq. (1.3))."""
    return (Q @ psi + g / 2.0 * ell2(psi, psi)
            + g**2 / 6.0 * np.einsum("ebcd,b,c,d->e", L3, psi, psi, psi))


def i_map(psi):
    return H0_KEEP * psi, np.zeros((N, N))


def p_map(phi):
    return phi[0]


def add(x, y, s=1.0):
    return x[0] + s * y[0], x[1] + s * y[1]


def rand_psi():
    P = np.zeros(N)
    P[GH2] = rng.standard_normal(len(GH2))
    return P


def F_rec(psi, scale=1.0, n_iter=8, extra=None):
    """Fixed point of F = i psi - h P B(F) (037 eq. (2.1)), run numerically."""
    F = i_map(psi)
    for _ in range(n_iter):
        F = add(i_map(psi), h_map(P_V(B_op(F), extra), scale), -1.0)
    return F


def L_transf(psi, scale=1.0, extra=None):
    return p_map(P_V(Ltilde(F_rec(psi, scale, extra=extra)), extra))


# ---- C1: contraction data ------------------------------------------------
# C1.0-dual: omega_2 identifies S^6 = (S^4)^*, and m_2cl IS V_4|_{S^4} under it
# (037 eq. (1.2)).  Omega2[i, j] = omega_2(S4_basis[i], S6_basis[j]),
# V4S4[i, j] = V_4(S4_basis[i], S4_basis[j]) = omega_2(S4_basis[i], m_2 b_j).
Omega2 = np.array([[omega2(a, b) for b in S6_basis] for a in S4_basis])
V4S4 = np.array([[omega2(a, m2(b)) for b in S4_basis] for a in S4_basis])
dual_ok = np.linalg.matrix_rank(Omega2, tol=1e-10) == dimS4
Mcl_from_V4 = np.linalg.solve(Omega2, V4S4)
report("C1.0-dual  omega_2 : S^6 = (S^4)^* and m_2cl = Omega_2^{-1} V_4|_{S^4}",
       dual_ok and np.abs(Mcl_from_V4 - Mcl).max() < 1e-9,
       f"|Omega_2^-1 V_4 - M_cl| = {np.abs(Mcl_from_V4 - Mcl).max():.2e}, "
       f"V_4|_S4 symmetric to {np.abs(V4S4 - V4S4.T).max():.2e}")

# Injective <=> V_4 non-degenerate on S^4 (PH1's injectivity half, R9); here
# dim S^4 = dim S^6, so in this finite-dimensional model it is bijectivity.
report("C1-rank  m_2cl : S^4 -> S^6 injective, = bijective in this model (V_4 non-deg. on S^4)",
       sv.min() > 1e-8 and dimS4 == dimS6,
       f"dims {dimS4}/{dimS6}, smallest sv of M_cl = {sv.min():.2e}")

# break leg C1-rank': make the quartic form on S^4 degenerate.  By C1.0-dual
# the matrix M_cl IS V_4|_{S^4} up to Omega_2, so annihilating one eigenvector
# of V4S4 is exactly "V_4 acquires a null direction in Sym^2 H_0^{(2)}" -- the
# falsifier of PH1 after the ker V_4 quotient.
_, U = np.linalg.eigh(V4S4)
null_dir = U[:, 0]
Proj_null = np.eye(dimS4) - np.outer(null_dir, null_dir)
Mcl_deg = Mcl @ Proj_null
report("C1-rank' V_4 given a null direction on S^4: bijectivity FAILS (break leg)",
       np.linalg.svd(Mcl_deg, compute_uv=False).min() < 1e-8,
       f"smallest sv = {np.linalg.svd(Mcl_deg, compute_uv=False).min():.2e}")

# C1.5-span: m_2 S^4 is NOT S^6 (the projector Pi_2 is not vacuous)
img_mat = np.array([m2(b).ravel() for b in S4_basis]).T
joint = np.linalg.matrix_rank(np.hstack([img_mat, S6_mat]), tol=1e-10)
report("C1.5-span  m_2 S^4 != S^6 (the projector Pi_2 is not vacuous)",
       joint > dimS6, f"rank[m_2 S^4 | S^6] = {joint} > dim S^6 = {dimS6}")


def sidecond_residual(scale):
    res = 0.0
    for _ in range(6):
        psi = np.zeros(N)
        psi[GH2] = rng.standard_normal(len(GH2))
        psi[GH3] = rng.standard_normal(len(GH3))
        sig = sum(c * b for c, b in zip(rng.standard_normal(3), S4_basis)) \
            + sum(c * b for c, b in zip(rng.standard_normal(3), S6_basis))
        phi = (psi, sig)
        lhs = add(h_map(ell1t(phi), scale), ell1t(h_map(phi, scale)))
        rhs = add(phi, i_map(p_map(phi)), -1.0)
        res = max(res, np.abs(lhs[0] - rhs[0]).max(), np.abs(lhs[1] - rhs[1]).max())
        # p h = 0, h i = 0, h^2 = 0, p i = id
        res = max(res, np.abs(p_map(h_map(phi, scale))).max())
        res = max(res, np.abs(h_map(i_map(psi), scale)[1]).max())
        res = max(res, np.abs(h_map(h_map(phi, scale), scale)[1]).max())
        res = max(res, np.abs(p_map(i_map(psi)) - H0_KEEP * psi).max())
    return res


r1 = sidecond_residual(1.0)
report("C1-sidecond  five contraction relations (037 eq. (1.6))", r1 < TOL,
       f"max residual = {r1:.2e}")
r2 = sidecond_residual(2.0)
report("C1-sidecond' h rescaled by 2 breaks them (break leg)", r2 > 1e-3, f"max residual = {r2:.2e}")

# Uniqueness of h: any eta = h' - h reduces, by the argument of 037 sec. 1
# *Uniqueness*, to eta : S^6 -> S^4 with m_2cl eta = 0.  That reduction is an
# argument, not a computation; its only numerical input is the injectivity of
# m_2cl, which C1-rank already reports.  So this line is a RESTATEMENT of
# C1-rank for the uniqueness claim, not an independent check, and it is not
# counted separately.
report("C1-rank/unique  (same datum as C1-rank, read for uniqueness of h; not a separate check)",
       sv.min() > 1e-8, f"smallest singular value of m_2cl = {sv.min():.2e}")


def d_matrix(Mcl_local):
    """Matrix of Ltilde_1 : V^0 -> V^1 in the bases
    V^0 = (gh-2 vectors) + S4_basis,  V^1 = (gh-3 vectors) + S6_basis.

    Nothing about the cohomology is assumed: the matrix is assembled from Q and
    from the Sigma-sector operator, and the ranks are taken from it.
    """
    n0, n1 = len(GH2) + dimS4, len(GH3) + dimS6
    D = np.zeros((n1, n0))
    D[: len(GH3), : len(GH2)] = Q[np.ix_(GH3, GH2)]
    D[len(GH3):, len(GH2):] = -(g**2) / 12.0 * Mcl_local
    return D


def coh_from_matrix(Mcl_local):
    """(dim H^0, dim H^1) of (V, Ltilde_1) and of (W, Q), from ranks only."""
    Qm = Q[np.ix_(GH3, GH2)]
    rQ = np.linalg.matrix_rank(Qm, tol=1e-10)
    hW = (len(GH2) - rQ, len(GH3) - rQ)
    D = d_matrix(Mcl_local)
    rD = np.linalg.matrix_rank(D, tol=1e-10)
    hV = (D.shape[1] - rD, D.shape[0] - rD)
    return hW, hV


# sanity: Ltilde_1 must really be the matrix D on the classical complex
res_dmat = 0.0
for _ in range(4):
    cv = rng.standard_normal(len(GH2) + dimS4)
    psi = np.zeros(N)
    psi[GH2] = cv[: len(GH2)]
    sig = sum(c * b for c, b in zip(cv[len(GH2):], S4_basis))
    out_psi, out_sig = ell1t((psi, sig))
    pred = d_matrix(Mcl) @ cv
    got = np.concatenate([out_psi[GH3], coeffs_S6(out_sig)])
    res_dmat = max(res_dmat, np.abs(pred - got).max())
report("C1-dmat  the assembled matrix of Ltilde_1 reproduces the operator",
       res_dmat < 1e-9, f"max residual = {res_dmat:.2e}")

hW, hV = coh_from_matrix(Mcl)
report("C1-acyclic  H(V, Ltilde_1) = H(W, Q), computed from ranks (Sigma acyclic)",
       hW == hV, f"H(W) = {tuple(int(x) for x in hW)}, H(V) = {tuple(int(x) for x in hV)}")
hW2, hV2 = coh_from_matrix(Mcl_deg)
report("C1-acyclic' V_4 degenerate on S^4: cohomology differs (break leg)",
       hW2 != hV2, f"H(W) = {tuple(int(x) for x in hW2)}, H(V) = {tuple(int(x) for x in hV2)}")
Mcl_drop = Mcl.copy()
Mcl_drop[:, -1] = 0.0
hW3, hV3 = coh_from_matrix(Mcl_drop)
report("C1-acyclic'' one column of the differential removed: detected (break leg)",
       hW3 != hV3, f"H(W) = {tuple(int(x) for x in hW3)}, H(V) = {tuple(int(x) for x in hV3)}")

# ---- C2 / C3: the transfer ------------------------------------------------
psi0 = rand_psi()


def taylor_coeffs(psi, scale=1.0, order=4, eps=0.35):
    """Coefficients of L^tr(t psi) in t, orders 1..order, by Vandermonde fit."""
    ts = eps * np.arange(1, order + 3)
    vals = np.array([L_transf(t * psi, scale) for t in ts])
    Vd = np.vander(ts, order + 2, increasing=True)[:, 1:]
    coef, *_ = np.linalg.lstsq(Vd, vals, rcond=None)
    return coef


coef = taylor_coeffs(psi0)
exp1 = Q @ psi0
exp2 = g / 2.0 * ell2(psi0, psi0)
exp3 = g**2 / 6.0 * np.einsum("ebcd,b,c,d->e", L3, psi0, psi0, psi0)
report("C2.1  ell_1^tr = Q", np.abs(coef[0] - exp1).max() < 1e-7,
       f"|diff| = {np.abs(coef[0] - exp1).max():.2e}")
report("C2.2  ell_2^tr = g ell_2", np.abs(coef[1] - exp2).max() < 1e-7,
       f"|diff| = {np.abs(coef[1] - exp2).max():.2e}, |exp| = {np.abs(exp2).max():.2e}")
report("C2.3  ell_3^tr = g^2 ell_3 (the Sigma-exchange tree)",
       np.abs(coef[2] - exp3).max() < 1e-7,
       f"|diff| = {np.abs(coef[2] - exp3).max():.2e}, |exp| = {np.abs(exp3).max():.2e}")
report("C2.4  ell_4^tr = 0", np.abs(coef[3]).max() < 1e-6, f"max = {np.abs(coef[3]).max():.2e}")

c2 = taylor_coeffs(psi0, scale=2.0)
report("C2.3' propagator rescaled by 2: ell_3^tr wrong (break leg)",
       np.abs(c2[2] - exp3).max() > 1e-4, f"|diff| = {np.abs(c2[2] - exp3).max():.2e}")
c3 = taylor_coeffs(psi0, scale=-1.0)
report("C2.3'' h sign flipped: ell_3^tr wrong (break leg)",
       np.abs(c3[2] - exp3).max() > 1e-4, f"|diff| = {np.abs(c3[2] - exp3).max():.2e}")

# limiting case V_3 = 0
L2_save = L2.copy()
L2 = np.zeros_like(L2)
coef0 = taylor_coeffs(psi0)
report("C2-V3zero  ell_2 = 0: ell_3^tr unchanged, ell_2^tr = 0",
       np.abs(coef0[2] - exp3).max() < 1e-7 and np.abs(coef0[1]).max() < 1e-7,
       f"|diff_3| = {np.abs(coef0[2] - exp3).max():.2e}")
L2 = L2_save

# C2-gscale: the g-counting the record claims (037 sec. 1, commentary (1.5)).
# h carries g^{-2} and is NOT a formal power series in g, so the statement
# "ell_n^tr ~ g^{n-1}" has to be measured, not asserted.
g_save = g
g_values = np.array([0.4, 0.55, 0.7, 0.9])
norms = []
for gv in g_values:
    g = gv
    cg = taylor_coeffs(psi0)
    norms.append([np.linalg.norm(cg[k]) for k in range(3)])
g = g_save
norms = np.array(norms)
slopes = [np.polyfit(np.log(g_values), np.log(norms[:, k]), 1)[0] for k in range(3)]
report("C2-gscale  ell_n^tr scales as g^{n-1} (fitted exponents at 4 values of g)",
       all(abs(s - k) < 1e-6 for k, s in enumerate(slopes)),
       "fitted = " + ", ".join(f"{s:.6f}" for s in slopes) + " (expected 0, 1, 2)")

# C3.1: F^(2) = psi^(x)2, F^(3) = 0
tsF = 0.3 * np.arange(1, 6)
Fv = np.array([F_rec(t * psi0)[1].ravel() for t in tsF])
VdF = np.vander(tsF, 6, increasing=True)[:, 1:]
cF, *_ = np.linalg.lstsq(VdF, Fv, rcond=None)
report("C3.1  F^(2) = psi^(x)2 and F^(3) = 0 (phi_2, phi_3 derived)",
       np.abs(cF[1].reshape(N, N) - np.outer(psi0, psi0)).max() < 1e-7
       and np.abs(cF[2]).max() < 1e-6,
       f"|F2 - psi^2| = {np.abs(cF[1].reshape(N, N) - np.outer(psi0, psi0)).max():.2e}, "
       f"|F3| = {np.abs(cF[2]).max():.2e}")

# ---- C4: morphism identity ------------------------------------------------
GH5_pairs = [(a, b) for a in range(N) for b in range(N) if NGH[a] + NGH[b] == 5]
S5_cols = []
for (a, b) in GH5_pairs:
    e_a = np.zeros(N); e_a[a] = 1.0
    e_b = np.zeros(N); e_b[b] = 1.0
    S5_cols.append(odot(e_a, e_b).ravel())
S5_mat = np.array(S5_cols).T


def morphism_defect(psi, scale=1.0, t=1e-4):
    """Ltilde(F(psi)) - dF|_psi[L^tr(psi)] on the classical complex,
    with F from the recursion and dF by central finite differences."""
    F = F_rec(psi, scale)
    lhs = P_V(Ltilde(F))
    X = L_transf(psi, scale)
    Fp = F_rec(psi + t * X, scale)
    Fm = F_rec(psi - t * X, scale)
    dF = P_V(((Fp[0] - Fm[0]) / (2 * t), (Fp[1] - Fm[1]) / (2 * t)))
    return lhs[0] - dF[0], lhs[1] - dF[1]


def defect_untruncated(psi, c=1.0):
    """Same defect with no truncation anywhere: Ltilde(psi, c psi^(x)2)
    minus (L(psi), c L(psi) (x)_sym psi).  This is 029 check D0."""
    a, b = Ltilde_full((psi, c * np.outer(psi, psi)))
    X = L_trunc(psi)
    return a - X, b - c * odot(X, psi)


dH, dS = morphism_defect(psi0)
report("C4.1  morphism defect vanishes on the classical complex",
       np.abs(dH).max() < 1e-6 and np.abs(dS).max() < 1e-6,
       f"|H_0| = {np.abs(dH).max():.2e}, |Sym^2| = {np.abs(dS).max():.2e}")
uH, uS = defect_untruncated(psi0)
report("C4.1-nonvac  the SAME defect without the truncation is NONZERO (029 D0)",
       np.abs(uH).max() < 1e-9 and np.abs(uS).max() > 1e-3,
       f"|H_0| = {np.abs(uH).max():.2e}, |Sym^2| = {np.abs(uS).max():.2e}")
report("C4.1-supp  the untruncated defect is supported at N_gh = 5 only",
       max(abs(uS[a, b]) for a in range(N) for b in range(N) if NGH[a] + NGH[b] != 5) < 1e-12)
bH, bS = morphism_defect(psi0, scale=1.3)
report("C4.1' phi_2 rescaled to 1.3 (x)^2: projected defect nonzero (break leg)",
       np.abs(bS).max() > 1e-3, f"|Sym^2| = {np.abs(bS).max():.2e}")

ok42 = True
worst = 0.0
for _ in range(10):
    psis = [rand_psi() for _ in range(4)]
    ts = rng.standard_normal(4)
    psi = sum(t * p for t, p in zip(ts, psis))
    a, b = morphism_defect(psi)
    worst = max(worst, np.abs(a).max(), np.abs(b).max())
    ok42 &= np.abs(a).max() < 1e-5 and np.abs(b).max() < 1e-5
report("C4.2  identity at generic superpositions (genericity, not arity-resolved)", ok42,
       f"worst = {worst:.2e}")

# C4.4: cyclicity of h
cyc = []
for _ in range(5):
    x = sum(c * b for c, b in zip(rng.standard_normal(3), S6_basis))
    y = sum(c * b for c, b in zip(rng.standard_normal(3), S6_basis))
    cyc.append(omega2(h_map((np.zeros(N), x))[1], y) - omega2(x, h_map((np.zeros(N), y))[1]))
scale_cyc = abs(omega2(h_map((np.zeros(N), S6_basis[0]))[1], S6_basis[0])) + 1.0
report("C4.4  h is cyclic w.r.t. omega_2 (inherited from graded symmetry of V_4)",
       max(abs(c) for c in cyc) < 1e-7 * scale_cyc,
       f"max asymmetry = {max(abs(c) for c in cyc):.2e}")

# break leg C4.4': compose h with a non-symmetric map on the S^4 coefficients
TWIST = np.eye(dimS4) + 0.4 * np.triu(np.ones((dimS4, dimS4)), 1)
cyc_b = []
for _ in range(5):
    x = sum(c * b for c, b in zip(rng.standard_normal(dimS6), S6_basis))
    y = sum(c * b for c, b in zip(rng.standard_normal(dimS6), S6_basis))
    cyc_b.append(omega2(h_map((np.zeros(N), x), twist=TWIST)[1], y)
                 - omega2(x, h_map((np.zeros(N), y), twist=TWIST)[1]))
report("C4.4' h composed with a non-symmetric map: cyclicity FAILS (break leg)",
       max(abs(c) for c in cyc_b) > 1e-6 * scale_cyc,
       f"max asymmetry = {max(abs(c) for c in cyc_b):.2e}")


# C4.5: a primitive exists for the transferred EOM, and it is S_eff assembled
# from the VERTICES -- not from L_trunc.  This is the cyclicity content of
# C4.3: integrating omega_1(psi, L^tr(t psi)) dt from 0 to 1 must give
#   S_eff(psi) = 1/2 omega_1(psi, Q psi) + g/3! V_3(psi^3) + g^2/4! V_4(psi^4),
# with V_3, V_4 the raw vertex tensors of the model (029 eq. (1.3)).  A wrong
# relative factor between the cubic and quartic terms, or a transferred
# structure that admitted no primitive, would break it.
def act_coeffs(psi, fn, order=4, eps=0.35):
    """Taylor coefficients in t of omega_1(psi, fn(t psi)), orders 1..order."""
    ts = eps * np.arange(1, order + 3)
    vals = np.array([psi @ omega @ fn(t * psi) for t in ts])
    Vd = np.vander(ts, order + 2, increasing=True)[:, 1:]
    c, *_ = np.linalg.lstsq(Vd, vals, rcond=None)
    return c


def S_eff_direct(psi, t):
    """S_eff(t psi) assembled from the vertices V_3, V_4 (029 eq. (1.3))."""
    x = t * psi
    return (0.5 * (x @ omega @ (Q @ x))
            + g / 6.0 * np.einsum("abc,a,b,c->", V3, x, x, x)
            + g**2 / 24.0 * np.einsum("abcd,a,b,c,d->", V4, x, x, x, x))


# Primitive of the transferred EOM: sum_n c_n t^{n+1} / (n+1) with
# c_n the Taylor coefficients of omega_1(psi, L^tr(t psi)).
a_tr = act_coeffs(psi0, lambda x: L_transf(x))
prim = [sum(c / (n + 1) * t ** (n + 1) for n, c in enumerate(a_tr, start=1))
        for t in (0.3, 0.6, 0.9)]
direct = [S_eff_direct(psi0, t) - S_eff_direct(psi0, 0.0) for t in (0.3, 0.6, 0.9)]
err45 = max(abs(p - d) for p, d in zip(prim, direct))
report("C4.5  primitive of the transferred EOM = S_eff built from V_3, V_4 (second method)",
       err45 < 1e-6 * (1.0 + max(abs(d) for d in direct)),
       f"max |primitive - S_eff| = {err45:.2e}, |S_eff| = {max(abs(d) for d in direct):.2e}")

# break leg C4.5': the same comparison with the quartic vertex rescaled by 1.5
# must FAIL -- the check does distinguish the relative cubic/quartic weight.
def S_eff_bad(psi, t):
    """S_eff with the quartic vertex rescaled by 1.5 (break leg for C4.5)."""
    x = t * psi
    return (0.5 * (x @ omega @ (Q @ x))
            + g / 6.0 * np.einsum("abc,a,b,c->", V3, x, x, x)
            + 1.5 * g**2 / 24.0 * np.einsum("abcd,a,b,c,d->", V4, x, x, x, x))


bad = [S_eff_bad(psi0, t) for t in (0.3, 0.6, 0.9)]
err45b = max(abs(p - d) for p, d in zip(prim, bad))
report("C4.5' quartic vertex rescaled by 1.5: primitive no longer matches (break leg)",
       err45b > 1e-6 * (1.0 + max(abs(d) for d in direct)),
       f"max |primitive - S_eff'| = {err45b:.2e}")

# ---- C5: the grading obstruction -----------------------------------------
NMAX = 2 * NGH.max()


def grading_system(gh_allowed):
    """Rows of the linear system (4.1) for h(n) on Sym^2, over the H_0 ghost
    numbers in `gh_allowed`.  Unknowns h(0..NMAX).

    Note: `inS` admits every Sym^2 ghost sum reachable from `gh_allowed`,
    including gh 5, which 037 A2 excludes.  The system solved is therefore not
    restricted to A2 by construction; the extra rows are removed by the
    ghost-number arithmetic, but the check should not be described as testing
    A2's system by construction.
    """
    rows, rhs = [], []
    inH = lambda a: NGH[a] in gh_allowed
    inS = lambda a, b: (NGH[a] + NGH[b]) in {a_ + b_ for a_ in gh_allowed for b_ in gh_allowed}
    for e, f, c, d in zip(*np.nonzero(np.abs(M2) > 1e-12)):
        if inS(e, f) and inS(c, d):                                    # (a) m_2
            r = np.zeros(NMAX + 1)
            r[NGH[e] + NGH[f]] += 1
            r[NGH[c] + NGH[d]] -= 1
            rows.append(r); rhs.append(1.0)
        if inS(e, f) and inH(c) and inH(d):                            # (b) m_2(A x B)
            r = np.zeros(NMAX + 1)
            r[NGH[e] + NGH[f]] += 1
            rows.append(r); rhs.append(float(NGH[c] - 2 + NGH[d] - 2 + 1))
    for e, b, c, d in zip(*np.nonzero(np.abs(L3) > 1e-12)):            # (c) ell_3(Sigma, Psi)
        if inH(e) and inS(b, c) and inH(d):
            r = np.zeros(NMAX + 1)
            r[NGH[b] + NGH[c]] += 1
            rows.append(r); rhs.append(float(NGH[e] - 2 - (NGH[d] - 2) - 1))
    return np.array(rows), np.array(rhs)


A_cl, b_cl = grading_system({2, 3})
res_cl = np.linalg.norm(A_cl @ np.linalg.lstsq(A_cl, b_cl, rcond=None)[0] - b_cl)
A_g, b_g = grading_system({1, 2, 3})
res_g = np.linalg.norm(A_g @ np.linalg.lstsq(A_g, b_g, rcond=None)[0] - b_g)
z2 = any(np.all(np.mod(A_g @ np.array([(bits >> n) & 1 for n in range(NMAX + 1)], float) - b_g, 2) == 0)
         for bits in range(2 ** (NMAX + 1)))
report("C5.1  no ghost-number grading of Sym^2 once gh-1 states are admitted (Z and Z_2)",
       res_g > 1e-3 and not z2, f"residual = {res_g:.2e}, Z_2 solution exists = {z2}")
report("C5.1' the same system on the classical complex IS solvable (break leg)",
       res_cl < 1e-9, f"residual = {res_cl:.2e}")

print(f"[summary] {TOTAL - FAILS}/{TOTAL} report lines PASS "
      f"({TOTAL - 1} distinct checks; C1-rank/unique restates C1-rank) "
      f"{'ALL PASS' if FAILS == 0 else f'-- {FAILS} FAIL'}")
sys.exit(1 if FAILS else 0)
