# Derivation record 006 — Phase 6: Riemann-surface interpretation of the HS construction

Date: 2026-06-28
Author agent: computator (writing mode)
Brief: agent/briefs/done-computator-phase6-riemann-20260628T175103.md
Outputs:
  - knowledge/cubic-sft-riemann-surfaces.tex (standalone note, compiles clean: biber + pdflatex x2, 0 undefined cites/refs, 13 pp after Revision 1)
  - knowledge/cubic-sft-riemann-surfaces.bib (seeded from cubic-sft-overview.bib)
  - codes/verify-phase6-riemann.py (8/8 PASS, falsifiable checks after Revision 1)

> **REVISION 1 (2026-06-28) — physics correction, read first.** The original §6/§7
> framed the auxiliarity of Σ as a **twist-only / s=0 / no-length-modulus** neck.
> That is **wrong** and conflated two distinct facts. This was flagged in review; the
> correction is verified against ledger R3 (Erbin–Fırat stub, review C9ETB6WE).
>
> - **Auxiliarity (R3, corrected).** The Σ-propagator integrates the proper-time
>   length s over a **BOUNDED** range, ∫_0^{2λ} ds e^{−sL₀} = (1−e^{−2λL₀})/L₀
>   → 2λ as L₀→0. It is regular (no on-shell pole) because the **s→∞ long-cylinder**
>   region — where the 1/L₀ pole lives — is **excluded**, NOT because s is frozen
>   at 0. The field genuinely propagates over a finite proper time. The Σ-neck
>   carries the **FULL complex plumbing modulus** q=e^{−s+iθ} (TWO real moduli,
>   dim_C=1).
> - **Moduli counting (corrected).** M_{0,4} is 2-real-dim (dim_C=1); V_{0,4} is
>   2-real-dim. One internal Σ-line = one complex modulus = 2 real = dim_R M_{0,4},
>   so it CAN (conjecturally, Q4) fill the **interior**. A twist-only (s fixed,
>   |q|=1) neck is only 1-real-dim and reaches **only** the codim-1 boundary
>   ∂V_{0,4}.
> - **R2 vs R3 disentangled.** (R2) twist-only |q|=1 gluing of two V₃' reproduces
>   the 1-real-dim BOUNDARY ∂V_{0,4} (boundary-matching check; interior = Q4 open).
>   (R3) bounded-length propagator excluding s→∞ = the AUXILIARITY mechanism, on a
>   full 2-real-dim neck. R2 must NOT be used to explain R3.
> - **Hyperbolic-seam parallel (corrected).** Both the hyperbolic seam and the
>   Σ-neck carry length moduli; the auxiliary/elementary feature is the **bounded**
>   length range (excluding the degeneration), NOT twist-only. The earlier
>   "hyperbolic length integrated but Σ-neck has no length modulus" was backwards.
> - **Script (Revision 1).** Two hollow checks removed: old (7) re-asserted
>   hard-coded constants; old (8) mislabelled p_{2,2,0} as single-output. Replaced
>   by falsifiable checks: new (6) auxiliary channel 2-real-dim vs twist-only
>   boundary 1-real-dim (2≠1); new (7) sympy: bounded propagator regular (→2λ) vs
>   unbounded pole (1/L₀) — the R3 mechanism; new (8) IBL degree collapses to −1 at
>   d=0 but is (k+g)-dependent at d≠0. New (3) made the load-bearing moduli count.
>   Still 8/8 PASS.
> - **Also fixed (critic B1/B2).** §5 cut-then-reglue prose corrected: Δ=ω₁⁻¹
>   **raises one INPUT leg** of ℓ₃ to a second output (net 2-in/2-out = p_{2,2,0}),
>   NOT "splits the output into two" (which would be 3-in/2-out = p_{3,2,0}). §5 R6
>   parenthetical reworded so Q-exactness modifies the **bracket–cobracket
>   composition**, with m₂ the witnessing homotopy — not attached to m₂ itself.
>
> The rest of the record below predates Revision 1; statements about "twist-only
> ⇒ auxiliary / no length modulus" in it are superseded by the above.

> **Nature of this record.** This is an *interpretive synthesis*, not a new
> derivation. No closed-string algebra is re-derived; ledger rows R1–R10 are
> reused and cited. The deliverable is the geometric *meaning* of the Phase-5
> objects, packaged as a standalone LaTeX note. This record states what was
> synthesised, every ledger row reused and where, the one class of new
> (checkable) quantitative claims and its check, and the open points carried.

---

## What was synthesised

A self-contained conceptual note giving the modular-operad / coloured-puncture
reading of every Phase-5 object, at the level of topology and operadic
combinatorics only (NO explicit local coordinates — the hyperbolic coords of
Z3ZEA644 App. A are a one-line pointer, brief hard scope). Section map of the
note:

1. **Punctures and the state space** (`sec:punctures`) — closed states = local
   operators at punctures; one puncture carries Hilb; level-matching
   `Hilb_0 = ker L0^- ∩ ker b0^-` is the spinless condition (L0^- generates the
   rigid rotation of the local frame). Ties to no-go (H3), untouched by HS.
2. **Coloured punctures** (`sec:coloured`) — colour 1 = physical Ψ-punctures
   (full Hilb_0, N_gh=2); colour 2 = auxiliary Σ-punctures, a *pair* in
   Sym^2 Hilb_0 (N_gh=4). Antisymmetric part ∧^2 decouples (R9). Coloured
   modular operad introduced as *dictionary only* (flagged, not a theorem).
3. **Modular operad / IBL dictionary** (`sec:operad`) — p_{k,ℓ,g} ↔ M_{g,k+ℓ}
   with k in/ℓ out punctures; χ=2-2g-k-ℓ (R5); Loo truncation = (ℓ=1,g=0)
   single-output sub-operad (R5/R6); cobracket p_{1,2,0} = separating
   degeneration (one output split into two).
4. **m2 = p_{2,2,0} on M_{0,4}** (`sec:m2`) — 2-in/2-out, χ=-2 (R5);
   m2 = Δ∘ℓ3 = cut-then-reglue (Δ re-opens the single ℓ3 output into the
   Σ-pair); R6 Q-exactness read as a boundary/degeneration statement, kept
   explicitly distinct from the R8 field EOM.
5. **ω2 = ω1^{⊗2} as gluing** (`sec:omega2`) — ω1 = sew two punctures (one odd
   c0^- defect); ω2 = glue two pairs; graded **SYMMETRIC** physically (R7), NOT
   a symplectic form on unshifted Hilb_0^{⊗2}; BV-shift partner = orientation
   choice on the sewing; cyclicity = relabel symmetry of the sphere.
6. **HS channel geometrically** (`sec:HS`) — V4 = residual region of M_{0,4}
   uncovered by two cubic vertices; HS = factor it through a Σ-pair across a
   |q|=1 twist-only neck (R2); twist-only ⇒ no length modulus ⇒ no s→∞
   degeneration ⇒ no on-shell pole ⇒ Σ auxiliary (R2/R3/R9); integrating Σ out
   (R10) = collapsing the neck = recovering the contact term. Hyperbolic seam =
   pointer only (parallel but NOT identical: hyperbolic seam length is
   integrated, the Σ-neck has no length modulus).
7. **No-go evasion geometrically** (`sec:nogo`) — single symmetric cubic vertex
   ⇒ unique 3-channel tiling of M_{0,4}, fails duality at λ=-1 (enhanced square
   group); second colour = the missing tile (twist-only ⇒ contact-like, not a
   4th propagator channel). Evades (H1) with (H4/H6) modified in tandem; NOT a
   contradiction of the theorem, NOT a proof the interior is covered.
8. **New vs borrowed** (`sec:newold`) — borrowed: CFL operad + transfer (R5/R6),
   classical vertex geometry; borrowed-with-caveat: strictification is
   single-output only (Borsten), the two-output leg remains to be built;
   genuinely new: ω2 (QOCHA has one ω per sector, no factorised form — WBEIHWFU;
   R7).
9. **Open questions** (`sec:open`) — H2 and (5.1) translated into geometry
   (symmetry of the 4-punctured correlator; non-degeneracy of the residual-region
   pairing on symmetric pairs) but explicitly NOT closed; plus inherited Q4/Q5/Q8.

---

## Ledger rows reused (and where)

| Row | Used for | Note location |
| --- | --- | --- |
| R1 | the boxed HS action `eq:SHS` | `sec:intro` eq. (1.1) |
| R2 | twist-only |q|=1 gluing reproduces ∂V_{0,4}; Z_4 traces channel boundary | `sec:HS` (twist-only, boundary-not-interior) |
| R3 | open-string analogue: propagator regular as L0→0, no on-shell pole | `sec:HS` (pole-free ⇒ auxiliary) |
| R4 | YM rank-3 auxiliary as the finite-dim strictification mirror | `sec:newold` |
| R5 | χ=2-2g-k-ℓ; \|p_{k,ℓ,g}\|; χ(0,4)=-2; Loo = (ℓ=1,g=0) | `sec:operad`, `sec:m2`, `sec:verif` |
| R6 | (2,2,0) structure eq.: m2 Q-exact, not zero; ℓ3 after (2,2,0) | `sec:m2` eq. (4.2), as a degeneration/boundary statement |
| R7 | ω2 = ω1^{⊗2} graded SYMMETRIC physically; cyclicity; det; symp partner = shift | `sec:omega2` (the central presentation pitfall) |
| R8 | Σ-EOM m2(Σ)=m2(Ψ^{⊗2}), stripped from non-degenerate G2 (not R6) | `sec:intro`, `sec:m2` (EOM ≠ R6), `sec:HS` |
| R9 | auxiliarity ⇔ injectivity of m2 on Sym^2; ∧^2 decouples; null vector = sharp counterexample; pole-free = heuristic | `sec:coloured`, `sec:HS`, `sec:open` (5.1) |
| R10 | integrate Σ out = original ℓ3 quartic; 2:1 ratio −1+2=+1; neck collapse | `sec:HS` (collapse), `sec:conclusion` |

All ten ledger rows are reused; none re-derived.

---

## New checkable relations and their check

The note states no new *algebraic* result. It does state small *quantitative*
geometric facts (Euler chars, moduli dims, channel/matching counts, twist-only
locus dim, ghost-number balance). Per the brief, these are backed by a small
combinatorial/sympy self-check rather than left as bare assertions:

`codes/verify-phase6-riemann.py` — **8/8 PASS** (pure Python + itertools; sympy
not required for these integer/combinatorial identities):

1. χ=2-2g-k-ℓ ⇒ χ(M_{0,4})=-2 for p_{2,2,0} and χ=1-k for p_{k,1,0} (R5 form).
2. dim_C M_{0,4}=1, dim_C M_{0,3}=0.
3. Degeneration dim count: 0+0+1(neck) = dim_C M_{0,4}=1.
4. Euler additivity: (-1)+(-1) = -2 (two pairs of pants → M_{0,4}).
5. #perfect matchings of 4 labelled punctures into 2 pairs = 3 (s,t,u channels),
   cross-checked by brute-force partition enumeration.
6. {|q|=1} twist-only locus: real dim 1, real codim 1 in real-2-dim M_{0,4}
   (covers ∂V_{0,4}, a real-codim-1 boundary).
7. Ghost-number balance: N_gh(Σ)=4=2×2, N_gh(m2)=-2.
8. \|p_{k,ℓ,g}\|=-2d(k+g-1)-1 = -1 at d=0 for the low operations (R5 form).

These are **consistency checks of the geometric dictionary against R5 and
elementary combinatorics** — NOT independent re-derivations of the closed-string
algebra, and they say nothing about H2 or (5.1). The verification section of the
note (`sec:verif`) records this scope honestly.

---

## Constraints honoured (brief audit)

- **Physical N_gh=2 parametrisation for all final objects.** Conventions block
  pins Ψ@2, Σ@4. Suspended/BV language appears only as an explicit intermediate
  with a one-line physical translation (ω2 symmetric → symp partner via shift,
  `sec:omega2`).
- **ω2 graded SYMMETRIC physically (R7)**, never called a symplectic form on the
  unshifted Hilb_0^{⊗2}; the symplectic object is the degree-shifted partner.
  Stated with a `\draftnote` pitfall flag.
- **No explicit local coordinates** anywhere; hyperbolic coords are a one-line
  pointer in `sec:HS`. Stayed at topology/operadic-combinatorics level.
- **H2 and (5.1) carried open.** `sec:open` items (A) and (B): translated into
  geometry, explicitly NOT closed; pole-free intuition labelled heuristic (R9).
- **Overclaim audit.** Up-front status block + flags throughout: hyperbolic
  recursion makes cubic structure *manifest*, not literally cubic (Z3ZEA644
  R-note); coloured-operad picture is *interpretation* not proof; interior of
  V_{0,4} conjectural (only ∂V_{0,4} established, R2); coloured operad is a
  dictionary not a theorem. `\draftnote`/`\draftcomment` used for each.
- **No hollow self-checks.** The 8 checks verify the actual quantitative numbers
  the note asserts (against R5 + combinatorics); the note flags that they do NOT
  touch the open CFT residuals.
- British English, cleveref, biblatex+biber, standalone preamble mirrored from
  the overview note (NOT maths_min.sty), arxiv.def reused, local bib seeded from
  cubic-sft-overview.bib.

---

## Open points (carried, not closed)

- **H2** — full graded symmetry of V4 (CFT-level). Geometric image: full S_4
  permutation symmetry of the 4-punctured correlator. Open.
- **(5.1)** — non-degeneracy of V4 on Sym^2(ker L0^- ∩ ker b0^-). Geometric
  image: residual-region pairing has no symmetric level-matched kernel. Open;
  a normalisable symmetric null vector of ℓ3 would be an honest flat direction
  (R9). Pole-free / "generic" arguments are heuristic, NOT evidence.
- **Q4** — covering the *interior* of V_{0,4} via the Σ integration (only the
  boundary ∂V_{0,4} established, R2). Conjectural.
- **Q5** — strict-dIBL counterpart for the cobracket (two-output) sector
  (strictification is single-output only). Not established.
- **Q8** — a fully developed coloured-operad formalism for the (Ψ,Σ) system.
  Not developed; used as dictionary only.

No new ledger row is proposed: this note proves nothing new, it interprets
R1–R10. If the orchestrator wishes to record the geometric dictionary as a
named artefact, it is a *synthesis* row (status: synthesised/Verified-consistency
via the 8/8 checks), not a Proven result.

---

## Verification scope note (no over-claim)

The 8/8 script confirms only that the geometric dictionary's integer/combinatorial
data are consistent with R5 and with elementary moduli combinatorics. It is NOT
an independent CFT-level check and does NOT bear on H2 or (5.1). An independent
numerical cross-check of any closed-string statement remains a numerical-verifier
task; nothing here is claimed as independently verified.
