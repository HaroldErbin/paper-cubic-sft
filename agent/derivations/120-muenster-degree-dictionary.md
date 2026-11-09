---
description: Degree/suspension dictionary paper ↔ CFL ↔ Münster–Sachs 2013/2014 for the (m,n) products; CFL's affine fit needs d = 1/2 (verified), Münster–Sachs use d = 0 via the double suspension, so the claim that d = 1/2 also holds for them does not hold; both paper sentences stand, one optional addition
---

# 120 – Suspension and degree conventions of Münster–Sachs against the paper's IBL grading

Brief: `agent/briefs/active-computator-muenster-degree-20261109T100800.md`.
Companion script: `agent/computations/verify-muenster-degree.py`.

## Status

Last completed step: all sections written (dictionary, answers (a)–(c), answer for the paper, checks 9/9 PASS + break, proposed ledger entry); record complete.
Next step: none (report written; critic review if the orchestrator wants one).

## Task and objective

**Literal task.** For an operation with $m$ inputs and $n$ outputs, extract the degree in the conventions of (i) the paper (ghost number $3n - 2m$, physical ghost numbers, no suspension), (ii) Cieliebak–Fukaya–Latschev (CFL, Def. 2.3), (iii) Münster–Sachs 2013 (quantum open-closed homotopy algebra), (iv) Münster–Sachs 2014 (homotopy classification); write the dictionary; answer (a) which degree the $p_{m,n}$ carry for Münster–Sachs and whether they use a CFL integer $d$, a suspension or another bookkeeping; (b) whether the paper's sentences at `07-ibl.tex:52` and `:171` are consistent with Münster–Sachs, and the question whether $d = \tfrac12$ carries over to Münster–Sachs; (c) whether the sign convention of the raised products $p^{\Omega}_{m,n}$ matches the Münster–Sachs suspension, and the dictionary.

**Motivating objective.** One `\agcomment` answer at `07-ibl.tex:166` and, if a sentence is wrong or incomplete, its replacement; final round, no new content.

## Source passages

Paper (`paper/sections/`):

- `07-ibl.tex:47–53`: $\Ngh(p_{m,n}) = 3n - 2m$, the sentence under test (line 52): "the only strand degree affine in the ghost number that reproduces their degrees is $3 - \Ngh$, and it requires $d = \tfrac12$, a value their definition excludes".
- `07-ibl.tex:107–118`: $p^{\Omega}_{m,n}$ defined through $\Omega_n(X, Y) = (-1)^{|X|}\langle X, Y\rangle_n$; $p^{\Omega}_{m,n} = (-1)^{\sum |B_i|} p_{m,n}$.
- `07-ibl.tex:165–166`: the existing comment and the earlier agent answer (point (ii)).
- `07-ibl.tex:171`: "Their degree bookkeeping, with an integer $d$, corresponds here to $d = \tfrac12$, with one suspension sign per slot when the slots of an operation are permuted."
- `07-ibl.tex:234–235`: genus-counting parameter of degree $2d$, odd at $d = \tfrac12$.
- `A-conventions.tex:102–145`: multi-string pairing with Koszul sign, saturation at $5n$, symmetric; odd symplectic form $\Omega(A, B) = (-1)^{|A|}\langle A, B\rangle$; products $p_{m,n}$, output strands at ghost number three.

CFL (arXiv:1508.02741):

- lines 128–132: $C[1]^d := C^{d+1}$, $|c| = \deg c - 1$; $E_k C$ symmetric power of $C[1]$.
- lines 167–180: $\mathfrak p_{k,\ell,g} \colon E_k C \to E_\ell C$, $k, \ell \ge 1$, of degree $|\mathfrak p_{k,\ell,g}| = -2d(k + g - 1) - 1$ "for some fixed integer $d$"; $|\hbar| = 2d$, $|\tau| = 0$; $\hat{\mathfrak p} = \sum \hat{\mathfrak p}_{k,\ell,g}\hbar^{k+g-1}\tau^{k+\ell+2g-2}$.
- line 184: Def. 2.3, $\hat{\mathfrak p}\circ\hat{\mathfrak p} = 0$.
- line 82 and 2058: for a cyclic complex with pairing of degree $-n$, the dIBL on $(B^{cyc*}A)[2-n]$ has $d = n - 3$ (Prop. 10.4); line 1063: in SFT (symplectic field theory) $d = n - 3$ for a contact manifold of dimension $2n - 1$.
- line 1061: Weyl algebra, $|p_\gamma| + |q_\gamma| = |\hbar| = 2d$.
- line 1402 (section 8): filtered version, "in contrast to the unfiltered case, we allow $k = 0$ and $\ell = 0$".

Münster–Sachs 2013 (arXiv:1109.4101):

- lines 176–186: $A_\infty$ coderivation $M$ of degree 1; shift $sA$, $(sA)_i = A_{i-1}$, $\tilde m_n = s \circ m_n \circ (s^{-1})^{\otimes n}$.
- lines 252, 280–284: $L_\infty$: $L \in \mathrm{Coder}(SA)$ of degree 1; cyclicity w.r.t. an odd symplectic $\omega$ of degree $-1$, $\omega(d_n(c_1, \ldots, c_n), c_{n+1})$ graded symmetric.
- lines 361–400 (sec. IV.B): $\mathfrak{coder}(SA, x) = \bigoplus x^{n-1}\mathrm{Coder}^n(SA)$, $\mathfrak D = \sum x^{n+g-1} D^{n,g}$ ($n$ = number of outputs); IBL$_\infty$: $\mathfrak L^2 = 0$, $|\mathfrak L| = 1$; no degree assigned to $x$.
- lines 402–404: to recover a classical IBL algebra "we have to shift the degree by one", $d = s\circ\tilde d\circ s^{-1}$ etc.
- lines 483–503 (sec. V.A): $|e^i| = 1 - i$, $\omega_c^{-1} = \tfrac12 e_i \wedge e^i$, $|\omega_c^{-1}| = 1$; $\mathfrak L_c = \sum_g \hbar^g L^g + \hbar D(\omega_c^{-1})$ "of degree 1".
- lines 892–900 (App. A.2): $S_{kin} = \tfrac12(\Psi, c_0^- Q\Psi)_{bpz}$, classical closed string field of ghost number 2, "we shift the degree by two", $A_c := s^{-2}\tilde A_c$; $\omega_c := (\cdot, c_0^-\cdot)_{bpz}\circ(s^2 \otimes s^2)$, graded antisymmetric, degree $-1$.

Münster–Sachs 2014 (arXiv:1208.5626):

- line 66: "We use the conventions where the string fields have degree zero, both in the closed string and the open string sector".
- lines 176–191: $\mathfrak L_c = \sum_g \hbar^g L^g + \hbar\,\Omega_c^{-1}$, $\Omega_c^{-1} = \widehat{\omega_c^{-1}} \in \mathrm{Coder}^2(SA_c)$, loop homotopy algebra.
- line 268: $\omega$ of degree $-1$, differential $d$ of degree $+1$.
- line 654 (footnote 2): "The ghost number is related to the grading used here by a double shift, i.e. the ground state $|0\rangle_c$ has degree minus two and ghost number zero".
- lines 988–1020 (App. A.2): $\mathfrak{coder}(SA, \hbar) = \bigoplus \hbar^{n-1}\mathrm{Coder}^n(SA)$, $\mathfrak d = \sum \hbar^{n+g-1} d^{n,g}$ expanded "in the number of outputs"; IBL$_\infty$ algebra: $\mathfrak L$ "of degree one that squares to zero".

## Claim tree

- **A1** Paper conventions (brief): physical ghost numbers, $\Ngh(\Psi) = 2$, $\Ngh(\Sigma_k) = 2k$, one-strand pairing saturating at ghost number five and graded symmetric (conventions ledger C1), $n$-strand pairing at $5n$; vertices $\mathcal V_k$ nonzero on total ghost number $2k$; parity of a state is $\Ngh \bmod 2$. CFL's degree formula is taken from the ledger entry R5 (Verified).
- **A2** "Degree" of a map means output degree minus input degree, additive under composition; a strand grading is a function $\delta(\Ngh)$ of the ghost number of the strand, and the degree of an $(m, n)$ operation read from a vertex is $\sum_{\text{out}}\delta - \sum_{\text{in}}\delta$.
- **C1** In the paper's grading, $\deg p_{m,n} = 3n - 2m$; the general affine strand grading $\delta = \alpha\Ngh + \beta$ gives $\deg_\delta p_{m,n} = n(3\alpha + \beta) - m(2\alpha + \beta)$. [by A1, A2; eq. (A.1)] [check: C1]
- **C2** CFL's degree $|\mathfrak p_{k,\ell,g}| = -2d(k + g - 1) - 1$ is reproduced at $g = 0$ by an affine strand grading iff $\beta = -3\alpha$, $\alpha = -2d$ and $2d = 1$: the unique solution is $\delta = 3 - \Ngh$ (as $C[1]$-degree), $d = \tfrac12$, operation degree $-m$. Allowing the overall sign of the grading to flip gives $\delta = \Ngh - 3$ with the same $d$. [by C1, R5; eq. (A.2)] [check: C2, C2-break]
- **C3** Münster–Sachs grade $A_c = s^{-2}\tilde A_c$: strand degree $\Ngh - 2$, string field of degree 0, $\omega_c$ of degree $-1$; every structure map ($l_n^g$ and $\omega_c^{-1}$) has degree $+1$ and $\hbar$ carries no degree. [cited: MS2013 App. A.2 lines 892–900, sec. V.A lines 483–503; MS2014 line 66, 654, 1019]
- **C4** In CFL's bookkeeping, Münster–Sachs's loop homotopy algebra is an IBL$_\infty$ algebra of degree $d = 0$, with the cohomological sign of the grading (every $\mathfrak p$ of degree $\mp 1$, $|\hbar| = 0$); its $(0, 2)$ operation $\omega_c^{-1}$ and the $g \ge 1$ tadpoles $l_0^g$ place it in CFL's section-8 extension, not in Def. 2.3. [by C3; cited: CFL lines 167–180, 1402] [check: C4]
- **C5** The paper's $(m, n)$ products carry degree $n$ in the Münster–Sachs grading ($\alpha = 1$, $\beta = -2$ in C1): they are not of uniform degree, hence not the structure maps of an IBL$_\infty$ algebra in their sense; they are the composites $l_{m+n-1}$ with $n - 1$ copies of $\omega_c^{-1}$, whose degree $1 + (n - 1)$ agrees. [by C1, C3; eq. (A.3)] [check: C5]
- **C6** No affine strand grading makes $\deg p_{m,n}$ independent of both $m$ and $n$ (it would force $\alpha = 0$ and an even degree); so the value of $d$ is not intrinsic to closed SFT but to the choice of structure maps: $d = 0$ for the Münster–Sachs family, $d = \tfrac12$ for the paper's vertex-raised family against CFL's form. [by C1, C2, C5] [check: C6]
- **C7** Sign dictionary: $\omega_c = \pm\Omega$, where $\Omega(A, B) = (-1)^{|A|}\langle A, B\rangle$ is the paper's odd symplectic form (the only odd graded-antisymmetric forms proportional to the symmetric pairing by a parity sign); the Münster–Sachs raising by $\omega_c^{-1}$ is the paper's raising by $\Omega^{-1}$, i.e. the family $p^{\Omega}_{m,n}$, not $p_{m,n}$; the double suspension $s^{-2}$ is even and brings no Koszul sign; the overall sign $\pm$ is not fixed by the Münster–Sachs text. [by A1 (conventions C1), C3; eq. (A.4)] [check: C7-sign, C7-tensor]
- **C8** The paper's sentences at `07-ibl.tex:52` and `:171` are correct as statements about CFL; the inference that $d = \tfrac12$ holds for Münster–Sachs too does not hold, and a one-sentence addition stating $d = 0$ for their family is optional. [by C2, C4, C5, C6, C7]

Open gaps: none
Hypotheses in force: none

## Dictionary

Notation: $N$ is the physical ghost number of a strand; an $(m, n)$ operation has $m$ input strands at $N = 2$ and $n$ output strands at $N = 3$ (A1); "degree" is output minus input (A2). The ledger entry R5 (CFL's formula, quoted and evaluated) is reused for the CFL column.

| | Paper | CFL (Def. 2.3) | Münster–Sachs 2013 | Münster–Sachs 2014 |
|---|---|---|---|---|
| Space | $\mathcal H$, physical ghost number, no suspension | $C[1]$, $\lvert c\rvert = \deg c - 1$ | $A_c = s^{-2}\tilde A_c$ | same ($\lvert c\rvert = N - 2$, footnote 2) |
| Strand degree | $N$ | fit: $3 - N$ (C2) | $N - 2$ | $N - 2$ |
| String field | $N = 2$, even | degree $1$, odd (in the fit) | degree $0$, even | degree $0$, even |
| Pairing / symplectic form | $\langle\cdot,\cdot\rangle$ symmetric, $\Omega = (-1)^{\lvert A\rvert}\langle\cdot,\cdot\rangle$ odd antisymmetric | not part of Def. 2.3 (cyclic examples: pairing of degree $-n$, $d = n - 3$) | $\omega_c = (\cdot, c_0^-\cdot)_{bpz}\circ(s^2\otimes s^2)$, degree $-1$, antisymmetric | $\omega$ of degree $-1$ |
| Structure maps | $p^{\Omega}_{m,n}$ (and $p_{m,n}$), all $(m, n)$ incl. $(m, 0)$, $(0, n)$ | $\mathfrak p_{k,\ell,g}$, $k, \ell \ge 1$ (sec. 8: $k, \ell \ge 0$) | $l_n^g \colon A_c^{\wedge n} \to A_c$ and $\omega_c^{-1} \in A_c^{\wedge 2}$ | same |
| Degree of an $(m, n)$ operation | $3n - 2m$ | $-2d(m + g - 1) - 1$ | $+1$ for every structure map; a vertex read with $n$ outputs: $n$ (C5) | same |
| Genus / output counting variable | $g_s$ (one power per cubic term) | $\hbar^{k+g-1}\tau^{k+\ell+2g-2}$, $\lvert\hbar\rvert = 2d$ | $x^{\ell+g-1}$ ($\ell$ outputs), no degree | $\hbar^{\ell+g-1}$, no degree |
| Sign of the grading | cohomological ($Q_B$: $+1$) | homological ($\mathfrak p_{1,1,0}$: $-1$) | cohomological ($\lvert\mathfrak L\rvert = +1$) | cohomological |
| Value of $d$ (CFL sense) | $\tfrac12$ against CFL's form (C2) | integer by definition | $0$ (C4) | $0$ |
| Permutation sign of slots | parity $N$ | parity $N + 1$ (one suspension per slot relative to the paper) | parity $N$ (even shift) | parity $N$ |
| Raising | $\Delta = \langle\cdot,\cdot\rangle^{-1}$ for $p_{m,n}$; $\Omega^{-1}$ for $p^{\Omega}_{m,n}$ | – | $\omega_c^{-1} = \tfrac12 e_i \wedge e^i$ ($= \pm\Omega^{-1}$, C7) | same |

Known operations on both sides (second method): $Q_B$ has ghost number $1$ (paper), degree $-1$ in CFL ($\mathfrak p_{1,1,0}$, any $d$; fit: $(3-3) - (3-2) = -1$), degree $+1$ in Münster–Sachs ($(3-2) - (2-2) = 1$). $\ell_2$: ghost number $-1$; CFL at $d = \tfrac12$: $-2\cdot\tfrac12\cdot 1 - 1 = -2$, fit: $0 - 2 = -2$; Münster–Sachs: $(3 - 2) - 2\cdot 0 = 1$. $p_{2,2}$: ghost number $2$; CFL at $d = \tfrac12$: $-2$, fit $0 - 2 = -2$; Münster–Sachs: $2\cdot 1 - 0 = 2$, equal to $\lvert l_3\rvert + \lvert\omega_c^{-1}\rvert = 1 + 1$. Cobracket $p_{1,2}$: ghost number $4$; CFL: $-1$ for every $d$ ($k = 1$), fit $0 - 1 = -1$; Münster–Sachs: $2 = \lvert l_2\rvert + \lvert\omega_c^{-1}\rvert$.

### Derivation block: affine strand gradings

\subsection*{Setup}
A1, A2. Strand grading $\delta(N) = \alpha N + \beta$; an $(m, n)$ operation read from the vertex $\mathcal V_{m+n}$ has $m$ inputs at $N = 2$ and $n$ outputs at $N = 3$.

\subsection*{Derivation}
$$\deg_\delta p_{m,n} = n\,\delta(3) - m\,\delta(2) = n(3\alpha + \beta) - m(2\alpha + \beta). \tag{A.1}$$
Matching CFL at genus zero, $|\mathfrak p_{m,\ell,0}| = -2d(m - 1) - 1$ for all $m, \ell \ge 1$:
$$3\alpha + \beta = 0, \qquad -(2\alpha + \beta) = -2d, \qquad 0 = 2d - 1 \quad\Longrightarrow\quad (\alpha, \beta, d) = (-1, 3, \tfrac12). \tag{A.2}$$
Münster–Sachs grading $(\alpha, \beta) = (1, -2)$:
$$\deg_{MS} l_m = 1 \cdot 1 - m \cdot 0 = 1, \qquad \deg_{MS}\omega_c^{-1} = (N_1 - 2) + (N_2 - 2) = 5 - 4 = 1, \qquad \deg_{MS} p_{m,n} = n. \tag{A.3}$$
Odd antisymmetric forms proportional to the symmetric pairing by a parity sign, on the support $|A| + |B| = 1$: $\epsilon(|B|, |A|) = -(-1)^{|A||B|}\epsilon(|A|, |B|) = -\epsilon(|A|, |B|)$, hence
$$\epsilon(|A|, |B|) = \pm(-1)^{|A|}, \qquad \omega_c = \pm\Omega. \tag{A.4}$$

\subsection*{Commentary}
(A.2): the three equations are the coefficients of $n$, of $m$ and the constant term in $\deg_\delta p_{m,n} - |\mathfrak p_{m,\ell,0}|$; they are linear and have exactly one solution, so the uniqueness claim of `07-ibl.tex:52` holds; the overall sign of the grading (homological CFL versus cohomological paper) is fixed by $Q_B$: CFL's $\mathfrak p_{1,1,0}$ has degree $-1$, so $\alpha < 0$. Flipping the sign convention gives $\delta = N - 3$ and the same $d$. Restricting $d$ to an integer leaves the system without solution (check `C2-break`).
(A.3): Münster–Sachs's $(0, 2)$ element $\omega_c^{-1} = \tfrac12 e_i \wedge e^i$ has $|e_i| + |e^i| = 1$ (MS2013 sec. V.A: $|e^i| = 1 - i$); its two strands have ghost numbers summing to $5$ (the pairing saturates at five), so the shifted total is $1$. The degree of $p_{m,n}$ in their grading is $n$ because every raising inserts one $\omega_c^{-1}$.
(A.4): the exchange symmetry of the pairing is convention C1 of `knowledge/conventions.md` ($s = +1$); its *BV odd symplectic form* bullet already records that the $(-1)^{\epsilon(B)}$ twist gives $-\Omega_1$. Münster–Sachs's text fixes neither the overall sign nor the bpz sign rule for $c_0^-$ that makes their $(\cdot, c_0^-\cdot)_{bpz}$ antisymmetric where C1's $\langle A\vert c_0^-\vert B\rangle$ is symmetric; the two forms agree up to that overall sign, which is invisible in $\mathfrak L^2 = 0$ ($\hbar\omega_c^{-1} \to -\hbar\omega_c^{-1}$ is $\hbar \to -\hbar$).

\subsection*{Result}
$$\boxed{\;\deg_\delta p_{m,n} = n(3\alpha + \beta) - m(2\alpha + \beta);\quad \text{CFL fit: } \delta = 3 - N,\ d = \tfrac12;\quad \text{Münster–Sachs: } \delta = N - 2,\ \deg l_n = \deg\omega_c^{-1} = 1,\ d = 0,\ \deg p_{m,n} = n.\;}$$

\subsection*{Verification}
`agent/computations/verify-muenster-degree.py`: C1, C2 (exact linear solve, unique solution), C2-numeric (five random $(m, n)$), C2-break (integer $d \in [-5, 5]$: no solution, the check FAILS as required), C4, C4-cfl, C5, C6, C7-sign, C7-tensor; 9/9 PASS, seed 20261109, 0.2 s, 54 MB.

## Answers

### (a) Degree of the $p_{m,n}$ for Münster–Sachs; integer $d$, suspension, or other bookkeeping

Münster–Sachs do not use CFL's integer $d$ and do not assign a degree to $\hbar$ (or $x$). Their bookkeeping is a suspension: $A_c = s^{-2}\tilde A_c$, the string field has degree $0$, $\omega_c$ has degree $-1$, and an IBL$_\infty$ algebra is an element $\mathfrak L \in \mathfrak{coder}(SA_c, \hbar)$ of degree $+1$ squaring to zero (MS2013 sec. IV.B, MS2014 App. A.2). Every structure map, $l_n^g$ for every $n$ and $g$ and the $(0, 2)$ element $\omega_c^{-1}$, has degree $+1$ (A.3). In CFL's language this is the degree-$d$ formula with $d = 0$ and the cohomological sign ($|\mathfrak p_{k,\ell,g}| = -1$ for every signature, $|\hbar| = 0$); the operations with no input ($\omega_c^{-1}$, the tadpoles $l_0^{g \ge 1}$) put the loop homotopy algebra in CFL's filtered extension (sec. 8, $k, \ell \ge 0$), not in Def. 2.3 (C4). The further shift by one that MS2013 perform around line 402 serves only to recover the classical IBL axioms (bracket of degree $0$) and is not used for the loop algebra.

The paper's products $p_{m,n}$, i.e. a vertex read with $n$ outputs, are not structure maps of the loop homotopy algebra: Münster–Sachs never read a closed-string vertex with several outputs. In their grading $p_{m,n}$ has degree $n$ (A.3), not $1$; this is consistent, because $p_{m,n}$ is the composite of $l_{m+n-1}$ with $n - 1$ copies of $\omega_c^{-1}$ and such composites appear in $\mathfrak L^2$ (the term $l_{n+2}^{g-1}\circ(\omega_c^{-1}\wedge 1^{\wedge n})$ of their main identity (28) is one of them, with both legs of $\omega_c^{-1}$ contracted) (C5).

### (b) The two paper sentences and the question on Münster–Sachs

Line 52 ("the only strand degree affine in the ghost number that reproduces their degrees is $3 - N_{gh}$, and it requires $d = \tfrac12$, a value their definition excludes"): **verified**, (A.2) and checks C2, C2-numeric, C2-break. The uniqueness is up to the overall sign convention of the grading, which $Q_B$ fixes to CFL's homological one; the strand degree $3 - N$ is a $C[1]$-degree ($\deg c = 4 - N$ on $C$), which the sentence need not say.

Line 171 ("Their degree bookkeeping, with an integer $d$, corresponds here to $d = \tfrac12$, with one suspension sign per slot when the slots of an operation are permuted"): **stands**. The regrading $N \to 3 - N$ flips the parity of every strand, so CFL's $E_k C$ symmetrises with parity $N + 1$ where the paper uses $N$: the relative sign for a transposition is $(-1)^{|A| + |B| + 1}$, the usual suspension sign. The sentence is about CFL only and is correct as such.

The question whether $d = \tfrac12$ also holds for Münster–Sachs: **no**. The value of $d$ is a property of the family of structure maps and of the strand grading, not of closed string field theory (C6): no affine strand grading makes $\deg p_{m,n}$ independent of both $m$ and $n$, so a family that contains the vertices read with several outputs cannot have uniform degree, and matching CFL's form (independent of the outputs, linear in the inputs) forces $d = \tfrac12$; Münster–Sachs's family has one-output maps and $\omega_c^{-1}$ only, and the grading $N - 2$ makes all of them of degree $1$, i.e. $d = 0$. Both statements hold at once. Consequently the earlier agent answer at line 165, point (ii), is now settled: the same value does not arise for Münster–Sachs; theirs is $d = 0$. The first sentence of the earlier answer, point (i), is unaffected: CFL's $\hbar$ of degree $2d$ is odd at $d = \tfrac12$, and even ($= 0$) for Münster–Sachs.

### (c) Sign convention of $p^{\Omega}_{m,n}$ against the Münster–Sachs suspension

The Münster–Sachs suspension is $s^{-2}$, an even shift: it changes degrees by $-2$ and brings no Koszul sign, so their parity is the paper's physical parity $N \bmod 2$ and their graded symmetry of $l_n$ and of $\omega_c(l_n(c_1, \ldots, c_n), c_{n+1})$ is the paper's graded symmetry in $N$. Their raising uses $\omega_c^{-1} = \tfrac12 e_i \wedge e^i$, the inverse of the odd symplectic form, and $\omega_c = \pm\Omega$ with the paper's $\Omega(A, B) = (-1)^{|A|}\langle A, B\rangle$ (A.4, convention C1 of `knowledge/conventions.md`). Hence the family that matches their raising, slot by slot, is $p^{\Omega}_{m,n}$ (raised with $\Omega^{-1}$ and the Koszul tensor power $\Omega_n$, check C7-tensor), not $p_{m,n}$ (raised with $\Delta = \langle\cdot,\cdot\rangle^{-1}$); the two differ by $(-1)^{\sum|B_i|}$, eq. `eq:ibl:raised-vs-sprod`, invisible on $\Psi$ and $\Sigma_k$. The dictionary for the one-output maps: with the vertex written $\mathcal V_{n+1}(A, B_1, \ldots, B_n) = \Omega(A, p^{\Omega}_{n,1}(B))$ (output in the second slot) and Münster–Sachs's $\omega_c(l_n(B), A)$ (output in the first slot), antisymmetry of the odd form gives $\omega_c(l_n(B), A) = -\Omega(A, l_n(B))$ when $\omega_c = \Omega$, so $l_n^{MS} = \sigma\, p^{\Omega}_{n,1} = \sigma\,(-1)^{\sum|B_i|}\ell_n$ with an overall sign $\sigma = \pm 1$ fixed by the sign of $\omega_c$ and by the normalisation of the action, which their text does not pin down and which $\mathfrak L^2 = 0$ does not see. Beyond this overall sign, the paper's $p^{\Omega}$ convention is the Münster–Sachs convention; the paper's phrase "like the choice of a suspension for an $A_\infty$ algebra" (line 118) is apt in that the Münster–Sachs odd shift $s$ appears only in their open-string sector ($A_o = s^{-1}\tilde A_o$) and in the recovery of the classical IBL axioms, not in the closed-string loop algebra.

### Answer for the paper

Proposed `\agcomment` after the existing comment at `07-ibl.tex:166` (register of the existing answers; no file edit made):

```latex
\agcomment{Checked against~\cite{Muenster:2013:QuantumOpenClosedHomotopy,Muenster:2014:HomotopyClassificationBosonic}. They use no integer $d$ and give $\hbar$ no degree: the closed string space is shifted by two, $A_c = s^{-2} \tilde A_c$, so that the string field has degree zero and $\omega_c$ degree $-1$, and the loop homotopy algebra is an element of degree one squaring to zero. Every structure map, the $l_n^g$ and the inverse symplectic form $\omega_c^{-1}$, then has degree one, which in the bookkeeping of~\cite{Cieliebak:2015:HomologicalAlgebraRelated} is $d = 0$ with the cohomological sign of the grading. The value $d = \tfrac{1}{2}$ is not a property of closed string field theory but of our family: they never read a vertex with several outputs, whereas our $p_{m, n}$ in their grading has degree $n$, the degree of $l_{m+n-1}$ composed with $n - 1$ copies of $\omega_c^{-1}$; no strand degree affine in the ghost number makes the degree of $p_{m, n}$ independent of both $m$ and $n$, and reproducing their input-dependent, output-independent form forces $d = \tfrac{1}{2}$. The even shift $s^{-2}$ carries no Koszul sign, their $\omega_c$ is our $\Omega$ up to an overall sign their text does not fix, and their raising by $\omega_c^{-1}$ is our $p^{\Omega}_{m, n}$ family. The sentences at the head of this section and after the theorem stand; the sentence below adds their value.}
```

Optional one-sentence addition after line 171 (same register, no theorem language), only if the author wants the comparison in the text:

```latex
In the conventions of~\cite{Muenster:2013:QuantumOpenClosedHomotopy,Muenster:2014:HomotopyClassificationBosonic}, where the string field has degree zero and the only operation with several outputs is the inverse symplectic form, every operation has degree one and $d = 0$; the value $d = \tfrac{1}{2}$ reflects our reading of the vertices with several outputs, not a property of closed string field theory.
```

If the addition is not wanted, replace the last sentence of the `\agcomment` by "The sentences at the head of this section and after the theorem stand as statements about~\cite{Cieliebak:2015:HomologicalAlgebraRelated}."

## Checks

Script `agent/computations/verify-muenster-degree.py`, run from the project root with `OMP_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2 MKL_NUM_THREADS=2 nice -n 19 uv run --no-sync python agent/computations/verify-muenster-degree.py` (seed 20261109, 0.2 s wall, 54 MB peak RSS, one process):

| Check | Node | What it tests | Independent path | Result |
|---|---|---|---|---|
| C1 | C1 | $\deg_\delta p_{m,n}$ at $(\alpha, \beta) = (1, 0)$ equals $3n - 2m$ | symbolic, against the paper's eq. `eq:ibl:ghost-numbers` | PASS |
| C2 | C2 | linear system (A.2) has the unique solution $(-1, 3, \tfrac12)$ | `sympy.solve` on the coefficients of $n$, $m$, constant | PASS |
| C2-numeric | C2 | $\delta = 3 - N$ reproduces CFL at $d = \tfrac12$ at 5 random $(m, n)$ | direct evaluation of both formulas | PASS |
| C2-break | C2 | with $d \in \{-5, \ldots, 5\}$ integer, an affine fit exists | must FAIL; it FAILS (no integer solution) | FAIL as required |
| C4 | C3, C4 | MS degree of $l_n$ and of $\omega_c^{-1}$ is $1$ | strand arithmetic vs the cited $\lvert\mathfrak L\rvert = 1$, $\lvert\omega_c^{-1}\rvert = 1$ | PASS |
| C4-cfl | C4 | $-(\text{CFL degree at } d = 0) = 1$ for all $k, g$ | symbolic | PASS |
| C5 | C5 | MS degree of $p_{m,n}$ is $n = 1 + (n - 1)$ | strand arithmetic vs composite counting | PASS |
| C6 | C6 | independence of $m$ and $n$ forces $\alpha = \beta = 0$ | `sympy.solve` | PASS |
| C7-sign | C7 | antisymmetric parity signs on the support are $\pm(-1)^{\lvert A\rvert}$ | enumeration of the four sign tables | PASS |
| C7-tensor | C7 | $\Omega_n = (-1)^{\lvert X\rvert}\langle\cdot,\cdot\rangle_n$ equals the Koszul tensor power of $\Omega$ | enumeration over parities, $n = 2, 3$ | PASS |

Not machine-checkable: the reading of the sources (C3 is a citation; the lines are listed under *Source passages*), the overall sign $\omega_c = \pm\Omega$ (their text does not fix it), and the IBL relations themselves (outside the brief).

Dimensional / limiting cases: degrees are integers, no units. Limiting case $n = 1$: all three gradings agree that $\ell_m$ has the degree of the differential's family ($3 - 2m$, $-m$, $1$ respectively), and $m = n = 1$ gives $Q_B$ with ghost number $1$, CFL $-1$, Münster–Sachs $+1$.

Self-review: (1) the objective (one `\agcomment`, verdict on two sentences) is answered; (2) weakest step: C7's identification $\omega_c = \pm\Omega$ relies on parity counting, not on reproducing Münster–Sachs's bpz sign rules, and is stated as such; (3) not checked: their eq. (28) sign conventions, not needed for degrees; (4) a stronger reader might ask whether the output-counting $x^{\ell+g-1}$ of Münster–Sachs versus the input-counting $\hbar^{k+g-1}$ of CFL affects the comparison of $d$: it does not, since $d$ enters only through the degree of the structure maps, and both weightings give $\mathfrak L$ (resp. $\hat{\mathfrak p}$) a homogeneous degree with $|\hbar| = 0$ at $d = 0$.

## Proposed ledger entries

Ledger section: ## Results

### R? — Degree dictionary paper / CFL / Münster–Sachs for the $(m,n)$ products: CFL's affine fit is $3 - N_{\rm gh}$ with $d = \tfrac12$, Münster–Sachs use $d = 0$ via $A_c = s^{-2}\tilde A_c$ [Verified]

- **Source**: `agent/derivations/120-muenster-degree-dictionary.md#C2`, `#C4`, `#C5`, `#C6`, `#C7`
- **Scope**: genus zero, products read from the fundamental vertices with inputs at ghost number 2 and outputs at 3 (physical ghost numbers, C1 pairing); degrees only, not the IBL relations; the overall sign $\omega_c = \pm\Omega$ is not fixed by the Münster–Sachs text
- **Verification**:
  - 2026-11-09 – exact check – `agent/computations/verify-muenster-degree.py` C1, C2, C2-numeric, C4, C4-cfl, C5, C6, C7-sign, C7-tensor, 9/9 PASS; C2-break (integer $d$) FAILS as required

With a strand degree $\delta = \alpha N_{\rm gh} + \beta$, an $(m,n)$ product has degree $n(3\alpha+\beta) - m(2\alpha+\beta)$ ($3n - 2m$ in the paper). CFL's $|\mathfrak p_{k,\ell,g}| = -2d(k+g-1) - 1$ (R5) is reproduced at genus zero by exactly one affine grading, $\delta = 3 - N_{\rm gh}$ (a $C[1]$-degree), with $d = \tfrac12$; no integer $d$ admits a fit, and no affine grading makes the degree independent of both $m$ and $n$. Münster–Sachs (arXiv:1109.4101 App. A.2, sec. IV.B, V.A; arXiv:1208.5626 App. A.2, footnote 2) grade $A_c = s^{-2}\tilde A_c$ (strand degree $N_{\rm gh} - 2$, string field of degree 0, $\omega_c$ of degree $-1$, no degree on $\hbar$): every structure map $l_n^g$ and $\omega_c^{-1}$ has degree $+1$, i.e. CFL's $d = 0$ with the cohomological sign, in the filtered extension ($k = 0$ operations). The paper's $p_{m,n}$ have degree $n$ in their grading, the degree of $l_{m+n-1}\circ(\omega_c^{-1})^{n-1}$, and are not structure maps of the loop homotopy algebra. Their even shift carries no Koszul sign; $\omega_c = \pm\Omega$ with $\Omega(A,B) = (-1)^{|A|}\langle A,B\rangle$ (conventions C1), so their raising corresponds to the paper's $p^{\Omega}_{m,n}$ family, equal to $p_{m,n}$ on even inputs.
