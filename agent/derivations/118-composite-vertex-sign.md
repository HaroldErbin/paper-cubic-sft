---
description: Sign rule of the composite vertices in the reduced vertices $\mathcal W_n$ – uniform minus sign with positive coefficient for every exchange diagram of the cubic theory (nodes = reduced vertices), diagram-dependent sign only after re-expansion in elementary vertices, first positive elementary term at $n = 7$ (the chain, $+\tfrac{42}{25}$)
---

# 118 – Sign of the composite vertices in the reduced vertices

## Status

Status: done – fix pass 1 applied (critic 118).

## Task and objective

**Literal task.** Determine whether the composite vertices subtracted from $\mathcal V_n$ to form the reduced vertex $\mathcal W_n$ (the paper's `\dvertex{n}`) enter with a minus sign at every order and for every diagram, or whether the sign depends on the diagram; state the rule, its scope, and the first order at which a positive composite term appears.

**Motivating objective.** Review comment at `paper/sections/06-worldsheet.tex:487`: a uniform minus sign would support the covering conjecture (the region of $\mathcal W_n$ is $\mathcal V_{0,n}$ minus the regions covered by the auxiliary exchanges) and should then be said in one sentence of that subsection.

## Conventions and assumptions

Notation of the paper (`paper/cubic-closed-sft.tex:234–240`): $\mathcal V_n$ = `\vertex{n}` the string vertex, $\mathcal W_n$ = `\dvertex{n}` the reduced vertex, $p_{m,n}$ = `\sprod{m}{n}`, $w_{k,k}$ = `\wprod{k}{k}`, $\widetilde S_{\le n}$ = `\caction[\le n]` the cubic action, $k^{(n)}_{k,k;\Psi}$ the dressed kinetic operators. Composite vertices $\mathcal V_{5 \cdot 5}$, $\mathcal V_{5 \cdot 5 \cdot 5}$, $\mathcal V_{6 \cdot 5}$ as in eqs. `hs5:exchange-vertex`, `hs7:S1`, `hs7:S2`.

- **A1** Tree level, formal power series in $g_s$, kernel conditions of section 3 assumed (brief; the paper's own assumptions at the head of section 3).
- **A2** Physical ghost number: $N_{\rm gh}(\Psi) = 2$, $N_{\rm gh}(\Sigma_k) = 2k$; all fields entering the elimination are Grassmann-even, so no Koszul sign appears in the tree expansion on these arguments (the project conventions).
- **A3** The coefficients of the paper's displays are taken as given: `hs6:dressed-vertex`, `hs7:dressed-vertex`, `hs7:diagonal`, `hs7:induced`, `hs5:eliminate`, `all:diagonal`, `all:nested`, `all:truncation` (lines 109–113 of `03-all-orders.tex`). This record reads signs off them and explains them; it does not re-derive the values $\tfrac65$, $\tfrac{42}{25}$, $\tfrac{14}{5}$ (ledger R25 (2)–(3) and derivation 018 do; R49 is the $\chi$ scheme with elementary vertices, a different action, and is not a cross-check of these numbers).
  Distinct trees with reduced nodes are taken to evaluate to independent forms, as the paper assumes for the string vertices (`02-5-septic.tex:262`, "which we assume for the string vertices as at the sextic order"); this is what makes "every composite term" and "the coefficient of $T$" well defined as terms.

No hypothesis is needed: the result is a statement about the algebraic structure of the elimination under A1–A3.

## Claim tree

- **A1**, **A2**, **A3** as above.
- **C1** In the basis of the diagrams of the cubic theory (tree diagrams with $\Sigma_k$ propagators and the reduced vertices $\mathcal W_m$, $m < n$, at the nodes), every composite term of $\mathcal W_n(\Psi^n)$ enters with a minus sign and a positive coefficient, at every order $n \ge 6$. [by C1.1–C1.3]
  - **C1.1** The leading-order value of every reduced vertex is $\mathcal W_n(\Psi^n) = \mathcal V_n(\Psi^n) - n! \, [g_s^{n-2}] \, \widetilde S_{\le n-1}|_{\rm sol}$ (one subtraction of everything the lower orders induce). [cited: paper eq. `all:diagonal`, `hs7:deficit`]
  - **C1.2** The on-shell value $\widetilde S_{\le n-1}|_{\rm sol}$ is a sum over tree diagrams with positive coefficients: in the triangular action every kinetic term is $- \tfrac{g_s^{2k-2}}{(2k)!} \mathcal W_{2k}(\Sigma_k, \Sigma_k)$ and every odd coupling enters with a positive coefficient (the sources enter linearly and come twice per $\Sigma_k$ chain, its two 1-valent ends, so their sign drops out), so the Feynman rules of the saddle-point value have propagators $(w_{k,k})^{-1}$ (positive), vertex factors the reduced vertices with positive coefficients, and no sign per diagram. [by A1, A2; block: tree-expansion] [check: toy model, eq. (T.3)]
  - **C1.3** The dressed operators `all:nested` carry every dressing with a minus sign, so their inverses (Neumann series) carry every term with a plus sign: this is C1.2 read on the paper's own closed forms, and it reproduces `hs5:identity`, `hs7:closed-form`, `hs7:induced`. [cited: paper eqs. `all:nested`, `hs5:identity`, `hs7:closed-form`; by C1.2]
- **C2** Re-expanded in elementary string vertices, the sign of a composite diagram depends on the diagram: the sign is $(-1)^{1 + r}$ where $r$ is the number of reductions applied to the nodes, summed over the ways the elementary diagram arises; the first positive elementary composite term is the chain $+ \tfrac{42}{25} \mathcal V_{5 \cdot 5 \cdot 5}(\Psi^7)$ in $\mathcal W_7$, from $- \tfrac{42}{25} + \tfrac{14}{5} \cdot \tfrac{6}{5} = + \tfrac{42}{25}$. [by C1, A3; eq. (R.2), (R.3)] [check: rational identities]
- **C3** The reality signs of appendix B ($\Sigma_k^\star = (-1)^k \Sigma_k$) and the exchange sign of the pairing are conditions on the fields and graded symmetries, not coefficients of the action: every composite term has a real rational coefficient and they do not enter C1–C2. [by A2; cited: paper eqs. `rea:cubic-real`, `rea:exchange-n`; septic reality statement `02-5-septic.tex:342`]
- **C4** The reading of `03-all-orders.tex:414` and of the caption of `fig:all:reduced-vertex` ("$\mathcal W_7$ subtracts $\mathcal V_{5 \cdot 5 \cdot 5}$ and $\mathcal V_{6 \cdot 5}$") is exact only when the nodes of the subtracted diagrams are the reduced vertices ($\mathcal W_6 \cdot \mathcal V_5$, not $\mathcal V_{6 \cdot 5}$); with elementary nodes the chain is added. [by C2]

Open gaps: none
Hypotheses in force: none

## Table of composite terms

Sign of the subtraction = sign of the term in $\mathcal W_n$ when the diagram is written with the cubic theory's own vertices (reduced nodes); sign of the coefficient = sign in the paper's display, which uses elementary nodes.

| Order | Diagram (elementary nodes) | Coefficient in $\mathcal W_n(\Psi^n)$ (display) | Same diagram, reduced nodes | Coefficient | Source |
|---|---|---|---|---|---|
| 6 | $\mathcal V_{5 \cdot 5}$: $\mathcal V_5 - \Sigma_2 - \mathcal V_5$ | $- \tfrac{6}{5}$ | identical ($\mathcal W_5 = \mathcal V_5$) | $- \tfrac{6}{5}$ | `hs6:dressed-vertex`, `hs6:remainder`; induced $+ \tfrac{g_s^4}{600}\mathcal V_{5 \cdot 5}$ in `hs5:eliminate`, $\tfrac{6!}{600} = \tfrac{6}{5}$ |
| 7 | $\mathcal V_{6 \cdot 5}$: $\mathcal V_6 - \Sigma_2 - \mathcal V_5$ | $- \tfrac{14}{5}$ | $\mathcal W_6 \cdot \mathcal V_5 := \mathcal W_6(\Psi^4, p_{2,2}^{-1} p_{3,2} \Psi^3) = \mathcal V_{6 \cdot 5} - \tfrac65 \mathcal V_{5 \cdot 5 \cdot 5}$ | $- \tfrac{14}{5}$ | `hs7:dressed-vertex`, `hs7:diagonal`; induced $+ \tfrac{g_s^5}{1800} (\mathcal W_6 \cdot \mathcal V_5)$ (cross term, `02-5-septic.tex:109–110`), $\tfrac{7!}{1800} = \tfrac{14}{5}$ |
| 7 | $\mathcal V_{5 \cdot 5 \cdot 5}$: chain of three $\mathcal V_5$, two $\Sigma_2$ lines | $+ \tfrac{42}{25}$ | identical | $- \tfrac{42}{25}$ | `hs7:dressed-vertex`; induced $+ \tfrac{g_s^5}{3000} \mathcal V_{5 \cdot 5 \cdot 5}$ (Neumann term, `02-5-septic.tex:105`), $\tfrac{7!}{3000} = \tfrac{42}{25}$ |
| $n \ge 8$ | every tree of the cubic theory at order $g_s^{n-2}$ with reduced nodes | not written in the paper | itself | $- c_T$, $c_T > 0$ | `all:diagonal` with C1.2; the induced term is $+ \sum_T c_T \, T$ |

Elementary-basis bookkeeping at order 7: $\mathcal W_7(\Psi^7) = \mathcal V_7 - \tfrac{42}{25}\mathcal V_{5 \cdot 5 \cdot 5} - \tfrac{14}{5}(\mathcal V_{6 \cdot 5} - \tfrac65 \mathcal V_{5 \cdot 5 \cdot 5}) = \mathcal V_7 + \tfrac{42}{25}\mathcal V_{5 \cdot 5 \cdot 5} - \tfrac{14}{5}\mathcal V_{6 \cdot 5}$, which is `hs7:diagonal`.

## Derivation: tree expansion of the eliminated action

\subsection*{Setup}
A1–A3. The triangular cubic action truncated at level $K$ (paper eq. `all:truncation`, `03-all-orders.tex:105–115`), with $\Sigma_1 := \Psi$:
$$
\widetilde S_{\le 2K+1} = S_{\le 3}(\Psi) + \sum_{k=2}^{K} \Big[ - \frac{g_s^{2k-2}}{(2k)!} \, \mathcal W_{2k}(\Sigma_k, \Sigma_k) + \frac{2 g_s^{2k-2}}{(2k)!} \, \mathcal W_{2k}(\Psi \otimes \Sigma_{k-1}, \Sigma_k) + \frac{g_s^{2k-1}}{(2k+1)!} \, \mathcal W_{2k+1}(\Sigma_k, \Sigma_k, \Psi) \Big]. \tag{T.1}
$$
Write $a_k := g_s^{2k-2}/(2k)!$, $b_k := g_s^{2k-1}/(2k+1)!$, both positive, and $\mathcal W_{2k}(A, B) = \langle A, w_{k,k} B \rangle_k$ (paper `all:kinetic`, line 139), $w_{k,k}$ the bare kinetic operator.

\subsection*{Derivation}
Each $\Sigma_k$ appears in (T.1) only through $-\tfrac{a_k}{2} \cdot 2 \langle \Sigma_k, w_{k,k} \Sigma_k \rangle$, a linear source and the odd vertex. Writing $U_k(\Sigma_k) := 2 a_k \, \mathcal W_{2k}(\Psi \otimes \Sigma_{k-1}, \Sigma_k) + b_k \, \mathcal W_{2k+1}(\Sigma_k, \Sigma_k, \Psi)$, the $\Sigma_k$-dependent part is
$$
F_k(\Sigma_k) = - a_k \, \langle \Sigma_k, w_{k,k} \Sigma_k \rangle + U_k(\Sigma_k), \tag{T.2}
$$
with every coefficient of $U_k$ positive (the vertex values themselves are the "coupling constants"). The stationary value of a functional $- \tfrac12 \langle \Sigma, A \Sigma \rangle + U(\Sigma)$ with $U$ a polynomial is the generating function of connected tree diagrams with propagator $A^{-1}$ and vertex factors the coefficients of $U$, each tree weighted by $+ 1/|\mathrm{Aut}|$: this is the tree-level (leading large-$N$) part of $\log \int e^{N(-\frac12 \Sigma A \Sigma + U)}$, where the Feynman rules of $e^{-\frac12 \Sigma A\Sigma}$ give the propagator $\langle \Sigma \Sigma \rangle = A^{-1}$ and those of $e^{U}$ give the vertex coefficients with no further sign. Applied to (T.2) with $A = 2 a_k w_{k,k}$:
$$
F_k(\Sigma_k^*) = \sum_{\text{trees } T} \frac{1}{|\mathrm{Aut}\, T|} \prod_{\text{edges}} \big( 2 a_k w_{k,k} \big)^{-1} \prod_{\text{nodes}} (\text{coefficient of } U_k), \tag{T.3}
$$
all factors positive. The first term is the exchange $\tfrac{1}{4 a_k} \langle J_k, w_{k,k}^{-1} J_k \rangle$ with $J_k$ the source, the next ones insert the odd vertex $b_k \mathcal W_{2k+1}$ on the propagators; these are exactly the Neumann-series terms of $(k_{k,k;\Psi})^{-1}$, paper eq. `all:nested`, where the dressing enters the operator with a minus sign, $k = w - \tfrac{g_s}{2k+1}\mathcal W_{2k+1} - \tfrac{g_s^2}{(2k+1)(2k+2)}\langle w(\Psi \otimes \cdot), k^{-1} w(\Psi\otimes\cdot)\rangle$, hence the inverse with a plus sign term by term. Eliminating from the top $k = K$ down to $k = 2$ (the triangular structure keeps the action quadratic in the next field, paper section 3.2) composes these expansions: every term of the final $\widetilde S|_{\rm sol} - S_{\le 3}$ is a tree whose nodes are reduced vertices $\mathcal W_m$ (even ones as sources, odd ones as couplings), whose edges are $\Sigma_k$ propagators $w_{k,k}^{-1}$, with a positive rational coefficient $c_T$:
$$
\widetilde S_{\le n-1} \big|_{\rm sol} - S_{\le 3} = \sum_{m=4}^{n-1} \frac{g_s^{m-2}}{m!} \, \mathcal W_m(\Psi^m) + \sum_{T \text{ non-trivial}} c_T \, g_s^{|T|} \, T[\mathcal W_\cdot](\Psi^{\cdots}), \qquad c_T > 0, \tag{T.4}
$$
the single-node trees being the reduced vertices at their leading-order values (each exchange of $\Sigma_k$ between its own source and itself collapses to the contact term $\mathcal W_{2k}(\Psi^{2k})$ with coefficient $a_k$, the "completed square" of the paper). Inserting (T.4) in the matching rule `all:diagonal`, $\mathcal W_n(\Psi^n) = \mathcal V_n(\Psi^n) - n!\,[g_s^{n-2}] \widetilde S_{\le n-1}|_{\rm sol}$, and using that the closure at the lower orders cancels the lower $\mathcal W_m$ against the lower $\mathcal V_m$ (paper `all:closure`):
$$
\boxed{\;\mathcal W_n(\Psi^n) = \mathcal V_n(\Psi^n) - \sum_{T:\ |T| = n-2} n! \, c_T \, T[\mathcal W_\cdot](\Psi^n), \qquad n! \, c_T > 0 .\;} \tag{T.5}
$$

\subsection*{Commentary}
(T.3): standard tree-level Feynman rules for a stationary value; the only sign that could appear per diagram is the sign of the propagator, which is the sign of minus the quadratic coefficient, here $+(2 a_k w_{k,k})^{-1}$ because the paper writes the kinetic term with a minus sign. A2 ensures no Koszul sign on the arguments (all fields even). (T.4): the composition of exchanges across levels is the Neumann-series-inside-Neumann-series structure the paper calls a continued fraction (`03-all-orders.tex:321`). (T.5): the "composite vertices" of the paper are the $T[\mathcal W_\cdot]$ with their nodes at reduced vertices; this is the sense in which the reduced sextic vertex subtracts $\mathcal V_{5 \cdot 5}$ (nodes $\mathcal W_5 = \mathcal V_5$).

\subsection*{Verification of (T.4)–(T.5) on the paper's displays}
Order 6: one tree, $\mathcal V_5 - \Sigma_2 - \mathcal V_5$, $c_T g_s^4 = \tfrac{g_s^4}{600}$ (`hs5:eliminate`, positive), so $\mathcal W_6 = \mathcal V_6 - \tfrac{6!}{600}\mathcal V_{5\cdot5} = \mathcal V_6 - \tfrac65 \mathcal V_{5\cdot5}$: `hs6:dressed-vertex`. Order 7: two trees, the chain $\mathcal V_5 - \Sigma_2 - \mathcal V_5 - \Sigma_2 - \mathcal V_5$ with $c_T g_s^5 = +\tfrac{g_s^5}{3000}$ (Neumann term, `02-5-septic.tex:105`), and $\mathcal W_6 - \Sigma_2 - \mathcal V_5$ with $c_T g_s^5 = +\tfrac{2 g_s^5}{5 \cdot 6!} = \tfrac{g_s^5}{1800}$ (cross term, line 109); both positive. Hence $\mathcal W_7 = \mathcal V_7 - \tfrac{42}{25}\mathcal V_{5\cdot5\cdot5} - \tfrac{14}{5}\,(\mathcal W_6 \cdot \mathcal V_5)$, both subtracted.

## Derivation: re-expansion in elementary vertices

\subsection*{Derivation}
A tree $T[\mathcal W_\cdot]$ with reduced nodes is re-expanded by substituting (T.5) at each node of order $m < n$. Each substitution replaces one node by the elementary vertex (sign $+$) or by one of its subtracted trees (sign $-$), so a term with $r$ nested reductions carries $(-1)^{1+r}$ relative to the elementary diagram's value, and the coefficient of an elementary diagram $D$ in $\mathcal W_n$ is
$$
[D]\,\mathcal W_n(\Psi^n) = - \sum_{(T, \text{reductions}) \to D} (-1)^{r} \, n! \, c_T \prod (\text{reduction coefficients}). \tag{R.1}
$$
Order 7, chain $D = \mathcal V_{5\cdot5\cdot5}$: from the direct chain ($r = 0$) and from $\mathcal W_6 \cdot \mathcal V_5$ with $\mathcal W_6 \to -\tfrac65 \mathcal V_{5\cdot5}$ ($r = 1$):
$$
[\mathcal V_{5\cdot5\cdot5}]\,\mathcal W_7 = - \frac{42}{25} + \frac{14}{5} \cdot \frac{6}{5} = - \frac{42}{25} + \frac{84}{25} = + \frac{42}{25}, \tag{R.2}
$$
$$
[\mathcal V_{6\cdot5}]\,\mathcal W_7 = - \frac{14}{5} \quad (r = 0 \text{ only}). \tag{R.3}
$$
Equivalently at the level of the induced action, $\tfrac{1}{3000} - \tfrac65 \cdot \tfrac{1}{1800} = \tfrac{1}{3000} - \tfrac{1}{1500} = -\tfrac{1}{3000} = -\tfrac15 \cdot \tfrac{1}{600}$, the chain coefficient of `hs7:induced`. The sign of the chain flips because the nested contribution is twice the direct one.

\subsection*{Commentary}
(R.1) is an inclusion–exclusion: the elementary basis counts a sub-diagram once for every reduced node that contains it. No uniform sign rule exists in that basis; the chain at $n = 7$ is the first elementary composite with a positive coefficient, and there is no earlier candidate since $\mathcal W_6$ has a single composite term with $\mathcal W_5 = \mathcal V_5$ (no nesting possible before $n = 7$). The paper's phrase "$\mathcal W_7$ subtracts $\mathcal V_{5\cdot5\cdot5}$ and $\mathcal V_{6\cdot5}$" (`03-all-orders.tex:414`, caption of `fig:all:reduced-vertex`) is exact for the trees with reduced nodes and inexact for the elementary chain (C4).

## Reality signs

Appendix B gives two kinds of sign: the exchange sign of the pairings (`rea:exchange-general`, `rea:exchange-n`), which is a graded symmetry of the forms, and the star-parities $\Psi^\star = -\Psi$, $\Sigma_k^\star = (-1)^k \Sigma_k$ (`rea:cubic-real`), which are conditions on the fields that make every term of the cubic action real. Neither is a coefficient: on the Grassmann-even arguments of the elimination (A2) the forms are symmetric without sign, and the paper states the septic term real with its rational coefficients (`02-5-septic.tex:342`). The odd-$k$ reality sign $\Sigma_3^\star = -\Sigma_3$ therefore does not flip the sign of any composite term; the only signs in $\mathcal W_n$ are the uniform minus of (T.5) and the inclusion–exclusion signs of (R.1). This separates the brief's two signs: the combinatorial sign is always a subtraction; the sign of the displayed coefficient is a basis artefact, not a parity or reality effect.

## Result

**Rule.** For every $n \ge 6$, $\mathcal W_n(\Psi^n) = \mathcal V_n(\Psi^n) - \sum_T n!\,c_T\,T$, where $T$ runs over the tree diagrams of the cubic theory at order $g_s^{n-2}$ with $n$ external $\Psi$ – $\Sigma_k$ propagators $w_{k,k}^{-1}$ joining reduced vertices $\mathcal W_m$, $m < n$ – and every $c_T$ is a positive rational (T.5). In this basis every composite vertex enters with a minus sign and a positive coefficient, at every order and for every diagram; no positive composite term ever appears. The sign is fixed by the sign of the quadratic form of each auxiliary field, negative in the same-sign tower of `eq:all:action`, which makes every propagator of the eliminated action positive; the odd couplings enter with positive coefficients (the sign of the sources drops out, each $\Sigma_k$ chain having two source ends); no parity or reality sign enters (C3).

**Scope.** Tree level, formal power series, kernel conditions (A1); the statement is about leading-order values $\mathcal W_n(\Psi^n)$, which is where the paper defines the reduced vertices at all orders (`all:diagonal`); the off-diagonal forms built from diagrams ($n = 6, 7$ in the paper) inherit the same signs since they are the polarizations of the same diagrams.
The rule is a property of the same-sign tower of `eq:all:action`, in which every auxiliary field has a negative quadratic form.
It does not apply to the partner-field construction of appendix `app:wrong-sign` (`02-4-sextic.tex:30`), a second 2-string field with the opposite-sign quadratic form, where the induced exchange terms are cancelled by the exchange of that field, the vertices stay elementary, and the composite terms are produced with the opposite sign by construction.

**Elementary basis.** Re-expanded in string vertices $\mathcal V_m$ at the nodes, the sign depends on the diagram by inclusion–exclusion (R.1): the chain $\mathcal V_{5\cdot5\cdot5}$ in $\mathcal W_7$ carries $+\tfrac{42}{25}$ (R.2), the first and, at $n \le 7$, only positive elementary composite term; $\mathcal V_{6 \cdot 5}$ carries $-\tfrac{14}{5}$ (R.3), a plain subtraction. The ledger entry R25 (2)–(3) gives the same induced action, $A_5^{\rm dr} = \tfrac{1}{600}[\tfrac13 S_2 - \tfrac15 S_1] = \tfrac{1}{1800} S_2 - \tfrac{1}{3000} S_1$, and the forced triple $(1, \tfrac{42}{25}, -\tfrac{14}{5})$ on $(V_7, \tilde A_{S_1}, \tilde A_{S_2})$, identical to `hs7:diagonal` and to (R.2)–(R.3).

**Reading for the covering conjecture.** The natural basis for a region reading is the one with reduced nodes: the cubic theory has no $\mathcal V_6$ vertex, only $\mathcal W_6$, so the Feynman regions it can cover are those of its own diagrams, plumbings of the reduced-vertex regions. In that basis the sign is uniformly negative, which is what "the composite terms are the regions subtracted from $\mathcal V_{0,n}$" requires; the positive elementary chain is the inclusion–exclusion count of a sub-region contained in a larger subtracted region. What the signs do not settle is the weights: the direct chain and the chain nested in $\mathcal W_6 \cdot \mathcal V_5$ come with $\tfrac{42}{25}$ and $\tfrac{84}{25}$, so if the two are one and the same region of moduli space it is counted with different multiplicities by the two trees, which is the "constant weight" question the paragraph already leaves open and is outside this record.

## Proposed sentence for the paper

For `06-worldsheet.tex`, after the sentence "For example, at the lower order, the reduced sextic vertex~\eqref{eq:hs6:dressed-vertex} is the sextic vertex minus the composite vertex, $\dvertex{6} = \vertex{6} - \tfrac{6}{5} \vertex{5 \cdot 5}$." (line 490):

```latex
The sign is general: by~\eqref{eq:all:diagonal}, $\dvertex{n}(\Psi^n)$ is $\vertex{n}(\Psi^n)$ minus every tree diagram of the cubic action of the previous order, $\caction[\le n - 1]$, at order $\gs^{n - 2}$, the exchanges of the auxiliary fields between the lower reduced vertices, and each diagram comes with a positive coefficient, since the kinetic term of every auxiliary field carries a minus sign and its odd couplings a plus sign, so that the elimination produces every exchange with a positive weight.
The exchange diagrams, with the reduced vertices at their nodes, are thus always subtracted, which supports the reading of each of them as a region removed from $\mathcal V_{0, n}$; when the diagrams are rewritten with the string vertices at their nodes the sign depends on the diagram, as the chain term $+ \tfrac{42}{25} \vertex{5 \cdot 5 \cdot 5}$ of~\eqref{eq:hs7:diagonal} shows, because a diagram nested in a reduced vertex is counted once more with the opposite sign.
```

Optional precision for `03-all-orders.tex:414` and the caption of `fig:all:reduced-vertex` (same fact, writer's choice): "as $\dvertex{7}$ subtracts $\vertex{5 \cdot 5 \cdot 5}$ and the diagram $\dvertex{6} \cdot \vertex{5}$, whose reduced node turns the sign of the chain in~\eqref{eq:hs7:diagonal}".
The same qualification, "with the reduced vertices at their nodes", applies wherever the paper says that $\dvertex{n}$ "subtracts" the composite vertices (`03-all-orders.tex:414`, caption at `:464`), since with elementary nodes the term $\vertex{5 \cdot 5 \cdot 5}$ of `eq:hs7:diagonal` is added.

## Checks

Run on 2026-11-09 with `uv run --no-sync python -c …` from the project root (sympy; no companion script, per the brief's `Resources: none`; the brief allows no file under `agent/computations/`).

- **Rational identities (C2, table).** $6!/600 = 6/5$, $7!/1800 = 14/5$, $7!/3000 = 42/25$; chain net $-\tfrac{42}{25} + \tfrac{14}{5}\cdot\tfrac65 = +\tfrac{42}{25}$; induced-action level $\tfrac{1}{3000} - \tfrac{1}{1500} = -\tfrac{1}{3000} = \tfrac15 \cdot \tfrac{1}{600}$; cross-term prefactor $\tfrac{2}{5 \cdot 6!} = \tfrac{1}{1800}$ and $\tfrac{1}{3} \cdot \tfrac{1}{600} = \tfrac{1}{1800}$. All PASS (exact arithmetic). Falsifiable: any transcription error in a display coefficient breaks an equality.
- **Toy model for (T.3)–(T.4) (C1.2).** Two-level triangular scalar action $F = -\tfrac12 w_2 s_2^2 + j s_2 + g v_5 s_2^2 - \tfrac12 w_3 s_3^2 + g\, w_3 s_3 s_2 + g W_7 s_3^2 + g^2 W_8 s_3^2$ with positive symbols; eliminate $s_3$ then $s_2$ exactly, expand to $O(g^3)$: every monomial of the stationary value has a positive coefficient ($j^2/2w_2$, $j^2 v_5/w_2^2$, $j^2(4v_5^2 + w_2 w_3)/2w_2^3$, $j^2(W_7 w_2^2 + 4 v_5^3 + 2 v_5 w_2 w_3)/w_2^4$). PASS. **Break:** flipping the odd coupling $W_7 \to -W_7$ produces negative monomials – the check detects a sign in the couplings. The toy model establishes the sign structure of the elimination (kind: representation of the commutative algebra), not the string-vertex values.
- **Consistency with the paper's displays.** (T.5) reproduces `hs6:dressed-vertex` and `hs7:diagonal` from `hs5:eliminate`, `02-5-septic.tex:105,109–110` (section *Verification of (T.4)–(T.5)* above). PASS by exact arithmetic.
- Not checked: the values of $c_T$ at $n \ge 8$ (not written in the paper; only their positivity is claimed, by (T.3)); the sign of the individual elementary terms at $n \ge 8$ (the general formula (R.1) is used only at $n = 7$; positive elementary terms are expected there whenever the nested count exceeds the direct one, but this is not computed); the region/weight interpretation (outside scope).

### Check code (fix pass 1)

The one-liners of the first run were not saved; the block below is a rewrite of the same two checks, re-run on 2026-11-09 with `uv run --no-sync python -c "…"` from the project root (output: `rational PASS`; the toy series reproduces the four monomials above, and with `-W7` the $O(g^3)$ coefficient contains $-W_7 w_2^2$, the break leg).

```python
import sympy as sp
from sympy import Rational as R, factorial as f

# rational identities (C2, table)
assert f(6) / 600 == R(6, 5) and f(7) / 1800 == R(14, 5) and f(7) / 3000 == R(42, 25)
assert -R(42, 25) + R(14, 5) * R(6, 5) == R(42, 25)
assert R(1, 3000) - R(6, 5) * R(1, 1800) == -R(1, 3000) == -R(1, 5) * R(1, 600)
assert R(2, 5 * 720) == R(1, 1800) == R(1, 3) * R(1, 600)
print("rational PASS")

# two-level toy elimination (C1.2); all symbols positive
g, j, w2, w3, v5, W7, W8, s2, s3 = sp.symbols("g j w2 w3 v5 W7 W8 s2 s3", positive=True)


def stationary_series(W7s):
    F = (
        -w2 * s2**2 / 2 + j * s2 + g * v5 * s2**2
        - w3 * s3**2 / 2 + g * w3 * s3 * s2 + g * W7s * s3**2 + g**2 * W8 * s3**2
    )
    s3s = sp.solve(sp.diff(F, s3), s3)[0]
    F2 = sp.simplify(F.subs(s3, s3s))
    s2s = sp.solve(sp.diff(F2, s2), s2)[0]
    return sp.expand(sp.series(F2.subs(s2, s2s), g, 0, 4).removeO())


for sgn in (1, -1):  # sgn = -1 is the break leg
    ser = stationary_series(sgn * W7)
    print(sgn, [sp.factor(ser.coeff(g, k)) for k in range(4)])
```

## Proposed ledger entries

Ledger section: ## Results

### R? — Composite vertices enter every reduced vertex with a minus sign and a positive coefficient in the diagram basis of the cubic theory; the sign depends on the diagram only after re-expansion in elementary vertices (first positive term at $n = 7$) [Proven]
Promoted as R114 (2026-11-09).

- **Source**: `agent/derivations/118-composite-vertex-sign.md`, claim tree C1–C4, eqs. (T.5), (R.1)–(R.3)
- **Scope**: tree level, formal power series in $g_s$, kernel conditions of section 3 (A1); leading-order values $\mathcal W_n(\Psi^n)$ for all $n \ge 6$; coefficients of the paper's displays taken as given (A3)
- **Verification**:
  - 2026-11-09 – symbolic check – sympy one-liner (no companion script, brief `Resources: none`) – rational identities $6!/600$, $7!/1800$, $7!/3000$ and chain net $+\tfrac{42}{25}$ PASS; two-level toy elimination: all stationary-value monomials positive to $O(g^3)$ PASS, break leg ($W_7 \to -W_7$) fires

**Statement.** $\mathcal W_n(\Psi^n) = \mathcal V_n(\Psi^n) - \sum_T n!\,c_T\,T$, the sum over tree diagrams of $\widetilde S_{\le n-1}$ at order $g_s^{n-2}$ with the reduced vertices at their nodes and $\Sigma_k$ propagators (the exchange diagrams are subtracted only in this reading: with elementary vertices at the nodes the "composite vertex" $\mathcal V_{5\cdot5\cdot5}$ is added, below), $c_T > 0$ for every $T$: the sign is that of the auxiliary quadratic forms (negative), which makes every propagator of the eliminated action positive, while the odd couplings are positive (the sign of the sources drops out); reality and parity signs do not enter. In the elementary basis the coefficient is an inclusion–exclusion sum, and the chain $\mathcal V_{5\cdot5\cdot5}$ in $\mathcal W_7$ carries $+\tfrac{42}{25} = -\tfrac{42}{25} + \tfrac{14}{5}\cdot\tfrac65$, the first positive elementary composite term; $\mathcal V_{6\cdot5}$ carries $-\tfrac{14}{5}$. Consistent with R25 (2)–(3): the induced action $\tfrac{1}{1800} S_2 - \tfrac{1}{3000} S_1$ and the forced triple $(1, \tfrac{42}{25}, -\tfrac{14}{5})$.
