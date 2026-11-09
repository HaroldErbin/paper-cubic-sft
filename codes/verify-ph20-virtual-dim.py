r"""
Verify the PH20 addendum of derivation 036 (2026-09-26).

Claim: the genus-0 virtual dimension vd_C(0, n) = h^1(T(-D)) - h^0(T(-D)) = n - 3
holds for every n >= 0 (Riemann-Roch on CP^1), in particular vd_C(0, 2) = -1
(h^0 = 1: the vector field z d/dz; h^1 = 0), so that hat d(two-punctured sphere) = -2
and hat d_B(cylinder / node) = -2 vd_C(0, 2) = +2; and the sewing law
    hat d = sum_v hat d_v + 2 N - 6 L,     L = N - V + 1              (036 eq. A.10)
reproduces the 17 rows of the N_gh table of derivation 030 section 1.3.

What is verified
----------------
C5.1-h0   h^0(T(-D)) as 3 - rank of the vanishing conditions f(z_i) = 0 on
          f = a + b z + c z^2 (a point at infinity imposes c = 0), n = 0..8, seeded
          random complex points; compared with max(3 - n, 0).            [FALSIFIABLE]
C5.1-h1   h^1 = h^0(K^2(D)) as the kernel dimension of the moment conditions
          sum_i a_i z_i^k = 0, k = 0, 1, 2 on h = sum_i a_i / (z - z_i) (h = O(z^-4) at
          infinity); compared with max(n - 3, 0).                         [FALSIFIABLE]
C5.1-n2   the n = 2 count directly (h^0 = 1, h^1 = 0).
C5.1-RR   h^0 - h^1 = deg T(-D) + 1 = 3 - n from the two rank computations.
                                                                          [FALSIFIABLE]
C5.3-node vd(0, n1 + n2 - 2) = vd(0, n1) + vd(0, n2) - vd(0, 2) for 1 <= n1, n2 <= 8,
          all three vd's from the rank computations (tree sewing, one node).
                                                                          [FALSIFIABLE]
C5.3-chi  chi_top additivity (A.8) and the vd sewing law (A.9) on 200 random connected
          multigraphs of genus-0 components (RR at the sewn genus is used as a
          formula here).                                                  [BOOKKEEPING]
C5.4-row  each of the 17 rows (22 readings) of 030 section 1.3: hat d from the
          geometric carrier (components, nodes, loops, insertion defect delta) with
          vd from C5.1, against the table's map ghost number via 035 eq. (1.7).
                                                                          [FALSIFIABLE]
C5.4-break-*  the same with vd(0, 2) replaced by -1/2 (i.e. -1 real) and by 0:
          at least one row must fail.                                     [FALSIFIABLE]

What is NOT verified
--------------------
The dictionary (A.4) n_c = 2 h^0, n_b = 2 h^1 between ghost insertions and cohomology
(standard, Polchinski vol. 1 sec. 5.2-5.3, from memory); the per-row insertion defect
delta (moduli without b, extra b's, unsoaked CKV directions) is transcribed by hand from
030's one-line derivations; row 17 uses R39's inverse lemma (no geometric carrier, R28);
RR at genus > 0 is used as a formula, not computed.
"""

from __future__ import annotations

import sys

import numpy as np

SEED = 20260926
rng = np.random.default_rng(SEED)
print(f"seed = {SEED}")

results: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, kind: str, note: str = "") -> None:
    """Record and print one labelled PASS/FAIL line."""
    results.append((name, ok, kind))
    print(f"[{'PASS' if ok else 'FAIL'}] ({kind}) {name}: {note}")


def rand_points(n: int) -> np.ndarray:
    """Return n generic complex points."""
    return rng.normal(size=n) + 1j * rng.normal(size=n)


def h0(n: int, with_infinity: bool = False) -> int:
    """
    Dimension of holomorphic vector fields f(z) d/dz on CP^1 vanishing at n points.

    Args:
        n: number of punctures.
        with_infinity: put one of the punctures at z = infinity.

    Returns:
        int: 3 - rank of the linear conditions on (a, b, c), f = a + b z + c z^2.

    """
    rows = []
    n_fin = n - 1 if (with_infinity and n > 0) else n
    for z in rand_points(n_fin):
        rows.append([1, z, z**2])
    if with_infinity and n > 0:
        rows.append([0, 0, 1])  # f(1/w)(-w^2) = -(a w^2 + b w + c) vanishes at w=0
    if not rows:
        return 3
    return 3 - int(np.linalg.matrix_rank(np.array(rows, dtype=complex), tol=1e-9))


def h1(n: int) -> int:
    """
    Dimension of quadratic differentials with at most simple poles at n finite points.

    h(z) dz^2 regular at infinity needs h = O(z^-4); with h = sum_i a_i / (z - z_i)
    the coefficients of z^-1, z^-2, z^-3 at infinity are sum_i a_i z_i^k, k = 0, 1, 2.

    Args:
        n: number of punctures (all finite).

    Returns:
        int: n - rank of the 3 x n moment matrix.

    """
    if n == 0:
        return 0
    z = rand_points(n)
    mat = np.array([z**k for k in range(3)], dtype=complex)
    return n - int(np.linalg.matrix_rank(mat, tol=1e-9))


# ------------------------------------------------------------------ C5.1
H0 = {n: h0(n) for n in range(9)}
H0inf = {n: h0(n, with_infinity=True) for n in range(9)}
H1 = {n: h1(n) for n in range(9)}
check("C5.1-h0", all(H0[n] == H0inf[n] == max(3 - n, 0) for n in H0), "F",
      f"h0 = {[H0[n] for n in range(9)]}")
check("C5.1-h1", all(H1[n] == max(n - 3, 0) for n in H1), "F",
      f"h1 = {[H1[n] for n in range(9)]}")
check("C5.1-RR", all(H0[n] - H1[n] == (2 - n) + 1 for n in H0), "B",
      "h0 - h1 = deg T(-D) + 1 - g at g = 0")
VD = {n: H1[n] - H0[n] for n in range(9)}  # complex virtual dimension, from ranks
check("C5.1-n2", (H0[2], H1[2], VD[2]) == (1, 0, -1), "F",
      "n = 2: one CKV (z d/dz), no modulus, vd_C = -1")

# ------------------------------------------------------------------ C5.3
ok = all(VD[a + b - 2] == VD[a] + VD[b] - VD[2]
         for a in range(1, 9) for b in range(1, 9) if a + b - 2 <= 8)
check("C5.3-node", ok, "B", "one node = -vd(0,2) = +1 complex, n1, n2 in 1..8")


def vd_rr(g: int, n: int) -> int:
    """Complex virtual dimension from RR as a formula: -(2 - 2g - n + 1 - g)."""
    return -((2 - 2 * g - n) + 1 - g)


ok_chi, ok_vd = True, True
for _ in range(200):
    V = int(rng.integers(1, 6))
    nv = [int(x) for x in rng.integers(1, 7, size=V)]
    # random connected multigraph: spanning tree + extra edges, respecting valences
    edges = [(int(rng.integers(0, v)), v) for v in range(1, V)]
    edges += [tuple(int(x) for x in rng.integers(0, V, size=2))
              for _ in range(int(rng.integers(0, 3)))]
    deg = [0] * V
    for a, b in edges:
        deg[a] += 1
        deg[b] += 1
    nv = [max(nv[i], deg[i]) for i in range(V)]
    N = len(edges)
    g = N - V + 1
    n = sum(nv) - 2 * N
    ok_chi &= sum(2 - x for x in nv) == 2 - 2 * g - n
    ok_vd &= vd_rr(g, n) == sum(VD[x] if x <= 8 else x - 3 for x in nv) + N
check("C5.3-chi", ok_chi and ok_vd, "B", "chi_top additive, vd = sum vd_v + N")

# ------------------------------------------------------------------ C5.4
# Geometric carriers.  A 'geo' reading: components (all genus 0, n_v punctures),
# N nodes, V components, loops L = N - V + 1, insertion defect delta.  A 'biv' reading:
# sewing object of s strands between two connected surfaces: s nodes, loops s - 1.
# delta: -1 per modulus not carried by a b insertion (frozen node), +1 per b beyond the moduli, +1 per CKV direction
# not soaked by a c, -1 per c beyond the CKVs.  Target: 035 eq. (1.7) on 030's gamma.
TABLE = [
    # (label, reading, l, gamma, carrier)
    ("1 frozen node", "biv", 1, 0, ("biv", 1, -1)),
    ("2 cylinder as map b0+/L0+", "form", 1, -1, ("geo", [2], 0, 2)),
    ("3 cylinder P", "biv", 1, -1, ("biv", 1, 0)),
    ("4 bounded cylinder", "biv", 1, -1, ("biv", 1, 0)),
    ("5 doubly-frozen node", "biv", 1, -1, ("biv", 1, 0)),
    ("6 G2^-1", "biv", 2, 0, ("biv", 2, -2)),
    ("7 double tube", "biv", 2, -2, ("biv", 2, 0)),
    ("8 bounded double tube", "biv", 2, -2, ("biv", 2, 0)),
    ("9a fully diagonal double tube", "biv", 2, 0, ("biv", 2, -2)),
    ("9b length-diagonal double tube", "biv", 2, -1, ("biv", 2, -1)),
    ("10 Sigma_{0,4}", "form", 2, 2, ("geo", [4], 0, 0)),
    ("10 Sigma_{1,4} = Sigma_{0,6} + 1 node", "form", 2, 2, ("geo", [6], 1, 0)),
    ("10 Sigma_{2,4} = Sigma_{0,8} + 2 nodes", "form", 2, 2, ("geo", [8], 2, 0)),
    ("11 rigid 4-punctured sphere", "form", 2, 4, ("geo", [4], 0, -2)),
    ("12 half-frozen sphere", "form", 2, 2, ("geo", [4], 0, 0)),
    ("13 V4 - 2 frozen nodes - V4", "form", 2, 4, ("geo", [4, 4], 2, -2)),
    ("13 V4 - frozen + smoothed - V4", "form", 2, 3, ("geo", [4, 4], 2, -1)),
    ("14 sphere + 4 extra b", "form", 2, -2, ("geo", [4], 0, 4)),
    ("15 G2 = omega1 x omega1", "form", 2, 0, ("geo", [2, 2], 0, 2)),
    ("16 m2 = G2^-1 V4", "form", 2, 2, ("geo", [4], 0, 0)),
    ("17 m2^-1 as bivector", "biv", 2, -2, ("inv", 4)),
    ("17 m2^-1 as 4-form (G2 m2^-1 G2)", "form", 2, -2, ("G2invG2", 4)),
]


def target(reading: str, ell: int, gamma: int) -> int:
    """Return hat d from the map ghost number, 035 eq. (1.7)."""
    return 6 - 5 * ell - gamma if reading == "biv" else 5 * ell - 6 - gamma


def geo(carrier: tuple, vd: dict) -> float:
    """Return hat d from the geometric carrier via (A.10), with vd(0, n) supplied."""
    node = -2 * vd[2]  # hat d_B of one cylinder / node
    kind = carrier[0]
    if kind == "biv":
        s, delta = carrier[1], carrier[2]
        return s * node - 6 * (s - 1) + delta
    if kind == "geo":
        comps, n_nodes, delta = carrier[1], carrier[2], carrier[3]
        loops = n_nodes - len(comps) + 1
        return sum(2 * vd[x] for x in comps) + n_nodes * node - 6 * loops + delta
    if kind == "inv":  # R39 inverse lemma on the stable Sigma_{0,n}
        return -2 * vd[carrier[1]]
    # G2 . B . G2 as a 4-form: tree gluing, hat d = 2 hat d(G2) + hat d_B(B)
    g2 = geo(("geo", [2, 2], 0, 2), vd)
    return 2 * g2 + geo(("inv", carrier[1]), vd)


def run_rows(vd: dict, verbose: bool) -> int:
    """Compare every row; return the number of failing rows."""
    nfail = 0
    for label, reading, ell, gamma, carrier in TABLE:
        t, d = target(reading, ell, gamma), geo(carrier, vd)
        if verbose:
            print(f"    {label:42s} table {t:+d}   geometric {d:+g}")
        nfail += t != d
    return nfail


nf = run_rows(VD, verbose=True)
check("C5.4-row", nf == 0, "F", f"{len(TABLE) - nf}/{len(TABLE)} readings agree")
for wrong in (-0.5, 0):
    vd_bad = dict(VD)
    vd_bad[2] = wrong
    nf_bad = run_rows(vd_bad, verbose=False)
    check(f"C5.4-break-vd2={wrong}", nf_bad >= 1, "F",
          f"{nf_bad}/{len(TABLE)} readings fail with vd_C(0,2) = {wrong}")

nfail = sum(not ok for _, ok, _ in results)
nfals = sum(1 for _, _, k in results if k == "F")
print(f"summary: {len(results) - nfail}/{len(results)} PASS "
      f"({nfals} falsifiable, {len(results) - nfals} bookkeeping)")
sys.exit(1 if nfail else 0)
