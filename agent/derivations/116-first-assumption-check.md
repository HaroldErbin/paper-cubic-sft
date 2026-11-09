---
description: Independent check of the "Assumptions on the propagator" / "On the first assumption" passage of `paper/sections/02-2-quartic.tex` (ll. 308–345 at afa9795) – verdict per sentence, answers to the five review questions, recommended shortened two-paragraph text; argument correct and consistent with R94–R97, PH35, PH36; sentence 7 of the second paragraph (kernel as a dynamical sector) corrected as the review comment asks
---

# 116 – Check of the "first assumption" passage (section 2.2)

## Status

done – fix pass 1 applied (critic 116). Verdicts on A1–A13 and B1–B12, the five answers, the recommended text, the checks (7/7 PASS, unchanged: no code change). Next: none; a writer applies the recommended text to `paper/sections/02-2-quartic.tex` ll. 305–342.

## Task and objective

**Literal task.** Re-derive and judge the two paragraphs *Assumptions on the propagator* and *On the first assumption* of `paper/sections/02-2-quartic.tex`; answer the five review-comment questions; propose a shorter replacement in two paragraphs.

**Objective.** Final wording of this passage of the paper. No new theorem: the ledger entries R94 (fixed-level operator: entire HS family, Schur reduction), R95 (dichotomy under PH35), R96 (stub change = congruence + exchange shell), R97 (kernel at every momentum is not a conservation law, under PH36), R53 (level-0 definiteness), PH35 (Fredholm form), PH36 (no pair state blind to the exchange tower) are reused as ground truth and the passage is judged against them.

**Conventions.** The paper's: `\sprod{2}{2}` $= p_{2,2}$ the quartic form on $\mathrm{Sym}^2\mathcal H_0$, level matched; at fixed total momentum $P$ and level $L$ it is the integral operator $K^{(L)}_p$ of R94 on $L^2$ in the relative momentum $q$ tensored with the finite oscillator space; "kernel" is the $L^2$ null space of that operator (paper l. 275); "invertible on the quotient" is injective with dense image (paper l. 284, 307). Nothing in this record depends on a sign or normalization convention.

## The passage, sentence by sentence

Paragraph A, *Assumptions on the propagator* (ll. 305–319):

- A1 The propagator inverts $\sprod{2}{2}$ on its image, since $\sprod{2}{2}$ is injective on the quotient.
- A2 At level $L$ and fixed $P$: a finite block of integral operators in $q$, compact, so its inverse on the image is unbounded.
- A3 "Invertible on the quotient" means injective with dense image.
- A4 Three assumptions.
- A5 First: no null vector at generic $P$, the singular squared momenta discrete; at level $0$ none at real $P^2$.
- A6 Second: sources lie in the image, not only in its closure. [Q1]
- A7 The kernel condition places the quintic source in the closure only.
- A8 Gaussian decay of the source is not enough: Gaussian model, window of rates. [Q2]
- A9 Third: quotient and propagator have a limit as the level grows, at generic $P$.
- A10 Weak form of "the kernel stabilizes".
- A11 Kernels at successive levels are not nested (new rows; new null vectors).
- A12 Only convergence assumed, not annihilation of every null vector by all higher rows.
- A13 No finite-level computation decides either form.

Paragraph B, *On the first assumption* (ll. 321–342): [Q3 on the whole]

- B1 Not automatic: zero of a compact operator never isolated; entire HS families with accumulating singular sets exist.
- B2 Fredholm form recovers the finite-dimensional intuition (footnote: Fredholm, index, analytic Fredholm theorem).
- B3 Divide on both sides by the square root of the level-$0$ block at a reference momentum (absolute value on odd functions, assumed injective); at level $0$ bounded with bounded inverse at real $P^2$.
- B4 Assume the result Fredholm of index $0$, analytic in $P^2$ near the real axis, at every level.
- B5 Dichotomy: null vector at every $P$, or at a discrete set of $P^2$.
- B6 One momentum without null vector per level would settle it; above level $0$ none is known. [Q4]
- B7 First case: a whole spacetime field of pair states with no quadratic term, decoupled from the quartic vertex, excluded on physical grounds. [Q5]
- B8 Stub lengthening: strip of exchanged single-string states of every mass, convergent sum, Laplace variable, level part of the stub factor moves no null vector.
- B9 A null vector persisting along the stub decouples from every mass level separately.
- B10 Assume no pair state decouples from the whole tower (level $0$ suggests it); a kernel at every $P$ is then not a conservation law.
- B11 An accidental kernel is not excluded by the argument; the physical exclusion covers it.
- B12 Above level $0$ the form is indefinite near $P^2 = 0$, so isolated real zeros are not excluded; hence "generic momentum".

## The five questions

- Q1 (l. 310) Is the second assumption (image, not closure) needed, or a technicality?
- Q2 (l. 313) Keep the Gaussian-model sentence A8?
- Q3 (l. 323) Independent check of the whole argument; shorten; make it an independent paragraph.
- Q4 (l. 333) Can B6 be proved by taking a generic momentum, where a null vector seems very unlikely?
- Q5 (l. 335) B7 treats a kernel component of $\Sigma_2$ as a field, but the quotient removes it by construction; the issue is at the quintic order: (1) $\mathcal V_5$ keeps the pair-state components along the kernel and the matching is not quintic, (2) $p_{2,2}^{-1} \circ p_{3,2}$ may be ill defined.

## Claim tree

- **A1** Fixed level $L$, fixed real total momentum, $L^2$ sense of the kernel (paper l. 275; R94's object). Vertex family with $\beta > \sqrt2$ (Hilbert–Schmidt, R94).
- **C1** The passage's argument is correct, with one misstatement (B7) and one imprecision (B8), and is consistent with R94–R97, PH35, PH36, R53. [by C1.1–C1.4]
  - **C1.1** Paragraph A: A1–A5, A7, A9–A13 correct; A3 and A10/A12 redundant; A6 needed (Q1: not pedantic); A8 correct but unverifiable by the reader (Q2). [by R94, R95, R53, C2; block: *Range versus closure*] [check: A6-range, A6-range-break]
  - **C1.2** Paragraph B, Fredholm part: B1–B5 correct and are R95 under PH35 in prose; B6 correct but misleading (Q4: horn 1 is "a null vector at every momentum", so no choice of momentum helps; what is needed is a proof of injectivity at one momentum, which at level $0$ is R53 and above level $0$ does not exist). [by R95, PH35, R53; block: *The dichotomy and the reference point*] [check: B6-horn1, B6-horn2, B6-break]
  - **C1.3** Paragraph B, stub part: B8–B12 are R96, R97 (2.2a) and R94 C3 in prose, correct; B8's "level part of the stub factor" is imprecise (the whole factor is injective and creates no null vector; the Gaussian part may remove one from the domain, R96) and B9's "persists" means fixed in the rescaled coordinates (R97). [by R96, R97, R94; block: *Laplace separation*] [check: B9-laplace, B9-accidental, B9-break]
  - **C1.4** B7 misstates the first horn (Q5): a kernel at every momentum is not a dynamical sector (the quotient removes it and the source $\vertex{4}(\Sigma_2, \Psi^2)$ does not reach it); it is a whole spacetime field of constraints, the kernel condition `eq:hs5:kernel-condition` at every momentum on $\mathcal V_5$ and the higher vertices; the range condition on $p_{3,2}$ is separate, needed in either horn (second assumption, C2). The two reasons are the two conditions of `02-3-quintic.tex` ll. 141–144. [by paper `02-3-quintic.tex` ll. 466–493, `eq:hs4:kernel`; block: *What the first horn costs*]
- **C2** The image of a compact operator of infinite rank is never closed, so "image, not closure" is a standing gap, not a pathology; the kernel condition gives $v \in (\ker p)^{\perp} = \overline{\mathrm{ran}\, p}$ for the symmetric bilinear pairing; the first term of `eq:hs5:neumann` needs $v \in \mathrm{ran}\, p$. [block: *Range versus closure*; cited: Picard's criterion, standard] [check: A6-range]

Open gaps: none
Hypotheses in force: PH35, PH36 (as the paper's own assumptions B4, B10; nothing here establishes them), PH25, PH29, PH30 through R53, R94

## Verdicts – paragraph A

| # | Verdict | Reason |
|---|---|---|
| A1 | correct | Definition of the inverse on the quotient; `eq:hs4:quotient`. |
| A2 | correct | R94 C2: finite matrix of Gaussian-times-polynomial integral operators, Hilbert–Schmidt. A compact operator of infinite rank has an unbounded inverse on its range (its singular values accumulate at $0$). |
| A3 | correct but redundant | The same definition is given at l. 284 ("injective with a dense image"). Keep one occurrence. |
| A4 | – | Structural. |
| A5 | correct | The first assumption as the paper states it; the level-$0$ clause is R53 (strict definiteness on even functions at every real $P^2$). "The singular squared momenta form a discrete set" is the content of D1 (R95). |
| A6 | correct, needed | See *Range versus closure* below: the range of a compact operator of infinite rank is never closed, so the gap between image and closure is always there, and the first term of the Neumann series `eq:hs5:neumann`, $\sprod{2}{2}^{-1} \circ \sprod{3}{2}(\Psi, \cdot)$, exists only on the image. Not pedantic. It can be stated in one sentence here, since `02-3-quintic.tex` ll. 488–490 restates and explains it. |
| A7 | correct | For the symmetric bilinear form, the annihilator of $\ker \sprod{2}{2}$ is the closure of the image (block below, eq. (1.2)). This is the justification of A6; merge the two into one sentence. |
| A8 | correct, but unverifiable as written | The statement is 104 C1.5 / eq. (1.6) (Mehler model: a Gaussian source is in the range iff its rate lies in a two-sided window), machine-checked there and again here (`A6-range`). The reader cannot check a model that is not written out. Recommend dropping the model clause; the sentence "Gaussian decay of the source does not by itself place it in the image" can stay without it, or go. |
| A9 | correct | The third assumption as stated; R97's D0 remark: convergence of the truncations gives the full operator, nothing on the kernels. |
| A10 | correct, redundant with A12 | Both say "weak form only". Keep one. |
| A11 | correct | R94 C3 (Schur reduction): a level-$L$ null vector, extended by zero, is null at level $L + 1$ iff the new off-diagonal block annihilates it; the new diagonal block can have its own null vectors. Dense for the paper; one clause suffices. |
| A12 | correct, redundant with A10 | See A10. |
| A13 | correct | Both forms are statements about the limit $L \to \infty$. Keep as the closing sentence. |

### Range versus closure (block for A6–A8, C2)

\subsection*{Setup}
A1. At fixed level and real total momentum, $K := p^{(L)}_{2,2}(P)$ is a compact operator on the fibre space $\mathcal H^{(L)}$ (R94), symmetric for the bilinear pairing $\langle \sigma, \sigma' \rangle = \int \sigma(-P, q) \, \sigma'(P, q)$ of `eq:hs4:diagonal`: $\langle \sigma, K \sigma' \rangle = \langle \sigma', K \sigma \rangle$. The quintic source at momentum $P$ is the covector $v = \sprod{3}{2}(\Psi, \cdot)\vert_P$.

\subsection*{Derivation}
$$
\ker K = \{ N : \langle \sigma, K N \rangle = 0 \ \forall \sigma \} = \{ N : \langle N, K \sigma \rangle = 0 \ \forall \sigma \} = (\mathrm{ran}\, K)^{\perp}, \tag{1.1}
$$
by symmetry; the kernel $V_4(P; q', q)$ is real at real Euclidean momenta (real quadratic form times a real polynomial, paper l. 277), so $\ker K$ is stable under the antilinear involution $J\sigma = \overline{\sigma(-P, \cdot)}$ and the bilinear annihilator coincides with the Hilbert orthocomplement; hence, taking annihilators in the Hilbert space,
$$
(\ker K)^{\perp} = \overline{\mathrm{ran}\, K}. \tag{1.2}
$$
The kernel condition `eq:hs5:kernel-condition` says $v \in (\ker K)^{\perp}$, i.e. $v \in \overline{\mathrm{ran}\, K}$ – and nothing more, since every element of the closure is reached this way.
If $K$ has infinite rank, $\mathrm{ran}\, K \ne \overline{\mathrm{ran}\, K}$: a compact operator with closed range has finite rank (open mapping theorem on $K : (\ker K)^{\perp} \to \mathrm{ran}\, K$ would give a bounded inverse, hence a compact identity on an infinite-dimensional space). So the second assumption excludes a set that is always non-empty.
Picard's criterion, with the singular system $K = \sum_j \mu_j \, u_j \langle w_j, \cdot \rangle$:
$$
v \in \mathrm{ran}\, K \iff v \perp \ker K^{*} \ \text{and} \ \sum_j \frac{|\langle u_j, v \rangle|^2}{\mu_j^2} < \infty, \qquad v \in \overline{\mathrm{ran}\, K} \iff v \perp \ker K^{*}. \tag{1.3}
$$

\subsection*{Commentary}
(1.1): the bilinear pairing of the paper is symmetric because $\vertex{4}$ is; with a sesquilinear product one would get $\overline{\mathrm{ran}\, K^*}$ instead, which is why the paper's "closure of its image" is right as written. (1.3): the Neumann series `eq:hs5:neumann` applies $K^{-1}$ to $v$ as its first term; the exchange *value* $\langle v, K^{-1} v \rangle = \sum_j \langle u_j, v \rangle \langle w_j, v \rangle / \mu_j$ needs only the form-domain condition (104 (1.6), mitigation (a)), weaker than (1.3) – the paper does not need this distinction.

\subsection*{Result}
A6 is a genuine condition (not pedantic), A7 is its exact justification, A8 is a correct illustration the reader cannot check.

\subsection*{Verification}
`A6-range` (Mehler kernel $a = 1$, $c = 1.2$, window $(0.64, 1)$): inside the window the Gaussian ansatz solves $E f = \mathrm{e}^{-b q^2}$ to $3 \times 10^{-16}$ and the Picard terms decrease geometrically (ratios $0.15$, $0.08$); outside, at $b = 0.532$ and $b = 1.108$, they grow (ratios $2.97$, $1.91$): the source is orthogonal to the (trivial) kernel, hence in the closure, and not in the range. `A6-range-break`: the one-sided criterion "$b < a$" admits $b = 0.532$, which the Picard test rejects.

## Verdicts – paragraph B

| # | Verdict | Reason |
|---|---|---|
| B1 | correct for the project's operator, over-general as worded (critic #5) | For a compact operator of infinite rank that is self-adjoint (here $K_p U$ at real $p$, R94), $0$ is an accumulation point of the spectrum (without normality it need not be: a finite-rank operator has $0$ isolated, a Volterra operator has spectrum $\{0\}$), so analytic perturbation theory of isolated eigenvalues gives nothing about the zero eigenvalue. The second clause is R95's exclusion: the family 104 (4.1) is entire, Hilbert–Schmidt, with Gaussian decay, and its singular set accumulates at a finite point. |
| B2 | correct | Footnote: Fredholm, index, and the analytic Fredholm theorem for an analytic family of index-$0$ Fredholm operators on a connected domain (either $\ker \ne 0$ everywhere or invertible off a discrete set) – the Gohberg–Sigal/Steinberg form, which is what R95 uses. Correct as stated. |
| B3 | correct as the statement of the hypothesis; the bounded-inverse clause is an assumption, not a result (critic #4) | PH35's form: $\mathcal T_L(p) = \mathbb K_0^{-1/2} K^{(L)}_p \mathbb K_0^{-1/2}$, $\mathbb K_0$ the level-$0$ block at a reference momentum, with $\lvert K_{00} \rvert$ on the $q$-odd sector, where R53 gives nothing: the injectivity of the block there is an explicit clause of PH35 (falsifier: a null vector of $K_{00}(p_{\rm ref})$ on odd functions), so the parenthesis stays in the text (critic #3). "Bounded with bounded inverse at level $0$ at real $P^2$" is held in the ledger only in the Motivation of PH35 (two-sided comparison of the tile weights, Douglas' lemma); no Proven entry states it (R53 gives strict definiteness at each real $P^2$, not two-sided bounds relative to $K_{00}(p_{\rm ref})$), so the text words it as part of the assumption. |
| B4 | correct | This is PH35, stated as the paper's assumption. |
| B5 | correct | R95's conditional statement. |
| B6 | correct, misleading (Q4) | See *The dichotomy and the reference point*. The sentence is true: a *proof* that $\ker K^{(L)}_{p_0} = 0$ at one $p_0$ selects the second horn, and above level $0$ no such proof exists. It is misread as "find a momentum without null vector", which no sampling can do: in the first horn there is a null vector at *every* momentum, so no momentum is "generic" in the sense wanted, and "a null vector at a given momentum is unlikely" is a statement about a probability measure on operators, not about the given operator. Reword. |
| B7 | wrong as worded (Q5) | See *What the first horn costs*. The kernel at every momentum is not "a field with no quadratic term": the quotient `eq:hs4:quotient` removes it from $\Sigma_2$ and the source $\vertex{4}(\Sigma_2, \Psi^2)$ does not reach it (`eq:hs4:kernel`: $\vertex{4}(N, \cdot) = 0$ on all of $\Hn{2}$, $\Psi^2$ included). What the first horn costs is the kernel condition `eq:hs5:kernel-condition` on a whole spacetime field of pair states, at every momentum, for $\mathcal V_5$ and every higher vertex. The range condition for the composition $p_{2,2}^{-1} \circ p_{3,2}$ is not a cost of the first horn: it is the second assumption, needed in either horn. The *physical* content "a sector of pair states the quartic vertex is blind to at every momentum" is correct and is what the stub argument addresses; it must be said of the vertex, not of the field. |
| B8 | correct, one imprecision | R96 (0.1)–(0.4): the stubbed operator is $\mathrm{e}^{-\alpha' \sigma p^2/4} \Lambda_\sigma (K[s_0] + \int \mathcal E) \Lambda_\sigma$ with $\Lambda_\sigma$ injective (Gaussian in $q$ times the level factor), and $\mathcal E$ the three-channel shell, a convergent sum over mass levels with exponents $h_n(P) = \alpha' P^2 / 2 + 2(n - 1)$ in the stub length – the Laplace variable. The paper says "the level part of the stub factor, invertible, moves no null vector"; the whole $\Lambda_\sigma$ is injective and creates none ($\ker \Lambda K \Lambda = \Lambda^{-1} \ker K$), while its Gaussian part can *remove* a null vector of insufficient decay from the domain (R96). The imprecision does not affect B9, which needs only "creates none". Say "the stub factor, injective, creates no null vector". |
| B9 | correct | R97 (2.1)–(2.2): a null vector fixed along the family (in the rescaled coordinates) satisfies $(K[s_0] + \int_{s_0}^{s} \mathcal E) N = 0$ for all $s$, hence $\mathcal E[s] N = 0$ for all $s$, and the uniqueness theorem for Laplace transforms separates the mass levels. "Persists" should be read as "fixed along the family"; a kernel present at every stub length with a rotating null vector is B11's accidental case. Toy check `B9-laplace`, `B9-accidental`. |
| B10 | correct | PH36(S) stated as an assumption, and R97 (2.2a). The parenthesis "at level $0$ the definiteness stated above suggests it" is the PH36 motivation. |
| B11 | correct, honest | R97: the first-horn exclusion rests on (R′), equivalent given (S) to the exclusion itself. The paper says so. |
| B12 | correct | R94 C3 (b): the full symmetric form is indefinite on a real neighbourhood of $P^2 = 0$ at level $1$ (R68's inertia $(2,1)$ on $\{TT, TD, DD\}$), so definiteness cannot exclude isolated zeros above level $0$. |

### The dichotomy and the reference point (block for B5–B6)

\subsection*{Setup}
A1; PH35 as the paper's assumption B4: $\mathcal T_L(p)$ an analytic family of index-$0$ Fredholm operators on a connected $\Omega_L \supset \mathbb R \cup i \mathbb R$, with $\ker \mathcal T_L(p) \cong \ker K^{(L)}_p$.

\subsection*{Derivation}
The analytic Fredholm theorem gives exactly one of
$$
\text{(I)}\ \ker K^{(L)}_p \ne 0 \ \ \forall p \in \Omega_L, \qquad \text{(II)}\ \{ p \in \Omega_L : \ker K^{(L)}_p \ne 0 \} \text{ discrete}. \tag{2.1}
$$
Hence
$$
\exists\, p_0 \in \Omega_L : \ker K^{(L)}_{p_0} = 0 \ \Longrightarrow\ \text{(II)}, \tag{2.2}
$$
and the converse holds trivially. (2.2) is B6's first clause. Its hypothesis is an injectivity statement about one infinite-dimensional operator; at level $0$ it holds at every real $P^2$ by R53 (strict definiteness on even functions), which is far more than one point. Above level $0$ no proof of injectivity at any single $p_0$ exists (R95 scope: "the reference point at $L \ge 1$ is open"), and definiteness is not available near $P^2 = 0$ (B12); this is B6's second clause.

Why sampling does not help (Q4): under (I) every $p$ has a null vector, so the set of "good" momenta is empty and genericity in $p$ is vacuous. The intuition "a null vector is unlikely" is a statement about a generic *operator* of the class, not about $K^{(L)}$: families in (I) exist in the class (every family with a conserved sector, e.g. a selection rule; toy `B6-horn1`), and whether $K^{(L)}$ is one of them is exactly the question. What the intuition does capture is that case (I) without a conservation law would be an accident; that is the heuristic of B7–B11, not a proof.

\subsection*{Result}
B6 is correct and should be reworded as: to select the second case it suffices to prove the absence of a null vector at a single total momentum per level; the level-$0$ definiteness does this at level $0$; above level $0$ no such proof exists, since the form is no longer definite.

\subsection*{Verification}
`B6-horn1`: an analytic $8 \times 8$ family $1 - C(p)$ with a built-in conserved vector has $\sigma_{\min} = 0$ at all $20$ random complex $p$ – sampling finds no kernel-free momentum. `B6-horn2`: the same family without the rule has $\sigma_{\min} \ge 0.13$ at the $20$ points (zeros of $\det$ isolated). `B6-break` (`--perturb B6-break`): a $10^{-2}$ random perturbation of the rule makes `B6-horn1` fail, as it must.

### Laplace separation and the accidental case (block for B8–B11)

\subsection*{Setup}
Finite-dimensional representation of R96 (0.4): $K(s) = K_0 + \sum_{n=0}^{3} \mathrm{e}^{-h_n s} E_n$, $h_n = 2n$ distinct, $E_n$ generic (the mass-level shells), $K_0$ generic.

\subsection*{Derivation}
If $K(s) N = 0$ for $s$ in an interval, then $K_0 N + \sum_n \mathrm{e}^{-h_n s} E_n N = 0$ identically; linear independence of the exponentials gives $E_n N = 0$ for every $n$ and $K_0 N = 0$ (eq. (3.1)) – B9. Conversely a vector null at one $s$ only is not annihilated by the $E_n$ (break). A family singular at every $s$ with a rotating null vector $N(s)$ has no common null vector, and (3.1) says nothing about it – B11's accidental kernel.

\subsection*{Result}
B8–B11 hold in this representation; the representation checks the logic (separation of the exponentials, the accidental case), not the string vertex, whose shell structure is R96's. The representation carries only the $s$-channel atoms $h_n(P)$; R97's separation also has an absolutely continuous $t, u$ part, which decouples as a whole, and PH36(S) names $(\mathcal E^t + \mathcal E^u) N = 0$ as a separate clause. So B9, and the replacement sentence on it, is the $s$-channel statement over R97 (critic #7).

\subsection*{Verification}
`B9-laplace`: with a built-in common null vector, $K(s) N = 0$ on $25$ points of $[0, 2]$ to $2 \times 10^{-15}$, the least-squares Laplace fit of $K(s) N$ on $\{1, \mathrm{e}^{-h_n s}\}$ returns coefficients $< 5 \times 10^{-15}$, and $|E_n N| < 10^{-15}$ directly. `B9-break`: a vector null at $s = 0$ only is not null at $s > 0$ (norm $2.9$) and not annihilated by the $E_n$. `B9-accidental`: $K(s) = M (1 - N(s) N(s)^{\top})$, $N(s) = (\cos s, \sin s, 0, \ldots)$, has $\sigma_{\min} \le 2 \times 10^{-16}$ at every $s$ and the stacked family has smallest singular value $2.3$ (no common null vector).

### What the first horn costs (block for B7, C1.4)

\subsection*{Setup}
$N_P \in \ker p^{(L)}_{2,2}(P)$ for every real $P^2$ (case (I)); the quotient `eq:hs4:quotient`; the kernel definition `eq:hs4:kernel`, $\vertex{4}(N, A) = 0$ for all $A \in \Hn{2}$.

\subsection*{Derivation}
At quartic order nothing happens: the kinetic term is a function on the quotient by construction, and the source term vanishes on the kernel,
$$
\vertex{4}(N, \Psi^2) = 0 \quad \text{for all } \Psi, \tag{4.1}
$$
by `eq:hs4:kernel` with $A = \Psi^2$. So the kernel directions carry no field and are sourced by nothing: B7's "whole spacetime field of pair states with no quadratic term" describes something the construction has already removed. At quintic order the cubic action is a function on the quotient iff `eq:hs5:kernel-condition` holds, i.e.
$$
\vertex{5}(N_P, A, B) = 0 \quad \forall A \in \Hn{2},\ B \in \Hs, \quad \text{at every } P, \tag{4.2}
$$
and the dressed inverse `eq:hs5:dressed-factor` exists iff moreover $\sprod{3}{2}(\Psi, \cdot)$ takes values in $\mathrm{ran}\, \sprod{2}{2}$ (block *Range versus closure*); this second condition is independent of the horn (it is needed even when $\sprod{2}{2}$ has no kernel, since the image is never closed). Two reasons apply: (1) without (4.2) the quintic coupling sees the component of the pair state along the kernel, the matching at order $\gs^3$ leaves a five-point term depending on the complement (`02-3-quintic.tex` ll. 491–493), and the eliminated action is not $S_{\le 5}$; (2) $p_{2,2}^{-1} \circ p_{3,2}$ needs the range clause. In case (II) the conditions (4.2) are imposed at isolated $P^2$ only; in case (I) they are imposed at every total momentum on a whole spacetime field of pair states, for $\mathcal V_5$ and then every higher vertex (`sec:all:kernel`) – constraints on the geometric vertices that nothing in the construction enforces.

\subsection*{Result}
B7 should say: in the first case the quartic vertex would be blind to a whole spacetime field of pair states; the quotient removes them from $\Sigma_2$ and the source does not reach them, so the quartic order is unaffected, but the construction then requires the quintic and every higher vertex to vanish on them at every momentum – the kernel conditions of the quintic section, imposed on a whole field rather than at isolated momenta. That is the whole first-horn cost. The range condition (the quintic source lies in $\mathrm{ran}\, \sprod{2}{2}$, not only in its closure) is not a cost of the first horn: it is the second assumption, needed in either horn, since the image of an infinite-rank compact operator is never closed (C2; paper `02-3-quintic.tex` l. 490, "needed even when $\sprod{2}{2}$ has no kernel"). It is what $\sprod{2}{2}^{-1} \circ \sprod{3}{2}$ requires in addition (reason (2) of the quintic section). We exclude the first horn on physical grounds. The stub argument then supports the exclusion as a statement about the vertex family.

\subsection*{Verification}
No machine check: (4.1) is the definition of the kernel, (4.2) is quoted from the paper.

## Answers to the five questions

**Q1 (second assumption needed?)** Needed, not pedantic. The image of a compact operator of infinite rank is never closed, so "in the image, not only in its closure" excludes a non-empty set every time; the kernel condition gives exactly the closure (eq. (1.2)); and the first term of the Neumann series `eq:hs5:neumann` is defined only on the image. It is also the second of the two reasons in Q5. Keep it in one sentence: the quintic section (ll. 488–490) explains it again where it is used.

**Q2 (Gaussian-model sentence)** Drop it. The statement is true (104 (1.6), re-checked here: `A6-range`), but the reader cannot check an unwritten model and the paper gains nothing from it. If a warning is wanted, the half sentence "Gaussian decay of the source in the relative momentum does not by itself ensure this" is enough and checkable: the range of a Gaussian kernel is a proper dense subspace whose elements have a specific decay.

**Q3 (independent check, shortening, paragraphing)** The argument is correct and is the ledger's R95 (dichotomy under PH35), R96–R97 (stub argument under PH36) and R94 C3 (indefiniteness above level $0$) in prose; nothing in it is wrong except B7's wording. It can be shortened by about a third: drop A3 (duplicate), A8, one of A10/A12, compress A11, move B3's parenthesis on odd functions out, merge B6 with B12. Paragraphing: the first paragraph holds the three assumptions (A1–A13 compressed); the second, *On the first assumption*, holds the dichotomy (B1–B6, B12) and, as a separate text paragraph, the physical exclusion and its stub argument (B7–B11). Text below.

**Q4 (B6 and generic momenta)** The sentence is correct but invites the misreading. The first horn of the dichotomy is a null vector at *every* momentum; if the operator is in that case, no momentum is free of null vectors and sampling a generic one cannot show anything. "Settle" means *prove* injectivity at one momentum: at level $0$ this is the definiteness (at every real $P^2$, more than needed); above level $0$ no proof at any single momentum exists, and the form is indefinite near $P^2 = 0$, so the definiteness route is closed. "Very unlikely" is the physicist's judgment that an accidental kernel at every momentum, with no conservation law behind it, does not happen – which is exactly the physical exclusion of B7–B11, and not a proof. Reword B6 as in the recommended text (merged with B12).

**Q5 (B7 and the kernel as a field)** The objection to B7 is correct. The kernel directions are removed from $\Sigma_2$ by the quotient and are not sourced ($\vertex{4}(N, \Psi^2) = 0$ by the definition of the kernel), so at quartic order a kernel at every momentum costs nothing. The cost is at quintic order and beyond: the quotient is available only if the quintic vertex vanishes on the kernel (`eq:hs5:kernel-condition`) – otherwise the quintic coupling retains the pair state's component along the kernel and the matching leaves a complement-dependent five-point term – and the dressed inverse needs $\sprod{3}{2}(\Psi, \cdot)$ in the image of $\sprod{2}{2}$. In the first horn the kernel condition is imposed at every momentum on a whole spacetime field of pair states, for every higher vertex; in the second, at isolated momenta only. The range condition is independent of the horn (second assumption, needed in either): it is what $p_{2,2}^{-1} \circ p_{3,2}$ requires in addition. The physical sentence to keep is about the *vertex*: a sector of pair states the quartic vertex is blind to at every momentum. The recommended text says both: the kernel conditions at every momentum, and the second assumption for the composition.

## Recommended text

Replaces ll. 305–342 of `paper/sections/02-2-quartic.tex` (from `\paragraph{Assumptions on the propagator.}` to the end of the sentence before `\paragraph{Collapse of the exchange.}`). Two `\paragraph` blocks; the second holds two text paragraphs (dichotomy; physical exclusion). 21 sentences plus the footnote against 25 plus the footnote. The review comments are answered in this record and not kept.

```latex
\paragraph{Assumptions on the propagator.}

The propagator inverts the vertex $\sprod{2}{2}$ on its image, since $\sprod{2}{2}$ is injective on the quotient $\Hn{2} / \ker \sprod{2}{2}$.
At level $L$ and fixed total momentum, $\sprod{2}{2}$ is a finite block of integral operators in the relative momentum, a compact operator, so its inverse on the image is unbounded.
The propagator rests on three assumptions.
First, at each level, $\sprod{2}{2}$ has no null vector at generic total momentum, the squared total momenta at which it has one forming a discrete set; at level $0$ it has none at real $P^2$, as stated above.
Second, the sources on which the inverse acts, such as the quintic source of \cref{sec:hs:quintic}, lie in the image of $\sprod{2}{2}$ and not only in its closure, which is all that the vanishing of the quintic vertex on the kernel~\eqref{eq:hs5:kernel-condition} gives; the image of a compact operator of infinite rank is never closed.
Third, the quotient and the propagator have a limit as the level grows, at generic total momentum.
This is a weak form of the statement that the kernel stabilizes: the kernels at successive levels are not nested, since the rows added at level $L + 1$ need not annihilate a null vector of level $L$ and can produce null vectors of their own, and we assume only the convergence of the quotient and of the propagator.
No finite-level computation decides this statement in either form.

\paragraph{On the first assumption.}

The first assumption is not automatic: the zero eigenvalue of an infinite-rank compact operator is never isolated when the operator is self-adjoint, as ours is at real momentum, and there are entire families of Hilbert--Schmidt operators of the same type with null vectors on a set of momenta accumulating at a finite point.
We recover the finite-dimensional intuition with a Fredholm form.\footnote{%
  A bounded operator is Fredholm when its kernel and its cokernel are finite-dimensional and its range is closed; its index is the difference of the two dimensions.
  For a family of Fredholm operators of index zero depending analytically on a parameter in a connected domain, the analytic Fredholm theorem states that either the operator is non-invertible for every value of the parameter, or it is invertible except on a discrete set of values.
}
We divide $\sprod{2}{2}$ at level $L$ on both sides by the square root of its level-$0$ block at a fixed reference momentum (of its absolute value on the functions odd in the relative momentum, on which we assume the block injective), and we assume that the result is, at level $0$, a bounded operator with a bounded inverse at real $P^2$ and, at every level, a Fredholm operator of index zero depending analytically on $P^2$ near the real axis.
The analytic Fredholm theorem then leaves two possibilities at each level: a null vector at every total momentum, or null vectors at a discrete set of values of $P^2$ only.
A proof that $\sprod{2}{2}$ has no null vector at a single total momentum would select the second case at that level; at level $0$ the definiteness stated above does it, but above level $0$ the form is indefinite near zero momentum (at level $1$, for the vertex family of~\cite{Erbin:2026:SL2CVerticesClosed}, \cref{sec:further}), so the definiteness route is closed and no other proof is known.
For the same reason isolated real zeros are not excluded above level $0$, and we state the first assumption at generic momentum.

In the first case the quartic vertex would be blind to a whole spacetime field of $2$-string states.
The quotient removes these states from $\Sigma_2$ and the source $\vertex{4}(\Sigma_2, \Psi^2)$ does not reach them, so the quartic order is unaffected; but the construction then requires the quintic and every higher vertex to vanish on them at every momentum, the kernel conditions of \cref{sec:hs:quintic,sec:all:kernel}, imposed on a whole field rather than at isolated momenta; the composition $\sprod{2}{2}^{-1} \circ \sprod{3}{2}$ needs in addition the second assumption, whichever the case.
We exclude this case on physical grounds, with the following argument in support.
Lengthening the stubs of the vertices adds to the vertex region a strip of surfaces on which a single-string state of every mass is exchanged, in a convergent sum over the masses, the added length acting as a Laplace variable that separates the intermediate masses, while the stub factor itself, injective, creates no null vector.
A null vector that persists as the stubs are lengthened must then decouple from the exchange of every mass level separately.
We assume that no $2$-string state decouples from the whole tower of single-string exchanges (at level $0$ the definiteness stated above suggests it); a kernel present at every momentum then cannot be a conservation law of the vertex family.
The argument does not exclude an accidental kernel, present at every momentum without a conservation law behind it, which is what the physical exclusion covers.
```

Changes against the current text, by sentence: A3 dropped (defined at l. 284); A6–A7 merged, with the one-line reason (compact operators of infinite rank); A8 dropped (Q2); A10–A12 merged; B3's parenthesis on the odd sector kept (it is a clause of PH35, falsifier included; critic #3), the bounded-inverse statement moved into the assumption (critic #4), and B3–B4 merged; B1 restricted to the infinite-rank, self-adjoint case (critic #5); B6 reworded and merged with B12 (Q4); B7 rewritten (Q5), with the physical content moved to the vertex; B8's "level part of the stub factor, invertible, moves no null vector" replaced by "the stub factor itself, injective, creates no null vector" (R96). A source for the footnote (analytic Fredholm theorem; candidates Reed–Simon I Thm VI.14, Gohberg–Sigal 1971, Steinberg 1968, all unverified, critic #11) is left to a literature scout; no citation is added to the text here. The Laplace separation of B9 is the $s$-channel statement (critic #7).

## Checks

- Against the ledger (by reading): every sentence of the passage mapped to R94 (A2, A11, B12), R53 (A5, B10's parenthesis), R95 (B1, B5), PH35 (B3–B4), R96 (B8), R97 (B9–B11), PH36 (B10), 104 C1.5 (A6–A8); no sentence contradicts an entry. B7 contradicts the paper's own construction (`eq:hs4:quotient`, `eq:hs4:kernel`), not the ledger.
- Toy-model script `agent/computations/verify-first-assumption.py`, run 2026-11-09 from the project root with `uv run --no-sync python …`, seed 20261109: 7/7 PASS (`A6-range`, `A6-range-break`, `B6-horn1`, `B6-horn2`, `B9-laplace`, `B9-break`, `B9-accidental`), exit 0, max RSS 42 MB, one process, 2 threads; `--perturb B6-break`: `B6-horn1` FAIL and `B6-break` PASS as intended. The checks test the logic of the passage on representations (Mehler kernel, analytic matrix families, finite exponential sums), not the string vertex; output in `agent/scratch/computator-first-assumption-20261109T000500/verify-first-assumption.txt`.
- Limiting case, level $0$: R53 makes $K_{00}(P)$ strictly definite on even functions at every real $P^2$, so case (II) holds at level $0$ with an empty real singular set, consistent with A5's last clause and with the recommended B6.
- Labels used in the recommended text exist: `sec:hs:quintic` (02-3 l. 2), `sec:further` (07b l. 2), `sec:all:kernel` (03 l. 581), `eq:hs5:kernel-condition` (02-3 l. 475).
- Not checked: PH35 and PH36 themselves (the paper's assumptions, open in the ledger); the two-sided comparison behind "bounded with bounded inverse at level $0$" (PH35 motivation only, no Proven entry; the replacement text states it as part of the assumption).

### Self-review

1. Objective answered: a verdict per sentence, the five answers, a shorter two-paragraph text.
2. Weakest step: the bounded-inverse clause of B3, which only the PH35 motivation supports; the text now words it as an assumption. (The odd-sector parenthesis was first dropped and is restored after critic #3.)
3. Not checked: nothing about the string vertex beyond the ledger; acceptable since the brief forbids re-derivation and the passage is prose over R94–R97.
4. A stronger physicist would ask whether "a kernel at every momentum" in the first horn is meant in the $L^2$ fibre sense or the plane-wave sense (104 C5 distinguishes them); the paper fixes the $L^2$ sense at l. 275, so the passage is consistent, and the recommended text keeps it.

## Proposed ledger entries

No new result or hypothesis: the record judges a passage of the paper against existing ledger entries. One annotation is proposed for an existing hypothesis (critic #10).

Ledger section: ## Hypotheses

The annotation is addressed to the *Motivation* of PH36: its wording "a null vector at every total momentum would be a whole spacetime field of two-string states with no quadratic term, a sector decoupled from the quartic vertex" (and the same wording in `knowledge/decisions.md`, 2026-10-20, "Track D closing document") is to be read of the vertex, not of the field. The text to append, under the heading below, is exactly the paragraph it contains.

### Annotation text for PH36

On the Motivation's "whole spacetime field of two-string states with no quadratic term": the physical content is a sector of pair states the quartic vertex is blind to at every momentum. The quotient removes these states from $\Sigma_2$ and the quartic source $\mathcal V_4(\Sigma_2, \Psi^2)$ does not reach them ($\mathcal V_4(N, A) = 0$ for all $A$, $\Psi^2$ included), so a kernel at every momentum is not a dynamical sector and costs nothing at quartic order. The cost is the kernel condition (the cubic action descends to the quotient) imposed at every momentum on a whole spacetime field, for $\mathcal V_5$ and every higher vertex; the range condition on the quintic source is independent of the horn (needed even when $p_{2,2}$ has no kernel). The hypothesis itself, (S) and (R′), concerns the vertex and is unaffected. Source: record 116, C1.4 (checked against the quintic section of the paper; no machine check).
