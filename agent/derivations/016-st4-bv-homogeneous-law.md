# Derivation 016 — ST4: BV taxonomy of the homogeneous auxiliary-rotation law

- **Task:** ST4 (brief `computator-st4-bv-xtilde-20260705T203205`). Settle the BV
  classification of the homogeneous piece of the $O(g_s^3)$ corrected gauge law,
  $$\delta\tilde X=\tfrac{g_s}{10}\,K_\Psi^{-1}V_5(\cdot,\tilde X,\delta\Psi)$$
  (011 §4 eq. B.8, third term of B.9), left open there as a "small open point"
  (R17 carve-out (c)); and simultaneously ground the two informal labels of B5
  — "trivial homogeneous" ($\delta Y_3=0$, 015 §4.1) and "implicit homogeneous"
  ($\delta Y_2$, 015 §4.2, R21 open flag (d), line 509/520).
- **Author:** Claude Opus 4.8 (computator subagent), session 2026-07-06.
- **Machine check:** `codes/verify-st4-bv-xtilde.py` — **6/6 PASS (executed
  2026-07-06; re-executed 2026-07-09 after the check-3/check-6 relabelling below)**.
- **Status:** **R22 (promoted 2026-07-06).** **Blind critic pass DONE 2026-07-08
  (Opus, ST9, combined with R21): ACCEPT — 0 Fatal, 0 Serious.** The critic
  re-derived the HT graded-antisymmetry condition (16.2) and the forced generator
  $\mu$ from scratch and confirmed both; check 2 ($\mu$ symmetric) judged genuine
  and decisive; the promotion stands. Non-blocking tidy-ups applied 2026-07-09:
  [C3] check 6's zero-rotation leg labelled *illustrative* (0=0 by construction —
  $\delta K$ is set to zero for a $\Psi$-independent kernel; the genuine
  $\delta Y_3=0$ machine test is check 3 of `verify-b5-ogs4-gauge-eom-ibl.py`,
  rewritten the same day); [M4] the check-3 "odd-parity probe" reworded — a sign
  flip does not model a Grassmann-odd $\delta\Psi$; the parity-spectator claim is
  carried by the analytic §3.2 argument, the numerics confirm only
  linearity+symmetry. Report:
  `agent/reports/critic-b5-st4-r21-r22-20260708T214500.md`.
- **Inputs reused (not re-derived):** R11 (composite law; $(X,X^+)$ contractible
  pair, Henneaux auxiliary-field theorems), R17 (011 §4: B.2, B.8, B.9, $K_\Psi$,
  $\tilde X$), R18 (012: no independent two-string parameter), R21 (015: $\delta Y_3=0$,
  $\delta Y_2$ implicit law), 009 §2.2 / Table 1 (physical $N_{\rm gh}$, parities).
  Henneaux–Teitelboim, *Quantization of Gauge Systems* (1992), Ch. 3 (trivial gauge
  symmetries / on-shell reducibility taxonomy).
- **Conventions:** physical $N_{\rm gh}$ grading (Ψ at 2, Σ/$\tilde X$ at 4, all
  Grassmann-even; $\delta\Psi$ even — a gauge transformation preserves the parity of
  the field it acts on); finite-dimensional algebraic layer (R1–R21 carve-out): $V_4,
  V_5,K_\Psi$ are generic graded-symmetric multilinear tensors on a finite-dim graded
  vector space; no CFT analytics. BV antifield parity fixed by the standard rule
  (opposite to the field); its worldsheet-$N_{\rm gh}$ label flagged in §1.

---

## 0. Executive summary

**Verdict: the homogeneous $\tilde X$-term is neither a Henneaux–Teitelboim *trivial*
gauge symmetry nor a *nontrivial* gauge symmetry. The trivial/nontrivial dichotomy is
the wrong axis.** It is the forced transformation law of the **auxiliary field
$\tilde X$** under the *single* closed-string $\Lambda$-gauge symmetry — the
$O(g_s^3)$ descendant of R11's $(X,X^+)$ **contractible pair**. Three facts settle it:

1. **HT-trivial test FAILS (decisive graded computation).** Writing the homogeneous
   piece as $\delta_h\tilde X=\mu\cdot E_{\tilde X}$ acting on the $\tilde X$-EOM
   $E_{\tilde X}\propto K_\Psi\tilde X$, the effective generator is
   $$\mu=-\tfrac{6}{5g_s}\,K_\Psi^{-1}\,W_{\delta\Psi}\,K_\Psi^{-1},\qquad
   (W_{\delta\Psi})_{IJ}:=V_5(\Lambda_I,\Lambda_J,\delta\Psi),$$
   which is **graded-SYMMETRIC**, $\mu^{IJ}=+\mu^{JI}$. For even fields HT-triviality
   requires $\mu$ **anti**symmetric (§2, §3). The hoped-for rescue — that the
   Grassmann parity of $\delta\Psi$ antisymmetrises the effective $\mu$ — **does not
   occur**: the two contracted slots $\Lambda_I,\Lambda_J\in\Sym^2$ are both even, and
   $\delta\Psi$ is a *spectator* in the $I\!\leftrightarrow\!J$ swap, so $W_{\delta\Psi}$
   is symmetric independently of the parity of $\delta\Psi$ (§3.2, check 3).
2. **It is not even a standalone symmetry.** With $\Psi$ frozen (so $\delta\Psi$ acts
   only inside $V_5$, not on $K_\Psi$), $\delta_h S_3=E_{\tilde X}\!\cdot\!\delta_h\tilde X
   =-\tfrac{g_s^3}{120}V_5(\tilde X,\tilde X,\delta\Psi)\neq0$ (check 4). The full
   transformation is a symmetry only because the *same* $\delta\Psi$ produces the
   compensating $\delta K_\Psi$-anomaly $-\tfrac{g_s}{5}V_5(\tilde X,\tilde X,\delta\Psi)$
   (check 5). So $\delta_h\tilde X$ is a **compensator**, not an independent symmetry —
   classifying it in isolation as trivial/nontrivial is a category error.
3. **Nontrivial test FAILS.** $\delta_h\tilde X$ carries **no independent gauge
   parameter** (it is a function of $\delta\Psi$, i.e. of the single $\Lambda$) and
   acts only on the auxiliary $\tilde X$, whose gauge generator
   $R^{\tilde X}_\Lambda\propto\tilde X$ **vanishes on-shell**. It does not act on the
   physical BRST cohomology and is removed by eliminating $\tilde X$ ($\tilde X=0$),
   leaving the R11 composite law on $\Psi^{\otimes2}$. So it is **cohomologically
   trivial** (contractible-pair sense), consistent with R18's "no independent
   two-string parameter."

**Unified classification (covers $O(g_s^3)$ $\delta\tilde X$ AND $O(g_s^4)$
$\delta Y_2$; distinguishes $\delta Y_3=0$):** all three are transformation laws of an
**auxiliary field forming a contractible pair**, with generator $\propto$ the
deviation (EOM), on-shell-vanishing, carrying no independent parameter. They differ
only by whether the auxiliary's **kinetic operator is field-dependent**:

| case | auxiliary kinetic | forced homogeneous rotation | label (grounded) |
|---|---|---|---|
| $\delta Y_3=0$ (015 §4.1) | $\Psi$-**independent** ($\tilde M$/$M$) | $=0$ exactly | strictly-trivial contractible pair |
| $\delta\tilde X$ (011 §4) | $\Psi$-**dependent** ($K_\Psi$) | $\propto\tilde X$, nonzero, explicit | field-dependent contractible pair |
| $\delta Y_2$ (015 §4.2) | $\Psi$-**dependent** (Hessian $\mathcal K$) | $\propto Y_2$, nonzero, **implicit** | field-dependent contractible pair (implicit) |

The adjectives "trivial" / "implicit" of B5 refer precisely to whether the forced
rotation *vanishes* (kinetic field-independent) or is a *nonzero, EOM-proportional,
Neumann-implicit* rotation (kinetic field-dependent). **None is HT-trivial**
($\mu$ symmetric in every case) and **none is nontrivial** (no independent parameter):
the correct, uniform BV home for all three is the contractible-pair auxiliary sector.

---

## 1. Setup: BV data and the taxonomy

**Fields and parities** (physical $N_{\rm gh}$, 009 Table 1 / R11 / R12): the physical
fields are $\Psi\in\Hilb_0$ ($N_{\rm gh}=2$, even) and $\Sigma\in\Sym^2\Hilb_0$
($N_{\rm gh}=4$, even). In the completed-square variable (R17 B.2),
$\tilde X=\Sigma-\Psi^{\otimes2}-\tfrac{g_s}{5}K_\Psi^{-1}v\in\Sym^2\Hilb_0$ ($N_{\rm gh}=4$,
even). The gauge parameter is $\Lambda\in\Hilb_0$ ($N_{\rm gh}=1$, Grassmann-**odd**),
and $\delta\Psi=Q_B\Lambda+g_s\ell_2(\Psi,\Lambda)+\dots$ is Grassmann-**even** — a
gauge transformation preserves the parity of the field it moves. Thus **every field
entering the $\tilde X$-kinetic $K_\Psi(\tilde X,\tilde X)$ is even**, and $\delta\Psi$
(as it appears inside $V_5$) is even.

**Antifield convention (flagged).** The BV antifield $\tilde X^+$ has Grassmann parity
**opposite** to $\tilde X$, hence **odd** — fixed by the standard BV rule and by R11's
"$(X,X^+)$ contractible pair." Its *worldsheet* $N_{\rm gh}$ label is **not pinned by
the ledger** (the ledger fixes worldsheet $N_{\rm gh}$ of the fields, not of BV
antifields). Natural choice, adopted here: $\tilde X^+$ pairs with $\tilde X$ under the
odd BV symplectic form, i.e. it sits at the complementary ghost number dictated by the
$c_0^-$-inserted $\omega_2$ pairing (one-unit suspension relative to $\omega_2$, 012
conventions). Nothing below depends on the numerical worldsheet-$N_{\rm gh}$ of
$\tilde X^+$ — only on its parity (odd) and on the parities of the *fields*.

**Classical action** (R17 B.2): $S_3=S^{(5)}_{\rm eff}-\tfrac{g_s^2}{4!}K_\Psi(\tilde X,
\tilde X)+\tfrac{g_s^4}{600}vK_\Psi^{-1}v$, with the dressed kernel $K_\Psi=V_4-
\tfrac{g_s}{5}V_5(\cdot,\cdot,\Psi)$ (graded-symmetric on $\Sym^2$, invertible on the
R13 quotient). Only the middle term depends on $\tilde X$; it is the $\tilde X$-sector.

**The taxonomy (Henneaux–Teitelboim, 1992, Ch. 3).** For fields $\phi^i$ of parity
$\epsilon_i$ and even action $S$, with $E_i:=\partial^L_iS$ (parity $\epsilon_i$):

- A gauge transformation $\delta\phi^i$ is a **trivial gauge symmetry** iff it can be
  written $\delta\phi^i=\mu^{ij}E_j$ with $\mu$ *graded-antisymmetric* in the sense
  derived in §2. Such transformations vanish on-shell and act trivially on the physical
  cohomology; in BV they are generated by a term $\tfrac12\phi^+_i\mu^{ij}\phi^+_j$
  quadratic in antifields and removed by a canonical transformation.
- A **nontrivial gauge symmetry** carries an independent gauge parameter and acts
  nontrivially on the BRST cohomology.
- A field whose EOM is purely algebraic (here $\tilde X=0$) and which forms a
  **contractible pair** $(\tilde X,\tilde X^+)$ is **auxiliary** (Henneaux
  auxiliary-field theorems, R11): its gauge transformation is not physical data and is
  removed together with the field upon elimination.

The question ST4 must answer: which box does $\delta_h\tilde X:=\tfrac{g_s}{10}
K_\Psi^{-1}V_5(\cdot,\tilde X,\delta\Psi)$ fall into?

## 2. The graded-antisymmetry condition (first principles)

We derive the exact condition on $\mu$ for $\delta\phi^i=\mu^{ij}E_j$ to be a symmetry,
because the sign is the whole game and the textbook statement is often quoted only for
the bosonic case. Let the transformation have "parameter parity" $p$, so
$\epsilon(\delta\phi^i)=\epsilon_i+p$ and hence $\epsilon(\mu^{ij})=\epsilon_i+\epsilon_j+p$.
Using $E_iE_j=(-1)^{\epsilon_i\epsilon_j}E_jE_i$ and relabelling dummies,

$$
\begin{aligned}
\delta S=E_i\mu^{ij}E_j
  &=\tfrac12\big(E_i\mu^{ij}E_j+E_j\mu^{ji}E_i\big)
  \\
  &=\tfrac12\,E_i\Big[\mu^{ij}
    +(-1)^{(\epsilon_i+\epsilon_j)(1+p)+\epsilon_i\epsilon_j}\,\mu^{ji}\Big]E_j,
\end{aligned}
\tag{16.1}
$$

so $\delta S\equiv0$ (off-shell identity) requires

$$
\boxed{\;\mu^{ij}=-(-1)^{(\epsilon_i+\epsilon_j)(1+p)+\epsilon_i\epsilon_j}\,\mu^{ji}.\;}
\tag{16.2}
$$

Special cases (checks against textbook, §4 commentary): bosonic fields + bosonic
parameter ($\epsilon=p=0$) → $\mu^{ij}=-\mu^{ji}$ (antisymmetric — standard HT for
Yang–Mills-type systems); fermionic fields + bosonic parameter ($\epsilon=1,p=0$) →
$\mu^{ij}=+\mu^{ji}$ (symmetric). The parameter parity enters only through the factor
$(\epsilon_i+\epsilon_j)(1+p)$: **for even fields ($\epsilon_i=\epsilon_j=0$) it drops
out entirely**, and (16.2) reduces to plain antisymmetry $\mu^{ij}=-\mu^{ji}$
*regardless of $p$*. This is the key structural fact that kills the "graded sign
rescues triviality" hope for our all-even sector.

## 3. The computation: the effective generator is symmetric

### 3.1 Reduction to $\mu\cdot E_{\tilde X}$

The $\tilde X$-EOM from $S_3$: $E_{\tilde X}:=\partial_{\tilde X}\big[-\tfrac{g_s^2}{4!}
K_\Psi(\tilde X,\tilde X)\big]=-\tfrac{g_s^2}{12}\,K_\Psi\tilde X$, so
$\tilde X=-\tfrac{12}{g_s^2}K_\Psi^{-1}E_{\tilde X}$ ($K_\Psi$ invertible on the
quotient). Substituting into the homogeneous law B.8, with the linear map
$W_{\delta\Psi}Z:=V_5(\cdot,Z,\delta\Psi)$ on $\Sym^2$,

$$
\delta_h\tilde X
  =\tfrac{g_s}{10}K_\Psi^{-1}W_{\delta\Psi}\tilde X
  =-\tfrac{6}{5g_s}\,K_\Psi^{-1}W_{\delta\Psi}K_\Psi^{-1}\,E_{\tilde X}
  =:\mu\,E_{\tilde X},
\qquad
\mu=-\tfrac{6}{5g_s}\,K_\Psi^{-1}W_{\delta\Psi}K_\Psi^{-1}.
\tag{16.3}
$$

Because $E_{\tilde X}=-\tfrac{g_s^2}{12}K_\Psi\tilde X$ ranges over all of
$\Sym^2\Hilb_0/\ker$ as $\tilde X$ does ($K_\Psi$ invertible), (16.3) fixes $\mu$
**uniquely** on the physical quotient: there is no freedom to add a kernel piece.

### 3.2 $\mu$ is graded-symmetric — and $\delta\Psi$ cannot antisymmetrise it

$K_\Psi^{-1}$ is symmetric (graded-symmetric on the even sector, R7). The middle factor
$(W_{\delta\Psi})_{IJ}=V_5(\Lambda_I,\Lambda_J,\delta\Psi)$: under $I\leftrightarrow J$,
total graded symmetry of $V_5$ gives $V_5(\Lambda_I,\Lambda_J,\delta\Psi)=
(-1)^{\epsilon(\Lambda_I)\epsilon(\Lambda_J)}V_5(\Lambda_J,\Lambda_I,\delta\Psi)$. Both
$\Lambda_I,\Lambda_J\in\Sym^2$ are **even**, so the sign is $+1$ and $W_{\delta\Psi}$ is
**symmetric**. Crucially, $\delta\Psi$ occupies the *third* slot and is a **spectator**
in the $I\leftrightarrow J$ swap: its Grassmann parity never enters the exchange sign.
Hence

$$
\mu^{IJ}=+\mu^{JI}\quad\text{(graded-symmetric),}
\tag{16.4}
$$

**independently of whether $\delta\Psi$ is even or odd.** By (16.2) with even fields,
HT-triviality requires $\mu$ *anti*symmetric; (16.4) is the opposite. So **no
antisymmetric-generator (HT-trivial) realisation of $\delta_h\tilde X$ exists** using
the $\tilde X$-EOM.

### 3.3 No rescue via the $\Psi$-EOM either

One might try to antisymmetrise by using both EOMs, $\delta\phi^a=\mu^{ab}E_b$ over
$\phi^a=(\Psi,\tilde X)$, with the homogeneous piece acting only on $\tilde X$
($\delta_h\Psi=0$). The $\Psi$-row then reads $0=\mu^{\Psi\tilde X}E_{\tilde X}
+\mu^{\Psi\Psi}E_\Psi$; for arbitrary off-shell $E$ this forces $\mu^{\Psi\tilde X}=0$
(and $\mu^{\Psi\Psi}$ acting as $0$), whence graded-antisymmetry forces
$\mu^{\tilde X\Psi}=-\mu^{\Psi\tilde X}=0$, leaving $\delta_h\tilde X=\mu^{\tilde X
\tilde X}E_{\tilde X}$ with $\mu^{\tilde X\tilde X}$ antisymmetric — contradicting the
symmetric map (16.4). So the two-EOM route fails as well: $\delta_h\tilde X$ is **not**
HT-trivial by any generator.

### 3.4 $\delta_h\tilde X$ is a compensator, not a standalone symmetry

Freeze $\Psi$ (so $\delta\Psi$ enters only inside $V_5$, not via $\delta K_\Psi$). Then

$$
\delta_hS_3=E_{\tilde X}\!\cdot\!\delta_h\tilde X
  =E_{\tilde X}^\top\mu\,E_{\tilde X}
  =-\tfrac{g_s^3}{120}\,V_5(\tilde X,\tilde X,\delta\Psi)\neq0,
\tag{16.5}
$$

a *symmetric* contraction, generically nonzero (consistent with (16.4): a symmetric
$\mu$ gives a nonvanishing quadratic form on even $E$). So $\delta_h\tilde X$ **alone is
not a symmetry**. The full transformation is a symmetry only because the same
$\delta\Psi$ generates, through the $\Psi$-dependence of the kinetic operator, the
compensating anomaly

$$
(\delta K_\Psi)(\tilde X,\tilde X)=-\tfrac{g_s}{5}V_5(\tilde X,\tilde X,\delta\Psi),
\qquad
2K_\Psi(\delta_h\tilde X,\tilde X)+(\delta K_\Psi)(\tilde X,\tilde X)=0,
\tag{16.6}
$$

which is exactly R17's check-5 invariance (B.3). Thus $\delta_h\tilde X$ is
**inextricably tied to $\delta\Psi$**: it is the piece that cancels the
$\delta K_\Psi$-anomaly, not an independent transformation one could switch on with its
own parameter.

## 4. Commentary (by label)

- **(16.2), the decisive sign.** The graded-antisymmetry condition is derived, not
  quoted, because the $(\epsilon_i+\epsilon_j)(1+p)$ factor is exactly the "graded sign"
  the brief flags as potentially decisive. The lesson is the *opposite* of the naive
  hope: for an all-**even** sector the parameter parity $p$ multiplies $\epsilon_i+
  \epsilon_j=0$ and **drops out**, so no choice of $\delta\Psi$-parity can convert the
  required *anti*symmetry into *symmetry*. The slogan "symmetric kernel ⇒ not a trivial
  symmetry" — which the note (011 §4) correctly suspected but left open — is therefore
  *right* here, but for a sharper reason than bosonic intuition: it survives the full
  graded analysis because the fields are even. (The graded loophole is real, but it
  lives in the odd sector: e.g. two odd fields with an even parameter genuinely flip
  symmetric↔antisymmetric. It is simply inapplicable to $\Sym^2\Hilb_0$, all even.)

- **(16.4), why $\delta\Psi$ is a spectator.** The would-be antisymmetriser is the
  exchange of the two $\Sym^2$-slots of $V_5$ that $K_\Psi^{-1}$ contracts. $\delta\Psi$
  sits in the *third* $V_5$-slot and is untouched by that exchange; its parity can never
  appear in the $I\leftrightarrow J$ sign. This is the concrete refutation of "insert
  the field parities and the bilinear antisymmetrises": the parity that would have to do
  the work belongs to a field ($\delta\Psi$) that is not one of the two being exchanged.
  This spectator argument is *analytic* and carries the claim by itself. (Check 3's
  numerical companion is only a sign-flip: it confirms $W_{\delta\Psi}$ is symmetric
  and linear in $\delta\Psi$ for $\pm\delta\Psi$, but a sign flip does **not** model
  a Grassmann-odd $\delta\Psi$ — there is no odd variable in the real-vector toy
  [reworded 2026-07-09, critic M4].)

- **(16.5)+(16.6), the category error.** These two lines are the heart of the
  resolution. $\delta_h\tilde X$ is *not a symmetry by itself* (16.5); it becomes part
  of a symmetry only glued to $\delta\Psi$ through $\delta K_\Psi$ (16.6). The HT
  trivial/nontrivial classification is a predicate on *actual symmetries*; applying it
  to the standalone piece $\delta_h\tilde X$ is ill-posed. Once one asks the well-posed
  question — "what is the transformation law of the auxiliary field $\tilde X$ under the
  single $\Lambda$-symmetry, and is it removable?" — the answer is unambiguous: it is
  the contractible-pair tail (§5).

- **Reconciliation with R11 ((X,X⁺) contractible pair).** At $O(g_s^2)$ the kinetic
  kernel is the *undressed* $V_4$, which is $\Psi$-**independent**; so $\delta K=0$,
  there is no anomaly, and the auxiliary rotation is *zero* — $\delta X=0$ (R11's exact
  $\delta X=0$). $\tilde X$ is then a clean contractible pair. At $O(g_s^3)$ the kernel
  dresses to $K_\Psi$, acquires $\Psi$-dependence, and the auxiliary rotation becomes
  *nonzero* (16.6) — but still $\propto\tilde X$ (on-shell-vanishing), so the pair stays
  contractible. **The contractible-pair structure of R11 persists; only the kinetic
  became field-dependent, forcing a nonzero (but EOM-proportional) auxiliary rotation.**
  This is the precise $O(g_s^3)$ statement of R11's BV entry.

- **Reconciliation with R18/012 ("no independent two-string parameter").** 012 §6
  already read the homogeneity of $\delta\tilde X$ as "the tower keeps pulling back the
  Ψ-gauge structure rather than generating new parameters." §3–§5 make this exact: the
  generator $R^{\tilde X}_\Lambda\propto\tilde X$ carries the *single* $\Lambda$, not a
  new $\Lambda_1\in\Sym^2$; it vanishes on-shell and is eliminable. No two-string gauge
  parameter is introduced at $O(g_s^3)$. The slogan "the HS step costs nothing in gauge
  invariance" is upheld at the BV-bookkeeping level: the only gauge structure is the
  auxiliary tail of the *closed-string* symmetry.

- **Grounding B5's labels (015 §4.1/§4.2).** "Trivial homogeneous" ($\delta Y_3=0$):
  $\Sigma_3$'s kinetic $\tilde M$/$M$ is $\Psi$-independent, so $\delta(\text{kinetic})
  =0$, no anomaly, forced rotation $=0$ — the *strictly-trivial* corner of the
  contractible pair (the R11 corner). "Implicit homogeneous" ($\delta Y_2$): the
  $\Sigma_2$-Hessian $\mathcal K$ is $\Psi$-dependent, so a nonzero rotation
  $\propto Y_2$ is forced to cancel $\delta\mathcal K$, and the relation is *implicit*
  (Neumann) because the Hessian's $Y_2$-dependence makes it nonlinear. **Both are the
  same BV object as $\delta\tilde X$** — field-dependent contractible pair — with
  $\delta Y_3=0$ the degenerate (field-independent-kinetic) limit. The machine check
  (§6, check 6) exhibits exactly this: switching the kernel's $\Psi$-dependence on/off
  toggles the forced rotation between $\delta\tilde X$-like (nonzero) and
  $\delta Y_3$-like (zero), with $\mu$ symmetric in *both* cases (never HT-trivial).

## 5. Result

$$
\boxed{
\begin{aligned}
&\text{The homogeneous term }\delta_h\tilde X=\tfrac{g_s}{10}K_\Psi^{-1}
  V_5(\cdot,\tilde X,\delta\Psi)\text{ is:}\\
&\bullet\ \textbf{not}\ \text{a Henneaux–Teitelboim trivial gauge symmetry — the
  effective generator }\mu=-\tfrac{6}{5g_s}K_\Psi^{-1}W_{\delta\Psi}K_\Psi^{-1}\\
&\quad\text{is graded-}\textbf{symmetric}\ (16.4),\ \text{whereas even fields require an
  }\textbf{anti}\text{symmetric }\mu\ (16.2);\ \text{and it is}\\
&\quad\text{not even a standalone symmetry }(16.5);\\
&\bullet\ \textbf{not}\ \text{a nontrivial gauge symmetry — it carries no independent
  parameter and }R^{\tilde X}_\Lambda\propto\tilde X\ \text{vanishes on-shell};\\
&\bullet\ \text{the forced transformation law of the }\textbf{auxiliary field}\
  \tilde X\ \text{under the single }\Lambda\text{-symmetry —}\\
&\quad\text{the }O(g_s^3)\text{ descendant of R11's }(\tilde X,\tilde X^+)\
  \textbf{contractible pair},\ \text{with the sole new feature}\\
&\quad\text{that the dressed kinetic }K_\Psi\ \text{is }\Psi\text{-dependent, forcing a
  nonzero but EOM-proportional rotation.}
\end{aligned}}
$$

**Physical reading.** The gauge algebra of $S_3$ is **not deformed by any new parameter
at $O(g_s^3)$**; the extra term is auxiliary-sector bookkeeping (cohomologically
trivial, removed with $\tilde X$). It unifies with the $O(g_s^4)$ $\delta Y_2$ (015
§4.2, same class) and reduces to the $\delta Y_3=0$ / R11 corner when the auxiliary
kinetic is field-independent. The trivial/nontrivial HT dichotomy is the wrong axis;
the right axis is **contractible-pair auxiliary structure**, parametrised by the
field-dependence of the auxiliary kinetic.

## 6. Verification

Script `codes/verify-st4-bv-xtilde.py` (numpy, $\Sym^2\Hilb_0$ toy in the R14/R17
orthonormal basis; generic symmetric $V_4$, $V_5$; run 2026-07-06, **6/6 PASS**;
re-run 2026-07-09 after the check-3/check-6 relabelling, 6/6 PASS):

- **check 1 — reduction (16.3).** $\delta_h\tilde X$ computed from B.8 equals
  $\mu E_{\tilde X}$ with $\mu=-\tfrac{6}{5g_s}K^{-1}W_{\delta\Psi}K^{-1}$ and
  $E_{\tilde X}=-\tfrac{g_s^2}{12}K\tilde X$, to machine precision. (Confirms the
  generator identification.)
- **check 2 — $\mu$ symmetric, not antisymmetric (16.4).** $\|\mu-\mu^\top\|\approx0$
  and $\|\mu+\mu^\top\|\gg0$; the distance from $\mu$ to the nearest antisymmetric
  matrix $=\|\tfrac12(\mu+\mu^\top)\|>0$. **Decisive:** no antisymmetric generator
  reproduces $\delta_h\tilde X$, i.e. it is not HT-trivial.
- **check 3 — $W_{\delta\Psi}$ symmetric and linear in $\delta\Psi$ (sign-flip
  leg).** $W_{\delta\Psi}$ is symmetric for $\delta\Psi$ and for $-\delta\Psi$
  alike. **Honest scope [M4]:** a sign flip is *not* a Grassmann-odd probe (the
  toy has no odd variables); the claim that the *parity* of $\delta\Psi$ cannot
  antisymmetrise $\mu$ is carried by the analytic spectator argument (§3.2:
  $\delta\Psi$ sits in the untouched third $V_5$-slot, so its parity never enters
  the $I\leftrightarrow J$ exchange sign), which needs no numerical companion.
- **check 4 — not a standalone symmetry (16.5).** With $\Psi$ frozen,
  $E_{\tilde X}^\top\mu E_{\tilde X}=-\tfrac{g_s^3}{120}V_5(\tilde X,\tilde X,\delta\Psi)
  \neq0$ (generic), matching the closed form.
- **check 5 — the compensation (16.6).** $2K(\delta_h\tilde X,\tilde X)+(\delta K)
  (\tilde X,\tilde X)=0$ to machine precision (the full-transformation invariance of the
  dressed quadratic form; cross-check of R17 check-5).
- **check 6 — field-dependence toggles the rotation; $\mu$ stays symmetric
  (grounds B5).** With the $\Psi$-**dependent** $K_\Psi$ the forced rotation is
  nonzero ($\delta\tilde X$/$\delta Y_2$ corner), and $\mu$ is symmetric (never
  antisymmetric) in **both** corners — these legs are genuine. **The
  $\Psi$-independent zero-rotation leg is ILLUSTRATIVE only [C3]:** $\delta K$ is
  set to the zero matrix *by definition* of a $\Psi$-independent kernel, so the
  solved rotation is $0=0$ by construction — it *illustrates* the $\delta Y_3$
  corner rather than testing it. (The genuine $\delta Y_3=0$ machine test is
  check 3 of `verify-b5-ogs4-gauge-eom-ibl.py`, rewritten 2026-07-09.) The
  decisive content of this derivation is checks 2–5.

Dimensional/grading check (analytic): $V_5$ eats $(\Sym^2,\Sym^2,\Hilb_0)$ at
$N_{\rm gh}=4+4+2=10$ (5-punctured-sphere saturation, R17 §1); $\mu=K^{-1}W K^{-1}$
maps a saturation-10 covector to an $N_{\rm gh}=4$ vector after two $K^{-1}$ — matches
$\delta\tilde X\in\Sym^2$ ($N_{\rm gh}=4$). The $g_s$-power of $\mu$ is $g_s^{-1}$
(one explicit $g_s$ from $W_{\delta\Psi}\sim V_5$ minus two from the $E_{\tilde X}
\sim g_s^2$ normalisation), so $\mu E_{\tilde X}\sim g_s^{-1}\cdot g_s^2=g_s$ — matches
the $\tfrac{g_s}{10}$ prefactor of B.8. ✓

## 7. What is established vs open

**Established (machine-checked, finite-dim algebraic layer):** the BV class of
$\delta\tilde X$ (auxiliary/contractible-pair, not HT-trivial, not nontrivial); the
graded computation showing $\mu$ symmetric with $\delta\Psi$ a spectator; the unified
classification covering $\delta\tilde X$ ($O(g_s^3)$), $\delta Y_2$ ($O(g_s^4)$), and
$\delta Y_3=0$; consistency with R11/R18/R21.

**Open / carve-outs:** (a) CFT-level analytics of $K_\Psi^{-1}$ (A2(iii)/T4) — the
classification is algebraic and does not need it; (b) worldsheet-$N_{\rm gh}$ label of
the antifield $\tilde X^+$ (convention, §1 — natural choice stated, not forced by the
ledger); (c) the all-orders statement (the auxiliary tower $\Sigma_k$ as an iterated
contractible-pair structure with field-dependent kinetics) — suggested, not proved;
(d) a blind critic pass (recommended, as for R16/R21).
