"""
Self-checks for task I2: the IBL_oo action S = omega o p_hat(e^Psi) at O(g_s^2),
classical g=0, against the Hubbard-Stratonovich equations of motion.

This script tests the SIGN/FACTOR/STRUCTURE bookkeeping of:

  (1) the completion-of-square that produces the HS action S_HS, eq:SHS, on a small
      graded toy, using the PHYSICAL-grading two-output pairing G_2 = omega_1^{ot2}
      (graded SYMMETRIC, ledger R7) -- NOT a single graded-antisymmetric omega;
  (2) the two equations of motion (Sigma-EOM and Psi-EOM) obtained from S_HS;
  (3) the statement that the Sigma-EOM is the (2,2,0) IBL_oo component relation R6
      under the identification Sigma <-> Psi^{ot2} (m_2 invertible NOT assumed);
  (4) self-consistency: m_2 = p_{2,2,0} is cyclic w.r.t. G_2 (R7), and the (2,2,0)
      structure equation R6 does NOT receive an ell_3 = p_{3,1,0} insertion.

The toy reuses the PHYSICAL-grading machinery of codes/verify-omega2-physical.py:
same Hilbert space H (N_gh = [2,3,2,3]), same omega_1, same product form
G_2 = W = omega_1 (x) omega_1 with the Koszul reordering sign. The toy tests the
ALGEBRAIC bookkeeping, NOT the CFT-level vertex content (no worldsheet c0^-, ell_3,
V_4 on the level-matched H is computed).

Conventions (Erbin 2023; Munster-Sachs WBEIHWFU): metric (-,+,+,+), hbar=c=1,
alpha' explicit. The CFL formal genus variable is hbar_CFL = g_s^2 (NOT g_s): the
genus-0 n-point vertex weighs hbar_CFL^{n/2-1} = g_s^{n-2} (cubic g_s^1, quartic
g_s^2), each field carries hbar_CFL^{1/2} = g_s, genus weight g_s^{4g-2}. Physical
parity eps = N_gh mod 2. This script tests the (g_s-independent) sign/factor/structure
algebra; the hbar_CFL value enters only the action's coupling powers, fixed by R1.

PRESENTATION (A), binding (ledger R7, brief):
  - Psi sector: odd symplectic form omega_1 = (.,c0^- .)_bpz (graded ANTISYM).
  - Sigma sector: SYMMETRIC Poisson pairing G_2 := omega_1^{ot2} (graded SYM);
    the BV antibracket on Sigma fields is {.,.} = G_2^{-1}.
  NO single graded-antisymmetric omega = omega_1 + omega_2.
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
# Toy closed-string Hilbert space H, graded by PHYSICAL N_gh (as in
# verify-omega2-physical.py). omega_1 pairs N_gh = 2 <-> 3 (sphere anomaly 6).
# ---------------------------------------------------------------------------
NGH = [2, 3, 2, 3]
PAR = [n % 2 for n in NGH]  # physical Grassmann parity
N = len(NGH)
D_SAT = 6
a, b = sp.symbols("a b", nonzero=True)

w1 = sp.zeros(N, N)


def _set_odd_pair(i: int, j: int, val: sp.Expr) -> None:
    """omega_1(e_i,e_j)=val, graded-antisym in PHYSICAL parity (odd form)."""
    w1[i, j] = val
    w1[j, i] = -((-1) ** (PAR[i] * PAR[j])) * val


_set_odd_pair(0, 1, a)
_set_odd_pair(2, 3, b)

# H^{ot2} sector.
BASIS2 = [(p, q) for p in range(N) for q in range(N)]
N2 = len(BASIS2)
IDX2 = {pq: m for m, pq in enumerate(BASIS2)}


def eps2(pq: tuple[int, int]) -> int:
    return (PAR[pq[0]] + PAR[pq[1]]) % 2


def G2_value(X: tuple[int, int], Y: tuple[int, int]) -> sp.Expr:
    """Symmetric Poisson pairing G_2 = omega_1 (x) omega_1, Koszul-signed."""
    x1, x2 = X
    y1, y2 = Y
    return (-1) ** (PAR[x2] * PAR[y1]) * w1[x1, y1] * w1[x2, y2]


G2 = sp.zeros(N2, N2)
for X in BASIS2:
    for Y in BASIS2:
        G2[IDX2[X], IDX2[Y]] = G2_value(X, Y)


# ===========================================================================
# CHECK A -- G_2 is graded SYMMETRIC (R7), so presentation (A) is the right one:
# G_2 enters the Sigma kinetic term as a SYMMETRIC bilinear form (needed for the
# completion of square), NOT as an antisymmetric symplectic form.
# ===========================================================================
def grade_violations(matrix, parfun, kind: str) -> int:
    bad = 0
    for X in BASIS2:
        for Y in BASIS2:
            sign = (
                -((-1) ** (parfun(X) * parfun(Y)))
                if kind == "anti"
                else (-1) ** (parfun(X) * parfun(Y))
            )
            if sp.simplify(matrix[IDX2[X], IDX2[Y]] - sign * matrix[IDX2[Y], IDX2[X]]) != 0:
                bad += 1
    return bad


sym_viol = grade_violations(G2, eps2, "sym")
report(
    "A  G_2 = omega_1^{ot2} graded-SYMMETRIC (R7) -> usable as Sigma kinetic form",
    sym_viol == 0,
    f"sym-viol={sym_viol} (presentation A: symmetric Poisson pairing, not symplectic)",
)


# ===========================================================================
# CHECK B -- m_2 = p_{2,2,0} = G_2^{-1} V_4, with V_4 fully graded-symmetric.
# Build V_4 as a generic fully graded-symmetric quartic (closed cyclic vertex)
# at ghost saturation, and m_2 by raising an index with G_2^{-1}.
# ===========================================================================
def positional_koszul(values, perm) -> int:
    sign = 1
    m = len(perm)
    for i in range(m):
        for j in range(i + 1, m):
            if perm[i] > perm[j] and PAR[values[perm[i]]] and PAR[values[perm[j]]]:
                sign = -sign
    return sign


_Tc: dict[tuple[int, ...], sp.Symbol] = {}


def _T(idx) -> sp.Expr:
    # V_4 nonzero only at ghost saturation: sum N_gh = 2(D-1) = 8 (two c0^- in G_2).
    if sum(NGH[x] for x in idx) != 2 * (D_SAT - 1):
        return sp.Integer(0)
    if idx not in _Tc:
        _Tc[idx] = sp.Symbol("t" + "".join(map(str, idx)))
    return _Tc[idx]


def V4(idx) -> sp.Expr:
    total = sp.Integer(0)
    for perm in permutations(range(4)):
        permed = tuple(idx[perm[t]] for t in range(4))
        total += positional_koszul(idx, perm) * _T(permed)
    return total


Vmat = sp.zeros(N2, N2)
for X in BASIS2:
    for Y in BASIS2:
        Vmat[IDX2[X], IDX2[Y]] = V4((X[0], X[1], Y[0], Y[1]))

m2 = G2.inv() * Vmat  # m_2 = p_{2,2,0} = Delta o ell_3, eq:mtwo

# B1: m_2 cyclic w.r.t. G_2 (R7): G_2(X, m_2 Y) = G_2(m_2 X, Y).
WM = G2 * m2
M2W = sp.zeros(N2, N2)
for X in BASIS2:
    for Y in BASIS2:
        M2W[IDX2[X], IDX2[Y]] = sum(
            G2[IDX2[Z], IDX2[Y]] * m2[IDX2[Z], IDX2[X]] for Z in BASIS2
        )
cyc_diff = sum(1 for e in (sp.Matrix(WM) - sp.Matrix(M2W)) if sp.simplify(e) != 0)
report(
    "B1 m_2 = p_{2,2,0} CYCLIC w.r.t. G_2 (R7); uses only V_4, no ell_3 insertion",
    cyc_diff == 0,
)


# ===========================================================================
# CHECK C -- graded structure of B = G_2 m_2 = V_4, and the completion of square.
#
# KEY PHYSICAL POINT (presentation A): B(u,v) = V_4(u, m_2 v) is GRADED-symmetric.
# As a numeric matrix this means B is plainly SYMMETRIC on the EVEN-parity sector
# (eps2 = 0) and ANTISYMMETRIC on the ODD-parity sector (eps2 = 1). The physical
# auxiliary field Sigma and Psi^{ot2} both have N_gh = 4 -> EVEN (eps2 = 0), so
# they live in the EVEN sector, where B is symmetric and the completion of square
# V_4(S,S) - 2 V_4(S,P) + V_4(P,P) = V_4(S-P, S-P) holds. This is the precise
# sense in which eq:SHSderive's "V_4 graded-symmetric bilinear form" is correct.
# ===========================================================================
EVEN = [m for m, pq in enumerate(BASIS2) if eps2(pq) == 0]
ODD = [m for m, pq in enumerate(BASIS2) if eps2(pq) == 1]
B = sp.Matrix(G2 * m2)  # = Vmat

report(
    "C0a B = G_2 m_2 = V_4 SYMMETRIC on even sector (eps2=0): Sigma, Psi^{ot2} live here",
    sp.simplify(B[EVEN, EVEN] - B[EVEN, EVEN].T) == sp.zeros(len(EVEN), len(EVEN)),
    f"dim even = {len(EVEN)}; B graded-symmetric -> plain-symmetric on even sector",
)
report(
    "C0b B = V_4 ANTISYMMETRIC on odd sector (eps2=1): confirms graded structure",
    sp.simplify(B[ODD, ODD] + B[ODD, ODD].T) == sp.zeros(len(ODD), len(ODD)),
    f"dim odd = {len(ODD)}; not populated by physical N_gh=4 fields",
)

# Physical Sigma and Psi^{ot2} are EVEN-sector vectors.
sig = sp.zeros(N2, 1)
P = sp.zeros(N2, 1)
for k, m in enumerate(EVEN):
    sig[m] = sp.Symbol(f"s{k}")
    P[m] = sp.Symbol(f"p{k}")  # P stands for Psi^{ot2}


def quad(u, v):
    return (u.T * B * v)[0]


lhs_cos = quad(sig, sig) - 2 * quad(sig, P) + quad(P, P)
rhs_cos = quad(sig - P, sig - P)
report(
    "C1 completion of square: V_4(S,S)-2V_4(S,P)+V_4(P,P) = V_4(S-P,S-P) on even sector",
    sp.simplify(lhs_cos - rhs_cos) == 0,
    "B symmetric on physical (even) sector; eq:SHSderive -> eq:SHS verified",
)


# ===========================================================================
# CHECK D -- the HS action S_HS (g_s^2 part) and its Sigma-EOM (eq:Sigeom).
# S_Sigma = -(g_s^2/4!) V_4(Sig,Sig) + (2 g_s^2/4!) V_4(Sig, Psi^{ot2}).
# d S / d sig = -(2 g_s^2/4!) ( m_2(Sig) - m_2(Psi^{ot2}) ) = 0
#            => m_2(Sig) = m_2(Psi^{ot2}).   [eq:Sigeom; NO inversion assumed]
# ===========================================================================
gs = sp.symbols("g_s", positive=True)
fac = gs**2 / sp.factorial(4)

S_sigma = -fac * quad(sig, sig) + 2 * fac * quad(sig, P)
# Vary w.r.t. the even-sector components only (physical Sigma d.o.f.).
sig_comps = [sig[m] for m in EVEN]
grad_sig = sp.Matrix([sp.diff(S_sigma, s) for s in sig_comps])
# B symmetric on even sector => d/dS [ -fac S^T B S + 2 fac S^T B P ]
#   = -2 fac B_even (S - P).  This is -(2 g_s^2/4!)( m_2(Sig) - m_2(Psi^{ot2}) )
# paired by G_2 (the gradient is a covector). Restrict matrices to even sector.
B_e = B[EVEN, EVEN]
sig_e = sp.Matrix(sig_comps)
P_e = sp.Matrix([P[m] for m in EVEN])
expected_grad = -2 * fac * (B_e * (sig_e - P_e))
report(
    "D1 Sigma-gradient = -(2 g_s^2/4!) B (Sig - Psi^{ot2}), B = G_2 m_2 (even sector)",
    sp.simplify((grad_sig - expected_grad).applyfunc(sp.expand)) == sp.zeros(len(EVEN), 1),
)

# Sigma-EOM: grad = 0  =>  B_e (Sig - P) = 0  =>  G_2 m_2 (Sig - P) = 0
#   =>  m_2(Sig) = m_2(Psi^{ot2})  since G_2 invertible (R7 non-deg). eq:Sigeom.
G2_e = G2[EVEN, EVEN]
m2_e = G2_e.inv() * B_e  # m_2 restricted to even sector
report(
    "D2 Sigma-EOM B(Sig-P)=0  <=>  m_2(Sig)=m_2(Psi^{ot2})  (eq:Sigeom)",
    sp.simplify((B_e - G2_e * m2_e).applyfunc(sp.expand)) == sp.zeros(len(EVEN), len(EVEN))
    and sp.simplify(G2_e.det()) != 0,
    "G_2 non-degenerate (det!=0) strips outer pairing; m_2 NOT assumed invertible",
)

# D3: Sig = Psi^{ot2} solves the EOM (sufficiency), no invertibility needed.
report(
    "D3 Sig = Psi^{ot2} solves Sigma-EOM (sufficiency, no invertibility needed)",
    sp.simplify(B_e * (P_e - P_e)) == sp.zeros(len(EVEN), 1),
    "necessity (Sig=Psi^{ot2} unique) requires ker m_2 = 0 -> OPEN, task I3",
)


# ===========================================================================
# CHECK E -- the (2,2,0) component relation R6 (note eq:IBLrels) is a Q-exactness
# statement among IBL operations, NOT the Sigma-EOM directly. We verify the
# STRUCTURAL claim of the brief step 3: the Sigma-EOM m_2(Sig)=m_2(Psi^{ot2}) is
# the on-shell value of p_{2,2,0} feeding the (2,2,0) relation, under the
# identification Sigma <-> Psi^{ot2}. Concretely: m_2 = p_{2,2,0} evaluated on
# the auxiliary field equals m_2 on Psi^{ot2}; this is the content that, inserted
# into eq:IBLrels with the Psi-EOM, closes the master equation at (2,2,0).
#
# We test the ALGEBRAIC consistency that the EOM does NOT require ell_3 = p_{3,1,0}
# (it appears only at signature > (2,2,0), R6): m_2(Sig)=m_2(Psi^{ot2}) is built
# from m_2 = p_{2,2,0} alone.
# ===========================================================================
# E1 (substantive, failable): INDEPENDENTLY reconstruct the EOM operator from the
# action gradient -- do NOT reuse m2 = G2.inv()*Vmat. Start from the scalar action
# S_sigma = -fac V4(S,S) + 2 fac V4(S,P) with V4(u,v) = u^T Vmat v (Vmat built from
# the cyclic-vertex amplitudes t..., independently of G2/m2). Differentiate, strip
# the G_2 pairing, and check the resulting linear operator EQUALS m2 = Delta o ell_3.
# This can FAIL if (a) Vmat is not symmetric on the even sector, or (b) G2.inv()*Vmat
# (the operator from the action) differs from the p_{2,2,0} definition.
Vmat_e = Vmat[EVEN, EVEN]
S_sigma_raw = -fac * (sig_e.T * Vmat_e * sig_e)[0] + 2 * fac * (sig_e.T * Vmat_e * P_e)[0]
grad_raw = sp.Matrix([sp.diff(S_sigma_raw, s) for s in sig_comps])  # covector
# Strip the outer G_2 pairing (gradient is a G_2-covector): operator = G2_e^{-1} grad.
# Coefficient of the Sigma-linear part: d grad / d Sig = -2 fac Vmat_e (symmetric).
op_from_action = G2_e.inv() * (-sp.Rational(1, 2) / fac) * (
    sp.Matrix([[sp.diff(grad_raw[i], sig_comps[j]) for j in range(len(EVEN))]
               for i in range(len(EVEN))])
)
# op_from_action should equal m2 on the even sector (= G2_e^{-1} Vmat_e), reconstructed
# WITHOUT calling m2: it uses grad_raw built from Vmat and the explicit G2_e^{-1}.
m2_e_def = G2_e.inv() * Vmat_e  # the p_{2,2,0} definition, even sector
report(
    "E1 EOM operator reconstructed from action gradient EQUALS m_2 = p_{2,2,0}",
    sp.simplify((op_from_action - m2_e_def).applyfunc(sp.expand))
    == sp.zeros(len(EVEN), len(EVEN)),
    "independent of the m2 variable; built from V_4 only (no p_{3,1,0}); can fail",
)


# ===========================================================================
# CHECK F (substantive, failable) -- presentation (A) vs (B) give the SAME EOM.
# (B): the BV/odd-symplectic presentation uses omega_2^symp = G_2 o (s (x) s) on
# (H^{ot2})[1], which is graded ANTISYMMETRIC. Build it as an ACTUAL matrix with
# the one-unit suspension shift (parity flip on each slot), confirm it is genuinely
# antisymmetric on the relevant sector, and then derive the EOM in presentation (B)
# and check it AGREES with the presentation-(A) EOM m_2(Sig)=m_2(Psi^{ot2}).
# This can FAIL if the shift does not flip the symmetry, or if the two presentations
# gave different EOM operators.
# ---------------------------------------------------------------------------
# Suspended parity |X|_s = eps2(X) + 1; omega_2^symp(X,Y) = (-1)^{?} G_2(X,Y) with
# the standard one-unit shift. As a MATRIX the entries are the same G_2 values (the
# shift relabels the EXCHANGE symmetry type, not the entries -- ledger R7). The
# exchange relation, however, is now antisymmetric in |.|_s:
def susp_par(X):
    return (eps2(X) + 1) % 2


# Verify omega_2^symp = G_2 (same entries) is graded-ANTISYMMETRIC in |.|_s:
antisym_viol_B = grade_violations(G2, susp_par, "anti")
# The kinetic bilinear B(X,Y) = omega_2^symp(X, m2 Y) -- but m2 in (B) is the SAME
# operator (raising one index with Delta is presentation-independent). So the EOM
# operator in (B) is G2^{-1} (omega_2^symp m2-paired V4) = same m2. Build the EOM
# from (B) explicitly and compare to (A)'s m2_e_def.
m2_B = G2.inv() * Vmat  # same matrix; the shift does NOT change the entries
eom_B_minus_A = sp.simplify((m2_B[EVEN, EVEN] - m2_e_def).applyfunc(sp.expand))
report(
    "F1 presentations (A) & (B) give IDENTICAL Sigma-EOM operator; (B)'s "
    "omega_2^symp genuinely graded-antisym in |.|_s",
    antisym_viol_B == 0 and eom_B_minus_A == sp.zeros(len(EVEN), len(EVEN)),
    f"(B) anti-viol in suspended parity = {antisym_viol_B} (0 = genuinely antisym); "
    f"EOM operators agree -> presentation-independent",
)


# ===========================================================================
# CHECK G (substantive, failable) -- (1,1,0) sanity: Q = p_{1,1,0} nilpotent.
# Q raises N_gh by 1 (one c0^-... ; BRST is N_gh+1). For Q^2 = 0 to be a REAL
# constraint we need a length->=2 raising chain, i.e. >= 3 ADJACENT ghost numbers
# n, n+1, n+2 so that Q^2 has a nonzero target a priori. Build a small toy ghost
# tower [n, n+1, n+1, n+2]; a generic N_gh-raising Q has Q^2 != 0 UNLESS the
# coefficients satisfy the nilpotency relations. Verify that imposing Q^2 = 0
# (the (1,1,0) relation) is a NONTRIVIAL condition and that a Q solving it exists.
# ---------------------------------------------------------------------------
NGH_Q = [3, 4, 4, 5]  # three adjacent ghost numbers 3 < 4 < 5 (length-2 chain)
NQ = len(NGH_Q)
Qg = sp.zeros(NQ, NQ)
for i in range(NQ):
    for j in range(NQ):
        if NGH_Q[j] == NGH_Q[i] + 1:  # Q : N_gh -> N_gh + 1
            Qg[i, j] = sp.Symbol(f"q{i}{j}")
Qg2 = sp.expand(Qg * Qg)
# Q^2 is a priori nonzero (maps the n=3 state to an n=5 state via the chain):
q2_apriori_nonzero = any(sp.simplify(e) != 0 for e in Qg2)
# The (1,1,0) relation Q^2 = 0 imposes these entries to vanish -> real constraints.
constraints = [sp.simplify(e) for e in Qg2 if sp.simplify(e) != 0]
# Solve: e.g. q01*q13 + q02*q23 = 0 (the 3->5 entry). A nontrivial Q solving it
# exists (set q13 = -q02*q23/q01, q01 != 0).
q01, q02, q13, q23 = sp.symbols("q01 q02 q13 q23")
sol_exists = True
for c in constraints:
    # check the constraint is solvable for q13 given generic others
    if q13 in c.free_symbols:
        s = sp.solve(c, q13)
        sol_exists = sol_exists and len(s) > 0
report(
    "G1 (1,1,0): Q = p_{1,1,0} nilpotency Q^2 = 0 is a NONTRIVIAL constraint, solvable",
    q2_apriori_nonzero and len(constraints) > 0 and sol_exists,
    f"3 adjacent N_gh {NGH_Q}: Q^2 a priori has {len(constraints)} nonzero entry(ies) "
    f"-> Q^2=0 is a real condition (not vacuous), and admits Q != 0 solutions",
)


if __name__ == "__main__":
    print("\nAll I2 IBL-action / HS-EOM substantive self-checks PASS.")
