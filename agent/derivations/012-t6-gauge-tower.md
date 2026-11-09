# Derivation 012 — T6: the gauge tower and the gauge-fixing question

- **Task:** T6 (`plans/remaining-o-gs2-tasks-2026-07-03.md`), open question
  (2026-07-02, A3 note §Gauge, "The gauge tower, and a gauge-fixing question"):
  *can the IBL form obtained after HS be interpreted as the gauge-fixed version of a
  theory with an independent two-string parameter Λ₁ ∈ Sym²H₀ — the composite law
  being what survives of the Λ₁-symmetry after fixing it?*
- **Author:** Claude Fable 5, inline, session 2026-07-03.
- **Machine checks:** `codes/verify-b1-quintic.py` checks (6), (7), (8) — executed,
  PASS (Route C flat directions; Stückelberg identity; ghost saturation arithmetic).
- **Status:** feasibility analysis; sharp parts = **R18**. Blind critic pass DONE
  (`agent/reports/critic-t6-gauge-tower-20260704T091730.md`, 2026-07-04): 0 Fatal, 2 Serious
  (both *scope of the negative verdict*, not algebra — all saturation arithmetic hand-verified
  correct). **Revised 2026-07-05** (author-revision, inline) per that report: §0/§1/§7 verdict
  language narrowed from "No hidden Λ₁" to "no *Q̂-raising* diagonal kinetic term / no unfixed
  flat direction"; can-vs-need framing added; §5 rescoped. The three **T6-bis flags** (relax
  the constraint on Σ; the Σ_full = Σ↓ + c₀Σ↑ route vs the ad-hoc Π-partner) are recorded for
  the Fable follow-up, not resolved here.
- **Conventions:** physical N_gh; ω₁ saturation N_gh(A)+N_gh(B) = 5 (⟨…⟩ = 6 with the
  c₀⁻ insertion); ω₂ = ω₁⊗² saturation 10; N_gh(m₂) = +2 (erratum-fixed); Λ₀ at
  N_gh 1, candidate Λ₁ at N_gh 3 (one unit below Σ's 4).

---

## 0. Answer in one paragraph

**Framing (which question is being answered).** Two distinct questions are in play and
must not be conflated. **(Q-can)** *Can* the HS theory be presented as the gauge fixing
of a theory with an independent two-string parameter Λ₁ (for a simpler parametrization
or new effects)? **(Q-need)** Is such an independent Λ₁ ever *needed* to reproduce the
physics? The question addressed is **(Q-can)**. This note answers **(Q-can) affirmatively**
(§3 trivially, §4 conditionally-nontrivially) and **(Q-need) negatively** (§1, §2, §6).
The negative results below bear on (Q-need); they do **not** close (Q-can) — indeed the
same-saturation, non-Q̂ enhancement that would realize (Q-can) inside the (Ψ,Σ) content
is *not* excluded here and is the subject of **T6-bis**.

**Within the HS field content (Ψ, Σ):** there is **no diagonal *Q̂-raising* kinetic term
for Σ** (§1a: ghost saturation kills ω₂(Σ, Q̂Σ)), and the actual kinetic operator V₄ has
**no unfixed flat directions beyond ker V₄** (§1b) — the kernel shifts being the one
*genuine* (but trivial, decoupled-zero-mode) two-string gauge symmetry of S_HS, with the
R13 quotient as its gauge fixing (§2). **This is weaker than "no hidden Λ₁":** it does
*not* exclude S_HS being the gauge-fixed form of an enlarged theory whose kinetic term is
a *same-saturation, non-Q̂* enhancement K = V₄ + ΔK (the closed analog of the open-SFT
c₀L₀ → Q_B enhancement, ΔK killed by a gauge + Gauss constraint) — cf. R6 (m₂ is Q-exact)
and R11 ((X, X⁺) a contractible pair), which are the textbook signature of a sector that
already *looks* gauge-fixed. That possibility is left open (T6-bis). **With enlarged field
content the answer to (Q-can) is YES, in two forms:**
a trivial one (§3, Stückelberg — always available, no new physics) and a nontrivial
conditional candidate (§4: a ghost-5 partner Π with cross-kinetic term ⟨Π, Q̂X⟩, where
the Λ₁-variation closes at leading order via δΠ ∝ m₂(Λ₁) and the residual anomaly is
a geometric-master-equation boundary term — and where **m₂-invertibility (R9)
reappears in a new role: as the condition that Π can be gauged away**, i.e. that the
gauge choice recovering S_HS is admissible). Route C is **not** the enlargement: its
multiplier sector has no flat directions at all (§5, machine-checked). The B1 result
(derivation 011 §4) supports the "no independent Λ₁ is ever *needed*" reading at the
next order: the deviation X̃ transforms homogeneously, so the tower extension keeps
pulling back the Ψ-gauge structure rather than generating new parameters (§6).

---

## 1. No *Q̂-raising* kinetic term, and no unfixed flat direction, inside S_HS

**(a) Ghost-number saturation forbids a diagonal *Q̂-raising* kinetic term.** An
independent transformation δΣ = Q̂Λ₁ + … can only be a symmetry supported by a kinetic
term whose Q̂-exact directions are flat, i.e. a term ω₂(Σ, Q̂Σ)-type. But ω₂ saturates
at total N_gh = 10, while N_gh(Σ) + N_gh(Q̂Σ) = 4 + 5 = 9 ≠ 10: **ω₂(Σ, Q̂Σ) ≡ 0
identically** (script check 8). No closed two-string bilocal at the physical ghost
number can carry a diagonal Q̂-kinetic term. *Contrast with the open-stub precedent
(C9ETB6WE):* the open-string auxiliary sits at N_gh 1 with ω-saturation 3, and
1+1+1 = 3 — the diagonal Q-kinetic term saturates, which is exactly why the open-stub Σ
has its own gauge parameter (Λ₂ there) and the closed HS Σ cannot. The open-stub
mechanism generalizes to the closed string **only in off-diagonal form** (a partner at
ghost 5; §4). **Scope (critic S2 / T6-bis):** this rules out only the *Q̂-raising*
diagonal term. It does **not** rule out a *same-saturation, non-Q̂* enhancement
K = V₄ + ΔK (total N_gh 10, e.g. an m₂-type or higher-ℓ dressing), which is precisely
the closed analog of the open-SFT c₀L₀ → Q_B enhancement; note the
physical Σ-kinetic term V₄ = ω₂(m₂Σ, Σ) is *itself* m₂-type (raising by 2), not Q̂-type,
so the Q̂-saturation count does not speak to that enhancement at all. Left open (T6-bis).

**(b) The actual kinetic operator has no unfixed flat directions — but this does not
exclude a gauge-fixed interpretation.** On the R13 quotient Sym²H₀/ker V₄ the Σ-kinetic
form V₄ is injective (R9/R13); off the quotient the flat directions are exactly ker V₄
(§2). **Correction (critic S1):** invertibility of V₄ establishes only that S_HS has no
*unfixed* flat Σ-directions beyond ker V₄ — it does **not** discriminate "no gauge
structure" from "*already gauge-fixed*", because gauge-fixed kinetic operators are
invertible *by construction* (the Siegel-gauge operator c₀L₀ = {Q_B, b₀} is invertible
on the gauge slice and Q-exact). In fact the project's own ledger reads the other way:
**R6** records the Σ-kinetic operator m₂ (V₄(Σ,Σ) = ω₂(m₂Σ, Σ)) is **Q-exact**
(m₂ = −[Q, p₂,₂,₀]), and **R11** records that (X, X⁺) is a **contractible pair**
(Henneaux auxiliary-field theorems). A Q-exact, invertible kinetic operator forming a
contractible pair is the textbook signature of an *already gauge-fixed / auxiliary*
sector — i.e. these facts are *compatible with* S_HS being the gauge fixing of an
enlarged theory, not evidence against it.

Hence the composite law is the pullback of the Ψ-gauge structure to the Σ-branch (R11;
strengthened at O(g_s³) by derivation 011 §4), and no *independent* Λ₁ is *needed*
within (Ψ, Σ) (Q-need). Whether S_HS is *additionally* the gauge fixing of a
same-saturation enhanced theory (Q-can) is **not settled here** — it is the open
T6-bis question.

## 2. The genuine two-string symmetry of S_HS: kernel shifts, and the quotient as their gauge fixing

S_HS *does* have a two-string-parameter gauge symmetry: the kernel shifts
δΣ = Ξ, Ξ ∈ ker(V₄|_{Sym²}) (R11's "residual freedom"; R13's decoupling). This is an
ultralocal shift symmetry — parameter a full field Ξ ∈ ker V₄, no derivatives, no Q̂.
Under it S_HS is exactly invariant (Ξ appears in neither the kinetic nor the source
term — R13). The R13 prescription "define Σ ∈ Sym²H₀/ker V₄" **is precisely the gauge
fixing of this symmetry** (pick one representative per orbit). So there is a genuine but
**trivial** (decoupled zero-mode) two-string gauge symmetry already inside S_HS: *the
kernel-shift tower, with the quotient as its fixing.* What it is not: a Q̂Λ₁-type
transformation with the IBL structure maps acting on the parameter — so it is **not** the
enlargement answering (Q-can) (an ultralocal shift of a decoupled spectator, not an
IBL-structure-map Λ₁-tower).

## 3. Trivial enlargement: Stückelberg dressing (always possible)

Define S̃[Ψ, Σ, B] := S_HS[Ψ, Σ − Q̂B] with a new field B ∈ Sym²H₀ at N_gh 3
(Grassmann-odd), and

δΣ = Q̂Λ₁ (+ composite law), δB = Λ₁, N_gh(Λ₁) = 3.

This is exactly invariant by construction (script check 7, exact to machine
precision), and the gauge B = 0 recovers S_HS with residual transformations those
preserving B = 0, i.e. Λ₁ = 0: **only the composite law survives** — the
scenario of the question, realized literally. But the enlargement is a field redefinition dressing: B
enters only through Σ − Q̂B, carries no dynamics, and the "tower" acts as a pure shift
on B. Verdict: the literal answer to the question is *yes, trivially*; the question
with content is whether a **natural** enlargement exists whose Λ₁ acts through the IBL
structure maps. That is §4.

## 4. Nontrivial candidate: the ghost-5 partner Π and the constraint ⟨Π, Q̂X⟩

Saturation fixes the partner: a cross-kinetic term ⟨Π, Q̂Σ⟩-type needs
N_gh(Π) = 10 − (4+1) = 5 (script check 8). Take Π ∈ Sym²H₀ at N_gh 5 (odd) and

$$
\tilde S[\Psi,\Sigma,\Pi] = S_{\rm HS} + \big\langle \Pi,\, \hat Q X\big\rangle_{\omega_2},
\qquad X=\Sigma-\Psi^{\otimes2},\quad \hat Q=Q\otimes1+1\otimes Q .
\tag{T.1}
$$

**Leading-order Λ₁-variation.** With δΣ = Q̂Λ₁ (so δX = Q̂Λ₁), δΨ = 0:

$$
\delta\tilde S = -\tfrac{2g_s^2}{4!}\,V_4(\hat Q\Lambda_1, X)
+ \langle\delta\Pi, \hat QX\rangle
+ \underbrace{\langle\Pi,\hat Q\hat Q\Lambda_1\rangle}_{=0}.
\tag{T.2}
$$

Move Q̂ across V₄ and define the **master-equation anomaly**
𝒜(Λ₁,X) := V₄(Q̂Λ₁,X) + V₄(Λ₁,Q̂X); by the geometric master equation
(∂V₀,₄ = V₃∘V₃ plumbing), 𝒜 is the V₃∘V₃ boundary bilinear — nonzero, but *known*.
Since V₄(Λ₁,·) = ω₂(m₂(Λ₁),·) (m₂ = Δ∘ℓ₃, the A3/R16 machinery; ghost check:
N_gh(m₂(Λ₁)) = 3+2 = 5 = N_gh(Π), parity odd = Π ✓, script check 8), the choice

$$
\delta\Pi = -\tfrac{2g_s^2}{4!}\, m_2(\Lambda_1) + O(g_s^3)
\tag{T.3}
$$

cancels the V₄(Λ₁,Q̂X) piece, leaving δS̃ = −(2g_s²/4!)·𝒜(Λ₁,X): the obstruction is
**purely the boundary term of the geometric master equation**. Cure (conjectured, not
verified): covariantize the constraint, Q̂ → 𝒬_Ψ := Q̂ + g_s[ℓ₂(Ψ,·)⊗1 + 1⊗ℓ₂(Ψ,·)] +
(g_s²/2)[ℓ₃(Ψ²,·)⊗1 + …] — the strand-wise linearized gauge operator — whose
curvature/variation produces exactly V₃∘V₃-type terms; closure order by order should
then follow from the L∞ relations. **This is the one genuinely open computation of
T6** (machine-checkable with a lemma-based toy à la R16 — listed as an Opus side
task).

**Why this candidate is interesting, if it closes:**

1. *Gauge-fixing recovers S_HS:* fixing Λ₁ by the gauge Π = 0 gives back exactly
   S_HS. Residual transformations preserve Π = 0: by (T.3), Λ₁ ∈ ker m₂ = 0 on the
   quotient — **the surviving symmetry is exactly the composite law**, the
   scenario of the question nontrivially realized.
2. *m₂-invertibility in a new role:* the gauge Π = 0 is admissible iff Π is pure
   gauge, i.e. iff m₂ is surjective onto the ghost-5 Sym² sector — R9's invertibility
   reappears as a **gauge-fixability condition** rather than an auxiliarity condition.
3. *Equivalence (tree-level):* integrating Π out imposes Q̂X = 0, restricting the
   X-integral to ker Q̂; the classical saddle X = 0 lies in ker Q̂, so **tree-level
   (g = 0) matching survives** and the effective theory is the same (with the same
   regularity carve-outs as R10 route (B)). *Caveat (critic C4):* the Gaussian
   *fluctuation determinant* is then taken over ker Q̂ here vs over all of Sym²H₀ in
   S_HS — these differ in general, so the "same effective theory" claim is tree-level;
   the ker Q̂-restricted vs full determinant is an open one-loop/quantum-tower item.
4. *Structural dichotomy with the open string made precise:* the open-stub
   two-parameter structure transplants to the closed string only in this
   off-diagonal (Π-partner) form — the diagonal form is ghost-forbidden (§1a).

**Honest caveats:** (i) the covariantization closure is unverified (the anomaly is
computed only at leading order); (ii) (T.1) is a *different presentation*, not an
un-gauge-fixing of S_HS discovered inside it; (iii) reality/BV treatment of the odd
ghost-5 Π not set up.

## 5. Route C is NOT the enlargement (negative check, machine-verified)

T6's approach sketch (a) suggested the Route C multiplier sector might carry a natural
two-string gauge invariance. It does not: the (σ, λ) sector's kinetic structure is the
off-diagonal pairing with constraint Jacobian

$$
\frac{\partial(\text{constraints})}{\partial(\sigma_2,\sigma_3,\sigma_4)}
=\begin{pmatrix}\mathbb1&0&0\\ -(\cdot\otimes\Psi)&\mathbb1&0\\ 0&-(\cdot\otimes\Psi)&\mathbb1\end{pmatrix}
$$

— unit-triangular, hence invertible **for every Ψ** (det = 1; script check 6:
σ_min > 0). No flat directions ⇒ **no *independent* gauge parameter** acting through
Q̂ on the multiplier tower: the specific *ghost-raising* transformation δσ₂ = Q̂Λ₁
cannot be compensated (the ⟨λ₂, Q̂Λ₁⟩ variation has no partner — λ₂ appears nowhere
else). **Scope (critic C1):** this is the same distinction as §1 — absence of flat
directions rules out an *independent* Q̂-acting parameter, not a gauge-fixed
presentation; what §5 establishes is "Route C carries no independent Λ₁", not "Route C
admits no enlargement". Route C's λ-tower is conjugate to the constraints, not to gauge
parameters. (This *sharpens* R13's OPEN item "gauge/BV structure": the gauge algebra
of S_C is the Ψ-gauge algebra pulled back to the constraint surface — composite laws
δσ_k = δ(Ψ^{⊗k}) + EOM-trivial + multiplier compensations — with no independent
parameters. The explicit λ-compensations remain to be written: B2 leftover.)

## 6. The tower reading, and what the IBL formalism actually provides

Two clarifications that dissolve the remaining mystique of the "tower of independent
parameters Λ = ΣΛ_n":

- **The natural classical L∞ candidate is not a symmetry.** δΨ = g_s ℓ₂(Λ₁)
  (the p₂,₁,₀-component of p̂(Λ₁, e^Ψ)) does not preserve S_eff:
  δS_eff = ω₁(EOM_Ψ, g_sℓ₂(Λ₁)) ≠ 0 off-shell. *(Caveat, critic C2: this one-line test
  fails for almost any δΨ, so it refutes only this specific candidate; the universal
  statement "the classical action admits no Λ₁-symmetry" rests on the quantum/loop-BV
  attribution below, not on this computation.)* The full tower is a symmetry structure
  of the **quantum/loop BV master action** on S(H₀) (Münster–Sachs), where the cobracket
  and higher-genus terms are present — not of the classical g = 0 action. At tree level
  and O(g_s²)–O(g_s³) there is (Q-need) no need for an independent Λ₁ acting nontrivially,
  in *either* presentation of the theory.
- **The B1 evidence (derivation 011 §4):** at O(g_s³) the corrected composite law is
  δΣ = δ(Σ_*(Ψ)) + homogeneous rotation of X̃ — the deviation transforms
  homogeneously, no inhomogeneous Q̂Λ₁ piece is generated by the tower step. The
  pattern conjecture (Phase B, all orders): *at every order of Route B the gauge
  algebra of the cubicized theory is the original Ψ-gauge algebra, with
  δΣ_k = δ(perturbative saddle) + homogeneous deviation terms; independent parameters
  never appear.* If instead one **wants** the enlarged home with independent Λ_n (as
  the natural habitat of the all-orders/quantum construction), the Π-partner
  construction of §4 is the candidate mechanism, and its per-order cost is one
  ghost-(2k+1) partner field per Σ_k.

## 7. Verdict

The question "is the HS theory a partial gauge fixing of a Λ₁-theory?" splits. Recall the
two readings: **(Q-can)** can it be *presented* as such? — the question as posed; **(Q-need)**
is an independent Λ₁ *needed*?

| reading | answer | where |
|---|---|---|
| *Q̂-raising* diagonal kinetic term for Σ inside S_HS | **No** (ghost saturation 9≠10) | §1a |
| unfixed flat direction of V₄ (beyond ker V₄) | **No** (invertible on quotient) — but this does *not* exclude an *already-gauge-fixed* reading (R6/R11) | §1b |
| same-saturation *non-Q̂* enhancement K = V₄+ΔK inside (Ψ,Σ) | **OPEN — not excluded** (the closed analog of c₀L₀→Q_B); the (Q-can) crux | §1a, **T6-bis** |
| two-string gauge symmetry of S_HS at all | **Yes but trivial: kernel shifts** (decoupled zero modes); R13 quotient = its gauge fixing | §2 |
| enlarged theory, trivial | **Yes** (Stückelberg; residual = composite law exactly) | §3 |
| enlarged theory, natural (Π-partner) | **Conditionally yes**: Π-partner + covariantized constraint; m₂-invertibility = gauge-fixability; anomaly = master-eq boundary term (closure open, ST2) | §4 |
| Route C as the enlargement | **No independent parameter** (no flat directions; not "no enlargement") | §5 |
| does the all-orders home *need* Λ₁? (Q-need) | Evidence says no (B1 homogeneous law); Π-tower available if wanted | §6 |

**Net:** (Q-need) is answered **no** (§1–§2, §6); (Q-can) is answered **yes** with enlarged
content (§3–§4) and remains **open** *within* the (Ψ,Σ) content via a same-saturation non-Q̂
enhancement — the T6-bis lead. The earlier "No hidden Λ₁, now an argument" headline is
**narrowed** to "no Q̂-raising kinetic term / no unfixed flat direction".

**Open:** (i) **T6-bis** — the same-saturation, non-Q̂ enhancement K = V₄ + ΔK, and the
Σ_full = Σ↓ + (c₀-dir)Σ↑ (Siegel-gauge Σ↑ = 0) reading of the Π-partner as the up-component
of an *unconstrained* two-string field (relax the constraint on Σ, rather than add an ad-hoc
Π); start from R6 (m₂ Q-exact) + R11 (contractible pair) as evidence the Σ-sector is already
in gauge-fixed form. *This is the constructive Fable follow-up, not resolved here.* (ii)
covariantization closure of §4 (lemma-based toy — ST2); (iii) BV/antifield treatment of the
Π-theory and of the homogeneous X̃-term (011 §4 — ST4); (iv) explicit λ-compensation laws for
Route C (B2 leftover — ST5); (v) the quantum-tower statement (Münster–Sachs loop master
action) — Phase B/quantum.
