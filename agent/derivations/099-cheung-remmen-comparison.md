---
description: Cheung–Remmen's cubic gravity action vs the cubic HS closed SFT in level truncation – notions of match, verdict per notion, Nützi–Reiterer, citation verdict
---

# 099 – Cheung–Remmen's cubic gravity action vs the cubic closed SFT in level truncation

Brief: `agent/briefs/active-computator-099-cheung-remmen-20261012T115500.md`.

## Task and objective

- **Literal task.** Decide whether the paper's cubic closed SFT ($\Sigma_k$ construction), restricted to a level truncation containing the massless sector, can be matched to the cubic action for gravity of Cheung and Remmen (arXiv:1705.00626, `Cheung:2017:HiddenSimplicityGravity`), structure first, fields and couplings only if a match looks possible.
- **Objective.** Settle the citation decision of `knowledge/decisions.md` (2026-10-12, about 12:00): Cheung–Remmen is cited next to the Yang–Mills strictification of Borsten et al. (`paper/sections/01-introduction.tex` l. 201–205) only if the two constructions match in level truncation.
  A negative answer must name the obstruction; a positive one must say in which sense they match.

## Conventions

- Book conventions (the project conventions); metric $(-,+,\dots,+)$, which is also Cheung–Remmen's ("mostly-plus", their eq. (4)), so no sign translation of $\eta$ is needed.
- Cheung–Remmen's formulas are quoted in their own normalisation (overall $1/16\pi G$, their $\sigma^{ab} = \sqrt{-g}\,g^{ab}$, $\sigma^{ab} = \eta^{ab} - h^{ab}$ for the $\sigma^{-1}$-basis actions); no SFT normalisation is mixed into them.
  Only structural statements (degree in the fields, locality, rank, inertia) are compared across the two theories, and those are normalisation-independent.
- Vertex normalisation of the SFT side: conventions C4; the quartic HS step is the paper's eq. `eq:hs4:S4tilde`.

## Notions of match and their deciding criteria

From strongest to weakest.

- **(a) Field-and-action match.** Cheung–Remmen's fields $(h_{ab}, A^a{}_{bc})$ and action arise from the level-truncated cubic theory $(\Psi_{\le L}, \Sigma_2, \dots)$ after a field redefinition (possibly non-local, perturbative).
  *Decided by:* (i) an invariant of perturbative field redefinitions on which the two theories differ – the on-shell quartic coupling of the massless sector, or the flatness of a zero-momentum direction; (ii) a counting of auxiliary degrees of freedom (local field with finitely many components per point vs bilocal field).
- **(b) Mechanism match.** The same mechanism – an algebraic auxiliary field, coupled linearly to a composite quadratic in the fields, with a field-independent invertible kernel, whose exchange replaces a quartic contact term – is present in both, and in the SFT at the massless level.
  *Decided by:* rewriting Cheung–Remmen's action in that form (if possible, by which redefinition), identifying the quartic contact term it replaces, and comparing with the term $\Sigma_2$ replaces in the massless truncation.
  Sub-question (b′): whether the paper's quartic step, applied to the Einstein–Hilbert $L_\infty$ algebra itself, gives Cheung–Remmen's auxiliary field.
- **(c) Analogy.** Both rewrite a non-polynomial gauge-theory action as a cubic one with algebraically eliminable auxiliary fields, as Borsten et al. do for Yang–Mills.
  *Decided by:* the structural facts of (b) without the identification of the replaced term.

## Claim tree

- **A1** Level truncation: $\Psi$ restricted to the states of level $\le L$, $L \ge (1,1)$, so that the massless sector (graviton, $B$-field, ghost dilaton, and the auxiliary vectors outside Siegel gauge) is kept; $\Sigma_2 \in \mathrm{Sym}^2$ of the truncated space modulo $\ker V_4$; vertices are those of the full theory restricted to the kept states (no massive field integrated out).
- **A2** Cheung–Remmen's action is their eq. (18) (equivalently (15), (23)), equivalent to Einstein–Hilbert to all orders about flat space, $D \ge 3$; their claims are cited, not rederived.
- **A3** "Field redefinition" means a perturbative one, $\Phi' = L\Phi + O(\Phi^2)$ with $L$ invertible, possibly non-local; auxiliary fields may be added or removed only through their algebraic elimination.
- **H1** In any level truncation containing the massless sector, the massless-pair block of the quartic kernel $K_P(q', q)$ (paper eq. `eq:hs4:diagonal`) has infinite rank as a kernel in the relative momentum. Motivation: the Koba–Nielsen factor of $V_4$ carries $\exp(\alpha' q \cdot q'\, \ell(\xi))$ with $\ell$ a logarithm of cross-ratios varying over the two-dimensional region $\mathcal V_{0,4}$, so the expansion in $q \cdot q'$ has as coefficients the moments of $\ell$ over the region, and the paper states that $K_P$ is smooth and not a delta function times a polynomial. Falsified or discharged by: the Taylor coefficients of the massless block of $K_P$ in $q \cdot q'$ – a non-zero coefficient at every order discharges H1, vanishing beyond a finite order falsifies it.
- **C0** Verdict: the cubic closed SFT in level truncation cannot be matched to Cheung–Remmen's action (notion (a) fails, with a field-redefinition-invariant obstruction); the two share a mechanism (notion (b)) only at quartic order and only for the Einstein–Hilbert action itself, not for the level-truncated string field theory; notion (c) holds. [by C1, C2, C3, C4]
- **C1** Notion (a) fails: no level truncation of the cubic theory is field-redefinition equivalent to Cheung–Remmen's action. [by C1.1–C1.3]
  - **C1.1** Einstein–Hilbert, hence Cheung–Remmen's action, has the constant-metric deformation along a compact direction as an exactly flat zero-momentum direction; in a level truncation of closed SFT the quartic effective potential of the corresponding marginal field is non-zero at every level where it has been computed – $I_4 \simeq -0.256$ for the massless sector alone, $c(0) + I_4 \simeq 0.456$ with the tachyon, and up to level $300$ (Yang–Zwiebach's level $\ell = L_0 + \bar L_0 + 2$) – and flatness is reached only as the level goes to infinity. [cited: Yang–Zwiebach 2005 (hep-th/0501142) sec. 1 (decomposition $\mathcal C(\ell) + I_4$ of the $a^4$ coefficient and the condition $\mathcal C(\infty) + I_4 = 0$), sec. 2 ($c(0) = 0.71191$), sec. 4 ($I_4 = -0.25598$), sec. 5 (metric and $B$ in two directions); same mechanism for the dilaton in the project: R64 (iv), R89]
  - **C1.2** The Hubbard–Stratonovich step does not change C1.1: at quartic order the elimination of $\Sigma_2$ is exact and returns the ordinary truncated quartic action, so the truncated cubic theory and the truncated non-polynomial theory have the same quartic zero-momentum potential. [by R64 (i), R89; paper `eq:hs4:S4tilde`]
  - **C1.3** A perturbative field redefinition (A3) maps a one-parameter family of zero-momentum solutions tangent to an on-shell state to such a family; a non-zero quartic potential along the marginal direction excludes the family at quartic order. [block: §1 (1.3)]
- **C2** Notion (b): Cheung–Remmen's action is, after a local linear shift of its auxiliary field, a Hubbard–Stratonovich rewriting of the quartic Einstein–Hilbert vertex in the densitised-inverse-metric basis, and the paper's quartic step applied to that vertex gives the same auxiliary field and the same quartic-order action; the term this replaces is not the term $\Sigma_2$ replaces in a massless truncation. [by C2.1–C2.5]
  - **C2.1** Cheung–Remmen's $A^a{}_{bc}$ is a local first-order (Palatini-type) variable: on shell $A^a{}_{bc} = \Gamma^a{}_{bc} - \tfrac12 \delta^a{}_{(b} \Gamma^d{}_{c)d}$, linear in $h$ at leading order, with an $A$–$h$ mixing in the quadratic action; its elimination is algebraic and exact to all orders. [cited: Cheung–Remmen eqs. (18), (20), (21) and sec. 1]
  - **C2.2** Under the local linear shift $A = A' - \tfrac12 M_0^{-1} b(h)$, the action becomes (2.5): $h$-only terms stop at cubic order, $A'$ has the constant kernel $M_0$, couples linearly to the local bilinear composite $J(h,h) = M_1(h) M_0^{-1} b(h)$, and through the vertex $A' M_1(h) A'$; the quartic vertex in this basis is $\tfrac14 J M_0^{-1} J$ and the $n$-point one $\tfrac14 b (M_0^{-1} M_1)^{n-2} M_0^{-1} b$. [eqs. (2.2)–(2.6)] [check: C2.2-shift, C2.2-tower]
  - **C2.3** $M_0$ is non-degenerate and indefinite: inertia $(10, 8)$, $(22, 18)$, $(40, 35)$ in $D = 3, 4, 5$. [by check: C2.3-D3, C2.3-D4, C2.3-D5]
  - **C2.4** The paper's quartic step $-V_4(\Sigma_2^2) + 2 V_4(\Sigma_2, \Psi^2)$ applied to $V_4 = \tfrac14 J^{\mathsf T} M_0^{-1} J$ (with $M_0^{-1}$ non-degenerate on $\operatorname{im} J$) equals the quartic-order part of (2.5) under $A' = -\tfrac12 M_0^{-1} J(\Sigma_2)$, and the paper's quotient $\mathrm{Sym}^2/\ker V_4$ is $\operatorname{im} J$, a space of local fields. [by C2.2, C2.3; eq. (2.7)] [check: C2.4-map, C2.4-rank]
  - **C2.5** In a massless truncation of the SFT, $\Sigma_2$ replaces the elementary quartic vertex restricted to massless states, while the quartic coupling of the massless fields that the Einstein–Hilbert term represents also contains the massive exchanges, which the cubic theory keeps as $\Psi$-exchange diagrams. [by C1.1, C1.2; paper `eq:hs4:S4tilde`]
- **C3** Notion (c) holds: both constructions make a non-polynomial gauge-theory action cubic with algebraically eliminable auxiliary fields with an invertible, indefinite kernel, in the same sense as the Yang–Mills strictification the paper already cites. [by C2.1–C2.4, R64 (ii)]
- **C4** Nützi–Reiterer formulate the field equations of GR as the Maurer–Cartan equation of a differential graded Lie algebra built from a frame and a Lorentz connection (first-order, no auxiliary field replacing a composite, no action), so they bear on the match only at the level of notion (c). [cited: Nützi–Reiterer 2018 Thm. 5.1, Prop. 5.6, footnote 9, sec. 1; §4 (4.1)]
- **C5** Under H1, the auxiliary spaces cannot be matched by counting: $\Sigma_2$ restricted to massless pairs has infinitely many components per spacetime point, Cheung–Remmen's $A$ has $D^2(D+1)/2$. [by H1, A1; §1 (1.4)]

Open gaps: none
Hypotheses in force: H1 (C5 only; C0 does not rest on C5)

## 1. Notion (a) – field-and-action match

\subsection*{Setup}

A1, A2, A3. On the SFT side, $\Psi_{\le L}$ and $\Sigma_2 \in \mathrm{Sym}^2 \mathcal H_{\le L} / \ker V_4$ with the quartic step of the paper, eq. `eq:hs4:S4tilde`,
$\tilde S_4 = -\tfrac{g_s^2}{4!} V_4(\Sigma_2^2) + \tfrac{2 g_s^2}{4!} V_4(\Sigma_2, \Psi^2)$.
On the gravity side, eq. (18) of Cheung–Remmen,
$\mathcal L_{\rm EH} = -\bigl(A^a{}_{bc} A^b{}_{ad} - \tfrac{1}{D-1} A^a{}_{ac} A^b{}_{bd}\bigr) \sigma^{cd} + A^a{}_{bc} \partial_a \sigma^{bc}$, $\sigma^{ab} = \sqrt{-g}\, g^{ab} = \eta^{ab} - h^{ab}$.
Let $a$ be the coefficient of the zero-momentum marginal state $c \bar c \, \partial X \bar\partial X$ along a compact direction $X$, a constant deformation of $G_{XX}$.

\subsection*{Derivation}

(1.1) *The two objects.*
Cheung–Remmen's auxiliary field is local, a function of one point with $D \cdot D(D+1)/2$ components ($40$ in $D = 4$), and on shell it is the linear combination (21) of Christoffel symbols, of degree one in $h$ at leading order.
The paper's $\Sigma_2$ has components $\sigma_{\alpha_1 \alpha_2}(k_1, k_2)$, functions of two momenta (paper, *Spacetime fields*), and on shell $\Sigma_2 = \Psi^2$ modulo $\ker V_4$, of degree two in $\Psi$; its quadratic term $V_4(\Sigma_2^2)$ does not mix it with $\Psi$.

(1.2) *The flat direction.*
For every constant $a$, $g = \eta + a\, \delta_X \delta_X$ is flat, so the Einstein–Hilbert action, a two-derivative functional, vanishes on the whole family and every member solves the field equations: the zero-momentum potential of $a$ vanishes to all orders.
Cheung–Remmen's action has the same family of solutions (A2: their equations of motion (19)–(20) are equivalent to Einstein's).
In closed SFT, the quartic term of the effective potential of $a$ is (Yang–Zwiebach, sec. 1)
$$
\kappa^2 \mathbb V_{(\ell)}(a) = \bigl(\mathcal C(\ell) + I_4\bigr) a^4 + O(a^6), \qquad \mathcal C(\ell) = \sum_{\ell' \le \ell} c(\ell'), \tag{1.2}
$$
with $c(\ell')$ the exchange of the massive fields of level $\ell'$ through the cubic vertex and $I_4$ the elementary quartic vertex.
Their values: $I_4 = -0.25598$ (sec. 4), $c(0) = 0.71191$ from the tachyon (sec. 2), $\mathcal C(\infty) = 0.25585$ by extrapolation, the cancellation $\mathcal C(\infty) + I_4 = 0$ holding to five digits with Moeller's value of $I_4$; the coefficient $\mathcal C(\ell) + I_4$ decreases in magnitude with the level, is non-zero at every level computed (up to $\ell = 300$, sec. 4), and is fitted by $d_0 + d_2/\ell^2 + d_3/\ell^3$, which vanishes only in the limit. An accidental zero at one finite level is not excluded by these data, but would remove the obstruction at that level and at quartic order only.
A truncation that keeps the massless sector only gives $I_4 \neq 0$; one that adds the tachyon gives $c(0) + I_4 \simeq 0.456$.
Section 5 of the same paper repeats the test for the constant metric and $B$-field in two directions, with the same outcome.
The project has the same phenomenon for the dilaton: in the level-$(1,1)$ truncation the dilaton valley is lifted by $+\tfrac{81}{8192} \beta^{-4} \delta^4$, exactly the dropped level-$(2,2)$ exchange (R64 (iv)), and at $d^5$ by the dropped $f_1$ exchange (R89).

(1.3) *Invariance of the obstruction.*
Let $F$ be a field redefinition (A3) from Cheung–Remmen's fields to the truncated fields, with the auxiliary fields of either side eliminated algebraically.
It maps the family $\Phi(a)$ of (1.2) to a family $F(\Phi(a))$ of zero-momentum solutions of the truncated theory, with tangent $L \Phi'(0)$ at $a = 0$: an on-shell zero-momentum state of the truncated free theory, which in the massless sector is the marginal state up to gauge.
The quartic term of the truncated potential along that state is (1.2) at the truncation level, non-zero, so the equations of motion of the truncated theory at order $a^3$ have no solution tangent to it: no such $F$ exists.
By R64 (i) the elimination of $\Sigma_2$ is exact at quartic order and returns the truncated non-polynomial quartic action, so the same holds for the cubic theory (C1.2); R89 adds that the cubic structure contributes nothing new up to $d^5$.

(1.4) *Counting (conditional).*
A field redefinition of the auxiliary sectors must be a bijection between the auxiliary spaces at each total momentum $P$.
Cheung–Remmen's is finite-dimensional, $D^2(D+1)/2$ per $P$.
The paper's is $\mathrm{Sym}^2 \mathcal H_{\le L} / \ker V_4$ at fixed $P$, whose massless-pair block is a space of functions of the relative momentum $q$ modulo the kernel of $K_P(q', q)$; under H1 it is infinite-dimensional.
Level truncation truncates the oscillator content, not the dependence on $q$, so this persists at every level.

\subsection*{Commentary}

- (1.1): the degree mismatch (degree one vs two at leading order) is not by itself an obstruction: it is removed by the local linear shift of §2, which turns Cheung–Remmen's field into one of degree two.
- (1.2): the marginal field of Yang–Zwiebach is a constant component of the closed-string metric along a compactified direction, the string-theory counterpart of the flat family of Einstein–Hilbert; their normalisation ($\alpha' = 2$, $\langle c_{-1} \bar c_{-1} c_0^- c_0^+ c_1 \bar c_1 \rangle = 1$) differs from the book's (C-ledger), which changes the numbers by positive factors and not whether they vanish.
- (1.3): the argument needs only that $F$ is perturbative and invertible at linear order, so non-local redefinitions such as those relating string fields to the metric are included.
  It does not need the momentum-dependent four-graviton amplitude, whose truncated form would require vertex data (excluded by the brief).
- The underlying reason: the Einstein–Hilbert quartic coupling corresponds to the effective quartic coupling of the massless fields after all massive fields, the tachyon included, are integrated out (the Wilsonian effective action; Sen 2016, arXiv:1609.00459, for the superstring), followed by the low-energy limit and a field redefinition; a finite truncation keeps the elementary vertex and a finite part of the exchanges.
- The content of the massless sector (graviton, $B$, ghost dilaton, auxiliary vectors) differs from Cheung–Remmen's (graviton only), but this is not used: in the Einstein frame the dilaton and $B$ enter the two-derivative action quadratically, so pure gravity is a consistent truncation at tree level, and the mismatch alone would not decide (a).

\subsection*{Result}

Notion (a) fails at every finite level: the truncated cubic theory lifts, at quartic order, a zero-momentum direction that Cheung–Remmen's action keeps exactly flat, and this is invariant under perturbative field redefinitions (C1).
Under H1 there is in addition a counting obstruction between the auxiliary spaces (C5).

\subsection*{Verification}

No machine check: (1.2) is cited (Yang–Zwiebach numbers, R64, R89), (1.3) is a two-line argument.
The cited cancellation was read in Yang–Zwiebach, hep-th/0501142, secs. 1, 2, 4.

## 2. Notion (b) – mechanism match

\subsection*{Setup}

A2. Write Cheung–Remmen's eq. (18) with $\sigma^{cd} = \eta^{cd} - h^{cd}$ as
$$
\mathcal L = -A \cdot M(h) \cdot A - A \cdot b(h), \qquad M(h) = M_0 - M_1(h), \tag{2.1}
$$
where $A \cdot M \cdot A$ is the quadratic form $\bigl(A^a{}_{bc} A^b{}_{ad} - \tfrac{1}{D-1} A^a{}_{ac} A^b{}_{bd}\bigr) \sigma^{cd}$ split into its $\eta$ part $M_0$ (constant, algebraic) and its $h$ part $M_1(h)$ (linear in $h$, algebraic), and $A \cdot b(h) = A^a{}_{bc} \partial_a h^{bc}$ (from $A^a{}_{bc} \partial_a \sigma^{bc} = -A^a{}_{bc} \partial_a h^{bc}$).
Inverses and products of $M_0$, $M_1$ act pointwise on the $D^2(D+1)/2$ components; $b$ is the only derivative.

\subsection*{Derivation}

$$
\begin{aligned}
A_* &= -\tfrac12 M(h)^{-1} b(h), \\
\mathcal L_{\rm eff} &= \tfrac14\, b\, M(h)^{-1} b = \sum_{n \ge 2} \tfrac14\, b \,\bigl(M_0^{-1} M_1(h)\bigr)^{n-2} M_0^{-1}\, b ,
\end{aligned} \tag{2.2–2.3}
$$
the $n$-th term being of degree $n$ in $h$.
Shift by the linearised on-shell value:
$$
A = A' - \tfrac12 M_0^{-1} b(h). \tag{2.4}
$$
Then
$$
\mathcal L = \tfrac14\, b M_0^{-1} b + \tfrac14\, b M_0^{-1} M_1(h) M_0^{-1} b - A' \cdot \bigl(M_0 - M_1(h)\bigr) \cdot A' - A' \cdot J(h, h), \qquad J(h, h) := M_1(h) M_0^{-1} b(h), \tag{2.5}
$$
and the quartic vertex of Einstein–Hilbert in this field basis is
$$
\mathcal L^{(4)}_{\rm eff} = \tfrac14\, J(h,h) \, M_0^{-1} J(h,h). \tag{2.6}
$$
Apply the paper's quartic step to a quartic form factorised as $V_4(\Sigma, \Sigma') = \tfrac14 J(\Sigma) M_0^{-1} J(\Sigma')$, with $J$ extended linearly to $\mathrm{Sym}^2$ (couplings stripped):
$$
-V_4(\Sigma_2, \Sigma_2) + 2 V_4(\Sigma_2, h^2) = -A' M_0 A' - A' \cdot J(h, h) \quad \text{at} \quad A' = -\tfrac12 M_0^{-1} J(\Sigma_2), \tag{2.7}
$$
and, when $M_0^{-1}$ is non-degenerate on $\operatorname{im} J$, $\ker V_4 = \ker J$, so $\mathrm{Sym}^2 / \ker V_4 \cong \operatorname{im} J$.

\subsection*{Commentary}

- (2.2–2.3): the elimination of $A$ is a Gaussian with a field-dependent kernel; the whole tower of Einstein–Hilbert vertices in the $\sigma^{ab}$ basis is the geometric series of $M(h)^{-1}$.
  This is a special property of Einstein–Hilbert in this basis (their conformal-weight homogeneity, eq. (13)–(14)), not of a generic non-polynomial action.
- (2.4): the shift is local, linear, invertible, with constant coefficients: a field redefinition in the sense of A3.
  It removes the $A$–$h$ mixing of the quadratic action; in the new variable the auxiliary field is of degree two on shell, $A'_* = -\tfrac12 (M_0 - M_1)^{-1} J$.
- (2.5): $-2 A' M_0 (-\tfrac12 M_0^{-1} b)$ cancels $-A' \cdot b$; the cross term from $M_1$ gives $-A' \cdot J$; the $h$-only terms are the quadratic and the cubic vertex. Checked as an exact polynomial identity in a finite-dimensional model (C2.2-shift).
- (2.6): the degree-four term of (2.3) is $\tfrac14 b M_0^{-1} M_1 M_0^{-1} M_1 M_0^{-1} b = \tfrac14 J M_0^{-1} J$ ($M_0^{-1}$ and $M_1$ symmetric).
- (2.7): direct substitution; the quotient statement is linear algebra ($V_4 = \tfrac14 J^{\mathsf T} M_0^{-1} J$ has the rank of $J$ when $M_0^{-1}$ is non-degenerate on $\operatorname{im} J$).
- Beyond quartic order (not decided, not needed for the verdict): Cheung–Remmen use one auxiliary field whose kernel depends on $h$, $M_0 - M_1(h)$; the paper's quintic step also makes the $\Sigma_2$ kernel field-dependent, $A - \tfrac{g}{5} W(\Psi)$ with $W$ built from $V_5$ (R64 (ii)), the same device.
  Whether the paper's tower, applied to the Einstein–Hilbert $V_5$, $V_6$, … in this basis, reproduces $A' M_1(h) A'$ and stops at $\Sigma_2$ is not checked: $W$ is built from the fully symmetrised $V_5$, while $M_1(h)$ is one particular split of it.
  Deciding it needs the paper's quintic and sextic steps applied to (2.3) at $n = 5, 6$.

\subsection*{The term replaced at the massless level}

In the massless truncation of the SFT, $\Sigma_2$ restricted to massless pairs replaces $V_4$ restricted to massless states: an elementary vertex with a smooth, non-polynomial kernel in the relative momentum (paper eq. `eq:hs4:diagonal`).
The quartic coupling that (2.6) represents is the effective one, $V_4|_{\rm massless}$ plus the exchanges of all massive fields (§1, (1.2) and commentary); in the cubic theory these exchanges stay $\Psi$-exchange diagrams through $V_3$ and are not absorbed into $\Sigma_2$.
So the two auxiliary fields act by the same mechanism on different quartic terms.
The identification (2.7) holds only if the paper's construction is applied to the low-energy effective theory of the massless fields, not to the level-truncated SFT; and only there does $\Sigma_2$ become local, because the quotient by $\ker V_4$ collapses the bilocal field onto $\operatorname{im} J$ when $V_4$ is local.

\subsection*{Result}

Notion (b) holds at quartic order in the following precise sense: after the local linear shift (2.4), Cheung–Remmen's action is a Hubbard–Stratonovich rewriting of the quartic Einstein–Hilbert vertex (2.6), with a local auxiliary field, a constant non-degenerate indefinite kernel, and a linear coupling to a bilinear composite; the paper's quartic step applied to that vertex gives the same field and the same quartic-order action (2.7).
It is not a match in level truncation: the term $\Sigma_2$ replaces in a massless truncation is the elementary $V_4$, not the effective quartic coupling that (2.6) is.

\subsection*{Verification}

`codes/verify-cheung-remmen.py` (seed 20261012), 12/12 PASS, each check with a broken counterpart that fails:
- C2.2-shift: (2.5) from (2.1)+(2.4), exact polynomial identity in a model with $\dim A = 4$, $\dim h = 3$, random integer $M_0$, $M_1$, $b$.
- C2.2-tower: the Taylor coefficients of $\tfrac14 b M(th)^{-1} b$ for $n = 2, \dots, 7$ against (2.3), and the quartic one against (2.6).
- C2.3-D3/D4/D5: Cheung–Remmen's kernel at $\sigma = \eta$, built from their eq. (18), exact determinant $\tfrac14$, $\tfrac{256}{81}$, $-243$; inertia $(10, 8)$, $(22, 18)$, $(40, 35)$; the break (degenerate $g^{cd}$) gives determinant zero.
- C2.4-map, C2.4-rank: (2.7) as a polynomial identity; $\operatorname{rank} V_4 = \operatorname{rank} J = 5$ on $\mathrm{Sym}^2 \mathbb R^4$ (dimension 10).
Scope: the model checks the algebra of the shift and of the map, not the Einstein–Hilbert tensor structure of $M_1$ and $b$ (only $M_0$ is the real one); that (18) is Einstein–Hilbert is cited.

## 3. Notion (c) – analogy

Both constructions make a non-polynomial gauge-theory action cubic by adding fields that are eliminated algebraically, with an invertible kernel that is indefinite: Cheung–Remmen's $M_0$ has inertia $(22, 18)$ in $D = 4$ (C2.3), the paper's auxiliary form has signature $(2, 1)$ already in the five-field truncation (R64 (ii)).
In both, the elimination is exact at quartic order; Cheung–Remmen's field is algebraic and carries no physical state, and the paper's carries none through the order its gauge section establishes (introduction, *Two illustrations*).
Differences that the analogy must not hide: Cheung–Remmen's field is local and also replaces all higher vertices through its $h$-dependent kernel, a property of Einstein–Hilbert in the $\sigma^{ab}$ basis; the paper's $\Sigma_2$ is bilocal, replaces the elementary quartic vertex only, and the higher vertices need the tower $\Sigma_k$.
Cheung–Remmen's construction is, in their words, "a field redefinition away from the first-order Palatini formalism" (sec. 1); the Hubbard–Stratonovich reading needs the shift (2.4).
This is the register of the Borsten et al. sentence already in the introduction (l. 201–205), which is also an illustration of the mechanism and not a level-truncation match; Cheung–Remmen's auxiliary field is, like theirs, rank three with an invertible kernel, here algebraic rather than $\Box$.
Verdict: holds.

## 4. Nützi–Reiterer (arXiv:1812.06454)

Read: arXiv:1812.06454, abstract, sec. 1, sec. 5 (Thm. 5.1, Def. 5.5, Prop. 5.6, 5.7).

(4.1) What it contains.
They formulate YM and GR about Minkowski space as differential graded Lie algebras whose Maurer–Cartan equations $du + \tfrac12 [u, u] = 0$ are the field equations, and define tree amplitudes as the $L_\infty$ minimal-model brackets, sums of trivalent trees (sec. 1, footnote 9: "By contrast, the Einstein–Hilbert Lagrangian for GR is not polynomial").
For GR, the dgLa is $(\Omega \otimes \mathfrak v)/I$ with $\mathfrak v = \mathbb C^4 \oplus \mathfrak{so}_{1,3}$ (a direct sum, "not the Lie algebra of the Poincaré group"), $\Omega = C^\infty \otimes \wedge \mathbb C^4$, whose degree-one elements are a frame and a Lorentz connection; the MC equation gives Ricci-flat metrics for real elements with a non-degenerate frame (Prop. 5.6, Def. 5.5; their ref. [11] for details).
The differential and bracket are constant-coefficient first-order differential operators, and the graded dimensions are $(10, 40, 50, 24, 4)$ in degrees $0, \dots, 4$.

(4.2) What it is not.
It is a strict formulation of the field equations, not of an action: a cyclic pairing of the kind a classical BV action requires would pair fields with equations (degree 1 with 2) and gauge parameters with Noether identities (0 with 3), and $40 \ne 50$, $10 \ne 24$.
The authors say they omit the proof that their amplitudes coincide with those of the Einstein–Hilbert Feynman rules (sec. 1).
Its variables are first-order (frame and connection, Cartan's formulation), so the cubic bracket comes from first-order variables, as in Cheung–Remmen's unshifted form, not from an auxiliary field replacing a composite.
There is no string theory and no level truncation in it.

(4.3) Bearing on the match.
GR's field equations are the Maurer–Cartan equation of a dgLa, i.e. GR is strictified at the level of equations.
It contains no cubic action for gravity, so it does not change the verdict on (a) or (b); it is a second instance of (c), at the level of equations rather than of an action.
If the paper ever cites a strictification of GR, this one and Cheung–Remmen's are the two natural references, one for the equations and one for the action.

## 5. Overall verdict

The cubic closed SFT cannot be matched to Cheung–Remmen's cubic gravity action in level truncation.
The obstruction is invariant: every finite level truncation of closed SFT lifts, at quartic order, the constant-metric direction that Einstein–Hilbert keeps exactly flat, the flatness being restored only by the exchanges of all massive fields (Yang–Zwiebach 2005; the project's own dilaton instance, R64 (iv)), and the Hubbard–Stratonovich step does not change this because its elimination is exact at quartic order (R64 (i)).
What the two do share is a mechanism: after a local linear shift of its auxiliary field, Cheung–Remmen's action is a Hubbard–Stratonovich rewriting of the quartic Einstein–Hilbert vertex, with a local auxiliary field, a constant non-degenerate indefinite kernel and a linear coupling to a bilinear composite, and the paper's quartic step applied to that vertex gives the same field and the same quartic-order action; but in the string field theory this mechanism acts on the elementary quartic vertex, not on the effective quartic coupling of the massless fields that the Einstein–Hilbert term represents.
By the criterion recorded on 2026-10-12, the paper does not cite Cheung–Remmen.
If the criterion is reconsidered, a citation in the register of the Borsten et al. sentence could rest only on the mechanism statement above, scoped to the Einstein–Hilbert action and to quartic order, and should not suggest that the string field theory reduces to it.

## Proposed ledger entries

None: the brief plans no ledger promotion (citation decision only).

## Status

Complete (2026-10-12): notions (a)–(c), Nützi–Reiterer, verdict; script 12/12 PASS. Next: none (critic review optional, stakes moderate).
