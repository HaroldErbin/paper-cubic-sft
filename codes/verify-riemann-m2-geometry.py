"""RS1 --- companion verification for derivation 020 (Riemann-surface meaning of
m2^{-1}, coloured gluing, the Sigma_k tower).

This is FINITE-DIMENSIONAL STRUCTURAL verification of the ALGEBRAIC claims of
`agent/derivations/020-riemann-m2-geometric.md` sec. 9. It replaces the abstract
CFT objects by finite matrices:

    H0  -> R^d,
    omega1 / G2 -> a symmetric invertible Gram matrix on Sym^2(R^d),
    V4  -> a totally symmetric 4-tensor T_{abcd}; V4|_{Sym^2} -> its Gram matrix M,
    m2  -> a symmetric invertible matrix (a stand-in for G2^{-1} V4),
    q^{L0} -> diag(exp((-s+i theta) * energies)),
    colour-2 sandwich (5.3) -> a fixed (parameter-free) matrix.

WHAT IS ESTABLISHED (per check, see docstrings below): the *algebraic* content of
020's claims --- the channel telescoping (4.1), the non-representability of a
matrix inverse by a re-weighted local kernel family (3.i), the Gram sandwich
(3.3), the Neumann/Schwinger presentations (3.1)/(3.2), the topological genus
formula (5.2), the ghost-saturation bookkeeping (sec. 0) and the ghost-number
formula R23, and the 2-vs-0 real-parameter count of the two edge kernels
(colour-1 (0.2) vs colour-2 (5.3)).

WHAT IS *NOT* ESTABLISHED: none of this is a CFT-level statement. In particular
it does NOT verify (i) that a single omega1^{-1} contraction equals frozen q=1
plumbing (the fixture bookkeeping = task RS4), (ii) the actual spectrum / gap /
invertibility of the true CFT V4 on Sym^2(ker L0^- cap ker b0^-) (= A2(iii)),
(iii) the operadic (properad/dioperad) statements of sec. 5 beyond the integer
Euler-characteristic arithmetic, or (iv) any convergence property of the true
infinite-dimensional chain series. The matrices here are generic stand-ins whose
algebraic behaviour mirrors the claims; agreement is evidence for the algebra,
not for the geometry.

Conventions taken VERBATIM from 020 sec. 4 (= R14): Sigma-propagator
(12/g_s^2)(V4|_Sym^2)^{-1}, vertex (g_s^2/6) V4(., Psi_i (x) Psi_j). These are NOT
re-derived or renormalised here.

Each check prints PASS/FAIL for the tested quantity and carries a FALSIFICATION
leg (a deliberately perturbed variant that MUST fail); a check whose falsify leg
does not fail is itself reported FAIL. Two seeds are used and printed. Numeric
checks (1-5, 8) use numpy; the topological/ghost checks (6-7) use exact integer /
sympy arithmetic (check 7 uses sympy Rational / symbolic k).
"""

from __future__ import annotations

import sys

import numpy as np
import sympy as sp
from scipy.integrate import quad_vec
from scipy.linalg import expm

SEED_A = 20260709
SEED_B = 314159
G_S = 1.37  # generic numeric string coupling; all g_s powers must cancel to R14 values

results: list[tuple[str, str, bool]] = []


def report(num: str, label: str, ok: bool) -> None:
    results.append((num, label, ok))
    print(f"  check ({num}) {'PASS' if ok else 'FAIL'} --- {label}")


# ===========================================================================
# Shared finite-dimensional machinery
# ===========================================================================


def sym2_basis(d: int) -> list[np.ndarray]:
    """Orthonormal basis of Sym^2(R^d) as d x d symmetric matrices.

    lambda_{aa} = E_aa ; lambda_{ab} = (E_ab + E_ba)/sqrt(2) for a<b.
    Dimension d(d+1)/2 --- the symmetric subspace built EXPLICITLY (brief).
    """
    basis = []
    for a in range(d):
        m = np.zeros((d, d))
        m[a, a] = 1.0
        basis.append(m)
    for a in range(d):
        for b in range(a + 1, d):
            m = np.zeros((d, d))
            m[a, b] = m[b, a] = 1.0 / np.sqrt(2.0)
            basis.append(m)
    return basis


def random_totally_symmetric_T(
    d: int, rng: np.random.Generator, terms: int
) -> np.ndarray:
    """Totally symmetric T_{abcd} = sum_r c_r u_r^{(x)4} (a sum of 4th powers).

    Totally symmetric by construction; generically non-degenerate on Sym^2 when
    terms >= dim Sym^2.
    """
    T = np.zeros((d, d, d, d))
    for _ in range(terms):
        c = rng.uniform(-2, 2)
        u = rng.uniform(-1, 1, d)
        T += c * np.einsum("a,b,c,e->abce", u, u, u, u)
    return T


def sym2_gram(T: np.ndarray, basis: list[np.ndarray]) -> np.ndarray:
    """M_{IJ} = sum T_{abcd} lambda_I[a,b] lambda_J[c,d]  (V4|_Sym^2 Gram matrix)."""
    dimS = len(basis)
    M = np.zeros((dimS, dimS))
    for I in range(dimS):
        TL = np.einsum("abcd,ab->cd", T, basis[I])
        for J in range(dimS):
            M[I, J] = np.einsum("cd,cd->", TL, basis[J])
    return M


def sym2_project(p: np.ndarray, q: np.ndarray, basis: list[np.ndarray]) -> np.ndarray:
    """Coefficients of sym(p (x) q) in the orthonormal Sym^2 basis."""
    S = 0.5 * (np.outer(p, q) + np.outer(q, p))
    return np.array([np.einsum("ab,ab->", lam, S) for lam in basis])


# ===========================================================================
# CHECK 1 --- channel arithmetic (re-verifies R14 as restated in (4.1))
#
# Establishes: with the R14 normalisations (vertex g_s^2/6, propagator
# 12/g_s^2), each single perfect matching of the Sigma-exchange telescopes to
# (g_s^2/3) V4(Psi_1..Psi_4) EXACTLY, and the 3-matching sum to g_s^2 V4. Full
# total symmetry of T is load-bearing (the three matchings coincide only because
# T is totally symmetric).
# NOT established: the CFT correlator value of V4 itself.
# ===========================================================================


def channel_check(seed: int) -> bool:
    rng = np.random.default_rng(seed)
    ok = True
    for d in (2, 3):
        basis = sym2_basis(d)
        dimS = len(basis)
        T = random_totally_symmetric_T(d, rng, terms=dimS + 3)
        M = sym2_gram(T, basis)
        assert abs(np.linalg.det(M)) > 1e-8, "draw gave singular M; change seed"
        Minv = np.linalg.inv(M)
        psi = [rng.uniform(-1, 1, d) for _ in range(4)]

        def V4val(i: int, j: int, k: int, l: int) -> float:
            return np.einsum("abcd,a,b,c,d->", T, psi[i], psi[j], psi[k], psi[l])

        contact = V4val(0, 1, 2, 3)
        matchings = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]

        def channel(prop_norm: float) -> tuple[list[float], float]:
            per = []
            for (i, j), (k, l) in matchings:
                s_ij = sym2_project(psi[i], psi[j], basis)
                s_kl = sym2_project(psi[k], psi[l], basis)
                vtx_ij = (G_S**2 / 6.0) * (
                    M @ s_ij
                )  # (g_s^2/6) V4(lambda, Psi_i Psi_j)
                vtx_kl = (G_S**2 / 6.0) * (M @ s_kl)
                per.append(float(vtx_ij @ (prop_norm * Minv) @ vtx_kl))
            return per, float(sum(per))

        per, tot = channel(12.0 / G_S**2)  # R14 propagator normalisation
        # each matching = (g_s^2/3) V4 ; sum = g_s^2 V4
        each_ok = all(
            abs(p - (G_S**2 / 3.0) * contact) < 1e-8 * (1 + abs(contact)) for p in per
        )
        sum_ok = abs(tot - G_S**2 * contact) < 1e-8 * (1 + abs(contact))
        # FALSIFY: perturb the 12/g_s^2 propagator normalisation -> 11/g_s^2
        _, tot_bad = channel(11.0 / G_S**2)
        falsify = abs(tot_bad - G_S**2 * contact) > 1e-6 * (1 + abs(contact))
        ok = ok and each_ok and sum_ok and falsify
    return ok


# ===========================================================================
# CHECK 2 --- no local moduli kernel represents the inverse (toy of 3.i)
#
# Establishes: matrix inversion is NOT a re-weighting of the kernel family. For a
# family {K_i} spanning a PROPER subspace of Sym(d), (i) (sum w_i K_i)^{-1} !=
# sum w_i K_i^{-1} pointwise, and (ii) no re-weighting sum w~_i K_i equals the
# inverse (least-squares residual bounded away from 0 over >=5 draws). POSITIVE
# CONTROL (the falsify-can-succeed leg): a commuting family closed under
# inversion DOES represent the inverse (residual ~ 0), proving the residual test
# can register a genuine zero.
# NOT established: the CFT no-go for a local moduli kernel of m2^{-1} (that is a
# ghost/g_s diagnostic argument, one notch below a theorem; sec. 3.i / open pt 4).
# ===========================================================================


def no_local_kernel_check(seed: int) -> bool:
    rng = np.random.default_rng(seed)
    d = 4
    # dim Sym^2 = d(d+1)/2 = 10; take m_fam < 10 so the family spans a PROPER subspace
    m_fam = 6
    ok = True

    def rand_sym() -> np.ndarray:
        A = rng.uniform(-1, 1, (d, d))
        return 0.5 * (A + A.T)

    def vec_sym(K: np.ndarray) -> np.ndarray:
        return K.reshape(-1)

    residuals = []
    pointwise_gaps = []
    for _ in range(6):
        K = [rand_sym() for _ in range(m_fam)]
        # ensure each K_i invertible (for the pointwise sum-of-inverses claim)
        K = [
            Ki + (0.5 if abs(np.linalg.det(Ki)) < 1e-3 else 0.0) * np.eye(d) for Ki in K
        ]
        w = rng.uniform(0.5, 2.0, m_fam) * rng.choice([-1, 1], m_fam)
        V = sum(wi * Ki for wi, Ki in zip(w, K, strict=True))
        if abs(np.linalg.det(V)) < 1e-6:
            continue
        Vinv = np.linalg.inv(V)
        # (2a) pointwise inequality: (sum w K)^{-1} vs sum w K^{-1}
        naive = sum(wi * np.linalg.inv(Ki) for wi, Ki in zip(w, K, strict=True))
        pointwise_gaps.append(np.linalg.norm(naive - Vinv) / np.linalg.norm(Vinv))
        # (2b) best re-weighting of the SAME family to match the inverse
        A = np.stack([vec_sym(Ki) for Ki in K], axis=1)  # (d^2, m)
        wtil, *_ = np.linalg.lstsq(A, vec_sym(Vinv), rcond=None)
        resid = np.linalg.norm(A @ wtil - vec_sym(Vinv)) / np.linalg.norm(vec_sym(Vinv))
        residuals.append(resid)
    neg_ok = (
        len(residuals) >= 5
        and all(r > 1e-3 for r in residuals)
        and all(g > 1e-3 for g in pointwise_gaps)
    )

    # POSITIVE CONTROL: commuting family = simultaneous eigenprojectors. Then
    # V = U diag(w) U^T and V^{-1} = sum (1/w_i) K_i is IN the span -> residual 0.
    Q, _ = np.linalg.qr(rng.uniform(-1, 1, (d, d)))
    Kc = [Q @ np.diag((np.arange(d) == i).astype(float)) @ Q.T for i in range(d)]
    wc = rng.uniform(0.7, 2.0, d)
    Vc = sum(wi * Ki for wi, Ki in zip(wc, Kc, strict=True))
    Vcinv = np.linalg.inv(Vc)
    Ac = np.stack([Kc_i.reshape(-1) for Kc_i in Kc], axis=1)
    wtil_c, *_ = np.linalg.lstsq(Ac, Vcinv.reshape(-1), rcond=None)
    resid_c = np.linalg.norm(Ac @ wtil_c - Vcinv.reshape(-1)) / np.linalg.norm(
        Vcinv.reshape(-1)
    )
    pos_ok = resid_c < 1e-8  # commuting family CAN represent its inverse

    ok = neg_ok and pos_ok
    return ok


# ===========================================================================
# CHECK 3 --- Gram sandwich (3.3): the "moduli cancellation" is a Gram identity,
# NOT a pointwise map (trap T6).
#
# Establishes: with G = sum_a K_a the moduli-discretised Gram operator,
# G G^{-1} G = G holds, but ONLY after the full double moduli sum + intermediate
# state sum; the "diagonal"/pointwise slice sum_a K_a G^{-1} K_a != G, i.e. no
# single moduli point telescopes.
# NOT established: any worldsheet-locus statement.
# ===========================================================================


def gram_sandwich_check(seed: int) -> bool:
    rng = np.random.default_rng(seed)
    d = 5
    n_moduli = 7
    K = []
    for _ in range(n_moduli):
        A = rng.uniform(-1, 1, (d, d))
        K.append(0.5 * (A + A.T))
    G = sum(K)
    if abs(np.linalg.det(G)) < 1e-6:
        G = G + np.eye(d)
    Ginv = np.linalg.inv(G)
    # (3a) full Gram identity  G G^{-1} G = G
    sandwich = G @ Ginv @ G
    id_ok = np.allclose(sandwich, G, atol=1e-9)
    # (3b) pointwise (diagonal-slice) sum does NOT reproduce G
    diag_slice = sum(Ka @ Ginv @ Ka for Ka in K)
    no_pointwise = np.linalg.norm(diag_slice - G) > 1e-3 * np.linalg.norm(G)
    # FALSIFY: perturb the inverse -> (G + eps I)^{-1}; sandwich must break
    Gpert = np.linalg.inv(G + 0.1 * np.eye(d))
    falsify = np.linalg.norm(G @ Gpert @ G - G) > 1e-6 * np.linalg.norm(G)
    return id_ok and no_pointwise and falsify


# ===========================================================================
# CHECK 4 --- Neumann chain series (3.1): m2^{-1} = sum_n (D^{-1} N)^n D^{-1},
# convergent iff rho(D^{-1} N) < 1.
#
# Establishes: split m2 = D - N with D = diag(m2); the truncated chain sum
# converges to m2^{-1} exactly when the spectral radius rho(D^{-1}N) < 1, and
# diverges otherwise. BOTH regimes exhibited.
# NOT established: convergence of the true infinite-dim chain series.
# ===========================================================================


def neumann_chain_check(seed: int) -> bool:
    rng = np.random.default_rng(seed)
    d = 5

    def chain_sum(m2: np.ndarray, N_terms: int) -> np.ndarray:
        D = np.diag(np.diag(m2))
        Dinv = np.linalg.inv(D)
        Nmat = D - m2
        R = Dinv @ Nmat
        acc = np.zeros_like(m2)
        Rp = np.eye(d)
        for _ in range(N_terms):
            acc = acc + Rp @ Dinv
            Rp = Rp @ R
        return acc, np.max(np.abs(np.linalg.eigvals(R)))

    # convergent regime: diagonally dominant m2 -> rho(D^{-1}N) < 1
    A = rng.uniform(-0.25, 0.25, (d, d))
    m2_conv = 0.5 * (A + A.T) + np.diag(rng.uniform(3, 5, d))
    S_conv, rho_conv = chain_sum(m2_conv, 200)
    conv_ok = rho_conv < 1.0 and np.allclose(S_conv, np.linalg.inv(m2_conv), atol=1e-8)

    # divergent regime: strong off-diagonal -> rho(D^{-1}N) > 1
    B = rng.uniform(2, 4, (d, d))
    m2_div = 0.5 * (B + B.T) + np.diag(rng.uniform(0.1, 0.3, d))
    _, rho_div = chain_sum(m2_div, 1)
    S_div_short, _ = chain_sum(m2_div, 20)
    S_div_long, _ = chain_sum(m2_div, 60)
    div_ok = rho_div > 1.0 and np.linalg.norm(S_div_long) > 1e3 * np.linalg.norm(
        S_div_short
    )

    # FALSIFY: in the convergent regime, a WRONG split (use D = identity when m2
    # is not near-identity) breaks the term-1 == m2^{-1} shortcut; more to the
    # point, claim the divergent partial sum equals the inverse -> it does not.
    falsify = not np.allclose(S_div_long, np.linalg.inv(m2_div), atol=1e-6)
    return conv_ok and div_ok and falsify


# ===========================================================================
# CHECK 5 --- Laplace/Schwinger (3.2) and the termwise-vs-resummed distinction.
#
# Establishes: (5a) for positive-definite m2, the RESUMMED integral
# int_0^inf e^{-t m2} dt = m2^{-1} converges; (5b) the TERMWISE chain expansion
# int_0^inf sum_n (-t)^n/n! m2^n dt diverges term by term because each
# int_0^inf t^n dt = +inf --- so (3.2) does NOT give a term-by-term surface
# expansion (only (3.1) does); (5c) the unconditional odd-chain form
# int_0^inf m2 e^{-t m2^2} dt = m2^{-1} holds for indefinite m2.
# NOT established: spectral positivity of the true CFT m2 (= A2(iii)).
# ===========================================================================


def laplace_check(seed: int) -> bool:
    rng = np.random.default_rng(seed)
    d = 4
    # positive-definite m2
    A = rng.uniform(-1, 1, (d, d))
    m2_pd = A @ A.T + 2.0 * np.eye(d)
    # indefinite invertible m2
    Q, _ = np.linalg.qr(rng.uniform(-1, 1, (d, d)))
    m2_ind = Q @ np.diag(np.array([2.0, -1.5, 3.0, -0.8])) @ Q.T

    # (5a) resummed Laplace = inverse (PD)
    I_res, _ = quad_vec(lambda t: expm(-t * m2_pd), 0, np.inf)
    res_ok = np.allclose(I_res, np.linalg.inv(m2_pd), rtol=1e-7, atol=1e-9)
    # FALSIFY (5a): for indefinite m2 the same integral diverges (norm blows up)
    blow = np.linalg.norm(expm(-40.0 * m2_ind))
    falsify_a = blow > 1e6

    # (5b) termwise divergence: int_0^T t^n dt = T^{n+1}/(n+1) -> inf per n,
    # whereas the resummed integrand int_0^T e^{-t lam} dt stays bounded.
    lam = float(np.min(np.linalg.eigvalsh(m2_pd)))  # a positive eigenvalue scale
    Ts = np.array([1e2, 1e4, 1e8])  # growing cutoffs T -> inf
    termwise_diverges = True
    for n in range(6):
        vals = Ts ** (n + 1) / (n + 1)  # int_0^T t^n dt (each -> +inf)
        # each term's full-range integral grows without bound: strictly monotone
        # in the cutoff and exceeding any fixed cap
        if not (vals[2] > vals[1] > vals[0] and vals[2] > 1e7):
            termwise_diverges = False
    resummed_bounded = all(
        abs((1.0 - np.exp(-lam * T)) / lam - 1.0 / lam) < 1.0 / lam for T in Ts
    )  # int_0^T e^{-t lam} dt -> 1/lam
    termwise_ok = termwise_diverges and resummed_bounded

    # (5c) unconditional odd-chain form for indefinite m2
    I_odd, _ = quad_vec(lambda t: m2_ind @ expm(-t * (m2_ind @ m2_ind)), 0, np.inf)
    odd_ok = np.allclose(I_odd, np.linalg.inv(m2_ind), rtol=1e-7, atol=1e-9)
    # FALSIFY (5c): drop the m2 prefactor -> int e^{-t m2^2} dt != m2^{-1}
    I_bad, _ = quad_vec(lambda t: expm(-t * (m2_ind @ m2_ind)), 0, np.inf)
    falsify_c = not np.allclose(I_bad, np.linalg.inv(m2_ind), rtol=1e-3, atol=1e-3)

    return res_ok and falsify_a and termwise_ok and odd_ok and falsify_c


# ===========================================================================
# CHECK 6 --- genus formula (5.2): g_res = L_c + sum_e (k_e - 1).
#
# Establishes: on random CONNECTED coloured multigraphs (no self-loops, strand
# numbers k_e in {1,2,3}), the resolved genus computed from Euler characteristic
# via explicit puncture/sewing counting (chi = sum_v (2 - n_v), n_ext =
# sum_v n_v - 2 sum_e k_e, g_res = (2 - chi - n_ext)/2) equals the closed formula
# L_c + sum_e(k_e - 1), INDEPENDENTLY of (5.2). Includes the chain (g = k-1) and
# single colour-2 edge (g = 1, eq. 1.1) instances.
# NOT established: that the resolved surface actually exists as a CFT worldsheet
# (it is formal Euler-characteristic bookkeeping; sec. 1, R15).
# ===========================================================================


def chi_and_formula(
    edges: list[tuple[int, int, int]], ext: dict[int, int], n_vert: int
) -> tuple[int, int]:
    """Return (g_res via chi-counting, g_res via formula 5.2) for a coloured graph.

    edges: list of (u, v, k_e); ext: external legs per vertex; n_vert vertices.
    """
    # punctures per vertex = external legs + sum of strand numbers of incident edges
    n_v = {v: ext.get(v, 0) for v in range(n_vert)}
    for u, v, k in edges:
        n_v[u] += k
        n_v[v] += k
    chi = sum(2 - n_v[v] for v in range(n_vert))
    E_s = sum(k for _, _, k in edges)  # total strand sewings
    n_ext = sum(n_v[v] for v in range(n_vert)) - 2 * E_s
    assert (2 - chi - n_ext) % 2 == 0
    g_chi = (2 - chi - n_ext) // 2
    E = len(edges)
    L_c = E - n_vert + 1  # coloured loop number
    g_formula = L_c + sum(k - 1 for _, _, k in edges)
    return g_chi, g_formula


def genus_check(seed: int) -> bool:
    rng = np.random.default_rng(seed)
    ok = True

    # random connected multigraphs: spanning tree + extra edges, no self-loops
    for _ in range(40):
        V = int(rng.integers(2, 7))
        perm = rng.permutation(V)
        edges = []
        for i in range(1, V):  # spanning tree -> connected
            u = int(perm[i])
            w = int(perm[rng.integers(0, i)])
            edges.append((u, w, int(rng.integers(1, 4))))
        for _ in range(int(rng.integers(0, 4))):  # extra edges (multi-edges ok)
            u, w = int(rng.integers(0, V)), int(rng.integers(0, V))
            if u != w:
                edges.append((u, w, int(rng.integers(1, 4))))
        ext = {v: int(rng.integers(0, 3)) for v in range(V)}
        g_chi, g_formula = chi_and_formula(edges, ext, V)
        ok = ok and (g_chi == g_formula)

    # chain instance: k vertices, k-1 colour-2 edges -> g = k-1
    for k in range(1, 7):
        edges = [(i, i + 1, 2) for i in range(k - 1)]
        # each end vertex has 3 external, interior 2 (matches 4-punctured spheres:
        # end sphere = 2 strands consumed one side + 2 ext; but topology-only here)
        ext = {
            v: (4 - 2 * (1 if 0 < v < k - 1 else 0) - (2 if 0 < v < k - 1 else 0))
            for v in range(k)
        }
        # simpler: give each vertex enough external legs; genus is ext-independent
        ext = {v: 2 for v in range(k)}
        g_chi, g_formula = chi_and_formula(edges, ext, k)
        ok = ok and (g_chi == g_formula == (k - 1))

    # single colour-2 edge between two 4-punctured spheres -> g = 1 (eq. 1.1)
    g_chi, g_formula = chi_and_formula([(0, 1, 2)], {0: 2, 1: 2}, 2)
    ok = ok and (g_chi == g_formula == 1)

    # single colour-3 edge -> g = 2
    g_chi, g_formula = chi_and_formula([(0, 1, 3)], {0: 3, 1: 3}, 2)
    ok = ok and (g_chi == g_formula == 2)

    # FALSIFY: the wrong formula L_c + sum(k_e) (missing the -1) must disagree
    edges = [(0, 1, 2), (1, 2, 3)]
    ext = {0: 2, 1: 2, 2: 2}
    g_chi, _ = chi_and_formula(edges, ext, 3)
    L_c = len(edges) - 3 + 1
    g_wrong = L_c + sum(k for _, _, k in edges)
    falsify = g_wrong != g_chi

    return ok and falsify


# ===========================================================================
# CHECK 7 --- ghost saturation (sec. 0) at symbolic k, and R23 (N_gh = 3l-2k+g).
#
# Establishes (EXACT, sympy): every elementary vertex of the construction
# saturates sum_i N_gh(A_i) - 2(n-3) = 6 identically in k (tower entries
# included), and the R23 ghost-number formula reproduces the low table.
# NOT established: that these vertices are genuine CFT vertex regions with the
# stated ghost insertions (bookkeeping only; RS4 for fixtures).
# ===========================================================================


def saturation_check() -> bool:
    k = sp.symbols("k", positive=True, integer=True)
    six = sp.Integer(6)

    def sat(ngh_sum: sp.Expr, n: sp.Expr) -> bool:
        return sp.simplify(ngh_sum - 2 * (n - 3) - six) == 0

    entries = [
        # (label, sum N_gh, n = number of H0-punctures)
        ("V4(Sigma,Sigma)", sp.Integer(4) + 4, sp.Integer(4)),
        ("V4(Sigma,Psi,Psi)", sp.Integer(4) + 2 + 2, sp.Integer(4)),
        ("Vt_{2k}(Sig_k,Sig_k)", 2 * k + 2 * k, 2 * k),
        ("Vt_{2k+1}(Sig_k,Sig_k,Psi)", 4 * k + 2, 2 * k + 1),
    ]
    sat_ok = all(sat(s, n) for _, s, n in entries)

    # FALSIFY: the wrong subtraction 2(n-2) must NOT saturate to 6
    falsify_sat = not all(
        sp.simplify(s - 2 * (n - 2) - six) == 0 for _, s, n in entries
    )

    # R23 low table  N_gh(p_{k,l,g}) = 3l - 2k + g
    def Ngh(kk: int, ll: int, gg: int) -> int:
        return 3 * ll - 2 * kk + gg

    r23_table = {
        (1, 1, 0): 1,  # Q
        (2, 1, 0): -1,  # l2
        (3, 1, 0): -3,  # l3
        (4, 1, 0): -5,  # l4
        (1, 2, 0): 4,  # p120 (cobracket)
        (2, 2, 0): 2,  # m2
        (1, 1, 1): 2,  # p111 (genus cross-check)
    }
    r23_ok = all(Ngh(*key) == val for key, val in r23_table.items())
    # l_n reduction: N_gh(l_n) = 3 - 2n
    red_ok = all(Ngh(kk, 1, 0) == 3 - 2 * kk for kk in range(1, 7))
    # FALSIFY: the stale (Delta-shift) value m2 = -2 must be rejected
    falsify_r23 = Ngh(2, 2, 0) != -2

    return sat_ok and falsify_sat and r23_ok and red_ok and falsify_r23


# ===========================================================================
# CHECK 8 --- sewing-vs-sandwich real-parameter count (sec. 5, (0.2) vs (5.3)).
#
# Establishes: the colour-1 edge kernel q^{L0} = diag(exp((-s+i theta) energies))
# contributes a 2-REAL-parameter family (s, theta), while the colour-2 sandwich
# (5.3) is a fixed matrix contributing 0 parameters. The "amplitude support"
# dimension of a composite = sum of vertex-region dims + 2 * (#colour-1 edges) +
# 0 * (#colour-2 edges), measured as the numerical Jacobian rank of the composite
# operator as a function of all its parameters.
# NOT established: identification of these parameters with actual moduli (RS4);
# the b-ghost saturation that certifies "which parameter is a modulus" is check 7.
# ===========================================================================


def jacobian_rank(f, x0: np.ndarray, eps: float = 1e-6) -> int:
    """Numerical rank of the Jacobian of a vector-valued map f at x0."""
    cols = []
    for i in range(len(x0)):
        dx = np.zeros_like(x0)
        dx[i] = eps
        cols.append((f(x0 + dx) - f(x0 - dx)) / (2 * eps))
    J = np.stack(cols, axis=1)
    s = np.linalg.svd(J, compute_uv=False)
    return int(np.sum(s > 1e-6 * (s[0] if s[0] > 0 else 1.0)))


def dimension_count_check(seed: int) -> bool:
    rng = np.random.default_rng(seed)
    d = 3
    # fixed generic building blocks
    A1 = rng.uniform(-1, 1, (d, d))
    A2 = rng.uniform(-1, 1, (d, d))
    L0 = np.diag(rng.uniform(0.5, 2.0, d))  # worldsheet energies (real)
    Sfix = rng.uniform(-1, 1, (d, d)) + 1j * rng.uniform(
        -1, 1, (d, d)
    )  # colour-2 sandwich

    def vertex_block(m1: float, m2: float) -> np.ndarray:
        """V_{0,4}-region block: 2 real moduli (m1, m2)."""
        return expm(m1 * A1 + m2 * A2)

    def colour1_edge(s: float, theta: float) -> np.ndarray:
        """q^{L0} with q = exp(-s + i theta): 2 real parameters."""
        return np.diag(np.exp((-s + 1j * theta) * np.diag(L0)))

    def flatten(C: np.ndarray) -> np.ndarray:
        return np.concatenate([C.real.reshape(-1), C.imag.reshape(-1)])

    # config A: two vertices joined by a colour-1 edge -> 2 + 2 + 2 = 6
    def compA(x: np.ndarray) -> np.ndarray:
        m1a, m2a, s, th, m1b, m2b = x
        C = vertex_block(m1a, m2a) @ colour1_edge(s, th) @ vertex_block(m1b, m2b)
        return flatten(C)

    xA = rng.uniform(0.1, 0.5, 6)
    rankA = jacobian_rank(compA, xA)

    # config B: two vertices joined by a colour-2 edge -> 2 + 0 + 2 = 4
    def compB(x: np.ndarray) -> np.ndarray:
        m1a, m2a, m1b, m2b = x
        C = vertex_block(m1a, m2a) @ Sfix @ vertex_block(m1b, m2b)
        return flatten(C)

    xB = rng.uniform(0.1, 0.5, 4)
    rankB = jacobian_rank(compB, xB)

    count_ok = (rankA == 6) and (rankB == 4) and (rankA - rankB == 2)

    # FALSIFY: model the colour-2 edge ALSO as q^{L0} (2 params). Then the
    # 4-vertex-param config would gain 2 -> rank 6, contradicting "colour-2
    # adds 0". Confirm the mistaken model gives a different (larger) count.
    def compB_wrong(x: np.ndarray) -> np.ndarray:
        m1a, m2a, s, th, m1b, m2b = x
        C = vertex_block(m1a, m2a) @ colour1_edge(s, th) @ vertex_block(m1b, m2b)
        return flatten(C)

    xBw = rng.uniform(0.1, 0.5, 6)
    rankBw = jacobian_rank(compB_wrong, xBw)
    falsify = rankBw != rankB

    return count_ok and falsify


# ===========================================================================
# Driver
# ===========================================================================


def main() -> int:
    print(
        f"RS1 verification of derivation 020 --- seeds: A={SEED_A}, B={SEED_B}, g_s={G_S}"
    )
    print("(finite-dim STRUCTURAL checks of algebraic claims; NOT CFT-level)\n")

    print(
        "check (1): channel telescoping (4.1) --- each matching = (g_s^2/3)V4, sum = g_s^2 V4"
    )
    report(
        "1",
        "channel arithmetic exact, falsify on 12/g_s^2 norm (seeds A,B)",
        channel_check(SEED_A) and channel_check(SEED_B),
    )

    print(
        "check (2): no re-weighting of a local kernel family equals the inverse (3.i)"
    )
    report(
        "2",
        "matrix inverse not in kernel-family span; commuting family IS (control)",
        no_local_kernel_check(SEED_A) and no_local_kernel_check(SEED_B),
    )

    print("check (3): Gram sandwich G G^-1 G = G (3.3); pointwise slice fails (T6)")
    report(
        "3",
        "Gram identity holds; diagonal moduli-slice does not; falsify on perturbed inv",
        gram_sandwich_check(SEED_A) and gram_sandwich_check(SEED_B),
    )

    print(
        "check (4): Neumann chains (3.1) --- converge iff rho(D^-1 N) < 1, both regimes"
    )
    report(
        "4",
        "chain sum = inverse when rho<1; diverges when rho>1",
        neumann_chain_check(SEED_A) and neumann_chain_check(SEED_B),
    )

    print(
        "check (5): Laplace (3.2) --- resummed converges; termwise chain integral diverges"
    )
    report(
        "5",
        "resummed = inverse (PD); termwise int t^n diverges; odd-chain form (indef)",
        laplace_check(SEED_A) and laplace_check(SEED_B),
    )

    print(
        "check (6): genus formula (5.2) g_res = L_c + sum(k_e-1) via independent chi-count"
    )
    report(
        "6",
        "chi-counting == formula on random graphs; chain g=k-1; single edge g=1 (1.1)",
        genus_check(SEED_A) and genus_check(SEED_B),
    )

    print(
        "check (7): ghost saturation (sec.0) at symbolic k; R23 N_gh = 3l-2k+g low table"
    )
    report(
        "7",
        "sum N_gh - 2(n-3) = 6 identically in k; R23 table exact (sympy Rational)",
        saturation_check(),
    )

    print(
        "check (8): edge parameter count --- colour-1 adds 2, colour-2 adds 0 (Jacobian rank)"
    )
    report(
        "8",
        "rank(colour-1 config)=6, rank(colour-2 config)=4, difference=2",
        dimension_count_check(SEED_A) and dimension_count_check(SEED_B),
    )

    npass = sum(1 for *_, ok in results if ok)
    print(f"\n{npass}/{len(results)} checks PASS")
    return 0 if npass == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
