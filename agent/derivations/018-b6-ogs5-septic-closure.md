# Derivation 018 — B6: the O(g_s⁵) septic closure and the merger of the schemes

- **Task:** the O(g_s⁵) closure, settled before the all-orders formulation (order
  chosen in the plan) — decide the scheme-A (3,2,2) vs scheme-B (3,3,1)
  odd-coupling menu at order n = 7 and test the tower expectation
  Σ_n ↔ (V_{2n}, V_{2n+1}).
- **Author:** Claude Fable 5, inline (no delegation), session 2026-07-07 (post-Fable
  resume session).
- **Machine check:** `codes/verify-b6-ogs5-septic.py` — **8/8 PASS (executed
  2026-07-07, two seeds: default 20260707 and 41)**.
- **Status:** **R25 — blind critic pass DONE 2026-07-08 (Opus, ST9): ACCEPT, 0
  Fatal/0 Serious** (report `agent/reports/critic-b6-ogs5-20260708T210500.md`). The
  critic hand-re-derived the full chain: 𝔽^dr closed form (all five coefficients),
  A₅^dr and the A₅^min strand re-symmetrisation sym 𝒞(V₄⁻¹v,P,P) = (1/3)(2S₁+S₃),
  the forced (42/25, −14/5) via 7!/600 = 8.4, the running-kernel identity −6g/25
  (sign included), and the scheme-A power counting. Author-edits applied per its 3
  Concerns/2 Minors: check 6 relabelled bookkeeping (§0.5(a), §8, script);
  "distinction dissolves" and "tower CONFIRMED" scoped inline (§0.4, §0.5, §9);
  script check 7 δY₂-leg nonzero guard + genuine homogeneity test (re-run 8/8 PASS,
  two seeds); Veronese-null scope + A₅^dr M̃⁻¹-independence noted (§2).
- **Terminology:** the project terms of art used below (*forced*,
  *dressed*, *feedback*, *running kernel*, *Veronese diagonal*, *strand-local*,
  *sequential exact Gaussianity*) are NOT standard SFT vocabulary; they are defined in
  standard matching/EFT language in the note's glossary,
  `knowledge/cubic-sft-ibl-pedagogical.tex` §sec:intro:glossary.
- **Inputs reused (not re-derived):** R1 (eq:SHS), R7 (physical grading), R9/R20
  (auxiliarity ⟺ kernel non-degeneracy), R12 (counting: Σ₃ first forced at
  V₇ = 3+2+2), R15 (two-coloured grading, moduli-free Σ-propagators), R17 (011:
  quintic, K_Ψ = V₄ − (g/5)W), R19 (013: W₆ = V₆ − (6/5)𝒞, minimal-scheme A₅,
  master-equation-agnostic matching), R21 (015: Φ-map, M̃ = M − (6/5)N,
  ũ = u − (6/5)ΦᵀV₄⁻¹v(Σ₂), collapse ũ(P) = M̃p₃, δY₃ = 0 at O(g_s⁴)), R22 (016:
  BV class of the homogeneous laws).
- **Conventions:** physical N_gh (Ψ:2, Σ₂:4, Σ₃:6, all even); finite-dimensional
  binding for the algebraic layer exactly as R14/R17/R19/R21 (CFT-level analytics of
  V₄⁻¹, M̃⁻¹ and the composite kernels = A2(iii)/T4 carve-out); e^S weight; V₄…V₇
  generic totally symmetric tensors (no L∞ input anywhere — the matching is
  master-equation-agnostic, R19 §7, and stays so here).

Notation: P := Ψ⊗², p₃ := Ψ⊗³, X := Σ₂ − P; v := V₅(·,P,Ψ), W := V₅(·,·,Ψ) (both on
Sym²); g₆ := V₆(Ψ⊗⁴,·)|_{Sym²}; Φ : Sym³ → (Sym²)*, Φ(A) := V₅(·,A) (R21 §2);
L̃ := ∂ũ/∂Σ₂ (the linear map Sym² → (Sym³)*, L̃X = V₆(·,X,Ψ) − (6/5)ΦᵀV₄⁻¹V₅(·,X,Ψ)).

---

## 0. Executive summary

**Order g_s⁵ closes, and it closes in a way that settles the menu question:**

1. **The dressed action is sequentially exactly Gaussian (§1) — new structural
   theorem.** In S_dr (R21) each auxiliary appears at most quadratically, with a
   triangular source pattern (Σ₃ sourced linearly by Σ₂, Σ₂ sourced by Ψ). So the
   elimination Σ₃-then-Σ₂ is a chain of *exact* Gaussians and the full feedback has
   the closed form (identity in g, no order-by-order expansion)
   $$ \mathbb F^{\rm dr}(g)
      = \frac{g^4}{600}\Big\{\big[v+\tfrac g6\tilde w\big]^{\!\top}\hat K^{-1}
        \big[v+\tfrac g6\tilde w\big] - v^\top V_4^{-1}v\Big\},\qquad
      \tilde w = \tilde L^\top \tilde M^{-1}\tilde u(P),\quad
      \hat K = V_4-\tfrac g5 W-\tfrac{g^2}{30}\tilde L^\top\tilde M^{-1}\tilde L. $$
   (Check 1a: closed form = joint Newton saddle at finite g to 1e-18.) This
   property propagates: the scheme-B ansatz eq:Sdrallorders is sequentially
   Gaussian at **every** order (§6), so its all-orders closure reduces to one
   diagonal condition per order — the recursion is mechanical.

2. **The dressed O(g_s⁵) feedback (§2), explicit (015 only said "O(g_s⁵)"):**
   $$ A_5^{\rm dr} = \frac1{600}\Big[\tfrac13 S_2 - \tfrac15 S_1\Big],\qquad
      S_1 := vV_4^{-1}WV_4^{-1}v,\quad S_2 := g_6^\top V_4^{-1}v, $$
   i.e. a three-V₅ chain and a V₆–V₄⁻¹–V₅ chain — both **strand-local** (no
   strand-split structure). Contrast the minimal (Σ₂-only) scheme's
   A₅ = (1/600)[½S₂ − ⅕S₁ − ⅕S₃] (013 check 2 re-expressed; corroborated here,
   check 5), which contains the **strand-split** three-V₅ chain
   S₃ := 𝒞(P,P,V₄⁻¹v). Note the sign flip of the S₁ term between presentations.

3. **Closure at O(g_s⁵) (§3):** the single scheme-B odd coupling at partition
   (3,3,1),
   $$ \boxed{\;\frac{g^5}{7!}\,\tilde V_7(\Sigma_3,\Sigma_3,\Psi),\qquad
      \tilde V_7 := V_7\big|_{331} + \tfrac{42}{25}\,\tilde A_{S_1}
      - \tfrac{14}{5}\,\tilde A_{S_2},\;} $$
   with the strand-local composite kernels
   $$ \tilde A_{S_1}(A,B,\psi) := \Phi(A)^\top V_4^{-1}\,V_5(\cdot,\cdot,\psi)\,
      V_4^{-1}\Phi(B),\qquad
      \tilde A_{S_2}(A,B,\psi) := \mathrm{sym}_{AB}\,
      V_6\big(A,\psi,V_4^{-1}\Phi(B)\big), $$
   closes order 7 **exactly**: S(saddles) − S_eff⁽⁷⁾ = O(g_s⁶) (check 2, residual
   log-slope 6.013, lower orders intact). The three coefficients (1, 42/25, −14/5)
   are **forced** given the independence of {V₇(Ψ⁷), S₁, S₂} as functions of Ψ
   (checks 0, 3); the bare geometric V₇ alone leaves exactly A₅^dr — dressing is
   forced, as at n = 6.

4. **The running-vertex rule extends verbatim — the tower expectation
   CONFIRMED (§4).** Ṽ₇ = the deficit vertex V_{7,eff}|₍₃,₃,₁₎ (V₇ minus 7!× the
   O(g_s⁵) feedback composites), and the S₁-part of the forced dressing is exactly
   the O(g) Taylor term of the **running kinetic dressing**: in the Σ₃-kinetic,
   Ṽ₇ enters as M̂ = M̃ − (g/7)Ṽ₇(·,·,Ψ), whose ΦᵀV₄⁻¹WV₄⁻¹Φ coefficient
   −(g/7)(42/25) = −(6/5)(g/5) is precisely the O(g) term of
   $$ M - \tfrac65\,\Phi^\top K_\Psi(g)^{-1}\Phi,\qquad K_\Psi = V_4 - \tfrac g5 W $$
   — i.e. the n = 6 dressing N = ΦᵀV₄⁻¹Φ was the g = 0 value of a running composite,
   and the O(g_s⁵) step is its first derivative. Σ₃ pairs with (Ṽ₆, Ṽ₇) exactly as
   Σ₂ paired with (V₄, V₅): **Σ_k ↔ (Ṽ_{2k}, Ṽ_{2k+1}) holds at k = 3** (at the
   finite-dimensional algebraic layer on generic tensors, as every matching
   statement in this series — the CFT-level status is the standing carve-out).

5. **The menu answer (§5): the partition choice is presentation freedom; the
   scheme distinction dissolves** (scope, critic C2: "dissolves" = the conjunction
   of (b) scheme-A-literal fails + the even Σ₃ HS pair is power-counting-forced,
   and (c) all odd partitions close identically; the one definitional step — that
   repairing scheme A by adding the forced even pair is the ONLY repair — is
   power-counting-forced within the §5 menu, not separately machine-tested).
   (a) *Power counting (check 6 — arithmetic bookkeeping of the counting, not an
   independent machine test):* the O(g_s⁵) coupling menu is exactly
   {(3,3,1), (3,2,2)} — everything else contaminates lower amplitudes or needs a
   Σ₄ whose only kinetic V₈(Σ₄,Σ₄) is O(g_s⁶), making an O(g_s⁵) Σ₄-source a
   divergent branch (Σ₄* ∼ g⁻¹, the R20 §1 argument one order up).
   (b) *Scheme A as literally specified FAILS (check 5):* "add the single balanced
   coupling W₇(Σ₃,Σ₂,Σ₂) at order 7" cannot work, because Σ₃ has no O(g_s⁴)
   source in scheme A, hence no O(1) saddle: its sector value scales as g⁶
   (log-slope 5.98) and the V₇(Ψ⁷) contact is **never produced** — the mismatch
   A₅^min − V₇(Ψ⁷)/7! is coupling- and kernel-independent. The Σ₃ HS pair at
   O(g_s⁴) (kinetic + source, scheme B's even pair) is **forced** before order 7
   can close. Scheme A must restructure its n = 6 sector; once it does, it *is* a
   member of the scheme-B family (up to the c₆-split of the sextic contact between
   W₆(Σ₂³) and the Σ₃-collapse, and up to the odd-partition choice below).
   (c) *Both partitions close (check 4):* with the strand-split (3,2,2) kernels
   B̃_{S₁}, B̃_{S₂} (the same two structures realized by splitting the strands of
   one Σ₂ slot across the composite blocks, 𝒞-style), (a₇,b₇) = (0,1) closes, and
   so does any mix a₇+b₇ = 1. Matching constrains only the symmetrized Veronese
   diagonal (one septic invariant) — the partition split is exactly the
   presentation/field-redefinition freedom class of 013 §3(c).
   (d) *Discriminators all favour (3,3,1):* (i) strand-locality — the (3,3,1)
   kernels need no strand-splitting, the (3,2,2) ones do; (ii) Gaussianity — the
   (3,3,1) coupling keeps the action quadratic in Σ₃ (kinetic dressing), while a
   (3,2,2) coupling makes the Σ₃-source quadratic in Σ₂, so after eliminating Σ₃
   the Σ₂-action acquires quartic terms and the sequential-Gaussian structure (and
   the closed-form 𝔽) is lost at the next order; (iii) uniformity — (3,3,1) is
   scheme B's Σ₃-odd member, matching the established k = 2 pattern.

6. **Gauge law at O(g_s⁵) (§7):** the (3,3,1) coupling makes the Σ₃-kinetic
   Ψ-dependent (M̂ = M̃ − (g/7)Ṽ₇(·,·,Ψ)), so R21's δY₃ = 0 was an **O(g_s⁴)
   accident**: the Σ₃-deviation now rotates like the Σ₂-one. Both laws are exact
   kernel rotations (fully explicit — not even implicit, since the dressed action
   is purely Gaussian in the deviations):
   $$ \delta Y_3 = -\tfrac12\hat M^{-1}(\delta\hat M)Y_3,\qquad
      \delta Y_2 = -\tfrac12\hat H^{-1}(\delta\hat H)Y_2, $$
   and with them δS − δ[S_eff⁽⁷⁾ + 𝔽₆] = 0 **exactly** (off-shell, arbitrary δΨ;
   all directional derivatives analytic, residual 1e-16; check 7). Dropping either
   rotation leaves exactly the predicted residual (falsification legs). Still
   homogeneous (δY ∝ Y), still no independent two-string parameter — R18's pattern
   at a fourth consecutive order; BV class as in R22 (field-dependent-kinetic
   corner for both sectors now).

---

## 1. Sequential exact Gaussianity of the dressed action

The R21 dressed action (natural normalisation (a,b) = (1,2); shared ½V₂ + g_sV₃/3!
suppressed throughout):

$$ S_{\rm dr} = -\frac{g^2}{4!}V_4(\Sigma_2,\Sigma_2) + \frac{2g^2}{4!}V_4(\Sigma_2,P)
   + \frac{g^3}{5!}V_5(\Sigma_2,\Sigma_2,\Psi)
   + \frac{g^4}{6!}\big[-\tilde M(\Sigma_3,\Sigma_3) + 2\langle\tilde u(\Sigma_2),
   \Sigma_3\rangle\big]. $$

Σ₃ appears exactly quadratically with kinetic M̃ (Ψ- and Σ₂-independent) and source
linear in Σ₂. Eliminating it is an exact Gaussian:
Σ₃* = M̃⁻¹ũ(Σ₂), value (g⁴/6!)ũᵀM̃⁻¹ũ — **exactly quadratic in Σ₂** (ũ = L̃Σ₂
linear). The residual Σ₂-action is therefore exactly quadratic too (V₅ has only two
Σ₂ slots), and the second elimination is again exact. Expanding Σ₂ = P + X and using
the collapses ũ(P) = M̃p₃, ⟨L̃X,p₃⟩ = ⟨g₆,X⟩ − (6/5)vᵀV₄⁻¹WX (Lemma 2.1 of 015 plus
one line):

- contacts: (g²/4!)V₄(Ψ⁴) + (g³/5!)V₅(Ψ⁵) + (g⁴/6!)W̃₆(Ψ⁶), W̃₆(Ψ⁶) = V₆(Ψ⁶) −
  (6/5)vV₄⁻¹v (the deliberate deficit −g⁴vV₄⁻¹v/600 vs the target);
- quadratic form −(g²/4!)K̂(X,X), K̂ = V₄ − (g/5)W − (g²/30)Q̃, Q̃ := L̃ᵀM̃⁻¹L̃;
- linear term ⟨b,X⟩, b = (g³/60)[v + (g/6)w̃], w̃ := L̃ᵀM̃⁻¹ũ(P) = g₆ − (6/5)WV₄⁻¹v.

Completing the (exact) square:

$$ \boxed{\;\mathbb F^{\rm dr}(g) := S_{\rm dr}(\text{saddles}) - S^{(6)}_{\rm eff}
   = \frac{g^4}{600}\Big\{[v+\tfrac g6\tilde w]^\top\hat K^{-1}[v+\tfrac g6\tilde w]
     - v^\top V_4^{-1}v\Big\}\;} $$

**identically in g** (given invertibility of M̃ and K̂ — the auxiliarity conditions,
CFT-open as always). No cubic remainder, no order-by-order bookkeeping: the entire
feedback tower of the dressed presentation is this one rational function of g.
Check 1a: equals the independent joint Newton saddle solve at g = 0.25 to 1.5e-18.
(Contrast 013 §4: the minimal scheme's W₆(Σ₂³) coupling is cubic in Σ₂, so its square
never completes exactly and the rewriting carries a T(X³) remainder.)

## 2. The O(g_s⁵) feedback

Expanding 𝔽^dr to first order (K̂⁻¹ = V₄⁻¹ + (g/5)V₄⁻¹WV₄⁻¹ + O(g²); the Q̃-term
enters at O(g⁶)):

$$ \mathbb F^{\rm dr} = g^5 A_5^{\rm dr} + O(g^6),\qquad
   A_5^{\rm dr} = \frac1{600}\Big[\tfrac15\,S_1 + \tfrac13\,v^\top V_4^{-1}\tilde w\Big]
   = \frac1{600}\Big[\tfrac13 S_2 - \tfrac15 S_1\Big], $$

using vᵀV₄⁻¹w̃ = S₂ − (6/5)S₁. Check 1b: Richardson extrapolation of the closed
form reproduces this to 1e-8 relative. Two structures only, both strand-local
chains: S₁ = [V₅–V₄⁻¹–V₅–V₄⁻¹–V₅] (Ψ-count 3+1+3 = 7) and S₂ = [V₆–V₄⁻¹–V₅]
(4+3 = 7). Diagrammatically: S₁ = the three-V₅ Σ₂-exchange chain; S₂-and-S₁ mix =
the Σ₃-exchange with one Σ₂-leg off-shell dressed by a V₅ (the w̃-cross-term).

Comparison, minimal scheme (013): expanding 013's A₅ = (1/600)[½T(V₄⁻¹v,P,P) + ⅕S₁]
with T = sym(V₆ − (6/5)𝒞) gives A₅^min = (1/600)[½S₂ − ⅕S₁ − ⅕S₃],
S₃ := 𝒞(P,P,V₄⁻¹v) — the *strand-split* three-V₅ chain (the V₄⁻¹v inserted
strand-by-strand into the two V₅ blocks). Corroborated numerically (check 5, three
coupling configurations, all → A₅^min). The feedback is presentation-dependent, as
it must be; the dressed presentation's is simpler (no S₃, and rank 2 instead of 3
in the invariant basis {S₁,S₂,S₃}; independence of {V₇(Ψ⁷),S₁,S₂,S₃} = check 0).
Two scope notes (critic M2): A₅^dr happens to be M̃⁻¹-independent (w̃ and K̂ carry
no M̃ at this order), so check 1b does not exercise the dressed Σ₃-kinetic — that
enters first through the O(g⁶) term of 𝔽^dr; and "forced" throughout means forced
modulo the Veronese-diagonal-null presentation freedom (013 §3(c)), as stated in §3.

## 3. Closure at O(g_s⁵): the forced dressed (3,3,1) coupling

Admissible O(g_s⁵) additions (power counting, §5/check 6): cubic couplings with
7-strand on-shell footprint = a₇·(3,3,1) + b₇·(3,2,2) only. Adding
(g⁵/7!)[a₇Ã(Σ₃,Σ₃,Ψ) + b₇B̃(Σ₃,Σ₂,Σ₂)], the Σ₃-sector stays Gaussian with

$$ \hat M = \tilde M - \tfrac g7 a_7\,\tilde A(\cdot,\cdot,\Psi),\qquad
   \hat s = \tilde u(\Sigma_2) + \tfrac g{14} b_7\,\tilde B(\cdot,\Sigma_2,\Sigma_2), $$

and the on-shell O(g_s⁵) contribution of the new couplings is exactly the naive
contact (g⁵/7!)[a₇Ã(p₃,p₃,Ψ) + b₇B̃(p₃,P,P)] (the M̂⁻¹ and ŝ expansions each give
the 1/7 and 1/14 factors that restore 1/7!). Matching against
S_eff⁽⁷⁾ = S_eff⁽⁶⁾ + (g⁵/7!)V₇(Ψ⁷) requires the single diagonal condition

$$ a_7\tilde A(p_3,p_3,\Psi) + b_7\tilde B(p_3,P,P)
   = V_7(\Psi^7) - 7!\,A_5^{\rm dr}
   = V_7(\Psi^7) + \tfrac{42}{25}S_1 - \tfrac{14}{5}S_2 $$

(7!/600 = 8.4: 8.4/5 = 42/25, 8.4/3 = 14/5). The scheme-B member (a₇,b₇) = (1,0)
with the strand-local kernels boxed in §0 satisfies it; closure verified at
machine level (check 2: Richardson → 8.5e-12, residual slope 6.013, O(g⁴) matching
untouched). Forcing: {V₇(Ψ⁷), S₁, S₂} are independent functions of Ψ, so within the
kernel basis {V₇|₃₃₁, Ã_{S₁}, Ã_{S₂}} the coefficients (1, 42/25, −14/5) are pinned
— each perturbation leaves exactly δc·(invariant)/7! (check 3); the bare geometric
V₇ alone leaves exactly A₅^dr (dressing forced, the n = 6 lesson repeating).
Kernel uniqueness holds, as always, only up to Veronese-diagonal-null forms
(013 §3(c) presentation freedom).

## 4. The running-vertex structure (tower rule confirmed)

Two readings of the forced dressing, both exact:

**(a) Deficit vertex.** Ṽ₇'s diagonal = V₇(Ψ⁷) − 7!A₅^dr — the "n-th derivative of
the eliminated lower-order action" rule (eq:runningV, operational form) verbatim at
n = 7. Scheme B's uniform tower Σ_k ↔ (Ṽ_{2k}, Ṽ_{2k+1}) extends: the k = 3 triple
is (M̃-pair at n = 6, Ṽ₇ at n = 7), exactly as the k = 2 triple was (V₄-pair, V₅).

**(b) Running kernel.** In the Σ₃-kinetic the coupling appears as
M̂(g) = M̃ − (g/7)Ṽ₇(·,·,Ψ). Its Ã_{S₁}-part has coefficient −(g/7)(42/25) =
−(6/5)(g/5) — exactly the O(g) term of the **resummed** Φ-dressing

$$ M - \tfrac65\,\Phi^\top K_\Psi(g)^{-1}\Phi
   = M - \tfrac65\Phi^\top V_4^{-1}\Phi - \tfrac65\cdot\tfrac g5\,
     \Phi^\top V_4^{-1}WV_4^{-1}\Phi + O(g^2). $$

So R21's dressing N = ΦᵀV₄⁻¹Φ is the g = 0 value of the running composite
ΦᵀK_Ψ⁻¹Φ, and the O(g_s⁵) S₁-dressing is its first Taylor coefficient: the Σ₂
propagator inside the Σ₃-kinetic dressing runs with the Ψ-dressed kernel K_Ψ, as
it should. The Ã_{S₂}-part (+2g/5 in M̂) is the [V₆-source]–V₄⁻¹–Φ chain — the
Σ₂-exchange between the bare V₆ source-vertex and the V₅-pair-vertex, i.e. the
cross-running of u against Φ. "More composite, not more ad hoc": the one-line rule
generates both.

## 5. The menu: what is forced, what is free

- **Forced:** the Σ₃ HS pair at O(g_s⁴). Scheme A's literal rule (one balanced
  coupling per order, eq:schemeA) fails at n = 7: (i) on {Ψ,Σ₂} no cubic coupling
  reaches 7 strands (max 2+2+2); (ii) Σ₃'s only saturation-12 kinetic is
  V₆-type ⇒ O(g_s⁴); (iii) with no O(g_s⁴) source, Σ₃* = O(g) and the coupling's
  on-shell footprint is O(g⁶) — no V₇ contact at O(g_s⁵), for any kernel and
  coefficient (check 5: the deficit −V₇(Ψ⁷)/7! survives untouched across b₇ = 0,
  bare, dressed; sector value slope 5.98). Retrofitting the pair changes the n = 6
  contact bookkeeping (the R20 condition c₆ + b²/4a = 1), i.e. scheme A must merge
  into the scheme-B family. **The tower rule (introduce Σ_n for V_{2n} and
  V_{2n+1}, no order left without its Σ₃) is the structurally
  correct instinct: the even pair is forced, not stylistic.**
- **Free:** the partition of the odd coupling. (3,3,1), (3,2,2), and any
  a₇ + b₇ = 1 mix close identically (check 4) — matching sees only the symmetrized
  Veronese diagonal. The c₆-split at n = 6 (how much sextic contact sits in a
  W₆(Σ₂³) vertex vs the Σ₃-collapse) is the same kind of freedom.
- **Canonical choice:** (3,3,1) with strand-local kernels — by strand-locality
  (the (3,2,2) realizations of S₁, S₂ require 𝒞-style strand-splitting of a Σ₂
  slot), by preservation of sequential Gaussianity (a (3,2,2) coupling makes the
  eliminated Σ₂-action quartic, destroying the closed-form 𝔽 at the next order),
  and by tower uniformity. This is scheme B.

## 6. Consequence for the all-orders formulation (spec for the next step)

The scheme-B ansatz eq:Sdrallorders is quadratic in every Σ_k separately (kinetic
M̃_k, odd coupling Ṽ_{2k+1}(Σ_k,Σ_k,Ψ) = kinetic dressing, source
⟨ũ_k(Σ_{k−1}),Σ_k⟩ linear in both), with triangular field-dependence. Hence the
top-down elimination Σ_K, Σ_{K−1}, …, Σ₂ is a chain of exact Gaussians **at every
truncation order**, each step preserving quadraticity in the next field down. Two
consequences, elevating 013 §8's conjecture to a mechanical scheme:

1. the on-shell value of any truncation is a **closed-form** rational function of
   g (nested Schur complements), and closure at order n is a single Veronese-
   diagonal condition — "Ṽ_n-diagonal = V_n(Ψⁿ) − n!·(g^{n−2}-coefficient of the
   previous truncation's 𝔽)";
2. the gauge laws are exact kernel rotations at every order (§7) — no implicit/
   Neumann structure anywhere in scheme B (that structure was an artifact of the
   minimal scheme's cubic-in-Σ₂ vertex).

Open for the O(g_s⁶) session: the menu there is richer ({(4,4) + (4,3,1)} pair vs
(3,3,2) — the first order where an *odd-field-count* coupling of existing fields
competes with the new pair), and the conjecture is that the Σ₄ pair with source
ũ₄(Σ₃) (which **uses Σ₃**) is again forced for
the V₈ contact while (3,3,2) is again the free partition split. Not checked here.

**[Addendum 2026-07-08, B7/R26:** settled by derivation 019 — the Σ₄ pair closes
O(g⁶)+O(g⁷) with forced diagonals, ũ₄(Σ₃) is forced and uses Σ₃, and the whole
spec is subsumed by the all-orders fixed-point theorem (Jacobi form + diagonal
recursion). The (3,3,2) free-split conjecture remains open (non-Gaussian shape,
outside the theorem). See `agent/derivations/019-b7-allorders-fixed-point.md`.**]**

## 7. The gauge law at O(g_s⁵)

With the (3,3,1) coupling, decompose (exactly — both sectors Gaussian):
S₅ = S_eff⁽⁷⁾(Ψ) + 𝔽₆(Ψ) + ½Y₂ᵀĤ(Ψ)Y₂ − (g⁴/6!)Y₃ᵀM̂(Ψ)Y₃, with
Y₂ = Σ₂ − Σ₂*(Ψ), Y₃ = Σ₃ − Σ₃*(Σ₂,Ψ) (conditional saddle), Ĥ the exact
Σ₂-Hessian of the Σ₃-eliminated action. Demanding δ[deviation part] = 0 under
arbitrary δΨ gives the **explicit** rotations
δY₃ = −½M̂⁻¹(δM̂)Y₃, δY₂ = −½Ĥ⁻¹(δĤ)Y₂, with δM̂ = −(g/7)Ṽ₇(·,·,δΨ) and δĤ
assembled from δW, δL̃(= Gsrc(δΨ)-linearity) and δ(M̂⁻¹). Then

$$ \delta S_5 - \delta\big[S^{(7)}_{\rm eff} + \mathbb F_6\big] = 0
   \quad\text{exactly (off-shell, arbitrary }\delta\Psi), $$

verified with all-analytic directional derivatives at 3e-16 relative (check 7;
δ[S_eff⁽⁷⁾+𝔽₆] computed by the envelope theorem as ∂_ΨS₅|_{saddles}·δΨ).
Falsification legs: setting δY₃ = 0 leaves exactly +（g⁵/7!)Ṽ₇(Y₃,Y₃,δΨ)
(= −(g⁴/6!)Y₃ᵀ(δM̂)Y₃); setting δY₂ = 0 leaves exactly ½Y₂ᵀ(δĤ)Y₂ — both matched
to 1e-10. R21's δY₃ = 0 is thereby superseded (it was the statement that M̃ was
Ψ-independent, true only through O(g_s⁴)); both deviations now sit in the
field-dependent-kinetic corner of R22's BV class. Homogeneity (δY ∝ Y) and the
absence of any independent two-string/three-string parameter persist — R18's
pattern at the fourth consecutive order.

## 8. What is established vs open

**Established (machine-checked, finite-dim algebraic layer, generic non-L∞
tensors, two seeds):**
(i) sequential exact Gaussianity of S_dr + closed-form 𝔽^dr (check 1);
(ii) A₅^dr = (1/600)[⅓S₂ − ⅕S₁], strand-local (check 1); A₅^min corroborated in
the same basis, with the strand-split S₃ (check 5);
(iii) closure at O(g_s⁵) by the dressed (3,3,1) coupling; coefficients
(1, 42/25, −14/5) forced; bare V₇ fails (checks 2, 3);
(iv) running-kernel identity: the S₁-dressing = O(g) term of −(6/5)ΦᵀK_Ψ⁻¹Φ
(arithmetic, §4);
(v) both partitions + mixes close: menu = presentation freedom (check 4);
(vi) scheme-A-literal failure: no V₇ contact without the O(g_s⁴) Σ₃ pair
(check 5); O(g_s⁵) menu = {(3,3,1),(3,2,2)} (check 6 = arithmetic bookkeeping
of the power counting, not an independent test — critic C1);
(vii) exact kernel-rotation gauge laws, exact equality, falsification legs,
homogeneity (check 7).

**Open / carve-outs:**
(a) CFT-level analytics of V₄⁻¹, M̃⁻¹, M̂⁻¹, Ĥ⁻¹ and the composite kernels —
A2(iii)/T4, inherited;
(b) region identification inherited (R14(b) language); the composites are
algebraic, moduli enter only through the geometric V₄…V₇;
(c) kernel uniqueness up to Veronese-diagonal-null forms (013 §3(c));
(d) the O(g_s⁶) step: (4,4)+(4,3,1) pair vs (3,3,2) — specified in §6, not
checked; the all-orders fixed-point statement (§6) is structural, its
order-by-order verification stops at n = 7;
(e) blind critic pass — DONE 2026-07-08 (Opus, blind): ACCEPT, 0 Fatal/0 Serious
(report `agent/reports/critic-b6-ogs5-20260708T210500.md`);
(f) perturbative-branch statements (R19 carve-out (g)).

**Result → candidate R25.** Order g_s⁵ closes; the closing coupling is scheme B's
Ṽ₇(Σ₃,Σ₃,Ψ) with forced strand-local dressing; the even HS pair is forced and the
odd-partition menu is presentation freedom — the scheme-A/scheme-B distinction
dissolves into one family whose canonical member is the sequentially-Gaussian
dressed tower (scope of "dissolves": see §0.5).
