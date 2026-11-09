"""Verify derivation 007 (A1): explicit amplitude-level telescoping of the Σ-exchange.

Checks that the Σ-exchange 4-point diagram built from the Feynman rules of eq:SHS
(propagator (12/gs²)·(V₄|Sym²)⁻¹, vertex (gs²/6)·V₄(·, Ψᵢ⊗Ψⱼ), 3 pairings)
reproduces the quartic contact kernel gs²·V₄(Ψ₁,Ψ₂,Ψ₃,Ψ₄) exactly, plus the
supporting bookkeeping claims of `agent/derivations/007-a1-amplitude-telescoping.md`.

Checks
------
1. Diagram = contact: 3-pairing Σ-exchange sum equals gs²·V₄(Ψ₁..Ψ₄) for generic
   distinct external states (N=2 and N=3, several random draws).
2. Gaussian = contact at all orders in t: ½·B·M⁻¹·B == (gs²/4!)·V₄(Ψ(t)⊗²,Ψ(t)⊗²) as a
   polynomial identity in t₁..t₄ (hence for ALL n-point kernels, not just 4-point), and
   its ∂⁴t coefficient equals the check-1 diagram sum (Gaussian ↔ diagram bookkeeping).
3. Completion of the square (R1, symbolic in Σ): S_Σ(Σ) = −(gs²/4!)V₄(X,X)
   + (gs²/4!)V₄(Ψ⊗²,Ψ⊗²), X = Σ−Ψ⊗², on Sym² components.
4. Sensitivity (NOT independent falsification — the code builds each vertex ∝ c, so
   the (c/2)² scaling is structural; the falsifiable content is diag(c=1) != contact):
   replacing the source coefficient 2gs²/4! → c·gs²/4! rescales the exchange by
   (c/2)²; for c=1 the diagram gives exactly 1/4 of the contact term.
5. Multiplicity bookkeeping (factor-2 trap): (a) D-cancellation lemma — the FULLY
   entrywise unordered-pair sandwich T̃ᵀ·Ṽ⁻¹·T̃ is correct (the m_I weights cancel
   between source and Gram matrix), while the INCONSISTENT mix (derivative-weighted
   source m_I·T̃_I with the entrywise inverse Ṽ⁻¹) fails; (b) the propagator identity
   M·P = 1_Sym (A.4) holds componentwise; (c) the Moore–Penrose pseudo-inverse on the
   full H⊗² gives the same diagram (the ∧² sector decouples automatically).
6. Degenerate V₄ (kernel decoupling, R13/§3): with rank-deficient totally symmetric
   V = Σ_r c_r u_r⊗⁴ on Sym², the source B annihilates ker V, the pseudo-inverse
   propagator telescopes, and the diagram still equals the contact kernel.
7. Toy dictionary (qft_stubs.tex): in the toy's own weight convention e^{i∫bracket}
   = e^{−iS} (its quoted rules are self-consistent there — critic iter 1, Issue 1),
   kinetic K = V/12 ⇒ propagator −i·K⁻¹ = (−i/2)·4!·V⁻¹ (the toy's quoted
   normalization), vertex +2iV/12, and the factor chain 3·(1/6)·12·(1/6) = 1 with
   A₄ = iV.

References: derivation 007; knowledge/fable-2026-07-01-assessment-and-results.md
§6bis(e); sources/notes/qft_stubs.tex (toy A₄ = 3·(2iV/12)·((−i/2)4!V⁻¹)·(2iV/12) = iV);
R10 (codes/verify-s6-integrate-out.py).
"""

import itertools
import random
import sys

import sympy as sp

gs = sp.symbols("g_s", positive=True)

random.seed(20260701)

PASS, FAIL = 0, 1
results = []


def report(num, label, ok):
    global results
    results.append((num, label, ok))
    print(f"  check ({num}) {'PASS' if ok else 'FAIL'} — {label}")


# ----------------------------------------------------------------------------
# Machinery: totally symmetric V, Sym² bases, propagators
# ----------------------------------------------------------------------------

def random_symmetric_V(N, terms=None, rmin=-9, rmax=9):
    """Totally symmetric V_{abcd} as a sum of fourth powers c_r·u_r⊗⁴.

    With `terms` >= dim Sym² = N(N+1)/2 generic vectors, V is generically
    non-degenerate on Sym²; with fewer terms its rank on Sym² is <= terms.
    """
    dim_sym = N * (N + 1) // 2
    if terms is None:
        terms = dim_sym + 2
    V = [[[[sp.Integer(0)] * N for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for _ in range(terms):
        c = sp.Rational(random.randint(1, 5), random.randint(1, 3)) * random.choice([1, -1])
        u = [sp.Rational(random.randint(rmin, rmax), random.randint(1, 3)) for _ in range(N)]
        for a in range(N):
            for b in range(N):
                for c_ in range(N):
                    for d in range(N):
                        V[a][b][c_][d] += c * u[a] * u[b] * u[c_] * u[d]
    return V


def rand_vec(N):
    return [sp.Rational(random.randint(-9, 9), random.randint(1, 3)) for _ in range(N)]


def V4_states(V, N, p, q, r, s):
    """V₄(p,q,r,s) = V_{abcd} p^a q^b r^c s^d."""
    return sp.expand(sum(
        V[a][b][c][d] * p[a] * q[b] * r[c] * s[d]
        for a in range(N) for b in range(N) for c in range(N) for d in range(N)
    ))


def lambda_basis(N, orthonormal=True):
    """Basis of Sym²(R^N) as N×N matrices: E_aa and (E_ab+E_ba)/√2 (a<b).

    orthonormal=False drops the 1/√2 weights (the deliberate factor-2 trap, check 5).
    """
    basis = []
    for a in range(N):
        m = sp.zeros(N, N)
        m[a, a] = 1
        basis.append(m)
    w = 1 / sp.sqrt(2) if orthonormal else sp.Integer(1)
    for a in range(N):
        for b in range(a + 1, N):
            m = sp.zeros(N, N)
            m[a, b] = w
            m[b, a] = w
            basis.append(m)
    return basis


def V_matrix(V, N, basis):
    """G_IJ = V₄(λ_I, λ_J) on the given Sym² basis."""
    d = len(basis)
    G = sp.zeros(d, d)
    for I in range(d):
        for J in range(d):
            G[I, J] = sum(
                V[a][b][c][e] * basis[I][a, b] * basis[J][c, e]
                for a in range(N) for b in range(N) for c in range(N) for e in range(N)
            )
    return G


def project_coeffs(T, basis, N):
    """Coefficients of a symmetric tensor T^{ab} in the orthonormal λ basis."""
    return sp.Matrix([
        sum(T[a][b] * basis[I][a, b] for a in range(N) for b in range(N))
        for I in range(len(basis))
    ])


def sym_outer(p, q, N):
    """Symmetric part of p⊗q as an N×N array."""
    return [[sp.Rational(1, 2) * (p[a] * q[b] + p[b] * q[a]) for b in range(N)] for a in range(N)]


def exchange_diagram(V, N, psis, Ginv=None, source_coeff=2):
    """Σ-exchange 4-point kernel: Σ_pairings vertex·propagator·vertex.

    vertex(i,j) = (source_coeff·gs²/12)·V₄(λ_I, Ψᵢ⊗Ψⱼ)  [= gs²/6 for source_coeff=2]
    propagator  = (12/gs²)·G⁻¹ in the orthonormal λ_I basis.
    """
    basis = lambda_basis(N)
    if Ginv is None:
        Ginv = V_matrix(V, N, basis).inv()
    total = sp.Integer(0)
    for (i, j), (k, l) in [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]:
        bij = project_coeffs(
            [[sum(V[a][b][c][e] * psis[i][c] * psis[j][e] for c in range(N) for e in range(N))
              for b in range(N)] for a in range(N)], basis, N)
        bkl = project_coeffs(
            [[sum(V[a][b][c][e] * psis[k][c] * psis[l][e] for c in range(N) for e in range(N))
              for b in range(N)] for a in range(N)], basis, N)
        vertex_ij = 2 * source_coeff * gs**2 / 24 * bij   # ∂²B/∂tᵢ∂tⱼ, B = (c·gs²/4!)V₄(Σ,Ψ⊗²)
        vertex_kl = 2 * source_coeff * gs**2 / 24 * bkl
        total += (vertex_ij.T * (12 / gs**2 * Ginv) * vertex_kl)[0, 0]
    return sp.expand(sp.simplify(total))


# ----------------------------------------------------------------------------
# Check 1 — diagram = contact, generic distinct externals, N=2 and N=3
# ----------------------------------------------------------------------------
print("check (1): Σ-exchange diagram (3 pairings) == gs²·V₄(Ψ₁,Ψ₂,Ψ₃,Ψ₄)")
ok1 = True
for N in (2, 3):
    for trial in range(2):
        V = random_symmetric_V(N)
        psis = [rand_vec(N) for _ in range(4)]
        contact = gs**2 * V4_states(V, N, *psis)
        diagram = exchange_diagram(V, N, psis)
        if sp.simplify(diagram - contact) != 0:
            ok1 = False
report(1, "diagram equals contact kernel (N=2,3; random draws)", ok1)

# ----------------------------------------------------------------------------
# Check 2 — Gaussian = contact as a polynomial identity in t (all n-point kernels),
#            and its t₁t₂t₃t₄ coefficient equals the check-1 diagram
# ----------------------------------------------------------------------------
print("check (2): ½·B·M⁻¹·B == (gs²/4!)·V₄(Ψ(t)⊗²,Ψ(t)⊗²) as a polynomial in t")
N = 2
V = random_symmetric_V(N)
psis = [rand_vec(N) for _ in range(4)]
ts = sp.symbols("t1 t2 t3 t4")
psi_t = [sum(ts[i] * psis[i][a] for i in range(4)) for a in range(N)]

basis = lambda_basis(N)
G = V_matrix(V, N, basis)
# B_I = (gs²/12)·V₄(λ_I, Ψ(t)⊗Ψ(t)); M = (gs²/12)·G  ⇒  ½·B·M⁻¹·B = (gs²/24)·b·G⁻¹·b
b = project_coeffs(
    [[sum(V[a][bb][c][e] * psi_t[c] * psi_t[e] for c in range(N) for e in range(N))
      for bb in range(N)] for a in range(N)], basis, N)
W_gauss = sp.expand(sp.Rational(1, 2) * (gs**2 / 12 * b).T.dot(12 / gs**2 * G.inv() * (gs**2 / 12 * b)))
W_contact = gs**2 / 24 * V4_states(V, N, psi_t, psi_t, psi_t, psi_t)
ok2a = sp.simplify(W_gauss - W_contact) == 0
gamma_from_W = sp.diff(W_gauss, *ts)
ok2b = sp.simplify(gamma_from_W - exchange_diagram(V, N, psis)) == 0
report(2, "Gaussian == contact (all orders in t) and ∂⁴ₜW == diagram", ok2a and ok2b)

# ----------------------------------------------------------------------------
# Check 3 — completion of the square (R1), symbolic Σ
# ----------------------------------------------------------------------------
print("check (3): S_Σ == −(gs²/4!)·V₄(X,X) + (gs²/4!)·V₄(Ψ⊗²,Ψ⊗²), X = Σ−Ψ⊗²")
sig_syms = sp.symbols(f"s0:{N*(N+1)//2}")
Sig = [[sp.Integer(0)] * N for _ in range(N)]
idx = 0
for a in range(N):
    for bb in range(a, N):
        Sig[a][bb] = Sig[bb][a] = sig_syms[idx]
        idx += 1
PsiPsi = sym_outer(psi_t, psi_t, N)


def V4_tensors(V, N, A, B_):
    return sp.expand(sum(
        V[a][b][c][d] * A[a][b] * B_[c][d]
        for a in range(N) for b in range(N) for c in range(N) for d in range(N)))


X = [[Sig[a][b] - PsiPsi[a][b] for b in range(N)] for a in range(N)]
S_sigma = -gs**2 / 24 * V4_tensors(V, N, Sig, Sig) + 2 * gs**2 / 24 * V4_tensors(V, N, Sig, PsiPsi)
rhs = -gs**2 / 24 * V4_tensors(V, N, X, X) + gs**2 / 24 * V4_tensors(V, N, PsiPsi, PsiPsi)
report(3, "completion of the square holds identically in (Σ, t)", sp.simplify(S_sigma - rhs) == 0)

# ----------------------------------------------------------------------------
# Check 4 — falsifiability: source coefficient c ⇒ diagram = (c/2)²·contact
# ----------------------------------------------------------------------------
print("check (4): source coeff c·gs²/4! ⇒ exchange = (c/2)²·contact; c=1 gives 1/4")
contact = gs**2 * V4_states(V, N, *psis)
diag_c1 = exchange_diagram(V, N, psis, source_coeff=1)
c_sym = sp.symbols("c")
diag_cs = exchange_diagram(V, N, psis, source_coeff=c_sym)
ok4 = (sp.simplify(diag_c1 - contact / 4) == 0
       and sp.simplify(diag_cs - (c_sym / 2)**2 * contact) == 0
       and sp.simplify(diag_c1 - contact) != 0)
report(4, "quadratic sensitivity to the 2:1 source-to-kinetic ratio", ok4)

# ----------------------------------------------------------------------------
# Check 5 — factor-2 trap: entrywise Ṽ_IJ wrong; correct bookkeepings agree; P·M = 1_Sym
# ----------------------------------------------------------------------------
print("check (5): D-cancellation lemma; inconsistent m_I-mix fails; pinv agrees; A.4 holds")
# (a) multiplicity bookkeeping in the unordered-pair index I = (a<=b), m_I = 1 (diag),
#     2 (off-diag). Entrywise matrix Ṽ_IJ = V_{abcd}; entrywise source T̃_I = T^{ab}.
#     D-cancellation lemma (positive result): the FULLY entrywise sandwich
#     T̃ᵀ·Ṽ⁻¹·T̃ is correct — the Gram matrix is G = D·Ṽ·D and the covariant source is
#     v = D·T̃ (D = diag(m_I)), so vᵀG⁻¹v = T̃ᵀṼ⁻¹T̃: the weights cancel.
#     The genuine trap is the INCONSISTENT mix: the source that arises from
#     differentiating w.r.t. the unordered variables σ_I (∂B/∂σ_I = m_I·T̃_I) contracted
#     with the entrywise inverse Ṽ⁻¹ instead of the inverse Gram D⁻¹Ṽ⁻¹D⁻¹ ⇒ wrong.
pairs = [(a, b) for a in range(N) for b in range(a, N)]
mults = sp.diag(*[sp.Integer(1) if a == b else sp.Integer(2) for (a, b) in pairs])
V_entry = sp.Matrix(len(pairs), len(pairs),
                    lambda I, J: V[pairs[I][0]][pairs[I][1]][pairs[J][0]][pairs[J][1]])
total_entry = sp.Integer(0)   # fully entrywise (consistent) — must equal contact
total_mix = sp.Integer(0)     # m-weighted source with entrywise inverse — must fail
for (i, j), (k, l) in [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]:
    Tij = [[sum(V[a][b][c][e] * psis[i][c] * psis[j][e] for c in range(N) for e in range(N))
            for b in range(N)] for a in range(N)]
    Tkl = [[sum(V[a][b][c][e] * psis[k][c] * psis[l][e] for c in range(N) for e in range(N))
            for b in range(N)] for a in range(N)]
    t_ij = sp.Matrix([Tij[a][b] for (a, b) in pairs])   # entrywise T̃
    t_kl = sp.Matrix([Tkl[a][b] for (a, b) in pairs])
    total_entry += (gs**2 / 6 * t_ij).T.dot(12 / gs**2 * V_entry.inv() * (gs**2 / 6 * t_kl))
    total_mix += (gs**2 / 6 * mults * t_ij).T.dot(
        12 / gs**2 * V_entry.inv() * (gs**2 / 6 * mults * t_kl))
ok5a = (sp.simplify(sp.expand(total_entry) - contact) == 0
        and sp.simplify(sp.expand(total_mix) - contact) != 0)
# (b) propagator identity (A.4): M·P = 1_Sym in tensor components, with
#     P = (12/gs²)·(V|_Sym²)⁻¹ reconstructed from the orthonormal λ_I basis.
basisN = lambda_basis(N)
GN = V_matrix(V, N, basisN)
Ginv_N = GN.inv()
dim_sym = len(basisN)


def sym_id_component(a, b, c, d):
    return sp.Rational(1, 2) * (sp.Integer(1 if (a == c and b == d) else 0)
                                + sp.Integer(1 if (a == d and b == c) else 0))


ok5c = True
for a in range(N):
    for b in range(N):
        for c in range(N):
            for d in range(N):
                # (M·P)_{ab}^{cd} = Σ_{IJ} V(e_ab, λ_I)(G⁻¹)^{IJ} λ_J^{cd}  (M coeff × P coeff → gs² cancels)
                MP = sum(
                    sum(V[a][b][x][y] * basisN[I][x, y] for x in range(N) for y in range(N))
                    * Ginv_N[I, J] * basisN[J][c, d]
                    for I in range(dim_sym) for J in range(dim_sym))
                if sp.simplify(MP - sym_id_component(a, b, c, d)) != 0:
                    ok5c = False
# (c) Moore–Penrose pseudo-inverse on the FULL N²×N² tensor square agrees with λ_I result
d2 = N * N
Vfull = sp.zeros(d2, d2)
for a in range(N):
    for b in range(N):
        for c in range(N):
            for e in range(N):
                Vfull[a * N + b, c * N + e] = V[a][b][c][e]
Vpinv = Vfull.pinv()
total_pinv = sp.Integer(0)
for (i, j), (k, l) in [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]:
    bij_full = sp.Matrix([sum(V[a][b][c][e] * psis[i][c] * psis[j][e]
                              for c in range(N) for e in range(N))
                          for a in range(N) for b in range(N)])
    bkl_full = sp.Matrix([sum(V[a][b][c][e] * psis[k][c] * psis[l][e]
                              for c in range(N) for e in range(N))
                          for a in range(N) for b in range(N)])
    total_pinv += (gs**2 / 6 * bij_full).T.dot(12 / gs**2 * Vpinv * (gs**2 / 6 * bkl_full))
ok5b = sp.simplify(sp.expand(total_pinv) - contact) == 0
report(5, "entrywise mistake fails; pinv agrees; M·P = 1_Sym (A.4)", ok5a and ok5b and ok5c)

# ----------------------------------------------------------------------------
# Check 6 — degenerate V₄: kernel unsourced, pseudo-inverse telescopes, diagram intact
# ----------------------------------------------------------------------------
print("check (6): rank-deficient V₄ on Sym²: B ⊥ ker V, diagram still == contact")
N6 = 2
V_deg = random_symmetric_V(N6, terms=2)          # rank ≤ 2 < dim Sym² = 3
basis6 = lambda_basis(N6)
G6 = V_matrix(V_deg, N6, basis6)
ok6_rank = G6.rank() < 3
kernel = G6.nullspace()
psis6 = [rand_vec(N6) for _ in range(4)]
psi6_t = [sum(ts[i] * psis6[i][a] for i in range(4)) for a in range(N6)]
b6 = project_coeffs(
    [[sum(V_deg[a][bb][c][e] * psi6_t[c] * psi6_t[e] for c in range(N6) for e in range(N6))
      for bb in range(N6)] for a in range(N6)], basis6, N6)
ok6_source = all(sp.simplify(b6.dot(kv)) == 0 for kv in kernel)   # B(ξ)=0 on ker (G symmetric)
G6p = G6.pinv()
ok6_tel = sp.simplify(G6 * G6p * G6 - G6) == sp.zeros(3, 3)
contact6 = gs**2 * V4_states(V_deg, N6, *psis6)
diagram6 = exchange_diagram(V_deg, N6, psis6, Ginv=G6p)
ok6_diag = sp.simplify(diagram6 - contact6) == 0
report(6, "kernel decoupling: unsourced kernel, exact telescoping, kernel-blind diagram",
       ok6_rank and ok6_source and ok6_tel and ok6_diag)

# ----------------------------------------------------------------------------
# Check 7 — toy dictionary: propagator normalization (−i/2)·4!·V⁻¹ and factor chain
# ----------------------------------------------------------------------------
print("check (7): qft_stubs propagator (−i/2)·4!·V⁻¹ from K=V/12; 3·(1/6)·12·(1/6)=1")
# e^{iS}, S ⊃ ½Kσσ ⇒ ⟨σσ⟩ = −i·K⁻¹; toy kinetic (1/4!)V_{IJ}σᴵσᴶ = ½(V/12)σσ
K_coeff = sp.Rational(2, sp.factorial(4))            # K = 2/4!·V = V/12
prop_toy = -sp.I / K_coeff                            # coefficient of V⁻¹
ok7a = sp.simplify(prop_toy - sp.Rational(-1, 2) * sp.factorial(4) * sp.I) == 0
ok7b = sp.Integer(3) * sp.Rational(1, 6) * 12 * sp.Rational(1, 6) == 1
# full toy factor chain (coefficients of V·V⁻¹·V → V):
# 3 · (2i/12) · ((−i/2)·4!) · (2i/12) = 3·(i/6)·(−12i)·(i/6) = i
chain = sp.simplify(sp.Integer(3) * (2 * sp.I / 12)
                    * (sp.Rational(-1, 2) * sp.factorial(4) * sp.I) * (2 * sp.I / 12))
ok7c = sp.simplify(chain - sp.I) == 0
report(7, "toy propagator normalization and A₄ factor chain reproduce qft_stubs", ok7a and ok7b and ok7c)

# ----------------------------------------------------------------------------

npass = sum(1 for *_, ok in results if ok)
print(f"\n{npass}/{len(results)} checks PASS")
sys.exit(0 if npass == len(results) else 1)
