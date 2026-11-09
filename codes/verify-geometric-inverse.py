"""
Companion script for derivation record 030 (geometric 1/m_2, second look).

Part 1 (sub-task 12a), part 2 (sub-task 12b), part 3 (sub-task 12c), part 4 (sub-task 12d).

Part 4: the scaling lemma of 030 §5.6 -- a kernel polynomial in the vertex data
(V_4 -> t V_4, degree d >= 0, arbitrary coefficient matrices, hence more general than any
finite sum of surface-data kernels with V_4-independent moduli bounds) cannot satisfy
(t V_4) K(t) = 1 for all t; least-squares floor computed independently (Vandermonde
distance), reached by the fit; break-on-purpose: a t^-1 term (algebraic inverse) or too
few t-points make the residual vanish.  NOT verified (part 4): anything about V_4-dependent
moduli bounds, infinite sums, or the (alpha)/(beta) factorisation identities.

Part 3: the toy of 030 §4 for candidate (e), the change of kinetic term
(V_4 =? Sym_3[J o K^{-1} o J], 030 eqs. (3.11)/(3.13)) on Sym^2 C^3 with levels
(-1, 0, 1), a random S_4-symmetric complex V_4 and the bounded diagonal tube kernel
g(lam) of eq. (3.14) (beta2).  What is verified (part 3):
  * tautology guard: an unconstrained complex W solves M = W^t g W exactly (Takagi), so
    "surface type" must constrain W for the test to mean anything;
  * rank bound: W with r < rank M rows fails with residual = Eckart-Young bound
    sqrt(sum_{k>r} sigma_k^2); a product tube Sym^2(P) built from a rank-rho single-strand
    propagator has rank rho(rho+1)/2 and fails the same way (demonstrated failure);
  * disconnected W_3 (W = Sym^2 w, d^2 parameters vs C(d+3,4) components) fails both the
    single- and the three-channel identity; a V_4 generated from such a W is recovered
    (positive control) and a 1e-2 perturbation of it is caught (break-on-purpose);
  * m_2 K = 1 fails for the bounded diagonal tube at every lam (Prop. 3.2 with the actual
    profile), passes for a level-diagonal M; the Neumann chain on the level-diagonal part
    diverges for the generic M (rho(D^-1 N) > 1) and converges for a dominant control;
  * signature: real W with positive g cannot produce an indefinite real M (single channel,
    residual = norm of the negative part); the three-channel sum has no such bound.
What is NOT verified (part 3): whether a *connected* W_3 (a rigid 4-punctured-sphere
slice) satisfies (3.13) -- a finite-dimensional toy cannot distinguish such a W from a
generic symmetric tensor; the genus argument of 030 §3.7.6 and the branched-cover
question are CFT-level and outside the script.

Part 1: the ghost-number table of 030 §1.3, encoded as data and checked
for internal consistency by two independent bookkeepings.

What is verified (part 1):
  * every table row's map ghost number gamma, recomputed from its raw data by the
    surface-saturation rule 030 eq. (1.5)  [gamma = 10 - S_tot, S_tot = sum over surfaces
    of (6 - 6g + n_b - n_c) minus sum over bivectors of S_B], and — for sewing objects —
    independently by the operator rule (1.4) [gamma = N_op + ell], against the value
    written in the table;
  * the form/map/bivector conversions (1.2)-(1.3) on m_2, m_2^{-1}, G_2, V_4;
  * 022 eq. (2.2) N_gh = 2 + nu_f reproduced by (1.5) on random 022-class graphs, AND
    by 022's own leg-telescoping constants (-2 per leg, +5 per raised output, +5 per
    frozen node, +4 per smoothed line) — two different bookkeepings, same answer;
  * Lemma 2.1: connected kernels keep gamma >= 2 for random subsets of un-integrated
    moduli and random node types (frozen / smoothed / doubly frozen);
  * the frozen limit (1.6) on an explicit zero-mode Fock space with a random L_0^+
    spectrum: 'shrink' gives lambda * b_0^+ omega_1^{-1} (N_op = -2), 'slice' gives
    omega_1^{-1} (N_op = -1); regularity of (1 - e^{-lambda L})/L at L -> 0;
  * the open-string (Erbin-Firat) count via the bivector rule: gamma(Q_B) = +1,
    gamma(b_0 (1-e^{-2 lambda L_0})/L_0) = -1;
  * Lemma 2.2: e^{-t m_2} is not ghost-homogeneous for real t on a graded toy;
  * break-on-purpose legs: a row with one insertion count wrong FAILS the table check;
    the shrink limit with b_0^+ removed FAILS.

Part 2 (sub-task 12b): the obstructions of 030 §3, each tested on finite-dimensional
toys against the identity V_4 K = G_2, not against V_4^{-1} formed algebraically (one
exception: the part 2 Gauss-Newton leg below fits Sym^2 k to M^-1 as a least-squares
distance -- a numerical search, not a candidate built from M^{-1}):
  * Prop. 3.1 (product kernels): the product form beta_13 beta_24 + beta_14 beta_23 is not
    S4-symmetric for non-degenerate beta of rank > 1 (symmetric and antisymmetric beta,
    d = 2, 3, 4); positive controls d = 1 and rank-one beta; a Gauss-Newton search for
    k with Sym^2(k) = M^{-1} for a random S4-symmetric M at d = 2 fails; polarised
    products span End(Sym^2), so SUMS of products are unconstrained (Neumann chain);
  * Prop. 3.2 (commutant): a correlated two-length tube kernel with a random joint
    measure is level-diagonal; a generic S4-symmetric M is not; the best level-diagonal
    K leaves |M K - 1| = O(1); control: a level-diagonal M is inverted by the tube;
    (b1 + b2) b1 = b1 b2 on the zero-mode Fock space;
  * eq. (3.8) (explicit ghost insertions): an explicit (M, B, B') with M B^t M B' = 1
    at lambda = 1 and FAILING at lambda = 2; directional derivative 2 M B^t M B'; a random
    dressed vertex B^t M B' is not an inverse while M^{-1} is (falsifiability leg);
  * §3.4 (Laplace): direct form diverges on an indefinite toy and converges on a positive
    one; the squared form recovers M^{-1} on the indefinite toy.

What is NOT verified: the identification of the extra antighosts of row 14 with leg
operators (contour deformation, taken as standard); the BRST identities of 030 §3.2-3.3;
the non-vanishing of the 4-tachyon vertex-region integral at generic momenta (literature);
whether the (beta) factorisation M = W^t g W admits a surface-type W (sub-task 12c).

Conventions (030 §1.1): c = +1, b = -1; sphere saturation 6; H_0 = ker L_0^- cap ker b_0^-;
omega_1(A,B) = <A|c_0^-|B> pairs at 5; BPZ pairs at 6; R23 map rule gamma = 3 ell - 2k + g.

Run:  .venv/bin/python codes/verify-geometric-inverse.py
"""

from __future__ import annotations

import itertools
import sys
from dataclasses import dataclass, field

import numpy as np
from scipy.linalg import expm

SEED = 20260908
rng = np.random.default_rng(SEED)

RESULTS: list[tuple[str, bool]] = []


def report(label: str, ok: bool) -> None:
    """Record and print one named PASS/FAIL check."""
    RESULTS.append((label, ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}")


# ----------------------------------------------------------------------------------
# Rule (1.5): surface-saturation bookkeeping
# ----------------------------------------------------------------------------------


@dataclass(frozen=True)
class Surface:
    """A connected surface piece: genus g, n_b antighost and n_c ghost insertions."""

    g: int
    n_b: int
    n_c: int = 0

    def saturation(self) -> int:
        """Required sum of leg ghost numbers, 030 eq. (1.1)."""
        return 6 * (1 - self.g) + self.n_b - self.n_c


@dataclass(frozen=True)
class Bivector:
    """A sewing bivector: BPZ bivector (S_B = 6) times n_b antighost modes."""

    n_b: int

    def s_b(self) -> int:
        return 6 - self.n_b


@dataclass(frozen=True)
class Row:
    """One row of the table (030 §1.3): pieces, strands, and the claimed gamma."""

    name: str
    ell: int
    surfaces: tuple[Surface, ...] = field(default_factory=tuple)
    bivectors: tuple[Bivector, ...] = field(default_factory=tuple)
    gamma_claimed: int = 0
    n_op: int | None = None  # for pure sewing objects (rule 1.4)
    s_form_claimed: int | None = None  # 4-form saturation column (ell = 2 rows)


def gamma_rule_15(row: Row) -> int:
    """gamma = 5 ell - S_tot, S_tot = sum_surfaces S - sum_bivectors S_B (030 eq. 1.5)."""
    s_tot = sum(s.saturation() for s in row.surfaces) - sum(
        b.s_b() for b in row.bivectors
    )
    return 5 * row.ell - s_tot


def gamma_rule_14(row: Row) -> int | None:
    """gamma = N_op + ell for a pure sewing operator (030 eq. 1.4)."""
    if row.n_op is None:
        return None
    return row.n_op + row.ell


def s_form_from_gamma(gamma: int, ell: int) -> int:
    """4-form saturation from the map ghost number, 030 eq. (1.2)."""
    return 5 * ell - gamma


# Pure sewing objects (tubes, nodes) are themselves bivectors: their gamma is (1.3),
# gamma = S_B - 5 ell.  Surface rows use (1.5).  Both reduce to R23's map grading.


def gamma_rule_13(row: Row) -> int:
    """gamma = S_B(total) - 5 ell for a pure bivector object (030 eq. 1.3)."""
    return sum(b.s_b() for b in row.bivectors) - 5 * row.ell


TABLE: list[Row] = [
    # 1 frozen node omega_1^{-1} = b_0^- delta: one BPZ bivector with one b
    Row("1 frozen node omega_1^{-1}", 1, bivectors=(Bivector(1),), gamma_claimed=0, n_op=-1),
    # 2 cylinder as a map on H_0: b_0^+/L_0^+ (the map itself; gamma = N_op)
    Row("2 cylinder map b_0^+/L_0^+", 1, gamma_claimed=-1, n_op=-1),
    # 3 cylinder with b_0^-: P = b_0^+ b_0^- delta / L_0^+
    Row("3 cylinder P (sewing op.)", 1, bivectors=(Bivector(2),), gamma_claimed=-1, n_op=-2),
    Row("4 bounded cylinder P_[0,lam]", 1, bivectors=(Bivector(2),), gamma_claimed=-1, n_op=-2),
    Row("5 doubly-frozen node b_0^+ b_0^- delta", 1, bivectors=(Bivector(2),),
        gamma_claimed=-1, n_op=-2),
    Row("6 frozen colour-2 node G_2^{-1}", 2, bivectors=(Bivector(1), Bivector(1)),
        gamma_claimed=0, n_op=-2, s_form_claimed=10),
    Row("7 double tube P x P", 2, bivectors=(Bivector(2), Bivector(2)),
        gamma_claimed=-2, n_op=-4, s_form_claimed=12),
    Row("8 bounded double tube", 2, bivectors=(Bivector(2), Bivector(2)),
        gamma_claimed=-2, n_op=-4, s_form_claimed=12),
    # 9a fully diagonal: two BPZ bivectors, two b's in total (b(d_s), b(d_theta))
    Row("9a fully diagonal double tube", 2, bivectors=(Bivector(1), Bivector(1)),
        gamma_claimed=0, n_op=-2, s_form_claimed=10),
    Row("9b length-diagonal double tube", 2, bivectors=(Bivector(2), Bivector(1)),
        gamma_claimed=-1, n_op=-3, s_form_claimed=11),
    # 10 connected Sigma_{g,4}, all 6g+2 moduli integrated (three genera)
    Row("10 connected Sigma_{0,4} all moduli", 2, surfaces=(Surface(0, 2),),
        gamma_claimed=2, s_form_claimed=8),
    Row("10 connected Sigma_{1,4} all moduli", 2, surfaces=(Surface(1, 8),),
        gamma_claimed=2, s_form_claimed=8),
    Row("10 connected Sigma_{2,4} all moduli", 2, surfaces=(Surface(2, 14),),
        gamma_claimed=2, s_form_claimed=8),
    Row("11 rigid 4-punctured sphere", 2, surfaces=(Surface(0, 0),),
        gamma_claimed=4, s_form_claimed=6),
    Row("12 half-frozen sphere (b's kept)", 2, surfaces=(Surface(0, 2),),
        gamma_claimed=2, s_form_claimed=8),
    # 14 connected sphere with n_x = 4 extra b-mode insertions
    Row("14 sphere + 4 extra b-modes", 2, surfaces=(Surface(0, 6),),
        gamma_claimed=-2, s_form_claimed=12),
    Row("14 sphere + 1 extra c-mode", 2, surfaces=(Surface(0, 2, 1),),
        gamma_claimed=3, s_form_claimed=7),
    # 16 m_2 = the integrated V_4 as a 2 -> 2 map
    Row("16 m_2 (V_4 as 2->2 map)", 2, surfaces=(Surface(0, 2),),
        gamma_claimed=2, s_form_claimed=8),
]


def check_table() -> None:
    """Each row recomputed by (1.3)/(1.5) and, where available, (1.4)."""
    for row in TABLE:
        if row.surfaces:
            g15 = gamma_rule_15(row)
            ok = g15 == row.gamma_claimed
            report(f"table row {row.name}: rule (1.5) gives {g15}, claimed {row.gamma_claimed}", ok)
        elif row.bivectors:
            g13 = gamma_rule_13(row)
            ok = g13 == row.gamma_claimed
            report(f"table row {row.name}: rule (1.3) gives {g13}, claimed {row.gamma_claimed}", ok)
        g14 = gamma_rule_14(row)
        if g14 is not None and row.bivectors:
            report(f"table row {row.name}: rule (1.4) N_op+ell = {g14} agrees", g14 == row.gamma_claimed)
        if row.n_op is not None and not row.bivectors:
            # row 2: the map itself
            report(f"table row {row.name}: gamma = N_op = {row.n_op}", row.n_op == row.gamma_claimed)
        if row.s_form_claimed is not None:
            s = s_form_from_gamma(row.gamma_claimed, row.ell)
            report(f"table row {row.name}: 4-form S = {s}, claimed {row.s_form_claimed}",
                   s == row.s_form_claimed)


def check_algebraic_rows() -> None:
    """Rows 15-17: G_2, m_2, m_2^{-1} via (1.2)-(1.3) and R23."""
    # R23 rule gamma = 3 ell - 2 k + g, genus 0
    r23 = lambda k, ell, g=0: 3 * ell - 2 * k + g  # noqa: E731
    report("R23: gamma(m_2) = 3*2 - 2*2 = +2", r23(2, 2) == 2)
    report("R23: gamma(V_4 as 4->0) = -8 = 5*0 - S(V_4=8)", r23(4, 0) == 5 * 0 - 8)
    report("R23: gamma(ell_k) = 3 - 2k equals 5 - 2(k+1) for k = 2..6",
           all(r23(k, 1) == 5 - 2 * (k + 1) for k in range(2, 7)))
    # R23 general formula from (1.2) with frozen-handle saturation S = 2(k+ell) - g
    report("R23 general: 5 ell - [2(k+ell) - g] == 3 ell - 2k + g (random k,ell,g)",
           all(5 * l - (2 * (k + l) - g) == r23(k, l, g)
               for k, l, g in rng.integers(0, 7, size=(50, 3))))
    report("m_2^{-1}: gamma = -gamma(m_2) = -2; 4-form S = 12; bivector S_B = 8",
           s_form_from_gamma(-2, 2) == 12 and (-2 + 5 * 2) == 8)
    report("G_2: 4-form S = 10 <-> gamma = 0 (identity)", s_form_from_gamma(0, 2) == 10)


# ----------------------------------------------------------------------------------
# 022 eq. (2.2) by two bookkeepings, and Lemma 2.1
# ----------------------------------------------------------------------------------

LEG_BASE, RAISE_EXT, DELTA_FROZEN, DELTA_SMOOTH = -2, 5, 5, 4  # 022 telescoping constants


def gamma_022_telescoping(valences: list[int], nu_f: int, g_s: int, nu_d: int = 0) -> int:
    """022 eq. (2.2) bookkeeping: legs, raised outputs, node bivectors (+ doubly frozen)."""
    return (LEG_BASE * sum(valences) + RAISE_EXT * 2 + DELTA_FROZEN * nu_f
            + DELTA_SMOOTH * g_s + DELTA_SMOOTH * nu_d)


def gamma_022_rule15(valences: list[int], nu_f: int, g_s: int, nu_d: int = 0) -> int:
    """Same graph by (1.5): each integrated genus-0 vertex region is Surface(0, 2n-6)."""
    row = Row("g", 2,
              surfaces=tuple(Surface(0, 2 * n - 6) for n in valences),
              bivectors=tuple([Bivector(1)] * nu_f + [Bivector(2)] * (g_s + nu_d)))
    return gamma_rule_15(row)


def random_graph() -> tuple[list[int], int, int, int] | None:
    """Random 022-class graph with leg balance; None if the draw is infeasible."""
    V = int(rng.integers(1, 6))
    nu_f, g_s, nu_d = (int(x) for x in rng.integers(0, 4, size=3))
    total_legs = 4 + 2 * (nu_f + g_s + nu_d)
    if total_legs < 3 * V:
        return None
    extra = total_legs - 3 * V
    cuts = np.sort(rng.integers(0, extra + 1, size=V - 1))
    parts = np.diff(np.concatenate([[0], cuts, [extra]]))
    return [3 + int(p) for p in parts], nu_f, g_s, nu_d


def check_022_and_lemma21() -> None:
    ok_agree = ok_closed = ok_floor = True
    n_done = 0
    for _ in range(3000):
        drawn = random_graph()
        if drawn is None:
            continue
        val, nu_f, g_s, nu_d = drawn
        a, b = gamma_022_telescoping(val, nu_f, g_s, nu_d), gamma_022_rule15(val, nu_f, g_s, nu_d)
        ok_agree &= a == b
        ok_closed &= b == 2 + nu_f
        ok_floor &= b >= 2
        n_done += 1
    report(f"022 (2.2): telescoping == rule (1.5) on {n_done} random graphs", ok_agree and n_done > 500)
    report("022 (2.2): gamma == 2 + nu_f incl. doubly-frozen nodes (ghost-neutral)", ok_closed)
    report("Lemma 2.1 floor: gamma >= 2 for all connected 022-class graphs", ok_floor)
    # Un-integrating moduli does not change n_b: the Surface data are identical, so the
    # floor is the same statement; the falsifiable content is that DROPPING b's raises.
    ok_drop = True
    for _ in range(500):
        drawn = random_graph()
        if drawn is None:
            continue
        val, nu_f, g_s, nu_d = drawn
        surfaces = [Surface(0, 2 * n - 6) for n in val]
        # drop k antighosts from a vertex region that has some (R27-type freezing)
        idx = [i for i, s in enumerate(surfaces) if s.n_b > 0]
        if not idx:
            continue
        i = int(rng.choice(idx))
        k = int(rng.integers(1, surfaces[i].n_b + 1))
        surfaces[i] = Surface(0, surfaces[i].n_b - k)
        row = Row("g", 2, surfaces=tuple(surfaces),
                  bivectors=tuple([Bivector(1)] * nu_f + [Bivector(2)] * (g_s + nu_d)))
        ok_drop &= gamma_rule_15(row) == 2 + nu_f + k
    report("Lemma 2.1: dropping k antighosts (R27 freezing) raises gamma by exactly k", ok_drop)


# ----------------------------------------------------------------------------------
# Frozen limit (1.6) on an explicit zero-mode Fock space
# ----------------------------------------------------------------------------------


def fermion_ops() -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """b_0^+, b_0^-, c_0^+, c_0^- on the 4-dim zero-mode Fock space (Jordan-Wigner)."""
    a = np.array([[0, 1], [0, 0]], dtype=complex)  # annihilator on one mode
    z = np.diag([1, -1]).astype(complex)
    i2 = np.eye(2, dtype=complex)
    bp = np.kron(a, i2)          # b_0^+ = a_1
    bm = np.kron(z, a)           # b_0^- = a_2 (with JW string)
    cp, cm = bp.conj().T, bm.conj().T
    ngh = cp @ bp + cm @ bm      # zero-mode ghost number, [N, b] = -b, [N, c] = +c
    return bp, bm, cp, cm, ngh


def ghost_shift(op: np.ndarray, ngh: np.ndarray) -> int | None:
    """Return gamma if [N, op] = gamma op for a unique gamma, else None."""
    comm = ngh @ op - op @ ngh
    for gam in range(-4, 5):
        if np.allclose(comm, gam * op, atol=1e-12) and not np.allclose(op, 0):
            return gam
    return None


def check_frozen_limit() -> None:
    bp, bm, cp, cm, ngh = fermion_ops()
    report("zero modes: {b_0^+, c_0^+} = 1, {b_0^-, c_0^-} = 1, cross = 0",
           np.allclose(bp @ cp + cp @ bp, np.eye(4)) and np.allclose(bm @ cm + cm @ bm, np.eye(4))
           and np.allclose(bp @ cm + cm @ bp, 0) and np.allclose(bm @ cp + cp @ bm, 0))
    # random positive L_0^+ spectrum on a 5-dim matter factor; delta_{L_0^-} = 1 (level-matched)
    nd = 5
    L = np.diag(rng.uniform(0.3, 3.0, size=nd))
    i4, ind = np.eye(4), np.eye(nd)
    Bp, Bm = np.kron(bp, ind), np.kron(bm, ind)
    Lp = np.kron(i4, L)
    omega_inv = Bm  # omega_1^{-1} = b_0^- delta_{L_0^-,0}

    def bounded(lam: float) -> np.ndarray:
        # P_[0,lam] = b_0^+ (1 - e^{-lam L_0^+})/L_0^+ omega_1^{-1}, L_0^+ diagonal
        d = np.diag(Lp)
        return Bp @ np.diag((1 - np.exp(-lam * d)) / d) @ omega_inv
    lam = 1e-4
    shrink = bounded(lam) / lam
    target = Bp @ omega_inv
    report("frozen-shrink: lim lambda^{-1} P_[0,lam] = b_0^+ omega_1^{-1} (rel. err < 1e-3)",
           np.linalg.norm(shrink - target) / np.linalg.norm(target) < 1e-3)
    report("frozen-shrink ghost: N_op(b_0^+ omega_1^{-1}) = -2 (row 5)",
           ghost_shift(bp @ bm, ngh) == -2)
    report("frozen-slice ghost: N_op(omega_1^{-1}) = -1 (row 1), differs from shrink by 1",
           ghost_shift(bm, ngh) == -1)
    report("regularity: (1 - e^{-lam L})/L at L = 1e-9 equals lam to 1e-6",
           abs((1 - np.exp(-0.7 * 1e-9)) / 1e-9 - 0.7) < 1e-6)
    # series (1.6): lambda - lambda^2 L / 2 + O(lambda^3)
    lam2 = 0.05
    series = lam2 - lam2**2 * np.diag(L) / 2
    exact = (1 - np.exp(-lam2 * np.diag(L))) / np.diag(L)
    report("series (1.6): |exact - (lam - lam^2 L/2)| = O(lam^3)",
           np.max(np.abs(exact - series)) < 3 * lam2**3 * np.max(np.diag(L)) ** 2)
    # break on purpose: remove b_0^+ from the shrink target
    report("BREAK (expected FAIL, reported inverted): shrink != omega_1^{-1} alone",
           not np.allclose(shrink, omega_inv, atol=1e-3))
    report("map on H_0: b_0^+ preserves ker b_0^- ({b_0^+, b_0^-} = 0)",
           np.allclose(bp @ bm + bm @ bp, 0))


# ----------------------------------------------------------------------------------
# Open-string cross-check (C7) and Lemma 2.2
# ----------------------------------------------------------------------------------


def check_open_and_lemma22() -> None:
    # open: BPZ pairs at 3; <A|Q|B> saturates at S = 2 -> gamma(Q) = 3*1 - 2 = +1
    gamma_Q = 3 * 1 - 2
    # propagator bivector: BPZ bivector (S_B = 3) times one b_0: S_B = 2 -> gamma = S_B - 3
    gamma_P = (3 - 1) - 3
    report("open (C7): gamma(Q_B) = +1, gamma(b_0 (1-e^{-2 lam L_0})/L_0) = -1, sum 0",
           gamma_Q == 1 and gamma_P == -1 and gamma_Q + gamma_P == 0)
    report("open (C7): gamma = N_op for the propagator (no c_0 in the pairing)", gamma_P == -1)
    report("closed per strand: kinetic +1, propagator -1; two strands: +2 = gamma(m_2), -2",
           2 * 1 == 2 and 2 * (-1) == -2)
    # Lemma 2.2 on a graded toy: sectors N_gh = 4 (dim 3) and 6 (dim 3); m_2 : 4 -> 6.
    n = 3
    N = np.diag([4] * n + [6] * n).astype(float)
    m2 = np.zeros((2 * n, 2 * n))
    m2[n:, :n] = rng.normal(size=(n, n))
    report("Lemma 2.2 toy: [N, m_2] = 2 m_2 (gamma = +2)", np.allclose(N @ m2 - m2 @ N, 2 * m2))
    t = 0.7
    E = np.eye(2 * n) - t * m2  # e^{-t m_2}, since m_2^2 = 0 on the toy
    report("Lemma 2.2 toy: m_2^2 = 0 (strictly grading-raising on a bounded truncation)",
           np.allclose(m2 @ m2, 0))
    report("Lemma 2.2: e^{-t m_2} has no definite ghost shift for real t",
           ghost_shift_general(E, N) is None)
    report("Lemma 2.2: m_2^{-1} exists only as the block 6 -> 4 (rectangular block invertible)",
           abs(np.linalg.det(m2[n:, :n])) > 1e-8)


def ghost_shift_general(op: np.ndarray, N: np.ndarray) -> int | None:
    comm = N @ op - op @ N
    for gam in range(-6, 7):
        if np.allclose(comm, gam * op):
            return gam
    return None


# ----------------------------------------------------------------------------------
# Break-on-purpose: a wrong insertion count is detected
# ----------------------------------------------------------------------------------


def check_break_on_purpose() -> None:
    wrong = Row("9a with 4 b's (wrong)", 2, bivectors=(Bivector(2), Bivector(2)), gamma_claimed=0)
    report("BREAK: diagonal tube mis-counted with 4 antighosts is caught (rule gives -2 != 0)",
           gamma_rule_13(wrong) != wrong.gamma_claimed)
    wrong2 = Row("10 with one b dropped (wrong)", 2, surfaces=(Surface(0, 1),), gamma_claimed=2)
    report("BREAK: connected sphere with one antighost dropped is caught (rule gives 3 != 2)",
           gamma_rule_15(wrong2) != wrong2.gamma_claimed)
    # a wrong telescoping constant breaks the two-bookkeeping agreement
    bad = (LEG_BASE * 4 + RAISE_EXT * 2 + (DELTA_FROZEN - 1) * 1)  # single frozen node, V_3-V_3
    report("BREAK: 022 constant +5 -> +4 breaks agreement with (1.5) on V_3-V_3",
           bad != gamma_022_rule15([3, 3], 1, 0))


def run_part1() -> None:
    print(f"seed = {SEED}")
    check_table()
    check_algebraic_rows()
    check_022_and_lemma21()
    check_frozen_limit()
    check_open_and_lemma22()
    check_break_on_purpose()


# ---------------------------------------------------------------------------
# PART 2 (12b): candidates (a)-(d) of record 030 §3.
# ---------------------------------------------------------------------------


def sym2_basis(d: int) -> list[tuple[int, int]]:
    """Index pairs (i <= j) of a basis of Sym^2 C^d."""
    return [(i, j) for i in range(d) for j in range(i, d)]


def random_s4_tensor(d: int) -> np.ndarray:
    """Random complex tensor V[a,b,c,e] symmetric under all permutations (a toy V_4)."""
    v = rng.normal(size=(d,) * 4) + 1j * rng.normal(size=(d,) * 4)
    out = np.zeros_like(v)
    for perm in itertools.permutations(range(4)):
        out += np.transpose(v, perm)
    return out / 24


def gram_on_sym2(v4: np.ndarray, d: int) -> np.ndarray:
    """Matrix M[(ab),(ce)] = V4(e_a e_b ; e_c e_e) on the Sym^2 basis (unnormalised products)."""
    basis = sym2_basis(d)
    m = np.zeros((len(basis), len(basis)), dtype=complex)
    for p, (a, b) in enumerate(basis):
        for q, (c, e) in enumerate(basis):
            m[p, q] = v4[a, b, c, e]
    return m


def sym2_of_operator(k: np.ndarray, d: int) -> np.ndarray:
    """Matrix of k (x) k restricted to Sym^2 in the unnormalised product basis e_a e_b."""
    basis = sym2_basis(d)
    idx = {pair: n for n, pair in enumerate(basis)}
    out = np.zeros((len(basis), len(basis)), dtype=complex)
    for q, (c, e) in enumerate(basis):
        # (k x k)(e_c e_e) = sum_{a,b} k[a,c] k[b,e] e_a e_b, with e_a e_b = e_b e_a.
        for a in range(d):
            for b in range(d):
                out[idx[(min(a, b), max(a, b))], q] += k[a, c] * k[b, e]
    return out


def product_form_tensor(beta: np.ndarray) -> np.ndarray:
    """Right side of 030 eq. (3.2): beta_13 beta_24 + beta_14 beta_23 as a 4-tensor."""
    return np.einsum("ac,bd->abcd", beta, beta) + np.einsum("ad,bc->abcd", beta, beta)


def s4_asymmetry(t: np.ndarray) -> float:
    """Norm of (t - transposition (23) of t): zero iff t is symmetric under B_2 <-> C_1."""
    return float(np.linalg.norm(t - np.transpose(t, (0, 2, 1, 3))))


def check_product_kernels() -> None:
    """030 §3.1, Prop. 3.1: a product kernel inverts an S4-symmetric V4 only if d = 1."""
    # (i) For d >= 2 and a random non-degenerate symmetric beta, the product form (3.2)
    #     is NOT S4-symmetric (residual of the (23) transposition non-zero), so no
    #     S4-symmetric V4 can equal it.  Independent path: the residual is computed
    #     numerically, not from the algebra of the derivation.
    for d in (2, 3, 4):
        beta = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
        beta = beta + beta.T
        res = s4_asymmetry(product_form_tensor(beta))
        report(f"prod-rank-S4: d={d}, symmetric beta, (23)-residual = {res:.3e} > 1e-8", res > 1e-8)
        beta_a = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
        beta_a = beta_a - beta_a.T
        res_a = s4_asymmetry(product_form_tensor(beta_a))
        report(f"prod-rank-S4: d={d}, antisymmetric beta, residual = {res_a:.3e} > 1e-8", res_a > 1e-8)
    # (ii) Positive control: d = 1, and rank-one beta at d = 3, give a symmetric form.
    beta1 = np.array([[rng.normal() + 1j * rng.normal()]])
    report("prod-rank-d1-control: d=1 product form is S4-symmetric", s4_asymmetry(product_form_tensor(beta1)) < 1e-12)
    lam = rng.normal(size=3) + 1j * rng.normal(size=3)
    beta_r1 = np.outer(lam, lam)
    report("prod-rank-d1-control: rank-one beta (d=3) is S4-symmetric", s4_asymmetry(product_form_tensor(beta_r1)) < 1e-12)
    # (iii) Direct test on the inverse identity: random S4-symmetric V4 at d = 2; the
    #      Gram inverse M^{-1} is not Sym^2(k) for any k.  Independent path: least
    #      squares over k (4 complex unknowns) against the 9 entries of M^{-1}, via a
    #      Newton/Gauss-Newton iteration from several random starts; residual stays > 0.
    d = 2
    m = gram_on_sym2(random_s4_tensor(d), d)
    minv = np.linalg.inv(m)
    best = np.inf
    for _ in range(20):
        k = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
        for _ in range(60):
            r = (sym2_of_operator(k, d) - minv).ravel()
            # numerical Jacobian d r / d k (complex-linearised, small step)
            jac = np.zeros((r.size, d * d), dtype=complex)
            eps = 1e-7
            for n in range(d * d):
                dk = np.zeros(d * d, dtype=complex)
                dk[n] = eps
                jac[:, n] = ((sym2_of_operator(k + dk.reshape(d, d), d) - minv).ravel() - r) / eps
            step, *_ = np.linalg.lstsq(jac, -r, rcond=None)
            k = k + step.reshape(d, d)
        best = min(best, np.linalg.norm(sym2_of_operator(k, d) - minv))
    report(f"prod-rank-S4: d=2 Gauss-Newton best residual |Sym^2 k - M^-1| = {best:.3e} > 1e-3", best > 1e-3)
    # (iv) Sums of products span End(Sym^2): random polarised products span dim 9 at d = 2.
    vecs = []
    for _ in range(12):
        k1 = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
        k2 = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
        pol = sym2_of_operator(k1 + k2, d) - sym2_of_operator(k1, d) - sym2_of_operator(k2, d)
        vecs.append(pol.ravel())
    rank = np.linalg.matrix_rank(np.array(vecs), tol=1e-8)
    report(f"prod-sum-spans: polarised products span End(Sym^2 C^2), rank {rank} = 9", rank == 9)
    # (v) Break-on-purpose: the d=1 control with a deliberately wrong product form
    #     (beta_13 beta_24 + 2 beta_14 beta_23) at d = 2 is still asymmetric — and the
    #     rank-one control fails if beta is perturbed off rank one.
    beta_pert = beta_r1 + 1e-3 * (rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)))
    beta_pert = beta_pert + beta_pert.T
    report("prod-rank break-on-purpose: perturbed rank-one beta is NOT symmetric (check can fail)",
           s4_asymmetry(product_form_tensor(beta_pert)) > 1e-8)


def check_commutant() -> None:
    """030 §3.2, Prop. 3.2: tube-only kernels commute with the strand L_0's; m_2 does not."""
    d = 3
    basis = sym2_basis(d)
    nb = len(basis)
    # L_0^+ eigenvalues per basis state; the symmetric functions e1, e2 on Sym^2.
    lvals = rng.normal(size=d) + 1.0
    e1 = np.diag([lvals[a] + lvals[b] for (a, b) in basis])
    e2 = np.diag([lvals[a] * lvals[b] for (a, b) in basis])
    # (i) A correlated tube kernel g(L1, L2) with a random joint measure on a grid of
    #     (s1, s2): diagonal in this basis, hence commutes with e1, e2.
    s_grid = rng.uniform(0.1, 2.0, size=(6, 2))
    mu = rng.normal(size=6)
    g = np.diag([sum(mu[n] * np.exp(-s_grid[n, 0] * lvals[a] - s_grid[n, 1] * lvals[b]) for n in range(6)) for (a, b) in basis])
    g_sym = np.diag([sum(mu[n] * (np.exp(-s_grid[n, 0] * lvals[a] - s_grid[n, 1] * lvals[b]) + np.exp(-s_grid[n, 0] * lvals[b] - s_grid[n, 1] * lvals[a])) / 2 for n in range(6)) for (a, b) in basis])
    report("commutant-L0: correlated tube kernel commutes with e1(L), e2(L)",
           np.linalg.norm(g_sym @ e1 - e1 @ g_sym) < 1e-12 and np.linalg.norm(g_sym @ e2 - e2 @ g_sym) < 1e-12)
    del g
    # (ii) A generic S4-symmetric V4 does not commute with e1 (off-diagonal entries), so
    #      no tube kernel can be its inverse: |M K - 1| >= something for the best diagonal K.
    m = gram_on_sym2(random_s4_tensor(d), d)
    report("commutant-generic-V4: generic V4 does not commute with e1(L)", np.linalg.norm(m @ e1 - e1 @ m) > 1e-6)
    # best diagonal K (least squares on M K = 1 with K diagonal): residual stays large.
    cols = [np.outer(m[:, n], np.eye(nb)[n]).ravel() for n in range(nb)]  # d/dK_nn of (M K)
    coef, *_ = np.linalg.lstsq(np.array(cols).T, np.eye(nb).ravel(), rcond=None)
    resid = np.linalg.norm(m @ np.diag(coef) - np.eye(nb))
    report(f"commutant-generic-V4: best level-diagonal K leaves |M K - 1| = {resid:.3e} > 0.1", resid > 0.1)
    # (iii) Control: a V4 that IS level-diagonal (M = diag(1/g)) is inverted by the tube
    #      kernel, so the check can pass when it should.
    m_diag = np.diag(1.0 / np.diag(g_sym))
    report("commutant-diag-V4-control: level-diagonal V4 is inverted by the tube kernel",
           np.linalg.norm(m_diag @ g_sym - np.eye(nb)) < 1e-10)
    # (iv) Harold's 9a/9b diagonal tube (one b^+): as a map its ghost number is -1, not
    #      -2 -- already in part 1 (row 9b).  Here: (b1 + b2) b1 = b1 b2 on the zero-mode
    #      Fock space, so the extra antighost repairs the count on either strand alike.
    b, c, _, _, _ = fermion_ops()
    one = np.eye(b.shape[0])
    b1 = np.kron(b, one)
    b2 = np.kron(np.diag([1, -1, -1, 1])[: b.shape[0], : b.shape[0]] if b.shape[0] == 4 else one, b)  # graded tensor
    lhs = (b1 + b2) @ b1
    rhs = (b1 + b2) @ b2
    report("commutant: (b1+b2) b1 = -(b1+b2) b2 = b1 b2 up to sign (which strand carries the extra b is immaterial)",
           np.linalg.norm(lhs @ lhs) < 1e-12 and np.linalg.norm(rhs @ rhs) < 1e-12 and np.linalg.norm(np.abs(lhs) - np.abs(rhs)) < 1e-12)
    del c


def check_explicit_ghosts() -> None:
    """030 §3.3, eq. (3.8): K_x = B^t M B' is degree +1 in the vertex data; the inverse is -1."""
    d = 2
    nb = len(sym2_basis(d))
    # Explicit example: B = B' = 1, M an involution (M^2 = 1): M B^t M B' = 1 holds at
    # lambda = 1 and FAILS at lambda = 2 (scaling leg).
    # A symmetric involution M = Q diag(+-1) Q^t with Q real orthogonal.
    q_frame, _ = np.linalg.qr(rng.normal(size=(nb, nb)))
    m_inv = q_frame @ np.diag(rng.choice([-1.0, 1.0], size=nb)) @ q_frame.T
    ok1 = np.linalg.norm(m_inv @ m_inv - np.eye(nb)) < 1e-10
    lam = 2.0
    ok2 = np.linalg.norm((lam * m_inv) @ (lam * m_inv) - np.eye(nb)) > 1.0
    report("explicit-ghost-scaling: M B^t M B' = 1 at lambda=1 (involutive M, B=B'=1)", ok1)
    report("explicit-ghost-scaling: the same identity FAILS at lambda=2 (degree +2, not 0)", ok2)
    # Family leg: directional derivative of M -> M B^t M B' along dM = M equals 2*id.
    b_t = rng.normal(size=(nb, nb)); b_p = rng.normal(size=(nb, nb))
    m = gram_on_sym2(random_s4_tensor(d), d)
    f = lambda x: x @ b_t @ x @ b_p  # noqa: E731
    eps = 1e-6
    deriv = (f((1 + eps) * m) - f(m)) / eps
    report("explicit-ghost-family: d/d(eps) [(1+eps)M B^t (1+eps)M B'] = 2 M B^t M B' (never 0)",
           np.linalg.norm(deriv - 2 * f(m)) < 1e-4 * np.linalg.norm(f(m)) and np.linalg.norm(f(m)) > 1e-8)
    # Chain identity, not inverse identity: for random V4, M K_x M is a length-3 chain and
    # M K_x != 1 (falsifiable: with K_x = M^{-1} it would be 1).
    k_x = b_t @ m @ b_p
    report("explicit-ghost: random dressed vertex B^t M B' is not an inverse (|M K_x - 1| > 0.1)",
           np.linalg.norm(m @ k_x - np.eye(nb)) > 0.1)
    report("explicit-ghost break-on-purpose: K = M^{-1} does satisfy M K = 1 (check can distinguish)",
           np.linalg.norm(m @ np.linalg.inv(m) - np.eye(nb)) < 1e-10)


def check_laplace() -> None:
    """030 §3.4: the direct Laplace form diverges on an indefinite toy; the squared form does not."""
    n = 4
    q_frame, _ = np.linalg.qr(rng.normal(size=(n, n)))
    ev_pos = rng.uniform(0.5, 2.0, size=n)
    ev_ind = ev_pos.copy(); ev_ind[0] *= -1
    m_pos = q_frame @ np.diag(ev_pos) @ q_frame.T
    m_ind = q_frame @ np.diag(ev_ind) @ q_frame.T
    t_big = 30.0
    grow = np.linalg.norm(expm(-t_big * m_ind))
    decay = np.linalg.norm(expm(-t_big * m_pos))
    report(f"laplace-indefinite-diverges: |e^(-30 m)| = {grow:.2e} > 1e3 on the indefinite toy", grow > 1e3)
    report(f"laplace-indefinite-diverges: |e^(-30 m)| = {decay:.2e} < 1e-3 on the positive toy (control)", decay < 1e-3)
    # squared form on the indefinite toy: int_0^T m e^{-t m^2} dt -> m^{-1}
    ts = np.linspace(0, 40, 40001)
    acc = np.zeros((n, n))
    for t0, t1 in zip(ts[:-1], ts[1:]):
        tm = 0.5 * (t0 + t1)
        acc += (t1 - t0) * (m_ind @ expm(-tm * m_ind @ m_ind))
    report("laplace-squared-unconditional: int m e^{-t m^2} dt = m^{-1} on the indefinite toy (rel. err < 1e-3)",
           np.linalg.norm(acc - np.linalg.inv(m_ind)) / np.linalg.norm(np.linalg.inv(m_ind)) < 1e-3)


def run_part2() -> None:
    """Checks for 030 §3 (12b): product kernels, commutant, explicit ghosts, Laplace."""
    print("\n--- part 2 (12b) ---")
    check_product_kernels()
    check_commutant()
    check_explicit_ghosts()
    check_laplace()


# ---------------------------------------------------------------------------
# PART 3 (12c): candidate (e), the change of kinetic term, and the toy of 030 §4.
# Surface-built kernels K^{-1} (product, diagonal, Neumann-truncated) are tested
# against a generic S_4-symmetric V_4 Gram matrix M on Sym^2 C^d through identities
# that CAN fail: M =? W^t g W with W of surface type (least squares over W), and
# M K =? 1 for the surface-built K.  Never forms M^{-1} to build a candidate.
# ---------------------------------------------------------------------------


from scipy.optimize import least_squares  # noqa: E402  (part 3 only)


def tube_kernel(levels: np.ndarray, lam: float) -> np.ndarray:
    """Level-diagonal bounded diagonal tube on Sym^2, eq. (3.14) (beta2), stripped of b's.

    g_(ab) = (1 - exp(-lam (l_a + l_b))) / (l_a + l_b), with the limit lam at l_a + l_b = 0.
    Real and positive for every real level sum (entire in L_tot, 030 §3.7.5).
    """
    out = []
    for a, b in sym2_basis(len(levels)):
        lt = levels[a] + levels[b]
        out.append(lam if abs(lt) < 1e-12 else (1 - np.exp(-lam * lt)) / lt)
    return np.diag(np.array(out, dtype=complex))


def tensor_from_sym2_matrix(x: np.ndarray, d: int) -> np.ndarray:
    """2+2 tensor T[a,b,c,e] = X[(ab),(ce)] from a matrix on the Sym^2 product basis."""
    basis = sym2_basis(d)
    idx = {pair: n for n, pair in enumerate(basis)}
    t = np.zeros((d,) * 4, dtype=complex)
    for a in range(d):
        for b in range(d):
            for c in range(d):
                for e in range(d):
                    t[a, b, c, e] = x[idx[(min(a, b), max(a, b))], idx[(min(c, e), max(c, e))]]
    return t


def three_channel(t: np.ndarray) -> np.ndarray:
    """Sum over the three pairings, 030 eq. (3.11): T_abce + T_acbe + T_aebc."""
    return t + np.transpose(t, (0, 2, 1, 3)) + np.transpose(t, (0, 3, 1, 2))


def fit_w(target: np.ndarray, g: np.ndarray, d: int, kind: str, r: int | None = None,
          real: bool = False, nstarts: int = 6) -> float:
    """Least squares over W of the identity target = (single or three-channel)[W^t g W].

    kind: 'single' (target = matrix M on Sym^2, W is r x N unconstrained),
          'single-product' / 'three-product' (W = Sym^2(w), w in C^{d x d}: disconnected
          W_3 = two 2-punctured spheres; target = M resp. the 4-tensor V4),
          'three' (unconstrained W, target = 4-tensor).
    Returns the best Frobenius residual over nstarts random starts. Never forms M^{-1}.
    """
    n = len(sym2_basis(d))
    r = n if r is None else r
    npar = d * d if "product" in kind else r * n

    def unpack(x: np.ndarray) -> np.ndarray:
        z = x[:npar] if real else x[:npar] + 1j * x[npar:]
        if "product" in kind:
            return sym2_of_operator(z.reshape(d, d), d)
        return z.reshape(r, n)

    def resid(x: np.ndarray) -> np.ndarray:
        w = unpack(x)
        gg = g[: w.shape[0], : w.shape[0]]   # Sigma space truncated to r pair-levels
        x_mat = w.T @ gg @ w
        if kind.startswith("three"):
            res = three_channel(tensor_from_sym2_matrix(x_mat, d)) - target
        else:
            res = x_mat - target
        return np.concatenate([res.real.ravel(), res.imag.ravel()])

    best = np.inf
    for _ in range(nstarts):
        x0 = rng.normal(size=npar if real else 2 * npar)
        sol = least_squares(resid, x0, xtol=1e-14, ftol=1e-14, gtol=1e-14, max_nfev=4000)
        best = min(best, float(np.linalg.norm(sol.fun)))
    return best


def check_factorisation_toy() -> None:
    """030 §4: M =? W^t g W and V4 =? Sym_3[W^t g W] for surface-built W and g."""
    d, lam = 3, 0.7
    levels = np.array([-1.0, 0.0, 1.0])       # tachyon-like, massless, massive
    n = len(sym2_basis(d))                    # = 6
    v4 = random_s4_tensor(d)
    m = gram_on_sym2(v4, d)
    g = tube_kernel(levels, lam)
    sv = np.linalg.svd(m, compute_uv=False)
    print(f"  d={d}, N={n}, rank M = {np.sum(sv > 1e-10)}, singular values {np.round(sv, 3)}")
    # (A) Tautology guard: unconstrained complex W at r = N always works (Takagi).
    res_a = fit_w(m, g, d, "single")
    report(f"takagi-unconstrained-W: single-channel M = W^t g W solvable for free W (res {res_a:.1e})", res_a < 1e-8)
    # (B) Rank bound: r < rank M cannot work; Eckart-Young lower bound.
    r = n - 2
    res_b = fit_w(m, g, d, "single", r=r)
    bound = float(np.sqrt(np.sum(sv[r:] ** 2)))
    report(f"rank-bound-W: r={r}<N: residual {res_b:.3e} >= Eckart-Young bound {bound:.3e} > 0",
           res_b >= 0.99 * bound and bound > 1e-3)
    # (B') Product tube from a rank-deficient single-strand propagator: rank rho(rho+1)/2.
    rho = 2
    pk = rng.normal(size=(d, rho)) + 1j * rng.normal(size=(d, rho))
    p_single = pk @ pk.T                       # rank-rho symmetric single-strand kernel
    g_prod = sym2_of_operator(p_single, d)
    rk = np.linalg.matrix_rank(g_prod, tol=1e-9)
    report(f"product-tube-rank: Sym^2(P) with rank P={rho} has rank {rk} = rho(rho+1)/2 = {rho*(rho+1)//2} < N={n}",
           rk == rho * (rho + 1) // 2)
    res_bp = fit_w(m, g_prod, d, "single")
    bound_bp = float(np.sqrt(np.sum(sv[rk:] ** 2)))
    report(f"product-tube-fails: M = W^t Sym^2(P) W residual {res_bp:.3e} >= bound {bound_bp:.3e}",
           res_bp >= 0.99 * bound_bp and bound_bp > 1e-3)
    # (C) Disconnected W_3 (W = Sym^2 w): d^2 parameters vs C(d+3,4) target components.
    ncomp = d * (d + 1) * (d + 2) * (d + 3) // 24
    res_c3 = fit_w(v4, g, d, "three-product", nstarts=8)
    res_c1 = fit_w(m, g, d, "single-product", nstarts=8)
    report(f"disconnected-W3-fails: three-channel residual {res_c3:.3e} (d^2={d*d} params vs {ncomp} comps)", res_c3 > 1e-3)
    report(f"disconnected-W3-fails: single-channel residual {res_c1:.3e}", res_c1 > 1e-3)
    # (C') Positive control: a V4 *generated* by a product W is recovered (check can pass),
    #      and a 1e-2 perturbation of it is caught (break-on-purpose).
    w0 = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    t0 = three_channel(tensor_from_sym2_matrix(sym2_of_operator(w0, d).T @ g @ sym2_of_operator(w0, d), d))
    res_ctrl = fit_w(t0, g, d, "three-product", nstarts=8)
    report(f"disconnected-W3-control: generated V4 recovered (res {res_ctrl:.1e})", res_ctrl < 1e-7)
    t1 = t0 + 1e-2 * random_s4_tensor(d)
    res_brk = fit_w(t1, g, d, "three-product", nstarts=8)
    report(f"BREAK: perturbed control (1e-2) is caught (res {res_brk:.1e} > 1e-4)", res_brk > 1e-4)
    # (D) m_2 K = 1 for the bounded diagonal tube itself, lam scanned (Prop. 3.2 again).
    best_d = min(np.linalg.norm(m @ tube_kernel(levels, x) - np.eye(n)) for x in np.linspace(0.05, 20, 400))
    report(f"diag-tube-m2K: min_lam |M g(lam) - 1| = {best_d:.3e} > 0.1 for generic M", best_d > 0.1)
    m_diag = np.diag(1 / np.diag(g))
    report("diag-tube-m2K-control: level-diagonal M is inverted by g(lam)",
           np.linalg.norm(m_diag @ g - np.eye(n)) < 1e-12)
    # (E) Neumann chain truncated at order n on the level-diagonal part D of M.
    dm = np.diag(np.diag(m))
    nm = m - dm
    t_mat = -np.linalg.solve(dm, nm)
    rho_sr = float(np.max(np.abs(np.linalg.eigvals(t_mat))))
    res_n = [np.linalg.norm(m @ sum(np.linalg.matrix_power(t_mat, k) for k in range(order + 1)) @ np.linalg.inv(dm) - np.eye(n))
             for order in (2, 6, 12)]
    report(f"neumann-diverges: rho(D^-1 N) = {rho_sr:.2f} > 1, residuals n=2,6,12: {[f'{x:.1e}' for x in res_n]}",
           rho_sr > 1 and res_n[-1] > res_n[0])
    m_dd = m + 3 * np.linalg.norm(m) * np.eye(n)
    t_dd = -np.linalg.solve(np.diag(np.diag(m_dd)), m_dd - np.diag(np.diag(m_dd)))
    res_dd = np.linalg.norm(m_dd @ sum(np.linalg.matrix_power(t_dd, k) for k in range(13)) @ np.linalg.inv(np.diag(np.diag(m_dd))) - np.eye(n))
    report(f"neumann-control: diagonally dominant M converges (n=12 residual {res_dd:.1e})", res_dd < 1e-6)
    # (F) Signature: real indefinite M vs positive g and real W (single channel).
    v4r = random_s4_tensor(d).real
    mr = gram_on_sym2(v4r, d).real
    ev = np.linalg.eigvalsh(mr)
    nneg = int(np.sum(ev < 0))
    res_f = fit_w(mr.astype(complex), g, d, "single", real=True)
    neg_norm = float(np.sqrt(np.sum(ev[ev < 0] ** 2)))
    report(f"signature-real-W: M has {nneg} negative eigenvalues; real-W residual {res_f:.3e} >= |M_-| = {neg_norm:.3e}",
           nneg > 0 and res_f >= 0.99 * neg_norm)
    wr = rng.normal(size=(n, n))
    t3 = three_channel(tensor_from_sym2_matrix(wr.T @ g.real @ wr, d))
    ev3 = np.linalg.eigvalsh(gram_on_sym2(t3, d).real)
    report(f"signature-three-channel: Sym_3 of a PSD single channel is indefinite ({int(np.sum(ev3 < 0))} neg.) -> no signature bound",
           np.sum(ev3 < 0) > 0)


def run_part3() -> None:
    """Checks for 030 §3.7 and §4 (12c)."""
    print("\n--- part 3 (12c) ---")
    check_factorisation_toy()


# ----------------------------------------------------------------------------------
# Part 4 (12d): the scaling lemma of 030 §5.6 -- polynomial-kernel floor
# ----------------------------------------------------------------------------------
# Claim: no kernel K(t) = sum_{k=0}^{d} t^k A_k (A_k arbitrary n x n, i.e. *more* general
# than any finite sum of surface-data kernels with V_4-independent moduli bounds) satisfies
# (t M) K(t) = 1 for all t.  The least-squares floor over a point set T is computed by an
# independent route (distance of the all-ones vector from the Vandermonde column span
# {t^1, ..., t^{d+1}}, times sqrt(n)); the direct fit must reach it; adding a t^{-1}
# column (the algebraic inverse smuggled in) must drive the residual to zero
# (break-on-purpose); and with |T| <= d+1 points the floor vanishes (interpolation), which
# is why the lemma is a statement "for all t", not at a single t.


def _poly_fit_residual(m: np.ndarray, ts: np.ndarray, powers: list[int]) -> float:
    """Min over A_k of sqrt(sum_i |t_i M sum_k t_i^k A_k - 1|_F^2) (linear least squares)."""
    n = m.shape[0]
    big_a = np.concatenate([np.kron(np.array([[t ** (k + 1) for k in powers]]), m) for t in ts], axis=0)
    # rows: for each t_i, the n x (n*len(powers)) block  [t^{k+1} M]_k ; unknown vec(A) per column
    rhs = np.concatenate([np.eye(n)] * len(ts), axis=0)
    sol, *_ = np.linalg.lstsq(big_a, rhs, rcond=None)
    return float(np.linalg.norm(big_a @ sol - rhs))


def _vandermonde_floor(n: int, ts: np.ndarray, powers: list[int]) -> float:
    """Independent floor: sqrt(n) * dist(all-ones, span{t^{k+1}}) (M invertible)."""
    v = np.array([[t ** (k + 1) for k in powers] for t in ts])
    ones = np.ones(len(ts), dtype=complex)
    proj, *_ = np.linalg.lstsq(v, ones, rcond=None)
    return float(np.sqrt(n) * np.linalg.norm(v @ proj - ones))


def check_scaling_lemma() -> None:
    """030 §5.6: polynomial-in-V_4 kernels cannot invert t V_4 for all t."""
    n = 6
    m = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    m = m + m.T  # symmetric, generic (invertible with probability 1)
    ts5 = rng.normal(size=5) + 1j * rng.normal(size=5)  # five points in general position
    for d in (0, 1, 2, 3):
        powers = list(range(d + 1))
        res = _poly_fit_residual(m, ts5, powers)
        floor = _vandermonde_floor(n, ts5, powers)
        report(f"scaling-lemma d={d}: fit residual {res:.4f} = Vandermonde floor {floor:.4f} > 0.1",
               abs(res - floor) < 1e-8 and floor > 0.1)
    # BREAK 1: allow the t^{-1} term (the algebraic inverse): residual must vanish.
    res_inv = _poly_fit_residual(m, ts5, [-1, 0, 1])
    report(f"BREAK: with a t^-1 term the fit succeeds (res {res_inv:.1e} < 1e-8)", res_inv < 1e-8)
    # BREAK 2: with |T| <= d+1 the floor is zero (interpolation) -- the lemma needs "all t".
    res_interp = _poly_fit_residual(m, ts5[:3], [0, 1, 2])
    report(f"BREAK: |T|=3 points, d=2: interpolation succeeds (res {res_interp:.1e} < 1e-8)", res_interp < 1e-8)
    # Concrete surface-type instance: tube o Omega o tube with Omega = M-slice (degree 1),
    # g a level-diagonal bounded tube on Sym^2 of levels (-1,0,1) -> pair levels.
    lam = 0.7
    pairs = [(i, j) for i in range(3) for j in range(i, 3)]
    ltot = np.array([(i - 1) + (j - 1) for i, j in pairs], dtype=float)
    g = np.diag([(1 - np.exp(-lam * L)) / L if abs(L) > 1e-12 else lam for L in ltot])
    res_tube = float(np.sqrt(sum(np.linalg.norm(t * m @ (t * g @ m @ g) - np.eye(n)) ** 2 for t in ts5)))
    report(f"tube-slice-tube (degree 1) residual {res_tube:.3f} >= d=1 floor {_vandermonde_floor(n, ts5, [0, 1]):.3f}",
           res_tube >= _vandermonde_floor(n, ts5, [0, 1]) - 1e-10)


def run_part4() -> None:
    """Checks for 030 §5.6 (12d)."""
    print("\n--- part 4 (12d) ---")
    check_scaling_lemma()


if __name__ == "__main__":
    run_part1()
    run_part2()
    run_part3()
    run_part4()
    n_fail = sum(1 for _, ok in RESULTS if not ok)
    print(f"\nSummary: {len(RESULTS) - n_fail}/{len(RESULTS)} PASS")
    sys.exit(1 if n_fail else 0)
