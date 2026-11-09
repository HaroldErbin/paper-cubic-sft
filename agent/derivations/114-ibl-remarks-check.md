---
description: Check of the 26 review remarks on the IBL section (07-ibl.tex) – the "features" paragraphs, the d = 1/2 grading, the reading of CFL Thm 6.1, and what the transfer theorem says physically about auxiliary fields
---

# 114 – Check of the review remarks on the IBL section

Brief: `agent/briefs/active-computator-ibl-remarks-20261107T1230.md`.

## Status

Complete (Parts 1–5, verification, ledger proposals), 2026-11-07; fix pass 1 (critic 114) applied the same day. No next step.

## Task and objective

- **Literal task.** Check the review remarks on `paper/sections/07-ibl.tex` (2026-11-07): (a) the three "features" paragraphs (L76–92) flagged as wrong or worrying, (b) the reading of the homotopy-transfer theorem (CFL Thm 6.1, L324), (c) whether something physically deeper follows from (b).
- **Objective.** The section is about to be cut and rewritten; the verdicts decide what is removed, corrected, or kept, and whether an improved statement carries information the section needs.

Note: CFL is Cieliebak, Fukaya and Latschev; the theorem under discussion (L325 of the section) is Theorem 6.1 of Cieliebak, Fukaya and Latschev (arXiv:1508.02741), cited as `Cieliebak:2015:HomologicalAlgebraRelated`.
CFL is not cached as a PDF; it is reviewed in `literature/reviews/RPEPEC4L.md` and `literature/reviews/RPEPEC4L-maurer-cartan.md` (the latter with page and equation numbers checked against v3), and these reviews are the source used here.

## Conventions and assumptions

- Physical ghost number, the book normalization, one $c_0^-$ per strand in the $n$-string pairing (the project conventions, `knowledge/conventions.md`).
- Single-strand pairing saturates at total ghost number 5, the sphere correlator at 6; input strands of a product sit at ghost number 2, output strands at 3, $N_{\rm gh}(p_{m,n}) = 3n - 2m$ (section eq. `eq:ibl:ghost-numbers`).
- CFL degrees (review `RPEPEC4L-maurer-cartan.md` (1), CFL §2 p. 9–10): $|\mathfrak p_{k,\ell,g}| = -2d(k+g-1)-1$ on $E_kC \to E_\ell C$, $|\hbar| = 2d$, $d \in \mathbb Z$.

## Claim tree

- **A1** Project conventions as above (C-entries of `knowledge/conventions.md`; physical ghost number, book normalization).
- **A2** CFL's definitions and theorem statements are taken from the two cached reviews (`RPEPEC4L*.md`), not from the PDF.
- **A3** Genus zero, quartic order of the cubic action ($\Psi$, $\Sigma_2$), as in the section.
- **C1** Inventory: the 26 remarks sort into fact / presentation / convention / citation as in the Part 1 table. [block: Part 1]
- **C2** The "features" paragraphs (L77–92) are correct in their literal factual content and misleading in their framing; the objection to the third is correct. [by C2.1–C2.3]
  - **C2.1** The kinetic operator of the $n$-string field of ghost number $2n$ has ghost number $n = N_{\rm gh}(p_{n,n})$; an operator of ghost number one acting strand by strand (such as $\hat Q_B$) can be a kinetic operator only at $n = 1$. In an IBL$_\infty$ algebra, by contrast, $\hat{\mathfrak p}_{1,1,0}$ acts on every strand. [by A1, A2; eq. (K.1)–(K.2)] [check: C2.1]
  - **C2.2** In the parity "worldsheet ghost number mod 2" the $n$-string pairing has parity $n \bmod 2$, so the 2-string pairing is even and is not a BV symplectic form; the BV$_\infty$ structure of an IBL$_\infty$ algebra (CFL §1, Markl–Voronov) is an operator on $EC$, not such a form, so it does not contradict the text. [by A1, A2; block B]
  - **C2.3** $\langle\Sigma, p_{2,2}\Sigma'\rangle_2 = V_4(\Sigma,\Sigma')$, and self-adjointness of $p_{2,2}$ for the graded-symmetric 2-string pairing is equivalent to pair-exchange symmetry of $V_4$; the pairing's symmetry enters (wrong symmetry spoils self-adjointness). [by A1; eqs. (S.1)–(S.2)] [check: C2.3]
- **C3** The unique per-strand degree affine in the ghost number that reproduces CFL's genus-zero degrees is $3 - N_{\rm gh}$, and it forces $d = \tfrac12$; the alternative $N_{\rm gh} - 2$ gives a degree depending on the number of outputs; at $d = \tfrac12$, $|\hbar| = 2d$ is odd. [by A2; eqs. (D.1)–(D.2)] [check: C3]
- **C4** Under PH1 (C4.3) and, for the BRST-spectrum clause C4.5, under R73's hypotheses PH1, PH5, PH14 [$O(g_s^4)$], PH27: the reading of CFL Thm 6.1 is correct as "only $\mathfrak p_{1,1}$ determines the one-particle states", not as "the other kinetic terms define auxiliary fields"; the latter holds for $\Sigma_2$ in the cubic action by C2.1, R41 and R73, not by Thm 6.1; the remark on L328 is correct. [by C4.1–C4.5]
  - **C4.1** (R1) The canonical model of an IBL$_\infty$ algebra with $\mathfrak p_{1,1,0} = Q_B$ lives on $E H(Q_B) = \mathrm{Sym}\,H(Q_B)$, the Fock space on the one-particle states $H(Q_B)$; the multi-string sectors are not empty. [cited: CFL Thm 6.1 via review `RPEPEC4L.md`; by A2] [check: C4.1]
  - **C4.2** (R2) Inside CFL's framework no multi-string direction has a $(k,k)$ operation as its only quadratic term, and $\mathrm{Sym}^k H(Q_B)$ survives: the multi-string directions are not auxiliary. [by C2.1, C4.1]
  - **C4.3** Under PH1, at quartic order, the pair ($\Sigma_2$, its equation of motion) is acyclic on the classical complex and its elimination is an $L_\infty$ homotopy transfer onto the quartic-truncated theory; this controls the solutions and their linearization, not the BRST spectrum. [by C2.1, R41 (Conditional(PH1))]
  - **C4.4** Strictification and auxiliary-field elimination are mutually inverse quasi-isomorphisms (for $\Sigma_2$: on the classical complex, under PH1); the minimal model is a further transfer onto $H(Q_B)$, whose genus-zero brackets are the tree-level on-shell amplitudes; the text's "minimal model opposite to strictification" conflates them. [by C4.1, C4.3; cited: Kajiura 2007 (minimal model of $A_\infty$, tree amplitudes); block 3.4]
  - **C4.5** The BRST cohomology of the cubic theory around a background equals $H(Q^{(k)}_{\Psi_0})$ in all ghost numbers to the truncation order ($\Sigma_2$, $k \in \{2,3\}$, $\ker V_4$ quotiented): the auxiliary field carries no physical state. [by R73 (mixed; string transfer Conditional(PH1, PH5, PH14 [$O(g_s^4)$], PH27) through R62)]
- **C5** Physical reading (Part 4): the $(2,2)$ failure is the mismatch between the crossing-symmetric master equation and CFL's requirement of at least one input and one output. [by C5.1, C5.2] (The statement that the transferred several-output operations are in/out on-shell amplitudes is a proposal, Part 4 item 4, not a node.)
  - **C5.1** The $(2,2)$ residual is $\tfrac12 T_4$, the channel with one incoming and one outgoing leg at each vertex, its own mirror image, while the mirrors of $T_1$–$T_3$ pass through operations with no input or no output. [by R31; section eqs. `eq:ibl:polarized-22`, `eq:ibl:io-22`]
  - **C5.2** In CFL's framework the operations with no output belong in a Maurer–Cartan element (fillings). [GAP] (reading of CFL §9 and review obs. 9; not checked against the paper; not used by any verdict)

Open gaps: C5.2
Hypotheses in force: PH1 (C4.3, C4.4); PH1, PH5, PH14 [$O(g_s^4)$], PH27 through R73/R62 (C4.5)

## Part 1 – Inventory

Line numbers are those of `paper/sections/07-ibl.tex` at 2026-11-07 (the line of the review comment).
Kind: **F** fact (checkable), **P** presentation, **Cv** convention, **Cit** citation.

| L | Text claim | Review objection | Kind | Handled in |
|---|---|---|---|---|
| 7 | Markl 2001 and Münster–Sachs cited for IBL in SFT | Markl does not discuss IBL; the inverse pairing alone does not make an IBL algebra | Cit + F | Part 1 verdict below |
| 15 | (section intro) | the section ignores that higher products come from reduced vertices; add a caveat | P (+F: true) | Part 5 |
| 34 | $\Psi_{\rm tot}$ | notation is now $\boldsymbol\Psi$ | P (mechanical) | Part 5 |
| 49 | "one more output slot raises the ghost number by five" | unclear | P (statement is true: $3n-2m$ changes by $3+2$) | Part 5 |
| 53 | dictionary gives $d = \tfrac12$ | why? is there a better suspension, e.g. $N_{\rm gh}-2$? | F + Cv | Part 2b (C3) |
| 76 | kinetic operator of $\Sigma_2$ is $p_{2,2}$, not BRST; contrast with the loop homotopy algebra | nothing supports a BRST kinetic term for $\Sigma_2$; importing SFT structures to the auxiliary field | F + P | Part 2 (C2.1) |
| 83 | $\Sigma_2$ auxiliary; the two sectors differ in BV structure (no single odd symplectic form) | why does Markl's MV-formalism IBL not give a BV structure? | F | Part 2 (C2.2) |
| 90 | symmetry of the $\Sigma_2$ kinetic term is a property of the vertex, not of the pairing | vertex symmetry and pairing symmetry are tied, as cyclicity of $\ell_n$ follows from symmetric vertices | F | Part 2 (C2.3) |
| 132 | $p^\Omega$ and $p$ "different maps" on odd inputs | it is a sign convention, like suspensions for $A_\infty$ | Cv | Part 5 |
| 178 | italic statement mixes two coefficient conventions | clarify | P | Part 5 |
| 181 | "the argument is finite-dimensional" | why finite-dimensional? | P (+F) | Part 5 |
| 184 | the family is not an IBL algebra in the sense of CFL Def. 2.3 | say clearly: relations include $m=0$ / $n=0$ operations; CFL have an extended definition | F + P | Part 5 |
| 224 | $L$, $K$ notation | new notation | P | Part 5 |
| 241 | $\mathfrak{sl}_2 \oplus \mathfrak{sl}_2^*$ counterexample | useful? | P | Part 5 |
| 256 | $\hbar$ | do not use $\hbar$ | P (cut by plan) | Part 5 |
| 263 | parity-inhomogeneous $\mathcal D$ paragraph | not understood | P (cut by plan) | Part 5 |
| 266 | brace criterion origin | origin not stated; to check | F (cut by plan) | Part 5 |
| 282 | "the criterion" | needs a name or reference | P (cut by plan) | Part 5 |
| 292 | start of restricted correspondence | repeats the above | P | Part 5 |
| 306 | quartic-order limitation | keep, move after the counterexample | P | Part 5 |
| 320 | homotopy transfer paragraph | make it a subsection | P | Part 5 |
| 324 | CFL Thm 6.1 | reading: only $p_{1,1} = Q_B$ carries physical states; any other kinetic term defines an auxiliary field; comment on it | F | Part 3 (C4), Part 4 |
| 328 | "minimal model goes opposite to strictification" | conflation: elimination of auxiliary fields is homotopy transfer; minimal model integrates everything out (on-shell states, S-matrix) | F | Part 3 (C4.4) |
| 338 | classical-complex paragraph | not understood | P (+F: content is R41/R36) | Part 5 |
| 353 | $\hat Q_B$ in the $\Lambda_2$ paragraph | undefined here, and "wrong above" | F + P | Part 2 (C2.1), Part 5 |
| 360 | $\Lambda_2$ tower paragraph | delete, mention elsewhere | P | Part 5 |

**L7, verdict (citation).** The objection is correct on the substance.
Markl's loop homotopy algebras are $L_\infty$ algebras with a BV-type second-order operator (quantum $L_\infty$); they are not presented as IBL algebras, and the presence of the inverse pairing does not make them one.
Münster–Sachs (2013) do relate the quantum closed (and open-closed) homotopy algebra to IBL$_\infty$ language, and CFL and Markl 2015 (MV formalism) define the IBL structure.
Recommendation: cite CFL and Münster–Sachs for IBL in SFT; Markl 2001 only where the loop homotopy algebra itself is meant.

## Part 2 – The "features" paragraphs (L74–92)

### 2.1 First feature (L77–81): $\Sigma_2$ has $p_{2,2}$ and not $\hat Q_B$ as kinetic operator

Statements in the text:

- (i) the kinetic operator of $\Sigma_2$ is $p_{2,2}$, of ghost number 2;
- (ii) $\langle \Sigma_2, \hat Q_B \Sigma_2\rangle_2 = 0$ by ghost number ($4 + 5 = 9 \ne 10$);
- (iii) in the loop homotopy algebra / IBL framework the differential on every multi-string component is the derivation extension $\hat Q_B$;
- (iv) the only two-output object there is the inverse pairing;
- (v) hence the cubic action is "a different object".

**Ghost-number balance of kinetic terms (block K).**
A quadratic term $\langle \Phi, K\Phi\rangle_n$ for an $n$-strand field of total ghost number $N$ is nonzero only if $2N + N_{\rm gh}(K) = 5n$, so
$$N_{\rm gh}(K) = 5n - 2N. \tag{K.1}$$
For the tower of the cubic action, $N(\Psi_n) = 2n$ (strands at ghost number 2), hence
$$N_{\rm gh}(K_n) = n = 3n - 2n = N_{\rm gh}(p_{n,n}). \tag{K.2}$$
The derivation extension $\hat Q_B = \sum_{i} 1^{\otimes(i-1)}\otimes Q_B\otimes 1^{\otimes(n-i)}$ (Koszul signs) has ghost number 1, so it can be the kinetic operator only at $n = 1$.
This holds for any operator of ghost number one acting strand by strand, not only for $\hat Q_B$, and for any distribution of the ghost number $2n$ among the strands.

**Verdict on (i)–(ii): correct.** Both are facts, and (K.2) sharpens them: ghost-number balance alone forces the kinetic operator of the $n$-strand field to have ghost number $n$, which is the ghost number of $p_{n,n}$; a BRST-type (derivation, ghost number one) kinetic term exists only for the one-string field.

**Verdict on (iii): correct, and it is the relevant point.** In CFL's IBL$_\infty$ algebra the extension $\hat{\mathfrak p}_{1,1,0}$ of the differential to $E_kC$ is a derivation acting on every strand (CFL Remark 2.2, review `RPEPEC4L.md` obs. 2), and it appears in the $E_2$ component of the Maurer–Cartan equation as $\hat{\mathfrak p}_{1,1,0}(\mathfrak m_{2,0})$ at the leading order $\hbar^{-1}$, with $\mathfrak p_{2,2,0}(\mathfrak m_{2,0})$ only at $\hbar^{0}$ (review `RPEPEC4L-maurer-cartan.md` (2), boxed $E_2$ display).
The cubic action has the opposite pattern: no $\hat Q_B\Sigma_2$ term (by (K.2)) and $p_{2,2}\Sigma_2$ at leading order.
The contrast rests on the cubic action's coupling $g_s$ being ghost-neutral: in CFL the two terms on one component are balanced by $\hbar$, which has ghost number $-1$ in the dictionary of 2.4.
This is one of the reasons record 103 found that the equations of motion of $(\Psi,\Sigma_2)$ are not the IBL Maurer–Cartan equation with $\Psi_2 = \mathfrak m_{2,0}$ (103, H2 refuted within $f = \alpha\Sigma_2 + \beta\Psi^2$).

**Verdict on (iv)–(v): imprecise.** "The only object with two outputs is the inverse pairing" mixes the loop homotopy algebra (Markl's, an $L_\infty$ algebra with a second-order BV operator) with the IBL framework; see L7.

**Objection.** The paragraph is read as claiming that $\Sigma_2$ should have a BRST kinetic term.
The paragraph claims the opposite, so on the facts the objection and the text agree: $\Sigma_2$ must not inherit the single-string structures.
What is wrong is the framing: "two features distinguish it from the actions of the IBL type found in the literature" presents the derivation $\hat Q_B$ on multi-string components as a norm the cubic action departs from.
The useful content is not a comparison with the literature but a structural fact about IBL$_\infty$: there, the multi-string components always carry $\hat Q_B$, and they carry physical (multi-particle) states; $\Sigma_2$ cannot.
Overall verdict: **correct but misleading**.

**Improved version (useful; it feeds Part 3).**
"Ghost-number conservation fixes the kinetic operator of the $n$-string component $\Psi_n$, of ghost number $2n$, to have ghost number $n$: it is $Q_B$ for $n = 1$ and $p_{n,n}$ for $n \ge 2$, and no operator acting strand by strand with ghost number one, such as the extension $\hat Q_B$ of the BRST operator, can appear.
In an IBL$_\infty$ algebra, by contrast, the differential acts on every strand of a multi-string state; this is why the auxiliary fields of the cubic action are not the multi-string components of an IBL$_\infty$ field."
The second sentence needs a citation to CFL (Remark 2.2) and is the bridge to the reading of Thm 6.1 (Part 3).

### 2.2 Second feature (L84–89): $\Sigma_2$ auxiliary; the two sectors differ in BV structure

Statements:

- (i) $\Sigma_2$ is auxiliary: its equation $p_{2,2}(\Sigma_2) = p_{2,2}(\Psi^2)$ fixes $\Sigma_2 = \Psi^2$ on the quotient by injectivity of $p_{2,2}$ there;
- (ii) with Grassmann parity equal to worldsheet ghost number mod 2, the 2-string pairing between $\Sigma_2$ (ghost number 4) and the states of ghost number 6 is even, so no single odd symplectic form covers both sectors;
- (iii) sec:gauge nevertheless pairs $\Sigma_2$ with an odd antifield, reading parity from the target-space ghost number.

**Check of (ii) (block B).** The $n$-string pairing joins total ghost numbers $N$ and $5n - N$; its parity, as a bilinear form on states graded by $N \bmod 2$, is $5n \bmod 2 = n \bmod 2$.
It is odd for $n = 1$ (the antibracket form $\Omega$) and even for $n = 2$.
If the coefficients carry the parity that makes the total multi-string field even (the rule the section uses for $\Psi$), the pairing of $\Sigma_2$ with any partner is an even form, which cannot be a BV symplectic form.
So (ii) is **correct**, under that parity rule.
(i) is **correct** (the quotient is by the kernel of $p_{2,2}$, so injectivity there is by construction; the existence of the inverse level by level is PH1's content, R41).
(iii) is correct and is what sec:gauge does.

**Objection: why does Markl 2015 (MV formalism for IBL) not provide a way to define a BV structure?**
Two notions of "BV structure" meet here.

- CFL (§1; review obs. 4) state, and Markl–Voronov's MV formalism develops (as we recall the paper; it is not cached), that an IBL$_\infty$ structure is a BV$_\infty$ structure: a higher-order differential operator $\hat{\mathfrak p}$ on the graded-commutative algebra $EC$, squaring to zero. This is a BV structure on the algebra of multi-string states, built from the grading of single strands (on $C[1]$), and it requires no symplectic form on $EC$.
- The paragraph speaks of the field-theory BV formalism: an odd symplectic form on the space of fields, the antibracket, a master action. Its statement is that the multi-string pairings do not provide such a form in the worldsheet parity.

So the text is not contradicted by Markl–Voronov, but the question exposes that the paragraph does not say which BV notion it means, and that it gives no information the section uses.
The IBL$_\infty$/BV$_\infty$ operator of Markl–Voronov would be the natural BV structure **if** the cubic action were the Maurer–Cartan action of an IBL$_\infty$ algebra; record 103 shows that it is not with $\Psi_2 = \mathfrak m_{2,0}$, within the class $f = \alpha\Sigma_2 + \beta\Psi^2$ of identifications, which is a stronger and better reason than the parity count. The Markl–Voronov statement is from memory: [unverified reference].
Overall verdict: **correct but misleading, low value**.
Improved version: keep only (i) in one sentence (it is in sec:hs anyway); replace (ii)–(iii) by one sentence: "The BV formulation of the cubic action (sec:gauge) reads the parity of $\Sigma_2$ from the target-space ghost number; it is not the BV$_\infty$ structure that an IBL$_\infty$ algebra defines on the symmetric algebra [CFL; Markl–Voronov], since the cubic action is not of that form."
Whether that sentence is needed depends on whether the rewrite keeps the comparison with the MC equation; if not, drop (ii)–(iii) entirely.

### 2.3 Third feature (L91–92): exchange symmetry is "a property of the vertex rather than of the pairing"

Write $K(\Sigma, \Sigma') := \langle \Sigma, p_{2,2}\Sigma'\rangle_2$.
By the definition of $p_{2,2}$ (`eq:conv:sprod`), $V_4(A_1, A_2, B_1, B_2) = \langle A_1\otimes A_2, p_{2,2}(B_1, B_2)\rangle_2$, so
$$K(\Sigma, \Sigma') = V_4(\Sigma, \Sigma'), \tag{S.1}$$
with $\Sigma$ in the first two slots.
Hence $K(\Sigma, \Sigma') = K(\Sigma', \Sigma)$ by the symmetry of $V_4$ alone; no property of the pairing enters, because the pairing and its inverse cancel in (S.1).
That much of the sentence is literally true.

The point is that the same is true in ordinary SFT: $\langle\Psi, \ell_n(\ldots)\rangle = V_{n+1}(\Psi,\ldots)$, and the cyclicity of $\ell_n$ for the BPZ pairing is the full symmetry of $V_{n+1}$ read through a graded-symmetric pairing.
For $p_{2,2}$ the same equivalence holds:
$$\langle X, p_{2,2} Y\rangle_2 = \pm\langle p_{2,2} X, Y\rangle_2 \;\text{ for all } X, Y \iff V_4(X, Y) = \pm V_4(Y, X), \tag{S.2}$$
given that $\langle\cdot,\cdot\rangle_2$ is graded symmetric, with the Koszul sign of the swap (trivial on $\Sigma_2$, of ghost number 4).
So "a property of the vertex rather than of the pairing" draws a contrast that does not exist: self-adjointness of $p_{2,2}$ for the pairing and pair-exchange symmetry of $V_4$ are one fact, exactly as for the $\ell_n$.
Verdict: **the objection is correct**: the sentence is true in its literal content and wrong in what it suggests.
Improved version, if anything is kept: "The quadratic form of $\Sigma_2$ is the quartic vertex itself, $\langle \Sigma, p_{2,2}\Sigma'\rangle_2 = V_4(\Sigma, \Sigma')$, symmetric because $V_4$ is; equivalently, $p_{2,2}$ is self-adjoint for the 2-string pairing, as $\ell_n$ is cyclic because $V_{n+1}$ is symmetric. This symmetry is what the completion of the square uses."
Usefulness for the section: low (one clause at most; the completion of the square is in sec:hs).
(S.2) is checked in a finite model (script check `C2.3`).

### 2.4 The grading $d = \tfrac12$ (L53)

Let a per-strand degree be affine in the ghost number, $s(x) = a\,N_{\rm gh}(x) + b$, with the multi-string degree the sum over strands.
A genus-zero operation with $m$ inputs, $n$ outputs and ghost number $G = 3n - 2m$ then has degree
$$\deg p_{m,n} = aG + b(n - m) = (3a + b)\,n - (2a + b)\,m. \tag{D.1}$$
CFL require $\deg\mathfrak p_{m,n,0} = -2d(m-1) - 1$ for all $m, n \ge 1$.
Matching the coefficients of $n$, $m$ and the constant:
$$3a + b = 0, \qquad 2a + b = 2d, \qquad 2d - 1 = 0, \tag{D.2}$$
so $d = \tfrac12$, $a = -1$, $b = 3$: the dictionary $s = 3 - N_{\rm gh}$ is the **unique** affine one, and it forces $d = \tfrac12$.
The alternative $s = N_{\rm gh} - 2$ ($a = 1$, $b = -2$) gives $\deg p_{m,n} = n$, which depends on the number of outputs and has no $d$; so does every other affine choice.
The obstruction is the constant term: in physical ghost number, adding an input to an operation lowers its ghost number by 2 and its degree by $2a + b$, and the differential has degree $-1$, so the bracket–differential gap $2d$ equals the unit cost of one input, which is 1.

Meaning of $d = \tfrac12$: CFL give the genus-counting variable the degree $|\hbar| = 2d$ so that $\hat{\mathfrak p} = \sum\hat{\mathfrak p}_{k,\ell,g}\hbar^{k+g-1}$ is homogeneous of degree $-1$ (review `RPEPEC4L-maurer-cartan.md` (1)).
At $d = \tfrac12$, $\hbar$ has odd degree (ghost number $-1$ in the physical dictionary, as record 103 also found), and an odd formal variable in a graded-commutative ring squares to zero.
This is consistent with CFL's requirement of an integer $d$, which keeps $\hbar$ even so that the expansion in $\hbar$ does not truncate (their motivation is not stated in the reviews; this is our reading).
Verdict on L53: **the question has a definite answer: no better suspension exists among affine ones; $d = \tfrac12$ is forced, and it means an odd genus-counting parameter.**
Recommendation: since the cut plan drops the parity dictionary, one sentence suffices if the section keeps any comparison with CFL's definition: "No grading of the strands affine in the ghost number puts the products into CFL's grading with integer $d$; the unique candidate, $3 - N_{\rm gh}$ per strand, gives $d = \tfrac12$, for which their genus-counting parameter would be odd."
(D.2) is checked symbolically (script check `C3`).

## Part 3 – The reading of CFL Theorem 6.1 (L324, L328)

### 3.1 The theorem and its hypotheses

CFL Thm 6.1 (= Thm 1.3; review `RPEPEC4L.md`, "Homotopy equivalence and canonical model"): every IBL$_\infty$ algebra $(C, \{\mathfrak p_{k,\ell,g}\})$ over a field of characteristic zero is homotopy equivalent to an IBL$_\infty$ structure $\{\mathfrak q_{k,\ell,g}\}$ on $H = H(C, \mathfrak p_{1,1,0})$, with $\mathfrak q_{1,1,0} = 0$, the $\mathfrak q$ built recursively from a splitting $C = H\oplus B\oplus A$ and a contracting homotopy.
Cor. 6.2: the structure can be transferred along any chain homotopy equivalence $C \to D$, with $\mathfrak q_{1,1,0} = \partial^D$.
Hypotheses: the IBL$_\infty$ axioms of Def. 2.3 (operations with $k, \ell \ge 1$; integer $d$; $\hat{\mathfrak p}_{1,1,0}$ extended to $EC$ as a derivation acting on every strand; the relations $\hat{\mathfrak p}\circ\hat{\mathfrak p} = 0$), characteristic zero, and in the filtered version (§8) the filtration/gapping conditions.

### 3.2 The reading, stated precisely

The reading at L324: only $p_{1,1} = Q_B$ contains physical states; any other kinetic term in IBL should define an auxiliary field.
In the language of the section this splits into two claims.

- **(R1)** For an IBL$_\infty$ algebra with $\mathfrak p_{1,1,0} = Q_B$, the space carrying the minimal (canonical) model is determined by $Q_B$ alone: it is $E H(Q_B) = \bigoplus_k \mathrm{Sym}^k H(Q_B)$ (with the CFL grading), and no other operation, whatever its number of inputs and outputs, adds or removes a state; all other operations, including any $(k,k)$ operation that one might read as a "kinetic term" of a $k$-string component, are transferred into the operations $\mathfrak q_{k,\ell,g}$ on that space.
- **(R2)** A $k$-string component of the field whose quadratic term comes from a $(k,k)$ operation rather than from $\mathfrak p_{1,1,0}$ is auxiliary: it can be integrated out, and it contributes no physical state.

### 3.3 Verdicts

**(R1) is correct and is the content of the theorem.**
The underlying space of the canonical model is the homology of $\mathfrak p_{1,1,0}$, and the symmetric algebra on it is, in characteristic zero, the homology of the derivation extension $\hat{\mathfrak p}_{1,1,0}$ on $EC$ (Künneth; script check `C4.1`).
So the canonical model of an IBL$_\infty$ theory lives on the Fock space $\mathrm{Sym}\,H(Q_B)$ built on the one-particle states $H(Q_B)$; this is a sharp form of "only $p_{1,1}$ contains physical states".
Two qualifications: the multi-string sectors of the canonical model are not empty, they are $\mathrm{Sym}^k H(Q_B)$ (read physically as multi-particle states, an interpretation); and the operations with $\ell \ge 2$ outputs survive as $\mathfrak q_{k,\ell,g}$ on $H$.

**(R2) is not what the theorem says, and inside CFL's framework it is false as stated.**
In an IBL$_\infty$ algebra no multi-string component has a $(k,k)$ operation as its only quadratic term: $\hat{\mathfrak p}_{1,1,0}$ acts on every strand (Part 2.1, (iii)), so every multi-string direction carries $\hat Q_B$ at leading order and $\mathrm{Sym}^k H(Q_B)$ survives in the canonical model; these directions are not auxiliary, they carry the multi-particle states.
The $(k,k)$ operations enter weighted by $\hbar^{k-1}$, as perturbations of $\hat{\mathfrak p}_{1,1,0}$, and the theorem transfers them, it does not integrate out a field because of them.

**What is true, and what the reading aims at.**
Combine (K.2) with (R1):

- (a) In the cubic action, with $g_s$ of ghost number zero, ghost number forces the kinetic operator of $\Sigma_n$ to have ghost number $n$, never to be $\hat Q_B$ (K.2); it is $p_{2,2}$ for $\Sigma_2$ at quartic order, dressed by $-\tfrac{g_s}{5}p_{3,2}(\Psi,\cdot)$ beyond, and built from reduced vertices for the higher $\Sigma_n$. (In CFL the $\hat{\mathfrak p}_{1,1}$ and $\mathfrak p_{2,2}$ terms on one component are balanced by $\hbar$, of ghost number $-1$ in the dictionary of 2.4; the contrast holds because the cubic action's coupling is ghost-neutral.) Where the $\Sigma_2$ kinetic operator is injective (on the quotient, PH1), the pair ($\Sigma_2$, its equation of motion) is acyclic.
- (b) Integrating out that pair is a homotopy transfer along a chain homotopy equivalence (the analogue of CFL Cor. 6.2, here for $L_\infty$ algebras), not a passage to homology: R41 (Conditional(PH1), finite-dimensional model, classical complex, quartic order) establishes it for $\Sigma_2$, with transferred brackets $(Q, g\ell_2, g^2\ell_3, 0)$ and the transfer map $\Psi\mapsto(\Psi, \Psi^2)$. R41 controls the solutions and their linearization, not the BRST spectrum.
- (c) The BRST spectrum is R73's statement: around a background, the linearized BRST operator of the cubic theory's master action is similar to $Q^{(k)}_{\Psi_0}$ plus a contractible pair, so $H(\mathcal Q_0) \cong H(Q^{(k)}_{\Psi_0})$ in all ghost numbers to the truncation order ($\Sigma_2$, $k \in \{2,3\}$, $\ker V_4$ quotiented; mixed, string transfer Conditional(PH1, PH5, PH14 [$O(g_s^4)$], PH27) through R62). Under these hypotheses $\Sigma_2$ carries no physical state, and only $Q_B$ does.
- (d) For the tower $\Sigma_n$, $n \ge 3$, the same is **expected** (ghost number $n$ is robust, (K.2)), but the dressed kinetic operators and the tower transfer have not been examined.

So the conclusion that the other kinetic terms define auxiliary fields holds for $\Sigma_2$ in the cubic action, by (K.2), R41 (classical complex, PH1) and R73 (BRST spectrum, its hypotheses), in $L_\infty$ language; for $n \ge 3$ it is expected.
It does not follow from CFL Thm 6.1, and it marks a difference, not a similarity, with IBL$_\infty$: there the multi-string directions carry $\hat Q_B$ and the sectors $\mathrm{Sym}^k H(Q_B)$; in the cubic action $\Sigma_2$ carries $p_{2,2}$ and no state (the higher $\Sigma_n$ expectedly the same), and the multi-particle states are carried by products of $\Psi$.

### 3.4 L328: minimal model, homotopy transfer, strictification

The text (L329) says the minimal model "goes in the opposite direction to a strictification".
The remark: the inverse of strictification is homotopy transfer onto the theory without the auxiliary fields; the minimal model is a further transfer, which integrates everything out and leaves the on-shell states and the S-matrix.
**The remark is correct.** The precise picture, for $L_\infty$ algebras (and in the same form for IBL$_\infty$, by Thm 6.1 and Cor. 6.2):

- strictification: original theory $\to$ larger quasi-isomorphic model with simpler operations (cubic action, bar–cobar of sec:bar-cobar);
- elimination of auxiliary fields: cubic action $\to$ original theory, a homotopy transfer along a contraction whose kernel is acyclic (R41: $\Sigma_2$, quartic order, classical complex, PH1); it inverts the strictification up to homotopy;
- minimal model: original theory $\to$ $H(Q_B)$, a homotopy transfer onto the cohomology, all off-shell modes integrated out with the homotopy $h$ as propagator; the transferred genus-zero brackets are the tree-level on-shell amplitudes (Kajiura 2007 for $A_\infty$; the same construction for the closed-string $L_\infty$ algebra).

All three are quasi-isomorphisms; strictification and elimination of auxiliary fields are inverse to each other; the minimal model is the endpoint of the transfer and is reached from either theory.
The paragraph L333–336 of the text already says that integrating $\Sigma_2$ out is an $L_\infty$ transfer and not an instance of Thm 6.1; that part is correct and should be kept, after the three-item picture above.

## Part 4 – What the transfer theorem says physically

1. **Physical states.** Thm 6.1 is a statement about the particle content: the canonical model lives on the free Fock space $\mathrm{Sym}\,H(Q_B)$ of on-shell one-string states, and every other operation becomes an amplitude. For an IBL$_\infty$ algebra whose operations with $m$ inputs and $n$ outputs come from string vertices, the transferred $\mathfrak q_{m,n,0}$ on $H$ would be the tree-level amplitudes with $m$ incoming and $n$ outgoing on-shell states: the several-output operations are the in/out reading of the S-matrix. This is the physical role of the outputs, and it is the natural link between IBL and the cubic action.

2. **What the $(2,2)$ failure means.** The family raised from the vertices satisfies the relations only with the operations with no input or no output (non-augmented form, R31): its relations are the master equation at $\Psi + \Psi'$, which is crossing symmetric, every vertex read with every split of its legs, including all-in and all-out. CFL Def. 2.3 requires every operation to have at least one input and one output; in their geometric origin (symplectic field theory) the operations with no output are the fillings, which CFL treat as Maurer–Cartan elements, not operations (review obs. 9). The residual (`eq:ibl:residual-22`) is half the exchange channel $T_4$, in which each of the two cubic vertices has one incoming and one outgoing leg: $T_4$ is its own mirror image, so the master equation gives it half the relative weight of $T_1, T_2, T_3$, whose mirrors pass through operations with no input or no output ($p_{0,2}$, $p_{2,0}$, $p_{0,3}$, $p_{3,0}$); Def. 2.3 drops these mirrors and gives the four channels equal weight. So the $(2,2)$ failure says: a crossing-symmetric family of vertices is not an IBL$_\infty$ algebra in CFL's sense when one simply discards the all-in and all-out readings; in CFL's framework the vertices with no output belong in a Maurer–Cartan element (reading of CFL §9; not checked against the paper beyond the cached review).

3. **What the transfer preserves.** Homotopy transfer preserves the homology (states) and the homotopy type of the operations (amplitudes, up to field redefinitions). Under it, the elimination of $\Sigma_2$ preserves the classical theory (solutions and their linearization) up to homotopy (R41, classical complex, PH1) and the BRST cohomology (R73, under PH1, PH5, PH14 [$O(g_s^4)$], PH27); the minimal model preserves only the on-shell data.

4. **A sharper statement, and its cost (proposal, not done).** The natural sharper statement is: *at genus zero, raising commutes with transfer*: the raised family of the minimal-model potential $W$ on $H(Q_B)$ (the generating function of tree amplitudes) equals the transfer of the raised family of $S$, in the non-augmented generating-function form; equivalently, the Taylor expansion of $W$ at $\phi + \phi'$ satisfies the polarized master equation on $H$. This is expected from functoriality (the raised family is the Taylor expansion of the potential, R31, and the potential transfers to $W$), and a finite-model check would take a cyclic dgla (e.g. the $\mathfrak{sl}_2\times\Lambda$ model of record 111), its HPT minimal model, and a comparison of $\mathfrak q_{2,2,0}$ with the 4-point tree amplitude read with two outputs. Cost: about two hours (the transfer recursion with signs on odd inputs is the slow part). Value for the paper: one sentence at most ("on the canonical model the operations with several outputs are the on-shell amplitudes read with several outgoing states"); it does not settle anything the paper already states, so under the 2026-10-10 scope rule it goes to `knowledge/open-problems.md` as "later project" if wanted.

The computation actually run within the time box is the finite-model check of the claims used above: (K.2), (D.2), (S.2), and the contrast between the IBL derivation differential (Künneth, multi-particle states survive) and the cubic-action $\Sigma$ sector (acyclic), in `codes/verify-ibl-remarks.py`.

## Part 5 – Recommendations per remark (for the rewrite)

Verdict key: **H** remark correct; **T** text right; **T/m** text right but misleading; **Cv** convention.

| L | Verdict | Recommendation |
|---|---|---|
| 7 | H | Cite CFL and Münster–Sachs for IBL in SFT; Markl 2001 only for the loop homotopy algebra. |
| 15 + 306 | H | One caveat, placed after the $(2,2)$ counterexample: the products studied are those of the fundamental vertices; from quintic order the cubic action uses reduced vertices, whose several-output readings are not studied. |
| 34 | H | Replace $\Psi_{\rm tot}$ by $\boldsymbol\Psi$ at L73, L249, L287. |
| 49 | T (unclear) | Drop the sentence; (`eq:ibl:ghost-numbers`) says it. |
| 53 | T; the alternative fails | If any comparison with CFL's grading stays: one sentence (Part 2.4). Otherwise drop with the parity dictionary. |
| 76 | T/m | Replace the paragraph by the improved version of Part 2.1 (ghost-number balance; IBL acts with $\hat Q_B$ on every strand). It is the bridge to the transfer comment. |
| 83 | T/m, low value | Keep "$\Sigma_2$ is auxiliary" in one sentence; drop the BV-parity sentences, or one sentence (Part 2.2). |
| 90 | H | Drop, or one clause: "$p_{2,2}$ is self-adjoint for the 2-string pairing because $V_4$ is symmetric, as for the $\ell_n$". |
| 132 | H (Cv) | Say the two families carry the same information, related by the parity operator on the inputs, a sign convention like the choice of suspension; drop "different maps". |
| 178 | H | Add the clause of the AG reading: coefficient rule for the relations of the family, Koszul convention for the $\Loo$ relations of the $\ell_n$ (R87). |
| 181 | H | "The argument is algebraic; for the string field it holds in the same formal sense as the master equation, $\Delta$ being a sum over a basis." |
| 184 | H | The remark is correct: the relations include operations with no input or no output, which CFL Def. 2.3 excludes and CFL §8 admits (R31); say so first, then the $d$ point, then "at $\min(m,n) = 1$ they agree, at $(2,2)$ not". |
| 224 | H | Drop $L$, $K$: "so that $\Omega$ is symmetric on two odd fields". |
| 241 | — | Keep the $\mathfrak{sl}_2\oplus\mathfrak{sl}_2^*$ sentence (it is the proof of "not implied", kept by the cut plan); the dgla sentence can go. |
| 256, 263, 266, 282 | — | Cut by the plan ($\hbar$ operator, brace criterion); nothing to check further. |
| 292 | H | Cut L294–297 (repeats). |
| 320 | — | Subsection. |
| 324 | partly H | Comment as in the proposed paragraph below. |
| 328 | H | Rewrite with the three-step picture of Part 3.4. |
| 338 | T (too dense) | Replace by two sentences: on the classical complex the elimination of $\Sigma_2$ is an $\Loo$ homotopy transfer (sec:all-orders); off it, $\Psi\mapsto(\Psi,\Psi^2)$ is not an $\Loo$ morphism, because the kinetic operator of $\Sigma_2$ has ghost number two and not one. |
| 353 | H | $\hat Q_B$ undefined ("on either strand" should be "on each strand, summed"); with L360, delete the $\Lambda_2$ paragraph. |
| 360 | H | Delete; mention in sec:gauge that $\Lambda_2$ is natural in the IBL formalism. |

**Proposed content for the transfer subsection (agent register; the writer rewrites it).**
Theorem 6.1 of CFL says that an IBL$_\infty$ algebra is homotopy equivalent to one on the homology of $\mathfrak p_{1,1}$: the transferred structure lives on the Fock space $\mathrm{Sym}\,H(Q_B)$ built on the one-particle states $H(Q_B)$, and every other operation becomes an operation on it.
In this sense only $\mathfrak p_{1,1} = Q_B$ carries physical states.
In an IBL$_\infty$ algebra, however, the multi-string components are not auxiliary: the differential acts on each of their strands, and their cohomology is $\mathrm{Sym}^k H(Q_B)$.
In the cubic action, whose coupling $g_s$ carries no ghost number, ghost-number conservation forbids such a term: the kinetic operator of $\Sigma_n$ has ghost number $n$; for $\Sigma_2$ it is $p_{2,2}$ at quartic order (dressed by a background-dependent term beyond), and on the quotient where it is injective the pair formed by $\Sigma_2$ and its equation of motion carries no cohomology.
On the classical complex, integrating $\Sigma_2$ out is a homotopy transfer of $\Loo$ algebras along a contraction of that pair (sec:all-orders), the inverse of the strictification that introduced it; around a background, the BRST cohomology of the cubic theory equals that of the original one.
The minimal model is a further transfer, onto $H(Q_B)$, whose operations are the on-shell amplitudes.
At quartic order the cubic theory and the original one therefore have the same physical states, as Theorem 6.1 would suggest, but by a different mechanism: $\Sigma_2$ is not a multi-string direction of an IBL$_\infty$ algebra.
For the higher auxiliary fields the same is expected, but their dressed kinetic operators and the transfer of the tower have not been examined.

(Sources for the writer, not for the prose: classical-complex transfer R41, Conditional(PH1); BRST cohomology R73, string transfer Conditional(PH1, PH5, PH14 [$O(g_s^4)$], PH27) through R62; minimal model and tree amplitudes, Kajiura 2007.)

## Verification

Script `codes/verify-ibl-remarks.py`, run 2026-11-07 with `uv run --no-project --with sympy python codes/verify-ibl-remarks.py` (the project `.venv` has no sympy), seed 20261107: **11/11 PASS**, peak RSS 55 MB.

Falsifiable checks: `C3` and `C4.1`. Transcription checks (they confirm the transcription of a one-line argument, they do not test it independently): `C2.1`, `C2.3`, `C4.2` (critic 114, #6).

- `C2.1` (K.2) by enumeration of all strand distributions, $n \le 6$ (transcription: $5n - 4n = n$ independently of the distribution); break leg: saturation 6 per strand.
- `C3` (D.2) by `sympy.solve` over $m, n \le 4$, unique solution $(a, b, d) = (-1, 3, \tfrac12)$; the alternative $N_{\rm gh} - 2$ gives $\deg = n$; break leg: CFL constant $-3$ (solution moves to $d = \tfrac32$).
- `C2.3` (S.2) on exact integer data: fully symmetric $V_4$ gives self-adjoint $p_{2,2}$ (transcription: reduces to $V = \pm V^{\mathsf T}$); break leg: $V_4$ symmetric within pairs only; control `C2.3-pairing`: an antisymmetric 2-string pairing turns self-adjointness into anti-self-adjointness for a fully symmetric $V_4$.
- `C4.1` Künneth on a random graded complex with $H = \{2{:}1, 3{:}1\}$: $H(\hat Q|_{\mathrm{Sym}^2}) = \{4{:}1, 5{:}1\} = \mathrm{Sym}^2 H$; break leg: Koszul sign dropped ($\hat Q^2 \ne 0$).
- `C4.2` classical complex with the $\Sigma$ pair: total cohomology $(1,1)$ equals the $\Psi$ sector (transcription: acyclicity of a two-term complex with an invertible map; no node cites it since fix pass 1); break leg: $V_4$ degenerate on $\mathrm{Sym}^2 C_2$ gives $(2,2)$.
- Each `-break` perturbation was also run with `--perturb`, and the plain check then reports FAIL (5/5).

Not machine-checked: the CFL statements (taken from the reviews, A2), the BV$_\infty$ reading of Markl–Voronov (paper not cached), C5.2.

## Fix pass 1 (2026-11-07, `agent/reports/critic-114-20261107T1225.md`)

Choice for major 1: both. The classical-complex statement stays on R41 (restricted to the classical complex, $\Sigma_2$, quartic order, PH1); the physical-states (BRST spectrum) statement is now sourced on R73 with its hypotheses PH1, PH5, PH14 [$O(g_s^4)$], PH27 through R62.

Changed nodes:

- **C4.3**: statement changed (restricted to the classical complex and quartic order; "both theories have linear homology $H(Q_B)$" removed); coverage tag `C4.2` removed.
- **C4.5**: new node (BRST spectrum, by R73).
- **C4**: statement changed (hypotheses of C4.5 added; "for $\Sigma_2$"; cites C4.1–C4.5).
- **C4.1**: statement changed (Fock space on the one-particle states $H(Q_B)$; "multi-particle" as interpretation, #8).
- **C4.4**: justification changed (Kajiura 2007 cited, #7) and statement qualified (classical complex, PH1 for $\Sigma_2$).
- "Hypotheses in force" updated.

Dependents: C4 (repaired in this pass); the ledger R? entry (rewritten: clause (c), hypotheses line, tag `mixed`, verification line); Part 3.3 (a)–(d), 3.4, Part 4 item 3, Part 5 proposed paragraph (all rewritten); the report Summary. C2.1–C2.3, C3, C5 do not depend on the changed nodes and still hold.

Other items: major 2, the Part 5 paragraph and 3.3 restricted to $\Sigma_2$, with the general-$n$ statement marked as expected; #3, a clause on the ghost-neutral $g_s$ (2.1, 3.3 (a), Part 5); #4, the class of record 103 stated, Markl–Voronov marked [unverified reference]; #5, "which is why" softened in 2.4 and the R31 annotation; #6, Verification split into falsifiable checks (`C3`, `C4.1`) and transcription checks (`C2.1`, `C2.3`, `C4.2`), the ledger verification line now lists `C4.1` only; #9, no change.
The script was not changed.

## Proposed ledger entries

Ledger section: ## Results

### R111 — Kinetic operators of the multi-string fields have ghost number $n$; CFL Thm 6.1 puts the canonical model on $\mathrm{Sym}\,H(Q_B)$ with non-auxiliary multi-string directions; $\Sigma_2$ is auxiliary by an $L_\infty$ transfer (R41) and R73, not by Thm 6.1 [Conditional(PH1, PH5, PH14, PH27) – mixed]

- **Source**: `agent/derivations/114-ibl-remarks-check.md`, nodes C2.1, C4.1–C4.5
- **Scope**: genus zero, ghost-neutral $g_s$; CFL Thm 6.1 as stated in `literature/reviews/RPEPEC4L.md` (PDF not cached); the IBL$_\infty$ side assumes CFL's axioms (integer $d$), which the raised family does not satisfy (R31), so (b) describes IBL$_\infty$ algebras, not the cubic action; (c) is $\Sigma_2$ only (quartic order for the classical complex, $k \in \{2,3\}$ for the BRST spectrum); the higher $\Sigma_n$ are expected to behave alike, not examined
- **Hypotheses**: (a), (b) none; (c) classical complex: PH1 through R41 (finite-dimensional model); BRST spectrum: PH1, PH5, PH14 [$O(g_s^4)$], PH27 through R73 and R62
- **Verification**:
  - 2026-11-07 – exact check – `codes/verify-ibl-remarks.py`, check C4.1 (Künneth for the derivation extension on $\mathrm{Sym}^2$, against $\mathrm{Sym}^2 H$ computed separately) with break leg (Koszul sign dropped), PASS, seed 20261107
(a) An $n$-string field of total ghost number $2n$, with a ghost-neutral coupling, has a kinetic operator of ghost number $n = N_{\rm gh}(p_{n,n})$, from $2N + N_{\rm gh}(K) = 5n$; an operator of ghost number one acting strand by strand (the extension $\hat Q_B$) is possible only at $n = 1$.
(b) By CFL Thm 6.1 (characteristic zero) and Künneth, the canonical model of an IBL$_\infty$ algebra with $\mathfrak p_{1,1,0} = Q_B$ lives on the Fock space $\mathrm{Sym}\,H(Q_B)$: only $\mathfrak p_{1,1}$ determines the one-particle states, but the multi-string directions carry $\hat Q_B$ and the sectors $\mathrm{Sym}^k H(Q_B)$, so they are not auxiliary.
(c) For $\Sigma_2$: under PH1, on the classical complex at quartic order, the pair ($\Sigma_2$, its equation of motion) is acyclic and its elimination is the $L_\infty$ homotopy transfer of R41, the inverse of the strictification; under PH1, PH5, PH14 [$O(g_s^4)$], PH27, the BRST cohomology of the cubic theory around a background equals that of the original theory (R73), so $\Sigma_2$ carries no physical state.
The reading of Thm 6.1 (2026-11-07) holds in the form (b) for "only $Q_B$ carries physical states", and in the form (a)+(c) for "the other kinetic terms define auxiliary fields" for $\Sigma_2$, the latter not as a consequence of Thm 6.1.

Ledger section: ## Results

Annotation proposed for `### R31 — Theorem A′: non-augmented raised family satisfies genus-zero IBL relations iff cyclic $L_\infty$ [Proven]`:

The value $d = \tfrac12$ is forced: among per-strand degrees affine in the ghost number, $3 - N_{\rm gh}$ is the only one reproducing CFL's genus-zero degrees $-2d(m-1)-1$, and it gives $d = \tfrac12$; $N_{\rm gh} - 2$ and every other affine choice give a degree depending on the number of outputs. At $d = \tfrac12$ CFL's genus-counting variable, of degree $2d$, is odd, consistent with their requirement of an integer $d$. Record 114 (2.4), node C3; `codes/verify-ibl-remarks.py` check C3 with break leg, 2026-11-07.
