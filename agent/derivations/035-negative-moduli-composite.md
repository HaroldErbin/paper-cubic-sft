---
id: 035-negative-moduli-composite
task: 16a (plan Task 16, first sub-task)
brief: agent/briefs/active-computator-negative-moduli-16a-20260921T081000.md
created: 2026-09-21
script: codes/verify-negative-moduli.py
---

# 035 — Negative-moduli calculus and the necessary conditions for $\mathcal V_5\,p_{2,2}^{-1}\,\mathcal V_5$ to be a chain in $\mathcal M_{0,6}$

## Status

Last completed: fix pass of 2026-09-21 on critic report `agent/reports/critic-035-negative-moduli-20260921T110000.md` (4 Serious, 9 minor), applied to §§1–4 and to `codes/verify-negative-moduli.py`. Script: `summary: 0 failure(s)` — 24 checks, all PASS (was 20). Changed nodes: A5 (new), C1.1, C2.1, C2.2, C2.3, C3, C3.4, C3.5, C3.6 (new), C4. Next: none (report written; ledger text of §4.5 awaits promotion by the orchestrator).

## 0. Task, objective, conventions

**Literal task.** (16a.1) Define a formal-dimension calculus $\hat d(\cdot)$ on the elementary kernels ($\mathcal V_n$, $Q_B$, $\Delta=Q_B^{-1}$, $p_{2,2}$, $p_{2,2}^{-1}$, $b$-insertions, contractions), prove its equivalence with the ghost-number bookkeeping of 030 §1, and obtain the closure of the count at 4, 5, 6 points as a corollary.
(16a.2) Derive the necessary conditions a chain representation $\mathcal C=\int_\Gamma$, $\Gamma$ a 6-real-dimensional chain of $\mathcal M_{0,6}$, imposes on the composite $\mathcal C\sim\mathcal V_5\,p_{2,2}^{-1}\,\mathcal V_5$ of 013.
(16a.3) Test the first condition (momentum analyticity) in a finite-dimensional toy, with a break-on-purpose check.
(16a.4) Verdict and hand-off.

**Motivating objective.** Whether the dressed sextic vertex $W_6=V_6-\tfrac65\mathcal C$ (R19) has a worldsheet reading, i.e. whether the auxiliary tower is geometric at the first order where $p_{2,2}^{-1}$ does not collapse. $p_{2,2}^{-1}$ alone is excluded (R28, R28′); the composite is not covered by those obstructions. A verdict, or the single decisive computation, is the deliverable; a calculus without a test is not.

**Conventions** (030 §1.1, cited not restated): physical grading $N_{\rm gh}(\Psi)=2$, $N_{\rm gh}(\Sigma)=4$; $\mathcal H_0=\ker L_0^-\cap\ker b_0^-$; $\omega_1$ pairs at 5, $G_2=\omega_1^{\otimes2}$ at 10; map ghost number $\gamma(\mathfrak p)=N_{\rm gh}(\mathfrak p(A_1..A_k))-\sum_iN_{\rm gh}(A_i)$, $\gamma(m_2)=+2$, $\gamma(m_2^{-1})=-2$; form saturation $S$; bivector content $S_B$; translations 030 eqs. (1.2)–(1.5). $p_{2,2}\equiv m_2=G_2^{-1}V_4$ (Harold's notation $\leftrightarrow$ agent notation, `knowledge/project-assessment-2026-09-07.md` §1.2). Anomaly on a connected surface: $S=6(1-g)+n_b-n_c$ (030 eq. (1.1)). $\dim_\R\mathcal M_{g,n}=6g-6+2n$.

**Ledger results reused as ground truth.** R15 (coloured vs resolved genus), R19 (the composite $\mathcal C$, $W_6$, the 90 labelled strand assignments — a Wick count, see (iii)), R23 (via 030: $\gamma(m_2)=+2$), R27 (frozen necks), R28/R28′ (no local kernel; scaling lemma), R38 (kernel condition $\Pi_NV_{5S}[:,:,a]=0$).

## Claim tree

- **A1** Ghost-number conventions and translation formulas of 030 §1.1–1.2 (physical grading; $S=6(1-g)+n_b-n_c$; $\gamma=5\ell-S$; $\gamma=S_B-5\ell$; gluing additivity $S_{\rm tot}=\sum_{\rm surf}S-\sum_{\rm biv}S_B$).
- **A2** Factorisation input of 022 §2.5: at a degenerating node the only insertions are $\omega_1^{-1}=b_0^-\delta_{L_0^-}$ (frozen) or $b_0^+b_0^-\delta/L_0^+$ (smoothed).
- **A3** Finite level truncation: all matrices are finite-dimensional; the matrix elements of $V_4$, $V_5$ are entire functions of the external momenta at fixed level.
- **A4** The composite is the one of 013: $\mathcal C(A,B,Z)=\sum_{\rm strands}\langle V_5(\cdot,A,z^{(1)}),V_4^{-1}V_5(\cdot,B,z^{(2)})\rangle$, $\mathcal C(P,P,P)=v^\top V_4^{-1}v$, $v=V_5(\cdot,P,\Psi)$.
- **A5** (added in the fix pass of 2026-09-21) In (H), the chains $\Gamma_\alpha$ and the coefficients $c_\alpha$ are independent of the external momenta $k_i$: all momentum dependence of the right-hand side of (2.0) comes from the integrals. This is what makes (H) a *worldsheet* representation.
- **C1** (16a.1) The formal dimension $\hat d:=S-6$ (forms/surfaces/maps via $S=5\ell-\gamma$) and $\hat d_B:=6-S_B$ (bivectors) is additive under gluing, equals $\dim_\R\mathcal M_{0,n}$ on integrated genus-0 vertices, gives $\hat d(Q_B)=-2$, $\hat d_B(\Delta)=+2$, $\hat d(p_{2,2})=+2$, $\hat d_B(p_{2,2}^{-1})=-2$, and is the affine image $\hat d=5\ell-6-\gamma$ of the map ghost number. [by A1, C1.1–C1.3; eqs. (1.1)–(1.7)]
  - **C1.1** Inverse lemma: a homogeneous form $\Omega$ of saturation $S$, invertible on the graded space it acts on (or on the quotient by its kernel, itself graded; graded pieces finite-dimensional by A3), has inverse bivector of content $S_B(\Omega^{-1})=S$, hence $\hat d_B(\Omega^{-1})=-\hat d(\Omega)$. [by A1, A3; eq. (1.6)] [check: C1.1]
  - **C1.2** Every row of the 17-row table of 030 §1.3 satisfies $\hat d=5\ell-6-\gamma$ (form/map reading) and $\hat d_B=6-5\ell-\gamma$ (bivector reading) with $\hat d$ computed from insertions. [by A1; eq. (1.7)] [check: C1.2]
  - **C1.3** Closure at 4, 5, 6 points: $2-2+2=2$, $2-2+4-2+2=4$, $4-2+4=6$ real, as gluing sums (1.4). [by C1.1, eqs. (1.2), (1.4); eq. (1.8)] [check: C1.3]
  - **C1.4** The calculus is necessary, not sufficient: the double tube $\mathsf P^{\otimes2}$ and $p_{2,2}^{-1}$ have the same $\hat d_B=-2$; $\mathcal V_4p_{2,2}^{-1}\mathcal V_4$ has $\hat d=2$ and collapses to $\mathcal V_4$. [by C1.2 (rows 7, 17), R27 item 4, R28′ (030 Prop. 3.1–3.2)]
- **C2** (16a.2) Necessary conditions for (H), eq. (2.0). [by C2.1–C2.5]
  - **C2.1** (i) A chain integral with standard node insertions is singular only on $\mathcal S_{\rm phys}$, entire if compact in the interior (Prop. 2.1); the composite is singular exactly on $Z=\{\det V_4=0\}$ at fixed level with residue (2.3); hence, **for coefficients $c_\alpha$ and chains $\Gamma_\alpha$ independent of the external momenta**, the isotropy condition (2.4′) — equivalently (2.4) at a simple zero — at every $P_0\in Z\setminus\mathcal S_{\rm phys}$ is necessary. [by A2, A3, A4, A5; eqs. (2.1)–(2.4′), (3.2)–(3.3)]
  - **C2.2** (v)/(ii′) At a coincidence point the residue must factorise through the level-$N$ single-string space; $\sum_iQ^{(i)}\mathcal C$ must be a codimension-one chain, recursively. [by A2, C2.1; eq. (2.5); cited: Zwiebach 1992, hep-th/9206084] — derived, not machine-checked
  - **C2.3** (iii) One strand-assignment term $\mathcal C_\sigma$ on $\Psi^{\otimes6}$ is invariant, *as a function*, under $G=(S_3\times S_3)\rtimes\mathbb Z_2$ of order 72 (total symmetry of $\mathcal V_5$), so there are $720/72=10$ distinct $(3|3)$ terms; R19's 90 labelled assignments are the Wick count, $90=10\times9$. [by A4; check: C2.3]
  - **C2.4** (iv) The composite has degree $(-1,2)$ in $(V_4,V_5)$; a region-integral chain with polynomial coefficients has non-negative degrees; hence (H) fails uniformly in the vertex data, R28′'s notion. [by A4, R28′; check: C2.4]
  - **C2.5** (ii) of the brief is C2.1 + C2.2; no further independent condition found. [by C2.1, C2.2]
- **C3** (16a.3) In the toy, the composite has a simple pole at a simple zero $P_0$ of $\det V_4(P)$ with residue $v(P_0)^\top N(N^\top M_1N)^{-1}N^\top v(P_0)$; it survives on generic $V_5$, is removed iff the image $W(P_0)$ is totally isotropic for $(N^\top M_1N)^{-1}$ (which at $\dim N=1$ is the R38 condition at $P_0$), and reappears when a non-isotropic direction is sourced. [by C3.1–C3.6]
  - **C3.1** $\det V_4$ vanishes at $P_0$ to order $\dim N$ with $N^\top M_1N$ invertible (toy families (3.1)). [by check: C3.1]
  - **C3.2** Laurent expansion (3.3) of $V_4^{-1}$ and of $\mathcal C$. [by A4; eqs. (3.2)–(3.3)] [check: C3.2]
  - **C3.3** The residue is non-zero for generic $V_5$ and generic external states. [by check: C3.3]
  - **C3.4** The residue vanishes for all polarisations iff $W(P_0)=\{N^\top V_5(\cdot,A,z)|_{P_0}\}$ is totally isotropic for $a^{-1}=(N^\top M_1N)^{-1}$; (2.4) is the case $W=0$, sufficient always and necessary at $\dim N=1$. Imposing (2.4) at $P_0$ alone removes the pole. [by C3.2; eq. (3.4)] [check: C3.4]
  - **C3.5** Break-on-purpose: sourcing $N$ with strength $\varepsilon$ along a generic (non-isotropic) direction restores the pole with residue $\propto\varepsilon^2$. [by check: C3.5]
  - **C3.6** (added in the fix pass) At $\dim N=2$ the converse fails: imposing the R38 condition for one null direction only, chosen so that the surviving image $W$ is the isotropic line of $a^{-1}$, gives an exactly vanishing residue with $\Pi_NV_5(P_0)\ne0$. Making the surviving line non-isotropic restores the pole. [by C3.2, eq. (3.4′); check: C3.6, C3.6-break]
- **C4** (16a.4) Verdict: not excluded at the actual vertex data; excluded as a uniform construction (A5, C2.4); the *first fixed-level falsifier* is named — condition (i) at level $L$, read off the complex zero locus of $\det V_4^{(L)}(P^2)$ with the isotropy/R38 test on it — whose transfer to the full composite requires control of $Z_L$ as $L\to\infty$ (open, §4.3 item 1). [by C1.4, C2.1, C2.4, C3]

**Fix pass 2026-09-21 — changed nodes and their dependents.** No ID was renumbered or withdrawn; A5 and C3.6 are insertions.

| Node           | Statement or justification?                                                                                                   | Dependents         | Still holds?                                                                                               |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------- | ------------------ | ---------------------------------------------------------------------------------------------------------- |
| **A5** (new)   | new assumption                                                                                                                | C2.1, C4           | —                                                                                                          |
| **C1.1**       | statement narrowed (invertibility on the graded space or its graded quotient; A3 cited)                                       | C1, C1.3           | yes, unchanged in content                                                                                  |
| **C2.1**       | statement: conclusion is now (2.4′), and conditional on A5; justification now cites (3.2)–(3.3) instead of the toy check C3.2 | C2, C2.2, C2.5, C4 | yes, with the same direction of implication                                                                |
| **C2.2**       | justification only (citation corrected to Zwiebach hep-th/9206084)                                                            | C2, C2.5           | yes                                                                                                        |
| **C2.3**       | **statement changed**: $\lvert G\rvert=72$, 10 orbits, 90 reinterpreted as the Wick count                                     | C2                 | yes — (iii) becomes a stronger requirement on a candidate chain; nothing downstream used the order-8 group |
| **C3**         | statement: "removed iff R38" → "removed iff $W$ isotropic"                                                                    | C4                 | yes                                                                                                        |
| **C3.4**       | **statement changed**: equivalence restricted to $\dim N=1$                                                                   | C3, C2.1           | yes in the direction actually used (sufficiency, and necessity at simple zeros)                            |
| **C3.5**       | statement clarified (generic, i.e. non-isotropic, direction)                                                                  | C3                 | yes                                                                                                        |
| **C3.6** (new) | new claim                                                                                                                     | C3                 | —                                                                                                          |
| **C4**         | **statement changed**: "sharp and decidable" → "first fixed-level falsifier, transfer open"                                   | root               | yes, weaker and now matching §4.3 item 1                                                                   |

Open gaps: C4's transfer to the full composite ($L\to\infty$ behaviour of $Z_L$, §4.3 item 1) is open and is part of the decisive computation, not a residual caveat; C2.2 ((v)/(ii′)) is derived without machine check and is marked so.

## 1. The calculus (16a.1)

### 1.1 Definition

\subsection*{Setup}
Uses A1. Objects: (a) a *form* $\Omega$ on $n$ legs of $\mathcal H_0$ (a connected surface correlator with its insertions, or a multilinear form built from one); (b) a *bivector* $B$ on $s$ strands (a sewing object filling $2s$ slots); (c) a *map* $\mathfrak p:\mathcal H_0^{\otimes k}\to\mathrm{Sym}^\ell\mathcal H_0$, identified with its $(k+\ell)$-form $\omega_1^{\otimes\ell}(\cdot,\mathfrak p\,\cdot)$.

**Definition (formal dimension).**
$$
\hat d(\Omega):=S(\Omega)-6,\qquad \hat d_B(B):=6-S_B(B),\qquad \hat d(\mathfrak p):=5\ell-6-\gamma(\mathfrak p).
\tag{1.1}
$$
The third is the first applied to the form of $\mathfrak p$, by 030 (1.2). Units: real dimensions.

\subsection*{Derivation}
*(1.2) Vertices.* An integrated genus-0 vertex $\mathcal V_{0,n}$ has $n_b=2n-6$, $n_c=0$, so $S=2n$ and
$$
\hat d(\mathcal V_{0,n})=2n-6=\dim_\R\mathcal M_{0,n}.
\tag{1.2}
$$
At genus $g$ with all moduli integrated, $S=2n$ still (030 row 10), so $\hat d=2n-6=\dim_\R\mathcal M_{g,n}-6g$: the formal dimension is the *sphere-equivalent* dimension, the handles counted at $-6$ each. This is the choice that makes the count of R15/R27 ("the resolved genus is bookkeeping") a statement of the calculus rather than an exception to it.

*(1.3) Kinetic terms.* $Q_B$ as the $1\to1$ map has $\gamma=+1$, so $\hat d(Q_B)=5-6-1=-2$; as the form $\omega_1(A,Q_BB)$: $S=4$ (one $c_0^-$ and one $c$-current, $n_c=2$), $\hat d=4-6=-2=\dim_\R\mathcal M_{0,2}$. $p_{2,2}=m_2$ as the $2\to2$ map: $\gamma=+2$, $\hat d=10-6-2=+2$; as the form $V_4$: $S=8$, $\hat d=2$. Both agree with (1.2).

*(1.4) Gluing.* Gluing forms $\Omega_1,\Omega_2$ through a bivector $B$ (any number of strands) gives $S_{\rm tot}=S_1+S_2-S_B$ (A1), hence
$$
\hat d(\Omega_1\,B\,\Omega_2)=\hat d(\Omega_1)+\hat d(\Omega_2)+\hat d_B(B).
\tag{1.4}
$$
Additivity holds for any number of factors by induction. Composition of *maps* is the special case $B=(\omega_1^{-1})^{\otimes m}$ ($m$ contracted legs, $S_B=5m$): $\hat d(\mathfrak p_1\circ_m\mathfrak p_2)=\hat d(\mathfrak p_1)+\hat d(\mathfrak p_2)+6-5m$, consistent with additivity of $\gamma$ and $\ell_{12}=\ell_1+\ell_2-m$.

*(1.5) Geometric bivectors.* A sewing bivector built from a family of tubes on $s$ strands with $n_b$ antighosts has $S_B=6s-n_b$ (A1, C6 of 030), so
$$
\hat d_B=n_b-6(s-1).
\tag{1.5}
$$
One strand: $\hat d_B=n_b$ = number of integrated moduli ($\omega_1^{-1}$: 1 twist, $\hat d_B=1$; $\mathsf P$: length and twist, $\hat d_B=2$). Two strands: $\hat d_B=n_b-6$; the $-6$ is the handle created when two connected pieces are joined along two nodes. Thus $\hat d_B(\Delta)=+2$ and $\hat d_B(G_2^{-1})=2-6=-4$, $\hat d_B(\mathsf P^{\otimes2})=4-6=-2$.

*(1.6) Inverse lemma (C1.1).* Let $\Omega$ be a non-degenerate bilinear form on a graded space (invertible on that space, or on its quotient by the kernel, which is itself graded because $\Omega$ is homogeneous — for $V_4$ this quotient is $\mathrm{Sym}^2\mathcal H_0/\ker V_4$, the R38 setting; graded pieces finite-dimensional by A3), non-zero only on pairs with $N(A)+N(B)=S$; in a homogeneous basis $\Omega_{ab}\ne0\Rightarrow N_a+N_b=S$. The inverse matrix $(\Omega^{-1})^{ab}$ is supported on the same pairs (the matrix is block-anti-diagonal in ghost number, and the inverse of a block-permutation matrix has the transposed block pattern; $\Omega$ symmetric so the pattern is unchanged). The inverse bivector $\Omega^{-1}=\sum(\Omega^{-1})^{ab}e_a\otimes e_b$ therefore has $S_B=S$, and
$$
\hat d_B(\Omega^{-1})=6-S=-\hat d(\Omega).
\tag{1.6}
$$
Applied: $\hat d_B(Q_B^{-1})=+2$ (matches $\mathsf P$, (1.5)); $\hat d_B(p_{2,2}^{-1})=6-8=-2$ (030 row 17, $S_B=8$). This is the statement "an inverse carries minus the dimension of what it inverts", proven rather than posited, and (1.6) is exactly 022 eq. (2.1) in dimension units.

*(1.7) Affine equivalence with $N_{\rm gh}$ (C1.2).* By (1.1) and 030 (1.2)–(1.3), at fixed strand/output number $\ell$ every object obeys the two affine relations
$$
\hat d=5\ell-6-\gamma\ (\text{form/map reading}),\qquad \hat d_B=6-5\ell-\gamma\ (\text{bivector reading}),
\tag{1.7}
$$
which differ by the constant $12-10\ell$ ($+2$ for $\ell=1$: $\hat{\mathsf P}$ has $\hat d=0$ as a map, $\mathsf P$ has $\hat d_B=2$ as a bivector, the difference being the twist and length of the node it fills; $-8$ for $\ell=2$: $m_2^{-1}$ has $\hat d=6$ as a $2\to2$ map — the sphere-equivalent dimension of the four-form $G_2(\cdot,m_2^{-1}\cdot)$ — and $\hat d_B=-2$ as the propagator bivector). Both readings are checked on all 17 rows of 030 §1.3 in script part 1: from the row's $(\ell,n_b,n_c,g)$ one computes $\hat d$ by (1.5)/(1.2) and from the row's $\gamma$ by (1.7); the two must agree.

*(1.8) Closure (C1.3).* With (1.2), (1.4), (1.6):

- 4 points: $\hat d(\mathcal V_4\,p_{2,2}^{-1}\,\mathcal V_4)=2-2+2=2=\dim_\R\mathcal M_{0,4}$;
- 5 points: $\hat d(\mathcal V_4\,p_{2,2}^{-1}\,\mathcal V_5\,p_{2,2}^{-1}\,\mathcal V_4)=2-2+4-2+2=4=\dim_\R\mathcal M_{0,5}$ (Harold's $1+2+1-1-1=2$ complex);
- 6 points: $\hat d(\mathcal V_5\,p_{2,2}^{-1}\,\mathcal V_5)=4-2+4=6=\dim_\R\mathcal M_{0,6}$.
These are corollaries of gluing additivity and are the same statement as the ghost saturation of R19 item (3) ($10+10-8=12=2\cdot6$). The $\Psi$-channel analogue: $\hat d(\mathcal V_3\,\Delta\,\mathcal V_3)=0+2+0=2$.

\subsection*{Commentary}
(1.2): the choice $\hat d=S-6$ rather than $n_b-n_c$ is forced by wanting one number that is additive under gluing *and* reproduces $\dim\mathcal M_{0,n}$; $n_b-n_c$ alone is additive but assigns $+8$ to $\mathcal V_4p^{-1}\mathcal V_4$ (two spheres, four antighosts, four $b_0^-$), the honest count of the resolved genus-1 surface (R15); subtracting $6g_{\rm res}$ gives back $2$. (1.6): the block-pattern argument needs only that ghost number is a grading of the basis and $\Omega$ is homogeneous; it is convention-free (a shift of conventions changes $S$ and $S_B$ together). (1.7): the two readings of the same object are not a contradiction but the frozen-node bookkeeping: composing maps costs $6-5m$ per composition, gluing forms through a bivector costs $\hat d_B$; the sums agree.

\subsection*{Result}
$$
\boxed{\hat d=S-6,\quad \hat d_B=6-S_B,\quad \hat d=5\ell-6-\gamma,\quad \hat d_B(\Omega^{-1})=-\hat d(\Omega),\quad \hat d(\text{glued})=\textstyle\sum\hat d+\sum\hat d_B.}
$$

### 1.2 What the calculus is, and is not

1. It is the ghost anomaly (030 eq. (1.1)) in dimension units: $S-6$ counts $b$ minus $c$ insertions minus six per handle. The part of this that is standard is the dimension of the moduli space of punctured spheres, $\dim_{\mathbb R}\overline{\mathcal M}_n=2n-6$, **for $n\ge3$** (Kimura, Stasheff & Voronov, *On operad structures of moduli spaces and string theory*, arXiv:hep-th/9307114 — their construction requires stability throughout, and they state no $n=2$ case and no cylinder). Continuing that formula to the unstable cases — the two-punctured sphere at $-2$, carrying the BRST operator, and its inverse the cylinder at $+2$, carrying the propagator — is done here and is taken from no source. The $b$-ghost measure forms and the identity $\sum_iQ^{(i)}\int_\Gamma\Omega=\int_{\partial\Gamma}\Omega$ are Zwiebach 1992, arXiv:hep-th/9206084. The sphere-equivalent handle term $-6g$, the bivector reading (1.5), the inverse lemma (1.6) and the affine map (1.7) to the project's three ghost gradings are re-derived here and are not taken from a source. (Identifiers checked against the arXiv listing; `hep-th/9301097` and `hep-th/9206084` also against `paper/string_theory.bib`. `hep-th/9307114` is in that file as `Kimura:1995:OperadStructuresModuli` but carried no arXiv identifier, which is why a grep for the eprint returned nothing; cite it by its key. the record previously attributed the count to "Sen–Zwiebach, hep-th/9301097", which is in fact Hata & Zwiebach, *Developing the covariant Batalin–Vilkovisky approach to string theory*, and to Costello, math/0412149, *Topological conformal field theories and Calabi–Yau categories*, which does not state a $-6g$ sphere-equivalent count. Both attributions are withdrawn.)
2. It is a *necessary* condition for a geometric representation and never sufficient (C1.4): the double tube $\mathsf P^{\otimes2}$ (030 row 7) and $p_{2,2}^{-1}$ (row 17) have identical $\hat d_B=-2$, $S_B=8$, $\gamma=-2$; the double tube is a bona fide surface family and is excluded as a representation of $p_{2,2}^{-1}$ by other arguments (030 Prop. 3.1–3.2). Conversely $\mathcal V_4p_{2,2}^{-1}\mathcal V_4$ has the right count and equals $\mathcal V_4$ by the algebraic collapse $m_2^{-1}m_2=\mathrm{id}$ (R27 item 4), a "chain" that is a single vertex region.
3. The claim that no family of surfaces has negative dimension is correct for $n_b$ (an antighost count is non-negative) and *wrong* for $\hat d$: two-strand families reach $\hat d_B=n_b-6<0$ through the handle. So negative formal dimension does not by itself obstruct; R28 needs the full grading argument ($\gamma=2+\nu_f$ for *connected* kernels).
4. Corollary for R28 in dimension units: a connected 022-class kernel has $\hat d=4-\gamma=2-\nu_f\le2$ as a map, i.e. its 4-form has $S\le8$: a connected geometric $2\to2$ kernel can never need more ghost number from its four legs than $V_4$ does, while $p_{2,2}^{-1}$ needs $12$.

\subsection*{Verification}
Script part 1: (C1.2) all 17 rows of 030 §1.3 (21 table entries, some rows carrying both a form and a bivector reading), both readings of (1.7) against the insertion count; (C1.1) inverse lemma on random graded symmetric matrices ($S_B(\Omega^{-1})=S(\Omega)$ block pattern, three random gradings, seeded, with a resample loop so that a degenerate draw cannot make the check vacuous); (C1.3) closure sums as integer arithmetic through (1.4)–(1.6); break-on-purpose: the $\ell=2$ affine constant replaced by $\ell=1$'s makes 16 of the $\ell=2$ entries fail.

*What these checks are worth.* C1.2 and C1.3 are **transcription checks, not evidence for the calculus**: (1.7) is (1.1) composed with 030's (1.2)–(1.3), an affine identity, and 030's $\gamma$ column was itself obtained from the same $S$; the break leg (a wrong affine constant) therefore fails trivially. What they establish is that the 17 rows have been transcribed consistently and that no row contradicts the affine relation — the content of C1 is the arithmetic of (1.1)–(1.6), which is proven above, not produced by the script. The same qualification applies to C2.4 below (the scaling $u^2/t$ of $v^\top(tV_4)^{-1}v\,u^2$ is linear algebra; the check verifies the transcription into the model). C1.1 is different: it tests a structural statement (support of the inverse matrix) that the derivation argues but does not compute, and its break leg — an off-grading perturbation — is a genuine falsifier.

## 2. Necessary conditions (16a.2)

\subsection*{Setup}
Uses A2, A3, A4. Hypothesis under test, for the rest of the record:
$$
(\mathrm H)\qquad \mathcal C(\psi_1,\dots,\psi_6)=\sum_{\alpha}c_\alpha\int_{\Gamma_\alpha}\Omega_6(\psi_1,\dots,\psi_6),
\tag{2.0}
$$
with $\Gamma_\alpha$ 6-real-dimensional chains of $\overline{\mathcal M}_{0,6}$ (interior, or reaching boundary divisors with the node insertions of A2, or lower-stratum pieces), $\Omega_6$ the standard $b$-ghost measure form, $c_\alpha$ real coefficients **independent of the external momenta $k_i$** (they may depend on momentum-independent vertex data, e.g. global normalisations), the chains $\Gamma_\alpha$ likewise momentum-independent, the sum finite — this is A5. All momentum dependence of the right-hand side then comes from the chain integrals; that is what makes (H) a *worldsheet* representation rather than an algebraic rewriting, and it is the hypothesis under which condition (i) below is necessary. External states $\psi_i$: momentum eigenstates at fixed level, momenta $k_i\in\mathbb C^D$, $\sum k_i=0$. For a strand assignment, $P:=k_1+k_2+k_3$ is the momentum through the $\Sigma$ propagator; the $\mathrm{Sym}^2\mathcal H_0$ block at total momentum $P$ is $V_4(P)$ (finite by A3), $V_5(P)$ likewise.

\subsection*{Derivation}

**(i) Momentum analyticity.**

*Proposition 2.1 (singular locus of a chain integral).* Under (H) with A2, $\int_\Gamma\Omega_6$ is meromorphic in the $k_i$ and its singularities lie on the physical mass shells
$$
\mathcal S_{\rm phys}=\bigcup_{I\subset\{1..6\},\,2\le|I|\le4}\ \bigcup_{N\ge0}\Big\{\alpha'P_I^2/4+N-1=0\Big\},\qquad P_I=\textstyle\sum_{i\in I}k_i ;
\tag{2.1}
$$
it is entire if $\Gamma$ is compact in the interior of $\mathcal M_{0,6}$.
*Proof.* On a compact interior chain, in any local coordinates the correlator of momentum eigenstates is $\delta(\sum k)\prod_{i<j}|z_{ij}|^{\alpha'k_i\cdot k_j}\times\mathrm{Pol}(k)$ with $|z_{ij}|$ bounded above and away from zero on $\Gamma$ (a compact set avoiding the diagonals), so the integrand is entire in $k$ and uniformly bounded on compact $k$-sets; the integral is entire. Near a boundary divisor of type $I|I^c$, A2 gives the local form $\int_{|q|<\epsilon}\!\frac{d^2q}{|q|^2}\sum_\phi q^{L_0}\bar q^{\bar L_0}V_L(\psi_I,\phi)V_R(\phi^c,\psi_{I^c})=\sum_\phi\frac{2\pi\,\epsilon^{2L_0^+(\phi)}}{2L_0^+(\phi)}\delta_{L_0^-}V_LV_R$ with $L_0^+(\phi)=\alpha'P_I^2/4+N_\phi-1$: a pole at each mass shell of the single-string spectrum, nothing else; a frozen lower-stratum piece contributes $\sum_\phi\delta_{L_0^-}V_LV_R$, entire. Higher-codimension strata iterate. $\square$

*Normalisation.* Here $L_0^+:=(L_0+\bar L_0)/2$, so that $L_0^+(\phi)=\alpha'P_I^2/4+N_\phi-1$ with $N_\phi=(N+\bar N)/2$; derivation 030 (C4)–(C5) uses instead $L_0^+:=L_0+\bar L_0$ (there $e^{-sL_0^+}$, $b_0^+/L_0^+$). The two differ by a factor 2 in the exponent and in the propagator normalisation; the mass-shell set $\mathcal S_{\rm phys}$ is the same, and nothing below depends on the choice.

*Robustness off the real axis.* The conclusion of Prop. 2.1 is stronger than its statement in one respect that matters for hunt item 2 ("is the coincidence branch the only exception?"). Suppose a chain approaches a divisor through a wedge in $\arg q$ rather than the full disc — a non-standard node insertion, outside A2. The local integral still produces poles only at $\alpha'P_I^2/4+(N+\bar N)/2-1+m=0$ with $m\ge0$ integer, i.e. only at **real** values of $P_I^2$ (now including non-level-matched levels, since the $\delta_{L_0^-}$ is lost). Hence a *complex* zero of $\det V_4$ is excluded from the singular locus of any chain with real-analytic approach to the divisor, A2 or not; A2 is needed only to pin $\mathcal S_{\rm phys}$ down to the level-matched integer levels on the real axis. Condition (i) is therefore robust in the regime where it is used below (complex $c_j$).

*The composite.* By A3, A4 and the finite dimension of the block, $V_4(P)^{-1}=\mathrm{adj}\,V_4(P)/\det V_4(P)$ with $\mathrm{adj}$ and $\det$ entire; $V_5$ entire (the vertex regions are compact in the interior of their moduli spaces). Hence $\mathcal C$ is meromorphic with singular locus
$$
Z:=\{P:\ \det V_4(P)=0\}\quad(\text{a function of }P^2\text{ in the continuum; of }P\text{ once the relative momentum is discretised}).
\tag{2.2}
$$
At a point $P_0\in Z$ where the zero of $\det$ is simple in the sense $N:=\ker V_4(P_0)$, $M_1:=\partial_PV_4(P_0)$ with $N^\top M_1N$ non-degenerate, the Laurent expansion is (derived in §3, eq. (3.3))
$$
V_4(P)^{-1}=\frac{N\,(N^\top M_1N)^{-1}N^\top}{P-P_0}+O(1),\qquad
\operatorname{Res}_{P_0}\mathcal C(A,B,Z)=\sum_{\rm strands}V_5(\cdot,A,z^{(1)})^\top N(N^\top M_1N)^{-1}N^\top V_5(\cdot,B,z^{(2)})\big|_{P_0}.
\tag{2.3}
$$

*Condition (i).* Under A5 the right-hand side of (H) is, by Prop. 2.1, regular off $\mathcal S_{\rm phys}$; the left-hand side must then be too. So (H) requires, for every $P_0\in Z$: either $P_0^2\in\mathcal S_{\rm phys}$ (coincidence with a mass shell), or the residue (2.3) vanishes for all external states. The strong form of the latter, and the only form available at a simple zero, is
$$
\Pi_{N(P_0)}\,V_5(\cdot,A,z)\big|_{P_0}=0\quad\forall A\in\mathrm{Sym}^2\mathcal H_0,\ z\in\mathcal H_0,
\tag{2.4}
$$
which is the R38 kernel condition ($\Pi_NV_{5S}[:,:,a]=0$) evaluated at the complex point $P_0$ instead of at the physical kernel.

(2.4) is **sufficient** for the residue to vanish, and at a *simple* zero ($\dim N=1$) also necessary: with $N=n$ the residue is $(n^\top v_1)(n^\top v_2)/(n^\top M_1n)$, which vanishes for all polarisations iff $n^\top V_5(\cdot,A,z)=0$ for all $A,z$. For $\dim N\ge2$ the exact condition is weaker. Writing $w(A,z):=N^\top V_5(\cdot,A,z)|_{P_0}$ and $W(P_0):=\operatorname{span}\{w(A,z)\}\subseteq\mathbb C^{\dim N}$, the residue (2.3) is the value of the bilinear form $a^{-1}=(N^\top M_1N)^{-1}$ on pairs of elements of $W$, so it vanishes for all polarisations iff
$$
W(P_0)\ \text{is totally isotropic for }(N^\top M_1N)^{-1}.
\tag{2.4$'$}
$$
Non-degeneracy of $a^{-1}$ does *not* force $W=0$; it only bounds $\dim W\le\dim N/2$, and at a complex $P_0$ the form $a$ is complex symmetric (not Hermitian), so "definite" is unavailable and a nonzero isotropic subspace always exists once $\dim N\ge2$ — e.g. $a=\operatorname{diag}(1,-1)$, $W=\mathbb C\,(1,1)^\top$. Condition (i) is therefore stated with (2.4′); at generic (simple) zeros, which is the expected situation for a complex zero of $\det V_4(P^2)$, it reduces to (2.4). §3 exhibits both branches in the toy (C3.4, C3.6).

Since $Z$ is a complex hypersurface (in $P^2$: a discrete set of complex values $c_j$, generically not real, while $\mathcal S_{\rm phys}$ is a set of real values), the coincidence branch requires $\det V_4(P^2)$ to vanish only at $P^2=-4(N-1)/\alpha'$, $N\in\mathbb N$ — a property of the vertex data, decidable.
The *unbounded-chain loophole* is therefore closed except for the coincidence branch; the *boundary-contribution loophole* (lower strata, 022 Def. item 4) adds no singularity at all. Both statements rest on A2.

*Caveat (fixed level).* $Z$ is the zero locus of the level-$L$ truncation; the truncated composite $V_5^{(L)\top}(V_4^{(L)})^{-1}V_5^{(L)}$ is not the truncation of the full composite. (2.4) is the necessary condition for a chain representation *of the level-$L$ object*; for the full theory one needs the behaviour of $Z_L$ as $L\to\infty$ (zeros converging to finite points, or escaping to infinity — in the latter case the full composite could be entire). Not checked here; §4.

**(ii) Factorisation, and (v) the residue structure.** By Prop. 2.1 the *location* part of (ii) is (i). What (ii) adds is the residue at a coincidence point $P_0^2=-4(N-1)/\alpha'$: under (H), $\operatorname{Res}=\sum_{\phi\in\text{level }N}V_L(\psi_I,\phi)\,V_R(\phi^c,\psi_{I^c})$ factorises through the single-string space at level $N$ (rank $\le\dim\mathcal H_0^{(N)}$ as a bilinear form on $\mathcal H_0^{\otimes3}\times\mathcal H_0^{\otimes3}$, with $V_{L,R}$ themselves 4-point chain integrals), while (2.3) factorises through $N(P_0)\subset\mathrm{Sym}^2\mathcal H_0$, with $V_5$ blocks on either side. Condition (v): at every coincidence point the two bilinear forms coincide; in particular $\operatorname{rank}(N^\top M_1N)^{-1}$-form $=\dim N(P_0)$ must equal the rank of the level-$N$ factorised form, and $V_5(\cdot,A,z)N$ must factor through a map $\mathcal H_0^{\otimes3}\to\mathcal H_0^{(N)}$ given by a 4-point chain. Not tested here (needs actual vertex data at a coincidence point; none is known to exist).

**(ii′) BRST closure.** A chain integral obeys $\sum_iQ^{(i)}\int_\Gamma\Omega_6=\int_{\partial\Gamma}\Omega_6$ (Zwiebach 1992, arXiv:hep-th/9206084; the record previously mis-attributed this to Sen–Zwiebach, hep-th/9301097, which is Hata–Zwiebach). Under (H), $\sum_iQ^{(i)}\mathcal C$ must be a 5-real-dimensional chain integral. From the cyclic $L_\infty$ relations, $\delta_QV_4=V_3\circ V_3|_{\partial\mathcal V_4}$ and $\delta_QV_5=(V_3\circ V_4+V_4\circ V_3)|_{\partial\mathcal V_5}$, and $\delta_Q(V_4^{-1})=-V_4^{-1}(\delta_QV_4)V_4^{-1}$, so
$$
\sum_iQ^{(i)}\mathcal C=\big[(V_3\!\circ\!V_4+V_4\!\circ\!V_3)\big]V_4^{-1}V_5+V_5V_4^{-1}\big[\cdots\big]-V_5V_4^{-1}(V_3\!\circ\!V_3)V_4^{-1}V_5 .
\tag{2.5}
$$
Terms in which the $V_4$ of $V_3\circ V_4$ feeds both of its remaining legs into $V_4^{-1}$ collapse to $V_3\circ V_5$ (chains: boundary Feynman regions of $\mathcal M_{0,6}$). The other terms — $V_4$ with one leg in $V_3$ and one in $V_4^{-1}$, and the last term with two inverses — are composites of the same type as $\mathcal C$ with one fewer real dimension. (ii′) is therefore recursive: a chain representation of $\mathcal C$ forces chain representations of these codimension-one composites, down to $V_3V_4^{-1}V_3$-type blocks, each subject to (i) with its own $Z$. It does not decide by itself and is not machine-checked here (the toy carries no $Q$).

**(iii) Symmetry.** For one strand assignment, $\mathcal C_\sigma=\langle V_5(\cdot,\Psi_j\Psi_k,\Psi_i),\,V_4^{-1}V_5(\cdot,\Psi_m\Psi_n,\Psi_l)\rangle$ on $\Psi^{\otimes6}$ is invariant under
$$
G=(S_3\times S_3)\rtimes\mathbb Z_2,\qquad |G|=3!\cdot3!\cdot2=72 .
\tag{2.6}
$$
Two of the three factors are obvious: the block exchange is the transpose ($V_4$ symmetric), and the two legs inside each $\mathrm{Sym}^2$ slot may be swapped. The third is **structural, not generic**: $\mathcal V_5$ is a totally (graded-)symmetric 5-form, and the coupling $V_5(\Sigma,\Sigma,\Psi)$ is that form with $\Sigma$ filling two of its legs, so $V_5(X,\Psi_j,\Psi_k,\Psi_i)$ is symmetric in $(i,j,k)$ for every $X\in\mathrm{Sym}^2\mathcal H_0$ — the "spectator" leg $\Psi_i$ is on the same footing as the two paired legs. (The record previously claimed invariance under $(S_2\times S_2)\rtimes\mathbb Z_2$ of order 8 only, and asserted that no further permutation is a symmetry "for generic vertices". That is false; the symmetry follows from total symmetry of $\mathcal V_5$ and holds for every vertex. Confirmed by direct enumeration over $S_6$ on a random totally symmetric $V_5$, script check C2.3b.) Consistently, the momentum $P=k_i+k_j+k_k$ through the $\Sigma$ propagator depends only on the *triple*, not on which of its legs is the spectator.

The orbit count is therefore $|S_6|/|G|=720/72=10$: the ten $(3|3)$ splittings of the six legs. Under (H) with labelled punctures a single chain $\Gamma_\sigma$ must be $G$-invariant (as a chain, up to the orientation sign of $\Omega_6$), and
$$
\mathcal C(\Psi^6)=\sum_{\sigma\in S_6/G}\int_{\sigma\Gamma}\Omega_6,\qquad \#\{\sigma\}=10 ,
$$
exactly as the three Feynman regions of $\mathcal V_3\Delta\mathcal V_3$ carry $S_4$ only together (here: ten $(3|3)$ channels). The number 90 of R19 item (5) / 013 §5 is the **Wick multiplicity**, not an orbit count: it enumerates the labelled assignments $\{(\{i,j\},k),(\{l,m\},n)\}$, of which there are $90=10\times9$ — ten splittings times the $3\times3$ choices of which leg in each triple is the spectator, all nine giving the same kernel value. 013's check 4 sums 90 terms equal in groups of nine and is unaffected. Script part 2 checks both numbers, the 90 by enumeration and the 72 by evaluating the stabiliser of $\mathcal C_\sigma$ *as a function*.

**(iv) Degree in the vertex data.** Consider the rescaling of the vertex *normalisations* $(V_4,V_5)\to(tV_4,uV_5)$ at fixed regions. An *interior* chain of $\Omega_6$ — one drawn inside $\mathcal M_{0,6}$ with the regions used only to delimit it — has degree $(0,0)$: the integrand does not contain the vertex tensors at all. A *Feynman-region* (plumbing) chain factorises into $k_4$ copies of the $\mathcal V_4$ vertex tensor and $k_5$ of $\mathcal V_5$ and so has degree $(k_4,k_5)$ with $k_4,k_5\ge0$. Either way the degree in each vertex tensor is $\ge0$, and it stays $\ge0$ for a finite sum with polynomial coefficients. The composite has degree $(-1,2)$ (A4; script part 2). Hence, exactly as in R28′: **uniformly in the vertex data**, (H) fails with vertex-independent or polynomial coefficients; it can hold only with $c_\alpha$ homogeneous of degree $-1$ in $V_4$ — coefficients that contain the algebraic inverse, the boundary drawn in 030 §5.6. At the actual vertex data (iv) is silent. The 4-point collapse $\mathcal V_4p_{2,2}^{-1}\mathcal V_4=\mathcal V_4$ has degree $(1)$, the degree of one region integral — the counterexample passes (iv), which is why (iv) does not by itself exclude the composite. Consequence for (i). One might fear that a coefficient of degree $-1$ in $V_4$ smuggles the pole into the right-hand side of (H) and voids condition (i): if $c_\alpha$ were allowed to be a function $c_\alpha(V_4(P),V_5(P))$ of the vertex data *at the running momentum*, it would be a function of $P$ and could be singular on $Z$, so nothing would force (2.4). A5 closes this: the coefficients are independent of the external momenta, so a factor $V_4(P)^{-1}$ cannot hide in $c_\alpha$. The degree $-1$ that (iv) forces on a uniform construction would then have to sit in the chains, which (iv) has just shown carry degree $\ge0$: it has nowhere left to go. (i) and (iv) together: a construction uniform in the normalisations is excluded outright, and a construction at the actual data must satisfy (i). What is *not* excluded, and is outside the scope of both conditions, is a representation whose coefficients depend on $P$ — but that is an algebraic rewriting, not a worldsheet one.

\subsection*{Commentary}
(2.1): the exponents in the local plumbing form are those of `bos_feynman` (Erbin 2023 ch. on Feynman rules), $q^{L_0}\bar q^{\bar L_0}$ with the $b_0^\pm$ soaked by $d^2q$; the pole is the $1/L_0^+$ of the propagator, present iff the chain reaches the divisor. (2.2): Lorentz invariance holds after the internal pair momenta are summed; in the toy $P$ is a scalar parameter. (2.4) $\Leftrightarrow$ vanishing residue uses $\dim N=1$ for the "only if"; for $\dim N\ge2$ the right statement is the isotropy condition (2.4′), and the gap is real, not a technicality — C3.6 realises it in the toy. (2.5): signs and the strand sum suppressed; only the structure is used. (iv): "uniform in the vertex data" is R28′'s notion; the family $(tV_4,uV_5)$ is not a consistent vertex system, and the argument only says that no construction blind to the normalisations can work.

\subsection*{Result}
Necessary conditions for (H), in order of strength at the actual vertex data:

1. **(i)** (under A5: momentum-independent chains and coefficients) every zero $P_0$ of $\det V_4(P)$ (fixed level) lies on a mass shell, or satisfies the isotropy condition (2.4′) at $P_0$ — at a simple zero, the R38 condition (2.4); [the first fixed-level falsifier; tested in §3 on a toy; needs the real $Z$, and its transfer to the full composite needs the $L\to\infty$ behaviour of $Z_L$, §4.3 item 1]
2. **(v)** at a coincidence point the residue factorises through the level-$N$ single-string space with 4-point chain blocks; [needs a coincidence point]
3. **(ii′)** $\sum_iQ^{(i)}\mathcal C$ is a codimension-one chain (recursive); [structural]
4. **(iii)** one chain per $(3|3)$ splitting, invariant under $G=(S_3\times S_3)\rtimes\mathbb Z_2$ with $|G|=72$, 10 images under $S_6$ (R19's 90 labelled assignments being $10\times9$ Wick multiplicity); [structural, satisfied by construction]
5. **(iv)** uniformly in the normalisations the composite is not a region integral (degree $(-1,2)$); at the actual data silent. [R28′ transplanted]
(ii) as stated in the brief is (i)+(v). No candidate condition was found to be implied by another beyond this.

\subsection*{Verification}
Script part 2: (C2.3) two distinct counts. (a) Enumeration of the unordered pairs $\{(\{i,j\},k),(\{l,m\},n)\}$ partitioning $\{1..6\}$ gives 90 labelled assignments, whose combinatorial stabiliser in $S_6$ has order 8 — this is the Wick count, and it is blind to the kernel. (b) The stabiliser of $\mathcal C_\sigma$ *as a function*: a fixed sextuple of random states permuted through all of $S_6$, counting the permutations that leave the value of $\mathcal C_\sigma$ unchanged, on a random totally symmetric $V_5$ and a random symmetric $V_4$. Result 72, and the surviving permutations are exactly those preserving the $(3|3)$ splitting $\{i,j,k\}|\{l,m,n\}$ as an unordered pair of triples — eq. (2.6), with $720/72=10$ and $90=10\times9$. Break-on-purpose: replacing $V_5$ by a tensor symmetric only in the two paired slots drops the stabiliser to 8. (C2.4) $\mathcal C(tV_4,uV_5)/\mathcal C(V_4,V_5)=u^2/t$ at random $(t,u)$ in the model of `verify-b3-sextic.py` (break: $u^2t^{-2}$ is rejected) — a transcription check, as noted in §1. (i), (v), (ii′) are analytic statements not checked by machine beyond §3.

## 3. First falsifier: momentum analyticity in a toy (16a.3)

\subsection*{Setup}
Uses A3, A4. Model of `verify-b3-sextic.py`: $\mathcal H_0=\mathbb R^N$, $N=3$, $D=\dim\mathrm{Sym}^2=6$, orthonormal $\mathrm{Sym}^2$ basis $e_I$, $V_{4S}\in\mathrm{Sym}(D\times D)$, $V_{5S}[I,J,a]$ the $\mathrm{Sym}^2\times\mathrm{Sym}^2\times\mathcal H_0$ block of a totally symmetric 5-tensor. Momentum: one complex scalar $P$, standing for $P^2$ of the $\Sigma$ channel; $P_0=0.3+0.7i$ a generic complex point. Families
$$
V_4(P)=M_0+\epsilon M_1+\epsilon^2M_2,\qquad V_5(P)=T_0+\epsilon T_1+\epsilon^2T_2,\qquad \epsilon:=P-P_0,
\tag{3.1}
$$
$M_i$ real symmetric, $M_0$ of corank $\dim N\in\{1,2\}$ with orthonormal null basis $N$ ($D\times\dim N$), $M_1,M_2,T_i$ generic. Composite: $\mathcal C(P)=\mathcal C(A,B,Z)$ of A4 with $V_4^{-1}=V_{4S}(P)^{-1}$ and, on the diagonal, $\mathcal C(P,P,P)=v(P)^\top V_4(P)^{-1}v(P)$, $v_I(P)=V_{5S}(P)[I,\psi\psi,\psi]$.

\subsection*{Derivation}
*(3.2) Block form.* Write $\mathrm{Sym}^2=N\oplus N^\perp$, $M_0=\begin{pmatrix}0&0\\0&K\end{pmatrix}$ with $K$ invertible ($M_0$ symmetric, $N^\perp=\operatorname{im}M_0$). Then
$$
V_4(P)=\begin{pmatrix}\epsilon a+\epsilon^2a_2 & \epsilon b^\top+\epsilon^2b_2^\top\\ \epsilon b+\epsilon^2 b_2 & K+\epsilon c+\epsilon^2c_2\end{pmatrix},\qquad a=N^\top M_1N,\ b=N_\perp^\top M_1N,\ c=N_\perp^\top M_1N_\perp .
\tag{3.2}
$$
*(3.3) Laurent expansion.* Schur complement of the lower-right block: $\Sigma(\epsilon)=\epsilon a+\epsilon^2a_2-\epsilon^2(b+\epsilon b_2)^\top(K+\epsilon c+\ldots)^{-1}(b+\epsilon b_2)=\epsilon\,a+O(\epsilon^2)$. If $a$ is invertible, $\Sigma^{-1}=\epsilon^{-1}a^{-1}+O(1)$, the off-diagonal blocks of the inverse are $-\Sigma^{-1}\epsilon\,b^\top(K+\ldots)^{-1}=O(1)$, and the lower-right block is $O(1)$. Hence
$$
V_4(P)^{-1}=\frac{N\,a^{-1}N^\top}{P-P_0}+O(1),\qquad
\operatorname{Res}_{P_0}\mathcal C(P,P,P)=v(P_0)^\top N\,a^{-1}N^\top v(P_0),
\tag{3.3}
$$
and for the polarised form the residue is $\sum_{\rm strands}V_5(\cdot,A,z^{(1)})^\top Na^{-1}N^\top V_5(\cdot,B,z^{(2)})|_{P_0}$, eq. (2.3). Note that $\det V_4(P)=\epsilon^{\dim N}\det a\det K+O(\epsilon^{\dim N+1})$: for $\dim N=2$ the determinant has a double zero but the inverse a simple pole (C3.1 checks the order).

*(3.4) Vanishing of the residue.* Set $w(A,z):=N^\top V_5(\cdot,A,z)|_{P_0}$ and $W:=\operatorname{span}\{w(A,z):A\in\mathrm{Sym}^2,\ z\in\mathcal H_0\}$. The residue is $a^{-1}(w(A,z^{(1)}),w(B,z^{(2)}))$ symmetrised, so
$$
\operatorname{Res}_{P_0}\mathcal C=0\ \text{for all polarisations}\iff W\ \text{is totally isotropic for }a^{-1}.
\tag{3.4}
$$
("$\Leftarrow$" is immediate. "$\Rightarrow$": take $A=B$, $z^{(1)}=z^{(2)}$ to get $a^{-1}(w,w)=0$ for every $w\in\{w(A,z)\}$, then polarise; since the $w(A,z)$ span $W$ and $a^{-1}$ is bilinear, $a^{-1}$ vanishes identically on $W\times W$.)

The relation to (2.4) is:

- $\dim N=1$: a nonzero isotropic subspace of a non-degenerate form on a one-dimensional space does not exist, so (3.4) forces $W=0$, i.e. $\Pi_NV_{5S}(P_0)[:,:,a]=0$ — the R38 condition (2.4). Equivalence holds.
- $\dim N\ge2$: (2.4) ($W=0$) remains sufficient but is no longer necessary. Non-degeneracy of $a^{-1}$ bounds $\dim W\le\dim N/2$ but does not force $W=0$, and an isotropic line exists whenever $a^{-1}$ has a null vector — always over $\mathbb C$, and already over $\mathbb R$ when $a$ is indefinite. Explicitly, at $\dim N=2$, choose $u\in\mathbb C^2$ with $u^\top a^{-1}u=0$, pick $\mu$ with $\mu^\top u=0$, and impose the R38 condition for the *single* null direction $n_\mu=N\mu$:
  $$
  n_\mu^{ij}\,T_{0,ijklm}=0\quad\forall\,k,l,m
  \ \Longrightarrow\ W\subseteq\mathbb C\,u\ \Longrightarrow\ \operatorname{Res}_{P_0}\mathcal C=0,\ \text{while}\ \Pi_NV_5(P_0)\ne0 .
  \tag{3.4$'$}
  $$
  This is checked in the script (C3.6), together with its falsifier: replacing $u$ by a generic, non-isotropic direction in the same construction restores the pole.

The earlier version of this record asserted the equivalence for all $\dim N$, on the ground that "with generic $T_1,T_2$ the span is all of $N$ unless the condition holds". That argument is wrong: $W$ is built from $T_0$ alone (the residue sees only $V_5(P_0)$, cf. the Commentary below), so the genericity of $T_1,T_2$ is irrelevant to it, and $W$ can be a proper isotropic subspace.

*(3.5) R38 closure subspace.* $\{T\in\mathrm{Sym}^5\mathbb R^N:\ n^{ij}T_{ijklm}=0\ \forall\,n\in N,\ \forall klm\}$; for $N=3$, $\dim\mathrm{Sym}^5=21$, $10\dim N$ constraints. $T_0$ is replaced by its orthogonal projection onto this subspace (script `r38_project`, SVD null space), $T_1,T_2$ left generic, so that only the value at $P_0$ is constrained — the weakest form of (2.4).

\subsection*{Commentary}
(3.3): the derivation uses only that $M_0$ is symmetric (so the complement is orthogonal) and that $a=N^\top M_1N$ is invertible — the generic "simple" case; if $a$ is singular the pole is of higher order and the residue formula changes (not needed: a higher-order pole is a fortiori a singularity). (3.4): the point of the toy is that the pole is governed by $v(P_0)$ alone; the $P$-dependence of $V_5$ away from $P_0$ is irrelevant to the residue, which is why the condition is one imposed *at $P_0$* and not at the physical kernel or anywhere else in $P$. What the condition *is* at $P_0$ is the isotropy of $W(P_0)$ (3.4): R38 there is sufficient always, and necessary only at a simple zero.

\subsection*{Result}
In the toy, with generic vertex data the composite has a simple pole at every simple zero of $\det V_4(P)$, residue (3.3), non-zero for generic external states; the pole is removed iff $W(P_0)$ is totally isotropic for $a^{-1}$ (3.4) — at $\dim N=1$, iff the R38 condition holds at $P_0$; sourcing a generic null direction with strength $\varepsilon$ restores it with residue $\propto\varepsilon^2$. At $\dim N=2$ the isotropic branch is realised: a $V_5$ with $\Pi_NV_5(P_0)\ne0$ can still have zero residue (3.4′), so R38 at $P_0$ is *strictly stronger* than what (i) demands at a multiple zero. Condition (i) is nonetheless **not vacuous**: it is not implied by R38 (which constrains the physical kernel, not the complex zero locus), and it fails for generic vertex data. What decides the real case is the set $Z$ and the R38 condition on it.

\subsection*{Verification}
`codes/verify-negative-moduli.py`, run with `.venv/bin/python`, seed 20260921, both $\dim N=1$ and $\dim N=2$ (numbers from the run of the fix pass; the random draws shifted when part 2 gained its new checks, so the values differ from the first run while the structure does not):

- C3.1: $|\det V_4(P_0)|<10^{-10}$, order of the zero $=\dim N$ (log-slope $0.999$, $2.003$), $\det a\ne0$;
- C3.2: residue of the matrix $V_4^{-1}$ by a 128-point Cauchy integral on $|P-P_0|=0.05$ vs $Na^{-1}N^\top$ (independent path), max deviation $\sim10^{-16}$; same for $\mathcal C(P,P,P)$ vs (3.3) ($-0.0075$ resp. $7.4143$);
- C3.3: $|\operatorname{Res}|=0.008,\ 0.077$ ($\dim N=1$; diagonal, polarised), $7.41,\ 1.11$ ($\dim N=2$): the pole survives;
- C3.4: after R38 projection at $P_0$ (violation $<10^{-15}$, $|T_0|=3.9,\ 3.5$), residues $<10^{-17}$ and $|\mathcal C(P_0+10^{-4})|/|\mathcal C(P_0+10^{-2})|\approx1$: no pole;
- C3.5 (break-on-purpose): $T_0^{R38}+\varepsilon\,\mathrm{Sym}(n\otimes w)$ with a *generic* null direction gives $|\operatorname{Res}|=2.1\cdot10^{-5}$ ($8.4\cdot10^{-5}$) at $\varepsilon=0.05$ and ratio $\operatorname{Res}(0.1)/\operatorname{Res}(0.05)=4.000$;
- C3.6 ($\dim N=2$, added in the fix pass): imposing the R38 condition for the single null direction $n_\mu$, $\mu\perp u$ with $u^\top a^{-1}u=0$ (here $u$ real, $|u^\top a^{-1}u|=4\cdot10^{-16}$), gives $W$ of rank 1 (singular values $2.01$, $7\cdot10^{-16}$) along $u$ to $2\cdot10^{-15}$, with $|\Pi_NV_5(P_0)|=1.00$ and residues $1.2\cdot10^{-16}$ (diagonal and polarised): the residue vanishes although R38 fails. At this seed $u$ is real and the break leg's direction is a real vector cast to complex, so `r38_project` is fed only real data: the `.conj().T` null-space extraction repaired in the fix pass is correct for a complex $a$, but the complex branch is not exercised by the committed run, and C3.6's PASS is not evidence that it works. Break leg: the same construction with a generic non-isotropic direction ($u^\top a^{-1}u=0.078$) gives $|\operatorname{Res}|=1.5\cdot10^{-5}$, $1.5\cdot10^{-1}$ — the pole is back.

Falsifiability of the two checks added in the fix pass, demonstrated by breaking each once outside the committed script: replacing the totally symmetric $V_5$ of C2.3b by one symmetric only inside each $\mathrm{Sym}^2$ slot makes C2.3b report `FAIL` with $|\mathrm{stab}|=8$; adding $(0.37,0)$ to the isotropic $u$ of C3.6 makes it report `FAIL` with $u^\top a^{-1}u=0.64$ and $|\operatorname{Res}|=3.7\cdot10^{-4}$, $5.3\cdot10^{-2}$.

Summary line: `summary: 0 failure(s)` (24 checks).

## 4. Verdict, hand-off, what was not checked (16a.4)

### 4.1 Verdict

**Not excluded at the actual vertex data; excluded as a uniform construction; the first fixed-level falsifier is named, and its transfer to the full composite is open.**

- *Uniformly in the vertex data* (the R28′ notion: a chain built from the regions and vertex-independent or polynomial coefficients, valid for the family $(tV_4,uV_5)$): excluded by (iv), degree $(-1,2)$ versus non-negative degrees. This transplants 030 §5.6 to the composite and is the same boundary — the algebraic inverse must sit in the coefficients, which A5 forbids for a worldsheet representation.
- *At the actual vertex data*: no obstruction is exhibited. The formal count closes (C1.3) but is not sufficient (C1.4). Condition (i) is the **first fixed-level falsifier**: the toy shows it is neither vacuous nor implied by R38 (C3). It is not a *sharp* criterion for (H) and should not be called one — what it decides directly is whether the level-$L$ truncated object $V_5^{(L)\top}(V_4^{(L)})^{-1}V_5^{(L)}$ is a chain integral, and that object is not the truncation of the composite (§4.3 item 1). Whether the condition holds at level $L$ is a property of the real vertices: condition (2.4′) on the complex zero locus $Z_L=\{\det V_4^{(L)}(P^2)=0\}$, reducing to (2.4) at simple zeros. Transferring a negative outcome to (H) requires the behaviour of $Z_L$ as $L\to\infty$, which is open and is part of the computation, not a residual caveat.
- *Loopholes closed under A2*: an unbounded chain (reaching degenerations) or a measure with lower-stratum contributions produces singularities only on the mass shells $\mathcal S_{\rm phys}$ (Prop. 2.1); the composite escapes (i) only if $Z\subseteq\mathcal S_{\rm phys}$ at the offending points (the coincidence branch) and then (v) must hold there.

### 4.2 The decisive computation: the fixed-level falsifier and its $L\to\infty$ transfer (hand-off to 16b / Task 15 Q2)

Compute, from the actual vertices, the $\mathrm{Sym}^2\mathcal H_0$ blocks $V_4(P^2)$ and $V_5(P^2)[:,:,a]$ at the lowest level truncation at which the block at total momentum $P$ is a finite matrix (compact target directions or a discretisation of the internal relative momentum $k_1-k_2$), as entire functions of complex $P^2$; locate the zeros $c_j$ of $\det V_4(P^2)$ in the complex plane; at each, compute $N(c_j)=\ker V_4(c_j)$, the image $W(c_j)=\{N^\top V_5(c_j)(\cdot,A,z)\}$ and test its isotropy for $(N^\top\partial V_4(c_j)N)^{-1}$ — at a simple zero ($\dim N=1$, the generic case) this is the R38 test $\Pi_{N(c_j)}V_5(c_j)[:,:,a]=0$ for all $a$. Outcomes:

- some $c_j\notin\{-4(N-1)/\alpha'\}$ with $W(c_j)$ not isotropic: the level-$L$ **truncated** object is not a chain integral with standard node insertions (A2). This is evidence against (H) only if the offending zeros persist — converge to finite points, with non-isotropic $W$ there — as $L\to\infty$; that tracking is part of the decisive computation, not a residual question;
- all zeros satisfy (2.4′): condition (i) passes and (v)/(ii′) become the next filters;
- all zeros on mass shells: (v) is the test.
Cheapest first step — a **model, not a truncation of the theory**: in the theory the tachyon-pair block at fixed total momentum $P$ is an integral kernel in the relative momentum $k_1-k_2$ (§4.3 item 2), and the four-tachyon Koba–Nielsen integral depends on $s$ and $t$, not on $P^2$ alone; so the relative momentum must first be frozen, e.g. to the diagonal $k_1=k_2=P/2$, which makes the block $1\times1$ and defines the model. In that model the tachyon–tachyon element $V_4^{TT}(P^2)=\int_{\mathcal V_{0,4}}d^2z\,|z|^{\alpha'k_1\cdot k_2\ldots}$ (the momentum-resolved form of R15 item 3, the integral $I(\beta)$ of the companion SL(2,C) computation) is a scalar entire function of $P^2$ with computable complex zeros; at a zero, $N$ is the whole one-dimensional block and (2.4) reads $V_5^{TTTTT}(c_j)=0$ — two Koba–Nielsen integrals over $\mathcal V_{0,4}$ and $\mathcal V_{0,5}$ sharing a complex zero, generically false and decidable numerically. A negative outcome here bounds nothing rigorously; it is a cheap indicator of what to expect from the real computation. Data shared with Task 15 Q2: the momentum-resolved $V_5$ block is the same object as the $N\subseteq N_5$ test of 034 §4 (viii).

### 4.3 What was not checked

1. **Level truncation / the infinite-dimensional inverse.** $Z$ is defined at finite level; the level-$L$ composite is not the truncation of the full composite (§2, caveat). Zeros of $\det V_4^{(L)}$ could move to infinity as $L\to\infty$, in which case the full composite might be entire and (i) satisfied. Not addressed; requires tracking $Z_L$ across levels.
2. **The internal momentum integral.** In the non-compact theory the block at total momentum $P$ is an integral kernel in the relative momentum of the $\Sigma$ pair; the toy discretises it. Endpoint or pinch singularities of that integral are a second possible source of non-analyticity, not seen by the toy.
3. **Genus $\ge1$.** The calculus (§1) is genus-aware (handles at $-6$), but the conditions of §2 and the toy concern $\mathcal M_{0,6}$ only; composites with $p_{2,2}^{-1}$ inside loops are not addressed.
4. **The unbounded-chain loophole** is closed only under A2 (factorisation input) and only outside the coincidence branch; whether $Z\cap\mathcal S_{\rm phys}\ne\emptyset$ for the real vertices is unknown.
5. **Conditions (ii′) and (v)** are derived, not tested (no $Q$ in the toy; no coincidence point known).
6. **The toy's finite dimension** cannot see: accumulation of zeros, essential singularities, or a nowhere-vanishing $\det$ (possible for an infinite matrix, impossible for a non-constant polynomial family).
7. **Higher-order zeros** ($N^\top M_1N$ singular): the residue formula (3.3) assumes the simple case; a higher-order pole is a stronger obstruction, so this does not weaken (i).
8. **Momentum-independence (A5)** of the chains $\Gamma_\alpha$ and coefficients $c_\alpha$. Standard for a worldsheet representation, and argued in (iv) to be the only reading under which (H) says anything, but it is an assumption and not a theorem: condition (i) is void without it.
9. **The isotropy refinement at multiple zeros.** (2.4′) rather than (2.4) is the necessary condition when $\dim N\ge2$; C3.6 shows the difference is real. Whether multiple zeros occur in $Z_L$ for the actual vertices is unknown, and the isotropy test is the one to implement in §4.2 even if simple zeros are expected.

### 4.4 Self-review

1. *Objective vs task.* The literal task (calculus, conditions, toy) is done; the objective (verdict on the worldsheet reading of $W_6$) is advanced to a fixed-level falsifier plus a named transfer problem, not settled — as the brief allows ("not excluded, with the decisive computation named"), provided the transfer is counted as part of that computation.
2. *Weakest step.* The identification of the singular locus of the composite with $Z$ at fixed level (item 1 above); shored up by stating it as a fixed-level statement and naming the $L\to\infty$ question in the hand-off, and no longer described as "sharp" or "decisive" anywhere.
3. *Not checked and why.* Items 1–9; each needs vertex data or infinite-dimensional analysis outside a 30-minute sub-task.
4. *Five-minute objection.* "The truncated inverse is not the inverse" — item 1, stated. Second: "R38 holds on the physical kernel; by analytic continuation in $P^2$ does it propagate to $Z$?" No: R38 is a condition at the points of $Z$ (if any) on the real axis, and (2.4) at a complex $c_j$ is an independent condition; there is no identity relating $V_5$ at different $P^2$ (the toy makes this explicit with generic $T_1,T_2$).

### 4.5 Proposed ledger text (orchestrator promotes; not written to `knowledge/results.md`)

> **R39 (proposed) — Task 16a: negative-moduli calculus and necessary conditions for $\mathcal V_5p_{2,2}^{-1}\mathcal V_5$ to be a chain of $\mathcal M_{0,6}$ (derivation 035).** (1) Calculus: $\hat d=S-6$ (forms), $\hat d_B=6-S_B$ (bivectors), additive under gluing, $=\dim_\R\mathcal M_{0,n}$ on integrated vertices with handles at $-6$; inverse lemma $\hat d_B(\Omega^{-1})=-\hat d(\Omega)$ (proven: the inverse of a homogeneous form, invertible on the graded space or on its graded quotient by the kernel, has the same ghost support); affine to the map ghost number, $\hat d=5\ell-6-\gamma$, transcription-checked on all 17 rows of 030 §1.3; closure $2-2+2$, $2-2+4-2+2$, $4-2+4$ as corollaries. The operadic degree is standard (Kimura–Stasheff–Voronov, hep-th/9307114; Zwiebach 1992, hep-th/9206084 for the $b$-ghost forms and the BRST–boundary identity); the $-6g$ handle term, the bivector reading and the inverse lemma are this record's. Necessary, never sufficient (double tube and $p_{2,2}^{-1}$ share $\hat d_B=-2$; negative $\hat d$ is not by itself an obstruction — the claim that no family has negative dimension holds for $n_b$, not $\hat d$). (2) Necessary conditions for $\mathcal C=\sum c_\alpha\int_{\Gamma_\alpha}$ with $\Gamma_\alpha,c_\alpha$ **independent of the external momenta** (the hypothesis that makes (H) a worldsheet representation; without it a coefficient of degree $-1$ in $V_4$ carries the pole and (i) says nothing): (i) every zero $P_0$ of $\det V_4(P^2)$ at fixed level lies on a mass shell, or the image $W(P_0)=\{N^\top V_5(P_0)(\cdot,A,z)\}$ is totally isotropic for $(N^\top\partial V_4N)^{-1}$ — at a simple zero, the R38 condition $\Pi_{N(P_0)}V_5(P_0)[:,:,a]=0$ at the complex point $P_0$ (Prop. 2.1: chain integrals with standard node insertions are singular only on mass shells, entire if bounded — closes the unbounded-chain and boundary-measure loopholes modulo the factorisation input, except for coincidence; off the real axis the conclusion survives even non-standard approach to the divisor); (v) residue factorisation at coincidence points; (ii′) BRST closure, recursive; (iii) one $G$-invariant chain per $(3|3)$ splitting with $G=(S_3\times S_3)\rtimes\mathbb Z_2$, $|G|=72$, $10=720/72$ images under $S_6$, R19's 90 labelled assignments being the Wick count $10\times9$; (iv) degree $(-1,2)$: excluded as a uniform construction (R28′ transplanted), silent at the actual data. (3) Toy (numpy, $\dim N=1,2$, 24/24 PASS, contour residue vs Laurent formula $v_0^\top N(N^\top M_1N)^{-1}N^\top v_0$, two break-on-purpose legs): the pole survives on generic $V_5$, is removed iff $W$ is isotropic, reappears $\propto\varepsilon^2$ when a generic null direction is sourced; at $\dim N=2$ an isotropic $W$ gives zero residue with $\Pi_NV_5\ne0$, so R38 is sufficient but not necessary there — (i) is not vacuous and not implied by R38. **Verdict: not excluded at the actual data; excluded as a uniform construction; first falsifier = complex zero locus of $\det V_4^{(L)}(P^2)$ with the isotropy/R38 test on it, at fixed level — decisive for (H) only together with the $L\to\infty$ behaviour of $Z_L$, which is open (hand-off 16b / Task 15 Q2; cheapest indicator, a model and not a truncation: shared complex zero of $V_4^{TT}$ and $V_5^{TTTTT}$ at frozen relative momentum).** Not checked: level-truncation limit of $Z$, internal momentum integral, genus $\ge1$, (ii′)/(v), momentum-independence of the chains (assumed), multiple-zero isotropy in the real vertices. | Calculus: Proven (finite bookkeeping) + transcription-checked (script part 1); conditions: derived ((i) rigorous under A2/A3/A5 at fixed level; (iii) verified; (iv) rigorous; (ii′), (v) argued); toy: Verified (24/24). | `agent/derivations/035-negative-moduli-composite.md`; `codes/verify-negative-moduli.py`
