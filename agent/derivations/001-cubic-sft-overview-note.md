# Derivation record 001 — Cubic closed SFT overview note

Date: 2026-06-23
Author agent: computator
Brief: agent/briefs/done-computator-note-20260623T203558.md
Output note: knowledge/cubic-sft-overview.tex
Verification script: codes/verify-cubic-sft-overview.py (sympy 1.14.0, all 17 checks PASS;
C6 added in the post-critic revision)

This record captures the re-derivations restated in the overview note and their
symbolic self-checks. The note is a *synthesis*; nothing here is new research.
Every check below is a self-check of algebra already asserted in the context
document or one of the nine reviews — it confirms internal consistency, it is
not an independent verification (that is the numerical-verifier's job).

---

## C1 — Hubbard–Stratonovich completion of the square

**Source.** `agent/scratch/context-cubic-sft.md` §"Auxiliary field Σ ∈ H⊗H":
`δS = −(g²/4!) V₄(Σ−Ψ², Σ−Ψ²)`, the resulting `S_HS`, and the EOM
`m₂(Σ) = m₂(Ψ²)`.

**Setup.** Model `V₄` by a symmetric bilinear form `B(X,Y) = Xᵀ M Y` with
`M = Mᵀ` the matrix of the two-output product `m₂` (so `m₂(X) := M X`). This is
the minimal algebraic content of the claim: it is a quadratic completion in the
field `Σ`, so the worldsheet structure of `V₄` is irrelevant to the identity.

**Checks.**
- **C1a.** `S₀ + δS = S_HS` up to the field-independent constant
  `−(g²/4!) V₄(Ψ²,Ψ²)`, where
  `S_HS = (g/3!)V₃ − (g²/4!)V₄(Σ,Σ) + (2g²/4!)V₄(Σ,Ψ²)`. PASS (diff = 0).
- **C1b.** `grad_Σ S_HS = −(2g²/4!)(m₂(Σ) − m₂(Ψ²))`. PASS.
- **C1c.** Stationarity with `M = m₂` invertible ⇒ `Σ = Ψ²` on-shell. PASS
  (`sig = p`).

**Conclusion.** The HS rewriting and its EOM are algebraically consistent;
`Σ` is purely auxiliary iff `m₂` is invertible (the open invertibility proof
is flagged DC1 in the context doc and as an open question in the note).

---

## C2 — Four-point puncture location vs cosh²H

**Source.** `notes_4_point_summary.tex` / context doc §"4-Point Vertex":
`Z₄^{(s)}(q) = cosh²H(q)`, `H(q) = ln(2β/√q)`, and the explicit puncture-location
formula `Z₄ = (q/16β'²)(1 + 4β'²/q)²` with `β' = β`.

**Checks.**
- **C2.** `(q/16β²)(1 + 4β²/q)² = cosh²(ln(2β/√q))`. PASS (diff = 0 after
  `cosh→exp` rewrite). This confirms that the s-channel puncture location from
  gluing two V₃′ at `|q| = 1` lands exactly on the SFT curve `Z₄^{(s)}`.
- **C2b/C2c.** Cross-ratio closure: with `Z_s = cosh²H`, the companion
  channels obey `Z_t = Z_s/(Z_s−1) = coth²H` and `Z_u = 1/(1−Z_s) = −1/sinh²H`,
  matching the context-doc expressions `Z₄^{(t)} = cosh²H/sinh²H`,
  `Z₄^{(u)} = −1/sinh²H`. PASS.

**Conclusion.** The explicit s/t/u channel data are mutually consistent and the
`|q|=1` gluing reproduces the boundary `∂V₀,₄`. Covering the *interior* remains
conjectural (Conjecture 5 in context doc; open question in the note).

---

## C3 — Auxiliary propagator regularity (Erbin–Fırat)

**Source.** Review C9ETB6WE eq. (2.17):
`tilde Δ_Σ = b₀(1 − e^{−2λL₀})/L₀ = 2λb₀[1 − λL₀ + …]`, regular as `L₀ → 0`.

**Checks (scalar part, drop `b₀`).**
- **C3a.** `lim_{L₀→0} (1 − e^{−2λL₀})/L₀ = 2λ` (finite, no pole). PASS.
- **C3b.** Small-`L₀` series `= 2λ(1 − λL₀ + …) = 2λ − 2λ²L₀`. PASS.

**Conclusion.** The open-string auxiliary kinetic operator `Q_B/(1−e^{−2λL₀})`
inverts to a propagator with *no on-shell pole*, so `Σ` carries no physical
degree of freedom. This is the open-string analogue of the closed-string
requirement that the `Σ` sector be purely auxiliary.

---

## C4 — Yang–Mills strictification: integrating out the rank-3 auxiliary

**Source.** Review FBSP8UQ9 §8.3/§9.1: the quartic YM vertex is strictified by a
rank-3 auxiliary `G_{μνκ}` with
`L = −½ G□G − g(∂_μA_ν + (1/√2)∂^κG_{κμν})[A^μ,A^ν]`, EOM
`□G = −(g/√2)∂_{[μ}[A_ν,A_{κ]}]`; substituting back reproduces the non-local
quartic.

**Checks (scalar representative, single contraction).** With
`L(G) = −½ G□G − (1/√2) GJ` and `J` the source:
- **C4a.** EOM `G = −(1/√2) J/□`. PASS.
- **C4b.** On-shell `L = (1/4) J(1/□)J`, the non-local quartic with the correct
  coefficient. PASS.

**Conclusion.** Coefficient bookkeeping of the completion of the square is
correct. This is the gauge-theory toy that mirrors the SFT HS step: a higher
vertex (`ℓ₃`) traded for cubic + auxiliary, integrable because the auxiliary
kinetic operator (here `□`, there `m₂`) is invertible.

---

## C5 — IBL∞ degree formula and L∞ embedding

**Source.** Review RPEPEC4L (CFL), Def. 2.3: `|p_{k,ℓ,g}| = −2d(k+g−1) − 1`;
Euler number `χ = 2 − 2g − k − ℓ`; L∞ truncation `ℓ=1, g=0`.

**Checks.**
- **C5a.** `(k,ℓ,g)=(1,1,0)`: degree `−1` (a differential). PASS.
- **C5b.** L∞ truncation `g=0`: `|p_{k,1,0}| = −2d(k−1) − 1`. PASS.
- **C5c.** `(2,2,0)` (the `m₂` product on a 4-punctured sphere) has
  `χ = −2`. PASS.

**Conclusion.** Degree/Euler bookkeeping is consistent. Note the suspension and
formal-ℏ caveats flagged in the note: CFL build `E_kC` on `C[1]`, `|ℏ|=2d`, and
`ω₁`/`Δ` live only in the cyclic-DGA model (§10–12), not in the abstract
IBL∞ definition.

---

## Items NOT machine-checkable (stated as such in the note's Verification block)

- The IBL∞ master equation `p̂∘p̂=0` component relations and the abstract
  L∞ ⇒ IBL∞ embedding / IBL∞ ⇒ L∞ projection are operadic identities, taken
  verbatim from CFL §2; no closed-form sympy check applies.
- The asymmetric-vertex off-shell exchange condition `z₃(z) = −z₃(1/z)`
  (Sen–Zwiebach 6.8) and the V₃′ local-coordinate maps are quoted from
  ITUZPSEW and the context doc; the `β'=β` puncture-location match is the part
  verified in C2.
- The hyperbolic three-vertex local coordinate (₂F₁ form) and mapping radius
  `ρ` (Γ-function product) are quoted verbatim from Z3ZEA644 App. 8; no
  re-derivation attempted (flagged with the branch-ambiguity caveat).

## Revision (2026-06-23, after blind-critic REVISE)

A blind critic returned REVISE (`agent/reports/critic-note-20260623T205039.md`)
with two Serious items (F1, F2), one Concern requiring a fix (F3), and three
cheap tweaks (F4, F11, F12). All were addressed; the note recompiles cleanly
(pdflatex→biber→pdflatex→pdflatex, 16 pages, no undefined refs, no float loss).

**F1 (Serious) — corrected the IBL∞ (2,2,0) structure equation.** The previous
displayed block `eq:IBLrels` asserted three independent relations
`ℓ̂ᵢ∘m̂₂+m̂₂∘ℓ̂ᵢ=0` (i=1,2,3) read as "ℓ₂,ℓ₃ commute with m₂". This is NOT the
CFL master-equation output and is wrong: there is no "ℓ₃ commutes with m₂"
relation in CFL at all. Replaced with the genuine CFL relations (RPEPEC4L,
Lemma 2.6 table): the (1,2,0) chain-map relation for the cobracket
`p̂₁,₁,₀∘₁p₁,₂,₀ + p₁,₂,₀∘₁p̂₁,₁,₀ = 0` (eq:IBLchain), and the boxed (2,2,0)
structure equation
`p̂₁,₁,₀∘₁p₂,₂,₀ + p₂,₂,₀∘₁p̂₁,₁,₀ + p₁,₂,₀∘₁p₂,₁,₀ + p̂₂,₁,₀∘₁p̂₁,₂,₀ = 0`
(eq:IBLrels). Corrected reading: m₂=p₂,₂,₀ is a Q-homotopy for the
cobracket–bracket composition (Q-exact, = −[Q,p₂,₂,₀]), NOT zero, and ℓ₃=p₃,₁,₀
does not enter (signature ordering places (3,1,0) after (2,2,0)).
New symbolic self-check **C6** verifies the corrected relation is well-formed:
- C6a: the (2,2,0) master-equation s=1 terms are exactly {Q,m₂} and
  {cobracket,bracket}. PASS.
- C6b: ℓ₃=p₃,₁,₀ is absent from the (2,2,0) relation. PASS.
- C6c: CFL signature ordering places (2,2,0) before (3,1,0). PASS.
- C6d: the surviving compositions are degree-homogeneous (both −2d−2). PASS.
The full operadic identity p̂∘p̂=0 itself remains quoted from CFL (not closed-form
sympy-checkable); C6 checks the structural facts the corrected text asserts.

**F2 (Serious) — re-attributed the twist-only |q|=1 gluing.** Sen–Zwiebach's
covering uses the standard twist-INTEGRATED propagator (θ∈[0,2π] + length
integration). The twist-only (|q|=1) gluing AND its reproduction of ∂V₀,₄ are
THIS PROJECT's modification/computation, not a result of \cite{SenZwiebach1994}.
Fixed the framing in §2.2 (H6 bullet), §3.2 (W₃/W₂ paragraph), and the §5.1
"Twist-only plumbing" opening (now titled "Twist-only plumbing (this project's
modification)" with an explicit disclaimer). V₃′ (the asymmetric vertex with
z₃(z)=−z₃(1/z)) remains correctly attributed to Sen–Zwiebach.

**F3 (Concern) — standardised the m₂ type.** Now: ℓ₃:H⊗³→H; raising one index
with Δ=ω₁⁻¹ gives the SQUARE map m₂=p₂,₂,₀=Δ∘ℓ₃:H⊗²→H⊗². The line
⟨A₁|m₂(A₂,A₃)⟩=ℓ₃ is stated to be just the pairing definition (pairing one output
back with ω₁ returns ℓ₃), not a second map. "Invertibility of m₂" is now stated as
invertibility of the square map p₂,₂,₀:H⊗²→H⊗² (equivalently non-degeneracy of
the bilinear form V₄ on H⊗²) — well-posed, unlike "ω₁⁻¹∘ℓ₃" as a non-square map.
C1 unchanged (it already modelled V₄ as a square symmetric matrix M=m₂).

**F4 (tweak) — tightened the volume-number footnote.** Now states the resolution:
DOI + majority of sources fix B336 185–221; the lone "B338 487–519" is an error in
the JY32WEUE review's reference list. Bib kept at B336.

**F11 (tweak) — softened the hyperbolic "matches exactly" claim.** Added that the
hyperbolic seam is a pure phase only at FIXED seam length ℓᵢ (still a modulus
integrated over), whereas the |q|=1 auxiliary-Σ propagator has NO length modulus;
the match is structural, not literal.

**F12 (tweak) — softened "necessarily modified as consequences" to "in tandem".**
Added that the review treats asymmetric vertices (H4) and twist-only sewing (H6)
as independent evasion routes, so the co-occurrence is the note's synthesis, not a
logical forcing.

Items the critic confirmed correct (F5–F10, F13, the s-channel formula C2, the YM
toy C4, the stub action/propagator C3, the no-go hypotheses) were left unchanged.

## Inconsistencies / flags found between reviews and the context doc

1. **Sonoda–Zwiebach hypotheses count.** The brief and context doc speak of
   "four no-go assumptions"; the review JY32WEUE enumerates *seven* hypotheses
   (single field with CFT coords; flat CFT background; restricted Hilbert space
   L₀=L̄₀; symmetric vertex; hermiticity; sewing propagator; BRST/off-shell
   duality). The note states all seven and maps the four "evasion" entries of
   the context doc onto them, flagging the discrepancy with `\draftcomment`.

2. **Sonoda–Zwiebach page/volume.** JY32WEUE gives the no-go theorem as NPB
   **B338**, 487–519 (1990) in its own reference list, while citing the
   companion B331 (1990) 592 and elsewhere quoting "B336, 185". ITUZPSEW and
   C9ETB6WE cite the no-go as NPB **B336**, 185–221. The bib entry uses the DOI
   from the JY32WEUE frontmatter (10.1016/0550-3213(90)90108-P) and notes the
   volume ambiguity in a `\draftcomment`.

3. **H2QBSXCT key mismatch.** The brief lists `H2QBSXCT` as "Maccaferri–Merlano,
   localization / explicit quartic in EKS action". The review filed at
   `H2QBSXCT.md` is in fact Maccaferri–Merlano 2019, arXiv:1905.04958 (correct
   key `W4WAL4CX`); `H2QBSXCT` properly belongs to Maccaferri–Vosmera 2022,
   arXiv:2208.00410. The note cites the *paper content* (Maccaferri–Merlano
   2019, EKS localization) as intended by the brief, with the arXiv ID
   1905.04958, and flags the key mismatch.

4. **Maccaferri–Merlano HS auxiliary lives in a single H, not H⊗².** The
   review (reviewer inference) stresses the localized quartic
   `tr[⟨H₁⁺|H₁⁻⟩ + ¼⟨H₀|H₀⟩]` factorises into single-copy states, so a HS
   reduction there keeps the auxiliary in a *single* `H` — unlike the closed
   HS route where `Σ ∈ H⊗²`. The note presents this as a contrast, not a
   precedent for the `H⊗²` structure.
