# 010 — A4: the CFL (2,2,0) relation for the HS product m₂ = Δ∘ℓ₃

**Date:** 2026-07-02/03 (Fable, inline;
no critic pass at promotion).
**Blind critic pass DONE 2026-07-09 (Opus, ST9): ACCEPT — 0 Fatal, 0 Serious.** The
critic re-derived by hand and confirmed: the odd-pairing Q-move (relative MINUS
genuine; naive coderivation fails; check 1e two-sided), the assembly signs (S2=−1,
C3=−1 pinned two ways), non-circularity (the lemmas hold on data where Jacobi FAILS;
Jacobi enters exactly once, at the end), (1,2,0)⇔[Q,ℓ₂]=0 as a genuine iff, and the
ghost bookkeeping. Clarifications applied 2026-07-09: [C1] see "Result" note below
(only two signs machine-measured); [C2] tex eq:lemmaB1 conflation of W·Y with the
coderivation term FIXED (distinct tensors, separately inert on the even sector);
[C3] ledger generality softened (toy-verified, general proof pending); [C4]/[C5] the
6b inertness mechanism and the CFL all-plus suspension reconciliation are named as the
two analytic steps owed to the paper-grade write-out. Report
`agent/reports/critic-r16-220-20260709T140000.md`.
**Question (2026-07-02; open core of the restricted correspondence, A3 note
§2.3):** does the two-output product m₂ = Δ∘ℓ₃ obtained from the HS construction satisfy
the IBL structure relations — in particular the CFL (2,2,0) relation — as a consequence
of the cyclic L∞ relations of the ℓ_n?

**Answer: YES on the even-parity sector, with the suspension bookkeeping identified
precisely.** ("Even-parity sector" = input pairs of equal Grassmann parity,
ε_A + ε_B ≡ 0 — pure OFF-SHELL Grassmann bookkeeping, no on-shell condition anywhere;
it contains every object of the construction, since Ψ (N_gh=2), Σ (N_gh=4) and all
gauge composites are Grassmann-even.) Verified by a lemma decomposition, each lemma tested at machine precision on
GENERIC cyclic data (no L∞ constraints imposed on the test data, so no degenerate corner
can make the checks hollow), in the physical grading ε = N_gh mod 2.
Script: `codes/verify-220-relation.py` (numpy, dim-16 graded toy, fixed seed, all checks
PASS; every discovered sign dressing unique in its search space; falsifiable — sign flips
and genus-term inclusion break the identities).

## Result

For any cyclic L∞ algebra (H, ω₁, Q, ℓ₂, ℓ₃) — Q cyclic and nilpotent, ℓ₂/ℓ₃ from
totally graded-symmetric vertices V₃/V₄, Jacobi-homotopy [Q,ℓ₃] = −ℓ₂∘₁ℓ₂ — define
Δ = ω₁⁻¹ (ghost +5 bivector), m₂ = Δ∘ℓ₃ = p₂,₂,₀, p = Δ∘ℓ₂ = p₁,₂,₀. Then, on the
E₂ coalgebra over the **even-parity sector** (input pairs of equal Grassmann parity;
contains the entire Σ/Ψ⊗² sector, ghost 4):

    Q̂∘m₂ − m₂∘Q̂ − p∘ℓ₂ + ℓ̂₂∘₁p̂  =  W·(Δ∘([Q,ℓ₃] + ℓ₂∘₁ℓ₂))  =  0   (Jacobi),

i.e. **the (2,2,0) relation holds**, with term signs (+1, −1, −1, +1) in bare physical
variables and W the first-output parity weight (see below). **Sign accounting
(critic C1, 2026-07-09):** only the two middle signs (−m₂Q̂, −p∘ℓ₂) are
machine-measured (uniqueness fits 5a/6a + falsification 7c); the first is the
normalisation reference, and the fourth term ℓ̂₂∘₁p̂ is *inert* on the even sector
(check 6b), so its sign is conventional, not measured — on the even sector the
relation is effectively the three-term identity Q̂m₂ − m₂Q̂ − p∘ℓ₂ = 0, the fourth
term being carried only to display the CFL shape. Likewise
**(1,2,0) ⟺ [Q,ℓ₂] = 0** (the L∞ (2,1,0) axiom) — so the full genus-zero chain
(1,1,0)–(2,2,0) of IBL relations holds for the Δ-raised products of a cyclic L∞ algebra.
**This closes the open core of the restricted (HS) correspondence at O(g_s²)** (A3 note
§2.3 candidate 1; the homological "contact" mechanism of §3.4(ii) is now on the same
footing as the dynamical one).

## Lemma decomposition (each verified independently, generic data)

- **Lemma A (Q-move; unique dressing, all inputs, raw):**
  Q̂∘m₂ − m₂∘Q̂ = W·(Δ∘[Q,ℓ₃]), where W multiplies the component whose first output
  strand is e_a by (−1)^{ε_a}. The relative MINUS (a graded commutator would naively
  give a plus for odd m₂... the bare N_gh(m₂)=+2 map is even) and the weight W both stem
  from the **odd-pairing Q-move**: since ω₁ pairs opposite parities (saturation 5), its
  inverse obeys Σ Qu_α⊗v_α − (−1)^{ε(u_α)} u_α⊗Qv_α = 0 (relative minus; the naive
  coderivation Q̂Δ = 0 is FALSE — check 1e). Same lemma for the cobracket.
- **Lemma B1 (regrouping; unique signs, all inputs, raw, pure ℓ₂-cyclicity):**
  W·(Δ∘(ℓ₂∘₁ℓ₂)) = W·Y − p∘ℓ₂, where Y = Δ-raised double-ℓ₂ chain terms
  Y = Δ^{ai}[ℓ₂(ℓ₂(v_i,·),·) + Koszul-swap]. Uses only graded symmetry of ℓ₂ and the
  parity flow of Δ ((−1)^{ε_i} = −(−1)^{ε_a} across Δ).
- **6b (physical sector):** the coderivation term ℓ̂₂∘₁p̂ (self-pair/genus term excluded)
  AND the chain term W·Y are each exactly **inert** on the E₂ coalgebra over even
  inputs: raw norms ≠ 0, projected 4e-15 — genuine cancellations, not support accidents
  (they are *distinct* tensors, separately inert; off the even sector they are not
  equal — critic C2). So on the physical sector the (2,2,0) content is carried by
  Lemma A + Lemma B1. **Open analytic step (critic C4):** the *graded mechanism* of
  this inertness (which symmetry component the coderivation lands in) is evidenced
  generically but not derived — it is one of the two steps owed to the paper-grade
  write-out (the other being the CFL all-plus suspension reconciliation, C5).

## Structural byproducts (exact in the toy, both parity conventions tested)

1. **The two output strands of ANY Δ-raised product are graded-symmetric in the
   one-unit-SHIFTED parity** (residual 0.0 for the shifted rule, O(1) for all others;
   both for m₂ and p, and in both the physical and the (N+1)-parity runs). This is the
   toy-level fingerprint of R7/Hq1: the E₂ coalgebra of the raised products is the
   twisted symmetric power — ω₂^symp = ω₁⊗²∘(s⊗s) is where cyclicity lives.
2. The odd-pairing Q-move sign (Lemma A) and the first-strand weight W are the explicit
   avatars of the suspension in bare physical variables.
3. **Genus separation matters at this order:** including the self-pair contraction (ℓ₂
   eating both strands of one cobracket — the (1,1,1) loop term) breaks the (2,2,0)
   identity (residual 12.6). Mechanically the content is that the loop term is NOT
   inert on the even sector (unlike the coderivation term), hence must be excluded by
   the genus grading (critic M6: modest reading).

## Scope and residuals (honest)

- **Toy-level verification** (dim-16, one graded space, generic random data, fixed
  seed). The identities are multilinear in (Q,ℓ₂,ℓ₃) with all parity sectors populated;
  machine-precision vanishing of ~10⁴-component tensors on generic data is strong
  evidence of the identity, but a paper-grade proof should be written out once (the
  hand derivations above are the skeleton; Lemma A and B1 are short).
- **Residual (flagged):** the full-space (odd-input-sector) bare-variable form of the
  coderivation term ℓ̂₂∘₁p̂ carries input-parity-dependent Koszul dressings — the honest
  one-unit suspension bookkeeping (CFL's E(C[1])) is needed there. This affects NO
  physical-sector statement (Σ, Ψ⊗², all gauge objects are even). Cheap future task:
  redo the toy in explicitly suspended variables with per-slot s-weights.
- For the string: as always, the formal manipulations assume the distributional
  Δ = ω₁⁻¹ contractions converge (same formal level as R1–R15).
- ~~NOT yet critic-reviewed~~ Blind critic pass DONE 2026-07-09: ACCEPT (see header).

## What this changes in the notes

- A3 note §2.3 (restricted correspondence, open core) and §3.4 (mechanism (ii) caveat):
  the (2,2,0) verification is now DONE at this level — updated in the note.
- Ledger: promoted as **R16** with the scope above (blind critic ACCEPT 2026-07-09).
