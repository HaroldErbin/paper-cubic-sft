# 021 — RS4: pinning the CFT sewing/propagator fixtures behind claim (1.a)

**Date:** 2026-07-09 (RS4 diagnostic pass).
**Status:** literature-grounding of the single structural claim (1.a) of derivation 020
and `knowledge/cubic-sft-riemann-surfaces.tex` against the primary CFT source. Machine
check: `codes/verify-rs4-sewing-fixtures.py` (27/27 PASS, seed 20260709).
**Primary source:** H. Erbin, *String Field Theory: A Modern Introduction* (the project's
`\cite{Erbin2023}`). Chapters read:
`bsft_bv.tex` (in full), `bos_feynman.tex` (propagator/sewing + stubs), `bos_geometry_Pgn.tex`
(plumbing fixture). **This pass is diagnostic only** — it does not edit 020 or the tex note;
it delivers the verdict and the precise downstream patch list.

**Verdict (headline).** **VERIFIED WITH CORRECTION.** The structural content of (1.a) — one
$\omega_1^{-1}$ contraction is a *rigid, length-frozen* closed-string gluing, of measure zero
in the moduli space of the resolved surface — is correct and now grounded in Erbin's
conventions. But the parenthetical fixture characterisation "**no $b$-ghost insertion**"
(bare identity $\sum_a|\phi_a\rangle\langle\phi^a|$ with nothing else) is **wrong**. The
correct fixture is
$$
\boxed{\;\omega_1^{-1} \;=\; b_0^-\,\delta_{L_0^-,0}\;}
$$
— it carries exactly **one** $b$-ghost ($b_0^-$) and the level-matching projector
$\delta_{L_0^-,0}$. What the frozen contraction is *missing* relative to the full propagator
is only the **length-modulus factor** $b_0^+/L_0^+$ (the $b_0^+$ ghost and the Schwinger
integral $\int_0^\infty ds\,e^{-sL_0^+}$). The caveat already anticipated this ("the $c_0^-$
of $\omega_1$ dualising to a $b_0^-\delta_{L_0^-,0}$ structure in $\omega_1^{-1}$"); RS4
confirms it is not a caveat to be dispelled but a genuine correction to the "no $b$" wording.
The correction is **benign for every structural conclusion** of 020/the note (genus formula,
coupling grading, no on-shell pole, no worldsheet locus for $m_2^{-1}$, the three-grading
table); it only sharpens *which* insertion distinguishes contact from propagation.

---

## 0. Restated task and objective

Literal task: check claim (1.a) — "one $\omega_1^{-1}$ contraction between two punctures is
plumbing at a frozen neck modulus ($q=1$, no $b$-ghost insertion): a legitimate CFT surface,
of measure zero in its moduli space" — against Erbin's book, and answer three fixture
questions (i)–(iii). Objective: (1.a) is the single not-yet-CFT-verified load-bearing claim
under the entire Riemann-surface reading of $m_2$/$m_2^{-1}$; the whole geometric side of the
paper rests on it. Success = a calibrated verdict (VERIFIED / …WITH CORRECTION / REFUTED)
plus, if not clean, an exact downstream patch list.

All conventions are Erbin's book (metric, ghost zero-mode split, BPZ) as in the project's
global conventions; $\hbar=c=1$, $\alpha'$ explicit where it appears.

---

## 1. Convention translation table (book ↔ project), verified on the propagator

Built **before** combining any book formula with 020/the note, per the research-skill
convention-translation rule. Verified on one quantity common to both (the propagator) in §2.

| object | Erbin book (`\cite{Erbin2023}`) | project (020 / note) | relation |
|---|---|---|---|
| off-shell Hilbert space | $\mc H^-\cap\ker L_0^-$, $\mc H^-=\ker b_0^-$ (`bos_feynman` §amp-prop; `bsft_bv` eq. `field-constraints`) | $\Hilb_0=\ker L_0^-\cap\ker b_0^-$ (020 §0) | **identical** |
| ghost zero-mode split | $\downarrow\downarrow,\downarrow\uparrow,\uparrow\downarrow,\uparrow\uparrow$ (`bsft_bv` eq. 57–73); field = $\downarrow\downarrow$ ($b_0^\pm=0$) | field states $\phi_a$, $b_0^\pm\phi_a=0$ | field = $\downarrow\downarrow$; dual $\phi^c$ = $\uparrow\uparrow$ ($c_0^\pm=0$, `bos_feynman` 674–678) |
| zero-mode algebra | $\{b_0^\pm,c_0^\pm\}=1$, cross $=0$, $b_0^\pm{}^2=0$; $b_0^\pm=b_0\pm\bar b_0$, $c_0^\pm=\tfrac12(c_0\pm\bar c_0)$ (`bsft_bv` 195; used 261) | same | **identical** (verified, script check 1) |
| BPZ pairing | $\langle\phi_r^c|\phi_s\rangle=\delta_{rs}$ (`bsft_bv` eq. 76–79) | $\langle\cdot|\cdot\rangle_{\rm bpz}$ | **identical** |
| symplectic form | $\langle A|c_0^-|B\rangle$; action $\tfrac12\langle\Psi|c_0^- Q_B|\Psi\rangle$, vertices $\mc V_{0,n}=\langle\Psi|c_0^-|\ell_{0,n-1}\rangle$ (`bsft_bv` eq. `V02-vertex-QB`, 399) | $\omega_1(A,B):=\langle A|c_0^-|B\rangle_{\rm bpz}$ (note eq. `mtwo`) | **identical**: $\omega_1$ = Erbin's $c_0^-$-BPZ symplectic form |
| free kinetic operator | $K=c_0^-c_0^+L_0^+\delta_{L_0^-,0}$ (`bsft_bv` eq. `closed-fixed-kinetic-op`, lines 180–187) | — | $\langle A|K|B\rangle=\omega_1(A,c_0^+L_0^+\delta\,B)$ |
| propagator | $\Delta=b_0^+b_0^-\,\dfrac{1}{L_0^+}\,\delta_{L_0^-,0}$ (`bsft_bv` eq. `propagator-fixed` 161–168 = `bos_feynman` eq. `offshell-prop-bpm` 616–620) | $\mathsf P=\dfrac{b_0^+b_0^-}{L_0^+}\delta_{L_0^-,0}$ (note eq. `sewing` / 020 eq. 0.2) | **identical, normalisation included** (§2) |
| plumbing modulus | $w^{(1)}w^{(2)}=q$, $|q|\le1$, $q=e^{-s+i\theta}$, $s\ge0$, $\theta\in[0,2\pi)$ (`bos_geometry_Pgn` eq. `plumbing`, `q-s-th`) | $q$, $s$, $\theta$ (note §kernels) | **identical** |
| stub | $s\in[s_0,\infty)$; $\Delta(s_0)=b_0^+\dfrac{e^{-s_0L_0^+}}{L_0^+}b_0^-\delta_{L_0^-,0}$ (`bos_feynman` eq. `offshell-prop-bpm-stub` 1031–1036) | stub parameter $s_0$ (note retraction ¶) | **identical** |

Two notational cautions recorded for downstream use:

- Erbin's $c_0^\pm=\tfrac12(c_0\pm\bar c_0)$ carries a factor $\tfrac12$ that $b_0^\pm=b_0\pm\bar b_0$
  does **not**; this is exactly what makes $\{b_0^\pm,c_0^\pm\}=1$ (not $2$ or $\tfrac12$). Any
  hand-manipulation of $\omega_1=c_0^-$ must keep this factor.
- The project's index-raising bivector $\omega_1^{-1}=\sum_a|\phi_a\rangle\langle\phi^a|$ uses
  the $\omega_1$-**dual** $\langle\phi^a|$ ($\langle\phi^a|c_0^-|\phi_b\rangle=\delta^a_b$),
  **not** the BPZ-dual $\langle\phi_a^c|$ ($\langle\phi_a^c|\phi_b\rangle=\delta_{ab}$). They
  differ by exactly one $c_0^-$: $\langle\phi^a|c_0^-=\langle\phi_a^c|$. This one-$c_0^-$ gap is
  the entire content of the correction below.

---

## 2. Convention check on the shared quantity (the propagator normalisation)

Erbin derives the propagator from the plumbing integral (`bos_feynman` eq. `fact-prop-op`
573–575):
$$
\Delta=\frac{1}{2\pi\I}\int\frac{\dd q}{q}\wedge\frac{\dd\bar q}{\bar q}\;
b_0\bar b_0\,q^{L_0}\bar q^{\bar L_0}.
$$
With $q=e^{-s+i\theta}$: measure $\frac{\dd q}{q}\wedge\frac{\dd\bar q}{\bar q}=-2\I\,\dd s\wedge\dd\theta$
(eq. 588–589); ghost recombination $b_0\bar b_0=-\tfrac12 b_0^+b_0^-$ (from $b_0^+b_0^-=-2b_0\bar b_0$);
weight $q^{L_0}\bar q^{\bar L_0}=e^{-sL_0^++i\theta L_0^-}$. Hence
$$
\Delta=\frac{1}{2\pi\I}(-2\I)\!\left(-\tfrac12\right)b_0^+b_0^-\!\int_0^\infty\!\dd s\,e^{-sL_0^+}\!\int_0^{2\pi}\!\dd\theta\,e^{i\theta L_0^-}
=\frac{1}{2\pi}b_0^+b_0^-\cdot\frac{1}{L_0^+}\cdot2\pi\,\delta_{L_0^-,0}
=b_0^+b_0^-\frac{1}{L_0^+}\delta_{L_0^-,0},
$$
matching `bos_feynman` eqs. 593–620. The project's eq. (0.2)/`eq:sewing`, written as
$\mathsf P=\int_0^\infty\!\dd s\int_0^{2\pi}\!\frac{\dd\theta}{2\pi}\,b_0^+b_0^-\,e^{-sL_0^++i\theta L_0^-}$,
is **exactly** this, prefactor included — the note's "schematic normalisation" is in fact the
precise one. **Translation table verified.** (Answers question (i); see §3.)

---

## 3. Answer to (i): the exact propagator fixture

**VERIFIED-against-primary-source, exact.** In Erbin's own conventions the propagator is
$$
\Delta=b_0^+\,b_0^-\,\frac{1}{L_0^+}\,\delta_{L_0^-,0}
$$
with **no extra prefactor** (`bsft:eq:propagator-fixed`, lines 161–168; identical to
`bos:eq:offshell-prop-bpm`, lines 616–620). It is the plumbing sewing kernel and it inverts
the free kinetic operator $K=c_0^-c_0^+L_0^+\delta_{L_0^-,0}$ via
$K\Delta=\{c_0^-,b_0^-\}\{c_0^+,b_0^+\}=1$ on the constrained field (`bsft_bv` computation,
lines 252–273; reproduced as script checks 2, "K.Delta|uu>=|uu>", "Delta.K|dd>=|dd>"). The
note's `eq:sewing`/(0.2) kernel $\mathsf P$ equals $\Delta$ identically, normalisation
included (§2). **No change needed to `eq:sewing`/(0.2).**

The one refinement worth recording downstream: $\Delta$ **factorises** as
$$
\Delta=\underbrace{\frac{b_0^+}{L_0^+}}_{\text{length modulus }s}\;\cdot\;
\underbrace{b_0^-\,\delta_{L_0^-,0}}_{=\,\omega_1^{-1}\ \text{(level-matching sewing measure)}},
$$
(script check "Delta = (b0^+/L0^+).omega_1^{-1}"). The right factor is the frozen-neck
contraction; the left factor is precisely the length-modulus data that the frozen contraction
drops. This factorisation is the technical heart of the RS4 answer.

---

## 4. Answer to (ii): the exact ghost content of $\omega_1^{-1}$ — the crux

**Result: $\omega_1^{-1}=b_0^-\,\delta_{L_0^-,0}$, carrying one $b$-ghost, NOT the bare
identity.** Worked explicitly, two independent routes; not quoted.

### 4.1 Route A — from Erbin's $K,\Delta$ (operator factorisation)

The symplectic form is $\omega_1(A,B)=\langle A|c_0^-|B\rangle$, so $\omega_1$ **as an
operator is $c_0^-$** (sandwiched in BPZ). Its inverse bivector is the operator that inverts
$c_0^-$ on the field space $\ker b_0^-$. Because $\{c_0^-,b_0^-\}=1$, for any field state
$|\phi\rangle$ with $b_0^-|\phi\rangle=0$,
$$
b_0^-\,c_0^-\,|\phi\rangle=\big(\{c_0^-,b_0^-\}-c_0^-b_0^-\big)|\phi\rangle
=\big(1-c_0^-b_0^-\big)|\phi\rangle=|\phi\rangle .
$$
So $b_0^-$ is the left inverse of the "$\omega_1$ map" $c_0^-$ on $\ker b_0^-$; restoring the
level-matching projector that the closed-string state space always carries,
$$
\omega_1^{-1}=b_0^-\,\delta_{L_0^-,0}.
$$
Consistency with the propagator: $\Delta=b_0^+\frac{1}{L_0^+}\,b_0^-\delta_{L_0^-,0}
=(c_0^+L_0^+\delta)^{-1}\,\omega_1^{-1}$, i.e. the full propagator = (inverse of the
kinetic *map* $c_0^+L_0^+$) $\times$ (inverse of the *pairing* $\omega_1$). Erbin's
$K\Delta=1$ is exactly the statement that these two inverses assemble correctly (script
checks 2). This is the precise realisation of the caveat's phrase "the $c_0^-$ of $\omega_1$
dualising to a $b_0^-\delta_{L_0^-,0}$ structure in $\omega_1^{-1}$."

### 4.2 Route B — explicit ghost zero-mode matrices (independent)

Realise $b_0^\pm,c_0^\pm$ as $4\times4$ matrices on the zero-mode Fock space
$\{\downarrow\downarrow,\downarrow\uparrow,\uparrow\downarrow,\uparrow\uparrow\}$ with the
Koszul sign making holomorphic/antiholomorphic modes anticommute
(`codes/verify-rs4-sewing-fixtures.py`). The algebra $\{b_0^\pm,c_0^\pm\}=1$ (cross $=0$,
nilpotent) reproduces (check 1). On the field line $|\!\downarrow\downarrow\rangle$ one finds
$b_0^-c_0^-|\!\downarrow\downarrow\rangle=|\!\downarrow\downarrow\rangle$ (check "omega_1^{-1}=b0^-
on ker b0^-") while $c_0^-|\!\downarrow\downarrow\rangle\neq0$ (it lands in the dual/up sector).
Crucially $b_0^-\neq\mathbb 1$ (check "omega_1^{-1}=b0^- is NOT the identity") and $b_0^-$
lowers ghost number by one (check "$N_{\rm gh}(\omega_1^{-1})=-1$"). Falsification legs pass:
replacing $b_0^-$ by the identity breaks $K\Delta=1$, and the bare-identity reading fails the
propagator factorisation. All 27 checks PASS.

### 4.3 What this means for the crux question, and for a colour-2 edge

- The bare $\omega_1^{-1}$ contraction is **not** "$q=1$ plumbing with no $b$". It **is**
  $b_0^-\delta_{L_0^-,0}$: it carries one $b$-ghost and the level-matching projector. Relative
  to the propagator (0.2) it is missing **only** the length-modulus factor $b_0^+/L_0^+$.
- A **colour-2 edge** (`def:colour2edge`) is two such contractions,
  $G_2^{-1}=\omega_1^{-1}\otimes\omega_1^{-1}=(b_0^-\delta_{L_0^-,0})^{\otimes2}$: it carries
  **two** $b_0^-$'s (one per strand) and two level-matching projectors, and **no**
  $b_0^+/L_0^+$ on either strand. So the note's "no $b$-insertion at all" for the colour-2
  edge (§0 object 2; `eq:Skernel` commentary; §kernels "Kernel 2") is **imprecise** and must
  be corrected to "no *length-modulus* ($b_0^+/L_0^+$) insertion; the level-matching sewing
  measure $b_0^-\delta_{L_0^-,0}$ per strand is retained."
- **Why the structural conclusions survive.** The $b_0^-\delta_{L_0^-,0}$ is the *universal
  closed-string level-matching sewing measure* — it sits on **every** internal closed-string
  line, propagating or contact, because the state space is $\ker b_0^-\cap\ker L_0^-$. It does
  not correspond to a *length* modulus and produces **no** $1/L_0^+$ pole, hence **no**
  on-shell degeneration and **no** $g_s$. The single object that distinguishes a propagating
  (colour-1) line from a frozen (colour-2) edge is therefore precisely the presence/absence of
  the **length factor** $b_0^+/L_0^+$ — not the presence/absence of *all* $b$'s. Every
  downstream claim of 020/the note that reads "the colour-2 edge carries no modulus / no
  $g_s$ / no pole / freezes the neck" is **correct as stated**; only the *diagnostic
  phrasing* "one $b$ per real modulus, so the contact edge has zero $b$'s" needs to be
  refined to "the *length*-modulus $b_0^+/L_0^+$ is the discriminant; the twist/level-matching
  $b_0^-\delta_{L_0^-,0}$ is common to both."

**Subtlety flagged (for honesty about the diagnostic).** The note's "one $b$ per real
modulus" counts the propagator's *two* $b$'s ($b_0^+,b_0^-$) against its *two* moduli
$(s,\theta)$. Under the correction, the frozen edge keeps $b_0^-$ (and $\delta_{L_0^-,0}$) but
not the $\theta$-*integration*: the twist survives as a level-matched projector (a compact
direction integrated to a Kronecker $\delta$, contributing a finite volume $2\pi$, not a
non-compact modulus dimension), while the length $s$ is the genuine non-compact modulus that
is frozen. So the sharpened diagnostic is: **the number of non-compact ($s$-type) length
moduli integrated = the number of $b_0^+/L_0^+$ factors**; the $b_0^-\delta_{L_0^-,0}$ is
level-matching bookkeeping, not a length modulus. This is the one place the note's wording is
technically loose, and the patch list (§7) fixes it.

---

## 5. Answer to (iii): is $|q|=1$ frozen-neck sewing valid/convergent?

**Consistent-with the book for the *stubbed* coordinates the construction uses; a genuinely
separate question from R2 and R15(3).**

- **Bare (no-stub) range.** Erbin's plumbing requires $|q|\le1$, $q=e^{-s+i\theta}$, $s\ge0$
  (`bos_geometry_Pgn` eqs. `plumbing`, `q-s-th`, lines 413–432). Thus $|q|=1\iff s=0$ is the
  **boundary** of the allowed range — the "sharp" gluing where the two unit-radius coordinate
  disks are joined directly at their boundary circles, zero-length tube (interpretation 1,
  `bos_geometry_Pgn` 456–502). It is included in the range but is the borderline (shortest-tube)
  configuration; the book does not single it out or discuss a "$q=1$ frozen contraction," which
  is the project's own construct.
- **Stubbed coordinates (what the HS construction actually uses).** With a stub $s_0$ the
  plumbing range is $s\in[s_0,\infty)$, i.e. $|q|\le e^{-s_0}<1$, and the propagator gains the
  factor $e^{-s_0L_0^+}$: $\Delta(s_0)=b_0^+\frac{e^{-s_0L_0^+}}{L_0^+}b_0^-\delta_{L_0^-,0}$
  (`bos_feynman` eqs. `offshell-prop-bpm-stub`, `offshell-prop-k-stub`, lines 1024–1042). The
  canonical convention absorbs $e^{-\frac{s_0}{2}L_0^+}$ into each vertex puncture (line 1045),
  so the **vertex local coordinates are stub-dressed**. Contracting two stub-dressed punctures
  with the *frozen* $\omega_1^{-1}=b_0^-\delta_{L_0^-,0}$ (no $q^{L_0}$ weight) yields an
  effective operator $e^{-\frac{s_0}{2}L_0^+}\,b_0^-\delta_{L_0^-,0}\,e^{-\frac{s_0}{2}L_0^+}
  =e^{-s_0L_0^+}b_0^-\delta_{L_0^-,0}$: an effective neck of length $s_0>0$, a **regular,
  non-degenerate** surface, with the state sum converging by the $e^{-s_0 m^2}$ suppression the
  book establishes (lines 1058–1063). So "$q=1$" for the *stubbed* vertices is **not** a
  literal zero-length tube; the stub provides a finite effective neck and frozen-neck sewing is
  convergent. This is the correct precise statement to replace the note's "$|q|=1$ sewing for
  the stubbed vertex coordinates" caveat.
- **Relation to R2 and R15(3).** *Separate.* R2's "twist-only $|q|=1$ gluing of two
  $\mc V_3'$ reproducing $\partial\mc V_{0,4}$" is the **vertex-decomposition** programme (the
  note's trap T5) — a different construction (two asymmetric cubic vertices, not the HS quartic
  $\Sigma$-exchange), so it bears on a $|q|=1$ gluing but not on *this* object; it does not
  settle the HS frozen-neck. R15 item (3)'s $\beta\ge3/2$ positivity is about invertibility of
  $V_4$ on the tachyon block (the Gram matrix $\mtwo$), **not** about $|q|=1$ neck convergence;
  it neither establishes nor bears on it. The $|q|=1$ convergence question is answered instead
  by the **stub factor** $e^{-s_0L_0^+}$ above, which is the genuinely relevant fact.

---

## 6. Verdict and its scope

**VERIFIED WITH CORRECTION.**

- **Verified against the primary source:** the propagator fixture (i); the symplectic-form
  identification $\omega_1=c_0^-$-BPZ; the ghost content $\omega_1^{-1}=b_0^-\delta_{L_0^-,0}$
  (ii); the propagator factorisation $\Delta=(b_0^+/L_0^+)\,\omega_1^{-1}$; the whole
  translation table (§1); stub convergence of the frozen contraction (iii). Machine-checked
  ghost algebra: 27/27 PASS.
- **Correction required:** the phrase "**no $b$-ghost insertion**" / "bare identity
  $\sum_a|\phi_a\rangle\langle\phi^a|$" attached to the frozen-neck contraction and the
  colour-2 edge. The correct fixture carries $b_0^-\delta_{L_0^-,0}$ per strand; the
  discriminant against propagation is the *length* factor $b_0^+/L_0^+$, not the $b$-count.
- **Not affected (survives verbatim):** claim (1.a)'s structural content (rigid,
  length-frozen, measure-zero gluing); the genus formula (5.2)/`eq:genus`; the coupling
  grading and the three-grading table; "no on-shell pole, $\Sigma$ auxiliary"; the
  no-worldsheet-locus statement for $m_2^{-1}$ (§3.i, §10.2); the $\Sigma_k$-tower extension.
  None of these uses the $b$-count of the edge; they use the absence of the *length* modulus,
  which is correct.
- **Calibration:** answers (i) and (ii) are **verified-against-primary-source** (explicit
  book equations + independent machine check). Answer (iii) is **consistent-with** the book
  (the stub factor is Erbin's; the specific "$q=1$ frozen contraction" object and its
  convergence claim are the project's, established via that factor, not stated as such in the
  book). The non-degeneracy of $\omega_1$ on the *physical field* (needed for $\omega_1^{-1}$
  to exist) is standard/textbook and **not** re-derived here (the zero-mode script sees only
  the ghost sector); this is the one input taken from the literature rather than checked.

---

## 7. Precise downstream patch list (for the orchestrator; do NOT apply in this pass)

The verdict is not clean VERIFIED, so per the brief here is the exact list of what changes and
how. Nothing below alters a structural conclusion; all are fixture-wording corrections.

### 7.1 `agent/derivations/020-riemann-m2-geometric.md`

1. **§0, object 2 ("The colour-2 contraction"), and the line "No $q$, no $s$-integral, no
   $b$-insertion, no $L_0$."** Change "**no $b$-insertion**" → "**no length-modulus insertion
   $b_0^+/L_0^+$** (the level-matching measure $b_0^-\delta_{L_0^-,0}$ per strand is retained)".
   Keep "no $q$, no $s$-integral, no $L_0^+$" — those are correct.
2. **§0, eq. (0.2) commentary** ("exact fixtures per Erbin 2023 = task RS4"). Replace the
   forward-reference with the settled result: add the factorisation
   $\mathsf P=(b_0^+/L_0^+)\,\omega_1^{-1}$ with $\omega_1^{-1}=b_0^-\delta_{L_0^-,0}$, cite
   `bsft:eq:propagator-fixed` / `bos:eq:offshell-prop-bpm`.
3. **§1, claim (1.a) box.** Reword: "One $\omega_1^{-1}$ contraction $=b_0^-\delta_{L_0^-,0}$ =
   plumbing with the **length** modulus frozen (no $b_0^+/L_0^+$), retaining the level-matching
   sewing measure; a legitimate CFT surface of measure zero." Delete "$q=1$, no $b$-ghost
   insertion"; replace by "length-frozen, one $b_0^-$ retained". Drop the "(Fixture bookkeeping
   … is the precision task RS4)" parenthetical — it is now settled; cite this derivation (021).
4. **§8 item 2 ("Weakest step: (1.a)")** and the do-not-reintroduce list. Update: (1.a) is now
   "verified-against-primary-source with the $b_0^-\delta_{L_0^-,0}$ correction (021)", no
   longer "structural, consistent-with". The trap T3 ("resolving colour-2 edges into worldsheet
   plumbing necks with moduli — adds … $b$'s") should be refined: the colour-2 edge *does* carry
   $b_0^-$'s, but **no length-modulus $b_0^+$**; the trap is adding a *length* modulus.
5. **§2, eq. (2.1) $K(m)$ and §10.1 `def:frozenneck` text.** The bivector used to raise indices
   is $\omega_1^{-1}=b_0^-\delta_{L_0^-,0}$, not a bare $\sum|\phi_a\rangle\langle\phi^a|$ with
   "no weight". State that the sum $\sum_a|\phi_a\rangle\langle\phi^a|$ (with the $\omega_1$-dual
   $\langle\phi^a|$) *equals* $b_0^-\delta_{L_0^-,0}$ — the two descriptions are the same object,
   and the "no $q^{L_0}$, no $\int ds\,d\theta$" is right but "omitting the $b$-ghost insertions"
   is wrong (only the $b_0^+/L_0^+$ is omitted).

### 7.2 `knowledge/cubic-sft-riemann-surfaces.tex`

1. **`eq:sewing` commentary** (~line 398, "schematic normalisation; the exact fixtures … are
   task RS4"). Replace with: normalisation is exact (verified 021); add factorisation
   $\mathsf P=(b_0^+/L_0^+)\,\omega_1^{-1}$, $\omega_1^{-1}=b_0^-\delta_{L_0^-,0}$.
2. **§kernels, "Kernel 2" paragraph** (~lines 408–424) and the **"Physical meaning"**
   paragraph (~427–435). Change "no $b$-insertion" → "no *length-modulus* insertion
   $b_0^+/L_0^+$"; keep "no $q$, no $s$-integral, no $L_0$". In the physical-meaning paragraph,
   the sentence "the reason is the *absence* of a modulus on its line" → "the absence of a
   *length* modulus ($b_0^+/L_0^+$)"; the retained $b_0^-\delta_{L_0^-,0}$ is the universal
   level-matching measure, not a length modulus.
3. **`def:frozenneck`** (~lines 458–467). Correct: "omitting the accompanying $b$-ghost
   insertions" → "omitting the length-modulus factor $b_0^+/L_0^+$ (the $b_0^+$ ghost and the
   Schwinger integral $\int\dd s\,e^{-sL_0^+}$), while retaining the level-matching sewing
   measure $b_0^-\delta_{L_0^-,0}$". Add: the bivector is
   $\omega_1^{-1}=\sum_a|\phi_a\rangle\langle\phi^a|=b_0^-\delta_{L_0^-,0}$.
4. **(1.a) quote block** (~lines 468–476). Same reword as 020 §1 above; relabel from
   "Structural … not verified" to "verified-against-primary-source (021), with the
   $b_0^-\delta_{L_0^-,0}$ fixture". Remove the RS4-pending caveat; cite 021.
5. **`def:colour2edge`** (~lines 485–492). Add that $G_2^{-1}=\omega_1^{-1}\otimes\omega_1^{-1}
   =(b_0^-\delta_{L_0^-,0})^{\otimes2}$ carries two $b_0^-$'s (one per strand) and no
   $b_0^+/L_0^+$.
6. **§open (`sec:open`)** (~lines 1109–1113) and the **status table** (~line 1167, "(1.a)=RS4").
   Move (1.a) from "open" to "closed by 021 (verified-with-correction)"; keep A2(iii)
   (spectrum of $\mtwo$) as the remaining genuinely-open geometric item.
7. **Consistency sweep of the "one $b$ per real modulus" diagnostic** wherever it appears
   (§kernels intro ~336–340, Table 1 caption ~377–384): add a footnote/clause that the
   discriminant is the *length*-modulus $b_0^+/L_0^+$; the twist/level-matching
   $b_0^-\delta_{L_0^-,0}$ is common to all closed-string lines and is not counted as a length
   modulus.

**Not to touch:** `eq:genus`/(5.2), the three-grading table, `sec:inverse` (§3.i, Gram
identity, Neumann/Laplace), `sec:covering`, `sec:operad`, `sec:osft`, `sec:tower` — none uses
the corrected fixture beyond the wording items above.

---

## 8. Self-review

1. *Answers the objective?* Yes: (1.a) is now grounded in Erbin's book, with the one wording
   correction isolated and shown benign; the geometric side of the paper can cite 021 instead
   of carrying an open RS4 caveat.
2. *Weakest step?* The claim that retaining $b_0^-\delta_{L_0^-,0}$ does not spoil the
   ghost-saturation *diagnostic* — shored up by identifying it as the universal level-matching
   measure (present on colour-1 too) and by the explicit $K\Delta=1$ factorisation, but the
   full genus-1 four-point saturation with frozen necks was argued structurally, not counted
   $b$-by-$b$ on the resolved surface. Flagged in §4.3; it does not affect any conclusion but a
   dedicated saturation count on the resolved genus-1 surface would upgrade it from
   "consistent" to "verified".
3. *Not checked (and why acceptable):* non-degeneracy of $\omega_1$ on the physical field
   (standard closed-string symplectic form; the zero-mode script only sees the ghost sector);
   the moduli-space *measure-zero* statement (Euler-characteristic bookkeeping, ledgered R15);
   the analytic $s_0$-convergence bound (the $e^{-s_0m^2}$ suppression is Erbin's, quoted).
4. *What a stronger physicist finds in 5 min:* that "no $b$-insertion" was too strong — which
   is exactly the correction delivered. The next natural sharpening (item 2 above) is the
   explicit $b$-count on the resolved surface.

---

## References

- Erbin, H. *String Field Theory: A Modern Introduction* (project `\cite{Erbin2023}`,
  draft): `chapters/bsft_bv.tex` (propagator `bsft:eq:propagator-fixed` 161–168, kinetic
  `bsft:eq:closed-fixed-kinetic-op` 180–187, $K\Delta=1$ 252–273, symplectic vertices 399);
  `chapters/bos_feynman.tex` (propagator derivation 570–627, stubs 1024–1065);
  `chapters/bos_geometry_Pgn.tex` (plumbing `bos:eq:plumbing`/`q-s-th` 413–432).
- Companion check: `codes/verify-rs4-sewing-fixtures.py` (27/27 PASS, seed 20260709).
- Reused ledger: R2 (vertex-decomposition $|q|=1$, `knowledge/results.md`), R14/R15
  (coloured grading, $V_4^{-1}$), R23 ($N_{\rm gh}$ assignments).
