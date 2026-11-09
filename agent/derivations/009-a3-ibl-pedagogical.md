# Derivation record 009 — A3: pedagogical write-up of the classical IBL_∞ ⇔ L_∞ correspondence at O(g_s²), physical grading

Date: 2026-07-02
Author agent: computator (writing mode)
Brief: `agent/briefs/done-computator-a3-ibl-pedagogical-20260702T120000.md`
Deliverables:
  - `knowledge/cubic-sft-ibl-pedagogical.tex` (+ `.bib`) — standalone pedagogical note (14 pp, compiles clean, 0 undefined citations)
  - `codes/verify-a3-ibl-pedagogical.py` (sympy, **15/15 PASS**)
  - this record

Reused verbatim (NOT re-derived): ledger **R1–R14** + the 2026-07-01 Annotation.
New algebra appears only where the brief demands it: the physical-grading
ghost-number balance of the IBL_∞ component relations (Hq4), the symmetry of the
Σ kinetic term (Hq2), and the h_{μν}=[A_μ,A_ν] elimination (Hq5(ii)).

---

## Scope and assumptions

- Sector: classical g=0, O(g_s²) (quartic truncation), Σ ∈ Sym²H₀.
- Erbin (2023); metric (−,+,+,+); ħ=c=1; α′ explicit; bra–ket.
- **Physical N_gh grading for ALL final objects** (binding). Suspended grading
  appears only as a clearly-marked intermediate with an explicit suspended↔physical
  bridge (§3 of the note).
- No hyperbolic content (shelved). British spelling.

This is a *writing-mode* deliverable: the note is the primary artefact. This record
documents (i) the physics decisions taken, (ii) the three newly-stated relations and
their checks, and (iii) the honest open-item flags.

---

## 1. The two-presentation thesis (note §2)

The O(g_s²) HS action `eq:SHS` (R1/R8) is presented as ONE classical structure with
two faces:

- **(a) g=0 IBL_∞ on H₀.** Products p_{k,ℓ,0}, ℓ≥1; the lowest two-output product is
  m₂ = p_{2,2,0} = Δ∘ℓ₃ (eq:mtwo, N_gh=−2). Σ never appears; it is a structure on the
  single-string space. Schematic action S = ω∘p̂(e^Ψ) (eq:iblaction).
- **(b) cyclic L_∞ on H₀⊕Sym²H₀.** Fields (Ψ,Σ); all products single-output (the two
  outputs of m₂ re-read as one output valued in the new summand Sym²H₀); products read
  off the HS vertices W₃(Σ,Ψ,Ψ), W₂(Σ,Σ) (eq:W3W2). This is the manifestly cubic theory
  one quantises.

**The dictionary (a)↔(b) IS the classical L_∞⇔IBL_∞ correspondence** (note-Q3; Fable
§6bis(d)):
- (b)→(a) = homotopy transfer / integrating Σ out (CFL Thm 1.3/6.1; realized at
  O(g_s²) by R10 and, at amplitude level, by R14's telescoping V₄V₄⁻¹V₄=V₄);
- (a)→(b) = strictification / integrating Σ in (Borsten et al.; CFL §2 embedding read
  backwards; realized at O(g_s²) by the HS step itself, R1/R8).
The leading quasi-isomorphism is (φ₁,φ₂) = (id, ·⊗²), the YM-toy pattern R4 with its
gauge-map component R11.

**Caveat carried (fable §1, critic C7; note §2.4):** "cyclic" on the enlarged space
requires the ODD symplectic form ω₂^symp = ω₁⊗²∘(s⊗s) on (Sym²H₀)[1] (R7's BV
presentation), because the physical ω₁⊗² is graded SYMMETRIC (R7). This *presupposes*
note-Q1's resolution in the BV presentation; it does NOT obviate Q1. Stated precisely,
flagged with a \draftcomment.

---

## 2. Physical ghost-number grading — undoing the suspension (Hq4, note §3)

### 2.1 Suspension determination (from the reviews)

- **CFL (RPEPEC4L):** suspend. E_kC built on C[1] (|c| = deg c − 1); structure maps
  carry |p_{k,ℓ,g}| = −2d(k+g−1)−1 (homological: the differential p_{1,1,0} has
  |·|=−1, i.e. LOWERS the CFL degree — opposite to N_gh, which the BRST operator
  raises). d = n−3 for SFT on a (2n−1)-dim contact target.
- **Münster–Sachs (WBEIHWFU):** suspend. Closed field A_c = s^{−2}Ã_c (degree 0);
  open A_o = s^{−1}Ã_o. Odd symplectic ω_c = (·,c₀⁻·)_bpz∘(s²⊗s²), antisymmetric
  BY the shift ("the apparent symmetry of the BPZ product is removed by the
  suspension", WBEIHWFU l.305).

So BOTH suspend fields AND structure maps, and BOTH fold the load-bearing sign of the
odd symplectic form into the shift.

### 2.2 De-suspended physical N_gh (note Table 1) — CORRECTED (ST6, 2026-07-06)

> **Correction notice (ST6, 2026-07-06).** The original §2.2/§2.3 asserted "+1 per
> Δ-raising", giving N_gh(m₂)=−2 and N_gh(p_{1,2,0})=0. That is the **bug** (naive
> metric-index raising). The Δ=ω₁⁻¹ is *not* a metric on one graded slot: ω₁ is the
> N_gh-5 symplectic pairing (one c₀⁻), so Δ-raising converts an ω₁-**pairing input
> slot** (referenced at N_gh 2) into a genuine **output slot** (referenced at N_gh 3),
> a net **+5**. The critic (Revision 1, S1) already fixed the note's Table 1; this
> brings §2.2/§2.3 into line and adds the decisive ω₂/V₄ saturation anchor.

Fields: N_gh(Ψ)=2, N_gh(Σ)=4. Operations from the sphere anomaly (N_gh=6; one c₀⁻ ⇒
ω₁ pairs states with N_gh sum 5; the genus-0 n-pt vertex saturates at Σᵢ N_gh(Aᵢ)=2n):

| op | (k,ℓ,g) | N_gh |
|----|---------|------|
| Q  | (1,1,0) | +1 |
| ℓ₂ | (2,1,0) | −1 |
| p_{1,2,0} cobracket | (1,2,0) | **+4** |
| ℓ₃ | (3,1,0) | −3 |
| m₂ | (2,2,0) | **+2** |
| p_{1,1,1} | (1,1,1) | **+2** |

**Single-output backbone.** `N_gh(ℓ_n) = 3−2n` from V_n = ω₁(A₁, ℓ_{n−1}(A₂,…,A_n))
with ω₁ pairing sum 5: the one output sits at N_gh 3, each of the n−1 inputs at N_gh 2,
so N_gh(ℓ_n) = 3 − 2n (out−in). Check: Q=ℓ₁ ⇒ +1, ℓ₂ ⇒ −1, ℓ₃ ⇒ −3. ✓

**Δ-raising = +5, not +1.** Raising one input of ℓ_n into an extra output with Δ=ω₁⁻¹
is *not* metric-index raising. ω₁ saturates at N_gh sum 5, so its inverse is a bivector
Δ = Σ_α u_α⊗v_α with N_gh(u_α)+N_gh(v_α)=5. In m₂ = Δ∘ℓ₃ = p_{2,2,0}, feeding u_α into
one ℓ₃-input (removing a −2 input slot) and emitting v_α as an output (adding a +3
output slot) shifts N_gh by (+3)−(−2) = **+5**:
- N_gh(m₂) = N_gh(ℓ₃) + 5 = −3 + 5 = **+2**;
- N_gh(p_{1,2,0}) = N_gh(ℓ₂) + 5 = −1 + 5 = **+4**.

**Two-parameter closed formula (genus-0).** Every output sits at N_gh 3, every input at
N_gh 2, so out−in gives, for a k-input, ℓ-output genus-0 map,

>   **N_gh(p_{k,ℓ,0}) = 3ℓ − 2k.**

ℓ=1 recovers the backbone N_gh(ℓ_k)=3−2k; each additional output (a Δ-raising) adds +5
= (−2 input removed) + (+3 output added). Check against the table: p_{1,2,0}=3·2−2=+4,
m₂=p_{2,2,0}=6−4=+2, ℓ₂=p_{2,1,0}=3−4=−1. ✓

**Genus term.** Adding g fixed by N_gh-homogeneity of the loop relations (§2.3, the
(1,1,1) relation): the genus-1 (1,1,1) map sits at +2 = 3·1−2·1+1, i.e. the genus
coefficient is **+1**:

>   **N_gh(p_{k,ℓ,g}) = 3ℓ − 2k + g.**    ← the ST6 result

Physical reading of +g: each handle in the genus expansion is closed by an operadic
self-gluing that identifies one output leg (referenced at N_gh 3) with one input leg
(referenced at N_gh 2); the ghost excess (3−2)=+1 of the sewn output over the sewn input
is the per-handle shift. (Equivalently: the geometric vertex V_{g,k+ℓ} saturates at
Σ N_gh = 2(k+ℓ) for *all* g — the 6−6g anomaly cancels the 6g−6+2n moduli b-insertions
— so the genus dependence is carried by the *algebraic* loop-operation normalisation, and
the loop relations pin its coefficient to +1.) Cross-check: p_{1,1,1}=+2 ✓ (§2.3).

**Decisive independent anchor — the ω₂/V₄ saturation.** The Σ kinetic term is
⟨Σ, m₂(Σ)⟩_{ω₂} = V₄(Σ,Σ) with Σ at N_gh 4. The two-string form ω₂ = ω₁⊗ω₁ pairs at
N_gh sum 10 (two c₀⁻; two-sphere saturation), and the genus-0 four-point vertex V₄
saturates at Σ N_gh = 2·4 = 8 = 4+4 (the two Σ inputs). Hence
N_gh(m₂(Σ)) = 10 − 4 = 6, so **N_gh(m₂) = 6 − 4 = +2** — independent of any Δ-shift
convention or suspension. This is the ground-truth that kills the stale −2.

### 2.3 Component relations in physical N_gh (note eqs. rel110–rel111)

Each relation is N_gh-homogeneous (N_gh additive under composition):
- (1,1,0): Q²=0, N_gh +2.
- (2,1,0): Q∘ℓ₂ + ℓ₂∘Q̂ = 0, N_gh 0.
- (1,2,0): Q̂∘p_{1,2,0} + p_{1,2,0}∘Q̂ = 0, N_gh **+5**.
- (3,1,0): Q∘ℓ₃ + ℓ₂∘ℓ₂ + ℓ₃∘Q̂ = 0, N_gh −2.
- **(2,2,0) [boxed]:** Q̂∘₁m₂ + m₂∘₁Q̂ + p_{1,2,0}∘₁ℓ₂ + ℓ̂₂∘₁p̂_{1,2,0} = 0, N_gh **+3**.
- (1,1,1): Q∘p_{1,1,1} + p_{1,1,1}∘Q + ℓ₂∘₂p_{1,2,0} = 0, N_gh **+3**.

**Key new result (CORRECTED, ST6):** ghost-number homogeneity of (2,2,0) FORCES
**N_gh(p_{1,2,0})=+4** (not 0). The first two terms have N_gh = N_gh(Q)+N_gh(m₂) =
1+2 = +3; matching the last two, p_{1,2,0}∘ℓ₂ and ℓ₂∘p_{1,2,0}, requires
N_gh(p_{1,2,0}) + N_gh(ℓ₂) = +3, i.e. N_gh(p_{1,2,0}) = 3 − (−1) = **+4**. This agrees
with the direct value N_gh(ℓ₂)+5 (Δ-raising, §2.2) and with out−in = (3+3)−2 = +4. It
is a physically transparent, suspension-free determination of the cobracket ghost
number. Similarly (1,1,1) forces **N_gh(p_{1,1,1})=+2**: N_gh(ℓ₂∘₂p_{1,2,0}) =
−1+4 = +3 (the genus-1 loop of the double gluing carries no extra ghost number), so
N_gh(Q∘p_{1,1,1}) = +3 ⇒ N_gh(p_{1,1,1}) = +2 = 3ℓ−2k+g|_{(1,1,1)}. This is the genus
cross-check of the two-parameter formula. (Checked, Hq4 block; ST6 re-check
`codes/verify-st6-ngh-formula.py`, all PASS.)

### 2.4 R6 ≠ R8 distinction (note §3.5) — NOT conflated

- The (2,2,0) relation (R6) is an **off-shell operator identity**: m₂=p_{2,2,0} is
  Q-exact (=−[Q,m₂]), NOT zero; ℓ₃=p_{3,1,0} does not enter (signature ordering
  (2,2,0)≺(3,1,0)). This is the mechanism making Σ a contact field.
- The Σ-EOM (R8) m₂(Σ)=m₂(Ψ⊗²) is a **field equation** in Sym²H₀ (N_gh 2 both sides),
  built from m₂ alone. Consistent WITH — not identical to — R6 (category distinction:
  operator identity vs field equation).

### 2.5 The suspended→physical bridge is per-slot — RESOLVED (ST6, 2026-07-06)

The absence of a single uniform per-field offset |p_{k,ℓ,g}| = ±N_gh + const is
**expected, not a defect** (note §3.2). It is the ordinary
consequence of the maps being multilinear (k inputs) AND multi-output (ℓ outputs), each
slot carrying its own suspension unit — exactly Harold's L∞ analogy (deg b_n=−1 in the
suspended b-picture is CONSTANT, deg ℓ_n=n−2 in the ℓ-picture grows with inputs; Hohm &
Zwiebach 2017, arXiv:1701.08824 §3.1–§3.2).

Concretely:
- **Physical:** N_gh(p_{k,ℓ,g}) = 3ℓ − 2k + g GROWS with ℓ (each output slot +3).
- **Suspended (CFL/b-picture):** |p_{k,ℓ,g}| = −2d(k+g−1) − 1 is **ℓ-INDEPENDENT**.
- **Dictionary:** the per-slot suspension puts one unit on each of the k input slots
  AND each of the ℓ output slots. The ℓ output-slot units are exactly what remove the
  +3ℓ growth: subtracting 3 per output collapses N_gh to −2k+g, ℓ-independent —
  mirroring how HZ's single output-suspension collapses deg ℓ_n=n−2 to the constant
  deg b_n=−1. A uniform per-*map* offset would need k+ℓ slot-units bundled into one
  constant, which is impossible once ℓ (and k) vary. Hence no offset formula exists,
  by construction — the A3 flag describes a **feature**.

Pinning CFL's absolute d for the critical bosonic string via the contact dimension
remains out of scope (naive fitting of a *single* offset is what gave the earlier
non-integer d — precisely the symptom of a per-slot, not per-map, dictionary). **The

physically unambiguous grading is N_gh (Table 1); the ghost-number balance is
self-contained and needs no d.** See note §3.2 (resolved,
ST6). Full ST6 record: this §2, `codes/verify-st6-ngh-formula.py`.

**Annotation (2026-10-03, node check `critic-r23-r31-degree-node-20261003T203000`).** The dictionary above is inconsistent: it announces a unit on every input and output slot, then shifts the outputs only (3 each). With the strand degree $3-N_{\rm gh}$ on inputs and outputs (CFL's $C[1]$, homological sign), $|p_{k,\ell,g}|=3\ell-3k-N_{\rm gh}(p_{k,\ell,g})=-(k+g)=-2d(k+g-1)-1$ at $d=\tfrac12$ for all $(k,\ell,g)$, the unique value (026 §1.4 (1.11)–(1.12)). A non-integer $d$ is therefore the correct outcome, not a symptom of a wrong dictionary (l. 195–196). Still true: no per-map offset exists, and input and output slots differ in parity (026 §1.2 (iii)).

---

## 3. Hq1 — grading of ω₂, one unit vs two (note §4)

The "two tensor factors → two units" intuition conflates two Z₂ data:
- **operation parity of G₂:** TWO c₀⁻ insertions (one per factor) ⇒ G₂=ω₁⊗² is
  even-as-operation ⇒ graded SYMMETRIC (R7 eq:G2sym): G₂(Y,X)=(−1)^{ε(X)ε(Y)}G₂(X,Y).
  This is where Harold's "two" lives — but it makes G₂ symmetric, the opposite of the
  naive expectation.
- **suspension of the form's complex:** ONE unit C→C[1], per FIELD (Σ is a single
  element of C=Sym²H₀, not two), converting the symmetric G₂ into the antisymmetric
  symplectic ω₂^symp = ω₁⊗²∘(s⊗s). c_s=1 is forced (R7 check Dict, eq:cs); it is a
  BV-presentation CHOICE, not a fact about Σ. The even s^{−2} integer shift is
  parity-irrelevant.

Reconciliation table in note §4.

---

## 4. Hq2 — symmetry of the Σ kinetic term (note §5; NEW check)

⟨Σ, m₂(Σ)⟩ = V₄(Σ,Σ) symmetric under exchange of the two Σ's:
- **(i) general p_{2,2,0}:** the QUADRATIC form only sees the symmetric part of
  B(X,Y)=G₂(X,pY) (eq:quadsym); genuine bilinear symmetry B(X,Y)=B(Y,X) requires p be
  G₂-self-adjoint (cyclic) — for generic p it FAILS. So symmetry is a real property.
- **(ii) m₂ = Δ∘ℓ₃:** holds. G₂(X,m₂Y)=V₄(x₁,x₂,y₁,y₂)=(−1)^{ε(X)ε(Y)}V₄(y₁,y₂,x₁,x₂)
  =(−1)^{ε(X)ε(Y)}G₂(Y,m₂X) from the pair-exchange symmetry of V₄ (special case of full
  graded S₄-symmetry, = cyclicity R7). On the even sector (Σ,Ψ⊗² both N_gh 4) the sign
  is +1: plainly symmetric. This is why the completion of square goes through (R1/R8);
  presentation-independent (R8 step 1a). H2 closed by citation (Zwiebach 1993;
  Annotation).

Checks: Hq2-consistency (B=V₄), Hq2(ii) (symmetric on even sector), Hq2(i)
(generic p asymmetric; quadratic form symmetrises).

---

## 5. Hq3 — reality of the Σ kinetic term (note §6) — with convention forks

- ω₁ carries one c₀⁻ (phase λ under conjugation); G₂=ω₁⊗² carries two ⇒ λ². V₄ real by
  vertex Hermiticity (Sonoda–Zwiebach H5).
- Induced reality: on-shell (Ψ⊗²)^‡=Ψ^‡⊗Ψ^‡=Ψ⊗Ψ ⇒ natural condition Σ^‡=Σ (real
  Sym²H₀, eq:Sigreal) ⇒ V₄(Σ,Σ) real.
- **Convention forks NOT fixed by the ledger (flagged, not silently chosen):**
  (i) the single-c₀⁻ reality phase λ (Zwiebach vs Erbin normalisation); the Σ term
      depends on λ² (one power more stable than the Ψ term's λ).
  (ii) the off-shell reality condition on the independent field Σ; eq:Sigreal is the
      natural (completion-of-square-manifestly-real) choice, recommended but a choice.
  A CFT-normalised sharp statement is deferred (consistent with R14's "CFT-normalised
  reality = write-up-phase" flag). \draftcomment on Hq3 status.

---

## 6. Gauge law R11 (note §7)

δΨ = Q_BΛ + g_sℓ₂(Ψ,Λ) + (g_s²/2)ℓ₃(Ψ,Ψ,Λ); composite law δΣ = δΨ⊗Ψ + Ψ⊗δΨ
(finite: Σ′=Σ+Ψ′⊗²−Ψ⊗²). Three-line proof: X=Σ−Ψ⊗², δX=0 ⇒ δ(S_HS−S_eff)=
−(2g_s²/4!)V₄(δX,X)=0. So δS_HS=δS_eff EXACT, off-shell, finite; S_HS gauge-invariant
to O(g_s³) like the truncation (NOT exactly invariant; δS_eff=O(g_s³)≠0; critic S1). No
independent Λ₂ (Σ has no Q_B kinetic term). Coalgebra reading: composite law = the H⊗²
component of p̂(Λ,e^Ψ), arXiv:1905.06785 eq. (5.55). This is R11 reused verbatim; not
re-checked here (already verified in codes/verify-hs-gauge-invariance.py, 5/5).

---

## 7. Hq5 — YM toy, comparison NOT substitution (note §8; NEW check for (ii))

- **(i) colour-kinematic 1/□ form (R4, FBSP8UQ9/Borsten2021 §8.3), KEPT:** rank-3 G,
  kinetic op □ (invertible away from p²=0), non-local quartic ¼J(1/□)J. "Excellent for
  understanding invertibility of m₂" — the auxiliary is auxiliary because □ has no
  on-shell pole in the contact channel.
- **(ii) Harold's h_{μν}=[A_μ,A_ν], worked completely (NEW):**
  L_h = ¼tr(h_{μν}h^{μν}) − ½tr(h_{μν}[A^μ,A^ν]).
  h-EOM: ½h − ½[A,A]=0 ⇒ h_{μν}=[A_μ,A_ν] (exactly).
  On-shell: ¼tr[A,A]² − ½tr[A,A]² = −¼tr[A_μ,A_ν][A^μ,A^ν] (correct coefficient).
  Kinetic operator ∂²L_h/∂h² = ½·1: ULTRALOCAL, constant, always invertible (no □).
  Checked Hq5(ii): EOM, on-shell value, constant invertible Hessian (su(2), Euclidean
  toy metric; identity is signature-independent).
- **Comparison (note §8.3):** G-form = non-local kinetic + local coupling; h-form =
  ultralocal kinetic + local coupling; closed-string Σ has V₄ = contact-type kinetic
  (like h: ultralocal-in-moduli, no pole) but non-trivial invertibility on Sym²/ker V₄
  (like G). V₄ sits between the two toys — which is why both illuminate and neither
  alone is the whole story.

---

## 8. Outlook (note §9) — cite, do not develop (Phase B)

All-orders tower on ⊕_k Sym(H₀⊗ᵏ) (R12); Route C multiplier linearization (R13);
trinion/pants picture (R12 geometry). Cobracket p_{1,2,0} and genus-1 p_{1,1,1} become
more than bookkeeping at loops. Next milestone: O(g_s³) quintic step.

---

## 9. Verification

**⚠ SUPERSEDED BLOCK (annotated 2026-07-09, blind-critic finding C1).** The Hq4
row below records the ORIGINAL (pre-Revision-1) run, whose "FORCED" values
N_gh(p_{1,2,0})=0 and N_gh(p_{1,1,1})=−2 are the **stale, WRONG** values later
corrected by Revision 1 / ST6 (correct: **+4** and **+2**; see §2.2, Table 1,
and the ST6 revision notice). The relation-homogeneity checks passed for the
wrong values because a uniform Δ-shift error cancels between the two sides of
each relation — they are convention-blind (this is exactly why the +5 Δ-shift
bug survived the original 9/9). Current verification: Revision 1's
`verify-a3-ibl-pedagogical.py` **21/21 PASS** (Hq4-sat derives the absolute
N_gh from saturations) and the ST6 script `verify-st6-ngh-formula.py`
(restructured 2026-07-09: Tier-1 saturation-support derivation, genuine). The
original table is kept only as an audit trail:

| block | checks | outcome |
|-------|--------|---------|
| Hq4 | ghost-number balance of (1,1,0)…(3,1,0),(2,2,0),(1,1,1); ~~(2,2,0) FORCES N_gh(p_{1,2,0})=0; (1,1,1) forces N_gh(p_{1,1,1})=−2~~ **[stale — see notice above]**; EOM N_gh=2 | 9/9 PASS (convention-blind) |
| Hq2 | B=G₂(·,m₂·)=V₄; symmetric on even sector (m₂ from symmetric V₄); generic p asymmetric; quadratic form symmetrises | 4/4 PASS |
| Hq5(ii) | h-EOM=[A,A]; elimination = −¼tr[A,A]²; ultralocal invertible Hessian | 3/3 PASS |

Scope: these are internal algebraic/arithmetic self-checks (ghost-number bookkeeping,
finite-dim sign algebra, matrix elimination), NOT independent CFT-level re-derivations.
Ledger results R1–R14 are inputs, quoted by ID.

Compile: `pdflatex ×3 + biber` in `knowledge/`; clean, 14 pp, 0 undefined citations,
0 undefined references.

---

## 10. Open items carried honestly (per brief)

- ω_k graded-symmetry proven only k=2 (R12); k≥3 expected, unchecked.
- A2 carve-outs: CFT-level analytics of V₄⁻¹ on infinite-dim Sym² (spectral/
  Schwinger), kernel size of V₄|_{Sym²} (SL(2,C) sister-vertex numerics) — cited only.
- Kernel quotient Sym²H₀/ker V₄ (R13 / 2026-07-01 Annotation).
- note-Q1 status: ω₂^symp is a prerequisite of the "cyclic L_∞" framing, not obviated.
- Hq3 convention forks (λ phase; off-shell Σ reality) unresolved — presented, not chosen.
- CFL abstract degree d ↔ N_gh: no uniform offset for multi-output maps; d unpinned.

---

## Revision 1 (2026-07-02, applied by the orchestrator — Fable, author-revision)

Merged revision after **critic iter 1 (blind, Opus): REVISE, 0 Fatal / 2 Serious /
4 Concern / 3 Minor** (`agent/reports/critic-a3-ibl-pedagogical-20260702T150001.md`)
**plus the review comments of 2026-07-02**. A single critic iteration was budgeted;
no iter 2.

### Critic findings applied

- **S1 (Serious, the big one): N_gh(m₂) = +2, NOT −2.** Under the note's own out−in
  rule with ω₁ saturating at 5, Δ = ω₁⁻¹ is a ghost-5 bivector, so Δ-raising shifts
  N_gh by **+5** (not +1): N(m₂) = −3+5 = **+2**, N(p₁,₂,₀) = **+4**, N(p₁,₁,₁) =
  **+2** (balance-forced). Verified 4 independent ways in the script (Hq4-sat, new).
  Table 1, eq:Deltashift (new), all relation labels ((1,2,0): +5; (2,2,0): +3;
  (1,1,1): +3), the EOM ghost (6, saturating G₂ at 10 against δΣ), §5's even-parity
  remark, and the closed formula N(p_{k,ℓ,0}) = 3ℓ−2k all updated.
  **ERRATUM FLAG (pending author decision): the overview's boxed eq:mtwo carries −2**
  (justified by a balance argument inconsistent with the G₂ saturation); overview is
  FINAL, NOT edited — flagged via draftcomment in §3.2 and in the state
  file. Ledger R7/R8 content unaffected (neither uses the label).
- **S2: CFL Thm 1.3/6.1 misattribution fixed.** New §2.3 paragraph: Thm 1.3/6.1 =
  minimal-model transfer to Q-homology (NOT strictification, NOT the Σ-elimination);
  the Σ-elimination = transfer across the contractible pair along a chain homotopy
  equivalence (CFL Cor 6.2), Ψ kept off-shell, **conditional on R9** (m₂ injective)
  + bounded V₄⁻¹ (R10/R15) — hypotheses now stated.
- **C1:** gauge ghost arithmetic fixed (δΨ at 2, δΣ at 4; gauge variations preserve
  N_gh; "one gauge unit" gloss dropped). **C2:** script no longer only hard-codes:
  Hq4-sat derives every absolute N_gh from saturations (would have caught S1);
  21/21 PASS (was 15/15). **C3:** φ₁ = inclusion, φ₂ = ·⊗² into Sym²; morphism
  relations flagged unproved. **C4:** overlap normalisation fixed in Conventions
  (see review comment 9). **M1:** abstract cyclicity scoped to the BV presentation.
  **M2:** two-ℏ footnote in outlook. **M3:** eq:iblaction scoped (schematic, DC5).

### Review comments applied (2026-07-02)

1. **The earlier claim that the dictionary is the classical L∞⇔IBL correspondence was withdrawn** (abstract,
   intro, §2.3 rewritten + retitled). No such correspondence is a theorem;
   establishing one is a project goal. §2.3 now separates: established O(g_s²)
   facts; **candidate correspondence 1 (restricted/HS)** — open core: whether
   m₂ = Δ∘ℓ₃ satisfies the IBL relations (esp. (2,2,0)) given the L∞ relations —
   NOT verified, now flagged everywhere (also §3.4); **candidate correspondence 2
   (general/repackaging)** — p_{n−1,2} = Δ∘ℓ_n, iterate ⇒ {p_{m,n}} from ℓ_n alone;
   do L∞ relations imply IBL? plus the reverse question on ⊕_n Sym^n H₀.
2. §2.3 title fixed (was "The dictionary is the classical correspondence").
3. CFL Thm 6.1 explained properly (= S2; explicitly NOT strictification).
4. **"IBL on the single-string space" CORRECTED** (abstract, intro (a), §2.1): the
   IBL algebra lives on S(H₀); master field Ψ = Σ_n Ψ_n, Σ ≡ Ψ₂ (MS coderivation
   expansion, 1109.4101 §IV.B, new eq:masterfield).
5. §2.4 expanded: "Everything is CFT data" paragraph — complete list of CFT inputs;
   the shift changes no correlator, only the bookkeeping parity declaration.
6. Q-exactness → contact mechanism spelled out (§3.4, new eq:Qexact + two-mechanism
   enumeration: dynamical (established: no Q_B kinetic term, V₄⁻¹ pole/modulus-free,
   R14/R15) vs homological (interpretive; conditional on the open (2,2,0)
   verification)). Precise statement: the COMPOSITE is Q-exact, m₂ is the homotopy.
7. Σ‡ = Σ recorded as **confirmed** (decision of 2026-07-02); reality fork (ii) closed.
8. **Gauge-tower question added** (§6, open): general IBL gauge parameter tower
   Λ = Σ_{n≥0} Λ_n; is the HS form the gauge-fixed version of a theory with an
   independent two-string Λ₁?
9. **Normalisation adopted: ⟨c₋₁c̄₋₁c₀⁻c₀⁺c₁c̄₁⟩ = −1/2** (Harold's convention;
   Zwiebach −1; no factor of i, hep-th/9206084 (2.31)) — stated in Conventions,
   used in §3 saturations and §7 reality (fork (i) closed: λ = 1).

Compile: pdflatex + biber + pdflatex ×2, clean, **17 pp**, 0 undefined citations/
references. Script: `codes/verify-a3-ibl-pedagogical.py` **21/21 PASS** (executed).

**Status: critic loop closed at the single-iteration cap.** The S1 ledger/overview
erratum is the one item escalated to the author.
