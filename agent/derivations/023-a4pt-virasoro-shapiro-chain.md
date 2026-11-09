# Derivation record 023 — Phase A: the 4-point amplitude chain, HS Feynman rules → telescoping → Virasoro–Shapiro, with H1/H2 displayed

Date: 2026-07-15
Author: Claude Fable 5 (computator, brief `computator-a4pt-chain-20260715T000000`)
Task source: `plans/amplitude-check-plan-2026-07-14.md`, Phase A (steps A1–A5); this is
the paper's future §7 (amplitude consistency) per `plans/paper-plan-2026-07-14.md` row 7.
Verification: `codes/verify-a4pt-chain.py` (sympy via project uv venv, seed 20260715,
executed 2026-07-15; re-executed 2026-09-21 after the second and third fix passes —
6/6 PASS on the same seed, the check-5 error sequences and every PASS/FAIL predicate
unchanged, the printed output extended by the `dominant_overlap` diagnostic added in
the second pass and by its guards added in the third). The script prints
"6/6 PASS", but that tally must not be read as six pieces of evidence: check 3 is a
*demonstration of vacuity* (it PASSes on deliberately corrupted vertex data, which is
its point, §5.1). The honest count is **5 checks + 1 vacuity demonstration**.
Critic: ACCEPT, 0 Fatal, 0 Serious, 4 Concern, 6 Minor (blind, iter 1 of cap 2 —
`agent/reports/critic-a4pt-chain-20260715T003000.md`). Full hunt list re-derived
independently and confirmed correct (prefactor chain, diagram-enumeration
completeness, H1/H2 placement, overclaim language, eq. (4.2) VS form); R14 ledger
cross-check consistent. The 4 Concern-level wording fixes (H1 phrasing; §5.2
convergence gloss; §9 brace scope + implicit pairing sum) applied by a sonnet-tier
mechanical pass (`agent/reports/computator-a4pt-fixes-20260715T020000.md`); no
derivation content changed. Promoted to ledger as **R29**.

Reused verbatim (not re-derived): **R14** (Σ-Feynman rules, the finite-dimensional
telescoping identity, D-cancellation multiplicity lemma, kernel-decoupling
diagrammatics — `agent/derivations/007-a1-amplitude-telescoping.md`; its
`codes/verify-a1-telescoping.py` checks are *extended*, not duplicated), **R27**
(Riemann-surface/coloured-operad dictionary: item 3.ii Neumann chain series, item 4
the m₂⁻¹-cancellation mechanism, item 5 the combinatorial 3-channel covering —
`agent/derivations/020-riemann-m2-geometric.md`), **R28** (no-local-kernel theorem
for m₂⁻¹ — `agent/derivations/022-rs5-no-local-kernel-theorem.md`), **R1/R8/R10**
(HS action `eq:SHS`, completion of the square, 2:1 source-to-kinetic ratio),
**R9/R13 + 2026-07-01 ledger annotation** (kernel = decoupled spectators, quotient
construction), **RS4/021** (Ψ-propagator fixture $\mathsf P=(b_0^+/L_0^+)\,\omega_1^{-1}$,
$\omega_1^{-1}=b_0^-\delta_{L_0^-,0}$).

**Status: 2026-09-21 — fix pass applied** (brief
`computator-023-fixpass-20260921T152500`, report
`agent/reports/computator-023-fixpass-20260921T152500.md`), after re-verification of
the findings of critic report `critic-20260921T124500` against this record: three of
its findings were planted in a modified copy and do not apply here (the "expected"
motivation of H2 as a *phrase*, the exclusion E2, the deleted §7 conditional bullet);
25 apply and are fixed. Changes, in order of appearance:

1. Header: "6/6 PASS" reported as 5 checks + 1 vacuity demonstration; script re-run
   2026-09-21 (the printout has since grown the `dominant_overlap` line; the
   predicates and the check-5 numbers are unchanged).
2. §0: **H3 declared** (covering of $\mathcal M_{0,4}$) as a third hypothesis, needed
   only on shell; H1 stated in its substantive (bounded-inverse) form; the headline is
   now conditional on H1–H3 on shell, H1–H2 off shell; "H1/H2 hold automatically at
   finite truncation" replaced by the uniformity statement.
3. §1: $D=26$ and the $\alpha'$/Mandelstam conventions stated; the $\Psi$- vs
   $\Sigma$-propagator sign convention reconciled ($V_2(\Psi^2)=-\Psi^\top K\Psi$);
   the source-vs-shift implementations of (1.1) shown to agree on the multilinear
   part; $S_4$-symmetry stated once as a *defining property* of the vertex family, not
   a hypothesis; strand-wise level matching of $\operatorname{Sym}^2\mathcal H_0$
   stated; H1, H2, H3 each given a motivation, a falsifier and a discharge condition;
   **H2 reconciled with R27's R33 annotation** — the pair sum runs over levels *and*
   the pair's relative momentum (031 §4.3, §7), so it is not a pure level sum and its
   finite-truncation status is weaker than previously written; the Moore–Penrose /
   orthogonality framing replaced by the inner-product-free statement
   ($V_4(\Xi,\cdot)=0$).
4. §3: (3.2) commentary updated for the momentum part of H2; (3.4) commentary
   demoted from "hypothesis" to "defining property"; regime bullets separate the three
   scopes conflated in "all orders in $t$ (loop terms included)" and cite **R38** for
   the $O(g_s^2)$ limit of the kernel-quotient defusal.
5. §4: new paragraph justifying the passage from (4.1) to the on-shell locus
   (multilinearity, shared channel poles, H1/H2 extended to on-shell external data and
   motivated by the finiteness/analyticity of $V_4$ on shell); Claim ON made explicitly
   conditional on H3 with the R2/R37 status of the SL(2,C) family; internal
   consistency of (4.2) checked ($\sum a_i=1$); the tower-completeness claim replaced
   by the explicit order count ($3+4-4=3$ with five external legs).
6. §5: R28's "modulo factorization" hedge restored; the teeth sentence split into
   coefficient content (certified) vs telescoping content (untestable at finite
   truncation); §5.2's model-B numbers corrected against the script output (the growth
   is $\times215$, *slower* than $\rho^{12}=1.97\times10^4$, with the per-step rate
   rising toward $\rho$); the two check-5 models described as *found* by rejection
   sampling.
7. §6: arithmetic-exactness wording clarified; check 2's Moore–Penrose use labelled as
   a construction, not a claim about the pairing; check 6 scoped to the level part of
   H2.
8. §7/§8: H3 added to the not-established list with its SL(2,C) status; the on-shell
   objection added to the anticipated objections; the weakest-step entry updated.
9. §9: the display rewritten (H1/H2 labelled at the right factors, $P$/$Q$ in the
   slots, prefactors collected); tadpole exclusions attributed correctly
   (order counting for $\Psi$, parity for $\Sigma$); H1's bounded inverse restored in
   the prose; R28's hedge restored; H3 stated with its open status; the
   **limitations-table line rewritten** to carry H1, H2, H3, the algebraic-vs-CFT
   distinction and R28's modulo.
10. References: Erbin book year vs bibtex key explained; the stub / auxiliary-field
    precedent (Schnabl–Stettinger, arXiv:2301.13182) and the project's own reviews
    added; the unverified Polchinski section *title* claim dropped.

Not done: instantiating check 2 or check 5 on R15's level-0 tachyon block instead of
random tensors (a new computation, not a fix).

**Status: 2026-09-21 — second fix pass applied** (brief
`computator-023-fixpass2-20260921T171000`, report
`agent/reports/computator-023-fixpass2-20260921T171000.md`), on the findings of critic
report `critic-023-fixpass-20260921T161500` (verdict REVISE). Changes:

1. **Scope of the tautology trap and of "automatic at finite truncation"** (§0, §3
   regime bullets, §5.1, §5.2, §9, script docstring): every such statement is now scoped
   to the finite-dimensional model — finitely many levels *and* the pair's relative
   momentum suppressed — where it is proven. For a level truncation of the actual
   theory the momentum integral survives, the collapse is not a finite matrix identity,
   and whether a truncated comparison carries information is stated as **open**, with
   what it could test named (convergence of $\int d^Dk_a$ on $m_2P$ at fixed level).
2. **On-shell H1** (§1 new paragraph "Where H1 is assumed to hold", §4, §8 item 4, §9):
   the non-degeneracy of $m_2$ at the external momenta used, tachyon shell included, is
   a declared part of H1, motivated by PH5 (genericity) rather than by the finiteness of
   $V_4$ (a numerator property), with the falsifier of PH18 — a zero of
   $\det V_4^{(L)}(P^2)$ on the shell persisting with the level.
3. **H1's analytic content and the inner product** (§0, §1, §6 check 2, §7, §9,
   limitations line): "inner-product-free" is kept for the kernel-decoupling half only;
   closed range and bounded inverse are stated *in a stated auxiliary inner product*, as
   ledger PH1 does. **Third fix pass (2026-09-21):** that inner product is now *fixed*
   rather than existentially quantified — the positive-definite Fock-space inner
   product of the matter-plus-ghost oscillator basis, extended factorwise to
   $\operatorname{Sym}^2\mathcal H_0$ (§1) — so that the singular-value falsifier
   refutes H1 itself; another admissible norm would be another hypothesis, and the
   choice is flagged as an open choice.
4. **(5.2) rewritten with the objects the script uses**: the diagonal split is of the
   $V_4$ Gram on $\operatorname{Sym}^2$, so $(V_4|_{\operatorname{Sym}^2})^{-1}=
   \sum_n(D^{-1}N)^nD^{-1}$ and $m_2^{-1}=\sum_n(D^{-1}N)^nD^{-1}G_2$; shown to agree
   term by term with 020 (3.1), whose $\tilde D=G_2^{-1}D$ gives the same $D^{-1}N$, so
   the quoted spectral radii are unambiguous. §9's display corrected likewise.
5. **$\Sigma$-tower exclusion made general** (§4): order rule $p(a,b)=2a+b-2$, diagram
   order $E+2L-2$ — order excludes nothing at four externals; the exclusion is the leg
   count $E=\sum_v(a_v+b_v-2)+2\ge V+2$ with $V\ge a_v+1\ge3$, hence $E\ge5$.
6. **§5.2 numbers and transient**: model A's $\rho^{12}=0.0251$ (factor $39.8$), not
   $0.031$; one explanation for both models ($\rho^K$ an asymptotic rate, not a bound),
   now **measured** — the dominant-mode weight in the error functional is
   $4.74\times10^{-3}$ (A) and $5.02\times10^{-3}$ (B), a new diagnostic printout in the
   script with no PASS/FAIL attached.
7. **(3.2) commentary**: why the relative-momentum integral leaves no trace in the
   collapsed answer, and why PH9's "no counterpart in the tree integrand" does not bite.
8. **Script** (`codes/verify-a4pt-chain.py`): docstring scope note and the H1/H2
   not-verified entries updated; check 6's docstring and printed label qualified to the
   level part; `dominant_overlap` added. Re-run 2026-09-21, 6/6 PASS, same seed, the
   check-5 error sequences unchanged.

**The ledger row R29 needs updating**: the headline is conditional on H1–H3, not H1–H2;
H1 carries the auxiliary-inner-product qualifier and the on-shell momentum clause, and
the tautology-trap statement must be scoped to the finite-dimensional model. `PH3` and
`PH21` need the wordings proposed in the second fix-pass report.

**Status: 2026-09-21 — third fix pass applied** (brief
`computator-023-fixpass3-20260921T183000`, on the findings of
`agent/reports/critic-023-iter2-20260921T180000.md`). Changes: (i) H1's auxiliary
inner product **fixed** to the positive-definite Fock-space inner product of the
oscillator basis, extended factorwise to $\operatorname{Sym}^2\mathcal H_0$, with the
falsifier restated in it, the "another admissible norm is another hypothesis" clause
added and the choice flagged as open — propagated to §0, §4, §6, §7, §9 and the
limitations line; (ii) R28's 2026-09-21 class re-scoping carried into §5.2, §9 (both
sites) and the limitations line — the exclusion holds within connected surfaces of
bounded type with standard sewing insertions, and a kernel fine-tuned at the actual
$V_4$ is not excluded; (iii) the minors: "on the quotient" in the (3.3) tag and §6,
the tower exclusion extended to $(a,b)=(1,b\ge3)$, the on-shell degeneration of the
amputating source added as the fourth observation of §4, `dominant_overlap` guarded
(reality/simplicity + eigendecomposition cross-checked against a power iteration with
a residual tolerance) and §5.2 reworded to predict smallness only, `ok2_src` labelled
an identity, the model size $N=2$/$\dim\operatorname{Sym}^2=3$ and the
"$D$ is a full, not level-, diagonal" caveat stated in §5.2 and §6, the stale
"identical output" header sentence corrected, PH5 quoted with its off-shell and
generic-family qualifiers and its "remedy, not evidence" annotation, (4.3) added to
§7's *Established* list, and the Costello–Zwiebach and Moeller–Taylor references
added (the Fırat reference, left open in that pass, was filled on 2026-09-22 from Zotero).
Script re-run: 6/6 PASS, same seed, check-5 error sequences and all predicates
unchanged; the two overlap values are unchanged and now validated by two routes.

2026-09-21: critic ACCEPT (third pass, focused); three mechanical fixes applied.

**Status: 2026-09-22 — H1 restated without an auxiliary inner product** (brief
`computator-h1-restate-20260922T110500`, on Harold's decision of the same day; last
completed step: propagation through §0, §1, §3, §4, §6, §7, §8, §9, the limitations line
and the script docstring; next step: none in this record — the ledger edits for PH1, R29
and R41 are proposed in `agent/reports/computator-h1-restate-20260922T110500.md` and are
the orchestrator's). What changed, and why:

- **H1 is now level-uniformity of the quotient**, in two clauses: (a) the kernels of the
  level-truncated forms stabilize, $\ker V_4^{(L)}=\ker V_4\cap\{\text{level}\le L\}$ for
  large $L$, so the quotient and the level-by-level $\Sigma$-propagator have a limit, the
  $\Sigma$ Gaussian being understood formally as in any SFT path integral; (b) at the
  momenta used, tachyon shell included, the truncated determinant on the quotient has no
  zero persisting with the level. The positive-definite Fock-space inner product of the
  2026-09-21 third pass, the closed-range and bounded-inverse clauses, and the
  "flagged as an open choice" sentence are **removed**.
- **Why:** the BPZ form is indefinite and the Fock form is neither Lorentz- nor
  BRST-invariant, so a singular-value drift stated in it is frame dependent (boosts
  preserve the level grading without acting boundedly on it) and cannot falsify a
  hypothesis of the theory; and §3 never used a bounded inverse — only
  $m_2^{-1}m_2P=P$ mod $\ker V_4$, where existence is trivial, uniqueness modulo the
  kernel is the definition of the quotient, and the amplitude sees the solution only
  through $V_4(\cdot,X)$.
- **What moved rather than disappeared:** the interchange of the intermediate-state sum
  with $m_2^{-1}$ at (3.2)→(3.3) is now an explicit **clause of H2** (§1), the only
  analytic input of the telescoping step. The singular-value drift survives as a
  **numerical conditioning diagnostic** (§1), labelled basis- and frame-dependent and
  explicitly not a falsifier.
- Script re-run after the docstring edit: 6/6 PASS, same seed, no numerical change.

2026-09-22: wording fixes D1–D4, D6 of `agent/reports/critic-h1-restate-20260922T120000.md`
applied (H1 opening and clause (a) now state level-by-level invertibility on the quotient;
H2's interchange clause restated on the scalar partial sums $s_N$; rank-test bridge added;
"truncated form" → "truncated determinant" in §9 and the limitations line) — no algebra,
no numerical change.

**Ledger defects this record identifies** (for the ledger pass, not fixed here):
R29's prose headline still says both hypotheses "hold automatically at any finite
truncation", which §5.1 and §1's H2 refute for a level truncation of the actual theory
(its `Conditional(PH1, PH3, PH4)` status field is already right); and **PH3's
motivation column is the defective part** — it reads "finite sums at each level",
whereas the $\operatorname{Sym}^2$ pair sum is a discrete level sum times
$\int d^Dk_a$ and is *not* finite at each level, so both its motivation and its
falsifier (which covers the level half only) need rewriting to name the
relative-momentum integral.

---

## 0. Claim

Let $S_{\rm HS}$ be the boxed HS action (`eq:SHS`, R1),

$$
S_{\rm HS}=\tfrac12 V_2(\Psi^2)+\frac{g_s}{3!}V_3(\Psi^3)
-\frac{g_s^2}{4!}V_4(\Sigma,\Sigma)+\frac{2g_s^2}{4!}V_4(\Sigma,\Psi^{\otimes2}),
\qquad \Sigma\in\operatorname{Sym}^2\mathcal H_0/\ker V_4,
\tag{0.1}
$$

with $V_3,V_4$ a fixed consistent geometric vertex family (SL(2,C), minimal-area, or
hyperbolic — the argument is family-uniform). Then the tree-level 4-point amplitude of
$S_{\rm HS}$ at $O(g_s^2)$, on four generic external states $\Psi_1,\dots,\Psi_4$, is

$$
\boxed{\;
A_4^{\rm HS}
=\underbrace{g_s^2\!\!\sum_{\{ij|kl\}}\!\! V_3\big(\Psi_i,\Psi_j,\mathsf P\,
V_3(\,\cdot\,,\Psi_k,\Psi_l)\big)}_{\text{3 }V_3\text{-exchange channels }(s,t,u)}
\;+\;\underbrace{g_s^2\,V_4(\Psi_1,\Psi_2,\Psi_3,\Psi_4)}_{\Sigma\text{-exchange, collapsed}}
\;=\;A_4^{\rm SFT}\big|_{\text{quartic-truncated}},
\;}
\tag{0.2}
$$

where $\mathsf P=(b_0^+/L_0^+)\,\omega_1^{-1}$ is the standard closed-string propagator
fixture (RS4) and the $\Sigma$-exchange collapse holds **conditional on two named
CFT-level hypotheses**, stated in §1 and used at the exact steps flagged in §3:

- **H1** — kernel quotient, level-uniform (restated 2026-09-22, **no auxiliary inner
  product**): (a) the kernels of the level-truncated forms stabilize,
  $\ker V_4^{(L)}=\ker V_4\cap\{\text{level}\le L\}$ for large $L$, so the quotient
  $\operatorname{Sym}^2\mathcal H_0/\ker V_4$ and the level-by-level $\Sigma$-propagator
  have a limit (the $\Sigma$ Gaussian integral being understood at the formal level of
  any SFT path integral); (b) at the external momenta used — the on-shell locus of (4.3)
  included — the truncated determinant on the quotient has no zero persisting with the
  level (§1, §4);
- **H2** — completeness and convergence of the $\operatorname{Sym}^2$ intermediate
  two-string state sum (levels *and* the pair's relative momentum), in the form that
  permits the sum to be interchanged with $m_2^{-1}$ at (3.2)→(3.3): the scalar partial
  sums $s_N(P,Q)=\sum_{I\le N}V_4(P,m_2^{-1}\lambda_I)\,\langle\lambda_I,m_2Q\rangle$
  converge to $V_4(P,Q)$ for the external data used (§1).

The on-shell statement (4.3) needs one further condition, also declared as a hypothesis
in §1 because for the family the paper actually uses it is not yet established:

- **H3** — the three plumbing Feynman regions plus the fundamental vertex region
  $\mathcal V_{0,4}$ cover $\mathcal M_{0,4}$ exactly once for the chosen family.

Consequences (§4): **off-shell**, $A_4^{\rm HS}$ equals the standard closed-SFT
off-shell 4-point amplitude *for the same vertex family* (scheme-relevant, the stronger
statement) — conditional on H1–H2 only, H3 plays no role off shell; **on-shell**, given
H3, $A_4^{\rm SFT}$ on four tachyons is the Virasoro–Shapiro amplitude (textbook —
cited). Hence:

> **The cubic HS action reproduces the on-shell 4-tachyon Virasoro–Shapiro amplitude,
> conditional on H1–H3.** The correct framing is "reduces to the standard SFT
> amplitude, which is textbook-known to equal Virasoro–Shapiro on-shell" — *not*
> "proves Virasoro–Shapiro" (overclaim guard, plan A5).

In the **finite-dimensional model** used throughout (a level truncation with the pair's
relative momentum suppressed — §1, last bullet), (0.2) is **exact matrix algebra**: the
algebraic content of H1/H2 is automatic there (a pseudo-inverse always exists, a finite
sum always converges), so a numerical comparison of the truncated exchange with the
truncated vertex cannot fail and verifies nothing (the tautology trap, §5.1). What H1/H2
add beyond that is *uniformity in the level* — that the kernel of the truncated form
stabilizes, so that the quotients and their inverses have a limit, and that the state sum
stays saturated as the truncation grows — which is exactly what a single finite
truncation of that model cannot see.

In the actual theory the situation at finite level is weaker, not stronger: a level
truncation does **not** truncate the momentum integral $\int d^Dk_a$ that H2 also covers
(§1), so the collapse at fixed truncation level is not a finite matrix identity and
whether a truncated comparison then carries information is **open**. What such a
comparison could test is precisely the part the level truncation leaves untouched: the
convergence of the relative-momentum integral on $m_2P$ at fixed level. **Off shell**,
the only place the identity can fail at CFT level, and hence the only falsifiable
numerical content identified here, is the representation theory of $m_2^{-1}$ (§5.2;
Phase B); on shell H3 is a second, geometric, failure mode.

---

## 1. Setup

### Conventions and assumptions

- **Background and $\alpha'$.** Critical bosonic string, $D=26$, closed oriented; the
  covering property (H3) and the Virasoro–Shapiro value (4.2) are statements about that
  background. $\alpha'$ is kept explicit; the Mandelstam variables in (4.2) are
  $s=-(k_1+k_2)^2$ etc. with the $(-,+,\dots,+)$ signature, so the four-tachyon shell
  $k_i^2=4/\alpha'$ gives $s+t+u=-16/\alpha'$.
- **Path-integral weight and propagator signs.** $Z=\int\mathcal D\Psi\,\mathcal D\Sigma
  \;e^{S}$, so every propagator is $-(\text{kinetic form})^{-1}$. For $\Sigma$ this is
  derived in §2.1: kinetic $-\tfrac{g_s^2}{4!}V_4(\Sigma,\Sigma)$ gives
  $+\tfrac{12}{g_s^2}V_4^{-1}$. For $\Psi$ the same rule applied to
  $+\tfrac12V_2(\Psi^2)$ gives $\mathsf P=-V_2^{-1}$; the finite-dimensional model
  therefore writes the $\Psi$-kinetic form as $-\tfrac12\Psi^\top K\Psi$, i.e.
  $V_2(\Psi^2)=-\Psi^\top K\Psi$, and $\mathsf P=+K^{-1}$ (script l. 218). The two
  propagators are thus given by *one* rule, not two; the sign is absorbed in $V_2$, and
  saying so matters because the relative sign between the $s,t,u$ poles and the contact
  term is physical in Claim ON (it cancels in Claim OFF, where both theories share the
  $\Psi$ rules).
- Correlators by Wick contraction; the project's notes carry no explicit $\mathrm i$'s. The
  comparison (0.2) is a *ratio* statement between two theories computed with identical
  rules, so the overall convention ($\mathrm i$'s, $(2\pi)^d\delta^{(d)}$ factors inside
  $V_n$) drops out; only the rational prefactor chain is at stake, and it is computed
  explicitly (§2–3).
- **Amplitude normalization (used throughout, vs R14's action normalization).** For
  four *generic distinct* external states, define
  $$
  A_4(\Psi_1,\dots,\Psi_4)
    :=\Gamma_4(\Psi_1,\dots,\Psi_4)
    =\partial_{t_1}\partial_{t_2}\partial_{t_3}\partial_{t_4}
    \log Z[J(t)]\Big|_{t=0},
  \qquad J(t)=V_2\Big(\textstyle\sum_i t_i\Psi_i,\;\cdot\Big),
  \tag{1.1}
  $$
  the connected 4-point function with each external leg amputated onto the state
  $\Psi_i$ (the source $J=V_2(\Psi_{\rm ext},\cdot)$ cancels the external propagator
  exactly — the "source-shift trick" of the companion script, where it is implemented
  as $\Psi\to\bar\Psi+\sum_it_i\Psi_i$). *The two implementations are different
  generating functionals* — the source version carries the free $-\tfrac12JK^{-1}J$
  piece, the shift version does not — and they agree on exactly the part (1.1) selects:
  the coefficient of $t_1t_2t_3t_4$ with four *distinct* external states, since the free
  piece is quadratic in $J$ and contributes only to $\partial_{t_i}\partial_{t_j}$.
  Everything below uses only that multilinear part. In this normalization every tree diagram on
  distinct externals has symmetry factor 1, and the action's $1/n!$'s are eaten by the
  leg-assignment sums; the *residual* rational factors are then exposed explicitly
  rather than hidden in conventions. R14 computed the same object for the
  $\Sigma$-sector only; here the full $O(g_s^2)$ assembly, $V_3$ sector included, is
  done in this normalization (new; machine-checked, script check 1). On-shell,
  $Q\Psi_i=0$, (1.1) is the tree-level S-matrix element up to the universal external
  normalization common to both theories.
- **Statistics and symmetry.** Physical $N_{\rm gh}$ grading (R7): $\Psi$ at
  $N_{\rm gh}=2$, $\Sigma$ at $N_{\rm gh}=4$, both Grassmann-even; the combinatorics is
  literally bosonic. $V_4$ carries full graded $S_4$ symmetry. **This is a defining
  property of a vertex family, not a hypothesis of this chain** (ledger header
  annotation of 2026-07-01, which closes the old "H2"): a family whose quartic vertex
  were not totally symmetric would not define a closed-SFT action in the first place.
  It is therefore *not* counted among H1–H3 below, and it is stated here once rather
  than re-flagged at (3.4). **To avoid the naming collision with the ledger's old "H2"
  we call it $S_4$-symmetry throughout, and reserve H1/H2/H3 for the amplitude
  hypotheses below** (the plan's and the paper's usage). Any promotion of this record
  to a ledger row must carry this renaming note, since R7–R13's prose still uses "H2"
  in the old sense.
- **State space.** $\mathcal H_0=\ker L_0^-\cap\ker b_0^-$ is the off-shell
  level-matched space (R9), and $\operatorname{Sym}^2\mathcal H_0$ means the pair is
  level-matched **strand by strand**: each of the two strands separately satisfies
  $L_0^-=b_0^-=0$, as the colour-2 contraction's $\omega_1^{-1}=b_0^-\delta_{L_0^-,0}$
  per strand requires (RS4/021, R27 item 1). Total level-matching alone would be a
  larger space and a different H2.
- **$m_2$ dictionary.** $m_2:\operatorname{Sym}^2\mathcal H_0\to
  \operatorname{Sym}^2\mathcal H_0$ is defined through the pairing
  $G_2=\omega_1^{\otimes2}$ (R7) by $V_4(A,B)=G_2(A,m_2B)$, i.e. $m_2=G_2^{-1}V_4$ as
  operators; the $\Sigma$-propagator can be written either as
  $(12/g_s^2)(V_4|_{\operatorname{Sym}^2})^{-1}$ (R14) or as
  $(12/g_s^2)\,m_2^{-1}G_2^{-1}$ (R27) — identical objects. In the degenerate case both
  are pseudo-inverses on the quotient (script check 2 verifies the $m_2$-form
  pseudo-inverse telescopes with a *non-diagonal* $G_2$, extending R14 §6 which had
  Euclidean pairing only).
- **Finite-dimensional layer vs CFT layer.** As in R7–R14: everything combinatorial
  (enumeration, prefactors, telescoping) is *proven* on a finite-dimensional model
  $\mathcal H_0\cong\mathbb R^N$ and machine-checked; the two places where the
  infinite-dimensional CFT statement is genuinely stronger are isolated as H1/H2.

### The three hypotheses (named once, used at flagged steps in §3–§4)

H1 and H2 carry the off-shell claim (4.1); H3 is needed only for the on-shell reduction
(4.3). Each is stated with its motivation and with what would falsify or discharge it.
Nothing else in the chain is hypothetical: $S_4$-symmetry is a defining property of the
vertex family (above), and the rest is proven algebra.

- **H1 (kernel quotient).** $m_2$ descends to an injective map on
  $\operatorname{Sym}^2\mathcal H_0/\ker V_4$, and at each truncation level the
  descended map is invertible there, so that $m_2^{-1}$ is defined on the truncated
  quotient and $m_2^{-1}m_2=\mathrm{id}$ (equivalently, the projector along
  $\ker V_4$ on $\operatorname{Sym}^2$). The
  kernel is harmless *by construction*: any $\Xi\in\ker V_4|_{\operatorname{Sym}^2}$
  satisfies $V_4(\Xi,\cdot)=0$, so the source *functional* of the $\Sigma$-sector
  annihilates it identically and it appears in neither the $\Sigma$-kinetic term nor
  the source (given $S_4$-symmetry); it is a zero-action **decoupled spectator**
  (R9/R13, ledger annotation 2026-07-01; R27 item 5 context) and the exchange never
  routes flux through it (R14 §6; script check 2). Note that this argument is
  *inner-product-free*: it is the vanishing of a linear functional on $\ker V_4$, not
  an orthogonality statement. That matters, because $G_2=\omega_1^{\otimes2}$ is
  indefinite (two $c_0^-$ insertions, BPZ) and R15's carve-out records "canonical inner
  product open": **the decoupling of $\ker V_4$ needs no auxiliary positive metric**.
  The analytic content stated next does not need one either, as the following
  paragraph explains.

  **No auxiliary inner product is used** (restated 2026-09-22; the earlier version of
  this record fixed a positive-definite Fock-space form and asserted closed range with
  a bounded inverse in it). Two reasons, one of principle and one of economy.
  *(i)* The string field space carries the BPZ form $G_2=\omega_1^{\otimes2}$, which is
  indefinite (ghosts, timelike oscillators); positivity holds only on the BRST
  cohomology. A positive-definite form on the whole Fock space — the oscillator
  monomials declared orthonormal, i.e. the fundamental norm of a Krein structure —
  does exist, but it is neither Lorentz- nor BRST-invariant, so a statement such as
  "the smallest singular value drifts to zero with the level" is frame dependent: a
  boost preserves the level grading but does not act uniformly boundedly on it, and the
  drift can be created or removed by changing frame. A hypothesis *of the theory*
  should not rest on such a structure.
  *(ii)* The chain of §3 does not need one. What is used at (3.3) is
  $m_2^{-1}m_2P=P$ **modulo $\ker V_4$**: existence of a solution $X$ of $m_2X=m_2P$ is
  trivial ($X=P$), uniqueness modulo the kernel is the definition of the quotient, and
  the amplitude sees $X$ only through $V_4(\,\cdot\,,X)$, which is blind to the kernel
  by the decoupling paragraph above. No norm, no continuity of $m_2^{-1}$, and no
  bounded inverse enter. "Closed range with a bounded inverse" was strictly stronger
  than what the physics uses. (The one place where an analytic input *is* needed — the
  interchange of the intermediate-state sum with the action of $m_2^{-1}$ at
  (3.2)→(3.3) — belongs to H2 and is stated there, not here.)

  **What H1 asserts**, beyond the purely formal quotient (given existence of the
  inverse on the quotient, "$m_2^{-1}m_2=\mathrm{id}$ there" is a tautology), is that
  the quotient and its inverse survive the limit of the level truncation in which the
  theory is actually defined and computed. Two clauses:

  - **(a) Compatibility of level truncation with the quotient.** The kernels of the
    level-truncated forms stabilize,
    $\ker V_4^{(L)}=\ker V_4\cap\{\text{level}\le L\}$ for $L$ large enough at the
    external data considered, so that the quotient
    $\operatorname{Sym}^2\mathcal H_0/\ker V_4$ and the $\Sigma$-propagator defined
    level by level have a limit. At each truncation level the descended map is
    invertible on the truncated quotient, so that $m_2^{-1}$ is defined there and
    $m_2^{-1}m_2=\mathrm{id}$; the clause asks that this survive the limit. The
    $\Sigma$ Gaussian integral on the quotient is
    understood at the formal level of any string field theory path integral — no
    measure-theoretic claim is made or needed.
    The kernel here is the exact one; the clause makes no reference to near-null
    directions and therefore needs no norm. In a numerical test the rank of
    $V_4^{(L)}$ must nonetheless be decided, by exact/rational arithmetic where the
    vertex data allow it, and otherwise at a stated singular-value threshold in the
    basis of the conditioning diagnostic below — in which case the threshold is part
    of the test, not of the hypothesis, and a rank verdict sensitive to it counts as
    inconclusive rather than as a falsification.
  - **(b) On-shell clause.** At the external momenta actually used, the four-tachyon
    mass shell of (4.3) included, the truncated determinant on the quotient has no zero
    that persists as the level grows. This is part of the hypothesis, not a corollary
    of (a): $V_4$, and hence $m_2$, is a family of operators depending on the external
    momenta, and the on-shell locus is exactly where the generic statement is not
    available.

  *Motivation:* what the chain uses is algebraic and holds at every finite level, where
  $V_4^{(L)}$ is a finite symmetric matrix and the quotient is linear algebra; level
  truncation is the working definition of closed- and open-SFT computations and has
  converged in every case where it has been tested [Moeller–Taylor, arXiv:hep-th/0002237,
  see §References]; and the kernel is a decoupled zero-action spectator (R9/R13, ledger
  header annotation 2026-07-01), so quotienting it changes no amplitude at any level.
  For (b): PH5 of the ledger has $\ker V_4=0$ on $\operatorname{Sym}^2\mathcal H_0$ at
  generic momentum, off shell, for a generic member of the vertex family — with the
  annotation "genericity over families is a remedy, not evidence" (critic F9), so the
  support is weaker than the bare citation suggests, and the on-shell locus is precisely
  outside PH5's stated scope. No selection rule forces a kernel there, and an accidental
  one is codimension one in the vertex family, so non-degeneracy is the generic
  situation; the open question is only whether the on-shell locus is one of the special
  loci where it fails, the zero-momentum ghost-dilaton block being the known example of
  such a locus.
  *Would be falsified by:* a kernel that does not stabilize — new null vectors of
  $V_4^{(L)}$ appearing at arbitrarily high level that do not lie in $\ker V_4$, so that
  the level-by-level quotients have no limit; or, for (b), a zero of
  $\det V_4^{(L)}(P^2)$ sitting on the four-tachyon shell and persisting as $L$ grows.
  The second falsifier is concrete rather than rhetorical: ledger PH18 asserts that
  $\det V_4^{(L)}(P^2)$ *does* have zeros, with no known reason for them to avoid any
  particular locus, so nothing available excludes the tachyon shell a priori.
  *Would be discharged by:* the level-truncated kernel dimensions of the $(V_4,G_2)$
  data stabilizing with $L$ (RS6 hand-off), and the level-truncated determinant data of
  task 16b evaluated on the shell. In the finite-dimensional model both clauses are
  vacuous (a pseudo-inverse exists for any symmetric matrix, check 2; there is no
  sequence of levels); the content lives only in the limit.

  **Conditioning diagnostic (explicitly *not* part of H1).** The smallest nonzero
  singular value of the level-truncated $m_2=G_2^{-1}V_4$, computed in the Euclidean
  norm of the coefficient vectors in the oscillator basis
  $e_I=\mathrm{Sym}(\lambda_a\otimes\lambda_b)$ of
  `knowledge/rs6-spec-for-companion-project-2026-07-14.md` §2, remains a useful
  **numerical conditioning diagnostic** for level-truncated work: it is what controls
  the accuracy with which the truncated propagator can be applied. It is basis- and
  frame-dependent (the basis norm is neither Lorentz- nor BRST-invariant), so its drift
  refutes nothing by itself and is not a falsifier of H1 or of any other hypothesis of
  this record.
- **H2 (completeness of the $\operatorname{Sym}^2$ intermediate state sum).** The
  composition [vertex ∘ propagator ∘ vertex] in the $\Sigma$-exchange is a sum over a
  complete set of intermediate two-string states of $\operatorname{Sym}^2\mathcal H_0$:
  inserting the resolution of the identity $\sum_I|\lambda_I\rangle\langle\lambda_I|$
  between the blocks must converge on the vectors $m_2P$ produced by the external
  sources, and satisfy the Gram identity
  $\sum_{K,L} G_{IK}(G^{-1})^{KL}G_{LJ}=G_{IJ}$ with the *full* sum.

  **Interchange clause (added 2026-09-22, when H1 was restated without an inner
  product).** The convergence is required in the form that permits the intermediate
  sum and the action of $m_2^{-1}$ to be interchanged at (3.2)→(3.3): writing
  $s_N(P,Q)=\sum_{I\le N}V_4\big(P,\,m_2^{-1}\lambda_I\big)\,\langle\lambda_I,\,m_2Q\rangle$
  for the partial sums of the inserted resolution, the numerical sequence $s_N(P,Q)$
  converges to $V_4(P,Q)$ for the external data used. This is convergence of numbers,
  not of vectors: no norm on the string field space is fixed, and none is needed. It
  presupposes that $m_2^{-1}\lambda_I$ is defined, which is the level-by-level
  invertibility of clause H1(a) — see H1. This is the only analytic input the
  telescoping step has, and it is an input about the *sum*, not about the inverse. It
  is recorded under H2 rather than H1 because it is a property of the state sum and is
  discharged or falsified by the same saturation data. *Would be falsified by:* a
  sequence $s_N$ that fails to settle, or settles away from $V_4(P,Q)$, while the state
  sum itself saturates.

  **What is summed.** Not a level sum alone. Per the 2026-09-14 annotation on R27
  (R33) and derivation 031 §4.3/§7, the pair-state sum on a colour-2 edge is the
  untwisted-sector neck sum of the doubled ($\mathbb Z_2$-orbifold) theory, and it
  **carries the cover's loop momentum**: the sum runs over oscillator levels of the two
  strands *and* over the pair's relative momentum $k_a$ (with
  $k_b=-k_1-k_2-k_a$), i.e. it is a discrete level sum times a continuous
  $\int d^Dk_a$. H2 is the statement that *this* combined sum — levels and relative
  momentum — is complete and convergent on $m_2P$. At a fixed level truncation the
  level part is a finite sum; the momentum integral is not truncated by level and its
  convergence on $m_2P$ is a genuine analytic condition even in the truncated theory.
  (The finite-dimensional model of §1's last bullet and of the script suppresses the
  momentum direction; its check 6 therefore probes the level part of H2 only.)

  *Motivation:* the same resolution of the identity is the standard closed-string
  factorization/sewing-completeness input on an ordinary neck, where it is established
  CFT technology; the colour-2 edge differs from an ordinary neck by being frozen
  ($q=1$, no $s$-integral), which removes a damping factor $e^{-sL_0^+}$ but not the
  state sum's structure, so the burden is convergence, not existence. R15's spectral
  data on the level-0 block and the orbifold reading of 031 §5.1 both point the same
  way. *Would be falsified by:* the saturation of the partial sums over $m_2P$ failing
  to converge, or drifting without settling, as the truncation level grows — Phase B3
  of the amplitude plan / RS6 hand-off; or, for the momentum part, a divergence of
  $\int d^Dk_a$ at fixed external momenta, which would show up as a pair-channel
  threshold singularity absent from the standard amplitude (031 §4.3). *Would be
  discharged by:* a proof that the frozen-neck resolution of the identity converges on
  the image of $m_2$, which is A2(iii) territory. Script check 6 exhibits the
  finite-dimensional shadow of the level part: deleting a single intermediate state
  breaks the collapse, so the hypothesis is load-bearing, not decorative.
- **H3 (covering of $\mathcal M_{0,4}$).** For the chosen vertex family, the three
  plumbing Feynman regions and the fundamental vertex region $\mathcal V_{0,4}$ cover
  $\mathcal M_{0,4}$ exactly once. Used **only** at (4.3), never off shell.
  *Status and motivation:* for minimal-area and hyperbolic families this is the
  standard construction and is not in doubt [Zwiebach 1992, arXiv:hep-th/9206084;
  Erbin 2023; for the hyperbolic case, Costello–Zwiebach, arXiv:1909.00033, and
  Fırat, arXiv:2102.03936, see §References]. For the SL(2,C) family H3 is supported but not closed in the interior (R2, R37).
  *Would be falsified by:*
  an overlap or a gap in the union of the four regions at some point of
  $\mathcal M_{0,4}$ for the SL(2,C) family, or by an obstruction to the
  $S_4$-covariant assembly of the SL(2,C) family.

These are the hypotheses the paper's limitations table must carry: H1 and H2 for the
off-shell claim, H1–H3 for the on-shell one. The amplitude section adds no stronger
hypothesis and silently drops none. $S_4$-symmetry is *not* on this list: it is a
defining property of the vertex family (§1, Statistics and symmetry).

---

## 2. A1 — HS Feynman rules to 4-point, assembled once

### 2.1 Rules from `eq:SHS`, with $g_s$-orders

| element | value | $g_s$-order | legs |
|---|---|---|---|
| $\Psi$-propagator | $\mathsf P=(b_0^+/L_0^+)\,\omega_1^{-1}$, $\;\omega_1^{-1}=b_0^-\delta_{L_0^-,0}$ (RS4/021; $=K^{-1}$ in the finite model) | $g_s^0$ | 2 $\Psi$ |
| $\Sigma$-propagator | $\dfrac{12}{g_s^2}\,\big(V_4|_{\operatorname{Sym}^2}\big)^{-1}=\dfrac{12}{g_s^2}\,m_2^{-1}G_2^{-1}$ (R14 eq. A.4; R27 item 1) | $g_s^{-2}$ | 2 $\Sigma$ |
| cubic vertex | from $\tfrac{g_s}{3!}V_3(\Psi^3)$: on distinct externals, $g_s\,V_3(\Psi_i,\Psi_j,\cdot)$ | $g_s^{1}$ | 3 $\Psi$ |
| $\Sigma\Psi\Psi$ vertex | from $\tfrac{2g_s^2}{4!}V_4(\Sigma,\Psi^{\otimes2})$: $\dfrac{g_s^2}{6}\,V_4(\,\cdot\,,\Psi_i\!\otimes\!\Psi_j)$, $i\neq j$ (R14 eq. A.5) | $g_s^{2}$ | 1 $\Sigma$ + 2 $\Psi$ |
| $\Sigma$ self-coupling | none at this order ($\Sigma$ purely quadratic in (0.1); the tower vertices $V_5(\Sigma_2,\Sigma_2,\Psi),V_6(\Sigma_2^3),\dots$ of R12/R25/R26 enter at $O(g_s^3)$ and beyond) | — | — |

The two factor-2 traps of R14 are inherited, not re-derived: the vertex factor
$g_s^2/6$ (not $g_s^2/12$) from the two slot assignments, and the propagator defined
w.r.t. the **symmetric identity** on $\operatorname{Sym}^2$ (the D-cancellation
multiplicity lemma of R14 §2 governs any unordered-pair bookkeeping).

### 2.2 Enumeration lemma (all connected 4-point diagrams at $O(g_s^2)$)

**Lemma.** The connected 4-point $\Psi$-amplitude of (0.1) at $O(g_s^2)$ receives
contributions from exactly four diagrams: the three $V_3$-exchange trees ($s,t,u$
matchings) and the single $\Sigma$-exchange tree. No loop, tadpole, or mixed diagram
contributes at this order.

*Proof (counting).* Let $n_3$ = number of cubic vertices, $n_B$ = number of
$\Sigma\Psi\Psi$ vertices, $I_\Psi,I_\Sigma$ = internal lines, $E=4$ external $\Psi$.
Since $\Sigma$ is internal-only and each $\Sigma$-line ends on two $\Sigma\Psi\Psi$
vertices: $n_B=2I_\Sigma$. Total $g_s$-order $=n_3+2n_B-2I_\Sigma=n_3+2I_\Sigma
\overset{!}{=}2$, so $(n_3,I_\Sigma)\in\{(2,0),(0,1)\}$ — **any** connected diagram,
loops included. $\Psi$-leg count $3n_3+2n_B=4+2I_\Psi$ then fixes $I_\Psi=1$ resp.
$0$, and the loop number $L=(I_\Psi+I_\Sigma)-(n_3+n_B)+1=0$ in both cases: tree
topology is *forced* by the order and the four externals, not assumed.
$(2,0)$: two cubic vertices, one internal $\Psi$-line, three matchings — the $s,t,u$
channels. $(0,1)$: two $\Sigma\Psi\Psi$ vertices, one $\Sigma$-line, three matchings —
the $\Sigma$-exchange. Exclusions for free: a $\Psi$-tadpole needs an odd leg count at
$O(g_s)$ (one-loop, wrong order); a $\Sigma$-tadpole $\langle\Sigma\rangle$ vanishes
(Gaussian, zero mean; equivalently a single $B$-insertion is odd in $\Sigma$);
disconnected pieces are removed by the $\log$ in (1.1); the $\Sigma$-Gaussian
determinant is field-independent regardless of signature (R14 §4) and cancels in the
normalized correlator. $\square$

This is the R17-style completeness argument the plan asked for; its mechanical
counterpart is script check 1, where the *entire* $O(g_s^2)$ generating functional is
expanded from the joint $(\Psi,\Sigma)$ Gaussian with **no diagram input** — the
$k\le2$ truncation of $e^{S_{\rm int}}$ used there is justified by exactly this
counting ($k\ge3$ terms are $O(g_s^3)$ after $\Sigma$-Wick or vanish as odd moments).

### 2.3 The assembled amplitude, every prefactor explicit

On distinct externals, in amplitude normalization (1.1):

$$
A_4^{\rm HS}
=\underbrace{\sum_{\{ij|kl\}} g_s V_3(\Psi_i,\Psi_j,\cdot)\;\mathsf P\;
g_s V_3(\cdot,\Psi_k,\Psi_l)}_{\text{(a) three }V_3\text{ channels}}
\;+\;\underbrace{\sum_{\{ij|kl\}}\frac{g_s^2}{6}V_4(\,\cdot\,,\Psi_i\Psi_j)
\;\frac{12}{g_s^2}\,m_2^{-1}G_2^{-1}\;\frac{g_s^2}{6}V_4(\,\cdot\,,\Psi_k\Psi_l)}_{\text{(b) three }\Sigma\text{-exchange matchings}},
\tag{2.1}
$$

with $\{ij|kl\}$ running over the three perfect matchings $\{12|34\},\{13|24\},
\{14|23\}$ in both sums, and *no other* rational factors: the $\tfrac12\times2$
exponential/assignment cancellation and the absence of residual symmetry factors on
distinct externals are R14 §3 (hand-confirmed by the R14 critic), and are re-verified
here in the presence of the $V_3$ sector by the mechanical expansion (script check 1:
the $\partial_t^4\log Z$ coefficient equals (2.1) term by term; the $O(g_s)$ 3-point
coefficient simultaneously confirms the $g_sV_3$ vertex normalization; dropping one
$V_3$ channel breaks the match — check 4d — so the comparison has teeth).

Sum (a) is *identical, diagram by diagram*, in $S_{\rm HS}$ and in the
quartic-truncated standard action
$S_{\rm eff}=\tfrac12V_2+\tfrac{g_s}{3!}V_3+\tfrac{g_s^2}{4!}V_4(\Psi^{\otimes2},
\Psi^{\otimes2})$ (both theories share every $\Psi$-sector rule). The entire content
of the comparison is sum (b) vs the contact kernel
$g_s^2V_4(\Psi_1,\Psi_2,\Psi_3,\Psi_4)$ of $S_{\rm eff}$ — §3.

---

## 3. A2 — the telescoping step, with H1/H2 displayed at the point of use

Take one matching in sum (b), external pair tensors
$P=\operatorname{Sym}(\Psi_i\otimes\Psi_j)$, $Q=\operatorname{Sym}(\Psi_k\otimes\Psi_l)$
(only the symmetric parts couple, by $S_4$-symmetry). The chain, one non-trivial
equality per line:

$$
\begin{aligned}
A_4^{(ij|kl)}
&=\frac{g_s^2}{6}\,V_4(\,\cdot\,,P)\;\circ\;\frac{12}{g_s^2}\,m_2^{-1}G_2^{-1}
\;\circ\;\frac{g_s^2}{6}\,V_4(\,\cdot\,,Q)
&&\text{(2.1b, one matching)}
\\[2pt]
&=\frac{g_s^2}{3}\,V_4\Big(\,\cdot\,,P\Big)\;m_2^{-1}G_2^{-1}\;G_2\big(\,\cdot\,,m_2Q\big)
&&\text{(3.1: def.\ of }m_2\text{)}
\\[2pt]
&=\frac{g_s^2}{3}\,V_4\Big(P,\;m_2^{-1}G_2^{-1}\,G_2\,m_2\,Q\Big)
&&\text{(3.2: intermediate state sum — \textbf{H2 used here})}
\\[2pt]
&=\frac{g_s^2}{3}\,V_4\big(P,\;m_2^{-1}m_2\,Q\big)
=\frac{g_s^2}{3}\,V_4(P,Q)
&&\text{(3.3: }m_2^{-1}m_2=\mathrm{id}\text{ on the quotient — \textbf{H1 used here})}
\\[2pt]
&=\frac{g_s^2}{3}\,V_4(\Psi_1,\Psi_2,\Psi_3,\Psi_4)
&&\text{(3.4: }S_4\text{-symmetry, matching-independent)}
\end{aligned}
$$

and summing the three matchings, $A_4^{\Sigma\text{-exch}}=3\times\tfrac{g_s^2}{3}V_4
=g_s^2\,V_4(\Psi_1,\Psi_2,\Psi_3,\Psi_4)$ — exactly the contact kernel of
$S_{\rm eff}$, coefficient 1 (R14 eq. A.9–A.10; the factor chain
$3\cdot\tfrac16\cdot12\cdot\tfrac16=1$).

**Commentary, step by step.**

- **(3.1)** — the *second* vertex, with its own $\mathcal V_{0,4}$ moduli integral
  already performed, is written through the pairing: $V_4(\cdot,Q)=G_2(\cdot,m_2Q)$.
  This is R27 item 4's reading: each vertex's moduli integral, once done, equals $G_2$
  applied to $m_2$ of the bare external pair. Geometrically nothing is "half-cancelled":
  the collapse below removes one whole vertex's $m_2$-factor and leaves a single
  freshly-saturated $\mathcal V_{0,4}$ integral (why $\dim_{\mathbb C}=1$ survives out
  of the naive $1+1=2$).
- **(3.2)** — the composition of the three blocks is a sum over intermediate
  two-string states of $\operatorname{Sym}^2\mathcal H_0$. **This is where H2 acts**:
  at CFT level that sum — over the two strands' levels *and* over the pair's relative
  momentum, per R33/031 §4.3 (§1, H2) — must be complete and convergent on $m_2Q$ (the vector the resolution of the identity
  acts on in (3.1)–(3.3); §1 and §7 state the same condition for a generic external pair,
  written $m_2P$ there, the two pairs playing symmetric roles). A
  level truncation makes the level part finite and exact but does not touch the
  momentum integral. That integral leaves no trace in the collapsed answer because what
  is inserted is a resolution of the identity on the *whole* pair space, momentum
  direction included: $G_2^{-1}G_2=\mathrm{id}$ saturates it against the neighbouring
  vertex rather than leaving an unmatched integration. This is why PH9's objection
  elsewhere in the ledger — that "the relative-momentum sum has no counterpart in the
  tree integrand" — does not bite here: there the sum is being matched to a tree
  integrand term by term, while here it is summed out in one step, and what survives is
  the convergence requirement recorded in H2, not a leftover integral. Script check 6
  shows the shadow of the level part: deleting
  one intermediate state breaks the equality (the hypothesis is load-bearing, not
  decorative).
- **(3.3)** — the collapse $m_2^{-1}m_2=\mathrm{id}$ is an *algebraic* step, not a
  geometric one (R27 item 4). **This is where H1 acts**: $Q$ enters mod
  $\ker V_4$, and the kernel components are unsourced decoupled spectators (R14 §6;
  script check 2 with non-diagonal $G_2$: source $\perp\ker$, pseudo-inverse
  telescopes, exchange still equals contact). No stronger hypothesis (e.g. strict
  invertibility on all of $\operatorname{Sym}^2$) is needed — and, since 2026-09-22, no
  auxiliary inner product either: existence of a solution of $m_2X=m_2Q$ is trivial
  ($X=Q$), uniqueness modulo $\ker V_4$ is the definition of the quotient, and $V_4(P,X)$
  is blind to the kernel. What H1 supplies here is not boundedness of $m_2^{-1}$ but the
  level-uniformity of the quotient it acts on (§1, H1(a)–(b)).
- **(3.4)** — full $S_4$-symmetry makes the three matchings equal; this is a defining
  property of the vertex family, not a hypothesis of this chain (§1), but it is
  load-bearing exactly here (R14 §3): pair-exchange
  symmetry alone would leave the matchings unequal. Note with R27 item 5: the three
  $\Sigma$-channels each reproduce the *whole* of $\mathcal V_{0,4}$ — the
  $3\times\tfrac13$ bookkeeping is combinatorial (symmetry factors), NOT a geometric
  tiling like the genuinely disjoint $s,t,u$ plumbing regions.

### Regime of validity (exactly where the identity is exact algebra vs where H1/H2 work)

- **The finite-dimensional model (level truncation with the momentum direction
  suppressed):** (3.2) is a finite sum, (3.3) holds for the Moore–Penrose
  pseudo-inverse of *any* symmetric $V_4$ — the whole chain is an identity of finite
  matrix algebra with **no physics input**. This is the tautology trap (§5.1): in that
  model a numerical comparison of exchange vs contact cannot fail and verifies nothing.
- **A level truncation of the actual theory:** the level part of (3.2) is finite, but
  the intermediate sum still carries $\int d^Dk_a$ over the pair's relative momentum
  (§1, H2), which the level truncation does not touch. The collapse is therefore *not*
  a finite matrix identity there, and whether a truncated comparison carries information
  is open; what it could test is the convergence of that momentum integral on $m_2P$ at
  fixed level.
- **CFT level (infinite-dimensional):** (3.2) requires H2 (completeness/convergence of
  the combined level-and-momentum sum — spectral input, A2(iii)/RS6 — **including the
  interchange clause**: the scalar partial sums
  $s_N(P,Q)=\sum_{I\le N}V_4(P,m_2^{-1}\lambda_I)\,\langle\lambda_I,m_2Q\rangle$ must
  converge to $V_4(P,Q)$, which is the only analytic input of the telescoping step);
  (3.3) requires H1
  (stabilization of $\ker V_4^{(L)}$ so that the quotient and its inverse have a level
  limit, and no persistent on-shell zero at the momenta used — §1, restated 2026-09-22
  without any auxiliary inner product; R15's Schwinger form is a stronger, norm-dependent
  statement that is *not* assumed here).
  For the *off-shell* chain of this section these are the only two inputs beyond
  the vertex family's defining properties ($S_4$-symmetry among them); everything else
  here is proven. The on-shell reduction of §4 adds one more, H3 (covering of
  $\mathcal M_{0,4}$), which plays no role in §3.
- **Beyond 4 points / all orders in $t$:** because $\Sigma$ enters (0.1) only
  quadratically, the Gaussian statement $Z_{\rm HS}[J]=\mathcal N\,Z_{\rm eff}[J]$
  ($\mathcal N$ field-independent) holds with all Green's functions equal (R14 §4).
  Three scopes must be kept apart here. (i) The Gaussian statement itself is exact in
  the externals and in the topology: it is an identity of generating functionals.
  (ii) Script check 1 verifies it at $O(g_s^2)$ at all orders in the external sources
  $t_i$ — including the terms with fluctuation contractions, which in the
  finite-dimensional model are the analogue of loop terms and which 007's check 2 did
  not exercise (no $V_3$ sector there). (iii) The §2.2 enumeration, by contrast, is a
  statement about the *four-external, $O(g_s^2)$* sector only, where it shows tree
  topology is forced. (ii) does not contradict (iii): (ii) tests orders in $t$ other
  than four, where loop topologies do occur, while (iii) counts at four externals.
  Higher orders in $g_s$ (the $\Sigma$-tower) are Phase-B/R25–R26 territory, out of
  scope here; note in particular that R38 restricts the $\ker V_4$ quotient's
  compatibility to $O(g_s^2)$, so none of this section may be extended past that order
  without R38's condition $V_5(\ker V_4,\operatorname{Sym}^2\mathcal H_0,\mathcal H_0)=0$.

---

## 4. A3 — the standard-SFT endpoint: two claims, sharply distinguished

$S_{\rm eff}$ is nothing but the standard closed bosonic SFT action truncated at
quartic order, for the chosen geometric vertex family. The chain (0.2) therefore ends
on two claims of different strength:

**Claim OFF (off-shell equality — the stronger, scheme-relevant statement).**
*For arbitrary (generic, off-shell) external states and the same vertex family,*
$$
A_4^{\rm HS}(\Psi_1,\dots,\Psi_4)\;=\;A_4^{\rm SFT,\;off\text{-}shell}(\Psi_1,\dots,\Psi_4)
\qquad\text{at }O(g_s^2),\ \text{given H1–H2.}
\tag{4.1}
$$
Status: **proven at the algebraic layer** (§2–3 + R14 §4's exact Gaussian statement,
machine-checked at all orders in the externals — script check 1), **conditional on
H1–H2 at CFT level**. This is scheme-relevant in the standard sense: off-shell
amplitudes depend on the vertex family and local-coordinate/stub choices; (4.1) says
the HS rewriting introduces *no new scheme dependence whatsoever* — the two theories
have identical off-shell Green's functions, not merely identical S-matrices.

**From (4.1) to the on-shell locus.** (4.1) is stated for generic off-shell externals,
while (4.3) evaluates it on four on-shell tachyons — a non-generic locus. Four
observations close the gap; the third is a declared part of H1 and H2, and it is a real
condition, not a formality, and the fourth is the analytically delicate one. First, the telescoping step (3.1)–(3.4) is *algebraic and multilinear in the external
states*: nothing in it uses genericity, so it holds wherever both sides are defined,
the on-shell locus included. Second, the channel poles are common to both sides: the
three $V_3$ channels are literally the same diagrams in both theories, built from the
same $\Psi$ Feynman rules and the same propagator $\mathsf P$, so the $L_0^+\to0$
behaviour at the channel poles is identical and no limit has to be interchanged with
the telescoping. Third, what remains is momentum-dependent and must be assumed at the
on-shell momenta: H1 is a property of the operator $m_2$, which depends on the external
momenta through $V_4$, and H2 is a property of the state sum on the vectors $m_2P$,
which depend on them too. Accordingly **H1 and H2 are to be read as including the
external momenta used in (4.3)** — this is clause (b) of H1 in §1 and is covered for H2
by its formulation on $m_2P$.
Fourth — the one step of this passage that is genuinely singular on shell — the
amplitude normalization (1.1) amputates the external legs with the source
$J=V_2(\Psi_{\rm ext},\cdot)$, and that amputation degenerates on shell: $Q\Psi_i=0$
kills the numerator while the external $1/L_0^+$ blows up. The degeneration is not
removed here; it cancels because the claim is **relative**. Both theories amputate
with the *same* $J$ and the same external propagators — the $\Psi$ kinetic term and
the $\Psi$ Feynman rules are untouched by the HS rewriting — so the on-shell limit is
taken on the universal external normalization common to the two sides, in the standard
LSZ manner, and drops out of the equality (4.1)⇒(4.3). §1 states this in one clause
("On-shell, $Q\Psi_i=0$, (1.1) is the tree-level S-matrix element up to the universal
external normalization common to both theories"); it is asserted there, not derived,
and it is the point at which an absolute (as opposed to relative) on-shell statement
would require an LSZ argument this record does not give.

The honest motivation is genericity, not the finiteness of the vertex. That the moduli
integral defining $V_4$ runs over the vertex region and therefore stays finite and
analytic in the momenta on shell is a property of the *numerator*; what H1 needs is
non-degeneracy of $m_2$ *on the quotient, uniformly in the level*, and an analytic
family of operators can degenerate on a proper analytic subvariety without any loss of
analyticity. The support
is instead PH5 — $\ker V_4=0$ at generic momentum, off shell, for a generic member of
the vertex family, no selection rule forcing a kernel; the ledger's own annotation
("genericity over families is a remedy, not evidence") and the fact that the on-shell
locus lies outside PH5's stated scope both weaken this support —
together with the absence of any mechanism tying a degeneration to the tachyon shell.
Against that, ledger PH18 records that $\det V_4^{(L)}(P^2)$ has zeros with no known
reason to avoid a given locus, so the failure mode is concrete: a zero on the tachyon
shell persisting with the level. That is exactly the falsifier recorded with H1 in §1.
What is *not* claimed is uniformity over all of momentum space.

**Claim ON (on-shell reduction — cited, not re-derived).** For on-shell external
tachyons ($Q\Psi_i=0$, momenta on the tachyon mass shell, $D=26$), the standard-SFT
tree 4-point amplitude equals the moduli-space integral over $\mathcal M_{0,4}$,
**given H3** — the three plumbing Feynman regions and the fundamental vertex region
$\mathcal V_{0,4}$ cover $\mathcal M_{0,4}$ exactly once. H3 is standard for minimal-area
and hyperbolic families [Zwiebach 1992, arXiv:hep-th/9206084; Erbin 2023,
arXiv:2301.01686, chapters "Off-shell amplitudes" and "Closed string field theory"
(covering of moduli space); live draft `bos_offshell_amplitudes.tex`, `bsft_bv.tex`],
and for the SL(2,C) family of this project it is supported but not closed (R2,
R37 — §1, H3). Given the covering, that integral is the
Virasoro–Shapiro amplitude
$$
A_4^{\rm SFT}\Big|_{\rm on\text{-}shell,\ 4\ tachyons}
= A_{\rm VS}(s,t,u)
\;\propto\;
\frac{\Gamma(-1-\alpha's/4)\,\Gamma(-1-\alpha't/4)\,\Gamma(-1-\alpha'u/4)}
{\Gamma(2+\alpha's/4)\,\Gamma(2+\alpha't/4)\,\Gamma(2+\alpha'u/4)}
\tag{4.2}
$$
[textbook: Polchinski Vol. I §6.6 (closed-string tree amplitudes; the section title is
not checked here); Erbin 2023, tree-level scattering chapters, for the sphere 4-point
integral in the project's primary conventions]. Internal consistency check of (4.2):
for four tachyons $m^2=-4/\alpha'$, so $s+t+u=\sum_im_i^2=-16/\alpha'$; the three
numerator arguments then sum to $-3-\tfrac{\alpha'}{4}(s+t+u)=-3+4=1$ and the three
denominator arguments to $6+\tfrac{\alpha'}{4}(s+t+u)=6-4=2$, with
$1-(-1-\alpha's/4)=2+\alpha's/4$ term by term — i.e. (4.2) is exactly of the canonical
form $\prod\Gamma(a_i)/\prod\Gamma(1-a_i)$ with $\sum_ia_i=1$. Combining with (4.1):

$$
\boxed{\;A_4^{\rm HS}\Big|_{\rm on\text{-}shell,\ 4\ tachyons}=A_{\rm VS},
\qquad\text{conditional on H1–H3.}\;}
\tag{4.3}
$$

**Overclaim guard (A5 hunt item, stated as a constraint on the paper's wording).**
What is established is: *the cubic HS action reproduces the standard-SFT 4-point
amplitude (off-shell, same vertex family), and the latter is textbook-known to equal
Virasoro–Shapiro on-shell.* The chain does **not** re-derive Virasoro–Shapiro, does
not test the vertex family's covering property (that is H3 — inherited, R14 carve-out
(b); for the SL(2,C) family the ledger currently leaves it open in the interior, R2/R37), and does
not establish H1–H3 — it *names* them. Claim ON is
vertex-family-independent (on-shell amplitudes are); Claim OFF is the one carrying
scheme content.

**Completeness at this order, including the $\Sigma$-tower.** §2.2's enumeration is
proven for the action (0.1), which has no $\Sigma$ self-coupling. The tower vertices
($V_5(\Sigma,\Sigma,\Psi)$, $V_6(\Sigma^3)$, the dressed $W_6,\dots$ of R19/R25, the
all-orders structure R26) are not in that count, and the naive order estimate is
misleading because the $\Sigma$-propagator carries $g_s^{-2}$. Run the count in general
rather than on one diagram. A vertex with $a$ $\Sigma$-legs and $b$ $\Psi$-legs comes
from an $n=2a+b$-punctured vertex and carries $g_s^{p}$ with
$$
p(a,b)=2a+b-2
$$
(check on the rules of §2.1: $(a,b)=(0,3)\to g_s$, $(1,2)\to g_s^2$, $(2,1)\to g_s^3$ for
$V_5(\Sigma,\Sigma,\Psi)$, $(3,0)\to g_s^4$ for $V_6(\Sigma^3)$). A connected diagram
with $V$ vertices, $I_\Sigma$ $\Sigma$-propagators ($g_s^{-2}$ each), $I_\Psi$
$\Psi$-propagators ($g_s^0$), $E$ external $\Psi$ and no external $\Sigma$ satisfies
$\sum_va_v=2I_\Sigma$ and $\sum_vb_v=E+2I_\Psi$, so its order is
$$
\sum_v(2a_v+b_v-2)-2I_\Sigma
= E+2\big(I_\Sigma+I_\Psi-V\big)
= E+2L-2 ,
$$
with $L=I-V+1$ the loop number. **Order therefore excludes nothing at four externals:**
*every* four-external tree diagram is $O(g_s^2)$, whatever vertices it uses, and
conversely $E=4$ at $O(g_s^2)$ forces $L=0$. What excludes the tower is the *leg count*.
Eliminating $I_\Psi$ the same way gives, at tree level,
$$
E=\sum_v\big(a_v+b_v-2\big)+2 ,
$$
and every interaction vertex of the tower has $a_v+b_v\ge3$ (the only $a+b=2$ object,
$(a,b)=(2,0)$, is the $\Sigma$-kinetic term, not a vertex), so $E\ge V+2$. Call a
**tower vertex** any interaction vertex with $a_v\ge1$ other than the source
$V_4(\Sigma,\Psi^{\otimes2})$, i.e. $(a,b)$ with $a\ge2$, or $a=1$ and $b\ge3$. Both
cases push $E$ to at least $5$. If $a_v\ge2$: at tree level its $a_v$ $\Sigma$-legs
must run to $a_v$ distinct other vertices (two of them meeting at one vertex would
close a loop), so $V\ge a_v+1\ge3$ and hence $E\ge V+2\ge5$. If $a_v=1$ and $b_v\ge3$:
that vertex contributes $a_v+b_v-2\ge2$ to $E=\sum_v(a_v+b_v-2)+2$, and its single
$\Sigma$-leg must end on a second vertex, which contributes at least $1$ (every vertex
has $a+b\ge3$); hence $E\ge2+1+2=5$. There is thus no four-external tower
diagram at all at tree level — the cheapest one has five external legs, and by the order
formula it sits at $O(g_s^3)$ — and §2.2's four diagrams are exhaustive as claimed. Two caveats attach to any extension of this: the estimate above uses the
$O(g_s^2)$ Feynman rules, and R38 restricts the compatibility of the $\ker V_4$
quotient with $V_5$ to $O(g_s^2)$ unless
$V_5(\ker V_4,\operatorname{Sym}^2\mathcal H_0,\mathcal H_0)=0$ — so (4.3) needs no
statement about the tower, but $O(g_s^3)$ statements would need R38's condition first.

---

## 5. A4 — the tautology trap and its one genuine resolution

### 5.1 The trap, demonstrated (not just asserted)

The scope of this subsection is the **finite-dimensional model**: a level truncation in
which the pair's relative momentum is suppressed, so that the intermediate space is
finite-dimensional. That is the setting of the companion script, and it is the setting
in which the trap below is *proven*.

In that model all three objects of the exchange — $V_4$-Gram, $G_2$, $m_2^{-1}$
(pseudo-inverse) — satisfy the telescoping identity as exact matrix algebra.
Consequence: **a numerical check that assembles the truncated $\Sigma$-exchange and
compares it to the truncated quartic vertex verifies nothing** — it re-derives an
identity that cannot fail (plan §0). The companion script makes this
concrete rather than rhetorical (check 3): replacing the physical $V_4$ by five
*deliberately corrupted* random totally symmetric vertices — different rank, different
sign structure, no relation to any CFT — the truncated identities
$$
V_4'\,\big(V_4'\big)^{+}\,V_4'=V_4',
\qquad
A_4^{\Sigma\text{-exch}}[V_4']=g_s^2\,V_4'(\Psi_1,\dots,\Psi_4)
\tag{5.1}
$$
**pass identically on garbage input**. A check that passes on garbage carries no
information about the physics; the PASS of check 3 is the demonstration of vacuity.

What *is* falsifiable at the finite-dimensional layer is the **cross-object
consistency** — that the same $V_4$ appears in the $\Sigma$-kinetic term, the source,
and the comparison contact term, with the 2:1 source-to-kinetic ratio of `eq:SHS`, and
that the intermediate sum is complete. Script check 4 breaks each of these on purpose
and confirms failure: kinetic-vs-source $V_4$ mismatch (4a), source coefficient
$2\to1$ gives exactly $\tfrac14$ (4b, R14's quadratic sensitivity), a wrong $G_2$ in
the $m_2^{-1}G_2^{-1}$ form (4c), a dropped $V_3$ channel in the enumeration (4d);
check 6 deletes one intermediate state (H2's shadow). What these teeth certify must be
stated exactly: they certify the **coefficient and support content** of checks 1–2 —
that the rational prefactor chain, the 2:1 ratio, the pairing $G_2$ and the channel
enumeration are the ones claimed, since perturbing any of them makes the check fail.
They do **not** certify the **telescoping** content, which by the argument just given
cannot fail in the finite-dimensional model and is therefore untestable there by
construction. Checks 1–2 are thus non-vacuous as coefficient checks and vacuous as tests
of the collapse itself.

**What this does and does not say about a truncation of the actual theory.** The proof
above is a statement of finite matrix algebra, and it uses the finiteness of the
intermediate sum. A level truncation of the actual theory is not finite in that sense:
by §1's H2 the intermediate sum runs over the two strands' levels *and* over the pair's
relative momentum, and truncating the level does not truncate $\int d^Dk_a$. The
collapse at fixed level is then not a matrix identity, the argument of this subsection
does not apply to it, and **whether a comparison of exchange and contact at fixed level
carries information in the actual theory is open**. One thing such a comparison could
test is exactly the part the level truncation leaves alone: whether the relative-momentum
integral on $m_2P$ converges at fixed level, whose failure H2's falsifier of §1 describes
as a pair-channel threshold singularity absent from the standard amplitude. Settling that
is Phase B territory, not something this record establishes either way. Everything below
in §5.2, and the paper prose of §9, is stated for the scope proven here.

### 5.2 The resolution: the identity can only fail through the representation of $m_2^{-1}$

At CFT level the *off-shell* chain of §3 has exactly two open joints, H1 and H2 — both
statements about $m_2^{-1}$ and the state space it acts on. (The on-shell statement
(4.3) adds H3, a statement about the vertex family's geometry, not about $m_2^{-1}$;
it is not at stake in this section.) By **R28** (no-local-kernel theorem, *proven
modulo the standard CFT factorization/sewing-completeness input*, and — per the
ledger's 2026-09-21 re-scoping — an exclusion **within the class of connected surfaces
of bounded type carrying standard sewing ghost insertions**), $m_2^{-1}$ admits
no local geometric kernel *in that class*: no such surface integral reaches
$N_{\rm gh}(m_2^{-1})=-2$. So within the class there is no
"explicit worldsheet construction" of the propagator whose convergence could be tested
directly. Outside it, R28 excludes nothing: a dressing fine-tuned at the actual $V_4$
— explicit-ghost dressings and mixed tube/slice kernels, excluded by R28$'$ only as
constructions *uniform in the vertex data* — remains open. The Neumann/frozen-neck-chain
series (R27 item 3.ii) is the one surface representation known, and it evades R28
precisely because it is an infinite sum and so not of bounded type — outside R28's
class rather than the only representation within it:
$$
V_4\big|_{\operatorname{Sym}^2}=D-N,
\qquad
\big(V_4|_{\operatorname{Sym}^2}\big)^{-1}=\sum_{n\ge0}\big(D^{-1}N\big)^n D^{-1},
\qquad
m_2^{-1}=\sum_{n\ge0}\big(D^{-1}N\big)^n D^{-1}\,G_2,
$$
$$
\text{all three convergent iff }\rho(D^{-1}N)<1,
\tag{5.2}
$$
where the split is performed on the **Gram matrix of $V_4$ on
$\operatorname{Sym}^2\mathcal H_0$** — $D$ its level-diagonal part (an invertible
reference, i.e. a scheme choice), $N$ the off-diagonal remainder — and each term is a
chain of $n$ frozen-neck surfaces; the $G_2$ on the right converts $V_4^{-1}$ into
$m_2^{-1}=V_4^{-1}G_2$ (§1, $m_2$ dictionary). This is the form the companion script
computes (`neumann_data`: `Gm` is the $V_4$-Gram, `D = diag(Gm)`, `Noff = D - Gm`, and
the partial sums enter the propagator slot that carries
$(V_4|_{\operatorname{Sym}^2})^{-1}$). It agrees term by term with 020 (3.1), which
writes the same series as $m_2^{-1}=\sum_n(\tilde D^{-1}\tilde N)^n\tilde D^{-1}$ with
$m_2=\tilde D-\tilde N$ and $\tilde D$ "the level-diagonal part of $V_4$ read through
$G_2$", i.e. $\tilde D=G_2^{-1}D$, $\tilde N=G_2^{-1}N$: then
$\tilde D^{-1}\tilde N=D^{-1}N$ and $\tilde D^{-1}=D^{-1}G_2$, so the iterated operator
— and therefore the spectral radius quoted below — is the *same* object under either
reading. What is not correct is the unqualified "$m_2=D-N$" with $D$ the level-diagonal
part of the $V_4$ Gram, which the earlier version of this record wrote: the diagonal
split is of $V_4$, not of $m_2$. Whether
$\rho(D^{-1}N)<1$ holds — and persists as the truncation level grows — is a genuine,
falsifiable, *geometric* question: it decides whether the cubic theory's Feynman rules
compute amplitudes as convergent sums over surfaces, or only through the abstract
algebraic inverse. That question is Phase B (B2), riding on the RS6 companion
hand-off; **this derivation only demonstrates the failure mode**, which is all §7 of
the paper needs:

Script check 5 uses two totally symmetric finite models with the level-diagonal split.
They are **found, not constructed**: the script draws random totally symmetric vertices
and keeps the first with $\rho<0.9$ and the first with $\rho\ge1.05$ (rejection
sampling, `find_model`). They therefore have no stated relation to any physical $V_4$,
and what the pair demonstrates is only that both regimes occur in the model class —
which is exactly what §5.2 needs, and nothing more. **Model size:** the script runs at
$N=2$, so $\dim\operatorname{Sym}^2=3$ and all of the spectral discussion below lives
on $3\times3$ matrices; with two states there is no level structure at all, so the
script's $D=\mathrm{diag}(V_4|_{\operatorname{Sym}^2})$ is a full diagonal part, not a
level-diagonal one. The demonstration therefore exhibits the two regimes of
$\rho(D^{-1}N)$ for *a* reference split; it says nothing about the *level*-diagonal
dominance that PH21 conjectures. PH21's motivation — that level-diagonal dominance is
"the usual situation in level truncation" — rests on the open-string level-truncation
record (Moeller–Taylor, arXiv:hep-th/0002237, and the Taylor-school studies that
follow it), transferred to the closed-string quartic Gram by analogy; no closed-string
datum supports it yet, which is exactly what the 16b/RS6 data would supply.

Model A, $\rho(D^{-1}N)=0.7356$: the partial-sum exchange converges monotonically to
the contact kernel, reaching relative error $1.7\times10^{-4}$ at $K=12$ (errors
$3.87\times10^3\to4.36\times10^1$ at the sampled $K=0,2,4,8,12$, contact
$-2.57\times10^5$). The total decay factor over $K=0\to12$ is $88.8$, against
$\rho^{12}=0.0251$ (factor $39.8$): the observed decay is *faster* than $\rho^K$ over
this range. See the common explanation below.

Model B, $\rho(D^{-1}N)=2.2803$: the partial sums *diverge* — the surface-represented
exchange moves away from the vertex, by a factor $\times215$ from $K=0$ to $K=12$
(errors $7.30\times10^4\to1.57\times10^7$ at the sampled $K=0,2,4,8,12$). Note that
this is **slower** than $\rho^{12}=1.97\times10^4$, not faster: the growth has not yet
reached its asymptotic rate at $K\le12$. The per-step factors rise monotonically,
$1.36,\,1.38,\,1.49,\,1.88$ over the four sampled intervals, approaching $\rho=2.28$.

**One explanation for both models, and it is measured.** The truncation error is
$B_K=\sum_{\{ij|kl\}}v_{ij}^\top T^{K+1}(V_4|_{\operatorname{Sym}^2})^{-1}v_{kl}$ with
$T=D^{-1}N$ and $v_{ij}$ the source vectors, so $|B_K|\sim|A|\,\rho^{K+1}$ *asymptotically*,
with $A$ the amplitude of the dominant eigendirection of $T$ in that functional:
$\rho^K$ is an asymptotic **rate**, not a bound, and a weakly excited dominant mode
produces a transient in *either* direction — an observed decay faster than $\rho^K$
(model A: per-step $88.8^{-1/12}=0.691<\rho$, which must rise back to $\rho$) and an
observed growth slower than $\rho^K$ (model B) are the same phenomenon. The script now
measures $|A|$, normalised by $\sum_m\|v_m\|\,\|x_m\|$: **model A $4.74\times10^{-3}$,
model B $5.02\times10^{-3}$** — in both models the dominant mode is weakly excited,
which is what the explanation predicts and what makes both transients expected at
$K\le12$. What the explanation predicts is *smallness*, and only that: the closeness of
the two numbers is not evidence for it — with a signed three-term sum normalised by
$\sum_m\|v_m\|\|x_m\|$ in a three-dimensional space, agreement to 5% across two
independently drawn vertices and two independently drawn external sets is as likely an
artefact of the normalisation as a common cause. (The
diagnostic carries no PASS/FAIL predicate; it is a measurement, not a check. It is
guarded: the script now requires the dominant eigenvalue of $T$ to be real and simple,
extracts the left and right eigenvectors by an exact eigendecomposition, and
cross-checks them against a power iteration with a residual tolerance — a
complex-conjugate dominant pair, which a zero-trace $T$ makes unexceptional, or a
non-converged iteration returns "not available" instead of a number. Both guards were
shown to fire on constructed matrices; with them in place the two values above are
unchanged.) What matters for
§7 is the sign of the exponent, not its value: the sequence diverges, and it does so
**while on the same model, same externals, the algebraic inverse still telescopes
exactly** (exact rational arithmetic for the algebraic inverse; the spectral radii and
the partial sums are floats). This is the precise
sense in which "the cubic reformulation's amplitude differs from standard SFT *only*
through the representation theory of $m_2^{-1}$": the algebraic identity is scheme-blind
and exact in the finite-dimensional model; the surface representation is a scheme-dependent claim that can
fail, and its failure is detectable ($\rho\ge1$), not silent.

If Phase B finds $\rho\ge1$ for the physical vertex data, the *identity* (4.3) is
untouched (it uses only H1–H3), but the frozen-neck-chain sum ceases to compute the
amplitude and the split choice $D$ acquires physical-looking scheme dependence — to be
flagged prominently, per the plan's B2 verdict table.

---

## 6. Verification

`codes/verify-a4pt-chain.py` — sympy via the project uv venv, exact rational
arithmetic throughout *except* the three float sub-parts of check 5 — its spectral
radii, its partial sums, and the `dominant_overlap` diagnostic (which carries no
predicate); the algebraic-inverse telescoping inside check 5 is exact. Model size:
$N=2$, hence $\dim\operatorname{Sym}^2=3$ — check 2's "rank $2<3$", check 6's deletion
of one of three intermediate states and check 5's spectral data all live on $3\times3$
matrices, and with two states there is no level structure, so the script's
$D=\mathrm{diag}$ is a full diagonal, not a level-diagonal, part (§5.2). Seed
20260715 printed; nonzero exit on failure. The script prints **6/6 PASS**, which should
be reported as **5 checks + 1 vacuity demonstration**: check 3 PASSes *by design* on
corrupted input and is evidence of nothing but the vacuity of truncated telescoping
comparisons (§5.1). One labelled check per claim:

1. **A1 enumeration + prefactors (new vs 007):** the connected amputated 4-point
   kernel of $S_{\rm HS}$ at $O(g_s^2)$, computed *mechanically* from the joint
   $(\Psi,\Sigma)$ Gaussian — source-shift trick, $\exp$-operator Wick moments, no
   diagrams input — equals (a) the same object for $S_{\rm eff}$ at all orders in the
   externals (loops included), (b) the hand-enumerated sum (2.1) in its multilinear
   part, (c) $g_s^2V_4$ for the $\Sigma$-part alone (R14 reuse), (d) $g_sV_3$ for the
   $O(g_s)$ 3-point (vertex normalization). Generic non-diagonal kinetic $K$.
2. **H1 shadow:** non-diagonal $G_2$ (random metric $g$), degenerate $V_4$ (rank
   $2<3$): $m_2^{+}m_2$ is the projector onto the row space of $m_2$ (the kernel
  quotient — *not* the image, which differs since $m_2=G_2^{-1}V_4$ is not symmetric
  in general); the source-orthogonality clause `ok2_src` is an **identity, not a test
  with teeth** — the sources are rows of the same Gram whose kernel is being paired
  against, so it vanishes for any vertex and any states, and no corruption of check 4
  gives it teeth; it records the correct inner-product-free statement of the
  kernel-decoupling half of H1, nothing more. The
   source functional annihilates $\ker V_4$, the $m_2$-form pseudo-inverse propagator
   telescopes, exchange = contact. Extends R14 §6 (which had Euclidean pairing). The
   script's realisation uses the Moore–Penrose pseudo-inverse, which is an
   inner-product-dependent *construction* convenient in the finite model; the
   statement it stands in for — $V_4(\Xi,\cdot)=0$ for $\Xi\in\ker V_4$, hence no
   sourcing of the kernel — is inner-product-free (§1, H1). The *level-uniform* half of
   H1 as restated on 2026-09-22 — stabilization of $\ker V_4^{(L)}$ and the absence of a
   persistent on-shell zero — is not tested here either: the model has a single fixed
   dimension and no sequence of levels. It is also inner-product-free, so unlike the
   earlier bounded-inverse wording it needs no norm to be stated.
3. **Tautology trap:** (5.1) passes on five corrupted vertices — the vacuity
   demonstration.
4. **Teeth:** four deliberate corruptions all break the equality (kinetic/source
   mismatch; $c=1\Rightarrow\tfrac14$; wrong $G_2$; dropped channel). Falsifiability
   of checks 1–2 certified.
5. **Neumann resolution:** convergent model ($\rho=0.7356$) vs divergent model
   ($\rho=2.2803$) as in §5.2, both found by rejection sampling; algebraic inverse
   exact on both. The script also *measures* (no PASS/FAIL attached) the weight of the
   dominant $D^{-1}N$ eigendirection in the error functional —
   $4.74\times10^{-3}$ and $5.02\times10^{-3}$, i.e. weakly excited in both models,
   which is the smallness §5.2's transient explanation predicts (the near-equality of
   the two numbers is not read as evidence, §5.2). The diagnostic is guarded: real and
   simple dominant eigenvalue, eigenvectors from an exact eigendecomposition
   cross-checked against a power iteration with a residual tolerance, "not available"
   otherwise; both guards were shown to fire on constructed matrices.
6. **H2 shadow:** deleting one intermediate state breaks exchange = contact; the full
   sum restores it. This probes the *level* part of H2 only — the finite-dimensional
   model has no momentum direction, so the $\int d^Dk_a$ of §1's H2 is not exercised.

Not machine-checkable here (named, not smuggled): H1/H2 at CFT level, including the
momentum part of H2 (§1); H3, the covering of $\mathcal M_{0,4}$, and the
Virasoro–Shapiro reduction (§4, cited). The
script's random $V=\sum_r c_r u_r^{\otimes4}$ is automatically totally symmetric, so
$S_4$-symmetry is exercised, not falsifiable, in the script (same caveat as R14,
critic Issue 7 there).

---

## 7. What this does and does not establish

**Established (proven at the algebraic layer / machine-checked):**

- the complete $O(g_s^2)$ diagram enumeration for 4 external $\Psi$, tree topology
  *forced* by counting (§2.2), with the mechanical path-integral cross-check;
- the assembled amplitude (2.1) with every prefactor explicit in amplitude
  normalization, $V_3$ sector included (new relative to R14);
- the telescoping chain (3.1)–(3.4) with H1/H2 stated at the exact steps where they
  act, and nowhere else;
- Claim OFF (4.1): off-shell equality with quartic-truncated standard SFT, same vertex
  family, conditional on H1–H2;
- (4.3), the on-shell 4-tachyon Virasoro–Shapiro statement, conditional on H1–H3 —
  the algebraic reduction is proven here, the Virasoro–Shapiro endpoint is cited;
- the tautology trap as a demonstrated fact **in the finite-dimensional model** (5.1)
  and the identification of the Neumann representation's convergence as the falsifiable
  numerical content that survives there (5.2), with both regimes exhibited.

**Not established here (named, tracked elsewhere):**

- H1 at CFT level, in its 2026-09-22 form: (a) stabilization of $\ker V_4^{(L)}$, so
  that the level-by-level quotient and its inverse have a limit, and (b) no zero of the
  truncated determinant on the quotient persisting with the level at the momenta used —
  the on-shell locus included, where PH18's determinant zeros are not excluded. No
  auxiliary inner product is assumed, and no bounded inverse is claimed; R15's
  Schwinger/spectral form is a stronger, norm-dependent statement, kept out of the
  hypothesis and demoted to a conditioning diagnostic (§1) — RS6 / task 16b;
- H2 at CFT level (completeness/convergence of the combined level *and* relative-momentum
  sum, R33/031 §4.3, including the interchange clause: the scalar partial sums
  $s_N(P,Q)=\sum_{I\le N}V_4(P,m_2^{-1}\lambda_I)\,\langle\lambda_I,m_2Q\rangle$ must
  converge to $V_4(P,Q)$) — A2(iii), Phase B3/RS6;
- H3, the covering of $\mathcal M_{0,4}$ by Feynman + vertex regions: standard for
  minimal-area/hyperbolic families, **open in the interior for the SL(2,C) family**
  (R2, R37);
- $\rho(D^{-1}N)<1$ for physical vertex data — Phase B2 (companion RS6 hand-off);
- whether a comparison of exchange and contact at a fixed level truncation of the
  *actual* theory carries information (the momentum integral is not truncated by
  level) — open, §5.1;
- the Virasoro–Shapiro value of the on-shell integral — cited (§4);
- $O(g_s^3)$ and beyond (the $\Sigma$-tower) — R25/R26, out of scope at 4 points.

---

## 8. Self-review (A5 pre-critic, per Scientific Reasoning Standards §5)

1. **Objective vs literal task.** The motivating objective — a §7 the paper can state
   without overclaiming or vagueness — is met by construction: the headline claim
   (4.3) is conditional on exactly three named hypotheses — H1 and H2, each flagged at
   its point of use (3.2, 3.3) and each with a finite-dimensional shadow check, plus H3
   at the on-shell reduction (§4), which has none and is tracked in the ledger
   — and the overclaim
   guard is written into §4. The literal deliverables (chain, script, paper prose) are
   all present.
2. **Weakest step.** The statement of H2. "Completeness of the intermediate state sum"
   is shorthand for a convergence statement about an infinite level sum sandwiched
   between unbounded objects; the precise functional-analytic phrasing (which topology,
   which domain for $m_2^{-1}$) is deliberately left at the level of the Gram identity
   with the full sum, matching R15's granularity. Shored up by: tying it to the
   measurable quantity (Phase B3 saturation drift) rather than to an unverifiable
   abstraction. A critic wanting a sharper H2 should point at A2(iii), not at this
   chain. *Sharpened 2026-09-21:* H2 now states what is summed — levels of the two
   strands **and** the pair's relative momentum, per R33/031 — which makes its
   finite-truncation "automatic" status weaker than originally written (the momentum
   integral is not truncated by level). *Carried through 2026-09-21 (second pass):* the
   consequence is now drawn everywhere. The "automatic at finite truncation" statements
   and the tautology trap are scoped to the finite-dimensional model (levels only,
   momentum suppressed), where they are proven; for a level truncation of the actual
   theory the collapse is not a finite matrix identity and the informational content of
   a truncated comparison is left open, with one concrete thing it could test (the
   convergence of $\int d^Dk_a$ on $m_2P$ at fixed level). This is still the item most
   likely to move again. *Restated 2026-09-22:* H2 additionally carries the interchange
   clause (the partial sums must converge after $m_2^{-1}$ is applied), which moved into
   H2 from the bounded-inverse wording H1 used to carry. H1 itself no longer fixes an
   auxiliary inner product: the positive-definite Fock form is neither Lorentz- nor
   BRST-invariant, so a singular-value drift stated in it is frame dependent and cannot
   falsify a hypothesis of the theory; and §3 never used a bounded inverse, only
   $m_2^{-1}m_2P=P$ mod $\ker V_4$. H1 is now level-uniformity of the quotient, (a) and
   (b) of §1. The drift survives as a conditioning diagnostic, labelled as such.
3. **Not checked, and why acceptable.** (i) $S_4$-symmetry is not falsifiable in the
   script (structural, see §6) — closed at ledger level, acceptable. (ii) The
   VS endpoint is cited — textbook, per the plan's explicit instruction. (iii) Koszul
   signs for Grassmann-odd components: the counting is grading-blind as in R14 §1
   (physical grading, both fields even); the graded extension remains a write-up
   remark. (iv) Real convergence rates of (5.2) on physical data — explicitly Phase B,
   the script only demonstrates the failure mode, as briefed.
4. **What would a stronger physicist find in five minutes?** Most likely objection:
   "your off-shell Claim OFF is only as meaningful as the off-shell amplitude
   definition — off-shell amplitudes are scheme-dependent." Answer already in §4: the
   claim is *relative* (HS vs standard SFT with the same vertex family), so scheme
   dependence cancels; that is exactly why the off-shell form is the stronger,
   well-posed statement. Second objection: "H1/H2 could hide the same content as
   'the theory works'." They are strictly weaker: both are statements about the
   quadratic $\Sigma$-sector spectral data, not about amplitudes; Phase B tests them
   independently of any amplitude comparison. Third objection, added 2026-09-21 and the
   one a referee would raise first: "(4.1) is stated for generic off-shell externals
   and (4.3) evaluates it on a non-generic locus". Answered in §4 ("From (4.1) to the
   on-shell locus"): the telescoping is algebraic and multilinear, the channel poles
   are shared, and the residual content — the non-degeneracy of $m_2$ at the on-shell
   momenta (H1) and the convergence of the state sum on the on-shell vectors $m_2P$
   (H2) — is declared as part of H1 and H2. Its motivation is genericity (PH5), not the
   finiteness of $V_4$, which concerns the numerator and would not exclude a
   degeneration of the inverse; the falsifier is a zero of $\det V_4^{(L)}(P^2)$ on the
   tachyon shell persisting with the level, which PH18 makes a live possibility.
   Uniformity over all of momentum space is not claimed.

---

## 9. Paper-ready prose for §7 (amplitude consistency)

*Drop-in draft for `plans/paper-plan-2026-07-14.md` row 7; citation keys to be
resolved against the paper's `.bib` (Erbin 2023 = arXiv:2301.01686, Zwiebach 1992 =
arXiv:hep-th/9206084, Polchinski 1998 Vol. I). Equation labels local to the section.*

> **Amplitude consistency at four points.** A rewriting of the theory is only as good as
> the amplitudes it returns. We check at four external strings and order $g_s^2$ that the
> auxiliary action \eqref{eq:SHS} reproduces the amplitudes of the theory it rewrites,
> and we state along the way the two assumptions the check rests on, together with the
> third that the on-shell statement adds.
>
> The auxiliary sector contributes two Feynman rules: a $\Sigma\Psi\Psi$ vertex
> $\frac{g_s^2}{6}\,\mathcal V_4(\,\cdot\,,\Psi_i\otimes\Psi_j)$ and a $\Sigma$-propagator
> $\frac{12}{g_s^2}\big(\mathcal V_4|_{\operatorname{Sym}^2\mathcal H_0}\big)^{-1}$.
> Throughout, $\braket{\cdot,\cdot}$ is the pairing on pair states and $p_{2,2}$ the
> operator it defines through $\mathcal V_4(A,B)=\braket{A,p_{2,2}B}$, so that the
> propagator is equally $\frac{12}{g_s^2}\,p_{2,2}^{-1}$ preceded by the raising of the
> index with the pairing — one object written two ways, with one kernel,
> $\ker p_{2,2}=\ker\mathcal V_4|_{\operatorname{Sym}^2\mathcal H_0}$. It is an algebraic
> contraction and not a moduli-carrying plumbing fixture: it contains no Schwinger
> parameter and no $b$-ghost insertion, and, as we show elsewhere
> [§ Riemann-surface interpretation], no local worldsheet kernel built from connected
> surfaces of bounded type with the standard sewing insertions represents it, granting
> the standard factorization input. Trading a higher vertex for an auxiliary quadratic
> sector has an open-string precedent \cite{Schnabl:2024:OpenStringField}.
>
> At $O(g_s^2)$ with four external $\Psi$, counting the order in $g_s$, the legs and the
> Euler character leaves exactly four connected diagrams: the three cubic exchange
> channels and one $\Sigma$-exchange. Tree topology is forced rather than assumed, the
> $\Sigma$-tadpole excluded by the parity of the $\Sigma$-Gaussian and the $\Psi$-tadpole,
> being one-loop, by order counting. The three cubic channels are identical, diagram by
> diagram, to those of the standard theory, so the entire comparison sits in the
> $\Sigma$-exchange.
>
> Take one of the three pairings $\{ij|kl\}$ and let $P=\operatorname{Sym}(\Psi_i\otimes\Psi_j)$
> and $Q=\operatorname{Sym}(\Psi_k\otimes\Psi_l)$ be the pair states filling the two vertex
> slots. Writing the second vertex through the pairing, $\mathcal V_4(\,\cdot\,,Q)=
> \braket{\,\cdot\,,p_{2,2}Q}$, and inserting a complete set $\{\lambda_I\}$ of
> intermediate two-string states between the blocks,
> $$
> A_4^{(ij|kl)}
> =\frac{g_s^2}{6}\cdot\frac{12}{g_s^2}\cdot\frac{g_s^2}{6}\;
> \mathcal V_4\Big(P,\;
> \underbrace{p_{2,2}^{-1}}_{\text{kernel quotient}}\;
> \underbrace{\textstyle\sum_I\lambda_I\,\braket{\lambda_I,\,p_{2,2}Q}}_{\text{intermediate state sum}}
> \Big)
> =\frac{g_s^2}{3}\,\mathcal V_4(P,Q).
> $$
> The three pairings give the same value — the quartic vertex carries full graded
> symmetry, which is a defining property of a vertex family and not an assumption of the
> argument — so that
> $A_4^{\Sigma\text{-exch}}=g_s^2\,\mathcal V_4(\Psi_1,\Psi_2,\Psi_3,\Psi_4)$: the contact
> term of the standard quartic vertex with coefficient exactly one,
> $3\cdot\tfrac16\cdot12\cdot\tfrac16=1$.
>
> Two steps of that line are not algebra, and they act at different places. The insertion
> asserts that the composition of vertex, propagator and vertex is a sum over a complete
> set of intermediate two-string states, convergent on the pair states $p_{2,2}Q$ that the
> external sources produce. The sum is not a level sum alone: it runs over the oscillator
> levels of the two strands *and* over the pair's relative momentum, a discrete sum times
> an integral $\int d^Dk_a$. What the collapse needs of it is that it may be interchanged
> with $p_{2,2}^{-1}$ — writing
> $s_N(P,Q)=\sum_{I\le N}\mathcal V_4\big(P,p_{2,2}^{-1}\lambda_I\big)\braket{\lambda_I,p_{2,2}Q}$
> for the partial sums, we assume that $s_N(P,Q)\to\mathcal V_4(P,Q)$ for the external
> data used. This is convergence of a sequence of numbers; no norm on the string field
> space is fixed, and none is needed. What makes it plausible is that the same resolution
> of the identity is the standard sewing-completeness input on an ordinary neck; the
> auxiliary edge differs from such a neck only by being frozen, which removes the damping
> $e^{-sL_0^+}$ but not the structure of the state sum, so the burden is convergence and
> not existence.
>
> The other step is the collapse $p_{2,2}^{-1}p_{2,2}=\mathrm{id}$. At fixed level it is
> elementary: a solution of $p_{2,2}X=p_{2,2}Q$ exists — namely $Q$ — it is unique modulo
> $\ker p_{2,2}$, and the amplitude sees $X$ only through $\mathcal V_4(P,X)$, which is
> blind to that kernel. The kernel is harmless for a reason that involves no metric at
> all: every $\Xi$ in it satisfies $\mathcal V_4(\Xi,\,\cdot\,)=0$, so the source
> functional of the auxiliary sector annihilates it identically and no diagram sources it
> — a zero-action decoupled spectator. No inner product enters any of this, and none is
> introduced: the pairing natural to the problem is indefinite, while a positive-definite
> Fock-space norm, although available, is neither Lorentz- nor BRST-invariant, so
> quantitative statements made in it are frame dependent. What we assume, beyond that
> level-by-level construction, is that it has a limit: the kernels of the level-truncated
> quartic forms stabilize, so that the quotient
> $\operatorname{Sym}^2\mathcal H_0/\ker p_{2,2}$ and the propagator defined on it level by
> level converge, and, at the external momenta used, the determinant of the truncated form
> on the quotient has no zero that persists as the level grows. Neither a bounded inverse
> nor a closed range is assumed, and the argument uses neither.
>
> In a finite-dimensional model — finitely many levels, with the relative momentum
> suppressed — both assumptions are empty: a pseudo-inverse exists and the sum is finite.
> What they add is uniformity as the truncation grows, a stable kernel and a saturated
> state sum in the limit, which no single truncation of that kind can exhibit. A level
> truncation of the theory itself is not of that kind, since it leaves the integral over
> the pair's relative momentum untouched; there the convergence of the intermediate sum is
> a genuine analytic condition already at fixed level. These two assumptions, together
> with the covering property below, are the entries carried by the limitations table of
> section [limitations].
>
> Granting them, the four-point amplitude of the cubic theory equals, off shell and for
> the same vertex family, that of the standard quartic-truncated closed string field
> theory: the auxiliary rewriting introduces no new scheme dependence. The step to
> on-shell external states is algebraic — the collapse is multilinear in the external
> states and uses no genericity, and the channel poles are shared because both theories
> use the same $\Psi$ Feynman rules. What it costs is that the two assumptions hold at the
> on-shell momenta as well: that the quartic form stay non-degenerate there, and that the
> intermediate sum still converge on the states the sources produce. We take this as part
> of the two assumptions rather than as a consequence of them. It is supported by
> genericity — no selection rule forces a kernel of the quartic form, and an accidental
> one is non-generic in the vertex family — and it is not settled: the determinant of the
> level-truncated quartic form does have zeros in the momentum variable, nothing we know
> keeps them away from the tachyon shell, and a zero sitting there and persisting as the
> level grows would invalidate the step.
>
> On shell one further condition enters: the three plumbing regions and the fundamental
> vertex region must cover $\mathcal M_{0,4}$ exactly once. For minimal-area and
> hyperbolic vertex families this is the standard construction
> \cite{Zwiebach:1992ie,Erbin:2021smf,Costello:2019:HyperbolicStringVertices,Firat:2021:HyperbolicThreestringVertex};
> for the family used here the interior
> statement remains open, so we carry
> it as an assumption rather than as an established input. Granting it, the standard
> amplitude on four tachyons is the Virasoro–Shapiro amplitude \cite{Polchinski:1998rq},
> and the cubic theory therefore reproduces it, on the covering property and the two
> assumptions above together. The logical shape is worth stating plainly: the cubic action *reduces to* the standard string field theory amplitude, which
> is textbook-known to equal Virasoro–Shapiro. No independent derivation of the latter is
> claimed, and the covering property is inherited from the vertex construction, not
> re-proven here.
>
> **What a numerical check can and cannot test.** In a finite-dimensional model — finitely
> many levels and no momentum integral — every object in the exchange satisfies the
> collapse identically, so assembling the truncated exchange and comparing it with the
> truncated vertex verifies nothing; the cleanest way to see this is that the same
> comparison succeeds on deliberately corrupted vertex data. Truncating the theory in the
> level alone does not put one in that situation, because the sum over the pair's relative
> momentum survives the truncation; what a comparison at fixed level could then test is
> the convergence of that momentum integral, and we leave open whether it does. Beyond
> this, the identity can fail only through the representation theory of $p_{2,2}^{-1}$.
> Among connected surfaces of bounded type carrying the standard sewing insertions no
> local worldsheet kernel exists, granting the standard factorization input [§ no-go], so
> within that class the only surface presentation is the frozen-neck chain series obtained
> from the diagonal split $\mathcal V_4|_{\operatorname{Sym}^2}=D-N$ with $D$ the
> level-diagonal part,
> $\big(\mathcal V_4|_{\operatorname{Sym}^2}\big)^{-1}=\sum_{n\ge0}(D^{-1}N)^nD^{-1}$,
> convergent exactly when $\rho(D^{-1}N)<1$. A dressing fine-tuned to the quartic vertex
> itself falls outside the no-go and is not excluded; we know of none. Whether the series
> converges on physical vertex data — the existence, kernel and gap of the
> $(\mathcal V_4,\braket{\cdot,\cdot})$ pencil per truncation level, and the drift of the
> state-sum saturation with level — is precisely the quantitative form of the two
> assumptions, and we leave it to a numerical study in preparation. The failure mode is at
> least detectable rather than silent: in a toy model with $\rho>1$ the partial chain sums
> demonstrably diverge from the vertex while the algebraic identity continues to telescope
> exactly.

*Limitations-table line (revised 2026-09-22; the 2026-09-21 version stated the first
hypothesis in an auxiliary inner product, which has been dropped):* “Four-point amplitude
consistency at $O(g_s^2)$: established as an identity of the algebra, and conditional at
the level of the conformal field theory on two hypotheses. **(H1)** The kernels of the
level-truncated quartic forms stabilize, so that the quotient
$\operatorname{Sym}^2\mathcal H_0/\ker p_{2,2}$ and the propagator defined on it level by
level have a limit; and, at the
external momenta used, the four-tachyon shell included, the determinant of the truncated
form on the quotient has no zero persisting with the level. No auxiliary inner product and
no bounded inverse are assumed. **(H2)** The intermediate two-string sum, over the strands'
oscillator levels and the pair's relative momentum, is complete and convergent on the
states the sources produce, in the form that permits it to be interchanged with
$p_{2,2}^{-1}$: the partial sums
$s_N(P,Q)=\sum_{I\le N}\mathcal V_4(P,p_{2,2}^{-1}\lambda_I)\braket{\lambda_I,p_{2,2}Q}$
converge to $\mathcal V_4(P,Q)$. The off-shell statement needs (H1)–(H2); the on-shell
Virasoro–Shapiro statement needs in addition **(H3)**, that the vertex family's Feynman
and vertex regions cover $\mathcal M_{0,4}$ exactly once — standard for minimal-area
families, open in the interior for the family used here. The associated no-go for a local
worldsheet kernel of $p_{2,2}^{-1}$ is an exclusion within connected surfaces of bounded
type with the standard sewing insertions, and holds modulo the standard factorization
input; a kernel fine-tuned at the actual quartic vertex is not excluded. (H1) and (H2) are
to be tested numerically, and (H3) settled for the family used here, in work in
preparation.”

---

## References

- Erbin, H. *String Field Theory: A Modern Introduction*. Springer LNP 980 (2021);
  arXiv:2301.01686 is the 2023 posting. The bibtex key used in the project is
  `Erbin:2021smf` — key year (2021, the book) and the arXiv year (2023) disagree by
  construction; cite the book year with that key and do not "correct" one to the
  other. (Live draft: `Reviews/String theory/document/`, chapters
  `bos_offshell_amplitudes.tex`, `bsft_bv.tex`, tree-level scattering chapters.)
- Schnabl, M. and Stettinger, G. (2023). *Open string field theory with stubs*.
  arXiv:2301.13182. The nearest external precedent for "an auxiliary structure makes
  the action cubic"; reviewed in the project at `literature/reviews/C9ETB6WE.md`
  (which also covers the Erbin–Fırat open-string auxiliary propagator, R3) and
  `literature/reviews/FBSP8UQ9.md` (conjugate-pair auxiliaries, R13). §9 must cite
  this literature; a §7 citing only Zwiebach, Erbin and Polchinski would read as
  unaware of it.
- Zwiebach, B. (1992). *Closed string field theory: Quantum action and the BV master
  equation*. Nucl. Phys. B 390. arXiv:hep-th/9206084.
- Costello, K. and Zwiebach, B. *Hyperbolic string vertices*. arXiv:1909.00033. The
  hyperbolic-vertex construction referred to in H3 (§1) and in §9; added 2026-09-21
  because the record asserted "the standard construction" for hyperbolic families
  while citing only Zwiebach 1992 and Erbin 2023.
- Fırat, A. H. (2021). *Hyperbolic three-string vertex*. JHEP 08 (2021) 035.
  arXiv:2102.03936, doi:10.1007/JHEP08(2021)035 (BibTeX key
  `Firat:2021:HyperbolicThreestringVertex`, the published version; the `-v1` key in the
  shared bibliography is the first arXiv version and should not be cited). Explicit
  hyperbolic vertices; the follow-ups arXiv:2302.12843 and arXiv:2409.02982 are in
  Zotero as well.
- Moeller, N. and Taylor, W. (2000). *Level truncation and the tachyon in open bosonic
  string field theory*. Nucl. Phys. B 583, 105. arXiv:hep-th/0002237. The support for
  the empirical claim in §5.2/PH21 that (level-)diagonal dominance and convergence of
  level truncation are "the usual situation"; note that this evidence is from **open**
  bosonic SFT and is transferred to the closed-string quartic Gram by analogy only.
- Polchinski, J. (1998). *String Theory, Vol. I*, §6.6 (closed-string tree
  amplitudes). Cambridge University Press. The section *title* was not checked against
  the book in this project; only the content reference is asserted.
- Project ledger: R1, R7–R15, R17, R23, R25–R28 — `knowledge/results.md`; derivations
  007 (R14), 020 (R27), 022 (R28); plan `plans/amplitude-check-plan-2026-07-14.md`.
