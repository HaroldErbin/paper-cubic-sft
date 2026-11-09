"""
Companion script for derivation record 083 (extensions of the PH31 rank test, R84).

Imports, unchanged, the engine of codes/verify-ph31-rank.py (record 078: Neumann
and ghost data of R2's V_3', Fock bases, amplitudes, exact ranks over F_p,
p = 2^31 - 1) and adds:

- a sparse exact count of the relations on W^even_{<=K} implied by the two
  conservation identities of record 078 (4.3),
      (b_1^- - z^2 b_{-1}^-) Phi_2 = 0 on ker b_0^-,
      (L_1^- - z^2 L_{-1}^-) Phi_2 = 0 on ker L_0^-,
  written as exact vectors over leg-0 monomials (chi of level <= kchi, every
  zero-mode sector), eliminated with the coordinates outside W^even_{<=K}
  ordered first; the relations are the echelon vectors whose leading
  coordinate lies inside W^even_{<=K}. Returned as vectors over the row basis
  of the scan, so that they can be applied to the measured image.
- the new rows of the rank table: d_eff = 3 at K = L = 2 (alpha'_v = 0);
  alpha'_v = 1/4 and -1/2 at K <= 3, L <= 2; K = 3, L = 3 at alpha'_v = 0
  (all L <= 2 pairs, then random pairs with a level-3 input, two Delta).

Named checks (PASS/FAIL), node IDs of record 083:
- E0-engine-K2: the sparse relation count reproduces record 078's dense
  identity_relations at K = 2, d = 2 (5), with and without the parity filter.
- E3-count-d3: block dimensions at d = 3 from the Fock enumeration equal the
  generating function (independent route).
- E3-rank-d3, E3-identities-d3, E3-relations-d3, E3-annihilate-d3,
  BREAK-relations-d3: rank at d = 3; (4.3) functionals vanish on H_0 columns;
  identity relation count against the measured deficit; the relations
  annihilate the measured image (sign-flipped z^2: they do not).
- E2-admissible: 032's non-overlap conditions at the two new alpha'_v.
- E2-alpha-<a>-K<K>: full rank at alpha'_v = 1/4, -1/2.
- E1-relations-K3, E1-annihilate-K3, E1-K3-L3, BREAK-relations-K3: the
  K = 3 relation count and the closure of the [34, 60] bracket.
- E3-split-d3, E1-split-K3: rank of the stacked b-alone and L-alone relations
  (gives the mixed-only count) and their containment in the joint span.
- E-exact-b-K3-d2: the b-alone count at K = 3 over Q (P-independent: holds at
  every P), against the F_p count.
- E-exact-K<K>-d<d>: at a rational momentum P_q the relations are computed
  over Q (exact at P_q for every Delta and every input level) and the mod-p
  scan at P_q bounds the rank over Q(Delta) from below: relations + rank = dim.

Not verified: unbounded level; the generic-P upper bound on the rank beyond
the genericity of the sampled point (record 083 section 4 item 3); saturation
of the relation count in the chi level; d_eff = 26; beta other than 3/2; vertex
points other than those listed. Each rank over F_p is a lower bound on the
generic rank over Q; exactness over Q follows only where an exact relation
count meets the mod-p deficit (record 078 section 3; record 083 section 4).
"""

from __future__ import annotations

import importlib.util
import json
import random
import sys
import time
from fractions import Fraction
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location(
    "v078", ROOT / "codes/verify-ph31-rank.py"
)
v = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(v)

PMOD = v.PMOD
SCRATCH = ROOT / "codes" / "output" / "ph31-rank-ext"
RESULTS: list[tuple[str, bool, str]] = []
OUT: dict = {}
TAG = "-".join(sys.argv[1:]) or "all"


def report(name: str, ok: bool, detail: str = "") -> None:
    RESULTS.append((name, ok, detail))
    print(f"{'PASS' if ok else 'FAIL'}  {name}: {detail}", flush=True)
    SCRATCH.mkdir(parents=True, exist_ok=True)
    (SCRATCH / f"checks-{TAG}.json").write_text(json.dumps(RESULTS, indent=1))
    (SCRATCH / f"results-{TAG}.json").write_text(json.dumps(OUT, indent=1, default=str))


def even_rows(K: int, d: int) -> list[dict]:
    return [
        st for st in v.closed_basis(K, d, 0, False) if (st["N"] - st["Nb"]) % 2 == 0
    ]


# ------------------------------------------------------------------ the scan
def scan(  # noqa: PLR0913
    amps,
    K: int,
    L: int,
    d: int,
    rng: random.Random,
    P: tuple,
    max_delta: int = 6,
    ech=None,
    pair_filter=None,
    cap: int | None = None,
    tag: str = "",
) -> tuple:
    """Joint rank over Delta samples (record 078 run_entry, returning the echelon).

    pair_filter(i, j) restricts the ordered input pairs; cap limits the number
    of (random) pairs per Delta sample. Stops when a sample adds nothing.
    """
    rows = even_rows(K, d)
    rstr = [v.state_strings(st) for st in rows]
    ins = v.input_basis(L, d)
    istr = [v.state_strings(st, z) for st, z in ins]
    ech = ech if ech is not None else v.Echelon(len(rows))
    inv2 = pow(2, PMOD - 2, PMOD)
    hist, ncols, t0 = [], 0, time.time()
    for it in range(max_delta):
        D = tuple(rng.randrange(PMOD) for _ in range(d))
        l1 = tuple((p * inv2 + x) % PMOD for p, x in zip(P, D))
        l2 = tuple((p * inv2 - x) % PMOD for p, x in zip(P, D))
        pairs = [
            (i, j)
            for i in range(len(ins))
            for j in range(len(ins))
            if pair_filter is None or pair_filter(ins[i], ins[j])
        ]
        rng.shuffle(pairs)
        if cap is not None:
            pairs = pairs[:cap]
        added = 0
        for i, j in pairs:
            col = np.array(
                [
                    (
                        amps.amp(B, istr[i], istr[j], l1, l2)
                        + amps.amp(B, istr[j], istr[i], l2, l1)
                    )
                    % PMOD
                    for B in rstr
                ],
                dtype=np.int64,
            )
            ncols += 1
            added += ech.add(col)
            if ech.rank == len(rows):
                break
        hist.append(ech.rank)
        print(
            f"  [{tag}] K={K} L={L} d={d} sample {it}: rank {ech.rank}/{len(rows)}"
            f" (+{added}, {len(pairs)} pairs) t={time.time() - t0:.1f}s",
            flush=True,
        )
        if ech.rank == len(rows) or (it >= 1 and added == 0):
            break
    blocks = sorted({(st["N"], st["Nb"]) for st in rows})
    basis = list(ech.piv.values())
    per_block = {}
    for blk in blocks:
        idx = [k for k, st in enumerate(rows) if (st["N"], st["Nb"]) == blk]
        per_block[f"{blk[0]},{blk[1]}"] = (
            v.rank_modp([b[idx] for b in basis]) if basis else 0,
            len(idx),
        )
    info = {
        "K": K,
        "L": L,
        "d": d,
        "rows_even": len(rows),
        "inputs": len(ins),
        "columns_used": ncols,
        "n_delta": len(hist),
        "rank_history": hist,
        "rank": ech.rank,
        "deficit": len(rows) - ech.rank,
        "per_block": per_block,
        "time_s": round(time.time() - t0, 1),
    }
    return ech, rows, info


# ------------------------------------------------- identity relations (sparse)
def identity_functionals(  # noqa: PLR0913
    vx,
    d: int,
    P: tuple,
    kchi: int,
    sgn: int = -1,
    parity: bool = True,
    kinds: str = "bL",
):
    """b- and L-functionals of record 078 (4.3) as dicts over canonical leg-0 monomials.

    sgn = -1 is (4.3); sgn = +1 flips the sign of the z^2 terms (break leg).
    parity = True keeps only chi with N - Nbar odd: their images lie on even rows;
    the others have images on odd rows only, disjoint coordinates, no relation.
    """
    z2 = Fraction(str(vx.z[1])) ** 2
    ell0 = tuple((-p) % PMOD for p in P)
    funcs = []
    for z in v.ZPREF:
        for st in (
            v.closed_basis(kchi, d, 1 - len(v.ZPREF[z]), False) if "b" in kinds else []
        ):
            if parity and (st["N"] - st["Nb"]) % 2 == 0:
                continue
            base = v.ZPREF[z] + st["gh"] + ((0, "c", 1), (1, "c", 1))
            strings = []
            for cf, op in (
                (1, (0, "b", -1)),
                (sgn * z2, (0, "b", 1)),
                (-1, (1, "b", -1)),
                (-sgn * z2, (1, "b", 1)),
            ):
                for s2, o in v.reduce_on_vacuum((op,) + base):
                    strings.append((v.fmod(Fraction(cf) * s2), st["mat"], o))
            funcs.append(strings)
        for st in (
            v.closed_basis(kchi, d, -len(v.ZPREF[z]), False) if "L" in kinds else []
        ):
            if parity and (st["N"] - st["Nb"]) % 2 == 0:
                continue
            base = v.ZPREF[z] + st["gh"] + ((0, "c", 1), (1, "c", 1))
            strings = []
            for cf, (n, ch) in (
                (1, (-1, 0)),
                (sgn * z2, (1, 0)),
                (-1, (-1, 1)),
                (-sgn * z2, (1, 1)),
            ):
                for s2, o in v.reduce_on_vacuum(base):
                    strings += v.apply_L(
                        n, ch, Fraction(cf) * s2, st["mat"], o, ell0, kchi + 1
                    )
            funcs.append(strings)
    vecs = []
    for strings in funcs:
        vec: dict = {}
        for cf, m, g in strings:
            cg = v.canon(g)
            if cg is None:
                continue
            key = (tuple(sorted(m)), cg[1])
            vec[key] = (vec.get(key, 0) + cf * cg[0]) % PMOD
        vec = {k: c for k, c in vec.items() if c}
        if vec:
            vecs.append(vec)
    return vecs


def sparse_relations(vecs: list[dict], K: int, exact: bool = False) -> list[dict]:
    """Echelon over F_p, coordinates outside W^even_{<=K} ordered first.

    Returns the echelon vectors whose leading coordinate lies inside
    W^even_{<=K}: a basis of span(vecs) cap (vectors supported on W^even_{<=K}).
    """

    def inside(key) -> bool:
        m, g = key
        if any(op[2] == 0 for op in g):
            return False
        a, b = v.string_levels(m, g)
        return a <= K and b <= K and (a - b) % 2 == 0

    order: dict = {}

    def rank_key(k):
        if k not in order:
            order[k] = (1 if inside(k) else 0, len(order))
        return order[k]

    piv: dict = {}
    for vec in vecs:
        w = dict(vec)
        while w:
            lead = min(w, key=rank_key)
            if lead in piv:
                c = w[lead]
                for k, x in piv[lead].items():
                    y = w.get(k, 0) - c * x
                    y = y if exact else y % PMOD
                    if y:
                        w[k] = y
                    else:
                        w.pop(k, None)
            else:
                if exact:
                    inv = 1 / Fraction(w[lead])
                    piv[lead] = {k: x * inv for k, x in w.items()}
                else:
                    inv = pow(w[lead], PMOD - 2, PMOD)
                    piv[lead] = {k: x * inv % PMOD for k, x in w.items()}
                break
    return [p for lead, p in piv.items() if rank_key(lead)[0] == 1]


# ------------------------------------------- exact count over Q at a rational P
def apply_L_Q(
    n: int, ch: int, cf: Fraction, mat: tuple, gh: tuple, ell0: tuple, kmax: int
) -> list:
    """Copy of record 078's apply_L over Q (no reduction mod p); ell0 rational."""
    out = []
    d = len(ell0)

    def lower(mt, mu, m):
        k = sum(1 for x in mt if x == (ch, mu, m))
        if not k:
            return []
        lst = list(mt)
        lst.remove((ch, mu, m))
        return [(k * m, tuple(lst))]

    for mu in range(d):
        for m in range(-kmax - 2, kmax + 3):
            k = n - m
            if k > m:
                continue
            fac = Fraction(1, 2) if k == m else Fraction(1)
            stage = [(Fraction(1), mat)]
            for mode in (m, k):
                new = []
                for c0, mt in stage:
                    if mode > 0:
                        new += [(c0 * a, t) for a, t in lower(mt, mu, mode)]
                    elif mode == 0:
                        new.append((c0 * ell0[mu], mt))
                    else:
                        new.append((c0, tuple(sorted(mt + ((ch, mu, -mode),)))))
                stage = new
            for c0, mt in stage:
                out.append((cf * fac * c0, mt, gh))
    for m in range(-kmax - 3, kmax + 4):
        if n + m == 0:
            continue
        for s2, o in v.reduce_on_vacuum(((ch, "b", n - m), (ch, "c", m)) + gh):
            out.append((cf * (n + m) * s2, mat, o))
    return [x for x in out if x[0]]


def relations_Q(  # noqa: PLR0913
    vx, d: int, Pq: tuple, K: int, kchi: int, kinds: str = "bL"
) -> list[dict]:
    """b- and L-relations on W^even_{<=K} over Q at the rational momentum Pq (chi odd N - Nbar)."""
    z2 = Fraction(str(vx.z[1])) ** 2
    ell0 = tuple(-p for p in Pq)
    funcs = []
    for z in v.ZPREF:
        for st in (
            v.closed_basis(kchi, d, 1 - len(v.ZPREF[z]), False) if "b" in kinds else []
        ):
            if (st["N"] - st["Nb"]) % 2 == 0:
                continue
            base = v.ZPREF[z] + st["gh"] + ((0, "c", 1), (1, "c", 1))
            strings = []
            for cf, op in (
                (1, (0, "b", -1)),
                (-z2, (0, "b", 1)),
                (-1, (1, "b", -1)),
                (z2, (1, "b", 1)),
            ):
                for s2, o in v.reduce_on_vacuum((op,) + base):
                    strings.append((Fraction(cf) * s2, st["mat"], o))
            funcs.append(strings)
        for st in (
            v.closed_basis(kchi, d, -len(v.ZPREF[z]), False) if "L" in kinds else []
        ):
            if (st["N"] - st["Nb"]) % 2 == 0:
                continue
            base = v.ZPREF[z] + st["gh"] + ((0, "c", 1), (1, "c", 1))
            strings = []
            for cf, (n, ch) in (
                (1, (-1, 0)),
                (-z2, (1, 0)),
                (-1, (-1, 1)),
                (z2, (1, 1)),
            ):
                for s2, o in v.reduce_on_vacuum(base):
                    strings += apply_L_Q(
                        n, ch, Fraction(cf) * s2, st["mat"], o, ell0, kchi + 1
                    )
            funcs.append(strings)
    vecs = []
    for strings in funcs:
        vec: dict = {}
        for cf, m, g in strings:
            cg = v.canon(g)
            if cg is None:
                continue
            key = (tuple(sorted(m)), cg[1])
            vec[key] = vec.get(key, 0) + cf * cg[0]
        vec = {k: c for k, c in vec.items() if c}
        if vec:
            vecs.append(vec)
    return sparse_relations(vecs, K, exact=True)


def relations_on_rows(rels: list[dict], rows: list[dict]) -> np.ndarray:
    """Relation vectors as row vectors over the scan's row basis (sign of each monomial)."""
    pos = {}
    for r, st in enumerate(rows):
        ((s, mat, o),) = v.state_strings(st)
        cs, g = v.canon(o)
        pos[(tuple(sorted(mat)), g)] = (r, s * cs)
    out = np.zeros((len(rels), len(rows)), dtype=np.int64)
    for i, rel in enumerate(rels):
        for k, c in rel.items():
            r, s = pos[k]
            out[i, r] = (
                v.fmod(Fraction(s * c)) if isinstance(c, Fraction) else (s * c) % PMOD
            )
    return out


def annihilates(Y: np.ndarray, ech) -> int:
    """Number of non-zero pairings y . b over relation vectors y and echelon basis b."""
    if len(Y) == 0 or not ech.piv:
        return 0
    B = np.array(list(ech.piv.values()), dtype=object)
    prod = (np.asarray(Y, dtype=object) @ B.T) % PMOD
    return int(np.count_nonzero(prod))


def count(vx, d, P, K, kchi, sgn=-1, parity=True, kinds="bL"):  # noqa: PLR0913
    t0 = time.time()
    vecs = identity_functionals(vx, d, P, kchi, sgn, parity, kinds)
    rels = sparse_relations(vecs, K)
    return rels, len(vecs), round(time.time() - t0, 1)


def split_check(name: str, rels, rb, rl, rows) -> None:
    """Rank of the stacked b-alone and L-alone relations, and their containment in the joint span.

    mixed = (joint count) - rank(b-alone + L-alone); the split b/L/mixed presumes
    the b-alone and L-alone relations independent only if this rank equals
    len(rb) + len(rl). PASS requires containment: rank(joint + b + L) = joint.
    """
    Yj = list(relations_on_rows(rels, rows))
    Ybl = list(relations_on_rows(rb, rows)) + list(relations_on_rows(rl, rows))
    r_bl = v.rank_modp(Ybl) if Ybl else 0
    r_all = v.rank_modp(Yj + Ybl)
    OUT[name] = {"rank_b_plus_L": r_bl, "mixed": len(rels) - r_bl}
    report(
        name,
        r_all == len(rels),
        f"rank(b-alone {len(rb)} + L-alone {len(rl)}) = {r_bl}; rank(joint + b + L) = {r_all} "
        f"(joint {len(rels)}); mixed-only = {len(rels) - r_bl}",
    )


# ----------------------------------------------------------------------- main
def run_d3(rng: random.Random) -> None:
    """Item (iii): d_eff = 3 at K = L = 2, alpha'_v = 0."""
    d, K = 3, 2
    gf = v.gf_count(K, d)
    en: dict = {}
    for st in v.closed_basis(K, d, 0, False):
        en[(st["N"], st["Nb"])] = en.get((st["N"], st["Nb"]), 0) + 1
    dim = sum(c for (a, b), c in gf.items() if (a - b) % 2 == 0)
    OUT["d3_blocks"] = {f"{a},{b}": c for (a, b), c in sorted(gf.items())}
    report(
        "E3-count-d3",
        gf == en,
        f"d=3: dim W^even_<=2 = {dim}; blocks {OUT['d3_blocks']}",
    )
    vx = v.Vertex(Fraction(3, 2), 3, 0, 3)
    amps = v.Amplitudes(vx, d, v.Field(PMOD))
    P = tuple(rng.randrange(PMOD) for _ in range(d))
    ech, rows, info = scan(amps, K, 2, d, rng, P, tag="d3")
    OUT["d3_K2L2"] = info
    report(
        "E3-rank-d3",
        info["rows_even"] == dim
        and info["deficit"] == 5
        and all(r == n for r, n in info["per_block"].values()),
        f"rank {info['rank']}/{dim}, deficit {info['deficit']}, {info['columns_used']} columns, "
        f"{info['n_delta']} Delta, {info['time_s']} s; blocks {info['per_block']}",
    )
    nb, vb, _ = v.check_ob_identity(amps, vx, K, 2, d, rng, P, -1)
    nl, nzl = v.check_ol_vanish(amps, vx, K, 2, d, rng, P, -1)
    report(
        "E3-identities-d3",
        vb and nzl == 0,
        f"{nb} b-functionals vanish: {vb}; {nl} L-functionals, {nzl} non-zero values",
    )
    rels, nf, t = count(vx, d, P, K, K + 1)
    OUT["d3_relations"] = len(rels)
    report(
        "E3-relations-d3",
        len(rels) == info["deficit"],
        f"{len(rels)} relations ({nf} functionals, chi level <= 3, {t} s); measured deficit {info['deficit']}",
    )
    rb, _, _ = count(vx, d, P, K, K + 1, kinds="b")
    rl, _, _ = count(vx, d, P, K, K + 1, kinds="L")
    OUT["d3_split"] = {"b": len(rb), "L": len(rl), "both": len(rels)}
    print(
        f"  d=3 split: b alone {len(rb)}, L alone {len(rl)}, both {len(rels)}",
        flush=True,
    )
    Y = relations_on_rows(rels, rows)
    nz = annihilates(Y, ech)
    rk = v.rank_modp(list(Y)) if len(Y) else 0
    split_check("E3-split-d3", rels, rb, rl, rows)
    report(
        "E3-annihilate-d3",
        nz == 0 and rk == len(rels),
        f"relations x image basis: {nz} non-zero pairings; rank of relations {rk}",
    )
    relsB, _, _ = count(vx, d, P, K, K + 1, sgn=+1)
    nzB = annihilates(relations_on_rows(relsB, rows), ech) if relsB else 0
    report(
        "BREAK-relations-d3",
        nzB > 0,
        f"sign-flipped z^2: {len(relsB)} 'relations', {nzB} non-zero pairings with the image (must be > 0)",
    )


def run_alpha(rng: random.Random) -> None:
    """Item (ii): alpha'_v = 1/4, -1/2 at K <= 3, L <= 2 (gamma' = 3, beta = 3/2)."""
    g, bt = Fraction(3), Fraction(3, 2)
    ok, det = True, []
    for a in (Fraction(1, 4), Fraction(-1, 2)):
        # 032 (1.1): disc of f_0' = [-1/(g-a), 1/(g+a)], disc of f_1' at r=1 = [(2b-1)/(2b+1), (2b+1)/(2b-1)],
        # f_inf' = exterior of |z - a| >= g; non-overlap with strict inequalities
        lo1, hi1 = (2 * bt - 1) / (2 * bt + 1), (2 * bt + 1) / (2 * bt - 1)
        c0 = g - a > 0 and g + a > 0 and 1 / (g + a) < lo1
        c1 = a <= g - 1  # Harold's f_0'-f_inf' condition (032 (1.1))
        cinf = a - g < lo1 and hi1 < a + g
        ok &= c0 and c1 and cinf
        det.append(f"a={a}: {c0},{c1},{cinf}")
    report("E2-admissible", ok, "; ".join(det))
    for a in (Fraction(1, 4), Fraction(-1, 2)):
        vx = v.Vertex(bt, 3, a, 4)
        amps = v.Amplitudes(vx, 2, v.Field(PMOD))
        P = tuple(rng.randrange(PMOD) for _ in range(2))
        for K, L in ((1, 1), (2, 2), (3, 2)):
            _, _, info = scan(amps, K, L, 2, rng, P, max_delta=3, tag=f"a={a}")
            OUT[f"alpha_{a}_K{K}L{L}"] = info
            report(
                f"E2-alpha-{a}-K{K}",
                info["rank"] == info["rows_even"],
                f"alpha'_v={a}, K={K}, L={L}: rank {info['rank']}/{info['rows_even']}, "
                f"{info['columns_used']} columns, {info['n_delta']} Delta, {info['time_s']} s",
            )


def run_engine_check(rng: random.Random) -> None:
    vx = v.Vertex(Fraction(3, 2), 3, 0, 4)
    P = tuple(rng.randrange(PMOD) for _ in range(2))
    dense = v.identity_relations(vx, 2, 2, P, 3)
    r1, _, _ = count(vx, 2, P, 2, 3, parity=True)
    r2, _, _ = count(vx, 2, P, 2, 3, parity=False)
    report(
        "E0-engine-K2",
        dense == len(r1) == len(r2) == 5,
        f"dense 078 count {dense}; sparse {len(r1)} (parity filter), {len(r2)} (no filter)",
    )


def run_k3(rng: random.Random, kchi: int, l3_cap: int) -> None:
    """Item (i): K = 3 at alpha'_v = 0: relation count, L = 2 image, L = 3 extension."""
    d, K = 2, 3
    vx = v.Vertex(Fraction(3, 2), 3, 0, 4)
    amps = v.Amplitudes(vx, d, v.Field(PMOD))
    P = tuple(rng.randrange(PMOD) for _ in range(d))
    rels, nf, t = count(vx, d, P, K, kchi)
    OUT["K3_relations"] = {"n": len(rels), "functionals": nf, "kchi": kchi, "time_s": t}
    print(
        f"  K=3 relations: {len(rels)} from {nf} functionals (chi level <= {kchi}), {t} s",
        flush=True,
    )
    rb, _, _ = count(vx, d, P, K, kchi, kinds="b")
    rl, _, _ = count(vx, d, P, K, kchi, kinds="L")
    OUT["K3_split"] = {"b": len(rb), "L": len(rl), "both": len(rels)}
    print(
        f"  K=3 split: b alone {len(rb)}, L alone {len(rl)}, both {len(rels)}",
        flush=True,
    )
    ech, rows, info = scan(amps, K, 2, d, rng, P, max_delta=2, tag="K3L2")
    OUT["K3L2"] = info
    Y = relations_on_rows(rels, rows)
    nz = annihilates(Y, ech)
    split_check("E1-split-K3", rels, rb, rl, rows)
    report(
        "E1-relations-K3",
        nz == 0 and len(rels) + info["rank"] == info["rows_even"],
        f"{len(rels)} exact relations (chi level <= {kchi}); L=2 rank {info['rank']}/{info['rows_even']} mod p; "
        f"relations + rank = {len(rels) + info['rank']} = dim: bracket closed",
    )
    report(
        "E1-annihilate-K3",
        nz == 0,
        f"relations x L=2 image basis: {nz} non-zero pairings",
    )
    relsB, _, _ = count(vx, d, P, K, kchi, sgn=+1)
    nzB = annihilates(relations_on_rows(relsB, rows), ech) if relsB else 0
    report(
        "BREAK-relations-K3",
        nzB > 0,
        f"sign-flipped z^2: {len(relsB)} 'relations', {nzB} non-zero pairings (must be > 0)",
    )
    # L = 3: random pairs with at least one level-3 input, added to the L = 2 echelon
    r2 = ech.rank
    ech, rows, info3 = scan(
        amps,
        K,
        3,
        d,
        rng,
        P,
        max_delta=2,
        ech=ech,
        pair_filter=lambda a, b: a[0]["N"] == 3 or b[0]["N"] == 3,
        cap=l3_cap,
        tag="K3L3",
    )
    info3["rank_L2_start"] = r2
    OUT["K3L3"] = info3
    report(
        "E1-K3-L3",
        info3["rank"] == r2,
        f"after {info3['columns_used']} random level-3 pairs ({info3['n_delta']} Delta, {info3['time_s']} s): "
        f"rank {r2} -> {info3['rank']} (each level-3 column lies in the span the relations annihilate)",
    )


def run_rational(rng: random.Random) -> None:
    """Exact statement at a rational momentum P_q: relations over Q, rank lower bound mod p."""
    for K, d, M, kchi in ((2, 2, 3, 3), (2, 3, 3, 3), (3, 2, 4, 4)):
        Pq = tuple(Fraction(rng.randint(-50, 50), rng.randint(1, 7)) for _ in range(d))
        vx = v.Vertex(Fraction(3, 2), 3, 0, M)
        t0 = time.time()
        rels = relations_Q(vx, d, Pq, K, kchi)
        tq = round(time.time() - t0, 1)
        amps = v.Amplitudes(vx, d, v.Field(PMOD))
        P = tuple(v.fmod(p) for p in Pq)
        ech, rows, info = scan(
            amps, K, 2, d, rng, P, max_delta=1, tag=f"Pq K={K} d={d}"
        )
        nz = annihilates(relations_on_rows(rels, rows), ech)
        if K == 3:
            t1 = time.time()
            rb = relations_Q(vx, d, Pq, K, kchi, kinds="b")
            split = OUT.get("K3_split", {}).get("b")
            report(
                "E-exact-b-K3-d2",
                len(rb) == 34 and (split is None or split == 34),
                f"b alone over Q at P_q: {len(rb)} relations ({time.time() - t1:.1f} s); "
                f"over F_p at the scan point: {split} (b-functionals are P-independent)",
            )
        OUT[f"rational_K{K}_d{d}"] = {
            "Pq": [str(p) for p in Pq],
            "relations_Q": len(rels),
            "rank": info["rank"],
            "dim": info["rows_even"],
            "t_Q": tq,
        }
        report(
            f"E-exact-K{K}-d{d}",
            len(rels) + info["rank"] == info["rows_even"] and nz == 0,
            f"P_q = {tuple(str(p) for p in Pq)}: {len(rels)} relations over Q ({tq} s) + rank {info['rank']} "
            f"(mod p lower bound on rank over Q(Delta)) = {info['rows_even']}; relations x image: {nz} non-zero",
        )


def main() -> None:
    seed = 20261083
    print(f"seed = {seed}, p = {PMOD}, beta = 3/2, gamma' = 3")
    rng = random.Random(seed)
    which = sys.argv[1:] or ["engine", "d3", "alpha", "k3", "rational"]
    if "engine" in which:
        run_engine_check(rng)
    if "d3" in which:
        run_d3(rng)
    if "alpha" in which:
        run_alpha(rng)
    if "k3" in which:
        run_k3(rng, kchi=4, l3_cap=6000)
    if "rational" in which:
        run_rational(rng)
    nfail = sum(1 for _, ok, _ in RESULTS if not ok)
    print(f"SUMMARY: {len(RESULTS) - nfail}/{len(RESULTS)} PASS")
    sys.exit(1 if nfail else 0)


if __name__ == "__main__":
    main()
