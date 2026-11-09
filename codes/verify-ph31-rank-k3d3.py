"""
Companion script for derivation record 087: the K = 3 cokernel of the PH31 rank
test (R84) at d_eff = 3 matter components, alpha'_v = 0, beta = 3/2, gamma' = 3.

Imports, unchanged, the engines of codes/verify-ph31-rank.py (record 078:
Neumann and ghost data of R2's V_3', Fock bases, amplitudes, exact ranks over
F_p, p = 2^31 - 1) and codes/verify-ph31-rank-ext.py (record 083: the sparse
count of the relations on W^even_{<=K} implied by the two identities (4.3) of
record 078,
    O_b = b_1^- - z^2 b_{-1}^-,   O_L = L_1^- - z^2 L_{-1}^-,
with chi of level <= kchi in every zero-mode sector, coordinates outside
W^even_{<=K} eliminated first; the relations as row vectors over the scan's
row basis). New code: a copy of the b-functional builder restricted to chi of
a given matter content (factorisation over matter states), a scan over
unordered input pairs with an early stop at the rank bound dim - n_rel (the
relations are exact left-null vectors for every Delta and input level), and a
mod-p pairing product split in 16-bit halves (int64, no overflow).

Named checks (PASS/FAIL), node IDs of record 087:
- D1-dim: dim W^even_{<=3} at d = 3 from the generating function equals the
  Fock enumeration, per (N, Nbar) block.
- D2-factorisation-d<d>: the b-alone count at K = 3 computed directly (all chi)
  equals sum_{a, abar} n_d(a) n_d(abar) r(a, abar), with r(a, abar) the count
  with chi restricted to one matter state of levels (a, abar) and n_d(l) the
  number of matter states of level l per chirality (d = 1, 2, 3).
- BREAK-D2-even-only: the sector sum restricted to a - abar even (the version
  of record 083's critic, #5) differs from the direct count at d = 2, 3.
- D2-bound: the critic's bound b-count(K = 3, d = 3) >= 34 + 3 (d^2 - 4) = 49.
- D2-b-Q: the b-alone count at K = 3, d = 3 over Q (P-independent) equals the
  F_p count.
- D3-relations, D3-b-in-joint: joint (b + L) relation count at K = 3, d = 3
  (the relations are pickled to the scratch directory); the b-alone relations
  lie in the joint span. D3-split (opt-in, argument split; the L-alone
  elimination takes > 20 min at d = 3): rank of the stacked b-alone and L-alone
  relations and their containment in the joint span (mixed-only count).
- D3-rank: rank of the projected map at K = 3, L = 2, d = 3 over F_p at a random
  momentum; closure relations + rank = dim.
- D3-annihilate: every relation pairs to zero with every echelon basis vector of
  the measured image; D3-post-stop: further random columns add nothing.
- BREAK-D3-b: the b-alone relations with z^2 -> -z^2 in that identity only do
  not annihilate the image. BREAK-D3-L (opt-in, argument breakL): the same for
  the L-alone relations.
- D3-pairing-engine: the int64 split pairing product equals the exact
  Python-integer product on a subset (engine consistency).
- D3-mv-<K>-<d>: matter-vacuum diagnostic: joint count with the L-functionals
  restricted to matter-vacuum chi (b-functionals unrestricted), against the
  full joint count (K = 2, d = 2, 3; K = 3, d = 2, 3).
- D4-alpha-half: alpha'_v = 1/2, K = 3, L = 2, d = 3: full rank 1447/1447.

Not verified: unbounded level; generic P beyond the Schwartz-Zippel bound of
record 083 section 4 item 3 (degree <= number of L-functionals) and the
bad-prime caveat; the joint count over Q at a rational momentum (only the
b-alone count, which is P-independent); the L-alone count and the
mixed-only count at d = 3 unless run with the argument split; saturation of the count in kchi beyond
the closure argument (record 083 Verification); d_eff = 26; other beta.
"""

from __future__ import annotations

import importlib.util
import json
import pickle
import random
import sys
import time
from fractions import Fraction
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent.parent


def _load(name: str, rel: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


x = _load("v083", "codes/verify-ph31-rank-ext.py")  # imports 078's engine as x.v
v = x.v

PMOD = v.PMOD
SCRATCH = ROOT / "codes" / "output" / "ph31-rank-k3d3"
RESULTS: list[tuple[str, bool, str]] = []
OUT: dict = {}
TAG = "-".join(sys.argv[1:]) or "all"
KCHI = 4  # chi level cutoff at K = 3 (record 083)


def report(name: str, ok: bool, detail: str = "") -> None:
    ok = bool(ok)  # numpy booleans are not JSON serialisable
    RESULTS.append((name, ok, detail))
    print(f"{'PASS' if ok else 'FAIL'}  {name}: {detail}", flush=True)
    SCRATCH.mkdir(parents=True, exist_ok=True)
    (SCRATCH / f"checks-{TAG}.json").write_text(json.dumps(RESULTS, indent=1))
    (SCRATCH / f"results-{TAG}.json").write_text(json.dumps(OUT, indent=1, default=str))


def vertex(alpha_v=Fraction(0)):
    return v.Vertex(Fraction(3, 2), 3, alpha_v, 4)


# ------------------------------------------------- restricted b/L functionals
def functionals(  # noqa: PLR0913
    vx,
    d: int,
    P: tuple,
    kchi: int,
    sgn_b: int = -1,
    sgn_l: int = -1,
    kinds: str = "bL",
    bfilter=None,
    lfilter=None,
):
    """Copy of record 083's identity_functionals with chi filters and per-identity signs.

    sgn_b = -1, sgn_l = -1 is (4.3); +1 flips the sign of the z^2 terms of that
    identity only (break legs). bfilter / lfilter(st) -> bool restrict the chi
    of the b- / L-functionals (None: all). Parity filter: chi with N - Nbar odd.
    """
    z2 = Fraction(str(vx.z[1])) ** 2
    ell0 = tuple((-p) % PMOD for p in P)
    funcs = []
    for z in v.ZPREF:
        if "b" in kinds:
            for st in v.closed_basis(kchi, d, 1 - len(v.ZPREF[z]), False):
                if (st["N"] - st["Nb"]) % 2 == 0:
                    continue
                if bfilter is not None and not bfilter(st):
                    continue
                base = v.ZPREF[z] + st["gh"] + ((0, "c", 1), (1, "c", 1))
                strings = []
                for cf, op in (
                    (1, (0, "b", -1)),
                    (sgn_b * z2, (0, "b", 1)),
                    (-1, (1, "b", -1)),
                    (-sgn_b * z2, (1, "b", 1)),
                ):
                    for s2, o in v.reduce_on_vacuum((op,) + base):
                        strings.append((v.fmod(Fraction(cf) * s2), st["mat"], o))
                funcs.append(strings)
        if "L" in kinds:
            for st in v.closed_basis(kchi, d, -len(v.ZPREF[z]), False):
                if (st["N"] - st["Nb"]) % 2 == 0:
                    continue
                if lfilter is not None and not lfilter(st):
                    continue
                base = v.ZPREF[z] + st["gh"] + ((0, "c", 1), (1, "c", 1))
                strings = []
                for cf, (n, ch) in (
                    (1, (-1, 0)),
                    (sgn_l * z2, (1, 0)),
                    (-1, (-1, 1)),
                    (-sgn_l * z2, (1, 1)),
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


def rcount(vx, d, P, K, kchi=KCHI, **kw) -> tuple[list[dict], int, float]:
    t0 = time.time()
    vecs = functionals(vx, d, P, kchi, **kw)
    rels = x.sparse_relations(vecs, K)
    return rels, len(vecs), round(time.time() - t0, 1)


def n_matter(level: int, d: int) -> int:
    """Number of matter Fock states of one chirality at the given level (d components)."""
    return len(v.partitions_colored(level, d))


def rep_matter(a: int, ab: int) -> tuple:
    """One matter state at levels (a, abar): (alpha^0_{-1})^a (alphabar^0_{-1})^abar."""
    return ((0, 0, 1),) * a + ((1, 0, 1),) * ab


# ----------------------------------------------------------------- linear alg.
def pair_modp(Y: np.ndarray, B: np.ndarray) -> np.ndarray:
    """Y @ B.T mod p in int64, B split in 16-bit halves (entries < 2^31, n < 2^11)."""
    Y = np.asarray(Y, dtype=np.int64) % PMOD
    B = np.asarray(B, dtype=np.int64) % PMOD
    lo, hi = B & 0xFFFF, B >> 16
    r_hi = (Y @ hi.T) % PMOD
    r_lo = (Y @ lo.T) % PMOD
    return (r_hi * 65536 + r_lo) % PMOD


def nonzero_pairings(Y: np.ndarray, ech) -> int:
    if len(Y) == 0 or not ech.piv:
        return 0
    B = np.array(list(ech.piv.values()), dtype=np.int64)
    return int(np.count_nonzero(pair_modp(Y, B)))


# ------------------------------------------------------------------ the scan
def scan_unordered(  # noqa: PLR0913
    amps,
    K: int,
    L: int,
    d: int,
    rng: random.Random,
    P: tuple,
    stop_rank: int | None = None,
    max_delta: int = 2,
    extra_after_stop: int = 0,
    tag: str = "",
    log_every: int = 1000,
) -> tuple:
    """Joint rank over Delta samples, unordered input pairs (the column is symmetric).

    Stops at full rank, or at stop_rank (an upper bound from exact relations),
    after which extra_after_stop further random pairs are added as a check; else
    after a Delta sample that adds nothing (record 078's rule) or max_delta.
    """
    rows = x.even_rows(K, d)
    rstr = [v.state_strings(st) for st in rows]
    ins = v.input_basis(L, d)
    istr = [v.state_strings(st, z) for st, z in ins]
    ech = v.Echelon(len(rows))
    inv2 = pow(2, PMOD - 2, PMOD)
    target = len(rows) if stop_rank is None else stop_rank
    hist, ncols, t0, post = [], 0, time.time(), None
    pairs_all = [(i, j) for i in range(len(ins)) for j in range(i, len(ins))]
    for it in range(max_delta):
        D = tuple(rng.randrange(PMOD) for _ in range(d))
        l1 = tuple((p * inv2 + y) % PMOD for p, y in zip(P, D))
        l2 = tuple((p * inv2 - y) % PMOD for p, y in zip(P, D))
        pairs = list(pairs_all)
        rng.shuffle(pairs)
        added, k = 0, 0

        def column(i, j, l1=l1, l2=l2):
            return np.array(
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

        for k, (i, j) in enumerate(pairs):
            ncols += 1
            added += ech.add(column(i, j))
            if (k + 1) % log_every == 0:
                print(
                    f"  [{tag}] sample {it}: {k + 1} pairs, rank {ech.rank}/{len(rows)}"
                    f" t={time.time() - t0:.1f}s",
                    flush=True,
                )
            if ech.rank >= target:
                break
        hist.append(ech.rank)
        print(
            f"  [{tag}] K={K} L={L} d={d} sample {it}: rank {ech.rank}/{len(rows)}"
            f" (+{added}, {k + 1} of {len(pairs)} pairs) t={time.time() - t0:.1f}s",
            flush=True,
        )
        if ech.rank >= target:
            if extra_after_stop and ech.rank < len(rows):
                r0, extra = ech.rank, pairs[k + 1 : k + 1 + extra_after_stop]
                t1 = time.time()
                for i, j in extra:
                    ech.add(column(i, j))
                post = {
                    "pairs": len(extra),
                    "rank_before": r0,
                    "rank_after": ech.rank,
                    "time_s": round(time.time() - t1, 1),
                }
                print(f"  [{tag}] post-stop columns: {post}", flush=True)
            break
        if it >= 1 and added == 0:
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
        "unordered_pairs": len(pairs_all),
        "columns_used": ncols,
        "n_delta": len(hist),
        "rank_history": hist,
        "rank": ech.rank,
        "deficit": len(rows) - ech.rank,
        "stop_rank": stop_rank,
        "post_stop": post,
        "per_block": per_block,
        "time_s": round(time.time() - t0, 1),
    }
    OUT[f"scan_{tag}"] = info
    return ech, rows, info


# ----------------------------------------------------------------------- runs
def run_dim() -> int:
    K, d = 3, 3
    gf = v.gf_count(K, d)
    en: dict = {}
    for st in v.closed_basis(K, d, 0, False):
        en[(st["N"], st["Nb"])] = en.get((st["N"], st["Nb"]), 0) + 1
    dim = sum(c for (a, b), c in gf.items() if (a - b) % 2 == 0)
    nrows = len(x.even_rows(K, d))
    OUT["dim_blocks"] = {
        f"{a},{b}": c for (a, b), c in sorted(gf.items()) if (a - b) % 2 == 0
    }
    report(
        "D1-dim",
        gf == en and dim == nrows == 1447,
        f"d=3, K=3: dim W^even_<=3 = {dim} (rows {nrows}); even blocks {OUT['dim_blocks']}",
    )
    return dim


def run_b_factorisation(rng: random.Random) -> dict:
    """b-alone count at K = 3 for d = 1, 2, 3 against the matter-sector formula."""
    K = 3
    vx = vertex()
    # b-functionals are P-independent: any P
    sect: dict = {}
    t0 = time.time()
    for a in range(K + 1):
        for ab in range(K + 1):
            rep = rep_matter(a, ab)
            rels, nf, _ = rcount(
                vx,
                1,
                (0,),
                K,
                kinds="b",
                bfilter=lambda st, rep=rep: tuple(sorted(st["mat"])) == rep,
            )
            sect[(a, ab)] = len(rels)
    OUT["b_sectors"] = {f"{a},{ab}": r for (a, ab), r in sect.items()}
    print(
        f"  b-relations per matter sector r(a,abar), K=3: {OUT['b_sectors']}"
        f" ({time.time() - t0:.1f} s)",
        flush=True,
    )
    direct = {}
    for d in (1, 2, 3):
        P = tuple(rng.randrange(PMOD) for _ in range(d))
        rels, nf, t = rcount(vx, d, P, K, kinds="b")
        direct[d] = len(rels)
        formula = sum(
            n_matter(a, d) * n_matter(ab, d) * r for (a, ab), r in sect.items()
        )
        OUT[f"b_count_d{d}"] = {
            "direct": len(rels),
            "formula": formula,
            "functionals": nf,
            "time_s": t,
        }
        report(
            f"D2-factorisation-d{d}",
            len(rels) == formula,
            f"K=3, d={d}: b-alone count {len(rels)} ({nf} functionals, {t} s); "
            f"sum_(a,abar) n_d(a) n_d(abar) r(a,abar) = {formula}",
        )
    # break leg: the sector sum over a - abar even only (083 critic #5's version)
    even = {
        dd: sum(
            n_matter(a, dd) * n_matter(ab, dd) * r
            for (a, ab), r in sect.items()
            if (a - ab) % 2 == 0
        )
        for dd in (1, 2, 3)
    }
    report(
        "BREAK-D2-even-only",
        all(even[dd] != direct[dd] for dd in (2, 3)),
        f"sector sum over a - abar even only: {even} vs direct {direct} (must differ at d = 2, 3)",
    )
    bound = 34 + 3 * (3**2 - 4)
    report(
        "D2-bound",
        direct[2] == 34 and direct[3] >= bound,
        f"b-count(K=3): d=2 {direct[2]} (083: 34), d=3 {direct[3]} >= 34 + 3(d^2-4) = {bound}",
    )
    # over Q (P-independent: holds at every P)
    t0 = time.time()
    rq = x.relations_Q(vx, 3, (Fraction(0),) * 3, K, KCHI, kinds="b")
    report(
        "D2-b-Q",
        len(rq) == direct[3],
        f"b alone over Q, K=3, d=3: {len(rq)} relations ({time.time() - t0:.1f} s); over F_p: {direct[3]}",
    )
    return direct


def run_main(
    rng: random.Random, break_l: bool = False, with_split: bool = False
) -> dict:
    """K = 3, L = 2, d = 3, alpha'_v = 0: relations, scan, closure, break legs.

    break_l: also run BREAK-D3-L (an L-alone count with flipped z^2; the L-alone
    elimination at d = 3 is the slowest step, > 20 min, so it is opt-in: argument
    breakL). with_split: the L-alone count and D3-split (opt-in: argument split).
    """
    K, d = 3, 3
    vx = vertex()
    amps = v.Amplitudes(vx, d, v.Field(PMOD))
    P = tuple(rng.randrange(PMOD) for _ in range(d))
    OUT["P_main"] = P
    rels, nf, t = rcount(vx, d, P, K)
    OUT["joint"] = {"n": len(rels), "functionals": nf, "time_s": t}
    print(f"  joint relations: {len(rels)} from {nf} functionals, {t} s", flush=True)
    report(
        "D3-relations",
        len(rels) > 0,
        f"K=3, d=3: {len(rels)} relations from (4.3) (chi level <= {KCHI}, {nf} functionals, {t} s)",
    )
    with open(SCRATCH / "joint-relations-K3d3.pkl", "wb") as fh:
        pickle.dump({"P": P, "rels": rels}, fh)
    rb, nfb, tb = rcount(vx, d, P, K, kinds="b")
    OUT["b_main"] = {"n": len(rb), "functionals": nfb, "time_s": tb}
    dim = len(x.even_rows(K, d))
    ech, rows, info = scan_unordered(
        amps,
        K,
        2,
        d,
        rng,
        P,
        stop_rank=dim - len(rels),
        max_delta=2,
        extra_after_stop=400,
        tag="K3L2d3",
    )
    Y = x.relations_on_rows(rels, rows)
    Yb = x.relations_on_rows(rb, rows)
    r_j = v.rank_modp(list(Y)) if len(Y) else 0
    r_jb = v.rank_modp(list(Y) + list(Yb))
    report(
        "D3-b-in-joint",
        r_jb == r_j == len(rels) and len(rb) <= len(rels),
        f"b-alone {len(rb)} ({tb} s) lie in the joint span: rank(joint + b) = {r_jb} "
        f"(joint {len(rels)}, rank {r_j}); L-alone + mixed = {len(rels) - len(rb)}",
    )
    if with_split:
        rl, nfl, tl = rcount(vx, d, P, K, kinds="L")
        Yl = x.relations_on_rows(rl, rows) if rl else np.zeros((0, dim), np.int64)
        r_bl = v.rank_modp(list(Yb) + list(Yl)) if len(Yb) + len(Yl) else 0
        r_all = v.rank_modp(list(Y) + list(Yb) + list(Yl))
        OUT["split"] = {"L": len(rl), "nf_L": nfl, "t_L": tl, "rank_b_plus_L": r_bl}
        report(
            "D3-split",
            r_all == r_j == len(rels),
            f"rank(b-alone {len(rb)} + L-alone {len(rl)} ({tl} s)) = {r_bl}; "
            f"rank(joint + b + L) = {r_all} (joint {len(rels)}); mixed-only = {len(rels) - r_bl}",
        )
    report(
        "D3-rank",
        info["rank"] + len(rels) == dim,
        f"rank {info['rank']}/{dim} mod p, deficit {info['deficit']}, {info['columns_used']} columns, "
        f"{info['n_delta']} Delta, {info['time_s']} s; relations + rank = {info['rank'] + len(rels)}; "
        f"blocks {info['per_block']}",
    )
    nz = nonzero_pairings(Y, ech)
    report(
        "D3-annihilate",
        nz == 0 and r_j == len(rels),
        f"relations x image basis ({len(rels)} x {ech.rank}): {nz} non-zero pairings",
    )
    post = info["post_stop"]
    if post is not None:
        report(
            "D3-post-stop",
            post["rank_after"] == post["rank_before"],
            f"{post['pairs']} further random pairs after the stop: rank "
            f"{post['rank_before']} -> {post['rank_after']} ({post['time_s']} s)",
        )
    # engine check of the int64 pairing product against exact Python integers
    B = np.array(list(ech.piv.values()), dtype=np.int64)
    sub = (
        np.vstack([Y[:3], (Y[:3] + 7) % PMOD])
        if len(Y)
        else np.ones((2, dim), np.int64)
    )
    exact = (np.asarray(sub, dtype=object) @ np.asarray(B, dtype=object).T) % PMOD
    fast = pair_modp(sub, B)
    report(
        "D3-pairing-engine",
        bool(np.array_equal(np.asarray(exact, dtype=np.int64), fast))
        and np.count_nonzero(fast) > 0,
        f"int64 split product = exact product on {sub.shape[0]} rows x {B.shape[0]} "
        f"(incl. 3 shifted rows, {np.count_nonzero(fast)} non-zero entries)",
    )
    # break legs: one identity's z^2 sign flipped, that identity alone
    rbB, _, _ = rcount(vx, d, P, K, kinds="b", sgn_b=+1)
    nzb = nonzero_pairings(x.relations_on_rows(rbB, rows), ech) if rbB else 0
    report(
        "BREAK-D3-b",
        nzb > 0,
        f"b alone, z^2 -> -z^2: {len(rbB)} 'relations', {nzb} non-zero pairings (must be > 0)",
    )
    if not break_l:
        return {"rels": len(rels), "rank": info["rank"], "b": len(rb)}
    rlB, _, tB = rcount(vx, d, P, K, kinds="L", sgn_l=+1)
    nzl = nonzero_pairings(x.relations_on_rows(rlB, rows), ech) if rlB else 0
    report(
        "BREAK-D3-L",
        nzl > 0 or len(rlB) == 0,
        f"L alone, z^2 -> -z^2: {len(rlB)} 'relations' ({tB} s), {nzl} non-zero pairings"
        f" (must be > 0 if any)",
    )
    return {"rels": len(rels), "rank": info["rank"], "b": len(rb)}


def run_mv(rng: random.Random) -> None:
    """Matter-vacuum diagnostic: L-functionals from matter-vacuum chi only."""
    full = {
        (2, 2): 5,
        (2, 3): 5,
        (3, 2): 60,
        (3, 3): OUT.get("joint", {}).get("n", 107),
    }
    # 5, 5, 60: record 083; 107: run_main of record 087 (used when run separately)
    for K, d in ((2, 2), (2, 3), (3, 2), (3, 3)):
        vx = v.Vertex(Fraction(3, 2), 3, 0, 3 if K == 2 else 4)
        P = tuple(rng.randrange(PMOD) for _ in range(d))
        rmv, nf, t = rcount(vx, d, P, K, kchi=K + 1, lfilter=lambda st: not st["mat"])
        rbo, _, _ = rcount(vx, d, P, K, kchi=K + 1, kinds="b")
        bmv, _, _ = rcount(
            vx, d, P, K, kchi=K + 1, kinds="b", bfilter=lambda st: not st["mat"]
        )
        OUT[f"mv_K{K}_d{d}"] = {
            "joint_L_mv": len(rmv),
            "b_all": len(rbo),
            "b_mv": len(bmv),
            "joint_full": full[(K, d)],
            "time_s": t,
        }
        report(
            f"D3-mv-{K}-{d}",
            full[(K, d)] is not None and len(rmv) <= full[(K, d)],
            f"K={K}, d={d}: b all chi + L matter-vacuum chi: {len(rmv)} relations "
            f"(full joint {full[(K, d)]}; b alone {len(rbo)}; b from matter-vacuum chi {len(bmv)}; {t} s)",
        )


def run_alpha_half(rng: random.Random) -> None:
    K, d = 3, 3
    vx = vertex(Fraction(1, 2))
    amps = v.Amplitudes(vx, d, v.Field(PMOD))
    P = tuple(rng.randrange(PMOD) for _ in range(d))
    _, _, info = scan_unordered(amps, K, 2, d, rng, P, max_delta=1, tag="alpha-half")
    report(
        "D4-alpha-half",
        info["rank"] == info["rows_even"] == 1447,
        f"alpha'_v=1/2, K=3, L=2, d=3: rank {info['rank']}/{info['rows_even']}, "
        f"{info['columns_used']} columns, {info['time_s']} s",
    )


def main() -> None:
    seed = 20261087
    print(
        f"seed = {seed}, p = {PMOD}, beta = 3/2, gamma' = 3, kchi = {KCHI}", flush=True
    )
    rng = random.Random(seed)
    which = sys.argv[1:] or ["dim", "b", "main", "half", "mv"]
    if "dim" in which:
        run_dim()
    if "b" in which:
        run_b_factorisation(rng)
    if "main" in which:
        run_main(rng, break_l="breakL" in which, with_split="split" in which)
    if "half" in which:
        run_alpha_half(rng)
    if "mv" in which:
        run_mv(rng)
    nfail = sum(1 for _, ok, _ in RESULTS if not ok)
    print(f"SUMMARY: {len(RESULTS) - nfail}/{len(RESULTS)} PASS", flush=True)
    sys.exit(1 if nfail else 0)


if __name__ == "__main__":
    main()
