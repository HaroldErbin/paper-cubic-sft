---
description: The dressed kinetic operator k_{k,k;Psi} does receive Psi-only (non-linear in Psi) corrections from eliminating the higher auxiliary fields, from relative order g_s^2 on; the truncated operator k^{(n)} agrees with the full one up to O(g_s^{n-2k+3}); the label stays on truncated operators (section 2) and is absent on the full-tower operator (section 3), with the rule stated once.
---

# 117 – Order label on the dressed kinetic operator $k_{k,k;\Psi}$

## Status

Done – fix pass 1 applied (critic 117). Occurrence table, steps 1–4, script 7/7 PASS (break legs fail as intended). No ledger entry proposed; a decision entry is suggested in the report. Nothing pending.

Fix pass 1 (2026-11-09, critic 117, verdict accept with minor fixes): changed the statement of C2 (domain $n \ge 2k-2$) and of the claim C3 (one exception, line 322) and C4 (unchanged content); other changes are wording (A3 index convention, line counts, `Sym^k`), the Checks scope notes, and the two proposed paper sentences. Dependents: C4 rests on C2 and C3 and still holds; the claim tree has no other dependents; the script is unchanged.

## Task and objective

- **Literal task.** Settle whether the dressed kinetic operator of $\Sigma_k$ receives corrections depending only on $\Psi$ when $\Sigma_{k+1}, \Sigma_{k+2}, \dots$ are eliminated, so that an order label is needed; propose one convention for sections 2 and 3.
- **Objective.** Answer the review comments at `paper/sections/02-3-quintic.tex:131` and `paper/sections/03-all-orders.tex:340` (consistency of the label; whether to change the letter $k$), in the final round of the paper: a notation rule and the list of displays to change.
- **Already settled.** The bare operator $w_{k,k}$ carries no label (`knowledge/decisions.md` 2026-11-07, record 115, node N4 of which already states that the dressed operators differ by $\Psi$-dependent exchange terms at $O(g_s^2)$ depending on the truncation). This record works it out explicitly, as the brief asks, and settles the notation.

## Conventions and assumptions

- The project `knowledge/conventions.md` applies; nothing here fixes a new convention.
- A1. The all-orders cubic action is `eq:all:action` of `paper/sections/03-all-orders.tex`: for each $k \ge 2$, a kinetic term $- a_k \langle \Sigma_k, w_{k,k}(\Sigma_k) \rangle_k$, a source $2 a_k \langle \Sigma_k, w_{k,k}(\Psi \otimes \Sigma_{k-1}) \rangle_k$ and an odd coupling $b_k \mathcal W_{2k+1}(\Sigma_k, \Sigma_k, \Psi)$, with $a_k = g_s^{2k-2}/(2k)!$, $b_k = g_s^{2k-1}/(2k+1)!$, $\Sigma_1 := \Psi$. Tree level, formal power series in $g_s$.
- A2. The pairings are symmetric and the kernel conditions of section 3.6 hold, so that every operator met here descends to the quotient of its bare operator and $w_{k,k}$ is invertible there; inverses of dressed operators are Neumann series in $g_s$ (`eq:hs5:neumann`).
- A3. The *truncation at order $g_s^n$* means the action of section 2 truncated at the power $g_s^n$ of the coupling. Index convention, stated once: in this record $n$ is the power of $g_s$, whereas the paper's `\caction[\le n]` $= \widetilde S_{\le n}$ is indexed by the vertex order, so that the action truncated at $g_s^n$ is the paper's $\widetilde S_{\le n+2}$ (the sextic action, $n = 4$, is $\widetilde S_{\le 6}$; $\widetilde S_{\le 2K+1}$ holds $\Sigma_2, \dots, \Sigma_K$, i.e. order $g_s^{2K-1}$). The superscript of `\kin{k}{\Psi}{n}` is the $g_s$ power in the paper as well, and any sentence proposed for the paper uses "the action truncated at order $\gs^n$", never the symbol $\widetilde S_{\le n}$. For $n = 2K - 1$ the tower is $\Sigma_2, \dots, \Sigma_K$ with the odd coupling of $\Sigma_K$ included; for $n = 2K$ the tower is $\Sigma_2, \dots, \Sigma_{K+1}$ with $\Sigma_{K+1}$ carrying its bare operator and source only (the sextic order: $\Sigma_3$ with $w_{3,3}$ and no $\mathcal W_7$).
- Notation of this record: $k^{(n)}_{k,k;\Psi}$ is the quadratic form of $\Sigma_k$ in the action truncated at $g_s^n$ (the paper's $\widetilde S_{\le n+2}$, see A3) once $\Sigma_{k+1}, \dots$ are eliminated (what the paper writes `\kin{k}{\Psi}{n}`); $k_{k,k;\Psi}$ without label is the same for the full tower (`eq:all:nested`).

## Claim tree

- **A1–A3** as above.
- **C1** For $k = 2$, the dressed operator receives corrections that depend only on $\Psi$ and are not linear in it, from the elimination of $\Sigma_3$: $k^{(4)}_{2,2;\Psi} - k^{(3)}_{2,2;\Psi} = - \tfrac{g_s^2}{30} \mathcal W_6(\Psi \otimes \cdot, \Psi \otimes \cdot)$, quadratic in $\Psi$; at order $g_s^3$ and $g_s^4$ the septic truncation adds terms cubic and quartic in $\Psi$, and the octic truncation adds a further quartic term. [by C1.1–C1.4]
  - **C1.1** Quintic order: $k^{(3)}_{2,2;\Psi} = p_{2,2} - \tfrac{g_s}{5} p_{3,2}(\Psi, \cdot)$, affine in $\Psi$. [cited: `eq:hs5:dressed`]
  - **C1.2** Sextic order: $k^{(4)}_{2,2;\Psi} = k^{(3)}_{2,2;\Psi} - \tfrac{g_s^2}{30} \mathcal W_6(\Psi \otimes \cdot, \Psi \otimes \cdot)$, exactly in $g_s$, quadratic in $\Psi$, from the elimination of $\Sigma_3$. [by A1–A3; eq. (1.2); cited: `eq:hs6:dressed-2`] [check: C1.2]
  - **C1.3** Septic order: $k^{(5)}_{2,2;\Psi}$ has the terms of eq. (1.4) at $g_s^2, g_s^3, g_s^4$, of degree 2, 3, 4 in $\Psi$. [by A1–A3, C1.2; eq. (1.4)] [check: C1.3]
  - **C1.4** Octic order: $k^{(6)}_{2,2;\Psi} - k^{(5)}_{2,2;\Psi} = - \tfrac{g_s^4}{1680} \mathcal W_8(\Psi^2 \otimes \cdot, \Psi^2 \otimes \cdot) + O(g_s^5)$; $k^{(7)} - k^{(6)} = O(g_s^5)$. [by A1–A3, C1.3; eq. (1.5)] [check: C1.4]
- **C2** General $k$ and truncation $n \ge 2k - 2$ (at $n = 2k-2$ the operator is the bare $w_{k,k}$ of the sextic-type truncation, written $w_{k,k}$ by the decision of 2026-11-07, and the order formula holds with the odd vertex as the first correction): $k^{(n)}_{k,k;\Psi} = k_{k,k;\Psi} + O(g_s^{n - 2k + 3})$ as formal power series, with a non-zero leading difference in general (a collapsed chain ending on $\mathcal W_{2K+2}$ or $\mathcal W_{2K+3}$; non-zero when that reduced vertex is non-zero on $\Psi^{K+1-k} \otimes A$, $\Psi^{K+1-k} \otimes B$, and the finite model establishes genericity only); every term of relative order $g_s^m \ge g_s^2$ depends on $\Psi$ only, with degree $m$. The label is needed on a truncated operator and redundant on the full one. [by A1–A3, C1; eqs. (2.1)–(2.3)] [check: C2]
- **C3** The label as the paper uses it – superscript $(n)$ = operator of the action truncated at $g_s^n$, no superscript = full tower – is consistent in every current occurrence except the sentence at `03-all-orders.tex:322`, which writes the unlabelled $k_{K,K;\Psi} = \kin{K}{\Psi}{2K-1}$ for a finite-$K$ object and is rewritten in step 4 (table above); the perceived inconsistency is that the rule is stated once per instance and after `eq:all:nested` only, for odd $n$ only. [by C2; step 3 audit of the occurrence table]
- **C4** Notation: keep the rule (option A), state it at `02-3-quintic.tex:113` and before `eq:all:nested`, change no display; the letter can be changed to $\kappa$ at the cost of one macro line, 13 hand-written lines in `03-all-orders.tex` and the renaming of the section-6 measure constant. [by C2, C3; step 4]

Open gaps: none.
Hypotheses in force: none.

## Occurrence table

Every display or sentence where a dressed operator appears (`rg -n '\\kin\{|k_\{k, k; \\Psi\}|k_\{2, 2; \\Psi\}|k_\{K, K|k_\{k \+ 1'`), 2026-11-09. "Label" is the superscript; $n$ = order of the truncated action.

| File:line | Form | Label | Meaning |
|---|---|---|---|
| `02-3-quintic.tex:106–109` (`eq:hs5:dressed`) | `\kin{2}{\Psi}{3}` | 3 | definition, quintic truncation |
| `02-3-quintic.tex:114, 120, 126, 140, 148, 153, 158–161, 242–277, 412–429, 454, 501–502` | `\kin{2}{\Psi}{3}` | 3 | uses at the quintic order (28 lines, 33 uses in the file) |
| `02-4-sextic.tex:250–254` (`eq:hs6:dressed-2`) | `\kin{2}{\Psi}{4}` and `\kin{2}{\Psi}{3}` | 4, 3 | definition of the sextic operator from the quintic one |
| `02-4-sextic.tex:260, 366, 371` | `\kin{2}{\Psi}{4}` | 4 | solution, gauge law |
| `02-5-septic.tex:30` | `\kin{2}{\Psi}{3}` | 3 | the operator of $\Sigma_2$ in $\widetilde S_{\le 6}$ (paper index) at fixed $\Sigma_3$ (correct: before eliminating $\Sigma_3$) |
| `02-5-septic.tex:45, 48, 63, 67, 74` | `\kin{2}{\Psi}{4}` | 4 | the operator after eliminating $\Sigma_3$ in $\widetilde S_{\le 6}$, and its inverse before `eq:hs7:induced` |
| `02-5-septic.tex:216` (`eq:hs7:dressed-3`), `228, 233, 249, 274, 294, 313, 324–326, 343` | `\kin{3}{\Psi}{5}` | 5 | the dressed operator of $\Sigma_3$ at the septic order |
| `02-5-septic.tex:243` (`eq:hs7:dressed-2`), `252, 314, 330, 333` | `\kin{2}{\Psi}{5}`, `\kin{2}{\Psi}{4}` | 5, 4 | the septic operator of $\Sigma_2$ and its comparison with the sextic one |
| `03-all-orders.tex:157` (`eq:all:dressed-odd`), `178` (`eq:all:blocks`) | `\kin{k}{\Psi}{2 k - 1}` | $2k - 1$ | the operator of $\Sigma_k$ as top field (bare plus odd vertex) |
| `03-all-orders.tex:285, 288, 298` (`eq:all:eom-top`, `eq:all:eliminate-top`) | `\kin{K}{\Psi}{2 K - 1}` | $2K - 1$ | the top field at truncation $K$ |
| `03-all-orders.tex:309, 318` (`eq:all:nested`) | `k_{k, k; \Psi}`, `k_{k + 1, k + 1; \Psi}` | none | definition of the full-tower operator |
| `03-all-orders.tex:322` | `k_{K, K; \Psi} = \kin{K}{\Psi}{2 K - 1}`, `\kin{k}{\Psi}{2 K - 1}`, `\kin{2}{\Psi}{5}`, `\kin{3}{\Psi}{5}` | mixed | the sentence stating the truncation rule |
| `03-all-orders.tex:330` (`eq:hs8:scaling`), `349, 353, 359, 366, 378, 380, 547, 552, 560` | `k_{k, k; \Psi}`, `k_{2, 2; \Psi}` | none | full tower (13 hand-written lines in the file, 309–560) |
| `07b-further-results.tex:15, 26, 28, 63` | `\kin{2}{\Psi}{3}`, `\kin{2}{\Psi^*}{3}` | 3 | quintic-order statements |

Counts (`rg -c`, which counts lines): `\kin{` – quintic 28, sextic 7, septic 21, all-orders 6, further results 4 (66 macro lines, 79 lines with the 13 hand-written ones); hand-written `k_{\cdot, \cdot; \Psi}` – all-orders 13 lines. Use counts (`rg -o`, several uses on one line): `\kin{` – quintic 33, sextic 9, septic 26, all-orders 9, further results 4, i.e. 81 macro uses on 66 lines. Nothing in `A-conventions.tex`, `01-introduction.tex` (words only), `09-discussion.tex` (words only). No `\kin{k}{}{…}` (bare with label) remains, as decided on 2026-11-07.

## Step 1 – The case $k = 2$ order by order

### Setup

A1–A3. Write $O_k := \mathcal W_{2k+1}(\cdot, \cdot, \Psi)$ for the odd vertex as a symmetric operator on $\mathrm{Sym}^k\mathcal H$, $\langle A, O_k B \rangle_k = \mathcal W_{2k+1}(A, B, \Psi)$, and $T_k \colon \mathrm{Sym}^k\mathcal H \to \mathrm{Sym}^{k+1}\mathcal H$, $A \mapsto \Psi \otimes A$. The source of $\Sigma_{k+1}$ is $w_{k+1,k+1} T_k \Sigma_k$. The elimination of a top field with operator $\kappa$ and source $w T A$ produces the exchange $\langle w T A, \kappa^{-1} w T B \rangle$ (`eq:all:eliminate-top`), which is absorbed into the operator of the level below with the coefficient $- g_s^2 / ((2k+1)(2k+2))$ (`eq:all:nested`; for $k = 2$: $- g_s^2/30$, the ratio of $\tfrac{g_s^4}{6!}$ to $\tfrac{g_s^2}{4!}$).

### Derivation

Quintic truncation ($n = 3$, tower $\Sigma_2$ only):
$$
k^{(3)}_{2,2;\Psi} = p_{2,2} - \frac{g_s}{5} O_2 . \tag{1.1}
$$

Sextic truncation ($n = 4$, tower $\Sigma_2, \Sigma_3$, $\Sigma_3$ with bare operator $w_{3,3}$ and source $w_{3,3} T_2 \Sigma_2$, no $\mathcal W_7$): the solution $\Sigma_3^* = w_{3,3}^{-1} w_{3,3} T_2 \Sigma_2 = T_2 \Sigma_2$ on the quotient (`eq:hs6:saddle-sigma3`), and the exchange collapses to the contact term
$$
k^{(4)}_{2,2;\Psi} = p_{2,2} - \frac{g_s}{5} O_2 - \frac{g_s^2}{30} T_2^{\mathsf T} w_{3,3} T_2 , \qquad \langle A, T_2^{\mathsf T} w_{3,3} T_2 B \rangle_2 = \mathcal W_6(\Psi \otimes A, \Psi \otimes B). \tag{1.2}
$$
This is `eq:hs6:dressed-2`. The new term is quadratic in $\Psi$, contains no auxiliary field, and comes from the elimination of $\Sigma_3$: before the elimination, the equation of $\Sigma_2$ at this order contains $\Sigma_3$ and no $\Psi^2$-dressing (`eq:hs6:eom-sigma2`, $+ \tfrac{g_s^2}{30} \mathcal W_6(\Psi \otimes \cdot, \Sigma_3)$); after it, $\Sigma_3 \to \Psi \otimes \Sigma_2$ turns that term into a $\Psi$-only dressing of the operator. Both recollections are correct and compatible: the equation of motion shows the higher field, the eliminated action shows the $\Psi$-only correction.

Septic truncation ($n = 5$, tower $\Sigma_2, \Sigma_3$ with $\mathcal W_7$): the top operator is $k^{(5)}_{3,3;\Psi} = w_{3,3} - \tfrac{g_s}{7} O_3$ (`eq:hs7:dressed-3`), and
$$
k^{(5)}_{2,2;\Psi} = p_{2,2} - \frac{g_s}{5} O_2 - \frac{g_s^2}{30} T_2^{\mathsf T} w_{3,3} \Big( w_{3,3} - \frac{g_s}{7} O_3 \Big)^{-1} w_{3,3} T_2 \tag{1.3}
$$
(`eq:hs7:dressed-2`). With the Neumann series $(w - \tfrac{g_s}{7} O)^{-1} = w^{-1} \sum_{m \ge 0} (\tfrac{g_s}{7} O w^{-1})^m$ and $w w^{-1} = 1$ on the quotient,
$$
\begin{aligned}
k^{(5)}_{2,2;\Psi}
&= p_{2,2} - \frac{g_s}{5} O_2 - \frac{g_s^2}{30} T_2^{\mathsf T} w_{3,3} T_2
 - \frac{g_s^3}{30 \cdot 7} T_2^{\mathsf T} O_3 T_2
 - \frac{g_s^4}{30 \cdot 49} T_2^{\mathsf T} O_3 w_{3,3}^{-1} O_3 T_2
 + O(g_s^5),
\end{aligned} \tag{1.4}
$$
i.e. in vertex form the $g_s^3$ term is $- \tfrac{g_s^3}{210} \mathcal W_7(\Psi \otimes A, \Psi \otimes B, \Psi)$, cubic in $\Psi$, and the $g_s^4$ term is $- \tfrac{g_s^4}{1470} \langle \mathcal W_7(\Psi \otimes A, \cdot, \Psi), w_{3,3}^{-1} \mathcal W_7(\cdot, \Psi \otimes B, \Psi) \rangle_3$, quartic in $\Psi$: a $\Sigma_3$ line between two septic vertices.

Octic truncation ($n = 6$, tower $\Sigma_2, \Sigma_3, \Sigma_4$, $\Sigma_4$ bare): eliminating $\Sigma_4$ dresses $\Sigma_3$ by $- \tfrac{g_s^2}{56} T_3^{\mathsf T} w_{4,4} T_3$ ($\tfrac{g_s^6}{8!} / \tfrac{g_s^4}{6!} = \tfrac{g_s^2}{56}$), so $k^{(6)}_{3,3;\Psi} = w_{3,3} - \tfrac{g_s}{7} O_3 - \tfrac{g_s^2}{56} T_3^{\mathsf T} w_{4,4} T_3$, and inserting it in (1.3) in place of $k^{(5)}_{3,3;\Psi}$,
$$
k^{(6)}_{2,2;\Psi} - k^{(5)}_{2,2;\Psi} = - \frac{g_s^4}{30 \cdot 56} T_2^{\mathsf T} T_3^{\mathsf T} w_{4,4} T_3 T_2 + O(g_s^5)
= - \frac{g_s^4}{1680} \mathcal W_8(\Psi^2 \otimes A, \Psi^2 \otimes B) + O(g_s^5). \tag{1.5}
$$
The two truncations agree through $g_s^3$ and differ at $g_s^4$. Likewise $k^{(7)} - k^{(6)} = - \tfrac{g_s^5}{30 \cdot 56 \cdot 9} T_2^{\mathsf T} T_3^{\mathsf T} O_4 T_3 T_2 + O(g_s^6)$.

### Commentary

- (1.2): the collapse $w_{3,3}^{-1} w_{3,3} = 1$ is the statement after `eq:hs8:scaling` ("the exchange term reduces at order $g_s^2$ to the reduced vertex of the next level"); on the quotient of $\ker w_{3,3}$ it is exact.
- (1.4): the symmetry of $O_3$ and $w_{3,3}$ is used to move $w_{3,3}$ through: $T^{\mathsf T} w\, w^{-1} (O w^{-1})^m w T = T^{\mathsf T} (O w^{-1})^{m-1} O T$.
- The $g_s^4$ term of (1.4) is not in the paper (it sits beyond the septic order in the action, $g_s^2 \cdot g_s^4 = g_s^6$); it is listed to show that the septic operator, exact for $\widetilde S_{\le 7}$, is itself an infinite series whose terms beyond $g_s^3$ are *not* those of the full tower (1.5).

### Result

Table of the terms of $k^{(n)}_{2,2;\Psi}$ by order (coefficient of $g_s^m$ in the operator; the action term is $g_s^{2+m}$):

| $m$ | term | $\Psi$-degree | origin | present in $n =$ |
|---|---|---|---|---|
| 0 | $p_{2,2}$ | 0 | quartic vertex | all |
| 1 | $- \tfrac{1}{5} O_2$ | 1 | quintic vertex | $\ge 3$ |
| 2 | $- \tfrac{1}{30} T_2^{\mathsf T} w_{3,3} T_2 = -\tfrac{1}{30} \mathcal W_6(\Psi \otimes \cdot, \Psi \otimes \cdot)$ | 2 | elimination of $\Sigma_3$ (bare) | $\ge 4$ |
| 3 | $- \tfrac{1}{210} \mathcal W_7(\Psi \otimes \cdot, \Psi \otimes \cdot, \Psi)$ | 3 | $\Sigma_3$ elimination, one $\mathcal W_7$ | $\ge 5$ |
| 4 | $- \tfrac{1}{1470} \langle \mathcal W_7(\Psi \otimes \cdot, \cdot, \Psi), w_{3,3}^{-1} \mathcal W_7(\cdot, \Psi \otimes \cdot, \Psi) \rangle_3$ | 4 | $\Sigma_3$ elimination, two $\mathcal W_7$ | $\ge 5$ |
| 4 | $- \tfrac{1}{1680} \mathcal W_8(\Psi^2 \otimes \cdot, \Psi^2 \otimes \cdot)$ | 4 | elimination of $\Sigma_4$ (bare) through $\Sigma_3$ | $\ge 6$ |

**Answer to the literal question.** Yes: from relative order $g_s^2$ on, the dressed operator of $\Sigma_2$ receives corrections that depend on $\Psi$ only, of degree $m$ in $\Psi$ at order $g_s^m$ (so not linearly), produced by the elimination of the higher fields. The term of order $g_s^m$ of the operator is final only once the action is truncated at order $n \ge m + 1$: $k^{(n)}_{2,2;\Psi}$ and $k^{(n+1)}_{2,2;\Psi}$ first differ at order $g_s^{n-1}$ ($n = 3$: $g_s^2$; $n = 4$: $g_s^3$; $n = 5$: $g_s^4$; $n = 6$: $g_s^5$). The label is therefore necessary on a truncated operator: `\kin{2}{\Psi}{3}`, `\kin{2}{\Psi}{4}`, `\kin{2}{\Psi}{5}` are three different operators, and the display before `eq:hs7:induced` (the inverse of `\kin{2}{\Psi}{4}` with its $O(g_s^2)$ exchange term) needs the $4$ to say which inverse is expanded.

## Step 2 – General $k$ and truncation $n$

### Setup

A1–A3, the operators $O_k$, $T_k$ of step 1. Let $c_k := \tfrac{1}{(2k+1)(2k+2)}$ be the exchange coefficient of `eq:all:nested`.

### Derivation

The recursion `eq:all:nested`, written with the truncation made explicit, is
$$
k^{(n)}_{k,k;\Psi} = w_{k,k} - \frac{g_s}{2k+1} O_k - g_s^2 c_k \, T_k^{\mathsf T} w_{k+1,k+1} \big( k^{(n)}_{k+1,k+1;\Psi} \big)^{-1} w_{k+1,k+1} T_k , \tag{2.1}
$$
with the top of the chain fixed by A3: for $n = 2K - 1$, $k^{(n)}_{K,K;\Psi} = w_{K,K} - \tfrac{g_s}{2K+1} O_K$; for $n = 2K$, $k^{(n)}_{K+1,K+1;\Psi} = w_{K+1,K+1}$. The full-tower operator $k_{k,k;\Psi}$ is (2.1) without a top, as a formal power series in $g_s$ (well defined because each rung costs $g_s^2$: the coefficient of $g_s^m$ involves levels $\le k + \lfloor m/2 \rfloor$ only).

**Triangular-structure argument (second method).** The only way the data of level $l > k$ reach the operator of $\Sigma_k$ is through the chain of $l - k$ exchanges, each of which carries $g_s^2$ and two $\Psi$'s (the two sources $w T$). Hence:

- a term of $k_{k,k;\Psi}$ of relative order $g_s^m$ is a product of $m$ factors of $g_s \Psi$ (`eq:hs8:scaling`): it is a polynomial of degree $m$ in $\Psi$ and contains no auxiliary field, which is the claim that the corrections depend only on $\Psi$ and not only linearly, for every $m \ge 2$;
- the level-$l$ odd vertex $O_l$ first enters $k_{k,k;\Psi}$ at order $g_s^{1 + 2(l-k)}$, and the level-$(l+1)$ bare operator $w_{l+1,l+1}$ (through the exchange of $\Sigma_{l+1}$) at order $g_s^{2(l+1-k)}$.

Passing from the truncation $n$ to $n + 1$ adds exactly one ingredient: for $n = 2K - 1 \to 2K$, the field $\Sigma_{K+1}$ with its bare operator, i.e. the exchange of $\Sigma_{K+1}$ dressing level $K$ at $g_s^2$; for $n = 2K \to 2K + 1$, the odd vertex $O_{K+1}$ dressing level $K + 1$ at $g_s$. By the two bullets,
$$
k^{(n+1)}_{k,k;\Psi} - k^{(n)}_{k,k;\Psi} = O(g_s^{n - 2k + 3}) \quad \text{with a non-zero leading term in general}, \tag{2.2}
$$
in both cases ($n = 2K-1$: $2(K+1-k) = n - 2k + 3$; $n = 2K$: $1 + 2(K+1-k) = n - 2k + 3$). Summing (2.2) over the truncations above $n$,
$$
k^{(n)}_{k,k;\Psi} = k_{k,k;\Psi} + O(g_s^{n - 2k + 3}) . \tag{2.3}
$$
Multiplied by the prefactor $g_s^{2k-2}/(2k)!$ of the kinetic term, the first missing term sits at order $g_s^{n+1}$ of the action: $k^{(n)}_{k,k;\Psi}$ is exactly the operator that the action truncated at $g_s^n$ determines, and nothing more.

The leading term of (2.2) is non-zero whenever the corresponding reduced vertex is non-zero on the relevant arguments: for $n = 2K-1$ it is $- g_s^{n-2k+3} \big(\prod_{j=k}^{K} c_j\big) \mathcal W_{2K+2}(\Psi^{K+1-k} \otimes A, \Psi^{K+1-k} \otimes B)$, for $n = 2K$ it is $- g_s^{n-2k+3} \big(\prod_{j=k}^{K} c_j\big) \tfrac{1}{2K+3} \mathcal W_{2K+3}(\Psi^{K+1-k} \otimes A, \Psi^{K+1-k} \otimes B, \Psi)$ (each rung collapsed to its bare contact value, as in (1.2)). These are the generalisations of (1.5) and of its $g_s^5$ companion.

### Result

$$
\boxed{\, k^{(n)}_{k,k;\Psi} = k_{k,k;\Psi} + O(g_s^{\, n - 2k + 3}), \qquad k^{(n+1)}_{k,k;\Psi} \ne k^{(n)}_{k,k;\Psi} \text{ at that order in general.} \,}
$$

Instances: $k = 2$: $O(g_s^{n-1})$, matching step 1; $k = 3$, $n = 5$: $k^{(5)}_{3,3;\Psi} = w_{3,3} - \tfrac{g_s}{7} O_3$ misses the $\Sigma_4$ exchange at $g_s^2$, as in (1.5); $k = K$, $n = 2K - 1$: $O(g_s^2)$, the statement of record 115, node N4. A labelled operator is defined for $n \ge 2k - 2$; at $n = 2k - 2$ it is the bare operator, written $w_{k,k}$ (decision of 2026-11-07), and (2.3) holds there too (the correction is the odd vertex, $O(g_s)$); for $n < 2k - 2$ the field $\Sigma_k$ is not in the action.

**Consequence for the notation.** The label is information: `\kin{k}{\Psi}{n}` for two values of $n$ are two different operators, and the unlabelled $k_{k,k;\Psi}$ is their common limit. Dropping the label in section 2, where every statement is about a truncated action and where `eq:hs6:dressed-2` and `eq:hs7:dressed-2` compare two truncations of the same operator, would lose a distinction the text uses. Adding a label in section 3 to the full-tower operator would require a symbol for "no truncation" ($\infty$) on every occurrence, with no gain: the full operator is a single object.

## Step 3 – The label in the current displays

Rule as the paper uses it, read off the occurrence table: **superscript $(n)$ = the dressed operator of the action truncated at order $g_s^n$; no superscript = the operator of the full tower.** Audit of every occurrence against it:

- Section 2.3 (`\kin{2}{\Psi}{3}`, 28 lines, 33 uses): the quintic action, $n = 3$. Consistent. The sentence after `eq:hs5:dressed` already states the rule for this instance ("the operator of the action truncated at order $g_s^3$, since it receives further corrections at the next orders").
- Section 2.4 (`eq:hs6:dressed-2`): $n = 4$ defined from $n = 3$. Consistent, and this is the display where the $\Psi$-only correction of step 1, (1.2), is introduced.
- Section 2.5: `02-5-septic.tex:30` uses `\kin{2}{\Psi}{3}` for the operator of $\Sigma_2$ in $\widetilde S_{\le 6}$ (paper index) *at fixed $\Sigma_3$* – correct, since before the elimination the quadratic form of $\Sigma_2$ is bare plus quintic vertex only. `eq:hs7:sigma2-expansion`, `eq:hs7:closed-form` and the display before `eq:hs7:induced` use `\kin{2}{\Psi}{4}` for $\widetilde S_{\le 6}$ – correct; `eq:hs7:dressed-3`, `eq:hs7:dressed-2` use $n = 5$ – correct, and line 252 compares with $n = 4$. Consistent.
- Section 3 (`eq:all:dressed-odd`, `eq:all:blocks`, `eq:all:eom-top`, `eq:all:eliminate-top`): `\kin{k}{\Psi}{2 k - 1}` is the operator of $\Sigma_k$ at fixed other fields, which equals its truncated operator at $n = 2k - 1$ (where it is the top field) – the sentence after `eq:all:dressed-odd` says so. `\kin{K}{\Psi}{2 K - 1}` for the top field at truncation $K$. Consistent.
- Section 3 (`eq:all:nested` and after, 13 hand-written $k_{k,k;\Psi}$): the full tower. Consistent, and line 322 states the rule ("At a truncation $K$ … we write `\kin{k}{\Psi}{2 K - 1}` … when the truncation matters").
- Section 7b: quintic-order statements, $n = 3$. Consistent.

**Finding.** No display uses the label inconsistently; the one inconsistent occurrence is the sentence at `03-all-orders.tex:322` ($k_{K,K;\Psi} = \kin{K}{\Psi}{2K-1}$ with the unlabelled symbol for a finite-$K$ object), rewritten in step 4. What reads as an inconsistency is that the two forms meet inside section 3 (labelled top-field operator in `eq:all:dressed-odd`, unlabelled nested operator in `eq:all:nested`) with the rule stated only *after* the second display, and in section 2.3 for one instance. One omission in the rule of line 322: it covers odd truncations $2K - 1$ only, while section 2 also uses the even truncation $n = 4$ (`\kin{2}{\Psi}{4}`, the sextic action, where $\Sigma_3$ carries its bare operator).

The two review comments are answered by the rule and by (2.3):

- `02-3-quintic.tex:131`: yes, the dressed operator receives $\Psi$-only corrections, of degree $m$ in $\Psi$ at order $g_s^m$, from the elimination of the higher fields ((1.2), (1.4), (1.5)); the label is needed on every truncated operator, and the display before `eq:hs7:induced` needs its $4$. In the general construction the label *is* there wherever the truncation matters (`eq:all:dressed-odd`, `eq:all:eom-top`, line 322); the unlabelled operator of `eq:all:nested` is the full-tower one, the limit of all truncations, for which a label would be $(\infty)$. What should be added to section 3 is the rule, not labels.
- `03-all-orders.tex:340`: same answer; the "equations above" (`eq:all:nested`, `eq:hs8:scaling`) are about the full tower, those "in this section" with a label are about the top field or a truncation.

## Step 4 – Notation proposal

### Recommended convention (option A: keep the current rule, state it twice)

1. **Dressed operator of a truncated action**: $k^{(n)}_{k,k;\Psi}$ (`\kin{k}{\Psi}{n}`), $n$ the order $g_s^n$ at which the action is truncated, defined for $n \ge 2k - 2$ (at $n = 2k-2$ it is the bare $w_{k,k}$, written without label); $k^{(2k-1)}_{k,k;\Psi}$ is the operator of $\Sigma_k$ at fixed other fields (bare plus odd vertex). Used throughout section 2, in section 7b, and in section 3 for the top field and for finite-$K$ statements.
2. **Dressed operator of the full tower**: $k_{k,k;\Psi}$, no label (`eq:all:nested`). Relation: $k^{(n)}_{k,k;\Psi} = k_{k,k;\Psi} + O(g_s^{n-2k+3})$.
3. **Bare operator**: $w_{k,k}$, no label (decision of 2026-11-07).

Displays to change: **none** (step 3). Text to change (file:line → new form), for the writer:

- `02-3-quintic.tex:113` (sentence "The superscript records that it is the operator of the action truncated at order $\gs^3$, since it receives further corrections at the next orders.") → state the general rule at its first instance: "The superscript records the order $\gs^n$ at which the action is truncated: $\kin{2}{\Psi}{n}$ is the operator of the action truncated at order $\gs^n$, dressed here by the quintic vertex and, from the sextic order on, by the elimination of the higher auxiliary fields, which corrects it at each further order. The operator of the full tower, written without superscript, is defined in \cref{sec:all:squares}."
- `02-3-quintic.tex:131` (review comment) → answered; `\agcomment{Done: …}` after the series once the sentence above is in.
- `03-all-orders.tex:322` (sentence "At a truncation $K$ the chain stops at the top, …") → move it *before* `eq:all:nested` as the definition of the unlabelled symbol, and cover both parities: "The operators of \cref{sec:hs} are the truncations of the chain below: at a truncation of the action at order $\gs^n$ the chain stops at the top field, with its odd vertex for $n$ odd and with its bare operator for $n$ even, and we write $\kin{k}{\Psi}{n}$ for the operator so obtained, as in \cref{sec:hs}; $k_{k, k; \Psi}$ without superscript denotes the operator of the full tower, and $\kin{k}{\Psi}{n} = k_{k, k; \Psi} + O(\gs^{n - 2 k + 3})$, since each rung of the chain costs $\gs^2$ and the odd vertex of the top field costs $\gs$. Thus $\kin{2}{\Psi}{5}$ and $\kin{3}{\Psi}{5}$ are the operators of the septic order, and $\kin{K}{\Psi}{2 K - 1}$ of~\eqref{eq:all:dressed-odd} is the top of the chain at the truncation $K$."
- `03-all-orders.tex:340` (review comment) → answered; `\agcomment{Done: rule stated before \eqref{eq:all:nested}}`.
- Optional, `A-conventions.tex`: if a notation list exists there, one line "$\kin{k}{\Psi}{n}$: dressed kinetic operator of $\Sigma_k$ in the action truncated at order $\gs^n$; $k_{k, k; \Psi}$: full tower; $\wprod{k}{k}$: bare". (No `\kin` occurs there now.)

Rejected alternatives: (B) a label on every operator, with $(\infty)$ or no value for the full tower – 13 edits in section 3, heavier displays (`eq:all:nested` would carry three superscripts), no information gained; (C) no label anywhere – loses the distinction between `eq:hs5:dressed`, `eq:hs6:dressed-2` and `eq:hs7:dressed-2`, which section 2 compares explicitly (line 252: "the operator $\kin{2}{\Psi}{4}$ … with the $\Sigma_3$ propagator dressed in its turn"), and contradicts the decision of 2026-11-07 which keeps the label on truncated operators.

### The letter (three $k$'s)

The repetition is $k_{k,k;\Psi}$: the operator letter, the level index twice. Two independent simplifications are available; the cost of each is small because 66 of the 79 lines (81 macro uses) go through the macro `\kin`, the other 13 lines being hand-written:

- **Change the letter** to one that is not an index: $\kappa_{k,k;\Psi}$ is the natural choice (same sound, "kinetic"; $\mathcal K_{k,l;\Psi}$ is already the block of `eq:all:blocks`, and $K$ is the truncation level). One clash: $\kappa$ is the normalisation constant of the propagator measure in section 6 (`06-worldsheet.tex:326, 333, 385, 389, 438, 451`, a scalar), to be renamed there ($c_V$ or $\mathcal N$, 6 edits in one file) or avoided by taking $\mathsf k_{k,k;\Psi}$ (sans-serif, 0 hits in the paper). Cost: one line in the preamble (`\kin` → `\kappa^{(#3)}_{#1,#1;#2}`), 13 hand-written `k_{…; \Psi}` in `03-all-orders.tex` (lines 309, 318, 322, 330, 349, 353, 359, 366, 378, 380, 547, 552, 560) to edit, and the inverse `k_{k, k; \Psi}^{-1}` forms with them; the notation sheet `agent/context/paper-notation-sheet.md:48–49, 128`. The derivation notes use $k_{2,2;\Psi}$ (Harold's notation), which does not bind.
- **Drop the doubled index**: the dressed operator always has equal indices (it maps $\mathrm{Sym}^k\mathcal H$ to itself), so $k_{k;\Psi}$ or $\kappa_{k;\Psi}$ carries the same information; the doubling exists only to mirror $w_{k,k}$, whose two indices are needed because $w_{m,n}$ with $m \ne n$ is meaningful (`02-4-sextic.tex:218` says the paper avoids writing them anyway). Cost: the same macro line plus the same 13 edits.

Recommendation: change the letter to $\kappa$ (renaming the section-6 measure constant) and keep the double index ($\kappa_{k,k;\Psi}$, $\kappa^{(n)}_{k,k;\Psi}$), so that the parallel $w_{k,k} \to \kappa_{k,k;\Psi}$ ("the bare operator dressed by $\Psi$") stays visible and $\kappa^{-1}_{k,k;\Psi}$ reads better than $k^{-1}_{k,k;\Psi}$. The typo risk is confined to the 13 hand-written occurrences of one file, each found by `rg -n 'k_\{[^}]*; \\Psi\}' paper/sections/03-all-orders.tex`; the safest route is to convert them to the macro at the same time, with the macro extended to print no superscript when its third argument is empty (`\kin{k}{\Psi}{}`), by the same `\ifx\relax#3\relax` test the macro already uses for the second argument. The sans-serif alternative $\mathsf k$ avoids the section-6 rename but reads as the letter $k$ in the derivation notes, so $\kappa$ is the better of the two if the rename is accepted. If section 3 is left untouched now, option A with the letter $k$ is consistent as it stands and costs nothing.

## Checks

Script `agent/computations/verify-dressed-operator-order.py` (sympy, exact rationals, seed 20261109), run 2026-11-09 from the project root with `uv run --no-sync python …`: 7/7 PASS, 18 s wall, 73 MB peak RSS, one process. Output in `agent/scratch/computator-k-order-label-20261109T000500/`.

Model: $\mathrm{Sym}^k\mathcal H = \mathbb Q^2$ for $k = 2, \dots, 5$; random symmetric invertible $w_{k,k}$, random symmetric $O_k$, random $T_k$. The dressed operator at truncation $n$ is computed by the recursion (2.1) with *exact* matrix inverses, and its Taylor coefficients in $g_s$ are compared with the hand Neumann expansions of step 1 – an independent path (exact inverse vs. series).

| Check | Node | What it compares | Outcome |
|---|---|---|---|
| `C1.1` | C1.1 | model sanity: $k^{(3)} = w_2 - \tfrac{g_s}{5} O_2$ | PASS |
| `C1.2` | C1.2 | $k^{(4)} - k^{(3)} = - \tfrac{g_s^2}{30} T_2^{\mathsf T} w_3 T_2$ exactly in $g_s$ | PASS |
| `C1.3` | C1.3 | coefficients of $g_s^2, g_s^3, g_s^4$ in $k^{(5)}$ against (1.4) | PASS |
| `C1.3-nv` | C1.3 | the three coefficients are non-zero (non-vacuity) | PASS |
| `C1.4`, `C1.4-gs5` | C1.4 | leading order and coefficient of $k^{(6)} - k^{(5)}$ ($g_s^4$, $-1/1680$) and of $k^{(7)} - k^{(6)}$ ($g_s^5$, $-1/15120$) | PASS |
| `C2` | C2 | leading order of $k^{(n+1)}_k - k^{(n)}_k$ equals $n - 2k + 3$ for $k = 2$, $n = 3..6$ and $k = 3$, $n = 5, 6$ | PASS |
| `C1.2-break` (`--perturb C1.2-break`) | – | coefficient $1/30 \to 1/31$ in the hand formula | FAIL as intended (6/7) |
| `C1.3-break` (`--perturb C1.3-break`) | – | coefficient $1/210 \to 1/211$ | FAIL as intended (6/7) |

Scope of the legs (critic 117, #7, #8):

- The order count `C2` has no break leg: no perturbation exercises it (for instance giving the even-$n$ top field its odd vertex, which would shift the expected order from $n - 2k + 3$ to $n - 2k + 2$ for even $n$ and fail `C1.4`). The two break legs perturb the explicit coefficients of `C1.2` and `C1.3` only.
- The recursion (2.1) with the top-of-chain rule A3 and the coefficients $1/((2k+1)(2k+2))$, $-g_s/(2k+1)$ is a shared input of the hand formulas and of the code; it is checked against the paper's `eq:all:nested` and `eq:all:truncation` and by the completed-square argument of the setup (step 1), not by the script. The independence claimed is that of the exact inverses against the Neumann series.
- `C2` covers the differences $n \to n+1$ for $k = 2$, $n = 3..6$ and $k = 3$, $n = 5, 6$ (truncations 3 to 7), as in the table; the docstring of the script says "$n = 3..7$" for $k = 2, 3$, which overstates the pairs tested (the script is not edited in this pass).

Not checked by machine: C3 and C4 are an audit of the source text and a notation proposal (the occurrence table is the evidence, produced by `rg`). Nothing here tests the actual string vertices; the model is abstract and the claims are structural (which orders, which $\Psi$-degree, which truncation), as the question requires.

Dimensional check: every term of $k^{(n)}_{2,2;\Psi}$ is a product of $m$ factors $g_s \Psi$ times an operator built from vertices and inverses of bare operators, consistent with `eq:hs8:scaling`. Limiting case: $\Psi = 0$ gives $w_{k,k}$ at every $n$ (record 115).

## Proposed ledger entries

None. The result is a notation decision resting on a structural fact (`eq:hs8:scaling`, record 115 node N4) made explicit; it belongs in `knowledge/decisions.md` as a companion of the 2026-11-07 entry, not in the results ledger.
