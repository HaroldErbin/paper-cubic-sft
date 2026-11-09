#!/usr/bin/env python3
"""
Machine checks for derivation 035 (Task 16a).

verify-negative-moduli.py -- machine checks for derivation 035 (Task 16a):
the negative-moduli calculus and the momentum-analyticity falsifier for the
sextic composite C = V5 . V4^{-1} . V5 (derivation 013).

Part 1 (claim C1): the formal dimension
    d_hat(form) = S - 6,   d_hat_B(bivector) = 6 - S_B,
    d_hat(map)  = 5 l - 6 - gamma,   d_hat_B = 6 - 5 l - gamma           (035 eq. 1.7)
computed from insertion counts (n_b, n_c, genus, strands; 035 eqs. 1.2, 1.5)
agrees with the affine image of the map ghost number gamma on all 17 rows of
the N_gh table of derivation 030 section 1.3 (C1.2); the inverse lemma
S_B(Omega^{-1}) = S(Omega) on random graded symmetric matrices (C1.1); the
closure sums at 4, 5, 6 points (C1.3); break-on-purpose (wrong affine
constant must fail).  C1.2, C1.3 and C2.4 are transcription checks, not
independent evidence: (1.7) is an affine rearrangement of the same data.
C1.1 is a genuine test of the block-support statement.

Part 2 (claim C2): two different counts, which the first version of this
script conflated.  C2.3a is the Wick count -- 90 labelled strand assignments,
combinatorial stabiliser 8 -- obtained by enumerating labelled assignments
without ever evaluating the kernel.  C2.3b is the symmetry of the kernel:
the stabiliser of C_sigma *as a function* on Psi^{(x)6}, obtained by permuting
a fixed sextuple of random states through all of S6, is (S3 x S3) x| Z2 of
order 72 (035 eq. 2.6), because V5 is totally symmetric; hence 720/72 = 10
distinct (3|3) terms and 90 = 10 x 9.  Also the scaling degree of the
composite, C(t V4, u V5) = u^2 t^{-1} C (C2.4), in the finite-dimensional
model of verify-b3-sextic.py.

Part 3 (claim C3): momentum toy.  V4(P) a symmetric matrix polynomial in a
complex scalar P with a zero of det at P0 (kernel N of dimension 1 or 2),
V5(P) a generic totally symmetric 5-tensor polynomial in P; the composite
C(P) = v(P)^T V4(P)^{-1} v(P), v = V5(., Psi Psi, Psi) (013 diagonal form) and
the full polarised form C(A, B, Z).  Checks: the residue at P0 obtained by a
numerical contour integral equals the Laurent prediction
    Res = v0^T N (N^T M1 N)^{-1} N^T v0,   M1 = V4'(P0)          (035 eq. 3.3)
(C3.1-C3.2); the pole survives on generic V5 (C3.3); it is removed when the
R38 condition Pi_N V5(P0)[:, :, a] = 0 holds at P0 (C3.4); it reappears, with
residue O(eps^2), when the null direction is sourced (C3.5, break-on-purpose).
C3.6 (dim N = 2 only) tests the converse, which is false: the exact condition
is that W(P0) = {N^T V5(., A, z)} be totally isotropic for (N^T M1 N)^{-1}
(035 eq. 2.4'), so imposing R38 for a single null direction chosen to leave W
on the isotropic line gives a vanishing residue with Pi_N V5(P0) != 0.  Its
break leg runs the same construction with a non-isotropic direction.

Not verified here: anything about the infinite-dimensional theory (the
internal momentum integral of the Sigma pair, convergence of level
truncation), the actual zero locus of det V4(P^2) for string vertices, the
BRST/boundary condition (ii'), genus >= 1.  See 035 section 4.
"""

from __future__ import annotations

import itertools
import math
import sys

import numpy as np

SEED = 20260921
rng = np.random.default_rng(SEED)
TOL = 1e-9
failures: list[str] = []


def report(name: str, ok: bool, detail: str = "") -> None:
    """Print one PASS/FAIL line and record failures."""
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name}: {detail}")
    if not ok:
        failures.append(name)


# --------------------------------------------------------------------------
# Part 1: the calculus on the 17-row table of 030 section 1.3
# --------------------------------------------------------------------------
# Each row: (label, reading, l, insertion data, gamma).  Insertion data:
#   reading "biv":  (strands s, n_b)         -> d_hat_B = n_b - 6 (s - 1)
#   reading "form": (n_surfaces, sum(6(1-g)), n_b, n_c, bivector S_B list)
#                   -> S = sum 6(1-g) + n_b - n_c - sum S_B ; d_hat = S - 6
TABLE = [
    ("1 frozen node omega1^-1", "biv", 1, (1, 1), 0),
    ("2 cylinder as map b0+/L0+", "form", 1, (1, 6, 1, 1, []), -1),
    ("3 cylinder P", "biv", 1, (1, 2), -1),
    ("4 bounded cylinder", "biv", 1, (1, 2), -1),
    ("5 doubly-frozen node", "biv", 1, (1, 2), -1),
    ("6 G2^-1", "biv", 2, (2, 2), 0),
    ("7 double tube", "biv", 2, (2, 4), -2),
    ("8 bounded double tube", "biv", 2, (2, 4), -2),
    ("9a fully diagonal double tube", "biv", 2, (2, 2), 0),
    ("9b length-diagonal double tube", "biv", 2, (2, 3), -1),
    ("10 Sigma_{g,4} integrated (g=0)", "form", 2, (1, 6, 2, 0, []), 2),
    ("10 Sigma_{g,4} integrated (g=2)", "form", 2, (1, -6, 14, 0, []), 2),
    ("11 rigid 4-punctured sphere", "form", 2, (1, 6, 0, 0, []), 4),
    ("12 half-frozen sphere", "form", 2, (1, 6, 2, 0, []), 2),
    # 13: V=2 vertices of valence 4 joined by nu_f=2 frozen nodes (S_B=5 each)
    ("13 022 kernel nu_f=2, g_s=0", "form", 2, (2, 12, 4, 0, [5, 5]), 4),
    # 13: two V4's joined by one frozen node + one smoothed handle
    ("13 022 kernel nu_f=1, g_s=1", "form", 2, (2, 12, 4, 0, [5, 4]), 3),
    ("14 sphere + n_x=4 extra b", "form", 2, (1, 6, 6, 0, []), -2),
    ("15 G2 (identity, two omega1)", "form", 2, (2, 12, 0, 2, []), 0),
    ("16 m2 = G2^-1 V4", "form", 2, (1, 6, 2, 0, []), 2),
    ("17 m2^-1 as bivector", "biv", 2, (2, None), -2),  # S_B = 8 given, not n_b
    ("17 m2^-1 as 4-form", "form", 2, (1, 6, 6, 0, []), -2),
]


def d_hat_from_insertions(reading: str, data: tuple) -> int:
    """Formal dimension from insertion counts, 035 eqs. (1.2), (1.5)."""
    if reading == "biv":
        s, n_b = data
        return n_b - 6 * (s - 1)
    n_surf, six_chi, n_b, n_c, biv = data
    s_tot = six_chi + n_b - n_c - sum(biv)
    return s_tot - 6


def d_hat_from_gamma(
    reading: str, ell: int, gamma: int, const_l: int | None = None
) -> int:
    """Affine image of the map ghost number, 035 eq. (1.7)."""
    ell_eff = ell if const_l is None else const_l
    if reading == "biv":
        return 6 - 5 * ell_eff - gamma
    return 5 * ell_eff - 6 - gamma


def part1() -> None:
    """Claim C1: the calculus."""
    # C1.2: every row of the table
    ok_all = True
    for label, reading, ell, data, gamma in TABLE:
        if label.startswith("17 m2^-1 as bivector"):
            # bivector content S_B = 8 (030 row 17): d_hat_B = 6 - S_B = -2
            d_ins = 6 - 8
        else:
            d_ins = d_hat_from_insertions(reading, data)
        d_gam = d_hat_from_gamma(reading, ell, gamma)
        ok = d_ins == d_gam
        ok_all &= ok
        if not ok:
            print(f"    row {label}: insertions {d_ins} vs gamma {d_gam}")
    report(
        "C1.2 all 17 rows of 030 table obey d_hat = affine(gamma)",
        ok_all,
        f"{len(TABLE)} table entries for the 17 rows (some rows in both readings)",
    )

    # break-on-purpose: use the l=1 constant on the l=2 rows
    n_fail = 0
    for label, reading, ell, data, gamma in TABLE:
        if ell != 2:
            continue
        d_ins = (
            6 - 8
            if label.startswith("17 m2^-1 as bivector")
            else d_hat_from_insertions(reading, data)
        )
        if d_ins != d_hat_from_gamma(reading, ell, gamma, const_l=1):
            n_fail += 1
    report(
        "C1.2-break wrong affine constant is detected",
        n_fail > 0,
        f"{n_fail} of the l=2 rows fail with the l=1 constant",
    )

    # C1.1: inverse lemma on random graded symmetric matrices.
    # Degenerate draws are resampled rather than skipped, and the number of
    # trials actually tested is asserted: skipping all of them would otherwise
    # make the check pass vacuously.
    ok_inv = True
    n_tested = 0
    n_resampled = 0
    while n_tested < 3 and n_resampled < 100:
        S = int(rng.integers(4, 12))
        # basis ghost numbers, paired so that N_a + N_b = S is possible
        half = [int(rng.integers(0, S + 1)) for _ in range(int(rng.integers(2, 5)))]
        grades = half + [S - n for n in half]
        n = len(grades)
        omega = np.zeros((n, n), dtype=complex)
        for a in range(n):
            for b in range(n):
                if grades[a] + grades[b] == S:
                    omega[a, b] = rng.normal() + 1j * rng.normal()
        omega = omega + omega.T
        if abs(np.linalg.det(omega)) < 1e-6:
            n_resampled += 1
            continue
        n_tested += 1
        inv = np.linalg.inv(omega)
        for a in range(n):
            for b in range(n):
                if grades[a] + grades[b] != S and abs(inv[a, b]) > TOL:
                    ok_inv = False
    report(
        "C1.1 inverse bivector has S_B = S (support on N_a+N_b=S)",
        ok_inv and n_tested == 3,
        f"{n_tested} random gradings tested ({n_resampled} degenerate draws resampled)",
    )
    # break: an inhomogeneous (non-graded) perturbation spreads the support
    S = 8
    grades = [2, 3, 6, 5]
    omega = np.zeros((4, 4), dtype=complex)
    for a in range(4):
        for b in range(4):
            if grades[a] + grades[b] == S:
                omega[a, b] = rng.normal()
    omega = omega + omega.T
    omega[0, 1] += 0.3
    omega[1, 0] += 0.3
    inv = np.linalg.inv(omega)
    spread = any(
        abs(inv[a, b]) > TOL
        for a in range(4)
        for b in range(4)
        if grades[a] + grades[b] != S
    )
    report(
        "C1.1-break inhomogeneous form breaks the block pattern",
        spread,
        "off-grading entry 0.3 added",
    )

    # C1.3: closure sums, using d_hat(V_n) = 2n-6, d_hat_B(p^-1) = -2, d_hat_B(P) = +2
    dV = {n: 2 * n - 6 for n in range(3, 7)}
    dPinv = 6 - 8  # inverse lemma: S(V4) = 8
    dDelta = 6 - 4  # inverse lemma: S(omega1(., Q .)) = 4
    checks = [
        ("4pt V4 p^-1 V4", dV[4] + dPinv + dV[4], 2),
        ("5pt V4 p^-1 V5 p^-1 V4", dV[4] + dPinv + dV[5] + dPinv + dV[4], 4),
        ("6pt V5 p^-1 V5", dV[5] + dPinv + dV[5], 6),
        ("4pt V3 Delta V3", dV[3] + dDelta + dV[3], 2),
    ]
    ok = all(val == target for _, val, target in checks)
    report(
        "C1.3 closure of the count at 4, 5, 6 points",
        ok,
        "; ".join(f"{lab}: {val} = {tgt}" for lab, val, tgt in checks),
    )


# --------------------------------------------------------------------------
# Finite-dimensional model (same conventions as verify-b3-sextic.py):
# H_0 = R^N, orthonormal Sym^2 basis, V4 symmetric D x D, V5 totally symmetric.
# --------------------------------------------------------------------------
N = 3
D = N * (N + 1) // 2


def sym2_basis(n: int) -> np.ndarray:
    """Orthonormal basis e_I (I = 0..D-1) of symmetric n x n matrices."""
    basis = []
    for i in range(n):
        e = np.zeros((n, n))
        e[i, i] = 1.0
        basis.append(e)
    for i in range(n):
        for j in range(i + 1, n):
            e = np.zeros((n, n))
            e[i, j] = e[j, i] = 1 / math.sqrt(2)
            basis.append(e)
    return np.array(basis)


E = sym2_basis(N)


def symmetrize(t: np.ndarray) -> np.ndarray:
    """Total symmetrisation of a tensor."""
    k = t.ndim
    out = np.zeros_like(t)
    for perm in itertools.permutations(range(k)):
        out += np.transpose(t, perm)
    return out / math.factorial(k)


def random_sym_tensor(k: int, complex_: bool = False) -> np.ndarray:
    """Return a generic totally symmetric rank-k tensor on R^N (or C^N)."""
    t = rng.normal(size=(N,) * k)
    if complex_:
        t = t + 1j * rng.normal(size=(N,) * k)
    return symmetrize(t)


def v4_to_sym(v4: np.ndarray) -> np.ndarray:
    """V4[i,j,k,l] -> V4S[I,J] in the orthonormal Sym^2 basis."""
    return np.einsum("ijkl,Iij,Jkl->IJ", v4, E, E)


def v5_to_sym(v5: np.ndarray) -> np.ndarray:
    """V5[i,j,k,l,a] -> V5S[I,J,a]."""
    return np.einsum("ijkla,Iij,Jkl->IJa", v5, E, E)


def pair_coords(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    """Coordinates of Sym(x (x) y) in the Sym^2 basis."""
    m = 0.5 * (np.outer(x, y) + np.outer(y, x))
    return np.einsum("Iij,ij->I", E, m)


def composite(
    v4s: np.ndarray,
    v5s: np.ndarray,
    a: np.ndarray,
    b: np.ndarray,
    z1: np.ndarray,
    z2: np.ndarray,
) -> complex:
    """
    Composite kernel of 013.

    C(A, B, Z) = sum_strands <V5(., A, z1), V4^{-1} V5(., B, z2)>,
    Z = Sym(z1 (x) z2) (both strand assignments summed with weight 1/2 each).
    """
    inv = np.linalg.inv(v4s)
    total = 0.0
    for za, zb in ((z1, z2), (z2, z1)):
        left = np.einsum("IJa,J,a->I", v5s, a, za)
        right = np.einsum("IJa,J,a->I", v5s, b, zb)
        total += 0.5 * left @ inv @ right
    return total


def diagonal_composite(v4s: np.ndarray, v5s: np.ndarray, psi: np.ndarray) -> complex:
    """C(P, P, P) = v^T V4^{-1} v with v = V5(., psi psi, psi)."""
    p = pair_coords(psi, psi)
    v = np.einsum("IJa,J,a->I", v5s, p, psi)
    return v @ np.linalg.inv(v4s) @ v


# --------------------------------------------------------------------------
# Part 2: symmetry count (C2.3) and scaling degree (C2.4)
# --------------------------------------------------------------------------
def part2() -> None:
    """Claim C2 (machine-checkable parts)."""
    legs = range(6)
    assignments = set()
    for a_pair in itertools.combinations(legs, 2):
        rest = [x for x in legs if x not in a_pair]
        for z1 in rest:
            rest2 = [x for x in rest if x != z1]
            for b_pair in itertools.combinations(rest2, 2):
                z2 = [x for x in rest2 if x not in b_pair][0]
                block1 = (frozenset(a_pair), z1)
                block2 = (frozenset(b_pair), z2)
                assignments.add(frozenset([block1, block2]))
    n_assign = len(assignments)
    # combinatorial stabiliser of one *labelled assignment* under S6: this is the
    # Wick bookkeeping (90 = 6!/8) and is blind to the kernel, since it never
    # evaluates C_sigma.
    one = next(iter(assignments))
    stab_label = 0
    for perm in itertools.permutations(legs):
        image = frozenset(
            (frozenset(perm[i] for i in pair), perm[z]) for pair, z in one
        )
        if image == one:
            stab_label += 1
    report(
        "C2.3a Wick count: 90 labelled strand assignments, labelled stabiliser 8",
        n_assign == 90 and stab_label == 8,
        f"assignments = {n_assign}, labelled stabiliser order = {stab_label}",
    )

    # C2.3b: the stabiliser of C_sigma *as a function* on Psi^{(x)6}.
    # C_sigma(p) = <V5(., p0 p1, p2), V4^{-1} V5(., p3 p4, p5)>.  Because V5 is
    # totally symmetric, V5(., pj pk, pi) is symmetric in (i, j, k), so the
    # invariance group is (S3 x S3) x| Z2 of order 72 (035 eq. 2.6) and the
    # orbit count is 720 / 72 = 10 (the (3|3) splittings).
    v4s_c = v4_to_sym(random_sym_tensor(4))
    inv_c = np.linalg.inv(v4s_c)
    psis = [rng.normal(size=N) for _ in range(6)]

    def c_sigma(v5s_loc: np.ndarray, p: list) -> float:
        left = np.einsum("IJa,J,a->I", v5s_loc, pair_coords(p[0], p[1]), p[2])
        right = np.einsum("IJa,J,a->I", v5s_loc, pair_coords(p[3], p[4]), p[5])
        return float(left @ inv_c @ right)

    def stabiliser(v5s_loc: np.ndarray) -> list:
        base = c_sigma(v5s_loc, psis)
        scale = max(1.0, abs(base))
        return [
            perm
            for perm in itertools.permutations(range(6))
            if abs(c_sigma(v5s_loc, [psis[i] for i in perm]) - base) < 1e-9 * scale
        ]

    v5s_tot = v5_to_sym(random_sym_tensor(5))
    stab_fun = stabiliser(v5s_tot)
    # every surviving permutation must preserve the (3|3) splitting {0,1,2}|{3,4,5}
    splitting = {frozenset((0, 1, 2)), frozenset((3, 4, 5))}
    preserves = all(
        {frozenset(perm[:3]), frozenset(perm[3:])} == splitting for perm in stab_fun
    )
    report(
        "C2.3b kernel symmetry: stabiliser of C_sigma as a function is |G| = 72",
        len(stab_fun) == 72 and preserves and 720 // len(stab_fun) == 10,
        f"|stab| = {len(stab_fun)}, all preserve the (3|3) splitting: {preserves}, "
        f"orbits = {720 // len(stab_fun)}, Wick multiplicity {n_assign // (720 // len(stab_fun))}",
    )

    # break-on-purpose: a V5 symmetric only inside each Sym^2 slot (not between
    # the paired legs and the spectator) has stabiliser 8, the labelled count.
    raw = rng.normal(size=(N,) * 5)
    raw = 0.5 * (raw + np.transpose(raw, (1, 0, 2, 3, 4)))
    raw = 0.5 * (raw + np.transpose(raw, (0, 1, 3, 2, 4)))
    stab_break = stabiliser(v5_to_sym(raw))
    report(
        "C2.3b-break a V5 without total symmetry drops the stabiliser to 8",
        len(stab_break) == 8,
        f"|stab| = {len(stab_break)} for a pairwise-only symmetric V5",
    )

    # C2.4 scaling degree of the composite
    v4 = random_sym_tensor(4)
    v5 = random_sym_tensor(5)
    v4s, v5s = v4_to_sym(v4), v5_to_sym(v5)
    psi = rng.normal(size=N)
    c0 = diagonal_composite(v4s, v5s, psi)
    ok = True
    for _ in range(4):
        t, u = rng.uniform(0.3, 3.0, size=2)
        c = diagonal_composite(t * v4s, u * v5s, psi)
        ok &= abs(c / c0 - u**2 / t) < 1e-9
    report(
        "C2.4 composite scales as u^2 / t under (V4, V5) -> (t V4, u V5)",
        ok,
        "4 random (t, u)",
    )
    t, u = 1.7, 0.6
    c = diagonal_composite(t * v4s, u * v5s, psi)
    report(
        "C2.4-break degree (-2, 2) is rejected",
        abs(c / c0 - u**2 / t**2) > 1e-3,
        f"|ratio - u^2/t^2| = {abs(c / c0 - u**2 / t**2):.3e}",
    )


# --------------------------------------------------------------------------
# Part 3: momentum toy (claim C3)
# --------------------------------------------------------------------------
P0 = 0.3 + 0.7j  # generic complex "momentum" where det V4 vanishes


def make_v4_family(dim_null: int) -> tuple:
    """
    Build the V4(P) family of 035 eq. (3.1).

    V4(P) = M0 + (P - P0) M1 + (P - P0)^2 M2, symmetric, with ker M0 of dimension
    dim_null spanned by the columns of Nmat (orthonormal).  Returns (fun, Nmat, M1).
    """
    q, _ = np.linalg.qr(rng.normal(size=(D, D)))
    nmat = q[:, :dim_null]
    perp = q[:, dim_null:]
    k = rng.normal(size=(D - dim_null, D - dim_null))
    k = k + k.T
    m0 = perp @ k @ perp.T
    m1 = rng.normal(size=(D, D))
    m1 = m1 + m1.T
    m2 = rng.normal(size=(D, D))
    m2 = m2 + m2.T

    def fun(p: complex) -> np.ndarray:
        e = p - P0
        return m0 + e * m1 + e**2 * m2

    return fun, nmat, m1


def make_v5_family(t0: np.ndarray) -> tuple:
    """V5(P) = T0 + (P - P0) T1 + (P - P0)^2 T2 with generic T1, T2."""
    t1, t2 = random_sym_tensor(5), random_sym_tensor(5)
    t0s, t1s, t2s = v5_to_sym(t0), v5_to_sym(t1), v5_to_sym(t2)

    def fun(p: complex) -> np.ndarray:
        e = p - P0
        return t0s + e * t1s + e**2 * t2s

    return fun


def contour_residue(f, radius: float = 0.05, n_pts: int = 128) -> complex:
    """Residue at P0 by the Cauchy integral on a circle (trapezoid, exact for Laurent polys)."""
    total = 0.0
    for m in range(n_pts):
        theta = 2 * math.pi * m / n_pts
        z = P0 + radius * np.exp(1j * theta)
        total += (
            f(z) * radius * np.exp(1j * theta)
        )  # f dz / (2 pi i) with dz = i r e^{i th} dth
    return total / n_pts


def r38_project(t0: np.ndarray, nmat: np.ndarray) -> np.ndarray:
    """
    Project a symmetric 5-tensor orthogonally onto the R38 closure subspace.

    Subspace
    { T : n^{ij} T_{ijklm} = 0 for every column n of nmat, and all k, l, m }
    (035 eq. 2.4 when nmat spans the whole kernel N; eq. 3.4' when it spans a
    proper subspace of it, which is how the isotropic branch is built).
    Parametrised on the independent components of Sym^5.  Complex columns of
    nmat are allowed; the projection is then the complex-orthogonal one.
    """
    dtype = np.result_type(t0.dtype, nmat.dtype)
    idx = list(itertools.combinations_with_replacement(range(N), 5))
    n_comp = len(idx)

    def from_coords(c: np.ndarray) -> np.ndarray:
        t = np.zeros((N,) * 5, dtype=np.result_type(dtype, c.dtype))
        for val, ind in zip(c, idx, strict=True):
            for perm in set(itertools.permutations(ind)):
                t[perm] = val
        return t

    def to_coords(t: np.ndarray) -> np.ndarray:
        return np.array([t[ind] for ind in idx])

    # linear map coords -> constraint values
    rows = []
    for c in np.eye(n_comp, dtype=dtype):
        t = from_coords(c)
        vals = []
        for col in range(nmat.shape[1]):
            nmatrix = np.einsum(
                "I,Iij->ij", nmat[:, col], E
            )  # null vector as N x N matrix
            vals.append(np.einsum("ij,ijklm->klm", nmatrix, t).ravel())
        rows.append(np.concatenate(vals))
    amat = np.array(rows).T  # constraints x n_comp
    _, sing, vt = np.linalg.svd(amat)
    rank = int(np.sum(sing > 1e-10))
    # A @ V[:, rank:] = 0 with V = vt.conj().T; valid for real and complex amat
    null_basis = vt[rank:].conj().T  # n_comp x (n_comp - rank)
    c0 = to_coords(t0).astype(dtype)
    proj = null_basis @ (null_basis.conj().T @ c0)
    return from_coords(proj)


def part3(dim_null: int) -> None:
    """Claim C3 for kernel dimension dim_null."""
    tag = f"[dimN={dim_null}]"
    v4fun, nmat, m1 = make_v4_family(dim_null)
    a_mat = nmat.T @ m1 @ nmat  # N^T M1 N

    # C3.1: det V4 vanishes at P0 to order dim_null, N^T M1 N invertible
    det0 = abs(np.linalg.det(v4fun(P0)))
    eps = 1e-3
    order = math.log(
        abs(np.linalg.det(v4fun(P0 + eps))) / abs(np.linalg.det(v4fun(P0 + 2 * eps)))
    ) / math.log(0.5)
    report(
        f"C3.1{tag} det V4(P0) = 0, zero of order dim N, N^T M1 N invertible",
        det0 < 1e-10
        and abs(order - dim_null) < 0.05
        and abs(np.linalg.det(a_mat)) > 1e-6,
        f"|det| = {det0:.1e}, order = {order:.3f}, det(N^T M1 N) = {np.linalg.det(a_mat):.3f}",
    )

    # C3.2: Laurent prediction for V4^{-1} vs contour residue of the inverse matrix
    res_inv = contour_residue(lambda p: np.linalg.inv(v4fun(p)))
    pred_inv = nmat @ np.linalg.inv(a_mat) @ nmat.T
    report(
        f"C3.2{tag} Res V4^{{-1}} = N (N^T M1 N)^{{-1}} N^T (contour vs Laurent)",
        np.max(np.abs(res_inv - pred_inv)) < 1e-8,
        f"max dev {np.max(np.abs(res_inv - pred_inv)):.1e}",
    )

    # generic V5
    t0 = random_sym_tensor(5)
    v5fun = make_v5_family(t0)
    psi = rng.normal(size=N)
    a_vec, b_vec = rng.normal(size=D), rng.normal(size=D)
    z1, z2 = rng.normal(size=N), rng.normal(size=N)

    def c_diag(p, v5f=v5fun):
        return diagonal_composite(v4fun(p), v5f(p), psi)

    def c_pol(p, v5f=v5fun):
        return composite(v4fun(p), v5f(p), a_vec, b_vec, z1, z2)

    res_diag = contour_residue(c_diag)
    res_pol = contour_residue(c_pol)
    # Laurent prediction (035 eq. 3.3)
    v0 = np.einsum("IJa,J,a->I", v5fun(P0), pair_coords(psi, psi), psi)
    pred_diag = v0 @ pred_inv @ v0
    report(
        f"C3.2{tag}-composite Res C(P,P,P) = v0^T N (N^T M1 N)^{{-1}} N^T v0",
        abs(res_diag - pred_diag) < 1e-8,
        f"contour {res_diag:.4f}, Laurent {pred_diag:.4f}",
    )
    report(
        f"C3.3{tag} pole survives on generic V5 (diagonal and polarised)",
        abs(res_diag) > 1e-3 and abs(res_pol) > 1e-3,
        f"|Res diag| = {abs(res_diag):.3f}, |Res pol| = {abs(res_pol):.3f}",
    )

    # C3.4: R38 at P0 removes the pole
    t0_r38 = r38_project(t0, nmat)
    v5fun_r38 = make_v5_family(t0_r38)
    # sanity: the projected tensor really satisfies the condition, and is not zero
    viol = max(
        np.max(np.abs(np.einsum("I,IJa->Ja", nmat[:, c], v5fun_r38(P0))))
        for c in range(dim_null)
    )
    res_diag_r38 = contour_residue(lambda p: c_diag(p, v5fun_r38))
    res_pol_r38 = contour_residue(lambda p: c_pol(p, v5fun_r38))
    growth = abs(c_diag(P0 + 1e-4, v5fun_r38)) / abs(c_diag(P0 + 1e-2, v5fun_r38))
    report(
        f"C3.4{tag} R38 at P0 (Pi_N V5(P0) = 0) removes the pole",
        viol < 1e-10
        and np.linalg.norm(t0_r38) > 0.1
        and abs(res_diag_r38) < 1e-8
        and abs(res_pol_r38) < 1e-8
        and growth < 3.0,
        f"violation {viol:.1e}, |T0| = {np.linalg.norm(t0_r38):.2f}, |Res| = {abs(res_diag_r38):.1e}, "
        f"{abs(res_pol_r38):.1e}, growth ratio {growth:.2f}",
    )

    # C3.5: break on purpose -- source the null direction
    w = rng.normal(size=(N, N, N))
    nmatrix = np.einsum("I,Iij->ij", nmat[:, 0], E)
    source = symmetrize(np.einsum("ij,klm->ijklm", nmatrix, w))
    res_by_eps = []
    for eps_s in (0.05, 0.1):
        v5fun_bad = make_v5_family(t0_r38 + eps_s * source)
        res_by_eps.append(contour_residue(lambda p, f=v5fun_bad: c_diag(p, f)))
    ratio = abs(res_by_eps[1] / res_by_eps[0])
    report(
        f"C3.5{tag} break-on-purpose: sourcing the null direction restores the pole, Res ~ eps^2",
        abs(res_by_eps[0]) > 1e-6 and abs(ratio - 4.0) < 0.2,
        f"|Res(0.05)| = {abs(res_by_eps[0]):.2e}, Res(0.1)/Res(0.05) = {ratio:.3f}",
    )

    if dim_null >= 2:
        isotropy_check(tag, v4fun, nmat, a_mat, t0, psi, a_vec, b_vec, z1, z2)


def isotropic_vector(b: np.ndarray) -> np.ndarray:
    """
    Return a nonzero u with u^T b u = 0, for a 2 x 2 symmetric b (035 eq. 3.4').

    Solves b00 x^2 + 2 b01 x + b11 = 0 and returns u = (x, 1); over C such a
    root always exists, so an isotropic line exists for every non-degenerate
    complex symmetric form in two variables.
    """
    if abs(b[0, 0]) < 1e-12:
        return np.array([1.0, 0.0], dtype=complex)
    root = np.roots([b[0, 0], 2 * b[0, 1], b[1, 1]])[0]
    return np.array([root, 1.0], dtype=complex)


def isotropy_check(
    tag: str,
    v4fun,
    nmat: np.ndarray,
    a_mat: np.ndarray,
    t0: np.ndarray,
    psi: np.ndarray,
    a_vec: np.ndarray,
    b_vec: np.ndarray,
    z1: np.ndarray,
    z2: np.ndarray,
) -> None:
    """
    C3.6: at dim N = 2 the R38 condition (2.4) is sufficient but not necessary.

    Build a V5 whose image W(P0) = {N^T V5(., A, z)|_{P0}} is the isotropic line
    of a^{-1} = (N^T M1 N)^{-1}: impose the R38 condition for the single null
    direction n_mu = N mu with mu orthogonal to an isotropic u (035 eq. 3.4').
    The residue then vanishes exactly although Pi_N V5(P0) != 0 -- the loophole
    the record's earlier "necessary and sufficient" claim missed.  The break leg
    runs the identical construction with a generic, non-isotropic direction and
    must find a pole.
    """
    b_form = np.linalg.inv(a_mat)

    def build(u_vec: np.ndarray) -> tuple:
        """Project T0 so that W is contained in the line spanned by u_vec."""
        mu = np.array([-u_vec[1], u_vec[0]])
        n_mu = (nmat.astype(complex) @ mu).reshape(D, 1)
        t0_loc = r38_project(t0, n_mu)
        v5f = make_v5_family(t0_loc)
        # G[c, (J, a)] = sum_I N[I, c] V5S(P0)[I, J, a]: the image W is its column space
        g_mat = np.einsum("Ic,IJa->cJa", nmat, v5f(P0)).reshape(nmat.shape[1], -1)
        return v5f, g_mat

    def residues(v5f) -> tuple:
        res_d = contour_residue(lambda p: diagonal_composite(v4fun(p), v5f(p), psi))
        res_p = contour_residue(
            lambda p: composite(v4fun(p), v5f(p), a_vec, b_vec, z1, z2)
        )
        return res_d, res_p

    u_iso = isotropic_vector(b_form)
    iso_defect = abs(u_iso @ b_form @ u_iso)
    v5_iso, g_iso = build(u_iso)
    # W is a line: rank 1, and its direction is u_iso
    sing = np.linalg.svd(g_iso, compute_uv=False)
    col = g_iso[:, np.argmax(np.linalg.norm(g_iso, axis=0))]
    along_u = abs(col[0] * u_iso[1] - col[1] * u_iso[0]) / np.linalg.norm(col)
    pi_n_v5 = np.max(np.abs(g_iso))
    res_d_iso, res_p_iso = residues(v5_iso)
    report(
        f"C3.6{tag} isotropic W: residue vanishes with Pi_N V5(P0) != 0 "
        f"((2.4) sufficient, not necessary)",
        iso_defect < 1e-10
        and pi_n_v5 > 0.1
        and sing[1] < 1e-10 * max(sing[0], 1.0)
        and along_u < 1e-8
        and abs(res_d_iso) < 1e-8
        and abs(res_p_iso) < 1e-8,
        f"u^T a^-1 u = {iso_defect:.1e} (u real: {abs(u_iso.imag).max() < 1e-12}), "
        f"|Pi_N V5| = {pi_n_v5:.2f}, sing(W) = ({sing[0]:.2f}, {sing[1]:.1e}), "
        f"W || u: {along_u:.1e}, |Res| = {abs(res_d_iso):.1e}, {abs(res_p_iso):.1e}",
    )

    # break-on-purpose: same construction, non-isotropic direction -> pole back
    u_bad = rng.normal(size=2).astype(complex)
    bad_defect = abs(u_bad @ b_form @ u_bad)
    v5_bad, g_bad = build(u_bad)
    res_d_bad, res_p_bad = residues(v5_bad)
    report(
        f"C3.6{tag}-break a non-isotropic W restores the pole",
        bad_defect > 1e-3 and abs(res_d_bad) > 1e-6 and abs(res_p_bad) > 1e-6,
        f"u^T a^-1 u = {bad_defect:.3f}, |Pi_N V5| = {np.max(np.abs(g_bad)):.2f}, "
        f"|Res| = {abs(res_d_bad):.3e}, {abs(res_p_bad):.3e}",
    )


def main() -> int:
    """Run all checks; return the number of failures."""
    print(f"seed = {SEED}")
    part1()
    part2()
    part3(1)
    part3(2)
    print(f"summary: {len(failures)} failure(s)")
    return len(failures)


if __name__ == "__main__":
    sys.exit(main())
