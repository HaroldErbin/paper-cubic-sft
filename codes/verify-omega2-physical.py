"""
Physical-grading self-checks for the two-output symplectic form omega_2.

This script settles the exchange (anti)symmetry of omega_2 = omega_1 (x) omega_1
for the closed-string auxiliary field Sigma in H^{ot2} *directly from physical
Grassmann statistics* -- no suspension-counting postulate carries the
load-bearing sign.

Physical input (Erbin 2023, Zwiebach 1993):
  - A closed-string state phi has Grassmann parity eps(phi) = N_gh(phi) mod 2.
  - c0^- is Grassmann-ODD (N_gh(c0^-) = 1).
  - Sphere ghost-number anomaly: <...> saturates at N_gh = 6. The kinetic term
    (1/2)<Psi| c0^- Q_B |Psi> has 2 + 1(c0^-) + 1(Q) + 2 = 6. Hence the form
    omega_1(A,B) = <A| c0^- |B>_bpz is non-zero only when
        N_gh(A) + N_gh(B) + 1 = 6  =>  N_gh(A) + N_gh(B) = 5  (ODD).
    So omega_1 pairs states of OPPOSITE physical parity:
        eps(A) + eps(B) = 5 mod 2 = 1.
    In particular omega_1(Psi,Psi) = 0 for the single physical field at N_gh=2
    (it pairs N_gh=2 with the N_gh=3 antifield sector) -- as a symplectic form
    must.
  - The BPZ inner product (.,.)_bpz is graded-SYMMETRIC for the states it pairs;
    moving the one odd c0^- across B and using BPZ symmetry makes omega_1
    graded-ANTIsymmetric in the PHYSICAL parity. The oddness/antisymmetry is
    carried by the SINGLE c0^- and the BPZ rule -- not by any suspension unit.

Conventions in the toy:
  - We model the closed-string Hilbert space H by a finite graded vector space,
    basis states carrying an integer ghost number N_gh; the PHYSICAL parity is
    par[i] = N_gh[i] mod 2. This is the ONLY grading the toy is built with.
    The suspension grading is introduced LATER as a derived relabelling, to test
    the dictionary -- it is not assumed to fix any sign.
  - omega_1(A,B) = (A, c0^- B)_bpz: we model it as an odd graded-antisymmetric
    non-degenerate matrix w.r.t. the PHYSICAL parity, pairing states i,j with
    N_gh[i] + N_gh[j] = D - 1 (ghost saturation with one c0^-).
  - W := omega_1 (x) omega_1 with the Koszul reordering sign in the physical
    parity:
        W(x1 ox x2, y1 ox y2) = (-1)^{par[x2]*par[y1]} omega_1(x1,y1) omega_1(x2,y2).

Checks (physical grading):
  P0   omega_1 graded-antisymmetric & non-degenerate in PHYSICAL parity.
  Sup1p omega_1 pairs only states with N_gh[i]+N_gh[j] = D-1 (saturation), hence
        a FIXED physical-parity correlation par[i]+par[j] = (D-1) mod 2.
  P1   omega_2 = W exchange sign in PHYSICAL parity: report whether it is graded
        antisymmetric  W(Y,X) = -(-1)^{eps(X)eps(Y)} W(X,Y)  on its support.
        THIS IS THE DECISIVE CHECK (DC6 verdict).
  P2   Off support W = 0 (so the conclusion is everywhere, vacuous off support).
  Dict suspended<->physical dictionary: the suspended parity |X|_s that REPRODUCES
        the physical exchange sign of P1 is |X|_s = eps(X) + 1, i.e. exactly one
        odd unit -- DERIVED from the physical computation, not postulated.
  Det  non-degeneracy det W = (det omega_1)^{2 dim H}.
  Cyc  cyclicity of m2 = p_{2,2,0} w.r.t. omega_2 from full graded symmetry of V4.
  Rob  robustness: omega_2 = W is graded-SYMMETRIC also for EVEN ghost saturation
        (N_gh sum = 4, same-parity pairing), so the verdict (b) does not hinge on
        the precise sphere anomaly value -- only on the two c0^- being even.
  n3   n=3 toy: exchange sign of omega_3 = omega_1^{ot3} in PHYSICAL parity, and
        the corresponding suspended relabelling. Reported, scope = preliminary.
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
# Toy closed-string Hilbert space H, graded by PHYSICAL ghost number N_gh.
# We pick a saturation level D so that omega_1 pairs i,j with N_gh[i]+N_gh[j]=D-1
# (one c0^- raises ghost number by 1; the BPZ form saturates at D).
# Sphere anomaly N_gh = 6; omega_1 = <.|c0^-|.> saturates at N_gh(A)+N_gh(B)=5.
# Take four states with N_gh = [2, 3, 2, 3]; physical parity = N_gh mod 2 =
# [0, 1, 0, 1]. omega_1 pairs N_gh=2 <-> N_gh=3 (sum 5): pairs (0,1) and (2,3).
# Physical parities of partners: (0,1) and (0,1) -- i.e. par[i]+par[j] = 1
# (OPPOSITE physical parity), as ghost saturation 5 (ODD) demands. This is the
# correct physical input; the form vanishes on same-parity (e.g. Psi,Psi) pairs.
# ---------------------------------------------------------------------------
NGH = [2, 3, 2, 3]
PAR = [n % 2 for n in NGH]  # physical Grassmann parity = N_gh mod 2
N = len(NGH)
D_SAT = 6  # sphere ghost anomaly; saturation N_gh[i]+N_gh[j]+1(c0^-) = 6
a, b = sp.symbols("a b", nonzero=True)

# Pairs allowed by ghost saturation N_gh[i]+N_gh[j] = D_SAT - 1 = 5.
PAIRS = [(i, j) for i in range(N) for j in range(N) if NGH[i] + NGH[j] == D_SAT - 1]

w1 = sp.zeros(N, N)


def _set_odd_pair(i: int, j: int, val: sp.Expr) -> None:
    """omega_1(e_i,e_j)=val, graded-antisym in PHYSICAL parity (odd form)."""
    w1[i, j] = val
    w1[j, i] = -((-1) ** (PAR[i] * PAR[j])) * val


_set_odd_pair(0, 1, a)  # N_gh 2 <-> 3, opposite parity (0,1)
_set_odd_pair(2, 3, b)  # N_gh 2 <-> 3, opposite parity (0,1)

# P0: omega_1 graded-antisymmetric in PHYSICAL parity, non-degenerate.
_p0_anti = all(
    sp.simplify(w1[i, j] + (-1) ** (PAR[i] * PAR[j]) * w1[j, i]) == 0
    for i in range(N)
    for j in range(N)
)
report("P0a omega_1 graded-antisymmetric in PHYSICAL parity (odd form)", _p0_anti)
report("P0b omega_1 non-degenerate", sp.simplify(w1.det()) != 0, f"det={w1.det()}")

# Sup1p: omega_1 nonzero only at ghost-saturating pairs; the physical-parity
# correlation par[i]+par[j] is FIXED = (D-1) mod 2 across the whole support.
_sat_ok = all(
    (w1[i, j] == 0) or (NGH[i] + NGH[j] == D_SAT - 1) for i in range(N) for j in range(N)
)
_corr = {(PAR[i] + PAR[j]) % 2 for i in range(N) for j in range(N) if w1[i, j] != 0}
report(
    "Sup1p omega_1 pairs only ghost-saturating states (N_gh sum fixed)",
    _sat_ok,
)
report(
    "Sup1p' physical-parity correlation par[i]+par[j] is constant on supp(omega_1)",
    len(_corr) == 1,
    f"par-sum on support = {_corr} = (D-1) mod 2 = {(D_SAT - 1) % 2}",
)
CORR = next(iter(_corr))  # the fixed physical-parity correlation c := (D-1) mod 2


# ---------------------------------------------------------------------------
# H^{ot2} sector, PHYSICAL parity, and W = omega_1 (x) omega_1.
# ---------------------------------------------------------------------------
BASIS2 = [(p, q) for p in range(N) for q in range(N)]
N2 = len(BASIS2)
IDX2 = {pq: m for m, pq in enumerate(BASIS2)}


def eps(pq: tuple[int, int]) -> int:
    """PHYSICAL Grassmann parity of an H^{ot2} state = sum of factor parities."""
    return (PAR[pq[0]] + PAR[pq[1]]) % 2


def W_value(X: tuple[int, int], Y: tuple[int, int]) -> sp.Expr:
    """W = omega_1 (x) omega_1 with Koszul reordering sign in PHYSICAL parity."""
    x1, x2 = X
    y1, y2 = Y
    return (-1) ** (PAR[x2] * PAR[y1]) * w1[x1, y1] * w1[x2, y2]


Wmat = sp.zeros(N2, N2)
for X in BASIS2:
    for Y in BASIS2:
        Wmat[IDX2[X], IDX2[Y]] = W_value(X, Y)


def grade_violations(matrix: sp.Matrix, parfun, kind: str) -> int:
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


# P1 (DECISIVE): exchange sign of omega_2 = W in the PHYSICAL parity eps.
anti_phys = grade_violations(Wmat, eps, "anti")
sym_phys = grade_violations(Wmat, eps, "sym")
report(
    "P1 DECISIVE: omega_2 = W graded-SYMMETRIC in PHYSICAL parity (sym viol=0)",
    sym_phys == 0,
    f"physical-parity: anti-viol={anti_phys}, sym-viol={sym_phys}",
)

# P2: off support (ghost non-saturating in either slot) W = 0.
_off = 0
_off_nz = 0
for X in BASIS2:
    for Y in BASIS2:
        sat = (NGH[X[0]] + NGH[Y[0]] == D_SAT - 1) and (
            NGH[X[1]] + NGH[Y[1]] == D_SAT - 1
        )
        if not sat:
            _off += 1
            if sp.simplify(W_value(X, Y)) != 0:
                _off_nz += 1
report(
    "P2 W vanishes off support (non-saturating slot => 0)",
    _off > 0 and _off_nz == 0,
    f"off-support entries={_off}, nonzero={_off_nz}",
)


# ---------------------------------------------------------------------------
# Dict: suspended<->physical dictionary. The suspended parity that REPRODUCES
# an antisymmetric exchange sign is |X|_s = eps(X) + c_s (c_s in {0,1}). c_s is
# fixed only CONDITIONALLY: *if* one demands a graded-antisymmetric (odd
# symplectic / BV) presentation, then c_s = 1 is forced. This is the choice of
# the BV presentation, NOT a derived worldsheet fact about Sigma (whose physical
# pairing is graded SYMMETRIC, P1). It matches Munster-Sachs' "antisymmetry from
# the degree shift" (WBEIHWFU review l.305).
# ---------------------------------------------------------------------------
def susp_par(c_s: int):
    return lambda pq: (eps(pq) + c_s) % 2


_cs_anti = {}
for c_s in (0, 1):
    _cs_anti[c_s] = grade_violations(Wmat, susp_par(c_s), "anti")
# Pick the shift that makes W antisymmetric.
_cs_pick = [c for c in (0, 1) if _cs_anti[c] == 0]
report(
    "Dict BV-presentation shift: demanding antisym forces c_s=1 (one odd unit)",
    _cs_pick == [1],
    f"anti-viol by shift: {_cs_anti}; antisym (odd-symplectic presentation) "
    f"requires c_s = {_cs_pick} => one odd suspension unit -- a presentation "
    f"CHOICE, not a fact about Sigma (physical pairing is SYMMETRIC, P1)",
)

# Det: non-degeneracy with exponent 2 dim H.
detW = sp.simplify(Wmat.det())
det_expected = sp.simplify(w1.det() ** (2 * N))
report(
    "Det omega_2 non-degenerate, det = (det omega_1)^{2 dim H}",
    detW != 0 and sp.simplify(detW - det_expected) == 0,
    f"det={detW}",
)


# ---------------------------------------------------------------------------
# Cyc: cyclicity of m2 = p_{2,2,0} from full graded symmetry of V4 (PHYSICAL).
# ---------------------------------------------------------------------------
def positional_koszul(values: tuple[int, ...], perm: tuple[int, ...]) -> int:
    sign = 1
    m = len(perm)
    for i in range(m):
        for j in range(i + 1, m):
            if perm[i] > perm[j] and PAR[values[perm[i]]] and PAR[values[perm[j]]]:
                sign = -sign
    return sign


_Tc: dict[tuple[int, ...], sp.Symbol] = {}


def _T(idx: tuple[int, ...]) -> sp.Expr:
    # V4 nonzero only at ghost saturation: sum N_gh = 2(D-1) = 8 (two c0^- in W).
    if sum(NGH[x] for x in idx) != 2 * (D_SAT - 1):
        return sp.Integer(0)
    if idx not in _Tc:
        _Tc[idx] = sp.Symbol("t" + "".join(map(str, idx)))
    return _Tc[idx]


def V4(idx: tuple[int, ...]) -> sp.Expr:
    total = sp.Integer(0)
    for perm in permutations(range(4)):
        permed = tuple(idx[perm[t]] for t in range(4))
        total += positional_koszul(idx, perm) * _T(permed)
    return total


Vmat = sp.zeros(N2, N2)
for X in BASIS2:
    for Y in BASIS2:
        Vmat[IDX2[X], IDX2[Y]] = V4((X[0], X[1], Y[0], Y[1]))

_v4_sym = 0
for i in range(N):
    for j in range(N):
        for k in range(N):
            for ll in range(N):
                base = V4((i, j, k, ll))
                if sp.simplify(base - (-1) ** (PAR[i] * PAR[j]) * V4((j, i, k, ll))) != 0:
                    _v4_sym += 1
report("Cyc-a V4 fully graded-symmetric (closed cyclic vertex, physical)", _v4_sym == 0)

m2 = Wmat.inv() * Vmat
WM = Wmat * m2
M2W = sp.zeros(N2, N2)
for X in BASIS2:
    for Y in BASIS2:
        M2W[IDX2[X], IDX2[Y]] = sum(
            Wmat[IDX2[Z], IDX2[Y]] * m2[IDX2[Z], IDX2[X]] for Z in BASIS2
        )
cyc_diff = sum(1 for e in (sp.Matrix(WM) - sp.Matrix(M2W)) if sp.simplify(e) != 0)
report(
    "Cyc-b m2 = p_{2,2,0} CYCLIC w.r.t. omega_2: W(X,m2 Y)=W(m2 X,Y)",
    cyc_diff == 0,
    f"from full graded symmetry of V4; uses only V4 (no ell_3 insertion)",
)


# ---------------------------------------------------------------------------
# Rob: robustness of the SYMMETRIC verdict to the saturation parity.
# Build a SECOND toy with EVEN saturation (N_gh sum = 4, D'=5): omega_1 then
# pairs SAME-parity states. The physical exchange of omega_2 = W must STILL be
# graded-symmetric -- i.e. P1's verdict does not hinge on the precise sphere
# anomaly value (6 / odd-sum 5), only on the TWO c0^- being even-as-operation.
# ---------------------------------------------------------------------------
NGH_E = [1, 3, 0, 2]  # parity [1,1,0,0]; even-sum pairs: (0,1) sum 4, (2,3) sum 2
PAR_E = [n % 2 for n in NGH_E]
wE = sp.zeros(N, N)
wE[0, 1] = a
wE[1, 0] = -((-1) ** (PAR_E[0] * PAR_E[1])) * a  # both odd -> same parity (1,1)
wE[2, 3] = b
wE[3, 2] = -((-1) ** (PAR_E[2] * PAR_E[3])) * b  # both even -> same parity (0,0)


def epsE(pq: tuple[int, int]) -> int:
    return (PAR_E[pq[0]] + PAR_E[pq[1]]) % 2


WmatE = sp.zeros(N2, N2)
for X in BASIS2:
    for Y in BASIS2:
        x1, x2 = X
        y1, y2 = Y
        WmatE[IDX2[X], IDX2[Y]] = (
            (-1) ** (PAR_E[x2] * PAR_E[y1]) * wE[x1, y1] * wE[x2, y2]
        )

_rob_sym = sum(
    1
    for X in BASIS2
    for Y in BASIS2
    if sp.simplify(
        WmatE[IDX2[X], IDX2[Y]]
        - (-1) ** (epsE(X) * epsE(Y)) * WmatE[IDX2[Y], IDX2[X]]
    )
    != 0
)
report(
    "Rob omega_2 graded-SYMMETRIC also for EVEN saturation (same-parity pairing)",
    _rob_sym == 0,
    "verdict (b) robust to the saturation parity; only the two c0^- being even matters",
)


# ---------------------------------------------------------------------------
# n3 toy (PRELIMINARY): omega_3 = omega_1^{ot3} on H^{ot3}, physical parity.
# Report exchange symmetry type and the suspended shift that makes it antisym.
# ---------------------------------------------------------------------------
BASIS3 = [(p, q, r) for p in range(N) for q in range(N) for r in range(N)]
N3 = len(BASIS3)
IDX3 = {pqr: m for m, pqr in enumerate(BASIS3)}


def eps3(t: tuple[int, int, int]) -> int:
    return (PAR[t[0]] + PAR[t[1]] + PAR[t[2]]) % 2


def W3_value(X, Y) -> sp.Expr:
    # omega_1^{ot3} with the Koszul sign for reordering (x2,x3) past (y1,y2):
    # standard tensor product of three forms.
    x1, x2, x3 = X
    y1, y2, y3 = Y
    s = (-1) ** (
        PAR[x2] * PAR[y1]
        + PAR[x3] * PAR[y1]
        + PAR[x3] * PAR[y2]
    )
    return s * w1[x1, y1] * w1[x2, y2] * w1[x3, y3]


W3 = sp.zeros(N3, N3)
for X in BASIS3:
    for Y in BASIS3:
        W3[IDX3[X], IDX3[Y]] = W3_value(X, Y)


def grade_viol3(matrix, parfun, kind: str) -> int:
    bad = 0
    for X in BASIS3:
        for Y in BASIS3:
            sign = (
                -((-1) ** (parfun(X) * parfun(Y)))
                if kind == "anti"
                else (-1) ** (parfun(X) * parfun(Y))
            )
            if sp.simplify(matrix[IDX3[X], IDX3[Y]] - sign * matrix[IDX3[Y], IDX3[X]]) != 0:
                bad += 1
    return bad


_n3_sym = grade_viol3(W3, eps3, "sym")
_n3_anti = grade_viol3(W3, eps3, "anti")
# suspended shift that makes omega_3 antisym:
_n3_cs = {}
for c_s in (0, 1):
    _n3_cs[c_s] = grade_viol3(W3, lambda t, c=c_s: (eps3(t) + c) % 2, "anti")
report(
    "n3 (PRELIMINARY) omega_3 = omega_1^{ot3} physical exchange type + suspended shift",
    True,  # informational; verdict reported, not gated
    f"physical: sym-viol={_n3_sym}, anti-viol={_n3_anti}; "
    f"suspended anti-viol by shift {_n3_cs} "
    f"=> antisym needs c_s={[c for c in (0, 1) if _n3_cs[c] == 0]}",
)


if __name__ == "__main__":
    print("\nAll physical-grading omega_2 self-checks PASS.")
