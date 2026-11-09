"""
Symbolic self-checks for the antisymmetric two-output symplectic form omega_2.

These check the ALGEBRAIC identities of the omega_2 construction
(agent/derivations/002-omega2-construction.md) on a finite-dimensional graded
toy model. They are internal self-checks, NOT an independent re-derivation and
NOT a proof of the abstract closed-string statement (the toy verifies only the
sign/grading algebra; the worldsheet content of c0^-, ell_3 and V_4 is modelled,
not computed). Scope is stated per check.

Conventions (Munster-Sachs / CFL suspended grading; review WBEIHWFU App. A):
  - omega_1 on H is the ODD, graded-ANTIsymmetric, non-degenerate closed-string
    symplectic form  omega_1(A,B) = <A | c0^- | B>_bpz o (s^2 ox s^2).
    Its oddness comes from the single c0^- insertion. In the toy we model omega_1
    directly as an odd graded-antisymmetric non-degenerate matrix.
  - Graded antisymmetry of an ODD form:  omega(A,B) = -(-1)^{|A||B|} omega(B,A).
  - The auxiliary field Sigma in H^{ot2} (N_gh = 4) is ONE suspended field: as a
    state in the suspended complex it carries ONE odd suspension unit beyond the
    two internal H-factors. Hence its SUSPENDED parity is
        |X|_s = (par[x1] + par[x2] + 1) mod 2.
  - W := omega_1 ox omega_1 on H^{ot2}, with the Koszul sign for reordering:
        W(x1 ox x2, y1 ox y2) = (-1)^{|x2||y1|} omega_1(x1,y1) omega_1(x2,y2).
  - tau is the graded swap of the two H slots: tau(u ox v) = (-1)^{|u||v|} v ox u.

The PROOF of graded antisymmetry rests on a SUPPORT argument, not on an
unconditional sign identity. The bare sign step

    (-1)^{ab}  ==  -(-1)^{(a+1)(b+1)}                                    (D.2)

with a = |X|_int, b = |Y|_int in {0,1}, is CONDITIONAL: expanding
(a+1)(b+1) = ab + a + b + 1 gives -(-1)^{(a+1)(b+1)} = (-1)^{ab} (-1)^{a+b}, so
(D.2) holds iff a + b is EVEN -- true for (0,0),(1,1); FALSE for (1,0),(0,1).
What makes the conclusion sound is that omega_2 = W vanishes off the support
where (D.2) holds: omega_1 is ODD, so omega_1(x_i, y_i) != 0 forces
|x_i| + |y_i| ODD; for W = omega_1 ox omega_1 to be non-zero one needs this in
BOTH slots, hence (|x1|+|y1|) + (|x2|+|y2|) even, i.e. a + b even. Therefore on
supp(W), (D.2) holds and W is graded-antisymmetric in the suspended grading; off
supp(W), W = 0 and both sides of the antisymmetry vanish (0 = 0). The graded
antisymmetry of omega_2 thus holds EVERYWHERE -- vacuously off-support, via (D.2)
on-support.

Main claims checked:
  S1.  The bare sign identity (D.2) is CONDITIONAL: it holds iff a + b is even,
       and FAILS for mixed parity (1,0),(0,1). [Demonstrates the SERIOUS-1 flaw
       in the bare statement and motivates the support argument.]
  Sup1 omega_1 is odd: omega_1(x,y) != 0 => |x| + |y| odd (pairs opposite parity).
  Sup2 W vanishes off support: for every mixed-parity pair (a + b odd), W == 0.
       This is the fact that rescues the proof. [Tests the OFF-support entries
       that W2 alone never exercises -- the SERIOUS-2 fix.]
  Sup3 On supp(W) the parities satisfy a + b even (so (D.2) applies on-support).
  W1.  W is graded-SYMMETRIC under the INTERNAL grading (two c0^- => even form).
       This is exactly the DC6 obstruction: omega_1^{ot2} has the wrong symmetry
       if one forgets the suspension. [On-support claim: the symmetry type is
       defined by the nonzero entries; off-support is 0 = 0.]
  W2.  W is graded-ANTIsymmetric under the SUSPENDED grading, on ALL entries
       (vacuously off-support via Sup2, by (D.2) on-support). This is the
       resolution: with the single odd suspension of the Sigma-field, omega_2 = W
       is a genuine odd symplectic form on its support. No antisymmetrisation is
       needed.
  W3.  The brief's candidate (1/2)(W - tau* W) has the SAME symmetry class as W
       (antisym in suspended grading, sym in internal) and is non-degenerate;
       i.e. the tau-antisymmetrisation does NOT change the symmetry type. The fix
       is the grading, not the antisymmetrisation.
  W4.  omega_2 = W is non-degenerate. det(omega_1 ox omega_1) = (det omega_1)^{2n}
       with n = dim H (standard det of a tensor product), != 0.
  W5.  Cyclicity of m2 = p_{2,2,0}: with V4 a fully graded-symmetric 4-form and
       m2 defined by W(X, m2 Y) = V4(X,Y), one has W(X, m2 Y) = W(m2 X, Y), i.e.
       m2 is self-adjoint (cyclic) w.r.t. omega_2 = W. This follows from the FULL
       graded symmetry of V4 (its pair-exchange symmetry). This is CYCLICITY; it
       is NOT the (2,2,0) structure equation R6 (the Q-homotopy / Q-exactness of
       m2), which is a separate relation.
  W6.  R6 consistency: the cyclicity test uses ONLY V4 (<=> Q, l2, cobracket
       data); no p_{3,1,0} = ell_3 insertion is required or used. R6 itself (the
       (2,2,0) relation) is reused verbatim and not re-derived here.
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
# Toy graded Hilbert space H and odd symplectic form omega_1.
# Four basis states with suspended degrees [0,1,0,1] (parities [0,1,0,1]).
# omega_1 pairs (e0<->e1) and (e2<->e3) with non-zero entries a, b, made
# graded-antisymmetric for an ODD form.
# ---------------------------------------------------------------------------
DEGS = [0, 1, 0, 1]
PAR = [d % 2 for d in DEGS]
N = len(DEGS)
a, b = sp.symbols("a b", nonzero=True)

w1 = sp.zeros(N, N)


def _set_odd_pair(i: int, j: int, val: sp.Expr) -> None:
    """omega_1(e_i,e_j) = val, with the odd graded-antisymmetric partner."""
    w1[i, j] = val
    w1[j, i] = -((-1) ** (PAR[i] * PAR[j])) * val


_set_odd_pair(0, 1, a)
_set_odd_pair(2, 3, b)

# Check the toy omega_1 is odd graded-antisymmetric and non-degenerate.
_w1_antisym = all(
    sp.simplify(w1[i, j] + (-1) ** (PAR[i] * PAR[j]) * w1[j, i]) == 0
    for i in range(N)
    for j in range(N)
)
report("W0a omega_1 graded-antisymmetric (odd form)", _w1_antisym)
report("W0b omega_1 non-degenerate", sp.simplify(w1.det()) != 0, f"det={w1.det()}")


# ---------------------------------------------------------------------------
# The H^{ot2} sector: basis pairs, internal vs suspended parity, and W.
# ---------------------------------------------------------------------------
BASIS2 = [(p, q) for p in range(N) for q in range(N)]
N2 = len(BASIS2)
IDX2 = {pq: m for m, pq in enumerate(BASIS2)}


def ipar(pq: tuple[int, int]) -> int:
    """Internal (un-suspended) parity of an H^{ot2} state."""
    return (PAR[pq[0]] + PAR[pq[1]]) % 2


def spar(pq: tuple[int, int]) -> int:
    """Suspended parity: one extra odd suspension unit for the single field."""
    return (PAR[pq[0]] + PAR[pq[1]] + 1) % 2


def W_value(X: tuple[int, int], Y: tuple[int, int]) -> sp.Expr:
    """W = omega_1 ox omega_1 with the Koszul reordering sign."""
    x1, x2 = X
    y1, y2 = Y
    return (-1) ** (PAR[x2] * PAR[y1]) * w1[x1, y1] * w1[x2, y2]


def tauW_value(X: tuple[int, int], Y: tuple[int, int]) -> sp.Expr:
    """(tau* W)(X,Y) = W(tau X, tau Y), tau the graded slot-swap."""
    x1, x2 = X
    y1, y2 = Y
    s = (-1) ** (PAR[x1] * PAR[x2]) * (-1) ** (PAR[y1] * PAR[y2])
    return s * W_value((x2, x1), (y2, y1))


Wmat = sp.zeros(N2, N2)
for X in BASIS2:
    for Y in BASIS2:
        Wmat[IDX2[X], IDX2[Y]] = W_value(X, Y)


def grade_violations(matrix: sp.Matrix, parfun, kind: str) -> int:
    """Count entries violating graded (anti)symmetry w.r.t. parfun."""
    bad = 0
    for X in BASIS2:
        for Y in BASIS2:
            sign = (
                -((-1) ** (parfun(X) * parfun(Y)))
                if kind == "anti"
                else (-1) ** (parfun(X) * parfun(Y))
            )
            lhs = matrix[IDX2[X], IDX2[Y]]
            rhs = sign * matrix[IDX2[Y], IDX2[X]]
            if sp.simplify(lhs - rhs) != 0:
                bad += 1
    return bad


# ---------------------------------------------------------------------------
# S1 / Sup1-3: the conditional sign identity and the support argument that
# makes the antisymmetry conclusion sound. This is the heart of the proof.
# ---------------------------------------------------------------------------
# S1: the bare identity (D.2) is CONDITIONAL -- holds iff a + b is even.
_d2_holds = {(a_, b_): ((-1) ** (a_ * b_) == -((-1) ** ((a_ + 1) * (b_ + 1)))) for a_ in (0, 1) for b_ in (0, 1)}
_d2_iff_even = all(
    _d2_holds[(a_, b_)] == ((a_ + b_) % 2 == 0) for a_ in (0, 1) for b_ in (0, 1)
)
report(
    "S1 bare sign identity (D.2) is CONDITIONAL: holds iff a+b even, fails for (1,0),(0,1)",
    _d2_iff_even and not _d2_holds[(1, 0)] and not _d2_holds[(0, 1)],
    "demonstrates the SERIOUS-1 flaw in the bare statement",
)

# Sup1: omega_1 is odd -> nonzero only on opposite-parity pairs.
_omega1_odd_support = all(
    (w1[i, j] == 0) or ((PAR[i] + PAR[j]) % 2 == 1)
    for i in range(N)
    for j in range(N)
)
report(
    "Sup1 omega_1 odd: omega_1(x,y) != 0 => |x|+|y| odd (pairs opposite parity)",
    _omega1_odd_support,
)

# Sup2: W vanishes off support -- for EVERY mixed-parity pair (a+b odd), W == 0.
# This explicitly exercises the off-support entries that W2 never tests.
_mixed_tested = 0
_mixed_nonzero = 0
for X in BASIS2:
    for Y in BASIS2:
        if (ipar(X) + ipar(Y)) % 2 == 1:  # off support: a + b odd
            _mixed_tested += 1
            if sp.simplify(W_value(X, Y)) != 0:
                _mixed_nonzero += 1
report(
    "Sup2 W vanishes off support: every mixed-parity (a+b odd) entry has W == 0",
    _mixed_tested > 0 and _mixed_nonzero == 0,
    f"mixed-parity entries tested={_mixed_tested}, with W!=0: {_mixed_nonzero} (rescues the proof)",
)

# Sup3: on supp(W) the parities satisfy a + b even (so (D.2) applies on-support).
_support_count = 0
_support_oddab = 0
for X in BASIS2:
    for Y in BASIS2:
        if sp.simplify(W_value(X, Y)) != 0:
            _support_count += 1
            if (ipar(X) + ipar(Y)) % 2 != 0:
                _support_oddab += 1
report(
    "Sup3 on supp(W): a+b even for every nonzero entry (so D.2 applies)",
    _support_count > 0 and _support_oddab == 0,
    f"nonzero W entries={_support_count}, with a+b odd: {_support_oddab}",
)

# W1: DC6 obstruction -- on its support, W is graded-SYMMETRIC under the internal
# grading (off-support is 0 = 0, so the symmetry type is set by the nonzero
# entries). Two c0^- => even form.
report(
    "W1 omega_1^{ot2} graded-SYMMETRIC in internal grading on supp (DC6 obstruction)",
    grade_violations(Wmat, ipar, "sym") == 0
    and grade_violations(Wmat, ipar, "anti") > 0,
    "two c0^- => even form => wrong symmetry if suspension forgotten",
)

# W2: resolution -- W is graded-ANTIsymmetric under the suspended grading, on
# ALL entries (vacuously off-support via Sup2, by D.2 on-support). The 'sym>0'
# count is the on-support sector where the antisym and sym signs differ.
report(
    "W2 omega_2 = omega_1^{ot2} graded-ANTIsymmetric in suspended grading (all entries)",
    grade_violations(Wmat, spar, "anti") == 0
    and grade_violations(Wmat, spar, "sym") > 0,
    "holds everywhere: 0=0 off-support (Sup2), D.2 on-support; single suspension fixes parity",
)

# W3: the brief's candidate has the SAME symmetry class as W.
cand = sp.zeros(N2, N2)
for X in BASIS2:
    for Y in BASIS2:
        cand[IDX2[X], IDX2[Y]] = sp.Rational(1, 2) * (
            W_value(X, Y) - tauW_value(X, Y)
        )
report(
    "W3a candidate (1/2)(W - tau* W) antisym in suspended grading too",
    grade_violations(cand, spar, "anti") == 0,
)
report(
    "W3b candidate (1/2)(W - tau* W) non-degenerate (det != 0)",
    sp.simplify(cand.det()) != 0,
    f"det={sp.simplify(cand.det())}",
)

# W4: omega_2 = W non-degenerate. For a tensor product of an n x n matrix with
# itself, det(omega_1 ox omega_1) = (det omega_1)^{2n} (each factor contributes
# det^n). Here n = N = dim H, so the expected exponent is 2N.
detW = sp.simplify(Wmat.det())
det_expected = sp.simplify(w1.det() ** (2 * N))
report(
    "W4 omega_2 = omega_1^{ot2} non-degenerate, det = (det omega_1)^{2 dim H}",
    detW != 0 and sp.simplify(detW - det_expected) == 0,
    f"det={detW} = (det omega_1)^{{2*{N}}}",
)


# ---------------------------------------------------------------------------
# W5/W6: cyclicity of m2 = p_{2,2,0}.
# Build a generic FULLY graded-symmetric 4-form V4 (the closed cyclic vertex)
# by averaging a generic tensor over S_4 with positional Koszul signs. Define
# m2 by W(X, m2 Y) = V4(X,Y), i.e. m2 = W^{-1} V4 as 16x16 matrices. Cyclicity
# of m2 w.r.t. omega_2 = W is W(X, m2 Y) = W(m2 X, Y), equivalent to the
# pair-exchange symmetry of V4.
# ---------------------------------------------------------------------------
def positional_koszul(values: tuple[int, ...], perm: tuple[int, ...]) -> int:
    """Koszul sign of permuting 'values' (basis indices) by 'perm'."""
    sign = 1
    m = len(perm)
    for i in range(m):
        for j in range(i + 1, m):
            if perm[i] > perm[j] and PAR[values[perm[i]]] and PAR[values[perm[j]]]:
                sign = -sign
    return sign


_Tcoef: dict[tuple[int, ...], sp.Symbol] = {}


def _T(idx: tuple[int, ...]) -> sp.Expr:
    """Generic tensor, supported only where the total parity is even."""
    if sum(PAR[x] for x in idx) % 2 != 0:
        return sp.Integer(0)
    if idx not in _Tcoef:
        _Tcoef[idx] = sp.Symbol("t" + "".join(map(str, idx)))
    return _Tcoef[idx]


def V4(idx: tuple[int, ...]) -> sp.Expr:
    """Fully graded-symmetric 4-form: average of _T over S_4 with Koszul signs."""
    total = sp.Integer(0)
    for perm in permutations(range(4)):
        permed = tuple(idx[perm[t]] for t in range(4))
        total += positional_koszul(idx, perm) * _T(permed)
    return total


# V4 as a 16x16 matrix indexed by H^{ot2} pairs.
Vmat = sp.zeros(N2, N2)
for X in BASIS2:
    for Y in BASIS2:
        Vmat[IDX2[X], IDX2[Y]] = V4((X[0], X[1], Y[0], Y[1]))

# Verify V4 is graded-symmetric (adjacent transpositions) -- prerequisite.
_v4_sym = 0
for i in range(N):
    for j in range(N):
        for k in range(N):
            for ll in range(N):
                base = V4((i, j, k, ll))
                if sp.simplify(base - (-1) ** (PAR[i] * PAR[j]) * V4((j, i, k, ll))) != 0:
                    _v4_sym += 1
                if sp.simplify(base - (-1) ** (PAR[j] * PAR[k]) * V4((i, k, j, ll))) != 0:
                    _v4_sym += 1
                if sp.simplify(base - (-1) ** (PAR[k] * PAR[ll]) * V4((i, j, ll, k))) != 0:
                    _v4_sym += 1
report("W5a V4 fully graded-symmetric (closed cyclic vertex)", _v4_sym == 0)

# m2 = W^{-1} V4.
m2 = Wmat.inv() * Vmat

# Cyclicity: W(X, m2 Y) [matrix Wmat*m2] vs W(m2 X, Y).
WM = Wmat * m2  # entry [X,Y] = W(X, m2 Y)
M2W = sp.zeros(N2, N2)
for X in BASIS2:
    for Y in BASIS2:
        M2W[IDX2[X], IDX2[Y]] = sum(
            Wmat[IDX2[Z], IDX2[Y]] * m2[IDX2[Z], IDX2[X]] for Z in BASIS2
        )
cyc_diff = sum(1 for e in (sp.Matrix(WM) - sp.Matrix(M2W)) if sp.simplify(e) != 0)
report(
    "W5b m2 = p_{2,2,0} CYCLIC w.r.t. omega_2: W(X, m2 Y) = W(m2 X, Y)",
    cyc_diff == 0,
    f"follows from FULL graded symmetry of V4; nonzero entries={cyc_diff}",
)

# Equivalent restatement: cyclicity <=> pair-exchange symmetry of V4. This is
# CYCLICITY, distinct from the (2,2,0) structure equation R6 (Q-exactness of m2).
pair_bad = 0
for X in BASIS2:
    for Y in BASIS2:
        sgn = (-1) ** (ipar(X) * ipar(Y))
        if sp.simplify(Vmat[IDX2[X], IDX2[Y]] - sgn * Vmat[IDX2[Y], IDX2[X]]) != 0:
            pair_bad += 1
report(
    "W6 cyclicity <=> V4 pair-exchange symmetry; uses ONLY V4, no p_{3,1,0} (R6 untouched)",
    pair_bad == 0,
    "cyclicity != R6 structure eq; ell_3 not inserted, R6 reused verbatim",
)


if __name__ == "__main__":
    print("\nAll omega_2 construction self-checks PASS.")
