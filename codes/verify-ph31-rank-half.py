"""
Companion script for derivation record 093: PH31's rank rows at the vertex
parameter alpha'_v = 1/2 beyond K <= 3, d_eff <= 3 (R84's method).

Imports, unchanged, the engines of codes/verify-ph31-rank.py (record 078:
Neumann and ghost data of R2's V_3' with 032's maps f_0'(w) = w/(alpha'_v w +
gamma'), special map at beta = 3/2; Fock bases; three-point amplitudes;
incremental reduced echelon over F_p, p = 2^31 - 1; the generating function
gf_count), codes/verify-ph31-rank-ext.py (record 083: even_rows, the sparse
count of the relations implied by the identities (4.3) of record 078,
    O_b = b_1^- - z^2 b_{-1}^-,   O_L = L_1^- - z^2 L_{-1}^-,
relations_on_rows) and codes/verify-ph31-rank-k3d3.py (record 087: the
functional builder and rcount). New code: a scan over unordered input pairs
with a per-Delta cap, an optional starting echelon and pair filter (L = 3
capped scan), antisymmetrised columns, progress written to the scratch
directory, and a chunked mod-p pairing.

The level-projected circle map at fixed momentum P: columns are the
amplitudes <V_3'| B (x) A_i (x) A_j> + (i <-> j, l1 <-> l2) for unordered
pairs of inputs A_i, A_j in H_0 (level <= L, ghost number 2, level-matched,
b_0^- annihilated), leg momenta l1 = P/2 + Delta, l2 = P/2 - Delta with a
random Delta per sample; rows are the monomials B of W^even_{<=K}. The rank
is the joint rank over the Delta samples (record 078).

Named checks (PASS/FAIL), node IDs of record 093:
- G1-dim: dim W^even_{<=K} from the generating function equals the Fock
  enumeration per (N, Nbar) block and the number of scan rows, at (K, d) =
  (3, 4), (3, 5), (4, 2).
- G7-den-<K><L>-<gamma'>: no denominator of the rational vertex data (matter
  N, a; ghost E, Z) at the alpha'_v = 1/2 vertices used is divisible by p, so
  the F_p matrix is the reduction of the rational one and a non-zero maximal
  minor mod p lifts (G7).
- G2-rank: alpha'_v = 1/2, K = 3, L = 2, d = 4: rank 3608/3608 over F_p.
- G3.1-L2-saturated: alpha'_v = 1/2, K = 4, L = 2, d = 2: the rank over Delta
  samples saturates (the last Delta adds nothing) below 2927 (measured 2882,
  every (N, Nbar) block onto separately); the check is the saturation.
- G3.1-null-blocks: the left-null space of the K = 4, L = 2 image has
  dimension = the deficit, and contains no vector supported in a single
  (N, Nbar) block (consistency with the per-block ranks); the rank of its
  projection on each block is logged.
- G3-L3: K = 4, d = 2, inputs of level <= 3 (pairs with a level-3 input, capped,
  on top of the L = 2 echelon): rank 2927/2927.
- G3.2-P2: K = 4, L = 2, a second random momentum: same saturated rank.
- G4-rank (opt-in, argument iii): alpha'_v = 1/2, K = 3, L = 2, d = 5.
- G5-gamma: gamma' = 3/2, alpha'_v = 1/2, K = 3, L = 2, d = 2: rank 487/487.
- G5-gamma-alpha0: gamma' = 3/2, alpha'_v = 0, K = 3, L = 2, d = 2: the
  joint relation count is 60 and the rank 427/487, as at gamma' = 3 (R84);
  further columns after the stop add nothing.
- G6-b-count-<K><d>: alpha'_v = 0: the b-alone relation count; at K = 3 it
  must equal R84's b(3, d) = 4 d^2 + 7 d + 4 (96 at d = 4).
- G6-annihilate-<K><d>: the b-relations pair to zero with every echelon
  vector of the measured alpha'_v = 0 image.
- G6-not-onto-<K><d>: only when the alpha'_v = 0 scan uses at least as many
  columns as rows: its rank is <= dim - b-count (the same pipeline is not onto
  at alpha'_v = 0: G2-rank / G3-rank can fail). With a smaller budget the bound
  is automatic and the check is not run; the bound for every budget then
  follows from G6-annihilate and the exact identity (4.3) of record 078.
- BREAK-G6-flip-<K><d>: the b-relations with z^2 -> -z^2 do not annihilate
  the alpha'_v = 0 image (G6-annihilate can fail).
- BREAK-antisym-<K><d>: antisymmetrised columns (minus sign on the exchanged
  amplitude) give rank 0 on W^even (exchange symmetry, record 078 C1).

Fix pass (critic iteration 1 of record 093, section "Fix pass"; parts k2l1, c44a,
c44, c44s, c45t; scratch computator-093-fix-20261005T012100; revised in fix pass
2, critic iteration 2). The c-ghost
pole structure for inputs of level <= L: in an input frame c_n A = 0 for
n > level(A), so (F.6) the quadratic differential (u^2 - z^2) du^2 gives the
left-null vectors (c_{-4} - z^2 c_{-2})(c_1 (x) chibar) and conjugates for
L = 2 (44 at K = 4, d = 2), phi = 1 gives the rows c_{-2}(c_1 (x) chibar) for
L = 1, and (F.13) no input of level <= 2 carries b_{-2} and bbar_{-2}, which
gives (c_{-3} cbar_{-3} + z^2 c_{-2} cbar_{-2})|0>. Checks:
- G3.7-K2L1-rank / -annihilate: K = 2, L = 1, d = 2: rank = 67, saturated (73
  would refute the law, < 67 would show an extra relation), the 6 rows
  annihilate the image and span its left-null space (dimension 6);
  BREAK-G3.7-L2: the same rows are non-zero on L = 2 columns.
- G3.5-count: 22 + 22 vectors (F.7), rank 44, block projections (F.8).
- G3.5-annihilate / BREAK-G3.5-flip / G3.5-in-null: against the K = 4, L = 2
  image at a fresh momentum (c44: scan stopped at 2882; c44s: saturated).
- G3.5-alpha-<a>-<g> / BREAK-G3.5-alpha-flip-*: on random L = 2 columns at
  alpha'_v = 1/5 (gamma' = 2) and 0.
- G3.6-L3-pattern: level-3 columns violate the holomorphic (antiholomorphic)
  vectors only through inputs with b_{-3} (bbar_{-3}) (F.10).
- G3.8-proj-N4 / -Nb4: the left-null space projects with rank 45 on the
  blocks with N = 4 or Nbar = 4, and 42 on Nbar = 4.
- G3.9-P3-saturated: rank 2882 (deficit 45) at a third momentum, saturated in
  Delta;
  G3.9-complement (logging): the null space modulo the 44, explicit form printed.
- G3.9-y45-in-null / BREAK-G3.9-y45-in-null-flip (c44, c44s; fix pass 2): the
  rank of (left-null space + 44 + y45) is 45, and 46 with -z^2 in y45.
- G3.9-y45-<a>-<g>-t (c45t, alpha'_v = 1/2, 1/5): y45 pairs to zero with 150
  targeted L <= 2 columns (one input with b_{-2}, the other with bbar_{-2})
  and e[R_33] is non-zero on at least one of them (non-vacuity);
  BREAK-...-flip: -z^2 is non-zero; BREAK-...-L3: y45 is non-zero on columns
  with a level-3 input. G3.9-alpha0-rows-vanish (alpha'_v = 0): e[R_33] and
  e[R_44] vanish separately on the targeted and the level-3 columns (R84 (4.3)
  at alpha'_v = 0); the y45 line there is printed as INFO. Part c45 (random
  pairs, vacuous sample) is retired (fix pass 2).
- Fix pass 2 also tightened G3.7-K2L1-rank (rank == 67), G3.7-K2L1-annihilate
  (left-null space of dimension 6) and G3.9-P3-saturated (rank == 2882).

Not verified: unbounded level; the rank at generic P beyond the lift of a
non-zero maximal minor (a full rank mod p at the sample point is a full rank
over Q at generic P; a deficit mod p is only an upper bound); the joint (b + L)
relation count at alpha'_v = 0 for d = 4 and K = 4 (only the b-alone part);
d_eff = 26; other beta.

Seeds: per part, random.Random(f"{SEED}-{part}") (string seeding is
deterministic), SEED = 20261093; printed.
"""

from __future__ import annotations

import importlib.util
import json
import random
import resource
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


k = _load("v087", "codes/verify-ph31-rank-k3d3.py")  # loads 083 as k.x, 078 as k.v
x = k.x
v = k.v

PMOD = v.PMOD
SEED = 20261093
SCRATCH = ROOT / "codes" / "output" / "ph31-rank-half"
RESULTS: list[tuple[str, bool, str]] = []
OUT: dict = {}
TAG = "-".join(sys.argv[1:]) or "default"
HALF = Fraction(1, 2)


def rss_mb() -> float:
    """Peak resident set size of this process so far (MB)."""
    return round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024, 1)


def save() -> None:
    SCRATCH.mkdir(parents=True, exist_ok=True)
    (SCRATCH / f"checks-{TAG}.json").write_text(json.dumps(RESULTS, indent=1))
    (SCRATCH / f"results-{TAG}.json").write_text(json.dumps(OUT, indent=1, default=str))


def report(name: str, ok: bool, detail: str = "") -> None:
    ok = bool(ok)
    RESULTS.append((name, ok, detail))
    print(f"{'PASS' if ok else 'FAIL'}  {name}: {detail}", flush=True)
    save()


def vertex(alpha_v: Fraction, gamma: Fraction, K: int, L: int):
    """V_3' of record 032 at beta = 3/2; mode cutoff max(K, L) + 1 (A6)."""
    return v.Vertex(Fraction(3, 2), gamma, alpha_v, max(K, L) + 1)


def pairings(Y: np.ndarray, ech, chunk: int = 400) -> int:
    """Number of non-zero y . b mod p over relation rows y and echelon vectors b."""
    if len(Y) == 0 or not ech.piv:
        return 0
    basis = list(ech.piv.values())
    nz = 0
    for s in range(0, len(basis), chunk):
        B = np.array(basis[s : s + chunk], dtype=np.int64)
        nz += int(np.count_nonzero(k.pair_modp(Y, B)))
    return nz


# ------------------------------------------------------------------ the scan
def scan(  # noqa: PLR0913
    amps,
    rows: list[dict],
    ins: list,
    rng: random.Random,
    P: tuple,
    target: int,
    max_delta: int = 1,
    cap: int | None = None,
    pair_filter=None,
    ech=None,
    extra_after_stop: int = 0,
    antisym: bool = False,
    tag: str = "",
    log_every: int = 250,
) -> tuple:
    """Joint rank over Delta samples of the projected map, unordered input pairs.

    Copy of record 087's scan_unordered with a per-Delta cap, a pair filter, a
    starting echelon and antisymmetrised columns. Stops at rank >= target (the
    block dimension, or dim - n_rel for exact relations), else after a Delta
    sample that adds nothing (record 078's rule), else after max_delta samples.
    """
    d = len(P)
    rstr = [v.state_strings(st) for st in rows]
    istr = [v.state_strings(st, z) for st, z in ins]
    ech = ech if ech is not None else v.Echelon(len(rows))
    r0 = ech.rank
    sg = -1 if antisym else 1
    inv2 = pow(2, PMOD - 2, PMOD)
    n = len(ins)
    lo = 1 if antisym else 0  # i < j for antisymmetric columns (i = j gives 0)
    pairs_all = [
        (i, j)
        for i in range(n)
        for j in range(i + lo, n)
        if pair_filter is None or pair_filter(i, j)
    ]
    hist, ncols, t0, post, Ds = [], 0, time.time(), None, []
    for it in range(max_delta):
        D = tuple(rng.randrange(PMOD) for _ in range(d))
        Ds.append(D)
        l1 = tuple((p * inv2 + y) % PMOD for p, y in zip(P, D))
        l2 = tuple((p * inv2 - y) % PMOD for p, y in zip(P, D))
        pairs = list(pairs_all)
        rng.shuffle(pairs)
        if cap is not None:
            pairs = pairs[: cap + extra_after_stop]
        added, kk = 0, -1

        def column(i, j, l1=l1, l2=l2):
            return np.array(
                [
                    (
                        amps.amp(B, istr[i], istr[j], l1, l2)
                        + sg * amps.amp(B, istr[j], istr[i], l2, l1)
                    )
                    % PMOD
                    for B in rstr
                ],
                dtype=np.int64,
            )

        main = pairs if cap is None else pairs[:cap]
        for kk, (i, j) in enumerate(main):
            ncols += 1
            added += ech.add(column(i, j))
            if (kk + 1) % log_every == 0:
                dt = time.time() - t0
                print(
                    f"  [{tag}] sample {it}: {kk + 1} pairs, rank {ech.rank}/{len(rows)}"
                    f" t={dt:.1f}s rss={rss_mb()}MB",
                    flush=True,
                )
                OUT[f"progress_{tag}"] = {
                    "sample": it,
                    "pairs": kk + 1,
                    "rank": ech.rank,
                    "t": round(dt, 1),
                    "rss_mb": rss_mb(),
                }
                save()
            if ech.rank >= target:
                break
        hist.append(ech.rank)
        print(
            f"  [{tag}] sample {it}: rank {ech.rank}/{len(rows)} (+{added}, "
            f"{kk + 1} of {len(pairs_all)} pairs) t={time.time() - t0:.1f}s",
            flush=True,
        )
        if ech.rank >= target:
            if extra_after_stop and ech.rank < len(rows):
                rb, t1 = ech.rank, time.time()
                for i, j in pairs[kk + 1 : kk + 1 + extra_after_stop]:
                    ech.add(column(i, j))
                post = {
                    "pairs": extra_after_stop,
                    "rank_before": rb,
                    "rank_after": ech.rank,
                    "time_s": round(time.time() - t1, 1),
                }
                print(f"  [{tag}] post-stop columns: {post}", flush=True)
            break
        if it >= 1 and added == 0:
            break
    info = {
        "rows_even": len(rows),
        "inputs": n,
        "pairs_per_delta": len(pairs_all),
        "columns_used": ncols,
        "n_delta": len(hist),
        "rank_start": r0,
        "rank_history": hist,
        "rank": ech.rank,
        "deficit": len(rows) - ech.rank,
        "target": target,
        "cap": cap,
        "post_stop": post,
        "Delta": Ds,
        "time_s": round(time.time() - t0, 1),
        "rss_mb": rss_mb(),
    }
    OUT[f"scan_{tag}"] = info
    save()
    return ech, info


def per_block(ech, rows: list[dict]) -> dict:
    """Rank of the image projected on each (N, Nbar) block (used only on a deficit)."""
    basis = list(ech.piv.values())
    out = {}
    for blk in sorted({(st["N"], st["Nb"]) for st in rows}):
        idx = [q for q, st in enumerate(rows) if (st["N"], st["Nb"]) == blk]
        out[f"{blk[0]},{blk[1]}"] = (
            v.rank_modp([b[idx] for b in basis]) if basis else 0,
            len(idx),
        )
    return out


# ----------------------------------------------------------------------- runs
EXPECTED = {(3, 4): 3608, (3, 5): 7945, (4, 2): 2927}


def run_dim() -> None:
    for (K, d), want in EXPECTED.items():
        gf = v.gf_count(K, d)
        en: dict = {}
        for st in v.closed_basis(K, d, 0, False):
            en[(st["N"], st["Nb"])] = en.get((st["N"], st["Nb"]), 0) + 1
        dim = sum(c for (a, b), c in gf.items() if (a - b) % 2 == 0)
        nrows = len(x.even_rows(K, d))
        blocks = {f"{a},{b}": c for (a, b), c in sorted(gf.items()) if (a - b) % 2 == 0}
        OUT[f"dim_K{K}_d{d}"] = {"dim": dim, "blocks": blocks}
        report(
            f"G1-dim-{K}{d}",
            gf == en and dim == nrows == want,
            f"K={K}, d={d}: dim W^even_<=K = {dim} (Fock rows {nrows}, gf = Fock per "
            f"block: {gf == en}); even blocks {blocks}",
        )


def run_den() -> None:
    """The mod-p reduction is the reduction of the rational data (A7, G7)."""
    for alpha_v, gamma, K, L in (
        (HALF, Fraction(3), 3, 2),
        (HALF, Fraction(3), 4, 3),
        (HALF, Fraction(3, 2), 3, 2),
    ):
        vx = vertex(alpha_v, gamma, K, L)
        vals = [
            q
            for tab in (vx.N, vx.a, vx.E, vx.Z)
            for q in tab.values()
            if isinstance(q, Fraction)
        ]
        dens = {q.denominator for q in vals}
        bad = [q for q in dens if q % PMOD == 0]
        report(
            f"G7-den-{K}{L}-{gamma}".replace("/", "_"),
            not bad and len(vals) > 0,
            f"alpha'_v={alpha_v}, gamma'={gamma}, mode cutoff {max(K, L) + 1}: "
            f"{len(vals)} rational coefficients, largest denominator {max(dens)}, "
            f"none divisible by p",
        )


def main_row(  # noqa: PLR0913
    part: str, node: str, K: int, L: int, d: int, gamma: Fraction, rng, onto=True
) -> tuple:
    """alpha'_v = 1/2 row: early stop at the block dimension; one Delta first.

    onto=True: the check is rank = dim. onto=False (a row measured not onto,
    record 093 run (ii)): the check is saturation over Delta (the last Delta
    sample adds nothing), with the per-block ranks logged.
    """
    t0 = time.time()
    vx = vertex(HALF, gamma, K, L)
    amps = v.Amplitudes(vx, d, v.Field(PMOD))
    tv = round(time.time() - t0, 1)
    rows = x.even_rows(K, d)
    ins = v.input_basis(L, d)
    P = tuple(rng.randrange(PMOD) for _ in range(d))
    OUT[f"P_{part}"] = P
    print(
        f"  [{part}] vertex built in {tv} s; rows {len(rows)}, inputs {len(ins)}; P = {P}"
    )
    ech, info = scan(
        amps, rows, ins, rng, P, len(rows), max_delta=4, tag=f"{part}-half"
    )
    info["vertex_s"] = tv
    if info["deficit"]:
        info["per_block"] = per_block(ech, rows)
    hist = info["rank_history"]
    ok = (
        info["rank"] == len(rows)
        if onto
        else len(hist) >= 2 and hist[-1] == hist[-2] and info["deficit"] > 0
    )
    report(
        node,
        ok,
        f"alpha'_v=1/2, gamma'={gamma}, K={K}, L={L}, d={d}: rank {info['rank']}/"
        f"{len(rows)} mod p, {info['columns_used']} columns ({info['n_delta']} Delta, "
        f"{info['pairs_per_delta']} pairs per Delta, rank history {hist}), "
        f"{info['time_s']} s, peak rss {rss_mb()} MB"
        + ("" if onto else f"; per block (rank, dim) {info.get('per_block')}"),
    )
    # antisymmetrised columns: rank 0 on W^even (exchange symmetry)
    _, ia = scan(
        amps,
        rows,
        ins,
        rng,
        P,
        len(rows),
        cap=200,
        antisym=True,
        tag=f"{part}-antisym",
        log_every=10**9,
    )
    report(
        f"BREAK-antisym-{K}{d}",
        ia["rank"] == 0,
        f"antisymmetrised columns, 200 pairs: rank {ia['rank']}/{len(rows)} "
        f"(must be 0), {ia['time_s']} s",
    )
    return amps, rows, ins, P, ech, info


def break_alpha0(  # noqa: PLR0913
    part: str, K: int, L: int, d: int, rng, budget: int, n_delta: int = 1
) -> None:
    """alpha'_v = 0 at the same size: b-relations, capped scan, pairings.

    budget: columns per Delta sample (at least the number the alpha'_v = 1/2
    row needed for full rank); n_delta: Delta samples (as the 1/2 row).
    """
    vx = vertex(Fraction(0), Fraction(3), K, L)
    amps = v.Amplitudes(vx, d, v.Field(PMOD))
    rows = x.even_rows(K, d)
    ins = v.input_basis(L, d)
    P = tuple(rng.randrange(PMOD) for _ in range(d))
    OUT[f"P_{part}0"] = P
    rb, nf, tb = k.rcount(vx, d, P, K, kchi=K + 1, kinds="b")
    rf, _, tf = k.rcount(vx, d, P, K, kchi=K + 1, kinds="b", sgn_b=+1)
    OUT[f"b_{part}0"] = {
        "n": len(rb),
        "functionals": nf,
        "time_s": tb,
        "flip_n": len(rf),
    }
    if K == 3:
        want = 4 * d * d + 7 * d + 4
        report(
            f"G6-b-count-{K}{d}",
            len(rb) == want,
            f"alpha'_v=0, K={K}, d={d}: b-alone relations {len(rb)} ({nf} functionals, "
            f"{tb} s); R84's b(3,d) = 4d^2+7d+4 = {want}",
        )
    else:
        report(
            f"G6-b-count-{K}{d}",
            len(rb) > 0,
            f"alpha'_v=0, K={K}, d={d}: b-alone relations {len(rb)} ({nf} functionals, "
            f"chi level <= {K + 1}, {tb} s) (no prediction; logged)",
        )
    ech, info = scan(
        amps,
        rows,
        ins,
        rng,
        P,
        len(rows) - len(rb),
        max_delta=n_delta,
        cap=budget,
        tag=f"{part}-alpha0",
    )
    Y = x.relations_on_rows(rb, rows)
    Yf = x.relations_on_rows(rf, rows)
    nz, nzf = pairings(Y, ech), pairings(Yf, ech)
    report(
        f"G6-annihilate-{K}{d}",
        nz == 0 and len(rb) > 0,
        f"b-relations x alpha'_v=0 image ({len(rb)} x {info['rank']}): {nz} non-zero pairings",
    )
    report(
        f"BREAK-G6-flip-{K}{d}",
        nzf > 0,
        f"b-relations with z^2 -> -z^2 ({len(rf)}): {nzf} non-zero pairings (must be > 0)",
    )
    detail = (
        f"alpha'_v=0, K={K}, L={L}, d={d}: rank {info['rank']}/{len(rows)} after "
        f"{info['columns_used']} columns (budget {budget} x {n_delta} Delta), deficit "
        f"{info['deficit']} >= b-count {len(rb)}; {info['time_s']} s, peak rss {rss_mb()} MB"
    )
    if info["columns_used"] >= len(rows):
        report(
            f"G6-not-onto-{K}{d}",
            info["rank"] <= len(rows) - len(rb),
            detail,
        )
    else:
        # fewer columns than rows: rank <= dim - b is automatic, no check; the
        # bound for every budget follows from G6-annihilate and the exact identity
        OUT[f"not_onto_{part}0"] = "budget < dim: no check (bound from G6-annihilate)"
        print(f"  (no G6-not-onto check: {detail})", flush=True)


def run_i(rng) -> None:
    main_row("i", "G2-rank", 3, 2, 4, Fraction(3), rng)


def run_i0(rng, budget: int) -> None:
    break_alpha0("i", 3, 2, 4, rng, budget)


def run_ii(rng) -> None:
    amps, rows, ins, P, ech, info = main_row(
        "ii", "G3.1-L2-saturated", 4, 2, 2, Fraction(3), rng, onto=False
    )
    if info["deficit"] == 0:
        return
    # left-null space of the L = 2 image: projection on each (N, Nbar) block
    nulls = v.left_null(ech)
    blk = [(st["N"], st["Nb"]) for st in rows]
    proj, single = {}, {}
    for b in sorted(set(blk)):
        idx = [q for q in range(len(rows)) if blk[q] == b]
        out = [q for q in range(len(rows)) if blk[q] != b]
        r_in = v.rank_modp([y[idx] for y in nulls])
        # relations supported in block b only: dim null - rank on the complement
        single[f"{b[0]},{b[1]}"] = len(nulls) - v.rank_modp([y[out] for y in nulls])
        proj[f"{b[0]},{b[1]}"] = r_in
    OUT["ii_null"] = {"n": len(nulls), "block_projection_rank": proj, "single": single}
    report(
        "G3.1-null-blocks",
        len(nulls) == info["deficit"] and not any(single.values()),
        f"K=4, L=2: {len(nulls)} left-null vectors of the image; rank of their "
        f"projection per block {proj}; relations supported in a single block "
        f"{sum(single.values())} (must be 0: every block is onto separately)",
    )
    # deficit: L = 3 capped scan on top of the L = 2 echelon, and a second momentum
    vx3 = vertex(HALF, Fraction(3), 4, 3)
    amps3 = v.Amplitudes(vx3, 2, v.Field(PMOD))
    ins3 = v.input_basis(3, 2)
    lev3 = [q for q, (st, _) in enumerate(ins3) if st["N"] == 3]
    s3 = set(lev3)
    _, i3 = scan(
        amps3,
        rows,
        ins3,
        rng,
        P,
        len(rows),
        max_delta=2,
        cap=6000,
        pair_filter=lambda i, j: i in s3 or j in s3,
        ech=ech,
        tag="ii-L3",
    )
    report(
        "G3-L3",
        i3["rank"] == len(rows),
        f"K=4, L=3 capped (pairs with a level-3 input, 6000 per Delta) on top of L=2: "
        f"rank {i3['rank_start']} -> {i3['rank']}/{len(rows)}",
    )
    P2 = tuple(rng.randrange(PMOD) for _ in range(2))
    _, i2 = scan(amps, rows, ins, rng, P2, len(rows), max_delta=4, tag="ii-P2")
    report(
        "G3.2-P2",
        i2["rank"] == info["rank"]
        and len(i2["rank_history"]) >= 2
        and i2["rank_history"][-1] == i2["rank_history"][-2],
        f"K=4, L=2, second momentum {P2}: rank {i2['rank']}/{len(rows)} (rank history "
        f"{i2['rank_history']}; first momentum {info['rank']}), {i2['time_s']} s",
    )


def run_ii0(rng, budget: int, n_delta: int) -> None:
    # L = 3 inputs: the alpha'_v = 1/2 row is onto only with level-3 inputs
    break_alpha0("ii", 4, 3, 2, rng, budget, n_delta)


def run_smoke(rng) -> None:
    """Engine smoke test at K = L = 2, d = 2 (not part of the final run)."""
    main_row("smoke", "SMOKE-rank", 2, 2, 2, Fraction(3), rng)
    break_alpha0("smoke", 2, 2, 2, rng, 200)


def run_iii(rng) -> None:
    main_row("iii", "G4-rank", 3, 2, 5, Fraction(3), rng)


def run_iv(rng) -> None:
    g = Fraction(3, 2)
    main_row("iv", "G5-gamma", 3, 2, 2, g, rng)
    # gamma'-independence where the rank is not full: alpha'_v = 0, K = 3, d = 2
    K, d = 3, 2
    vx = vertex(Fraction(0), g, K, 2)
    amps = v.Amplitudes(vx, d, v.Field(PMOD))
    rows = x.even_rows(K, d)
    P = tuple(rng.randrange(PMOD) for _ in range(d))
    rels, nf, t = k.rcount(vx, d, P, K, kchi=4)
    _, info = scan(
        amps,
        rows,
        v.input_basis(2, d),
        rng,
        P,
        len(rows) - len(rels),
        max_delta=2,
        extra_after_stop=300,
        tag="iv-alpha0",
    )
    post = info["post_stop"] or {}
    report(
        "G5-gamma-alpha0",
        len(rels) == 60
        and info["rank"] == 427
        and post.get("rank_after") == post.get("rank_before"),
        f"gamma'=3/2, alpha'_v=0, K=3, L=2, d=2: {len(rels)} joint relations ({nf} "
        f"functionals, {t} s), rank {info['rank']}/487 after {info['columns_used']} "
        f"columns, post-stop {post} (R84 at gamma'=3: 60, 427/487)",
    )


# --------------------------------------------- fix pass (critic iteration 1)
# The c-ghost conservation law of record 093, F1(a): for a quadratic
# differential phi(u) du^2 holomorphic except at the special puncture u = inf,
# sum over punctures of oint phi_r(w) c(w) dw = 0, phi_r = phi(h_r) h_r'^2.
# phi = u^2 - z^2 gives c_{-4} - z^2 c_{-2} at the output (h_0 = 1/w) and only
# c_3, c_4, ... at the inputs (h_r(0) = +-z), which kill inputs of level <= 2
# (eq. (F.6)); phi = 1 gives c_{-2} at the output and c_2, c_3, ... at the
# inputs, which kill inputs of level <= 1.
SCRATCH_FIX = ROOT / "codes" / "output" / "ph31-rank-half-fix"
# c45 (random pairs, vacuous sample) retired in fix pass 2 (critic iteration 2,
# #4(d)): superseded by c45t; its log run-c45.log is kept as superseded
NEW_PARTS = ("k2l1", "c44a", "c44", "c44s", "c45t")


def c_vectors(rows: list[dict], ops: list, ch: int, K: int, d: int) -> list:
    """Row vectors (F.7): sum_n coef * e[c_{-n} on c_1 (x) chi], chirality ch.

    ops: list of (n, coef mod p) for the output operator sum coef c_{-n} in
    chirality ch (0 holomorphic, 1 antiholomorphic); B = c_1|0> (x) chi with chi
    of the other chirality at level <= K and ghost charge -1 (relative to
    c_1|0>). Keys follow closed_basis: holomorphic matter, antiholomorphic
    matter; holomorphic ghost string, antiholomorphic ghost string. A vector is
    kept only if every term is a row (otherwise it is cut by the truncation or
    lies on odd rows); returns (vectors, chi labels, number cut).
    """
    pos = {(st["mat"], st["gh"]): r for r, st in enumerate(rows)}
    out, labels, cut = [], [], 0
    for lev, q, mat, gh in v.chiral_states(K, d):
        if q != -1:
            continue
        o = 1 - ch
        m = tuple((o, mu, n) for mu, n in mat)
        g = tuple((o, t, n) for t, n in gh)
        keys = []
        for n, _ in ops:
            cg = ((ch, "c", -n),)
            keys.append((m, cg + g if ch == 0 else g + cg))
        hit = [kk in pos for kk in keys]
        if not any(hit):
            continue
        if not all(hit):
            cut += 1
            continue
        y = np.zeros(len(rows), dtype=np.int64)
        for (_, cf), kk in zip(ops, keys):
            y[pos[kk]] = cf % PMOD
        out.append(y)
        labels.append(f"ch{ch}:lev{lev}:{mat}|{gh}")
    return out, labels, cut


def block_ranks(Y: list, rows: list[dict]) -> dict:
    """Rank of the projection of the vectors Y on each (N, Nbar) block."""
    out = {}
    for blk in sorted({(st["N"], st["Nb"]) for st in rows}):
        idx = [q for q, st in enumerate(rows) if (st["N"], st["Nb"]) == blk]
        r = v.rank_modp([y[idx] for y in Y]) if len(Y) else 0
        if r:
            out[f"{blk[0]},{blk[1]}"] = r
    return out


def zsq(vx) -> int:
    """z^2 mod p with z = f_1(0) read from the vertex (must be 1/(2 beta))."""
    z = Fraction(str(vx.z[1]))
    assert z == Fraction(1, 3), z  # beta = 3/2
    return v.fmod(z * z)


def columns(amps, ins: list, pairs: list, P: tuple, D: tuple, rows: list) -> list:
    """Symmetrised columns for the given unordered input pairs at (P, Delta)."""
    inv2 = pow(2, PMOD - 2, PMOD)
    l1 = tuple((p * inv2 + y) % PMOD for p, y in zip(P, D))
    l2 = tuple((p * inv2 - y) % PMOD for p, y in zip(P, D))
    rstr = [v.state_strings(st) for st in rows]
    istr = [v.state_strings(st, z) for st, z in ins]
    return [
        np.array(
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
        for i, j in pairs
    ]


def nz_pair(Y: list, cols: list) -> int:
    """Number of non-zero pairings y . col (exact, Python integers)."""
    if not len(Y) or not cols:
        return 0
    Ya = np.array(Y, dtype=object)
    Ca = np.array(cols, dtype=object)
    return int(np.count_nonzero((Ya @ Ca.T) % PMOD))


def ratrec(a: int, bound: int = 46340) -> str:
    """Rational reconstruction n/m of a mod p with |n|, m <= bound (else the residue)."""
    r0, r1, s0, s1 = PMOD, a % PMOD, 0, 1
    while r1 > bound:
        q = r0 // r1
        r0, r1, s0, s1 = r1, r0 - q * r1, s1, s0 - q * s1
    if s1 == 0 or abs(s1) > bound:
        return str(a)
    num, den = (r1, s1) if s1 > 0 else (-r1, -s1)
    return str(Fraction(num, den))


def c44_vectors(rows: list[dict], z2: int, sgn: int = -1) -> tuple:
    """The 22 + 22 vectors (c_{-4} - z^2 c_{-2}) (c_1 (x) chi) and conjugates."""
    ops = [(4, 1), (2, sgn * z2)]
    yh, lh, ch_ = c_vectors(rows, ops, 0, 4, 2)
    ya, la, ca = c_vectors(rows, ops, 1, 4, 2)
    return yh, ya, lh + la, ch_ + ca


def run_k2l1(rng) -> None:
    """F1(c): K = 2, L = 1, d = 2, alpha'_v = 1/2: rank <= 73 - 6 predicted."""
    K, L, d = 2, 1, 2
    vx = vertex(HALF, Fraction(3), K, L)
    amps = v.Amplitudes(vx, d, v.Field(PMOD))
    rows = x.even_rows(K, d)
    ins = v.input_basis(L, d)
    P = tuple(rng.randrange(PMOD) for _ in range(d))
    OUT["P_k2l1"] = P
    yh, _, cuth = c_vectors(rows, [(2, 1)], 0, K, d)
    ya, _, cuta = c_vectors(rows, [(2, 1)], 1, K, d)
    Y6 = yh + ya
    blocks6 = block_ranks(Y6, rows)
    ech, info = scan(amps, rows, ins, rng, P, len(rows), max_delta=10, tag="k2l1")
    nulls = v.left_null(ech)
    nz = pairings(np.array(Y6), ech)
    inspan = v.rank_modp(nulls + Y6) == len(nulls) if nulls else False
    OUT["k2l1"] = {
        "n_vec": len(Y6),
        "cut": cuth + cuta,
        "blocks": blocks6,
        "rank": info["rank"],
        "hist": info["rank_history"],
        "nulls": len(nulls),
        "per_block": per_block(ech, rows),
    }
    # fix pass 2 (critic iteration 2, #6): the rank must equal 67 (the claim of
    # G3.7: the 6 rows of (F.9) at L = 1 are the whole cokernel), not only <= 67,
    # and the left-null space must have dimension exactly 6
    report(
        "G3.7-K2L1-rank",
        info["rank"] == len(rows) - 6
        and len(info["rank_history"]) >= 2
        and info["rank_history"][-1] == info["rank_history"][-2],
        f"alpha'_v=1/2, gamma'=3, K=2, L=1, d=2: rank {info['rank']}/{len(rows)} "
        f"(rank history {info['rank_history']}, {info['columns_used']} columns, "
        f"{info['pairs_per_delta']} pairs per Delta; predicted = {len(rows) - 6}, "
        f"saturated; 73 would refute the law, < 67 an extra relation); per block "
        f"{per_block(ech, rows)}",
    )
    report(
        "G3.7-K2L1-annihilate",
        len(Y6) == 6
        and blocks6 == {"2,2": 6}
        and nz == 0
        and inspan
        and len(nulls) == 6,
        f"phi = 1 relations c_-2 (c_1 (x) chi_2) and conjugates: {len(Y6)} vectors "
        f"(cut by truncation {cuth + cuta}), block ranks {blocks6}; "
        f"{nz} non-zero pairings with the L=1 image; in its left-null space "
        f"({len(nulls)} vectors, must be 6): {inspan}",
    )
    # break leg: the same rows pair non-zero with L = 2 columns (c_2 acts on b_-2)
    vx2 = vertex(HALF, Fraction(3), K, 2)
    amps2 = v.Amplitudes(vx2, d, v.Field(PMOD))
    ins2 = v.input_basis(2, d)
    D = tuple(rng.randrange(PMOD) for _ in range(d))
    pairs = [(rng.randrange(len(ins2)), rng.randrange(len(ins2))) for _ in range(100)]
    cols = columns(amps2, ins2, pairs, P, D, rows)
    nzb = nz_pair(Y6, cols)
    report(
        "BREAK-G3.7-L2",
        nzb > 0,
        f"the 6 vectors x 100 random L=2 columns: {nzb} non-zero pairings "
        f"(must be > 0: c_2 acts on inputs with b_-2)",
    )


def run_c44a(rng) -> None:
    """F1(b), other vertices: the 44 vectors vanish on L = 2 columns at any alpha'_v, gamma'."""
    K, L, d = 4, 2, 2
    rows = x.even_rows(K, d)
    ins = v.input_basis(L, d)
    for av, g in ((Fraction(1, 5), Fraction(2)), (Fraction(0), Fraction(3))):
        vx = vertex(av, g, K, L)
        amps = v.Amplitudes(vx, d, v.Field(PMOD))
        z2 = zsq(vx)
        yh, ya, _, _ = c44_vectors(rows, z2)
        fh, fa, _, _ = c44_vectors(rows, z2, sgn=+1)
        P = tuple(rng.randrange(PMOD) for _ in range(d))
        D = tuple(rng.randrange(PMOD) for _ in range(d))
        pairs = [(rng.randrange(len(ins)), rng.randrange(len(ins))) for _ in range(150)]
        t0 = time.time()
        cols = columns(amps, ins, pairs, P, D, rows)
        nz, nzf = nz_pair(yh + ya, cols), nz_pair(fh + fa, cols)
        tag = f"{av}-{g}".replace("/", "_")
        OUT[f"c44a_{tag}"] = {"P": P, "nz": nz, "nz_flip": nzf, "n": len(yh + ya)}
        report(
            f"G3.5-alpha-{tag}",
            len(yh + ya) == 44 and nz == 0,
            f"alpha'_v={av}, gamma'={g}, K=4, d=2: the {len(yh + ya)} vectors (F.7) x "
            f"150 random L=2 columns: {nz} non-zero pairings ({time.time() - t0:.1f} s)",
        )
        report(
            f"BREAK-G3.5-alpha-flip-{tag}",
            nzf > 0,
            f"same with c_-4 + z^2 c_-2: {nzf} non-zero pairings (must be > 0)",
        )


def run_c44(rng, saturate: bool = False) -> None:
    """F1(b), (d): the 44 vectors against the K = 4, L = 2 image at a fresh momentum.

    saturate=False (part c44): the scan stops at rank 2882, so the left-null
    space is that of a partial image. saturate=True (part c44s): the scan runs
    until a Delta sample adds nothing (record 078's rule), so the null space is
    that of the saturated image and the deficit is measured at a third momentum.
    """
    K, L, d = 4, 2, 2
    vx = vertex(HALF, Fraction(3), K, L)
    amps = v.Amplitudes(vx, d, v.Field(PMOD))
    rows = x.even_rows(K, d)
    ins = v.input_basis(L, d)
    z2 = zsq(vx)
    yh, ya, labels, cut = c44_vectors(rows, z2)
    fh, fa, _, _ = c44_vectors(rows, z2, sgn=+1)
    Y44, F44 = yh + ya, fh + fa
    rk44 = v.rank_modp(Y44)
    br = block_ranks(Y44, rows)
    want = {"2,2": 6, "2,4": 22, "4,2": 22, "4,4": 38}
    OUT["c44_vectors"] = {"n": len(Y44), "rank": rk44, "blocks": br, "cut": cut}
    report(
        "G3.5-count",
        len(yh) == len(ya) == 22 and rk44 == 44 and br == want,
        f"(F.7) at K=4, d=2: {len(yh)} + {len(ya)} vectors, rank {rk44}, block "
        f"projection ranks {br} (predicted (F.8) {want}); cut by truncation {cut}",
    )
    P = tuple(rng.randrange(PMOD) for _ in range(d))
    OUT["P_c44"] = P
    if saturate:
        ech, info = scan(amps, rows, ins, rng, P, len(rows), max_delta=3, tag="c44s")
        hist = info["rank_history"]
        # fix pass 2 (#6): the saturated rank must be 2927 - 45 = 2882 (the 45
        # exact relations (F.6), (F.13) bound it from above at every P), not any
        # saturated value below 2927
        report(
            "G3.9-P3-saturated",
            len(hist) >= 2 and hist[-1] == hist[-2] and info["rank"] == len(rows) - 45,
            f"third momentum {P}: K=4, L=2 rank {info['rank']}/2927 mod p, rank "
            f"history {hist} ({info['columns_used']} columns, {info['time_s']} s, "
            f"peak rss {rss_mb()} MB)",
        )
    else:
        ech, info = scan(amps, rows, ins, rng, P, 2882, max_delta=2, tag="c44")
    nz, nzf = pairings(np.array(Y44), ech), pairings(np.array(F44), ech)
    report(
        "G3.5-annihilate",
        nz == 0 and info["rank"] >= 2882,
        f"fresh momentum {P}: L=2 image rank {info['rank']}/2927 after "
        f"{info['columns_used']} columns ({info['time_s']} s, peak rss {rss_mb()} MB); "
        f"44 vectors x {info['rank']} image vectors: {nz} non-zero pairings",
    )
    report(
        "BREAK-G3.5-flip",
        nzf > 0,
        f"c_-4 + z^2 c_-2 instead: {nzf} non-zero pairings (must be > 0)",
    )
    nulls = v.left_null(ech)
    r_all = v.rank_modp(nulls + Y44)
    report(
        "G3.5-in-null",
        r_all == len(nulls) and rk44 == 44,
        f"left-null space {len(nulls)} vectors; rank of (null space + 44 vectors) "
        f"{r_all} (= {len(nulls)}: the 44 lie in it); complement "
        f"{len(nulls) - rk44}",
    )
    # fix pass 2 (critic iteration 2, #4(a)): (F.13) over the whole image. y45
    # must lie in the left-null space (rank stays 45); with -z^2 it must not
    # (rank 46). At c44 the image at rank 2882 is complete (2882 is a proven
    # upper bound at every P), so this tests (F.13) on every column.
    y45, y45f = y45_vector(rows, z2), y45_vector(rows, z2, sgn=-1)
    r45 = v.rank_modp(nulls + Y44 + [y45])
    r45f = v.rank_modp(nulls + Y44 + [y45f])
    OUT[f"c44_y45_in_null_{'s' if saturate else 'p'}"] = {"r45": r45, "r45_flip": r45f}
    report(
        "G3.9-y45-in-null",
        len(nulls) == 45 and r45 == 45,
        f"rank of (left-null space + 44 vectors + (c_-3 cb_-3 + z^2 c_-2 cb_-2)|0>) "
        f"{r45} (must be 45 = dim of the left-null space {len(nulls)}: (F.13) "
        f"annihilates the whole image)",
    )
    report(
        "BREAK-G3.9-y45-in-null-flip",
        r45f == 46,
        f"same with c_-3 cb_-3 - z^2 c_-2 cb_-2: rank {r45f} (must be 46)",
    )
    # (d) projection of the left-null space on the blocks with N = 4 or Nbar = 4
    blk = [(st["N"], st["Nb"]) for st in rows]
    i4 = [q for q in range(len(rows)) if 4 in blk[q]]
    ib4 = [q for q in range(len(rows)) if blk[q][1] == 4]
    r4 = v.rank_modp([y[i4] for y in nulls])
    rb4 = v.rank_modp([y[ib4] for y in nulls])
    report(
        "G3.8-proj-N4",
        r4 == len(nulls),
        f"rank of the left-null space projected on the blocks with N=4 or Nbar=4: "
        f"{r4} (must be {len(nulls)}: K=3, L=2 is onto, so no null vector lives "
        f"on W_<=3)",
    )
    report(
        "G3.8-proj-Nb4",
        rb4 == len(nulls) - 3,
        f"projected on Nbar=4 only: {rb4} (predicted {len(nulls)} - 3: the 3 "
        f"holomorphic vectors with chi at level 2 live on (4,2), (2,2))",
    )
    # the 45th relation: reduce the null space modulo the span of the 44
    e44 = v.Echelon(len(rows))
    for y in Y44:
        e44.add(y)
    extra = []
    for y in nulls:
        w = y % PMOD
        for p_, b in e44.piv.items():
            if w[p_]:
                w = (w - w[p_] * b) % PMOD
        if np.any(w) and e44.add(w.copy()):
            extra.append(w)
    sup = {}
    lab33 = []
    for y in extra:
        for q in np.nonzero(y)[0]:
            key = f"{blk[q][0]},{blk[q][1]}"
            sup[key] = sup.get(key, 0) + 1
            if blk[q] == (3, 3):
                lab33.append(v.row_label(rows[q]))
    charges = {}
    for y in extra:
        for q in np.nonzero(y)[0]:
            st = rows[q]
            qh = sum(1 if t == "c" else -1 for c_, t, _ in st["gh"] if c_ == 0)
            qa = sum(1 if t == "c" else -1 for c_, t, _ in st["gh"] if c_ == 1)
            kk = f"({blk[q][0]},{blk[q][1]}) q=({qh},{qa})"
            charges[kk] = charges.get(kk, 0) + 1
    OUT["c44_extra"] = {
        "n": len(extra),
        "support_per_block": sup,
        "labels_33": lab33[:60],
        "charges": charges,
    }
    report(
        "G3.9-complement",
        len(extra) == len(nulls) - 44,
        f"null space modulo the 44: {len(extra)} vector(s); support per block {sup}; "
        f"rows by (block, chiral charges) {charges}",
    )
    print(f"  (3,3) rows of the extra vector(s): {lab33[:40]}", flush=True)
    # explicit form of the extra vector(s) when the support is small: labels and
    # coefficients normalised to the first entry, with a rational reconstruction
    explicit = []
    for y in extra:
        nzq = list(np.nonzero(y)[0])
        if len(nzq) > 12:
            explicit.append({"support": len(nzq)})
            continue
        c0 = pow(int(y[nzq[0]]), PMOD - 2, PMOD)
        explicit.append(
            {v.row_label(rows[q]): ratrec(int(y[q]) * c0 % PMOD) for q in nzq}
        )
    OUT["c44_extra"]["explicit"] = explicit
    print(f"  extra vector(s), normalised: {explicit}", flush=True)
    # (F.10): level-3 columns; the 44 vanish unless an input contains b_-3 / bt_-3
    ins3 = v.input_basis(3, d)
    hb = [any(o == (0, "b", -3) for o in st["gh"]) for st, _ in ins3]
    ab = [any(o == (1, "b", -3) for o in st["gh"]) for st, _ in ins3]
    lev3 = [q for q, (st, _) in enumerate(ins3) if st["N"] == 3]
    plain = [q for q in range(len(ins3)) if not hb[q] and not ab[q]]
    l3p = [q for q in lev3 if not hb[q] and not ab[q]]
    hq = [q for q in lev3 if hb[q] and not ab[q]]
    aq = [q for q in lev3 if ab[q] and not hb[q]]
    D = tuple(rng.randrange(PMOD) for _ in range(d))
    nset = 80
    sets = {
        "no_b3": [(rng.choice(l3p), rng.choice(plain)) for _ in range(nset)],
        "hol_b3": [(rng.choice(hq), rng.choice(plain)) for _ in range(nset)],
        "ah_b3": [(rng.choice(aq), rng.choice(plain)) for _ in range(nset)],
    }
    res = {}
    for name, prs in sets.items():
        cols = columns(amps, ins3, prs, P, D, rows)
        res[name] = (nz_pair(yh, cols), nz_pair(ya, cols))
    OUT["c44_L3"] = {
        "level3_inputs": len(lev3),
        "with_b3": sum(hb[q] for q in lev3),
        "with_bt3": sum(ab[q] for q in lev3),
        "pairings (hol, antihol)": res,
    }
    ok = (
        res["no_b3"] == (0, 0)
        and res["hol_b3"][0] > 0
        and res["hol_b3"][1] == 0
        and res["ah_b3"][0] == 0
        and res["ah_b3"][1] > 0
    )
    report(
        "G3.6-L3-pattern",
        ok,
        f"level-3 inputs {len(lev3)} (with b_-3: {sum(hb[q] for q in lev3)}, with "
        f"bt_-3: {sum(ab[q] for q in lev3)}); non-zero pairings (22 hol, 22 antihol) "
        f"x {nset} columns per set: {res} (predicted (F.10): no_b3 (0, 0); hol_b3 "
        f"(>0, 0); ah_b3 (0, >0))",
    )


def y45_vector(rows: list[dict], z2: int, sgn: int = 1) -> np.ndarray:
    """(F.13): e[c_-3 cbar_-3 |0>] + z^2 e[c_-2 cbar_-2 |0>] on the engine's rows.

    The rows are b_-1 c_-n bbar_-1 cbar_-n c_1 cbar_1|0> = c_-n cbar_-n |0>
    (n = 2, 3; sign +1 from b_-1 c_1|0> = |0> in each chirality).
    """
    pos = {(st["mat"], st["gh"]): r for r, st in enumerate(rows)}
    y = np.zeros(len(rows), dtype=np.int64)
    for n, cf in ((3, 1), (2, sgn * z2)):
        key = ((), ((0, "b", -1), (0, "c", -n), (1, "b", -1), (1, "c", -n)))
        y[pos[key]] = cf % PMOD
    return y


def rnn_vector(rows: list[dict], n: int) -> np.ndarray:
    """e[R_nn]: the single row b_-1 c_-n bbar_-1 cbar_-n c_1 cbar_1|0> = c_-n cbar_-n|0>."""
    pos = {(st["mat"], st["gh"]): r for r, st in enumerate(rows)}
    y = np.zeros(len(rows), dtype=np.int64)
    y[pos[((), ((0, "b", -1), (0, "c", -n), (1, "b", -1), (1, "c", -n)))]] = 1
    return y


def run_c45(rng, targeted: bool = False) -> None:
    """F1(b'): the 45th relation (F.13) on L <= 2 and level-3 columns.

    targeted=False (part c45, first attempt; retired in fix pass 2, no longer
    dispatched): random pairs. The rows of (F.13) are non-zero only on columns
    with b_-2 in one input and bbar_-2 in the other (B, C of (F.12)), which
    random pairs rarely hit (about one column in 150), so the break legs were
    vacuous there (FAIL). targeted=True (part c45t): L <= 2 pairs (input with
    b_-2, input with bbar_-2); level-3 pairs with an input that contains both
    b_-2 and bbar_-2 (A != 0) or b_-3 (double pole). Fix pass 2: at alpha'_v != 0
    the check G3.9-y45-* also requires e[R_33] non-zero on some column (a
    vacuous sample fails it), with two break legs (-flip: sign of z^2; -L3:
    level-3 columns); at alpha'_v = 0 the check is G3.9-alpha0-rows-vanish.
    """
    K, d = 4, 2
    rows = x.even_rows(K, d)
    ins = v.input_basis(2, d)
    ins3 = v.input_basis(3, d)
    lev3 = [q for q, (st, _) in enumerate(ins3) if st["N"] == 3]

    def has(st, o):
        return o in st["gh"]

    hb2 = [q for q, (st, _) in enumerate(ins) if has(st, (0, "b", -2))]
    ab2 = [q for q, (st, _) in enumerate(ins) if has(st, (1, "b", -2))]
    both3 = [
        q
        for q in lev3
        if has(ins3[q][0], (0, "b", -2)) and has(ins3[q][0], (1, "b", -2))
    ]
    hb3 = [q for q in lev3 if has(ins3[q][0], (0, "b", -3))]
    ab2_3 = [q for q, (st, _) in enumerate(ins3) if has(st, (1, "b", -2))]
    OUT["c45_inputs"] = {
        "b-2": len(hb2),
        "bt-2": len(ab2),
        "level3 with b-2 and bt-2": len(both3),
        "level3 with b-3": len(hb3),
    }
    for av, g in (
        (HALF, Fraction(3)),
        (Fraction(1, 5), Fraction(2)),
        (Fraction(0), Fraction(3)),
    ):
        vx = vertex(av, g, K, 3)
        amps = v.Amplitudes(vx, d, v.Field(PMOD))
        z2 = zsq(vx)
        y, yf = y45_vector(rows, z2), y45_vector(rows, z2, sgn=-1)
        P = tuple(rng.randrange(PMOD) for _ in range(d))
        D = tuple(rng.randrange(PMOD) for _ in range(d))
        if targeted:
            pairs = [(rng.choice(hb2), rng.choice(ab2)) for _ in range(150)]
            pairs3 = [(rng.choice(both3), rng.randrange(len(ins3))) for _ in range(75)]
            pairs3 += [(rng.choice(hb3), rng.choice(ab2_3)) for _ in range(75)]
        else:
            pairs = [
                (rng.randrange(len(ins)), rng.randrange(len(ins))) for _ in range(150)
            ]
            pairs3 = [(rng.choice(lev3), rng.randrange(len(ins3))) for _ in range(150)]
        cols = columns(amps, ins, pairs, P, D, rows)
        cols3 = columns(amps, ins3, pairs3, P, D, rows)
        nz, nzf = nz_pair([y], cols), nz_pair([yf], cols)
        nz3 = nz_pair([y], cols3)
        # the two rows separately: e[R_33] = e[c_-2 cb_-2|0>], e[R_44] = e[c_-3 cb_-3|0>]
        e33, e44 = rnn_vector(rows, 2), rnn_vector(rows, 3)
        n33, n44 = nz_pair([e33], cols), nz_pair([e44], cols)
        n33_3, n44_3 = nz_pair([e33], cols3), nz_pair([e44], cols3)
        tag = f"{av}-{g}".replace("/", "_") + ("-t" if targeted else "")
        OUT[f"c45_{tag}"] = {
            "P": P,
            "nz": nz,
            "nz_flip": nzf,
            "nz_L3": nz3,
            "R33 (L<=2, L3)": (n33, n33_3),
            "R44 (L<=2, L3)": (n44, n44_3),
        }
        kind = "targeted" if targeted else "random"
        if av != 0:
            # fix pass 2 (critic iteration 2, #4(b)): non-vacuity count in the
            # check (the sample must reach the rows: e[R_33] non-zero on some
            # column), and the break conjunction split into two legs
            report(
                f"G3.9-y45-{tag}",
                nz == 0 and n33 > 0,
                f"alpha'_v={av}, gamma'={g}, K=4, d=2: (c_-3 cb_-3 + z^2 c_-2 "
                f"cb_-2)|0> x 150 {kind} L<=2 columns: {nz} non-zero pairings; "
                f"e[R_33] non-zero on {n33} of them (must be > 0: non-vacuous "
                f"sample), e[R_44] on {n44}",
            )
            report(
                f"BREAK-G3.9-y45-{tag}-flip",
                nzf > 0,
                f"with -z^2: {nzf} non-zero pairings (must be > 0)",
            )
            report(
                f"BREAK-G3.9-y45-{tag}-L3",
                nz3 > 0,
                f"(F.13) on 150 columns with a level-3 input: {nz3} non-zero "
                f"(must be > 0)",
            )
        else:
            # fix pass 2 (#4(c)): at alpha'_v = 0 each row c_-n cb_-n|0> is by
            # itself a left-null vector for inputs of every level (R84's identity
            # (4.3) on chi = c_-n cb_-n c_1|0>: the O_b functional is e[R_nn]),
            # so y45 vanishes trivially there (logging line) and the check is
            # that the two rows vanish separately on L <= 2 and level-3 columns
            print(
                f"INFO  G3.9-y45-{tag}: alpha'_v={av}, gamma'={g}, K=4, d=2: "
                f"(c_-3 cb_-3 + z^2 c_-2 cb_-2)|0> x 150 {kind} L<=2 columns: {nz} "
                f"non-zero pairings; with -z^2: {nzf}; level-3 columns: {nz3} "
                "(logging line, not a check: both rows vanish separately here)",
                flush=True,
            )
            report(
                "G3.9-alpha0-rows-vanish",
                n33 == 0 and n44 == 0 and n33_3 == 0 and n44_3 == 0,
                f"alpha'_v=0, gamma'={g}, K=4, d=2: non-zero pairings of e[R_33], "
                f"e[R_44] with 150 {kind} L<=2 columns: ({n33}, {n44}); with 150 "
                f"columns with a level-3 input: ({n33_3}, {n44_3}) (all must be 0: "
                f"R84 (4.3) at alpha'_v=0)",
            )


def main() -> None:
    which = sys.argv[1:] or ["dim", "i", "ii", "iv"]
    budget, n_delta = 4000, 1
    for a in which:
        if a.startswith("budget="):
            budget = int(a.split("=")[1])
        if a.startswith("ndelta="):
            n_delta = int(a.split("=")[1])
    global SCRATCH  # noqa: PLW0603
    if any(a in NEW_PARTS for a in which):
        # fix-pass parts write to their own scratch directory (record 093 fix)
        SCRATCH = SCRATCH_FIX
    print(f"seed = {SEED}, p = {PMOD}, beta = 3/2, parts {which}", flush=True)
    t0 = time.time()
    for part, fn in (
        ("dim", lambda r: run_dim()),
        ("den", lambda r: run_den()),
        ("i", run_i),
        ("i0", lambda r: run_i0(r, budget)),
        ("ii", run_ii),
        ("ii0", lambda r: run_ii0(r, budget, n_delta)),
        ("smoke", run_smoke),
        ("iii", run_iii),
        ("iv", run_iv),
        ("k2l1", run_k2l1),
        ("c44a", run_c44a),
        ("c44", run_c44),
        ("c44s", lambda r: run_c44(r, saturate=True)),
        ("c45t", lambda r: run_c45(r, targeted=True)),
    ):
        if part in which:
            print(f"--- part {part}: rng seed '{SEED}-{part}'", flush=True)
            fn(random.Random(f"{SEED}-{part}"))
            OUT[f"rss_after_{part}_mb"] = rss_mb()
            save()
    nfail = sum(1 for _, ok, _ in RESULTS if not ok)
    print(
        f"SUMMARY: {len(RESULTS) - nfail}/{len(RESULTS)} PASS "
        f"({time.time() - t0:.0f} s, peak rss {rss_mb()} MB)",
        flush=True,
    )
    sys.exit(1 if nfail else 0)


if __name__ == "__main__":
    main()
