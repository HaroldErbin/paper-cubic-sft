"""ST6 --- two-parameter physical ghost-number formula for IBL structure maps.

Checks the closed formula

    N_gh(p_{k,ell,g}) = 3*ell - 2*k + g

in TWO tiers (restructured 2026-07-09 after the blind critic pass, finding S1:
the original 11 checks were tautological, circular, or convention-blind — the
homogeneity checks pass equally for the corrected values (+4, +2, +2) and the
stale ones (0, -2, -2), because the uniform Delta-shift error cancels between
the two sides of each relation; the earlier verify-a3 script indeed
"9/9-PASS-verified" the stale values through the same tests).

Tier 1 (NEW, GENUINE): a saturation-support derivation on the physical-grading
toy of verify-omega2-physical.py (dim H0=4, N_gh=[2,3,2,3], omega1 pairing
2<->3 at total 5, G2=omega1^{x2}). The maps l2, m2=p220, p120 are BUILT from
generic tensors V3 (saturation-6 support), V4 (saturation-8 support) and
Delta=omega1^{-1}, and their ghost shifts are MEASURED from the realized
support, not asserted: l2 -> {-1}, m2 -> {+2}, p120 -> {+4}. This derivation
would FAIL on the stale values (m2=-2, p120=0). The (1,1,1) relation then pins
p111=+2 GIVEN the independently anchored p120=+4 (no longer convention-blind).
The genus coefficient is thereby verified at g=1 only; for g>=2 the +g term is
a convention-consistent extension (ghost-additive operadic self-gluing), not an
independently anchored computation [critic C3].

Tier 2 (bookkeeping): the original formula-consistency checks, KEPT but
relabelled as internal consistency of the closed formula (they do not, by
themselves, discriminate the +5-vs-+1 Delta-shift convention).

Reference values: Erbin (2023) conventions; project ledger R7/R16; brief ST6.
"""

from __future__ import annotations

import itertools

import numpy as np


def N(k: int, ell: int, g: int) -> int:
    """Physical ghost number of the IBL structure map p_{k,ell,g}."""
    return 3 * ell - 2 * k + g


# ---------------------------------------------------------------------------
# Tier 1: saturation-support derivation (genuine; added 2026-07-09, critic S1)
# ---------------------------------------------------------------------------

NGH = np.array([2, 3, 2, 3])  # physical-grading toy: two ghost-2, two ghost-3
DIM = 4
TOLZ = 1e-12


def _support_tensor(rank: int, total: int, rng) -> np.ndarray:
    """Generic tensor supported exactly on Sum N_gh(legs) == total."""
    T = np.zeros((DIM,) * rank)
    for idx in itertools.product(range(DIM), repeat=rank):
        if sum(NGH[i] for i in idx) == total:
            T[idx] = rng.standard_normal()
    return T


def _shift_set(T: np.ndarray, n_out: int) -> set:
    """Realized ghost shifts sum(out legs) - sum(in legs) over the nonzero
    support of a map tensor whose FIRST n_out axes are outputs."""
    shifts = set()
    for idx in zip(*np.nonzero(np.abs(T) > TOLZ)):
        out = sum(NGH[i] for i in idx[:n_out])
        inn = sum(NGH[i] for i in idx[n_out:])
        shifts.add(out - inn)
    return shifts


def tier1(all_ok: bool) -> bool:
    rng = np.random.default_rng(20260709)
    # omega1: generic pairing supported on n_i + n_j == 5 (one c0^-; R7)
    w = _support_tensor(2, 5, rng)
    inv_ok = abs(np.linalg.det(w)) > 1e-6
    Delta = np.linalg.inv(w)
    # Delta support: also 2<->3, i.e. a bivector at total N_gh = 5 (not 6)
    d_ok = all(
        NGH[i] + NGH[j] == 5
        for i, j in zip(*np.nonzero(np.abs(Delta) > TOLZ))
    )
    print(f"omega1 invertible on 2<->3 support; Delta bivector at total 5: "
          f"{'PASS' if inv_ok and d_ok else 'FAIL'}")
    all_ok &= inv_ok and d_ok

    V3 = _support_tensor(3, 6, rng)  # 3-point saturation 2n=6
    V4 = _support_tensor(4, 8, rng)  # 4-point saturation 2n=8
    nz_ok = np.abs(V3).max() > 0 and np.abs(V4).max() > 0

    # l2 = Delta-raised V3 (first slot): l2[o,a,b] = Delta[o,p] V3[p,a,b]
    l2 = np.einsum("op,pab->oab", Delta, V3)
    s_l2 = _shift_set(l2, 1)
    ok_l2 = s_l2 == {-1}
    print(f"l2 = Delta.V3: measured shift {s_l2} == {{-1}}:      "
          f"{'PASS' if ok_l2 else 'FAIL'}")

    # m2 = G2^{-1} V4 (two Delta-raisings): m2[c,d,a,b] = D[c,p]D[d,q]V4[pqab]
    m2 = np.einsum("cp,dq,pqab->cdab", Delta, Delta, V4)
    s_m2 = _shift_set(m2, 2)
    ok_m2 = s_m2 == {+2} and -2 not in s_m2
    print(f"m2 = G2^-1 V4: measured shift {s_m2} == {{+2}} (stale -2 EXCLUDED): "
          f"{'PASS' if ok_m2 else 'FAIL'}")

    # p120 = Delta-raised l2: p120[c,d,a] = l2[c,p,a] Delta[p,d]
    p120 = np.einsum("cpa,pd->cda", l2, Delta)
    s_p120 = _shift_set(p120, 2)
    ok_p120 = s_p120 == {+4} and 0 not in s_p120
    print(f"p120 = (l2 x id).Delta: measured shift {s_p120} == {{+4}} "
          f"(stale 0 EXCLUDED): {'PASS' if ok_p120 else 'FAIL'}")

    # (1,1,1) relation now PINS p111 given the ANCHORED p120 (+4):
    # N(Q o p111) = N(l2 o p120)  =>  1 + N(p111) = -1 + 4  =>  N(p111) = +2.
    # (With p120 derived, this is no longer convention-blind: the stale pair
    # (p120=0 -> p111=-2) is excluded because p120=0 is excluded above.)
    n_p111 = (-1 + max(s_p120)) - 1
    ok_p111 = n_p111 == +2
    print(f"(1,1,1) relation + anchored p120 pins N(p111) = {n_p111:+d} == +2: "
          f"{'PASS' if ok_p111 else 'FAIL'}")
    print("NOTE: genus coefficient +g hereby verified at g=1 only; g>=2 is the "
          "ghost-additive convention extension [C3].")

    return all_ok and nz_ok and ok_l2 and ok_m2 and ok_p120 and ok_p111


def main() -> None:
    print("=== Tier 1: saturation-support derivation (genuine) ===")
    all_ok = tier1(True)

    print("\n=== Tier 2: closed-formula internal consistency (bookkeeping; "
          "does NOT discriminate the Delta-shift convention by itself) ===")
    # (name, (k, ell, g), expected N_gh) --- Table 1 values. The three ST6
    # values (+4, +2, +2) are NOT independent anchors here: they are the
    # Tier-1-derived values re-stated (circular if cited alone; critic S1).
    cases = [
        ("Q      (1,1,0)", (1, 1, 0), +1),
        ("l2     (2,1,0)", (2, 1, 0), -1),
        ("l3     (3,1,0)", (3, 1, 0), -3),
        ("l4     (4,1,0)", (4, 1, 0), -5),  # 3-2n special case
        ("p120   (1,2,0)", (1, 2, 0), +4),
        ("m2     (2,2,0)", (2, 2, 0), +2),
        ("p111   (1,1,1)", (1, 1, 1), +2),  # genus cross-check
    ]
    for name, (k, ell, g), want in cases:
        got = N(k, ell, g)
        ok = got == want
        all_ok &= ok
        print(f"{name}  N_gh={got:+d}  expected={want:+d}  {'PASS' if ok else 'FAIL'}")

    # ell = 1, g = 0 reduces to N_gh(l_n) = 3 - 2n.
    red = all(N(k, 1, 0) == 3 - 2 * k for k in range(1, 7))
    print(f"ell=1,g=0 reduces to 3-2n:            {'PASS' if red else 'FAIL'}")
    all_ok &= red

    # N_gh-homogeneity of the (2,2,0) relation: all four terms must match.
    r220 = {N(1, 1, 0) + N(2, 2, 0), N(1, 2, 0) + N(2, 1, 0)}
    print(f"(2,2,0) relation homogeneous at {r220}: {'PASS' if r220 == {3} else 'FAIL'}")
    all_ok &= r220 == {3}

    # N_gh-homogeneity of the (1,1,1) relation. The genus-1 loop in
    # l2 o_2 p120 is formed by a double operadic gluing that carries no extra
    # ghost number, so N_gh is additive: -1 + 4 = +3, matching Q o p111 = +3.
    r111 = {N(1, 1, 0) + N(1, 1, 1), N(2, 1, 0) + N(1, 2, 0)}
    print(f"(1,1,1) relation homogeneous at {r111}: {'PASS' if r111 == {3} else 'FAIL'}")
    all_ok &= r111 == {3}

    # Suspended (CFL) picture: subtract 3 per output slot (one suspension
    # operation per slot, weighted by the slot's ghost number 3) --> the
    # +3*ell growth is removed, leaving an ell-INDEPENDENT degree -2k+g. The
    # match with CFL's |p_{k,ell,g}| = -2d(k+g-1)-1 is in ell-INDEPENDENCE
    # ONLY [critic S2]: the residual (k,g)-structure cannot agree for any d
    # (CFL is k<->g symmetric through k+g; -2k+g is not: k-slope wants d=1,
    # g-slope wants d=-1/2). Expected, since the per-slot dictionary is not a
    # per-map offset.
    susp = {(k, ell, g): N(k, ell, g) - 3 * ell
            for k in (1, 2, 3) for ell in (1, 2, 3) for g in (0, 1)}
    ell_indep = all(
        susp[(k, 1, g)] == susp[(k, ell, g)]
        for k in (1, 2, 3) for ell in (2, 3) for g in (0, 1)
    )
    print(f"suspended degree ell-independent:      {'PASS' if ell_indep else 'FAIL'}")
    all_ok &= ell_indep

    print("\nALL PASS" if all_ok else "\nSOME FAIL")


if __name__ == "__main__":
    main()
