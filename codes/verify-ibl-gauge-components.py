"""Record 111, step 1: term list of the IBL gauge transformation delta m' = e^{-m'} [hat p', lambda'] e^{m'}.

Record: agent/derivations/111-ibl-gauge-components.md (claim-tree nodes in brackets).

Setting (record 111 A1-A4; record 103 block R, output-counting form).  m' = Psi + Sigma_2,
lambda' = Lambda_1 + Lambda_2, hat p' = sum_{k,l>=1, k+l<=4} hat p_{k,l} hbar^{l-1} g_s^{k+l-2},
genus zero.  hat phi is CFL's order-k differential operator (2.1): its k inputs are strands
of the factors of lambda' e^{m'}, at least one from lambda' (the graded commutator keeps
exactly those subsets), each factor of e^{m'} feeding >= 1 strand (connectedness); the
unfed strands stay as outputs.

Checks (each named after the node it tests):
  C1.1        the connected terms (operation, hbar-order l-1, g_s-order k+l-2, output length
              L, ghost number) enumerated here agree with record 103's enum_gauge (CFL
              weight, lambda = hbar^{-1}(L1+L2)) on E_1, E_2 after the dressing shift
              hbar^{(k-1)-1-j+1} -> hbar^{l-1}, and the ghost rule 2L + l_p - 1 holds on
              every term (E_1..E_4).  -break: a perturbed hbar rule l-2 disagrees.
  C1.2-count  the multiplicities: the number of distinct connected configurations equals
              the row count of the record's table (block T), per output length.
  C1.4        the raised two-output tensor p_{1,2}(Lambda_1) (ghost 5, strands (2,3) mixed)
              is graded antisymmetric in the physical parity, so the engine's plain
              projection to_sym(eps_out) annihilates it; the decalage re-signing
              T'^{c1 c2} = (-1)^{eps(c1)} T^{c1 c2} is graded symmetric in the shifted parity
              and survives (-break).  Step 2 must fix this identification before the
              ghost-5 sector of delta Sigma_2 can be computed.
  C2.3        limiting case: with Sigma_2 = Lambda_2 = 0 the E_1 part of e^{-m'} [hat p', L1]
              e^{m'}, computed literally in the graded-symmetric algebra (engine of record
              103: hat, s_exp, s_mul with the physical parity, Lambda_1 odd), equals
              Q Lambda_1 + sum_{n=2,3} g_s^{n-1}/(n-1)! l_n(Psi^{n-1}, Lambda_1) built with
              feed, the book's closed-SFT gauge law; and the E_2 part equals
              hbar [g_s p_{1,2}(Lambda_1) + g_s^2 p_{2,2}(Psi, Lambda_1)] on raw tensors
              (before any projection, C1.4).  -break: the
              coefficient 1/2 of l_3 replaced by 1 is detected; the sign of l_2 flipped
              is detected.

Step 2 (record block M, nodes C3.x; cyclic dgla model sl2 x Lambda[theta_1..3], d =
theta_2 theta_3 d/dtheta_1, pairing tr x int d^3theta, ghost = form degree + 1, dim 24;
limitation: Q = 0 on ghost 1, so Q Lambda_1 = 0 and the (2,2) part of hat Q Lambda_2
vanishes on this model, see dgla_model):
  C3.0        the model: Q = raise_family(1,1) is d, Q^2 = 0, V_2, V_3 graded symmetric in
              the ghost parity, V_3 != 0, the derivation relation Q l2(a,b) + l2(Qa,b)
              + (-1)^{eps a} l2(a,Qb) = 0 as a tensor identity (physical parity).
  C3.1        operator form on words with odd letters (physical parity on every letter,
              one-output letters included): Q^2 = 0 and Q l2 + l2 Q = 0 on random words
              of length <= 3 holding Lambda_1, Lambda_2 letters; -break: the relation
              with the opposite relative sign fails.
  C1.3-low    leg 1 of block F at hbar^0 through O(g_s): rows 1, 2, 3, 7, 8, 9, 17 with
              the signed feed (Koszul rule A2) equal the literal E_1, E_2, E_3 parts of
              e^{-m'} [hat p', lambda'] e^{m'}; -break: the sign of row 7 flipped, the
              sign of row 3 flipped.
  C3.2        leg 2 of block F at hbar^0 through O(g_s), E_1 and E_2: delta_T E
              - [hat p', lambda'] E + lambda' hat p' E = 0 with E = hat p'(e^{m'}) and
              delta_T from the table; -break: row 7 flipped fails at O(g_s) on E_1
              (through Q l2(Lambda_2) + l2(hat Q Lambda_2) = 0), row 3 flipped fails.
  C3.3        the (1,1)-(1,2) relation on a raw two-output tensor, hat Q p12(X)
              + p12(Q X) = 0, tested on X = Psi (Q Lambda_1 = 0 on this model), with the
              Leibniz sign of hat Q in the physical parity of the first output letter;
              the shifted-parity Leibniz sign and the opposite relative sign fail
              (-break).  The ghost-6 part of the covariance of delta Sigma_2 at
              O(hbar g_s) is this relation on X = Lambda_1 (not probed here).

NOT verified (step 2, this script): O(g_s^2) rows (l_3, p_{2,2}: the model has V_4 = 0),
the E_3, E_4 parts of the covariance identity, any composition feeding a two-output
letter (rule V of PH42).  Engine helpers are imported from
codes/verify-ibl-mc-conventions.py (never edited); the signed feed and the dgla model are
new functions of this script.
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
    "iblmc", ROOT / "verify-ibl-mc-conventions.py"
)
iblmc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(iblmc)

SEEDS = (20261022, 20261023)
RESULTS: list[tuple[str, bool]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    RESULTS.append((name, bool(ok)))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}")


# ---------------------------------------------------------------- enumeration
def enum_gauge_out(kl_max: int = 4) -> list[dict]:
    """Connected terms of e^{-m'} [hat p', lambda'] e^{m'}, output-counting weight.

    Fields: k, l, lam (L1/L2), tl strands of lambda fed, a copies of Psi, takes = strands
    fed from each Sigma_2 copy; out = output length L; hbar = l - 1; gs = k + l - 2;
    coef = 1/(a! b1! b2!) with b1 (b2) the number of singly (doubly) fed Sigma_2;
    ngh = ghost number at (Psi, Sigma_2; L1, L2) = (2, 4; 1, 3) with N_gh(hbar) = -1
    counted on the tensor (hbar excluded): sum N_gh(factors) + 3l - 2k.
    """
    gh = {"L1": 1, "L2": 3}
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
                                b1, b2 = takes.count(1), takes.count(2)
                                out.append(
                                    dict(
                                        k=k,
                                        l=l,
                                        lam=lam,
                                        tl=tl,
                                        a=a,
                                        takes=takes,
                                        out=l + (rl - tl) + sum(2 - t for t in takes),
                                        hbar=l - 1,
                                        gs=k + l - 2,
                                        coef=Fraction(
                                            1,
                                            factorial(a)
                                            * factorial(b1)
                                            * factorial(b2),
                                        ),
                                        ngh=gh[lam] + 2 * a + 4 * b + 3 * l - 2 * k,
                                    )
                                )
    return out


def label(t: dict) -> str:
    op = {
        (1, 1): "Q",
        (2, 1): "l2",
        (3, 1): "l3",
        (1, 2): "p12",
        (2, 2): "p22",
        (1, 3): "p13",
    }
    args = []
    if t["tl"] == 2 or (t["lam"] == "L1"):
        args.append(t["lam"])
    args += ["Psi"] * t["a"]
    args += ["Sig2" if s == 2 else "." for s in t["takes"]]
    lifts = (1 if t["tl"] == 1 and t["lam"] == "L2" else 0) + t["takes"].count(1)
    lifted = ["L2"] if (t["tl"] == 1 and t["lam"] == "L2") else []
    lifted += ["Sig2"] * t["takes"].count(1)
    name = f"{op[(t['k'], t['l'])]}({', '.join(args)})"
    if lifts:
        name = f"lift[{','.join(lifted)}] " + name
    return name


def key_103(t: dict) -> tuple:
    return (t["k"], t["l"], t["lam"], t["tl"], t["a"], tuple(sorted(t["takes"])))


# ---------------------------------------------------------------- literal algebra
def hat_touch(eps, comp, k, X, lam_letters: set):
    """CFL (2.1) restricted to the k-subsets containing a letter of lam_letters:
    [hat phi, lambda] e^{m} on X = lambda e^{m}; copy of the engine's hat with the
    predicate (the engine is never edited)."""
    byb: dict = {}
    for (b, c), v in comp.items():
        byb.setdefault(b, []).append((c, v))
    out: dict = {}
    for w, x in X.items():
        n = len(w)
        for S in itertools.combinations(range(n), k):
            if not any(w[p] in lam_letters for p in S):
                continue
            sg = 1
            for p in S:
                cnt = sum(1 for q in range(p) if q not in S and eps[w[q]])
                if eps[w[p]] and cnt % 2:
                    sg = -sg
            b = tuple(w[p] for p in S)
            rest = tuple(w[q] for q in range(n) if q not in S)
            for c, v in byb.get(b, []):
                key, s = iblmc.sym_norm(eps, c + rest)
                if key is None:
                    continue
                out[key] = out.get(key, 0) + sg * s * x * v
    return {k2: v for k2, v in out.items() if v != 0}


def run_c23(seed: int, coef3=Fraction(1, 2), sign2=1) -> tuple[bool, bool]:
    """E_1 and E_2 parts of e^{-m'} [hat p', Lambda_1] e^{m'} at Sigma_2 = Lambda_2 = 0,
    literal, against the book's law (E_1) and the two-output companion (E_2)."""
    D = iblmc.Data(seed)
    M, eps = D.M, D.M.eps
    psi = {(a,): v for (a,), v in D.psi1.items()}
    lam = {(a,): v for (a,), v in D.lam1.items()}
    lam_letters = {a for (a,) in D.lam1}
    # literal: sum over k of hat_touch on lambda e^{Psi}, then e^{-Psi} times, E_1 part
    X = iblmc.s_mul(eps, lam, iblmc.s_exp(eps, psi))
    lit = {1: {}, 2: {}}
    for (k, l), comp in D.fam["g"].items():
        Y = hat_touch(eps, comp, k, X, lam_letters)
        Z = iblmc.s_mul(eps, iblmc.s_exp(eps, {w: -x for w, x in psi.items()}), Y)
        for L in (1, 2):
            part = {w: x for w, x in Z.items() if len(w) == L}
            lit[L] = iblmc.s_add(lit[L], part)
    # formula: book law on E_1 (every term at hbar^0, g_s^{n-1}; here g_s = 1)
    f1: dict = {}
    for n, c in ((1, Fraction(1)), (2, Fraction(1)), (3, coef3)):
        T = iblmc.feed(M, D.fam["g"][(n, 1)], [(D.lam1, 1)] + [(D.psi1, 1)] * (n - 1))
        f1 = iblmc.s_add(f1, iblmc.to_sym(eps, T), c * (sign2 if n == 2 else 1))
    # formula: E_2 companion, compared on raw tensors (no projection: C1.4), against
    # the raw literal sum over subsets feeding Lambda_1 with two-output blocks
    f2: dict = {}
    for (k, l), c in (((1, 2), Fraction(1)), ((2, 2), Fraction(1))):
        T = iblmc.feed(M, D.fam["g"][(k, l)], [(D.lam1, 1)] + [(D.psi1, 1)] * (k - 1))
        f2 = iblmc.s_add(f2, T, c)
    raw2: dict = {}
    for (k, l), comp in D.fam["g"].items():
        if l != 2:
            continue
        for w, x in X.items():
            if len(w) != k:
                continue  # E_2 part of e^{-Psi}(.) with all letters fed: no leftovers
            for (b, cc), v in comp.items():
                if b == w:
                    raw2[cc] = raw2.get(cc, 0) + x * v
    raw2 = {k2: v for k2, v in raw2.items() if v != 0}
    ok1 = iblmc.s_add(lit[1], f1, -1) == {} and lit[1] != {}
    ok2 = iblmc.s_add(raw2, f2, -1) == {} and raw2 != {}
    return ok1, ok2


# ---------------------------------------------------------------- step 2: signed feed
def feed_signed(eps: list, comp: dict, factors: list) -> dict:
    """p_{k,l} applied to t strands of each factor (T, t) with the Koszul sign of A2.

    The word is the concatenation of the factors' index tuples (factor order kept);
    the fed letters are moved to the front keeping their order, with the sign of
    passing the unfed letters (physical parity eps); the outputs stand at the front,
    followed by the leftovers in word order.  Raw tensor {(c..., left...): v}; apply
    iblmc.to_sym(eps, .) to read it in E_L C.
    """
    byb: dict = {}
    for (b, c), v in comp.items():
        byb.setdefault(b, []).append((c, v))
    opts = []
    for T, t in factors:
        lst = []
        for idx, val in T.items():
            for pos in itertools.combinations(range(len(idx)), t):
                lst.append((idx, pos, val))
        opts.append(lst)
    out: dict = {}
    for combo in itertools.product(*opts):
        word, fedpos, w, off = [], [], Fraction(1), 0
        for idx, pos, val in combo:
            word += list(idx)
            fedpos += [off + p for p in pos]
            w *= val
            off += len(idx)
        b = tuple(word[p] for p in fedpos)
        if b not in byb:
            continue
        sg = 1
        for p in fedpos:
            cnt = sum(1 for q in range(p) if q not in fedpos and eps[word[q]])
            if eps[word[p]] and cnt % 2:
                sg = -sg
        left = tuple(word[q] for q in range(len(word)) if q not in fedpos)
        for c, v in byb[b]:
            key = c + left
            out[key] = out.get(key, 0) + sg * w * v
    return {k: v for k, v in out.items() if v != 0}


def resign(eps: list, T: dict) -> dict:
    """Decalage re-signing (record 111 C1.4): T'^{c1 c2 ...} = (-1)^{eps(c1)} T^{c1 c2 ...}."""
    return {c: (-1) ** eps[c[0]] * v for c, v in T.items()}


# ---------------------------------------------------------------- step 2: dgla model
SUBSETS = [()] + [(1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
SL2 = {  # [X_i, X_j] = sum_k f[i][j][k] X_k for (H, E, F); tr(HH)=2, tr(EF)=1
    (0, 1): {1: 2},
    (1, 0): {1: -2},
    (0, 2): {2: -2},
    (2, 0): {2: 2},
    (1, 2): {0: 1},
    (2, 1): {0: -1},
}
KAPPA = {(0, 0): 2, (1, 2): 1, (2, 1): 1}


def wedge(I: tuple, J: tuple):
    """theta^I theta^J = sign * theta^K (sorted), or (0, None) if not disjoint."""
    if set(I) & set(J):
        return 0, None
    w = list(I) + list(J)
    s = 1
    for i in range(len(w)):
        for j in range(i + 1, len(w)):
            if w[i] > w[j]:
                s = -s
    return s, tuple(sorted(w))


def dgla_model():
    """sl2 x Lambda[theta_1, theta_2, theta_3] with d = theta_2 theta_3 d/dtheta_1.

    Limitation (record 111 block M): d is a derivation of Lambda_3, so it kills the
    constants: the ghost-1 sector (degree 0) is Q-closed, Q Lambda_1 = 0 and the
    ghost-1 strand of Lambda_2 is Q-closed.  Rows 1 and the (2,2) part of row 7 are
    vacuous on this model; the (3,1) part of row 7 and rows 2, 3, 8, 9, 17 are not.  A
    finite-dimensional cyclic cdga with d != 0 on degree 0 was not found in the time
    box (C[u]/(u^2) x Lambda_3 with d = theta_1 d/du is not a cdga: d(u^2) != 0).
    Basis index a = 8 x + i (x the sl2 index, i the subset index); ghost = |I| + 1;
    pairing g(a, b) = int d^3theta tr(a b); V_2(a, b) = g(a, d b);
    V_3(a, b, c) = (-1)^{alpha} g(a, [b, c]) with alpha the first of a list of
    degree-linear candidates that makes V_3 graded symmetric in the ghost parity.
    Returns (Model, d as {(b,),(c,)}: v, alpha label).
    """
    N = 24
    gh = [len(SUBSETS[a % 8]) + 1 for a in range(N)]
    eps = [n % 2 for n in gh]

    def dec(a):
        return a // 8, SUBSETS[a % 8]

    # d theta^I = theta_2 theta_3 d/dtheta_1 theta^I
    d: dict = {}
    for a in range(N):
        x, I = dec(a)
        if 1 not in I:
            continue
        rest = tuple(i for i in I if i != 1)  # 1 is first in I: no sign
        s, K = wedge((2, 3), rest)
        if s:
            d[((a,), (8 * x + SUBSETS.index(K),))] = Fraction(s)
    g: dict = {}
    for a in range(N):
        for b in range(N):
            x, I = dec(a)
            y, J = dec(b)
            s, K = wedge(I, J)
            if s and K == (1, 2, 3) and (x, y) in KAPPA:
                g[(a, b)] = Fraction(s * KAPPA[(x, y)])

    def bracket(b, c):
        y, J = dec(b)
        z, K = dec(c)
        s, L = wedge(J, K)
        if not s or (y, z) not in SL2:
            return {}
        return {
            8 * w + SUBSETS.index(L): Fraction(s * f) for w, f in SL2[(y, z)].items()
        }

    V2: dict = {}
    for (b_, c_), v in d.items():
        for a in range(N):
            w = g.get((a, c_[0]), 0)
            if w:
                V2[(a, b_[0])] = V2.get((a, b_[0]), 0) + w * v
    raw3: dict = {}
    for b in range(N):
        for c in range(N):
            br = bracket(b, c)
            for a in range(N):
                tot = sum(g.get((a, e), 0) * v for e, v in br.items())
                if tot:
                    raw3[(a, b, c)] = tot
    deg = [gh[a] - 1 for a in range(N)]  # form degree
    cands = {
        "0": lambda a, b, c: 0,
        "p_a": lambda a, b, c: deg[a],
        "p_b": lambda a, b, c: deg[b],
        "p_c": lambda a, b, c: deg[c],
        "p_a+p_b": lambda a, b, c: deg[a] + deg[b],
        "p_a+p_c": lambda a, b, c: deg[a] + deg[c],
        "p_b+p_c": lambda a, b, c: deg[b] + deg[c],
        "p_a p_b": lambda a, b, c: deg[a] * deg[b],
        "p_b p_c": lambda a, b, c: deg[b] * deg[c],
        "p_a p_c": lambda a, b, c: deg[a] * deg[c],
    }

    def graded_sym_ok(V, eps):
        for idx, v in V.items():
            for perm in itertools.permutations(range(len(idx))):
                jdx = tuple(idx[i] for i in perm)
                s = 1
                for i in range(len(idx)):
                    for j in range(i + 1, len(idx)):
                        if (
                            perm[i] > perm[j]
                            and eps[idx[perm[i]]]
                            and eps[idx[perm[j]]]
                        ):
                            s = -s
                if V.get(jdx, 0) != s * v:
                    return False
        return True

    for name, f in cands.items():
        V3 = {(a, b, c): (-1) ** f(a, b, c) * v for (a, b, c), v in raw3.items()}
        if graded_sym_ok(V3, eps):
            break
    else:
        raise RuntimeError("no candidate sign makes V_3 graded symmetric")
    M = gap7.Model(gh, g, {2: V2, 3: V3})
    return M, d, name, graded_sym_ok(V2, eps)


gap7 = iblmc.gap7
iblgen = iblmc.iblgen


def word(eps, T: dict) -> dict:
    return iblmc.to_sym(eps, T)


def lens(X: dict, Ls) -> dict:
    return {w: x for w, x in X.items() if len(w) in Ls}


_CACHE: dict = {}


def run_step2(seed: int, flip7: int = 1, flip3: int = 1, variant: str = "") -> dict:
    """Leg 1 (C1.3-low) and leg 2 (C3.2) at hbar^0 through O(g_s); returns flags."""
    rng = random.Random(seed)
    if "model" not in _CACHE:
        M, d, alpha, v2ok = dgla_model()
        _CACHE["model"] = (M, d, alpha, v2ok)
        _CACHE["fam"] = {
            (k, l): iblgen.raise_family(M, k, l, "g")
            for (k, l) in ((1, 1), (2, 1), (1, 2))
        }
    M, d, alpha, v2ok = _CACHE["model"]
    eps = M.eps
    Q, l2 = _CACHE["fam"][(1, 1)], _CACHE["fam"][(2, 1)]
    psi = iblmc.rand_tensor(M, rng, 1, 2)
    lam1 = iblmc.rand_tensor(M, rng, 1, 1)
    sig = iblmc.rand_tensor(M, rng, 2, 4, strands=(2, 2))
    lam2 = iblmc.rand_tensor(M, rng, 2, 3, strands=(2, 1))
    m = iblmc.s_add(word(eps, psi), word(eps, sig))
    lam = iblmc.s_add(word(eps, lam1), word(eps, lam2))
    em = iblmc.s_exp(eps, m)
    emi = iblmc.s_exp(eps, {w: -x for w, x in m.items()})
    ops = {0: (Q, 1), 1: (l2, 2)}  # g_s order -> (components, k)
    H = lambda j, X: iblmc.hat(eps, ops[j][0], ops[j][1], X)  # noqa: E731
    S = iblmc.s_mul
    A = iblmc.s_add
    # literal delta m' at g_s^0, g_s^1
    dm_lit = {}
    for j in (0, 1):
        D = A(H(j, S(eps, lam, em)), S(eps, lam, H(j, em)))
        dm_lit[j] = lens(S(eps, emi, D), (1, 2, 3))
    # table rows (signed feed), g_s^0: rows 1, 7; g_s^1: rows 2, 3, 8, 9, 17
    fs = lambda comp, fac: word(eps, feed_signed(eps, comp, fac))  # noqa: E731
    dm_T = {
        0: A(fs(Q, [(lam1, 1)]), fs(Q, [(lam2, 1)]), 1),
        1: {},
    }
    dm_T[0] = A(fs(Q, [(lam1, 1)]), fs(Q, [(lam2, 1)]), flip7)
    r1 = A(fs(l2, [(lam1, 1), (psi, 1)]), fs(l2, [(lam2, 2)]), flip3)
    r2 = A(fs(l2, [(lam1, 1), (sig, 1)]), fs(l2, [(lam2, 1), (psi, 1)]))
    r3 = fs(l2, [(lam2, 1), (sig, 1)])
    dm_T[1] = A(A(r1, r2), r3)
    leg1 = all(A(dm_lit[j], dm_T[j], -1) == {} for j in (0, 1)) and all(
        lens(dm_T[1], (L,)) != {} for L in (1, 2, 3)
    )
    # leg 2: E = hat p'(e^m); residual = p(dm e^m) - p(lam E) at each order, E_1, E_2
    E = {0: H(0, em), 1: H(1, em)}
    res = {}
    for j in (0, 1):
        R: dict = {}
        for i in range(j + 1):
            R = A(R, H(i, S(eps, dm_T[j - i], em)))
            R = A(R, H(i, S(eps, lam, E[j - i])), -1)
        res[j] = lens(R, (1, 2))
    leg2 = all(res[j] == {} for j in (0, 1))
    nonvac = lens(E[1], (1, 2)) != {} and dm_T[0] != {}
    return dict(
        leg1=leg1,
        leg2=leg2,
        res1_E1=lens(res[1], (1,)) != {},
        nonvac=nonvac,
        alpha=alpha,
        v2ok=v2ok,
        M=M,
        d=d,
        Q=Q,
        l2=l2,
        eps=eps,
        rng=rng,
        lam1=lam1,
        lam2=lam2,
        psi=psi,
    )


def tensor_Q(M, Q, x: dict) -> dict:
    return iblmc.feed(M, Q, [(x, 1)])


def check_model(seed: int) -> None:
    """C3.0 and C3.1."""
    r = run_step2(seed)
    M, d, Q, l2, eps = r["M"], r["d"], r["Q"], r["l2"], r["eps"]
    rng = random.Random(seed + 7)
    q_is_d = Q == d
    # Q^2 = 0 on the basis
    q2 = all(
        tensor_Q(M, Q, tensor_Q(M, Q, {(a,): Fraction(1)})) == {} for a in range(M.N)
    )

    # derivation relation on random homogeneous vectors
    def rel(a, b, sgn):
        l = iblmc.feed(M, l2, [(a, 1), (b, 1)])
        ea = next(eps[i] for (i,) in a)
        t1 = tensor_Q(M, Q, l)
        t2 = iblmc.feed(M, l2, [(tensor_Q(M, Q, a), 1), (b, 1)])
        t3 = iblmc.feed(M, l2, [(a, 1), (tensor_Q(M, Q, b), 1)])
        return iblmc.s_add(iblmc.s_add(t1, t2), t3, sgn * (-1) ** ea)

    vecs = [iblmc.rand_tensor(M, rng, 1, n) for n in (1, 2, 3)]
    pairs = [(x, y) for x in vecs for y in vecs]
    rel_ok = all(rel(x, y, +1) == {} for x, y in pairs)
    rel_nv = any(iblmc.feed(M, l2, [(x, 1), (y, 1)]) != {} for x, y in pairs)
    rel_break = not all(rel(x, y, -1) == {} for x, y in pairs)
    check(
        "C3.0",
        q_is_d and q2 and rel_ok and rel_nv and r["v2ok"] and bool(M.V[3]),
        f"seed {seed}: Q = d, Q^2 = 0, V_2 graded symmetric, V_3 graded symmetric with "
        f"alpha = {r['alpha']}, Q l2(a,b) + l2(Qa,b) + (-1)^a l2(a,Qb) = 0 "
        f"({len(pairs)} pairs)",
    )
    check("C3.0-break", rel_break, f"seed {seed}: the opposite relative sign fails")
    # C3.1: operator form on words with odd letters
    H = lambda comp, k, X: iblmc.hat(eps, comp, k, X)  # noqa: E731
    words = [
        iblmc.s_mul(eps, iblmc.to_sym(eps, r["lam1"]), iblmc.to_sym(eps, r["psi"])),
        iblmc.s_mul(eps, iblmc.to_sym(eps, r["lam2"]), iblmc.to_sym(eps, r["psi"])),
        iblmc.to_sym(eps, r["lam2"]),
        iblmc.s_mul(eps, iblmc.to_sym(eps, r["lam1"]), iblmc.to_sym(eps, r["lam2"])),
    ]
    op_ok = True
    op_nv = False
    op_break = False
    for w in words:
        qq = H(Q, 1, H(Q, 1, w))
        ql = iblmc.s_add(H(Q, 1, H(l2, 2, w)), H(l2, 2, H(Q, 1, w)))
        qlm = iblmc.s_add(H(Q, 1, H(l2, 2, w)), H(l2, 2, H(Q, 1, w)), -1)
        op_ok = op_ok and qq == {} and ql == {}
        op_nv = op_nv or H(l2, 2, w) != {}
        op_break = op_break or qlm != {}
    check(
        "C3.1",
        op_ok and op_nv,
        f"seed {seed}: Q^2 = 0 and Q l2 + l2 Q = 0 on {len(words)} words with odd "
        f"letters (Lambda_1, Lambda_2), physical parity on every letter",
    )
    check("C3.1-break", op_break, f"seed {seed}: Q l2 - l2 Q != 0")


def check_c33(seed: int) -> None:
    """C3.3: hat Q p12(Lambda_1) + p12(Q Lambda_1) = 0 on the raw tensor."""
    r = run_step2(seed)
    M, Q, eps = r["M"], r["Q"], r["eps"]
    p12 = _CACHE["fam"][(1, 2)]
    T = iblmc.feed(M, p12, [(r["psi"], 1)])
    U = iblmc.feed(M, p12, [(tensor_Q(M, Q, r["psi"]), 1)])

    def hatQ(par):
        out: dict = {}
        for (c1, c2), v in T.items():
            for ((b,), (c,)), q in Q.items():
                if b == c1:
                    out[(c, c2)] = out.get((c, c2), 0) + q * v
                if b == c2:
                    out[(c1, c)] = out.get((c1, c), 0) + (-1) ** par[c1] * q * v
        return {k: v for k, v in out.items() if v != 0}

    shifted = [1 - e for e in eps]
    ok = iblmc.s_add(hatQ(eps), U) == {} and T != {} and U != {}
    bad1 = iblmc.s_add(hatQ(shifted), U) != {}
    bad2 = iblmc.s_add(hatQ(eps), U, -1) != {}
    check(
        "C3.3",
        ok,
        f"seed {seed}: hat Q p12(Psi) + p12(Q Psi) = 0 with the physical-parity Leibniz "
        f"sign on the raw tensor ({len(T)} entries)",
    )
    check(
        "C3.3-break",
        bad1 and bad2,
        f"seed {seed}: shifted-parity Leibniz sign fails; opposite relative sign fails",
    )


def main() -> int:
    print(f"seeds {SEEDS}")
    terms = enum_gauge_out()
    old = iblmc.enum_gauge()
    # C1.1: same configurations on E_1, E_2 as record 103 (block Lambda), hbar shifted
    old12 = {key_103(t): t for t in old if t["out"] <= 2}
    new12 = {key_103(t): t for t in terms if t["out"] <= 2}
    same = set(old12) == set(new12)
    ghost_rule = all(t["ngh"] == 2 * t["out"] + t["l"] - 1 for t in terms)
    hb_rule = all(t["hbar"] == t["l"] - 1 for t in terms)
    gs_same = all(old12[k]["tau"] == new12[k]["gs"] for k in new12)
    check(
        "C1.1",
        same and ghost_rule and hb_rule and gs_same,
        f"{len(new12)} terms on E_1, E_2 match record 103; ghost rule 2L+l_p-1 on all "
        f"{len(terms)} terms (E_1..E_4); hbar-order l_p-1",
    )
    check(
        "C1.1-break",
        not all(t["hbar"] == t["l"] - 2 for t in terms),
        "perturbed hbar rule l_p-2 disagrees",
    )
    counts = {L: sum(1 for t in terms if t["out"] == L) for L in (1, 2, 3, 4)}
    check(
        "C1.2-count",
        counts == {1: 6, 2: 10, 3: 7, 4: 3},
        f"rows per output length {counts} (record block T: 6, 10, 7, 3)",
    )
    print("--- term table (record block T) ---")
    for L in (1, 2, 3, 4):
        for t in sorted(
            (t for t in terms if t["out"] == L),
            key=lambda t: (t["gs"], t["hbar"], t["k"]),
        ):
            print(
                f"E_{L}  {label(t):34s} hbar^{t['hbar']} g_s^{t['gs']} "
                f"N_gh={t['ngh']} coef={t['coef']}"
            )
    for seed in SEEDS:
        ok1, ok2 = run_c23(seed)
        check(
            "C2.3",
            ok1 and ok2,
            f"seed {seed}: E_1 = book law, E_2 = two-output companion",
        )
        b1, _ = run_c23(seed, coef3=Fraction(1))
        b2, _ = run_c23(seed, sign2=-1)
        check(
            "C2.3-break",
            not b1 and not b2,
            f"seed {seed}: coefficient 1 and sign flip detected",
        )
    for seed in SEEDS:
        D = iblmc.Data(seed)
        M = D.M
        T = iblmc.feed(M, D.fam["g"][(1, 2)], [(D.lam1, 1)])
        anti = all(
            T.get((c2, c1), 0) == -((-1) ** (M.eps[c1] * M.eps[c2])) * v
            for (c1, c2), v in T.items()
        )
        Tp = {(c1, c2): (-1) ** M.eps[c1] * v for (c1, c2), v in T.items()}
        shifted = all(
            Tp.get((c2, c1), 0) == (-1) ** ((M.eps[c1] + 1) * (M.eps[c2] + 1)) * v
            for (c1, c2), v in Tp.items()
        )
        mixed = {k for k in T if M.eps[k[0]] != M.eps[k[1]]}
        killed = iblmc.to_sym(iblmc.eps_out(M, 2), T) == {}
        check(
            "C1.4",
            anti and shifted and killed and bool(mixed) and bool(T),
            f"seed {seed}: p12(L1) raw graded-antisymmetric (physical), re-signed "
            f"(-1)^eps(c1) graded-symmetric (shifted); plain projection kills it "
            f"({len(mixed)} mixed-sector entries)",
        )
        check(
            "C1.4-break",
            iblmc.to_sym(iblmc.eps_out(M, 2), Tp) != {},
            f"seed {seed}: the re-signed tensor survives the projection",
        )
    # ---- step 2
    for seed in SEEDS:
        check_model(seed)
        r = run_step2(seed)
        check(
            "C1.3-low",
            r["leg1"] and r["nonvac"],
            f"seed {seed}: rows 1, 2, 3, 7, 8, 9, 17 (signed feed) = literal "
            f"e^(-m')[hat p', lambda']e^(m') on E_1, E_2, E_3 at g_s^0, g_s^1, hbar^0",
        )
        b7 = run_step2(seed, flip7=-1)
        b3 = run_step2(seed, flip3=-1)
        check(
            "C1.3-low-break",
            not b7["leg1"] and not b3["leg1"],
            f"seed {seed}: row 7 flipped and row 3 flipped detected by leg 1",
        )
        check(
            "C3.2",
            r["leg2"],
            f"seed {seed}: delta_T E - [hat p', lambda'] E + lambda' hat p' E = 0 on "
            f"E_1, E_2 at g_s^0, g_s^1, hbar^0 (alpha = {r['alpha']})",
        )
        check(
            "C3.2-break",
            (not b7["leg2"]) and b7["res1_E1"] and (not b3["leg2"]) and b3["res1_E1"],
            f"seed {seed}: row 7 flipped fails at O(g_s) on E_1; row 3 flipped fails",
        )
        check_c33(seed)
    n_fail = sum(1 for _, ok in RESULTS if not ok)
    print(f"summary: {len(RESULTS) - n_fail}/{len(RESULTS)} PASS")
    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(main())
