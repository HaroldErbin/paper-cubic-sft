"""
Symbolic self-checks for the cubic closed SFT overview note.

Each block verifies one non-trivial relation restated in
knowledge/cubic-sft-overview.tex. The relations and their sources are:

  C1. Hubbard-Stratonovich completion of the square: adding
      dS = -(g^2/4!) V4(S - P2, S - P2)  to the O(g^2) action reproduces
      S_HS and the EOM m2(S) = m2(P2), i.e. S = P2 on-shell when m2 is
      invertible.  Source: context-cubic-sft.md (delta S, S_HS, EOM).

  C2. The s-channel four-point puncture location
        Z4 = (q / 16 b^2) (1 + 4 b^2 / q)^2
      equals  cosh^2 H(q)  with H(q) = ln(2 b / sqrt(q)).
      Source: notes_4_point_summary.tex; context doc Z4^(s), H(q).

  C3. The auxiliary-field propagator of Erbin-Firat,
        tilde Delta = b0 (1 - e^{-2 l L0}) / L0,
      is regular as L0 -> 0 with small-L0 expansion 2 l b0 (1 - l L0 + ...).
      Source: review C9ETB6WE, eq. (2.17).

  C4. Yang-Mills strictification (Borsten et al.): integrating out the
      rank-3 auxiliary G with action
        L = -1/2 G_{mnk} box G^{mnk} - g (d_m A_n + (1/sqrt2) d^k G_{kmn})[A^m, A^n]
      reproduces the non-local quartic vertex.  We verify the scalar/index
      bookkeeping of the completion of the square on a simplified
      representative (single contraction): integrating out G gives back
      -(1/2) (1/box) (source)^2 with the correct coefficient.
      Source: review FBSP8UQ9, eqs. around (4th/5th order action).

  C5. IBL_oo degree formula and the L_oo embedding consistency:
      |p_{k,l,g}| = -2d(k+g-1) - 1.  Check that for (k,l,g)=(1,1,0) it gives
      a differential of degree -1, and that the L_oo truncation l=1,g=0
      gives |p_{k,1,0}| = -2d(k-1)-1, matching CFL.  Source: review RPEPEC4L.

  C6. Well-formedness of the corrected CFL signature-(2,2,0) structure equation
      (the F1 fix): its terms are exactly {Q, m2} and {cobracket, bracket}, it
      contains NO ell_3 = p_{3,1,0}, the CFL signature ordering places (2,2,0)
      before (3,1,0), and the surviving compositions are degree-homogeneous.
      Source: review RPEPEC4L, Lemma 2.6 table and Def. 2.5 ordering.
"""

from __future__ import annotations

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
# C1. Hubbard-Stratonovich completion of the square.
# We model the algebra abstractly with commuting scalar placeholders that
# stand for the BV brackets, since the claim is purely the structure of a
# quadratic completion. V4 is a symmetric bilinear form B(., .); V3 is fixed.
# Action pieces (drop the V2 kinetic term, irrelevant to the completion):
#   S0  = (g/3!) c3                              [the V3 term]
#   dS  = -(g^2/4!) B(Sig - P, Sig - P)          [HS insertion]
# with B(X, Y) the value of V4 on (X, Y); P := Psi^2, Sig the aux field.
# Claim (context doc): S_HS = (g/3!)c3 - (g^2/4!) B(Sig,Sig) + (2 g^2/4!) B(Sig,P)
#                       (up to the field-independent -(g^2/4!)B(P,P) piece).
# ---------------------------------------------------------------------------
g, c3 = sp.symbols("g c3", real=True)
# B is a symmetric bilinear form; represent its values on the relevant pairs.
BSS, BSP, BPP = sp.symbols("BSS BSP BPP", real=True)  # B(Sig,Sig), B(Sig,P), B(P,P)

dS = -(g**2 / sp.factorial(4)) * (BSS - 2 * BSP + BPP)  # B(Sig-P,Sig-P), B symmetric
S_HS_claimed = (
    (g / sp.factorial(3)) * c3
    - (g**2 / sp.factorial(4)) * BSS
    + (2 * g**2 / sp.factorial(4)) * BSP
)
S0 = (g / sp.factorial(3)) * c3
# The HS action equals S0 + dS up to the field-independent constant -(g^2/4!)B(P,P).
diff = sp.simplify((S0 + dS) - (S_HS_claimed - (g**2 / sp.factorial(4)) * BPP))
report("C1a HS action = S0 + dS (mod const)", diff == 0, f"diff={diff}")

# EOM for Sigma.  Model V4 by a symmetric bilinear form on a finite-dim
# representative space: V4(X,Y) = X^T M Y with M = M^T the matrix of m2 (so
# m2(X) := M X).  The Sigma-dependent action is
#   F(Sig) = -(g^2/4!) Sig^T M Sig + (2 g^2/4!) Sig^T M P .
# Stationarity grad_Sig F = 0  =>  -(2 g^2/4!) M Sig + (2 g^2/4!) M P = 0
#   <=>  M Sig = M P  <=>  m2(Sig) = m2(Psi^2).  If M (=m2) is invertible,
# Sig = P, i.e. Sigma = Psi^2 on-shell.
sig1, sig2, p1, p2 = sp.symbols("sig1 sig2 p1 p2", real=True)
m11, m12, m22 = sp.symbols("m11 m12 m22", real=True)  # symmetric M entries
M = sp.Matrix([[m11, m12], [m12, m22]])
Sig = sp.Matrix([sig1, sig2])
P = sp.Matrix([p1, p2])
F = (-(g**2 / sp.factorial(4)) * (Sig.T * M * Sig)
     + (2 * g**2 / sp.factorial(4)) * (Sig.T * M * P))[0]
grad = sp.Matrix([sp.diff(F, s) for s in (sig1, sig2)])
# grad should equal -(2 g^2/4!) (M Sig - M P)
expected_grad = -(2 * g**2 / sp.factorial(4)) * (M * Sig - M * P)
report("C1b grad_Sig S_HS = -(2g^2/4!)(m2(Sig)-m2(P))",
       sp.simplify(grad - expected_grad) == sp.zeros(2, 1),
       f"grad-expected={list(sp.simplify(grad - expected_grad))}")
# Solve grad=0 for Sig with M invertible -> Sig = P (Sigma = Psi^2 on-shell).
sol = sp.solve([sp.Eq(grad[0], 0), sp.Eq(grad[1], 0)], [sig1, sig2], dict=True)[0]
report("C1c m2 invertible => Sigma = Psi^2 on-shell",
       sp.simplify(sol[sig1] - p1) == 0 and sp.simplify(sol[sig2] - p2) == 0,
       f"sol={sol}")


# ---------------------------------------------------------------------------
# C2. s-channel puncture location vs cosh^2 H.
# ---------------------------------------------------------------------------
q, b = sp.symbols("q beta", positive=True)
H = sp.log(2 * b / sp.sqrt(q))
# rewrite(exp) turns cosh(log(.)) into algebraic form so simplify can reduce it
Z_cosh = (sp.cosh(H) ** 2).rewrite(sp.exp)
Z_formula = (q / (16 * b**2)) * (1 + 4 * b**2 / q) ** 2
report(
    "C2 Z4^(s): (q/16b^2)(1+4b^2/q)^2 = cosh^2(ln(2b/sqrt q))",
    sp.simplify(Z_cosh - Z_formula) == 0,
    f"diff={sp.simplify(Z_cosh - Z_formula)}",
)
# Also check t- and u-channel companions for internal consistency:
#   Z^(t) = cosh^2 H / sinh^2 H,  Z^(u) = -1/sinh^2 H.
Zt = (sp.cosh(H) ** 2 / sp.sinh(H) ** 2).rewrite(sp.exp)
Zu = (-1 / sp.sinh(H) ** 2).rewrite(sp.exp)
# Standard cross-ratio identities: Z^(s) + relations.  Check Z^(s)-Z^(t)*...:
# Mobius consistency lambda_s + lambda_t-type: here we just confirm the
# three are related by 1 - Zs = ... (sanity, cross ratio closes):
report(
    "C2b cross-ratio closure: Zt = Zs/(Zs-1) holds with Zs=cosh^2,Zt=coth^2",
    sp.simplify(Zt - Z_formula / (Z_formula - 1)) == 0,
    f"diff={sp.simplify(Zt - Z_formula/(Z_formula-1))}",
)
report(
    "C2c Zu = 1/(1-Zs)",
    sp.simplify(Zu - 1 / (1 - Z_formula)) == 0,
    f"diff={sp.simplify(Zu - 1/(1-Z_formula))}",
)


# ---------------------------------------------------------------------------
# C3. Auxiliary propagator regularity (Erbin-Firat).
# tilde Delta(L0) = (1 - e^{-2 l L0}) / L0  (drop the b0 ghost factor, scalar).
# Check the L0 -> 0 limit is finite (= 2 l) and the small-L0 series is
# 2 l (1 - l L0 + ...).
# ---------------------------------------------------------------------------
L0, lam = sp.symbols("L0 lambda", real=True, positive=True)
tilde = (1 - sp.exp(-2 * lam * L0)) / L0
lim0 = sp.limit(tilde, L0, 0)
report("C3a propagator finite as L0->0 (=2 lambda)", sp.simplify(lim0 - 2 * lam) == 0,
       f"limit={lim0}")
ser = sp.series(tilde, L0, 0, 2).removeO()
expected = 2 * lam - 2 * lam**2 * L0  # 2 l (1 - l L0)
report("C3b small-L0 series = 2 lambda (1 - lambda L0 + ...)",
       sp.simplify(ser - expected) == 0, f"series={ser}")


# ---------------------------------------------------------------------------
# C4. Yang-Mills strictification: completion of the square reproduces the
# non-local quartic vertex.  Simplified scalar representative:
#   L(G) = -1/2 G box G - (1/sqrt2) G J ,
# where J stands for the source d^k(...)[A,A] contracted appropriately and
# 'box' is the (invertible, momentum-space) wave operator.  Integrating out G:
#   EOM: box G + (1/sqrt2) J = 0  =>  G = -(1/sqrt2) J / box.
# Substituting back:  L_on-shell = (1/4) J (1/box) J.
# The original non-local quartic vertex is  +(1/4) J (1/box) J  (matching the
# completion of the square with the sign of the cyclic pairing).  We verify the
# coefficient bookkeeping symbolically.
# ---------------------------------------------------------------------------
G, box, J = sp.symbols("G box J", real=True)
L_aux = -sp.Rational(1, 2) * G * box * G - (1 / sp.sqrt(2)) * G * J
G_eom = sp.solve(sp.diff(L_aux, G), G)[0]
report("C4a G EOM = -(1/sqrt2) J / box", sp.simplify(G_eom - (-(1 / sp.sqrt(2)) * J / box)) == 0,
       f"G={G_eom}")
L_onshell = sp.simplify(L_aux.subs(G, G_eom))
report("C4b on-shell aux Lagrangian = (1/4) J (1/box) J",
       sp.simplify(L_onshell - sp.Rational(1, 4) * J / box * J) == 0,
       f"L_onshell={L_onshell}")


# ---------------------------------------------------------------------------
# C5. IBL_oo degree formula.
# |p_{k,l,g}| = -2 d (k+g-1) - 1.
# ---------------------------------------------------------------------------
d, k, ell, gg = sp.symbols("d k l g", integer=True)
deg = -2 * d * (k + gg - 1) - 1
report("C5a differential (1,1,0): degree -1",
       sp.simplify(deg.subs({k: 1, gg: 0}) - (-1)) == 0,
       f"deg(1,1,0)={deg.subs({k:1, gg:0})}")
deg_Loo = deg.subs({gg: 0})  # L_oo truncation l=1, g=0
report("C5b L_oo truncation: |p_{k,1,0}| = -2 d (k-1) - 1",
       sp.simplify(deg_Loo - (-2 * d * (k - 1) - 1)) == 0,
       f"deg(k,1,0)={deg_Loo}")
# Euler number bookkeeping: a (k,l,g) surface has chi = 2 - 2g - k - l.
chi = 2 - 2 * gg - k - ell
report("C5c Euler number chi = 2-2g-k-l for (2,2,0) sphere with 4 punctures",
       sp.simplify(chi.subs({k: 2, ell: 2, gg: 0}) - (-2)) == 0,
       f"chi(2,2,0)={chi.subs({k:2, ell:2, gg:0})}")


# ---------------------------------------------------------------------------
# C6. The corrected CFL signature-(2,2,0) structure equation (RPEPEC4L, Lemma
# 2.6 table) is *well-formed*: it is the s=1 sector of the component master
# equation (CFL eq. 2.4),
#   sum_{s} sum_{k1+k2=k+s, l1+l2=l+s, g1+g2=g+1-s}
#       ( phat_{k2,l2,g2}  o_s  phat_{k1,l1,g1} )|_{E_k C} = 0 ,
# specialised to (k,l,g)=(2,2,0).  We verify two things this revision asserts:
#   (a) for (k,l,g)=(2,2,0), s=1, the SOLUTIONS of the index constraints with
#       all (k_i,l_i,g_i) admissible (k_i,l_i>=1, g_i>=0) are exactly the four
#       unordered partial compositions appearing in eq:IBLrels, namely the
#       pairs {(1,1,0),(2,2,0)}, {(2,2,0),(1,1,0)}, {(1,2,0),(2,1,0)},
#       {(2,1,0),(1,2,0)} -- i.e. Q-m2 (two orders), and cobracket-bracket
#       (two orders).  In particular NO term involves p_{3,1,0}=ell_3.
#   (b) the signature ordering of CFL Def. 2.5 places (3,1,0) [= ell_3] AFTER
#       (2,2,0), confirming ell_3 cannot enter the m2 structure equation.
# These are the precise structural facts the corrected text claims; the full
# operadic identity p^.p^=0 itself is not closed-form sympy-checkable and is
# quoted verbatim from CFL (stated in the Verification block of the note).
# ---------------------------------------------------------------------------
# (a) enumerate index solutions for (k,l,g)=(2,2,0), s=1.
K, L, G, s = 2, 2, 0, 1
pairs = []
for k1 in range(1, K + s):
    k2 = K + s - k1
    for l1 in range(1, L + s):
        l2 = L + s - l1
        for g1 in range(0, G + 2 - s):
            g2 = G + 1 - s - g1
            if k2 >= 1 and l2 >= 1 and g2 >= 0:
                pairs.append(((k1, l1, g1), (k2, l2, g2)))
# Expected: the four (ordered) compositions. We compare as a set of frozensets
# of the two signatures (unordered pair), deduplicated.
got = {frozenset((a, b)) for (a, b) in pairs}
expected = {
    frozenset(((1, 1, 0), (2, 2, 0))),   # Q and m2
    frozenset(((1, 2, 0), (2, 1, 0))),   # cobracket and bracket
}
report("C6a (2,2,0) master-eq terms are {Q,m2} and {cobracket,bracket} only",
       got == expected, f"got={sorted(tuple(sorted(p)) for p in got)}")
# Explicitly: ell_3 = p_{3,1,0} is absent.
ell3_present = any((3, 1, 0) in (a, b) for (a, b) in pairs)
report("C6b ell_3 = p_{3,1,0} does NOT appear in the (2,2,0) relation",
       not ell3_present, f"ell3_present={ell3_present}")

# (b) signature ordering of CFL Def. 2.5: ordered by (k+g, then ... ) such that
#     (1,1,0)<(1,2,0)<(2,1,0)<(1,1,1)<(1,3,0)<(2,2,0)<(3,1,0)<...
# We reproduce the published ordering as a list and check (2,2,0) precedes
# (3,1,0).
cfl_order = [
    (1, 1, 0), (1, 2, 0), (2, 1, 0), (1, 1, 1),
    (1, 3, 0), (2, 2, 0), (3, 1, 0),
]
report("C6c CFL signature ordering places (2,2,0) before (3,1,0)=ell_3",
       cfl_order.index((2, 2, 0)) < cfl_order.index((3, 1, 0)),
       f"idx(2,2,0)={cfl_order.index((2,2,0))} < idx(3,1,0)={cfl_order.index((3,1,0))}")

# (c) all four terms carry equal degree: a composed term phat_{k2,l2,g2} o
#     phat_{k1,l1,g1} has degree |p_{k1,l1,g1}|+|p_{k2,l2,g2}| with
#     |p_{k,l,g}| = -2d(k+g-1)-1.  Check the two surviving compositions have
#     the same total degree (necessary for the relation to be homogeneous).
def pdeg(kk, gg_, dd):
    return -2 * dd * (kk + gg_ - 1) - 1
dsym = sp.symbols("d", integer=True)
deg_Qm2 = pdeg(1, 0, dsym) + pdeg(2, 0, dsym)          # {Q, m2}
deg_cb = pdeg(1, 0, dsym) + pdeg(2, 0, dsym)           # {cobracket(1,2,0), bracket(2,1,0)}
report("C6d the two compositions in the (2,2,0) relation have equal degree",
       sp.simplify(deg_Qm2 - deg_cb) == 0,
       f"deg(Q.m2)={deg_Qm2}, deg(cobr.bra)={deg_cb}")

print("\nAll symbolic self-checks passed.")
