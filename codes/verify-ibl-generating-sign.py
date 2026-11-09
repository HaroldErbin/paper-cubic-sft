"""
IBL section of the paper: which family the generating function encodes, and where the
Omega^{-1} raising enters the relations.

Record: agent/derivations/088-ibl-generating-sign.md (paper 07-ibl.tex l. 128-160).

Families compared (A4 of the record), all defined from the same vertices V_{m+n}:
  sprod   V(A_1..A_n, B) = <A_1 x .. x A_n, p_{m,n}(B)>_n        (paper eq:conv:sprod)
  Omega   V(A_1..A_n, B) = Omega_n(A, pO_{m,n}(B)),   Omega(A,B) = (-1)^|A| <A,B>
  Omega'  V(A_1..A_n, B) = Omega'_n(A, pO'_{m,n}(B)), Omega'(A,B) = (-1)^|B| <A,B> = -Omega
Each n-fold form is the tensor power with the Koszul sign of eq:conv:pairing-n,
(-1)^{sum_{i<j} |B_i||A_j|}.  The families are built by raising each leg with the inverse
matrix of the form (g^{-1}, Omega^{-1}, -Omega^{-1}), not from the claimed twist formula.

Check labels and the record-088 node each one tests.  The labels are NOT node IDs (they
were fixed before the claim tree was numbered); the node is given in brackets and agrees
with the tree's [check: ...] tags.  The Omega family pO is p^{Omega} in the record.
  C1.1 [node C1.1]: pO_{m,n} = (-P)^{(x)n} p_{m,n} componentwise, pO' = P^{(x)n} p,
    P = (-1)^eps.  C1.1-break [C1.1]: pO = P^{(x)n} p fails
  C1-def [node C1.1]: each family satisfies its defining relation on basis states
  C1.1-input [node C1.2]: the same read on the inputs, pO_{m,n}(B) = (-1)^{|B|} p(B),
    pO'_{m,n}(B) = (-1)^{n+|B|} p_{m,n}(B)
  C1.2 [node C1.3]: ghost-two inputs, pO/p = +1 on every component for n = 1, 2, 3;
    pO'/p = (-1)^n on every component (overall sign, never component-dependent).
    C1.2-break [C1.3]
  C1.3 [node C1.4]: unrestricted inputs, pO/p takes both signs already at n = 1.
    C1.3-superfield [C1.4]: pO_{m,1}(Psi^m) != +-l_m(Psi^m); on ghost-two Psi,
    pO = +l, pO' = -l
  C2.1 [node C2.1]: eq:ibl:generating verbatim (sprod family, <.,.>_n), n = 0..4, all
    (m,n).  C2.1-break [C2.1]: sprod family read through Omega_1 misses V
  C2.2 [node C2.2]: Omega family with Omega_n (and Omega' with Omega'_n) reproduces
    the same terms
  C2.3 [node C2.3]: Omega family inserted in the paper's formula (<.,.>_n): the n = 1
    terms differ from +-V_{m+1}(Psi', Psi^m) on unrestricted superfields; on ghost-two
    Psi they equal +V (Omega) and -V (Omega')
  C2.4 [node C2.1]: rule dependence, with no Koszul signs anywhere (naive rule, applied
    to V, p and the pairing alike) C2.1 still holds
  C3.0 [node C3.1]: both sides of (088.9) for F in {sprod, Omega, Omega'}.
    (i) Freed strand, every basis state e_a: F_{l2}(e_a (x) Psi'^{l2-1},
    p^F_{k2,l2}(Psi^{k2})) (l2-output member, l2-fold form) = F_1(e_a, Z^F) with
    Z^F = p^F_{k2+l2-1,1}(Psi'^{l2-1}, Psi^{k2}) (one-output member)
    = V(e_a, Psi'^{l2-1}, Psi^{k2}).
    (ii) Receiving product on the odd superfield Z^F, every configuration with
    l1 >= 2 or l2 >= 2: F_{l1}(Psi'^{l1}, p^F_{k1,l1}(Z^F, Psi^{k1-1}))
    = V(Psi'^{l1}, Z^F, Psi^{k1-1}).  Non-hollow: nonzero V at l2 >= 2 and at l1 >= 2.
    C3.0-break [C3.1]: the sprod strand, and the sprod receiving member, read in the
    Omega form each fail somewhere.
    Added in the fix pass after critic 088 #13; written 2026-10-04, not yet run.
  C3.1 [node C3.2]: R^F_{m,n} := sum over configurations of V(Psi'^{l1},
    p^F_{.,1}(Psi'^{l2-1}, Psi^{k2}), Psi^{k1-1}) / ((k1-1)! l1! k2! (l2-1)!)
    (plain composition in the family's own form, right-hand side of (088.9)) equals
    -E_{m,n} for Omega and +E_{m,n} for Omega' (C3.1-prime [C3.2]), every bidegree,
    generic data (E from the polarized master equation, 086 engine).
    C3.1-break [C3.2]: R^Omega = +E fails
  C3.2 [node C3.3]: R^sprod_{m,n} == 0 identically on generic data (mirror pairs
    cancel), while its individual terms do not vanish.  C3.2-break [C3.3]: dropping
    one mirror term leaves it nonzero
  C3.2-delta [node C3.3]: the polarized master equation contracted with Delta = g^{-1}
    instead of Omega^{-1} vanishes identically at every bidegree (generic data)
  C3.3 [node C3.4]: sl2 + sl2* (cyclic dg Lie): E = 0 and R^Omega = 0;
    Jacobi-violating variant: E != 0 and R^Omega = -E != 0; R^sprod = 0 on both
Most -break legs (C1.1-, C1.2-, C2.1-, C3.1-break) assert that the negation of the
claim fails on the data, i.e. they are non-hollowness checks; C3.2-break and
C3.0-break perturb the computation itself (critic 088 #12).
Method: exact Grassmann polynomials over Fractions (engine imported from
codes/verify-paper-gap-7.py, not edited); rule K for superfields (record 086 A2).
NOT verified: closed-string vertices; CFL's operator-level signs (the relations are taken
in generating-function form, as in the paper and record 086 C1.2).

Usage:  .venv/bin/python codes/verify-ibl-generating-sign.py
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
_spec = importlib.util.spec_from_file_location("gap7", ROOT / "verify-paper-gap-7.py")
gap7 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(gap7)

SEED = 20261004
RESULTS: list[tuple[str, bool]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    """Record and print one named PASS/FAIL check."""
    RESULTS.append((name, bool(ok)))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}")


# ---------------------------------------------------------------- forms and families
def form_matrix(M, kind: str) -> dict:
    """Matrix of the single-string form: g, Omega, or Omega' = -Omega."""
    if kind == "g":
        return dict(M.g)
    if kind == "O":
        return dict(M.omega)
    if kind == "Op":
        return {k: -v for k, v in M.omega.items()}
    raise ValueError(kind)


def raise_family(M, m: int, n: int, kind: str) -> dict:
    """Components {(b, c): value} of the family member with m inputs, n outputs.

    Solves V_{a_1..a_n b} = sum_c (-1)^{sum_{i<j} eps(c_i) eps(a_j)} prod_i F_{a_i c_i}
    p^{c}_b by raising each leg with the inverse matrix of F.
    """
    eps = M.eps
    F = form_matrix(M, kind)
    Finv = gap7.inverse(M.N, F)
    rows: dict[int, list[tuple[int, Fraction]]] = {}
    for (c, a), w in Finv.items():
        rows.setdefault(a, []).append((c, w))
    out: dict = {}
    for idx, val in M.V.get(m + n, {}).items():
        a, b = idx[:n], idx[n:]
        for choice in itertools.product(*[rows.get(ai, []) for ai in a]):
            c = tuple(x[0] for x in choice)
            w = Fraction(val)
            for x in choice:
                w *= x[1]
            # Koszul sign of the pairing; on the support eps(a_j) = eps(c_j) + 1
            kap = sum(
                eps[c[i]] * (eps[c[j]] + 1) for i in range(n) for j in range(i + 1, n)
            )
            key = (b, c)
            out[key] = out.get(key, 0) + (-1) ** kap * w
    return {k: v for k, v in out.items() if v != 0}


def form_n_basis(M, F: dict, a: tuple, c: tuple) -> Fraction:
    """n-fold form on basis tensors, Koszul sign of eq:conv:pairing-n."""
    eps = M.eps
    w = Fraction(1)
    for ai, ci in zip(a, c):
        w *= F.get((ai, ci), 0)
        if w == 0:
            return Fraction(0)
    n = len(a)
    s = sum(eps[c[i]] * eps[a[j]] for i in range(n) for j in range(i + 1, n))
    return (-1) ** s * w


def apply(M, comp: dict, args: list, naive: bool = False) -> dict:
    """p(args) on superfields with rule K: {c: polynomial} (coefficient left of e_c)."""
    eps = M.eps
    out: dict = {}
    for (b, c), val in comp.items():
        coef = {(): Fraction(val)}
        ok = True
        for k, bk in enumerate(b):
            x = args[k][bk]
            if not x:
                ok = False
                break
            s = 1
            if not naive:
                s = (-1) ** (M.ga.parity(x) * sum(eps[bi] for bi in b[:k]))
            coef = M.ga.mul(coef, {mm: s * v for mm, v in x.items()})
        if ok and coef:
            out[c] = M.ga.add(out.get(c, {}), coef)
    return {k: v for k, v in out.items() if v}


def tpow(M, f: list, n: int, naive: bool = False) -> dict:
    """Psi^{(x)n} = (Psi^a e_a)^{(x)n} with rule K: {a: polynomial}."""
    return apply(
        M,
        {(a, a): Fraction(1) for a in itertools.product(range(M.N), repeat=n)},
        [f] * n,
        naive,
    )


def form_n(M, kind: str, X: dict, Y: dict, naive: bool = False) -> dict:
    """Form_n(lam e_a, mu e_c) = (-1)^{|mu| eps(a)} lam mu Form_n(e_a, e_c)."""
    F = form_matrix(M, kind)
    eps = M.eps
    total: dict = {}
    for a, lam in X.items():
        for c, mu in Y.items():
            w = form_n_basis(M, F, a, c)
            if w == 0:
                continue
            s = 1 if naive else (-1) ** (M.ga.parity(mu) * sum(eps[x] for x in a))
            total = M.ga.add(total, M.ga.mul(lam, mu), coeffs=[1, s * w])
    return total


def vertex_naive(M, n: int, args: list) -> dict:
    """V_n(args) with coefficients pulled left WITHOUT Koszul signs."""
    total: dict = {}
    for idx, val in M.V.get(n, {}).items():
        coef = {(): Fraction(val)}
        for arg, a in zip(args, idx):
            c = arg[a]
            if not c:
                coef = {}
                break
            coef = M.ga.mul(coef, c)
        if coef:
            total = M.ga.add(total, coef)
    return total


def scal(c, P: dict) -> dict:
    return {m: c * v for m, v in P.items() if c * v != 0}


def sub(M, A: dict, B: dict, c=1) -> dict:
    return M.ga.add(A, B, coeffs=[1, -c])


def restrict(M, f: list, gh: int) -> list:
    """Keep only the components of a superfield along basis vectors of ghost number gh."""
    return [x if M.gh[a] == gh else {} for a, x in enumerate(f)]


# ---------------------------------------------------------------- generating function
def gen_term(M, fam: str, form: str, m: int, n: int, p, q, naive=False) -> dict:
    """(1/m! n!) Form_n(Psi'^n, p^fam_{m,n}(Psi^m))."""
    comp = raise_family(M, m, n, fam)
    Y = apply(M, comp, [p] * m, naive)
    X = tpow(M, q, n, naive)
    return scal(Fraction(1, factorial(m) * factorial(n)), form_n(M, form, X, Y, naive))


def target(M, m: int, n: int, p, q, naive=False) -> dict:
    """(1/m! n!) V_{m+n}(Psi'^n, Psi^m), the bidegree-(m,n) term of S(Psi + Psi')."""
    args = [q] * n + [p] * m
    v = vertex_naive(M, m + n, args) if naive else M.vertex(m + n, args)
    return scal(Fraction(1, factorial(m) * factorial(n)), v)


# ---------------------------------------------------------------- relations
def relation(M, fam: str, m: int, n: int, drop_one: bool = False) -> tuple[dict, int]:
    """Plain-composition relation of family fam at (m,n), generating-function form.

    Each configuration (k1,l1;k2,l2), k1+k2-1 = m, l1+l2-1 = n, k1 >= 1, l2 >= 1:
    an output strand of p^fam_{k2,l2} (the others read with Psi' through fam's own form,
    which reproduces V) is inserted into an input of p^fam_{k1,l1} (outputs read with Psi'
    through fam's form): the scalar V(Psi'^{l1}, Z, Psi^{k1-1}), Z = p^fam_{K,1}(Psi'^{l2-1},
    Psi^{k2}), with the weight of C(H_{k1,l1}, H_{k2,l2}).
    """
    p, q = M.field("p"), M.field("q")
    total: dict = {}
    nterms = 0
    for k1 in range(1, m + 2):
        k2 = m + 1 - k1
        for l2 in range(1, n + 2):
            l1 = n + 1 - l2
            if k1 + l1 not in M.V or k2 + l2 not in M.V:
                continue
            K = k2 + l2 - 1
            Zd = apply(M, raise_family(M, K, 1, fam), [q] * (l2 - 1) + [p] * k2)
            Z = [Zd.get((c,), {}) for c in range(M.N)]
            val = M.vertex(k1 + l1, [q] * l1 + [Z] + [p] * (k1 - 1))
            if not val:
                continue
            nterms += 1
            if drop_one and nterms == 1:
                continue
            w = Fraction(1, factorial(k1 - 1) * factorial(l1) * factorial(k2))
            w /= factorial(l2 - 1)
            total = M.ga.add(total, val, coeffs=[1, w])
    return total, nterms


def tensor(M, args: list) -> dict:
    """A_1 (x) ... (x) A_n of superfields with rule K: {(a_1..a_n): polynomial}."""
    n = len(args)
    ident = {(a, a): Fraction(1) for a in itertools.product(range(M.N), repeat=n)}
    return apply(M, ident, args)


def basis_field(M, a: int) -> list:
    """The basis state e_a written as a superfield with the even coefficient 1."""
    return [{(): Fraction(1)} if b == a else {} for b in range(M.N)]


def freed_strand(
    M, fam: str, k2: int, l2: int, zfam: str | None = None
) -> tuple[bool, int]:
    """First line of (088.9), on every basis state A = e_a.

    Compares F_{l2}(e_a (x) Psi'^{l2-1}, p^F_{k2,l2}(Psi^{k2})), built from the
    l2-output member and the l2-fold form, with F_1(e_a, Z), where
    Z = p^F_{k2+l2-1,1}(Psi'^{l2-1}, Psi^{k2}) is built from the one-output member, and
    with V_{k2+l2}(e_a, Psi'^{l2-1}, Psi^{k2}) (rule K throughout).

    Args:
        M: model (086 engine).
        fam: family F ("g" sprod, "O" Omega, "Op" Omega').
        k2: inputs of the supplying product.
        l2: outputs of the supplying product (>= 1).
        zfam: family used for Z (default fam; another family is a break leg).

    Returns:
        tuple[bool, int]: (all three agree for every a, number of nonzero V values).

    """
    p, q = M.field("p"), M.field("q")
    zfam = zfam or fam
    Y = apply(M, raise_family(M, k2, l2, fam), [p] * k2)
    Zd = apply(M, raise_family(M, k2 + l2 - 1, 1, zfam), [q] * (l2 - 1) + [p] * k2)
    ok, nonzero = True, 0
    for a in range(M.N):
        A = basis_field(M, a)
        lhs = form_n(M, fam, tensor(M, [A] + [q] * (l2 - 1)), Y)
        mid = form_n(M, fam, tensor(M, [A]), Zd)
        rhs = M.vertex(k2 + l2, [A] + [q] * (l2 - 1) + [p] * k2)
        if sub(M, lhs, mid) or sub(M, mid, rhs):
            ok = False
        nonzero += bool(rhs)
    return ok, nonzero


def receiving(
    M, fam: str, k1: int, l1: int, Z: list, pfam: str | None = None
) -> tuple[dict, dict]:
    """Second line of (088.9) for an odd superfield Z.

    Returns F_{l1}(Psi'^{l1}, p^{pfam}_{k1,l1}(Z, Psi^{k1-1})), the receiving product
    applied to Z with its l1 outputs read with Psi' through F's own form, and
    V_{k1+l1}(Psi'^{l1}, Z, Psi^{k1-1}); pfam defaults to fam (another family is a break
    leg).
    """
    p, q = M.field("p"), M.field("q")
    pfam = pfam or fam
    Y = apply(M, raise_family(M, k1, l1, pfam), [Z] + [p] * (k1 - 1))
    lhs = form_n(M, fam, tpow(M, q, l1), Y)
    rhs = M.vertex(k1 + l1, [q] * l1 + [Z] + [p] * (k1 - 1))
    return lhs, rhs


def polarized(M) -> dict:
    """E = C(S(Psi+Psi'), S(Psi+Psi')), contraction with Omega^{-1} (086 engine)."""
    Su = M.S("u")
    return M.contract(Su, Su)


def bidegrees(M) -> list[tuple[int, int]]:
    top = 2 * max(M.V) - 2
    return [(m, d - m) for d in range(2, top + 1) for m in range(d + 1)]


# ---------------------------------------------------------------- main
def ratios(M, fam: str, m: int, n: int, gh_in: int | None) -> set:
    """Set of component ratios p^fam / p^sprod (inputs restricted to ghost gh_in)."""
    A, B = raise_family(M, m, n, fam), raise_family(M, m, n, "g")
    keys = set(A) | set(B)
    out = set()
    for key in keys:
        b = key[0]
        if gh_in is not None and any(M.gh[x] != gh_in for x in b):
            continue
        x, y = A.get(key, 0), B.get(key, 0)
        out.add(x / y if y != 0 else ("inf" if x else "0/0"))
    return out


def main() -> int:
    print(f"seed {SEED}")
    rng = random.Random(SEED)
    M = gap7.generic_model(rng)
    eps, N = M.eps, M.N
    print("ghosts", M.gh, "| vertex degrees", sorted(M.V))

    # ---------------- C1: components of the two families
    mn_list = [(m, n) for d in sorted(M.V) for n in range(1, d + 1) for m in [d - n]]
    ok_twist, ok_twist_p, broke = True, True, False
    for m, n in mn_list:
        g = raise_family(M, m, n, "g")
        O = raise_family(M, m, n, "O")
        Op = raise_family(M, m, n, "Op")
        for key in set(g) | set(O) | set(Op):
            c = key[1]
            Pn = (-1) ** sum(eps[x] for x in c)
            mP = (-1) ** n * Pn
            if O.get(key, 0) != mP * g.get(key, 0):
                ok_twist = False
            if Op.get(key, 0) != Pn * g.get(key, 0):
                ok_twist_p = False
            if O.get(key, 0) != Pn * g.get(key, 0):
                broke = True
    check(
        "C1.1",
        ok_twist and ok_twist_p,
        f"pO = (-P)^n p and pO' = P^n p on every component, (m,n) in {mn_list}",
    )
    check("C1.1-break", broke, "pO = P^n p (wrong twist) fails somewhere (expected)")
    # same statement read on the inputs: pO_{m,n}(e_b) = (-1)^{eps(b_1)+..+eps(b_m)} p(e_b)
    ok_in, ok_inp = True, True
    for m, n in mn_list:
        g = raise_family(M, m, n, "g")
        O = raise_family(M, m, n, "O")
        Op = raise_family(M, m, n, "Op")
        for key in set(g) | set(O):
            sb = (-1) ** sum(eps[x] for x in key[0])
            if O.get(key, 0) != sb * g.get(key, 0):
                ok_in = False
            if Op.get(key, 0) != (-1) ** n * sb * g.get(key, 0):
                ok_inp = False
    check(
        "C1.1-input",
        ok_in and ok_inp,
        "pO_{m,n}(B) = (-1)^{|B|} p_{m,n}(B), pO' = (-1)^{n+|B|} p, every component",
    )
    # definition re-check: Form_n(e_a, p(e_b)) == V_{ab}
    okdef = True
    for fam in ("g", "O", "Op"):
        for m, n in mn_list:
            comp = raise_family(M, m, n, fam)
            F = form_matrix(M, fam)
            acc: dict = {}
            for (b, c), v in comp.items():
                for a in itertools.product(range(N), repeat=n):
                    w = form_n_basis(M, F, a, c)
                    if w:
                        acc[a + b] = acc.get(a + b, 0) + w * v
            acc = {k: v for k, v in acc.items() if v != 0}
            if acc != {k: Fraction(v) for k, v in M.V[m + n].items()}:
                okdef = False
    check(
        "C1-def", okdef, "each family satisfies its defining relation on basis states"
    )

    lines = []
    ok_g2, ok_g2p, nonhollow = True, True, True
    for m, n in mn_list:
        rO, rOp = ratios(M, "O", m, n, 2), ratios(M, "Op", m, n, 2)
        if m == 0:
            continue
        lines.append(
            f"(m,n)=({m},{n}): O {sorted(map(str, rO))} O' {sorted(map(str, rOp))}"
        )
        if not rO:
            nonhollow = False
        if rO != {1}:
            ok_g2 = False
        if rOp != {(-1) ** n}:
            ok_g2p = False
    for ln in lines:
        print("   ", ln)
    check(
        "C1.2",
        ok_g2 and ok_g2p and nonhollow,
        "ghost-two inputs: pO/p = +1 for n = 1,2,3; pO'/p = (-1)^n, one value each",
    )
    check(
        "C1.2-break",
        ratios(M, "O", 2, 1, 2) != {-1},
        "claim 'pO = -l at one output on ghost-two inputs' fails (expected)",
    )
    both = all(ratios(M, "O", m, 1, None) >= {1, -1} for m in (1, 2, 3))
    check(
        "C1.3", both, "unrestricted inputs: pO/p takes both signs at n = 1, m = 1,2,3"
    )
    p, q = M.field("p"), M.field("q")
    p2 = restrict(M, p, 2)
    sf_ok = True
    for m in (1, 2, 3):
        lO = apply(M, raise_family(M, m, 1, "O"), [p] * m)
        lg = apply(M, raise_family(M, m, 1, "g"), [p] * m)
        same = all(not sub(M, lO.get(c, {}), lg.get(c, {})) for c in set(lO) | set(lg))
        opp = all(not M.ga.add(lO.get(c, {}), lg.get(c, {})) for c in set(lO) | set(lg))
        if same or opp or not lg:
            sf_ok = False
        lO2 = apply(M, raise_family(M, m, 1, "O"), [p2] * m)
        lOp2 = apply(M, raise_family(M, m, 1, "Op"), [p2] * m)
        lg2 = apply(M, raise_family(M, m, 1, "g"), [p2] * m)
        ks = set(lO2) | set(lg2) | set(lOp2)
        if not lg2 or not all(
            not sub(M, lO2.get(c, {}), lg2.get(c, {}))
            and not M.ga.add(lOp2.get(c, {}), lg2.get(c, {}))
            for c in ks
        ):
            sf_ok = False
    check(
        "C1.3-superfield",
        sf_ok,
        "pO_{m,1}(Psi^m) != +-l_m(Psi^m) generic; ghost-two Psi: pO = +l, pO' = -l",
    )

    # ---------------- C2: generating function
    pairs = [(m, n) for d in sorted(M.V) for n in range(0, d + 1) for m in [d - n]]
    ok21, ok22, hol = True, True, []
    for m, n in pairs:
        t = target(M, m, n, p, q)
        hol.append(bool(t))
        if sub(M, gen_term(M, "g", "g", m, n, p, q), t):
            ok21 = False
        if sub(M, gen_term(M, "O", "O", m, n, p, q), t):
            ok22 = False
        if sub(M, gen_term(M, "Op", "Op", m, n, p, q), t):
            ok22 = False
        Hk = M.H(m, n)
        if sub(M, Hk, t):
            ok21 = False
    check(
        "C2.1",
        ok21 and all(hol),
        f"sprod family in <.,.>_n reproduces every term of S(Psi+Psi'), {pairs}",
    )
    brk = any(
        sub(M, gen_term(M, "g", "O", m, 1, p, q), target(M, m, 1, p, q))
        for m in (1, 2, 3)
    )
    check("C2.1-break", brk, "sprod family read through Omega_1 misses V (expected)")
    check(
        "C2.2", ok22, "Omega family in Omega_n, Omega' family in Omega'_n: same terms"
    )
    ok23 = True
    for m in (1, 2, 3):
        t = target(M, m, 1, p, q)
        gO = gen_term(M, "O", "g", m, 1, p, q)
        if not sub(M, gO, t) or not M.ga.add(gO, t):
            ok23 = ok23 and False
        t2 = target(M, m, 1, p2, q)
        if not t2:
            ok23 = False
        if sub(M, gen_term(M, "O", "g", m, 1, p2, q), t2):
            ok23 = False
        if M.ga.add(gen_term(M, "Op", "g", m, 1, p2, q), t2):
            ok23 = False
    check(
        "C2.3",
        ok23,
        "Omega family in the paper's formula: n=1 terms != +-V generic;"
        " ghost-two Psi: +V (Omega), -V (Omega')",
    )
    ok24 = True
    for m, n in pairs:
        if sub(
            M,
            gen_term(M, "g", "g", m, n, p, q, naive=True),
            target(M, m, n, p, q, naive=True),
        ):
            ok24 = False
    check(
        "C2.4", ok24, "naive rule (no Koszul signs) applied uniformly: C2.1 still holds"
    )

    # ---------------- C3.0: both sides of (088.9), node C3.1 (critic 088 #13)
    # Written in the fix pass of 2026-10-04 and not yet run (text-only pass).
    degs = sorted(M.V)
    supplying = [(d - j, j) for d in degs for j in range(1, d + 1)]  # (k2, l2), l2 >= 1
    receivers = [(d - j, j) for d in degs for j in range(0, d)]  # (k1, l1), k1 >= 1
    ok30, brk_z, brk_p = True, False, False
    nz_l2: dict[str, int] = {}
    nz_l1: dict[str, int] = {}
    for fam in ("g", "O", "Op"):
        nz_l2[fam], nz_l1[fam] = 0, 0
        for k2, l2 in supplying:
            ok, nz = freed_strand(M, fam, k2, l2)
            ok30 = ok30 and ok
            if l2 >= 2:
                nz_l2[fam] += nz
            # Z^F, the freed strand as an odd superfield (one-output member of F)
            Zd = apply(
                M, raise_family(M, k2 + l2 - 1, 1, fam), [q] * (l2 - 1) + [p] * k2
            )
            Z = [Zd.get((c,), {}) for c in range(N)]
            for k1, l1 in receivers:
                if l1 < 2 and l2 < 2:
                    continue
                lhs, rhs = receiving(M, fam, k1, l1, Z)
                if sub(M, lhs, rhs):
                    ok30 = False
                if l1 >= 2 and rhs:
                    nz_l1[fam] += 1
                # break leg: receiving member of the sprod family read in the Omega form
                if fam == "O" and l1 >= 1 and not brk_p:
                    lb, _ = receiving(M, fam, k1, l1, Z, pfam="g")
                    if sub(M, lb, rhs):
                        brk_p = True
    # break leg: the strand of the sprod family read in the Omega form
    for k2, l2 in supplying:
        if not freed_strand(M, "O", k2, l2, zfam="g")[0]:
            brk_z = True
    nonh30 = all(nz_l2[f] > 0 and nz_l1[f] > 0 for f in nz_l2)
    check(
        "C3.0",
        ok30 and nonh30,
        "(088.9) both sides, F in {sprod, Omega, Omega'}: freed strand of the l2-output"
        " member = one-output member = V; receiving member on the odd Z^F = V;"
        f" nonzero V with l2 >= 2: {nz_l2}, with l1 >= 2: {nz_l1}",
    )
    check(
        "C3.0-break",
        brk_z and brk_p,
        "sprod strand or sprod receiving member in the Omega form fails (expected)",
    )

    # ---------------- C3: relations, generic data (not satisfying the master equation)
    E = polarized(M)
    ok31, ok31p, okb, ok32, nonh, drop_breaks = True, True, False, True, True, True
    info = []
    for m, n in bidegrees(M):
        Emn = gap7.bideg(E, N, m, n)
        RO, nt = relation(M, "O", m, n)
        ROp, _ = relation(M, "Op", m, n)
        Rg, ntg = relation(M, "g", m, n)
        info.append(f"({m},{n}):|E|={gap7.size(Emn)},terms={nt}")
        if M.ga.add(RO, Emn):
            ok31 = False
        if sub(M, ROp, Emn):
            ok31p = False
        if Emn and sub(M, RO, Emn):
            okb = True
        if Rg:
            ok32 = False
        # every configuration that is not its own mirror gives a nonzero Delta-term;
        # a self-mirror one vanishes alone (only configuration at (0,2), (2,0), ...)
        if Emn and nt >= 2 and ntg < 2:
            nonh = False
        if Emn and nt == 1 and ntg != 0:
            nonh = False
        if ntg >= 2:
            Rd, _ = relation(M, "g", m, n, drop_one=True)
            if not Rd:
                drop_breaks = False
    print("   ", " ".join(info))
    check("C3.1", ok31, "R^Omega_{m,n} == -E_{m,n} at every bidegree (generic data)")
    check("C3.1-prime", ok31p, "R^Omega'_{m,n} == +E_{m,n} at every bidegree")
    check("C3.1-break", okb, "R^Omega == +E fails where E != 0 (expected)")
    check(
        "C3.2",
        ok32 and nonh,
        "R^sprod_{m,n} == 0 identically (plain composition, Delta on the strand);"
        " >= 2 nonzero terms where E has >= 2, the lone self-mirror term vanishes",
    )
    check("C3.2-break", drop_breaks, "dropping one term of R^sprod leaves it nonzero")
    Su = M.S("u")
    Ed = M.contract(Su, Su, plain=True)
    check(
        "C3.2-delta",
        not Ed and bool(E),
        "polarized master equation contracted with Delta = g^{-1}: identically 0,"
        f" all bidegrees (with Omega^{{-1}}: |E| = {gap7.size(E)})",
    )

    # ---------------- C3.3: cyclic dg Lie and a Jacobi-violating variant
    S2 = gap7.lie_model(gap7.SL2, 3)
    bad = gap7.structure({(2, 0): {0: 2}, (2, 1): {1: -3}, (0, 1): {2: 1}}, 3)
    B2 = gap7.lie_model(bad, 3)
    res = {}
    for name, Mod in (("sl2", S2), ("bad", B2)):
        Em = polarized(Mod)
        RO = {}
        Rg = {}
        for m, n in bidegrees(Mod):
            RO = Mod.ga.add(RO, relation(Mod, "O", m, n)[0])
            Rg = Mod.ga.add(Rg, relation(Mod, "g", m, n)[0])
        res[name] = (Em, RO, Rg, Mod)
    Em, RO, Rg, _ = res["sl2"]
    Eb, ROb, Rgb, Bm = res["bad"]
    check(
        "C3.3",
        not Em
        and not RO
        and not Rg
        and Eb
        and ROb
        and not Bm.ga.add(ROb, Eb)
        and not Rgb,
        f"sl2: E = R^O = 0; Jacobi-violating: |E| = {gap7.size(Eb)}, R^O = -E,"
        " R^sprod = 0 on both",
    )

    n_fail = sum(1 for _, ok in RESULTS if not ok)
    print(f"summary: {len(RESULTS) - n_fail}/{len(RESULTS)} PASS (seed {SEED})")
    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(main())
