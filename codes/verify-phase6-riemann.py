"""
Consistency self-checks for the Phase 6 geometric-interpretation note.

Target note: ``knowledge/cubic-sft-riemann-surfaces.tex''.

This note is an interpretive synthesis: it re-derives no closed-string algebra
(ledger R1-R10 are reused). It does make a handful of small *quantitative*
geometric claims -- Euler characteristics, moduli dimensions, channel/matching
counts, the auxiliary-channel vs boundary-locus dimensions, and the
bounded-vs-unbounded propagator regularity (the R3 auxiliarity mechanism). The
checks below confirm those numbers are internally consistent with the verified
Euler/degree bookkeeping (ledger R5), the bounded-propagator auxiliarity (ledger
R3), and elementary combinatorics.

These are CONSISTENCY checks of the geometric dictionary, NOT independent
re-derivations of the closed-string result, and they say NOTHING about the two
open CFT-level residuals H2 (full graded symmetry of V4) and (5.1)
(non-degeneracy of V4 on Sym^2 of the level-matched space), which no symbolic
toy can settle.

PHYSICS NOTE (corrected after Harold's flag, 2026-06-28): auxiliarity is the
BOUNDED length-integration of the Sigma-propagator excluding the s->infty pole
(R3, stub note), NOT a twist-only / s=0 / frozen-length neck. The
auxiliary Sigma-channel carries the FULL complex neck modulus (2 real moduli);
the twist-only |q|=1 locus is a SEPARATE 1-real-dim boundary-matching check (R2)
reaching only dV_{0,4}.

Run: python codes/verify-phase6-riemann.py   (or: uv run python ...)
"""

from __future__ import annotations

from itertools import combinations

import sympy as sp


def euler_char(g: int, k: int, ell: int) -> int:
    """Euler characteristic chi = 2 - 2g - k - ell of the (g, k+ell)-surface (R5)."""
    return 2 - 2 * g - k - ell


def ibl_degree(d: int, k: int, g: int) -> int:
    """|p_{k,ell,g}| = -2 d (k + g - 1) - 1  (CFL / R5)."""
    return -2 * d * (k + g - 1) - 1


def dim_c_moduli(n: int) -> int:
    """Complex dimension of M_{0,n} = n - 3 (genus zero)."""
    return n - 3


def num_pair_matchings(n: int) -> int:
    """Number of perfect matchings of n labelled points into n/2 unordered pairs.

    For n = 4 this is the count of separating channels (s, t, u) of M_{0,4}.
    """
    if n % 2 != 0:
        return 0
    return _count_matchings(list(range(n)))


def _count_matchings(points: list[int]) -> int:
    if not points:
        return 1
    first, rest = points[0], points[1:]
    total = 0
    for j in range(len(rest)):
        remaining = rest[:j] + rest[j + 1 :]
        total += _count_matchings(remaining)
        _ = (first, rest[j])  # the chosen pair (documentation only)
    return total


def main() -> None:
    results: list[tuple[str, bool]] = []

    # (1) Euler characteristic from R5: chi(M_{0,4}) = -2 for p_{2,2,0};
    #     chi = 1 - k for the single-output p_{k,1,0} on M_{0,k+1}.
    c1 = euler_char(0, 2, 2) == -2 and all(
        euler_char(0, k, 1) == 1 - k for k in range(1, 6)
    )
    results.append(("(1) chi(M_0,4)=-2 for p_220 and chi=1-k for p_k10 (R5)", c1))

    # (2) Complex moduli dimensions: dim_C M_{0,4} = 1, dim_C M_{0,3} = 0.
    c2 = dim_c_moduli(4) == 1 and dim_c_moduli(3) == 0
    results.append(("(2) dim_C M_0,4 = 1 and dim_C M_0,3 = 0", c2))

    # (3) LOAD-BEARING moduli count: one internal Sigma-line carries one complex
    #     neck modulus = 2 real = dim_R M_{0,4}; and two thrice-punctured spheres
    #     (dim_C 0 each) plus one complex neck reproduce dim_C M_{0,4} = 1.
    neck_complex_dim = 1
    one_line_real_moduli = 2 * neck_complex_dim          # s and theta
    dim_r_M04 = 2 * dim_c_moduli(4)                      # = 2
    c3 = (one_line_real_moduli == dim_r_M04 == 2
          and dim_c_moduli(3) + dim_c_moduli(3) + neck_complex_dim
          == dim_c_moduli(4) == 1)
    results.append(("(3) one Sigma-line = 1 complex neck = 2 real = dim_R M_0,4", c3))

    # (4) Euler additivity under separating degeneration: two pairs of pants
    #     (each chi = 2-0-3 = -1) give chi = -2 = chi(M_{0,4}).
    chi_pop = euler_char(0, 3, 0)
    c4 = chi_pop == -1 and (chi_pop + chi_pop == euler_char(0, 2, 2))
    results.append(("(4) chi = (-1)+(-1) = -2 (Euler additivity)", c4))

    # (5) Number of perfect matchings of 4 labelled punctures into 2 pairs = 3
    #     = the s, t, u channel count (cross-checked by brute-force partitions).
    parts = set()
    pts = (0, 1, 2, 3)
    for pair in combinations(pts, 2):
        other = tuple(p for p in pts if p not in pair)
        parts.add(frozenset({frozenset(pair), frozenset(other)}))
    c5 = num_pair_matchings(4) == 3 and len(parts) == 3
    results.append(("(5) #perfect matchings of 4 punctures = 3 (s,t,u channels)", c5))

    # (6) CORRECTED moduli statement: the auxiliary Sigma-channel is the FULL
    #     2-real-dim neck region (fills interior, conjecturally Q4); the
    #     twist-only |q|=1 boundary-matching locus is 1-real-dim (codim 1,
    #     dV_{0,4}, R2). The two are DISTINCT -- 2 != 1 is the whole point.
    #     HARDENED (2026-07-02, phase-6 critic iter-2 Concern): the twist-only
    #     dimension is DERIVED from an explicit constraint count -- parametrize
    #     the neck q = e^{-s+i*theta} (2 real parameters), impose |q|^2 - 1 = 0,
    #     and compute dim = (#params) - rank(Jacobian) at the solution locus --
    #     instead of hard-coding the "-1".
    s_p, th_p = sp.symbols("s_p theta_p", real=True)
    neck_params = (s_p, th_p)                            # q = e^{-s} e^{i theta}
    real_dim_aux_channel = len(neck_params)              # full neck = 2
    constraint = sp.exp(-2 * s_p) - 1                    # |q|^2 = e^{-2s} = 1
    jac = sp.Matrix([[sp.diff(constraint, v) for v in neck_params]])
    jac_rank_on_locus = jac.subs(s_p, 0).rank()          # locus |q|=1 <=> s=0
    real_dim_twist_only_boundary = len(neck_params) - jac_rank_on_locus
    codim_boundary = dim_r_M04 - real_dim_twist_only_boundary
    # cross-check the constraint actually cuts s = 0 (unique real solution)
    locus = sp.solve(constraint, s_p)
    c6 = (real_dim_aux_channel == 2          # auxiliary channel: NOT 1
          and jac_rank_on_locus == 1         # one independent constraint
          and real_dim_twist_only_boundary == 1
          and codim_boundary == 1
          and locus == [0]
          and real_dim_aux_channel != real_dim_twist_only_boundary)
    results.append(
        ("(6) aux channel 2-real-dim vs twist-only boundary 1-real-dim "
         "(derived: 2 params - rank-1 constraint)", c6)
    )

    # (7) R3 AUXILIARITY MECHANISM (falsifiable, symbolic): the BOUNDED-range
    #     propagator integral is regular as L0 -> 0, while the UNBOUNDED one
    #     diverges. This is the actual auxiliarity criterion (no on-shell pole).
    s, L0, lam = sp.symbols("s L0 lambda", positive=True)
    bounded = sp.integrate(sp.exp(-s * L0), (s, 0, 2 * lam))
    bounded_simpl = sp.simplify(bounded - (1 - sp.exp(-2 * lam * L0)) / L0)
    bounded_limit = sp.limit(bounded, L0, 0)              # -> 2 lambda (finite)
    unbounded = sp.integrate(sp.exp(-s * L0), (s, 0, sp.oo))  # -> 1/L0
    unbounded_limit = sp.limit(unbounded, L0, 0)          # -> oo (pole)
    c7 = (bounded_simpl == 0
          and sp.simplify(bounded_limit - 2 * lam) == 0
          and bool(bounded_limit.is_finite)
          and sp.simplify(unbounded - 1 / L0) == 0
          and unbounded_limit == sp.oo)
    results.append(
        ("(7) R3: bounded prop regular (->2lam), unbounded prop pole (1/L0)", c7)
    )

    # (8) IBL degree separates operations only for d != 0. At d = 0 the formula
    #     collapses to -1 for ALL (k, g) (so d=0 does NOT distinguish them); at
    #     d = 1 it is (k+g)-dependent and distinguishes the low operations.
    low_ops = {  # (k, g) for p_110, p_210, p_220, p_310
        "p_110": (1, 0),
        "p_210": (2, 0),
        "p_220": (2, 0),
        "p_310": (3, 0),
    }
    d0_all_minus1 = all(ibl_degree(0, k, g) == -1 for (k, g) in low_ops.values())
    d1 = {name: ibl_degree(1, k, g) for name, (k, g) in low_ops.items()}
    d1_expected = {"p_110": -1, "p_210": -3, "p_220": -3, "p_310": -5}
    d1_distinguishes = len(set(d1.values())) >= 3  # not all equal at d != 0
    c8 = d0_all_minus1 and d1 == d1_expected and d1_distinguishes
    results.append(
        ("(8) |p_klg| collapses to -1 at d=0; (k+g)-dependent at d=1", c8)
    )

    npass = sum(1 for _, ok in results if ok)
    width = max(len(name) for name, _ in results)
    print("Phase 6 geometric-dictionary consistency checks")
    print("=" * (width + 8))
    for name, ok in results:
        print(f"{name:<{width}}  {'PASS' if ok else 'FAIL'}")
    print("=" * (width + 8))
    print(f"{npass}/{len(results)} PASS")
    if npass != len(results):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
