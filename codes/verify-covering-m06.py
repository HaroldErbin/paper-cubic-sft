r"""
Verify derivation 036: what the Sigma-composite covers in M_{0,6}.

Every check is tagged BOOKKEEPING or FALSIFIABLE and the summary reports the split.

    BOOKKEEPING = a transcription of hand-entered data, or an algebraic identity that
    holds for any input (a Moore-Penrose axiom, a linear identity in the loop
    variables).  It tests the typist or sympy, not the physics, and no wrong physical
    result could make it fail.

    FALSIFIABLE = a definite wrong statement of the record (a wrong formula, coefficient,
    sign or list) would make it fail with the script's inputs.  A leg whose assertion is
    an arithmetic restatement of another check's assertion on the same numbers, or an
    identity valid for any input, is BOOKKEEPING even when it is called a break leg
    (second fix pass, 2026-09-21: C1.5-genus-break, C1.6-bound-break, C2.6-break,
    C2.6-irred-break demoted on that criterion; split 24 falsifiable / 11 bookkeeping).

What is verified
----------------
C1.1  [BOOKKEEPING] Genus-0 anomaly identity S - n_b + n_c = 6 on a 9-row hand-entered
      table of elementary objects (V_n, omega_1, Q_B, P, the k=1 and k=3 kinetic
      surfaces).  The rows are inputs written to satisfy the identity.
C1.4  [BOOKKEEPING] Harold's removal law R(k) = 4k-6: [(2a-6)+(2b-6)] - [2(a+b-2k)-6]
      equals 4k-6 identically in (a, b), one line of algebra.  The substance is R39's
      additivity and inverse lemma.
C1.5  [BOOKKEEPING] S_B = 6 + 6g - n_b + n_c substituted back into the conservation law
      it was derived from; both sides reduce to 12 - 6s identically.
C1.5-genus        [FALSIFIABLE] genus of the glued surface from an explicit cell
      structure (one 0-cell and 1-cell per boundary circle, l-1 arcs, 2g_i handle loops,
      one 2-cell per piece; gluing merges circle cells, capping adds 2-cells;
      g = (2 - chi)/2) against the connectivity law g = sum g_i + 2s - C - 1 (036 eq. 1.7),
      over all set partitions of the 2s sewing legs at s = 1, 2, 3, component genera 0, 1.
      Independent of the dual-graph Betti number E - V + 1 that the law is.
C1.5-genus-break  [BOOKKEEPING] the off-by-one law g = sum g_i + 2s - C and the
      superseded g = s - 1 (when C != s) disagree with the cell count, and the cell count
      with the glued 0-cells left unmerged gives g - s: all three are arithmetic
      consequences of C1.5-genus passing (law + 1 != law; 2s - C - 1 != s - 1 iff C != s;
      chi + 2s), so the leg cannot fail once C1.5-genus does.  Kept so that the
      perturbation runs quoted in the record are in the script.
C1.6-bound        [FALSIFIABLE] n_b^max two independent ways: the glued-moduli deficit
      dim_R M_{g,n} - sum_i dim_R M_{0,n_i} with g taken from the graph, versus the
      per-component count 2 real plumbing parameters per node plus the virtual
      dimension 6g_i - 6 + 2 l_i of each component.  Agreement tests the genus law.
C1.6-bound-break  [BOOKKEEPING] perturbing the virtual dimension to 6g_i - 6 + 3 l_i
      breaks the agreement: the perturbed count is the unperturbed one plus 2s, so
      this cannot fail once C1.6-bound passes.
C1.6              [FALSIFIABLE] enumeration over all leg distributions (connectivity and
      capped legs detected from the graph, not assumed), component genera 0, 1, 2:
      every solution of S_B = 8 at s = 2 has n_c = 0.
C1.6-list         [FALSIFIABLE] with genus-0 components and no capped leg the solutions
      are exactly (C, g, n_b) = (2, 1, 4) (double tube) and (1, 2, 10) (connected sewing
      sphere): no uniqueness.
C1.6-tower        [FALSIFIABLE] allowing handles in the sewing object adds one
      saturating configuration per genus, so the candidate list is infinite and only
      R28 (any genus) closes it.
C1.6-break-target [FALSIFIABLE] at S_B = 10 the same machinery does produce n_c > 0
      solutions: the n_c = 0 conclusion is a property of S_B = 8, not of the code.
C1.6-break-genus  [FALSIFIABLE] with the superseded g = s - 1 the solution set changes
      (the genus-2 pattern disappears): how the earlier version reached uniqueness.
C2.1  [BOOKKEEPING] V4 V4^+ V4 = V4 is a Moore-Penrose axiom; repeated over 200 draws.
C2.2-raw          [FALSIFIABLE] without R38's condition the five-point double collapse
      fails, over independent draws.
C2.2              [FALSIFIABLE] with V5 = Pi^T V5 Pi (R38's condition) it holds.
C2.3  [BOOKKEEPING] pinv(t A) = t^{-1} pinv(A) for any nonzero scalar.
C2.3-break        [BOOKKEEPING] the same identity with one V5 replaced by p_{2,2}.
C2.3-pole         [FALSIFIABLE] the composite v^T V4(tau)^+ v diverges like
      1/(tau - tau_0) at a zero tau_0 of det V4(tau) along a random pencil.
C2.3-pole-break   [FALSIFIABLE] with v orthogonal to the null vector at tau_0 the pole
      disappears and the same test reports no pole.
C2.6, C2.6-only, C2.6-irred, C2.6-residue  [FALSIFIABLE]; C2.6-break, C2.6-irred-break
      [BOOKKEEPING]
      Proposition 2.6 (converse of the collapse criterion): for slot vectors affine in V,
      u = u0 + V y, w = w0 + V z, the contraction u^T V^-1 w is a polynomial in the
      entries of V iff u0 = 0 or w0 = 0.  Symbolic at n = 2, 3: the remainder of
      u^T adj(V) w modulo det V is u0^T adj(V) w0 != 0 (C2.6); u0^T adj(V) w0 == 0
      identically forces u0 = 0 or w0 = 0 (C2.6-only); det of a generic symmetric
      matrix is irreducible at n = 2, 3, 4 (C2.6-irred, used only in a remark); numeric
      n = 4: the residue at det V = 0 along a pencil is (u0.N)(N.w0)/(N^T B N), the
      affine parts dropping out (C2.6-residue).  Bookkeeping legs: a pure source end
      gives remainder 0 and y^T w (C2.6-break: the identity V adj(V) = det V, valid for
      any input; it only shows `reduced` can return 0) and a block-diagonal determinant
      factors (C2.6-irred-break: a visible product, tests sympy's factoriser only).
C3.1  [BOOKKEEPING] 90/75 = 6/5 in exact rational arithmetic, on two integers from R19.
C3.2              [FALSIFIABLE] over random symmetric pencils V4(P2) = V4 + P2 B: at
      each real zero of det V4(P2) in the sampled window the contraction has a simple
      pole with the R39 (3) residue.  Same content as C2.3-pole on pencils in P2; the
      "region model finite there" clause of the earlier version was decorative and is
      gone.  Does not test that the actual det V4^(L) has a zero (H2a).
C3.2-break        [FALSIFIABLE] with v orthogonal to the null vector the pole test
      reports no pole (the break leg the record described but the script lacked).
C3.6              [FALSIFIABLE] a region touching a degeneration divisor in a cusp
      r < c (theta - theta0)^k has, at the level-phi term, the collar integral (3.6)
      c^{2h} delta^{2hk+1} / (2h (2hk+1)) with a simple pole at 2hk = -1, off the
      plumbing lattice P_I^2 = -(2/alpha')(N + Nbar - 2) iff 1/k is not an integer (k = 1
      lands on it, k = 2 does not; the lattice arithmetic is not checked here): quadrature (tanh-sinh after theta = e^{-x}) against the closed form, and the
      Richardson-extrapolated residue against c^{2h*}/(2h* 2k), k = 1, 2, 0.6.
C3.6-break        [FALSIFIABLE] the sector-type region (3.5) r < eps has residue 0 there
      (Proposition 3.5 at one term: poles on the lattice only): the extraction can
      report 'no pole'.
C4.1, C4.1-fixed, C4.1-break, C4.1-lower, C4.2  [FALSIFIABLE] scalar model
      phi^3+phi^4+phi^5+phi^6: integrating the auxiliary sigma out at tree level returns
      V_orig + lambda_5^2 phi^6/(600 lambda_4); lambda_6' = lambda_6 - (6/5)
      lambda_5^2/lambda_4 cancels it, theta = 1 does not, orders 3-5 are exact, and the
      phi^6 term decomposes into exchange + sextic with nothing else.

What is not verified
--------------------
Anything about the actual closed-string vertices; the BRST consistency of W_6 (R19
item 7); the geometric existence of a double-line theory (R30) and its exclusion (R33);
that a compact sub-region with the standard measure is entire in the momenta (035
Prop. 2.1, easy half, a prose argument -- the polynomial "region model" below is an
illustration of it, not evidence for it); that V5 p^-1 V5 is not a combination of V_6
invariants at the actual data (R19 (2); Proposition 2.6 is checked as an identity in the
data, C2.6); hypotheses H2a (a non-isotropic zero of det V4^(L)(P^2) off the plumbing
lattice) and H2b (C entire), both open, hand-off 16b; that a cusp-type region equals C
(residue matching on the zero locus, named and not done).
"""

from __future__ import annotations

import itertools
import sys

import numpy as np
import sympy as sp

SEED = 20260921
RTOL, ATOL = 1e-7, 1e-9
rng = np.random.default_rng(SEED)
print(f"seed = {SEED}   numeric tolerance: rtol = {RTOL}, atol = {ATOL}")
results: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, kind: str, note: str = "") -> None:
    """Record and print one named check; kind is 'B' (bookkeeping) or 'F' (falsifiable)."""
    results.append((name, ok, kind))
    tag = "BOOKKEEPING" if kind == "B" else "FALSIFIABLE"
    print(f"{'PASS' if ok else 'FAIL'}  [{tag}]  {name}  {note}")


def close(a, b) -> bool:
    """Compare to the module-wide tolerance."""
    return bool(np.allclose(a, b, rtol=RTOL, atol=ATOL))


# ---------------------------------------------------------------- C1.1
# (object, S, n_b, n_c) in the form reading on the reduced space H_0.
table = [
    ("V_3", 6, 0, 0),
    ("V_4", 8, 2, 0),
    ("V_5", 10, 4, 0),
    ("V_6", 12, 6, 0),
    ("omega_1 (c_0^-)", 5, 0, 1),
    ("Q_B form", 4, 0, 2),
    ("P form (b_0^+, twist b cancels c_0^-)", 6, 1, 1),
    ("V_2(Sigma_1,Sigma_1) k=1 (unstable: n_c=2, not n_b=4k-6)", 4, 0, 2),
    ("V_2k(Sigma_k,Sigma_k) k=3", 12, 6, 0),
]
ok = all(S - nb + nc == 6 for _, S, nb, nc in table)
check("C1.1", ok, "B", f"S - n_b + n_c = 6 on all {len(table)} hand-entered rows")

# ---------------------------------------------------------------- C1.4
ok = True
for a in range(2, 10):
    for b in range(2, 10):
        for k in range(1, min(a, b) + 1):
            src = (2 * a - 6) + (2 * b - 6)
            tgt = 2 * (a + b - 2 * k) - 6
            ok &= src - tgt == 4 * k - 6
            ok &= 4 * k - 6 == 2 * (2 * k) - 6  # = dim M_{0,2k}
check("C1.4", ok, "B", "R(k)=4k-6=dim M_{0,2k}, identically in (a,b)")

# ---------------------------------------------------------------- C1.5
# Substituting S_i = 6 + nb_i - nc_i and S_B = 6 + 6g - n_b + n_c into
# S_1+S_2-S_B-(nb_tot)+(nc_tot) leaves 12 - 6s on both sides: an identity.
sym = sp.symbols("s g nb nc nb1 nc1 nb2 nc2")
s_, g_, nb_, nc_, nb1, nc1, nb2, nc2 = sym
S1, S2 = 6 + nb1 - nc1, 6 + nb2 - nc2
SB_sym = 6 + 6 * g_ - nb_ + nc_
lhs = S1 + S2 - SB_sym - (nb1 + nb2 + nb_) + (nc1 + nc2 + nc_)
ok = sp.simplify(lhs - (6 - 6 * g_)) == 0
check("C1.5", ok, "B", "S_B = 6 + 6g - n_b + n_c is the conservation law rewritten")


# ------------------------------------------------- gluing patterns (C1.5-genus, C1.6)
def set_partitions(items: list) -> list[list[list]]:
    """All set partitions of a list (Bell number many)."""
    if not items:
        return [[]]
    first, rest = items[0], items[1:]
    out = []
    for part in set_partitions(rest):
        for i in range(len(part)):
            out.append(part[:i] + [[first, *part[i]]] + part[i + 1 :])
        out.append([[first], *part])
    return out


def patterns(s: int):
    """
    Sewing-object patterns: partitions of the 2s legs among components.

    A leg is labelled by the vertex piece it comes from, 0 or 1 (s legs each).  A
    pattern yields the number of components C, the leg counts l_i, whether the dual
    graph (2 vertex pieces + C components, one edge per leg) is connected, the first
    Betti number of that graph, and whether some component carries a single leg (a
    "cap": a state insertion, not a gluing).
    """
    legs = [(0, i) for i in range(s)] + [(1, i) for i in range(s)]
    seen = set()
    for part in set_partitions(legs):
        key = tuple(sorted(tuple(sorted(p, key=lambda x: x[0])) for p in part))
        if key in seen:
            continue
        seen.add(key)
        comps = [[leg[0] for leg in block] for block in part]
        C = len(comps)
        # connectivity of the bipartite multigraph on {piece0, piece1, comp_0..comp_{C-1}}
        adj = {("p", 0): set(), ("p", 1): set()}
        for j in range(C):
            adj[("c", j)] = set()
        for j, sides in enumerate(comps):
            for side in sides:
                adj[("p", side)].add(("c", j))
                adj[("c", j)].add(("p", side))
        stack, seen_v = [("p", 0)], {("p", 0)}
        while stack:
            u = stack.pop()
            for w in adj[u]:
                if w not in seen_v:
                    seen_v.add(w)
                    stack.append(w)
        connected = len(seen_v) == 2 + C
        V, E = 2 + C, 2 * s
        yield {
            "C": C,
            "legs": tuple(len(c) for c in comps),
            "connected": connected,
            "betti": E - V + 1,
            "capped": any(len(c) == 1 for c in comps),
        }


# C1.5-genus: genus of the glued surface from an explicit cell structure (Euler
# characteristic), independent of the dual-graph Betti number that the law (1.7) is.
# Each piece (a vertex sphere with e_j + s boundary circles, or a sewing component of
# genus g_i with l_i boundary circles) gets the CW structure: one 0-cell per boundary
# circle, one 1-cell per circle, l - 1 arcs joining consecutive circles, 2 g_i handle
# loops, and one 2-cell (the surface cut along the arcs and the handle loops is a disc).
# Gluing two circles identifies their 0-cell and their 1-cell; capping an external
# circle adds a 2-cell.  Then chi = V - E + F = 2 - 2g for the closed connected surface.


def genus_by_cells(legs: tuple[int, ...], gi: list[int], s: int, e1: int = 3, e2: int = 3,
                   identify_vertices: bool = True) -> int | None:
    """
    Genus of the glued closed surface from cell counts; None if 2 - chi is odd.

    Args:
        legs: number of sewing legs carried by each sewing component.
        gi: genus of each sewing component.
        s: number of strands (each vertex sphere carries s sewing legs).
        e1: external legs of the first vertex sphere.
        e2: external legs of the second vertex sphere.
        identify_vertices: set False to break the gluing on purpose (0-cells not merged).

    """
    pieces = [(0, e1 + s), (0, e2 + s)] + [(g, ell) for g, ell in zip(gi, legs, strict=True)]
    V = sum(ell for _, ell in pieces)
    E = sum(ell + (ell - 1) + 2 * g for g, ell in pieces)
    F = len(pieces)
    n_glue = 2 * s  # circle pairs identified
    V -= n_glue if identify_vertices else 0
    E -= n_glue
    F += e1 + e2  # cap the external circles
    chi = V - E + F
    return (2 - chi) // 2 if (2 - chi) % 2 == 0 else None


ok, ok_break_old, ok_break_off, ok_unglued, n_pat = True, True, True, True, 0
for s in (1, 2, 3):
    for pat in patterns(s):
        if not pat["connected"]:
            continue
        for gi in itertools.product((0, 1), repeat=pat["C"]):
            n_pat += 1
            g_cells = genus_by_cells(pat["legs"], list(gi), s)
            law = sum(gi) + 2 * s - pat["C"] - 1
            ok &= g_cells == law
            # the three legs below are arithmetic consequences of ok (bookkeeping)
            ok_break_off &= g_cells != law + 1  # off-by-one law fails everywhere
            if pat["C"] != s and all(x == 0 for x in gi):
                ok_break_old &= g_cells != s - 1  # superseded law fails when C != s
            # 0-cells of glued circles left unmerged: chi + 2s, genus law - s
            ok_unglued &= genus_by_cells(pat["legs"], list(gi), s, identify_vertices=False) == law - s
check("C1.5-genus", ok, "F",
      f"genus from an explicit cell structure (chi = V - E + F after gluing and capping) = law (1.7) on {n_pat} connected patterns, s = 1, 2, 3, component genera 0, 1")
check("C1.5-genus-break", ok_break_off and ok_break_old and ok_unglued, "B",
      "off-by-one law, superseded g = s - 1 (C != s) and unmerged 0-cells (g - s) all disagree with the cell count: arithmetic given C1.5-genus")


def nb_max_glued(g: int, s: int, e1: int = 3, e2: int = 3) -> int:
    """dim_R M_{g,e1+e2} minus the two vertex families dim_R M_{0,e_i+s}."""
    dim = lambda gg, n: 6 * gg - 6 + 2 * n  # noqa: E731  dim_R M_{g,n}
    return dim(g, e1 + e2) - dim(0, e1 + s) - dim(0, e2 + s)


def nb_max_components(legs: tuple[int, ...], gi: list[int], virt_coeff: int = 2) -> int:
    """Count 2 real plumbing parameters per node, plus each component's virtual dimension."""
    return sum(2 * ell + (6 * gg - 6 + virt_coeff * ell) for ell, gg in zip(legs, gi, strict=True))


# C1.6-bound: the two routes agree (which tests the genus law feeding route (a))
ok, ok_break, n_tested = True, False, 0
for s in (1, 2, 3):
    for pat in patterns(s):
        if not pat["connected"]:
            continue
        for gi in itertools.product((0, 1), repeat=pat["C"]):
            g = sum(gi) + 2 * s - pat["C"] - 1
            for e1, e2 in ((3, 3), (2, 4), (4, 5)):
                n_tested += 1
                a = nb_max_glued(g, s, e1, e2)
                b = nb_max_components(pat["legs"], list(gi))
                ok &= a == b
                if a != nb_max_components(pat["legs"], list(gi), virt_coeff=3):
                    ok_break = True
check("C1.6-bound", ok, "F", f"n_b^max: glued deficit = per-component count, {n_tested} cases")
check("C1.6-bound-break", ok_break, "B",
      "perturbed virtual dimension (2 l_i -> 3 l_i) disagrees: it is the unperturbed count + 2s, arithmetic given C1.6-bound")


def solutions(target_SB: int, s: int = 2, genus_law: str = "connectivity",
              genera: tuple[int, ...] = (0, 1)) -> list[dict]:
    """
    All geometric sewing objects with S_B = target_SB, enumerated over patterns.

    S_B = 6 + 6g - n_b + n_c  (036 eq. 1.5), 0 <= n_b <= n_b^max (eq. 1.8), n_c >= 0.
    genus_law = "connectivity" uses g = sum g_i + 2s - C - 1; "old" uses the superseded
    g = s - 1 that the first version of this record assumed.
    """
    sols = []
    for pat in patterns(s):
        if not pat["connected"]:
            continue
        for gi in itertools.product(genera, repeat=pat["C"]):
            g = sum(gi) + 2 * s - pat["C"] - 1 if genus_law == "connectivity" else s - 1
            nbmax = nb_max_glued(g, s)
            if nbmax < 0:
                continue  # more b-insertions than moduli: the form vanishes
            for nb in range(nbmax + 1):
                for nc in range(13):
                    if 6 + 6 * g - nb + nc == target_SB:
                        sols.append({"C": pat["C"], "legs": pat["legs"], "g": g,
                                     "nb": nb, "nc": nc, "capped": pat["capped"]})
    return sols


sols = solutions(8, genera=(0, 1, 2))
check("C1.6", all(d["nc"] == 0 for d in sols), "F",
      f"S_B=8: every one of the {len(sols)} solutions has n_c=0, at every connectivity and component genus")
sols0 = solutions(8, genera=(0,))
capless = sorted({(d["C"], d["g"], d["nb"]) for d in sols0 if not d["capped"]})
check("C1.6-list", capless == [(1, 2, 10), (2, 1, 4)], "F",
      f"genus-0 components, no capped leg: capless (C,g,n_b) = {capless}")
capless_any = sorted({(d["C"], d["g"], d["nb"]) for d in sols if not d["capped"]})
check("C1.6-tower", len(capless_any) > len(capless), "F",
      f"allowing handles in the sewing object adds one saturating configuration per genus: {capless_any} "
      "-- the list is infinite and only R28 (any genus) closes it")

sols10 = solutions(10)
check("C1.6-break-target", any(d["nc"] > 0 for d in sols10), "F",
      f"S_B=10 does admit c-insertions: {sorted({(d['C'], d['g'], d['nb'], d['nc']) for d in sols10})[:4]} ...")

sols_old = solutions(8, genus_law="old")
capless_old = sorted({(d["C"], d["g"], d["nb"]) for d in sols_old if not d["capped"]})
check("C1.6-break-genus", capless_old != capless, "F",
      f"superseded genus law gives capless {capless_old} (genus-2 pattern lost)")

# ---------------------------------------------------------------- C2.x
n = 4  # dim Sym^2 (toy)


def rand_sym(k: int, rank: int | None = None) -> np.ndarray:
    """Draw a random real symmetric k x k matrix, optionally of reduced rank."""
    # real symmetric: the quotient inverse is bilinear (BPZ-type), not Hermitian, so a
    # complex-symmetric draw with numpy's Hermitian pinv would be inconsistent (see
    # 036 §5.2: the model sidesteps the kernel/range obstruction of the real case).
    A = rng.normal(size=(k, k))
    A = A + A.T
    if rank is not None:
        U, s_, Vh = np.linalg.svd(A)
        s_[rank:] = 0
        A = (U * s_) @ Vh
        A = (A + A.T) / 2
    return A


ok = True
for _ in range(200):
    A = rand_sym(n, rank=n - 1)
    Pa = np.linalg.pinv(A)
    x = rng.normal(size=n) + 1j * rng.normal(size=n)
    y = rng.normal(size=n) + 1j * rng.normal(size=n)
    ok &= close((A @ x) @ Pa @ (A @ y), x @ A @ y)
check("C2.1", ok, "B", "V4 V4^+ V4 = V4 (Moore-Penrose axiom), 200 draws")

ok_raw, ok_r38 = True, True
for _ in range(50):
    V4 = rand_sym(n, rank=n - 1)  # p_{2,2} with a one-dimensional kernel
    p_inv = np.linalg.pinv(V4)
    Pi = V4 @ p_inv  # projector onto the range of p_{2,2}
    x = rng.normal(size=n) + 1j * rng.normal(size=n)
    y = rng.normal(size=n) + 1j * rng.normal(size=n)
    V5_raw = rand_sym(n)
    ok_raw &= not close((V4 @ x) @ p_inv @ V5_raw @ p_inv @ (V4 @ y), x @ V5_raw @ y)
    V5 = Pi.T @ V5_raw @ Pi  # R38-compatible V5: vanishes on ker p_{2,2}
    ok_r38 &= close((V4 @ x) @ p_inv @ V5 @ p_inv @ (V4 @ y), x @ V5 @ y)
check("C2.2-raw", ok_raw, "F", "without R38 (V5 not vanishing on ker p) the double collapse FAILS, 50 draws")
check("C2.2", ok_r38, "F", "V4 p^-1 V5 p^-1 V4 = V5 with R38-compatible V5, 50 draws")

V4 = rand_sym(n, rank=n - 1)
p_inv = np.linalg.pinv(V4)
x = rng.normal(size=n) + 1j * rng.normal(size=n)
V5 = rand_sym(n)
v = V5 @ x
t1, t2 = 1.7 + 0.3j, -0.6 + 1.1j
comp = lambda t: v @ np.linalg.pinv(t * V4) @ v  # noqa: E731
ok = close(comp(t1) * t1, comp(t2) * t2) and not close(comp(t1), comp(t2))
check("C2.3", ok, "B", "pinv(tA) = t^-1 pinv(A): degree -1 is an identity, not a test")
comp_break = lambda t: (t * V4 @ x) @ np.linalg.pinv(t * V4) @ v  # noqa: E731
check("C2.3-break", close(comp_break(t1), comp_break(t2)), "B",
      "same identity with one V5 -> p_{2,2}: degree 0")


def pencil_zero(A: np.ndarray, B: np.ndarray) -> tuple[float, np.ndarray] | None:
    """Return a real tau_0 with det(A + tau_0 B) = 0, and the null vector there."""
    taus = -np.linalg.eigvals(np.linalg.solve(B, A))
    real = [t.real for t in taus if abs(t.imag) < 1e-9]
    if not real:
        return None
    tau0 = float(real[0])
    M0 = A + tau0 * B
    w, U = np.linalg.eigh(M0)
    return tau0, U[:, int(np.argmin(np.abs(w)))]


def pole_strength(A, B, v, tau0) -> float:
    """
    Ratio of |v^T (A+tau B)^-1 v| at distances 1e-3 and 1e-6 from tau0.

    ~1000 for a simple pole, ~1 for a regular point.  Used for the break legs, where
    only the absence of growth has to be detected.
    """
    f = lambda d: abs(v @ np.linalg.pinv(A + (tau0 + d) * B) @ v)  # noqa: E731
    return f(1e-6) / f(1e-3)


def residues(A, B, v, tau0, u, d: float = 1e-7) -> tuple[float, float]:
    """
    Numerical and analytic residue of v^T (A + tau B)^-1 v at a simple zero tau_0.

    Numerical: d * v^T (A + (tau_0+d) B)^-1 v as d -> 0, Richardson-extrapolated over
    d and 2d to remove the linear contribution of the regular part.
    Analytic: for a real symmetric pencil with simple null vector u at tau_0,
    (A + tau B)^-1 = u u^T / [(tau - tau_0) u^T B u] + regular, so the residue is
    (v.u)^2 / (u^T B u).  The two are computed by independent routes; a regular
    point gives 0 for the first and the second is then the falsifier.
    """
    f = lambda dd: dd * (v @ np.linalg.pinv(A + (tau0 + dd) * B) @ v)  # noqa: E731
    num = 2 * f(d) - f(2 * d)  # Richardson: f(d) = R + d * (regular part) + O(d^2)
    ana = (v @ u) ** 2 / (u @ B @ u)
    return float(num), float(ana)


# C2.3-pole: the composite v^T V4(tau)^+ v really has the pole, on the actual structure
ok, ok_break, n_draw = True, True, 0
for _ in range(20):
    A, B = rand_sym(n), rand_sym(n)
    z = pencil_zero(A, B)
    if z is None:
        continue
    tau0, u = z
    vv = rand_sym(n) @ (rng.normal(size=n))  # v = V5 x, the composite's structure
    num, ana = residues(A, B, vv, tau0, u)
    if abs(ana) < 1e-6:  # v accidentally almost orthogonal to u: no pole to detect
        continue
    n_draw += 1
    ok &= abs(num - ana) <= 1e-3 * abs(ana)
    v_perp = vv - u * (u @ vv)  # orthogonal to the null vector: residue vanishes
    ok_break &= pole_strength(A, B, v_perp, tau0) < 10
check("C2.3-pole", ok and n_draw >= 5, "F",
      f"residue of v^T V4(tau)^+ v at det V4 = 0 matches (v.u)^2/(u^T B u), {n_draw} pencils")
check("C2.3-pole-break", ok_break and n_draw >= 5, "F",
      "v orthogonal to the null vector: no pole, and the test reports none")

# ---------------------------------------------------------------- C2.6 (converse)
# Proposition 2.6: for ends u = u0 + V y, w = w0 + V z (affine in V), u^T V^-1 w is a
# polynomial in the entries of V iff u0 = 0 or w0 = 0.  The proof is a degree count:
# u0^T adj(V) w0 has degree n-1 < n = deg det V.  Checked symbolically at n = 2, 3 by
# polynomial reduction modulo det V, with the pure-source end as the break leg.


def sym_matrix(k: int) -> sp.Matrix:
    """Build a generic symmetric k x k matrix with independent symbolic entries."""
    M = sp.zeros(k, k)
    for i in range(k):
        for j in range(i, k):
            M[i, j] = M[j, i] = sp.Symbol(f"V{i}{j}")
    return M


ok_irred, ok_irred_break = True, False
for k in (2, 3, 4):
    M = sym_matrix(k)
    _, factors = sp.factor_list(M.det())
    ok_irred &= len(factors) == 1 and factors[0][1] == 1
    # break leg: a block-diagonal symmetric matrix has a reducible determinant
    Mb = sp.diag(sym_matrix(1), sym_matrix(k - 1)) if k > 2 else sp.diag(sp.Symbol("a"), sp.Symbol("b"))
    _, fb = sp.factor_list(Mb.det())
    ok_irred_break |= len(fb) > 1
check("C2.6-irred", ok_irred, "F", "det of a generic symmetric matrix is irreducible at n = 2, 3, 4")
check("C2.6-irred-break", ok_irred_break, "B",
      "block-diagonal symmetric det factors (a visible product): tests sympy's factoriser only")

ok_gen, ok_src, ok_only = True, True, True
for k in (2, 3):
    M = sym_matrix(k)
    gens = sorted(M.free_symbols, key=str)
    d = M.det()
    u0 = sp.Matrix(sp.symbols(f"u0:{k}"))
    w0 = sp.Matrix(sp.symbols(f"w0:{k}"))
    y = sp.Matrix(sp.symbols(f"y0:{k}"))
    z = sp.Matrix(sp.symbols(f"z0:{k}"))
    # generic affine ends: numerator of u^T V^-1 w is u^T adj(V) w; polynomial iff det | it
    u, w = u0 + M * y, w0 + M * z
    num = sp.expand((u.T * M.adjugate() * w)[0])
    _, rem = sp.reduced(num, [d], *gens)
    ok_gen &= sp.expand(rem) != 0
    # the remainder must be exactly the u0-w0 part (the affine parts are polynomial)
    ok_gen &= sp.expand(rem - (u0.T * M.adjugate() * w0)[0]) == 0
    # break leg = the "if" direction: a pure source end u = V y gives remainder 0
    us = M * y
    nums = sp.expand((us.T * M.adjugate() * w)[0])
    _, rems = sp.reduced(nums, [d], *gens)
    ok_src &= sp.expand(rems) == 0
    ok_src &= sp.expand(sp.cancel((us.T * M.inv() * w)[0]) - (y.T * w)[0]) == 0
    # "only if": u0^T adj(V) w0 == 0 identically in V forces u0 = 0 or w0 = 0
    N = sp.Poly((u0.T * M.adjugate() * w0)[0], *gens)
    sols = sp.solve(N.coeffs(), list(u0) + list(w0), dict=True)
    ok_only &= all(all(s.get(ui, ui) == 0 for ui in u0) or all(s.get(wi, wi) == 0 for wi in w0)
                   for s in sols)
check("C2.6", ok_gen, "F",
      "affine ends: u^T adj(V) w mod det V = u0^T adj(V) w0 != 0 (n = 2, 3), so u^T V^-1 w is not polynomial")
check("C2.6-break", ok_src, "B",
      "pure source end u = V y: remainder 0 and u^T V^-1 w = y^T w (the identity V adj V = det V, valid for any input; shows `reduced` can return 0)")
check("C2.6-only", ok_only, "F",
      "u0^T adj(V) w0 == 0 identically forces u0 = 0 or w0 = 0 (n = 2, 3, sympy solve on the coefficients)")

# numeric counterpart at n = 4 along a pencil: the residue at det V(tau) = 0 depends on
# u0, w0 only -- the affine parts V y, V z of the ends drop out of the residue.
ok_res, n_draw = True, 0
for _ in range(20):
    A, B = rand_sym(n), rand_sym(n)
    zz = pencil_zero(A, B)
    if zz is None:
        continue
    tau0, uu = zz
    u0v, w0v, yv, zv = (rng.normal(size=n) for _ in range(4))
    def f(dd, A=A, B=B, tau0=tau0, u0v=u0v, w0v=w0v, yv=yv, zv=zv):
        """Return dd times the affine-end contraction at tau0 + dd (residue extraction)."""
        Vd = A + (tau0 + dd) * B
        return dd * ((u0v + Vd @ yv) @ np.linalg.pinv(Vd) @ (w0v + Vd @ zv))

    num = 2 * f(1e-7) - f(2e-7)
    ana = (u0v @ uu) * (uu @ w0v) / (uu @ B @ uu)
    if abs(ana) < 1e-6:
        continue
    n_draw += 1
    ok_res &= abs(num - ana) <= 1e-3 * abs(ana)
check("C2.6-residue", ok_res and n_draw >= 5, "F",
      f"affine ends, n = 4: residue at det V = 0 equals (u0.N)(N.w0)/(N^T B N), affine parts drop out, {n_draw} pencils")

# ---------------------------------------------------------------- C3.1
check("C3.1", sp.Rational(90, 75) == sp.Rational(6, 5), "B", "90/75 = 6/5 (R19 Wick count, two integers)")

# ---------------------------------------------------------------- C3.2
# Random pencils V4(P2) = V4 + P2 B in a sampled window, region model = polynomial.
ok, ok_break, n_draw, n_skip = True, True, 0, 0
for _ in range(20):
    A, B = rand_sym(n), rand_sym(n)
    z = pencil_zero(A, B)
    if z is None or abs(z[0]) > 10.0:  # no zero in the sampled window |P2| <= 10
        n_skip += 1
        continue
    tau0, u = z
    vv = rng.normal(size=n)
    num, ana = residues(A, B, vv, tau0, u)
    if abs(ana) < 1e-6:
        n_skip += 1
        continue
    n_draw += 1
    ok &= abs(num - ana) <= 1e-3 * abs(ana)
    v_perp = vv - u * (u @ vv)
    ok_break &= pole_strength(A, B, v_perp, tau0) < 10
check("C3.2", ok and n_draw >= 5, "F",
      f"pole of v V4(P2)^-1 v at det V4 = 0 with the R39 (3) residue; {n_draw} pencils, {n_skip} skipped")
check("C3.2-break", ok_break and n_draw >= 5, "F",
      "rigged v (orthogonal to the null vector): the pole test correctly reports no pole")

# ---------------------------------------------------------------- C3.6 (cusp regions)
# A region touching the degeneration divisor in a cusp r < c (theta - theta0)^k has, at
# the level-phi term, the integral (3.6) c^{2h} delta^{2hk+1} / (2h (2hk+1)): a pole at
# 2hk = -1, off every mass shell.  A sector-type region (3.5) has only the pole h = 0.
# The angular integral is done by tanh-sinh quadrature (mpmath), the radial one by its
# analytic continuation eps^{2h}/(2h); the closed form is the independent route.
import mpmath as mp  # noqa: E402

mp.mp.dps = 30


def cusp_integral(h: float, k: float, c: float = 0.7, delta: float = 0.9) -> float:
    """
    Level-phi collar integral over the cusp region, angular part by quadrature.

    The substitution theta = e^{-x} moves the near-non-integrable endpoint theta^{2hk}
    (2hk close to -1) to a slowly decaying exponential on [-ln delta, inf), which
    tanh-sinh integrates to machine precision; on [0, delta] directly it lost 4-60 %.
    """
    return float(mp.quad(lambda x: (c * mp.e ** (-k * x)) ** (2 * h) * mp.e ** (-x) / (2 * h),
                         [-mp.log(delta), mp.inf]))


def cusp_closed(h: float, k: float, c: float = 0.7, delta: float = 0.9) -> float:
    """Evaluate the closed form (3.6) of the cusp integral."""
    return float(c ** (2 * h) * delta ** (2 * h * k + 1) / (2 * h * (2 * h * k + 1)))


def sector_integral(h: float, eps: float = 0.7, delta: float = 0.9) -> float:
    """Level-phi collar integral over a sector r < eps, theta in [0, delta], eq. (3.5)."""
    return float(mp.quad(lambda th: eps ** (2 * h) / (2 * h), [0, delta]))


def residue_in_h(f, h_star: float, eta: float = 1e-3) -> float:
    """Richardson-extrapolated residue of f at h_star: 2 eta f(h*+eta) - 2 eta f(h*+2 eta)."""
    return 2 * eta * f(h_star + eta) - 2 * eta * f(h_star + 2 * eta)


ok_cusp, ok_sector = True, True
for k in (1.0, 2.0, 0.6):
    h_star = -1 / (2 * k)
    for eta in (5e-2, 1e-2):
        hq = h_star + eta
        ok_cusp &= abs(cusp_integral(hq, k) - cusp_closed(hq, k)) <= 1e-10 * abs(cusp_closed(hq, k))
    res_ana = 0.7 ** (2 * h_star) / (2 * h_star * 2 * k)  # residue of (3.6) in h at 2hk = -1
    res_num = residue_in_h(lambda h, k=k: cusp_integral(h, k), h_star)
    ok_cusp &= abs(res_num - res_ana) <= 1e-4 * abs(res_ana)  # Richardson leaves O(eta^2)
    ok_sector &= abs(residue_in_h(sector_integral, h_star)) <= 1e-4 * abs(res_ana)
check("C3.6", ok_cusp, "F",
      "cusp region r < c theta^k: quadrature matches (3.6) to 1e-10 and the residue at 2hk = -1 matches, k = 1, 2, 0.6")
check("C3.6-break", ok_sector, "F",
      "sector region (3.5): the same residue extraction gives 0 at 2hk = -1 (no pole; only h = 0)")

# ---------------------------------------------------------------- C4.x
phi, sig, l3, l4, l5, l6 = sp.symbols("phi sigma lambda3 lambda4 lambda5 lambda6")
V_orig = l3 * phi**3 / 6 + l4 * phi**4 / 24 + l5 * phi**5 / 120 + l6 * phi**6 / 720


def V_cubic(l6p: sp.Expr) -> sp.Expr:
    """Build the cubic (Hubbard-Stratonovich) potential with sextic coupling l6p."""
    # HS: l4 phi^4/4! -> l4 (2 sigma phi^2 - sigma^2)/4!; phi^5 -> sigma^2 phi; phi^6 -> sigma^3
    return (l3 * phi**3 / 6 + l4 * (2 * sig * phi**2 - sig**2) / 24
            + l5 * sig**2 * phi / 120 + l6p * sig**3 / 720)


def integrate_out(V: sp.Expr, order: int = 7) -> sp.Expr:
    """Integrate sigma out at tree level and return the effective potential in phi."""
    # tree level: solve dV/dsigma = 0 as a series sigma = phi^2 + sum_{m>=3} c_m phi^m
    cs = sp.symbols(f"c3:{order}")
    ans = phi**2 + sum(c * phi ** (i + 3) for i, c in enumerate(cs))
    eq = sp.expand(sp.diff(V, sig).subs(sig, ans))
    sol: dict = {}
    for m in range(3, order):
        coeff = sp.expand(eq.coeff(phi, m)).subs(sol)  # c_m enters dV/dsigma linearly at phi^m
        sol[cs[m - 3]] = sp.solve(coeff, cs[m - 3])[0]
    ans = ans.subs(sol)
    return sp.series(sp.expand(V.subs(sig, ans)), phi, 0, order).removeO()


Veff = integrate_out(V_cubic(l6))
diff6 = sp.simplify(sp.expand(Veff - V_orig).coeff(phi, 6))
check("C4.1", sp.simplify(diff6 - l5**2 / (600 * l4)) == 0, "F", f"feedback at phi^6 = {diff6}")
Veff_fixed = integrate_out(V_cubic(l6 - sp.Rational(6, 5) * l5**2 / l4))
check("C4.1-fixed", sp.simplify(sp.expand(Veff_fixed - V_orig).coeff(phi, 6)) == 0, "F",
      "lambda6' = lambda6 - 6/5 lambda5^2/lambda4 cancels the phi^6 feedback")
Veff_break = integrate_out(V_cubic(l6 - 1 * l5**2 / l4))
check("C4.1-break", sp.simplify(sp.expand(Veff_break - V_orig).coeff(phi, 6)) != 0, "F",
      "theta = 1 leaves a residual")
ok = all(sp.simplify(sp.expand(Veff_fixed - V_orig).coeff(phi, m)) == 0 for m in range(3, 6))
check("C4.1-lower", ok, "F", "phi^3..phi^5 reproduced exactly")

# C4.2: diagrammatic decomposition of the momentum-independent 6-point contact term.
# sigma propagator (l4/12)^{-1}, source vertex l4 phi^2 sigma/12, quintic l5 sigma^2 phi/120.
# The sigma-exchange class = terms quadratic in l5; the sextic class = terms linear in l6'.
c6 = sp.expand(Veff).coeff(phi, 6)
exch = c6.coeff(l5, 2) * l5**2
sext = c6.coeff(l6, 1) * l6
check("C4.2", sp.simplify(exch - sp.Rational(6, 5) * l5**2 / l4 / 720) == 0
      and sp.simplify(sext - l6 / 720) == 0 and sp.simplify(c6 - exch - sext) == 0, "F",
      "phi^6/6!: exchange = (6/5) l5^2/l4, sextic = l6, nothing else")

nfail = sum(not ok for _, ok, _ in results)
nfals = sum(1 for _, _, k in results if k == "F")
print(f"summary: {len(results) - nfail}/{len(results)} PASS "
      f"({nfals} falsifiable, {len(results) - nfals} bookkeeping)")
sys.exit(1 if nfail else 0)
