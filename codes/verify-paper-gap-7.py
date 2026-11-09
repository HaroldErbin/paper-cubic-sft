"""
Paper gap 7: the two forms of the (2,2) relation of the raised family, weights, residual.

Record: agent/derivations/086-paper-gap-7.md (re-derivation of 026 Sec. 3.1-3.2 / R16, R31
in the paper's conventions: symmetric pairing g, Omega(A,B) = (-1)^|A| <A,B>, raising with
Omega^{-1}).

Claims tested (node IDs of record 086):
  C1.1        every (2,2) contraction  d^r_Psi F (Omega^-1) d^l_Psi' G  equals
              Omega(L_1, L_2) of the two superfield outputs (rule K signs), on generic data
  C1.3        the inputs-and-outputs-only relation C(H_0, H_0)_(2,2) = T1+T2+T3+T4,
              with the coefficients 1/2, 1/2, 1/4, 1 of (086.6)
  C2.1        the full relation E_(2,2) = C(S(Psi+Psi'), S(Psi+Psi'))_(2,2) equals the sum of
              the seven configurations (086.6)-(086.7)
  C2.2        mirror symmetry Tbar_i = T_i ;  C2.2-break: with plain g^{-1} they are opposite
  C2.3        E_(2,2) = 2(T1+T2+T3) + T4 ;  C2.3-break: weight of T4 set to 2 fails
  C3.1        R - E/2 = (1/2) Omega(l2(Psi,Psi'), l2(Psi,Psi')) identically (generic data)
  C3.2-sl2    sl2 + sl2* (ghost 1, 4): full master relation E = 0 at every bidegree
              C3.2-break: one structure constant perturbed -> E != 0
  C3.3-sl2    sl2: R_(2,2) != 0 and R = T4/2 ;  C3.3-equal: weights set equal (T4 counted
              twice in the full form) -> difference vanishes
  C3.3-heis   control, Heisenberg algebra (Jacobi-closed, l2 != 0, l2 o l2 = 0):
              E = 0, R = 0, both forms agree
Method: exact sparse Grassmann polynomials over Fractions; coefficients psi^a, psi'^a of
parity eps_a = N_gh mod 2.  The contraction uses right derivatives computed from the
monomial ordering (not the (-1)^eps shortcut) and the numerically inverted Omega matrix.
The outputs l_n(...) are reconstructed from <e_a, L> = V(e_a, ...) with rule K (coefficients
pass the basis vectors to their left), with the parity of each component read off the
polynomial.  Generic data: random graded-symmetric V2, V3, V4 on ghost numbers 1..4, dims
(1,2,2,1), NOT satisfying the master equation (the identities C1-C3.1 are algebraic).
NOT verified: anything about the closed-string vertices; the equivalence of C(H_0,H_0) = 0
with CFL Def. 2.3 (CFL Prop. 7.2, cited).

Usage:  uv run --no-sync python codes/verify-paper-gap-7.py
"""

from __future__ import annotations

import itertools
import random
import sys
from fractions import Fraction
from math import factorial

SEED = 20261004
RESULTS: list[tuple[str, bool]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    """Record and print one named PASS/FAIL check."""
    RESULTS.append((name, ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}")


# ---------------------------------------------------------------- Grassmann polynomials
class GA:
    """Polynomials in commuting and anticommuting variables, exact coefficients.

    A monomial is a sorted tuple of variable ids; even ids may repeat, odd ids may not.
    """

    def __init__(self, parity: list[int]) -> None:
        self.par = parity

    def canon(self, mono: list[int]) -> tuple[int, tuple[int, ...]]:
        """Sort a word of variables; return (sign, monomial) or (0, ())."""
        word = list(mono)
        sign = 1
        # bubble sort, counting swaps of two odd variables
        for i in range(len(word)):
            for j in range(len(word) - 1 - i):
                if word[j] > word[j + 1]:
                    if self.par[word[j]] and self.par[word[j + 1]]:
                        sign = -sign
                    word[j], word[j + 1] = word[j + 1], word[j]
        for i in range(len(word) - 1):
            if word[i] == word[i + 1] and self.par[word[i]]:
                return 0, ()
        return sign, tuple(word)

    def mul(self, a: dict, b: dict) -> dict:
        out: dict = {}
        for m1, c1 in a.items():
            for m2, c2 in b.items():
                s, m = self.canon(list(m1) + list(m2))
                if s:
                    out[m] = out.get(m, 0) + s * c1 * c2
        return {m: c for m, c in out.items() if c != 0}

    def add(self, *ps: dict, coeffs: list | None = None) -> dict:
        out: dict = {}
        coeffs = coeffs or [1] * len(ps)
        if len(coeffs) != len(ps):
            raise ValueError("one coefficient per polynomial")
        for p, k in zip(ps, coeffs):
            for m, c in p.items():
                out[m] = out.get(m, 0) + k * c
        return {m: c for m, c in out.items() if c != 0}

    def dl(self, p: dict, v: int) -> dict:
        """Left derivative: move v to the front, then strip it."""
        out: dict = {}
        for m, c in p.items():
            if v not in m:
                continue
            i = m.index(v)
            n_v = m.count(v)
            sign = (-1) ** sum(self.par[x] for x in m[:i]) if self.par[v] else 1
            rest = m[:i] + m[i + 1 :]
            out[rest] = out.get(rest, 0) + sign * c * (1 if self.par[v] else n_v)
        return {m: c for m, c in out.items() if c != 0}

    def dr(self, p: dict, v: int) -> dict:
        """Right derivative: move v to the end, then strip it."""
        out: dict = {}
        for m, c in p.items():
            if v not in m:
                continue
            i = m.index(v)
            n_v = m.count(v)
            sign = (-1) ** sum(self.par[x] for x in m[i + 1 :]) if self.par[v] else 1
            rest = m[:i] + m[i + 1 :]
            out[rest] = out.get(rest, 0) + sign * c * (1 if self.par[v] else n_v)
        return {m: c for m, c in out.items() if c != 0}

    def parity(self, p: dict) -> int | None:
        ps = {sum(self.par[x] for x in m) % 2 for m in p}
        if not ps:
            return None
        assert len(ps) == 1, "inhomogeneous polynomial"
        return ps.pop()


def bideg(p: dict, nb: int, k: int, l: int) -> dict:
    """Part of p with k variables of the first set (< nb) and l of the second."""
    return {
        m: c
        for m, c in p.items()
        if sum(1 for x in m if x < nb) == k and sum(1 for x in m if x >= nb) == l
    }


def is_zero(p: dict) -> bool:
    return not p


def size(p: dict) -> Fraction:
    return sum((abs(Fraction(c)) for c in p.values()), Fraction(0))


# ---------------------------------------------------------------- graded space and data
class Model:
    """Graded space with symmetric pairing g, vertices V_n, superfields Psi, Psi'."""

    def __init__(self, ghosts: list[int], g: dict, V: dict[int, dict]) -> None:
        self.gh = ghosts
        self.eps = [n % 2 for n in ghosts]
        self.N = len(ghosts)
        self.g = g  # {(a, b): value}, symmetric
        self.V = V  # n -> {(a1..an): value}, full graded-symmetric tensor
        # variables: psi^a -> a, psi'^a -> N + a ; parity eps_a
        self.ga = GA(self.eps + self.eps)
        self.ginv = inverse(self.N, g)
        omega = {(a, b): (-1) ** self.eps[a] * v for (a, b), v in g.items()}
        self.omega = omega
        self.oinv = inverse(self.N, omega)

    def field(self, which: str) -> list[dict]:
        """Coefficient list u^a of Psi ('p'), Psi' ('q') or Psi + Psi' ('u')."""
        out = []
        for a in range(self.N):
            p = {(a,): 1}
            q = {(self.N + a,): 1}
            out.append({"p": p, "q": q, "u": self.ga.add(p, q)}[which])
        return out

    def vertex(self, n: int, args: list) -> dict:
        """V_n(args) with rule K; an arg is a coefficient list or ('e', a)."""
        total: dict = {}
        for idx, val in self.V.get(n, {}).items():
            coef = {(): Fraction(val)}
            ok = True
            for k, (arg, a) in enumerate(zip(args, idx)):
                if isinstance(arg, tuple):  # basis vector
                    if arg[1] != a:
                        ok = False
                        break
                    continue
                c = arg[a]
                if not c:
                    ok = False
                    break
                # coefficient passes e_{a_j}, j < k (rule K)
                par_c = self.ga.parity(c)
                s = (-1) ** (par_c * sum(self.eps[b] for b in idx[:k]))
                coef = self.ga.mul(coef, {m: s * v for m, v in c.items()})
            if ok and coef:
                total = self.ga.add(total, coef)
        return total

    def output(self, n: int, args: list) -> list[dict]:
        """Superfield L = l_n(args): <e_a, L> = V_{n+1}(e_a, args), rule K."""
        X = [self.vertex(n + 1, [("e", a)] + args) for a in range(self.N)]
        L = []
        for c in range(self.N):
            comp: dict = {}
            for a in range(self.N):
                gi = self.ginv.get((c, a), 0)
                if gi == 0 or not X[a]:
                    continue
                # <e_a, L^c e_c> = (-1)^{|L^c| eps_a} L^c g_ac ; |L^c| = |X_a|
                s = (-1) ** (self.ga.parity(X[a]) * self.eps[a])
                comp = self.ga.add(comp, X[a], coeffs=[1, s * gi])
            L.append(comp)
        return L

    def Omega(self, L: list[dict], K: list[dict], rule_k: bool = True) -> dict:
        """Omega(L, K) with rule K: L^c (-1)^{|K^d| eps_c} K^d Omega_cd."""
        out: dict = {}
        for (c, d), w in self.omega.items():
            if not L[c] or not K[d]:
                continue
            s = (-1) ** (self.ga.parity(K[d]) * self.eps[c]) if rule_k else 1
            out = self.ga.add(out, self.ga.mul(L[c], K[d]), coeffs=[1, s * w])
        return out

    def S(self, which: str) -> dict:
        """S(field) = sum_n V_n(field^n)/n! (g_s = 1)."""
        f = self.field(which)
        out: dict = {}
        for n in self.V:
            out = self.ga.add(
                out, self.vertex(n, [f] * n), coeffs=[1, Fraction(1, factorial(n))]
            )
        return out

    def contract(self, F: dict, G: dict, plain: bool = False) -> dict:
        """d^r_{psi^a} F (Omega^-1)^{ab} d^l_{psi'^b} G  (plain: g^{-1} instead)."""
        mat = self.ginv if plain else self.oinv
        out: dict = {}
        for (a, b), w in mat.items():
            A = self.ga.dr(F, a)
            if not A:
                continue
            B = self.ga.dl(G, self.N + b)
            if B:
                out = self.ga.add(out, self.ga.mul(A, B), coeffs=[1, w])
        return out

    def H(self, k: int, l: int) -> dict:
        """Bidegree piece H_{k,l} = V_{k+l}(Psi^k, Psi'^l)/(k! l!)."""
        p, q = self.field("p"), self.field("q")
        return {
            m: c * Fraction(1, factorial(k) * factorial(l))
            for m, c in self.vertex(k + l, [p] * k + [q] * l).items()
        }


def inverse(N: int, M: dict) -> dict:
    """Exact inverse of a sparse N x N matrix (Gauss-Jordan over Fractions)."""
    A = [
        [Fraction(M.get((i, j), 0)) for j in range(N)]
        + [Fraction(int(i == j)) for j in range(N)]
        for i in range(N)
    ]
    for col in range(N):
        piv = next(r for r in range(col, N) if A[r][col] != 0)
        A[col], A[piv] = A[piv], A[col]
        pv = A[col][col]
        A[col] = [x / pv for x in A[col]]
        for r in range(N):
            if r != col and A[r][col] != 0:
                f = A[r][col]
                A[r] = [x - f * y for x, y in zip(A[r], A[col])]
    return {(i, j): A[i][N + j] for i in range(N) for j in range(N) if A[i][N + j] != 0}


def graded_sym(ghosts: list[int], n: int, rng: random.Random, sat: int) -> dict:
    """Random graded-symmetric tensor V_n, nonzero only at total ghost number sat."""
    eps = [x % 2 for x in ghosts]
    N = len(ghosts)
    V: dict = {}
    for base in itertools.combinations_with_replacement(range(N), n):
        if sum(ghosts[a] for a in base) != sat:
            continue
        # odd index repeated -> graded symmetry forces zero
        if any(eps[a] and base.count(a) > 1 for a in set(base)):
            continue
        val = Fraction(rng.randint(-5, 5) or 1)
        for perm in set(itertools.permutations(range(n))):
            idx = tuple(base[i] for i in perm)
            # Koszul sign of the permutation on odd entries
            s = 1
            for i in range(n):
                for j in range(i + 1, n):
                    if perm[i] > perm[j] and eps[base[perm[i]]] and eps[base[perm[j]]]:
                        s = -s
            V[idx] = s * val
    return V


def generic_model(rng: random.Random) -> Model:
    ghosts = [1, 2, 2, 3, 3, 4]
    # symmetric pairing: 1<->4, 2<->3 blocks, random nondegenerate
    g = {(0, 5): 1, (5, 0): 1}
    blk = [[rng.randint(1, 4), rng.randint(-3, 3)], [0, rng.randint(1, 4)]]
    for i in range(2):
        for j in range(2):
            g[(1 + i, 3 + j)] = blk[i][j]
            g[(3 + j, 1 + i)] = blk[i][j]
    g = {k: v for k, v in g.items() if v != 0}
    V = {n: graded_sym(ghosts, n, rng, 2 * n) for n in (2, 3, 4)}
    return Model(ghosts, g, V)


def lie_model(f: dict, dim: int) -> Model:
    """g_(1) + g*_(4); <c_i, c*^j> = delta; V3(c*^i, c_j, c_k) = f_jk^i, graded-sym."""
    ghosts = [1] * dim + [4] * dim
    eps = [x % 2 for x in ghosts]
    g = {}
    for i in range(dim):
        g[(i, dim + i)] = 1
        g[(dim + i, i)] = 1
    V3: dict = {}
    for (j, k, i), val in f.items():
        base = (dim + i, j, k)
        for perm in itertools.permutations(range(3)):
            idx = tuple(base[p] for p in perm)
            s = 1
            for a in range(3):
                for b in range(a + 1, 3):
                    if perm[a] > perm[b] and eps[base[perm[a]]] and eps[base[perm[b]]]:
                        s = -s
            V3[idx] = V3.get(idx, 0) + s * Fraction(val)
    V3 = {k: v for k, v in V3.items() if v != 0}
    return Model(ghosts, g, {3: V3})


def structure(pairs: dict, dim: int) -> dict:
    """f_jk^i from [t_j, t_k] = sum_i f_jk^i t_i given for j < k."""
    f = {}
    for (j, k), res in pairs.items():
        for i, v in res.items():
            f[(j, k, i)] = v
            f[(k, j, i)] = -v
    return f


# basis order e, f, h:  [h,e] = 2e, [h,f] = -2f, [e,f] = h
SL2 = structure({(2, 0): {0: 2}, (2, 1): {1: -2}, (0, 1): {2: 1}}, 3)
HEIS = structure({(0, 1): {2: 1}}, 3)  # [x, y] = z


# ---------------------------------------------------------------- the configurations
def configurations(M: Model, plain: bool = False) -> dict:
    """T and Tbar of (086.6)-(086.7) as contractions C(H_{k1,l1}, H_{k2,l2})."""
    cfg = {
        "T1": (1, 1, 2, 2),
        "T2": (2, 2, 1, 1),
        "T3": (1, 2, 2, 1),
        "T4": (2, 1, 1, 2),
        "Tb1": (3, 1, 0, 2),
        "Tb2": (2, 0, 1, 3),
        "Tb3": (3, 0, 0, 3),
    }
    return {
        k: M.contract(M.H(a, b), M.H(c, d), plain) for k, (a, b, c, d) in cfg.items()
    }


def output_form(M: Model) -> dict:
    """T_i from (086.6) as Omega(L1, L2) of the superfield outputs (independent path)."""
    p, q = M.field("p"), M.field("q")
    Qp, Qq = M.output(1, [p]), M.output(1, [q])
    l2pq = M.output(2, [p, q])
    l2pp, l2qq = M.output(2, [p, p]), M.output(2, [q, q])
    l3ppq, l3pqq = M.output(3, [p, p, q]), M.output(3, [p, q, q])
    h, qt = Fraction(1, 2), Fraction(1, 4)
    sc = lambda c, P: {m: c * v for m, v in P.items()}  # noqa: E731
    return {
        "T1": sc(h, M.Omega(Qq, l3ppq)),
        "T2": sc(h, M.Omega(l3pqq, Qp)),
        "T3": sc(qt, M.Omega(l2qq, l2pp)),
        "T4": M.Omega(l2pq, l2pq),
        "Tb1": sc(h, M.Omega(l3ppq, Qq)),
        "Tb2": sc(h, M.Omega(Qp, l3pqq)),
        "Tb3": sc(qt, M.Omega(l2pp, l2qq)),
    }


def full_and_reduced(M: Model) -> tuple[dict, dict]:
    """E = C(S(u), S(u)) and R = C(H0, H0), full polynomials."""
    Su = M.S("u")
    H0 = M.ga.add(Su, M.S("p"), M.S("q"), coeffs=[1, -1, -1])
    return M.contract(Su, Su), M.contract(H0, H0)


def main() -> int:
    print(f"seed {SEED}")
    rng = random.Random(SEED)
    ga_sub = lambda M, a, b, c=1: M.ga.add(a, b, coeffs=[1, -c])  # noqa: E731

    # ---------------- generic data (identities C1-C3.1 are algebraic)
    M = generic_model(rng)
    nb = M.N
    T = configurations(M)
    O = output_form(M)
    E, R = full_and_reduced(M)
    E22, R22 = bideg(E, nb, 2, 2), bideg(R, nb, 2, 2)
    nz = all(T[k] for k in T)
    check(
        "C2.1-nonhollow",
        nz,
        "all seven T nonzero: " + ", ".join(f"{k}:{size(v)}" for k, v in T.items()),
    )
    check(
        "C1.1",
        all(is_zero(ga_sub(M, T[k], O[k])) for k in T),
        "contraction == Omega(L1, L2) for all seven configurations",
    )
    p_, q_ = M.field("p"), M.field("q")
    l2 = M.output(2, [p_, q_])
    check(
        "C1.1-break",
        not is_zero(ga_sub(M, T["T4"], M.Omega(l2, l2, rule_k=False))),
        "Omega read without the rule-K sign does NOT match T4 (expected)",
    )
    check(
        "C2.2",
        all(is_zero(ga_sub(M, T[f"T{i}"], T[f"Tb{i}"])) for i in (1, 2, 3)),
        "Tbar_i == T_i",
    )
    Tp = configurations(M, plain=True)
    anti = (
        all(is_zero(M.ga.add(Tp[f"T{i}"], Tp[f"Tb{i}"])) for i in (1, 2, 3))
        and Tp["T1"]
    )
    check(
        "C2.2-break",
        bool(anti),
        "plain g^{-1}: Tbar_i == -T_i (mirror pairs cancel), T1 != 0",
    )
    sum7 = M.ga.add(*T.values())
    check(
        "C2.1",
        is_zero(ga_sub(M, E22, sum7)),
        f"E_(2,2) == sum of seven configurations, |E22| = {size(E22)}",
    )
    two = M.ga.add(T["T1"], T["T2"], T["T3"], T["T4"], coeffs=[2, 2, 2, 1])
    check("C2.3", is_zero(ga_sub(M, E22, two)), "E_(2,2) == 2(T1+T2+T3) + T4")
    bad = M.ga.add(T["T1"], T["T2"], T["T3"], T["T4"], coeffs=[2, 2, 2, 2])
    check(
        "C2.3-break",
        not is_zero(ga_sub(M, E22, bad)),
        "weight 2 on T4 does NOT match (expected)",
    )
    four = M.ga.add(T["T1"], T["T2"], T["T3"], T["T4"])
    check(
        "C1.3",
        is_zero(ga_sub(M, R22, four)),
        f"R_(2,2) == T1+T2+T3+T4, |R22| = {size(R22)}",
    )
    resid = M.ga.add(R22, E22, coeffs=[1, Fraction(-1, 2)])
    check(
        "C3.1",
        is_zero(ga_sub(M, resid, {m: Fraction(1, 2) * c for m, c in O["T4"].items()})),
        "R - E/2 == (1/2) Omega(l2(Psi,Psi'), l2(Psi,Psi'))",
    )
    check(
        "C3.1-break",
        not is_zero(ga_sub(M, resid, O["T4"])),
        "R - E/2 == Omega(l2,l2) (weight 1) fails (expected)",
    )

    # ---------------- sl2 + sl2* at ghost numbers 1 and 4
    S2 = lie_model(SL2, 3)
    E, R = full_and_reduced(S2)
    check(
        "C3.2-sl2",
        is_zero(E),
        f"master relation E == 0 at every bidegree ({len(S2.V[3])} V3 components)",
    )
    bad_f = structure({(2, 0): {0: 2}, (2, 1): {1: -3}, (0, 1): {2: 1}}, 3)
    Eb, _ = full_and_reduced(lie_model(bad_f, 3))
    check(
        "C3.2-break",
        not is_zero(Eb),
        f"Jacobi-violating [h,f] = -3f: E != 0, |E| = {size(Eb)}",
    )
    R22 = bideg(R, S2.N, 2, 2)
    Os = output_form(S2)
    check(
        "C3.3-sl2",
        bool(R22)
        and is_zero(
            ga_sub(S2, R22, {m: Fraction(1, 2) * c for m, c in Os["T4"].items()})
        ),
        f"R_(2,2) != 0 ({len(R22)} monomials, |R22| = {size(R22)}) and == T4/2",
    )
    Ts = configurations(S2)
    eq_full = S2.ga.add(Ts["T1"], Ts["T2"], Ts["T3"], Ts["T4"], coeffs=[2, 2, 2, 2])
    check(
        "C3.3-equal",
        is_zero(ga_sub(S2, R22, eq_full, Fraction(1, 2))),
        "weights set equal (T4 counted twice in the full form): R - (full)/2 == 0",
    )
    rest = {kl: bideg(R, S2.N, *kl) for kl in [(3, 1), (1, 3)]}
    check(
        "C3.3-min1",
        all(is_zero(v) for v in rest.values()),
        "sl2: R_(3,1) = R_(1,3) = 0 (min(k,l) = 1 forms agree)",
    )
    print("  sample R_(2,2) monomials (sl2):", list(R22.items())[:3])

    # ---------------- Heisenberg control: Jacobi-closed, l2 != 0, l2 o l2 = 0
    Hs = lie_model(HEIS, 3)
    E, R = full_and_reduced(Hs)
    p, q = Hs.field("p"), Hs.field("q")
    l2 = Hs.output(2, [p, q])
    Th = configurations(Hs)
    check(
        "C3.3-heis",
        is_zero(E) and is_zero(R) and any(l2),
        "Heisenberg: E == 0 and R == 0 (both forms hold), l2(Psi,Psi') != 0; "
        + "T sizes "
        + ", ".join(f"{k}:{size(v)}" for k, v in Th.items()),
    )
    print("  sl2 T sizes:", ", ".join(f"{k}:{size(v)}" for k, v in Ts.items()))

    n_fail = sum(1 for _, ok in RESULTS if not ok)
    print(f"summary: {len(RESULTS) - n_fail}/{len(RESULTS)} PASS (seed {SEED})")
    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(main())
