"""Verify derivation 023 (Phase A): the 4-point amplitude chain HS -> telescoping -> SFT.

Companion to `agent/derivations/023-a4pt-virasoro-shapiro-chain.md` (brief
computator-a4pt-chain-20260715T000000; plan `plans/amplitude-check-plan-2026-07-14.md`
Phase A, steps A1-A5). Finite-dimensional model: H_0 = R^N, totally symmetric vertices,
generic non-diagonal kinetic K and pairing metric g (so G_2 is non-diagonal on Sym^2).

What IS verified (finite-dimensional algebraic layer, exact rational arithmetic):
  1. A1 diagram enumeration + amplitude-normalized prefactors: the connected amputated
     4-point kernel of the HS theory at O(g_s^2), computed MECHANICALLY from the joint
     (Psi, Sigma) Gaussian (source-shift trick, exp(L) moment operator — no diagrams
     input by hand), equals (a) the same mechanical object for the quartic-truncated
     standard action S_eff at ALL orders in the external parameters t (so every n-point
     kernel, loops included, not only 4-point), and (b) the HAND-enumerated diagram sum
     [3 V3-exchange channels + Sigma-exchange with vertex (g_s^2/6)V4(.,psi_i x psi_j),
     propagator (12/g_s^2)(V4|Sym2)^{-1}, 3 matchings] for the multilinear t1t2t3t4
     part, and (c) the O(g_s) 3-point vertex normalization g_s C(psi1,psi2,psi3).
     This is NEW relative to codes/verify-a1-telescoping.py (which never included the
     V3 sector nor a mechanical, enumeration-free path-integral expansion).
  2. H1's finite-dim shadow with NON-diagonal G_2 and degenerate V4: source _|_ ker
     (an identity, see the note at the check — it cannot fail), the m_2-form propagator
     pinv(m_2) G_2^{-1} telescopes (pinv(m_2) m_2 = id on the kernel quotient =
     rowspace(m_2), NOT on the image: m_2 = G_2^{-1} V4 is not symmetric in general),
     and the exchange still equals the contact kernel.
  3. THE TAUTOLOGY TRAP (plan section 0): the truncated telescoping
     V4' pinv(V4') V4' = V4' holds IDENTICALLY for arbitrary — including corrupted —
     totally symmetric V4', so a truncated exchange-vs-contact comparison verifies
     nothing. The PASS on garbage input is the point being demonstrated.
  4. Teeth (falsifiability of the layers that DO carry content): the cross-object
     equality breaks under (a) kinetic-vs-source V4 mismatch, (b) source coefficient
     2 -> 1 (gives exactly 1/4), (c) mismatched G_2 in the m_2-form propagator,
     (d) dropping one V3 channel from the hand enumeration of check 1.
  5. THE RESOLUTION (the one falsifiable numerical statement, R27 item 3.ii / R28):
     the Neumann/frozen-neck-chain representation m_2^{-1} = sum_n (D^{-1}N)^n D^{-1}
     reproduces the contact vertex iff rho(D^{-1}N) < 1; a model with rho >= 1 has
     divergent partial sums (surface-represented exchange fails) while the ALGEBRAIC
     inverse still telescopes exactly on the same model.
  6. H2's finite-dim shadow, LEVEL PART ONLY: deleting one intermediate state from the
     Sym^2 state sum between vertex and propagator breaks exchange = contact; the full
     sum restores it (completeness of the intermediate two-string state sum over the
     strands' levels is load-bearing). The model has no momentum direction, so the
     relative-momentum integral that H2 also covers is not exercised (023 section 1, H2).

Model size. N = 2, so dim Sym^2 = 3: every matrix statement below (check 2's
"rank 2 < 3", check 6's deletion of one of three intermediate states, and all of
check 5's spectral data) lives on 3x3 matrices. The model has NO level structure, so
`D = diag(Gm)` is a full diagonal part, not a level-diagonal part; check 5 therefore
says nothing about the level-diagonal dominance of PH21.

Scope note (023 sections 0, 5.1). The model here is finite-dimensional: finitely many
levels AND the pair's relative momentum suppressed. The tautology trap of check 3 is a
statement about THAT model. A level truncation of the actual theory does not truncate
the momentum integral, so the collapse at fixed level is not a finite matrix identity
there and whether a truncated comparison carries information is open.

What is NOT verified here (carried as named hypotheses / citations in 023):
  - H1 at CFT level, restated 2026-09-22 WITHOUT any auxiliary inner product (023
    section 1): (a) the kernels of the level-truncated forms stabilise,
    ker V4^(L) = ker V4 ∩ {level <= L} for large L, so the quotient Sym^2 H_0 / ker V4
    and the level-by-level Sigma-propagator have a limit; (b) at the external momenta
    used — the tachyon shell included, where det V4^(L)(P^2) is not known to be nonzero
    (ledger PH18) — the truncated determinant on the quotient has no zero persisting
    with the level. Neither clause is testable in this model: it has one fixed
    dimension and no sequence of levels. No bounded inverse is assumed anywhere; the
    singular values of the truncated m2 are a basis- and frame-dependent CONDITIONING
    DIAGNOSTIC, not a falsifier.
  - H2 at CFT level: convergence/completeness of the intermediate two-string sum over
    BOTH the two strands' levels and the pair's relative momentum k_a (R33 annotation
    on R27; derivation 031 sections 4.3, 7), including the interchange clause added
    2026-09-22 — the partial sums must still converge after m2^{-1} is applied, which
    is the only analytic input of the telescoping step — A2(iii), RS6 numerics, Phase B
    of the amplitude plan. The level truncation of the model bounds the first part only.
  - The standard-SFT -> Virasoro-Shapiro on-shell endpoint (textbook; Erbin 2023,
    arXiv:2301.01686; cited in 023 section A3, not re-derived).

Conventions: Z = int e^{S}, correlators by Wick contraction (no explicit i's),
S_HS = -1/2 K(Psi,Psi) + (g_s/3!) C(Psi^3) - (g_s^2/4!) V4(Sigma,Sigma)
      + (2 g_s^2/4!) V4(Sigma, Psi x Psi)   [eq:SHS, R1],
S_eff = same Psi-sector + (g_s^2/4!) V4(Psi x Psi, Psi x Psi)  [R10].
All arithmetic exact (sympy Rationals) except check 5's spectral radii / partial-sum
errors (floats, seeded, printed).

References: agent/derivations/007-a1-amplitude-telescoping.md (R14);
agent/derivations/020-riemann-m2-geometric.md (R27, eq. 3.1);
agent/derivations/022-rs5-no-local-kernel-theorem.md (R28);
plans/amplitude-check-plan-2026-07-14.md section 0 (tautology trap).
"""

from __future__ import annotations

import random
import sys

import sympy as sp

SEED = 20260715
random.seed(SEED)
print(f"seed = {SEED}")

gs = sp.symbols("g_s", positive=True)
t1, t2, t3, t4 = ts = sp.symbols("t1 t2 t3 t4")

results: list[tuple[int, str, bool]] = []


def report(num: int, label: str, ok: bool) -> None:
    results.append((num, label, ok))
    print(f"  check ({num}) {'PASS' if ok else 'FAIL'} — {label}")


# ----------------------------------------------------------------------------
# Machinery: random tensors, Sym^2 bases, Gaussian moment operator
# ----------------------------------------------------------------------------

def rand_rat(lo: int = -9, hi: int = 9) -> sp.Rational:
    return sp.Rational(random.randint(lo, hi), random.randint(1, 3))


def rand_vec(N: int) -> list[sp.Rational]:
    return [rand_rat() for _ in range(N)]


def random_symmetric_V4(N: int, terms: int | None = None):
    """Totally symmetric V_{abcd} = sum_r c_r u_r^{x4} (generic rank = min(terms, dim Sym^2))."""
    dim_sym = N * (N + 1) // 2
    if terms is None:
        terms = dim_sym + 2
    V = [[[[sp.Integer(0)] * N for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for _ in range(terms):
        c = sp.Rational(random.randint(1, 5), random.randint(1, 3)) * random.choice([1, -1])
        u = rand_vec(N)
        for a in range(N):
            for b in range(N):
                for cc in range(N):
                    for d in range(N):
                        V[a][b][cc][d] += c * u[a] * u[b] * u[cc] * u[d]
    return V


def random_symmetric_C3(N: int):
    """Totally symmetric C_{abc}, generic (direct symmetrized random entries)."""
    C = [[[sp.Integer(0)] * N for _ in range(N)] for _ in range(N)]
    for a in range(N):
        for b in range(a, N):
            for c in range(b, N):
                val = rand_rat()
                for p in {(a, b, c), (a, c, b), (b, a, c), (b, c, a), (c, a, b), (c, b, a)}:
                    C[p[0]][p[1]][p[2]] = val
    return C


def random_sym_invertible(N: int) -> sp.Matrix:
    """Random symmetric invertible (generically non-diagonal) rational matrix."""
    while True:
        M = sp.Matrix(N, N, lambda i, j: 0)
        for i in range(N):
            for j in range(i, N):
                M[i, j] = M[j, i] = rand_rat()
        if M.det() != 0:
            return M


def V4_states(V, N, p, q, r, s):
    """V4(p,q,r,s) = V_{abcd} p^a q^b r^c s^d."""
    return sp.expand(sum(
        V[a][b][c][d] * p[a] * q[b] * r[c] * s[d]
        for a in range(N) for b in range(N) for c in range(N) for d in range(N)))


def lambda_basis(N: int) -> list[sp.Matrix]:
    """Euclidean-orthonormal basis of Sym^2 R^N: E_aa and (E_ab+E_ba)/sqrt2 (a<b)."""
    basis = []
    for a in range(N):
        m = sp.zeros(N, N)
        m[a, a] = 1
        basis.append(m)
    for a in range(N):
        for b in range(a + 1, N):
            m = sp.zeros(N, N)
            m[a, b] = m[b, a] = 1 / sp.sqrt(2)
            basis.append(m)
    return basis


def gram_matrix(V, N: int, basis) -> sp.Matrix:
    """G_IJ = V4(lambda_I, lambda_J) — the Sym^2 Gram matrix of the quartic vertex."""
    d = len(basis)
    return sp.Matrix(d, d, lambda I, J: sum(
        V[a][b][c][e] * basis[I][a, b] * basis[J][c, e]
        for a in range(N) for b in range(N) for c in range(N) for e in range(N)))


def source_vec(V, N: int, basis, x, y) -> sp.Matrix:
    """b_I = V4(lambda_I, x (x) y) — the Sigma-source of an external pair (x, y)."""
    return sp.Matrix([sum(
        V[a][b][c][e] * basis[I][a, b] * x[c] * y[e]
        for a in range(N) for b in range(N) for c in range(N) for e in range(N))
        for I in range(len(basis))])


MATCHINGS = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]


def exchange_diagram(V, N, psis, prop_sym2: sp.Matrix, source_coeff=2) -> sp.Expr:
    """Sigma-exchange 4-point kernel, amplitude normalization, distinct externals.

    vertex(i,j) = (source_coeff * g_s^2/12) * 2 * V4(lambda_I, psi_i (x) psi_j)
                  [= (g_s^2/6) V4 for the eq:SHS value source_coeff = 2],
    propagator  = (12/g_s^2) * prop_sym2 in the orthonormal lambda_I basis,
    summed over the 3 perfect matchings (R14 rules).
    """
    basis = lambda_basis(N)
    total = sp.Integer(0)
    for (i, j), (k, l) in MATCHINGS:
        vij = 2 * source_coeff * gs**2 / 24 * source_vec(V, N, basis, psis[i], psis[j])
        vkl = 2 * source_coeff * gs**2 / 24 * source_vec(V, N, basis, psis[k], psis[l])
        total += (vij.T * (12 / gs**2 * prop_sym2) * vkl)[0, 0]
    return sp.expand(total)


def gauss_expect(P: sp.Expr, variables: list[sp.Symbol], cov: sp.Matrix) -> sp.Expr:
    """Gaussian expectation of a polynomial: E[P] = exp(1/2 sum cov_ij d_i d_j) P |_{x=0}.

    Exact for polynomials (the operator nilpotent above the degree); this encodes
    Isserlis/Wick without enumerating pairings.
    """
    n = len(variables)
    term = sp.expand(P)
    total = term.subs({v: 0 for v in variables})
    m = 1
    while True:
        term = sp.expand(sp.Rational(1, 2) / m * sum(
            cov[i, j] * sp.diff(term, variables[i], variables[j])
            for i in range(n) for j in range(n)))
        if term == 0:
            break
        total += term.subs({v: 0 for v in variables})
        m += 1
    return sp.expand(total)


# ----------------------------------------------------------------------------
# Model for check 1: N = 2, generic K, C, V4 (non-degenerate), distinct externals
# ----------------------------------------------------------------------------
N = 2
K = random_sym_invertible(N)          # Psi-kinetic: S ⊃ -1/2 Psi.K.Psi
Kinv = K.inv()
C3 = random_symmetric_C3(N)           # cubic vertex C_{abc}
V4T = random_symmetric_V4(N)          # quartic vertex V_{abcd}, generic on Sym^2
psis = [rand_vec(N) for _ in range(4)]
basisN = lambda_basis(N)
G = gram_matrix(V4T, N, basisN)
assert G.det() != 0, "generic draw should be non-degenerate on Sym^2"
Ginv = G.inv()

# fluctuation symbols and background shift Psi -> pb + Phi(t), Phi = sum_i t_i psi_i
pb = list(sp.symbols(f"pb0:{N}"))
Phi = [sum(ts[i] * psis[i][a] for i in range(4)) for a in range(N)]
Psi_sh = [pb[a] + Phi[a] for a in range(N)]

# interactions, shifted (source-shift trick: J = K * sum t_i psi_i amputates legs
# exactly onto the external states psi_i; see 023 section A1)
A_int = gs / 6 * sp.expand(sum(
    C3[a][b][c] * Psi_sh[a] * Psi_sh[b] * Psi_sh[c]
    for a in range(N) for b in range(N) for c in range(N)))
# Sigma-source B = (2 g_s^2/4!) V4(Sigma, Psi x Psi) = sum_I sigma_I bI; only <B^2>_Sigma
# survives at O(g_s^2) (B linear in Sigma: <B> = 0; higher powers are O(g_s^3+) or odd)
bI = [gs**2 / 12 * sp.expand(sum(
    V4T[a][b][c][e] * basisN[I][a, b] * Psi_sh[c] * Psi_sh[e]
    for a in range(N) for b in range(N) for c in range(N) for e in range(N)))
    for I in range(len(basisN))]
cov_sigma = 12 / gs**2 * Ginv          # Wick covariance of the sigma_I coefficients
B2_sigma = sp.expand(sum(
    cov_sigma[I, J] * bI[I] * bI[J]
    for I in range(len(basisN)) for J in range(len(basisN))))
# quartic contact of S_eff, shifted
Q4 = gs**2 / 24 * sp.expand(sum(
    V4T[a][b][c][e] * Psi_sh[a] * Psi_sh[b] * Psi_sh[c] * Psi_sh[e]
    for a in range(N) for b in range(N) for c in range(N) for e in range(N)))

# ----------------------------------------------------------------------------
# Check 1 — A1: mechanical path-integral expansion == hand-enumerated diagram sum
# ----------------------------------------------------------------------------
print("check (1): mechanical (Psi,Sigma) expansion at O(gs^2): HS == eff (all t) == hand sum")
# E(t) = <exp(S_int)>_{pb,sigma} to O(g_s^2): terms 1 + A + A^2/2 + <B^2>_Sigma/2.
# (A+B)^k, k>=3, and the dropped k=2 cross term AB are O(g_s^3) after Sigma-Wick or
# vanish (odd in sigma) — the mechanical counterpart of the enumeration lemma in 023 A1.
E_HS = sp.expand(
    gauss_expect(1 + A_int + A_int**2 / 2, pb, Kinv)
    + gauss_expect(B2_sigma, pb, Kinv) / 2)
E_eff = sp.expand(
    gauss_expect(1 + A_int + A_int**2 / 2, pb, Kinv)
    + gauss_expect(Q4, pb, Kinv))
W_HS = sp.expand(sp.series(sp.log(E_HS), gs, 0, 3).removeO())
W_eff = sp.expand(sp.series(sp.log(E_eff), gs, 0, 3).removeO())
ok1a = sp.expand(W_HS - W_eff) == 0                       # all orders in t, loops included

# multilinear t1t2t3t4 part = amputated connected 4-point kernel Gamma_4 at O(g_s^2)
Gamma_mech = sp.diff(W_HS, t1, t2, t3, t4).subs({t: 0 for t in ts})
# hand enumeration, amplitude normalization (distinct externals, symmetry factors 1):
#   3 V3-exchange channels: g_s C(psi_i,psi_j,.) o K^{-1} o g_s C(.,psi_k,psi_l)
#   Sigma-exchange: R14 rules (vertex g_s^2/6, propagator (12/g_s^2) Ginv, 3 matchings)
def C_pair(x, y):
    return sp.Matrix([sum(C3[a][b][c] * x[b] * y[c] for b in range(N) for c in range(N))
                      for a in range(N)])

hand_v3 = sp.expand(sum(
    gs**2 * (C_pair(psis[i], psis[j]).T * Kinv * C_pair(psis[k], psis[l]))[0, 0]
    for (i, j), (k, l) in MATCHINGS))
hand_sigma = exchange_diagram(V4T, N, psis, Ginv)
ok1b = sp.expand(Gamma_mech - hand_v3 - hand_sigma) == 0
# R14 reuse: the Sigma-exchange part telescopes to exactly g_s^2 V4(psi_1..psi_4)
ok1c = sp.expand(hand_sigma - gs**2 * V4_states(V4T, N, *psis)) == 0
# 3-point normalization at O(g_s): coeff of t1t2t3 == g_s C(psi_1,psi_2,psi_3)
Gamma3_mech = sp.diff(W_HS, t1, t2, t3).subs({t: 0 for t in ts})
Gamma3_mech = sp.expand(Gamma3_mech).coeff(gs, 1) * gs
hand_c3 = gs * sum(C3[a][b][c] * psis[0][a] * psis[1][b] * psis[2][c]
                   for a in range(N) for b in range(N) for c in range(N))
ok1d = sp.expand(Gamma3_mech - hand_c3) == 0
report(1, "W_HS == W_eff at O(gs^2) (all t); d4W == [3 V3-channels + Sigma-exch]; "
          "Sigma-exch == gs^2 V4; 3-pt vertex == gs C", ok1a and ok1b and ok1c and ok1d)

# ----------------------------------------------------------------------------
# Check 2 — H1 finite-dim shadow: non-diagonal G_2, degenerate V4, kernel quotient
# ----------------------------------------------------------------------------
print("check (2): H1 shadow — pinv(m2) m2 = id on the kernel quotient (rowspace);"
      " m2-form propagator telescopes;"
      " exchange == contact (non-diagonal G_2, ker V4 != 0)")
g_met = random_sym_invertible(N)      # non-diagonal pairing metric on H_0
# G_2 on Sym^2 in the lambda basis: (G2)_IJ = tr(lambda_I g lambda_J g)
G2m = sp.Matrix(len(basisN), len(basisN),
                lambda I, J: sp.expand((basisN[I] * g_met * basisN[J] * g_met).trace()))
assert G2m.det() != 0
V_deg = random_symmetric_V4(N, terms=2)      # rank <= 2 < dim Sym^2 = 3
G_deg = gram_matrix(V_deg, N, basisN)
ok2_rank = G_deg.rank() < len(basisN)
m2 = G2m.inv() * G_deg                        # m_2 = G_2^{-1} V4 (R9 dictionary)
m2p = m2.pinv()
# H1 on the quotient: pinv(m2) m2 = orthogonal projector onto rowspace(m2) = complement
# of ker m2 = ker V4 (the kernel quotient); the identity holds on that quotient, not on
# all of Sym^2 and not on the image (m2 = G_2^{-1} V4 is not symmetric in general)
proj = sp.simplify(m2p * m2)
ok2_proj = sp.simplify(proj * proj - proj) == sp.zeros(*proj.shape) \
    and sp.simplify(proj.T - proj) == sp.zeros(*proj.shape) \
    and proj.rank() == m2.rank() != len(basisN)
# sources are automatically _|_ ker (R14 section 6, now with non-diagonal G_2).
# NOTE: `ok2_src` below is an IDENTITY, not a test with teeth: the source vectors are
# the rows V_deg(., x (x) y) of the same Gram whose kernel `kernel` is, so s^T kv = 0
# holds for any vertex and any states by the definition of the kernel. It records the
# correct inner-product-free statement of the kernel-decoupling half of H1; it cannot
# fail, and no corruption in check 4 gives it teeth.
kernel = G_deg.nullspace()
psis2 = [rand_vec(N) for _ in range(4)]
srcs = [source_vec(V_deg, N, basisN, psis2[i], psis2[j]) for (i, j), _ in MATCHINGS]
ok2_src = all(sp.simplify(s.T * kv)[0, 0] == 0 for s in srcs for kv in kernel)
# m_2-form propagator pinv(m2) G_2^{-1} telescopes: V4 [pinv(m2) G2^{-1}] V4 = V4
ok2_tel = sp.simplify(G_deg * (m2p * G2m.inv()) * G_deg - G_deg) == sp.zeros(*G_deg.shape)
# and the exchange diagram built from it equals the contact kernel
diag2 = exchange_diagram(V_deg, N, psis2, m2p * G2m.inv())
ok2_diag = sp.expand(diag2 - gs**2 * V4_states(V_deg, N, *psis2)) == 0
report(2, "kernel quotient: proj on rowspace; source _|_ ker (identity, no teeth); "
          "m2-form pinv telescopes; "
          "exchange == contact", ok2_rank and ok2_proj and ok2_src and ok2_tel and ok2_diag)

# ----------------------------------------------------------------------------
# Check 3 — THE TAUTOLOGY TRAP: truncated telescoping holds for ARBITRARY input
# ----------------------------------------------------------------------------
print("check (3): tautology trap — truncated telescoping PASSES even on corrupted V4"
      " (the identity cannot fail at any finite truncation)")
ok3 = True
for trial in range(5):
    # arbitrary corruption: a DIFFERENT random totally symmetric vertex, possibly
    # degenerate — no relation to the 'physical' V4T of check 1
    Vc = random_symmetric_V4(N, terms=random.choice([1, 2, 3, 5]))
    Gc = gram_matrix(Vc, N, basisN)
    Gcp = Gc.pinv()
    # (a) telescoping is an identity of the pseudo-inverse, for ANY symmetric input
    if sp.simplify(Gc * Gcp * Gc - Gc) != sp.zeros(*Gc.shape):
        ok3 = False
    # (b) the self-consistent truncated exchange-vs-contact comparison passes too —
    # with the CORRUPTED vertex used consistently in kinetic, source, and contact
    psx = [rand_vec(N) for _ in range(4)]
    diag_c = exchange_diagram(Vc, N, psx, Gcp)
    if sp.expand(diag_c - gs**2 * V4_states(Vc, N, *psx)) != 0:
        ok3 = False
report(3, "V' pinv(V') V' = V' and exchange(V')==contact(V') for 5 corrupted V' — "
          "PASS on garbage input demonstrates the truncated check is vacuous", ok3)

# ----------------------------------------------------------------------------
# Check 4 — teeth: the layers that DO carry content are falsifiable
# ----------------------------------------------------------------------------
print("check (4): teeth — cross-object corruptions break the equality")
contact = gs**2 * V4_states(V4T, N, *psis)
# (a) kinetic/source mismatch: propagator from V4T + Delta, sources from V4T
Delta = random_symmetric_V4(N, terms=1)
V_mix = [[[[V4T[a][b][c][d] + Delta[a][b][c][d] for d in range(N)] for c in range(N)]
          for b in range(N)] for a in range(N)]
G_mix = gram_matrix(V_mix, N, basisN)
diag_mix = exchange_diagram(V4T, N, psis, G_mix.inv())   # sources V4T, kinetic V_mix
ok4a = sp.expand(diag_mix - contact) != 0
# (b) source coefficient 2 -> 1 (the 2:1 ratio of eq:SHS): exchange = contact/4
diag_c1 = exchange_diagram(V4T, N, psis, Ginv, source_coeff=1)
ok4b = sp.expand(diag_c1 - contact / 4) == 0 and sp.expand(diag_c1 - contact) != 0
# (c) mismatched G_2 in the m_2-form propagator: pinv(m2) G2'^{-1} with G2' != G2
G2wrong = sp.Matrix(len(basisN), len(basisN),
                    lambda I, J: G2m[I, J] + (sp.Rational(1, 2) if I == J == 0 else 0))
m2_full = G2m.inv() * G                                  # non-degenerate model
diag_g2w = exchange_diagram(V4T, N, psis, m2_full.inv() * G2wrong.inv())
ok4c = sp.expand(diag_g2w - contact) != 0
# (d) check 1's hand sum with one V3 channel dropped no longer matches the mechanical
hand_2ch = sp.expand(sum(
    gs**2 * (C_pair(psis[i], psis[j]).T * Kinv * C_pair(psis[k], psis[l]))[0, 0]
    for (i, j), (k, l) in MATCHINGS[:2]))
ok4d = sp.expand(Gamma_mech - hand_2ch - hand_sigma) != 0
report(4, "mismatched kinetic/source V4 fails; c=1 gives 1/4; wrong G_2 fails; "
          "dropping a V3 channel fails", ok4a and ok4b and ok4c and ok4d)

# ----------------------------------------------------------------------------
# Check 5 — THE RESOLUTION: Neumann chain representation converges iff rho < 1
# ----------------------------------------------------------------------------
print("check (5): Neumann/frozen-neck-chain representation of m2^{-1} (R27 3.ii):"
      " converges iff rho(D^{-1}N) < 1; rho >= 1 breaks the surface-represented"
      " identity while the algebraic one still holds")


def neumann_data(V, N):
    """Gram G, split G = D - Noff (D = diagonal of G in the lambda basis), rho(D^-1 Noff)."""
    Gm = gram_matrix(V, N, lambda_basis(N))
    D = sp.diag(*[Gm[i, i] for i in range(Gm.shape[0])])
    assert all(D[i, i] != 0 for i in range(D.shape[0]))
    Noff = D - Gm
    T = D.inv() * Noff
    rho = max(abs(complex(ev)) for ev in sp.Matrix(T).evalf().eigenvals())
    return Gm, D, Noff, T, rho


def find_model(pred, max_draws=400):
    for _ in range(max_draws):
        V = random_symmetric_V4(N)
        Gm = gram_matrix(V, N, basisN)
        if Gm.det() == 0 or any(Gm[i, i] == 0 for i in range(Gm.shape[0])):
            continue
        _, _, _, _, rho = neumann_data(V, N)
        if pred(rho):
            return V, rho
    raise RuntimeError("no model found — enlarge the search")


V_conv, rho_conv = find_model(lambda r: r < 0.9)
V_div, rho_div = find_model(lambda r: r >= 1.05)
print(f"    model A rho = {rho_conv:.4f} (< 1), model B rho = {rho_div:.4f} (>= 1)")


def _power_iterate(
    M: sp.Matrix, iters: int = 300, tol: float = 1e-10
) -> tuple[sp.Matrix, bool]:
    """Dominant eigenvector of M by power iteration (floats, deterministic seed vector).

    Returns (v, converged). Convergence is tested on the eigenvector residual
    ||Mv - (v^T M v) v||, NOT on the iteration count: power iteration does not converge
    when the dominant eigenvalue is complex (a conjugate pair) or degenerate in modulus,
    and T = D^{-1}N has zero diagonal by construction (`Noff = D - Gm`), hence zero
    trace, so such a pair is not exotic here. A non-converged run must not be reported.

    Used only to quantify the transient discussed in 023 section 5.2: how much of the
    error functional is carried by the dominant eigendirection of D^{-1}N. No PASS/FAIL
    predicate depends on it.
    """
    n = M.shape[0]
    v = sp.Matrix([sp.Float(1 + i) for i in range(n)])
    Mf = M.evalf()
    converged = False
    for _ in range(iters):
        w = Mf * v
        nrm = sp.sqrt(sum(float(c) ** 2 for c in w))
        if nrm == 0:
            return v, False
        v = w / nrm
        lam = float((v.T * Mf * v)[0, 0])
        resid = float((Mf * v - lam * v).norm())
        converged = resid < tol * max(abs(lam), 1.0)
        if converged:
            break
    return v, converged


def _dominant_eigvec(M: sp.Matrix, gap: float = 1e-6) -> sp.Matrix | None:
    """Return the dominant eigenvector from an eigendecomposition, None if ill-defined.

    Independent route to `_power_iterate`; the two are compared in `dominant_overlap`,
    so a disagreement (slow power iteration, wrong branch) shows up instead of being
    silently reported.
    """
    best = None
    mods = []
    for lam, _mult, vecs in M.evalf().eigenvects():
        lam_c = complex(sp.N(lam))
        mods.append(abs(lam_c))
        if abs(lam_c.imag) >= gap * max(abs(lam_c), 1.0):
            continue
        if best is None or abs(lam_c) > best[0]:
            best = (abs(lam_c), sp.re(vecs[0].evalf()))
    if best is None:
        return None
    if sorted(mods)[-1] > best[0] * (1 + gap):   # dominant one is complex
        return None
    v = best[1]
    nrm = float(v.norm())
    return None if nrm == 0 else v / nrm


def _dominant_is_real_and_simple(M: sp.Matrix, gap: float = 1e-6) -> bool:
    """Test that M has a unique eigenvalue of maximal modulus and that it is real.

    Guard for the power iteration above: with a complex-conjugate or modulus-degenerate
    dominant pair the iteration has no limit and the overlap diagnostic is meaningless.
    """
    mods = []
    real_flags = []
    for lam, mult in M.evalf().eigenvals().items():
        lam_c = complex(sp.N(lam))
        for _ in range(mult):
            mods.append(abs(lam_c))
            real_flags.append(abs(lam_c.imag) < gap * max(abs(lam_c), 1.0))
    order = sorted(range(len(mods)), key=lambda i: -mods[i])
    top = order[0]
    if not real_flags[top]:
        return False
    return not (len(order) > 1 and mods[order[1]] > mods[top] * (1 - gap))


def dominant_overlap(V, psx_shared) -> float:
    """Weight of the dominant D^{-1}N mode in the error functional (023 section 5.2).

    The truncation error is B_K = sum_matchings v^T T^{K+1} G^{-1} v' (up to a constant),
    so its asymptotics are rho^{K+1} times the dominant-mode amplitude
    A = sum_m (v_m . u_1)(w_1 . x_m)/(w_1 . u_1), with u_1, w_1 the dominant right/left
    eigenvectors of T = D^{-1}N and x_m = (the inverse of the V_4 Gram matrix) v'_m.
    The number returned is |A| divided
    by sum_m |v_m||x_m|: a small value means the dominant mode is weakly excited and the
    observed rate over the first K steps differs from rho (a transient), and the same
    quantity explains a slower-than-rho growth and a faster-than-rho decay.

    Returns NaN (and the caller prints "not available") whenever the diagnostic is not
    well defined: a dominant eigenvalue that is complex or not simple, a power iteration
    that did not meet its residual tolerance, or a vanishing left-right normalisation.
    """
    Gm, D, Noff, T, _ = neumann_data(V, N)
    if not _dominant_is_real_and_simple(T):
        return float("nan")
    u1 = _dominant_eigvec(T)
    w1 = _dominant_eigvec(T.T)
    if u1 is None or w1 is None:
        return float("nan")
    # cross-check the eigendecomposition against power iteration (independent route)
    for M, v in ((T, u1), (T.T, w1)):
        p, ok_p = _power_iterate(M, iters=5000, tol=1e-9)
        if not ok_p or abs(float((p.T * v)[0, 0])) < 1 - 1e-6:
            return float("nan")
    denom = float((w1.T * u1)[0, 0])
    if abs(denom) < 1e-12:
        return float("nan")
    basis = lambda_basis(N)
    Gminv = Gm.inv()
    num = 0.0
    scale = 0.0
    for (i, j), (k, ll) in MATCHINGS:
        v = source_vec(V, N, basis, psx_shared[i], psx_shared[j]).evalf()
        x = (Gminv * source_vec(V, N, basis, psx_shared[k], psx_shared[ll])).evalf()
        num += float((v.T * u1)[0, 0]) * float((w1.T * x)[0, 0]) / denom
        scale += float(v.norm()) * float(x.norm())
    return abs(num) / scale


def neumann_partial_errors(V, Ks=(0, 2, 4, 8, 12)):
    """|exchange(S_K) - contact| at gs=1 (floats) for partial sums S_K of the chain.

    Returns the source vectors `psx` as well, so the caller can pass them to
    `dominant_overlap` for the same model without going through a global.
    """
    Gm, D, Noff, T, _ = neumann_data(V, N)
    psx = [rand_vec(N) for _ in range(4)]
    contact_num = float(V4_states(V, N, *psx))
    Dinv = D.inv()
    errs = []
    for Kmax in Ks:
        SK = sp.zeros(*Gm.shape)
        Tp = sp.eye(Gm.shape[0])
        for _n in range(Kmax + 1):
            SK += Tp * Dinv
            Tp = T * Tp
        diag_num = float(exchange_diagram(V, N, psx, SK).subs(gs, 1))
        errs.append(abs(diag_num - contact_num))
    # algebraic inverse on the SAME model and externals: exact telescoping
    alg_ok = sp.expand(exchange_diagram(V, N, psx, Gm.inv())
                       - gs**2 * V4_states(V, N, *psx)) == 0
    return errs, alg_ok, contact_num, psx


errs_A, algA, cA, psx_A = neumann_partial_errors(V_conv)
ovl_A = dominant_overlap(V_conv, psx_A)
errs_B, algB, cB, psx_B = neumann_partial_errors(V_div)
ovl_B = dominant_overlap(V_div, psx_B)
print(f"    model A errors {['%.3e' % e for e in errs_A]} (contact {cA:.3e})")
print(f"    model B errors {['%.3e' % e for e in errs_B]} (contact {cB:.3e})")
_fmt_ovl = lambda x: "not available (guard)" if x != x else f"{x:.3e}"  # noqa: E731
print(f"    dominant-mode weight in the error functional: model A {_fmt_ovl(ovl_A)},"
      f" model B {_fmt_ovl(ovl_B)} (transient diagnostic, no PASS/FAIL attached)")
ok5a = errs_A[-1] < 1e-3 * max(abs(cA), 1.0) and all(
    errs_A[i + 1] < errs_A[i] for i in range(len(errs_A) - 1)) and algA
ok5b = errs_B[-1] > 10 * errs_B[0] and errs_B[-1] > abs(cB) and algB
report(5, "rho<1: partial sums converge to contact (monotone); rho>=1: partial sums"
          " diverge while the algebraic inverse still telescopes exactly", ok5a and ok5b)

# ----------------------------------------------------------------------------
# Check 6 — H2 finite-dim shadow: completeness of the intermediate state sum
# ----------------------------------------------------------------------------
print("check (6): H2 shadow — deleting one intermediate Sym^2 state breaks"
      " exchange == contact; the full sum restores it")
dS = len(basisN)
Pi_full = sp.eye(dS)
Pi_trunc = sp.eye(dS)
Pi_trunc[dS - 1, dS - 1] = 0            # drop the last intermediate state
diag_full = exchange_diagram(V4T, N, psis, Pi_full * Ginv * Pi_full)
diag_trunc = exchange_diagram(V4T, N, psis, Pi_trunc * Ginv * Pi_trunc)
ok6 = (sp.expand(diag_full - contact) == 0
       and sp.expand(diag_trunc - contact) != 0)
report(6, "incomplete intermediate sum fails; complete sum collapses to the contact"
          " kernel — completeness of the LEVEL part of the state sum (H2) is"
          " load-bearing; the momentum part of H2 is not exercised in this model", ok6)

# ----------------------------------------------------------------------------
npass = sum(1 for *_, ok in results if ok)
print(f"\n{npass}/{len(results)} checks PASS (seed {SEED})")
print("    read as 5 checks + 1 vacuity demonstration: check 3 PASSes by design on"
      " corrupted vertex data and is evidence of nothing but the vacuity of a"
      " truncated telescoping comparison (record 023 §5.1)")
sys.exit(0 if npass == len(results) else 1)
