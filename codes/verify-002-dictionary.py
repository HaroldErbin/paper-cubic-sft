"""
Verify record 002, step 4' (2026-09-26): exchange symmetry of the BV odd symplectic form.

Objects (record 002, eq. R2.3 and (D4.0)-(D4.9)):

    <A,B>       = omega_1(A, B) = <A| c0^- |B>          (BPZ bra, order-preserving)
    Omega_1(A,B) = (-1)^{|A|} <A,B>                      (|A| = N_gh mod 2)
    omega_2, Omega_2 = Koszul tensor squares (record 055 A4, physical parity).

Representation: the ghost zero-mode Fock algebra. Six anticommuting modes
c_{-1}, cb_{-1}, c_0, cb_0, c_1, cb_1 act on the SL(2,C) vacuum; a pure-c correlator
is the coefficient of the top monomial, <c_{-1} cb_{-1} c_0 cb_0 c_1 cb_1> = -1
(book bos:eq:ws-closed-vacuum-normalization), hence
<c_{-1} cb_{-1} c0^- c0^+ c_1 cb_1> = -1/2 (AGENTS.md). BPZ: bpz(c_n) = (-1)^{n-1} c_{-n},
order-preserving on products (conventions ledger C1 (ii)-(iii)). No rearrangement
identity is used: the exchange signs below are computed, not assumed.

Checks (named after the equations of 002 step 4'):
  N0      normalisation of the representation.
  C1pair  A = c1 cb1|0>, B = c0^+ c1 cb1|0>: omega_1 = -1/2 both orders (055 B3.4);
          Omega_1(A,B) = -Omega_1(B,A).
  PAIR2   the other parity assignment, level matched: A = c0^+|0> (odd, gh 1),
          B = c_{-1} cb_{-1} c1 cb1|0> (even, gh 4); same exchange signs.
  D4.0    book relation <B,A> = (-1)^{(1+|A|)(1+|B|)} <A,B>, all 64x64 monomial pairs.
  D4.1/2  omega_1 graded symmetric in eps (support) and in eps+1 (identically).
  D4.3/4  Omega_1 graded antisymmetric in eps (identically) and in eps+1; odd form.
  D4.5    twist variants.
  D4.6-9  Omega_2 = (-1)^{eps(X)} omega_2; graded symmetric in eps; antisymmetric in
          eps+c iff c odd (c_s = 1); suspended-Koszul square of Omega_1 = omega_2 on
          support; even form. Exhaustive on the level-matched ker b0^- strand basis
          (12 states, 144^2 tensor pairs), sampled on the full 64-state algebra.
  COR3    k = 3 corollary Omega_3(Y,X) = -(-1)^{eps eps} Omega_3(X,Y) (sampled).
Break legs (reported PASS when the wrong statement FAILS):
  BRK-a   <A,B> without the twist is not graded antisymmetric (the brief's break leg).
  BRK-b   bpz(c_0) = +c_0 (hermitian-like zero-mode sign) flips omega_1 to graded
          antisymmetric (s = -1): the representation sees convention (ii), so D4.1
          could have failed.
Finding check:
  REV     the reversed-order BPZ product leaves omega_1's exchange sign unchanged on
          every support pair (reversing r odd modes costs (-1)^{r(r-1)/2} on each bra,
          and r_A + r_B = 5 makes the product +1): s is decided by the zero-mode sign
          (ii), s = -sigma_0, not by the order rule (iii). Corrects the parenthetical
          of 055 B3.4, which expected s = -1 from order reversal alone.
  BRK-c   Omega_2 is not graded antisymmetric in eps; not antisymmetric in eps+0.
The Koszul tensor omega_k is imported from codes/verify-omega-k.py (functions kappa,
omega_k, extracted by AST so that the module's own checks are not executed).

Not verified: the BPZ conventions themselves (inputs (ii)-(iii), cited); states with
b-modes or c_n, |n| >= 2, and the matter factor (an even, symmetric BPZ product that
cannot change an exchange sign); the Muenster-Sachs (.,.)_bpz conventions.

Run: .venv/bin/python codes/verify-002-dictionary.py   (VERIFY_SEED overrides the seed)
"""

from __future__ import annotations

import ast
import itertools
import math
import os
import sys
from fractions import Fraction
from pathlib import Path

import numpy as np

SEED = int(os.environ.get("VERIFY_SEED", 20260926))
rng = np.random.default_rng(SEED)
RESULTS: list[tuple[str, bool]] = []

# modes: 0 c_{-1}, 1 cb_{-1}, 2 c_0, 3 cb_0, 4 c_1, 5 cb_1
MODE_N = [-1, -1, 0, 0, 1, 1]
BPZ_IDX = [4, 5, 2, 3, 0, 1]  # c_n -> c_{-n}
TOP = (0, 1, 2, 3, 4, 5)
Elt = dict[tuple[int, ...], Fraction]


def check(name: str, ok: bool, detail: str = "") -> None:
    """Record and print a named PASS/FAIL line."""
    RESULTS.append((name, bool(ok)))
    print(
        f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else "")
    )


def mono_mul(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, tuple[int, ...]]:
    """Product of two ordered Grassmann monomials: (sign, sorted monomial) or (0, ())."""
    seq = list(a) + list(b)
    if len(set(seq)) < len(seq):
        return 0, ()
    inv = sum(
        1 for i in range(len(seq)) for j in range(i + 1, len(seq)) if seq[i] > seq[j]
    )
    return (-1) ** inv, tuple(sorted(seq))


def mul(x: Elt, y: Elt) -> Elt:
    """Product in the Grassmann algebra of the six ghost zero modes."""
    out: Elt = {}
    for ma, ca in x.items():
        for mb, cb in y.items():
            sgn, m = mono_mul(ma, mb)
            if sgn:
                out[m] = out.get(m, Fraction(0)) + sgn * ca * cb
    return {m: c for m, c in out.items() if c != 0}


def mode(i: int) -> Elt:
    """Single ghost zero mode number i as an algebra element."""
    return {(i,): Fraction(1)}


C0P = {(2,): Fraction(1, 2), (3,): Fraction(1, 2)}  # c0^+ = (c0 + cb0)/2
C0M = {(2,): Fraction(1, 2), (3,): Fraction(-1, 2)}  # c0^- = (c0 - cb0)/2
ONE: Elt = {(): Fraction(1)}


def prod(*xs: Elt) -> Elt:
    """Ordered product of algebra elements."""
    out = ONE
    for x in xs:
        out = mul(out, x)
    return out


def vev(x: Elt) -> Fraction:
    """<0| x |0> for a pure-c element: -1 times the top coefficient."""
    return -x.get(TOP, Fraction(0))


def bpz(x: Elt, reverse: bool = False, sigma0: int = -1) -> Elt:
    """
    BPZ conjugate of x|0>, as the element acting to the left on <0|.

    bpz(c_n) = sigma_n c_{-n} with sigma_n = (-1)^{n-1} (convention (ii)); sigma0
    overrides the zero-mode sign (break leg BRK-b). Order-preserving (convention
    (iii)) unless reverse=True (finding check REV).
    """
    out: Elt = {}
    for m, c in x.items():
        factors = [
            {(BPZ_IDX[i],): Fraction(sigma0 if MODE_N[i] == 0 else 1)} for i in m
        ]
        if reverse:
            factors = factors[::-1]
        for k, v in prod(*factors).items():
            out[k] = out.get(k, Fraction(0)) + c * v
    return {m: c for m, c in out.items() if c != 0}


def pair(a: Elt, b: Elt, reverse: bool = False, sigma0: int = -1) -> Fraction:
    """omega_1(A,B) = <A| c0^- |B>."""
    return vev(prod(bpz(a, reverse, sigma0), C0M, b))


def parity(x: Elt) -> int:
    """Physical parity N_gh mod 2 of a homogeneous element."""
    ps = {len(m) % 2 for m in x}
    assert len(ps) == 1, "inhomogeneous element"
    return ps.pop()


# ---------------------------------------------------------------- import of 055's omega_k
def load_omega_k(par: list[int]) -> dict:
    """Extract kappa and omega_k from codes/verify-omega-k.py with PAR := par."""
    src = Path(__file__).with_name("verify-omega-k.py").read_text()
    tree = ast.parse(src)
    fns = [
        n
        for n in tree.body
        if isinstance(n, ast.FunctionDef) and n.name in ("kappa", "omega_k")
    ]
    assert len(fns) == 2
    ns: dict = {"math": math, "PAR": par}
    exec(
        compile(ast.Module(body=fns, type_ignores=[]), "verify-omega-k.py", "exec"), ns
    )
    return ns


print(f"seed = {SEED}")

# ---------------------------------------------------------------- normalisation, C1 pairs
n0 = vev(prod(mode(0), mode(1), C0M, C0P, mode(4), mode(5)))
check("N0 <c_{-1} cb_{-1} c0^- c0^+ c1 cb1> = -1/2", n0 == Fraction(-1, 2), f"{n0}")


def omega_cap(a: Elt, b: Elt) -> Fraction:
    """Omega_1(A,B) = (-1)^{|A|} <A,B>, the BV odd symplectic form."""
    return (-1) ** parity(a) * pair(a, b)


A = prod(mode(4), mode(5))
B = prod(C0P, mode(4), mode(5))
wab, wba = pair(A, B), pair(B, A)
Wab, Wba = omega_cap(A, B), omega_cap(B, A)
check(
    "C1pair omega_1(A,B) = omega_1(B,A) = -1/2 (|A|,|B|)=(0,1)",
    wab == wba == Fraction(-1, 2),
    f"{wab}, {wba}",
)
check("C1pair Omega_1(B,A) = -Omega_1(A,B) != 0", Wba == -Wab != 0, f"{Wab}, {Wba}")
A2 = C0P
B2 = prod(mode(0), mode(1), mode(4), mode(5))
w2ab, w2ba = pair(A2, B2), pair(B2, A2)
W2ab, W2ba = omega_cap(A2, B2), omega_cap(B2, A2)
check(
    "PAIR2 (|A|,|B|)=(1,0), level matched: omega_1 symmetric, nonzero",
    w2ab == w2ba != 0,
    f"{w2ab}, {w2ba}",
)
check("PAIR2 Omega_1(B,A) = -Omega_1(A,B) != 0", W2ba == -W2ab != 0, f"{W2ab}, {W2ba}")
check(
    "BRK-a C1pair+PAIR2: untwisted <A,B> fails antisymmetry",
    wba != -wab and w2ba != -w2ab,
)

# ---------------------------------------------------------------- k = 1, all 64 monomials
BASIS = [tuple(m) for r in range(7) for m in itertools.combinations(range(6), r)]
ELTS = [{m: Fraction(1)} for m in BASIS]
PAR = [len(m) % 2 for m in BASIS]
N = len(BASIS)
W1 = np.empty((N, N), dtype=object)
W1rev = np.empty((N, N), dtype=object)
W1s0 = np.empty((N, N), dtype=object)
for i, j in itertools.product(range(N), repeat=2):
    W1[i, j] = pair(ELTS[i], ELTS[j])
    W1rev[i, j] = pair(ELTS[i], ELTS[j], reverse=True)
    W1s0[i, j] = pair(ELTS[i], ELTS[j], sigma0=+1)
OM1 = np.empty((N, N), dtype=object)
for i, j in itertools.product(range(N), repeat=2):
    OM1[i, j] = (-1) ** PAR[i] * W1[i, j]
supp1 = [(i, j) for i in range(N) for j in range(N) if W1[i, j] != 0]


def count_viol(M, sign_fn, pairs) -> int:
    """Count pairs with M[j,i] != sign_fn(i,j) M[i,j]."""
    return sum(1 for i, j in pairs if M[j, i] != sign_fn(i, j) * M[i, j])


allp = list(itertools.product(range(N), repeat=2))
ps = PAR
ss = [(p + 1) % 2 for p in PAR]
check(
    f"D4.0 support: {len(supp1)} nonzero pairs, all with eps(A)+eps(B)=1",
    len(supp1) > 0 and all((ps[i] + ps[j]) % 2 == 1 for i, j in supp1),
)
v = count_viol(W1, lambda i, j: (-1) ** ((1 + ps[i]) * (1 + ps[j])), allp)
check(
    "D4.0 book relation <B,A> = (-1)^{(1+|A|)(1+|B|)}<A,B>, 4096 pairs",
    v == 0,
    f"viol={v}",
)
v = count_viol(W1, lambda i, j: (-1) ** (ps[i] * ps[j]), supp1)
check("D4.1 omega_1 graded symmetric in eps on support", v == 0, f"viol={v}")
v = count_viol(W1, lambda i, j: (-1) ** (ss[i] * ss[j]), allp)
check("D4.2 omega_1 graded symmetric in eps+1 identically", v == 0, f"viol={v}")
v = count_viol(OM1, lambda i, j: -((-1) ** (ps[i] * ps[j])), allp)
check("D4.3 Omega_1 graded antisymmetric in eps identically", v == 0, f"viol={v}")
v = count_viol(OM1, lambda i, j: -((-1) ** (ss[i] * ss[j])), allp)
check("D4.4 Omega_1 graded antisymmetric in eps+1 (all pairs)", v == 0, f"viol={v}")
check(
    "D4.4 Omega_1 odd form: nonzero only on deg_s(A)+deg_s(B) odd",
    all((ss[i] + ss[j]) % 2 == 1 for i, j in allp if OM1[i, j] != 0),
)
vb = count_viol(OM1, lambda i, j: -1, supp1)
va = count_viol(W1, lambda i, j: -1, supp1)
check(
    "D4.4 on support: plain antisymmetry of Omega_1; <.,.> plain symmetric",
    vb == 0 and count_viol(W1, lambda i, j: 1, supp1) == 0,
)
v_twB = sum(1 for i, j in supp1 if (-1) ** ps[j] * W1[i, j] != -OM1[i, j])
v_tws = sum(1 for i, j in supp1 if (-1) ** ss[i] * W1[i, j] != -OM1[i, j])
v_tw2 = sum(1 for i, j in supp1 if (-1) ** (ps[i] + ps[j]) * W1[i, j] != -W1[i, j])
check(
    "D4.5 twist variants (-1)^|B|, (-1)^{|A|_s}: -Omega_1; (-1)^{|A|+|B|}: -<.,.>",
    v_twB == v_tws == v_tw2 == 0,
)
check(
    "BRK-a <A,B> without (-1)^|A| fails odd-symplectic antisymmetry (all 4096)",
    count_viol(W1, lambda i, j: -((-1) ** (ss[i] * ss[j])), allp) == len(supp1) == va,
    f"viol={va} = all {len(supp1)} support pairs",
)
vr = count_viol(W1s0, lambda i, j: -((-1) ** (ps[i] * ps[j])), allp)
vrs = count_viol(W1s0, lambda i, j: (-1) ** (ps[i] * ps[j]), supp1)
check(
    "BRK-b bpz(c_0)=+c_0: omega_1 graded antisymmetric (s=-1), D4.1 fails there",
    vr == 0 and vrs == len(supp1),
    f"antisym viol={vr}, sym viol={vrs}",
)
vv = count_viol(W1rev, lambda i, j: (-1) ** (ps[i] * ps[j]), supp1)
flips = sum(1 for i, j in supp1 if W1rev[i, j] != W1[i, j])
check(
    "REV reversed-order BPZ product: omega_1 still graded symmetric (s=+1)",
    vv == 0 and flips > 0,
    f"sym viol={vv}; {flips}/{len(supp1)} values flip sign",
)
c1rev = (pair(A, B, reverse=True), pair(B, A, reverse=True))
check(
    "REV C1pair under reversal: both orders flip together",
    c1rev == (-wab, -wba),
    f"{c1rev[0]}, {c1rev[1]}",
)

# ---------------------------------------------------------------- k = 2
LMGEN = [mode(0), mode(1), C0P, mode(4), mode(5)]  # c_{-1}, cb_{-1}, c0^+, c1, cb1
LMLEV = [(1, 0), (0, 1), (0, 0), (-1, 0), (0, -1)]  # (L0, Lb0) shift of each factor
LM = []
for r in range(6):
    for sub in itertools.combinations(range(5), r):
        if sum(LMLEV[g][0] for g in sub) == sum(LMLEV[g][1] for g in sub):
            LM.append(prod(*[LMGEN[g] for g in sub]) if sub else ONE)
PL = [parity(x) for x in LM]
NL = len(LM)
WL = np.empty((NL, NL), dtype=object)
for i, j in itertools.product(range(NL), repeat=2):
    WL[i, j] = pair(LM[i], LM[j])
OL = np.empty((NL, NL), dtype=object)
for i, j in itertools.product(range(NL), repeat=2):
    OL[i, j] = (-1) ** PL[i] * WL[i, j]
check(
    f"LM basis: {NL} level-matched ker b0^- states, omega_1 rank "
    f"{np.linalg.matrix_rank(WL.astype(float))}",
    NL == 12,
)

nsP = load_omega_k(PL)
nsS = load_omega_k([(p + 1) % 2 for p in PL])


def eX(X, par):
    """Physical (or shifted) parity of a basis tensor."""
    return sum(par[x] for x in X) % 2


def k2_checks(tag, om_k_phys, om_k_susp, par, W, Om, pairs_iter):
    """Run the D4.6-D4.9 and BRK-c checks on an iterator of tensor pairs."""
    stats = dict.fromkeys(
        ["n", "nz", "D46", "D47", "D48c1", "D48c0", "D48a", "D49", "BRKc"], 0
    )
    for X, Y in pairs_iter:
        w_xy = om_k_phys(W, X, Y)
        o_xy, o_yx = om_k_phys(Om, X, Y), om_k_phys(Om, Y, X)
        ex, ey = eX(X, par), eX(Y, par)
        stats["n"] += 1
        stats["D46"] += o_xy != (-1) ** ex * w_xy
        if o_xy == 0:
            continue
        stats["nz"] += 1
        g = (-1) ** (ex * ey)
        stats["D47"] += o_yx != g * o_xy
        stats["D48c1"] += o_yx != -((-1) ** (((ex + 1) * (ey + 1)) % 2)) * o_xy
        stats["D48c0"] += o_yx == -g * o_xy  # antisym in eps+0 must fail
        stats["D48a"] += om_k_susp(Om, X, Y) != w_xy
        stats["D49"] += ex != ey
        stats["BRKc"] += o_yx == -g * o_xy
    n, nz = stats["n"], stats["nz"]
    check(f"D4.6 {tag} Omega_2 = (-1)^eps(X) omega_2 ({n} pairs)", stats["D46"] == 0)
    check(
        f"D4.7 {tag} Omega_2 graded symmetric in eps ({nz} nonzero)",
        stats["D47"] == 0 and nz > 0,
        f"viol={stats['D47']}",
    )
    check(
        f"D4.8 {tag} c_s=1: Omega_2 graded antisymmetric in eps+1",
        stats["D48c1"] == 0 and nz > 0,
        f"viol={stats['D48c1']}",
    )
    check(
        f"D4.8 {tag} c_s=0 excluded: antisymmetry in eps holds on no nonzero pair",
        stats["D48c0"] == 0,
        f"agree={stats['D48c0']}",
    )
    check(
        f"D4.8a {tag} suspended-Koszul square of Omega_1 = omega_2 on support",
        stats["D48a"] == 0,
        f"viol={stats['D48a']}",
    )
    check(f"D4.9 {tag} Omega_2 even form: eps(X)=eps(Y) on support", stats["D49"] == 0)
    check(
        f"BRK-c {tag} Omega_2 graded-antisymmetric-in-eps claim fails on every nonzero pair",
        stats["BRKc"] == 0 and nz > 0,
    )


tens = list(itertools.product(range(NL), repeat=2))
k2_checks(
    "LM exhaustive",
    nsP["omega_k"],
    nsS["omega_k"],
    PL,
    WL,
    OL,
    ((X, Y) for X in tens for Y in tens),
)

# full 64-state algebra, sampled
nsP64 = load_omega_k(PAR)
nsS64 = load_omega_k([(p + 1) % 2 for p in PAR])
partners = {i: [j for j in range(N) if W1[i, j] != 0] for i in range(N)}
has_p = [i for i in range(N) if partners[i]]


def sample_pairs(k, n):
    """Seeded random k-strand pairs, 90% paired strand by strand on support."""
    for _ in range(n):
        X = tuple(int(rng.choice(has_p)) for _ in range(k))
        if rng.random() < 0.9:
            Y = tuple(int(rng.choice(partners[x])) for x in X)
        else:
            Y = tuple(int(rng.integers(N)) for _ in range(k))
        yield X, Y


k2_checks(
    "64 sampled",
    nsP64["omega_k"],
    nsS64["omega_k"],
    PAR,
    W1,
    OM1,
    sample_pairs(2, 20000),
)

# k = 3 corollary
bad = nz = 0
for X, Y in sample_pairs(3, 8000):
    o_xy, o_yx = nsP64["omega_k"](OM1, X, Y), nsP64["omega_k"](OM1, Y, X)
    if o_xy != 0:
        nz += 1
        bad += o_yx != -((-1) ** (eX(X, PAR) * eX(Y, PAR))) * o_xy
check(
    "COR3 Omega_3(Y,X) = -(-1)^{eps eps} Omega_3(X,Y) (sampled)",
    bad == 0 and nz > 0,
    f"viol={bad}, nonzero={nz}",
)

n_fail = sum(not ok for _, ok in RESULTS)
print(f"\nseed = {SEED}: {len(RESULTS) - n_fail}/{len(RESULTS)} PASS")
sys.exit(1 if n_fail else 0)
