# 093 — PH31's rank rows at $\alpha'_{\rm v}=\tfrac12$ beyond $K\le3$, $d_{\rm eff}\le3$

Brief: `agent/briefs/active-computator-093-ph31-rank-half-20261004T233900.md` (numerical scan).
Model: claude/opus. Date: 2026-10-05 (started 2026-10-04).

## Status

Fix pass 2 (critic iteration 2) done (2026-10-05): all 14 findings addressed (#1–#6, #8–#14 applied, #7 a note with no action), see `## Fix pass 2 (critic iteration 2)`; changed parts `k2l1`, `c45t`, `c44`, `c44s` run on the final script, 31/31 PASS, exit 0 each; by-hand break legs fire. Next step: none for the computator (orchestrator's re-run of all parts, then promotion of the §5 lines; the falsifier wording is Harold's decision). Fix pass 1 (critic iteration 1) done, see `## Fix pass (critic iteration 1)`. Original run: rows (i), (ii), (iv) and the break legs obtained, row (iii) not obtained (§3).

## Task and objective

**Literal task.** In the fixed-halves model of $p_{2,2}$ at $\alpha'_{\rm v}=\tfrac12$ ($\beta=\tfrac32$, $\gamma'=3$), measure the rank of the level-projected circle map $\pi_{\le K}\pi_W\Phi_2$ on $\mathrm{Sym}^2\mathcal H_0^{\le L}$ against $\dim W^{\rm even}_{\le K}$ (R84's method: mod $p$, random momentum, early stop at the block dimension) for (i) $K=3$, $L=2$, $d_{\rm eff}=4$; (ii) $K=4$, $d_{\rm eff}=2$, $L=2$ (then $L=3$ capped if not onto); (iii) $K=3$, $L=2$, $d_{\rm eff}=5$ if the size estimate fits; (iv) $\gamma'=\tfrac32$, $K=3$, $d_{\rm eff}=2$ (check of the $\gamma'$-independence of R84's Scope). Block dimension and size estimate before each run; a break leg per new row type.

**Objective.** PH31 (surjectivity of the extended circle map onto the even ghost-number-4 block modulo $\ker G$) is `supported` at $\alpha'_{\rm v}=\tfrac12$ by full-rank rows at $K\le3$, $L\le2$, $d_{\rm eff}\le3$ only. Its falsifier is a persistent deficit for growing $K$ and $L$. These rows test the first output level beyond 3 ($K=4$) and the growth in the number of matter components ($d_{\rm eff}=4$, 5), the two directions in which a deficit could first appear. Full rank strengthens the support; a deficit would be a new mechanism (the R84 identities need $\alpha'_{\rm v}=0$).

## Conventions and assumptions

- **A1–A5** of 078 unchanged (the project conventions: physical ghost number, book normalisation; vertex $\mathcal V_3'$ of 032 with $f_0'(w)=w/(\alpha'_{\rm v}w+\gamma')$, special map at $\beta=\tfrac32$; Euclidean matter truncated to $d_{\rm eff}$ components; inputs $\mathcal H_0$ at ghost number 2 per leg, level-matched and $b_0^-$-annihilated, symmetric pairs; finite levels). Here $\alpha'_{\rm v}=\tfrac12$, $\gamma'=3$ except row (iv) ($\gamma'=\tfrac32$) and the break legs ($\alpha'_{\rm v}=0$).
- **A6** Mode cutoff $M=\max(K,L)+1$ (as 078/083/087: $M=4$ at $K=3$, $L\le3$; $M=5$ at $K=4$). The Neumann and ghost coefficients are exact rationals independent of $M$; $M$ only fixes which are tabulated, and a missing one raises a `KeyError` (no silent truncation).
- **A7** Exact arithmetic over $\mathbb F_p$, $p=2^{31}-1$, at a random momentum $P\in\mathbb F_p^{d}$ and random $\Delta\in\mathbb F_p^{d}$ per sample. A full rank over $\mathbb F_p$ at the sample point is a full rank of the joint matrix as a polynomial matrix in $(P,\Delta_1,\dots,\Delta_s)$, hence at generic $P$: a non-zero maximal minor mod $p$ lifts to a non-zero rational minor, a non-zero polynomial in $(P,\Delta_1,\dots,\Delta_s)$ (wording of critic #7).
- Engine: `codes/verify-ph31-rank.py` (078: Neumann data, Fock bases, amplitudes, `Echelon`, `gf_count`), `codes/verify-ph31-rank-ext.py` (083: `even_rows`, relations on rows) and `codes/verify-ph31-rank-k3d3.py` (087: functional builder, `rcount`, `pair_modp`), imported unchanged by `codes/verify-ph31-rank-half.py`.

## Claim tree

093 extends R84 (records 078, 083, 087); its nodes are numbered G0–G7, with children G3.1–G3.9 under G3. Fix pass (critic iteration 1): G0, G3, G3.1, G3.3, G5, G5.2, G6, G6.2, G7 changed; G3.5–G3.9 new (see *Changed nodes and dependents*). Fix pass 2 (critic iteration 2): G3.7 (justification: conditions tightened) and G3.9 (statement extended, justification: new checks) changed; see *Fix pass 2*, *Changed nodes and dependents*.

- **A1–A7** as above.
- **G0** (root) At $\alpha'_{\rm v}=\tfrac12$, $\beta=\tfrac32$, the level-projected circle map $\pi_{\le K}\pi_W\Phi_2$ is onto $W^{\rm even}_{\le K}$ at the new rows — (i) $K=3$, $L=2$, $d=4$ (3608/3608); (ii) $K=4$, $d=2$ with inputs of level $\le3$ (2927/2927); (iv) $\gamma'=\tfrac32$, $K=3$, $L=2$, $d=2$ (487/487) [(iii): see G4] — over $\mathbb F_p$ at the sampled momentum, hence at generic $P$ over $\mathbb Q$. With inputs of level $\le2$ the $K=4$ row is not onto: 2882/2927 mod $p$ at three sampled momenta, saturated in $\Delta$, and exactly 2882 at generic $P$: the 45 missing directions are exact relations of the $c$-ghost correlator with inputs of level $\le2$, valid at every $\alpha'_{\rm v}$ — 44 from the conservation law of $(u^2-z^2)\,du^2$ (F.6) and one from the selection rule that no such input carries both $b_{-2}$ and $\bar b_{-2}$ (F.13) (F1). This deficit is of finite input level: relations of type (F.6) exist at input level $L$ iff $K\ge2L$, and level-3 inputs close it. No persistent deficit appears at the first output level beyond 3 or at $d_{\rm eff}=4$. [by G1–G7]
  - **G1** Block dimensions: $\dim W^{\rm even}_{\le3}=3608$ ($d=4$), $7945$ ($d=5$); $\dim W^{\rm even}_{\le4}=2927$ ($d=2$); generating function = Fock enumeration per block. [by check: G1-dim-34, G1-dim-35, G1-dim-42]
  - **G2** Row (i): $K=3$, $L=2$, $d=4$, $\alpha'_{\rm v}=\tfrac12$, $\gamma'=3$: rank 3608/3608 over $\mathbb F_p$ at the sampled $(P,\Delta)$. [by check: G2-rank] [check: BREAK-antisym-34]
  - **G3** Row (ii): $K=4$, $d=2$, $\alpha'_{\rm v}=\tfrac12$, $\gamma'=3$: onto with inputs of level $\le3$; with inputs of level $\le2$ a saturated deficit of 45 mod $p$, exactly 45 at generic $P$, all of whose relations are $c$-ghost relations ((F.6): 44; (F.13): 1); not of R84's type. [by G3.1–G3.9, G7] [check: BREAK-antisym-42]
    - **G3.1** With inputs of level $\le2$ the rank mod $p$ at the sampled momentum saturates at 2882 (deficit 45): the second $\Delta$ adds nothing over all 5151 pairs; every $(N,\bar N)$ block is onto separately; the 45-dimensional left-null space projects on the blocks $(4,4)$, $(2,4)$, $(4,2)$, $(2,2)$, $(3,3)$ with ranks 39, 22, 22, 6, 1 (0 elsewhere). At generic $P$ the rank is $\ge2882$ (G7). [by check: G3.1-L2-saturated; logged: G3.1-null-blocks]
    - **G3.2** The $L=2$ deficit is the same (45) at a second random momentum. [by check: G3.2-P2]
    - **G3.3** The $L=2$ deficit is not of R84's type: its relations are the $c$-ghost relations (F.6) and (F.13), which hold for inputs of level $\le2$ only and at every $\alpha'_{\rm v}$ (R84's identities hold for inputs of every level and need $\alpha'_{\rm v}=0$); level-3 inputs violate them (F.10 and the $L=3$ remark of F1(b')) and close the whole deficit. [by G3.4, G3.5, G3.6, G3.9, R84 (identities (4.2)–(4.3), Proven, derived at $\alpha'_{\rm v}=0$); eq. (F.9)]
    - **G3.4** With inputs of level $\le3$ (the $L=2$ echelon plus pairs with a level-3 input, same momentum): rank 2927/2927. [by check: G3-L3]
    - **G3.5** For every $\alpha'_{\rm v}$, $\gamma'$, $P$, the 44 vectors (F.7) $(c_{-4}-z^2c_{-2})(c_1\otimes\bar\chi)$ and conjugates ($\bar\chi$ at level 2 or 4, charge $-1$) are independent left-null vectors of the $K=4$ projected map on inputs of level $\le2$, with block projections (F.8); hence the generic rank at $K=4$, $L=2$ is $\le2883$. [eq. (F.6)–(F.8)] [check: G3.5-count, G3.5-annihilate, BREAK-G3.5-flip, G3.5-in-null, G3.5-alpha-1_5-2, G3.5-alpha-0-3, BREAK-G3.5-alpha-flip-*]
    - **G3.6** With level-3 inputs the 44 vectors are violated exactly by columns with an input containing $b_{-3}$ (holomorphic vectors) or $\bar b_{-3}$ (antiholomorphic ones). [eq. (F.10)] [check: G3.6-L3-pattern]
    - **G3.7** At $K=2$, $L=1$, $d=2$, $\alpha'_{\rm v}=\tfrac12$ the law with $\phi=1$ predicts 6 vanishing rows of the $(2,2)$ block; measured: rank 67/73 mod $p$, saturated, left-null space = those 6 rows. [eq. (F.9); by check: G3.7-K2L1-rank, G3.7-K2L1-annihilate] [check: BREAK-G3.7-L2]
    - **G3.8** The left-null space of the $K=4$, $L=2$ image (mod $p$, at the fresh momenta of parts `c44` and `c44s`, the latter saturated) projects injectively on the blocks with $N=4$ or $\bar N=4$ (no null vector on $W_{\le3}$, as R84's $K=3$, $L=2$ surjectivity requires), and with rank $45-3$ on the blocks with $\bar N=4$ (as F.8 predicts). [by check: G3.8-proj-N4, G3.8-proj-Nb4]
    - **G3.9** The 45th relation is $y_{45}=(c_{-3}\bar c_{-3}+z^2c_{-2}\bar c_{-2})|0\rangle$ (F.13): exact for inputs of level $\le2$ at every $\alpha'_{\rm v}$, $\gamma'$, $P$, independent of the 44; it lies in the left-null space of the whole $\alpha'_{\rm v}=\tfrac12$ image at two momenta and its sign flip does not; at a third momentum the image saturates at 2882 and its left-null space modulo the 44 is spanned by $y_{45}$ with the predicted ratio $1/z^2=9$. At $\alpha'_{\rm v}=0$ each of its two rows is by itself a left-null vector (R84 (4.3) on $\chi=c_{-n}\bar c_{-n}c_1|0\rangle$), so (F.13) has no content there. [eq. (F.11)–(F.13); by check: G3.9-P3-saturated, G3.9-y45-in-null] [check: BREAK-G3.9-y45-in-null-flip, G3.9-y45-1_2-3-t, BREAK-G3.9-y45-1_2-3-t-flip, BREAK-G3.9-y45-1_2-3-t-L3, G3.9-y45-1_5-2-t, BREAK-G3.9-y45-1_5-2-t-flip, BREAK-G3.9-y45-1_5-2-t-L3, G3.9-alpha0-rows-vanish; logged: G3.9-complement (explicit form, `run-c44s.log`), the INFO line G3.9-y45-0-3-t; part `c45` (random columns, vacuous) retired in fix pass 2]
  - **G4** Row (iii): $K=3$, $L=2$, $d=5$ — not obtained: the run was stopped after 1000 columns when the measured rates extrapolated to $\approx73$ min, beyond the budget of the run (§3). No claim. [not run to completion]
  - **G5** $\gamma'$-independence (R84 Scope) at $K=3$, $L=2$, $d=2$: an engine check of an exact symmetry ($f_1^{(\gamma'/\kappa)}(w)=f_1^{(\gamma')}(\kappa w)$, critic #13). [by G5.1, G5.2]
    - **G5.1** $\gamma'=\tfrac32$, $\alpha'_{\rm v}=\tfrac12$: rank 487/487, as at $\gamma'=3$. [by check: G5-gamma] [check: BREAK-antisym-32]
    - **G5.2** $\gamma'=\tfrac32$, $\alpha'_{\rm v}=0$: 60 joint relations and rank 427/487 (300 post-stop pairs add nothing), as at $\gamma'=3$ (R84) — the engine reproduces the symmetry at a point where the rank is not full. [by check: G5-gamma-alpha0; R84]
  - **G6** Break legs: the full-rank checks can fail on the same rows with the same engine, in the ghost sector. [by G6.1–G6.3]
    - **G6.1** At $\alpha'_{\rm v}=0$, $K=3$, $d=4$, the $b$-alone relations number $b(3,4)=96=4\cdot16+7\cdot4+4$ (R84's formula, machine-checked before at $d\le3$ only). [by check: G6-b-count-34]
    - **G6.2** These relations (and the $\ge304$ $b$-relations with $\chi$ of level $\le5$ at $K=4$, $d=2$) annihilate the $\alpha'_{\rm v}=0$ image on 1000 random columns (level-3 inputs included at $K=4$), so the $\alpha'_{\rm v}=0$ rank is $\le\dim-b$ for every number of columns; the sign-flipped relations do not annihilate it. The legs are matter-blind ($b$-identity): they test the ghost sector, $z^2$ and the matter indexing of the relations, not the matter Neumann data at $d=4$ or mode 5. [by check: G6-annihilate-34, G6-annihilate-42; R84; logged: G6-b-count-42] [check: BREAK-G6-flip-34, BREAK-G6-flip-42]
    - **G6.3** Antisymmetrised columns give rank 0 at every new row type (exchange symmetry, 078 C1). [by check: BREAK-antisym-34, BREAK-antisym-42, BREAK-antisym-32]
  - **G7** Lift: a full rank over $\mathbb F_p$ at the sampled $(P,\Delta)$ is a full rank of the joint matrix as a polynomial matrix in $(P,\Delta_1,\dots,\Delta_s)$, hence at generic $P$ (a non-zero maximal minor mod $p$ lifts to a non-zero rational minor, since the $\mathbb F_p$ matrix is the reduction of the rational one: no denominator of the vertex data is divisible by $p$; `G7-den-*` is a guard for that). More generally a rank mod $p$ is a lower bound on the generic rank: at $K=4$, $L=2$ the generic rank is $\ge2882$, and with G3.5, G3.9 (45 independent exact relations) exactly 2882. [by A7, G3.5, G3.9; by check: G7-den-32-3, G7-den-43-3, G7-den-32-3_2]

Open gaps: none
Hypotheses in force: none

## §1 Block dimensions

Generating function `v.gf_count` (even $N-\bar N$ blocks), checked against the Fock enumeration `v.closed_basis` in `G1-dim-*` (run 0, PASS):

| $K$ | $d$ | $\dim W^{\rm even}_{\le K}$ | blocks $(N,\bar N)$: dim |
|---|---|---|---|
| 3 | 2 | 487 | (0,0) 1, (1,1) 6, (2,0),(0,2) 6, (2,2) 54, (3,1),(1,3) 44, (3,3) 326 |
| 3 | 3 | 1447 | (0,0) 1, (1,1) 11, (2,0),(0,2) 10, (2,2) 132, (3,1),(1,3) 107, (3,3) 1069 |
| 3 | 4 | **3608** | (0,0) 1, (1,1) 18, (2,0),(0,2) 15, (2,2) 275, (3,1),(1,3) 222, (3,3) 2840 |
| 3 | 5 | **7945** | (0,0) 1, (1,1) 27, (2,0),(0,2) 21, (2,2) 513, (3,1),(1,3) 412, (3,3) 6538 |
| 4 | 2 | **2927** | (0,0) 1, (1,1) 6, (2,0),(0,2) 6, (2,2) 54, (3,1),(1,3) 44, (3,3) 326, (4,0),(0,4) 32, (4,2),(2,4) 306, (4,4) 1764 |

Inputs $\mathcal H_0$ (`v.input_basis`): $L=2$: 101 ($d=2$), 230 ($d=3$), 452 ($d=4$), 803 ($d=5$); $L=3$, $d=2$: 667. Unordered pairs per $\Delta$: 5151, 26565, 102378, 322806; 222778.

## §2 Size estimates (written before each run)

**Run (i)**, $K=3$, $L=2$, $d=4$, $\alpha'_{\rm v}=\tfrac12$:
- Rows 3608 (2.49 × the $d=3$ row); 102378 unordered pairs per $\Delta$, of which $\approx3700$–3900 are expected before the early stop at 3608 (087: 1582 columns for 1447, 083: 499 for 487).
- Time per column: 087's $d=3$ run used 25 ms per column (1582 columns, 39.6 s). The amplitude part scales with the rows ($\times2.5$), the reduced-echelon update with rank $\times$ rows ($\times6.2$). With an even split at $d=3$: $\approx0.03+0.08\approx0.11$ s per column, $\approx7$ min for the run; worst case (echelon-dominated) $\approx15$ min. A 30-s timing probe on the first columns replaces this estimate before the run.
- Memory: echelon $3608^2\times8$ B $\approx104$ MB, plus amplitude caches (ghost cache $d$-independent; matter cache per $\Delta$); estimate $<400$ MB, below 1.5 GB.

**Measured during run (i)** (log lines every 250 columns): 15.6 s for the first 250 columns, then +0.4 to +1.1 s per further 250; i.e. $\approx62$ ms per column for the amplitudes ($\approx17\,\mu$s per row and ordering pair) plus $\approx16\,\mu$s $\times$ rank for the reduced-echelon update at 3608 rows. Peak memory grows by 7 MB per 250 columns (the echelon), 153 MB at rank 2237. Projection for (i): $\approx6$ min, $\approx230$ MB.

**Run (ii)**, $K=4$, $L=2$, $d=2$, $\alpha'_{\rm v}=\tfrac12$ (estimate written before the run, from the rates of (i)):
- Rows 2927; inputs 101, so only 5151 unordered pairs per $\Delta$: full rank needs more than half of one $\Delta$'s pairs, and a second $\Delta$ if the first saturates below 2927 (the joint rank over $\Delta$ samples is the rank over functions of $\Delta$, which the inputs include).
- Amplitudes $\approx17\,\mu$s per row (same rate at $K=2$, $d=2$ in the smoke test: 88 columns of 73 rows in 0.1 s) → $\approx50$ ms per column; echelon $\approx13\,\mu$s $\times$ rank, average $\approx19$ ms; $\approx3000$ columns → $\approx3.5$ min, plus the vertex at mode cutoff 5 (sympy, $<1$ min). Memory $2927^2\times8$ B $\approx69$ MB + base, $<250$ MB.
- If not onto: $L=3$ capped scan (pairs with a level-3 input, 6000 per $\Delta$, two $\Delta$, on top of the $L=2$ echelon; $\approx15$ min) and a second momentum.

**Run (iii)**, $K=3$, $L=2$, $d=5$ (estimate written before the run, from the rates measured at the end of (i): $\approx62$ ms per column for the amplitudes at 3608 rows and $\approx11\,\mu$s per (column, pivot) for the echelon, 19 % more columns than rows): rows 7945, 322806 pairs per $\Delta$; amplitudes $\approx150$ ms per column ($\times2.2$ rows, a little more per row at $d=5$); echelon, assumed linear in the rows, $\approx24\,\mu$s per (column, pivot); $\approx9700$ columns → $\approx42$ min. Memory: $7945^2\times8$ B $\approx505$ MB for the echelon, $\approx650$ MB peak, inside 1.5 GB. Decision: run last, after (ii), (iv) and the break legs, if the budget of the run allows it. The outcome (stopped after the first 1000 columns on a re-measured rate) is in §3.

## §3 Runs

(one line per completed run; script `codes/verify-ph31-rank-half.py`, seed 20261093, per-part generator `random.Random(f"20261093-{part}")`; single process, `OMP/OPENBLAS/MKL_NUM_THREADS=1`; peak memory from `/usr/bin/time -v`; logs in `agent/scratch/computator/computator-093-ph31-rank-half-20261004T233900/`)

- **Run 0** (`smoke-dim.log`, 6.6 s, peak 77 MB): `G1-dim-34`, `G1-dim-35`, `G1-dim-42` PASS (generating function = Fock enumeration per block = scan rows: 3608, 7945, 2927). Engine smoke test at $K=L=2$, $d=2$ (part `smoke`, not in the final set): $\alpha'_{\rm v}=\tfrac12$ 73/73 after 88 columns; antisymmetrised columns rank 0; $\alpha'_{\rm v}=0$: $b$-alone 3 relations, rank 68/73 after 200 columns, 0 non-zero pairings, sign-flipped $b$-relations 4 non-zero pairings — the 078/083 numbers.
- **Run (i)** (`run-i.log`, part `i`, wall 6:26, **peak 196.5 MB**): **$K=3$, $L=2$, $d=4$, $\alpha'_{\rm v}=\tfrac12$, $\gamma'=3$: rank 3608/3608 over $\mathbb F_p$** after 4278 unordered pairs (one $\Delta$, of 102378 pairs; 364.9 s; vertex 8.7 s), momentum $P=(1198607414, 939924080, 1337140248, 416864837)$, $\Delta$ in `results-i.json`. `G2-rank` PASS. Antisymmetrised columns: rank 0/3608 on 200 pairs (12.3 s), `BREAK-antisym-34` PASS. Rank growth: 1:1 up to $\approx2500$ columns, then slower (3460 after 4000 columns, the last 148 in 278 columns): 19 % more columns than rows, against 9 % at $d=3$.
- **Run (iv)** (`run-iv.log`, part `iv`, wall 0:54, **peak 181.5 MB**): **$\gamma'=\tfrac32$, $\alpha'_{\rm v}=\tfrac12$, $K=3$, $L=2$, $d=2$: rank 487/487** after 498 pairs (one $\Delta$, 3.2 s), $P=(1962262394, 686480202)$; `G5-gamma` PASS; antisymmetrised columns rank 0/487 (`BREAK-antisym-32` PASS). Engine check of an exact symmetry ($f_1^{(\gamma'/\kappa)}(w)=f_1^{(\gamma')}(\kappa w)$, critic #13), at a point where the rank is not full: **$\gamma'=\tfrac32$, $\alpha'_{\rm v}=0$, same size: 60 joint relations** (12670 functionals, 25.7 s; the vertex datum $z=f_1(0)=1/(2\beta)$ does not depend on $\gamma'$, so the identities are the same) **and rank 427/487** after 1131 pairs (6.0 s, early stop at $487-60$), 300 post-stop pairs add nothing; `G5-gamma-alpha0` PASS. Both numbers equal R84's at $\gamma'=3$.
- **Run (ii)** (`run-ii-first.log`, part `ii`, wall 16:27, **peak 248.8 MB**, vertex at mode cutoff 5 in 21.8 s): **$K=4$, $L=2$, $d=2$, $\alpha'_{\rm v}=\tfrac12$, $\gamma'=3$: rank 2882/2927, deficit 45**, $P=(2051951019, 188120195)$: the first $\Delta$ gives 2882 after all 5151 pairs (240 s), the second $\Delta$ adds nothing over all 5151 pairs (saturated, 078's stopping rule; 10302 columns, 458.6 s). **Every $(N,\bar N)$ block is onto separately** ((4,4) 1764/1764, (2,4),(4,2) 306/306, …): the 45 missing directions are relations between blocks. Antisymmetrised columns rank 0/2927 (`BREAK-antisym-42` PASS). **$L=3$ capped scan** (pairs with a level-3 input, 667 inputs, 217627 such pairs per $\Delta$, same $P$, on top of the $L=2$ echelon): **2882 → 2927/2927 after 709 pairs** (32.7 s): onto with inputs of level $\le3$. **Second momentum** (same script run, the momentum drawn from the part's generator after the $L=3$ scan; not printed by this version of the script): rank 2882/2927 after the first $\Delta$ (reached at $\approx3000$ pairs), the second $\Delta$ adds nothing over all 5151 pairs (458.2 s): the same saturated deficit 45. Labels in this log: the $L=2$ line was printed as `FAIL G3-rank` (the check was then "rank = dim at $L=2$") and the $L=3$ and second-momentum lines with placeholder `PASS` conditions; the script was then revised to encode the claims (`G3.1-L2-saturated`: saturation over $\Delta$ below the dimension; `G3-L3`: rank = 2927; `G3.2-P2`: same saturated rank at a second momentum; new `G3.1-null-blocks`) and part `ii` re-run (below), which reproduced every number of this run.
- **Run i0 = break leg of (i)** (`run-i0.log`, part `i0 budget=1000`, wall 1:20, **peak 219.9 MB**): $\alpha'_{\rm v}=0$, $\gamma'=3$, $K=3$, $L=2$, $d=4$: **$b$-alone relations 96** (64722 functionals, 1.9 s) $=4\cdot4^2+7\cdot4+4$, R84's formula at a fourth value of $d$ (`G6-b-count-34` PASS); 1000 random pairs: rank 900; the 96 relations pair to zero with all 900 image vectors (`G6-annihilate-34` PASS), the $z^2\to-z^2$ relations give 268 non-zero pairings (`BREAK-G6-flip-34` PASS). With 1000 columns the bound rank $\le3608-96$ is automatic, so no `G6-not-onto` check is run; the bound for every number of columns follows from the annihilation and the exact identity (R84).
- **Run ii0 = break leg of (ii)** (`run-ii0.log`, part `ii0 budget=1000 ndelta=1`, wall 1:00, **peak 215.6 MB**): $\alpha'_{\rm v}=0$, $K=4$, $d=2$, inputs of level $\le3$ (the level at which the $\alpha'_{\rm v}=\tfrac12$ row is onto): **$b$-alone relations $\ge304$** ($\chi$ level $\le5$, 38186 functionals, 1.2 s; a new number, no prediction; completeness of $\chi$ level $\le K+1$ at $K=4$ not shown); 1000 random pairs (222778 per $\Delta$): rank 763; 0 non-zero pairings of the 304 relations with the image, including level-3 inputs (`G6-annihilate-42` PASS); flipped relations 26719 non-zero pairings (`BREAK-G6-flip-42` PASS). So at $\alpha'_{\rm v}=0$ the $K=4$ rank is $\le2927-304=2623$ for every input level (valid whether or not 304 is the complete $b$-count: these are exact relations), while at $\alpha'_{\rm v}=\tfrac12$ the same engine reaches 2927 at $L=3$.
- **Run den** (`run-den.log`, part `den`, wall 0:32, **peak 85.6 MB**): `G7-den-32-3`, `G7-den-43-3`, `G7-den-32-3_2` PASS — the $\alpha'_{\rm v}=\tfrac12$ vertex data at $\gamma'=3$ (mode cutoffs 4, 5) and $\gamma'=\tfrac32$ (cutoff 4) have 438, 633, 438 rational coefficients, largest denominators 157464, 7558272, 19683, all below $p$: the $\mathbb F_p$ matrices are reductions of the rational ones (needed by G7).
- **Run (iii) — stopped** (`run-iii.log`, part `iii`, killed by hand (SIGTERM) after 1000 columns, wall 3:29, peak 190.8 MB at that point): $K=3$, $L=2$, $d=5$, $P=(1830913421, 488462395, 1181436853, 1757268859, 198625126)$, rank 998 after 1000 pairs (177.6 s; not a result). Measured rates: 154 ms per column at low rank (amplitudes, as estimated) but the echelon update costs $\approx67\,\mu$s per (column, pivot) at 7945 rows, against $\approx10\,\mu$s at 3608 (more than the linear scaling assumed in §2: the 64 kB vectors and the reduced-echelon back-substitution, with run 094 sharing the machine's memory bandwidth). Extrapolation: $\approx3300$ s to rank $\approx7945$ plus $\approx1500$ extra columns at $\approx0.7$ s, **$\approx73$ min in total, beyond the budget of the run**: stopped, per the brief's rule. Memory would have stayed below 1 GB (505 MB echelon). Row (iii) is not obtained.
- **Run (ii) re-run with the final script** (`run-ii.log`, part `ii`, wall 16:36, **peak 249.4 MB**; the first run's files are kept as `run-ii-first.log`, `results-ii-first.json`, `checks-ii-first.json`): same momentum $P=(2051951019, 188120195)$, same numbers — rank history $[2882,2882]$ (475.2 s), every block onto separately (`G3.1-L2-saturated` PASS); antisymmetrised columns 0/2927 (`BREAK-antisym-42` PASS); left-null space of the $L=2$ image: 45 vectors, rank of their projection on the blocks $(2,2)$ 6, $(2,4)$ and $(4,2)$ 22 each, $(3,3)$ 1, $(4,4)$ 39, all other blocks 0, none supported in a single block (`G3.1-null-blocks` PASS); $L=3$ capped scan 2882 → 2927/2927 after 709 pairs (32.3 s, `G3-L3` PASS); second momentum $P_2=(510465446, 1832801432)$: rank history $[2882,2882]$ (450.3 s, `G3.2-P2` PASS). 5/5 PASS.

- **Fix-pass runs** (2026-10-05, parts `k2l1`, `c44a`, `c44`, `c44s`, `c45`, `c45t`, scratch `agent/scratch/computator/computator-093-fix-20261005T012100/`): see F1(b)–(d) and the Verification block; largest peak 212.3 MB (`c44s`).
- **Fix-pass-2 runs** (2026-10-05, parts `k2l1`, `c45t`, `c44`, `c44s` of the revised script, tag `fix2`; by-hand break legs; logs in `agent/scratch/computator/computator-093-fix2-20261005T021500/`): 31/31 PASS, exit 0 each; largest peak 208.0 MB (`c44s`). See the Verification block.

## §4 Rank table and break legs

$\beta=\tfrac32$; exact ranks over $\mathbb F_p$, $p=2^{31}-1$, at a random momentum; "columns" = unordered input pairs used; early stop at the block dimension (rows (i)–(iv)) or at $\dim-n_{\rm rel}$ (the $\alpha'_{\rm v}=0$ control of (iv)).

| row | $\alpha'_{\rm v}$ | $\gamma'$ | $K$ | $L$ | $d$ | rank / dim | columns ($\Delta$ samples) | time | peak memory |
|---|---|---|---|---|---|---|---|---|---|
| (i) | 1/2 | 3 | 3 | 2 | 4 | **3608/3608** | 4278 (1) | 365 s | 197 MB |
| (ii) | 1/2 | 3 | 4 | 2 | 2 | 2882/2927, saturated (deficit 45; every block onto separately) | 10302 (2; the 2nd adds 0) | 475 s (re-run; 459 s first run) | 249.4 MB (whole part, re-run) |
| (ii) | 1/2 | 3 | 4 | 2 | 2 | 2882/2927 at a second momentum $P_2$, saturated | 10302 (2) | 450 s | (same process) |
| (ii) | 1/2 | 3 | 4 | $\le3$ | 2 | **2927/2927** | $L=2$ echelon + 709 pairs with a level-3 input (1) | 32 s | (same process) |
| (iv) | 1/2 | 3/2 | 3 | 2 | 2 | **487/487** | 498 (1) | 3.2 s | 181 MB (whole part) |
| (iv) control | 0 | 3/2 | 3 | 2 | 2 | 427/487 = $487-60$ (60 joint relations); +300 post-stop pairs add 0 | 1131 + 300 (1) | 6.0 s + 25.7 s count | (same process) |
| (iii) | 1/2 | 3 | 3 | 2 | 5 | not obtained (stopped at 998 after 1000 columns; extrapolated 73 min) | — | — | 190.8 MB at stop |

Break legs (one per new row type; the $\alpha'_{\rm v}=0$ legs use 1000 random pairs, so they test the pipeline's sensitivity to the vertex, not the size of the $\alpha'_{\rm v}=0$ cokernel):

| leg | row type | outcome | must be |
|---|---|---|---|
| `BREAK-antisym-34` | $K=3$, $d=4$ | rank 0/3608 on 200 antisymmetrised pairs | 0 (exchange symmetry) |
| `BREAK-antisym-42` | $K=4$, $d=2$ | rank 0/2927 | 0 |
| `BREAK-antisym-32` | $K=3$, $d=2$, $\gamma'=\tfrac32$ | rank 0/487 | 0 |
| `G6-b-count-34` | $\alpha'_{\rm v}=0$, $K=3$, $d=4$ | 96 $b$-relations | $b(3,4)=96$ (R84) |
| `G6-annihilate-34` / `BREAK-G6-flip-34` | same | 0 / 268 non-zero pairings with the image (900 vectors) | 0 / $>0$ |
| `G6-b-count-42` (logging line) | $\alpha'_{\rm v}=0$, $K=4$, $d=2$ | $\ge304$ $b$-relations ($\chi$ level $\le5$) | logged (new) |
| `G6-annihilate-42` / `BREAK-G6-flip-42` | same, inputs of level $\le3$ | 0 / 26719 non-zero pairings (763 vectors) | 0 / $>0$ |

**Reading.** At $\alpha'_{\rm v}=0$ the 96 (resp. $\ge304$) $b$-relations are exact left-null vectors of the projected map for every input level (R84's identity, Proven), and the engine finds them annihilating the measured image; so the same engine, on the same rows, cannot report full rank at $\alpha'_{\rm v}=0$ (rank $\le3512$ at $d=4$, $\le2623$ at $K=4$). The full ranks at $\alpha'_{\rm v}=\tfrac12$ are therefore not a property of the pipeline in the ghost sector. The $b$-identity is matter-blind, so these legs test the ghost sector, $z^2$ and the matter indexing of the relations; the matter Neumann data at $d=4$ and at mode 5 are tested only by exchange symmetry (blind to a leg-symmetric error: $N^{11}=N^{22}$) and by the $d$-genericity of the code (critic #9). The fix-pass checks (F1) are matter-blind as well. $b(3,4)=96$ is a fourth machine check of R84's formula $b(3,d)=4d^2+7d+4$ (before: $d\le3$). $b(4,2)\ge304$ ($\chi$ level $\le5$) is new; the joint ($b+L$) count at $K=4$ was not computed.

**The $K=4$, $L=2$ deficit.** Three measured facts locate it.
1. It is saturated: a second $\Delta$ sample adds nothing over all 5151 pairs, at three momenta ($P$, $P_2$ of run (ii), $P_3$ of part `c44s`); the deficit mod $p$ is 45 at each.
2. It is not in any single block: the image projected on each $(N,\bar N)$ block of $W^{\rm even}_{\le4}$ is onto that block, so the 45 missing directions are linear relations between blocks.
3. It is closed by level-3 inputs: 709 random pairs with a level-3 input raise the rank from 2882 to 2927.

Its mechanism is the pole structure of the $c$-ghost correlator (fix pass F1, after critic #1). In an input frame, $c(w)A(0)$ is singular only through $c_nA$, $n\ge2$, and $c_nA=0$ for $n$ above the level of $A$; with inputs of level $\le2$ the correlator with a $c$ insertion has at most simple poles at the two input punctures $\pm z$. Two exact consequences, at every $\alpha'_{\rm v}$, $\gamma'$ and $P$:
- (F.6): the quadratic differential $(u^2-z^2)\,du^2$ vanishes at both inputs, so its conservation law gives the left-null vectors $(c_{-4}-z^2c_{-2})(c_1\otimes\bar\chi)$ and their conjugates — 44 at $K=4$, $d_{\rm eff}=2$, with block projections $(4,4)$ 38, $(2,4)$ 22, $(4,2)$ 22, $(2,2)$ 6;
- (F.13): no input of level $\le2$ at ghost number 2 contains both $b_{-2}$ and $\bar b_{-2}$, so the correlator with $c(u)\bar c(\bar u)$ has no simultaneous pole at one input, which gives $(c_{-3}\bar c_{-3}+z^2c_{-2}\bar c_{-2})|0\rangle$, the relation that ties $(4,4)$ to $(3,3)$.

These 45 relations are independent, so the rank at every $P$ is $\le2882$; with G7 the generic rank is exactly 2882 and the generic deficit exactly 45. Checks, by relation. The 44 of (F.6) annihilate the image on the saturated scan and on random columns at $\alpha'_{\rm v}=\tfrac12,\tfrac15,0$, lie in its left-null space, and their sign-flipped versions do not annihilate it (F1(b)). The 45th, (F.13), is checked informatively at $\alpha'_{\rm v}=\tfrac12$ — it lies in the left-null space of the whole image at two momenta and its sign flip does not (`G3.9-y45-in-null`, fix pass 2), it spans the saturated null space modulo the 44 with the predicted ratio 9, and it vanishes on targeted columns — and at $\tfrac15$ (targeted columns); its random-column test (part `c45`, retired) and its $\alpha'_{\rm v}=0$ test are empty (F1(b')). Together they span the left-null space. Level-3 inputs break both: $c_3$ acts on inputs with $b_{-3}$ (resp. $\bar b_{-3}$), which violate exactly the holomorphic (resp. antiholomorphic) vectors (F.10, observed chirality by chirality), and inputs such as $b_{-2}c_{-1}\otimes\bar b_{-2}\bar c_{-1}$ carry a pole in both chiralities.

This deficit is not of R84's type: R84's relations hold for inputs of every level and need $\alpha'_{\rm v}=0$, whereas these hold at every $\alpha'_{\rm v}$ for inputs of bounded level. They are ghost-sector identities of the same contour type, the failure mode PH31's Motivation anticipates, but level-limited. Relations of type (F.6) at input level $L$ exist iff $K\ge2L$ (F.9), so the minimal closing level obeys $L_{\min}(K)\ge\lfloor K/2\rfloor+1$, which equals the observed 2, 2, 3 at $K=2$, 3, 4 (at $d_{\rm eff}=2$ for $K=2,4$; at $K=3$ the value 2 combines the measured full rank at $L=2$ with (F.9) at $L=1$, where $K=3$ was not run). At $K=2$, $L=1$ the same law ($\phi=1$) predicts 6 vanishing rows of the $(2,2)$ block: measured rank 67/73, left-null space exactly those rows (F1(c)).

*Remark (counting argument, critic #2).* At fixed $L$ the image over all functions of $\Delta$ is spanned by the Taylor coefficients in $\Delta$ of the columns. Premise: the columns are polynomial in $\Delta$ once the plane-wave prefactor is dropped, which is legitimate because it is a common non-zero scalar of the two orderings ($|\rho_1|=|\rho_2|$, $h_2=-h_1$). Each amplitude has degree $\le2K+4L$ in $\Delta$, so their span has dimension $\le5151\binom{2K+10}{2}$ at $d=2$, $L=2$, polynomial in $K$, while $\dim W^{\rm even}_{\le K}$ grows like $\exp(c\sqrt K)$. The bound first forces a deficit at $K=9$ ($1.95\times10^6$ against $3.82\times10^6$; at $K=8$: $1.67\times10^6$ against $1.06\times10^6$). It says nothing at $K=4$.

## §5 What changes in R84 and PH31 (proposed lines)

Revised in fix pass 1 (critic #1, #3, #5, #11, #12, #14) and fix pass 2 (critic iteration 2 #8–#13; the PH31 and R84 lines are the critic's accepted text). The lines cite the orchestrator's re-run of the final script, all parts: `dim`, `den`, `i`, `iv`, `ii`, `i0`, `ii0` and the fix-pass parts `k2l1`, `c44a`, `c44`, `c44s`, `c45t` (part `c45` retired in fix pass 2); logging lines (Verification block) and the INFO line of `c45t` are not counted as checks.

**PH31.** Heading unchanged (`supported – R84 at $\alpha'_{\rm v}=\tfrac12$ (finite level)`). Proposed verification line:

> 2026-10-05 – falsifier run – record 093 (`codes/verify-ph31-rank-half.py`, seed 20261093; orchestrator's re-run of the final script; critics `critic-093-20261005T005700`, `critic-093-iter2-20261005T015500`): at $\alpha'_{\rm v}=\tfrac12$ the level-projected circle map is onto at $K=3$, $L=2$, $d_{\rm eff}=4$ (3608/3608) and at $K=4$, $d_{\rm eff}=2$ with inputs of level $\le3$ (2927/2927); full ranks over $\mathbb F_p$ at the sampled momentum, lifted to generic $P$ (non-zero maximal minor; no denominator of the vertex data divisible by $p$). With inputs of level $\le2$ the $K=4$ rank is 2882 (mod $p$, saturated in $\Delta$ at three momenta, every $(N,\bar N)$ block onto separately) and exactly 2882 at generic $P$: the 45 missing directions are exact relations from the pole structure of the $c$-ghost correlator with inputs of level $\le2$ (hand derivation, record 093 F1) — 44 from the conservation law of $(u^2-z^2)\,du^2$, $(c_{-4}-z^2c_{-2})(c_1\otimes\bar\chi)$ and conjugates, and $(c_{-3}\bar c_{-3}+z^2c_{-2}\bar c_{-2})|0\rangle$ from the absence of inputs with both $b_{-2}$ and $\bar b_{-2}$ — valid at every $\alpha'_{\rm v}$ (the 44 checked on columns at $\tfrac12$, $\tfrac15$, 0; the 45th at $\tfrac12$, with its predicted coefficient in the saturated null space, and at $\tfrac15$); level-3 inputs close the deficit, violating the relations exactly through inputs with $b_{-3}$ or $\bar b_{-3}$. Not of R84's type (R84's relations hold for inputs of every level and need $\alpha'_{\rm v}=0$). The holomorphic law exists at input level $L$ iff $K\ge2L$, so the minimal closing level obeys $L_{\min}(K)\ge\lfloor K/2\rfloor+1$, with equality at $K=2,4$ ($d_{\rm eff}=2$) and $K=3$ ($L=1$ by the law); at $K=2$, $L=1$ the law predicts and the run finds 67/73. The controls are ghost-sector: the $\alpha'_{\rm v}=0$ break legs and the $c$-ghost checks are matter-blind, and the matter data at $d_{\rm eff}=4$ and mode 5 are tested only by exchange symmetry. $\gamma'=\tfrac32$: 487/487, and at $\alpha'_{\rm v}=0$ 60 relations and 427/487, as at $\gamma'=3$ (engine check of an exact symmetry). $d_{\rm eff}=5$ ($K=3$, $L=2$, 7945 rows): attempted, stopped for time after 1000 columns, no claim.

**Proposed – Harold's decision (change to a registered hypothesis's falsifier).** Not adopted: not to be promoted without Harold's go (critic iteration 2 #8). Proposed addition to PH31's **Would be falsified by** (critic #5's wording, adapted to F1):

> "… a persistent deficit for growing $K$ and $L$: at some $K$, a deficit that survives at $L\ge\lfloor K/2\rfloor+1$ and does not shrink over further increments of $L$, or an exact left-null identity valid for inputs of every level (R84's type). Deficits from the pole structure of the $c$-ghost correlator at bounded input level — the conservation law of $(u^2-z^2)^{L-1}g(u)\,du^2$, with left-null vectors at every $K\ge2L$, and the one-input selection rules such as $(c_{-3}\bar c_{-3}+z^2c_{-2}\bar c_{-2})|0\rangle$ at $L=2$ — are not falsifiers ($K=4$, $d_{\rm eff}=2$: 45 at $L=2$, closed at $L=3$, record 093). Closure at every $K$ is necessary for PH31, not sufficient (the extension is not continuous level by level)."

Optional tightening (critic iteration 2 #8): in the second sentence, "Deficits from relations of the $c$-ghost pole structure that hold only below a finite input level and disappear when $L$ is raised …" in place of "Deficits from the pole structure of the $c$-ghost correlator at bounded input level …", so that a deficit cannot be set aside by its label alone.

**R84.** Proposed Scope edits (matter content and $\gamma'$):
- "$b(3,d)=4d^2+7d+4$ (machine-checked at $d\le3$ …)" → "(machine-checked at $d\le4$: 96 at $d=4$, record 093 …)"; add "$b$-alone relations at $K=4$, $d_{\rm eff}=2$: $\ge304$ ($\chi$ level $\le5$; completeness of that $\chi$ range at $K=4$ not shown; the joint count at $K=4$ not computed), record 093".
- After the $\gamma'$-independence sentence: "checked at $\gamma'=\tfrac32$, $K=3$, $L=2$, $d_{\rm eff}=2$: $\alpha'_{\rm v}=0$ 60 relations and 427/487, $\alpha'_{\rm v}=\tfrac12$ 487/487 (record 093; an engine check of the exact rescaling symmetry)".
- Add to the $\alpha'_{\rm v}=\tfrac12$ part: "at fixed input level $L$ the map has exact level-limited relations at every $\alpha'_{\rm v}$ (the $c$-ghost pole structure, record 093 F1), present iff $K\ge2L$ for the holomorphic law; the full-rank rows at $L=2$, $K\le3$ are below that threshold".

Proposed R84 verification line:

> 2026-10-05 – exact check over $\mathbb F_p$ – `codes/verify-ph31-rank-half.py`, seed 20261093, record 093 (orchestrator's re-run of the final script): at $\alpha'_{\rm v}=\tfrac12$ full rank at $K=3$, $L=2$, $d_{\rm eff}=4$ (3608/3608) and at $K=4$, $d_{\rm eff}=2$ with inputs of level $\le3$ (2927/2927), lifted to generic $P$; with inputs of level $\le2$, 2882/2927 mod $p$ at three momenta, saturated, the 45 relations identified as exact $c$-ghost relations (record 093 F1), so the generic rank is exactly 2882; closed by level-3 inputs; $K=2$, $L=1$: 67/73 as the same law predicts. At $\alpha'_{\rm v}=0$: $b(3,4)=96$ (formula), $b$-alone $\ge304$ at $K=4$, $d_{\rm eff}=2$ ($\chi$ level $\le5$), both annihilating the measured image on 1000 random columns (900 and 763 image vectors; level-3 inputs included at $K=4$; sign-flipped relations do not); these legs are matter-blind. $\gamma'=\tfrac32$ reproduces the $\gamma'=3$ numbers (60, 427/487; 487/487; engine check of an exact symmetry). $K=3$, $d_{\rm eff}=5$: not obtained (stopped for time).

Proposed R84 **Status**, added clause (critic iteration 2 #11, the critic's text; separate from the existing "full rank at $\alpha'_{\rm v}=1/2$ … — Verified" clause, which is not extended):

> at $\alpha'_{\rm v}=\tfrac12$: full rank at $K=3$, $L=2$, $d_{\rm eff}=4$ and at $K=4$, $L\le3$, $d_{\rm eff}=2$ — Verified (record 093); $K=4$, $L=2$, $d_{\rm eff}=2$: generic rank exactly 2882/2927 — the 45 level-limited $c$-ghost relations Proven (record 093 F1, hand derivation; consequences machine-checked with break legs), the lower bound Verified (mod $p$, lifted)

Tag calibration. The 45 relations are a complete hand proof ((F.1)–(F.13), with the "only if" half of (F.9) for combinations added in fix pass 2), not a machine check: they are tagged Proven with "hand derivation", and what is machine-checked is their consequences (annihilation of the image at three vertices, membership in the measured left-null space, the level-3 violation pattern, the $K=2$, $L=1$ prediction), each with a break leg. The $K=4$, $L=2$ row is not a full-rank row: it gets its own clause (upper bound Proven by the relations, lower bound $\ge2882$ Verified mod $p$ with the G7 lift), not a place in the full-rank row set. Nothing changes in R84's refutation at $\alpha'_{\rm v}=0$, in R86, or in R80's routing.

Proposed R84 narrative edit (critic iteration 2 #12, a proposal): in "For $\alpha'_{\rm v}\ne0$ the vector field picks up a $w^2\partial_w$ term in the local frames, no selection rule follows, …", append after "no selection rule follows": "(no every-level rule; at input level $L$ there are level-limited $c$-ghost relations once $K\ge2L$, record 093)". Whether the $c$-ghost law deserves its own ledger entry (it is a property of the circle map at every $\alpha'_{\rm v}$, not of the $\alpha'_{\rm v}=0$ selection rule R84 is about) is the orchestrator's call.

## Verification

`codes/verify-ph31-rank-half.py` (imports 078's, 083's and 087's scripts unchanged), seed 20261093, one part per invocation, run from the project root with `.venv/bin/python -u codes/verify-ph31-rank-half.py <part>` under `/usr/bin/time -v`, single process, `OMP/OPENBLAS/MKL_NUM_THREADS=1`. Parts: `dim` (with the smoke test in run 0), `den`, `i`, `iv`, `ii` (re-run), `i0 budget=1000`, `ii0 budget=1000 ndelta=1`, `iii` (stopped). PASS/FAIL lines as printed by the final script (smoke-test lines, part `smoke`, and the `SUMMARY` line's smoke count in `smoke-dim.log` refer to the engine test, not to the final set):

```
# smoke-dim.log
PASS  G1-dim-34: K=3, d=4: dim W^even_<=K = 3608 (Fock rows 3608, gf = Fock per block: True); even blocks {'0,0': 1, '0,2': 15, '1,1': 18, '1,3': 222, '2,0': 15, '2,2': 275, '3,1': 222, '3,3': 2840}
PASS  G1-dim-35: K=3, d=5: dim W^even_<=K = 7945 (Fock rows 7945, gf = Fock per block: True); even blocks {'0,0': 1, '0,2': 21, '1,1': 27, '1,3': 412, '2,0': 21, '2,2': 513, '3,1': 412, '3,3': 6538}
PASS  G1-dim-42: K=4, d=2: dim W^even_<=K = 2927 (Fock rows 2927, gf = Fock per block: True); even blocks {'0,0': 1, '0,2': 6, '0,4': 32, '1,1': 6, '1,3': 44, '2,0': 6, '2,2': 54, '2,4': 306, '3,1': 44, '3,3': 326, '4,0': 32, '4,2': 306, '4,4': 1764}
SUMMARY: 9/9 PASS (6 s, peak rss 76.4 MB)
# run-den.log
PASS  G7-den-32-3: alpha'_v=1/2, gamma'=3, mode cutoff 4: 438 rational coefficients, largest denominator 157464, none divisible by p
PASS  G7-den-43-3: alpha'_v=1/2, gamma'=3, mode cutoff 5: 633 rational coefficients, largest denominator 7558272, none divisible by p
PASS  G7-den-32-3_2: alpha'_v=1/2, gamma'=3/2, mode cutoff 4: 438 rational coefficients, largest denominator 19683, none divisible by p
SUMMARY: 3/3 PASS (32 s, peak rss 83.2 MB)
# run-i.log
PASS  G2-rank: alpha'_v=1/2, gamma'=3, K=3, L=2, d=4: rank 3608/3608 mod p, 4278 columns (1 Delta, 102378 pairs per Delta), 364.9 s, peak rss 191.7 MB
PASS  BREAK-antisym-34: antisymmetrised columns, 200 pairs: rank 0/3608 (must be 0), 12.3 s
SUMMARY: 2/2 PASS (386 s, peak rss 191.9 MB)
# run-iv.log
PASS  G5-gamma: alpha'_v=1/2, gamma'=3/2, K=3, L=2, d=2: rank 487/487 mod p, 498 columns (1 Delta, 5151 pairs per Delta), 3.2 s, peak rss 81.3 MB
PASS  BREAK-antisym-32: antisymmetrised columns, 200 pairs: rank 0/487 (must be 0), 1.0 s
PASS  G5-gamma-alpha0: gamma'=3/2, alpha'_v=0, K=3, L=2, d=2: 60 joint relations (12670 functionals, 25.7 s), rank 427/487 after 1131 columns, post-stop {'pairs': 300, 'rank_before': 427, 'rank_after': 427, 'time_s': 1.5} (R84 at gamma'=3: 60, 427/487)
SUMMARY: 3/3 PASS (54 s, peak rss 177.2 MB)
# run-ii.log
PASS  G3.1-L2-saturated: alpha'_v=1/2, gamma'=3, K=4, L=2, d=2: rank 2882/2927 mod p, 10302 columns (2 Delta, 5151 pairs per Delta, rank history [2882, 2882]), 475.2 s, peak rss 220.9 MB; per block (rank, dim) {'0,0': (1, 1), '0,2': (6, 6), '0,4': (32, 32), '1,1': (6, 6), '1,3': (44, 44), '2,0': (6, 6), '2,2': (54, 54), '2,4': (306, 306), '3,1': (44, 44), '3,3': (326, 326), '4,0': (32, 32), '4,2': (306, 306), '4,4': (1764, 1764)}
PASS  BREAK-antisym-42: antisymmetrised columns, 200 pairs: rank 0/2927 (must be 0), 5.8 s
PASS  G3.1-null-blocks: K=4, L=2: 45 left-null vectors of the image; rank of their projection per block {'0,0': 0, '0,2': 0, '0,4': 0, '1,1': 0, '1,3': 0, '2,0': 0, '2,2': 6, '2,4': 22, '3,1': 0, '3,3': 1, '4,0': 0, '4,2': 22, '4,4': 39}; relations supported in a single block 0 (must be 0: every block is onto separately)
PASS  G3-L3: K=4, L=3 capped (pairs with a level-3 input, 6000 per Delta) on top of L=2: rank 2882 -> 2927/2927
PASS  G3.2-P2: K=4, L=2, second momentum (510465446, 1832801432): rank 2882/2927 (rank history [2882, 2882]; first momentum 2882), 450.3 s
SUMMARY: 5/5 PASS (996 s, peak rss 243.5 MB)
# run-i0.log
PASS  G6-b-count-34: alpha'_v=0, K=3, d=4: b-alone relations 96 (64722 functionals, 1.9 s); R84's b(3,d) = 4d^2+7d+4 = 96
PASS  G6-annihilate-34: b-relations x alpha'_v=0 image (96 x 900): 0 non-zero pairings
PASS  BREAK-G6-flip-34: b-relations with z^2 -> -z^2 (96): 268 non-zero pairings (must be > 0)
SUMMARY: 3/3 PASS (79 s, peak rss 214.8 MB)
# run-ii0.log
PASS  G6-b-count-42: alpha'_v=0, K=4, d=2: b-alone relations 304 (38186 functionals, chi level <= 5, 1.2 s) (no prediction; logged)
PASS  G6-annihilate-42: b-relations x alpha'_v=0 image (304 x 763): 0 non-zero pairings
PASS  BREAK-G6-flip-42: b-relations with z^2 -> -z^2 (304): 26719 non-zero pairings (must be > 0)
SUMMARY: 3/3 PASS (60 s, peak rss 210.5 MB)
# run-iii.log: stopped by hand after 1000 columns (no check line)
```

**Original set (computator's runs): 22 PASS lines** (`dim` 3, `den` 3, `i` 2, `iv` 3, `ii` 5, `i0` 3, `ii0` 3), of which four are logging lines rather than checks (critic #4, #11, #14): `G3.1-L2-saturated` tests saturation only (it passes for any saturated deficit), `G3.1-null-blocks` (its dimension half is tautological, its single-block half restates the per-block ranks), `G6-b-count-42` (condition $>0$). The ledger lines cite the orchestrator's re-run of the final script, not these counts. Parts `ii`, `i0`, `ii0`, `den` ran the final code of their path. Parts `dim`, `i`, `iv` ran before two later edits: the main-row line now appends the rank history to its printed detail (and takes an `onto` flag whose default is the condition they ran), and new code paths were added that they do not use. Their check conditions are unchanged. Superseded: the first run of part `ii` (`run-ii-first.log`) printed 3/4 PASS. Its `FAIL G3-rank` was the check as first written ("rank = dim at $K=4$, $L=2$"), refuted by the measurement (the finding of G3.1, not an engine failure), and its `G3-L3` and `G3-P2` lines had placeholder conditions. The re-run with the revised checks reproduced every number.

**Fix-pass parts** (critic iteration 1; scratch `agent/scratch/computator/computator-093-fix-20261005T012100/`; same seed, per-part generator; run from the project root with `.venv/bin/python -u codes/verify-ph31-rank-half.py <part>` under `/usr/bin/time -v`, `OMP/OPENBLAS/MKL_NUM_THREADS=1`, one process; peak memory: `k2l1` 75.9 MB, `c44a` 108.2 MB, `c44` 211.7 MB, `c44s` 212.3 MB, `c45` 117.7 MB, `c45t` 119.8 MB). PASS/FAIL lines as printed:

```
# run-k2l1.log
PASS  G3.7-K2L1-rank: alpha'_v=1/2, gamma'=3, K=2, L=1, d=2: rank 67/73 (rank history [56, 67, 67], 198 columns, 66 pairs per Delta; predicted <= 67; 73 would refute); per block {'0,0': (1, 1), '0,2': (6, 6), '1,1': (6, 6), '2,0': (6, 6), '2,2': (48, 54)}
PASS  G3.7-K2L1-annihilate: phi = 1 relations c_-2 (c_1 (x) chi_2) and conjugates: 6 vectors (cut by truncation 0), block ranks {'2,2': 6}; 0 non-zero pairings with the L=1 image; in its left-null space (6 vectors): True
PASS  BREAK-G3.7-L2: the 6 vectors x 100 random L=2 columns: 92 non-zero pairings (must be > 0: c_2 acts on inputs with b_-2)
SUMMARY: 3/3 PASS (5 s, peak rss 75.7 MB)
# run-c44a.log
PASS  G3.5-alpha-1_5-2: alpha'_v=1/5, gamma'=2, K=4, d=2: the 44 vectors (F.7) x 150 random L=2 columns: 0 non-zero pairings (5.2 s)
PASS  BREAK-G3.5-alpha-flip-1_5-2: same with c_-4 + z^2 c_-2: 844 non-zero pairings (must be > 0)
PASS  G3.5-alpha-0-3: alpha'_v=0, gamma'=3, K=4, d=2: the 44 vectors (F.7) x 150 random L=2 columns: 0 non-zero pairings (5.1 s)
PASS  BREAK-G3.5-alpha-flip-0-3: same with c_-4 + z^2 c_-2: 496 non-zero pairings (must be > 0)
SUMMARY: 4/4 PASS (54 s, peak rss 108.2 MB)
# run-c44.log
PASS  G3.5-count: (F.7) at K=4, d=2: 22 + 22 vectors, rank 44, block projection ranks {'2,2': 6, '2,4': 22, '4,2': 22, '4,4': 38} (predicted (F.8) {'2,2': 6, '2,4': 22, '4,2': 22, '4,4': 38}); cut by truncation 0
PASS  G3.5-annihilate: fresh momentum (1445105185, 1847624051): L=2 image rank 2882/2927 after 2913 columns (146.2 s, peak rss 206.7 MB); 44 vectors x 2882 image vectors: 0 non-zero pairings
PASS  BREAK-G3.5-flip: c_-4 + z^2 c_-2 instead: 44 non-zero pairings (must be > 0)
PASS  G3.5-in-null: left-null space 45 vectors; rank of (null space + 44 vectors) 45 (= 45: the 44 lie in it); complement 1
PASS  G3.8-proj-N4: rank of the left-null space projected on the blocks with N=4 or Nbar=4: 45 (must be 45: K=3, L=2 is onto, so no null vector lives on W_<=3)
PASS  G3.8-proj-Nb4: projected on Nbar=4 only: 42 (predicted 45 - 3: the 3 holomorphic vectors with chi at level 2 live on (4,2), (2,2))
PASS  G3.9-complement: null space modulo the 44: 1 vector(s); support per block {'3,3': 1, '4,4': 1}; rows by (block, chiral charges) {'(3,3) q=(0,0)': 1, '(4,4) q=(0,0)': 1}
PASS  G3.6-L3-pattern: level-3 inputs 566 (with b_-3: 22, with bt_-3: 22); non-zero pairings (22 hol, 22 antihol) x 80 columns per set: {'no_b3': (0, 0), 'hol_b3': (1082, 0), 'ah_b3': (0, 898)} (predicted (F.10): no_b3 (0, 0); hol_b3 (>0, 0); ah_b3 (0, >0))
SUMMARY: 8/8 PASS (178 s, peak rss 206.7 MB)
# run-c44s.log
PASS  G3.5-count: (F.7) at K=4, d=2: 22 + 22 vectors, rank 44, block projection ranks {'2,2': 6, '2,4': 22, '4,2': 22, '4,4': 38} (predicted (F.8) {'2,2': 6, '2,4': 22, '4,2': 22, '4,4': 38}); cut by truncation 0
PASS  G3.9-P3-saturated: third momentum (91777430, 203495592): K=4, L=2 rank 2882/2927 mod p, rank history [2882, 2882] (10302 columns, 447.3 s, peak rss 161.7 MB)
PASS  G3.5-annihilate: fresh momentum (91777430, 203495592): L=2 image rank 2882/2927 after 10302 columns (447.3 s, peak rss 207.3 MB); 44 vectors x 2882 image vectors: 0 non-zero pairings
PASS  BREAK-G3.5-flip: c_-4 + z^2 c_-2 instead: 44 non-zero pairings (must be > 0)
PASS  G3.5-in-null: left-null space 45 vectors; rank of (null space + 44 vectors) 45 (= 45: the 44 lie in it); complement 1
PASS  G3.8-proj-N4: rank of the left-null space projected on the blocks with N=4 or Nbar=4: 45 (must be 45: K=3, L=2 is onto, so no null vector lives on W_<=3)
PASS  G3.8-proj-Nb4: projected on Nbar=4 only: 42 (predicted 45 - 3: the 3 holomorphic vectors with chi at level 2 live on (4,2), (2,2))
PASS  G3.9-complement: null space modulo the 44: 1 vector(s); support per block {'3,3': 1, '4,4': 1}; rows by (block, chiral charges) {'(3,3) q=(0,0)': 1, '(4,4) q=(0,0)': 1}
PASS  G3.6-L3-pattern: level-3 inputs 566 (with b_-3: 22, with bt_-3: 22); non-zero pairings (22 hol, 22 antihol) x 80 columns per set: {'no_b3': (0, 0), 'hol_b3': (1027, 0), 'ah_b3': (0, 1200)} (predicted (F.10): no_b3 (0, 0); hol_b3 (>0, 0); ah_b3 (0, >0))
SUMMARY: 9/9 PASS (478 s, peak rss 207.3 MB)
# run-c45.log
PASS  G3.9-y45-1_2-3: alpha'_v=1/2, gamma'=3, K=4, d=2: (c_-3 cb_-3 + z^2 c_-2 cb_-2)|0> x 150 random L<=2 columns: 0 non-zero pairings
FAIL  BREAK-G3.9-y45-1_2-3: with -z^2: 0 non-zero pairings; (F.13) on 150 columns with a level-3 input: 1 non-zero (both must be > 0)
PASS  G3.9-y45-1_5-2: alpha'_v=1/5, gamma'=2, K=4, d=2: (c_-3 cb_-3 + z^2 c_-2 cb_-2)|0> x 150 random L<=2 columns: 0 non-zero pairings
FAIL  BREAK-G3.9-y45-1_5-2: with -z^2: 0 non-zero pairings; (F.13) on 150 columns with a level-3 input: 4 non-zero (both must be > 0)
PASS  G3.9-y45-0-3: alpha'_v=0, gamma'=3, K=4, d=2: (c_-3 cb_-3 + z^2 c_-2 cb_-2)|0> x 150 random L<=2 columns: 0 non-zero pairings
FAIL  BREAK-G3.9-y45-0-3: with -z^2: 0 non-zero pairings; (F.13) on 150 columns with a level-3 input: 0 non-zero (both must be > 0)
SUMMARY: 3/6 PASS (91 s, peak rss 114.9 MB)
# run-c45t.log
PASS  G3.9-y45-1_2-3-t: alpha'_v=1/2, gamma'=3, K=4, d=2: (c_-3 cb_-3 + z^2 c_-2 cb_-2)|0> x 150 targeted L<=2 columns: 0 non-zero pairings
PASS  BREAK-G3.9-y45-1_2-3-t: with -z^2: 61 non-zero pairings; (F.13) on 150 columns with a level-3 input: 93 non-zero (both must be > 0)
PASS  G3.9-y45-1_5-2-t: alpha'_v=1/5, gamma'=2, K=4, d=2: (c_-3 cb_-3 + z^2 c_-2 cb_-2)|0> x 150 targeted L<=2 columns: 0 non-zero pairings
PASS  BREAK-G3.9-y45-1_5-2-t: with -z^2: 64 non-zero pairings; (F.13) on 150 columns with a level-3 input: 84 non-zero (both must be > 0)
PASS  G3.9-y45-0-3-t: alpha'_v=0, gamma'=3, K=4, d=2: (c_-3 cb_-3 + z^2 c_-2 cb_-2)|0> x 150 targeted L<=2 columns: 0 non-zero pairings
FAIL  BREAK-G3.9-y45-0-3-t: with -z^2: 0 non-zero pairings; (F.13) on 150 columns with a level-3 input: 0 non-zero (both must be > 0)
SUMMARY: 5/6 PASS (94 s, peak rss 117.0 MB)
```

Script versions: parts `c44a`, `c44`, `c45` ran intermediate versions of the script; the later edits added code paths (the `saturate` flag and the explicit print used by `c44s`, the `targeted` flag of `c45t`) and a `ruff format`, without changing their check conditions. Part `k2l1` was re-run on the final script (`run-k2l1-final.log`, peak 77.4 MB) and reproduced its three lines. Fix-pass tally: 32 PASS, 4 FAIL (36 lines). The four FAIL lines are break legs with no content, not failures of a relation: `c45` (random columns, all three vertices) and `c45t` at $\alpha'_{\rm v}=0$; diagnosis in F1(b'). Logging lines among the PASS: `G3.9-complement` (its condition holds by construction once `G3.5-in-null` holds), and the three `G3.9-y45-*` PASS lines of `c45` (vacuous sample). Informative checks of the fix pass: `G3.7-K2L1-rank`, `G3.7-K2L1-annihilate`, `BREAK-G3.7-L2`; `G3.5-count`, `G3.5-annihilate`, `BREAK-G3.5-flip`, `G3.5-in-null` (twice: `c44`, `c44s`), `G3.5-alpha-*` with `BREAK-G3.5-alpha-flip-*`; `G3.6-L3-pattern` (twice); `G3.8-proj-N4`, `G3.8-proj-Nb4` (twice); `G3.9-P3-saturated`; `G3.9-y45-*-t` with `BREAK-G3.9-y45-*-t` at $\alpha'_{\rm v}=\tfrac12$, $\tfrac15$. The explicit form of the 45th vector (ratio 9) is a printed line of `run-c44s.log`, compared by hand to the prediction (F.13).

(Fix-pass-1 tally above: superseded by fix pass 2, which replaces the four FAIL legs and retires part `c45`.)

**Fix pass 2** (critic iteration 2; script edits #4, #6; runs 2026-10-05, `.venv/bin/python -u codes/verify-ph31-rank-half.py <part> fix2` from the project root under `/usr/bin/time -v`, `OMP/OPENBLAS/MKL_NUM_THREADS=1`, one process at a time). The extra argument `fix2` only sets the output tag: the JSON outputs are `checks-<part>-fix2.json`, `results-<part>-fix2.json` in the fix-pass-1 scratch (earlier files left in place), the logs `run-<part>-fix2.log` in `agent/scratch/computator/computator-093-fix2-20261005T021500/`. The per-part generators are unchanged, so every draw (momenta, $\Delta$, pairs) is that of fix pass 1, and every number the earlier runs printed is reproduced (67/73; 61, 93, 64, 84; 2882 at $P=(1445105185, 1847624051)$ and $P_3=(91777430, 203495592)$, 44, 45, 42, ratio 9; 1082/898 and 1027/1200). Peak memory (`/usr/bin/time -v`, kB/1024): `k2l1` 76.5 MB, `c45t` 123.1 MB, `c44` 207.6 MB, `c44s` **208.0 MB** (largest), by-hand legs 123.9 MB. Exit status 0 for each of the four parts. Part `c44a` was not re-run (no change in its code path); the original parts are unchanged in code and conditions.

```
# run-k2l1-fix2.log
PASS  G3.7-K2L1-rank: alpha'_v=1/2, gamma'=3, K=2, L=1, d=2: rank 67/73 (rank history [56, 67, 67], 198 columns, 66 pairs per Delta; predicted = 67, saturated; 73 would refute the law, < 67 an extra relation); per block {'0,0': (1, 1), '0,2': (6, 6), '1,1': (6, 6), '2,0': (6, 6), '2,2': (48, 54)}
PASS  G3.7-K2L1-annihilate: phi = 1 relations c_-2 (c_1 (x) chi_2) and conjugates: 6 vectors (cut by truncation 0), block ranks {'2,2': 6}; 0 non-zero pairings with the L=1 image; in its left-null space (6 vectors, must be 6): True
PASS  BREAK-G3.7-L2: the 6 vectors x 100 random L=2 columns: 92 non-zero pairings (must be > 0: c_2 acts on inputs with b_-2)
SUMMARY: 3/3 PASS (5 s, peak rss 76.3 MB)
# run-c45t-fix2.log
PASS  G3.9-y45-1_2-3-t: alpha'_v=1/2, gamma'=3, K=4, d=2: (c_-3 cb_-3 + z^2 c_-2 cb_-2)|0> x 150 targeted L<=2 columns: 0 non-zero pairings; e[R_33] non-zero on 61 of them (must be > 0: non-vacuous sample), e[R_44] on 61
PASS  BREAK-G3.9-y45-1_2-3-t-flip: with -z^2: 61 non-zero pairings (must be > 0)
PASS  BREAK-G3.9-y45-1_2-3-t-L3: (F.13) on 150 columns with a level-3 input: 93 non-zero (must be > 0)
PASS  G3.9-y45-1_5-2-t: alpha'_v=1/5, gamma'=2, K=4, d=2: (c_-3 cb_-3 + z^2 c_-2 cb_-2)|0> x 150 targeted L<=2 columns: 0 non-zero pairings; e[R_33] non-zero on 64 of them (must be > 0: non-vacuous sample), e[R_44] on 64
PASS  BREAK-G3.9-y45-1_5-2-t-flip: with -z^2: 64 non-zero pairings (must be > 0)
PASS  BREAK-G3.9-y45-1_5-2-t-L3: (F.13) on 150 columns with a level-3 input: 84 non-zero (must be > 0)
INFO  G3.9-y45-0-3-t: alpha'_v=0, gamma'=3, K=4, d=2: (c_-3 cb_-3 + z^2 c_-2 cb_-2)|0> x 150 targeted L<=2 columns: 0 non-zero pairings; with -z^2: 0; level-3 columns: 0 (logging line, not a check: both rows vanish separately here)
PASS  G3.9-alpha0-rows-vanish: alpha'_v=0, gamma'=3, K=4, d=2: non-zero pairings of e[R_33], e[R_44] with 150 targeted L<=2 columns: (0, 0); with 150 columns with a level-3 input: (0, 0) (all must be 0: R84 (4.3) at alpha'_v=0)
SUMMARY: 7/7 PASS (93 s, peak rss 123.1 MB)
# run-c44-fix2.log
PASS  G3.5-count: (F.7) at K=4, d=2: 22 + 22 vectors, rank 44, block projection ranks {'2,2': 6, '2,4': 22, '4,2': 22, '4,4': 38} (predicted (F.8) {'2,2': 6, '2,4': 22, '4,2': 22, '4,4': 38}); cut by truncation 0
PASS  G3.5-annihilate: fresh momentum (1445105185, 1847624051): L=2 image rank 2882/2927 after 2913 columns (138.0 s, peak rss 207.6 MB); 44 vectors x 2882 image vectors: 0 non-zero pairings
PASS  BREAK-G3.5-flip: c_-4 + z^2 c_-2 instead: 44 non-zero pairings (must be > 0)
PASS  G3.5-in-null: left-null space 45 vectors; rank of (null space + 44 vectors) 45 (= 45: the 44 lie in it); complement 1
PASS  G3.9-y45-in-null: rank of (left-null space + 44 vectors + (c_-3 cb_-3 + z^2 c_-2 cb_-2)|0>) 45 (must be 45 = dim of the left-null space 45: (F.13) annihilates the whole image)
PASS  BREAK-G3.9-y45-in-null-flip: same with c_-3 cb_-3 - z^2 c_-2 cb_-2: rank 46 (must be 46)
PASS  G3.8-proj-N4: rank of the left-null space projected on the blocks with N=4 or Nbar=4: 45 (must be 45: K=3, L=2 is onto, so no null vector lives on W_<=3)
PASS  G3.8-proj-Nb4: projected on Nbar=4 only: 42 (predicted 45 - 3: the 3 holomorphic vectors with chi at level 2 live on (4,2), (2,2))
PASS  G3.9-complement: null space modulo the 44: 1 vector(s); support per block {'3,3': 1, '4,4': 1}; rows by (block, chiral charges) {'(3,3) q=(0,0)': 1, '(4,4) q=(0,0)': 1}
PASS  G3.6-L3-pattern: level-3 inputs 566 (with b_-3: 22, with bt_-3: 22); non-zero pairings (22 hol, 22 antihol) x 80 columns per set: {'no_b3': (0, 0), 'hol_b3': (1082, 0), 'ah_b3': (0, 898)} (predicted (F.10): no_b3 (0, 0); hol_b3 (>0, 0); ah_b3 (0, >0))
SUMMARY: 10/10 PASS (168 s, peak rss 207.6 MB)
# run-c44s-fix2.log
PASS  G3.5-count: (F.7) at K=4, d=2: 22 + 22 vectors, rank 44, block projection ranks {'2,2': 6, '2,4': 22, '4,2': 22, '4,4': 38} (predicted (F.8) {'2,2': 6, '2,4': 22, '4,2': 22, '4,4': 38}); cut by truncation 0
PASS  G3.9-P3-saturated: third momentum (91777430, 203495592): K=4, L=2 rank 2882/2927 mod p, rank history [2882, 2882] (10302 columns, 443.3 s, peak rss 162.3 MB)
PASS  G3.5-annihilate: fresh momentum (91777430, 203495592): L=2 image rank 2882/2927 after 10302 columns (443.3 s, peak rss 208.0 MB); 44 vectors x 2882 image vectors: 0 non-zero pairings
PASS  BREAK-G3.5-flip: c_-4 + z^2 c_-2 instead: 44 non-zero pairings (must be > 0)
PASS  G3.5-in-null: left-null space 45 vectors; rank of (null space + 44 vectors) 45 (= 45: the 44 lie in it); complement 1
PASS  G3.9-y45-in-null: rank of (left-null space + 44 vectors + (c_-3 cb_-3 + z^2 c_-2 cb_-2)|0>) 45 (must be 45 = dim of the left-null space 45: (F.13) annihilates the whole image)
PASS  BREAK-G3.9-y45-in-null-flip: same with c_-3 cb_-3 - z^2 c_-2 cb_-2: rank 46 (must be 46)
PASS  G3.8-proj-N4: rank of the left-null space projected on the blocks with N=4 or Nbar=4: 45 (must be 45: K=3, L=2 is onto, so no null vector lives on W_<=3)
PASS  G3.8-proj-Nb4: projected on Nbar=4 only: 42 (predicted 45 - 3: the 3 holomorphic vectors with chi at level 2 live on (4,2), (2,2))
PASS  G3.9-complement: null space modulo the 44: 1 vector(s); support per block {'3,3': 1, '4,4': 1}; rows by (block, chiral charges) {'(3,3) q=(0,0)': 1, '(4,4) q=(0,0)': 1}
PASS  G3.6-L3-pattern: level-3 inputs 566 (with b_-3: 22, with bt_-3: 22); non-zero pairings (22 hol, 22 antihol) x 80 columns per set: {'no_b3': (0, 0), 'hol_b3': (1027, 0), 'ah_b3': (0, 1200)} (predicted (F.10): no_b3 (0, 0); hol_b3 (>0, 0); ah_b3 (0, >0))
SUMMARY: 11/11 PASS (474 s, peak rss 208.0 MB)
```

Fix-pass-2 tally: 31/31 PASS over the four changed parts (`k2l1` 3, `c45t` 7, `c44` 10, `c44s` 11), one INFO line, exit 0 each. New checks: `G3.9-y45-in-null` and `BREAK-G3.9-y45-in-null-flip` (twice), `G3.9-y45-*-t` with the non-vacuity count, `BREAK-G3.9-y45-*-t-flip`, `BREAK-G3.9-y45-*-t-L3`, `G3.9-alpha0-rows-vanish`; tightened: `G3.7-K2L1-rank`, `G3.7-K2L1-annihilate`, `G3.9-P3-saturated`. Logging lines: `G3.9-complement` (twice) and the INFO line. Each new or changed check fails on a named wrong result: a wrong sign or coefficient of $z^2$ in (F.13) (`G3.9-y45-in-null`: rank 46; `G3.9-y45-*-t`: 61, 64 non-zero, run A below); a vacuous sample (`G3.9-y45-*-t`, run B); rows that are not left-null at the vertex used (`G3.9-alpha0-rows-vanish`; at $\alpha'_{\rm v}=\tfrac12$ the same type of column gives $e[R_{33}]$ non-zero 61 times); a relation beyond the six of (F.9) at $K=2$, $L=1$ (`G3.7-K2L1-*`, run C); a deficit other than 45 at the third momentum (`G3.9-P3-saturated`).

*By-hand break legs* (`break_by_hand.py` in the fix-pass-2 scratch, imports the final script unchanged and perturbs one input per run; `run-break-by-hand.log`, wall 2:55, exit 1 as expected, 7/17 PASS):
- **A** — part `c45t` with the sign of $z^2$ in (F.13) flipped inside `y45_vector`: `G3.9-y45-1_2-3-t` **FAIL** (61 non-zero pairings), `G3.9-y45-1_5-2-t` **FAIL** (64); the `-flip` legs FAIL too (they now test the true relation: 0); `G3.9-alpha0-rows-vanish` still PASS (it does not use $y_{45}$). The main check fires on a wrong sign.
- **B** — the retired random sample of part `c45` (generator `20261093-c45`, the draws of `run-c45.log`) under the new conditions: `G3.9-y45-1_2-3` and `G3.9-y45-1_5-2` **FAIL** through the non-vacuity count ($e[R_{33}]$ non-zero on 0 of 150 columns), the defect the critic found in `c45`.
- **C** — part `k2l1` with the vertex at $\alpha'_{\rm v}=0$ (the printed label "alpha'_v=1/2" is hard-coded text; the vertex was replaced): rank 62/73, saturated, left-null space of dimension 11, containing the six rows of (F.9) ($11=6+5$, consistent with R84's five relations at $K=2$; the five not identified here); `G3.7-K2L1-rank` **FAIL** and `G3.7-K2L1-annihilate` **FAIL**, where the old conditions (`rank <= 67`; the 6 in the null space) would have passed.

**Falsifiability.**
- `G2-rank`, `G5-gamma` (and `G4-rank`) can fail: the same engine on the same rows at $\alpha'_{\rm v}=0$ has 96 (resp. 60) exact left-null vectors (`G6-annihilate-34`, `G5-gamma-alpha0`), and at $K=4$, $L=2$ the $\alpha'_{\rm v}=\tfrac12$ row itself is not onto (`G3.1`).
- `G6-annihilate-*` would fail for a wrong vertex datum $z^2$ in the relations: `BREAK-G6-flip-*` (268 and 26719 non-zero pairings).
- `G6-b-count-34` tests R84's formula at a new $d$: the formula was derived (087 §5), matched at $d=1,2,3$; $d=4$ tests the $d$-independence of the sector counts (critic #10). `G6-b-count-42` is a logging line (condition $>0$); 304 is a lower bound on the $b$-part at $K=4$ ($\chi$ level $\le5$, as 083's $K+1$ rule).
- `G5-gamma-alpha0` compares to R84's $\gamma'=3$ numbers (60, 427), not re-computed here; a $\gamma'$-dependence would change either.
- `G3-L3` can fail (it did not close with the $L=2$ inputs); `G3.2-P2` would fail for a momentum-dependent deficit.
- `G1-dim-*` compares the generating function to an independent Fock enumeration.
- `BREAK-antisym-*` would fail if the exchange symmetry of the vertex (078 C1) failed at the new levels or if the column were not built from both orderings.
- `G7-den-*`: all denominators are below $p$ (largest 7558272), so the reduction mod $p$ is the reduction of the rational data, which the lift (G7) needs.

**Not machine-checked.**
- The contour and pole arguments (F.2), (F.12) as such: their consequences (F.6), (F.10), (F.13) are checked on columns mod $p$ (F1); the generic value of the $K=4$, $L=2$ rank (2882) rests on them plus G7.
- Relations beyond (F.6) and (F.13) at higher $K$, $L$ (the general pole-structure count was not done); $L_{\min}(K)$ for $K\ge5$.
- The joint ($b+L$) relation count at $\alpha'_{\rm v}=0$ for $d=4$ and $K=4$ (only the $b$-alone part, $\ge304$ at $K=4$).
- The matter Neumann data at $d=4$ and mode 5 beyond exchange symmetry and the $d$-genericity of the code (critic #9): every break leg and every F1 check is matter-blind.
- $K=4$ at $d\ge3$ ($\dim W^{\rm even}_{\le4}=10926$ at $d=3$: out of the time and memory budget at this engine's rates); $K\ge5$.
- $d_{\rm eff}=5$ ($K=3$, $L=2$, 7945 rows): attempted, stopped for time after 1000 columns, no claim (row (iii), critic #12).
- `G6-not-onto-*` (not run: the break legs used 1000 columns, fewer than the rows).

## Self-review

1. *Objective.* Answered in both directions the brief names, with one qualification. Matter components: $d_{\rm eff}=4$ is onto at $K=3$, $L=2$ (3608/3608); $d_{\rm eff}=5$ was not reached (time, not memory). Output level: $K=4$ ($d_{\rm eff}=2$) is onto, but only once inputs of level 3 are admitted; with level $\le2$ the image saturates 45 short. This is not a PH31 falsifier (PH31 is about unbounded input level, and level 3 closes it), and it is not R84's mechanism (R84's relations survive every input level and need $\alpha'_{\rm v}=0$). It does sharpen how the falsifier must be read (fix pass): at input level $L$ the $c$-ghost pole structure forces exact relations once $K\ge2L$, so the falsifier must be run at $L\ge\lfloor K/2\rfloor+1$ or modulo these relations. PH31's support grows from "$K\le3$, $d\le3$, $L=2$" to "$K\le3$ at $d\le4$ with $L=2$, and $K=4$ at $d=2$ with $L=3$". The $\gamma'$-independence of R84's Scope now has a direct check at a point where the rank is not full (60 relations, 427/487 at $\gamma'=\tfrac32$).
2. *Weakest step.* (Revised in the fix pass.) The $K=4$, $L=2$ deficit is now explained: 45 exact relations, 44 from the conservation law (F.6) and one from the selection rule (F.13), each derived by a contour or pole argument on the $c$-ghost correlator and verified through its consequences: (F.6) on columns at three vertices ($\alpha'_{\rm v}=\tfrac12,\tfrac15,0$), in the measured left-null space, and through the level-3 violation pattern; (F.13) in the left-null space of the whole image at $\alpha'_{\rm v}=\tfrac12$ (two momenta, predicted ratio in the saturated null space) and on targeted columns at $\tfrac12$ and $\tfrac15$ (its $\alpha'_{\rm v}=0$ test is empty). The derivations themselves are not machine-checked as contour statements; what is checked are their consequences, with break legs. The weakest remaining step is the extrapolation: (F.9) gives only a lower bound $L_{\min}(K)\ge\lfloor K/2\rfloor+1$. The pole-structure view predicts further relations of the (F.13) type at higher $K$ and $L$ (simultaneous poles at one input need inputs whose ghost charges compensate, i.e. higher level), which were not enumerated; they could raise $L_{\min}(K)$ at $K\ge5$.
3. *Not checked, and why acceptable.*
   - Row (iii): the measured echelon cost made it a $\approx73$ min run. The brief makes it conditional on the budget of the run.
   - $K=4$ at $d\ge3$: 10926 rows, out of reach of this engine.
   - The joint ($b+L$) relation counts at $\alpha'_{\rm v}=0$ for $d=4$ and $K=4$: the break legs need only the $b$-part.
   - The $\alpha'_{\rm v}=0$ test of (F.13) (`c45t`) has no content: each row $R_{nn}=c_{-n}\bar c_{-n}|0\rangle$ is by itself a left-null vector there (R84 (4.3) on $\chi=c_{-n}\bar c_{-n}c_1|0\rangle$, F1(b')), which fix pass 2 checks as `G3.9-alpha0-rows-vanish`; (F.13) rests on $\alpha'_{\rm v}=\tfrac12$ (saturated null space, targeted columns) and $\tfrac15$ (targeted columns).
   - The $\alpha'_{\rm v}=0$ break legs use 1000 columns. They show the engine sees the exact relations, not the size of the $\alpha'_{\rm v}=0$ cokernel; R84 at $K=4$ or $d=4$ is a separate question.
4. *What a stronger physicist would ask.* (Revised in the fix pass.)
   - The minimal input level $L_{\min}(K)$. (F.9) gives $\lfloor K/2\rfloor+1$ as a lower bound, equal to the observed 2, 2, 3 at $K=2,3,4$ (at $d_{\rm eff}=2$ for $K=2,4$; at $K=3$ the value 2 combines the measured full rank at $L=2$ with (F.9) at $L=1$, where $K=3$ was not run); the guess "$L(K)\approx K-1$" of the first version is withdrawn (it disagrees from $K=5$ on). The next test is $K=5$ at $L=3$: no relation of type (F.6) exists there ($K<2L$), so a deficit would come from (F.13)-type selection rules or from something new. It needs a faster echelon (block elimination or a compiled routine), as row (iii) does.
   - Whether the whole cokernel at fixed $L$ is the pole structure of the $c$-ghost correlator. It is at $K=2$, $L=1$ (6 of 6) and at $K=4$, $L=2$ (45 of 45). If that holds generally, the finite-level evidence for PH31 becomes a statement with a mechanism: the cokernel at input level $L$ consists of the constraints imposed by the bounded pole orders of level-$L$ inputs, and these disappear at fixed $K$ once $L$ is large enough. That would be the natural route to PH31's finite-level shadow, in place of the triangularity guess.

## Fix pass (critic iteration 1)

Brief `agent/briefs/active-computator-093-fix-20261005T012100.md`; critique `agent/reports/critic-093-20261005T005700.md` (REVISE, light: 0 blocking, 1 major, 6 minor, 7 notes). New script parts (`k2l1`, `c44a`, `c44`, `c44s`, `c45`, `c45t`; `c45` retired in fix pass 2) write to `agent/scratch/computator/computator-093-fix-20261005T012100/`; the parts `dim`, `den`, `i`, `iv`, `ii`, `i0`, `ii0` are unchanged and were not re-run.

### F1 (finding #1): the $c$-ghost conservation law

#### F1(a) Derivation

The critic's mechanism, written out and tested below (F1(b)–(d)); the derivation is mine, the idea and the counts are the critic's.

\subsection*{Setup}
A1, A2 (078: mode conventions $c(u)=\sum_nc_nu^{-n+1}$, $\{b_m,c_n\}=\delta_{m+n,0}$; the vertex at any $\alpha'_{\rm v}$, $\gamma'$), A4, A6. Local coordinates (078 §1 *Maps*): output (special leg) $h_0(w)=1/w$; inputs $h_1=f_1$, $h_2=f_2=-f_1$, with
$$
f_1(w)=\frac{(\alpha'_{\rm v}+1)w+\gamma'}{2\beta\big((\alpha'_{\rm v}-1)w+\gamma'\big)},\qquad f_1(0)=\frac1{2\beta}=:z,\qquad f_2(0)=-z ,
\tag{F.0}
$$
for every $\alpha'_{\rm v}$, $\gamma'$. Matrix element (078 §1): $M_{B,{\rm col}}=\langle h_0\circ B(0)\,f_1\circ A_1(0)\,f_2\circ A_2(0)\rangle+(A_1\leftrightarrow A_2,\ \ell_1\leftrightarrow\ell_2)$, $B$ a Fock monomial of $\mathcal H^\downarrow$ on $c_1\bar c_1|0\rangle$ (ghost number 2), the plane-wave prefactor dropped (common to the two terms). "Level" of a state is its oscillator level above $c_1\bar c_1|0\rangle$; $q$, $\bar q$ are the chiral ghost charges relative to $c_1|0\rangle$, $\bar c_1|0\rangle$.

\subsection*{Derivation}
$$
\begin{aligned}
&c^{(u)}\big(h(w)\big)=h'(w)\,c^{(w)}(w)\qquad(\text{weight }-1\text{ primary}) \\
&\omega:=\phi(u)\,c(u)\,du=\phi_r(w)\,c^{(w)}(w)\,dw,\qquad \phi_r(w):=\phi\big(h_r(w)\big)\,h_r'(w)^2 \\
&\oint_0\frac{dw}{2\pi i}\,w^m\,c^{(w)}(w)=c_{m+2}\quad\Longrightarrow\quad \mathcal C_r[\phi]:=\oint_0\frac{dw}{2\pi i}\,\phi_r(w)\,c^{(w)}(w)=\sum_m\phi_{r,m}\,c^{(r)}_{m+2},\qquad \phi_r(w)=\sum_m\phi_{r,m}w^m
\end{aligned}\tag{F.1}
$$
For $\phi$ holomorphic on the $u$-sphere except at $u=\infty$ (the special puncture), $\omega$ inside the correlator is meromorphic with poles only at the three punctures, and the sum of its residues vanishes:
$$
\big\langle(\mathcal C_0[\phi]B)\otimes A_1\otimes A_2\big\rangle+(-1)^{|B|}\big\langle B\otimes(\mathcal C_1[\phi]A_1)\otimes A_2\big\rangle+(-1)^{|B|+|A_1|}\big\langle B\otimes A_1\otimes(\mathcal C_2[\phi]A_2)\big\rangle=0 .
\tag{F.2}
$$
Take $\phi(u)=u^2-z^2$. At the output, $h_0'(w)=-w^{-2}$:
$$
\phi_0(w)=\big(w^{-2}-z^2\big)\,w^{-4}=w^{-6}-z^2w^{-4}\quad\Longrightarrow\quad\mathcal C_0[\phi]=c_{-4}-z^2c_{-2}.
\tag{F.3}
$$
At an input, by (F.0):
$$
\begin{aligned}
\phi_r(w)&=\big(h_r(w)-z\big)\big(h_r(w)+z\big)\,h_r'(w)^2=\sum_{m\ge1}\phi_{r,m}w^m,\qquad \phi_{1,1}=2z\,f_1'(0)^3\neq0,\quad \phi_2=\phi_1, \\
\mathcal C_r[\phi]&=\phi_{r,1}\,c_3+\phi_{r,2}\,c_4+\phi_{r,3}\,c_5+\cdots
\end{aligned}\tag{F.4}
$$
For $n\ge2$: $c_n|0\rangle=0$, and $c_n$ anticommutes with $c_k$ (all $k$), with $\bar b_k,\bar c_k$, with $b_k$ for $k\ne-n$, and commutes with the matter; $\{c_n,b_{-n}\}=1$. An input $A\in\ker b_0^-$ of holomorphic level $N$ is a sum of strings of creation modes, $c_0$, $\bar c_0$, $c_1$, $\bar c_1$ on $|0\rangle$, and contains $b_{-n}$ only if $N\ge n$. Hence
$$
c_nA=0\quad\text{for }n\ge\max(2,N+1),\qquad\text{so}\quad\mathcal C_r[u^2-z^2]\,A=0\ \text{ for }N(A)\le2 .
\tag{F.5}
$$
With (F.2)–(F.5), for every $B$ and all inputs of holomorphic level $\le2$, in both orderings:
$$
\boxed{\;\big\langle\mathcal V_3'\big|\,\big(c_{-4}-z^2c_{-2}\big)B\otimes A_1\otimes A_2\big\rangle=0,\qquad \big\langle\mathcal V_3'\big|\,\big(\bar c_{-4}-z^2\bar c_{-2}\big)B\otimes A_1\otimes A_2\big\rangle=0\ \ (\bar N(A_i)\le2)\;}
\tag{F.6}
$$
the second from $\bar\phi(\bar u)=\bar u^2-z^2$ ($z$ real). Within the projected matrix, $y_B:=(c_{-4}-z^2c_{-2})B$ expanded on the rows is a left-null vector iff its support lies in the row set: $N(B)+4\le K$, $\bar N(B)\le K$, $N(B)-\bar N(B)$ even (a $y_B$ on odd rows only is not a relation of the even block), and $B\in\mathcal H^\downarrow$ at ghost number 1, i.e. $q+\bar q=-1$ ($c_{-4}$, $c_{-2}$ do not touch the zero modes, so $y_B\in\mathcal H^\downarrow$). At $K=4$: $N(B)=0$, so $B=c_1|0\rangle\otimes\bar\chi$ ($q=0$, no holomorphic matter) with $\bar\chi$ of level $\bar n\in\{0,2,4\}$ and $\bar q=-1$. In the engine's basis (holomorphic modes to the left of antiholomorphic ones, then $c_1\bar c_1|0\rangle$) $c_{-4}B$ and $c_{-2}B$ are single monomials with sign $+1$, and the conjugate vectors are single monomials with the common sign $(-1)^{|g|}$ ($g$ the holomorphic ghost string of $B$), irrelevant for a null vector:
$$
y^{\rm hol}_{\bar\chi}=e\big[c_{-4}\,|\,\bar\chi\big]-z^2\,e\big[c_{-2}\,|\,\bar\chi\big],\qquad y^{\rm ah}_{\chi}=e\big[\chi\,|\,\bar c_{-4}\big]-z^2\,e\big[\chi\,|\,\bar c_{-2}\big].
\tag{F.7}
$$
Counting with the chiral numbers $a_d(n,q)$ (states of one chirality at level $n$ and charge $q$): $a_2(0,-1)=0$, $a_2(2,-1)=3$ ($b_{-2}$, $b_{-1}\alpha^\mu_{-1}$), $a_2(4,-1)=19$:
$$
\#\{y^{\rm hol}\}=\#\{y^{\rm ah}\}=0+3+19=22,\qquad 44\text{ in all};\qquad
\text{block projections: }(4,4)\ 38,\ (2,4)\ 22,\ (4,2)\ 22,\ (2,2)\ 6,\ \text{others }0 .
\tag{F.8}
$$
They are independent: distinct $\bar\chi$ put their $c_{-4}$ components on distinct rows, and $y^{\rm hol}$ ($q=1$, $\bar q=-1$) and $y^{\rm ah}$ ($q=-1$, $\bar q=1$) have disjoint supports. At $(2,4)$: $19$ from $c_{-2}B$ with $\bar n=4$ plus $3$ from $\bar c_{-4}$ on $\chi$ of level 2.

General $(K,L)$. Inputs of level $\le L$ are annihilated by $c_n$, $n\ge L+1$ (F.5), so $\phi_r$ must vanish to order $L-1$ at $w=0$ in both input frames: $\phi=(u^2-z^2)^{L-1}g(u)$, $g$ a polynomial (a pole of $\phi$ at $\pm z$ would put creation modes on the inputs). A monomial $u^j$ of $\phi$ gives $w^{-j-4}$ in the output frame, i.e. $c_{-j-2}$; the top mode of the lowest choice $g=1$ is $c_{-2L}$, and $\deg g=k$ gives $c_{-2L-k}$. The vector $y_B$ fits in the truncation iff $N(B)+2L+k\le K$. With $N(B)=0$, $\bar n=2$ ($a_d(2,-1)=d+1>0$) and $g=1$:
$$
\text{relations of type (F.6) at input level }L\text{ exist iff }K\ge2L,\qquad\text{so}\qquad L_{\min}(K)\ \ge\ \Big\lfloor\frac K2\Big\rfloor+1 ,
\tag{F.9}
$$
a lower bound on the minimal closing level ($L_{\min}=2,2,3$ observed at $K=2,3,4$ (at $d_{\rm eff}=2$ for $K=2,4$; at $K=3$ the value 2 combines the measured full rank at $L=2$ with (F.9) at $L=1$, where $K=3$ was not run); other obstructions could raise it). At $L=1$ the condition is empty ($\phi=1$ allowed: $\phi_r=h_r'^2$ gives $c_2,c_3,\dots$ at the inputs, which kill level $\le1$): at $K=2$, $\phi=1$ gives $\mathcal C_0=c_{-2}$, and the relations are the single rows $e[c_{-2}\,|\,\bar\chi_2]$, $e[\chi_2\,|\,\bar c_{-2}]$, $\bar\chi_2,\chi_2$ at level 2 and charge $-1$: $3+3=6$ rows of the $(2,2)$ block that vanish on the whole $L=1$ image, rank $\le73-6=67$.

*The "only if" half of (F.9) for combinations* (fix pass 2, critic iteration 2 #1). The level count above treats a single $y_B=\mathcal C_0[\phi]B$; a combination $y=\sum_i\mathcal C_0[\phi_i]B_i$ could a priori cancel its high components. It cannot. The allowed $\phi$ are $(u^2-z^2)^{L-1}g(u)$, so the span of the output operators $\mathcal C_0[\phi]$ is spanned by
$$
e_j:=\mathcal C_0\big[u^{j-2L}(u^2-z^2)^{L-1}\big]=c_{-j}+\big(\text{combination of }c_{-j+2},\dots,c_{-j+2L-2}\big),\qquad j\ge2L
$$
(the top monomial $u^{j-2}$ gives $c_{-j}$, the lowest $u^{j-2L}$ gives $c_{-(j-2L+2)}$, all creation modes since $j-2L+2\ge2$; the critic's text writes the prefactor $u^{j-2}$, whose top mode is $c_{-(j+2L-2)}$, so the exponent is corrected here to $j-2L$). Change basis of the holomorphic fermionic creation modes from $\{c_{-n}\}_{n\ge2}$ to $\{c_{-2},\dots,c_{-(2L-1)}\}\cup\{e_j\}_{j\ge2L}$: the change is triangular with unit diagonal, hence invertible, and the monomials in the new modes (times the other oscillators and zero modes) form a basis. Every $y$ of type (F.6) is a combination of new monomials containing at least one $e_j$, $j\ge2L$. Replacing each $e_j$ by its leading term $c_{-j}$ maps distinct new monomials to distinct old ones and keeps the level, while the lower terms of $e_j$ lower the level by at least 2. So the component of a non-zero $y$ at its top level is the image of its top-level new monomials, which is non-zero and consists of old monomials containing some $c_{-j}$, $j\ge2L$: its holomorphic level is $\ge2L$. Hence $y$ fits in the rows only if $K\ge2L$, for combinations as well as for a single $y_B$. The lower bound $L_{\min}(K)\ge\lfloor K/2\rfloor+1$ uses only the "if" half; the "only if" half carries the closure remark below ($K=4$, $L=3$) and the R84 Scope text of §5.

Closure at $L=3$, $K=4$. With level-3 inputs $\phi=u^2-z^2$ leaves $\phi_{r,1}c_3$ at the inputs ($c_4$, $c_5$ kill level $\le3$), and $c_3A\ne0$ only if $A$ contains $b_{-3}$; so
$$
y^{\rm hol}_{\bar\chi}\cdot{\rm col}(A_1,A_2)=-(-1)^{|B|}\phi_{1,1}\Big[\big\langle B\otimes c_3A_1\otimes A_2\big\rangle+(-1)^{|A_1|}\big\langle B\otimes A_1\otimes c_3A_2\big\rangle\Big]+(\text{exchanged order}),
\tag{F.10}
$$
which vanishes unless $A_1$ or $A_2$ contains $b_{-3}$ (resp. $\bar b_{-3}$ for $y^{\rm ah}$). A double zero, $\phi=(u^2-z^2)^2g$, has top mode $c_{-6}$: no relation of type (F.6) survives at $K=4$, $L=3$, consistent with 2927/2927 (G3.4).

\subsection*{Commentary}
(F.1): transformation of a weight $-1$ primary; $\phi\,c$ has weight $2-1=1$, a 1-form, in every frame. (F.2): residue theorem on the sphere for a meromorphic 1-form — the $c$-ghost analogue of the conservation laws of a vertex used in 078 §4 (Rastelli–Zwiebach, *Tachyon potentials, star products and universality*, JHEP 09 (2001) 038, arXiv:hep-th/0006240, §3; arXiv number confirmed against `paper/string_theory.bib`, key `Rastelli:2001:TachyonPotentialsStar`; the section number is 078's and the critic's, to be checked against the paper); each local contour encircles its puncture counterclockwise (holomorphic coordinate maps preserve orientation), and the Koszul signs come from moving the odd contour operator past the earlier insertions. The 3-punctured sphere has no moduli, so no $b$-insertions interfere; the matter is a spectator, so (F.6) holds at every momentum. (F.3): $u=1/w$, $du^2=w^{-4}dw^2$. (F.4): $\phi$ even and $f_2=-f_1$ give $\phi_2=\phi_1$; $\phi_{1,1}\ne0$ because $f_1'(0)\neq0$. Only $h_r(0)=\pm z$ is used — no higher jet of the frames — hence the validity at every $\alpha'_{\rm v}$, $\gamma'$, unlike R84's CKV identity, which needs the frames to be exact dilations ($\alpha'_{\rm v}=0$). (F.5): a $b_{-n}$ in a monomial raises the level by $n$; the $b_{-1}$ that 078's engine removes by $b_{-1}c_1|0\rangle=|0\rangle$ is irrelevant since $n\ge2$. (F.7): sign conventions of `closed_basis`/`state_strings` (078: holomorphic ghost string, antiholomorphic ghost string, then $c_1\bar c_1$). (F.8): the counts are those of the generating function of 078 §1 (computed in part `c44`). (F.9): an upper bound on what this mechanism produces would need all $\phi$; for the existence statement $g=1$ suffices. Why the $c$ ghost and not $b$, $T$ or $j$: conservation laws with $b$ (vector fields, input modes $b_{k-1}$), $T$ (input modes $L_{k-1}$) or $j=i\partial X$ (input modes $\alpha_k$) need zeros of order $L+2$, $L+2$, $L+1$ at $\pm z$ and give output levels $\ge2L+3$, $2L+3$, $2L+2$; the weight $-1$ of $c$ makes its quadratic differentials the cheapest, with output level $2L$.

\subsection*{Result}
For R2's $\mathcal V_3'$ at every $\alpha'_{\rm v}$, $\gamma'$, $P$: the vectors (F.7) — 22 holomorphic and 22 antiholomorphic at $K=4$, $d_{\rm eff}=2$ — are exact left-null vectors of the level-projected circle map restricted to inputs of level $\le2$, with the block projections (F.8). At input level $L$ such relations exist iff $K\ge2L$, so $L_{\min}(K)\ge\lfloor K/2\rfloor+1$ (F.9). They are violated at $L=3$ exactly by columns with an input containing $b_{-3}$ or $\bar b_{-3}$ (F.10). At $K=2$, $L=1$: 6 identically vanishing rows of the $(2,2)$ block.

\subsection*{Verification}
Machine checks in F1(b)–(d) (parts `c44`, `k2l1`, `c44a` of `codes/verify-ph31-rank-half.py`). Not machine-checked: (F.2) as a contour statement (tested through its consequence (F.6) on columns). That no further relation exists at $K=4$, $L=2$ is not argued from the Commentary's level count (which covers $b$, $T$, $j$ and $c$ with polynomial $\phi$ only) but measured: the left-null space is exactly the 44 plus (F.13) (F1(b')).

#### F1(b) The 44 vectors at $K=4$, $L=2$

The vectors (F.7) are built by `c_vectors` from the chiral basis of 078 (`chiral_states`), with $z^2$ read from the vertex ($z=f_1(0)$, asserted $=1/(2\beta)=\tfrac13$). Break leg throughout: $c_{-4}+z^2c_{-2}$ (sign of $z^2$ flipped).

- **Part `c44a`** (`run-c44a.log`, wall 54 s, **peak 108.2 MB**): the 44 vectors against 150 random $L\le2$ columns at two other vertices, fresh momenta: $\alpha'_{\rm v}=\tfrac15$, $\gamma'=2$: 0 non-zero pairings (`G3.5-alpha-1_5-2` PASS), flipped 844 (`BREAK-G3.5-alpha-flip-1_5-2` PASS); $\alpha'_{\rm v}=0$, $\gamma'=3$: 0 (`G3.5-alpha-0-3` PASS), flipped 496 (`BREAK-G3.5-alpha-flip-0-3` PASS). The law does not depend on the frames' higher jets, as derived (only $h_r(0)=\pm z$ enters).
- **Part `c44`** (`run-c44.log`, wall 2:58, **peak 211.7 MB**), $\alpha'_{\rm v}=\tfrac12$, $\gamma'=3$, fresh momentum $P=(1445105185, 1847624051)$:
  - `G3.5-count` PASS: 22 + 22 vectors, rank 44, none cut by the truncation; block projection ranks $(4,4)$ 38, $(2,4)$ 22, $(4,2)$ 22, $(2,2)$ 6 — the prediction (F.8).
  - The $L=2$ image, scanned to rank 2882 (2913 pairs of one $\Delta$, 146 s; the scan stops at 2882, so this image is not tested for saturation here — see part `c44s`). The 44 vectors pair to zero with all 2882 image vectors (`G3.5-annihilate` PASS); flipped: 44 non-zero pairings (`BREAK-G3.5-flip` PASS).
  - Left-null space of that image: 45 vectors; rank of (null space + 44 vectors) = 45, so the 44 lie in it (`G3.5-in-null` PASS); complement 1.
  - Level-3 columns (F.10), same $P$, fresh $\Delta$, 80 pairs per set (one level-3 input and one input of level $\le3$ without $b_{-3}$, $\bar b_{-3}$): of the 566 level-3 inputs, 22 contain $b_{-3}$ and 22 contain $\bar b_{-3}$ (the critic's count). Non-zero pairings (22 holomorphic, 22 antiholomorphic vectors): no $b_{-3}$ anywhere: $(0,0)$; level-3 input with $b_{-3}$: $(1082,0)$; with $\bar b_{-3}$: $(0,898)$ — **exactly the pattern (F.10)** (`G3.6-L3-pattern` PASS). The violation at $L=3$ comes only from the $c_3$ term at the inputs, chirality by chirality.
  - The complement (null space modulo the span of the 44, reduced on the 44's echelon): support on exactly **two rows**, one in $(3,3)$, $b_{-1}c_{-2}\bar b_{-1}\bar c_{-2}\,c_1\bar c_1|0\rangle=\pm c_{-2}\bar c_{-2}|0\rangle$, and one in $(4,4)$, both with chiral charges $(q,\bar q)=(0,0)$ (`G3.9-complement`, logging line). Its explicit form is in part `c44s`.

**Reading.** The critic's mechanism holds: the 44 vectors are exact left-null vectors at every vertex tested ($\alpha'_{\rm v}=\tfrac12,\tfrac15,0$), they lie in the measured left-null space and account for its block projections except one unit of $(4,4)$ and the unit of $(3,3)$, and their violation at $L=3$ follows (F.10) to the chirality. The generic rank at $K=4$, $L=2$ is therefore $\le2927-44=2883$, and with G7 $\ge2882$; with the 45th relation (F1(b')) it is exactly 2882.

#### F1(b') The 45th relation: derivation and test

Part `c44` located the complement of the 44 on two rows with $(q,\bar q)=(0,0)$: $R_{33}=b_{-1}c_{-2}\bar b_{-1}\bar c_{-2}\,c_1\bar c_1|0\rangle$ and one row of $(4,4)$. Since $b_{-1}c_1|0\rangle=|0\rangle$ in each chirality, $R_{33}=c_{-2}\bar c_{-2}|0\rangle$ (sign $+1$: the two odd strings $b_{-1}c_{-2}c_1$ and $\bar b_{-1}\bar c_{-2}\bar c_1$ each give $-c_{-n}|0\rangle$). This suggests the $(4,4)$ row $R_{44}=c_{-3}\bar c_{-3}|0\rangle$ and a two-chirality version of the argument of F1(a), derived here before reading its explicit form off part `c44s`.

\subsection*{Setup}
As F1(a). $G(u,\bar u):=\big\langle c(u)\,\bar c(\bar u)\,f_1\circ A_1(0)\,f_2\circ A_2(0)\big\rangle$ on the $u$-plane, vacuum at $u=\infty$; $A_1$, $A_2$ inputs of level $\le2$ (ghost number 2, $\ker b_0^-$).

\subsection*{Derivation}
For the output rows $c_{-n}\bar c_{-m}|0\rangle$, $h_0\circ c(w)=(h_0'(w))^{-1}c(1/w)=-w^2c(1/w)$ gives
$$
M_{c_{-n}\bar c_{-m}|0\rangle,\,(A_1,A_2)}=\big[w^{n+1}\bar w^{m+1}\big]\,F(w,\bar w),\qquad F(w,\bar w):=w^2\bar w^2\,G(1/w,1/\bar w).
\tag{F.11}
$$
As a function of $u$, $G$ is meromorphic with poles only at $\pm z$, grows at most like $u^2$ at $u=\infty$ ($\langle0|c(u)=\langle0|(c_{-1}u^2+c_0u+c_1+O(u^{-1}))$), and its pole at $u=\pm z$ has order $\le1$: in the input frame the singular part of $c(w)A(0)$ is $\sum_{n\ge2}c_nA\,w^{1-n}$, and $c_nA=0$ for $n\ge3$ (F.5). The same holds in $\bar u$. Hence
$$
G=\frac{\mathsf A}{(u-z)(\bar u-z)}+\frac{\mathsf B}{(u-z)(\bar u+z)}+\frac{\mathsf C}{(u+z)(\bar u-z)}+\frac{\mathsf D}{(u+z)(\bar u+z)}+\big(\text{terms polynomial in }u\text{ or in }\bar u\big),
$$
$$
t_{k,l}:=\big[w^{3+k}\bar w^{3+l}\big]F=z^{k+l}\Big(\mathsf A+(-1)^l\mathsf B+(-1)^k\mathsf C+(-1)^{k+l}\mathsf D\Big),\qquad k,l\ge0,
\tag{F.12}
$$
using $w^2/(1/w\mp z)=\sum_k(\pm z)^kw^{3+k}$; the polynomial terms reach only $w^{0,1,2}$ or $\bar w^{0,1,2}$. $\mathsf A$ is the double residue at $u=\bar u=z$, proportional to $\langle(c_2\bar c_2A_1)\,A_2\rangle$; it is non-zero only if $A_1$ contains $b_{-2}$ and $\bar b_{-2}$. At level $\le2$ that forces $A_1\propto b_{-2}\bar b_{-2}c_1\bar c_1|0\rangle$ (up to $c_0^+$), with $q+\bar q=-2$, while $\mathcal H_0$ at ghost number 2 has $q+\bar q\in\{0,-1\}$ ($\mathcal H^\downarrow$, resp. $c_0^+\mathcal H^\downarrow$). So $\mathsf A=0$, and likewise $\mathsf D=0$ ($A_2$). Then $t_{1,1}=-z^2(\mathsf B+\mathsf C)=-z^2t_{0,0}$, for each ordering of the inputs separately:
$$
\boxed{\;\big\langle\mathcal V_3'\big|\,\big(c_{-3}\bar c_{-3}+z^2c_{-2}\bar c_{-2}\big)|0\rangle\otimes A_1\otimes A_2\big\rangle=0\qquad(\text{inputs of level}\le2)\;}
\tag{F.13}
$$
i.e. $y_{45}=e[R_{44}]+z^2e[R_{33}]$, normalised to $R_{33}$: $\{R_{33}:1,\ R_{44}:1/z^2=9\}$. It holds at every $\alpha'_{\rm v}$, $\gamma'$, $P$ (only $h_r(0)=\pm z$ and the matter as a spectator). It fails at $L=3$: $c_3A\ne0$ for $A\ni b_{-3}$ adds double poles to $G$, and an input such as $b_{-2}c_{-1}\otimes\bar b_{-2}\bar c_{-1}$ (level $(3,3)$, $q=\bar q=0$) makes $\mathsf A\ne0$.

\subsection*{Commentary}
(F.11): the row $c_{-n}\bar c_{-m}|0\rangle$ is the coefficient of $w^{n+1}\bar w^{m+1}$ in $c(w)\bar c(\bar w)|0\rangle$, and $c$ is primary of weight $-1$. (F.12): $G$ is a function of $(u,\bar u)$ that is meromorphic in each variable separately (the inputs are finite sums of products of holomorphic and antiholomorphic states); the four double-pole coefficients are double residues. The same structure reproduces the holomorphic law: at fixed $\bar u$-structure, $t_{k+2,l}=z^2t_{k,l}$ is (F.6) on $B=\bar c$-part (rows outside $K=4$ here). (F.13) is new: it uses the ghost-number selection rule on a single input, $\mathsf A=\mathsf D=0$, and needs both chiralities; it is why the 45th vector ties $(4,4)$ to $(3,3)$. Odd-row analogue: $t_{1,0}=-t_{0,1}$, on the rows $(4,3)$, $(3,4)$, which are not in $W^{\rm even}$. The 44 and the 45th are both pole-structure statements on the $c$-ghost correlator of level-$\le2$ inputs: simple poles at $\pm z$, and no simultaneous holomorphic and antiholomorphic pole at the same input.

\subsection*{Result}
(F.13) is an exact left-null vector of the $K=4$ projected map on inputs of level $\le2$, at every $\alpha'_{\rm v}$, $\gamma'$, $P$, independent of the 44 (support on $(q,\bar q)=(0,0)$ rows). With F1(b): the generic rank at $K=4$, $L=2$, $d_{\rm eff}=2$ is $\le2927-45=2882$, and with G7 $\ge2882$: **the generic deficit is exactly 45**, all of it explained by the $c$-ghost pole structure.

\subsection*{Verification}
Part `c44s` (saturated image at a third momentum): the explicit normalised complement vector against the prediction $\{R_{33}:1,R_{44}:9\}$. Part `c45`: $y_{45}$ on random $L\le2$ columns at $\alpha'_{\rm v}=\tfrac12,\tfrac15,0$ (must vanish), with $-z^2$ (must not), and on columns with a level-3 input (must not vanish somewhere); vacuous sample, replaced by part `c45t` and retired in fix pass 2. Fix pass 2 adds `G3.9-y45-in-null` (parts `c44`, `c44s`: $y_{45}$ in the left-null space of the whole image, its flip not). Results below and in the Verification block.

Results.
- **Part `c44s`** (`run-c44s.log`, wall 7:58, **peak 212.3 MB**), $\alpha'_{\rm v}=\tfrac12$, $\gamma'=3$, third momentum $P_3=(91777430, 203495592)$, scanned to saturation (rank history $[2882,2882]$, 10302 columns, `G3.9-P3-saturated` PASS). Modulo the 44, the left-null space of the saturated image is spanned by one vector, normalised on its first entry: $\{R_{33}=b_{-1}c_{-2}\bar b_{-1}\bar c_{-2}\,c_1\bar c_1|0\rangle:\ 1,\ \ R_{44}=b_{-1}c_{-3}\bar b_{-1}\bar c_{-3}\,c_1\bar c_1|0\rangle:\ 9\}$ — **the prediction (F.13) exactly, including the ratio $1/z^2=9$** (logged by `G3.9-complement` and the explicit print; the prediction was written before the print was read). The same run repeats all of part `c44`'s checks on the saturated image: `G3.5-count`, `G3.5-annihilate` (0 non-zero pairings with 2882 image vectors), `BREAK-G3.5-flip` (44), `G3.5-in-null`, `G3.8-proj-N4` (45), `G3.8-proj-Nb4` (42), `G3.6-L3-pattern` (`no_b3` (0, 0), `hol_b3` (1027, 0), `ah_b3` (0, 1200)): 9/9 PASS.
- **Part `c45`** (`run-c45.log`, wall 1:32, **peak 117.7 MB**; superseded by `c45t` and retired in fix pass 2), first attempt, $y_{45}$ on 150 random $L\le2$ columns at $\alpha'_{\rm v}=\tfrac12,\tfrac15,0$: 0 non-zero pairings at each (PASS), but the break legs **FAIL**: the flipped vector ($-z^2$) also gives 0, and level-3 columns give 1, 4, 0. Diagnosis: a vacuous sample, not a wrong relation. The rows $R_{33}$, $R_{44}$ are non-zero only on columns with $b_{-2}$ in one input and $\bar b_{-2}$ in the other ($\mathsf B$, $\mathsf C$ of (F.12)); 9 of the 101 inputs contain $b_{-2}$ and 9 contain $\bar b_{-2}$, so random pairs rarely hit them (about one column in 150 with $t_{0,0}\ne0$: a hit has probability $2\cdot81/101^2\approx1.6\,\%$, about 2.4 hit columns per 150, about 40 % of them with $t_{0,0}\ne0$; none at both vertices has probability $\approx e^{-2}\approx0.14$, critic iteration 2 #4), and both rows vanish on the sample. The three PASS lines of `c45` have no content for the same reason.
- **Part `c45t`** (`run-c45t.log`, wall 1:34, **peak 119.8 MB**), targeted: $L\le2$ pairs (input with $b_{-2}$, input with $\bar b_{-2}$); level-3 pairs with an input containing both $b_{-2}$ and $\bar b_{-2}$ (5 such inputs; $\mathsf A\ne0$ possible) or $b_{-3}$ (double pole). $\alpha'_{\rm v}=\tfrac12$: $y_{45}$ 0 non-zero pairings on 150 columns (`G3.9-y45-1_2-3-t` PASS), flipped 61, level-3 93 (`BREAK-G3.9-y45-1_2-3-t` PASS). $\alpha'_{\rm v}=\tfrac15$, $\gamma'=2$: 0; flipped 64, level-3 84 (PASS, PASS). $\alpha'_{\rm v}=0$: 0, but flipped 0 and level-3 0 (`BREAK-G3.9-y45-0-3-t` **FAIL**): at $\alpha'_{\rm v}=0$ the two rows vanish separately on these columns, so the $\alpha'_{\rm v}=0$ line tests nothing. The reason is R84's identity (4.3) (critic iteration 2 #3, hand argument): for $\chi=c_{-n}\bar c_{-n}c_1|0\rangle$ (ghost number 3, in $\mathcal H^\downarrow$) the row functional of $O_b$ is $[(b_{-1}-z^2b_1)-{\rm c.c.}]\chi$ (078 §4), and $b_{-1}\chi=+c_{-n}\bar c_{-n}|0\rangle$ while $b_1\chi=\bar b_{\pm1}\chi=0$; so at $\alpha'_{\rm v}=0$ each row $R_{nn}=c_{-n}\bar c_{-n}|0\rangle$ is by itself a left-null vector, for inputs of every level, and $y_{45}$, its flip and the level-3 leg all vanish there. Fix pass 2 replaces the FAIL leg by the check of this prediction, `G3.9-alpha0-rows-vanish` (the two rows separately on the targeted and the level-3 columns), and prints the $y_{45}$ line at $\alpha'_{\rm v}=0$ as INFO. The evidence for (F.13) is therefore: the exact ratio 9 in the saturated null space at $\alpha'_{\rm v}=\tfrac12$, and the targeted columns at $\alpha'_{\rm v}=\tfrac12$ and $\tfrac15$ with working break legs.

#### F1(c) $K=2$, $L=1$

Part `k2l1` (`run-k2l1.log`, wall 5 s, **peak 75.9 MB**): $\alpha'_{\rm v}=\tfrac12$, $\gamma'=3$, $K=2$, $L=1$, $d=2$, 11 inputs, 66 unordered pairs per $\Delta$, fresh momentum. Prediction (F.9) at $L=1$: the 6 rows $e[c_{-2}\,|\,\bar\chi_2]$, $e[\chi_2\,|\,\bar c_{-2}]$ of the $(2,2)$ block vanish on the image, rank $\le67$; 73/73 would refute the mechanism.

- Rank history $[56,67,67]$ over three $\Delta$ samples: **rank 67/73, saturated** (`G3.7-K2L1-rank` PASS). Per block: every block onto except $(2,2)$, 48/54.
- The 6 vectors (built by `c_vectors`, none cut by the truncation) all lie in $(2,2)$, pair to zero with the whole image, and span its left-null space (6 vectors): **the deficit at $K=2$, $L=1$ is exactly the $\phi=1$ law** (`G3.7-K2L1-annihilate` PASS).
- Break leg: the same 6 vectors on 100 random $L=2$ columns give 92 non-zero pairings ($c_2$ acts on inputs with $b_{-2}$; `BREAK-G3.7-L2` PASS). So the check can fail, and the relations are level-limited as derived.

The prediction was a specific number (67) made before the run; it came out exactly, with the left-null space identified completely.

#### F1(d) Projection of the left-null space on the blocks with $N=4$ or $\bar N=4$

Critic #4's test. Since $K=3$, $L=2$ is onto (R84), no left-null vector of the $K=4$ image can be supported on $W^{\rm even}_{\le3}$, so the projection on the blocks with $N=4$ or $\bar N=4$ must be injective on the null space. Part `c44` (null space of the image at rank 2882, fresh momentum): rank 45 (`G3.8-proj-N4` PASS). The second, predicted, projection — on the blocks with $\bar N=4$ only — must lose exactly the 3 holomorphic vectors with $\bar\chi$ at level 2 (supported on $(4,2)$, $(2,2)$) if the rest of the null space is as found: rank 42 (`G3.8-proj-Nb4` PASS); this shows that the rank function can return less than 45 on this null space. Re-run on the saturated image at a third momentum in part `c44s`: 45 and 42 again (PASS, PASS). With F1(b'), the null space is $\mathrm{span}(44)\oplus\langle y_{45}\rangle$, and the projection on $\bar N=4$ loses exactly the 3 holomorphic vectors with $\bar\chi$ at level 2 ($y_{45}$ has its $(4,4)$ component).

#### F1(e) Rewrites

Outcome: **the critic's mechanism holds, and the 45th relation is identified.** The 44 vectors are exact left-null vectors (F1(b)), the $K=2$, $L=1$ prediction (67/73) is met exactly (F1(c)), the projection test passes (F1(d)), and the 45th relation is the two-chirality selection rule (F.13), found from its support and confirmed with its predicted coefficient (F1(b')). The generic deficit at $K=4$, $L=2$, $d_{\rm eff}=2$ is exactly 45. Rewritten accordingly:
- §4, "The $K=4$, $L=2$ deficit": the three facts (now at three momenta), the mechanism ((F.6), (F.13)), the checks, why it is not R84's type, the closing level $L_{\min}(K)\ge\lfloor K/2\rfloor+1$, and the counting argument demoted to a remark with its premise and onset (#2).
- G3.3 (and G0, G3, G3.9, G7): see the claim tree and *Changed nodes and dependents*.
- Self-review 1 (falsifier reading), 2 (weakest step: the derivations are checked through their consequences; the extrapolation (F.9) is a lower bound only), 3 (the non-informative $\alpha'_{\rm v}=0$ test of (F.13)), 4 (the guess $L(K)\approx K-1$ withdrawn; the pole-structure question as the next test).
- §5: the PH31 verification line and the falsifier addition (critic #5's wording, extended by (F.13) and by the remark that closure at every $K$ is necessary, not sufficient); the R84 lines.

Where the critic's account differed: the 45th relation is not "unexplained" but of the same origin, the pole structure of the $c$-ghost correlator at bounded input level; the critic's lower bound "$[44,45]$" becomes exactly 45. The prediction "$K=4$, $L=2$, $d=3$: deficit $\ge80$" follows from (F.6) alone ($2[a_3(2,-1)+a_3(4,-1)]=2(4+36)$, critic's counts, not recomputed here), with (F.13) adding at least one more ($R_{33}$, $R_{44}$ carry no matter); not run ($K=4$ at $d=3$ is out of this engine's reach, *Not machine-checked*).

### Minor findings and notes

- **#2 [minor] applied.** The $\Delta$-degree counting argument is kept as a remark (§4, rewritten), with its premise and its onset. Premise: the columns are polynomials in $\Delta$ only after the plane-wave prefactor is dropped; that factor is a common non-zero scalar of the two orderings of a column because $|\rho_1|=|\rho_2|$ ($h_2=-h_1$, 078 §1), so dropping it does not change the span. Onset at $d_{\rm eff}=2$, $L=2$: the Taylor span has at most $5151\binom{2K+10}{2}$ vectors (degree $\le2K+4L$ in two variables), against $\dim W^{\rm even}_{\le K}$ from `gf_count` (scratch computation): $K=8$: $1674075$ vs $1063651$ (no bound); $K=9$: $1947078$ vs $3824543$. The argument forces a deficit from $K=9$ on and says nothing at $K=4$; the deficit there is the $c$-ghost law (F1).
- **#3 [minor] applied.** The qualifier is added in G0, G3, G3.1, §4 and both proposed ledger lines: the deficit 45 is mod $p$ at the sampled momenta (three now: $P$, $P_2$ of run (ii) and $P_3$ of part `c44s`, all saturated in $\Delta$); the 44 relations of F1(b) and the 45th of F1(b') are exact and independent, so the rank is $\le2882$ at every $P$, and with G7 ($\ge2882$ at generic $P$) **the generic deficit is exactly 45** — stronger than the critic's $[44,45]$, which assumed the 45th unexplained. R84's probabilistic convention is not needed for this row.
- **#4 [note] applied.** The cheap test is run (F1(d), `G3.8-proj-N4`), with a second, predicted projection (`G3.8-proj-Nb4`). `G3.1-null-blocks` is relabelled as a logging line in the Verification block: `len(nulls) == deficit` holds by construction of `left_null`, and "no relation in a single block" restates the per-block ranks of `G3.1-L2-saturated`.
- **#5 [minor] applied** as a proposal in §5 (revised PH31 lines below), with the closing level of F1 and the two caveats: no finite run establishes "no $L$ closes", and every-$K$ closure is necessary, not sufficient, for PH31.
- **#7 [note] applied.** A7 now reads "full rank of the joint matrix as a polynomial matrix in $(P,\Delta_1,\dots,\Delta_s)$"; G7 calls `G7-den-*` a guard (it can fail only for a denominator $\ge p$).
- **#9 [minor] applied by scoping, not by new legs.** The $L$-type functionals were not added: 087 measured the $L$-alone elimination at $>20$ min at $K=3$, $d=3$, and the $d=4$ and $K=4$ cases are larger, outside the budget of the run. §4 *Reading* now says the $\alpha'_{\rm v}=0$ legs test the pipeline in the ghost sector (the $b$-identity is matter-blind), and that the matter sector at $d=4$ and mode 5 is tested only by exchange symmetry (blind to a leg-symmetric error, since $N^{11}=N^{22}$) and by the $d$-genericity of the code; *Not machine-checked* gains the item. The new F1 checks are matter-blind as well ($c$-ghost law).
- **#10 [note] applied.** Falsifiability bullet 3 reads "derived (087 §5); matched at $d=1,2,3$; $d=4$ tests the $d$-independence of the sector counts".
- **#11 [minor] applied.** "$\ge304$ ($\chi$ level $\le5$)" in G6.2, §4 and the R84 lines (completeness of $\chi$ level $\le K+1$ at $K=4$ is not shown); `G6-b-count-42` is listed as a logging line; the R84 verification line says "on 1000 random columns (900 and 763 image vectors)".
- **#12 [minor] applied.** Row (iii) is in *Not machine-checked* and in the PH31 line: "$d_{\rm eff}=5$ ($K=3$, $L=2$, 7945 rows): attempted, stopped for time after 1000 columns, no claim".
- **#13 [note] applied.** Run (iv) and G5 call the $\alpha'_{\rm v}=0$, $\gamma'=\tfrac32$ row an engine check of an exact symmetry ($f_1^{(\gamma'/\kappa)}(w)=f_1^{(\gamma')}(\kappa w)$), at a point where the rank is not full.
- **#14 [note] applied.** The proposed ledger lines no longer cite "22/22 PASS"; they cite the orchestrator's re-run of the final script for all parts: `dim`, `den`, `i`, `iv`, `ii`, `i0`, `ii0` and the fix-pass parts `k2l1`, `c44a`, `c44`, `c44s`, `c45t` (aligned in fix pass 2, critic iteration 2 #13; `c45` retired). The Verification block separates checks from logging lines (`G3.1-L2-saturated` as a saturation test, `G3.1-null-blocks`, `G6-b-count-42`, `G3.9-complement`). The stale docstring of `pair_modp` (087: "n < 2^11"; the int64 bound is $n<2^{16}$) is in a script this brief forbids editing; noted here only. No overflow at $n\le3608$.
- **#6, #8 [notes]**: no action requested (confirmations).

### Changed nodes and dependents

Changed nodes (statement or justification):
- **A7** — wording only (#7); statement unchanged in content.
- **G0** (root) — **statement changed**: the $K=4$, $L=2$ deficit is now "2882/2927 mod $p$ at three momenta, exactly 2882 at generic $P$, 45 exact $c$-ghost relations ((F.6) 44, (F.13) 1), finite input level"; before: "a finite-input-level deficit of 45, … not of R84's type", without qualifier (#3) or mechanism.
- **G3** — **statement changed** (exactly 45 at generic $P$; relations identified); justification now [by G3.1–G3.9, G7].
- **G3.1** — statement qualified (mod $p$; generic rank $\ge2882$); `G3.1-null-blocks` relabelled as a logging line (#4).
- **G3.3** — **statement changed**: "not of R84's type" now rests on the identified relations (level-limited, every $\alpha'_{\rm v}$), not on "closed by level-3 inputs" alone; justification [by G3.4, G3.5, G3.6, G3.9, R84; (F.9)].
- **G3.5–G3.9** — new: G3.5 (44 vectors), G3.6 (level-3 violation pattern), G3.7 ($K=2$, $L=1$), G3.8 (projection tests, #4), G3.9 (the 45th relation).
- **G5**, **G5.2** — wording (#13: engine check of an exact symmetry); claims unchanged.
- **G6** — statement scoped to the ghost sector (#9); **G6.2** — "$\ge304$" (#11), matter-blindness stated, `G6-b-count-42` as a logging line.
- **G7** — statement extended: generic rank exactly 2882 at $K=4$, $L=2$ (with G3.5, G3.9); `G7-den-*` called a guard (#7).

Dependents (transitively up to the root):
- G3.1 → G3 → G0: G3 and G0 rewritten in this pass; they hold as now written.
- G3.3 → G3 → G0: as above.
- G3.5, G3.9 → G7 (lift bracket) → G0: G7's new upper bound uses them; G0 states the exact value with them. Both hold as written, with the derivations (F.6), (F.13) as hand arguments checked through their consequences.
- G5.2 → G5 → G0: G0 cites row (iv) only for 487/487 (G5.1, unchanged); holds.
- G6.2 → G6 → G0: G0 cites the break legs as engine controls; the scoping to the ghost sector does not change G0's statement (G0 claims ranks, and the legs only support that the engine can fail); holds.
- Restatements updated: §4 deficit paragraph and *Reading*, §5 lines, Verification (*Falsifiability*, *Not machine-checked*, the tally), Self-review 1–4, Run (iv) and Run ii0 lines of §3, the §4 break-leg table.

`Open gaps: none`. `Hypotheses in force: none`. The root statement changed, so the next critic pass is a full re-review by the schema's rule; the changes are concentrated in G3.x and F1.

## Fix pass 2 (critic iteration 2)

Brief `agent/briefs/active-computator-093-fix2-20261005T021500.md`; critique `agent/reports/critic-093-iter2-20261005T015500.md` (REVISE, mechanical: 0 blocking, 0 major, 10 minor, 4 notes). No third critic pass; the orchestrator re-runs every part of the final script (must exit 0) and reads the changed passages. Script edits are confined to the fix-pass parts `k2l1`, `c44`, `c44s`, `c45t` (and the retirement of `c45`); the original parts `dim`, `den`, `i`, `iv`, `ii`, `i0`, `ii0` are unchanged in code and conditions. Fix-pass-2 runs: logs in `agent/scratch/computator/computator-093-fix2-20261005T021500/`, JSON outputs in the fix-pass-1 directory under the tag suffix `-fix2` (the earlier files are left in place).

Findings, one entry each, in the order applied (text findings first, then the script findings #4, #6 with their runs):

- **#1 [minor] applied.** Paragraph *The "only if" half of (F.9) for combinations* added after (F.9) in F1(a): a triangular change of basis of the holomorphic creation modes, $e_j=\mathcal C_0[u^{j-2L}(u^2-z^2)^{L-1}]=c_{-j}+\dots$ ($j\ge2L$), shows that the top-level component of any non-zero combination of type (F.6) contains some $c_{-j}$, $j\ge2L$. One correction to the critic's text: the prefactor is $u^{j-2L}$, not $u^{j-2}$ (the latter has top mode $c_{-(j+2L-2)}$); the argument is otherwise the critic's. G0's "iff" now rests on a complete argument; no statement changes.
- **#2 [minor] applied.** "$L_{\min}=2,2,3$ observed at $K=2,3,4$" now carries "(at $d_{\rm eff}=2$ for $K=2,4$; at $K=3$ the value 2 combines the measured full rank at $L=2$ with (F.9) at $L=1$, where $K=3$ was not run)" in §4 (deficit paragraph), F1(a) after (F.9) and Self-review 4; the §5 PH31 line takes the critic's accepted text (#9), which carries the same qualifier. Self-review 1 does not restate the values.
- **#3 [note] applied.** "presumably R84's identities … not analysed" (F1(b'), part `c45t` bullet) replaced by the one-line argument (Route 1 of the critic): the $O_b$ functional on $\chi=c_{-n}\bar c_{-n}c_1|0\rangle$ is $e[R_{nn}]$, so at $\alpha'_{\rm v}=0$ each row is by itself a left-null vector for inputs of every level. Self-review 3 updated. The argument is a hand argument (the critic's); its consequence is now machine-checked by `G3.9-alpha0-rows-vanish` (#4(c)).
- **#5 [minor] applied.** The §4 sentence "Checks: the vectors annihilate the image … at $\alpha'_{\rm v}=\tfrac12,\tfrac15,0$ … sign-flipped versions do not annihilate it" is split by relation: the 44 at three vertices; (F.13) informatively at $\tfrac12$ (whole image at two momenta via `G3.9-y45-in-null`, saturated null space with ratio 9, targeted columns) and $\tfrac15$ (targeted columns), its random-column and $\alpha'_{\rm v}=0$ tests empty. Self-review 2's "three vertices for (F.6) and (F.13)" is split the same way.
- **#13 [minor] applied.** Aligned with the orchestrator's re-run of all parts: the §5 preamble (now: all parts, `c45` retired, logging lines and the INFO line not counted), *Minor findings* #14 of fix pass 1, and the fix-pass-1 intro (all six parts named, `c45` marked retired). The Verification block gains a fix-pass-2 block (below, with the runs).
- **#8 [minor] applied.** The falsifier block in §5 is headed "Proposed – Harold's decision (change to a registered hypothesis's falsifier). Not adopted: not to be promoted without Harold's go". The critic's optional tightening ("Deficits from relations of the $c$-ghost pole structure that hold only below a finite input level and disappear when $L$ is raised …") is added below it as an optional choice, not merged into the wording.
- **#9 [minor] applied.** The §5 PH31 verification line is the critic's accepted text: it adds the ghost-sector scope of the controls (the $\alpha'_{\rm v}=0$ legs and the $c$-ghost checks are matter-blind; the matter data at $d_{\rm eff}=4$ and mode 5 are tested only by exchange symmetry), the $L_{\min}$ qualifiers of #2, the tag "hand derivation" for the relations, and the critics' report names.
- **#10 [minor] applied.** The §5 R84 verification line is the critic's accepted text: "with inputs of level $\le3$" in place of "for $L=3$", the lift stated for the full-rank rows, row (iii) added ("$K=3$, $d_{\rm eff}=5$: not obtained").
- **#11 [minor] applied.** The sentence "Status of R84 unchanged (… — Verified gains the rows above) … proposed as part of R84's `Verified` row set" is replaced by a separate proposed Status clause (the critic's text): full-rank rows Verified; $K=4$, $L=2$: generic rank exactly 2882/2927, the 45 relations Proven (hand derivation, consequences machine-checked with break legs), the lower bound Verified. A *Tag calibration* paragraph says why: the relations are a hand proof checked through their consequences, and the $K=4$, $L=2$ row is not a full-rank row.
- **#12 [note] applied as a proposal.** §5 gains a proposed R84 narrative edit: after "no selection rule follows", "(no every-level rule; at input level $L$ there are level-limited $c$-ghost relations once $K\ge2L$, record 093)"; whether the $c$-ghost law gets its own ledger entry is left to the orchestrator.
- **#14 [note] applied.** F1(a) Commentary on (F.2) cites Rastelli–Zwiebach, arXiv:hep-th/0006240, §3, as the method of which (F.6) is the $c$-ghost analogue. The arXiv number is confirmed against `paper/string_theory.bib` (key `Rastelli:2001:TachyonPotentialsStar`, JHEP 09 (2001) 038); the section number comes from 078 and the critic and is marked "to be checked" (no local review of the paper).
- **#4 [minor] applied (script).** All four replacements made as the critic proposes; every new or changed condition was set after the first outcomes (fix pass 1), which this entry discloses with the derivation behind each.
  - (a) `G3.9-y45-in-null` and `BREAK-G3.9-y45-in-null-flip`, new in `run_c44` (parts `c44`, `c44s`). Before: the coefficient 9 of $y_{45}$ was a printed line of `run-c44s.log`, compared by hand. Now: rank(left-null space + the 44 + $y_{45}$) must be 45 with a left-null space of dimension 45, i.e. $y_{45}$ annihilates every column of the image. Derivation: (F.13) holds for every pair of inputs of level $\le2$; at `c44` the scan stops at rank 2882, which is the whole image since 2882 is a proven upper bound at every $P$ (critic's remark). The flip leg must give 46: $y_{45}$ and its flip differ by $2z^2e[R_{33}]$, so both lie in the null space only if $e[R_{33}]$ does, and at $\alpha'_{\rm v}=\tfrac12$ it does not ($e[R_{33}]$ is non-zero on 61 of 150 targeted columns, `c45t`).
  - (b) `c45t`: `G3.9-y45-*-t` (at $\alpha'_{\rm v}=\tfrac12,\tfrac15$) now passes only if $y_{45}$ pairs to zero **and** $e[R_{33}]$ is non-zero on at least one of the 150 columns. Before: "$y_{45}$ pairs to zero" alone, which a sample missing the rows passes (as the three `c45` lines did). Derivation of the non-vacuity condition: by (F.12) the rows $R_{33}$, $R_{44}$ see a column only through $\mathsf B$, $\mathsf C$, i.e. through pairs with $b_{-2}$ in one input and $\bar b_{-2}$ in the other, which is what the targeted sample draws. The former conjunction `BREAK-G3.9-y45-*-t` ($-z^2$ non-zero **and** level-3 columns non-zero) is split into `BREAK-G3.9-y45-*-t-flip` and `BREAK-G3.9-y45-*-t-L3`, so that a failure names the leg. Remark: once $y_{45}\cdot{\rm col}=0$, the flip pairs to $-2z^2\,e[R_{33}]\cdot{\rm col}$, so the flip count equals the non-vacuity count (61, 64); the `-L3` leg is the independent one.
  - (c) `c45t` at $\alpha'_{\rm v}=0$: the leg `BREAK-G3.9-y45-0-3-t`, which failed because its premise was wrong, is replaced by `G3.9-alpha0-rows-vanish`: $e[R_{33}]$ and $e[R_{44}]$ pair to zero separately on the 150 targeted $L\le2$ columns and the 150 level-3 columns. Derivation: R84 (4.3) at $\alpha'_{\rm v}=0$ on $\chi=c_{-n}\bar c_{-n}c_1|0\rangle$ (#3), for inputs of every level. It can fail on a named wrong result: rows that are not left-null at the vertex used, as at $\alpha'_{\rm v}=\tfrac12$, where the same type of column gives $e[R_{33}]$ non-zero 61 times. The $y_{45}$ line at $\alpha'_{\rm v}=0$ is printed as `INFO` (not in the PASS/FAIL count).
  - (d) Part `c45` retired: removed from `NEW_PARTS` and from the dispatch table, so the orchestrator's re-run does not run it; `run_c45(targeted=False)` stays in the code (used once by hand below); `run-c45.log`, `checks-c45.json`, `results-c45.json` stay in the fix-pass-1 scratch as superseded. "Almost never" in F1(b') is corrected to "about one column in 150" (critic's estimate: $P(\text{hit})=2\cdot81/101^2\approx1.6\,\%$, about 2.4 hit columns per 150, of which about 40 % have $t_{0,0}\ne0$).
- **#6 [minor] applied (script).** Three conditions tightened after their first outcomes:
  - `G3.7-K2L1-rank`: `rank <= 67` → `rank == 67` (still saturated). The old condition passed for any saturated rank $\le67$ and could not detect a relation beyond the six rows of (F.9) at $L=1$ (an extra mechanism, or an engine losing columns). The value 67 = 73 − 6 is (F.9) at $L=1$ (six independent single rows, rank $\le67$) together with G3.7's claim that they are the whole cokernel; it was written as the prediction before the first run (F1(c)) but encoded as $\le$.
  - `G3.7-K2L1-annihilate`: adds `len(nulls) == 6`. The old condition (the 6 lie in the left-null space) passed for a left-null space of any dimension containing them, so it could not detect a seventh null vector; G3.7 claims the 6 span it. Same derivation (rank 67, six independent rows).
  - `G3.9-P3-saturated`: `rank < 2927` → `rank == 2927 - 45`. The old condition passed for any saturated deficit and could not detect a different deficit at the third momentum (44, if (F.13) failed there; 46, from an extra relation). The value 2882 is the upper bound from the 45 independent exact relations (F.6), (F.13), valid at every $P$, attained at a generic momentum by G7; it had been measured at $P$, $P_2$ (run (ii)) and $P_3$ (fix pass 1) before the condition was tightened.
- **#7 [note] no action needed.** The critic's list of the checks that can fail on a named wrong result agrees with the Verification block; its one open item, the ratio 9 as a printed line only, is promoted to a check by #4(a) (`G3.9-y45-in-null`).

### Changed nodes and dependents (fix pass 2)

Changed nodes:
- **G3.7** — justification only: the conditions of `G3.7-K2L1-rank` (`== 67`) and `G3.7-K2L1-annihilate` (left-null space of dimension 6) now assert what the node states; statement unchanged.
- **G3.9** — statement extended (no claim withdrawn): $y_{45}$ lies in the left-null space of the whole $\alpha'_{\rm v}=\tfrac12$ image at two momenta and its flip does not; at $\alpha'_{\rm v}=0$ each of its two rows is by itself a left-null vector (R84 (4.3)), which is why its test there is empty. Justification: new checks `G3.9-y45-in-null` (+ flip leg), the non-vacuity count in `G3.9-y45-*-t`, the split legs `-flip`, `-L3`, `G3.9-alpha0-rows-vanish`; `G3.9-P3-saturated` tightened to `rank == 2882`; part `c45` retired.
- **G0**, **G3.3** — statements unchanged; the "iff" of (F.9) that both cite now has its "only if" half for combinations (F1(a), #1), so their justification is complete where it was argued for a single $y_B$ only.

Dependents (transitively up to the root):
- G3.7 → G3 → G0: G3's and G0's statements use G3.7 as stated; hold.
- G3.9 → G3, G7 → G0: G7's upper bound uses "45 independent exact relations", unchanged; G3 and G0 hold as written. The extension of G3.9 is a stronger check of the same relation.
- Restatements updated: §4 deficit paragraph (checks split by relation, $L_{\min}$ qualifier), F1(a) (after (F.9), Commentary citation), F1(b') (`c45`, `c45t` bullets), Self-review 2, 3, 4, §5 (all lines), Verification (fix-pass-2 block).

`Open gaps: none`. `Hypotheses in force: none`.
