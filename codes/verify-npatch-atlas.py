"""
Companion checks for record 077: the n-puncture patch in the atlas picture.

Verified (exact integer / rational arithmetic, no floating point except the
Moebius checks, which use exact sympy rationals too):
  C1.1  trivalent tree counts V = N-2, E_int = N-3 (enumeration, N <= 8);
  C1.2  ghost bookkeeping 2N - 2(N-3) = 6 against the S-6 calculus;
  C2.1  two-patch presentation: the configuration {z^R} u {1/(q z^L)} modulo
        PSL(2,C) is invariant under a Moebius change of the global coordinate
        with a new q' (cross-ratios compared), redundancy 4 = (2n+1) - (2n-3);
  C2.2  the seam (z^L/lam, lam z^R, q) leaves the configuration invariant;
  C3.1  2 d_n + 1 = 2n - 3  iff  d_n = n - 2;
  C3.2  sum_k V_k (k-3) + E_int = N - 3 symbolically and by enumeration of
        valence vectors for N = 4, 6, 8;
  C3.3  trinion count (a-1)+(b-1)+(c-1) = a+b+c-3;
  C4.1  dressed patch-state ghost number 2n - 2(n-2) = 4 (n >= 2), virtual at n = 1;
  C4.2  pairing 4 + 4 - 2 = 6;
  C4.3  antighost split 2(n-2)+2(n-2)+2 = 4n-6 and the trinion split;
  C4.4  Sigma_k-edge count: composite of two vertices has the counts of a
        (N1+N2-2k)-point sphere iff the edge removes 2k-3 moduli, 4k-6 b's;
  C5.1  n = 1 virtual counts;
  C5.3  HS diagrams at N = 4, 6 have N-3 moduli.
Each family has a break leg (a deliberately wrong formula) that must FAIL.

Not verified: the covering statements (R80 C1.2-C1.3), the operator identity
(2.4), the structure of p_{k,k}^{-1} at k >= 3 (a count only), anything about
the local coordinates off shell.

Record: agent/derivations/077-npatch-atlas.md.
"""

from __future__ import annotations

import itertools
import random
import sys

import sympy as sp

CHECKS: list[tuple[str, bool]] = []
BREAKS: list[tuple[str, bool]] = []
SEED = 20261004


def check(name: str, ok: bool) -> None:
    """Register one named PASS/FAIL check."""
    CHECKS.append((name, ok))
    print(f"{'PASS' if ok else 'FAIL'}  {name}")


def break_leg(name: str, wrong_passes: bool) -> None:
    """Register a break leg: the wrong formula must fail (wrong_passes False)."""
    BREAKS.append((name, not wrong_passes))
    print(f"{'PASS' if not wrong_passes else 'FAIL'}  break:{name} (wrong formula fails: {not wrong_passes})")


# ---------------------------------------------------------------- trees


def valence_vectors(n_leaves: int, kmax: int | None = None):
    """All (V_3, ..., V_kmax) with sum_k (k-2) V_k = N-2 (eq. 3.2)."""
    kmax = kmax or n_leaves
    ks = list(range(3, kmax + 1))
    target = n_leaves - 2

    def rec(i: int, rest: int):
        if i == len(ks):
            if rest == 0:
                yield ()
            return
        w = ks[i] - 2
        for v in range(rest // w + 1):
            for tail in rec(i + 1, rest - v * w):
                yield (v, *tail)

    return [dict(zip(ks, vec)) for vec in rec(0, target)]


def tree_moduli(vk: dict[int, int], per_vertex) -> int:
    """sum_k V_k per_vertex(k) + E_int with E_int = V - 1 (eq. 3.3)."""
    v_tot = sum(vk.values())
    return sum(v * per_vertex(k) for k, v in vk.items()) + (v_tot - 1)


def enumerate_trivalent_trees(n_leaves: int) -> list[tuple[int, int]]:
    """Build all unlabelled-shape trivalent trees with N leaves by leaf insertion; return (V, E_int)."""
    # Start from the 3-leaf star: vertices {0}, leaves 1..3; insert a new leaf on each edge.
    trees = [({(0, 1), (0, 2), (0, 3)}, 1, 3)]  # (edges, n_internal, n_leaves)
    for _ in range(3, n_leaves):
        new = []
        for edges, nv, nl in trees:
            for e in sorted(edges):
                a, b = e
                v = 1000 + nv  # fresh internal vertex id
                leaf = nl + 1
                ne = set(edges)
                ne.remove(e)
                ne |= {(a, v), (v, b), (v, leaf)}
                new.append((ne, nv + 1, leaf))
        trees = new
    out = []
    for edges, nv, nl in trees:
        # internal edge: both endpoints internal (0 or >= 1000)
        e_int = sum(1 for a, b in edges if (a == 0 or a >= 1000) and (b == 0 or b >= 1000))
        out.append((nv, e_int))
    return out


def c1_trees() -> None:
    ok = True
    for n in range(3, 9):
        for v, e_int in enumerate_trivalent_trees(n):
            ok &= v == n - 2 and e_int == n - 3
    check("C1.1-trivalent", ok)
    wrong = all(v == n - 1 for n in range(3, 9) for v, _ in enumerate_trivalent_trees(n))
    break_leg("C1.1-trivalent", wrong)
    ok = all(2 * n - 2 * (n - 3) == 6 and (2 * n - 6) == 2 * (n - 3) for n in range(3, 11))
    check("C1.2-ghost", ok)
    break_leg("C1.2-ghost", all(2 * n - 2 * (n - 2) == 6 for n in range(3, 11)))


# ---------------------------------------------------------------- C2: Moebius redundancy


def cross_ratios(pts: list[sp.Expr]) -> list[sp.Expr]:
    """All cross-ratios (p_i - p_k)(p_j - p_l) / ((p_i - p_l)(p_j - p_k)) over 4-subsets, canonical order."""
    out = []
    for i, j, k, l in itertools.combinations(range(len(pts)), 4):
        a, b, c, d = pts[i], pts[j], pts[k], pts[l]
        out.append(sp.simplify((a - c) * (b - d) / ((a - d) * (b - c))))
    return out


def rand_c(rng: random.Random) -> sp.Expr:
    """A non-zero Gaussian rational in general position (never 0: positions enter as 1/(q z))."""
    while True:
        z = sp.Rational(rng.randint(-9, 9), rng.randint(1, 5)) + sp.I * sp.Rational(rng.randint(-9, 9), rng.randint(1, 5))
        if z != 0:
            return z


def c2_redundancy(rng: random.Random) -> None:
    ok, wrong = True, True
    for n in (2, 3, 4):
        for _ in range(3):
            zl = [rand_c(rng) for _ in range(n)]
            zr = [rand_c(rng) for _ in range(n)]
            q = rand_c(rng)
            conf = zr + [1 / (q * z) for z in zl]
            # Moebius g on u_R, new q'
            while True:  # a Moebius map regular on the configuration (no point sent to infinity)
                a, b, c, d = (rand_c(rng) for _ in range(4))
                if sp.simplify(a * d - b * c) != 0 and all(sp.simplify(c * u + d) != 0 for u in conf):
                    break
            g = lambda u, a=a, b=b, c=c, d=d: (a * u + b) / (c * u + d)
            qp = rand_c(rng)
            zr_new = [g(u) for u in zr]
            zl_new = [1 / (qp * g(u)) for u in (1 / (q * z) for z in zl)]
            conf_new = zr_new + [1 / (qp * z) for z in zl_new]
            ok &= all(sp.simplify(x - y) == 0 for x, y in zip(cross_ratios(conf), cross_ratios(conf_new)))
            # break: non-Moebius map u -> u^2
            conf_bad = [u**2 for u in conf]
            wrong &= all(sp.simplify(x - y) == 0 for x, y in zip(cross_ratios(conf), cross_ratios(conf_bad)))
    check("C2.1-redundancy", ok and all((2 * n + 1) - 4 == 2 * n - 3 for n in range(2, 9)))
    break_leg("C2.1-redundancy", wrong)
    # seam: (z^L/lam, lam z^R, q) -> configuration scaled by lam (same surface)
    ok, wrong = True, True
    for n in (2, 3):
        zl = [rand_c(rng) for _ in range(n)]
        zr = [rand_c(rng) for _ in range(n)]
        q, lam = rand_c(rng), rand_c(rng)
        conf = zr + [1 / (q * z) for z in zl]
        conf_seam = [lam * z for z in zr] + [1 / (q * z / lam) for z in zl]
        ok &= all(sp.simplify(x - y) == 0 for x, y in zip(cross_ratios(conf), cross_ratios(conf_seam)))
        conf_bad = zr + [1 / (q * z / lam) for z in zl]
        wrong &= all(sp.simplify(x - y) == 0 for x, y in zip(cross_ratios(conf), cross_ratios(conf_bad)))
    check("C2.2-seam", ok)
    break_leg("C2.2-seam", wrong)


# ---------------------------------------------------------------- C3


def c3_counts() -> None:
    check("C3.1-kinetic", all((2 * (n - 2) + 1 == 2 * n - 3) and ((1 == 2 * n - 3) == (n == 2)) for n in range(1, 9)))
    break_leg("C3.1-kinetic", all(2 * (n - 3) + 1 == 2 * n - 3 for n in range(1, 9)))
    vs = sp.symbols("V3:9", integer=True, nonnegative=True)
    n_sym = sum((k - 2) * v for k, v in zip(range(3, 9), vs)) + 2  # N from (3.2)
    moduli = sum((k - 3) * v for k, v in zip(range(3, 9), vs)) + sum(vs) - 1
    check("C3.2-tree-formula", sp.expand(moduli - (n_sym - 3)) == 0)
    ok, wrong, count = True, True, 0
    for n in (4, 6, 8):
        for vk in valence_vectors(n):
            count += 1
            ok &= tree_moduli(vk, lambda k: k - 3) == n - 3
            wrong &= tree_moduli(vk, lambda k: k - 2) == n - 3
    print(f"      valence vectors enumerated (N=4,6,8): {count}")
    check("C3.2-enumeration", ok and count == len(valence_vectors(4)) + len(valence_vectors(6)) + len(valence_vectors(8)))
    break_leg("C3.2-enumeration", wrong)
    per_leg = lambda n: n - 1
    ok = all(sum(per_leg(x) for x in abc) == sum(abc) - 3 for abc in itertools.product(range(1, 7), repeat=3) if sum(abc) <= 8)
    check("C3.3-trinion", ok)
    break_leg("C3.3-trinion", all(sum(x - 2 for x in abc) == sum(abc) - 3 for abc in itertools.product(range(1, 7), repeat=3) if sum(abc) <= 8))


# ---------------------------------------------------------------- C4


def c4_ghost() -> None:
    check("C4.1-dressed", all(2 * n - 2 * (n - 2) == 4 for n in range(1, 9)))
    break_leg("C4.1-dressed", all(2 * n - 2 * (n - 1) == 4 for n in range(2, 9)))
    check("C4.2-pairing", 4 + 4 - 2 == 6 and 2 + 2 + 2 == 6)
    # break: undressed 3-patch states (ghost number 6 each) glued by b_0^+ b_0^- miss the anomaly
    break_leg("C4.2-pairing", (2 * 3) + (2 * 3) - 2 == 6)
    ok = all(2 * (n - 2) + 2 * (n - 2) + 2 == 4 * n - 6 == (4 * n) - 6 for n in range(2, 9))
    ok &= all(sum(2 * (x - 1) for x in abc) == 2 * sum(abc) - 6 for abc in itertools.product(range(1, 7), repeat=3) if sum(abc) <= 8)
    check("C4.3-S6", ok)
    break_leg("C4.3-S6", all(sum(2 * (x - 2) for x in abc) == 2 * sum(abc) - 6 for abc in itertools.product(range(1, 7), repeat=3) if sum(abc) <= 8))
    ok, wrong = True, True
    for n1, n2, k in itertools.product(range(3, 9), range(3, 9), (2, 3)):
        if n1 < k + 1 or n2 < k + 1:
            continue
        n_tot = n1 + n2 - 2 * k
        ok &= (n1 - 3) + (n2 - 3) - (2 * k - 3) == n_tot - 3
        ok &= 2 * (n1 - 3) + 2 * (n2 - 3) - (4 * k - 6) == 2 * n_tot - 6
        wrong &= (n1 - 3) + (n2 - 3) - 1 == n_tot - 3
    check("C4.4-sigma-edge", ok)
    break_leg("C4.4-sigma-edge", wrong)


# ---------------------------------------------------------------- C5



def c5_limits() -> None:
    n = 1
    check("C5.1-n1", (2 * n + 1 - 4 == -1) and (2 * (n - 2) + 1 == 2 * n - 3) and (2 * n - 2 * (n - 2) == 4))
    break_leg("C5.1-n1", 2 * n - 2 * (n - 2) == 2)
    ok, wrong = True, True
    for n_ext in (4, 6):
        # trees of patches / pants / symmetric vertices
        for vk in valence_vectors(n_ext):
            ok &= tree_moduli(vk, lambda k: k - 3) == n_ext - 3
        # composites V_{N1} p_{2,2}^{-1} V_{N2}: moduli (N1-3)+(N2-3)-1, no gluing edge
        for n1 in range(4, n_ext + 1):
            n2 = n_ext + 4 - n1
            if n2 < 4:
                continue
            ok &= (n1 - 3) + (n2 - 3) - 1 == n_ext - 3
            wrong &= (n1 - 3) + (n2 - 3) + 0 == n_ext - 3
    # the explicit table (5.1)
    table = {
        "V4": 1, "V3-V3": 0 + 0 + 1, "p22(Psi2,Psi2)": 0 + 1 + 0, "p22 p22^-1 p22": 1 + 1 - 1,
        "V6": 3, "V4-V3-V3": 1 + 2, "V3^4": 3, "p33(Psi3,Psi3)": 1 + 1 + 1, "pants+3V3'": 3, "V5 p22^-1 V5": 2 + 2 - 1,
    }
    ok &= all(v == (1 if k in ("V4", "V3-V3", "p22(Psi2,Psi2)", "p22 p22^-1 p22") else 3) for k, v in table.items())
    check("C5.3-hs-trees", ok)
    break_leg("C5.3-hs-trees", wrong)


def main() -> int:
    """Run all checks; return nonzero on failure."""
    print(f"seed: {SEED}")
    rng = random.Random(SEED)
    c1_trees()
    c2_redundancy(rng)
    c3_counts()
    c4_ghost()
    c5_limits()
    n_fail = sum(1 for _, ok in CHECKS if not ok) + sum(1 for _, ok in BREAKS if not ok)
    print(f"summary: {len(CHECKS) + len(BREAKS) - n_fail}/{len(CHECKS) + len(BREAKS)} PASS ({len(CHECKS)} checks + {len(BREAKS)} break legs)")
    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(main())
