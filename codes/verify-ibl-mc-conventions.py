"""
Task 19a: grading of the genus-zero Maurer-Cartan equation of the raised IBL family.

Record: agent/derivations/103-ibl-mc-conventions.md (claim-tree nodes in brackets).

Setting (record A1-A8).  CFL: hat p = sum hat p_{k,l,g} hbar^{k+g-1} tau^{k+l+2g-2},
|hbar| = 2d, |p_{k,l,g}| = -2d(k+g-1) - 1 (CFL Def. 2.3, R5); d = 1/2 and strand degree
3 - N_gh on every strand (R23); N_gh(p_{k,l,0}) = 3l - 2k (R23); m = hbar^{-1}(Psi_1 + Psi_2)
(CFL Def. 9.1); the components are those of e^{-m} hat p(e^m) in E_1 C, E_2 C; g_s = tau.
Gauge parameter lambda = hbar^{-1}(Lambda_1 + Lambda_2) in delta e^m = [hat p, lambda] e^m.

Checks (each named after the node it tests):
  C1       [C1]  ghost-number shift of every p_{k,l} (k, l >= 1, k + l <= 4), measured on a
                 support-constrained model (vertices V_n saturating at 2n, pairing at 5),
                 equals R23's 3l - 2k, both families; CFL degree from the strand
                 dictionary equals R5's -2d(k-1) - 1 at d = 1/2.
  C2-C3    [C2, C3]  the connected terms of e^{-m} hat p(e^m) in E_1 and E_2, enumerated
                 from CFL's definition of hat phi (an order-k differential operator) with
                 m = hbar^{-1}(Psi_1 + Psi_2), equal the record's table (operation,
                 hbar-power, g_s-power).  -break: a perturbed hbar rule (k-1) - a - 2b
                 disagrees with the table (fix pass; replaces a decorative leg).
  C2-C3-E34 [C8.1.5] (fix pass) the E_3, E_4 terms equal (MC.8)-(MC.9) (operation,
                 hbar-, g_s-powers), no E_L with L > 4, output-counting order l_p - 1,
                 measured N_gh = 2L + l_p at N_gh(Psi_2) = 4 (terms nonzero); -break: the
                 table without p13(Psi) is detected.  Coefficients NOT checked.
  NV       [C4-C6] (fix pass) non-vacuity: no E_1, E_2 term vanishes at N_gh(Psi_2) =
                 4, 5, no gauge term at (4, 3), (5, 4), so C4-C6 run over every term.
  C5-ord   [C5.4] (fix pass) order-by-order homogeneity: CFL weight -> N_gh(Psi_2) {5},
                 output weight -> N_gh(Sigma_2) {4}; Lambda_2: CFL {4}, output {3};
                 -break: merging the orders (x = 0) leaves no value.
  C5-ord-n [C5.4] (final fix pass) dressing hbar^{-1-n} of the two-string component,
                 n in -2..3: order by order {5} (n = 0), {4} (n = 1), every value otherwise;
                 whole component over x in -3..3: only (-1, 5 - n).  -break: the rule
                 hbar^{-n} at n = 1 misses {4}.
  C4       [C4]  CFL degree (|hbar| = 1), measured ghost numbers: the set of N_gh(Psi_2)
                 in the scan making E_1 and E_2 both homogeneous is {5}.
                 -break: with |hbar| = 0 or |hbar| = 2 (wrong gradings) the set is empty.
  C5       [C5]  physical ghost number, N_gh(hbar) = N_gh(g_s) = 0: E_1 alone -> {4},
                 E_2 alone -> {}, both -> {}; over N_gh(hbar) = x in -3..3 the unique pair
                 (x, N_gh(Psi_2)) making both homogeneous is (-1, 5), and CFL-homogeneity
                 coincides with x = -1 homogeneity at every scanned value.
  C5.3     [C5.3] at N_gh(Psi_2) = 4 every term of E_L has N_gh = 2L + l_p; the E_2 terms split into the ghost-5 sector (exactly
                 the lifts) and the ghost-6 sector; removing the lifts makes E_2 homogeneous.
  C6       [C6]  Lambda grading, every enumerated term of delta Psi_1, delta Psi_2 (k+l <= 4):
                 CFL with N_gh(Psi_2) = 5: N_gh(Lambda_2) set {4}; physical with
                 N_gh(Psi_2) = 4: delta Psi_1 alone -> {3}, delta Psi_2 -> {} for every value.
  C7.1     [C7.1] with the weight hbar^{-n} on the n-string components (Sigma_2 = hbar
                 Psi_2, Lambda_2 likewise) and N_gh (Psi, Sigma_2; Lambda_1, Lambda_2) =
                 (2, 4; 1, 3), all four components are CFL-homogeneous and every term of
                 E_L has hbar^{-L + l_p - 1} (l_p = outputs of the product).
                 -break: CFL's uniform weight with Sigma_2 at 4 is not homogeneous.
  TW       [C2.3, C3.3] R87 twist: every term evaluated with p^Omega equals the sprod
                 evaluation times (-1)^{|fed inputs|} componentwise; on Psi_2 with
                 (2,2) strands every MC term agrees between the families (twist +1); on
                 Psi_2 at total ghost 5 the E_1 terms flip sign.
Task 19b (record blocks MC, H2, V19b; nodes C8.x):
  C8.1     [C8.1] e^{-m'} hat p_{k,l} e^{m'} computed literally (CFL (2.1) in the
                 symmetric algebra: k-subsets of letters, Koszul sign of the moves,
                 outputs to the left; e^{m'} and e^{-m'} expanded), m' = t Psi + u Sigma_2,
                 equals the record's formula (MC.3) block by block ((k, l), k + l <= 4,
                 output length L = 1, 2), two (t, u); every block used is nonzero; with
                 Psi_2 = 0 the E_1 component is the original EOM.
                 -break: the paper's 1/3! on l3(Psi, Psi_2), 1/2 on the lift of
                 l3(Psi_2, .), and the sign -1 on the lift of l2(Psi, .) each FAIL.
  C8.1-par [A9]  the raised outputs are graded-symmetric in the shifted parity N_gh + 1,
                 not in the physical one: the physical quotient kills the (3,3)-strand
                 part of p12(Psi), the shifted quotient kills Sigma_2 (no single parity).
  C8.1-review [C8.1.3] Task 17's display (2) (CFL weight, m_{2,0} hbar-independent),
                 evaluated with hat and the connected part (inclusion-exclusion), equals the
                 literal blocks; after m_{2,0} = hbar^{-1} Sigma_2 and phi^{-1} every term
                 sits at hbar^{l_p - 1}.
  C8.2     [C8.2.2-C8.2.4] reading (I) of H2: the exact linear systems M_1(f) = c_1 E_Psi,
                 M_2^(6)(f) = c_2 E_Sigma (f = alpha Sigma_2 + beta Psi^2; alpha, beta, c_i
                 Laurent in g_s, powers -2..2; four random samples; through O(g_s^2)) are
                 inconsistent, separately and jointly.
  C8.2-break [C8.2.2-C8.2.4] drop M-a (g_s l2(Psi_2)): E_1 solvable; drop M-b (g_s
                 p12(Psi)): E_6 solvable; drop both: joint still unsolvable (M-c); drop M-a,
                 M-b, M-c: joint solvable with alpha_0 = 1/6, beta_0 = -1/6.
  C8.2-quot [C8.2.6] kernel model (V_4 = 0 when e_2 occurs twice, N = e_2 x e_2):
                 p22(N) = 0, E_Psi, E_Sigma invariant under Sigma_2 -> Sigma_2 + N, the MC
                 components with f = Sigma_2/6 not (l2(N), hat Q N nonzero).
  C8.2-shell [C8.2.8] free model (Q_B e_2 = 0): Psi = eps e_2, Sigma_2 = Psi^2 solves the
                 EOM at O(eps); the O(eps) part of M_2^(6) is g_s p12(e_2) != 0.
  C8.2-action [C8.2.9] (H2.6): M_1 and M_2^(6) are the gradients of S_MC =
                 sum_n g_s^{n-2} V_n((e^{Psi + Psi_2})_n) - V_2(Psi_2) at g_s^0..g_s^2.
  Parity (A9 = convention C6): field letters (Psi, Psi_2, leftover strands) carry the
  physical parity; the output words of two-output blocks are normalized with the shifted
  parity.  eps_out gives one-output blocks the physical parity, output letter included;
  C6 puts every output strand in the shifted parity; on the sectors used the output and
  field strands have opposite parity, where both give the exchange sign +1 (immaterial).
  Two-output words get the shifted parity on every letter, leftover field letters
  included, contrary to C6: immaterial for E_2 (no leftover letters), wrong for a literal
  E_3/E_4 extension, hence C2-C3-E34 measures ghost numbers on unsymmetrized tensors.
  eps_out is therefore not C6 and cannot serve as the falsifier of H-par (record 103).
  C8.2-action: <x, l_{n-1}> = V_n is definitional in raise_family, so its independent
  content is the combinatorics of the exponential, not the operations.
  NOT verified: hypothesis H-par (single-contraction part of hat p' o hat p' = 0 in the
  C6-graded algebra) and the double-contraction relations: the random data do not
  satisfy the L-infinity / IBL relations, so no check bears on them.
  NOT verified (19b): genus >= 1, k + l > 4, field strands other than (2,2) for Sigma_2,
  readings (II) and (III) beyond the first-order statements of C8.2-shell; the L-infinity
  relations are not imposed on the random data (the component identities do not use them).
Method: exact Fractions; the raised families are built by raise_family of
codes/verify-ibl-generating-sign.py (engine of codes/verify-paper-gap-7.py), neither edited.
Two seeds (random pairing blocks, vertices, fields).
NOT verified: signs of the component equations (Koszul signs of the lifts are not
tracked: gradings only), the combinatorial coefficients (record, by hand; 19b), the
closed-string vertices, any statement at genus >= 1, CFL's operator-level signs.

Usage:  .venv/bin/python codes/verify-ibl-mc-conventions.py
"""

from __future__ import annotations

import importlib.util
import itertools
import random
import sys
from fractions import Fraction
from math import factorial
from pathlib import Path

ROOT = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location(
    "iblgen", ROOT / "verify-ibl-generating-sign.py"
)
iblgen = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(iblgen)
gap7 = iblgen.gap7

SEEDS = (20261018, 20261019)
RESULTS: list[tuple[str, bool]] = []
GHOSTS = [0, 1, 2, 2, 3, 3, 4, 5]  # pairing pairs N_gh a with 5 - a
Y_SCAN = range(2, 7)  # N_gh(Psi_2) values scanned
Z_SCAN = range(1, 6)  # N_gh(Lambda_2) values scanned
X_SCAN = range(-3, 4)  # N_gh(hbar) values scanned


def check(name: str, ok: bool, detail: str = "") -> None:
    """Record and print one named PASS/FAIL check."""
    RESULTS.append((name, bool(ok)))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}")


# ---------------------------------------------------------------- model
def model(rng: random.Random):
    """Graded model: symmetric pairing at total ghost 5, V_n graded symmetric at 2n."""
    gh = GHOSTS
    g = {(0, 7): 1, (7, 0): 1, (1, 6): 1, (6, 1): 1}
    while True:
        blk = [[rng.randint(-3, 3) for _ in range(2)] for _ in range(2)]
        if blk[0][0] * blk[1][1] - blk[0][1] * blk[1][0] != 0:
            break
    for i in range(2):
        for j in range(2):
            if blk[i][j]:
                g[(2 + i, 4 + j)] = blk[i][j]
                g[(4 + j, 2 + i)] = blk[i][j]
    V = {n: gap7.graded_sym(gh, n, rng, 2 * n) for n in (2, 3, 4)}
    return gap7.Model(gh, g, V)


def rand_tensor(M, rng: random.Random, rank: int, total: int, strands=None) -> dict:
    """Random graded-symmetric tensor (input strands, physical parity) at total ghost."""
    T: dict = {}
    for base in itertools.combinations_with_replacement(range(M.N), rank):
        if sum(M.gh[a] for a in base) != total:
            continue
        if strands is not None and sorted(M.gh[a] for a in base) != sorted(strands):
            continue
        if any(M.eps[a] and base.count(a) > 1 for a in set(base)):
            continue
        val = Fraction(rng.choice([-4, -3, -2, -1, 1, 2, 3, 4]))
        for perm in set(itertools.permutations(range(rank))):
            idx = tuple(base[i] for i in perm)
            s = 1
            for i in range(rank):
                for j in range(i + 1, rank):
                    if (
                        perm[i] > perm[j]
                        and M.eps[base[perm[i]]]
                        and M.eps[base[perm[j]]]
                    ):
                        s = -s
            T[idx] = s * val
    return T


def feed(M, comp: dict, factors: list, twist: bool = False) -> dict:
    """Apply p_{k,l} ({(b, c): v}) to t strands of each factor (T, t), summing over the
    choice of fed strands when t < rank(T) (the lift); output (c..., leftovers...).

    Koszul signs of the strand moves are not tracked (gradings only).  With twist,
    each basis input b is weighted by (-1)^{sum eps(b)} (R87).
    """
    byb: dict = {}
    for (b, c), v in comp.items():
        byb.setdefault(b, []).append((c, v))
    opts = []
    for T, t in factors:
        lst = []
        for idx, val in T.items():
            r = len(idx)
            for pos in itertools.combinations(range(r), t):
                fed = tuple(idx[p] for p in pos)
                left = tuple(idx[p] for p in range(r) if p not in pos)
                lst.append((fed, left, val))
        opts.append(lst)
    out: dict = {}
    for combo in itertools.product(*opts):
        b = sum((x[0] for x in combo), ())
        if b not in byb:
            continue
        left = sum((x[1] for x in combo), ())
        w = Fraction(1)
        for x in combo:
            w *= x[2]
        if twist:
            w *= (-1) ** sum(M.eps[i] for i in b)
        for c, v in byb[b]:
            key = c + left
            out[key] = out.get(key, 0) + v * w
    return {k: v for k, v in out.items() if v != 0}


def support(M, T: dict) -> set:
    return {sum(M.gh[i] for i in key) for key in T}


# ---------------------------------------------------------------- enumeration
def enum_mc(kl_max: int = 4) -> list[dict]:
    """Connected terms of e^{-m} hat p(e^m), m = hbar^{-1}(Psi_1 + Psi_2), genus zero.

    hat p_{k,l,0} hbar^{k-1} tau^{k+l-2} is an order-k differential operator (CFL (2.1)):
    its k inputs are strands of j factors of m, each factor feeding >= 1 strand; the
    unfed strands stay as outputs.  hbar-power (k-1) - j, output E-degree
    l + sum(unfed strands).
    """
    out = []
    for k in range(1, kl_max):
        for l in range(1, kl_max - k + 1):
            for a in range(0, k + 1):
                for b in range(0, k + 1):
                    if a + b == 0:
                        continue
                    for takes in itertools.combinations_with_replacement((1, 2), b):
                        if a + sum(takes) != k:
                            continue
                        deg = l + sum(2 - t for t in takes)
                        out.append(
                            dict(
                                k=k,
                                l=l,
                                a=a,
                                takes=takes,
                                out=deg,
                                hbar=(k - 1) - (a + b),
                                tau=k + l - 2,
                            )
                        )
    return out


def enum_gauge(kl_max: int = 4) -> list[dict]:
    """Connected terms of e^{-m}[hat p, lambda] e^m linear in lambda = hbar^{-1}(L1 + L2).

    One lambda factor feeds >= 1 strand; hbar-power (k-1) - 1 - j; the power reported is
    that of delta Psi_out, i.e. relative to delta(hbar^{-1} Psi_out): +1.
    """
    out = []
    for k in range(1, kl_max):
        for l in range(1, kl_max - k + 1):
            for lam, rl in (("L1", 1), ("L2", 2)):
                for tl in range(1, rl + 1):
                    for a in range(0, k):
                        for b in range(0, k):
                            for takes in itertools.combinations_with_replacement(
                                (1, 2), b
                            ):
                                if tl + a + sum(takes) != k:
                                    continue
                                deg = l + (rl - tl) + sum(2 - t for t in takes)
                                out.append(
                                    dict(
                                        k=k,
                                        l=l,
                                        lam=lam,
                                        tl=tl,
                                        a=a,
                                        takes=takes,
                                        out=deg,
                                        hbar=(k - 1) - 1 - (a + b) + 1,
                                        tau=k + l - 2,
                                    )
                                )
    return out


def label(t: dict) -> str:
    """Operation name of an enumerated term (record notation)."""
    args = ["Psi1"] * t["a"]
    lift = []
    for s in t["takes"]:
        if s == 2:
            args.append("Psi2")
        else:
            lift.append("Psi2")
    if "lam" in t:
        if t["tl"] == 1 and t["lam"] == "L2":
            lift.append("L2")
        else:
            args.append(t["lam"])
    name = f"p{t['k']}{t['l']}({', '.join(args + ['.'] * len(lift))})"
    if lift:
        tag = " [lift of p_{1,1}, derived]" if (t["k"], t["l"]) == (1, 1) else ""
        name = f"lift {name} on {'/'.join(lift)}{tag}"
    return name


# record table (block E1, E2): (k, l, a, takes) -> (hbar-power, tau-power)
TABLE_E1 = {
    (1, 1, 1, ()): (-1, 0),  # Q_B Psi_1
    (2, 1, 2, ()): (-1, 1),  # (1/2) l2(Psi_1^2)
    (3, 1, 3, ()): (-1, 2),  # (1/6) l3(Psi_1^3)
    (2, 1, 0, (2,)): (0, 1),  # l2(Psi_2), both strands
    (3, 1, 1, (2,)): (0, 2),  # l3(Psi_1, Psi_2)
}
TABLE_E2 = {
    (1, 1, 0, (1,)): (-1, 0),  # lift of p_{1,1} on Psi_2 (derived)
    (2, 1, 1, (1,)): (-1, 1),  # lift of l2(Psi_1, .) on Psi_2
    (3, 1, 2, (1,)): (-1, 2),  # lift of (1/2) l3(Psi_1^2, .) on Psi_2
    (1, 2, 1, ()): (-1, 1),  # p_{1,2}(Psi_1)
    (2, 2, 2, ()): (-1, 2),  # (1/2) p_{2,2}(Psi_1^2)
    (2, 2, 0, (2,)): (0, 2),  # p_{2,2}(Psi_2)
    (3, 1, 0, (1, 2)): (0, 2),  # lift of l3(Psi_2, .) on a second Psi_2
}
LIFTS_E2 = {(1, 1, 0, (1,)), (2, 1, 1, (1,)), (3, 1, 2, (1,)), (3, 1, 0, (1, 2))}
# record (MC.8)-(MC.9), fix pass: E_3 and E_4 terms (CFL weight hbar-power, tau-power)
TABLE_E3 = {
    (1, 3, 1, ()): (-1, 2),  # p_{1,3}(Psi_1), M-r0 (baseline)
    (1, 2, 0, (1,)): (-1, 1),  # lift of p_{1,2} on Psi_2
    (2, 2, 1, (1,)): (-1, 2),  # lift of p_{2,2}(Psi_1, .) on Psi_2
    (2, 1, 0, (1, 1)): (-1, 1),  # l2 on one strand each of two Psi_2
    (3, 1, 1, (1, 1)): (-1, 2),  # l3(Psi_1, ., .) on one strand each of two Psi_2
}
TABLE_E4 = {
    (1, 3, 0, (1,)): (-1, 2),  # lift of p_{1,3} on Psi_2
    (2, 2, 0, (1, 1)): (-1, 2),  # p_{2,2} on one strand each of two Psi_2
    (3, 1, 0, (1, 1, 1)): (-1, 2),  # l3 on one strand each of three Psi_2
}


def hb_out(t: dict) -> int:
    """hbar-power of an MC term in the output-counting form (Sigma_2 = hbar Psi_2, phi^-1)."""
    return (t["k"] - 1) - t["a"] - 2 * len(t["takes"]) + t["out"]


def by_order(pairs: list) -> bool:
    """Order-by-order homogeneity: (order, N_gh) pairs, None values skipped."""
    groups: dict = {}
    for o, n in pairs:
        if n is not None:
            groups.setdefault(o, set()).add(n)
    return all(len(v) == 1 for v in groups.values())


def key(t: dict) -> tuple:
    return (t["k"], t["l"], t["a"], t["takes"])


# ---------------------------------------------------------------- evaluation
class Data:
    """One seed: model, both families, fields."""

    def __init__(self, seed: int) -> None:
        self.rng = random.Random(seed)
        self.M = model(self.rng)
        self.fam = {
            kind: {
                (k, l): iblgen.raise_family(self.M, k, l, kind)
                for k in range(1, 4)
                for l in range(1, 4)
                if k + l <= 4
            }
            for kind in ("g", "O")
        }
        self.psi1 = rand_tensor(self.M, self.rng, 1, 2)
        self.lam1 = rand_tensor(self.M, self.rng, 1, 1)
        self.psi2 = {y: rand_tensor(self.M, self.rng, 2, y) for y in Y_SCAN}
        self.lam2 = {z: rand_tensor(self.M, self.rng, 2, z) for z in Z_SCAN}
        self.psi2_22 = rand_tensor(self.M, self.rng, 2, 4, strands=(2, 2))

    def factors(self, t: dict, psi2: dict, lam2: dict | None = None) -> list:
        f = [(self.psi1, 1)] * t["a"] + [(psi2, s) for s in t["takes"]]
        if "lam" in t:
            f = [(self.lam1, 1) if t["lam"] == "L1" else (lam2, t["tl"])] + f
        return f

    def term(self, t, psi2, lam2=None, kind="g", twist=False) -> dict:
        comp = self.fam[kind][(t["k"], t["l"])]
        return feed(self.M, comp, self.factors(t, psi2, lam2), twist)

    def ghost(self, t, psi2, lam2=None) -> int | None:
        """Measured N_gh of the term (None if it vanishes); asserts homogeneity."""
        T = self.term(t, psi2, lam2)
        s = support(self.M, T)
        if not s:
            return None
        if len(s) != 1:
            raise RuntimeError(f"inhomogeneous term {label(t)}: {s}")
        rank = {len(k) for k in T}
        if rank != {t["out"]}:
            raise RuntimeError(f"rank {rank} != {t['out']} for {label(t)}")
        return s.pop()


def homogeneous(vals: list) -> bool:
    return len(set(vals)) == 1


def cfl_degree(n_gh: int, out: int, hb: int, hbar_deg: int = 1) -> int:
    """CFL degree of hbar^hb X, X in E_out C: hb |hbar| + sum_strands (3 - N_gh)."""
    return hb * hbar_deg + 3 * out - n_gh


# ================================================================ Task 19b
# Components of the Maurer-Cartan equation with coefficients and signs, and H2.
# Output-counting form (record block R): m' = Psi + Psi_2, weight hbar^{l-1} g_s^{k+l-2}.
# Independent path: CFL's extension (2.1) applied literally in the symmetric algebra
# (Koszul signs of the letters, outputs to the left), e^{-m'} hat p_{k,l} e^{m'}.
KL = ((1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (1, 3))


def sym_norm(eps: list, w: tuple):
    """Sort a word of the graded-symmetric algebra; (word, Koszul sign) or (None, 0)."""
    w = list(w)
    s = 1
    for i in range(len(w)):
        for j in range(len(w) - 1 - i):
            if w[j] > w[j + 1]:
                if eps[w[j]] and eps[w[j + 1]]:
                    s = -s
                w[j], w[j + 1] = w[j + 1], w[j]
    t = tuple(w)
    if any(eps[a] and t.count(a) > 1 for a in set(t)):
        return None, 0
    return t, s


def s_add(A: dict, B: dict, c=1) -> dict:
    out = dict(A)
    for k, v in B.items():
        out[k] = out.get(k, 0) + c * v
    return {k: v for k, v in out.items() if v != 0}


def s_mul(eps: list, A: dict, B: dict, lmax: int = 4) -> dict:
    out: dict = {}
    for wa, xa in A.items():
        for wb, xb in B.items():
            if len(wa) + len(wb) > lmax:
                continue
            key, s = sym_norm(eps, wa + wb)
            if key is None:
                continue
            out[key] = out.get(key, 0) + s * xa * xb
    return {k: v for k, v in out.items() if v != 0}


def to_sym(eps: list, T: dict) -> dict:
    """pi: tensor components {(c_1..c_L): v} -> element of E_L C (A9)."""
    out: dict = {}
    for c, v in T.items():
        key, s = sym_norm(eps, c)
        if key is None:
            continue
        out[key] = out.get(key, 0) + s * v
    return {k: v for k, v in out.items() if v != 0}


def s_exp(eps: list, m: dict, rmax: int = 4) -> dict:
    res, term = {(): Fraction(1)}, {(): Fraction(1)}
    for r in range(1, rmax + 1):
        term = {k: v / r for k, v in s_mul(eps, term, m).items()}
        res = s_add(res, term)
    return res


def eps_out(M, l: int) -> list:
    """Parity used to normalize words of block (., l): physical for one output (the
    output letter and the leftover field letters), shifted N_gh + 1 for two outputs
    (the outputs of a raised product, raised with the inverse pairing of odd ghost
    number 5, are graded-symmetric in the shifted parity; record A9, check C8.1-par)."""
    return M.eps if l == 1 else [1 - e for e in M.eps]


def hat(eps: list, comp: dict, k: int, X: dict, eps_o: list | None = None) -> dict:
    """CFL (2.1): sum over k-subsets of letters, Koszul sign of moving them to the
    front (order kept; parity eps of the field letters), phi applied, outputs placed
    to the left of the rest; the output word is normalized with eps_o."""
    eps_o = eps if eps_o is None else eps_o
    byb: dict = {}
    for (b, c), v in comp.items():
        byb.setdefault(b, []).append((c, v))
    out: dict = {}
    for w, x in X.items():
        n = len(w)
        for S in itertools.combinations(range(n), k):
            sg = 1
            for p in S:
                cnt = sum(1 for q in range(p) if q not in S and eps[w[q]])
                if eps[w[p]] and cnt % 2:
                    sg = -sg
            b = tuple(w[p] for p in S)
            rest = tuple(w[q] for q in range(n) if q not in S)
            for c, v in byb.get(b, []):
                key, s = sym_norm(eps_o, c + rest)
                if key is None:
                    continue
                out[key] = out.get(key, 0) + sg * s * x * v
    return {k2: v for k2, v in out.items() if v != 0}


def mc_block(eps: list, comp: dict, k: int, m: dict, eps_o: list | None = None) -> dict:
    """e^{-m} hat p_k(e^m), split by word length {L: element}, L <= 2.

    For two-output blocks (eps_o shifted) the L <= 2 part is the pure output word,
    so normalizing the product with eps_o is consistent (no field letter in it)."""
    eps_o = eps if eps_o is None else eps_o
    Y = hat(eps, comp, k, s_exp(eps, m), eps_o)
    Z = s_mul(eps_o, s_exp(eps, {w: -x for w, x in m.items()}), Y)
    out = {L: {w: x for w, x in Z.items() if len(w) == L} for L in (0, 1, 2)}
    return out


def formula_block(D, k: int, l: int, L: int, psi, sig, t, u, coef=None) -> dict:
    """Record formula (MC.3)/(MC.5)-(MC.7), block (k, l), output length L, with
    m' = t Psi + u Sigma.  coef overrides a coefficient (break legs)."""
    M, fam = D.M, D.fam["g"][(k, l)]
    c = {
        "p(Psi^k)": Fraction(1, factorial(k)),
        "p(Psi_2)": Fraction(1),
        "p(Psi,Psi_2)": Fraction(1),
        "lift p(Psi,.)": Fraction(1),
        "lift p(Psi,Psi,.)": Fraction(1, 2),
        "lift p(Psi_2,.)": Fraction(1),
    }
    if coef:
        c.update(coef)
    terms = []  # (coefficient, t-power, u-power, factors)
    if L == l:
        terms.append((c["p(Psi^k)"], k, 0, [(psi, 1)] * k))
        if k == 2:
            terms.append((c["p(Psi_2)"], 0, 1, [(sig, 2)]))
        if k == 3:
            terms.append((c["p(Psi,Psi_2)"], 1, 1, [(psi, 1), (sig, 2)]))
    if L == l + 1:
        if k == 1:
            terms.append((Fraction(1), 0, 1, [(sig, 1)]))  # lift of p_{1,l}, derived
        if k == 2:
            terms.append((c["lift p(Psi,.)"], 1, 1, [(psi, 1), (sig, 1)]))
        if k == 3:
            terms.append((c["lift p(Psi,Psi,.)"], 2, 1, [(psi, 1), (psi, 1), (sig, 1)]))
            terms.append((c["lift p(Psi_2,.)"], 0, 2, [(sig, 2), (sig, 1)]))
    total: dict = {}
    for cc, a, b, fac in terms:
        total = s_add(total, to_sym(eps_out(M, l), feed(M, fam, fac)), cc * t**a * u**b)
    return total


def gauss_consistent(rows: list, rhs: list):
    """Exact consistency of A x = b; returns (consistent, one solution or None)."""
    n = len(rows[0]) if rows else 0
    A = [list(r) + [b] for r, b in zip(rows, rhs)]
    piv_cols, r = [], 0
    for col in range(n):
        p = next((i for i in range(r, len(A)) if A[i][col] != 0), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        pv = A[r][col]
        A[r] = [x / pv for x in A[r]]
        for i in range(len(A)):
            if i != r and A[i][col] != 0:
                f = A[i][col]
                A[i] = [x - f * y for x, y in zip(A[i], A[r])]
        piv_cols.append(col)
        r += 1
    if any(all(x == 0 for x in row[:n]) and row[n] != 0 for row in A):
        return False, None
    sol = [Fraction(0)] * n
    for i, col in enumerate(piv_cols):
        sol[col] = A[i][n]
    return True, sol


J = range(-2, 3)  # Laurent powers of g_s in alpha, beta, c_1, c_2


def h2_system(D, samples, use=("E1", "E6"), drop=()):
    """Linear system of reading (I): M_1(f) = c_1 E_Psi and M_2^(6)(f) = c_2 E_Sigma
    through O(g_s^2), f = alpha Sigma + beta Psi^2, alpha, beta, c_i Laurent in g_s.

    M_1, M_2^(6) are computed by the literal CFL path (mc_block); `drop` removes
    named terms (formula side, equal to the literal blocks by C8.1): 'a' = g_s
    l2(Psi_2), 'b' = g_s p12(Psi), 'c' = (1/2) g_s^2 p22(Psi^2).  Returns
    (consistent, one solution {name: value} or None).
    """
    M = D.M
    eps = M.eps
    fam = D.fam["g"]
    names = [f"{x}{j}" for x in ("al", "be", "c1", "c2") for j in J]
    rows, rhs = [], []
    for psi, sig in samples:
        P, S = to_sym(eps, psi), to_sym(eps, sig)
        P2 = s_mul(eps, P, P)  # pi(Psi x Psi)

        def op(k, l, fac, c=1):
            T = to_sym(eps_out(M, l), feed(M, fam[(k, l)], fac))
            return {w: c * x for w, x in T.items()}

        # paper eq:hs4:eom, by g_s-order
        eP = {
            0: op(1, 1, [(psi, 1)]),
            1: op(2, 1, [(psi, 1)] * 2, Fraction(1, 2)),
            2: op(3, 1, [(psi, 1), (sig, 2)], Fraction(1, 6)),
        }
        eS = {0: s_add(op(2, 2, [(psi, 1)] * 2), op(2, 2, [(sig, 2)]), -1)}
        for cname, l, eq_E in (("E1", 1, eP), ("E6", 2, eS)):
            if cname not in use:
                continue
            const: dict = {}
            lin: dict = {"al": {}, "be": {}}
            for k in (1, 2, 3):
                if k + l > 4:
                    continue
                o = k + l - 2
                eo = eps_out(M, l)
                base = mc_block(eps, fam[(k, l)], k, P, eo)[l]
                const[o] = s_add(const.get(o, {}), base)
                for nm, F in (("al", S), ("be", P2)):
                    li = s_add(
                        mc_block(eps, fam[(k, l)], k, s_add(P, F), eo)[l], base, -1
                    )
                    li2 = s_add(
                        mc_block(eps, fam[(k, l)], k, s_add(P, F, 2), eo)[l], base, -1
                    )
                    if li2 != {w: 2 * x for w, x in li.items()}:
                        raise RuntimeError("component not affine in Psi_2")
                    lin[nm][o] = s_add(lin[nm].get(o, {}), li)
            if cname == "E1" and "a" in drop:
                lin["al"][1] = s_add(lin["al"].get(1, {}), op(2, 1, [(sig, 2)]), -1)
                lin["be"][1] = s_add(lin["be"].get(1, {}), op(2, 1, [(psi, 1)] * 2), -1)
            if cname == "E6" and "b" in drop:
                const[1] = s_add(const.get(1, {}), op(1, 2, [(psi, 1)]), -1)
            if cname == "E6" and "c" in drop:
                const[2] = s_add(
                    const.get(2, {}), op(2, 2, [(psi, 1)] * 2), Fraction(-1, 2)
                )
            words = set()
            for dct in (const, lin["al"], lin["be"], eq_E):
                for v in dct.values():
                    words |= set(v)
            cn = "c1" if cname == "E1" else "c2"
            for n in range(-4, 3):
                for w in words:
                    co: dict = {}
                    for j in J:
                        for nm in ("al", "be"):
                            x = lin[nm].get(n - j, {}).get(w, 0)
                            if x:
                                co[f"{nm}{j}"] = co.get(f"{nm}{j}", 0) + x
                        x = eq_E.get(n - j, {}).get(w, 0)
                        if x:
                            co[f"{cn}{j}"] = co.get(f"{cn}{j}", 0) - x
                    b = -const.get(n, {}).get(w, 0)
                    if co or b:
                        rows.append([co.get(nm, 0) for nm in names])
                        rhs.append(b)
    ok, sol = gauss_consistent(rows, rhs)
    return ok, (dict(zip(names, sol)) if sol else None)


def variant(seed: int, kind: str):
    """Data with a modified vertex: 'kernel' (V_4 = 0 when e_2 occurs twice, so that
    N = e_2 x e_2 is in ker p_{2,2}) or 'free' (V_2(e_2, gh-2) = 0, so Q_B e_2 = 0)."""
    D = Data.__new__(Data)
    D.rng = random.Random(seed)
    D.M = model(D.rng)
    if kind == "kernel":
        D.M.V[4] = {i: v for i, v in D.M.V[4].items() if i.count(2) < 2}
    if kind == "free":
        D.M.V[2] = {
            i: v
            for i, v in D.M.V[2].items()
            if not (2 in i and all(D.M.gh[a] == 2 for a in i))
        }
    D.fam = {
        "g": {
            (k, l): iblgen.raise_family(D.M, k, l, "g")
            for k in range(1, 4)
            for l in range(1, 4)
            if k + l <= 4
        }
    }
    D.psi1 = rand_tensor(D.M, D.rng, 1, 2)
    D.psi2_22 = rand_tensor(D.M, D.rng, 2, 4, strands=(2, 2))
    return D


def run_19b() -> None:
    for seed in SEEDS:
        print(f"--- 19b, seed {seed}")
        D = Data(seed)
        M = D.M
        eps = M.eps
        rng = random.Random(seed + 7)
        psi, sig = D.psi1, D.psi2_22
        P, S = to_sym(eps, psi), to_sym(eps, sig)

        # C8.1: literal CFL path == formula (MC.3) block by block, two (t, u) points
        ok, nz = True, True
        need = {
            (1, 1): (1, 2),
            (2, 1): (1, 2),
            (3, 1): (1, 2),
            (1, 2): (2,),
            (2, 2): (2,),
        }
        for t, u in (
            (Fraction(3, 2), Fraction(-2, 5)),
            (Fraction(-5, 3), Fraction(7, 4)),
        ):
            m = s_add(
                {w: t * x for w, x in P.items()}, {w: u * x for w, x in S.items()}
            )
            for k, l in KL:
                B = mc_block(eps, D.fam["g"][(k, l)], k, m, eps_out(M, l))
                ok &= not B[0]
                for L in (1, 2):
                    ok &= B[L] == formula_block(D, k, l, L, psi, sig, t, u)
                nz &= all(bool(B[L]) for L in need.get((k, l), ()))
        # with Psi_2 = 0 the E_1 component is the original equation of motion (A9)
        eom = {}
        for k in (1, 2, 3):
            eom = s_add(
                eom,
                to_sym(eps, feed(M, D.fam["g"][(k, 1)], [(psi, 1)] * k)),
                Fraction(1, factorial(k)),
            )
        e1_0 = {}
        for k in (1, 2, 3):
            e1_0 = s_add(e1_0, mc_block(eps, D.fam["g"][(k, 1)], k, P)[1])
        check(
            f"C8.1 (seed {seed})",
            ok and nz and e1_0 == eom,
            "e^{-m'} hat p_{k,l} e^{m'} (CFL (2.1) literally, Koszul signs, outputs left) =="
            " (MC.3) for every (k, l), k + l <= 4, at L = 1, 2, two (t, u); blocks nonzero;"
            f" Psi_2 = 0 gives the original EOM: {e1_0 == eom}",
        )
        # break legs: the paper's 1/3! on l3(Psi, Psi_2), and 1/2 on the lift of l3(Psi_2, .)
        t, u = Fraction(3, 2), Fraction(-2, 5)
        m = s_add({w: t * x for w, x in P.items()}, {w: u * x for w, x in S.items()})
        B31 = mc_block(eps, D.fam["g"][(3, 1)], 3, m)
        br1 = B31[1] == formula_block(
            D, 3, 1, 1, psi, sig, t, u, {"p(Psi,Psi_2)": Fraction(1, 6)}
        )
        br2 = B31[2] == formula_block(
            D, 3, 1, 2, psi, sig, t, u, {"lift p(Psi_2,.)": Fraction(1, 2)}
        )
        B21 = mc_block(eps, D.fam["g"][(2, 1)], 2, m)
        br3 = B21[2] == formula_block(
            D, 2, 1, 2, psi, sig, t, u, {"lift p(Psi,.)": Fraction(-1)}
        )
        check(
            f"C8.1-break (seed {seed})",
            not br1 and not br2 and not br3,
            f"coefficient 1/3! on l3(Psi, Psi_2) reproduces the block: {br1}; 1/2 on the lift"
            f" of l3(Psi_2, .): {br2}; sign -1 on the lift of l2(Psi, .): {br3} (False expected)",
        )

        # C8.1-par: no single parity for E_2 C holds Sigma_2 and the raised outputs
        sh = eps_out(M, 2)
        T12 = feed(M, D.fam["g"][(1, 2)], [(psi, 1)])
        gsym_sh = all(
            T12.get((c2, c1), 0) == (-1) ** (sh[c1] * sh[c2]) * v
            for (c1, c2), v in T12.items()
        )
        gsym_ph = all(
            T12.get((c2, c1), 0) == (-1) ** (eps[c1] * eps[c2]) * v
            for (c1, c2), v in T12.items()
        )
        part33 = {c: v for c, v in T12.items() if M.gh[c[0]] == 3 and M.gh[c[1]] == 3}
        ph33 = {
            w: x for w, x in to_sym(eps, T12).items() if all(M.gh[a] == 3 for a in w)
        }
        sig_sh = to_sym(sh, sig)
        check(
            f"C8.1-par (seed {seed})",
            gsym_sh
            and not gsym_ph
            and bool(part33)
            and not ph33
            and bool(sig)
            and not sig_sh,
            f"p12(Psi) graded-symmetric in the shifted parity: {gsym_sh}, in the physical"
            f" parity: {gsym_ph}; its (3,3)-strand part nonzero: {bool(part33)}, killed by the"
            f" physical-parity quotient: {not ph33}; Sigma_2 killed by the shifted-parity"
            f" quotient: {not sig_sh}",
        )

        # C8.1-review: Task 17's display (2), CFL weight with m_{2,0} hbar-independent,
        # evaluated with hat and the connected part; conjugated hbar-power = l_p - 1
        def conn(k, comp, factors, eo):
            r = len(factors)
            tot: dict = {}
            for size in range(1, r + 1):
                for Ssub in itertools.combinations(range(r), size):
                    prod = {(): Fraction(1)}
                    for i in Ssub:
                        prod = s_mul(eps, prod, factors[i])
                    rest = {(): Fraction(1)}
                    for i in range(r):
                        if i not in Ssub:
                            rest = s_mul(eps, rest, factors[i])
                    # outputs normalized with eo; for l = 2 the L = 2 part has rest = 1
                    term = s_mul(eo, hat(eps, comp, k, prod, eo), rest)
                    tot = s_add(tot, term, (-1) ** (r - size))
            return tot

        # (k, l, coefficient, factor list as 'm1'/'m2', CFL hbar-power c - 1, output L)
        review = [
            (1, 1, Fraction(1), ["m1"], -1, 1),
            (2, 1, Fraction(1, 2), ["m1", "m1"], -1, 1),
            (3, 1, Fraction(1, 6), ["m1"] * 3, -1, 1),
            (2, 1, Fraction(1), ["m2"], 0, 1),
            (3, 1, Fraction(1), ["m1", "m2"], 0, 1),
            (1, 2, Fraction(1), ["m1"], -1, 2),
            (2, 2, Fraction(1, 2), ["m1", "m1"], -1, 2),
            (1, 1, Fraction(1), ["m2"], -1, 2),
            (2, 1, Fraction(1), ["m1", "m2"], -1, 2),
            (3, 1, Fraction(1, 2), ["m1", "m1", "m2"], -1, 2),
            (2, 2, Fraction(1), ["m2"], 0, 2),
            (3, 1, Fraction(1, 2), ["m2", "m2"], 0, 2),
        ]
        ok_r, ok_h = True, True
        acc: dict = {}
        for k, l, cf, fl, hb, L in review:
            eo = eps_out(M, l)
            fac = [P if f == "m1" else S for f in fl]
            val = {
                w: x
                for w, x in conn(k, D.fam["g"][(k, l)], fac, eo).items()
                if len(w) == L
            }
            key2 = (k, l, L)
            acc[key2] = s_add(acc.get(key2, {}), val, cf)
            # conjugation: m_{2,0} = hbar^{-1} Sigma_2, then phi^{-1}: hbar^{+L} on E_L
            hb_oc = hb - fl.count("m2") + L
            ok_h &= hb_oc == l - 1
        for (k, l, L), val in acc.items():
            ok_r &= (
                bool(val)
                and val
                == mc_block(eps, D.fam["g"][(k, l)], k, s_add(P, S), eps_out(M, l))[L]
            )
        check(
            f"C8.1-review (seed {seed})",
            ok_r and ok_h,
            "Task 17 review (2), its coefficients evaluated with hat and the connected part,"
            f" equals the literal blocks: {ok_r}; after m_(2,0) = hbar^-1 Sigma_2 and phi^-1"
            f" every term sits at hbar^(l_p - 1): {ok_h}",
        )

        # C8.2: reading (I) of H2, Laurent alpha, beta, c_1, c_2; three samples
        samples = [(psi, sig)] + [
            (rand_tensor(M, rng, 1, 2), rand_tensor(M, rng, 2, 4, strands=(2, 2)))
            for _ in range(3)
        ]
        r1, _ = h2_system(D, samples, use=("E1",))
        r6, _ = h2_system(D, samples, use=("E6",))
        rj, _ = h2_system(D, samples)
        check(
            f"C8.2 (seed {seed})",
            not r1 and not r6 and not rj,
            f"M_1 = c_1 E_Psi solvable: {r1}; M_2^(6) = c_2 E_Sigma solvable: {r6}; jointly: {rj}"
            " (all False: H2 refuted in reading (I))",
        )
        a1, s1 = h2_system(D, samples, use=("E1",), drop=("a",))
        b6, _ = h2_system(D, samples, use=("E6",), drop=("b",))
        ab, _ = h2_system(D, samples, drop=("a", "b"))
        abc, s3 = h2_system(D, samples, drop=("a", "b", "c"))
        sol_ok = (
            bool(s3) and s3["al0"] == Fraction(1, 6) and s3["be0"] == Fraction(-1, 6)
        )
        check(
            f"C8.2-break (seed {seed})",
            a1 and b6 and not ab and abc and sol_ok,
            f"drop M-a: E_1 solvable {a1}; drop M-b: E_6 solvable {b6}; drop M-a, M-b:"
            f" joint solvable {ab} (False: M-c); drop M-a, M-b, M-c: joint solvable {abc},"
            f" alpha_0 = {s3['al0'] if s3 else None}, beta_0 = {s3['be0'] if s3 else None}",
        )

        # C8.2-quot: kernel model, N = e_2 x e_2 in ker p_{2,2}
        K = variant(seed, "kernel")
        KM = K.M
        N = {(2, 2): Fraction(1)}
        sK = K.psi2_22
        sKN = {k2: v for k2, v in sK.items()}
        sKN[(2, 2)] = sKN.get((2, 2), 0) + 1
        p22N = feed(KM, K.fam["g"][(2, 2)], [(N, 2)])
        p22S = feed(KM, K.fam["g"][(2, 2)], [(sK, 2)])
        l3a = feed(KM, K.fam["g"][(3, 1)], [(K.psi1, 1), (sK, 2)])
        l3b = feed(KM, K.fam["g"][(3, 1)], [(K.psi1, 1), (sKN, 2)])
        e_inv = not p22N and bool(p22S) and l3a == l3b and bool(l3a)
        al = Fraction(1, 6)
        fK = {k2: al * v for k2, v in sK.items()}
        fKN = {k2: al * v for k2, v in sKN.items()}
        PK = to_sym(KM.eps, K.psi1)
        ch1, ch5 = False, False
        for k in (1, 2, 3):
            comp = K.fam["g"][(k, 1)]
            bA = mc_block(KM.eps, comp, k, s_add(PK, to_sym(KM.eps, fK)))
            bB = mc_block(KM.eps, comp, k, s_add(PK, to_sym(KM.eps, fKN)))
            ch1 |= bA[1] != bB[1]
            ch5 |= bA[2] != bB[2]
        l2N = feed(KM, K.fam["g"][(2, 1)], [(N, 2)])
        qN = feed(KM, K.fam["g"][(1, 1)], [(N, 1)])
        check(
            f"C8.2-quot (seed {seed})",
            e_inv and ch1 and ch5 and bool(l2N) and bool(qN),
            f"p22(N) = 0, E_Psi and E_Sigma invariant under Sigma -> Sigma + N: {e_inv};"
            f" with f = Sigma/6 the MC terms change (M_1: {ch1}, M_2^(5): {ch5});"
            f" l2(N) != 0: {bool(l2N)}, hat Q N != 0 (lift of p_(1,1), derived): {bool(qN)}",
        )

        # C8.2-shell: free model, Q_B e_2 = 0; Psi = eps e_2, Sigma = Psi^2 solves the EOM
        # at O(eps); the O(eps) part of M_2^(6) is g_s p12(e_2), f-independent
        F = variant(seed, "free")
        FM = F.M
        e2 = {(2,): Fraction(1)}
        qe2 = feed(FM, F.fam["g"][(1, 1)], [(e2, 1)])
        p12 = feed(FM, F.fam["g"][(1, 2)], [(e2, 1)])
        # literal: O(eps) part of the (1,2) block at m' = eps e_2 + f, f = O(eps^2)
        lit = mc_block(
            FM.eps, F.fam["g"][(1, 2)], 1, to_sym(FM.eps, e2), eps_out(FM, 2)
        )[2]
        check(
            f"C8.2-shell (seed {seed})",
            not qe2 and bool(p12) and lit == to_sym(eps_out(FM, 2), p12),
            f"Q_B e_2 = 0: {not qe2}; p12(e_2) != 0: {bool(p12)} (the cubic vertex"
            " V_3(., ., e_2)); the O(eps) part of M_2^(6) is g_s p12(e_2) for every f of A10",
        )

        # C8.2-action (H2.6): M_1, M_2^(6) are the gradients of
        # S_MC = sum_n g_s^{n-2} V_n((e^{Psi + Psi_2})_n) - V_2(Psi_2), order by order
        def vn_sym(n, X):
            Vn = M.V.get(n, {})
            return sum(
                (x * Vn.get(w, 0) for w, x in X.items() if len(w) == n), Fraction(0)
            )

        def s_mc(n, Pp, Ss):
            E = s_exp(eps, s_add(Pp, Ss))
            return vn_sym(n, E) - (vn_sym(2, Ss) if n == 2 else 0)

        def deriv(fun):
            # exact first derivative at 0 of a polynomial of degree <= 4
            return (fun(-2) - 8 * fun(-1) + 8 * fun(1) - fun(2)) / 12

        ok_a = True
        for n in (2, 3, 4):
            k = n - 1
            blk1 = mc_block(eps, D.fam["g"][(k, 1)], k, s_add(P, S))[1]
            for x in range(M.N):
                if M.gh[x] != 2:
                    continue
                lhs = deriv(lambda tt: s_mc(n, s_add(P, {(x,): Fraction(1)}, tt), S))
                rhs = sum(M.g.get((x, w[0]), 0) * val for w, val in blk1.items())
                ok_a &= lhs == rhs
            if n >= 3:
                k = n - 2
                blk6 = formula_block(D, k, 2, 2, psi, sig, Fraction(1), Fraction(1))
                T6 = feed(M, D.fam["g"][(k, 2)], [(psi, 1)] * k)
                T6 = {kk: v / factorial(k) for kk, v in T6.items()}
                if k == 2:
                    T6 = s_add(T6, feed(M, D.fam["g"][(2, 2)], [(sig, 2)]))
                ok_a &= to_sym(eps_out(M, 2), T6) == blk6 and bool(blk6)
                for a_, b_ in ((2, 2), (2, 3), (3, 3)):
                    AB = (
                        to_sym(eps, {(a_, b_): Fraction(1), (b_, a_): Fraction(1)})
                        if a_ != b_
                        else {(a_, a_): Fraction(1)}
                    )
                    lhs = deriv(lambda tt: s_mc(n, P, s_add(S, AB, tt)))
                    # <A x B, T>_2 symmetrized as AB = pi(A x B + B x A)/(1 or 2) ...
                    tens = (
                        {(a_, b_): Fraction(1), (b_, a_): Fraction(1)}
                        if a_ != b_
                        else {(a_, a_): Fraction(1)}
                    )
                    rhs = sum(
                        tv
                        * T6.get((c1, c2), 0)
                        * M.g.get((p, c1), 0)
                        * M.g.get((q, c2), 0)
                        for (p, q), tv in tens.items()
                        for c1 in range(M.N)
                        for c2 in range(M.N)
                    )
                    ok_a &= lhs == rhs
        check(
            f"C8.2-action (seed {seed})",
            ok_a,
            "(H2.6): delta_Psi S_MC = <., M_1> and delta_Psi_2 S_MC = <., M_2^(6)>_2 at"
            " every order g_s^0..g_s^2 (S_MC from the vertices on e^{Psi + Psi_2};"
            " independent content: the exponential's combinatorics)",
        )


def main() -> int:
    mc = enum_mc()
    e1 = [t for t in mc if t["out"] == 1]
    e2 = [t for t in mc if t["out"] == 2]
    gauge = enum_gauge()
    g1 = [t for t in gauge if t["out"] == 1]
    g2 = [t for t in gauge if t["out"] == 2]

    # C2-C3: enumeration against the record's table (seed-independent)
    got1 = {key(t): (t["hbar"], t["tau"]) for t in e1}
    got2 = {key(t): (t["hbar"], t["tau"]) for t in e2}
    check(
        "C2-C3",
        got1 == TABLE_E1 and got2 == TABLE_E2,
        f"E_1: {len(got1)} terms, E_2: {len(got2)} terms, operations and hbar-, "
        "g_s-powers equal the record's table",
    )
    # break: a perturbed hbar rule (k-1) - a - 2b in place of (k-1) - (a+b)
    bad1 = {key(t): ((t["k"] - 1) - t["a"] - 2 * len(t["takes"]), t["tau"]) for t in e1}
    bad2 = {key(t): ((t["k"] - 1) - t["a"] - 2 * len(t["takes"]), t["tau"]) for t in e2}
    check(
        "C2-C3-break",
        bad1 != TABLE_E1 and bad2 != TABLE_E2,
        "perturbed hbar rule (k-1) - a - 2b disagrees with the table in E_1 and E_2"
        " (expected)",
    )
    e3 = [t for t in mc if t["out"] == 3]
    e4 = [t for t in mc if t["out"] == 4]
    got3 = {key(t): (t["hbar"], t["tau"]) for t in e3}
    got4 = {key(t): (t["hbar"], t["tau"]) for t in e4}
    no_more = all(t["out"] <= 4 for t in mc)
    rule_out = all(hb_out(t) == t["l"] - 1 for t in e3 + e4)
    drop13 = {k: v for k, v in TABLE_E3.items() if k != (1, 3, 1, ())}
    print(
        "  E_3:", "; ".join(f"{label(t)} hbar^{t['hbar']} g_s^{t['tau']}" for t in e3)
    )
    print(
        "  E_4:", "; ".join(f"{label(t)} hbar^{t['hbar']} g_s^{t['tau']}" for t in e4)
    )
    print(
        "  E_1:", "; ".join(f"{label(t)} hbar^{t['hbar']} g_s^{t['tau']}" for t in e1)
    )
    print(
        "  E_2:", "; ".join(f"{label(t)} hbar^{t['hbar']} g_s^{t['tau']}" for t in e2)
    )

    for seed in SEEDS:
        print(f"--- seed {seed}")
        D = Data(seed)
        M = D.M

        # C1: measured shifts of every p_{k,l}, both families
        ok, rows = True, []
        for (k, l), comp in D.fam["g"].items():
            for kind in ("g", "O"):
                T = feed(M, D.fam[kind][(k, l)], [(D.psi1, 1)] * k)
                s = support(M, T)
                shift = (s.pop() - 2 * k) if len(s) == 1 else None
                ok &= shift == 3 * l - 2 * k
                cfl = 3 * l - 3 * k - (3 * l - 2 * k)  # strand dictionary
                ok &= cfl == -2 * Fraction(1, 2) * (k - 1) - 1
            rows.append(f"p{k}{l}:{shift}")
        check(f"C1 (seed {seed})", ok, "measured shifts " + ", ".join(rows))

        # measured ghost numbers of the MC terms for each N_gh(Psi_2)
        gh = {}
        for y in Y_SCAN:
            gh[y] = {key(t): D.ghost(t, D.psi2[y]) for t in mc if t["out"] in (1, 2)}
        vanish = [(y, k) for y in gh for k, v in gh[y].items() if v is None]
        if vanish:
            print("  vanishing terms (excluded from that y):", vanish)

        def hom(y, terms, x=None, hbar_deg=None, drop=()):
            vals = []
            for t in terms:
                if key(t) in drop or gh[y][key(t)] is None:
                    continue
                n = gh[y][key(t)]
                if hbar_deg is not None:
                    vals.append(cfl_degree(n, t["out"], t["hbar"], hbar_deg))
                else:
                    vals.append(n + t["hbar"] * x)
            return homogeneous(vals)

        # NV: no MC term vanishes at y = 4, 5 and no gauge term at (4, 3), (5, 4),
        # so the homogeneity sets of C4, C5, C6 are taken over every term
        nv = all(gh[y][key(t)] is not None for y in (4, 5) for t in mc if t["out"] < 3)
        nv &= all(
            D.ghost(t, D.psi2[y], D.lam2[z]) is not None
            for (y, z) in ((4, 3), (5, 4))
            for t in gauge
            if t["out"] in (1, 2)
        )
        check(
            f"NV (seed {seed})",
            nv,
            "every E_1, E_2 term nonzero at N_gh(Psi_2) = 4, 5 and every gauge term at"
            " (y, z) = (4, 3), (5, 4)",
        )

        # C5-ord: order-by-order homogeneity (A12), x-independent by construction
        ord_cfl = {
            y
            for y in Y_SCAN
            if by_order([(t["hbar"], gh[y][key(t)]) for t in e1])
            and by_order([(t["hbar"], gh[y][key(t)]) for t in e2])
        }
        ord_out = {
            y
            for y in Y_SCAN
            if by_order([(hb_out(t), gh[y][key(t)]) for t in e1])
            and by_order([(hb_out(t), gh[y][key(t)]) for t in e2])
        }

        def lam_ord(y, z, hb):
            return all(
                by_order(
                    [
                        (hb(t), D.ghost(t, D.psi2[y], D.lam2[z]))
                        for t in gauge
                        if t["out"] == o
                    ]
                )
                for o in (1, 2)
            )

        def hb_lam_out(t):
            w = 1 if t["lam"] == "L1" else 2
            return (t["k"] - 1) - w - t["a"] - 2 * len(t["takes"]) + t["out"]

        z_ord_cfl = {z for z in Z_SCAN if lam_ord(5, z, lambda t: t["hbar"])}
        z_ord_out = {z for z in Z_SCAN if lam_ord(4, z, hb_lam_out)}
        # break: merging the orders (x = 0, whole component) loses both values
        merged = {
            y
            for y in Y_SCAN
            if by_order([(0, gh[y][key(t)]) for t in e1])
            and by_order([(0, gh[y][key(t)]) for t in e2])
        }
        check(
            f"C5-ord (seed {seed})",
            ord_cfl == {5}
            and ord_out == {4}
            and z_ord_cfl == {4}
            and z_ord_out == {3}
            and not merged,
            f"order by order: CFL weight N_gh(Psi_2) {ord_cfl}, output weight "
            f"N_gh(Sigma_2) {ord_out}; Lambda_2: CFL {z_ord_cfl}, output {z_ord_out};"
            f" orders merged at x = 0: {merged} (empty expected)",
        )

        # C5-ord-n (final fix pass, critic 21a2 #2): dressing hbar^{-1-n} of the
        # two-string component.  Expected, derived by hand in (H.2''), (H.3'):
        # order by order {5} for n = 0, {4} for n = 1, every scanned value otherwise;
        # whole component over x: only (x, y) = (-1, 5 - n).
        def hb_n(t, n):
            return (t["k"] - 1) - t["a"] - (1 + n) * len(t["takes"])

        def ord_n(n, rule=hb_n):
            return {
                y
                for y in Y_SCAN
                if by_order([(rule(t, n), gh[y][key(t)]) for t in e1])
                and by_order([(rule(t, n), gh[y][key(t)]) for t in e2])
            }

        def whole_n(n):
            return {
                (x, y)
                for x in range(-3, 4)
                for y in Y_SCAN
                if all(
                    by_order([(0, gh[y][key(t)] + hb_n(t, n) * x) for t in comp])
                    for comp in (e1, e2)
                )
            }

        exp_ord = {0: {5}, 1: {4}}
        ok_n = all(
            ord_n(n) == exp_ord.get(n, set(Y_SCAN)) for n in range(-2, 4)
        ) and all(
            whole_n(n) == ({(-1, 5 - n)} if 5 - n in Y_SCAN else set())
            for n in range(-2, 4)
        )
        # break: the rule without the 1 in (1 + n) (dressing hbar^{-n}) must miss
        brk_n = ord_n(1, rule=lambda t, n: (t["k"] - 1) - t["a"] - n * len(t["takes"]))
        check(
            f"C5-ord-n (seed {seed})",
            ok_n,
            "order-by-order set {5} (n = 0), {4} (n = 1), full scan for n in"
            " {-2, -1, 2, 3}; whole component (-1, 5 - n) for every n",
        )
        check(
            f"C5-ord-n-break (seed {seed})",
            brk_n != exp_ord[1],
            f"perturbed dressing rule at n = 1 gives {brk_n}, not {{4}} (FAIL as expected)",
        )

        # C2-C3-E34: E_3, E_4 terms, measured N_gh = 2L + l_p at N_gh(Psi_2) = 4
        g34 = {key(t): D.ghost(t, D.psi2[4]) for t in e3 + e4}
        rule34 = all(g34[key(t)] == 2 * t["out"] + t["l"] for t in e3 + e4)
        check(
            f"C2-C3-E34 (seed {seed})",
            got3 == TABLE_E3
            and got4 == TABLE_E4
            and no_more
            and rule_out
            and rule34
            and got3 != drop13,
            f"E_3: {len(got3)} terms, E_4: {len(got4)} terms equal (MC.8)-(MC.9); no"
            f" E_L with L > 4: {no_more}; output-counting order l_p - 1: {rule_out};"
            f" measured N_gh = 2L + l_p (nonzero): {rule34}; table without p13(Psi)"
            " detected",
        )

        # C4: CFL degree
        cfl_set = {
            y for y in Y_SCAN if hom(y, e1, hbar_deg=1) and hom(y, e2, hbar_deg=1)
        }
        check(
            f"C4 (seed {seed})", cfl_set == {5}, f"homogeneous N_gh(Psi_2): {cfl_set}"
        )
        brk = {
            hd: {
                y for y in Y_SCAN if hom(y, e1, hbar_deg=hd) and hom(y, e2, hbar_deg=hd)
            }
            for hd in (0, 2)
        }
        check(
            f"C4-break (seed {seed})",
            all(not v for v in brk.values()),
            f"|hbar| = 0: {brk[0]}, |hbar| = 2: {brk[2]} (empty expected)",
        )

        # C5: physical ghost number, x = N_gh(hbar)
        s1 = {y for y in Y_SCAN if hom(y, e1, x=0)}
        s2 = {y for y in Y_SCAN if hom(y, e2, x=0)}
        pairs = {
            (x, y)
            for x in X_SCAN
            for y in Y_SCAN
            if hom(y, e1, x=x) and hom(y, e2, x=x)
        }
        equiv = all(
            (hom(y, e1, hbar_deg=1) and hom(y, e2, hbar_deg=1))
            == (hom(y, e1, x=-1) and hom(y, e2, x=-1))
            for y in Y_SCAN
        )
        check(
            f"C5 (seed {seed})",
            s1 == {4} and not s2 and pairs == {(-1, 5)} and equiv,
            f"E_1 alone {s1}, E_2 alone {s2}, both {s1 & s2}; (x, y) pairs {pairs}; "
            f"CFL == (x = -1): {equiv}",
        )
        print(
            "  N_gh at y = 4:",
            "; ".join(f"{label(t)}: {gh[4][key(t)]}" for t in e1 + e2),
        )
        print(
            "  N_gh at y = 5:",
            "; ".join(f"{label(t)}: {gh[5][key(t)]}" for t in e1 + e2),
        )

        # C5.3: at y = 4 the ghost-5 sector is exactly the lifts
        sect = {}
        for t in e2:
            sect.setdefault(gh[4][key(t)], set()).add(key(t))
        rule = all(gh[4][key(t)] == 2 * t["out"] + t["l"] for t in e1 + e2)
        check(
            f"C5.3 (seed {seed})",
            rule
            and sect == {5: LIFTS_E2, 6: set(TABLE_E2) - LIFTS_E2}
            and hom(4, e2, x=0, drop=LIFTS_E2),
            f"N_gh = 2L + l_p for every term at N_gh(Psi_2) = 4: {rule}; E_2: ghost 5 ="
            " the four lifts, ghost 6 = p_{1,2}(Psi_1), p_{2,2}(Psi_1^2), p_{2,2}(Psi_2);"
            " homogeneous once the lifts are removed",
        )

        # C7.1: weight hbar^{-n} on the n-string components (Sigma_2 = hbar Psi_2),
        # Sigma_2 at N_gh 4, Lambda_2 at 3: CFL-homogeneous, hbar-power = -L + l_p - 1
        def hb_re(t):
            w_lam = 0 if "lam" not in t else (1 if t["lam"] == "L1" else 2)
            p = (t["k"] - 1) - w_lam - t["a"] - 2 * len(t["takes"])
            return p + (t["out"] if "lam" in t else 0)

        ok71 = True
        for comp_terms in (e1, e2):
            vals = [cfl_degree(gh[4][key(t)], t["out"], hb_re(t)) for t in comp_terms]
            ok71 &= homogeneous(vals)
            ok71 &= all(hb_re(t) == -t["out"] + t["l"] - 1 for t in comp_terms)
        for out in (1, 2):
            terms = [t for t in gauge if t["out"] == out]
            vals = [
                cfl_degree(D.ghost(t, D.psi2[4], D.lam2[3]), out, hb_re(t) - out)
                for t in terms
            ]
            ok71 &= homogeneous(vals)
        # break leg: CFL's uniform weight hbar^{-1} with Sigma_2 at 4 is not homogeneous
        brk71 = homogeneous([cfl_degree(gh[4][key(t)], 2, t["hbar"]) for t in e2])
        check(
            f"C7.1 (seed {seed})",
            ok71 and not brk71,
            "m = hbar^-1 Psi_1 + hbar^-2 Sigma_2, lambda = hbar^-1 L1 + hbar^-2 L2 at"
            " N_gh (2, 4; 1, 3): E_1, E_2, delta Psi_1, delta Psi_2 CFL-homogeneous,"
            f" hbar-power = -L + l_p - 1: {ok71}; uniform hbar^-1 weight at N_gh 4"
            f" homogeneous: {brk71} (False expected)",
        )

        # C6: Lambda grading
        def ghl(y, z):
            return {
                (t["lam"], t["tl"], key(t), t["out"]): (
                    D.ghost(t, D.psi2[y], D.lam2[z]),
                    t["hbar"],
                    t["out"],
                )
                for t in gauge
                if t["out"] in (1, 2)
            }

        def homl(y, z, out, x=None, hbar_deg=None):
            vals = []
            for (_, _, _, o), (n, hb, oo) in ghl(y, z).items():
                if o != out or n is None:
                    continue
                vals.append(
                    cfl_degree(n, oo, hb, hbar_deg)
                    if hbar_deg is not None
                    else n + hb * x
                )
            return homogeneous(vals)

        z_cfl = {
            z for z in Z_SCAN if homl(5, z, 1, hbar_deg=1) and homl(5, z, 2, hbar_deg=1)
        }
        z1 = {z for z in Z_SCAN if homl(4, z, 1, x=0)}
        z2 = {z for z in Z_SCAN if homl(4, z, 2, x=0)}
        check(
            f"C6 (seed {seed})",
            z_cfl == {4} and z1 == {3} and not z2,
            f"CFL (N_gh(Psi_2) = 5): N_gh(Lambda_2) {z_cfl}; physical (N_gh(Psi_2) = 4): "
            f"delta Psi_1 alone {z1}, delta Psi_2 alone {z2}",
        )
        if seed == SEEDS[0]:
            for z, y in ((3, 4), (4, 5)):
                print(f"  gauge terms, N_gh(Lambda_2) = {z}, N_gh(Psi_2) = {y}:")
                for t in g1 + g2:
                    n = D.ghost(t, D.psi2[y], D.lam2[z])
                    print(
                        f"    dPsi_{t['out']}: {label(t)} hbar^{t['hbar']} g_s^{t['tau']}"
                        f" N_gh {n}"
                    )

        # TW: R87 twist
        ok_tw = True
        for t in mc:
            if t["out"] not in (1, 2):
                continue
            for y in (4, 5):
                A = D.term(t, D.psi2[y], kind="O")
                B = D.term(t, D.psi2[y], kind="g", twist=True)
                ok_tw &= A == B
        for t in gauge:
            if t["out"] not in (1, 2):
                continue
            A = D.term(t, D.psi2[4], D.lam2[3], kind="O")
            B = D.term(t, D.psi2[4], D.lam2[3], kind="g", twist=True)
            ok_tw &= A == B
        plus22 = all(
            D.term(t, D.psi2_22, kind="O") == D.term(t, D.psi2_22, kind="g")
            for t in mc
            if t["out"] in (1, 2)
        )
        minus5 = all(
            D.term(t, D.psi2[5], kind="O")
            == {k: -v for k, v in D.term(t, D.psi2[5], kind="g").items()}
            for t in e1
            if t["takes"]
        )
        check(
            f"TW (seed {seed})",
            ok_tw and plus22 and minus5,
            f"p^Omega = (-1)^|B| p componentwise: {ok_tw}; (2,2)-strand Psi_2, twist +1 on "
            f"every MC term: {plus22}; N_gh(Psi_2) = 5, E_1 Psi_2-terms flip: {minus5}",
        )

    run_19b()

    n_fail = sum(1 for _, ok in RESULTS if not ok)
    print(f"SUMMARY: {len(RESULTS) - n_fail}/{len(RESULTS)} PASS (seeds {SEEDS})")
    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(main())
