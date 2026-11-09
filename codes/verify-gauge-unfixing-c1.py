"""Gauge unfixing of Sigma_2, candidate C1: the constraint table in a strand model.

Record: agent/derivations/108-gauge-unfixing-c1-strand-model.md (sub-task 3a).
Usage: uv run --no-sync python codes/verify-gauge-unfixing-c1.py [SEED]
(the record runs it at SEED = 20261018 and 20261019).

Strand model (record 108, section Strand model): H^ext = sum_m V_m, m in {-1,0,1},
V_m = H_m^- + c_0^- H_m^-, H_0^- = model M of record 102 (dims 1,5,5,1 at ghost
1..4), H_{+-1}^- of dims (1,2,2,1).  Zero modes (M.1); full pairing (M.2) at ghost
sum 6, equal m only; two strands with Koszul signs and the pairing (M.4)
(eq:conv:pairing-n); E, L the graded-symmetric two-strand states at ghost 4, 3
(C6); S_0 = (H_0^{^2})_4 with p the form of M (V_4 on H_2^{^2}, record 102);
D = sum_i c^(i) [alpha(m_i, m_j) + gamma(m_i, m_j) N^(j)], N = c_0^- b_0^-;
B_2 = b^(1) + b^(2), slice S = ker B_2; S_per = c-count 0.

VERIFIED (each check named after its claim-tree node)
  C1.1-pairing   (M.2) graded symmetric, non-degenerate (rank 48), support at
                 ghost sum 6 and equal m.
  C1.2-adjoint   (M.3) for c_0^-, b_0^-, L_0^- on all basis pairs (consequences
                 of (M.2), not inputs).  Break leg: bpz(c_0^-) = +c_0^- fails.
  C1.3-omega1    <<A, c_0^- B>> equals M's pairing on H_0 (independent table).
  C1.4-two-strand  (M.5): <Sigma, X>_2 = - <<Sigma, c^(1) c^(2) X>>_2 for random
                 Sigma (ghost 4) and X (ghost 6) on H_0 strands, against the
                 restricted pairing eq:conv:pairing-n built independently.
                 Break leg: the + sign fails.
  C2.1-raise     For every D tested: D L subset E (tau-symmetric), D preserves
                 the sectors, raises the c-count by exactly one; im D in C,
                 S_0 cap im D = 0; the source term J extended by zero is
                 invariant, J(D Lambda_2) = 0.
  C2.3-count     dim E^(1)_sigma = 2 dim L^(0)_sigma in every sector (the counting
                 lemma's input), hence rank(D on L^(0)) <= dim E^(1)_sigma / 2.
  C2.2-brute     Small strand model (all H_m^- of dims 1,1,1,1, random p on S_0):
                 the direct linear solve for symmetric q (q(D l, x) = 0 for all
                 l, x; q|S_0 = p), mod 2^31 - 1, has the nullity of the formula
                 C(n+1,2) - C(s+1,2), n = dim E - rank D; with the decoupling rows
                 q(S_0, C) = 0 the nullity C(c'+1,2), c' = dim C - rank D; the
                 formula family is exact (Pi D = 0 over Q), so equality is
                 rigorous (rank mod p <= rank over Q).  Break leg: q not
                 symmetric -- nullity differs from the formula.
  C2.2-family    Main model: a random member q = Pi^T Q_K Pi of the solution
                 family satisfies q = q^T, q D = 0, q|S_0 = p exactly.
  C3-table       The columns of criterion (i) for every D: dim{q}, dim P_D,
                 non-transverse sectors (relative to S = ker B_2 and S_per),
                 kernel excess at a random point of the family (and of P_D),
                 literal verdict; the control row D = 0 gets the same literal
                 verdict "yes" (the coupling clause does not need a gauge
                 symmetry).  Refined columns: excess beyond the slice
                 C(n+1,2) - C(dim S-bar + 1, 2), E1a dimension.
  C4-prediction  For D = c_0^- f(L_0^-) symmetrized: sector {m1, m2} is
                 transverse w.r.t. ker B_2 iff f(m1) + f(m2) != 0; non-transverse
                 of type (a) (W != 0, S cap im D = 0) where f(m1) = f(m2) = 0 and
                 of type (b) (S cap im D != 0) where f(m1) = -f(m2) != 0; D = c_0^-
                 is transverse in every sector.  The plan's wording ("where f(m)
                 != 0") is compared and its mismatches listed.

NOT VERIFIED HERE
  Anything about the string vertex on non-level-matched states (q is a generic
  stand-in, A5); the residual symmetry, the compensating Lambda_2 and the
  elimination of Sigma_2 (sub-task 3b); field-dependent D (E2); D2-type
  operators built from p_{2,2} on non-level-matched inputs.  Model M is the
  on-shell model of record 102 (its scope is inherited).  The lift of Q_B to
  several strands appears nowhere.
"""

from __future__ import annotations

import random
import sys
from fractions import Fraction
from itertools import combinations_with_replacement, permutations
from math import comb

import numpy as np

SEED = int(sys.argv[1]) if len(sys.argv) > 1 else 20261018
LP = 2147483647  # 2^31 - 1, modular ranks (int64-safe products after reduction)
RESULTS: list[tuple[str, bool, str]] = []


def record(name: str, ok: bool, detail: str) -> None:
    """Store and print one named check."""
    RESULTS.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}")


# ------------------------------------------------------------ exact linear algebra


def rref(rows: list[list[Fraction]]) -> tuple[list[list[Fraction]], list[int]]:
    """Reduced row echelon form over Q; returns (rows, pivot columns)."""
    a = [list(r) for r in rows]
    if not a:
        return a, []
    ncol = len(a[0])
    piv, r = [], 0
    for col in range(ncol):
        pr = next((i for i in range(r, len(a)) if a[i][col] != 0), None)
        if pr is None:
            continue
        a[r], a[pr] = a[pr], a[r]
        inv = 1 / a[r][col]
        a[r] = [x * inv for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][col] != 0:
                f = a[i][col]
                a[i] = [x - f * y for x, y in zip(a[i], a[r])]
        piv.append(col)
        r += 1
        if r == len(a):
            break
    return a[:r], piv


def rank(rows: list[list[Fraction]]) -> int:
    """Rank over Q."""
    return len(rref(rows)[1]) if rows and rows[0] else 0


def nullspace(rows: list[list[Fraction]], ncol: int) -> list[list[Fraction]]:
    """Basis of the null space {x : rows x = 0} over Q."""
    if not rows:
        return [[Fraction(int(i == j)) for i in range(ncol)] for j in range(ncol)]
    red, piv = rref(rows)
    free = [c for c in range(ncol) if c not in piv]
    basis = []
    for fcol in free:
        v = [Fraction(0)] * ncol
        v[fcol] = Fraction(1)
        for r, pc in enumerate(piv):
            v[pc] = -red[r][fcol]
        basis.append(v)
    return basis


def inverse(a: list[list[Fraction]]) -> list[list[Fraction]]:
    """Inverse of a square matrix over Q (Gauss-Jordan)."""
    n = len(a)
    aug = [list(r) + [Fraction(int(i == j)) for j in range(n)] for i, r in enumerate(a)]
    red, piv = rref(aug)
    assert piv[:n] == list(range(n)), "singular matrix"
    return [r[n:] for r in red]


def rank_mod(m: np.ndarray) -> int:
    """Rank modulo LP (a lower bound for the rank over Q)."""
    a = m.copy() % LP
    nr, nc = a.shape
    r = 0
    for col in range(nc):
        if r == nr:
            break
        nz = np.nonzero(a[r:, col])[0]
        if nz.size == 0:
            continue
        p = r + nz[0]
        if p != r:
            a[[r, p]] = a[[p, r]]
        inv = pow(int(a[r, col]), LP - 2, LP)
        a[r] = (a[r] * inv) % LP
        others = np.nonzero(a[:, col])[0]
        others = others[others != r]
        if others.size:
            f = a[others, col].reshape(-1, 1)
            a[others] = (a[others] - (f * a[r]) % LP) % LP
        r += 1
    return r


def modp(x: Fraction) -> int:
    """Fraction to residue mod LP."""
    return (x.numerator % LP) * pow(x.denominator % LP, LP - 2, LP) % LP


# ------------------------------------------------------------ model M (record 102)
# Copied from codes/verify-gauge-unfixing-structure.py (record 102, model M),
# unchanged in content: basis, ghost numbers, pairing, random V_4 on H_2.

M_GH = [1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4]  # lam; chi ph1 ph2 ph3 mu; antifields; lam*
M_DUAL = {0: 11, 1: 6, 2: 7, 3: 8, 4: 9, 5: 10}
M_DUAL.update({v: k for k, v in list(M_DUAL.items())})
PHYS, NOCHI = [2, 3, 4], [2, 3, 4, 5]
U_GH = [1, 2, 2, 3, 3, 4]  # H_{+-1}^-: u0; u1 u2; u3 u4; u5
U_DUAL = {0: 5, 1: 3, 2: 4}
U_DUAL.update({v: k for k, v in list(U_DUAL.items())})


def rand_rat(rng: random.Random, lo: int = -9, hi: int = 9) -> Fraction:
    """Random small rational."""
    return Fraction(rng.randint(lo, hi), rng.randint(1, 4))


def model_v4(rng: random.Random, degenerate: bool = False) -> dict:
    """V_4 of model M on the (2,2,2,2) block: V4free + V4chi (record 102)."""
    c = {}
    for t in combinations_with_replacement(NOCHI, 3):
        x = rand_rat(rng)
        for perm in set(permutations(t)):
            c[perm] = x
    mm = {(a, b): rand_rat(rng) for a in PHYS for b in PHYS}
    v4 = {}
    if degenerate:
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

    def mvec(v: dict) -> dict:
        return {y: sum(mm[(y, x)] * v.get(x, 0) for x in PHYS) for y in PHYS}

    def cub(a: dict, b: dict, d: dict) -> Fraction:
        return sum(
            c[(i, j, k)] * a.get(i, 0) * b.get(j, 0) * d.get(k, 0)
            for i in NOCHI
            for j in NOCHI
            for k in NOCHI
        )

    e = {i: {i: 1} for i in NOCHI}
    for a, b, d in combinations_with_replacement(NOCHI, 3):
        val = -(
            cub(mvec(e[a]), e[b], e[d])
            + cub(mvec(e[b]), e[d], e[a])
            + cub(mvec(e[d]), e[a], e[b])
        )
        for perm in set(permutations((1, a, b, d))):
            v4[perm] = v4.get(perm, 0) + val
    return v4


# ------------------------------------------------------------ strand model


class StrandModel:
    """H^ext, its zero modes, pairings, and the two-strand spaces E, L."""

    def __init__(self, small: bool = False) -> None:
        self.small = small
        self.sb = []  # (m, typ, i, ghost)
        for m in (-1, 0, 1):
            gh = [1, 2, 3, 4] if small else (M_GH if m == 0 else U_GH)
            for typ in (0, 1):
                for i, g in enumerate(gh):
                    self.sb.append((m, typ, i, g + typ))
        self.idx = {(m, t, i): k for k, (m, t, i, _) in enumerate(self.sb)}
        self.n = len(self.sb)
        self.E = self.sym_basis(4)
        self.L = self.sym_basis(3)
        self.Eix = {ab: k for k, ab in enumerate(self.E)}
        self.Lix = {ab: k for k, ab in enumerate(self.L)}

    # single strand
    def par(self, a: int) -> int:
        return self.sb[a][3] % 2

    def gh(self, a: int) -> int:
        return self.sb[a][3]

    def m(self, a: int) -> int:
        return self.sb[a][0]

    def typ(self, a: int) -> int:
        return self.sb[a][1]

    def c(self, a: int) -> int | None:
        m, t, i, _ = self.sb[a]
        return self.idx[(m, 1, i)] if t == 0 else None

    def b(self, a: int) -> int | None:
        m, t, i, _ = self.sb[a]
        return self.idx[(m, 0, i)] if t == 1 else None

    def omega(self, m: int, i: int, j: int) -> int:
        """Restricted pairing omega^(m)_{ij} (ghost sum 5, symmetric)."""
        if self.small:
            return 1 if i + j == 3 else 0  # ghosts 1..4: pairs (1,4), (2,3)
        dual = M_DUAL if m == 0 else U_DUAL
        return 1 if dual[i] == j else 0

    def G1(self, a: int, bb: int, flip: int = 1) -> int:
        """Full pairing (M.2); flip=-1 breaks graded symmetry (break legs)."""
        ma, ta, ia, ga = self.sb[a]
        mb, tb, ib, gb = self.sb[bb]
        if ma != mb:
            return 0
        if ta == 0 and tb == 1:
            return self.omega(ma, ia, ib)
        if ta == 1 and tb == 0:
            return flip * (-1) ** (ga * gb) * self.omega(ma, ia, ib)
        return 0

    # two strands
    def sym_basis(self, G: int) -> list[tuple[int, int]]:
        out = []
        for a in range(self.n):
            for bb in range(a, self.n):
                if self.gh(a) + self.gh(bb) != G:
                    continue
                if a == bb and self.par(a) == 1:
                    continue
                out.append((a, bb))
        return out

    def vec(self, ab: tuple[int, int]) -> dict:
        a, bb = ab
        if a == bb:
            return {(a, a): Fraction(1)}
        return {
            (a, bb): Fraction(1),
            (bb, a): Fraction((-1) ** (self.par(a) * self.par(bb))),
        }

    def tau(self, v: dict) -> dict:
        out = {}
        for (a, bb), x in v.items():
            key = (bb, a)
            out[key] = out.get(key, 0) + (-1) ** (self.par(a) * self.par(bb)) * x
        return {k: x for k, x in out.items() if x != 0}

    def coords(self, v: dict, basis: dict) -> list[Fraction]:
        """Coordinates of a tau-symmetric ordered vector in a sym basis."""
        out = [Fraction(0)] * len(basis)
        for (a, bb), x in v.items():
            if x == 0:
                continue
            if a <= bb:
                out[basis[(a, bb)]] += x
        return out

    def sector(self, ab: tuple[int, int]) -> tuple[int, int]:
        return tuple(sorted((self.m(ab[0]), self.m(ab[1]))))

    def ccount(self, ab: tuple[int, int]) -> int:
        return self.typ(ab[0]) + self.typ(ab[1])

    def apply_D(self, v: dict, alpha, gamma) -> dict:
        """D = sum_i c^(i) [alpha(m_i, m_j) + gamma(m_i, m_j) N^(j)] (Koszul)."""
        out = {}
        for (a, bb), x in v.items():
            ma, mb = self.m(a), self.m(bb)
            ca = self.c(a)
            if ca is not None:
                co = alpha(ma, mb) + gamma(ma, mb) * (self.typ(bb) == 1)
                if co:
                    out[(ca, bb)] = out.get((ca, bb), 0) + co * x
            cb = self.c(bb)
            if cb is not None:
                co = alpha(mb, ma) + gamma(mb, ma) * (self.typ(a) == 1)
                if co:
                    s = (-1) ** self.par(a)
                    out[(a, cb)] = out.get((a, cb), 0) + s * co * x
        return {k: x for k, x in out.items() if x != 0}

    def apply_B(self, v: dict) -> dict:
        """B_2 = b^(1) + b^(2) (Koszul)."""
        out = {}
        for (a, bb), x in v.items():
            ba = self.b(a)
            if ba is not None:
                out[(ba, bb)] = out.get((ba, bb), 0) + x
            b2 = self.b(bb)
            if b2 is not None:
                s = (-1) ** self.par(a)
                out[(a, b2)] = out.get((a, b2), 0) + s * x
        return {k: x for k, x in out.items() if x != 0}

    def D_matrix(self, alpha, gamma) -> list[list[Fraction]]:
        """dim E x dim L matrix of D (columns = images of the L basis)."""
        cols = [
            self.coords(self.apply_D(self.vec(l), alpha, gamma), self.Eix)
            for l in self.L
        ]
        return [list(r) for r in zip(*cols)] if cols else []

    def B_matrix(self) -> list[list[Fraction]]:
        cols = [self.coords(self.apply_B(self.vec(e)), self.Lix) for e in self.E]
        return [list(r) for r in zip(*cols)]


def p_form(sm: StrandModel, v4: dict, s0: list[int]) -> list[list[Fraction]]:
    """p on S_0: p(Sigma, Sigma') = sum V4^{abcd} Sigma^{ab} Sigma'^{cd} (record 102)."""
    vecs = [sm.vec(sm.E[k]) for k in s0]

    def mi(a: int) -> int:
        return sm.sb[a][2]

    out = []
    for vk in vecs:
        row = []
        for vl in vecs:
            tot = Fraction(0)
            for (a, b), x in vk.items():
                for (c, d), y in vl.items():
                    tot += x * y * v4.get((mi(a), mi(b), mi(c), mi(d)), 0)
            row.append(tot)
        out.append(row)
    return out


# ------------------------------------------------------------ the D's tested (A7)


def rows_tested(rng: random.Random) -> list[tuple[str, str, object, object]]:
    """(name, description, alpha, gamma)."""
    ra = {(i, j): rand_rat(rng, 1, 9) for i in (-1, 0, 1) for j in (-1, 0, 1)}
    rg = {(i, j): rand_rat(rng, 1, 9) for i in (-1, 0, 1) for j in (-1, 0, 1)}
    ra0 = dict(ra)
    ra0[(0, 0)] = Fraction(0)
    z = lambda m1, m2: 0  # noqa: E731
    return [
        ("D0", "control, D = 0", z, z),
        ("Dc", "c_0^- (f = 1)", lambda m1, m2: 1, z),
        ("DcL", "c_0^- L_0^- (f(m) = m)", lambda m1, m2: m1, z),
        ("Dcd", "c_0^- delta(L_0^-) (f = delta_{m,0})", lambda m1, m2: int(m1 == 0), z),
        ("Dc1d", "c_0^- (1 - delta(L_0^-))", lambda m1, m2: int(m1 != 0), z),
        ("DcLo", "c_0^- times L_0^- of the other strand", lambda m1, m2: m2, z),
        ("DN", "c_0^- (x) c_0^- b_0^- (gamma = 1)", z, lambda m1, m2: 1),
        ("Dgen", "generic D1 (random alpha, gamma)", lambda m1, m2: ra[(m1, m2)],
         lambda m1, m2: rg[(m1, m2)]),
        ("Dgen0", "generic D1 with alpha(0,0) = 0", lambda m1, m2: ra0[(m1, m2)],
         lambda m1, m2: rg[(m1, m2)] if (m1, m2) != (0, 0) else 0),
    ]  # fmt: skip


FORM_F = {  # rows of the form D = c_0^- f(L_0^-), f on the c_0^- strand
    "Dc": lambda m: 1,
    "DcL": lambda m: m,
    "Dcd": lambda m: int(m == 0),
    "Dc1d": lambda m: int(m != 0),
}


# ------------------------------------------------------------ C1: the strand model


def check_c1(sm: StrandModel, rng: random.Random) -> None:
    n = sm.n
    G = [[sm.G1(a, b) for b in range(n)] for a in range(n)]
    sym = all(
        G[b][a] == (-1) ** (sm.par(a) * sm.par(b)) * G[a][b]
        for a in range(n)
        for b in range(n)
    )
    supp = all(
        G[a][b] == 0 or (sm.gh(a) + sm.gh(b) == 6 and sm.m(a) == sm.m(b))
        for a in range(n)
        for b in range(n)
    )
    rk = rank([[Fraction(x) for x in r] for r in G])
    Gf = [[sm.G1(a, b, flip=-1) for b in range(n)] for a in range(n)]
    sym_f = all(
        Gf[b][a] == (-1) ** (sm.par(a) * sm.par(b)) * Gf[a][b]
        for a in range(n)
        for b in range(n)
    )
    record(
        "C1.1-pairing",
        sym and supp and rk == n and not sym_f,
        f"graded symmetric {sym}, support ghost 6 / equal m {supp}, rank {rk}/{n}; "
        f"break (sign of <<c e, e>> flipped): symmetric {sym_f} (expected False)",
    )

    def g(a, b):
        return 0 if a is None or b is None else sm.G1(a, b)

    def adj(sign_c: int) -> tuple[bool, bool]:
        okc = okb = True
        for a in range(n):
            for b in range(n):
                s = (-1) ** sm.par(a)
                if g(sm.c(a), b) != sign_c * s * g(a, sm.c(b)):
                    okc = False
                if g(sm.b(a), b) != s * g(a, sm.b(b)):
                    okb = False
        return okc, okb

    okc, okb = adj(-1)
    okL = all(
        sm.m(a) * G[a][b] == sm.m(b) * G[a][b] for a in range(n) for b in range(n)
    )
    bad_c, _ = adj(+1)
    record(
        "C1.2-adjoint",
        okc and okb and okL and not bad_c,
        f"(M.3): c_0^- with bpz = -c_0^- {okc}, b_0^- with bpz = +b_0^- {okb}, "
        f"L_0^- even {okL}; break (bpz(c_0^-) = +c_0^-): holds {bad_c} (expected False)",
    )
    # omega_1 on H_0 = M's pairing table, and graded symmetric (C1, s = +1)
    h0 = [a for a in range(n) if sm.m(a) == 0 and sm.typ(a) == 0]
    ok = True
    for a in h0:
        for b in h0:
            w = g(a, sm.c(b))
            wt = 1 if M_DUAL[sm.sb[a][2]] == sm.sb[b][2] else 0
            wr = g(b, sm.c(a))
            if w != wt or wr != (-1) ** (sm.par(a) * sm.par(b)) * w:
                ok = False
    record("C1.3-omega1", ok, "<<A, c_0^- B>> = M's pairing on H_0, symmetric (s = +1)")
    # (M.5) two-strand relation
    s0 = [k for k, e in enumerate(sm.E) if sm.sector(e) == (0, 0) and sm.ccount(e) == 0]
    sig = {}
    for k in s0:
        x = rand_rat(rng)
        for key, val in sm.vec(sm.E[k]).items():
            sig[key] = sig.get(key, 0) + x * val
    X = {}
    for a in h0:
        for b in h0:
            if sm.gh(a) + sm.gh(b) == 6:
                X[(a, b)] = rand_rat(rng)

    def restricted(u: dict, v: dict) -> Fraction:
        tot = Fraction(0)
        for (x1, x2), cu in u.items():
            for (y1, y2), cv in v.items():
                w1 = 1 if M_DUAL[sm.sb[x1][2]] == sm.sb[y1][2] else 0
                w2 = 1 if M_DUAL[sm.sb[x2][2]] == sm.sb[y2][2] else 0
                tot += (-1) ** (sm.par(y1) * sm.par(x2)) * w1 * w2 * cu * cv
        return tot

    def full(u: dict, v: dict) -> Fraction:
        tot = Fraction(0)
        for (x1, x2), cu in u.items():
            for (y1, y2), cv in v.items():
                tot += (
                    (-1) ** (sm.par(y1) * sm.par(x2))
                    * sm.G1(x1, y1)
                    * sm.G1(x2, y2)
                    * cu
                    * cv
                )
        return tot

    ccX = {}
    for (y1, y2), x in X.items():  # c^(1) c^(2) (y1 (x) y2) = (-1)^{|y1|} c y1 (x) c y2
        ccX[(sm.c(y1), sm.c(y2))] = (-1) ** sm.par(y1) * x
    lhs, rhs = restricted(sig, X), full(sig, ccX)
    record(
        "C1.4-two-strand",
        lhs != 0 and lhs == -rhs and lhs != rhs,
        f"<Sigma, X>_2 = {lhs}, -<<Sigma, c c X>>_2 = {-rhs}; break (+ sign) equal: "
        f"{lhs == rhs} (expected False)",
    )


# ------------------------------------------------------------ C2-C4: per D


def sector_lists(sm: StrandModel) -> dict:
    out = {}
    for k, e in enumerate(sm.E):
        out.setdefault(sm.sector(e), [[], []])[0].append(k)
    for k, l in enumerate(sm.L):
        out.setdefault(sm.sector(l), [[], []])[1].append(k)
    return out


def analyse(sm: StrandModel, DE, BM, secs: dict) -> dict:
    """Per-sector ranks and transversality w.r.t. S = ker B_2 and S_per."""
    res = {}
    for sg, (Ei, Li) in sorted(secs.items()):
        Dsg = [[DE[i][j] for j in Li] for i in Ei]
        Dcols = [list(c) for c in zip(*Dsg)] if Li else []
        rD = rank(Dcols) if Dcols else 0
        Bsg = [[BM[i][j] for j in Ei] for i in Li]
        Sb = nullspace(Bsg, len(Ei))
        Sper = [
            [Fraction(int(t == r)) for t in range(len(Ei))]
            for r, i in enumerate(Ei)
            if sm.ccount(sm.E[i]) == 0
        ]
        out = {"dimE": len(Ei), "dimL": len(Li), "rD": rD}
        for name, sb in (("S", Sb), ("Sper", Sper)):
            tot = rank(sb + Dcols) if (sb or Dcols) else 0
            out[name] = {"dim": len(sb), "i": len(sb) + rD - tot, "w": len(Ei) - tot}
        E1 = [i for i in Ei if sm.ccount(sm.E[i]) == 1]
        L0 = [j for j in Li if sm.ccount(sm.L[j]) == 0]
        out["dimE1"], out["dimL0"] = len(E1), len(L0)
        out["S_cap_E1"] = (
            rank(
                [
                    [v[r] for r, i in enumerate(Ei) if sm.ccount(sm.E[i]) == 1]
                    for v in Sb
                ]
            )
            if Sb and E1
            else 0
        )
        res[sg] = out
    return res


def complement_projection(sm, DE, secs, s0set):
    """Pi: E -> K coordinates along im D, K spanned by coordinate vectors, S_0 in K."""
    dimE = len(sm.E)
    Kglob, rows = [], []
    for sg, (Ei, Li) in sorted(secs.items()):
        Dsg = [[DE[i][j] for j in Li] for i in Ei]
        Dcols = [list(c) for c in zip(*Dsg)] if Li else []
        red, piv = rref([list(c) for c in Dcols]) if Dcols else ([], [])
        indep = [Dcols[j] for j in range(len(Dcols))] if False else []
        # independent columns of D (greedy)
        basis = []
        for col in Dcols:
            if rank(basis + [col]) > len(basis):
                basis.append(col)
        chosen = []
        order = [r for r, i in enumerate(Ei) if i in s0set] + [
            r for r, i in enumerate(Ei) if i not in s0set
        ]
        for r in order:
            u = [Fraction(int(t == r)) for t in range(len(Ei))]
            if rank(basis + chosen + [u]) > len(basis) + len(chosen):
                chosen.append(u)
        T = [list(r) for r in zip(*(chosen + basis))]
        Ti = inverse(T)
        for kk, u in enumerate(chosen):
            r = u.index(1)
            Kglob.append(Ei[r])
            full = [Fraction(0)] * dimE
            for t, i in enumerate(Ei):
                full[i] = Ti[kk][t]
            rows.append(full)
    return Kglob, rows


def matmul(a, b):
    bt = list(zip(*b))
    return [[sum(x * y for x, y in zip(r, c)) for c in bt] for r in a]


def kernel_dim(q, lower: int) -> int:
    """dim ker over Q: lower <= ker_Q <= ker_mod; exact when they meet."""
    km = len(q) - rank_mod(np.array([[modp(x) for x in r] for r in q], dtype=np.int64))
    if km == lower:
        return km
    return len(q) - rank(q)


def family_point(sm, DE, secs, s0, p, rng, decoupled: bool):
    """Random q = Pi^T Q_K Pi in the solution family (or in P_D)."""
    s0set = set(s0)
    K, Pi = complement_projection(sm, DE, secs, s0set)
    nK = len(K)
    pos = {i: k for k, i in enumerate(K)}
    QK = [[Fraction(0)] * nK for _ in range(nK)]
    for a in range(nK):
        for b in range(a, nK):
            ia, ib = K[a], K[b]
            if ia in s0set and ib in s0set:
                v = p[s0.index(ia)][s0.index(ib)]
            elif decoupled and ((ia in s0set) != (ib in s0set)):
                v = Fraction(0)
            else:
                v = rand_rat(rng)
            QK[a][b] = QK[b][a] = v
    PiT = [list(r) for r in zip(*Pi)]
    q = matmul(matmul(PiT, QK), Pi)
    return q, Pi, pos


def binom2(n: int) -> int:
    return comb(n + 1, 2)


def d_checks(sm: StrandModel, alpha, gamma, DE) -> tuple[bool, str]:
    """C2.1: D L in E, sectors preserved, c-count +1, im D in C."""
    ok_sym = ok_sec = ok_cc = True
    for l in sm.L:
        v = sm.apply_D(sm.vec(l), alpha, gamma)
        if sm.tau(v) != v:
            ok_sym = False
        for key in v:
            if sm.sector(key) != sm.sector(l):
                ok_sec = False
            if sm.ccount(key) != sm.ccount(l) + 1:
                ok_cc = False
    s0 = [k for k, e in enumerate(sm.E) if sm.sector(e) == (0, 0) and sm.ccount(e) == 0]
    ok_c = all(DE[i][j] == 0 for i in s0 for j in range(len(sm.L)))
    return ok_sym and ok_sec and ok_cc and ok_c, (
        f"tau-symmetric {ok_sym}, sectors {ok_sec}, c-count +1 {ok_cc}, im D in C {ok_c}"
    )


def brute(sm: StrandModel, DE, s0: list[int], symmetric: bool, decouple: bool) -> int:
    """Nullity mod LP of the homogeneous system for q (C2.3)."""
    dimE, dimL = len(sm.E), len(DE[0]) if DE else 0
    if symmetric:
        unk = {}
        for i in range(dimE):
            for j in range(i, dimE):
                unk[(i, j)] = len(unk)

        def u(i, j):
            return unk[(min(i, j), max(i, j))]
    else:
        unk = {(i, j): i * dimE + j for i in range(dimE) for j in range(dimE)}

        def u(i, j):
            return unk[(i, j)]

    rows = []
    for j in range(dimL):
        col = [DE[i][j] for i in range(dimE)]
        if not any(col):
            continue
        for x in range(dimE):
            r = np.zeros(len(unk), dtype=np.int64)
            for i, d in enumerate(col):
                if d:
                    r[u(i, x)] = (r[u(i, x)] + modp(d)) % LP
            rows.append(r)
    s0set = set(s0)
    for s in s0:
        for t in s0:
            if symmetric and t < s:
                continue
            r = np.zeros(len(unk), dtype=np.int64)
            r[u(s, t)] = 1
            rows.append(r)
    if decouple:
        for s in s0:
            for c in range(dimE):
                if c in s0set:
                    continue
                r = np.zeros(len(unk), dtype=np.int64)
                r[u(s, c)] = 1
                rows.append(r)
                if not symmetric:
                    r2 = np.zeros(len(unk), dtype=np.int64)
                    r2[u(c, s)] = 1
                    rows.append(r2)
    if not rows:
        return len(unk)
    return len(unk) - rank_mod(np.array(rows))


def check_c2_brute(rng: random.Random) -> None:
    sm = StrandModel(small=True)
    s0 = [k for k, e in enumerate(sm.E) if sm.sector(e) == (0, 0) and sm.ccount(e) == 0]
    details, ok = [], True
    rows = [
        r for r in rows_tested(rng) if r[0] in ("D0", "Dc", "DcL", "Dcd", "DN", "Dgen")
    ]
    for name, _, al, ga in rows:
        DE = sm.D_matrix(al, ga)
        rD = rank([list(c) for c in zip(*DE)]) if DE else 0
        dimE, s = len(sm.E), len(s0)
        n, cp = dimE - rD, dimE - s - rD
        f_sol, f_p = binom2(n) - binom2(s), binom2(cp)
        b_sol = brute(sm, DE, s0, True, False)
        b_p = brute(sm, DE, s0, True, True)
        # the formula family is exact: Pi D = 0 over Q
        secs = sector_lists(sm)
        _, Pi = complement_projection(sm, DE, secs, set(s0))
        exact = all(x == 0 for r in matmul(Pi, DE) for x in r) if DE else True
        good = b_sol == f_sol and b_p == f_p and exact
        ok &= good
        details.append(f"{name}: Sol {b_sol}/{f_sol}, P_D {b_p}/{f_p}")
    # break leg: drop the symmetry of q (first-slot condition only)
    DE = sm.D_matrix(lambda a, b: 1, lambda a, b: 0)
    rD = rank([list(c) for c in zip(*DE)])
    n = len(sm.E) - rD
    b_ns = brute(sm, DE, s0, False, False)
    brk = b_ns != binom2(n) - binom2(len(s0))
    record(
        "C2.2-brute",
        ok and brk,
        f"small model dim E = {len(sm.E)}, |S_0| = {len(s0)}; "
        + "; ".join(details)
        + f"; break (q not symmetric, Dc): nullity {b_ns} != formula "
        f"{binom2(n) - binom2(len(s0))}: {brk}",
    )


def main() -> int:
    rng = random.Random(SEED)
    print(f"seed {SEED}")
    sm = StrandModel()
    check_c1(sm, rng)
    secs = sector_lists(sm)
    s0 = [k for k, e in enumerate(sm.E) if sm.sector(e) == (0, 0) and sm.ccount(e) == 0]
    dimE, dimL, s = len(sm.E), len(sm.L), len(s0)
    dimC = dimE - s
    print(f"strand states {sm.n}; dim E = {dimE}, dim L = {dimL}, dim S_0 = {s}")
    print(
        "sectors (dim E, dim L): "
        + ", ".join(
            f"{sg}: ({len(Ei)}, {len(Li)})" for sg, (Ei, Li) in sorted(secs.items())
        )
    )
    BM = sm.B_matrix()
    # B_2 B_2 = 0 on E -> ghost 2 is not needed; check B_2 maps E into L (tau-symmetric)
    okB = all(sm.tau(sm.apply_B(sm.vec(e))) == sm.apply_B(sm.vec(e)) for e in sm.E)
    variants = {}
    for deg in (False, True):
        v4 = model_v4(random.Random(SEED + int(deg)), degenerate=deg)
        p = p_form(sm, v4, s0)
        variants[deg] = (p, s - rank(p))
    print(
        f"dim ker p on S_0: generic {variants[False][1]}, degenerate {variants[True][1]}"
    )

    ok21, ok22, ok24, okc3, okc4 = True, True, True, True, True
    d21, d24, table, c4notes = [], [], [], []
    for name, desc, al, ga in rows_tested(rng):
        DE = sm.D_matrix(al, ga)
        good, det = d_checks(sm, al, ga, DE)
        ok21 &= good and okB
        if not good:
            d21.append(f"{name}: {det}")
        an = analyse(sm, DE, BM, secs)
        for sg, a in an.items():
            if a["dimE1"] != 2 * a["dimL0"]:
                ok22 = False
        rD = sum(a["rD"] for a in an.values())
        n, cp = dimE - rD, dimC - rD
        dsol, dP = binom2(n) - binom2(s), binom2(cp)
        Sbar = sum(a["S"]["dim"] - a["S"]["i"] for a in an.values())
        Sbar_per = sum(a["Sper"]["dim"] - a["Sper"]["i"] for a in an.values())
        ref = binom2(n) - binom2(Sbar)
        ref_per = binom2(n) - binom2(Sbar_per)
        i_tot = sum(a["S"]["i"] for a in an.values())
        nt = [(sg, a["S"]["i"], a["S"]["w"]) for sg, a in an.items()
              if a["S"]["i"] or a["S"]["w"]]  # fmt: skip
        nt_per = [sg for sg, a in an.items() if a["Sper"]["i"] or a["Sper"]["w"]]
        # generic points (generic variant of p), kernel excess
        exc = {}
        for deg in (False, True):
            p, kp = variants[deg]
            q, Pi, _ = family_point(sm, DE, secs, s0, p, rng, decoupled=False)
            qd, _, _ = family_point(sm, DE, secs, s0, p, rng, decoupled=True)
            fam_ok = (
                all(q[i][j] == q[j][i] for i in range(dimE) for j in range(dimE))
                and all(x == 0 for r in matmul(q, DE) for x in r)
                and all(q[a][b] == p[ia][ib] for ia, a in enumerate(s0)
                        for ib, b in enumerate(s0))
                and all(qd[a][c] == 0 for a in s0 for c in range(dimE) if c not in s0)
            )  # fmt: skip
            ok24 &= fam_ok
            k_gen = kernel_dim(q, rD)
            k_dec = kernel_dim(qd, rD + kp)
            exc[deg] = (k_gen - rD - kp, k_dec - rD - kp)
        lit = "yes" if (dsol > dP or exc[False][0] != 0) else "no"
        refv = "yes" if (ref > 0 or i_tot > 0) else "no"
        table.append((name, desc, dsol, dP, nt, nt_per, exc, lit, ref, ref_per, i_tot,
                      refv, rD, n, cp, Sbar, an))  # fmt: skip
        # C4: prediction for D = c_0^- f(L_0^-)
        if name in FORM_F:
            f = FORM_F[name]
            for sg, a in an.items():
                m1, m2 = sg
                tr = a["S"]["i"] == 0 and a["S"]["w"] == 0
                pred = f(m1) + f(m2) != 0
                if tr != pred:
                    okc4 = False
                if not tr:
                    if (
                        f(m1) == 0
                        and f(m2) == 0
                        and not (a["S"]["i"] == 0 and a["S"]["w"] > 0)
                    ):
                        okc4 = False
                    if f(m1) == -f(m2) != 0 and not a["S"]["i"] > 0:
                        okc4 = False
                plan = f(m1) != 0 and f(m2) != 0
                if plan != tr:
                    c4notes.append(f"{name} {sg}: plan says {'T' if plan else 'NT'}, "
                                   f"computed {'T' if tr else 'NT'}")  # fmt: skip
            if name == "Dc" and nt:
                okc4 = False
    record(
        "C2.1-raise",
        ok21,
        "all rows: tau-symmetric, sectors kept, c-count +1, "
        f"im D in C, B_2 E in L ({okB}); J(D Lambda_2) = 0 follows" + "; ".join(d21),
    )
    record("C2.3-count", ok22, "dim E^(1)_sigma = 2 dim L^(0)_sigma in every sector")
    check_c2_brute(rng)
    record(
        "C2.2-family",
        ok24,
        "random members of the family and of P_D satisfy "
        "q = q^T, q D = 0, q|S_0 = p (and the zero coupling block) exactly",
    )
    # C3: control row
    ctrl = next(t for t in table if t[0] == "D0")
    okc3 = ctrl[7] == "yes" and all(t[7] == "yes" for t in table)
    record(
        "C3-table",
        okc3,
        "literal verdict 'yes' in every row, including the "
        "control D = 0 (coupling block dim S_0 * c' > 0)",
    )
    print(
        "\nTABLE (criterion (i), decision (A); kernel excess generic/decoupled, "
        "variant ker p = 6 | 10)"
    )
    for t in table:
        (name, desc, dsol, dP, nt, nt_per, exc, lit, ref, ref_per, i_tot, refv,
         rD, n, cp, Sbar, an) = t  # fmt: skip
        print(f"{name:6s} {desc}")
        print(f"   rank D {rD}, n = dim E/im D {n}, c' {cp}, dim S-bar {Sbar}")
        print(f"   dim Sol {dsol}, dim P_D {dP}, diff {dsol - dP} (= s c' = {s * cp})")
        print(f"   kernel excess (generic, decoupled): {exc[False]} | {exc[True]}")
        print(f"   non-transverse w.r.t. ker B_2 (sector, dim S cap im D, dim W): {nt}")
        print(f"   non-transverse w.r.t. S_per: {len(nt_per)}/{len(an)} sectors")
        print(
            f"   literal verdict {lit}; refined excess {ref} (S_per: {ref_per}), "
            f"E1a dim {i_tot}; refined verdict {refv}"
        )
    print(
        "\nper-sector data of Dc (sector: dim E, rank D, dim S, S cap E^(1), "
        "dim E^(1), dim L^(0))"
    )
    dc = next(t for t in table if t[0] == "Dc")
    for sg, a in dc[16].items():
        print(
            f"   {sg}: {a['dimE']}, {a['rD']}, {a['S']['dim']}, {a['S_cap_E1']}, "
            f"{a['dimE1']}, {a['dimL0']}"
        )
    record(
        "C4-prediction",
        okc4,
        "transverse w.r.t. ker B_2 iff f(m1) + f(m2) != 0, "
        "type (a) at common zeros, type (b) at f(m1) = -f(m2) != 0; Dc transverse "
        f"everywhere; plan wording mismatches: {c4notes}",
    )
    nf = sum(1 for _, ok, _ in RESULTS if not ok)
    print(f"\nSUMMARY seed {SEED}: {len(RESULTS) - nf}/{len(RESULTS)} PASS")
    return 1 if nf else 0


if __name__ == "__main__":
    sys.exit(main())
