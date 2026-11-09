"""
Self-checks for the A3 pedagogical note `knowledge/cubic-sft-ibl-pedagogical.tex`.

Only the *newly stated* relations of A3 are checked here (the ledger results
R1-R14 are reused, not re-derived).  Three blocks:

  Hq4  physical ghost-number (N_gh) balance of the IBL_infty component relations
       (1,1,0) ... (2,2,0), and the claim that ghost-number homogeneity of the
       (2,2,0) relation *forces* N_gh(p_{1,2,0}) = +4.  (Undoing the CFL/Munster-
       Sachs suspension: the physical grading of every structure map.)
       Hq4-sat DERIVES the absolute N_gh of every map from the omega_1/G_2
       saturations alone (three independent routes), with NO hard-coded table --
       added after critic finding C2/S1 (2026-07-02): the original version
       hard-coded N_gh(m2) = -2, which is inconsistent (the Delta-raising shift
       is +5, not +1); the corrected value is N_gh(m2) = +2.

  Hq2  full symmetry of the Sigma kinetic term <Sigma, m2(Sigma)> under exchange
       of the two Sigma's, (i) for a general p_{2,2,0} (only the symmetric part
       survives the quadratic form; genuine bilinear symmetry can FAIL), and
       (ii) for m2 = Delta o ell_3 built from a totally graded-symmetric V4
       (then it holds -- cyclicity, R7).  Reuses the physical-grading toy of
       codes/verify-omega2-physical.py.

  Hq5  Harold's Yang-Mills auxiliary h_{mu nu} = [A_mu, A_nu]: eliminating the
       ULTRALOCAL auxiliary reproduces the quartic -1/4 tr[A_mu,A_nu][A^mu,A^nu]
       exactly, and its kinetic operator is the identity (trivially invertible,
       no 1/Box) -- the contact-type analogue of the closed-string Sigma, to be
       compared with the colour-kinematic 1/Box form (R4).

Conventions: Erbin (2023); metric (-,+,+,+) (Hq5 uses a Euclidean toy metric,
flagged); physical N_gh grading throughout.  sympy only.
"""

from __future__ import annotations

from itertools import permutations

import sympy as sp


def report(name: str, ok: bool, detail: str = "") -> None:
    """Print a PASS/FAIL line and raise on failure."""
    status = "PASS" if ok else "FAIL"
    line = f"[{status}] {name}"
    if detail:
        line += f"  --  {detail}"
    print(line)
    if not ok:
        raise AssertionError(f"check failed: {name}")


# ===========================================================================
# Hq4 -- physical ghost-number balance of the IBL_infty component relations.
#
# Physical N_gh (Erbin 2023; sphere anomaly N_gh=6, one c0^- -> omega_1 pairs
# N_gh sum 5; n-pt genus-0 vertex saturates at sum 2n):
#   fields:      N_gh(Psi)=2, N_gh(Sigma)=4
#   operations:  Q=p_{1,1,0}:+1, ell_2=p_{2,1,0}:-1, p_{1,2,0}:x (to be fixed),
#                ell_3=p_{3,1,0}:-3, m2=p_{2,2,0}:+2, p_{1,1,1}:y.
# N_gh(ell_n) = 3-2n is derived from V_n(A_1..A_n) = omega_1(A_1, ell_{n-1}(..))
# with omega_1 pairing sum 5 and each A_i at N_gh 2.
# N_gh(m2) = +2: Delta = omega_1^{-1} is a bivector of total ghost 5, so raising
# one input of ell_n into an output shifts N_gh by +5 (NOT +1).
# ===========================================================================

# --- Hq4-sat: DERIVE the absolute gradings from the saturations (no table) ---
S1 = 6 - 1  # omega_1 = <.|c0^-|.> saturation: sphere anomaly 6 minus one c0^-
SG2 = 2 * S1  # G2 = omega_1 (x) omega_1 saturation

# route 1: V_{n+1} = omega_1(A_1, ell_n(A_2..A_{n+1})), vertex saturation 2(n+1)
#          => N(ell_n) = S1 - 2 - (2(n+1) - 2 - 2n) ... i.e. solve the balance:
ngh_ell = {}
for n in (1, 2, 3):
    Nl = sp.Symbol("Nl")
    # N(A_1) + [sum_{i>=2} N(A_i) + N(ell_n)] = S1 with all A_i at ghost 2
    (soln,) = sp.solve(sp.Eq(2 + (2 * n + Nl), S1), Nl)
    ngh_ell[n] = soln
report(
    "Hq4-sat route 1: omega_1 saturation reproduces N_gh(ell_n)=3-2n",
    all(ngh_ell[n] == 3 - 2 * n for n in (1, 2, 3)),
    f"{ngh_ell}",
)

# route 2: Delta = omega_1^{-1} is a bivector of total ghost S1=5, so the
#          raising shift is +5: m2 = Delta o ell_3, cobracket = Delta o ell_2.
m2_r2 = ngh_ell[3] + S1
cob_r2 = ngh_ell[2] + S1
report(
    "Hq4-sat route 2 (Delta-raising +5): N_gh(m2)=+2, N_gh(p_{1,2,0})=+4",
    (m2_r2, cob_r2) == (2, 4),
    f"m2 = {ngh_ell[3]}+{S1} = {m2_r2}; cobracket = {ngh_ell[2]}+{S1} = {cob_r2}",
)

# route 3: out-minus-in with outputs at ghost 3 (each output pairs with an
#          external ghost-2 state under one omega_1 of G2, since S1 - 2 = 3):
OUT = S1 - 2
m2_r3 = 2 * OUT - (2 + 2)  # two outputs, two ghost-2 inputs
cob_r3 = 2 * OUT - 2  # two outputs, one ghost-2 input
q_r3 = OUT - 2  # one output, one input
report(
    "Hq4-sat route 3 (out-minus-in, outputs at 3): m2=+2, cobracket=+4, Q=+1",
    (m2_r3, cob_r3, q_r3) == (2, 4, 1),
    f"m2 = {m2_r3}; cobracket = {cob_r3}; Q = {q_r3}",
)

# and the G2-saturation consistency: V4 saturates at 8, G2 at 10, so
# N(m2) = SG2 - 8 = +2  (V4(A1..A4) = G2(A1 (x) A2, m2(A3 (x) A4))).
report(
    "Hq4-sat G2 consistency: N_gh(m2) = G2_sat - V4_sat = 10 - 8 = +2",
    SG2 - 8 == 2,
)

# N_gh(ell_n = p_{n,1,0}) = 3 - 2n : sanity for n=1,2,3.
_ellgh = {n: 3 - 2 * n for n in (1, 2, 3)}
report(
    "Hq4-0 N_gh(ell_n)=3-2n : Q=+1, ell_2=-1, ell_3=-3",
    (_ellgh[1], _ellgh[2], _ellgh[3]) == (1, -1, -3),
    f"{_ellgh}",
)

# A structure map p_{k,l,g} composed as a term contributes its N_gh additively.
# Represent the physical N_gh of each map; p_{1,2,0} and p_{1,1,1} unknown.
x = sp.Symbol("x", integer=True)  # N_gh(p_{1,2,0})
y = sp.Symbol("y", integer=True)  # N_gh(p_{1,1,1})
NGH_OP = {
    (1, 1, 0): 1,  # Q
    (2, 1, 0): -1,  # ell_2
    (3, 1, 0): -3,  # ell_3
    (2, 2, 0): 2,  # m2 (derived in Hq4-sat above; corrected from -2)
    (1, 2, 0): x,  # cobracket
    (1, 1, 1): y,  # genus-1 involutivity homotopy
}
report(
    "Hq4 table consistency: hard-coded N_gh(m2) equals the Hq4-sat derivations",
    NGH_OP[(2, 2, 0)] == m2_r2 == m2_r3,
)


def term_ngh(*ops: tuple[int, int, int]) -> sp.Expr:
    """N_gh of a composite term = sum of the N_gh of its factors."""
    return sp.sympify(sum(NGH_OP[o] for o in ops))


# (1,1,0):  p_{1,1,0}^2 = 0  -- single N_gh, +2 operator. (homogeneous trivially)
report("Hq4 (1,1,0) Q^2=0 is N_gh=+2 homogeneous", term_ngh((1, 1, 0), (1, 1, 0)) == 2)

# (2,1,0):  Q o ell_2 + ell_2 o Q = 0  -- chain map, each term N_gh 0.
_t210 = [term_ngh((1, 1, 0), (2, 1, 0)), term_ngh((2, 1, 0), (1, 1, 0))]
report("Hq4 (2,1,0) ell_2 chain map: both terms N_gh=0", set(_t210) == {0}, f"{_t210}")

# (1,2,0):  Q o p_{1,2,0} + p_{1,2,0} o Q = 0 -- both terms N_gh = x+1
#           (does NOT fix x on its own).
_t120 = [term_ngh((1, 1, 0), (1, 2, 0)), term_ngh((1, 2, 0), (1, 1, 0))]
report(
    "Hq4 (1,2,0) cobracket chain map: both terms N_gh=x+1 (x free here)",
    sp.simplify(_t120[0] - _t120[1]) == 0,
    f"{_t120}",
)

# (2,2,0):  the four terms; ghost-number homogeneity FORCES x = N_gh(p_{1,2,0}).
#   T1 = p_{1,1,0} o m2       -> N_gh = 1 + 2 = +3
#   T2 = m2 o p_{1,1,0}       -> N_gh = 2 + 1 = +3
#   T3 = p_{1,2,0} o ell_2    -> N_gh = x + (-1)
#   T4 = ell_2 o p_{1,2,0}    -> N_gh = -1 + x
_t220 = [
    term_ngh((1, 1, 0), (2, 2, 0)),
    term_ngh((2, 2, 0), (1, 1, 0)),
    term_ngh((1, 2, 0), (2, 1, 0)),
    term_ngh((2, 1, 0), (1, 2, 0)),
]
_sol = sp.solve([sp.Eq(_t220[0], _t220[2]), sp.Eq(_t220[0], _t220[3])], x, dict=True)
x_val = _sol[0][x]
report(
    "Hq4 (2,2,0) homogeneity FORCES N_gh(p_{1,2,0})=+4 (all terms N_gh=+3)",
    x_val == 4 and {t.subs(x, x_val) for t in _t220} == {3},
    f"solved x = N_gh(p_(1,2,0)) = {x_val}; terms = {[t.subs(x, x_val) for t in _t220]}",
)
report(
    "Hq4 forced cobracket value agrees with the Hq4-sat direct derivations",
    x_val == cob_r2 == cob_r3,
)

# (1,1,1):  Q o p_{1,1,1} + p_{1,1,1} o Q + ell_2 o_2 p_{1,2,0} = 0
#           with x=+4 forces y = N_gh(p_{1,1,1}) = +2.
_last = term_ngh((2, 1, 0), (1, 2, 0)).subs(x, x_val)  # ell_2 o cobracket = +3
_soly = sp.solve(sp.Eq(term_ngh((1, 1, 0), (1, 1, 1)), _last), y, dict=True)
y_val = _soly[0][y]
report(
    "Hq4 (1,1,1) homogeneity forces N_gh(p_{1,1,1})=+2 (genus-1 homotopy)",
    y_val == 2,
    f"y = N_gh(p_(1,1,1)) = {y_val}; all terms N_gh = {_last}",
)

# (3,1,0):  the L_infty (Jacobi) relation Q o ell_3 + ell_2 o ell_2 + ell_3 o Q = 0
_t310 = [
    term_ngh((1, 1, 0), (3, 1, 0)),
    term_ngh((2, 1, 0), (2, 1, 0)),
    term_ngh((3, 1, 0), (1, 1, 0)),
]
report(
    "Hq4 (3,1,0) L_infty Jacobi for ell_3: all three terms N_gh=-2",
    set(_t310) == {-2},
    f"{_t310}",
)

# Cross-check the *field-content* ghost numbers of the HS action terms (eq:SHS)
#   1/2 V2(Psi^2)                     : omega_1(Psi, Q Psi)  -> 2+1+2 = ... sat 5
#   V3(Psi^3), V4(Sigma,Sigma), V4(Sigma,Psi^2): all vertex-saturating.
# The auxiliarity EOM m2(Sigma)=m2(Psi^2): both sides N_gh = 4 + 2 = 6, and
# pairing the field equation against delta-Sigma (N_gh 4) saturates G2 at 10.
report(
    "Hq4 EOM m2(Sigma)=m2(Psi^ot2): both sides N_gh = 4 + N_gh(m2) = 6; +4 saturates G2",
    4 + NGH_OP[(2, 2, 0)] == 6 and 6 + 4 == SG2,
)


# ===========================================================================
# Hq2 -- symmetry of the Sigma kinetic term <Sigma, m2(Sigma)> = V4(Sigma,Sigma).
#
# Reuse the physical-grading toy of verify-omega2-physical.py:
# H0 = R^4, N_gh = [2,3,2,3], physical parity eps = N_gh mod 2 = [0,1,0,1];
# omega_1 pairs N_gh 2<->3 (sum 5); G2 = omega_1 (x) omega_1 with Koszul signs;
# V4 totally graded-symmetric; m2 = G2^{-1} V4.
# ===========================================================================
# NB: this toy's vertex saturation (sum 10, fields+antifields basis) is an
# internal convention inherited from verify-omega2-physical.py; it certifies
# SIGNS and SYMMETRY only.  Absolute N_gh values are certified by Hq4-sat above
# (the string's V4 saturates at 8, giving N_gh(m2) = 10 - 8 = +2).
NGH = [2, 3, 2, 3]
PAR = [n % 2 for n in NGH]
N = len(NGH)
D_SAT = 6
a, b = sp.symbols("a b", nonzero=True)

w1 = sp.zeros(N, N)


def _set_odd_pair(i: int, j: int, val: sp.Expr) -> None:
    w1[i, j] = val
    w1[j, i] = -((-1) ** (PAR[i] * PAR[j])) * val


_set_odd_pair(0, 1, a)
_set_odd_pair(2, 3, b)

BASIS2 = [(p, q) for p in range(N) for q in range(N)]
N2 = len(BASIS2)
IDX2 = {pq: m for m, pq in enumerate(BASIS2)}


def eps2(pq: tuple[int, int]) -> int:
    """Physical parity of an H0^{ot2} state = sum of factor parities mod 2."""
    return (PAR[pq[0]] + PAR[pq[1]]) % 2


def G2_value(X: tuple[int, int], Y: tuple[int, int]) -> sp.Expr:
    """G2 = omega_1 (x) omega_1 with the Koszul reordering sign (physical)."""
    x1, x2 = X
    y1, y2 = Y
    return (-1) ** (PAR[x2] * PAR[y1]) * w1[x1, y1] * w1[x2, y2]


G2 = sp.zeros(N2, N2)
for X in BASIS2:
    for Y in BASIS2:
        G2[IDX2[X], IDX2[Y]] = G2_value(X, Y)


def positional_koszul(values: tuple[int, ...], perm: tuple[int, ...]) -> int:
    """Koszul sign for reordering graded slots by ``perm`` (physical parity)."""
    sign = 1
    m = len(perm)
    for i in range(m):
        for j in range(i + 1, m):
            if perm[i] > perm[j] and PAR[values[perm[i]]] and PAR[values[perm[j]]]:
                sign = -sign
    return sign


# Totally graded-symmetric V4 (closed cyclic vertex, H2 closed).
_Tc: dict[tuple[int, ...], sp.Symbol] = {}


def _T(idx: tuple[int, ...]) -> sp.Expr:
    if sum(NGH[x] for x in idx) != 2 * (D_SAT - 1):  # vertex saturation sum 10 = 2*(6-1)
        return sp.Integer(0)
    if idx not in _Tc:
        _Tc[idx] = sp.Symbol("t" + "".join(map(str, idx)))
    return _Tc[idx]


def V4(idx: tuple[int, ...]) -> sp.Expr:
    """Totally graded-symmetric quartic vertex on four H0 indices (H2)."""
    total = sp.Integer(0)
    for perm in permutations(range(4)):
        permed = tuple(idx[perm[t]] for t in range(4))
        total += positional_koszul(idx, perm) * _T(permed)
    return total


Vmat = sp.zeros(N2, N2)
for X in BASIS2:
    for Y in BASIS2:
        Vmat[IDX2[X], IDX2[Y]] = V4((X[0], X[1], Y[0], Y[1]))

m2 = G2.inv() * Vmat  # p_{2,2,0} = Delta o ell_3 in the toy

# The Sigma kinetic bilinear B(X,Y) = G2(X, m2 Y) = V4(X,Y).
Bmat = G2 * m2
report(
    "Hq2-consistency B(X,Y)=G2(X,m2 Y) equals the vertex matrix V4(X,Y)",
    sp.simplify(Bmat - Vmat) == sp.zeros(N2, N2),
)

# (ii) m2 from totally symmetric V4:  B is symmetric on the physical even sector
# (N_gh(Sigma)=4 => eps=0), i.e. <Sigma, m2 Sigma'> = <Sigma', m2 Sigma>.
EVEN = [pq for pq in BASIS2 if eps2(pq) == 0]
_sym_even = all(
    sp.simplify(Bmat[IDX2[X], IDX2[Y]] - Bmat[IDX2[Y], IDX2[X]]) == 0
    for X in EVEN
    for Y in EVEN
)
report(
    "Hq2(ii) <Sigma,m2 Sigma'> symmetric on even sector (m2 from symmetric V4)",
    _sym_even,
    "cyclicity/R7: symmetry of the Sigma kinetic term follows from full graded "
    "symmetry of V4",
)

# (i) general p_{2,2,0}: the *bilinear* B'=G2(.,p .) need NOT be symmetric.
# Build a generic (NOT V4-derived) even-sector map p and show B' asymmetric,
# while the QUADRATIC FORM only ever sees the symmetric part.
p_gen = sp.zeros(N2, N2)
_ctr = 0
for X in EVEN:
    for Y in EVEN:
        _ctr += 1
        p_gen[IDX2[X], IDX2[Y]] = sp.Symbol(f"g{_ctr}")
Bgen = G2 * p_gen
_asym = any(
    sp.simplify(Bgen[IDX2[X], IDX2[Y]] - Bgen[IDX2[Y], IDX2[X]]) != 0
    for X in EVEN
    for Y in EVEN
)
report(
    "Hq2(i) generic p_{2,2,0}: bilinear G2(.,p.) is NOT symmetric in general",
    _asym,
    "so genuine <Sigma,pSigma'> symmetry is a nontrivial property (cyclicity), "
    "not automatic",
)

# (i) but the quadratic form Q(v)=v^T Bgen v only sees the symmetric part:
# Q(v) = v^T Bgen v = v^T ((Bgen+Bgen^T)/2) v  identically.
vsym = sp.Matrix([sp.Symbol(f"v{IDX2[X]}") if X in EVEN else 0 for X in BASIS2])
_qform = sp.expand((vsym.T * Bgen * vsym)[0])
_qsym = sp.expand((vsym.T * ((Bgen + Bgen.T) / 2) * vsym)[0])
report(
    "Hq2(i) quadratic form <Sigma,pSigma> sees only the symmetric part of p",
    sp.simplify(_qform - _qsym) == 0,
    "for ANY p_{2,2,0}: the kinetic term automatically symmetrises",
)


# ===========================================================================
# Hq5(ii) -- Harold's Yang-Mills auxiliary  h_{mu nu} = [A_mu, A_nu].
#
# Ultralocal auxiliary (NO 1/Box):  L_h = 1/4 tr(h_{mu nu} h^{mu nu})
#                                        - 1/2 tr(h_{mu nu} [A^mu, A^nu]).
# h-EOM:  1/2 h_{mu nu} - 1/2 [A_mu,A_nu] = 0  =>  h_{mu nu} = [A_mu, A_nu].
# On-shell:  L_h|_* = 1/4 tr[A,A]^2 - 1/2 tr[A,A]^2 = -1/4 tr[A_mu,A_nu][A^mu,A^nu].
# Kinetic operator d^2 L_h / d h^2 = 1/2 * identity : ULTRALOCAL, invertible.
#
# Toy: 2 Lorentz components mu=0,1 (Euclidean metric here -- signature is
# irrelevant to the algebraic identity), su(2)-valued A_mu as generic 2x2
# traceless matrices with symbolic entries.
# ===========================================================================
NMU = 2  # number of Lorentz components in the toy


def _sym_traceless(tag: str) -> sp.Matrix:
    p, q, r = sp.symbols(f"{tag}p {tag}q {tag}r")
    return sp.Matrix([[p, q], [r, -p]])  # generic traceless 2x2


A = [_sym_traceless(f"A{mu}") for mu in range(NMU)]


def comm(M: sp.Matrix, Nn: sp.Matrix) -> sp.Matrix:
    """Matrix commutator [M, N]."""
    return M * Nn - Nn * M


# Target quartic:  -1/4 sum_{mu,nu} tr( [A_mu,A_nu] [A_mu,A_nu] )  (Euclidean).
target = sp.Integer(0)
for mu in range(NMU):
    for nu in range(NMU):
        C = comm(A[mu], A[nu])
        target += -sp.Rational(1, 4) * sp.trace(C * C)
target = sp.expand(target)

# Auxiliary form with h a free antisymmetric field h_{mu nu} = -h_{nu mu}.
# Independent components: h[mu][nu] for mu<nu; here only (0,1).
h01p, h01q, h01r = sp.symbols("h01p h01q h01r")
h01 = sp.Matrix([[h01p, h01q], [h01r, -h01p]])
hmat = {(0, 1): h01, (1, 0): -h01, (0, 0): sp.zeros(2), (1, 1): sp.zeros(2)}

L_h = sp.Integer(0)
for mu in range(NMU):
    for nu in range(NMU):
        L_h += sp.Rational(1, 4) * sp.trace(hmat[(mu, nu)] * hmat[(mu, nu)])
        L_h += -sp.Rational(1, 2) * sp.trace(hmat[(mu, nu)] * comm(A[mu], A[nu]))
L_h = sp.expand(L_h)

# h-EOM: solve dL_h/dh_component = 0 for the (0,1) components.
hvars = [h01p, h01q, h01r]
eom = [sp.diff(L_h, v) for v in hvars]
sol = sp.solve(eom, hvars, dict=True)[0]

# Confirm the saddle is h_{01} = [A_0, A_1].
C01 = comm(A[0], A[1])
_eom_ok = all(
    sp.simplify(sol[hvars[k]] - [C01[0, 0], C01[0, 1], C01[1, 0]][k]) == 0
    for k in range(3)
)
report(
    "Hq5(ii) h-EOM gives h_{mu nu} = [A_mu, A_nu] exactly",
    _eom_ok,
    "ultralocal auxiliary, algebraic EOM",
)

# On-shell value reproduces the quartic.
L_onshell = sp.expand(L_h.subs(sol))
report(
    "Hq5(ii) eliminating h reproduces -1/4 tr[A_mu,A_nu][A^mu,A^nu] exactly",
    sp.simplify(L_onshell - target) == 0,
)

# Kinetic operator (Hessian in h) is ultralocal = (1/2) identity: invertible,
# NO 1/Box, no momentum dependence -> the contact-type analogue of Sigma's V4.
hess = sp.Matrix([[sp.diff(sp.diff(L_h, u), v) for v in hvars] for u in hvars])
report(
    "Hq5(ii) h kinetic operator is ULTRALOCAL & invertible (Hessian const, det!=0)",
    hess.free_symbols == set() and sp.simplify(hess.det()) != 0,
    f"Hessian = {hess.tolist()}, det = {hess.det()} (no Box, always invertible)",
)


if __name__ == "__main__":
    print("\nAll A3 pedagogical self-checks PASS.")
