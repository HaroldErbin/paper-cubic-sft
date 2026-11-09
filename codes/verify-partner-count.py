#!/usr/bin/env python3
"""verify-partner-count.py – companion of agent/derivations/101-partner-count.md.

What is verified.

C0-trees-<D>: the catalogue of whole-slot tree structures (038 §3.2 lemma) of
    degree D = 8, 9, 10 (orders g^6, g^7, g^8): nodes are elementary vertices V_n
    with internal slots (lines of strand 2, 3, 4 = p_{2,2}^{-1}, p_{3,3}^{-1},
    p_{4,4}^{-1}) and external Psi strands, modulo the Veronese/kinetic
    collapses, with the admissibility rules of the record (block A).  The script
    enumerates them and prints, per degree, the number of structures and the
    number with no strand-2 line (the ones no Upsilon_2 coupling can reach).
    The corrected hand count of the record for D = 8 (9 structures, 2 without a
    strand-2 line, the contact included) is asserted; D = 9, 10 are recorded
    from this output.
C1-J-coefficient: in the Sigma_3 sector alone (Sigma_2 frozen at Psi^2), with
    the septic couplings a7 V7(Sigma_3^2, Psi) + b7 V7(Sigma_3, Sigma_2^2),
    the g^6 term of the eliminated action is
        (2 a7 + b7)^2 / (4 * 7 * 7!) * V7(Psi^4, p33^{-1} V7(Psi^4, .)),
    tested on random symmetric tensors (N = 3) for four (a7, b7) pairs, with a
    break test (wrong prefactor must FAIL).
C2-square-9, C3-square-10: the completed-square combinations at V9 and V10 have
    no term linear in the deviation of the heaviest field at the Veronese
    point (Veronese identities on random tensors), while the naive partition
    does.

What is NOT verified: the full O(g^6), O(g^7), O(g^8) deficit of the partner
scheme (coefficients of every structure) – a second step (record 101, "What is
missing").
"""

from __future__ import annotations

import itertools
import math
import sys

import numpy as np

SEED = 20261018
rng = np.random.default_rng(SEED)
print(f"seed = {SEED}")
results: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, info: str = "") -> None:
    results.append((name, ok, info))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {info}")


# ----------------------------------------------------------------------------
# C0: tree catalogue
# ----------------------------------------------------------------------------
# A tree: nodes 0..k-1, edges (i, j, s) with strand s in {2, 3, 4}, externals e_i.
# Node admissibility (record block A, rules N1-N4):
#  N1 n_i = sum of incident strands + e_i >= 3 (a vertex V_n, n >= 3);
#  N2 no collapse: not (one line of strand s and e = s) [Veronese source],
#     not (exactly two lines, equal strands s, e = 0) [kinetic];
#  N3 n_i >= 2 s for every incident strand s (an auxiliary of strand s does not
#     appear below its kinetic order; kills the mixings V5(.2,.3), V7(.3,.4));
#  N4 cubic realisability: m internal slots (m <= 3) and the e externals grouped
#     into <= 3 - m Veronese slots of strand <= smax (3, or 4 with Sigma_4).


def labeled_trees(k: int):
    """All labeled trees on k nodes as edge lists (Pruefer)."""
    if k == 1:
        yield []
        return
    if k == 2:
        yield [(0, 1)]
        return
    for seq in itertools.product(range(k), repeat=k - 2):
        degree = [1] * k
        for x in seq:
            degree[x] += 1
        edges = []
        s = list(seq)
        for x in s:
            for leaf in range(k):
                if degree[leaf] == 1:
                    edges.append((leaf, x))
                    degree[leaf] -= 1
                    degree[x] -= 1
                    break
        u, v = [i for i in range(k) if degree[i] == 1]
        edges.append((u, v))
        yield edges


def canon(k: int, edges, ext) -> str:
    """Canonical string of a tree with edge labels and node labels (AHU)."""
    adj = {i: [] for i in range(k)}
    for i, j, s in edges:
        adj[i].append((j, s))
        adj[j].append((i, s))

    def enc(v, parent, s_in):
        subs = sorted(enc(w, v, s) for w, s in adj[v] if w != parent)
        return f"({s_in}:{ext[v]}" + "".join(subs) + ")"

    return min(enc(r, -1, 0) for r in range(k))


def shapes(k: int):
    """Unlabeled trees on k nodes (one labeled representative each)."""
    seen = {}
    for edges in labeled_trees(k):
        key = canon(k, [(i, j, 0) for i, j in edges], [0] * k)
        seen.setdefault(key, edges)
    return list(seen.values())


def ext_options(inc: list[int], smax: int) -> list[int]:
    """Admissible external counts of a node with incident strands `inc`."""
    m = len(inc)
    if m > 3:
        return []
    opts = []
    for e in range(0, (3 - m) * smax + 1):
        n = sum(inc) + e
        if n < 3 or any(n < 2 * s for s in inc):
            continue
        if m == 1 and e == inc[0]:
            continue
        if m == 2 and inc[0] == inc[1] and e == 0:
            continue
        opts.append(e)
    return opts


def catalogue(D: int, smax: int, strands=(2, 3, 4)):
    found = {}
    for k in range(1, 7):
        for shape in shapes(k):
            for strs in itertools.product(strands, repeat=len(shape)):
                edges = [(i, j, s) for (i, j), s in zip(shape, strs)]
                opts = []
                for i in range(k):
                    inc = [s for a, b, s in edges if i in (a, b)]
                    opts.append(ext_options(inc, smax))
                if any(not o for o in opts):
                    continue
                # externals sum to D (degree = number of external Psi strands)
                for ext in itertools.product(*opts):
                    if sum(ext) != D:
                        continue
                    key = canon(k, edges, list(ext))
                    if key not in found:
                        found[key] = (k, edges, list(ext))
    return found


def describe(k, edges, ext) -> str:
    nodes = []
    for i in range(k):
        inc = sorted(s for a, b, s in edges if i in (a, b))
        nodes.append(f"V{sum(inc) + ext[i]}({','.join(map(str, inc))}|{ext[i]})")
    return " ".join(nodes)


for D, smax in ((8, 3), (9, 3), (10, 4)):
    cat = catalogue(D, smax)
    no2 = [v for v in cat.values() if all(s != 2 for _, _, s in v[1])]
    with4 = [v for v in cat.values() if any(s == 4 for _, _, s in v[1])]
    print(
        f"-- degree {D} (order g^{D - 2}), smax = {smax}: {len(cat)} structures, "
        f"{len(no2)} without a strand-2 line, {len(with4)} with a strand-4 line"
    )
    for v in sorted(cat.values(), key=lambda t: (t[0], describe(*t))):
        print("   ", describe(*v))
    if D == 8:
        # hand count of record 101 block A after correction: 9 structures (the
        # first hand pass missed the chain v W W v), 2 without a strand-2 line
        # (the contact and the Sigma_3 exchange J)
        check(
            "C0-trees-8",
            len(cat) == 9 and len(no2) == 2,
            f"({len(cat)} structures, {len(no2)} without strand-2 line; hand count 9, 2)",
        )
    else:
        # rule N2 counts of step 1 (superseded by N2'/N2'' for the catalogue:
        # 14 at D = 9, 36 at D = 10, verify-partner-closure.py C0-trees-9/10 and
        # verify-partner-octic.py); asserted so that a change of N1-N4 is caught
        expect = {9: (22, 3, 0), 10: (77, 9, 10)}[D]  # no2 includes the contact
        check(
            f"C0-trees-{D}",
            (len(cat), len(no2), len(with4)) == expect,
            f"({len(cat)} structures, {len(no2)} without strand-2 line, "
            f"{len(with4)} with a strand-4 line; rule N2 of step 1, expected {expect})",
        )
    # Sigma_4 absent: realisability with smax = 3 only
    if D == 10:
        cat3 = catalogue(D, 3)
        check(
            "C0-trees-10-nosigma4",
            len(cat3) == 74,
            f"({len(cat3)} structures without Sigma_4 slots; rule N2, expected 74)",
        )

# ----------------------------------------------------------------------------
# Tensor model
# ----------------------------------------------------------------------------
N = 3


def sym_tensor(k: int) -> np.ndarray:
    t = rng.standard_normal((N,) * k)
    out = np.zeros_like(t)
    perms = list(itertools.permutations(range(k)))
    for p in perms:
        out += np.transpose(t, p)
    return out / len(perms)


V6, V7, V8, V9, V10 = (sym_tensor(k) for k in (6, 7, 8, 9, 10))
Psi = rng.standard_normal(N)
P = np.einsum("i,j->ij", Psi, Psi)
p3 = np.einsum("i,j,k->ijk", Psi, Psi, Psi)
p4 = np.einsum("i,j,k,l->ijkl", Psi, Psi, Psi, Psi)

# symmetric basis of Sym^3(R^N)
idx3 = [c for c in itertools.combinations_with_replacement(range(N), 3)]
B3 = []
for c in idx3:
    t = np.zeros((N,) * 3)
    for p in set(itertools.permutations(c)):
        t[p] = 1.0
    B3.append(t / np.sqrt(len(set(itertools.permutations(c)))))
B3 = np.array(B3)  # (10, N, N, N)


def to_sym3(x: np.ndarray) -> np.ndarray:
    return np.einsum("a,aijk->ijk", x, B3)


# ----------------------------------------------------------------------------
# C1: Sigma_3-sector elimination, g^6 coefficient
# ----------------------------------------------------------------------------
def S_sigma3_sector(g: complex, a7: float, b7: float) -> complex:
    """-g^4/6! V6(S3,S3) + 2 g^4/6! V6(S3,P,Psi) + g^5/7! [a7 V7(S3,S3,Psi) + b7 V7(S3,P,P)],
    eliminated exactly (quadratic in S3), in the Sym^3 basis."""
    M = np.einsum("aijk,bmno,ijkmno->ab", B3, B3, V6)
    W7 = np.einsum("aijk,bmno,ijkmnop,p->ab", B3, B3, V7, Psi)
    src6 = np.einsum("aijk,ijkmno,mn,o->a", B3, V6, P, Psi)
    src7 = np.einsum("aijk,ijkmnop,mn,op->a", B3, V7, P, P)
    K = -(g**4) / math.factorial(6) * M + g**5 / math.factorial(7) * a7 * W7
    J = 2 * g**4 / math.factorial(6) * src6 + g**5 / math.factorial(7) * b7 * src7
    # S = x K x + J x, stationary at x* = -K^{-1} J / 2, value -J K^{-1} J / 4
    x = np.linalg.solve(K, -J / 2)
    return x @ K @ x + J @ x


def taylor_coeff(f, order: int, r: float = 0.2, K: int = 24) -> complex:
    vals = [f(r * np.exp(2j * np.pi * k / K)) for k in range(K)]
    return sum(v * np.exp(-2j * np.pi * k * order / K) for k, v in enumerate(vals)) / (
        K * r**order
    )


M3 = np.einsum("aijk,bmno,ijkmno->ab", B3, B3, V6)
u7 = np.einsum("aijk,ijkmnop,m,n,o,p->a", B3, V7, Psi, Psi, Psi, Psi)
Jstruct = u7 @ np.linalg.solve(M3, u7)  # V7(Psi^4, p33^{-1} V7(Psi^4, .))
V6c = np.einsum("ijkmno,i,j,k,m,n,o", V6, *([Psi] * 6))
V7c = np.einsum("ijkmnop,i,j,k,m,n,o,p", V7, *([Psi] * 7))

allok = True
for a7, b7 in ((1.0, 0.0), (0.0, 1.0), (-1.0, 2.0), (0.5, 0.5)):
    f = lambda g, a7=a7, b7=b7: S_sigma3_sector(g, a7, b7)
    c4 = taylor_coeff(f, 4)
    c5 = taylor_coeff(f, 5)
    c6 = taylor_coeff(f, 6)
    pred = (2 * a7 + b7) ** 2 / (4 * 7 * math.factorial(7)) * Jstruct
    ok4 = abs(c4 - V6c / math.factorial(6)) < 1e-9 * max(1, abs(V6c))
    ok5 = abs(c5 - (a7 + b7) * V7c / math.factorial(7)) < 1e-9 * max(1, abs(V7c))
    ok6 = abs(c6 - pred) < 1e-8 * max(1, abs(Jstruct) / 7 / math.factorial(7))
    allok &= ok4 and ok5 and ok6
    print(
        f"    (a7,b7)=({a7},{b7}): g^6 coeff {c6.real:+.6e}, predicted {pred:+.6e}, "
        f"contact checks {ok4}, {ok5}"
    )
check(
    "C1-J-coefficient",
    bool(allok),
    "(g^6 term of the Sigma_3-sector elimination = (2a7+b7)^2/(4*7*7!) * J, 4 pairs)",
)
# break test: a wrong prefactor (1/(7*7!) at (0,1) instead of 1/(4*7*7!)) must fail
c6_01 = taylor_coeff(lambda g: S_sigma3_sector(g, 0.0, 1.0), 6)
wrong = 1.0 / (7 * math.factorial(7)) * Jstruct
check(
    "C1-J-coefficient-break",
    abs(c6_01 - wrong) > 1e-6 * abs(wrong),
    "(perturbed prefactor is rejected)",
)

# ----------------------------------------------------------------------------
# C2, C3: completed squares at V9 and V10 (Veronese identities)
# ----------------------------------------------------------------------------
# V9: -V9(S4,S4,Psi) + 2 V9(S4,S3,S2): gradient wrt S4 at (p4,p3,P) vanishes.
g4_naive = np.einsum(
    "ijklmnopq,m,n,o,p,q->ijkl", V9, *([Psi] * 5)
)  # from V9(S4,S4,Psi) alone
g4_sq = -2 * np.einsum("ijklmnopq,mnop,q->ijkl", V9, p4, Psi) + 2 * np.einsum(
    "ijklmnopq,mno,pq->ijkl", V9, p3, P
)
check(
    "C2-square-9",
    np.max(np.abs(g4_sq)) < 1e-12 * np.max(np.abs(g4_naive))
    and np.max(np.abs(g4_naive)) > 1e-6,
    "(-V9(S4^2,Psi)+2V9(S4,S3,S2): no term linear in the Sigma_4 deviation; "
    "V9(S4^2,Psi) alone has one)",
)
# but the same combination sources the Sigma_3 deviation: 2 V9(p4, ., P) != 0
g3_sq = 2 * np.einsum("ijklmnopq,ijkl,pq->mno", V9, p4, P)
check(
    "C2-square-9-sigma3-source",
    np.max(np.abs(g3_sq)) > 1e-6,
    "(the completed square at V9 still sources the Sigma_3 deviation)",
)
# V10: -V10(S4,S4,S2) + 2 V10(S4,S3,S3): no Sigma_4-linear term; and the
# alternative -V10(S5,S5)+2V10(S5,S3,S2) is the HS pair of a Sigma_5.
g4_10 = -2 * np.einsum("ijklmnopqr,mnop,qr->ijkl", V10, p4, P) + 2 * np.einsum(
    "ijklmnopqr,mno,pqr->ijkl", V10, p3, p3
)
g4_10_naive = np.einsum("ijklmnopqr,mnop,qr->ijkl", V10, p4, P)
check(
    "C3-square-10",
    np.max(np.abs(g4_10)) < 1e-12 * np.max(np.abs(g4_10_naive))
    and np.max(np.abs(g4_10_naive)) > 1e-6,
    "(-V10(S4^2,S2)+2V10(S4,S3^2): no term linear in the Sigma_4 deviation)",
)
# break: a wrong relative coefficient must leave a linear term
g4_10_bad = -2 * np.einsum("ijklmnopqr,mnop,qr->ijkl", V10, p4, P) + 1 * np.einsum(
    "ijklmnopqr,mno,pqr->ijkl", V10, p3, p3
)
check(
    "C3-square-10-break",
    np.max(np.abs(g4_10_bad)) > 1e-6,
    "(coefficient 1 instead of 2 leaves a linear term)",
)

# ----------------------------------------------------------------------------
nfail = sum(1 for _, ok, _ in results if not ok)
print(f"\n{len(results) - nfail}/{len(results)} checks PASS")
sys.exit(1 if nfail else 0)
