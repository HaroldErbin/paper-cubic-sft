"""
Self-checks for task I3: invertibility of the two-output product
m_2 = p_{2,2,0} = Delta o ell_3 : H^{ot2} -> H^{ot2} (note eq:mtwo) on the
LEVEL-MATCHED subspace of H^{ot2}.

GOAL of the task: decide whether ker m_2 = 0, so that the Sigma equation of
motion m_2(Sigma) = m_2(Psi^{ot2}) (note eq:Sigeom) forces Sigma = Psi^{ot2}
UNIQUELY -- i.e. Sigma is purely auxiliary (no independent propagating d.o.f.).
R8 already gave SUFFICIENCY (Sigma = Psi^{ot2} solves the EOM); uniqueness is
exactly ker m_2 = 0.

WHAT THIS SCRIPT TESTS (finite-dimensional graded toy, physical N_gh grading,
reusing the machinery of verify-i2-ibl-action.py / verify-omega2-physical.py).

The PHYSICAL fields Sigma, Psi^{ot2} live in the N_gh = 4 EVEN sub-block of
H^{ot2} (note eq:Sigexpand: N_gh(Sigma) = 4, fixed so V_4(Sigma,Sigma) saturates
the ghost anomaly with two copies of the N_gh = 2 field Psi). So the Sigma
KINETIC pairing V_4(Sigma,Sigma) needs the toy ghost saturation tuned to pair
N_gh = 4 with N_gh = 4 (total 8), which is the relevant block; we work there.

  (T1) STRUCTURAL REDUCTION.  m_2 = G_2^{-1} V_4 with G_2 = omega_1^{ot2}
       non-degenerate (R7). Hence on the relevant block
            ker m_2 = ker V_4 ,
       so  ker m_2 = 0  <=>  V_4 non-degenerate as a bilinear form on the
       (level-matched) Sigma-sector of H^{ot2}. THIS IS THE EQUIVALENCE the task
       asks to establish.

  (T1e) SYMMETRIC OUTPUTS (critic C2).  m_2 maps Sym^2 -> Sym^2 (the antisymmetric
       component of m_2(Sym^2) vanishes; equivalently V_4 is block-diagonal in the
       sym/antisym split). This is what makes the equivalence (2.3)
            ker(m_2|Sym^2) = 0  <=>  V_4|Sym^2 non-degenerate
       actually hold: without symmetric outputs, a symmetric Y with m_2 Y purely
       antisymmetric would satisfy V_4|Sym^2(.,Y) = 0 yet m_2 Y != 0. It follows
       from the FULL graded symmetry of V_4 (output slots, not only input slots).

  (T2) NON-DEGENERATE CASE.  V_4 injective => m_2 injective => the Sigma-EOM
       m_2(Sigma) = m_2(Psi^{ot2}) has the UNIQUE solution Sigma = Psi^{ot2}:
       Xi := Sigma - Psi^{ot2} in ker m_2 => Xi = 0 => Sigma purely auxiliary.

  (T3) SHARPNESS / COUNTEREXAMPLE.  If V_4 degenerates (a null vector Xi:
       V_4(., Xi) = 0), then m_2(Xi) = 0, so Sigma = Psi^{ot2} + Xi is ALSO a
       solution. Exhibit this explicitly: invertibility fails IFF V_4 degenerates.
       This is exactly what a counterexample to auxiliarity looks like -- a null
       vector of the quartic CONTACT vertex is a flat direction of the Sigma-EOM.

  (T4) HEURISTIC ILLUSTRATION ONLY (critic S2 -- NOT part of the verified core).
       A toy "no-pole" model: vertex amplitudes REGULAR (polynomial, no 1/q poles)
       in an external invariant q -> det V_4(q) a nonzero polynomial with a finite
       zero set. This ILLUSTRATES the contact-term picture (Step 3 of the
       derivation) but does NOT certify the vertex and is NOT evidence for the open
       condition (5.1): (i) pole-freeness of a contact term is AUTOMATIC and bears
       no logical relation to non-degeneracy (a pole-free/entire function can still
       vanish identically or on a large set); (ii) "generic / measure-zero" has no
       meaning for the SINGLE FIXED CFT vertex, which either has a symmetric null
       vector or not; (iii) the YM Box-at-p^2=0 analogy does not transfer -- (5.1)
       is an operator-kernel question, not "det vanishes at special momenta", and a
       normalizable null vector would be an honest flat direction, not a removable
       shell. T4a/T4b are retained only as illustrations of the heuristic.

WHAT THIS SCRIPT DOES *NOT* TEST (honest scope, mirroring R7/R8):
  - It does NOT compute the worldsheet c0^-, ell_3, V_4 on the genuine
    level-matched infinite-dimensional H. The genuinely OPEN part is the
    CFT-level / infinite-dimensional non-degeneracy of V_4 (equivalently the
    absence of null vectors of the quartic contact vertex on
    ker L_0^- cap ker b_0^-). The toy establishes the ALGEBRAIC EQUIVALENCE
    ker m_2 = 0 <=> V_4 non-deg, the structure of any counterexample, and the
    no-pole/measure-zero character of the degeneration locus; it cannot certify
    the infinite-dimensional non-degeneracy itself.

Conventions: Erbin (2023); metric (-,+,+,+); hbar=c=1; alpha' explicit; bra-ket;
physical parity eps = N_gh mod 2. Closed-string pairing carries c0^- (R7).
Presentation (A): omega_1 odd symplectic on Psi; G_2 = omega_1^{ot2} symmetric
Poisson on the H^{ot2} sector; m_2 = Delta o ell_3, Delta = omega_1^{-1}.
"""

from __future__ import annotations

from itertools import permutations

import sympy as sp


def report(name: str, ok: bool, detail: str = "") -> None:
    status = "PASS" if ok else "FAIL"
    line = f"[{status}] {name}"
    if detail:
        line += f"  --  {detail}"
    print(line)
    if not ok:
        raise AssertionError(f"check failed: {name}")


# ---------------------------------------------------------------------------
# Toy closed-string Hilbert space H, graded by PHYSICAL N_gh. omega_1 pairs
# N_gh = 2 <-> 3 (one c0^- insertion). Every basis vector stands for a
# LEVEL-MATCHED state (we do not model L_0^- here; the toy IS the level-matched
# subspace). The Sigma sector is the N_gh = 4 EVEN block of H^{ot2}; the toy
# ghost saturation is tuned (D_SAT = 5 -> total 8) so the Sigma KINETIC pairing
# V_4(Sigma, Sigma) (two N_gh = 4 tensors) is the saturated, nonzero block.
# ---------------------------------------------------------------------------
# Three N_gh = 2 states (indices 0,1,2) and three N_gh = 3 states (3,4,5). The
# enlarged single-particle space is needed so the fully graded-symmetric quartic
# vertex V_4 restricted to the N_gh = 4 two-particle sector is GENERICALLY
# non-degenerate (a 2-state single-particle space gives a structurally
# rank-deficient symmetric quartic -- an artefact of too few states, not of the
# physics). omega_1 pairs each N_gh = 2 state with one N_gh = 3 state.
NGH = [2, 2, 2, 3, 3, 3]
PAR = [n % 2 for n in NGH]
N = len(NGH)
SAT_TOTAL = 8  # 2 * N_gh(Sigma) = 2 * 4: pairs N_gh=4 with N_gh=4 (Sigma kinetic)
a, b, c = sp.symbols("a b c", nonzero=True)

w1 = sp.zeros(N, N)


def _set_odd_pair(i: int, j: int, val: sp.Expr) -> None:
    w1[i, j] = val
    w1[j, i] = -((-1) ** (PAR[i] * PAR[j])) * val


_set_odd_pair(0, 3, a)
_set_odd_pair(1, 4, b)
_set_odd_pair(2, 5, c)

BASIS2 = [(p, q) for p in range(N) for q in range(N)]
N2 = len(BASIS2)
IDX2 = {pq: m for m, pq in enumerate(BASIS2)}


def eps2(pq: tuple[int, int]) -> int:
    return (PAR[pq[0]] + PAR[pq[1]]) % 2


def ngh2(pq: tuple[int, int]) -> int:
    return NGH[pq[0]] + NGH[pq[1]]


def G2_value(X: tuple[int, int], Y: tuple[int, int]) -> sp.Expr:
    x1, x2 = X
    y1, y2 = Y
    return (-1) ** (PAR[x2] * PAR[y1]) * w1[x1, y1] * w1[x2, y2]


G2 = sp.zeros(N2, N2)
for X in BASIS2:
    for Y in BASIS2:
        G2[IDX2[X], IDX2[Y]] = G2_value(X, Y)

# The PHYSICAL Sigma sector: N_gh = 4 (=> EVEN). These are the only states a
# physical Sigma / Psi^{ot2} populate (note eq:Sigexpand).
SIG = [m for m, pq in enumerate(BASIS2) if ngh2(pq) == 4]
assert all(eps2(BASIS2[m]) == 0 for m in SIG)  # N_gh = 4 => even
DIMSIG = len(SIG)


# ---------------------------------------------------------------------------
# Fully graded-symmetric quartic vertex V_4 (closed cyclic vertex), nonzero only
# at ghost saturation sum N_gh = SAT_TOTAL = 8. m_2 = G_2^{-1} V_4 raises one
# index with Delta = omega_1^{-1}. On the Sigma sector V_4 pairs N_gh=4 <-> N_gh=4.
# ---------------------------------------------------------------------------
def positional_koszul(values, perm) -> int:
    sign = 1
    m = len(perm)
    for i in range(m):
        for j in range(i + 1, m):
            if perm[i] > perm[j] and PAR[values[perm[i]]] and PAR[values[perm[j]]]:
                sign = -sign
    return sign


def make_V4(amp):
    Vmat = sp.zeros(N2, N2)
    for X in BASIS2:
        for Y in BASIS2:
            idx = (X[0], X[1], Y[0], Y[1])
            if sum(NGH[x] for x in idx) != SAT_TOTAL:
                continue
            total = sp.Integer(0)
            for perm in permutations(range(4)):
                permed = tuple(idx[perm[t]] for t in range(4))
                total += positional_koszul(idx, perm) * amp(permed)
            Vmat[IDX2[X], IDX2[Y]] = total
    return Vmat


_amp_cache: dict[tuple[int, ...], sp.Symbol] = {}


def amp_generic(idx) -> sp.Expr:
    if sum(NGH[x] for x in idx) != SAT_TOTAL:
        return sp.Integer(0)
    key = tuple(sorted(idx))
    if key not in _amp_cache:
        _amp_cache[key] = sp.Symbol("t" + "".join(map(str, key)))
    return _amp_cache[key]


Vmat = make_V4(amp_generic)

# Sector bookkeeping. m_2 : H^{ot2} -> H^{ot2} is defined by
#     V_4(X, Y) = G_2(X, m_2 Y),     X, Y in H^{ot2}.
# Read off the sectors. The Sigma INPUT sector S_in is where V_4(.,.) is
# saturated: V_4(X,Y) != 0 needs N_gh(X) = N_gh(Y) = 4 (SAT_TOTAL = 8), so the
# physical input/output of the kinetic bilinear is the N_gh = 4 block S_in = SIG.
# G_2 pairs S_in (N_gh = 4) with the DUAL sector S_out (N_gh = 6), since G_2 is
# saturated at N_gh(X) + N_gh(Y) = 10. Hence m_2 maps S_in -> S_out:
#     m_2 = (G_2|_{S_out, S_in})^{-1}  V_4|_{S_in, S_in}.
# This is the precise index structure of m_2 = Delta o ell_3 (eq:mtwo); G_2
# restricted to (S_out, S_in) is the non-degenerate block of the c0^- pairing.
S_in = SIG  # N_gh = 4: physical Sigma / Psi^{ot2}
S_out = [m for m, pq in enumerate(BASIS2) if ngh2(pq) == 6]  # G_2-dual sector
DIMIN, DIMOUT = len(S_in), len(S_out)

V_block = Vmat[S_in, S_in]              # bilinear form, S_in x S_in
G2_block = G2[S_out, S_in]             # non-degenerate pairing, S_out x S_in
m2_block = G2_block.inv() * V_block    # m_2 : S_in -> S_out

amp_syms = sorted(_amp_cache.values(), key=str)
generic_vals = [3, -5, 7, 2, -11, 13, 4, -9, 17, 6, -1, 19, 8, -3, 23, 29, -31]
subs_g = {s: sp.Integer(v) for s, v in zip(amp_syms, generic_vals)}
subs_g.update({a: sp.Integer(1), b: sp.Integer(1), c: sp.Integer(1)})

# ---------------------------------------------------------------------------
# SYMMETRISATION of the Sigma sector. A closed string field is BOSONIC and the
# auxiliary tensor naturally lives in the GRADED-SYMMETRIC square Sym^2 H (this
# is where Psi^{ot2} lives). The fully graded-symmetric vertex V_4(x1,x2,y1,y2)
# is symmetric under x1<->x2 (even-parity insertions, no Koszul sign here), so
# V_4 ANNIHILATES the antisymmetric part wedge^2 H of H^{ot2}. Hence ker m_2 on
# the FULL H^{ot2} automatically CONTAINS wedge^2 H -- an UNPHYSICAL kernel that
# is removed by restricting Sigma to Sym^2 H. We build the sym/antisym split of
# the N_gh=4 sector and the projector onto Sym^2.
# ---------------------------------------------------------------------------
def sym_antisym_basis(sector):
    """Return (sym_cols, anti_cols): change-of-basis columns (in S_in indexing)
    onto graded-symmetric and graded-antisymmetric two-particle states.
    """
    pairs = [BASIS2[m] for m in sector]
    pos = {pq: i for i, pq in enumerate(pairs)}
    dim = len(pairs)
    sym_cols, anti_cols, seen = [], [], set()
    for (p, q) in pairs:
        if (p, q) in seen or (q, p) in seen:
            continue
        seen.add((p, q))
        v_s = sp.zeros(dim, 1)
        if p == q:
            v_s[pos[(p, q)]] = 1
            sym_cols.append(v_s)
        else:
            seen.add((q, p))
            v_s[pos[(p, q)]] = 1
            v_s[pos[(q, p)]] = 1  # symmetric (even insertions)
            sym_cols.append(v_s)
            v_a = sp.zeros(dim, 1)
            v_a[pos[(p, q)]] = 1
            v_a[pos[(q, p)]] = -1  # antisymmetric
            anti_cols.append(v_a)
    return sym_cols, anti_cols


sym_cols, anti_cols = sym_antisym_basis(S_in)
Psym = sp.Matrix.hstack(*sym_cols)   # S_in x dim(Sym^2)
Panti = sp.Matrix.hstack(*anti_cols)  # S_in x dim(wedge^2)
DIM_SYM = Psym.shape[1]


# ===========================================================================
# T1 -- STRUCTURAL REDUCTION:  m_2 = (G_2|_{S_out,S_in})^{-1} V_4|_{S_in,S_in},
# G_2-block non-degenerate (R7), hence ker m_2 = ker V_4.
#   ker m_2 = 0  <=>  V_4 non-degenerate.
# ===========================================================================
report(
    "T1a G_2 = omega_1^{ot2} NON-DEGENERATE (R7): full det G_2 != 0, and the "
    "(S_out, S_in) block is invertible",
    sp.simplify(G2.det()) != 0 and sp.simplify(G2_block.det()) != 0,
    f"det G_2 = {sp.simplify(G2.det())} = (det omega_1)^{{2 dim H}}; "
    f"det G_2|_{{S_out,S_in}} = {sp.simplify(G2_block.det())} != 0 "
    "=> G_2-block invertible (no m_2 inversion used to DEFINE m_2)",
)
report(
    "T1b m_2 = G_2^{-1} V_4 (eq:mtwo): G_2|_{S_out,S_in} m_2 = V_4|_{S_in,S_in}",
    sp.simplify((G2_block * m2_block - V_block).applyfunc(sp.expand))
    == sp.zeros(DIMOUT, DIMIN),
    "the Sigma kinetic bilinear is exactly V_4 = G_2 m_2 (one index raised by Delta)",
)

V_num = V_block.subs(subs_g)
m2_num = m2_block.subs(subs_g)
report(
    "T1c ker m_2 = ker V_4 on the full Sigma sector (G_2-block invertible): "
    "rank(m_2) = rank(V_4)",
    V_num.rank() == m2_num.rank(),
    f"dim Sigma sector = {DIMIN}; rank V_4 = {V_num.rank()} = rank m_2 "
    "=> ker m_2 = ker V_4 (THE EQUIVALENCE), so ker m_2 = 0 IFF V_4 non-degenerate",
)

# T1d: the full-space kernel CONTAINS wedge^2 H (unphysical), because the fully
# graded-symmetric V_4 annihilates the antisymmetric part. So the relevant space
# for auxiliarity is Sym^2 H, where Psi^{ot2} also lives.
m2_on_anti = m2_num * Panti
report(
    "T1d full-space ker m_2 CONTAINS wedge^2 H (V_4 kills the antisymmetric part): "
    "m_2 | wedge^2 = 0",
    sp.simplify(m2_on_anti.applyfunc(sp.expand)) == sp.zeros(DIMOUT, Panti.shape[1]),
    f"dim wedge^2 = {Panti.shape[1]}; this is an UNPHYSICAL kernel removed by "
    "Sigma in Sym^2 H (decoupling: wedge^2 appears in NEITHER the Sigma kinetic nor "
    "the source term; Psi^{ot2} symmetric)",
)

# T1e (critic C2): SYMMETRIC OUTPUTS. The equivalence (2.3)
#     ker(m_2|Sym^2) = 0  <=>  V_4|Sym^2 non-degenerate
# is only valid if m_2 maps Sym^2 -> Sym^2 (symmetric OUTPUTS), so that
# G_2(X, m_2 Y) = 0 for all symmetric X forces the FULL m_2 Y (not just its
# symmetric component) to vanish. Without this, a symmetric Y with m_2 Y purely
# ANTIsymmetric would satisfy V_4|Sym^2(.,Y) = 0 yet m_2 Y != 0, breaking (2.3).
# Symmetric outputs is a consequence of the FULL graded symmetry of V_4 (symmetry
# in the OUTPUT slots, not only the input slots) together with G_2 being
# block-diagonal w.r.t. the sym/antisym split. We check it directly: the
# antisymmetric component of m_2(Sym^2) vanishes, i.e. Panti^T m_2 Psym = 0.
m2_sym_anti = Panti.T * (m2_num * Psym)  # antisym component of m_2(Sym^2)
v4_cross = (Psym.T * V_block * Panti).subs(subs_g)  # Sym<->antisym block of V_4
report(
    "T1e SYMMETRIC OUTPUTS m_2(Sym^2) subset Sym^2 (C2): antisymmetric component of "
    "m_2(Sym^2) is zero (Panti^T m_2 Psym = 0), equivalently V_4 block-diagonal in "
    "the sym/antisym split (Psym^T V_4 Panti = 0)",
    sp.simplify(m2_sym_anti.applyfunc(sp.expand)) == sp.zeros(*m2_sym_anti.shape)
    and sp.simplify(v4_cross.applyfunc(sp.expand)) == sp.zeros(DIM_SYM, Panti.shape[1]),
    "m_2 has symmetric outputs (full graded symmetry of V_4 in the OUTPUT slots + "
    "block-diagonal G_2) => the equivalence (2.3) ker(m_2|Sym^2)=0 <=> V_4|Sym^2 "
    "non-deg is VALID (no symmetric Y leaks an antisymmetric m_2 Y past V_4|Sym^2)",
)


# ===========================================================================
# T2 -- NON-DEGENERATE CASE on Sym^2 H: V_4 restricted to the symmetric square
# is GENERICALLY non-degenerate => m_2 invertible on Sym^2 => UNIQUE solution
# Sigma = Psi^{ot2}. (This is the physical statement; wedge^2 is projected out.)
# ===========================================================================
V_sym = (Psym.T * V_num * Psym)          # bilinear form on Sym^2
report(
    "T2a V_4 GENERICALLY non-degenerate on Sym^2 H (det != 0) => m_2 invertible "
    "on Sym^2",
    sp.simplify(V_sym.det()) != 0,
    f"dim Sym^2 = {DIM_SYM}; det V_4|Sym^2 = {sp.simplify(V_sym.det())} != 0 "
    "(generic amplitudes) => m_2 invertible on the PHYSICAL symmetric sector",
)
# Uniqueness: Xi in Sym^2 with m_2(Xi) = 0 => V_4(.,Xi)|Sym^2 = 0 => Xi = 0.
ker_sym = V_sym.nullspace()
report(
    "T2b m_2 invertible on Sym^2 => Sigma-EOM m_2(Sigma)=m_2(Psi^{ot2}) has UNIQUE "
    "soln Sigma=Psi^{ot2}",
    len(ker_sym) == 0,
    "ker m_2|Sym^2 = {0}: Xi := Sigma - Psi^{ot2} in Sym^2 cap ker m_2 => Xi = 0 "
    "=> Sigma PURELY AUXILIARY (no propagating d.o.f.)",
)


# ===========================================================================
# T3 -- SHARPNESS / COUNTEREXAMPLE on Sym^2: if V_4 degenerates ON Sym^2, m_2
# acquires a PHYSICAL kernel and the Sigma-EOM no longer fixes Sigma uniquely.
# Tune one amplitude so V_4|Sym^2 is rank-deficient, exhibit a symmetric null
# vector Xi, and verify Sigma = Psi^{ot2} + Xi also solves the EOM. This is what
# a genuine counterexample to auxiliarity would look like.
# ===========================================================================
V_sym_sym = Psym.T * V_block * Psym  # symbolic V_4|Sym^2
free = sorted(V_sym_sym.free_symbols - {a, b, c}, key=str)
base = {s: sp.Integer(v) for s, v in zip(free[:-1], generic_vals[: len(free) - 1])}
base.update({a: sp.Integer(1), b: sp.Integer(1), c: sp.Integer(1)})
last = free[-1]
det_poly = sp.expand(V_sym_sym.subs(base).det())
roots = sp.solve(det_poly, last)
assert roots, "could not tune det V_4|Sym^2 = 0"
tune = base | {last: roots[0]}
V_sym_deg = V_sym_sym.subs(tune)
null = V_sym_deg.nullspace()  # symmetric null vector of V_4 (=> of m_2)
Xi_sym = null[0] if null else None
# m_2(Xi) = 0 in S_out: V_4(., Xi)|Sym^2 = 0 => the EOM residual vanishes.
residual = (V_sym_deg * Xi_sym).applyfunc(sp.expand) if Xi_sym is not None else None
report(
    "T3 SHARPNESS: V_4 degenerate on Sym^2 (det=0) => m_2 has PHYSICAL kernel "
    "Xi != 0 => Sigma=Psi^{ot2}+Xi ALSO solves the EOM",
    sp.simplify(V_sym_deg.det()) == 0
    and Xi_sym is not None
    and residual == sp.zeros(DIM_SYM, 1),
    "would-be counterexample to auxiliarity: a SYMMETRIC null vector of the quartic "
    "CONTACT vertex is a flat direction of the Sigma-EOM (so invertibility <=> V_4 "
    "non-deg on Sym^2 is SHARP)",
)


# ===========================================================================
# T4 -- "NO-POLE" / momentum analogue (FBSP8UQ9 sec.8.3 Box-invertibility; R3
# open-stub regularity). Amplitudes REGULAR (affine, no 1/q poles) in an external
# invariant q -> det V_4(q) a nonzero polynomial -> degeneration on a measure-zero
# locus only, removable like 1/Box at p^2 = 0.
# ===========================================================================
q = sp.symbols("q", positive=True)


def amp_q(idx) -> sp.Expr:
    base_amp = amp_generic(idx)
    if base_amp == 0:
        return sp.Integer(0)
    c1 = sp.Symbol("c_" + str(base_amp))
    return base_amp + c1 * q  # regular (no pole) q-dependence: contact term


Vq = make_V4(amp_q)
Vq_sym = Psym.T * Vq[S_in, S_in] * Psym  # restrict to Sym^2 (physical sector)
qsubs = {}
vals = generic_vals + [37, -41, 43, -47, 53, -59]
for i, s in enumerate(sorted(Vq_sym.free_symbols - {q}, key=str)):
    qsubs[s] = sp.Integer(vals[i % len(vals)])
detq = sp.expand(Vq_sym.subs(qsubs).det())
report(
    "T4a (HEURISTIC ILLUSTRATION ONLY, NOT certified core): toy contact-term model "
    "det V_4(q) a nonzero POLYNOMIAL in q (regular, no poles)",
    detq != 0 and detq.is_polynomial(q),
    f"deg_q det = {sp.degree(detq, q) if detq.has(q) else 0}; illustrates Step 3 only "
    "-- pole-freeness is AUTOMATIC and unrelated to non-degeneracy; NOT evidence for (5.1)",
)
zero_locus = sp.solve(detq, q) if detq.has(q) else []
report(
    "T4b (HEURISTIC ILLUSTRATION ONLY, NOT certified core): toy zero set finite "
    "(#zeros <= deg)",
    (not detq.has(q)) or len(zero_locus) <= sp.degree(detq, q),
    f"#zeros = {len(zero_locus)} <= deg = "
    f"{sp.degree(detq, q) if detq.has(q) else 0}; 'generic/measure-zero' has NO meaning "
    "for the single fixed CFT vertex -- illustration of the heuristic, not a certification",
)


if __name__ == "__main__":
    print("\nAll I3 m_2-invertibility self-checks PASS.")
    print(
        "ESTABLISHED (verified algebraic core, toy):\n"
        "  * On Sym^2 H (the physical bosonic sector where Sigma, Psi^{ot2} live),\n"
        "    ker(m_2|Sym^2) = 0  <=>  V_4|Sym^2 non-degenerate; non-deg V_4 =>\n"
        "    Sigma = Psi^{ot2} UNIQUE (purely auxiliary). This is INJECTIVITY; the\n"
        "    integrate-out step (S6) needs in addition a bounded inverse V_4^{-1}.\n"
        "  * On the FULL H^{ot2}, ker m_2 automatically CONTAINS wedge^2 H (V_4 is\n"
        "    graded-symmetric => kills the antisymmetric part); this kernel is\n"
        "    UNPHYSICAL and removed by DECOUPLING (wedge^2 appears in neither the\n"
        "    Sigma kinetic nor the source term). The auxiliarity statement is a\n"
        "    statement on Sym^2 H, NOT on all of H^{ot2}.\n"
        "  * m_2 has SYMMETRIC OUTPUTS (T1e), which is what makes the equivalence\n"
        "    ker(m_2|Sym^2)=0 <=> V_4|Sym^2 non-deg actually hold.\n"
        "HEURISTIC ONLY (T4, NOT certified): the toy 'no-pole/measure-zero' model\n"
        "  illustrates the contact-term picture but is NOT evidence -- pole-freeness\n"
        "  is automatic and unrelated to non-degeneracy, and 'generic' is meaningless\n"
        "  for the single fixed CFT vertex.\n"
        "OPEN (CFT-level, NOT settled here): the infinite-dimensional non-degeneracy\n"
        "  of V_4 on Sym^2(ker L_0^- cap ker b_0^-) -- i.e. that the quartic contact\n"
        "  vertex has no symmetric null vectors. The toy REDUCES the question to this\n"
        "  spectral condition; it does not certify it."
    )
