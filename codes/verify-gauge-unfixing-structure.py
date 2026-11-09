"""Gauge unfixing of Sigma_2: structure lemma L1 and the finite model M (record 102).

Record: agent/derivations/102-gauge-unfixing-structure.md (sub-task 1a: C1, C2;
sub-task 1b: L2-model C3, the building-block table C5).

VERIFIED (each check named after its claim-tree node)
  C1-search   L1 at two seeds: for random (E, S, D, p) -- even instances with p
              non-degenerate and with p degenerate, a graded instance (ghost
              degrees 3, 4, 5, q pairing degrees summing to 8, graded symmetry
              with the Koszul sign), and the model-tied instance S = Sym^2 H_2 of M
              with p = p_{2,2} read from V_4 (dim ker p = 1, and 5 in the degenerate
              variant), E = S + H_1^H_3,
              D a random rational matrix (not an operator of M) -- the linear system {q graded symmetric, q(D l, x) = 0,
              q|_S = p} has the unique solution q = P^T p P, P the projector onto S
              along im D, and ker q = ker p (+) im D.  Uniqueness: nullity of the
              coefficient matrix is 0 (exact Fractions for the abstract instances;
              modulo the prime 2^61 - 1 for the 210-unknown model instance, which is
              rigorous for nullity 0 since rank mod p <= rank over Q).  Existence:
              P^T p P, computed by an independent route (coordinates in S (+) im D),
              satisfies every equation exactly.  A falsifiability probe compares the
              solve with a wrong candidate (P computed along a wrong complement).
  C1-break-sym  Drop the symmetry of q: the solution space grows to dimension
              dim S * rank D (even instance); the uniqueness test then FAILS, as
              expected.
  C1-break-transverse  Drop transversality: (a) S + im D a proper subspace, the
              symmetric solution space grows (FAIL as expected); (b) S and im D
              meet, the system is inconsistent for p non-degenerate and consistent
              when the intersection lies in ker p, with nullity 0 (both asserted;
              FAIL as expected for (b)-generic).
  C2-gauge    Model M: Q^2 = 0 and Q self-adjoint (conv:QB-self-adjoint); the
              truncated action S_<=4 = 1/2<Psi,Q Psi> + g/3! V_3(Psi^3)
              + g^2/4! V_4(Psi^4) is invariant under delta Psi = Q Lambda
              + g l_2(Psi, Lambda) at orders g^0, g^1, g^2 (exact sympy polynomial
              identity in the five field components); chi (x) chi lies in ker p;
              dim ker p printed (generic and degenerate variant).  Break legs: V_4^chi
              dropped, and V_4^chi doubled -- the g^2 coefficient is non-zero (FAIL as
              expected).

  C3-solve    L2-model (record 102, Block L2-model).  HS action (L2.1) on M at
              g = 1 (restored from the weight: psi, eps weight 1; sigma, theta
              weight 2).  Ansatz: delta linear in (eps, theta), polynomial, shifts
              s = 0, 1, 2 (5205 coefficients); equations: every monomial of
              delta S of weight <= 4 vanishes.  The coefficients no S^(w), w <= 4 - s,
              depends on (U) are shown to have zero columns; on the other 240 the
              null space (mod 2^31 - 1) is compared with the rank of the span of
              (G) composite law of delta Psi = Lambda'(chi + M Psi), Lambda' of
              weight 1..3; (K) delta Sigma_2 = m N, N in ker p; (T) mu^{ij} E_j,
              mu antisymmetric over all 20 coordinates (both equations of motion).
              Every generator is checked exactly over Q to solve the system.  Rank
              mod p <= rank over Q at both ends makes the equality rigorous.
              Generic (dim ker p = 1) and degenerate (5) variants, two seeds.
  C3-break    Break legs of C3-solve: mu symmetric; delta Psi ~ E_Sigma without its
              partner; mixed mu^{Psi Sigma} entries dropped; kernel class dropped.
  C3.3-restriction  S_el = S~(psi, Psi^2) equals S_<=4 built from the vertices; a
              random exact solution restricted to the saddle (Psi^2, plus a kernel
              element in the degenerate variant) is a symmetry of S_el at weight
              <= 4 although it does not preserve Sigma_2 = Psi^2; break leg: the
              restriction to Sigma_2 = 2 Psi^2 is not a symmetry.
  C5-table    Ghost shifts of l_2, l_3, p_{2,2}, <.,.> read off M's tensors; the
              rows of the building-block table for D, B_2, delta_{Lambda_2} Psi,
              Lambda(Lambda_2, ...) enumerated by two routes (sequence search;
              integer balance) and compared -- a consistency check, the two
              routes share the balance rules; level-matched rows tested on the
              present content (per-strand grading: Sigma_2 and Psi strands at
              ghost 2, Lambda_2 at (1, 2), operations at every ghost number) and on
              M's grading and supports; the present-content count of level-matched
              B_2 rows is asserted to be 0.  Break legs: a wrong N_gh(l_3) in one
              route; Sigma_2 strands at (1, 3) make a level-matched B_2 row appear.

  C1.4-E1b-source (after the last review) Elimination of extra directions W
              with the source q(Sigma_2, Psi^2), eqs. (L1.10)-(L1.11): closed
              form exact at random points; the Schur condition alone does not
              reproduce the present action (FAIL as expected), nor q_SS = p with
              q_WS != 0 and q_WW definite; q_WS = 0 does; an indefinite q_WW
              with q_WS(S) isotropic does, with w* != 0.
  C4.theta-core (after the last review) Finite acyclic graded model (self-
              adjoint Q, no cohomology at ghost 2): (theta.1) the solutions of
              <A, Q Psi> = 0 are im Q; (theta.2) the solutions b of
              omega(bX, X) = 0 are the span of im-Q-valued maps and mu o Q with
              mu antisymmetric (exact ranks).  Break legs: the mu o Q class
              dropped; a Q-cohomology direction (both steps then FAIL as
              expected).  The linear algebra of record 102's C4.theta only.
  C1-break-transverse (a) now asserts nullity == 4 (1 + 3), not > 0.
  C5-table also asserts the counts (rows, level-matched, present A6) per block
              and the equality of the Lambda_2 (0, 3) counts; the total-ghost-4
              reading (ruled out by A6, Harold's decision) is asserted as a note:
              B_2 count 2.

NOT VERIFIED HERE
  L2-SFT (an argument with a citation, no machine check applies).  M is the
  on-shell analogue (physical fields with zero kinetic term): C3 checks the
  combined L2 statement modulo the unseen part U, which holds every
  field-dependent gauge parameter, so the completeness ("same orbits") step is
  not tested here; a generic-momentum variant of M is not built.  The quotient
  formulation of C3 (implied by the representative one).  Wirings inside a table
  row; the non-level-matched rows on an implemented H^ext.  Nothing about the
  string vertices: M is a finite graded model with no momenta and no level
  matching; the formal extension H^ext of the record is not implemented.
  The lift of Q to several strands appears nowhere (excluded by the brief).

Run from the project root: .venv/bin/python codes/verify-gauge-unfixing-structure.py
"""

from __future__ import annotations

import random
import sys
from fractions import Fraction
from itertools import combinations, combinations_with_replacement, permutations, product

import numpy as np
import sympy as sp

SEEDS = (20261018, 7)
PRIME = 2**61 - 1
RESULTS: list[tuple[str, bool, str]] = []


def record(name: str, ok: bool, detail: str) -> None:
    """Store and print one named check."""
    RESULTS.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}")


# ---------------------------------------------------------------- linear algebra


def rand_rat(rng: random.Random, lo: int = -9, hi: int = 9) -> Fraction:
    """Random small rational."""
    return Fraction(rng.randint(lo, hi), rng.randint(1, 4))


def rand_mat(rng: random.Random, n: int, m: int) -> list[list[Fraction]]:
    """Random n x m rational matrix."""
    return [[rand_rat(rng) for _ in range(m)] for _ in range(n)]


def matmul(a: list[list], b: list[list]) -> list[list]:
    """Matrix product."""
    bt = list(zip(*b))
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


def transpose(a: list[list]) -> list[list]:
    """Matrix transpose."""
    return [list(r) for r in zip(*a)]


def rref_solve(rows: list[list], rhs: list, field: str = "Q") -> dict:
    """Gaussian elimination of A u = b over Q (Fractions) or GF(PRIME).

    Returns rank, nullity, consistency and one particular solution.
    """
    ncol = len(rows[0])
    if field == "Q":
        aug = [list(r) + [b] for r, b in zip(rows, rhs)]

        def inv(x):
            return 1 / x

        def norm(x):
            return x
    else:

        def norm(x):
            x = Fraction(x)
            return x.numerator % PRIME * pow(x.denominator % PRIME, -1, PRIME) % PRIME

        aug = [[norm(x) for x in r] + [norm(b)] for r, b in zip(rows, rhs)]

        def inv(x):
            return pow(x, -1, PRIME)

    piv_cols = []
    r = 0
    for c in range(ncol):
        piv = next((i for i in range(r, len(aug)) if aug[i][c] != 0), None)
        if piv is None:
            continue
        aug[r], aug[piv] = aug[piv], aug[r]
        iv = inv(aug[r][c])
        aug[r] = [x * iv if field == "Q" else x * iv % PRIME for x in aug[r]]
        for i in range(len(aug)):
            if i != r and aug[i][c] != 0:
                f = aug[i][c]
                if field == "Q":
                    aug[i] = [x - f * y for x, y in zip(aug[i], aug[r])]
                else:
                    aug[i] = [(x - f * y) % PRIME for x, y in zip(aug[i], aug[r])]
        piv_cols.append(c)
        r += 1
    consistent = all(any(x != 0 for x in row[:-1]) or row[-1] == 0 for row in aug)
    sol = [0] * ncol
    for i, c in enumerate(piv_cols):
        sol[c] = aug[i][-1]
    return {
        "rank": r,
        "nullity": ncol - r,
        "consistent": consistent,
        "particular": sol,
    }


def inverse(a: list[list[Fraction]]) -> list[list[Fraction]]:
    """Exact inverse of a square rational matrix."""
    n = len(a)
    aug = [list(a[i]) + [Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    for c in range(n):
        piv = next(i for i in range(c, n) if aug[i][c] != 0)
        aug[c], aug[piv] = aug[piv], aug[c]
        iv = 1 / aug[c][c]
        aug[c] = [x * iv for x in aug[c]]
        for i in range(n):
            if i != c and aug[i][c] != 0:
                f = aug[i][c]
                aug[i] = [x - f * y for x, y in zip(aug[i], aug[c])]
    return [row[n:] for row in aug]


def rank_q(a: list[list]) -> int:
    """Exact rank over Q."""
    if not a or not a[0]:
        return 0
    return rref_solve(a, [0] * len(a), "Q")["rank"]


# ---------------------------------------------------------------- the L1 problem


class Instance:
    """Data (E, S, D, p) of the linear transverse problem.

    Basis of E indexed 0..n-1 with ghost degrees deg[i]; q may pair i, j only if
    deg[i] + deg[j] == kappa; graded symmetry q[j][i] = (-1)^{|i||j|} q[i][j].
    BS: n x k matrix (columns: basis of S); D: n x r matrix (columns: D of a basis
    of the parameter space L); p: k x k matrix of the form on S.
    """

    def __init__(self, deg, kappa, BS, D, p, label):
        self.deg, self.kappa, self.BS, self.D, self.p = deg, kappa, BS, D, p
        self.n, self.k, self.r = len(deg), len(BS[0]), len(D[0])
        self.label = label

    def allowed(self, i: int, j: int) -> bool:
        return self.deg[i] + self.deg[j] == self.kappa

    def sign(self, i: int, j: int) -> int:
        return -1 if (self.deg[i] % 2 and self.deg[j] % 2) else 1


def unknowns(inst: Instance, symmetric: bool):
    """Parametrize q: dict (i, j) -> list of (unknown index, coefficient)."""
    idx, param = {}, {}
    for i in range(inst.n):
        for j in range(inst.n):
            if not inst.allowed(i, j):
                continue
            if symmetric:
                a, b = min(i, j), max(i, j)
                s = 1 if i <= j else inst.sign(i, j)
                if a == b and inst.sign(a, a) == -1:
                    continue  # odd diagonal entry vanishes by graded symmetry
                if (a, b) not in idx:
                    idx[(a, b)] = len(idx)
                param[(i, j)] = [(idx[(a, b)], s)]
            else:
                idx[(i, j)] = len(idx)
                param[(i, j)] = [(idx[(i, j)], 1)]
    return param, len(idx)


def equations(inst: Instance, symmetric: bool):
    """Rows of the linear system q(D l, e_j) = 0, BS^T q BS = p."""
    param, nu = unknowns(inst, symmetric)
    rows, rhs = [], []

    def bilinear_row(u, v):
        row = [Fraction(0)] * nu
        for (i, j), terms in param.items():
            coef = u[i] * v[j]
            if coef:
                for t, s in terms:
                    row[t] += s * coef
        return row

    basis = [[Fraction(int(a == b)) for a in range(inst.n)] for b in range(inst.n)]
    for lam in range(inst.r):
        dl = [inst.D[i][lam] for i in range(inst.n)]
        for j in range(inst.n):
            rows.append(bilinear_row(dl, basis[j]))
            rhs.append(Fraction(0))
    for a in range(inst.k):
        sa = [inst.BS[i][a] for i in range(inst.n)]
        for b in range(inst.k):
            sb = [inst.BS[i][b] for i in range(inst.n)]
            rows.append(bilinear_row(sa, sb))
            rhs.append(inst.p[a][b])
    return rows, rhs, param, nu


def projector_form(inst: Instance) -> list[list[Fraction]]:
    """q0 = P^T p P by coordinates: x = BS s + Dcols t, q0(x, y) = p(s_x, s_y).

    Independent of the linear solve: uses only the inverse of [BS | basis of im D].
    """
    dcols = column_basis(inst.D)
    full = [inst.BS[i] + dcols[i] for i in range(inst.n)]
    cinv = inverse(full)
    C = cinv[: inst.k]  # k x n: x -> s_x
    return matmul(matmul(transpose(C), inst.p), C)


def column_basis(m: list[list[Fraction]]) -> list[list[Fraction]]:
    """Columns of m forming a basis of its column space (greedy, exact)."""
    n, cols, chosen = len(m), [], []
    for c in range(len(m[0])):
        trial = chosen + [[m[i][c] for i in range(n)]]
        if rank_q(transpose(trial)) == len(trial):
            chosen = trial
    for i in range(n):
        cols.append([chosen[c][i] for c in range(len(chosen))])
    return cols


def satisfies(inst: Instance, q: list[list[Fraction]], symmetric: bool) -> bool:
    """Exact test of the hypotheses of L1 on a candidate matrix q."""
    n = inst.n
    for i in range(n):
        for j in range(n):
            if q[i][j] != 0 and not inst.allowed(i, j):
                return False
            if symmetric and q[j][i] != inst.sign(i, j) * q[i][j]:
                return False
    qd = matmul(transpose(inst.D), q)  # rows: q(D l, .)
    if any(x != 0 for row in qd for x in row):
        return False
    return matmul(matmul(transpose(inst.BS), q), inst.BS) == inst.p


def kernel_dim(m: list[list[Fraction]]) -> int:
    """dim ker of a square matrix (as a form: x with q(x, .) = 0)."""
    return len(m) - rank_q(m)


# ---------------------------------------------------------------- instance builders


def rand_sym_form(rng, deg, kappa, rank_drop=0):
    """Random graded-symmetric form on a graded basis; rank lowered if asked."""
    n = len(deg)
    f = [[Fraction(0)] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            if deg[i] + deg[j] != kappa:
                continue
            if i == j and deg[i] % 2:
                continue
            x = rand_rat(rng)
            f[i][j] = x
            f[j][i] = (-1 if deg[i] % 2 and deg[j] % 2 else 1) * x
    if rank_drop:
        # restrict to a random complement of a rank_drop-dim subspace: f -> R^T f R
        # with R killing rank_drop directions of one homogeneous block
        g0 = deg[0]
        block = [i for i in range(n) if deg[i] == g0]
        kill = block[:rank_drop]
        R = [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]
        for i in kill:
            R[i][i] = Fraction(0)
        A = rand_invertible_blockwise(rng, deg)
        T = matmul(R, A)
        f = matmul(matmul(transpose(T), f), T)
    return f


def rand_invertible_blockwise(rng, deg):
    """Random invertible matrix preserving the ghost degree."""
    n = len(deg)
    while True:
        a = [
            [rand_rat(rng) if deg[i] == deg[j] else Fraction(0) for j in range(n)]
            for i in range(n)
        ]
        if rank_q(a) == n:
            return a


def build_abstract(rng, dims_s, dims_d, kappa, rank_drop=0, label=""):
    """E graded by degrees in dims_s (dim of S per degree) + dims_d (rank D per degree).

    S and im D are random subspaces of each homogeneous block, transverse; D has one
    extra column in the first block (non-injective: ker D is irrelevant to L1).
    """
    degs = sorted(set(dims_s) | set(dims_d))
    deg = []
    for g in degs:
        deg += [g] * (dims_s.get(g, 0) + dims_d.get(g, 0))
    n = len(deg)
    A = rand_invertible_blockwise(rng, deg)  # random frame: columns adapted to blocks
    s_cols, d_cols = [], []
    pos = 0
    for g in degs:
        ks, kd = dims_s.get(g, 0), dims_d.get(g, 0)
        s_cols += list(range(pos, pos + ks))
        d_cols += list(range(pos + ks, pos + ks + kd))
        pos += ks + kd
    BS = [[A[i][c] for c in s_cols] for i in range(n)]
    D = [[A[i][c] for c in d_cols] for i in range(n)]
    # non-injective D: append a multiple of the first D column (homogeneous)
    a = rand_rat(rng, 1, 9)
    for i in range(n):
        D[i].append(a * D[i][0])
    sdeg = [deg[c] for c in s_cols]
    p = rand_sym_form(rng, sdeg, kappa, rank_drop)
    return Instance(deg, kappa, BS, D, p, label)


# ---------------------------------------------------------------- model M


BASIS = ["lam", "chi", "ph1", "ph2", "ph3", "mu",
         "chi*", "ph1*", "ph2*", "ph3*", "mu*", "lam*"]  # fmt: skip
GH = [1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4]
FIELDS = [1, 2, 3, 4, 5]  # chi, ph1, ph2, ph3, mu inside H_2
PHYS = [2, 3, 4]  # ph1..ph3
NOCHI = [2, 3, 4, 5]  # span{ph, mu}


def model(rng: random.Random, degenerate: bool = False) -> dict:
    """Random instance of the finite model M (record 102, section Finite model M).

    Field indices refer to BASIS.  c: cubic on NOCHI; M: 3x3 on PHYS (l_2(x, lam)
    = M x); V4free on NOCHI (two fourth powers if degenerate); V4chi fixed by O(g^2)
    relation.
    """
    c = {}
    for t in combinations_with_replacement(NOCHI, 3):
        x = rand_rat(rng)
        for perm in set(permutations(t)):
            c[perm] = x
    M = {(a, b): rand_rat(rng) for a in PHYS for b in PHYS}  # M[(y, x)]
    v4 = {}
    if degenerate:
        # V4free = sum of two fourth powers of random linear forms on span{ph, mu}:
        # rank <= 2 on Sym^2, so ker p grows (record 102, degenerate variant)
        forms = [{i: rand_rat(rng) for i in NOCHI} for _ in range(2)]
        for t in combinations_with_replacement(NOCHI, 4):
            x = sum(w[t[0]] * w[t[1]] * w[t[2]] * w[t[3]] for w in forms)
            for perm in set(permutations(t)):
                v4[perm] = x
    else:
        for t in combinations_with_replacement(NOCHI, 4):
            x = rand_rat(rng)
            for perm in set(permutations(t)):
                v4[perm] = x
    return {"c": c, "M": M, "v4free": v4}


def Mvec(Mx: dict, psi: dict) -> dict:
    """(M psi)_y = sum_x M_yx psi_x on PHYS; M chi = M mu = 0."""
    return {y: sum(Mx[(y, x)] * psi.get(x, 0) for x in PHYS) for y in PHYS}


def cubic(c: dict, a: dict, b: dict, d: dict):
    """c(a, b, d) for vectors given as dicts on NOCHI."""
    return sum(
        c[(i, j, k)] * a.get(i, 0) * b.get(j, 0) * d.get(k, 0)
        for i in NOCHI
        for j in NOCHI
        for k in NOCHI
    )


def v4chi_tensor(mdl: dict, scale=1) -> dict:
    """Components V4chi(chi, a, b, c) = -[c(Ma,b,c)+c(Mb,c,a)+c(Mc,a,b)], symmetrized."""
    out = {}
    e = {i: {i: 1} for i in NOCHI}
    for a, b, d in combinations_with_replacement(NOCHI, 3):
        val = -(
            cubic(mdl["c"], Mvec(mdl["M"], e[a]), e[b], e[d])
            + cubic(mdl["c"], Mvec(mdl["M"], e[b]), e[d], e[a])
            + cubic(mdl["c"], Mvec(mdl["M"], e[d]), e[a], e[b])
        )
        for perm in set(permutations((1, a, b, d))):
            out[perm] = scale * val
    return out


def v4_full(mdl: dict, scale=1) -> dict:
    """V_4 on the (2,2,2,2) block: V4free + scale * V4chi."""
    v = dict(mdl["v4free"])
    for key, val in v4chi_tensor(mdl, scale).items():
        v[key] = v.get(key, 0) + val
    return v


def q_operator():
    """Q as a 12 x 12 matrix (column = image): Q lam = chi, Q chi* = -lam*, Q mu = mu*."""
    n = len(BASIS)
    Q = [[0] * n for _ in range(n)]
    Q[1][0] = 1
    Q[11][6] = -1
    Q[10][5] = 1
    return Q


def pairing(i: int, j: int) -> int:
    """<e_i, e_j>: 1 on (e, e*) and (e*, e), zero elsewhere."""
    dual = {0: 11, 1: 6, 2: 7, 3: 8, 4: 9, 5: 10}
    dual.update({v: k for k, v in list(dual.items())})
    return 1 if dual[i] == j else 0


# ---------------------------------------------------------------- checks


def check_c1_search() -> None:
    details, ok = [], True
    for seed in SEEDS:
        rng = random.Random(seed)
        insts = [
            build_abstract(rng, {4: 3}, {4: 2}, 8, 0, "even, p non-degenerate"),
            build_abstract(rng, {4: 3}, {4: 2}, 8, 1, "even, p of rank 2"),
            build_abstract(
                rng, {3: 1, 4: 2, 5: 1}, {3: 1, 4: 1, 5: 1}, 8, 0, "graded 3/4/5"
            ),
        ]
        insts.append(model_instance(rng))
        insts.append(model_instance(rng, degenerate=True))
        for inst in insts:
            rows, rhs, param, nu = equations(inst, symmetric=True)
            field = "Q" if nu <= 60 else "P"
            res = rref_solve(rows, rhs, field)
            q0 = projector_form(inst)
            exist = satisfies(inst, q0, symmetric=True)
            # kernel: ker q0 = ker p (+) im D
            kq, kp, rd = kernel_dim(q0), kernel_dim(inst.p), rank_q(inst.D)
            imd_in = all(x == 0 for row in matmul(transpose(inst.D), q0) for x in row)
            kerp_in = kernel_inclusion(inst, q0)
            # falsifiability probe: projector along a wrong complement
            wrong = wrong_projector_form(inst, rng)
            probe = not satisfies(inst, wrong, symmetric=True)
            good = (
                res["nullity"] == 0
                and exist
                and kq == kp + rd
                and imd_in
                and kerp_in
                and probe
            )
            ok &= good
            details.append(
                f"seed {seed} [{inst.label}] n={inst.n} unknowns={nu} "
                f"({'exact Q' if field == 'Q' else 'mod 2^61-1'}): nullity "
                f"{res['nullity']}, P^T p P solves={exist}, dim ker q={kq} = "
                f"dim ker p {kp} + rank D {rd}, wrong-P rejected={probe}"
            )
    record(
        "C1-search",
        ok,
        "solution space = {P^T p P} in every instance\n    " + "\n    ".join(details),
    )


def kernel_inclusion(inst: Instance, q0) -> bool:
    """BS . ker p lies in ker q0."""
    k = inst.k
    res = nullspace_q(inst.p)
    for v in res:
        x = [sum(inst.BS[i][a] * v[a] for a in range(k)) for i in range(inst.n)]
        if any(sum(x[i] * q0[i][j] for i in range(inst.n)) != 0 for j in range(inst.n)):
            return False
    return True


def nullspace_q(m: list[list[Fraction]]) -> list[list[Fraction]]:
    """Exact null space basis of a matrix."""
    n = len(m[0])
    aug = [list(r) for r in m]
    piv, r = [], 0
    for c in range(n):
        p = next((i for i in range(r, len(aug)) if aug[i][c] != 0), None)
        if p is None:
            continue
        aug[r], aug[p] = aug[p], aug[r]
        iv = 1 / aug[r][c]
        aug[r] = [x * iv for x in aug[r]]
        for i in range(len(aug)):
            if i != r and aug[i][c] != 0:
                f = aug[i][c]
                aug[i] = [x - f * y for x, y in zip(aug[i], aug[r])]
        piv.append(c)
        r += 1
    free = [c for c in range(n) if c not in piv]
    basis = []
    for fc in free:
        v = [Fraction(0)] * n
        v[fc] = Fraction(1)
        for i, pc in enumerate(piv):
            v[pc] = -aug[i][fc]
        basis.append(v)
    return basis


def wrong_projector_form(inst: Instance, rng) -> list[list[Fraction]]:
    """P'^T p P' with P' the projector along a tilted complement im D' != im D.

    D' = (basis of im D) + BS R, R random and degree-preserving: q' satisfies
    q' o D' = 0 and q'|_S = p, and must fail q' o D = 0 (falsifiability probe).
    """
    dcols = column_basis(inst.D)
    sdeg = [next(inst.deg[i] for i in range(inst.n) if inst.BS[i][a] != 0)
            for a in range(inst.k)]  # fmt: skip
    ddeg = [next(inst.deg[i] for i in range(inst.n) if dcols[i][c] != 0)
            for c in range(len(dcols[0]))]  # fmt: skip
    R = [[rand_rat(rng, 1, 9) if sdeg[a] == ddeg[c] else Fraction(0)
          for c in range(len(ddeg))] for a in range(inst.k)]  # fmt: skip
    tilt = [
        [dcols[i][c] + sum(inst.BS[i][a] * R[a][c] for a in range(inst.k))
         for c in range(len(ddeg))]
        for i in range(inst.n)
    ]  # fmt: skip
    fake = Instance(inst.deg, inst.kappa, inst.BS, tilt, inst.p, inst.label)
    return projector_form(fake)


def model_instance(rng: random.Random, degenerate: bool = False) -> Instance:
    """S = Sym^2 H_2 of M with p = V_4 on it, E = S (+) H_1^H_3, D random."""
    mdl = model(rng, degenerate)
    v4 = v4_full(mdl)
    pairs = list(combinations_with_replacement(FIELDS, 2))  # 15

    def mult(a, b):
        return 2 if a != b else 1

    p = [
        [
            Fraction(mult(a, b) * mult(c, d)) * v4.get((a, b, c, d), 0)
            for (c, d) in pairs
        ]
        for (a, b) in pairs
    ]
    n = len(pairs) + 5  # + H_1 ^ H_3 (lam (x) y*, y* in H_3)
    BS = [[Fraction(int(i == a)) for a in range(len(pairs))] for i in range(n)]
    D = rand_mat(rng, n, 5)
    deg = [4] * n
    tag = ", degenerate" if degenerate else ""
    return Instance(deg, 8, BS, D, p, f"model M{tag}: S = Sym^2 H_2, p = p_{{2,2}}")


def check_c1_break_sym() -> None:
    details, failed_as_expected = [], True
    for seed in SEEDS:
        rng = random.Random(seed + 1)
        inst = build_abstract(rng, {4: 3}, {4: 2}, 8, 0, "even")
        rows, rhs, param, nu = equations(inst, symmetric=False)
        res = rref_solve(rows, rhs, "Q")
        expected = inst.k * rank_q(inst.D)
        unique = res["nullity"] == 0
        failed_as_expected &= (not unique) and res["nullity"] == expected
        details.append(
            f"seed {seed}: non-symmetric q, nullity {res['nullity']} "
            f"(dim S * rank D = {expected}), uniqueness test "
            f"{'PASS' if unique else 'FAIL (as expected)'}"
        )
    record(
        "C1-break-sym",
        failed_as_expected,
        "dropping the symmetry of q enlarges the solution space\n    "
        + "\n    ".join(details),
    )


def check_c1_break_transverse() -> None:
    details, ok = [], True
    for seed in SEEDS:
        rng = random.Random(seed + 2)
        # (a) S + im D proper: drop one D direction (E keeps its dimension)
        inst = build_abstract(rng, {4: 3}, {4: 2}, 8, 0, "even")
        D_small = [[inst.D[i][0]] for i in range(inst.n)]
        a = Instance(inst.deg, 8, inst.BS, D_small, inst.p, "S + im D proper")
        rows, rhs, _, nu = equations(a, symmetric=True)
        ra = rref_solve(rows, rhs, "Q")
        # nullity binom(dim W + 1, 2) + dim W * dim S = 1 + 3 for dim W = 1, dim S = 3
        grow = ra["consistent"] and ra["nullity"] == 4
        # (b) S and im D meet: add s0 = first S basis vector to im D
        D_meet = [inst.D[i][:2] + [inst.BS[i][0]] for i in range(inst.n)]
        b = Instance(inst.deg, 8, inst.BS, D_meet, inst.p, "S meets im D")
        rows, rhs, _, _ = equations(b, symmetric=True)
        rb = rref_solve(rows, rhs, "Q")
        # (b') same with p chosen so that s0 lies in ker p
        p_k = [row[:] for row in inst.p]
        for j in range(inst.k):
            p_k[0][j] = Fraction(0)
            p_k[j][0] = Fraction(0)
        bk = Instance(inst.deg, 8, inst.BS, D_meet, p_k, "S meets im D in ker p")
        rows, rhs, _, _ = equations(bk, symmetric=True)
        rbk = rref_solve(rows, rhs, "Q")
        good = (
            grow
            and (not rb["consistent"])
            and rbk["consistent"]
            and rbk["nullity"] == 0
        )
        ok &= good
        details.append(
            f"seed {seed}: (a) consistent={ra['consistent']}, nullity "
            f"{ra['nullity']} (expected 4) -> uniqueness FAIL (as expected); (b) p generic: "
            f"consistent={rb['consistent']} -> FAIL (as expected); (b') "
            f"S cap im D in ker p: consistent={rbk['consistent']}, nullity "
            f"{rbk['nullity']}"
        )
    record(
        "C1-break-transverse",
        ok,
        "without transversality L1's conclusion fails in both directions\n    "
        + "\n    ".join(details),
    )


def rat(x) -> sp.Rational:
    """Exact sympy rational from an int or Fraction."""
    x = Fraction(x)
    return sp.Rational(x.numerator, x.denominator)


def check_c2_gauge() -> None:
    n = len(BASIS)
    Q = q_operator()
    Q2 = [
        [sum(Q[i][k] * Q[k][j] for k in range(n)) for j in range(n)] for i in range(n)
    ]
    nil = all(x == 0 for row in Q2 for x in row)
    # <Q e_i, e_j> = (-1)^{|e_i|} <e_i, Q e_j>
    sa = all(
        sum(Q[k][i] * pairing(k, j) for k in range(n))
        == (-1) ** (GH[i] % 2) * sum(pairing(i, k) * Q[k][j] for k in range(n))
        for i in range(n)
        for j in range(n)
    )
    g, eps = sp.symbols("g epsilon")
    psi = {i: sp.Symbol(f"psi_{BASIS[i]}") for i in FIELDS}
    details, ok = [f"Q^2 = 0: {nil}; Q self-adjoint: {sa}"], nil and sa
    for seed in SEEDS:
        rng = random.Random(seed + 3)
        mdl = model(rng)
        for scale, label, expect_ok in ((1, "M", True), (0, "V4chi dropped", False),
                                        (2, "V4chi doubled", False)):  # fmt: skip
            v4 = v4_full(mdl, scale)
            S = sp.Rational(1, 2) * psi[5] ** 2
            S += (
                g
                / 6
                * sum(
                    rat(val) * psi[i] * psi[j] * psi[k]
                    for (i, j, k), val in mdl["c"].items()
                )
            )
            S += (
                g**2
                / 24
                * sum(
                    rat(val) * psi[i] * psi[j] * psi[k] * psi[m]
                    for (i, j, k, m), val in v4.items()
                )
            )
            dpsi = {i: sp.Integer(0) for i in FIELDS}
            dpsi[1] = eps  # Q Lambda = eps chi
            for y in PHYS:  # g l_2(Psi, Lambda) = eps g M Psi, M chi = M mu = 0
                dpsi[y] += eps * g * sum(rat(mdl["M"][(y, x)]) * psi[x] for x in PHYS)
            dS = sp.expand(sum(sp.diff(S, psi[i]) * dpsi[i] for i in FIELDS))
            coeffs = [sp.expand(dS.coeff(g, o)) for o in range(3)]
            inv = all(cf == 0 for cf in coeffs)
            if expect_ok:
                ok &= inv
            else:
                ok &= not inv
            details.append(
                f"seed {seed} [{label}]: delta S at g^0,g^1,g^2 vanishes = {inv}"
                + (
                    ""
                    if expect_ok
                    else f" -> {'FAIL (as expected)' if not inv else 'unexpected PASS'}"
                )
            )
        # ker p of the model and of the degenerate variant
        for degen in (False, True):
            m2 = model(random.Random(seed + 4), degenerate=degen)
            v4 = v4_full(m2)
            pairs = list(combinations_with_replacement(FIELDS, 2))
            mult = [2 if a != b else 1 for a, b in pairs]
            pm = [
                [Fraction(mult[r] * mult[s]) * v4.get(pairs[r] + pairs[s], 0)
                 for s in range(len(pairs))]
                for r in range(len(pairs))
            ]  # fmt: skip
            chichi = pairs.index((1, 1))
            in_ker = all(pm[chichi][s] == 0 for s in range(len(pairs)))
            ok &= in_ker
            details.append(
                f"seed {seed} [{'degenerate' if degen else 'generic'} V4free]: "
                f"dim Sym^2 H_2 = {len(pairs)}, dim ker p = {kernel_dim(pm)}, "
                f"chi(x)chi in ker p = {in_ker}"
            )
    record("C2-gauge", ok, "model M\n    " + "\n    ".join(details))


# ---------------------------------------------------------------- L2-model (1b)
#
# Coordinates of the HS solve (record 102, Block L2-model, eq. (L2.1)):
#   0..4    psi_e, e in (chi, ph1, ph2, ph3, mu)   (BASIS index - 1), weight 1
#   5..19   sigma_ab = Sigma_2^{ab}, a <= b, a, b in 0..4, weight 2
#   20      epsilon (Lambda = epsilon lam), weight 1
#   21..25  theta_f (Lambda_2 = sum_f theta_f lam ^ e_f), weight 2
# g is set to 1 and restored from the weight (shift s carries g^s).

NPSI = 5
PAIRS = [(a, b) for a in range(NPSI) for b in range(a, NPSI)]
SIG = {pr: NPSI + k for k, pr in enumerate(PAIRS)}
NFIELD = NPSI + len(PAIRS)  # 20
EPS = NFIELD
THETA = [NFIELD + 1 + f for f in range(NPSI)]
NVAR = NFIELD + 1 + NPSI
WT = [1] * NPSI + [2] * len(PAIRS) + [1] + [2] * NPSI
MU_I, CHI_I = 4, 0
PHI_I = [1, 2, 3]
LP = 2147483647  # prime 2^31 - 1 for the modular ranks (int64-safe products)


def sig(a: int, b: int) -> int:
    """Variable index of Sigma_2^{ab} = Sigma_2^{ba}."""
    return SIG[(min(a, b), max(a, b))]


def pmul(p: dict, q: dict) -> dict:
    """Product of polynomials {sorted var tuple: coefficient}."""
    out: dict = {}
    for k1, v1 in p.items():
        for k2, v2 in q.items():
            k = tuple(sorted(k1 + k2))
            out[k] = out.get(k, 0) + v1 * v2
    return {k: v for k, v in out.items() if v != 0}


def padd(p: dict, q: dict, c=1) -> dict:
    """p + c q."""
    out = dict(p)
    for k, v in q.items():
        out[k] = out.get(k, 0) + c * v
    return {k: v for k, v in out.items() if v != 0}


def pdiff(p: dict, v: int) -> dict:
    """Partial derivative with respect to variable v."""
    out: dict = {}
    for k, c in p.items():
        n = k.count(v)
        if n:
            lst = list(k)
            lst.remove(v)
            kk = tuple(lst)
            out[kk] = out.get(kk, 0) + n * c
    return out


def wt(key: tuple) -> int:
    """Weight of a monomial."""
    return sum(WT[v] for v in key)


def hs_action(mdl: dict) -> dict:
    """Return {w: S^(w)} for the HS action (L2.1) on model M at g = 1."""
    S2 = {(MU_I, MU_I): Fraction(1, 2)}
    S3: dict = {}
    for (i, j, k), val in mdl["c"].items():  # BASIS indices in NOCHI
        key = tuple(sorted((i - 1, j - 1, k - 1)))
        S3[key] = S3.get(key, 0) + Fraction(val) / 6
    v4 = v4_full(mdl)
    S4: dict = {}
    for (a, b, c, d), val in v4.items():
        a, b, c, d = a - 1, b - 1, c - 1, d - 1
        k1 = tuple(sorted((sig(a, b), sig(c, d))))  # -1/24 V4(Sigma, Sigma)
        S4[k1] = S4.get(k1, 0) - Fraction(val) / 24
        k2 = tuple(sorted((sig(a, b), c, d)))  # +2/24 V4(Sigma, Psi^2)
        S4[k2] = S4.get(k2, 0) + Fraction(val) * 2 / 24
    return {2: S2, 3: S3, 4: {k: v for k, v in S4.items() if v != 0}}


def param_monomials(weight: int) -> list[tuple]:
    """Monomials linear in (epsilon, theta), of total weight `weight`, in fields."""
    out = []
    for par in [EPS] + THETA:
        rest = weight - WT[par]
        if rest < 0:
            continue

        # field monomials of weight rest (psi weight 1, sigma weight 2)
        def rec(start: int, left: int, acc: tuple):
            if left == 0:
                out.append(tuple(sorted(acc + (par,))))
                return
            for v in range(start, NFIELD):
                if WT[v] <= left:
                    rec(v, left - WT[v], acc + (v,))

        rec(0, rest, ())
    return out


def kernel_basis_p(mdl: dict) -> list[dict]:
    """Basis of ker p on Sym^2 H_2, as dicts {sigma var: coefficient}."""
    v4 = v4_full(mdl)
    rows = []
    for c, d in PAIRS:
        rows.append(
            [Fraction(1 if a == b else 2) * v4.get((a + 1, b + 1, c + 1, d + 1), 0)
             for a, b in PAIRS]
        )  # fmt: skip
    basis = nullspace_q(rows)
    return [{SIG[PAIRS[r]]: x for r, x in enumerate(v) if x != 0} for v in basis]


class L2Solve:
    """The truncated solve of record 102, Block L2-model, on one model instance."""

    def __init__(self, mdl: dict) -> None:
        self.mdl = mdl
        self.S = hs_action(mdl)
        self.Sfull: dict = {}
        for w in (2, 3, 4):
            self.Sfull = padd(self.Sfull, self.S[w])
        self.E = [pdiff(self.Sfull, i) for i in range(NFIELD)]
        self.dep = {w: {v for k in self.S[w] for v in k} for w in (2, 3, 4)}
        # unknowns: (field i, monomial m) with shift 0..2
        self.unknowns = []
        for i in range(NFIELD):
            for s in (0, 1, 2):
                for m in param_monomials(WT[i] + s):
                    self.unknowns.append((i, m))
        self.uidx = {u: n for n, u in enumerate(self.unknowns)}
        # determined: some S^(w), w <= 4 - s, depends on the field
        self.det = [
            n
            for n, (i, m) in enumerate(self.unknowns)
            if any(i in self.dep[w] for w in (2, 3, 4) if w <= 4 - (wt(m) - WT[i]))
        ]
        self.didx = {n: k for k, n in enumerate(self.det)}
        self.cols = [self.column(i, m) for (i, m) in self.unknowns]

    def column(self, i: int, m: tuple) -> dict:
        """delta S monomials (weight <= 4) of the unknown delta phi^i = m."""
        return {k: v for k, v in pmul({m: 1}, self.E[i]).items() if wt(k) <= 4}

    def undetermined_silent(self) -> bool:
        """Every coefficient in U (L2.2) enters no equation at W <= 4."""
        dset = set(self.det)
        return all(not self.cols[n] for n in range(len(self.unknowns)) if n not in dset)

    def matrix_mod(self) -> np.ndarray:
        """Coefficient matrix (rows: monomials of delta S; cols: determined)."""
        rows: dict = {}
        for k, n in enumerate(self.det):
            for key, v in self.cols[n].items():
                rows.setdefault(key, {})[k] = v
        A = np.zeros((len(rows), len(self.det)), dtype=np.int64)
        for r, (_, entries) in enumerate(rows.items()):
            for k, v in entries.items():
                A[r, k] = modp(v)
        return A

    def vector(self, delta: dict, truncate: bool = True) -> dict:
        """Coordinates {unknown index: coeff} of a transformation {i: poly}."""
        out: dict = {}
        for i, poly in delta.items():
            for m, c in poly.items():
                s = wt(m) - WT[i]
                if truncate and s > 2:
                    continue
                n = self.uidx[(i, m)]
                out[n] = out.get(n, 0) + c
        return {n: c for n, c in out.items() if c != 0}

    def solves(self, vec: dict) -> bool:
        """Exact check: the truncated variation of S vanishes (all coefficients)."""
        tot: dict = {}
        for n, c in vec.items():
            tot = padd(tot, self.cols[n], c)
        return not tot

    def projected(self, vec: dict) -> dict:
        """Projection onto the determined coefficients."""
        return {self.didx[n]: c for n, c in vec.items() if n in self.didx}

    # --- the three classes -------------------------------------------------

    def gauge_class(self) -> list[dict]:
        """(G): composite law of delta Psi = Lambda'(chi + M Psi), Lambda' weight 1..3."""
        Mx = self.mdl["M"]
        out = []
        for r in (1, 2, 3):
            for lam in param_monomials(r):
                dpsi = {CHI_I: {lam: Fraction(1)}}
                for y in PHI_I:  # (M Psi)_y = sum_x M_yx psi_x (BASIS y+1, x+1)
                    poly = {}
                    for x in PHI_I:
                        mxy = Fraction(Mx[(y + 1, x + 1)])
                        if mxy:
                            poly = padd(poly, {tuple(sorted(lam + (x,))): mxy})
                    dpsi[y] = poly
                delta = dict(dpsi)
                for a, b in PAIRS:  # dSigma^{ab} = dpsi_a psi_b + psi_a dpsi_b
                    poly = padd(
                        pmul(dpsi.get(a, {}), {(b,): 1}),
                        pmul({(a,): 1}, dpsi.get(b, {})),
                    )
                    if poly:
                        delta[SIG[(a, b)]] = poly
                out.append(delta)
        return out

    def kernel_class(self) -> list[dict]:
        """(K): delta Sigma_2 = m N, N in ker p, m in {eps psi_a, theta_f}."""
        out = []
        for N in kernel_basis_p(self.mdl):
            for m in param_monomials(2):  # eps psi_a, theta_f
                out.append({i: {m: c} for i, c in N.items()})
        return out

    def trivial_class(self, sym: bool = False, pairs: str = "all") -> list[dict]:
        """(T): delta phi^i = mu^{ij} E_j, mu antisymmetric (symmetric if sym)."""
        out = []
        for i in range(NFIELD):
            for j in range(i + 1, NFIELD):
                kind = ("p" if i < NPSI else "s") + ("p" if j < NPSI else "s")
                if pairs == "no-mixed" and kind in ("ps", "sp"):
                    continue
                if pairs == "one-sided" and kind in ("ps", "sp"):
                    # reviewer's failure mode: delta Psi ~ E_Sigma only, no partner
                    for r in (1, 2, 3):
                        for m in param_monomials(r):
                            out.append({i: pmul({m: 1}, self.E[j])})
                    continue
                for r in (1, 2, 3):
                    for m in param_monomials(r):
                        out.append({
                            i: pmul({m: 1}, self.E[j]),
                            j: pmul({m: (1 if sym else -1)}, self.E[i]),
                        })  # fmt: skip
        return out


def modp(x) -> int:
    """Fraction -> residue modulo LP."""
    x = Fraction(x)
    return (x.numerator % LP) * pow(x.denominator % LP, LP - 2, LP) % LP


def rank_mod(A: np.ndarray) -> int:
    """Rank of an int64 matrix modulo LP (Gaussian elimination, vectorized)."""
    A = A.copy() % LP
    nrow, ncol = A.shape
    r = 0
    for c in range(ncol):
        if r == nrow:
            break
        nz = np.nonzero(A[r:, c])[0]
        if nz.size == 0:
            continue
        p = r + nz[0]
        if p != r:
            A[[r, p]] = A[[p, r]]
        inv = pow(int(A[r, c]), LP - 2, LP)
        A[r] = (A[r] * inv) % LP
        col = A[:, c].copy()
        col[r] = 0
        rows = np.nonzero(col)[0]
        if rows.size:
            A[rows] = (A[rows] - (col[rows, None] * A[r][None, :]) % LP) % LP
        r += 1
    return r


def stack_mod(vecs: list[dict], ncol: int) -> np.ndarray:
    """Rows of projected vectors modulo LP."""
    M = np.zeros((max(len(vecs), 1), ncol), dtype=np.int64)
    for r, v in enumerate(vecs):
        for k, c in v.items():
            M[r, k] = modp(c)
    return M


def l2_instances():
    """Model instances of the L2 solve: generic (seed + 3, the C2-gauge instance)
    and degenerate (seed + 4, the C2 ker-p instance), per seed."""
    for seed in SEEDS:
        for degen in (False, True):
            mdl = model(random.Random(seed + (4 if degen else 3)), degenerate=degen)
            yield seed, degen, L2Solve(mdl)


def span_rank(L: L2Solve, classes: list[list[dict]]) -> int:
    """Rank (mod LP) of the projected span of the given generator lists."""
    vecs = [L.projected(L.vector(d)) for cls in classes for d in cls]
    vecs = [x for x in vecs if x]
    return rank_mod(stack_mod(vecs, len(L.det))) if vecs else 0


def check_c3_solve(cache: dict) -> None:
    details, ok = [], True
    for seed, degen, L in l2_instances():
        G, K, T = L.gauge_class(), L.kernel_class(), L.trivial_class()
        cache[(seed, degen)] = (L, G, K, T)
        silent = L.undetermined_silent()
        A = L.matrix_mod()
        null = A.shape[1] - rank_mod(A)
        incl = {
            n: all(L.solves(L.vector(d)) for d in cls)
            for n, cls in (("G", G), ("K", K), ("T", T))
        }
        rG, rK, rT = (span_rank(L, [c]) for c in (G, K, T))
        rs = span_rank(L, [G, K, T])
        good = silent and all(incl.values()) and rs == null
        ok &= good
        details.append(
            f"seed {seed} [{'degenerate' if degen else 'generic'}, "
            f"dim ker p = {len(kernel_basis_p(L.mdl))}]: unknowns {len(L.unknowns)}, "
            f"determined {len(L.det)}, U silent {silent}; equations {A.shape[0]}; "
            f"dim Sol_det = {null}; exact inclusion G/K/T {incl}; "
            f"rank G {rG}, K {rK}, T {rT}, G+K+T {rs} -> "
            f"{'equal' if rs == null else 'MISMATCH'}"
        )
    record("C3-solve", ok, "L2-model truncated solve\n    " + "\n    ".join(details))


def check_c3_break(cache: dict) -> None:
    details, ok = [], True
    for (seed, degen), (L, G, K, T) in cache.items():
        A = L.matrix_mod()
        null = A.shape[1] - rank_mod(A)
        lab = f"seed {seed} [{'degenerate' if degen else 'generic'}]"
        # (a) mu symmetric: the generators are no longer solutions
        Tsym = L.trivial_class(sym=True)
        bad = sum(not L.solves(L.vector(d)) for d in Tsym)
        # (b) one-sided delta Psi ~ E_Sigma without partner delta Sigma ~ E_Psi
        Tone = [d for d in L.trivial_class(pairs="one-sided") if min(d) < NPSI]
        bad1 = sum(not L.solves(L.vector(d)) for d in Tone)
        # (c) mixed entries dropped (only psi-psi and sigma-sigma mu): span shrinks
        r_nomix = span_rank(L, [G, K, L.trivial_class(pairs="no-mixed")])
        # (d) kernel-shift class dropped
        r_nok = span_rank(L, [G, T])
        fa, fb = bad > 0, bad1 > 0
        fc, fd = r_nomix < null, r_nok < null
        ok &= fa and fb and fc and (fd or not degen)
        details.append(
            f"{lab}: (a) mu symmetric: {bad}/{len(Tsym)} generators violate dS = 0 "
            f"-> {'FAIL (as expected)' if fa else 'unexpected PASS'}; "
            f"(b) one-sided dPsi ~ E_Sigma: {bad1}/{len(Tone)} violate "
            f"-> {'FAIL (as expected)' if fb else 'unexpected PASS'}; "
            f"(c) no mixed mu: rank {r_nomix} vs dim Sol_det {null} "
            f"-> {'FAIL (as expected)' if fc else 'unexpected PASS'}; "
            f"(d) no kernel shifts: rank {r_nok} vs {null} -> "
            + ("FAIL (as expected)" if fd else
               "equal (ker p = span{chi(x)chi} enters no equation)")
        )  # fmt: skip
    record("C3-break", ok, "break legs of C3-solve\n    " + "\n    ".join(details))


def subst_saddle(poly: dict, factor: int = 1, shift: dict | None = None) -> dict:
    """Substitute sigma_ab -> factor * psi_a psi_b (+ shift_ab, a kernel element)."""
    rep = {}
    for (a, b), v in SIG.items():
        r = {tuple(sorted((a, b))): Fraction(factor)}
        if shift and v in shift:
            r = padd(r, shift[v])
        rep[v] = r
    out: dict = {}
    for k, c in poly.items():
        term = {(): Fraction(c)}
        for x in k:
            term = pmul(term, rep[x]) if x in rep else pmul(term, {(x,): 1})
        out = padd(out, term)
    return out


def check_c3_restriction(cache: dict) -> None:
    details, ok = [], True
    rng = random.Random(SEEDS[0] + 11)
    for (seed, degen), (L, G, K, T) in cache.items():
        lab = f"seed {seed} [{'degenerate' if degen else 'generic'}]"
        # S_<=4(psi) computed directly from the vertices (independent of the HS form)
        S_trunc = {(MU_I, MU_I): Fraction(1, 2)}
        S_trunc = padd(S_trunc, L.S[3])
        for (a, b, c, d), val in v4_full(L.mdl).items():
            k = tuple(sorted((a - 1, b - 1, c - 1, d - 1)))
            S_trunc[k] = S_trunc.get(k, 0) + Fraction(val) / 24
        S_trunc = {k: x for k, x in S_trunc.items() if x != 0}
        # a random exact solution: combination of G, K, T plus a random U part
        # generators with a non-zero determined part (the part the truncated action
        # sees), the constant-parameter gauge law always included
        visible = [d for d in G + K + T if L.projected(L.vector(d))]
        gens = [G[0]] + visible  # all of them, with random coefficients
        delta: dict = {}
        for d in gens:
            c = rand_rat(rng)
            for i, poly in d.items():
                delta[i] = padd(delta.get(i, {}), poly, c)
        dset = set(L.det)
        for n in rng.sample([n for n in range(len(L.unknowns)) if n not in dset], 30):
            i, m = L.unknowns[n]
            delta[i] = padd(delta.get(i, {}), {m: rand_rat(rng)})
        # truncate delta to s <= 2 (as in the solve); keep psi components
        dpsi = {
            i: {m: c for m, c in delta.get(i, {}).items() if wt(m) - WT[i] <= 2}
            for i in range(NPSI)
        }
        vec = L.vector({i: p for i, p in delta.items()})
        assert L.solves(vec)

        def dS_el(Sel: dict, factor: int, shift=None) -> dict:
            tot: dict = {}
            for i in range(NPSI):
                dres = subst_saddle(dpsi[i], factor, shift)
                tot = padd(tot, pmul(pdiff(Sel, i), dres))
            return {k: v for k, v in tot.items() if wt(k) <= 4}

        kshift = None
        if degen:  # saddle on representatives: Psi^2 + N, N in ker p (field indep.
            # N must carry weight 2 to keep the filtration: use theta-free psi psi N)
            N = kernel_basis_p(L.mdl)[-1]
            kshift = {v: {(0, 1): c} for v, c in N.items()}  # psi_chi psi_ph1 N
        Sel = subst_saddle(L.Sfull, 1, kshift)  # S_el(psi) = S~(psi, Sigma_2^*)
        elim = not padd(Sel, S_trunc, -1)  # eq:hs4:eliminate on M
        r_ok = elim and not dS_el(Sel, 1, kshift)
        # break: restriction to sigma = 2 Psi^2, where d_Sigma S != 0
        Sel2 = subst_saddle(L.Sfull, 2)
        r_bad = bool(dS_el(Sel2, 2))
        # the diagonal is not preserved: dSigma - d(Psi^2) at Sigma = Psi^2
        nonpres = False
        for (a, b), v in SIG.items():
            d_psi2 = padd(pmul(delta.get(a, {}), {(b,): 1}),
                          pmul({(a,): 1}, delta.get(b, {})))  # fmt: skip
            diff = padd(subst_saddle(delta.get(v, {})), subst_saddle(d_psi2), -1)
            if {k: c for k, c in diff.items() if wt(k) <= 4}:
                nonpres = True
                break
        good = r_ok and r_bad and nonpres
        ok &= good
        details.append(
            f"{lab}: S_el = S_<=4: {elim}; delta_el S_el = 0 at W <= 4 on the saddle "
            f"{'Psi^2 + kernel shift' if degen else 'Psi^2'}: {r_ok}; "
            f"on Sigma = 2 Psi^2: {'non-zero, FAIL (as expected)' if r_bad else 'zero'}"
            f"; diagonal not preserved by delta: {nonpres}"
        )
    record("C3.3-restriction", ok, "restriction to the saddle\n    "
           + "\n    ".join(details))  # fmt: skip


# ---------------------------------------------------------------- table (C5)
#
# Ghost shifts of the building blocks (R23; conv:pairing-n): l_2 -1, l_3 -3,
# p_{2,2} +2, a contraction <.,.> of two strands -5 (non-zero only at ghost sum 5),
# c_0^- +1, b_0^- -1, L_0^- 0 (per strand).  Q-hat is excluded (brief).
OPS = {"l2": (-1, 1), "l3": (-3, 2), "pair": (-5, 2), "p22": (+2, 0)}  # (gh, -strands)
FIELDS_GH = {"Psi": (1, 2), "Sigma2": (2, 4), "Lambda2": (2, 3)}  # (strands, gh)
BLOCKS = {  # name: (fixed input, target strands, target ghost number)
    "D": ("Lambda2", 2, 4),
    "B2": ("Sigma2", 2, 3),
    "dPsi": ("Lambda2", 1, 2),
    "Lambda": ("Lambda2", 1, 1),
}
CONTENTS = [(), ("Psi",), ("Sigma2",), ("Psi", "Psi"), ("Psi", "Sigma2"),
            ("Sigma2", "Sigma2")]  # fmt: skip
MAXOPS = 5


def dress_words(n: int, k: int) -> int:
    """Number of zero-mode words of net shift k on n ordered strands, L-degree <= 1.

    Per strand: shift +1 {c0-}, 0 {1, c0- b0-}, -1 {b0-}; an L_0^- factor on at
    most one strand (1 + n choices)."""
    per = {1: 1, 0: 2, -1: 1}
    tot = 0
    for combo in product((1, 0, -1), repeat=n):
        if sum(combo) == k:
            w = 1
            for s in combo:
                w *= per[s]
            tot += w
    return tot * (1 + n)


def rows_by_search(block: str) -> set:
    """Route 1: depth-first search over operation sequences on (strands, ghost)."""
    fixed, n_out, target = BLOCKS[block]
    out = set()
    for content in CONTENTS:
        n0 = FIELDS_GH[fixed][0] + sum(FIELDS_GH[f][0] for f in content)
        g0 = FIELDS_GH[fixed][1] + sum(FIELDS_GH[f][1] for f in content)

        def dfs(n, g, ops):
            if n == n_out and abs(target - g) <= n_out:
                out.add((content, tuple(sorted(ops)), g, target - g))
            if len(ops) == MAXOPS:
                return
            for op, (dg, dn) in OPS.items():
                need = {"l2": 2, "l3": 3, "pair": 2, "p22": 2}[op]
                if n >= need and n - dn >= 1:
                    dfs(n - dn, g + dg, ops + [op])

        dfs(n0, g0, [])
    return out


def rows_by_count(block: str) -> set:
    """Route 2: non-negative integer solutions of the strand and ghost balance."""
    fixed, n_out, target = BLOCKS[block]
    out = set()
    for content in CONTENTS:
        n0 = FIELDS_GH[fixed][0] + sum(FIELDS_GH[f][0] for f in content)
        g0 = FIELDS_GH[fixed][1] + sum(FIELDS_GH[f][1] for f in content)
        for a in range(MAXOPS + 1):
            for b in range(MAXOPS + 1 - a):
                for c in range(MAXOPS + 1 - a - b):
                    for d in range(MAXOPS + 1 - a - b - c):
                        if n0 - a - 2 * b - 2 * c != n_out:
                            continue
                        g = g0 - a - 3 * b - 5 * c + 2 * d
                        if abs(target - g) > n_out:
                            continue
                        # every order is feasible: strand counts decrease
                        # monotonically to n_out >= 1, and p22 can act first
                        ops = ["l2"] * a + ["l3"] * b + ["pair"] * c + ["p22"] * d
                        out.add((content, tuple(sorted(ops)), g, target - g))
    return out


def realizable_in_M(block: str, content: tuple, ops: tuple) -> bool:
    """Level-matched row realized on M's grading (per-strand ghost numbers 1..4).

    Supports of M (record 102, Finite model M): l_2 on strand ghosts (2,2) -> 3,
    (2,1) -> 2, (2,3) -> 4, (3,1) -> 3; l_3 on (2,2,2) -> 3; p_{2,2} on (2,2) ->
    (3,3); a contraction needs ghost sum 5.  Strands: Psi (2), Sigma2 (2,2),
    Lambda2 (1,2); target strands as in BLOCKS, each in 1..4."""
    fixed, n_out, target = BLOCKS[block]
    strands = {"Psi": [2], "Sigma2": [2, 2], "Lambda2": [1, 2]}
    start = tuple(sorted(strands[fixed] + [s for f in content for s in strands[f]]))
    l2 = {(2, 2): 3, (1, 2): 2, (2, 3): 4, (1, 3): 3}

    def step(st: tuple, op: str):
        st = list(st)
        res = set()
        idx = range(len(st))
        if op == "l2":
            for i in idx:
                for j in idx:
                    if i < j and tuple(sorted((st[i], st[j]))) in l2:
                        rest = [st[k] for k in idx if k not in (i, j)]
                        res.add(
                            tuple(sorted(rest + [l2[tuple(sorted((st[i], st[j])))]]))
                        )
        elif op == "l3":
            for i in idx:
                for j in idx:
                    for k in idx:
                        if i < j < k and (st[i], st[j], st[k]) == (2, 2, 2):
                            rest = [st[m] for m in idx if m not in (i, j, k)]
                            res.add(tuple(sorted(rest + [3])))
        elif op == "pair":
            for i in idx:
                for j in idx:
                    if i < j and st[i] + st[j] == 5:
                        res.add(tuple(sorted(st[k] for k in idx if k not in (i, j))))
        elif op == "p22":
            for i in idx:
                for j in idx:
                    if i < j and (st[i], st[j]) == (2, 2):
                        rest = [st[k] for k in idx if k not in (i, j)]
                        res.add(tuple(sorted(rest + [3, 3])))
        return res

    for order in set(permutations(ops)):
        states = {start}
        for op in order:
            states = {t for s in states for t in step(s, op)}
        if any(len(s) == n_out and sum(s) == target for s in states):
            return True
    return False


def realizable_present(
    block: str,
    content: tuple,
    ops: tuple,
    sigma: tuple = (2, 2),
    lam: tuple = (1, 2),
    sigma_extra: tuple | None = None,
) -> bool:
    """Level-matched row realized on the present field content of closed SFT.

    Per-strand grading only, no support restriction beyond ghost number (the
    string vertices exist at every ghost number): Psi (2), Sigma_2 strands
    `sigma` ((2, 2) on the present content, `paper/sections/02-2-quartic.tex`),
    Lambda_2 strands `lam` ((1, 2), the grading of Lambda (x) Psi).  l_2 on (a, b)
    -> a + b - 1; l_3 on (a, b, c) -> a + b + c - 3; p_{2,2} on (a, b) -> any
    (x, y) with x + y = a + b + 2; a contraction needs ghost sum 5.  Strand ghost
    numbers are restricted to [-4, 9], wide enough for <= 5 operations."""
    fixed, n_out, target = BLOCKS[block]
    strands = {"Psi": [2], "Sigma2": list(sigma), "Lambda2": list(lam)}
    # sigma_extra: the split of a Sigma_2 occurring as an extra field (the
    # total-ghost-4 reading lets the two occurrences sit in different splits)
    extra = dict(strands)
    if sigma_extra is not None:
        extra["Sigma2"] = list(sigma_extra)
    start = tuple(sorted(strands[fixed] + [s for f in content for s in extra[f]]))
    lo, hi = -4, 9

    def step(st: tuple, op: str):
        st = list(st)
        res = set()
        idx = range(len(st))
        if op in ("l2", "pair", "p22"):
            for i, j in combinations(idx, 2):
                rest = [st[k] for k in idx if k not in (i, j)]
                a, b = st[i], st[j]
                if op == "l2":
                    res.add(tuple(sorted(rest + [a + b - 1])))
                elif op == "pair" and a + b == 5:
                    res.add(tuple(sorted(rest)))
                elif op == "p22":
                    for x in range(lo, hi + 1):
                        y = a + b + 2 - x
                        if lo <= y <= hi:
                            res.add(tuple(sorted(rest + [x, y])))
        elif op == "l3":
            for i, j, k in combinations(idx, 3):
                rest = [st[m] for m in idx if m not in (i, j, k)]
                res.add(tuple(sorted(rest + [st[i] + st[j] + st[k] - 3])))
        return {t for t in res if all(lo <= g <= hi for g in t)}

    for order in set(permutations(ops)):
        states = {start}
        for op in order:
            states = {t for s in states for t in step(s, op)}
        if any(len(s) == n_out and sum(s) == target for s in states):
            return True
    return False


def check_c5_table() -> None:
    details, ok = [], True
    # (i) the ghost shifts used by the table, measured on M's supports:
    # V_3 non-zero only at ghost sum 6 -> N_gh(l_2) = 6 - 5 - 2*... read as
    # out = (6 - in1 - in2) dual -> 5 - (6 - in1 - in2) = in1 + in2 - 1
    meas = measured_shifts(model(random.Random(SEEDS[0] + 3)))
    shifts_ok = all(meas[k] == OPS[k][0] for k in OPS)
    ok &= shifts_ok
    details.append(
        f"ghost shifts from M's saturation numbers {meas}: match = {shifts_ok}"
    )
    total = {}
    for block in BLOCKS:
        r1, r2 = rows_by_search(block), rows_by_count(block)
        same = r1 == r2
        ok &= same
        lm = sorted(r for r in r1 if r[3] == 0)
        lm_M = [r for r in lm if realizable_in_M(block, r[0], r[1])]
        lm_P = [r for r in lm if realizable_present(block, r[0], r[1])]
        lm_P03 = [r for r in lm if realizable_present(block, r[0], r[1], lam=(0, 3))]
        n_out = BLOCKS[block][1]
        mono = sum(dress_words(n_out, r[3]) for r in r1)
        # total-ghost-4 reading (ruled out by A6, Harold's decision): any split
        lm_T = [
            r
            for r in lm
            if any(
                realizable_present(block, r[0], r[1], sigma=sg, lam=la, sigma_extra=sx)
                for sg in ((2, 2), (1, 3), (0, 4))
                for sx in ((2, 2), (1, 3), (0, 4))
                for la in ((1, 2), (0, 3))
            )
        ]
        ok &= len(lm_P03) == len(lm_P)
        total[block] = (len(r1), len(lm), len(lm_P), len(lm_M), mono, len(lm_T))
        details.append(
            f"{block}: rows {len(r1)} (search = count: {same}); level-matched rows "
            f"(shift 0) {len(lm)}, on the present content (Sigma_2 strands (2, 2), "
            f"Lambda_2 (1, 2)) {len(lm_P)}, realized on M's grading {len(lm_M)}; "
            f"Lambda_2 at (0, 3): {len(lm_P03)} (asserted equal); total-ghost-4 "
            f"reading (note only, ruled out by A6): {len(lm_T)}; "
            f"non-level-matched monomials (rows x dressing words) {mono}"
        )
        for r in lm:
            details.append(
                f"  {block} lm row {'+'.join(r[0]) or '-'} / {','.join(r[1])}: "
                f"present {realizable_present(block, r[0], r[1])}, "
                f"M {realizable_in_M(block, r[0], r[1])}"
            )
    # per-strand grading of the present content: no level-matched B_2 row
    # (B5, B8 need a strand pair of ghost sum 5 among ghost-2 strands)
    expected = {
        "D": (28, 6, 6, 6),
        "B2": (13, 2, 0, 2),
        "dPsi": (19, 6, 6, 6),
        "Lambda": (12, 4, 4, 4),
    }
    counts_ok = all(
        (total[b][0], total[b][1], total[b][2], total[b][5]) == expected[b]
        for b in expected
        if b in total
    ) and set(expected) == set(total)
    ok &= counts_ok
    details.append(
        "asserted (rows, level-matched, present A6, total-ghost reading) = "
        f"{ {b: (total[b][0], total[b][1], total[b][2], total[b][5]) for b in total} }"
        f": {counts_ok}"
    )
    nb = total["B2"][2] if "B2" in total else None
    b2_zero = nb == 0
    ok &= b2_zero
    details.append(f"present content: level-matched B_2 rows = {nb} (expected 0)")
    # break leg: Sigma_2 strands at (1, 3) -> a ghost-sum-5 pair exists, B5 appears
    lmB = [r for r in rows_by_search("B2") if r[3] == 0]
    nb13 = sum(realizable_present("B2", r[0], r[1], sigma=(1, 3)) for r in lmB)
    ok &= nb13 > 0
    details.append(
        f"break: Sigma_2 strands at (1, 3) -> level-matched B_2 rows {nb13} "
        + ("(FAIL of the zero count, as expected)" if nb13 > 0 else "(unexpected)")
    )
    # break leg: a wrong shift for l_3 in route 1 only -> the two routes disagree
    saved = OPS["l3"]
    OPS["l3"] = (-2, 2)
    changed = any(rows_by_search(b) != rows_by_count(b) for b in BLOCKS)
    OPS["l3"] = saved
    ok &= changed
    details.append(
        "break: N_gh(l_3) = -2 -> row sets change "
        + ("(FAIL as expected)" if changed else "(unexpected: unchanged)")
    )
    record("C5-table", ok, "building-block table\n    " + "\n    ".join(details))
    return total


def measured_shifts(mdl: dict) -> dict:
    """Ghost shifts of l_2, l_3, p_{2,2}, <.,.> read off M's non-zero tensor entries.

    <z, l_2(x, y)> = V_3(z, x, y): the output l_2(x, y) has a component along the
    dual z* of z, ghost 5 - gh(z); shift = 5 - gh(z) - gh(x) - gh(y).  Same for
    l_3 with V_4.  <A, p(B)>_2 = V_4(A, B) with the two-string pairing at ghost
    sum 10: shift = 10 - gh(A) - gh(B).  The pairing: ghost sum of its support."""
    n = len(BASIS)
    sh: dict = {"l2": set(), "l3": set(), "p22": set(), "pair": set()}
    v3 = dict(mdl["c"])
    for (y, x), val in mdl["M"].items():  # V_3(y*, x, lam) = M_yx and orderings
        if val:
            for perm in permutations((y + 5, x, 0)):
                v3[perm] = val
    for (z, x, y), val in v3.items():
        if val:
            sh["l2"].add(5 - GH[z] - GH[x] - GH[y])
    for (z, a, b, c), val in v4_full(mdl).items():
        if val:
            sh["l3"].add(5 - GH[z] - GH[a] - GH[b] - GH[c])
            sh["p22"].add(10 - (GH[z] + GH[a]) - (GH[b] + GH[c]))
    for i in range(n):
        for j in range(n):
            if pairing(i, j):
                sh["pair"].add(-(GH[i] + GH[j]))
    return {k: (v.pop() if len(v) == 1 else sorted(v)) for k, v in sh.items()}


# ------------------------------------------- after the last review: C1.4, C4.theta


def qform(m: list[list[Fraction]], x: list, y: list) -> Fraction:
    """Bilinear form x^T m y."""
    return sum(x[i] * m[i][j] * y[j] for i in range(len(x)) for j in range(len(y)))


def check_c14_e1b_source() -> None:
    """C1.4 (E1b) with the source q(Sigma_2, Psi^2): eqs. (L1.10)-(L1.11).

    E = S (+) W (im D drops by (L1.8)), t in S plays Psi^2 (S = S_Psi, the A6
    slice).  A(s, w) = 1/2 q(s + w, s + w) - q(s + w, t), minimized in w at
    w* = -q_WW^{-1} q_WS (s - t), is compared at random points (i) with the
    closed form 1/2 q_Sch(u, u) - 1/2 q_SS(t, t), u = s - t, and (ii) with the
    present A_0 = 1/2 p(s, s) - p(s, t), for: (a) Schur-only q (q_Sch = p,
    q_WS != 0): must differ (the Schur condition alone is not enough);
    (b) q_SS = p with q_WS != 0 and q_WW definite: must differ; (c) q_WS = 0,
    q_SS = p: must agree; (d) q_WW = diag(1, -1), q_WS = v a^T with v isotropic
    for q_WW^{-1}, q_SS = p: agrees although q_WS != 0 and w* != 0.
    """
    details, ok = [], True
    for seed in SEEDS:
        rng = random.Random(seed + 41)
        nS, nW = 3, 2

        def sym(n):
            a = rand_mat(rng, n, n)
            return [[a[i][j] + a[j][i] for j in range(n)] for i in range(n)]

        p = sym(nS)

        def evaluate(qSS, qSW, qWW):
            qWS = transpose(qSW)
            qWWi = inverse(qWW)
            sch = [
                [qSS[i][j] - qform(qWWi, [r[i] for r in qWS], [r[j] for r in qWS])
                 for j in range(nS)]
                for i in range(nS)
            ]  # fmt: skip
            closed_ok, match, wnz = True, True, False
            for _ in range(3):
                sv = [rand_rat(rng) for _ in range(nS)]
                t = [rand_rat(rng) for _ in range(nS)]
                u = [a - b for a, b in zip(sv, t)]
                qu = [sum(qWS[k][i] * u[i] for i in range(nS)) for k in range(nW)]
                w = [-sum(qWWi[k][l] * qu[l] for l in range(nW)) for k in range(nW)]
                wnz |= any(x != 0 for x in w)
                A = (
                    qform(qSS, sv, sv) / 2
                    + qform(qSW, sv, w)
                    + qform(qWW, w, w) / 2
                    - qform(qSS, sv, t)
                    - qform(qWS, w, t)
                )
                closed = qform(sch, u, u) / 2 - qform(qSS, t, t) / 2
                A0 = qform(p, sv, sv) / 2 - qform(p, sv, t)
                closed_ok &= A == closed
                match &= A == A0
            return closed_ok, match, wnz

        qSW = rand_mat(rng, nS, nW)
        qWWd = [[Fraction(1 + rng.randint(1, 5)), Fraction(0)],
                [Fraction(0), Fraction(1 + rng.randint(1, 5))]]  # fmt: skip
        corr = matmul(matmul(qSW, inverse(qWWd)), transpose(qSW))
        qSS_schur = [[p[i][j] + corr[i][j] for j in range(nS)] for i in range(nS)]
        ca, ma, _ = evaluate(qSS_schur, qSW, qWWd)
        cb, mb, _ = evaluate(p, qSW, qWWd)
        zero = [[Fraction(0)] * nW for _ in range(nS)]
        cc, mc, _ = evaluate(p, zero, qWWd)
        a_vec = [rand_rat(rng) for _ in range(nS)]
        qSW_iso = [[a_vec[i], a_vec[i]] for i in range(nS)]  # q_WS = v a^T, v=(1,1)
        qWWi = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(-1)]]
        cd, md, wd = evaluate(p, qSW_iso, qWWi)
        good = ca and cb and cc and cd and (not ma) and (not mb) and mc and md and wd
        ok &= good
        details.append(
            f"seed {seed}: closed form (L1.10) exact in all cases = {ca and cb and cc and cd}; "
            f"(a) Schur-only matches present = {ma} (FAIL as expected); "
            f"(b) q_SS = p, q_WS != 0, definite = {mb} (FAIL as expected); "
            f"(c) q_WS = 0 = {mc}; (d) indefinite isotropic q_WS = {md}, w* != 0 = {wd}"
        )
    record(
        "C1.4-E1b-source",
        ok,
        "elimination of W with the source\n    " + "\n    ".join(details),
    )


def acyclic_model(rng: random.Random, n1: int, m: int, cohomology: bool = False):
    """Finite graded model with a self-adjoint Q and no cohomology at ghost 2.

    Ghost 2 basis (chi_a = Q lambda_a, a < n1; eta_b, b < m), ghost 3 its dual
    (chi*_a, eta*_b), pairing <e, e*> = 1.  Q eta_b = sum_c K_bc eta*_c with K
    symmetric invertible (Q self-adjoint: <Q eta_b, eta_c> = K_bc symmetric).
    With cohomology=True, K gets a zero row and column (a physical eta_0).
    Returns Q2 (ghost 2 -> ghost 3 matrix, coordinates chi*, eta*) and Omega,
    the form omega(X, Y) = <X, Q Y> on ghost 2.
    """
    while True:
        a = rand_mat(rng, m, m)
        K = [[a[i][j] + a[j][i] for j in range(m)] for i in range(m)]
        if cohomology:
            for j in range(m):
                K[0][j] = K[j][0] = Fraction(0)
        if cohomology or rank_q(K) == m:
            break
    n = n1 + m
    Q2 = [[Fraction(0)] * n for _ in range(n)]
    for b in range(m):
        for c in range(m):
            Q2[n1 + c][n1 + b] = K[b][c]
    Omega = Q2  # <X, Q Y> = X . (Q2 Y) with the identity pairing
    return Q2, Omega, n


def check_c4_theta_core() -> None:
    """C4.theta: the finite-dimensional core of (theta.1) and (theta.2).

    (theta.1) {A in H_2 : <A, Q Psi> = 0 for all Psi} = im Q at ghost 2.
    (theta.2) {b : H_2 -> H_2 linear, omega(bX, X) = 0 for all X} equals the span
    of Q o kappa' (kappa' : H_2 -> H_1, values in im Q) and mu o Q with mu graded
    antisymmetric for the pairing (here an antisymmetric matrix: all strands of
    ghost 2 are even).  Exact ranks over Q.  Break legs: a Q-cohomology direction
    (an eta with Q eta = 0) gives a solution of (theta.1) outside im Q; the class
    mu o Q dropped leaves the span short of the solution space.  This is a
    finite acyclic representation of the linear algebra only; it says nothing
    about the string vertices.
    """
    details, ok = [], True
    for seed in SEEDS:
        rng = random.Random(seed + 43)
        n1, m = 2, 3
        for coh in (False, True):
            Q2, Om, n = acyclic_model(rng, n1, m, cohomology=coh)
            # (theta.1): A^T Omega = 0  <=>  rows of Omega^T
            null1 = n - rank_q(transpose(Om))
            imq = n1  # im Q at ghost 2 = span chi
            # (theta.2): unknown b (n x n), condition Omega b + (Omega b)^T = 0
            idx = [(i, j) for i in range(n) for j in range(n)]
            rows = []
            for r in range(n):
                for c in range(r, n):
                    row = [Fraction(0)] * len(idx)
                    for k, (i, j) in enumerate(idx):
                        # (Omega b)_{rc} = sum_i Om[r][i] b[i][c]
                        if j == c:
                            row[k] += Om[r][i]
                        if j == r:
                            row[k] += Om[c][i]
                    rows.append(row)
            null2 = len(idx) - rank_q(rows)
            gens_G, gens_T = [], []
            for i in range(n1):  # outputs along chi_i (im Q), any input column
                for j in range(n):
                    v = [Fraction(0)] * len(idx)
                    v[i * n + j] = Fraction(1)
                    gens_G.append(v)
            for a, b in combinations(range(n), 2):  # mu antisymmetric, b = mu Q2
                mu = [[Fraction(0)] * n for _ in range(n)]
                mu[a][b], mu[b][a] = Fraction(1), Fraction(-1)
                bm = matmul(mu, Q2)
                gens_T.append([bm[i][j] for i in range(n) for j in range(n)])
            solves = all(
                all(sum(rw[k] * g[k] for k in range(len(idx))) == 0 for rw in rows)
                for g in gens_G + gens_T
            )
            rGT = rank_q(gens_G + gens_T)
            rG = rank_q(gens_G)
            if not coh:
                good = null1 == imq and solves and rGT == null2 and rG < null2
                ok &= good
                details.append(
                    f"seed {seed}, acyclic: (theta.1) solutions {null1} = dim im Q "
                    f"{imq}; (theta.2) solutions {null2}, rank(G + T) {rGT}, "
                    f"generators solve = {solves}; break, T dropped: rank {rG} < "
                    f"{null2} (FAIL as expected)"
                )
            else:
                good = null1 > imq and null2 > rGT
                ok &= good
                details.append(
                    f"seed {seed}, break with a cohomology direction: (theta.1) "
                    f"solutions {null1} > dim im Q {imq} (FAIL as expected); "
                    f"(theta.2) solutions {null2} > rank(G + T) {rGT} (FAIL as expected)"
                )
    record("C4.theta-core", ok, "Lambda_2 sector core\n    " + "\n    ".join(details))


def main() -> int:
    print(f"seeds: {SEEDS}; modular arithmetic prime: 2^61 - 1")
    check_c1_search()
    check_c1_break_sym()
    check_c1_break_transverse()
    check_c14_e1b_source()
    check_c2_gauge()
    cache: dict = {}
    check_c3_solve(cache)
    check_c3_break(cache)
    check_c3_restriction(cache)
    check_c5_table()
    check_c4_theta_core()
    npass = sum(ok for _, ok, _ in RESULTS)
    print(f"\nSummary: {npass}/{len(RESULTS)} named checks PASS")
    return 0 if npass == len(RESULTS) else 1


if __name__ == "__main__":
    sys.exit(main())
