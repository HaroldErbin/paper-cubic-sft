# Derivation 013 — B3: the O(g_s⁴) sextic milestone

- **Task:** Phase B, "(i) O(g_s⁴) milestone" (state file resume block 2026-07-03;
  spec = derivation 011 §6): construct the O(g_s⁴) step of the Route-B cubicization
  tower — the three-Σ coupling — and determine whether/how the matching closes.
  Scope set at the Phase B resume: worth doing to understand how higher orders work;
  classical only (no quantum/tadpole work).
- **Author:** Claude Fable 5, inline (no delegation), session 2026-07-03 (#3).
- **Machine check:** `codes/verify-b3-sextic.py` — **7/7 PASS (executed 2026-07-03)**.
- **Status:** candidate **R19**. NO critic pass this session (critic
  dispatch = ST1 extension in `agent/state/opus-side-tasks.md`).
- **Inputs reused (not re-derived):** R1 (eq:SHS), R7 (physical grading), R9/R13
  (invertibility/quotient), R11 (composite law), R12 (counting: 6 = 2+2+2, Σ₂
  suffices through V₆), R14 (Σ-Feynman rules, telescoping), R15 (V₄⁻¹ status,
  two-gradings), R17 (011: exact rewriting (B.2), dressed kernel K_Ψ, feedback
  (g_s⁴/600)vK_Ψ⁻¹v, gauge law (B.8)), R18 (012: no independent Λ₁).
- **Conventions:** physical N_gh (Ψ at 2, Σ at 4, even); finite-dimensional model
  binding for the combinatorial/algebraic layer exactly as in R14/R17 (CFT-level
  analytics stay with A2(iii)/T4); e^S weight; V₄, V₅, V₆ totally graded-symmetric
  geometric vertices.

---

## 0. Executive summary

**The naive expectation of 011 §6 is FALSIFIED, in an instructive way.** At O(g_s⁴)
the matching does *not* close with the geometric V₆ alone, and the geometric master
equation is *not* what closes it. Let P ≡ Ψ⊗², X ≡ Σ − P, and recall from R17 the
O(g_s³) feedback (g_s⁴/600)·vV₄⁻¹v, v = V₅(·,P,Ψ). The results:

1. **Uniqueness of the coupling class (§1):** at O(g_s⁴) the only admissible cubic
   additions are three-Σ couplings T(Σ,Σ,Σ). Every other candidate (Ψ³-contact,
   purely-Ψ additions — a Ψ²-kinetic correction and a Ψ-tadpole — source or coupling
   corrections, kinetic corrections, ΣΨ-mixing, Σ-tadpole) contaminates an n-point tree
   amplitude at order g_s⁴ ≠ g_s^{n−2} (power-counting exclusion table, script check 6;
   the purely-Ψ ones are excluded by the *same* power counting — a Ψ-tadpole shifts the
   1-point function at g_s⁴, a Ψ²-kinetic correction the 2-point at g_s⁴).

2. **Pure V₆ fails (§2):** with the coupling (g_s⁴/6!)c₆V₆(Σ,Σ,Σ) alone, the
   on-shell mismatch is
   $$ S_4(\Sigma_*) - S^{(6)}_{\rm eff}
      = \frac{g_s^4}{600}\,vV_4^{-1}v + (c_6-1)\frac{g_s^4}{6!}V_6(\Psi^6) + O(g_s^5), $$
   and since vV₄⁻¹v and V₆(Ψ⁶) are independent invariants of Ψ (script check 3c),
   **no choice of c₆ cancels the feedback**. The V₆-collapse can only supply the
   V₆ contact; the two-V₅ Σ-exchange trees of the HS side have no counterpart in
   $S^{(6)}_{\rm eff}$ and must be cancelled *by hand*. *(Scope of "FALSIFIED", critic
   Concern 2: the feedback (g_s⁴/600)vV₄⁻¹v is produced by the §4 exact rewriting, which
   is an identity in generic tensors — it therefore survives when the V_n are genuine L∞
   vertices too, so the falsification is structural, not merely a generic-tensor artifact.
   It is not machine-verified against a master-equation-conditioned V₆; the structural
   argument is what carries it.)*

3. **The forced dressed vertex (§3):** matching forces the unique (up to
   on-diagonal-null kernels, §3c) three-Σ coupling
   $$ \boxed{\;\frac{g_s^4}{6!}\,W_6(\Sigma,\Sigma,\Sigma),\qquad
      W_6 := V_6 \;-\; \tfrac{6}{5}\,\mathcal C,\;} $$
   where 𝒞 is the **composite Σ-channel kernel**: two V₅ blocks joined by one
   Σ-propagator (V₄⁻¹), with the *third* Σ's two strands split one-per-block,
   $$ \mathcal C(A,B,Z) := \sum_{\rm strands}
      \big\langle V_5(\cdot,A,z^{(1)}),\,V_4^{-1}V_5(\cdot,B,z^{(2)})\big\rangle,
      \qquad Z=\textstyle\sum z^{(1)}\!\otimes z^{(2)}, $$
   which satisfies 𝒞(P,P,P) = vV₄⁻¹v exactly. Coefficients forced:
   (c₆, θ) = (1, 6/5) (script check 3). Ghost saturation is consistent throughout:
   V₆ saturates 12 = 4+4+4; inside 𝒞 each V₅ saturates 10 = 4(Σ)+2(strand)+4(prop
   slot) and the V₄⁻¹ pairing joins two ghost-4 slots (8 = V₄ saturation)
   (check 6).

4. **Exact rewriting (§4), the (B.2)-analogue with a cubic remainder:** for any
   (c₆, θ), identically in (Σ, Ψ, g_s),
   $$ S_4 = S^{(6)}_{\rm eff}
      \;-\;\frac{g_s^2}{4!}K_6(\tilde X_6,\tilde X_6)
      \;+\;\frac{g_s^4}{6!}\,T(X,X,X)
      \;+\;\frac{g_s^4}{600}\,v_6K_6^{-1}v_6
      \;+\;\frac{g_s^4}{6!}\big[T(P^3)-V_6(\Psi^6)\big], $$
   with T = c₆V₆ − θ𝒞 (symmetrized), K₆ = K_Ψ − (g_s²/10)T(·,·,P),
   v₆ = v + (g_s/4)T(·,P,P), X̃₆ = X − (g_s/5)K₆⁻¹v₆ (check 1, 1e-16). The square
   no longer completes exactly — the deviation now has a **cubic self-interaction**
   — but on-shell the cubic remainder is O(g_s⁷) and the shifted-square remainder
   O(g_s¹⁰), so with (c₆,θ) = (1,6/5) the on-shell mismatch is O(g_s⁵) with the
   explicit leading coefficient A₅ (check 2) — the next feedback, to be absorbed
   by the O(g_s⁵) step.

5. **Diagrammatics (§5):** the 6-point O(g_s⁴) tree diagrams of the HS side add
   one genuinely new class, the two-V₅ Σ-exchange
   [src–Σprop–V₅–Σprop–V₅–Σprop–src]: 90 assignments × (g_s⁴/75)·(kernel), whose
   sum equals both the polarized feedback (g_s⁴/600)vV₄⁻¹v and (exactly minus) the
   θ𝒞-contact of W₆ — coefficient bookkeeping closed by exact polarization
   (check 4, 1e-16).

6. **Gauge law (§6):** around the exact saddle Σ*(Ψ), with Y := Σ − Σ*, the
   corrected law is the **implicit homogeneous rotation**
   $$ \boxed{\;\delta Y=\mathcal K^{-1}\Big[-\tfrac12(\delta\mathcal K)(\cdot,Y)
      +\tfrac{g_s^2}{20}\,T(\cdot,Y,\delta Y)\Big],\qquad
      \delta\Sigma=\delta\big[\Sigma_*(\Psi)\big]+\delta Y,} $$
   (𝒦 = the saddle Hessian kernel; unique solution for small g_s by Neumann).
   With it, δS₄ − δS_eff⁽⁶⁾ = δ[𝔽₅] **exactly** (identity in fields, off-shell,
   arbitrary δΨ; 𝔽₅(Ψ) := S₄(Σ*) − S_eff⁽⁶⁾ = O(g_s⁵)); the law is homogeneous in
   Y (δY|_{Y=0} = 0: **Σ transforms as its saddle, exactly**), and both the
   T-truncated law and the verbatim 011 law (B.8) are falsified at this order
   (check 5). R18's pattern persists: **no independent two-string parameter is
   generated at O(g_s⁴)**.

7. **Structural lesson (§7):** Route-B cubicization is completion-of-squares plus
   **Σ-channel exchange subtraction** at every order; the geometric master equation
   never enters the matching — all of its content lives in the target
   ($S^{(n)}_{\rm eff}$'s own consistency and gauge invariance, which the exact
   equality then transfers to S₄). This corrects 011 §6's expectation ("the master
   equation should make it close with c₆ = 1") and gives the all-orders skeleton
   (§8).

---

## 1. Uniqueness: only three-Σ couplings are admissible at O(g_s⁴)

Tree n-point amplitudes scale exactly as g_s^{n−2}. Any O(g_s⁴) addition to the
action that effectively contributes an n-point tree structure with n < 6
contaminates an amplitude at the wrong order. Exhaustively (cubic-in-fields
candidates; script check 6 records the arithmetic):

| candidate addition | contaminates | order | target order |
|---|---|---|---|
| g_s⁴·(kernel)(Ψ³) | 3-point contact | g_s⁴ | g_s |
| g_s⁴·D(Σ,Ψ²) source corr. | on-shell D(P,Ψ²) = 4-point | g_s⁴ | g_s² |
| g_s⁴·ΔW(Σ,Σ,Ψ) coupling corr. | on-shell ΔW(P,P,Ψ) = 5-point | g_s⁴ | g_s³ |
| g_s⁴·ΔK(Σ,Σ) kinetic corr. | [src–prop–ΔK–prop–src] 4-point | g_s⁴ | g_s² |
| g_s⁴·V₃(Σ,Ψ) mixing | [ext–mix–prop–src] 3-point | g_s⁴ | g_s |
| g_s⁴·L(Σ) tadpole | [L–prop–src] 2-point | g_s⁴ | g_s⁰ |

(N_gh note: V₃(Σ,Ψ) is saturation-allowed, 4+2 = 6 — it is excluded by power
counting, not ghost counting.) The only cubic monomial whose on-shell footprint is
6-linear in Ψ at O(g_s⁴) is a **three-Σ coupling** g_s⁴T(Σ,Σ,Σ) — its kernel T is
the object matching must fix. R12's counting (6 = 2+2+2, no Σ₃ needed through V₆)
is confirmed dynamically: Σ₃ could not even be *sourced* cubically at this order
without contaminating lower amplitudes.

## 2. Failure of the pure geometric V₆

Take T = c₆V₆ (the naive tower step). From R17's exact rewriting, on-shell,
S₃(Σ*) = S_eff⁽⁵⁾ + (g_s⁴/600)vK_Ψ⁻¹v; expanding the V₆(Σ³)-collapse around the
saddle adds c₆(g_s⁴/6!)V₆(P³) + O(g_s⁵) (the X-linear V₆ terms shift the saddle
only at O(g_s²), affecting the action at O(g_s⁶)). With
S_eff⁽⁶⁾ = S_eff⁽⁵⁾ + (g_s⁴/6!)V₆(Ψ⁶) and V₆(P,P,P) = V₆(Ψ⁶):

$$ S_4(\Sigma_*)-S^{(6)}_{\rm eff}
   =\frac{g_s^4}{600}vV_4^{-1}v+(c_6-1)\frac{g_s^4}{720}V_6(\Psi^6)+O(g_s^5). $$

Script check 3(a): with c₆ = 1 the mismatch per g_s⁴ Richardson-extrapolates to
(1/600)vV₄⁻¹v to 1e-3, ≠ 0. Check 3(b): c₆ = 1.3 adds exactly (c₆−1)V₆(Ψ⁶)/720.
Check 3(c): across random Ψ the ratio vV₄⁻¹v / V₆(Ψ⁶) varies by O(1) — the two
invariants are independent functions of Ψ, so matching **forces two conditions**:
the V₆-part coefficient c₆ = 1 *and* a separate cancellation of the feedback,
impossible within span{V₆}. Diagrammatic reading: the feedback is the two-V₅
Σ-exchange tree class (§5), a *bona fide diagram of the HS theory* with no
counterpart in S_eff⁽⁶⁾; a contact V₆ cannot cancel an exchange-class kernel.

## 3. The forced dressed vertex W₆ = V₆ − (6/5)𝒞

**(a) The composite kernel.** The unique (see (c)) object that is (i) a trilinear
form on Sym²H₀, (ii) built from the already-present structure, and (iii) equal to
vV₄⁻¹v on the diagonal Σ = P, is the Σ-channel composite 𝒞 defined in §0: two V₅
blocks, one Σ into the pair-slot of each, joined by one Σ-propagator, with the
third Σ's two strands distributed one per block. On Σ = P = Ψ⊗² each strand
becomes a Ψ and each pair-slot becomes P, giving 𝒞(P,P,P) = vV₄⁻¹v exactly
(script check 0, both for the raw kernel and its symmetrization).

**(b) Coefficient forcing.** With the coupling (g_s⁴/6!)[c₆V₆ − θ𝒞](Σ³), the
θ-term contributes −θ(g_s⁴/720)vV₄⁻¹v on-shell; cancelling the feedback
(g_s⁴/600)vV₄⁻¹v requires θ/720 = 1/600, i.e. **θ = 6/5**, and then c₆ = 1 as
before. Both verified by Richardson extrapolation (check 3) and, independently of
the saddle route, by the diagrammatic polarization identity (check 4).

**(c) Uniqueness scope.** Matching constrains T only through its on-shell diagonal
T(P,P,P) as a function of Ψ (a sextic polynomial). Kernels vanishing identically
on the Veronese diagonal {P = Ψ⊗²} can be added freely — the same
presentation/field-redefinition freedom class as in 011 §1 and R13's quotient.
W₆ = V₆ − (6/5)𝒞 is the canonical representative: it is the one whose contact
term *literally* cancels the two-V₅ exchange diagrams assignment-by-assignment
(§5), not merely on the diagonal.

**(d) What W₆ is geometrically.** In the coloured-operad picture (R15), 𝒞 is a
coloured tree with two V₀,₅ blocks and one internal colour-2 edge — formal
uncoloured genus 2, physically graded by the coloured tree structure (g_s⁴ =
6-point tree, consistent with R15's two-gradings statement). So the three-Σ
"vertex" of the cubic theory is **not the elementary geometric V₆ but the
V₆-region minus the Σ-channel exchange composite** — the colour-2 analogue of the
familiar "vertex region = amplitude minus exchange regions" structure. The
subtraction is algebraic (Σ-propagators are moduli-free kernels, R15), not a
moduli-region split; the moduli integrals still enter solely through the geometric
V₄, V₅, V₆ inside W₆ and the sources. **Honest flag:** the O(g_s⁴) action is
cubic *in the fields* but its three-Σ kernel is composite (contains V₄⁻¹); whether
an enlarged field content (e.g. introducing Σ₃ early with elementary kernels)
could trade the composite kernel away is an open presentational question for the
all-orders session (§8), inheriting the V₄⁻¹ analytics carve-out either way.

## 4. The exact rewriting at O(g_s⁴)

For **any** (c₆, θ), with T := c₆V₆ − θ𝒞 (symmetrized), expanding T(Σ³) around
Σ = P + X and regrouping (the manipulations of R17 §2 plus the T-terms):

- quadratic: K₆ := K_Ψ − (g_s²/10)T(·,·,P) (further Ψ-dressing of the kinetic
  kernel — invertible for small g_s on the R13 quotient by Neumann; check 0);
- linear: v₆ := v + (g_s/4)T(·,P,P);
- **cubic in X: (g_s⁴/6!)T(X,X,X) — new at this order; the square no longer
  completes exactly.**

Identity (check 1, verified at 1e-16 over random (Σ,Ψ,g_s,c₆,θ)):

$$ S_4-S^{(6)}_{\rm eff}
   =-\frac{g_s^2}{4!}K_6(\tilde X_6,\tilde X_6)
   +\frac{g_s^4}{6!}T(X,X,X)
   +\frac{g_s^4}{600}v_6K_6^{-1}v_6
   +\frac{g_s^4}{6!}\big[T(P^3)-V_6(\Psi^6)\big],
   \qquad \tilde X_6 = X-\frac{g_s}{5}K_6^{-1}v_6. $$

With the tuned (1, 6/5): T(P³) − V₆(Ψ⁶) = −(6/5)vV₄⁻¹v, so the last two terms
combine into the **exact next feedback**
F₆(Ψ) := (g_s⁴/600)[v₆K₆⁻¹v₆ − vV₄⁻¹v] = O(g_s⁵). On-shell (saddle solved by
damped Newton with g_s-continuation): X̃₆(Σ*) = (g_s²/20)K₆⁻¹T(X*,X*,·) = O(g_s⁴),
so the mismatch splits exactly (check 2) as

$$ \mathbb F_5(\Psi) = S_4(\Sigma_*)-S^{(6)}_{\rm eff}
   = \underbrace{F_6}_{O(g_s^5)}
   + \underbrace{\tfrac{g_s^4}{6!}T(X_*^3)}_{O(g_s^7)}
   + \underbrace{-\tfrac{g_s^2}{4!}K_6(\tilde X_6^{*2})}_{O(g_s^{10})}, $$

with the log-slopes 7 and 10 verified by halving and the leading coefficient
A₅ = (1/600)[½T(V₄⁻¹v,P,P) + ⅕vV₄⁻¹WV₄⁻¹v], W = V₅(·,·,Ψ), verified directly on
the exact F₆ formula (check 2). **This 𝔽₅ is the target the O(g_s⁵) step must
absorb** — the recursion continues (§8).

## 5. Diagram enumeration at O(g_s⁴) (6 points, tree)

New classes beyond R14/R17 collapses (all others are shared or collapse on
sources exactly as at lower orders, R14's slot-agnostic telescoping):

- **Two-V₅ Σ-exchange** [src–Σprop]–V₅–[Σprop]–V₅–[Σprop–src]: per assignment
  {single i, pair (jk) | single l, pair (mn)}, the two source chains telescope to
  2q each, the Wick factor is 2×2 (source-vs-internal choice of the two identical
  Σ-slots per V₅), the internal propagator is 12/g_s²:
  (g_s³/5!)²·4·(12/g_s²)·⟨V₅(·,2q_{jk},Ψ_i), V₄⁻¹V₅(·,2q_{mn},Ψ_l)⟩ =
  **(g_s⁴/75)·⟨V₅(·,q_{jk},Ψ_i), V₄⁻¹V₅(·,q_{mn},Ψ_l)⟩**; **90 assignments**
  (10 unordered triple-partitions of 6 × 3 × 3 single-choices).
- **W₆ contact**: the V₆-part collapses to (g_s⁴/6!)V₆(Ψ⁶)-worth of contact
  (coefficient 1, the R17 telescoping argument verbatim); the −(6/5)𝒞-part gives
  a contact equal to **minus** the two-V₅ exchange sum.

Check 4 verifies, by exact polarization (coefficient extraction of ψ₁⋯ψ₆ via the
2⁶ inclusion-exclusion identity, machine-exact for polynomial actions), that the
90-assignment sum equals both the polarized feedback (g_s⁴/600)vV₄⁻¹v and the
polarized θ𝒞-contact — so in the 6-point function the exchange class and the
𝒞-contact cancel identically, leaving [V₆ contact] + [inherited collapse classes]
= the S_eff⁽⁶⁾ diagram set. Combined with the action-level identity (§4), every
tree amplitude matches through O(g_s⁴). Moduli: same carve-out language as
R14(b)/R17 §5 — coefficients computed, region identification inherited; the
Σ-propagators and the 𝒞-subtraction are moduli-free.

## 6. The gauge law at O(g_s⁴): implicit, still homogeneous

Around the exact saddle: S₄ = S_eff⁽⁶⁾ + Φ*(Y;Ψ) + 𝔽₅(Ψ) identically, where
Y := Σ − Σ*(Ψ) and (exact Taylor of a cubic action)
Φ*(Y;Ψ) = −(g_s²/4!)𝒦(Y,Y) + (g_s⁴/6!)T(Y,Y,Y), with 𝒦 the (Ψ-dependent) saddle
Hessian kernel 𝒦 = K₆ − (g_s²/10)T(·,·,X*). Demanding δΦ* = 0 under arbitrary δΨ
(T's kernel is fixed — the design choice of building 𝒞 with V₄⁻¹ rather than
K_Ψ⁻¹ pays off here) gives one scalar condition; its canonical solution is the
implicit linear law boxed in §0. Verification of the cancellation:
2𝒦(δY,Y) = −(δ𝒦)(Y,Y) + (g_s²/10)T(Y,Y,δY), so the quadratic-form variation
leaves −(g_s⁴/240)T(Y²,δY), cancelled exactly by the cubic term's (g_s⁴/240)T(δY,Y²).
Then

$$ \delta S_4-\delta S^{(6)}_{\rm eff}=\delta\big[\mathbb F_5(\Psi)\big]
   \quad\text{EXACTLY (identity in fields, off-shell, arbitrary }\delta\Psi). $$

Machine check 5 (all-analytic: implicit-function-theorem δΣ*, envelope-theorem
δ𝔽₅): residual 4e-17 over random off-shell draws; homogeneity δY(Y=0) = 0 exact;
falsifiability: dropping the T-correction, or using 011's law (B.8) verbatim,
leaves nonzero residuals. Consequences:

- Since 𝔽₅ = O(g_s⁵) and Σ-independent, **S₄ is gauge-invariant to the same
  O(g_s⁵) as the sextic-truncated theory itself** — the tower step again costs
  nothing (R11 → R17 → here).
- The law is **homogeneous in the deviation** at this order too: no inhomogeneous
  Q̂Λ₁ piece can be generated. R18's verdict extends: through O(g_s⁴) the gauge
  algebra of the cubicized theory is the Ψ-gauge algebra, with δΣ = δ(saddle) +
  homogeneous rotation — now with the qualitatively new feature that the rotation
  is only **implicitly** defined (solved by Neumann series in g_s²), a foretaste of
  the all-orders structure.
- Note δS_eff⁽⁶⁾ = O(g_s⁵) itself requires the L∞ relations through ℓ₅ (geometric
  master equation through V₀,₆). The exact equality **transfers** that statement to
  S₄; it does not use it. See §7.

## 7. Where the master equation actually lives

011 §6 expected the O(g_s⁴) matching to be "the first place the geometric master
equation is load-bearing". The computation shows a sharper split:

- **Matching (this derivation): master-equation-agnostic.** The identity of §4
  holds for arbitrary symmetric tensors V₄, V₅, V₆ — no L∞ relations were imposed
  anywhere in the model, and all checks pass with generic (non-L∞) data. The
  closure mechanism is completion-of-squares + Σ-channel exchange subtraction.
- **The target's consistency: all master-equation content.** That S_eff⁽⁶⁾ has the
  right amplitudes (region decomposition of M₀,₆) and is gauge-invariant to
  O(g_s⁵) is exactly the geometric master equation / L∞ structure. The exact
  equalities (on-shell matching + gauge equality) transfer these properties to S₄
  wholesale.

So Route B never *tests* the master equation; it *inherits* it. The practical
consequence for the program: the cubicization recursion can be run — and proved —
as pure algebra on the vertex data, with the geometric input isolated in the
target. (This also explains *why* the naive c₆ = 1 expectation failed: the master
equation relates ∂V₀,₆ to Ψ-channel plumbings and says nothing about the
Σ-channel exchange class, which is a creature of the HS side alone.)

## 8. The all-orders skeleton (conjecture + spec for the next big step)

The pattern through O(g_s⁴), now visible:

- **Couplings:** at each order, the new three-field coupling is
  [target vertex on Σ-slots, coefficient 1] − [all Σ-channel exchange composites
  already generated by lower couplings], e.g. W₄ = V₄ (kinetic+source), W₅ = V₅,
  W₆ = V₆ − (6/5)[W₅∘V₄⁻¹∘W₅]-composite; expected W₇ = V₇ − [W₅W₆-composites] −
  [triple-W₅ composites], etc., with Σ₃ entering at V₇ (7 = 3+2+2, R12) —
  including its own kinetic V₆(Σ₃,Σ₃) and *cubic* source V₆(Σ₃,Σ₂,Ψ) or
  V₅(Σ₃,Ψ,Ψ) (both saturation-allowed: 6+2+2 = 10); the tower sources itself
  triangularly (Σ_k sourced via Σ_{k−1}).
- **Rewriting:** S_cubic = S_eff⁽ⁿ⁾ − (dressed quadratic form in the deviation) +
  (polynomial remainder in the deviation, degree ≤ 3 per field sector) +
  (Σ-independent feedback, O(g_s^{n−1})), all exact identities; the feedback at
  each order is the next order's subtraction target — a recursive generating
  structure that should admit a closed all-orders formulation (the deliverable of
  the next session: set it up as a fixed-point/generating-function statement,
  fields Ψ ⊕ {Σ_k}, and prove the recursion closes; candidate framing: the
  coloured-operad two-coloured tree expansion of R15, where "subtract all
  colour-2-reducible trees" is precisely the passage from amplitudes to a
  coloured vertex decomposition — i.e. the cubic action is the statement that
  **the target L∞ vertices, seen in the two-coloured operad, are generated by a
  finite set of coloured-irreducible cubic vertices**).
- **Gauge:** δ(fields) = δ(perturbative saddle) + homogeneous (implicitly defined)
  rotation of the deviation, exact equality with δ[feedback] at every order; no
  independent parameters (R18's conjecture, now supported at two consecutive
  orders); the enlarged-Λ₁ home, if wanted, remains the Π-partner route (012 §4,
  reframed by the 2026-07-03 comments — see the state file).

## 9. What is established vs open

**Established (machine-checked, finite-dim algebraic layer; generic tensors, no
L∞ input):**
(i) O(g_s⁴) admissible-coupling uniqueness (power counting; check 6);
(ii) pure geometric V₆ fails: mismatch = R17 feedback, independent of c₆ (check 3);
(iii) forced dressed vertex W₆ = V₆ − (6/5)𝒞, (c₆,θ) = (1,6/5) (checks 3, 4);
(iv) exact rewriting with K₆, v₆, cubic remainder (check 1) and exact on-shell
split with O(g_s⁵) feedback and analytic A₅ (check 2);
(v) 6-point diagrammatics: 90 two-V₅ trees = feedback = 𝒞-contact, exact
polarization (check 4);
(vi) exact gauge equality with the implicit homogeneous law; naive and 011-laws
falsified; no independent two-string parameter (check 5).

**Open / carve-outs:**
(a) CFT-level analytics of V₄⁻¹, K₆⁻¹, and now of the composite kernel 𝒞
(inherits A2(iii)/T4);
(b) region identification inherited, not re-derived (R14(b) language);
(c) kernel-uniqueness only up to Veronese-diagonal-null forms (§3c) —
presentation freedom, quotient class;
(d) composite-vs-elementary kernel: can enlarged field content (early Σ₃)
restore elementary kernels? (§3d, next session);
(e) BV classification of the implicit homogeneous law (extends ST4's scope);
(f) the all-orders formulation (§8) — the next big step;
(g) saddle-fold caveat: at finite g_s beyond a draw-dependent fold the
perturbative Σ*-branch can disappear in the toy (script resamples such draws);
all statements are perturbative-branch statements, as everywhere in Phase B.
