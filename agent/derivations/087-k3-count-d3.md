# 087 — The $K=3$ cokernel of the PH31 rank test at $d_{\rm eff}=3$ (R84)

Brief: `agent/briefs/active-computator-087-k3-count-d3-20261004T153500.md` (numerical scan, time box 75 min).
Model: claude/opus. Date: 2026-10-04.

## Status

Partial (16:40): items (i), (iii), (iv) and the closure of (ii) done; the $L$-alone count and the $L$/mixed split of (ii) not obtained. Final run of `codes/verify-ph31-rank-k3d3.py` 19/19 PASS (16:24–16:34, single process). Not done: the $L$-alone count at $d=3$ and hence the $L$/mixed split (elimination > 20 min, §3 run 2); the joint count over $\mathbb Q$ at a rational momentum. Fix pass for critic iteration 1 (text only, no script run): see `## Fix pass (critic iteration 1)`. Next step: none for the computator (promotion of the R84 lines of the last section, with the critic's text, orchestrator's call).

## Task and objective

**Literal task.** At $K=3$, $d_{\rm eff}=3$, $\alpha'_{\rm v}=0$ ($\beta=3/2$, $\gamma'=3$): (i) the block dimension $\dim W^{\rm even}_{\le3}$; (ii) the rank of the level-projected circle map at $L=2$ (mod $p$, random momentum, 078's method) and whether the cokernel equals the span of the relations of the two identities (4.3) of 078 ($b$, $L$, mixed counts as 083 §4); (iii) a machine check of the critic's factorisation bound $b$-count $\ge34+3(d^2-4)=49$ at $d=3$, and the matter-vacuum diagnostic (critic 083 #5); (iv) a control at $\alpha'_{\rm v}=\tfrac12$ (full rank expected).

**Objective.** R84 states its $K=3$ number (60/487) for $d_{\rm eff}=2$ only, and its Scope asserts $d$-dependence at $K=3$ on an unchecked hand argument. Decide which of two readings holds at $d=3$: the two identities still generate the whole cokernel (the selection-rule reading of R84 extends, with a checked count formula), or there are relations beyond them (a new mechanism that bears on PH31's status and the model's $\alpha'_{\rm v}$). R84's refutation of PH31 does not depend on this run.

## Conventions and assumptions

- **A1–A5** of 078 unchanged (the project conventions: physical ghost number, book normalisation; vertex $\beta=3/2$, $\gamma'=3$; Euclidean matter truncation to $d_{\rm eff}$ components; $\mathcal H_0$ symmetric inputs; finite levels), with $d_{\rm eff}=3$ and $K=3$, $L=2$ here; mode cutoff $M=4$ (as 083 at $K=3$).
- Engine: `codes/verify-ph31-rank-ext.py` (relation count, split, annihilation) and `codes/verify-ph31-rank.py` (amplitudes, bases, echelon), both imported unchanged by `codes/verify-ph31-rank-k3d3.py`.

## Claim tree

087 extends 083's claim tree (E1, E3) and 078's (C3, C4); its nodes are numbered D0–D4.

- **A1–A5** of 078, with $d_{\rm eff}=3$, $K=3$, $L=2$, mode cutoff $M=4$; random momentum $P\in\mathbb F_p^3$, $p=2^{31}-1$.
- **D0** (root) At $\alpha'_{\rm v}=0$, $\beta=3/2$, $\gamma'=3$, $K=3$, $d_{\rm eff}=3$: the level-projected circle map has rank 1340 on $\dim W^{\rm even}_{\le3}=1447$ for every $L\ge2$ at the sampled momentum (over $\mathbb F_p$ at the scan point, with no exact closure over $\mathbb Q$ at a rational point, unlike $d_{\rm eff}=2$; at generic $P$ rank $\ge1340$, and $=1340$ with failure probability $\le18240/p$, $p=2^{31}-1$ not checked to be a good prime), and its cokernel, 107, is exactly the joint span of the relations of the two identities (4.3): no relation beyond them. The $b$-part, 61, factorises over matter monomials of every level pair, $b(3,d)=4d^2+7d+4$ for every $d$ (derived; machine-checked at $d\le3$); the critic's bound 49 holds. At $\alpha'_{\rm v}=\tfrac12$ the map is onto. [by D1–D4]
  - **D1** $\dim W^{\rm even}_{\le3}=1447$ at $d=3$ (blocks §2). [by check: D1-dim]
  - **D2** The $b$-relations at $K=3$. [by D2.1–D2.3]
    - **D2.1** The $b$-relation space factorises over matter monomials, $b(K,d)=\sum_{a,\bar a}n_d(a)n_d(\bar a)\,r_K(a,\bar a)$, the sum running over all $(a,\bar a)$, odd $a-\bar a$ included. [by A1 ($O_b$ acts on ghosts only); §5 Structure; §5 Second route (critic's hand derivation of the ghost counts)] [check: D2-factorisation-d1, D2-factorisation-d2, D2-factorisation-d3, BREAK-D2-even-only]
    - **D2.2** $r_3$: $(0,0)$ 4, $(1,0),(0,1)$ 2, $(2,0),(0,2)$ 1, $(1,1)$ 3, others 0; $b(3,d)=4d^2+7d+4$ for every $d$ (derived; machine-checked at $d\le3$), i.e. 15, 34, 61 at $d=1,2,3$ (61 also over $\mathbb Q$, $P$-independent), $\ge49$. [by D2.1; §5 Second route (the critic's hand derivation of $r_3$); by check: D2-factorisation-d1, D2-factorisation-d2, D2-factorisation-d3, D2-b-Q, D2-bound]
    - **D2.3** $b(2,d)=3$ for every $d$. [by D2.1, 083 E3 ($b$-count 3 at $d=2,3$); §5 $K=2$; §5 Second route ($r_2$)]
  - **D3** At $\alpha'_{\rm v}=0$, $K=3$, $d=3$ the cokernel is the joint span of (4.3)'s relations, 107, at every $L\ge2$. [by D3.1–D3.3]
    - **D3.1** (4.3) gives 107 independent relations on $W^{\rm even}_{\le3}$ ($k_\chi=4$); they are left-null vectors of the projected map for every $\Delta$ and every input level. [by R84 (identities (4.2)–(4.3), Proven); by check: D3-rank (the identity $1340+107=1447$ fixes the count 107), D3-annihilate (independence of the 107 on the rows, `r_j == len(rels)`, and left-null on the measured image)] [check: BREAK-D3-b, D3-pairing-engine]
    - **D3.2** At the scan point, rank $\ge1340$ at $L=2$. [by check: D3-rank] [check: D3-post-stop]
    - **D3.3** Generic $P$: rank $\ge1340$, and $=1340$ with failure probability $\le18240/p\approx8.5\times10^{-6}$ ($p=2^{31}-1$ not checked to be a good prime; over $\mathbb F_p$, no rational-point closure). [by D3.1, D3.2, 083 §4 item 3 (degree bound: the $L$-functionals are affine in $P$, 18240 of them)]
    - **D3.4** The 61 $b$-alone relations lie in the joint span; $L$-alone + mixed $=46$. [by check: D3-b-in-joint]
    - **D3.5** The $L$-functionals of matter-vacuum $\chi$, added to all $b$-functionals, give no relation beyond $b$ at $K=2$ ($d=2,3$) and 2 at $K=3$ ($d=2,3$): the two mixed relations at $K=2$, and 24 of 26 ($d=2$) and 44 of 46 ($d=3$) non-$b$ relations at $K=3$, need $L$-functionals of matter-excited $\chi$ (§6). [by check: D3-mv-2-2, D3-mv-2-3, D3-mv-3-2, D3-mv-3-3]
  - **D4** At $\alpha'_{\rm v}=\tfrac12$, $K=3$, $L=2$, $d=3$ the map is onto (1447/1447). [by check: D4-alpha-half]

Open gaps: none
Hypotheses in force: none

## Fix pass (critic iteration 1)

Source: `agent/reports/critic-087-20261004T164100.md` (verdict: ACCEPT after mechanical edits; the numbers 1447, 1340, 107, 61, the closure and the factorisation stand).
Text-only pass (started 16:55): no script run, no script or ledger edit, no number changed.
One line per finding; the table of changed nodes and the dependents follow.

- **#3** (§4 Reading (c), "86 straddle several"): applied, critic's text verbatim: the relations supported in a single block span 21 dimensions, the other 86 dimensions have no single-block representative. Only a wording of §4 Reading (c); no node changed.
- **#4** (node D3.5, "mixed relations need matter-excited $\chi$"): applied, critic's replacement of the node's tail: "the two mixed relations at $K=2$, and 24 of 26 ($d=2$) and 44 of 46 ($d=3$) non-$b$ relations at $K=3$, need $L$-functionals of matter-excited $\chi$ (§6)". D3.5 *statement* changed (narrowed to what §6 shows: at $K=3$ the 2 extra relations of the matter-vacuum $L$-functionals are not assigned to $L$-alone or mixed); justification and checks unchanged; no node cites D3.5, D0 does not use this content.
- **#6** (Status: partial, the $L$/mixed split not obtained): applied, critic's wording: "Partial (16:40): items (i), (iii), (iv) and the closure of (ii) done; the $L$-alone count and the $L$/mixed split of (ii) not obtained", rest of the line kept (plus the pointer to this section). No node changed (the split is not a node of the tree; `Open gaps:` stays none).
- **#7** (§7 item 1 and Self-review 4: "three" points listing four): applied, critic's wording at both places: "at the four tested points ($K=2$: $d=2,3$, the cokernel staying at 5; $K=3$: $d=2,3$), the $K=3$ cokernel growing with $d$ (60 → 107)" (§7 item 1) and "Four data points of exact closure" (Self-review 4, same parenthesis). The $K=2$ cokernel stays at 5 (as the brief asked). No node changed.
- **#11** (tags only, D3.1: `D3-relations` asserts only $>0$): applied. D3.1 now reads "[by R84 (identities (4.2)–(4.3), Proven); by check: D3-rank, D3-annihilate] [check: BREAK-D3-b, D3-pairing-engine]": the count 107 is fixed by `D3-rank` ($1340+107=1447$), the independence of the 107 relations and their annihilation of the image by `D3-annihilate` (`r_j == len(rels)`, 0 of $107\times1340$ pairings). `D3-relations` is dropped as evidence and its weakness is stated in the Verification block. Script untouched. D3.1 *justification* changed only.
- **#12** (Verification *Falsifiability* bullet 1 and Self-review 2 bullet 1: the early stop): applied, critic's wording. Bullet 1 now says the scan stops at $\dim-n_{\rm rel}$, so `D3-rank` fails for an undercount of relations and cannot catch an overcount, which `D3-post-stop` (400 columns, counted in `D3-rank`) and `D3-annihilate` do; "independent pipelines" is kept only with that qualification. Self-review 2: "the exact meeting with the scan's rank, which reaches the relation bound (an undercount would have kept it below)". No node changed.
- **#5** (proposed R84 Status line, qualifiers): applied. The record's proposed R84 lines are replaced, in the last section, by the critic's *R84 text I would accept* copied verbatim (checked by `diff` against the critic's report): the Status clause keeps "over $\mathbb F_p$ at the sampled momentum", "no rational-point closure", "$p=2^{31}-1$ not a bad prime (unchecked)", and the new Verification line and the selection-rule paragraph are the critic's. The same qualifiers are carried by the body: D0, D3.3 and §7 item 1 now say "over $\mathbb F_p$ at the scan point, no exact closure over $\mathbb Q$ at a rational point, unlike $d_{\rm eff}=2$ (083 §4)" and "$p=2^{31}-1$ not checked to be a good prime" (the earlier text said "$p$ not a bad prime", which could be read as asserted). No number changed.
- **#8** (proposed R84 Scope text): applied, same replacement: the critic's full Scope text replaces the parenthesis from "matter with $d_{\rm eff}=2$ components" up to "so 60/487 is a $d_{\rm eff}=2$ number)" (a replacement, not an insertion, so "matter with" is not duplicated), and the wrong reason "at $K=2$ no matter excitation fits the level budget" is recorded as wrong in the lead paragraph of that section.
- **#2** (optional, §5 second route): applied. §5 gains the paragraph "Second route (the critic's hand derivation, critic 087 C2)": contracting homotopy $h=-c_{-1}/z^2$, $R_b=\ker O_b\cap I$, adapted basis $1,b_{-1},c_{-1},b_{-1}c_{-1}-z^2$, the pair count, the 16 $r_3$ and $r_2$; cited as the critic's, no number changes. It is not machine-checked (the critic's own computation, read by this pass and not re-run). D2.1, D2.2, D2.3 cite it as a second route; D0 and D2.2 now read "$b(3,d)=4d^2+7d+4$ for every $d$ (derived; machine-checked at $d\le3$)", the wording the critic proposed.

**Changed nodes.**

| Node | Change | Kind |
|---|---|---|
| D3.1 | tags: `D3-relations` dropped, `D3-rank`, `D3-annihilate` cited (#11) | justification only |
| D3.5 | tail narrowed to what §6 shows (#4) | statement |
| D3.3 | "$p=2^{31}-1$ not checked to be a good prime; over $\mathbb F_p$, no rational-point closure" (#5) | wording of the existing caveat |
| D2.1, D2.3 | §5 second route added as a support (#2) | justification only |
| D2.2 | "for every $d$ (derived; machine-checked at $d\le3$)" (#2) | statement made explicit: the earlier text gave the formula at $d\le3$ in the node and used it at $d=26$ in §5 and §7 |
| D0 | qualifiers of the $d_{\rm eff}=3$ rank statement made explicit (#5); $b$-count "for every $d$ (derived; machine-checked at $d\le3$)" (#2) | wording; the numbers 1447, 1340, 107, 61 and the closure are unchanged |

**Dependents.** D3.1 → D3 → D0: the justification changed, the statement did not, all three hold as written. D3.5: no node cites it (D3 cites D3.1–D3.3, D0 cites D1–D4), the narrowing affects only §6's reading. D2.2 → D2 → D0: D2 cites D2.1–D2.3 and holds; D0 is updated to match D2.2. D2.1, D2.3: statements unchanged. D1, D4, D3.2, D3.4: untouched. By the schema's criterion the root statement counts as changed only through the explicit-qualifier wording of D0 and the $b$-count scope of D2.2/D0; the critic ruled that no further critic pass is needed (an orchestrator self-confirmation suffices), and this pass does not widen any numerical or physical claim.

Open gaps: none (unchanged). Hypotheses in force: none (unchanged). Restatements updated: Status, D0, D3.3, §7 items 1–3, Verification *Falsifiability*, Self-review 2 and 4, the last section (R84 lines). The checks of `codes/verify-ph31-rank-k3d3.py` are unchanged and were not re-run.

## §1 Size estimate of the $K=3$, $d=3$ run (written before the run)

- Rows: $\dim W^{\rm even}_{\le3}(d=3)=1447$ (generating function, `v.gf_count`; blocks below), against 487 at $d=2$ and 164 at $K=2$, $d=3$.
- Inputs: $\mathcal H_0$ at $L=2$, $d=3$: 230 states. The column of a pair is symmetric in the two inputs (`scan` adds the two orderings), so the unordered pairs suffice: $230\cdot231/2=26565$ columns per $\Delta$ (083 used all 52900 ordered pairs, each column twice).
- Per entry: 083's timings give $\approx10\,\mu$s per (column, row) at $K=3$, $d=2$ (101 s for $20402\times487$) and $\approx13\,\mu$s at $K=2$, $d=3$ (232 s for $105800\times164$), amplitude and elimination included. At 1447 rows the elimination grows with the rank (one vector operation per pivot, $\approx1400$ pivots): estimate $\approx25$ ms per column, so $\approx11$ min per full $\Delta$, $\approx22$ min for two.
- Early stop: the identity relations are exact left-null vectors of the projected map for every $\Delta$ and every input level (078 (4.3), checked on the image by the annihilation pairings), so $\operatorname{rank}\le1447-n_{\rm rel}$. The scan stops when it reaches this bound (closure); otherwise it runs the full $\Delta$ and then a second one (078's stopping rule).
- Relation count: 42016 $\chi$ functionals at $k_\chi=4$ with $N-\bar N$ odd (23776 $b$, 18240 $L$), against 12742 at $d=2$ (25–29 s): estimate 2–10 min.
- $\alpha'_{\rm v}=\tfrac12$ control: stops at full rank, $\approx1500$–2000 columns, $\approx1$ min.
- Total: $\approx20$–45 min, below the 60-min cap; a safety cap of 26565 pairs per $\Delta$ (one full $\Delta$) and two $\Delta$ is set in the script. Single process, `OMP_NUM_THREADS=OPENBLAS_NUM_THREADS=MKL_NUM_THREADS=1`.
- *Outcome* (after the runs): joint count 464–501 s (above the estimate); scan 21 ms per column, the bound 1340 reached after 2308 pairs (55 s), far below one full $\Delta$; the $L$-alone count, not in the estimate, did not finish in 20 min and was dropped from the default run. Final run 9.5 min; total machine time of runs 1–5 about 45 min, one process at a time.

## §2 Block dimension

$d_{\rm eff}=3$, $K=3$ (generating function `v.gf_count`, equal to the Fock enumeration block by block, `D1-dim`): (0,0) 1, (1,1) 11, (2,0),(0,2) 10, (2,2) 132, (3,1),(1,3) 107, (3,3) 1069; $\dim W^{\rm even}_{\le3}=1447$.

## §3 Runs

(one line per completed run; script seed 20261087, single process, `OMP/OPENBLAS/MKL_NUM_THREADS=1`)

- **Run 1** (15:40, `run-dim-b.log`, 11 s; identical in `verify-full.log`): `D1-dim` PASS, 1447 = Fock enumeration per block. $b$-alone count at $K=3$, $k_\chi=4$: $d=1$: 15, $d=2$: 34 (= 083), $d=3$: **61** (over $\mathbb Q$ also 61, `D2-b-Q`). Sector counts $r(a,\bar a)$ ($\chi$ restricted to one matter state of levels $(a,\bar a)$): $r(0,0)=4$, $r(1,0)=r(0,1)=2$, $r(2,0)=r(0,2)=1$, $r(1,1)=3$, all others 0. The formula $\sum n_d(a)n_d(\bar a)r(a,\bar a)$ reproduces the direct count at $d=1,2,3$ (`D2-factorisation-d1..3` PASS). Bound $61\ge49$ (`D2-bound` PASS).
- **Run 2** (15:40–16:10, `run2-killed-at-L-alone.log`, stopped by hand): joint $(b+L)$ relation count at $K=3$, $d=3$, $k_\chi=4$: **107** relations from 41870 non-empty functionals, 500.8 s (`D3-relations`). The $L$-alone count, next in the script, had not finished after 20 min (memory growing, 770 MB: without the $b$-pivots the $L$-functionals fill in badly in the outside-first elimination). Stopped so that the scan could run inside the time box; the script was reordered (joint count → scan → annihilation → $b$ break leg; $L$-alone count and split opt-in, argument `split`).
- **Run 3** (16:11–16:21, `run3-json-crash.log`, same seed, so the same momentum; the 107 relations recomputed in 485.2 s): **scan $K=3$, $L=2$, $d=3$, $\alpha'_{\rm v}=0$: rank 1340/1447 after 2308 unordered pairs (one $\Delta$, 53.3 s)**, the bound $1447-107$ reached; 400 further random pairs add nothing (9.1 s); relations $\times$ image basis: 0 of $107\times1340$ pairings non-zero; $b$-alone 61 inside the joint span. `D3-b-in-joint`, `D3-rank`, `D3-annihilate`, `D3-post-stop`, `D3-pairing-engine` PASS. The process then stopped on a bookkeeping error (a numpy boolean passed to the JSON dump of the check list, after the `D3-pairing-engine` line was printed); no number is affected. Fixed (`report` casts to `bool`).
- **Run 4** (16:21–16:23, `run4-superseded.log`): stopped by hand during the joint count, after the break leg `BREAK-D2-even-only` was added to the script, so that the final log comes from the final script.
- **Run 5 = final run** (16:24–16:34, `verify-full.log`, seed 20261087, single process, exit 0): **19/19 PASS**; every number of runs 1–3 reproduced (same seed, same momentum): $b$ 15/34/61, joint 107 (464.2 s), rank 1340/1447 after 2308 pairs (54.8 s), 400 post-stop pairs +0, 0 of $107\times1340$ pairings non-zero; new: `BREAK-D2-even-only`, `BREAK-D3-b` (163 non-zero pairings), `D4-alpha-half` (1447/1447 after 1582 pairs, 39.6 s), matter-vacuum diagnostic (§6). Quoted in Verification.

## §4 Rank against the relation counts

$\beta=3/2$, $\gamma'=3$, $\alpha'_{\rm v}=0$, $L=2$; ranks over $\mathbb F_p$, $p=2^{31}-1$, at a random momentum; relation counts at $k_\chi=K+1$ (exact relations from (4.3), a lower bound on the cokernel). Rows $d=2$ and $K=2$ from 078/083.

| $K$ | $d_{\rm eff}$ | dim | rank | deficit | joint relations | $b$ alone | $L$ alone | mixed only | source |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 2 | 73 | 68 | 5 | 5 | 3 | 0 | 2 | 078, 083 |
| 2 | 3 | 164 | 159 | 5 | 5 | 3 | 0 | 2 | 083 |
| 3 | 2 | 487 | 427 | 60 | 60 | 34 | 2 | 24 | 083 |
| 3 | **3** | **1447** | **1340** | **107** | **107** | **61** (also over $\mathbb Q$) | not computed | $L$ alone + mixed $=46$ | 087 |

**Closure at $K=3$, $d=3$.** The 107 relations are exact consequences of (4.3): they annihilate the image of $\mathrm{Sym}^2\mathcal H_0$ for every $\Delta$ and every input level (078 §4), so $\operatorname{rank}\le1447-107=1340$ at the scan momentum for every $L$. The scan reaches 1340 at $L=2$ (2308 pairs; 400 more add nothing), and the relations pair to zero with all 1340 image vectors, a test of the relation vectors themselves, of the vertex datum $z^2$ in particular (083 Self-review 2: the count alone is blind to $z^2$, the pairings are not; `BREAK-D3-b`). Hence, at the scan point over $\mathbb F_p$: rank $=1340$ and cokernel $=107$ for every $L\ge2$, and the cokernel is exactly the joint span of the relations of the two identities. No relation beyond the two identities appears at $d=3$.

**Generic $P$** (083 §4 item 3, same argument). The rank is $\ge1340$ for generic $P$ rigorously (a non-zero minor at the sample point is a non-zero polynomial in $P$). The upper bound: the count is $\operatorname{rk}F-\operatorname{rk}F_{\rm out}$; the $b$-functionals are $P$-independent and the $L$-functionals affine in $P$, so every minor of $F_{\rm out}$ has degree $\le\#\{L\text{-functionals}\}=18240$ (of 41870 non-empty functionals). By the Schwartz–Zippel lemma (Schwartz 1980; Zippel 1979) the failure probability at the uniformly random point of $\mathbb F_p^3$ is $\le18240/(2^{31}-1)\approx8.5\times10^{-6}$. Caveat: $p$ not a bad prime, i.e. the generic rank of $F_{\rm out}$ over $\mathbb F_p(P)$ equals its generic rank over $\mathbb Q(P)$ (not checked). No rational-point computation over $\mathbb Q$ was made for the joint count at $d=3$ (the $b$-alone count over $\mathbb Q$, 61, is $P$-independent and holds at every $P$).

**Reading.**
(a) *$b$ alone.* $61=4d^2+7d+4$ at $d=3$; the factorisation over matter states is machine-checked at $d=1,2,3$ (§5). The critic's bound $34+3(d^2-4)=49$ holds and is not tight (61).
(b) *$L$ alone and mixed.* Their sum is $107-61=46$ (26 at $d=2$: 2 + 24). The $L$-alone count was not obtained: its elimination did not finish in 20 min (run 2). The split between the two is open; it does not affect the closure, which uses the joint span only.
(c) *Per block.* The image's projection is onto the blocks (0,0), (0,2), (1,1), (2,0), (2,2) and misses 1, 1, 19 dimensions in (1,3), (3,1), (3,3). A block deficit counts the relations supported inside that block alone (a functional supported on a block annihilates the projection iff it annihilates the image), so the relations supported in a single block span 21 dimensions; the other 86 dimensions of the relation space have no single-block representative.
(d) *Growth with $d$.* At $K=3$ the cokernel grows from 60 ($d=2$) to 107 ($d=3$), all of it accounted for by the two identities; the $b$-part grows by 27 ($15+4+8$ by matter sector, §5), the rest by 20.

## §5 The $b$-count: factorisation over matter states

**Structure.** $O_b=b_1^--z^2b_{-1}^-$ acts on ghosts only. For $\chi=m\otimes\chi_{\rm gh}$ ($m$ a matter Fock monomial of levels $(a,\bar a)$), the functional $y_\chi=\chi\circ O_b$ is $m\otimes(\chi_{\rm gh}\circ O_b)$ and is supported on coordinates with the same matter monomial $m$. Whether a coordinate $(m,g)$ is inside $W^{\rm even}_{\le K}$ depends on $m$ only through $(a,\bar a)$ (total levels $\le K$, no $c_0$, $\bar c_0$, total $N-\bar N$ even). The span of the $b$-functionals is therefore a direct sum over $m$, and so is its intersection with the inside:
$$R_b(K,d)=\bigoplus_m m\otimes R^{\rm gh}_b\big(K-a,\,K-\bar a;\ a-\bar a\bmod2\big),\qquad b(K,d)=\sum_{a,\bar a}n_d(a)\,n_d(\bar a)\,r_K(a,\bar a),$$
with $n_d(\ell)$ the number of matter states of one chirality at level $\ell$ and $r_K(a,\bar a)$ the ghost count with budget $(K-a,K-\bar a)$ and ghost parity $n_{\rm gh}-\bar n_{\rm gh}\equiv a-\bar a$ (the $\chi$-level cutoff becomes $k_\chi-a$, $k_\chi-\bar a$ on the ghost part). This is the critic's factorisation (083 #5) with one correction: the sum runs over all $(a,\bar a)$, not only $a-\bar a$ even. For $a-\bar a$ odd the ghost part must have odd parity, and such ghost relations exist.

**Measured** (`D2-factorisation-d1..3`, run 1 and run 4). $r_3(a,\bar a)$ computed with $\chi$ restricted to one matter monomial $(\alpha^0_{-1})^a(\bar\alpha^0_{-1})^{\bar a}$ at $d=1$: $r_3(0,0)=4$, $r_3(1,0)=r_3(0,1)=2$, $r_3(2,0)=r_3(0,2)=1$, $r_3(1,1)=3$, all other $(a,\bar a)\le(3,3)$ zero. With $n_d(0)=1$, $n_d(1)=d$, $n_d(2)=d(d+3)/2$:
$$b(3,d)=4+2\cdot2\,d+2\cdot1\cdot\tfrac{d(d+3)}2+3d^2=4d^2+7d+4:\qquad15,\ 34,\ 61\ (d=1,2,3),\quad 2890\ (d=26).$$
The formula equals the direct count (all $\chi$, no factorisation used, mixed matter directions included) at $d=1,2,3$; $d=2$ reproduces 083's 34, and the $d=3$ count is 61 over $\mathbb Q$ as well (`D2-b-Q`). The check is falsifiable: a matter-dependence of the $b$-functionals, or a sector-dependent canonicalisation sign that broke the block structure, would make the direct count differ from the sector sum at $d\ge2$, where the monomials with several directions are not represented by the $d=1$ sectors.

**Against the critic's argument.**
- The bound $b(3,d)\ge34+3(d^2-4)$ holds (49 at $d=3$, measured 61; `D2-bound`). Its derivation needs only the $(1,1)$ sector ($r_3(1,1)=3$ = the three $K=2$ ghost relations, as the critic said) and the monotonicity of the other terms, which the omitted sectors do not affect.
- The decomposition is not the critic's: at $d=2$, $34=4\,[(0,0)]+8\,[(1,0),(0,1)]+10\,[(2,0),(0,2)]+12\,[(1,1)]$. The odd sectors he excluded give 8, and the $(2,0)$-type terms he expected might vanish give 10. His matter-vacuum prediction ("22 if the $(2,0)$-type terms vanish") is not borne out: the matter-vacuum $b$-count is $r_3(0,0)=4$.
- Growth $d=2\to3$: $61-34=27=15\,[(1,1)]+4\,[(1,0),(0,1)]+8\,[(2,0),(0,2)]$.

**$K=2$.** The same structure gives $b(2,d)=\sum n_d(a)n_d(\bar a)\,r_2(a,\bar a)$ with non-negative integers $r_2$. 083 measured $b(2,2)=b(2,3)=3$; since $n_3(a)n_3(\bar a)>n_2(a)n_2(\bar a)$ for every $(a,\bar a)\ne(0,0)$, every non-vacuum $r_2$ vanishes and $b(2,d)=3$ for every $d$. This reaches the critic's $K=2$ conclusion without his parity restriction. (The factorisation is machine-checked at $K=3$; at $K=2$ it is the same structural statement.)

**Second route (the critic's hand derivation, critic 087 C2; not run by the elimination engine).** Cited as the critic's: it is a derivation of the ghost counts $r_K(a,\bar a)$ that does not use the elimination code, and it changes no number.

Setting: the state picture of the script, $O_b=\beta-\bar\beta$ on the $c_1\bar c_1$-based Fock space, $\beta=b_{-1}-z^2b_1$, $b_1=\partial/\partial c_{-1}$ (the BPZ image of $\chi\circ(b_1^--z^2b_{-1}^-)$, up to an overall sign); $\beta^2=0$, $\{\beta,\bar\beta\}=0$.

1. *The relation space is a kernel.* $h=-c_{-1}/z^2$ satisfies $\beta h+h\beta=1$, so $H=h\otimes1$ is a contracting homotopy of $O_b$. Every $y\in\ker O_b\cap I$ ($I$ = inside: charge 0, no zero modes, ghost levels $\le(K_h,\bar K)$, parity fixed) equals $O_b(Hy)$, and $Hy$ has levels $(n+1,\bar n)\le(K_h+1,\bar K)$, charge $+1$ and opposite parity: it lies in the script's $\chi$ set ($k_\chi=K+1$, $N-\bar N$ odd). Conversely $\operatorname{im}O_b\subset\ker O_b$. Hence $R_b=\ker O_b\cap I$ exactly, and $k_\chi=K+1$ saturates the $b$-part at every $K$.
2. *Adapted basis.* Per chirality $u=b_{-1}$, $v=c_{-1}$, $r$ a monomial in $\{b_{-n},c_{-n}\}_{n\ge2}$ of level $\ell$ and charge $q$. With $e_0=1$, $e_1=u$, $e_2=v$, $e_3=uv-z^2$: $\beta e_0=e_1$, $\beta e_2=e_3$, $\beta e_1=\beta e_3=0$. Top levels: $e_0r$: $\ell$; $e_1r,e_2r$: $\ell+1$; $e_3r$: $\ell+2$ (mixed with $\ell$, same parity), so the level-truncated space is spanned by the adapted elements of top level $\le K$ (triangular change of basis). $P=\operatorname{span}\{e_0r,e_2r\}$, $Q=\operatorname{span}\{e_1r,e_3r\}=\ker\beta$, and $\beta:P\to Q$ is a bijection of basis elements raising the top level by one.
3. *Count.* $\ker O_b=(Q\otimes\bar Q)\oplus O_b(P\otimes\bar P)$, and $O_b(x)$ is truncated iff $x\in P_{\le K_h-1}\otimes\bar P_{\le\bar K-1}$. With budget $(K_h,\bar K)=(K-a,K-\bar a)$ the ghost count is the number of charge-0 pairs in $Q_{\le K_h}\times\bar Q_{\le\bar K}$ plus the number of charge-$(+1)$ pairs in $P_{\le K_h-1}\times\bar P_{\le\bar K-1}$ (the parity condition is automatic). Lists of (top level, charge): $Q_{\le1}$: (1,−1); $Q_{\le2}$: add (2,0) [$e_3$]; $Q_{\le3}$: add (3,−2) [$ub_{-2}$], (3,0) [$uc_{-2}$]; $P_{\le0}$: (0,0); $P_{\le1}$: add (1,+1) [$v$]; $P_{\le2}$: add (2,−1) [$b_{-2}$], (2,+1) [$c_{-2}$].

With $\rho(K_h,\bar K)=r_3(3-K_h,3-\bar K)$ the pair counts give $\rho(3,3)=2+2=4$, $\rho(3,2)=1+1=2$, $\rho(3,1)=0+1=1$, $\rho(3,0)=0$, $\rho(2,2)=1+2=3$, and $\rho=0$ for $(2,1),(2,0),(1,1),(1,0),(0,0)$. That is $r_3(0,0)=4$, $r_3(1,0)=r_3(0,1)=2$, $r_3(2,0)=r_3(0,2)=1$, $r_3(1,1)=3$, and all other $r_3$ zero: **all 16 equal the measured table** (§3 run 1). At $K=2$ only $r_2(0,0)=3$ survives, so $b(2,d)=3$ for every $d$ (D2.3 by a second route). With $n_d$ as above, $b(3,d)=4d^2+7d+4$ for every $d$. The critic's explicit relations in the odd sector $(1,0)$ (matter $\alpha^\mu_{-1}$, ghost budget $(2,3)$), as states on $c_1\bar c_1|0\rangle$: $\alpha^\mu_{-1}(b_{-1}c_{-1}-z^2)\,\bar b_{-1}\bar c_{-2}$ and $\alpha^\mu_{-1}\,O_b(\bar c_{-2})$; an odd ghost level difference compensates the odd matter level difference, which is why the even-only restriction of critic 083 #5 fails.

## §6 Matter-vacuum diagnostic and $\alpha'_{\rm v}=\tfrac12$ control

**Matter-vacuum diagnostic** (critic 083 #5; `D3-mv-*`, a diagnostic: its pass condition is only "$\le$ the full count"). Two statements of the critic were tested.
1. "The matter-vacuum $b$-count at $K=3$, $d=2$ is $34-12=22$ if the $(2,0)$-type terms vanish." Measured: 4 at $d=2$ and $d=3$ (it is $r_3(0,0)$, §5). The $(2,0)$-type terms give 10 at $d=2$ and the odd sectors 8.
2. "The two mixed relations at $K=2$ likely come from matter-vacuum $\chi$, on which the matter part of $O_L$ produces only $P\cdot\alpha_{-1}$." Test: the joint count with every $b$-functional and only the $L$-functionals of matter-vacuum $\chi$.

| $K$ | $d$ | $b$ alone | $b$ + matter-vacuum $L$ | full joint |
|---|---|---|---|---|
| 2 | 2 | 3 | 3 | 5 |
| 2 | 3 | 3 | 3 | 5 |
| 3 | 2 | 34 | 36 | 60 |
| 3 | 3 | 61 | 63 | 107 |

The matter-vacuum $L$-functionals add nothing at $K=2$, so the two mixed relations there need $L$-functionals of matter-excited $\chi$: the critic's guess is not borne out. At $K=3$ they add 2 at both $d=2$ and $d=3$. At $d=2$ the $L$-alone count is also 2 (083), which suggests (not checked) that the $L$-alone relations come from matter-vacuum $\chi$. The remaining 24 ($d=2$) and 44 ($d=3$) relations all need matter-excited $L$-functionals. The $d$-independence of the $K=2$ mixed count (2 at $d=2,3$) therefore has no explanation yet.

**$\alpha'_{\rm v}=\tfrac12$ control** (`D4-alpha-half`): $K=3$, $L=2$, $d=3$, same pipeline, onto: rank 1447/1447 after 1582 unordered pairs (39.6 s). A full rank over $\mathbb F_p$ is a full rank over $\mathbb Q$ at generic $P$ (a non-zero maximal minor lifts). The $\alpha'_{\rm v}\ne0$ side of R84 extends to $d_{\rm eff}=3$ at $K=3$.

## §7 What changes in R84

1. **$K=3$, $d_{\rm eff}=3$ row (new).** Rank 1340/1447, cokernel 107 for every $L\ge2$ over $\mathbb F_p$ at the sampled momentum (no exact closure over $\mathbb Q$ at a rational point, unlike $d_{\rm eff}=2$, 083 §4; generic $P$: $\ge1340$ rigorously, $=1340$ with failure probability $\le18240/p$, $p=2^{31}-1$ not checked to be a good prime), equal to the joint span of the relations of (4.3) ($b$ alone 61, also over $\mathbb Q$; $L$ alone + mixed 46). The identity-generation statement of R84 now holds at the four tested points ($K=2$: $d=2,3$, the cokernel staying at 5; $K=3$: $d=2,3$), the $K=3$ cokernel growing with $d$ (60 → 107). The selection-rule reading extends to $d_{\rm eff}=3$; nothing beyond the two identities appears.
2. **Scope, matter content.** The hand argument is replaced by a checked statement and one correction: the $b$-relations factorise over matter monomials of *every* level pair $(a,\bar a)$, odd $a-\bar a$ included (the critic's sum over even $a-\bar a$ gives 26 at $d=2$ against the measured 34); $b(3,d)=4d^2+7d+4$ (machine-checked at $d\le3$, ghost counts re-derived by hand by the critic, §5 second route; 2890 at $d=26$ by the factorisation); $b(2,d)=3$ for every $d$. The critic's bound $34+3(d^2-4)$ holds but is not the count.
3. **Selection-rule paragraph.** "(5 of 73 at $K=2$, 60 of 487 at $K=3$ ($d_{\rm eff}=2$))" → "(5 of 73 at $K=2$; at $K=3$, 60 of 487 for $d_{\rm eff}=2$ and 107 of 1447 for $d_{\rm eff}=3$)" (the critic's text, last section).
4. Nothing changes in R84's refutation of PH31 at $\alpha'_{\rm v}=0$, in the routing to R80, or in R86's reading (the selection rule is a property of the fixed-halves model at $\alpha'_{\rm v}=0$).

## Verification

`.venv/bin/python -u codes/verify-ph31-rank-k3d3.py` (no argument: parts `dim b main half mv`; the opt-in arguments `split` and `breakL` were not run in the final run), seed 20261087, single process with `OMP_NUM_THREADS=OPENBLAS_NUM_THREADS=MKL_NUM_THREADS=1`, 2026-10-04 16:24–16:34, exit 0; log `agent/scratch/computator/computator-087-k3-count-d3-20261004T153500/verify-full.log` (progress lines omitted below):

```
seed = 20261087, p = 2147483647, beta = 3/2, gamma' = 3, kchi = 4
PASS  D1-dim: d=3, K=3: dim W^even_<=3 = 1447 (rows 1447); even blocks {'0,0': 1, '0,2': 10, '1,1': 11, '1,3': 107, '2,0': 10, '2,2': 132, '3,1': 107, '3,3': 1069}
  b-relations per matter sector r(a,abar), K=3: {'0,0': 4, '0,1': 2, '0,2': 1, '0,3': 0, '1,0': 2, '1,1': 3, '1,2': 0, '1,3': 0, '2,0': 1, '2,1': 0, '2,2': 0, '2,3': 0, '3,0': 0, '3,1': 0, '3,2': 0, '3,3': 0} (0.1 s)
PASS  D2-factorisation-d1: K=3, d=1: b-alone count 15 (1516 functionals, 0.0 s); sum_(a,abar) n_d(a) n_d(abar) r(a,abar) = 15
PASS  D2-factorisation-d2: K=3, d=2: b-alone count 34 (7040 functionals, 0.2 s); sum_(a,abar) n_d(a) n_d(abar) r(a,abar) = 34
PASS  D2-factorisation-d3: K=3, d=3: b-alone count 61 (23630 functionals, 0.7 s); sum_(a,abar) n_d(a) n_d(abar) r(a,abar) = 61
PASS  BREAK-D2-even-only: sector sum over a - abar even only: {1: 11, 2: 26, 3: 49} vs direct {1: 15, 2: 34, 3: 61} (must differ at d = 2, 3)
PASS  D2-bound: b-count(K=3): d=2 34 (083: 34), d=3 61 >= 34 + 3(d^2-4) = 49
PASS  D2-b-Q: b alone over Q, K=3, d=3: 61 relations (0.7 s); over F_p: 61
  joint relations: 107 from 41870 functionals, 464.2 s
PASS  D3-relations: K=3, d=3: 107 relations from (4.3) (chi level <= 4, 41870 functionals, 464.2 s)
PASS  D3-b-in-joint: b-alone 61 (0.8 s) lie in the joint span: rank(joint + b) = 107 (joint 107, rank 107); L-alone + mixed = 46
  [K3L2d3] K=3 L=2 d=3 sample 0: rank 1340/1447 (+1340, 2308 of 26565 pairs) t=54.8s
PASS  D3-rank: rank 1340/1447 mod p, deficit 107, 2308 columns, 1 Delta, 64.3 s; relations + rank = 1447; blocks {'0,0': (1, 1), '0,2': (10, 10), '1,1': (11, 11), '1,3': (106, 107), '2,0': (10, 10), '2,2': (132, 132), '3,1': (106, 107), '3,3': (1050, 1069)}
PASS  D3-annihilate: relations x image basis (107 x 1340): 0 non-zero pairings
PASS  D3-post-stop: 400 further random pairs after the stop: rank 1340 -> 1340 (9.4 s)
PASS  D3-pairing-engine: int64 split product = exact product on 6 rows x 1340 (incl. 3 shifted rows, 3993 non-zero entries)
PASS  BREAK-D3-b: b alone, z^2 -> -z^2: 61 'relations', 163 non-zero pairings (must be > 0)
PASS  D4-alpha-half: alpha'_v=1/2, K=3, L=2, d=3: rank 1447/1447, 1582 columns, 39.6 s
PASS  D3-mv-2-2: K=2, d=2: b all chi + L matter-vacuum chi: 3 relations (full joint 5; b alone 3; b from matter-vacuum chi 3; 0.0 s)
PASS  D3-mv-2-3: K=2, d=3: b all chi + L matter-vacuum chi: 3 relations (full joint 5; b alone 3; b from matter-vacuum chi 3; 0.1 s)
PASS  D3-mv-3-2: K=3, d=2: b all chi + L matter-vacuum chi: 36 relations (full joint 60; b alone 34; b from matter-vacuum chi 4; 0.3 s)
PASS  D3-mv-3-3: K=3, d=3: b all chi + L matter-vacuum chi: 63 relations (full joint 107; b alone 61; b from matter-vacuum chi 4; 0.9 s)
SUMMARY: 19/19 PASS
```

Earlier runs (same seed, every common number identical): `run-dim-b.log` (run 1), `run2-killed-at-L-alone.log` (joint count 107 in 500.8 s; $L$-alone unfinished after 20 min), `run3-json-crash.log` (scan, closure, annihilation: identical), `run4-superseded.log`. The scan engine was smoke-tested before run 3 at $K=2$, $d=2$ (unordered pairs, early stop at 68 after 158 columns, full scan without stop 68/73 over two $\Delta$; int64 and Python-integer pairings agree), not logged to a file.

**Falsifiability.**
- `D3-rank` and `D3-relations` are independent pipelines, but the scan stops at $\dim-n_{\rm rel}$. `D3-rank` therefore fails for an undercount of relations (the scan cannot reach the bound). An overcount is caught by the 400 post-stop columns, which would raise the rank (`D3-post-stop`, and `D3-rank`, which counts them), and by `D3-annihilate`.
- `D3-relations` itself asserts only that the count is positive (`len(rels) > 0`): it is a log of the relation count, not evidence for the number 107. The number is fixed by `D3-rank` ($1340+107=1447$) and the independence of the 107 relations on the rows by `D3-annihilate`; the node D3.1 cites those two (critic #11).
- `D3-annihilate` is the only test of the vertex datum $z^2$ in the relations (the count alone is invariant under $z^2\to z^2/\lambda^2$, 083 Self-review 2); `BREAK-D3-b` shows it fails for a flipped sign (163 non-zero pairings).
- `D2-factorisation-d*` would fail for a matter-dependent $b$-count at fixed $(a,\bar a)$; `BREAK-D2-even-only` shows the direct counts discriminate the critic's sector list from the measured one (26 vs 34 at $d=2$). At $d=3$ the even-only sum is 49, equal to the critic's bound by coincidence: $4d^2+3d+4=3d^2+22$ only at $d=3$.
- `D4-alpha-half` can fail (the same pipeline gives the deficit at $\alpha'_{\rm v}=0$).
- `D3-mv-*` are diagnostics: their pass condition ($\le$ the full count) is weak; the information is in the numbers.

**Not machine-checked.**
- The $L$-alone count at $d=3$ and the $L$/mixed split (opt-in `split`, > 20 min).
- `BREAK-D3-L` (opt-in `breakL`): only the $b$ identity's sign was perturbed.
- The joint count over $\mathbb Q$ at a rational momentum.
- The generic-$P$ upper bound beyond its Schwartz–Zippel bound, and the bad-prime caveat.
- The factorisation at $K=2$ (same structure, §5; the ghost counts $r_2$ are re-derived by hand in the second route, not by machine).
- $d\ge4$; $K=3$, $L=3$ at $d=3$, which cannot change the number: the relations hold for inputs of every level.

## Self-review

1. *Objective.* Answered. At $K=3$, $d_{\rm eff}=3$ the cokernel is 107 and equals the joint span of the two identities' relations. No new mechanism appears, and the selection-rule reading of R84 extends to $d=3$. The hand argument behind R84's Scope is replaced by a checked count. The factorisation holds, but over every matter level pair, odd $a-\bar a$ included: $b(3,d)=4d^2+7d+4$, not the critic's sector list. The critic's bound (49) holds and is not the count. Part of the literal task is not met: the $L$-alone/mixed split (brief item ii). The closure does not need it.
2. *Weakest step.* The relation count at the new size (41870 functionals, about 8 min). Shored up by three things:
   - the exact meeting with the scan's rank, which reaches the relation bound (an undercount would have kept it below; $1340+107=1447$);
   - 0 non-zero pairings out of $107\times1340$, against 163 for the sign-flipped $b$-relations;
   - the early stop, which is safe: it uses the relations only as an upper bound, and 400 post-stop columns add nothing.

   The second weakest step is the generic-$P$ statement. It is probabilistic (failure probability $\le8.5\times10^{-6}$), with the bad-prime caveat, as in 083.
3. *Not checked, and why acceptable.*
   - The $L$/mixed split: it does not enter the closure or R84's statements.
   - The joint count over $\mathbb Q$ at a rational point: 083 found the $\mathbb Q$ and $\mathbb F_p$ counts equal at every tested point. Here the Schwartz–Zippel bound carries the generic statement.
   - $L=3$: forced by the relations.
   - $d\ge4$: the $b$-part is known at every $d$ by the factorisation, the $L$/mixed part is not.
4. *What a stronger physicist would ask.* Whether the joint count has a closed form in $d$. Two data points at $K=3$ (60, 107) cannot fix a quadratic; $d=1$ at $K=3$ is cheap and would give a third point. More to the point: why the $L$-type relations grow with $d$ (26 → 46) while the matter-vacuum $L$-functionals contribute a $d$-independent 2. A natural guess is an organisation by transverse $SO(d-1)$ representations relative to $P$ (only $P\cdot\alpha$ enters through $\alpha_0$). It is untested, because the random $P$ mod $p$ hides the symmetry. A structural proof that $\Phi_2(\mathrm{Sym}^2\mathcal H_0)$ is dense in the joint kernel at every $K$ and $d$ (083 Self-review 4) remains the open conceptual question. Four data points of exact closure ($K=2$: $d=2,3$, the cokernel staying at 5; $K=3$: $d=2,3$) support it.

## Proposed R84 lines

The proposed lines of the first version of this record are replaced by the critic's text (`agent/reports/critic-087-20261004T164100.md`, *R84 text I would accept*), copied verbatim; critic findings #5 (Status and Verification qualifiers: "over $\mathbb F_p$ at the sampled momentum", "$p=2^{31}-1$ not checked to be a good prime", no exact closure over $\mathbb Q$ at a rational point at $d_{\rm eff}=3$, unlike $d_{\rm eff}=2$) and #8 (Scope: the old reason "at $K=2$ no matter excitation fits the level budget" was wrong, matter (1,1), (2,0), (0,2) fit and their ghost sectors carry no relation, $\rho(1,1)=\rho(2,0)=0$; the replacement of the Scope parenthesis is a full replacement, not an insertion). Orchestrator's call to promote.

**Scope.** Replace the text from "matter with $d_{\rm eff}=2$ components" up to and including "so 60/487 is a $d_{\rm eff}=2$ number)" with:

> matter with $d_{\rm eff}=2$ and $3$ components (the $b$-identity is matter-blind but its count is not: the $b$-relations factorise over the matter Fock monomials of every level pair $(a,\bar a)$, odd $a-\bar a$ included, into $d$-independent ghost counts, so the $b$-count is 3 at $K=2$ and $4d^2+7d+4$ at $K=3$ for every $d$ (machine-checked at $d\le3$, ghost counts re-derived by hand; 2890 at $d=26$); the $K=3$ cokernel is 60/487 at $d_{\rm eff}=2$ and 107/1447 at $d_{\rm eff}=3$, in both cases the joint span of the two identities; the $L$-type and mixed relations (2 at $K=2$ for $d_{\rm eff}=2,3$; 26 and 46 at $K=3$) are measured at $d_{\rm eff}\le3$ only, and their $d$-dependence is not explained)

**Status.** After "$K=3$ cokernel $=60$, rank 427/487 for every $L\ge2$ at the sampled momenta, $d_{\rm eff}=2$ — Verified (record 083)" insert:

> ; $K=3$, $d_{\rm eff}=3$: cokernel $=107$, the joint identity count ($b$ alone 61, exact over $\mathbb Q$ at every $P$), rank 1340/1447 for every $L\ge2$, over $\mathbb F_p$ at the sampled momentum (no rational-point closure); at generic $P$ the rank is $\ge1340$ rigorously and $=1340$ with failure probability $\le18240/p\approx8.5\cdot10^{-6}$, $p=2^{31}-1$ not a bad prime (unchecked) — Verified (record 087)

and replace "full rank at $\alpha'_{\rm v}=1/2$, $1/4$ and $-1/2$, $K\le3$, $L\le2$" by "full rank at $\alpha'_{\rm v}=1/2$, $1/4$ and $-1/2$, $K\le3$, $L\le2$, $d_{\rm eff}=2$, and at $\alpha'_{\rm v}=1/2$, $K=3$, $L=2$, $d_{\rm eff}=3$".

**Verification** (new line):

> 2026-10-04 – exact check over $\mathbb F_p$ (ranks, joint relation count) and over $\mathbb Q$ ($b$-count) – `codes/verify-ph31-rank-k3d3.py`, seed 20261087, 19/19 PASS (`agent/scratch/computator/computator-087-k3-count-d3-20261004T153500/verify-full.log`), record 087; critic `agent/reports/critic-087-20261004T164100.md` (ACCEPT after mechanical edits; block dimension and the 16 sector counts $r_3$ re-derived by hand, $R_b=\ker O_b\cap W$): at $\alpha'_{\rm v}=0$, $K=3$, $d_{\rm eff}=3$ ($\dim W^{\rm even}_{\le3}=1447$) the identities (4.3) give exactly 107 independent relations ($b$ alone 61, also over $\mathbb Q$; $L$ alone + mixed 46, split not computed), which annihilate the measured image (0 of $107\times1340$ pairings; $z^2$-flipped $b$-relations: 163 non-zero); rank 1340/1447 at $L=2$, hence for every $L\ge2$, over $\mathbb F_p$ at the random momentum; at generic $P$ rank $\ge1340$ rigorously and $=1340$ with failure probability $\le18240/p\approx8.5\cdot10^{-6}$ ($p$ not a bad prime, unchecked; no rational-point closure at $d_{\rm eff}=3$); $b(3,d)=4d^2+7d+4$ (15, 34, 61 at $d=1,2,3$ equal to the direct counts; the even-only sector sum fails at $d=2,3$); $\alpha'_{\rm v}=1/2$: 1447/1447

(The orchestrator adds its re-run note when it has one.)

**Selection-rule paragraph.** "(5 of 73 at $K=2$, 60 of 487 at $K=3$ ($d_{\rm eff}=2$))" → "(5 of 73 at $K=2$; at $K=3$, 60 of 487 for $d_{\rm eff}=2$ and 107 of 1447 for $d_{\rm eff}=3$)". Optionally, "the map is onto the block at $K\le3$ for $L\le2$" → "… for $L\le2$ ($d_{\rm eff}=2$; also $d_{\rm eff}=3$ at $\alpha'_{\rm v}=1/2$, $K=3$)".

R84's title, Origin, refutation clause and Consequences need no change.
