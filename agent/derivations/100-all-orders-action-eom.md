---
description: The cubic action at K = ∞ as a formal power series in g_s (two terms per even order, one per odd order), the truncation at K as the truncation of that series at g_s^{2K-1}, the equations of motion of Ψ and of every Σ_k by variation (general k, boundary cases, first orders to Σ_3, octic instance), and their triangular structure; checked in a finite-dimensional model through K = 4
---

# Derivation 100 — The cubic action at $K = \infty$ and the equations of motion of all fields

Brief: `agent/briefs/active-computator-100-all-orders-eom-20261018T020000.md`.

## Task and objective

**Literal task.** From the truncated cubic action of the paper (`03-all-orders.tex`, `eq:all:action`, `eq:all:kinetic`, `eq:all:dressed-odd`, `eq:all:tridiagonal`, `eq:all:blocks`): (1) write the action with the full tower $\Sigma_2, \Sigma_3, \ldots$ ($K = \infty$) as a formal power series in $g_s$, say in which sense it is well defined, and say what the truncation at a generic $K$ is in terms of that series; (2) derive the equations of motion of $\Psi$, $\Sigma_2$, $\Sigma_3$ and a general $\Sigma_k$ at $K = \infty$, with sums, boundary cases ($k = 2$, the top field at finite $K$), then the first orders up to $\Sigma_3$; (3) the octic instance, every term explicit, consistent with `eq:hs8:saddle-4`, and how it exhibits the triangular form named in `02-5-septic.tex`.

**Motivating objective.** Additions X-01, X-02, X-03 requested for the paper: the paper should show that there is a general cubic action at all orders, not only a truncated form, and the equations of motion should give the reader intuition about how the fields couple. The writers display the results of this record in sections 3 and 2.6; nothing goes into the paper that this record has not derived and checked.

## Conventions and notation

The paper's macros are used in the displays: $\pair[k]{\cdot}{\cdot}$ is the $k$-string pairing (`eq:conv:pairing-n`), $\vertex{n} = \mathcal V_n$ the elementary vertices, $\dvertex{n} = \mathcal W_n$ the dressed vertices, $\kin{k}{}{2k-2} = k^{(2k-2)}_{k,k}$ the bare kinetic operator of $\Sigma_k$ (`eq:all:kinetic`), $\kin{k}{\Psi}{2k-1} = k^{(2k-1)}_{k,k;\Psi}$ the operator dressed by the odd vertex (`eq:all:dressed-odd`), $\sprod{m}{n} = p_{m,n}$ the products, $\caction[\ldots] = \widetilde S_{\ldots}$ the cubic action. In this Markdown record the same objects are written $\langle\cdot,\cdot\rangle_k$, $\mathcal V_n$, $\mathcal W_n$, $k_{k,k}$, $k_{k,k;\Psi}^{(n)}$, $p_{m,n}$, $\widetilde S$; $g := g_s$.

Shorthands used throughout the record:

$$a_k := \frac{g^{2k-2}}{(2k)!}, \qquad b_k := \frac{g^{2k-1}}{(2k+1)!}, \qquad \frac{b_k}{a_k} = \frac{g}{2k+1}, \qquad \frac{a_{k+1}}{a_k} = \frac{g^2}{(2k+1)(2k+2)}, \qquad \Sigma_1 := \Psi .$$

**Open-slot notation** (the paper's, `eq:hs6:eom`): for a multilinear form with one slot left open, the symbol with a dot denotes the state paired with that slot through the pairing of the slot's strand number. Thus $\mathcal W_{2k}(\Psi \otimes \cdot\,, B) \in \mathcal H^{\wedge k}$ is defined by $\langle A, \mathcal W_{2k}(\Psi \otimes \cdot\,, B)\rangle_k = \mathcal W_{2k}(\Psi \otimes A, B)$ for all $A \in \mathcal H^{\wedge k}$; $\mathcal W_{2k}(\cdot \otimes \Sigma_{k-1}, B) \in \mathcal H$ by $\langle C, \mathcal W_{2k}(\cdot \otimes \Sigma_{k-1}, B)\rangle = \mathcal W_{2k}(C \otimes \Sigma_{k-1}, B)$; $\mathcal W_{2k+1}(\cdot\,, B, \Psi) \in \mathcal H^{\wedge k}$ and $\mathcal W_{2k+1}(A, B, \cdot) \in \mathcal H$ likewise. In the paper's product notation, $\mathcal W_{2k}(\Psi \otimes \cdot\,, B) = k_{k,k}(\cdot)$ transposed, i.e. $\langle A, \mathcal W_{2k}(\Psi\otimes\cdot, B)\rangle_k = \langle k_{k,k}(\Psi \otimes A), B\rangle_k$ by `eq:all:kinetic` and the symmetry of $k_{k,k}$.

$\Psi \otimes \Sigma_{k-1}$ denotes the element of $\mathcal H^{\wedge k}$ obtained by graded symmetrization, so that $\Psi \otimes \Psi^{k-1} = \Psi^k$.

## Claim tree

- **A1** Conventions of the paper: pairing $\langle A, B\rangle = \langle A | c_0^- | B \rangle$ (`eq:hs1:pairing`, C1 of `knowledge/conventions.md`), $n$-string pairing `eq:conv:pairing-n`; $\Psi$ and every $\Sigma_k$ Grassmann even, so that every multi-string pairing met here is the plain product of the strand pairings and is symmetric, and the transposition identity `eq:conv:transpose` holds without sign; multi-string spaces as in C6.
- **A2** The cubic action is `eq:all:action` with its normalizations ($\Sigma_1 := \Psi$). $\mathcal W_{2k}$ is a symmetric bilinear form on $\mathcal H^{\wedge k}$, $\mathcal W_{2k+1}$ a trilinear form on $\mathcal H^{\wedge k} \times \mathcal H^{\wedge k} \times \mathcal H$ symmetric in its first two arguments; $\mathcal W_4 = \mathcal V_4$ and $\mathcal W_5 = \mathcal V_5$ are the fully graded-symmetric string vertices (`eq:all:counting`). No symmetry of $\mathcal W_n$, $n \ge 6$, beyond this block symmetry is used.
- **A3** Normalization of the equations of motion: the convention of `02-2-quartic.tex`–`02-6-octic.tex` ($\delta \widetilde S = \sum_X \langle \delta X, \mathcal E_X \rangle$ up to a positive factor, stated at `eq:hs8:saddle-4`), made precise as $\delta \widetilde S = \langle \delta\Psi, \mathcal E_\Psi \rangle + \sum_{k \ge 2} 2 a_k \langle \delta \Sigma_k, \mathcal E_{\Sigma_k} \rangle_k$, which reproduces `eq:hs4:eom`, `eq:hs5:eom`, `eq:hs6:eom`, `eq:hs7:saddle-3`, `eq:hs8:saddle-4`. The display `eq:all:eom-top` keeps the factor $2 a_K$ inside $\mathcal E_{\Sigma_K}$; see the finding in *For the writers*.
- **A4** Tree level; every identity in $g$ is read as a formal power series, exact and rational at each finite truncation $K$ (paper, section 3 preamble). Where an inverse is taken, the setting is the one of R26 and R70: a finite-dimensional truncation (fixed level, momenta fixed or discretized).
- **A5** The auxiliary fields live on the quotients $\mathcal H^{\wedge k} / \ker k_{k,k}$ and the action descends to them under the kernel condition `eq:hs8:kernel-condition`. Where a claim needs this, it cites the hypotheses the ledger attaches to it: PH1 and PH5 at $k = 2$, PH2 (b) for $k \ge 3$, as in R26 and R70.
- **C1** The cubic action at $K = \infty$ is a well-defined formal power series in $g$ whose coefficient at each order is a polynomial of degree $\le 3$ in finitely many fields: two terms at every even order $g^{2k-2}$, $k \ge 2$ (kinetic term and source of $\Sigma_k$), one at every odd order $g^{2k-1}$ (the odd coupling of $\Sigma_k$); the field $\Sigma_k$ enters first at order $g^{2k-2}$. [by C1.1–C1.4]
  - **C1.1** Explicit coefficient of $g^m$ for every $m \ge 0$ (eq. (1.2)). [by A2; block 1]
  - **C1.2** The $K = \infty$ nested operators $k^{(\infty)}_{k,k;\Psi}$ and their inverses exist as formal power series on the quotients as soon as the bare operators are invertible there and the kernel condition holds; no condition beyond those of finite $K$ is needed, and the analytic statement of finite $K$ (invertible for $g\Psi$ in a neighbourhood of zero) is replaced by a coefficientwise one. [by A4, A5, R70; block 1] (conditional on PH1, PH5, PH2 (b))
  - **C1.3** Coefficientwise stabilization, an algebraic identity between the finite-$K$ and the $K = \infty$ recursions valid whenever the bare inverses exist on the quotients: for the odd truncation $\widetilde S_{\le 2K+1}$, $[g^m]\, k^{(2K-1)}_{k,k;\Psi}$ is independent of $K$ for $K \ge k + \lfloor m/2 \rfloor$, $[g^m]\, \Sigma_k^{*(K)}$ for $K \ge k + \lfloor m/2 \rfloor$, and $[g^m]$ of the value for $K \ge 1 + \lfloor m/2 \rfloor$; for the even truncation $\widetilde S_{\le 2K}$ replace $\lfloor m/2 \rfloor$ by $\lceil m/2 \rceil$; hence the $K = \infty$ objects are the coefficientwise limits. [by C1.2; block 1] [check: C1.3] (for the string objects, the coefficients being those of C1.2 on the quotients: conditional on PH1, PH5, PH2 (b) through A5; unconditional in the finite model)
  - **C1.4** At $K = \infty$ the value of the action on the solution equals $S$ as a formal power series, with the dressed vertices of R26. [by R26, C1.3, C2.2] (conditional on PH1, PH2 (b), PH5, PH14)
- **C2** The truncation at $K$ is the truncation of the series of C1 at order $g^{2K-1}$ inclusive ($\widetilde S_{\le 2K+1}$) or at order $g^{2K-2}$ ($\widetilde S_{\le 2K}$); it reproduces the eliminated action through that order and drops everything above it. [by C2.1–C2.2]
  - **C2.1** $\widetilde S_{\le 2K+1} = \sum_{m \le 2K-1} g^m [g^m] \widetilde S_\infty$ and $\widetilde S_{\le 2K} = \sum_{m \le 2K-2} g^m [g^m] \widetilde S_\infty$; the even truncation drops the odd coupling of $\Sigma_K$ only. [by C1.1; block 1]
  - **C2.2** $\widetilde S_{\le 2K+1}|_{\rm sol} = S_{\le 2K+1} + O(g^{2K})$ and $\widetilde S_{\le 2K}|_{\rm sol} = S_{\le 2K} + O(g^{2K-1})$; the remainder is the first order at which the next level enters. [by R26; `eq:all:recovered`, `eq:hs8:eliminate`] [check: C2.2] (conditional as R26)
- **C3** Equations of motion of the action `eq:all:action` for every $K \le \infty$, by variation. [by C3.1–C3.5]
  - **C3.1** $\mathcal E_\Psi$, eq. (2.4). [by A1–A3; block 2] [check: C3.1]
  - **C3.2** $\mathcal E_{\Sigma_k}$, eq. (2.5), with its boundary cases $k = 2$ (source $p_{2,2}(\Psi^2)$) and $k = K$ (no exchange term). [by A1–A3; block 2] [check: C3.2]
  - **C3.3** Under the kernel condition the equations are statements on the quotients: $\mathcal E_{\Sigma_k}$ is independent of the kernel components of every field and pairs to zero with every kernel direction. [by A1, A5; block 2] (conditional on PH1, PH5, PH2 (b))
  - **C3.4** At $k = K$, eq. (2.5) is `eq:all:eom-top` up to the normalization of A3, and substituting its solution gives `eq:all:eliminate-top`. [by C3.2; block 2] [check: C3.4]
  - **C3.5** At $K = \infty$ the system is solvable order by order in $g$: $[g^m]\Sigma_k^*$ is determined by $[g^m]\Sigma_{k-1}^*$, $[g^{m-1}]\Sigma_k^*$, $[g^{m-2}]\Sigma_{k+1}^*$ (eq. (2.7)), a finite recursion in $(m, k)$ with $[g^0]\Sigma_k^* = \Psi^k$. [by C3.2, C1.2; block 2] [check: C3.5]
- **C4** First orders of the equations through $\Sigma_3$: the $K = 3$ instance, eqs (3.1)–(3.3), with the septic action $\widetilde S_{\le 7}$; and the explicit low orders of the solutions. [by C3.1, C3.2; block 3] [check: C4]
- **C5** The octic instance: equations of motion of $\Psi$, $\Sigma_2$, $\Sigma_3$, $\Sigma_4$ for $\widetilde S_{\le 8}$, eqs (4.1)–(4.4), consistent with `eq:hs8:saddle-4`, `eq:hs7:saddle-3`, `eq:hs6:eom`, `eq:hs5:eom`. [by C3.1, C3.2, C2.1; block 4] [check: C5]
- **C6** Triangular structure: each $\Sigma_k$ equation is linear in the tower, couples $\Sigma_k$ to $\Sigma_{k \pm 1}$ only (block-tridiagonal, `eq:all:tridiagonal`), with the source of $\Sigma_k$ depending on lighter fields alone and the heavier neighbour entering at relative order $g^2$; the top equation closes the chain; solving from the top at fixed $g$, or order by order from the bottom, is a finite elimination. [by C3.2, C3.5, C5; block 4] [check: C6-top-first] Closure clause: the octic equations solved order by order reproduce $S_{\le 8}$ through $g^6$ once $\mathcal W_6, \mathcal W_7, \mathcal W_8$ are the dressed vertices of `eq:all:diagonal`. [by C5, R26; block 4] [check: C6-closure-g{0..6}] (conditional as R26: PH1, PH2 (b), PH5, PH14)

Open gaps: none
Hypotheses in force: PH1, PH2 (b), PH5, PH14 (through R26) for C1.4, C2.2 and the closure clause of C6 (last sentence); PH1, PH5, PH2 (b) (through A5, the quotient prescription) for C1.2, C3.3, and for C1.3, C3.4, C3.5 in so far as their coefficients are those of the objects of C1.2 (as algebraic identities between the finite-$K$ and $K = \infty$ recursions, valid whenever the bare inverses exist on the quotients, they are unconditional); C1.1, C2.1, C3.1, C3.2, C4, C5 and the structural part of C6 are unconditional algebra.

## Status

Complete (2026-10-18): blocks 1–4, companion script `codes/verify-all-orders-eom.py` (53/53 PASS, seeds 20261018 and 41), Verification, For the writers, Proposed ledger entries. Fix pass of 2026-10-18 applied (section below); script rerun, 53/53 PASS. Next: narrow confirmation pass or promotion, per the orchestrator.

## Fix pass (2026-10-18)

Critique: `agent/reports/critic-100-all-orders-eom-20261018T022500.md`. No displayed equation changed; the script is unchanged (no finding concerns its code) and was rerun after the edits: 53/53 PASS, seeds 20261018 and 41 (`agent/scratch/computator/computator-100-fix-20261018T023500/run-{20261018,41}.log`).

| finding | change | node | statement or justification |
|---|---|---|---|
| #1 major | C6 split: the structural part keeps its justification [by C3.2, C3.5, C5]; the closure clause ("the octic equations solved order by order reproduce $S_{\le 8}$ through $g^6$") now cites R26 (`eq:all:diagonal`) and is conditional as R26. C1.3 restated as an algebraic identity between recursions, valid whenever the bare inverses exist on the quotients, with the conditionality (A5) named for its application to the string objects. `Hypotheses in force:` line rewritten accordingly. Ledger entry 1, item (4): "whenever the inverses exist on the quotients (A5)" added; Scope lists the closure clause of C6 as belonging to entry 2. | C6, C1.3 | statement (conditionality added); displays unchanged |
| #2 minor | Boundary sentence after (2.5) extended to (2.4): in the even truncation the odd term of $k = K$ is absent from $\mathcal E_\Psi$ too, at $K = 2$ the $\ell_4$ term; same in the writers' C3 text and in the "limiting cases" paragraph. | C3.1 | justification (scope sentence; (2.4) unchanged) |
| #3 minor | Stabilization bounds named for the odd truncation; even truncation: $\lfloor m/2 \rfloor \to \lceil m/2 \rceil$, in block 1, the writers' C1 text, remark (ii), ledger entry 1 item (4). | C1.3 | statement (scope clause added) |
| #4 minor | The R70 appeal for the descent of $\kappa_{k,[m]}$ to the quotients replaced by the direct argument from the two clauses of `eq:hs8:kernel-condition`, by induction on the level. | C1.2 | justification |
| #5 minor | C1.1: $\mathcal F$ defined on $\mathcal H \times \prod_k \mathcal H^{\wedge k}$, with the descent to the quotients under A5 stated separately; `Hypotheses in force:` qualifies C3.4, C3.5 (see #1). | C1.1, C3.4, C3.5 | justification (C1.1); statement qualified (C3.4, C3.5) |
| #6 minor | C3.5 claim text: "(eq. (2.8))" → "(eq. (2.7))". | C3.5 | typo |
| #7 minor | Verification table, last row: "through $g^7$" → "through $g^6$ (the change is $O(g^8)$ by stationarity)". | — | wording |
| #8 minor | Writers' C3 sentence: the factor 2 attributed to the $\ell_3$ term alone, $\ell_4$ named as the $k = 2$ odd term. | — | wording |
| #9–#12 notes | #9: ledger entry 1 tag changed to "Proven – Verified (finite model)" and the verification line to "numerical check"; the `eq:all:eom-top` finding kept in the entry body as a remark for the writers (the clerk may drop it). #10–#12: no change. | — | — |

Dependents of the changed nodes: C1 (cites C1.1–C1.4) holds as written, its own statement being unconditional algebra plus the conditional C1.2–C1.4 as before; C1.4 (cites C1.3) holds, already conditional as R26 and on A5; C3.5 (cites C1.2) and C3.4 (cites C3.2) hold, now with their conditionality named; C3 and C6 hold as written. The root claim (`description:`) is unchanged. The `Hypotheses in force:` line changed, which by `claim-tree.md` calls for a full re-review if a further pass runs.

## Block 1 — The action at $K = \infty$ and its truncation (C1, C2)

### Setup

Uses A1, A2, A4, A5. The level-$k$ terms of `eq:all:action` are, with $\Sigma_1 := \Psi$,

$$
\widetilde S^{(k)} := - a_k \langle \Sigma_k, k_{k,k}(\Sigma_k) \rangle_k + 2 a_k \langle \Sigma_k, k_{k,k}(\Psi \otimes \Sigma_{k-1}) \rangle_k + b_k \mathcal W_{2k+1}(\Sigma_k, \Sigma_k, \Psi), \qquad k \ge 2. \tag{1.1}
$$

### Derivation

**The series.** Define the action with the full tower as the formal sum of the level terms,

$$
\widetilde S_\infty := S_{\le 3} + \sum_{k \ge 2} \widetilde S^{(k)}
= \sum_{m \ge 0} g^m \, \widetilde S_{[m]},
$$

with the coefficients read off the powers of $g$ in (1.1), $a_k \propto g^{2k-2}$, $b_k \propto g^{2k-1}$:

$$
\begin{aligned}
\widetilde S_{[0]} &= \tfrac12 \langle \Psi, Q_B \Psi \rangle, \qquad
\widetilde S_{[1]} = \tfrac{1}{3!} \mathcal V_3(\Psi^3), \\
\widetilde S_{[2k-2]} &= - \frac{1}{(2k)!} \langle \Sigma_k, k_{k,k}(\Sigma_k) \rangle_k + \frac{2}{(2k)!} \langle \Sigma_k, k_{k,k}(\Psi \otimes \Sigma_{k-1}) \rangle_k, \qquad k \ge 2, \\
\widetilde S_{[2k-1]} &= \frac{1}{(2k+1)!} \mathcal W_{2k+1}(\Sigma_k, \Sigma_k, \Psi), \qquad k \ge 2 .
\end{aligned}
\tag{1.2}
$$

Every coefficient is a polynomial of degree at most three in the fields; the coefficient of $g^m$ involves $\Psi$ and the fields $\Sigma_{\lfloor m/2 \rfloor + 1}$ and (at even $m$) $\Sigma_{\lfloor m/2 \rfloor}$ only. $\widetilde S_\infty$ is therefore an element of $\mathcal F[[g]]$, $\mathcal F$ the polynomial functions on $\mathcal H \times \prod_{k \ge 2} \mathcal H^{\wedge k}$ depending on finitely many factors; under the kernel condition (A5) each coefficient descends to the quotients $\mathcal H^{\wedge k}/\ker k_{k,k}$, the statement of C3.3, which the coefficient form does not need. No convergence is involved: at a given order there is nothing to sum. This is the sense of "well defined" for the action itself. (C1.1)

In the rescaled variables $\widetilde\Sigma_k = g^{k-1}\Sigma_k$ of `eq:all:rescaling` the same sum is $\widetilde S_\infty = \frac12 \mathbb K(\Phi, \Phi) + g\, \mathbb V(\Phi, \Phi, \Phi)$ on $\Phi = \sum_{n\ge1}\widetilde\Sigma_n \in \bigoplus_{n \ge 1} \mathcal H^{\wedge n}$ (`eq:all:rescaled`, `eq:all:total-field`): a quadratic form and a cubic form, each a direct sum over levels, finite on any configuration with finitely many nonzero components. The two readings differ only in the bookkeeping of $g$; the formal-series reading is the one in which the elimination is organized.

**The nested operators at $K = \infty$.** At finite $K$ the operators `eq:all:nested` are defined from the top down and are rational in $g$. At $K = \infty$ there is no top: the recursion is read coefficientwise instead. Write $k^{(\infty)}_{k,k;\Psi} = \sum_{m \ge 0} g^m \kappa_{k,[m]}$. Then `eq:all:nested` with `eq:all:dressed-odd` reads

$$
\kappa_{k,[0]} = k_{k,k}, \qquad
\kappa_{k,[1]} = - \frac{1}{2k+1} \mathcal W_{2k+1}(\cdot, \cdot, \Psi), \qquad
\kappa_{k,[m]} = - \frac{1}{(2k+1)(2k+2)} \, \Big[ g^{m-2} \Big] \, k_{k+1,k+1}(\Psi \otimes \cdot)^{\mathsf T} \circ \big( k^{(\infty)}_{k+1,k+1;\Psi} \big)^{-1} \circ k_{k+1,k+1}(\Psi \otimes \cdot), \quad m \ge 2,
\tag{1.3}
$$

where $[g^{m-2}]$ of the inverse is a polynomial in $\kappa_{k+1,[j]}$, $j \le m-2$, and in $k_{k+1,k+1}^{-1}$ (Neumann series). The recursion for $\kappa_{k,[m]}$ calls level $k+1$ at orders $\le m-2$, level $k+2$ at orders $\le m-4$, and so on; it terminates because every $\kappa_{j,[0]} = k_{j,j}$ is given. Hence $\kappa_{k,[m]}$ involves the levels $j \le k + \lfloor m/2 \rfloor$ only, and is a finite expression. (C1.2, first part)

Invertibility: on the quotient, $k^{(\infty)}_{k,k;\Psi} = k_{k,k} \circ (1 + O(g))$ as a formal series, and a formal power series with invertible constant term is invertible; its inverse is the Neumann series, each coefficient a finite sum. So $(k^{(\infty)}_{k,k;\Psi})^{-1}$ exists in $\mathrm{End}(\mathcal H^{\wedge k}/\ker k_{k,k})[[g]]$ exactly when $k_{k,k}$ is invertible on its quotient, which is the finite-$K$ assumption (`03-all-orders.tex`, "We assume, as in section 2.6, that the bare operators are invertible on their quotients"). That every $\kappa_{k,[m]}$ descends to the same quotient follows from the two clauses of `eq:hs8:kernel-condition` directly, by induction on the level: for $N_k \in \ker k_{k,k}$, $\kappa_{k,[1]} = \frac{1}{2k+1}\mathcal W_{2k+1}(\cdot, \cdot, \Psi)$ vanishes on $N_k$ by the first clause, and every $\kappa_{k,[m]}$ with $m \ge 2$ is of the form $L_{k+1}^{\mathsf T}(\cdots)L_{k+1}$ with $L_{k+1} := k_{k+1,k+1}(\Psi \otimes \cdot)$ and $L_{k+1}N_k = k_{k+1,k+1}(\Psi \otimes N_k) = 0$ by the second clause, the inner factor $(\cdots)$ being a coefficient of the level-$(k+1)$ inverse, which acts on the level-$(k+1)$ quotient by the induction hypothesis (each coefficient involves finitely many levels, so the induction is finite at every order). This is the finite-$K$ condition again, and agrees with R70's statement at every finite $K$ (the nested kernels depend on $g\Psi$ only and reduce at $g = 0$ to the bare radical); R70 itself is not needed at $K = \infty$. What is lost at $K = \infty$ is only the analytic statement: at finite $K$ the inverse exists for $g\Psi$ in a neighbourhood of zero (a rational function of $g$); at $K = \infty$ it is a formal series whose convergence is not addressed, as the paper's preamble to section 3 says. (C1.2)

**Stabilization in $K$.** The finite-$K$ operator $k^{(2K-1)}_{k,k;\Psi}$ is the same recursion stopped at level $K$ (no exchange term at $k = K$). Since $[g^m]$ of the $K = \infty$ recursion involves levels $\le k + \lfloor m/2 \rfloor$ only, 

$$
[g^m]\, k^{(2K-1)}_{k,k;\Psi} = [g^m]\, k^{(\infty)}_{k,k;\Psi} \quad \text{for } K \ge k + \lfloor m/2 \rfloor . \tag{1.4}
$$

The solutions `eq:all:saddles`, $\Sigma_k^* = (k_{k,k;\Psi})^{-1} \circ k_{k,k}(\Psi \otimes \Sigma_{k-1}^*)$, inherit the bound by induction on $k$ ($\Sigma_1^* = \Psi$ is exact): $[g^m]\Sigma_k^*$ uses $[g^{j}](k_{k,k;\Psi})^{-1}$ and $[g^{m-j}]\Sigma_{k-1}^*$, stable for $K \ge k + \lfloor j/2 \rfloor$ and $K \ge k - 1 + \lfloor (m-j)/2 \rfloor$, both implied by $K \ge k + \lfloor m/2 \rfloor$. The value `eq:all:value` is $S_{\le 3} + a_2 \langle p_{2,2}(\Psi^2), (k_{2,2;\Psi})^{-1} p_{2,2}(\Psi^2)\rangle_2$: its $g^m$ coefficient uses $[g^{m-2}]$ of the level-2 inverse, stable for $K \ge 2 + \lfloor (m-2)/2 \rfloor = 1 + \lfloor m/2 \rfloor$. In words: level $K+1$ first changes the value at order $g^{2K}$, the $\Sigma_k^*$ at order $g^{2(K+1-k)}$ and the operator of $\Sigma_k$ at order $g^{2(K+1-k)}$; these are the "each rung costs $g^2$" statements of the paper, now as explicit bounds. They are written for the odd truncation $\widetilde S_{\le 2K+1}$. For the even truncation $\widetilde S_{\le 2K}$ the top level lacks its odd dressing, so level $K$ may be called at order $0$ only: $m - 2(K - k) \le 0$ in the recursion of (1.3), i.e. $K \ge k + \lceil m/2 \rceil$ for the operator and for $\Sigma_k^*$, and $K \ge 1 + \lceil m/2 \rceil$ for the value (equivalently, the even-$K$ value is stable through $g^{2K-2}$, consistent with C2.2). The bounds are an algebraic identity between the two recursions, valid whenever the bare inverses exist on the quotients (for the string objects, under A5; in the finite model, unconditionally). The $K = \infty$ operators, solutions and value are the coefficientwise limits of the finite-$K$ ones, every coefficient being attained at a finite $K$. (C1.3)

**Closure at $K = \infty$.** R26 (within its ansatz and hypotheses) supplies dressed vertices $\mathcal W_n$ for every $n$ such that `eq:all:recovered` holds at every $K$: $\widetilde S_{\le 2K+1}|_{\rm sol} = S_{\le 2K+1} + O(g^{2K})$. By (1.4) the coefficient $[g^m]$ of the $K = \infty$ value is the one of any $K \ge 1 + \lfloor m/2 \rfloor$, and for such $K$, $m \le 2K - 1$, so it equals $[g^m] S$. Hence $\widetilde S_\infty|_{\rm sol} = S$ as an identity of formal power series in $g$, under the hypotheses of R26 (PH1, PH2 (b), PH5, PH14). The paper's "every coefficient stabilizes" (after `eq:all:value`) is this statement. (C1.4)

**The truncation at $K$.** By (1.2) the levels $k \le K$ occupy exactly the orders $m \le 2K-1$, and level $K+1$ begins at $g^{2K}$. Therefore

$$
\widetilde S_{\le 2K+1} = \sum_{m=0}^{2K-1} g^m\, \widetilde S_{[m]}, \qquad
\widetilde S_{\le 2K} = \sum_{m=0}^{2K-2} g^m\, \widetilde S_{[m]} = \widetilde S_{\le 2K+1} - b_K \mathcal W_{2K+1}(\Sigma_K, \Sigma_K, \Psi):
\tag{1.5}
$$

the truncation "with the fields $\Sigma_2, \ldots, \Sigma_K$" is the truncation of the series at order $g^{2K-1}$ inclusive, and the even truncation of `02-6-octic.tex` ($K = 4$, $\widetilde S_{\le 8}$) is the truncation at $g^{2K-2}$, which keeps the kinetic term and source of $\Sigma_K$ and drops its odd coupling. Nothing else is dropped: a truncation of the series at any order $m$ is one of these two, with $K = \lfloor m/2 \rfloor + 1$. (C2.1)

What the truncation reproduces: by `eq:all:recovered` (R26), $\widetilde S_{\le 2K+1}|_{\rm sol} = S_{\le 2K+1} + O(g^{2K})$, and by `eq:hs8:eliminate` generalized (the same argument with the odd coupling of level $K$ absent: the $g^{2K-1}$ coefficient then lacks $\mathcal W_{2K+1}(\Psi^{2K+1})/(2K+1)!$), $\widetilde S_{\le 2K}|_{\rm sol} = S_{\le 2K} + O(g^{2K-1})$. The remainder is in each case at the order of the first term of the series left out, and it is not zero in general: the truncated action's value is a rational function of $g$ whose expansion continues past the matched order with coefficients that are not those of $S$ (the finite-$K$ value lacks the level-$(K+1)$ contact term and carries its own non-collapsing exchange terms). The truncation therefore reproduces the eliminated action exactly through the order of its last term and drops the orders above, where it is neither $S$ nor zero. (C2.2)

### Commentary

- (1.2): the only bookkeeping is $a_k \propto g^{2k-2}$, $b_k \propto g^{2k-1}$; the even coefficient collects the two terms of `eq:all:square` expanded, the odd one is `eq:all:odd`.
- (1.3): the inverse in `eq:all:nested` is expanded as a Neumann series around $k_{k+1,k+1}^{-1}$; the $g$-order of each term is at least the sum of the orders of its $\kappa$ factors, which is what makes $[g^{m-2}]$ a finite sum. The bound "levels $\le k + \lfloor m/2\rfloor$" is the statement of `03-all-orders.tex` after `eq:all:nested` ("the coefficient of $g^m$ involves the levels $k \le m/2 + 2$ only" for $k = 2$), proved here by the recursion.
- (1.4): the finite-$K$ recursion and the $K = \infty$ one coincide on every coefficient that never calls a level above $K$.
- Beyond finite $K$, the $K = \infty$ form needs: (i) the existence of $\mathcal W_n$ for all $n$ — R26's recursion `eq:all:diagonal`, under its hypotheses; (ii) nothing new for invertibility, since a formal series with invertible constant term is invertible; (iii) the acceptance that the identity is coefficientwise only, with no statement on convergence. The brief's candidate condition, "invertibility of the dressed operators as formal power series", is implied by the bare invertibility already assumed at finite $K$.

### Result

$$
\boxed{\;
\widetilde S_\infty = \tfrac12 \langle \Psi, Q_B \Psi \rangle + \tfrac{g}{3!} \mathcal V_3(\Psi^3)
+ \sum_{k \ge 2} \Big[ \frac{g^{2k-2}}{(2k)!} \Big( 2 \langle \Sigma_k, k_{k,k}(\Psi \otimes \Sigma_{k-1}) \rangle_k - \langle \Sigma_k, k_{k,k}(\Sigma_k) \rangle_k \Big) + \frac{g^{2k-1}}{(2k+1)!} \mathcal W_{2k+1}(\Sigma_k, \Sigma_k, \Psi) \Big], \;}
$$

a formal power series in $g$ with two terms at each even order and one at each odd order; $\widetilde S_{\le 2K+1}$ is its truncation at $g^{2K-1}$, $\widetilde S_{\le 2K}$ at $g^{2K-2}$.

### Verification

C1.1, C2.1 are bookkeeping of powers (checked by reading (1.2) against `eq:all:action`; machine check: the script builds the $K = 4$ action from (1.2) and compares with the level-sum form at random fields and $g$, `C1.1-series-equals-level-sum`). C1.3 is checked by `C1.3-stabilization`: $[g^m]\Sigma_2^*$ agrees between $K = 3$ and $K = 4$ for $m \le 3$ and differs at $m = 4$; $[g^m]$ of the value agrees for $m \le 5$ and differs at $m = 6$. C2.2 is covered by the closure checks of block 4.

## Block 2 — Equations of motion, general $k$ (C3)

### Setup

Uses A1–A5 and the open-slot notation. $K \le \infty$; for $K = \infty$ every sum is a formal series (block 1). The variation of each term of (1.1) is written through the pairing of the varied field; the symmetry of $k_{k,k}$ with respect to $\langle\cdot,\cdot\rangle_k$ (`eq:all:kinetic`, $\mathcal W_{2k}$ symmetric) and of $\mathcal W_{2k+1}$ in its first two slots (A2) are the only properties used.

### Derivation

**Variation of each term.** For the level-$k$ terms (1.1), with $\delta$ acting on all fields:

$$
\begin{aligned}
\delta \big[ - a_k \langle \Sigma_k, k_{k,k}(\Sigma_k) \rangle_k \big] &= - 2 a_k \langle \delta\Sigma_k, k_{k,k}(\Sigma_k) \rangle_k , \\
\delta \big[ 2 a_k \langle \Sigma_k, k_{k,k}(\Psi \otimes \Sigma_{k-1}) \rangle_k \big] &= 2 a_k \langle \delta\Sigma_k, k_{k,k}(\Psi \otimes \Sigma_{k-1}) \rangle_k
 + 2 a_k \langle \delta\Psi, \mathcal W_{2k}(\cdot \otimes \Sigma_{k-1}, \Sigma_k) \rangle
 + 2 a_k \langle \delta\Sigma_{k-1}, \mathcal W_{2k}(\Psi \otimes \cdot\,, \Sigma_k) \rangle_{k-1} , \\
\delta \big[ b_k \mathcal W_{2k+1}(\Sigma_k, \Sigma_k, \Psi) \big] &= 2 b_k \langle \delta\Sigma_k, \mathcal W_{2k+1}(\cdot\,, \Sigma_k, \Psi) \rangle_k + b_k \langle \delta\Psi, \mathcal W_{2k+1}(\Sigma_k, \Sigma_k, \cdot) \rangle ,
\end{aligned}
\tag{2.1}
$$

where in the second line $\langle \Sigma_k, k_{k,k}(\Psi \otimes \Sigma_{k-1})\rangle_k = \mathcal W_{2k}(\Sigma_k, \Psi \otimes \Sigma_{k-1})$ was varied slot by slot. At $k = 2$ the second line is special, since $\Sigma_1 = \Psi$ appears twice in $\Psi \otimes \Sigma_1 = \Psi^2$: the two last terms merge into

$$
\delta \big[ 2 a_2 \mathcal V_4(\Sigma_2, \Psi^2) \big] \supset 2 a_2 \cdot 2\, \mathcal V_4(\Sigma_2, \delta\Psi \otimes \Psi) = \frac{4 g^2}{4!} \langle \delta\Psi, \ell_3(\Psi, \Sigma_2) \rangle = \frac{g^2}{3!} \langle \delta\Psi, \ell_3(\Psi, \Sigma_2) \rangle ,
\tag{2.2}
$$

the term of `eq:hs4:delta-S` (`eq:hs4:same-vertex`). For $S_{\le 3}$: $\delta S_{\le 3} = \langle \delta\Psi, Q_B\Psi + \tfrac{g}{2} \ell_2(\Psi^2) \rangle$.

**Collecting.** Summing (2.1) over $k = 2, \ldots, K$ and grouping by the varied field,

$$
\delta \widetilde S_{\le 2K+1} = \langle \delta\Psi, \mathcal E_\Psi \rangle + \sum_{k=2}^{K} 2 a_k \langle \delta\Sigma_k, \mathcal E_{\Sigma_k} \rangle_k ,
\tag{2.3}
$$

with, after dividing the $\Sigma_k$ bracket by $2 a_k$ (A3) and using $b_k / a_k = g/(2k+1)$, $a_{k+1}/a_k = g^2/((2k+1)(2k+2))$:

$$
\boxed{\;
\mathcal E_\Psi = Q_B \Psi + \frac{g}{2} \ell_2(\Psi^2) + \frac{g^2}{3!} \ell_3(\Psi, \Sigma_2) + \frac{g^3}{5!} \ell_4(\Sigma_2^2)
+ \sum_{k=3}^{K} \Big[ \frac{2 g^{2k-2}}{(2k)!} \mathcal W_{2k}(\cdot \otimes \Sigma_{k-1}, \Sigma_k) + \frac{g^{2k-1}}{(2k+1)!} \mathcal W_{2k+1}(\Sigma_k, \Sigma_k, \cdot) \Big] \;}
\tag{2.4}
$$

$$
\boxed{\;
\mathcal E_{\Sigma_k} = k_{k,k}(\Psi \otimes \Sigma_{k-1}) - k_{k,k}(\Sigma_k) + \frac{g}{2k+1} \mathcal W_{2k+1}(\cdot\,, \Sigma_k, \Psi) + \frac{g^2}{(2k+1)(2k+2)} \mathcal W_{2k+2}(\Psi \otimes \cdot\,, \Sigma_{k+1}), \qquad 2 \le k \le K, \;}
\tag{2.5}
$$

with the boundary cases: at $k = 2$ the source is $k_{2,2}(\Psi \otimes \Sigma_1) = p_{2,2}(\Psi^2)$ and the odd term is $\frac{g}{5} p_{3,2}(\Psi, \Sigma_2)$ (`eq:hs5:p32`); at $k = K < \infty$ the last term is absent, there being no $\Sigma_{K+1}$; in the even truncation $\widetilde S_{\le 2K}$ the odd term of $k = K$ is absent from both equations, from (2.5) at $k = K$ and from (2.4), where it is the term $\frac{g^{2K-1}}{(2K+1)!}\mathcal W_{2K+1}(\Sigma_K, \Sigma_K, \cdot)$ — at $K = 2$ the $\ell_4$ term displayed outside the sum, so that (2.4) reduces to `eq:hs4:eom-psi` only once that term is dropped. In (2.4), the $k = 2$ terms are written in the paper's product notation; in the uniform notation they read $\frac{2 \cdot 2 g^2}{4!} \mathcal V_4(\cdot \otimes \Sigma_1, \Sigma_2)$ and $\frac{g^3}{5!} \mathcal V_5(\Sigma_2, \Sigma_2, \cdot)$, the factor $2$ of (2.2) being the one boundary effect. With the dressed operator `eq:all:dressed-odd`, the middle terms of (2.5) are $- k^{(2k-1)}_{k,k;\Psi}(\Sigma_k)$:

$$
\mathcal E_{\Sigma_k} = k_{k,k}(\Psi \otimes \Sigma_{k-1}) - k^{(2k-1)}_{k,k;\Psi}(\Sigma_k) + \frac{a_{k+1}}{a_k} \, k_{k+1,k+1}(\Psi \otimes \cdot)^{\mathsf T}(\Sigma_{k+1}),
\tag{2.6}
$$

where $k_{k+1,k+1}(\Psi \otimes \cdot)^{\mathsf T} : \mathcal H^{\wedge(k+1)} \to \mathcal H^{\wedge k}$ is the transpose of the source map with respect to the pairings (`eq:conv:transpose`), $\langle A, k_{k+1,k+1}(\Psi\otimes\cdot)^{\mathsf T} B \rangle_k = \langle k_{k+1,k+1}(\Psi \otimes A), B \rangle_{k+1}$: this is the block $-\mathcal K_{k,k+1;\Psi}/a_k$ of `eq:all:blocks`, so (2.6) is the row $k$ of the block-tridiagonal system $\mathcal K_\Psi \Sigma = $ source of `eq:all:tridiagonal`. (C3.1, C3.2)

**The quotients (C3.3).** Let $N_j \in \ker k_{j,j}$. (i) $\mathcal E_{\Sigma_k}$ is unchanged under $\Sigma_j \to \Sigma_j + N_j$ for every $j$: for $j = k$, $k_{k,k}(N_k) = 0$ and $\mathcal W_{2k+1}(\cdot, N_k, \Psi) = 0$ by the first clause of `eq:hs8:kernel-condition`; for $j = k-1$, $k_{k,k}(\Psi \otimes N_{k-1}) = 0$ by the second clause; for $j = k+1$, $\langle A, \mathcal W_{2k+2}(\Psi \otimes \cdot, N_{k+1}) \rangle_k = \langle k_{k+1,k+1}(\Psi \otimes A), N_{k+1} \rangle_{k+1} = 0$ by the symmetry of $k_{k+1,k+1}$. (ii) $\langle N_k, \mathcal E_{\Sigma_k} \rangle_k = 0$ identically: the two $k_{k,k}$ terms by symmetry, the odd term by the first clause, the exchange term by $\langle N_k, \mathcal W_{2k+2}(\Psi\otimes\cdot, \Sigma_{k+1})\rangle_k = \langle k_{k+1,k+1}(\Psi \otimes N_k), \Sigma_{k+1}\rangle_{k+1} = 0$, the second clause. (iii) $\mathcal E_\Psi$ is unchanged under kernel shifts by the same clauses (this is `eq:all:kernel-shift` of the paper). Hence under the kernel condition the equations $\mathcal E_{\Sigma_k} = 0$ are exactly the stationarity conditions on the quotients: no component is lost and no spurious equation is added. Without the condition, (ii) fails and the equation along $N_k$ is the one of `eq:hs8:rational`, with a field-dependent mass of order $g$. (C3.3, conditional on the hypotheses of A5)

**The top field (C3.4).** At $k = K$, (2.6) without its last term is $k_{K,K}(\Psi \otimes \Sigma_{K-1}) - k^{(2K-1)}_{K,K;\Psi}(\Sigma_K)$, which is the bracket of `eq:all:eom-top`; the paper's display carries the prefactor $2 a_K$ of (2.3) in front, while (2.5) follows the normalization of the lower-order sections (A3). The solution is $\Sigma_K^* = (k^{(2K-1)}_{K,K;\Psi})^{-1} \circ k_{K,K}(\Psi \otimes \Sigma_{K-1})$, and substituting it in the level-$K$ terms of (1.1), which equal $- a_K \langle \Sigma_K, k^{(2K-1)}_{K,K;\Psi}\Sigma_K\rangle_K + 2 a_K \langle \Sigma_K, u_K\rangle_K$ with $u_K := k_{K,K}(\Psi \otimes \Sigma_{K-1})$, gives $- a_K \langle u_K, (k^{(2K-1)}_{K,K;\Psi})^{-1} u_K \rangle_K + 2 a_K \langle u_K, (k^{(2K-1)}_{K,K;\Psi})^{-1} u_K\rangle_K = + a_K \langle u_K, (k^{(2K-1)}_{K,K;\Psi})^{-1} u_K \rangle_K$, which is the induced term of `eq:all:eliminate-top`. (C3.4)

**Order-by-order solvability at $K = \infty$ (C3.5).** Expand $\Sigma_k = \sum_{m \ge 0} g^m \Sigma_k^{[m]}$ with $\Sigma_1^{[m]} = \delta_{m,0}\Psi$. The coefficient of $g^m$ in $\mathcal E_{\Sigma_k} = 0$ is

$$
k_{k,k}\big(\Sigma_k^{[m]}\big) = k_{k,k}\big(\Psi \otimes \Sigma_{k-1}^{[m]}\big) + \frac{1}{2k+1} \mathcal W_{2k+1}\big(\cdot\,, \Sigma_k^{[m-1]}, \Psi\big) + \frac{1}{(2k+1)(2k+2)} \mathcal W_{2k+2}\big(\Psi \otimes \cdot\,, \Sigma_{k+1}^{[m-2]}\big),
\tag{2.7}
$$

with negative-order coefficients zero. At $m = 0$: $k_{k,k}(\Sigma_k^{[0]}) = k_{k,k}(\Psi \otimes \Sigma_{k-1}^{[0]})$, whence $\Sigma_k^{[0]} = \Psi^k$ on the quotient by induction on $k$ (`eq:all:same-form`). For $m \ge 1$ the right-hand side involves only coefficients already determined when the pairs $(m', k')$ are ordered by $m'$ first and $k'$ second: $(m, k-1)$, $(m-1, k)$, $(m-2, k+1)$. Each $\Sigma_k^{[m]}$ is therefore obtained by one inversion of the bare $k_{k,k}$ on its quotient, and is a polynomial in $\Psi$, homogeneous of degree $k + m$ (homogeneity of block 1). At finite $K$ the same recursion holds with $\Sigma_{K+1} := 0$, and by block 1 the two recursions agree on $[g^m]\Sigma_k$ for $K \ge k + \lfloor m/2 \rfloor$. In the rescaled variables the $\Psi$ equation at order $g^m$ likewise involves finitely many fields. (C3.5)

$$
\Sigma_k^{[1]} = \frac{1}{2k+1} k_{k,k}^{-1} \mathcal W_{2k+1}(\cdot\,, \Psi^k, \Psi) + \Psi \otimes \Sigma_{k-1}^{[1]}, \qquad \Sigma_1^{[1]} = 0,
\tag{2.8}
$$

the first correction, a sum over the odd vertices of the levels $2, \ldots, k$ (the level $j < k$ contributions reach $\Sigma_k$ through the source).

### Commentary

- (2.1), second line: the three slots of $\mathcal W_{2k}(\Sigma_k, \Psi \otimes \Sigma_{k-1})$ hold three different fields for $k \ge 3$; each variation is read through the pairing of its own strand number by the open-slot convention, which is the paper's in `eq:hs6:eom`.
- (2.2): at $k = 2$ the slot $\Psi \otimes \Sigma_1$ is $\Psi^2$, so $\delta(\Psi^2) = 2\,\delta\Psi \otimes \Psi$ (symmetrized); the factor $2$ is why the $k = 2$ term of (2.4) is $\frac{g^2}{3!}\ell_3$ and not $\frac{2g^2}{4!}\ell_3$, matching `eq:hs4:eom-psi`. It is the only place where the general pattern has a boundary factor.
- (2.5), exchange term: positive sign and coefficient $a_{k+1}/a_k$, as in `eq:hs6:eom-sigma2` ($g^2/30$ at $k = 2$); the odd term's sign is that of `eq:hs5:eom-sigma` ($+ g/5$). The form (2.6) shows that these two terms are exactly $-k^{(2k-1)}_{k,k;\Psi}(\Sigma_k)$ plus the transpose of the next source.
- (2.7): at order $g^m$ the equation of $\Sigma_k$ is an inhomogeneous linear equation with the bare operator; the dressing and the exchange only feed lower-order coefficients forward. This is the precise sense in which the $K = \infty$ system is "triangular": not in the field index alone (the Hessian is tridiagonal), but in the order $(m, k)$.

### Result

Equations (2.4), (2.5), boxed above, with their boundary cases; (2.6) their form through the dressed operator and the source transpose; (2.7) the order-by-order recursion.

### Verification

Script checks `C3.1-psi-K{2,3,4}`, `C3.2-sigma{k}-K{K}` (odd and even truncations): the stated equations against the complex-step gradient of the action in the finite-dimensional model, at random fields and random $g$, for random block-symmetric $\mathcal W_n$ up to $n = 9$; break legs on the coefficient $1/56$, on the factor $2$ of (2.2) and on the sign of the exchange term. `C3.4-eliminate-top`: the elimination identity at $K = 3, 4$. `C3.5-order-by-order`: the recursion (2.7) summed to high order at small $g$ against the exact linear solve of the action's stationarity.

## Block 3 — First orders through $\Sigma_3$ (C4)

### Setup

Uses A1–A3. Instance $K = 3$ of (2.4)–(2.5), the septic action $\widetilde S_{\le 7}$ (`eq:hs7:action-6` plus `eq:hs7:S7tilde`), that is the truncation of $\widetilde S_\infty$ at $g^5$. The $K = 2$ instance (quintic action, truncation at $g^3$) is `eq:hs5:eom` and is contained below by dropping $\Sigma_3$.

### Derivation

From (2.4) with $K = 3$:

$$
\mathcal E_\Psi = Q_B\Psi + \frac{g}{2}\ell_2(\Psi^2) + \frac{g^2}{3!}\ell_3(\Psi, \Sigma_2) + \frac{g^3}{5!}\ell_4(\Sigma_2^2) + \frac{2 g^4}{6!}\mathcal W_6(\cdot \otimes \Sigma_2, \Sigma_3) + \frac{g^5}{7!}\mathcal W_7(\Sigma_3, \Sigma_3, \cdot) .
\tag{3.1}
$$

From (2.5) with $k = 2$ (source $p_{2,2}(\Psi^2)$, odd term $\tfrac{g}{5}p_{3,2}(\Psi,\Sigma_2)$, exchange of $\Sigma_3$):

$$
\mathcal E_{\Sigma_2} = p_{2,2}(\Psi^2) - p_{2,2}(\Sigma_2) + \frac{g}{5} p_{3,2}(\Psi, \Sigma_2) + \frac{g^2}{30}\mathcal W_6(\Psi \otimes \cdot\,, \Sigma_3) .
\tag{3.2}
$$

From (2.5) with $k = 3 = K$ (no exchange term):

$$
\mathcal E_{\Sigma_3} = k_{3,3}(\Psi \otimes \Sigma_2) - k_{3,3}(\Sigma_3) + \frac{g}{7}\mathcal W_7(\cdot\,, \Sigma_3, \Psi) = k_{3,3}(\Psi \otimes \Sigma_2) - k^{(5)}_{3,3;\Psi}(\Sigma_3) .
\tag{3.3}
$$

(3.1) is `eq:hs6:eom-psi` plus the $\mathcal W_7$ term; (3.2) is `eq:hs6:eom-sigma2`; (3.3) is `eq:hs7:saddle-3`. The first orders of the solutions, from (2.7)–(2.8):

$$
\begin{aligned}
\Sigma_2^* &= \Psi^2 + \frac{g}{5} p_{2,2}^{-1} p_{3,2}(\Psi, \Psi^2) + O(g^2), \\
\Sigma_3^* &= \Psi^3 + g \Big[ \Psi \otimes \frac{1}{5} p_{2,2}^{-1} p_{3,2}(\Psi, \Psi^2) + \frac{1}{7} k_{3,3}^{-1} \mathcal W_7(\cdot\,, \Psi^3, \Psi) \Big] + O(g^2),
\end{aligned}
\tag{3.4}
$$

where the $O(g^2)$ of $\Sigma_2^*$ contains the $\Sigma_3$ exchange, $\frac{1}{30} p_{2,2}^{-1}\mathcal W_6(\Psi\otimes\cdot, \Psi^3)$, plus the iterate of the quintic dressing, $\frac{1}{25}(p_{2,2}^{-1}p_{3,2}(\Psi,\cdot))^2\Psi^2$. The first line is `eq:hs5:saddle` expanded; the second shows the two routes by which the order-$g$ correction reaches $\Sigma_3$: through its source (the correction of $\Sigma_2$) and through its own odd vertex.

### Commentary

- (3.2): the coefficient $g^2/30 = a_3/a_2$ is the one of `eq:hs6:eom-sigma2`; the $\Sigma_3$ exchange appears in the $\Sigma_2$ equation at the sextic order already, while $\mathcal W_7$ reaches $\Sigma_2$ only through $\Sigma_3^*$, at order $g^3$ in $\Sigma_2^*$.
- (3.4): $p_{2,2}^{-1}$ and $k_{3,3}^{-1}$ are the inverses on the quotients (A5).

### Result

Equations (3.1)–(3.3): the equations of motion of the septic action, i.e. the first orders of (2.4)–(2.5) through $\Sigma_3$.

### Verification

`C4-septic-*`: (3.1)–(3.3) against the gradient of $\widetilde S_{\le 7}$ in the model; `C4-sigma-first-order`: (3.4) against the order-by-order solution.

## Block 4 — The octic instance and the triangular structure (C5, C6)

### Setup

Uses A1–A3, C2.1. The octic action $\widetilde S_{\le 8}$ of `02-6-octic.tex` is $\widetilde S_{\le 7} + \widetilde S_8$ with `eq:hs8:S8tilde`: the truncation of $\widetilde S_\infty$ at $g^6$, i.e. $K = 4$ in its even truncation (1.5), without the coupling $\mathcal W_9(\Sigma_4, \Sigma_4, \Psi)$. Written out, with `eq:hs8:kinetic`,

$$
\begin{aligned}
\widetilde S_{\le 8} - S_{\le 3} ={}& - \frac{g^2}{4!}\mathcal V_4(\Sigma_2^2) + \frac{2g^2}{4!}\mathcal V_4(\Sigma_2, \Psi^2) + \frac{g^3}{5!}\mathcal V_5(\Sigma_2^2, \Psi) \\
& - \frac{g^4}{6!}\langle \Sigma_3, k_{3,3}(\Sigma_3)\rangle_3 + \frac{2g^4}{6!}\langle \Sigma_3, k_{3,3}(\Psi \otimes \Sigma_2)\rangle_3 + \frac{g^5}{7!}\mathcal W_7(\Sigma_3, \Sigma_3, \Psi) \\
& - \frac{g^6}{8!}\langle \Sigma_4, k_{4,4}(\Sigma_4)\rangle_4 + \frac{2g^6}{8!}\langle \Sigma_4, k_{4,4}(\Psi \otimes \Sigma_3)\rangle_4 .
\end{aligned}
\tag{4.0}
$$

### Derivation

Instances of (2.4) and (2.5) with $K = 4$, the odd term of $k = 4$ dropped:

$$
\mathcal E^{(6)}_\Psi = Q_B\Psi + \frac{g}{2}\ell_2(\Psi^2) + \frac{g^2}{3!}\ell_3(\Psi, \Sigma_2) + \frac{g^3}{5!}\ell_4(\Sigma_2^2) + \frac{2g^4}{6!}\mathcal W_6(\cdot \otimes \Sigma_2, \Sigma_3) + \frac{g^5}{7!}\mathcal W_7(\Sigma_3, \Sigma_3, \cdot) + \frac{2g^6}{8!}\mathcal W_8(\cdot \otimes \Sigma_3, \Sigma_4),
\tag{4.1}
$$

$$
\mathcal E^{(6)}_{\Sigma_2} = p_{2,2}(\Psi^2) - p_{2,2}(\Sigma_2) + \frac{g}{5}p_{3,2}(\Psi, \Sigma_2) + \frac{g^2}{30}\mathcal W_6(\Psi \otimes \cdot\,, \Sigma_3),
\tag{4.2}
$$

$$
\mathcal E^{(6)}_{\Sigma_3} = k_{3,3}(\Psi \otimes \Sigma_2) - k_{3,3}(\Sigma_3) + \frac{g}{7}\mathcal W_7(\cdot\,, \Sigma_3, \Psi) + \frac{g^2}{56}\mathcal W_8(\Psi \otimes \cdot\,, \Sigma_4),
\tag{4.3}
$$

$$
\mathcal E^{(6)}_{\Sigma_4} = k_{4,4}(\Psi \otimes \Sigma_3) - k_{4,4}(\Sigma_4).
\tag{4.4}
$$

Each term of (4.1)–(4.4) is the variation of one term of (4.0), in the order of (4.0): the seven terms of (4.1) are the $\Psi$-variations of $S_{\le 3}$ (two terms), of the quartic source, of the quintic coupling, of the sextic source, of the septic coupling and of the octic source; (4.2) collects the quartic source, the quartic kinetic term, the quintic coupling and the sextic source; (4.3) the sextic source, the sextic kinetic term, the septic coupling and the octic source; (4.4) the octic source and the octic kinetic term. The normalizations are $2a_2 = g^2/12$, $2a_3 = g^4/360$, $2a_4 = g^6/20160$ (A3). Consistency: (4.4) is `eq:hs8:saddle-4`; (4.3) without its last term is `eq:hs7:saddle-3`; (4.2) is `eq:hs6:eom-sigma2`; (4.1) through $g^4$ is `eq:hs6:eom-psi`. The coefficients $1/30$ and $1/56$ are $a_3/a_2 = 4!/6!$ and $a_4/a_3 = 6!/8!$, the same numbers as in the dressed operators `eq:hs6:dressed-2`, `eq:hs8:dressed-3`, since the exchange term of the equation of $\Sigma_k$ is the transpose of the source of $\Sigma_{k+1}$ and the dressed operator of $\Sigma_k$ is what that source produces once $\Sigma_{k+1}$ is eliminated. (C5)

**The triangular structure (C6).** The equations (4.2)–(4.4) of the auxiliary fields are linear in the tower $(\Sigma_2, \Sigma_3, \Sigma_4)$, and each couples its field to its two neighbours only:

| equation | source (lighter fields) | own field | heavier neighbour |
|---|---|---|---|
| $\mathcal E_{\Sigma_2}$ | $p_{2,2}(\Psi^2)$ | $-k^{(3)}_{2,2;\Psi}(\Sigma_2)$ | $\tfrac{g^2}{30}\mathcal W_6(\Psi\otimes\cdot, \Sigma_3)$ |
| $\mathcal E_{\Sigma_3}$ | $k_{3,3}(\Psi \otimes \Sigma_2)$ | $-k^{(5)}_{3,3;\Psi}(\Sigma_3)$ | $\tfrac{g^2}{56}\mathcal W_8(\Psi\otimes\cdot, \Sigma_4)$ |
| $\mathcal E_{\Sigma_4}$ | $k_{4,4}(\Psi \otimes \Sigma_3)$ | $-k_{4,4}(\Sigma_4)$ | — |

This is the block-tridiagonal system `eq:all:tridiagonal`, and the triangular form of `02-5-septic.tex` is read off it in two ways. At fixed $g$, the last row contains no heavier field, so it is solved first, $\Sigma_4 = \Psi \otimes \Sigma_3$ on the quotient; substituting in the row above turns its heavier-neighbour term into $\frac{g^2}{56}\mathcal W_8(\Psi\otimes\cdot, \Psi\otimes\Sigma_3)$, a correction of the operator acting on $\Sigma_3$, which is the dressing `eq:hs8:dressed-3`; the row of $\Sigma_3$ is then solved, and the row of $\Sigma_2$ in its turn, with `eq:hs8:dressed-2`. Each step inverts one operator and the operator of each step is the one of the previous step dressed by the exchange just eliminated: the Gaussian elimination of a tridiagonal system from the bottom. Order by order in $g$, (2.7) makes the system strictly triangular in the order $(m, k)$: the heavier neighbour enters with $g^2$, the own-field dressing with $g$, so that $[g^m]\Sigma_k$ needs only coefficients of lower order or of the lighter field at the same order. The $\Psi$ equation (4.1) is the only one that involves every field and is non-linear; it is not part of the elimination, and once the tower is eliminated it becomes the equation of motion of the eliminated action, `eq:all:eom-recovered`.

The sources are triangular in the paper's sense: the source of $\Sigma_k$ is linear in $\Sigma_{k-1}$ and $\Psi$, and the coupling of $\Sigma_k$ to $\Sigma_{k+1}$ is the source of $\Sigma_{k+1}$ read the other way (the transpose, (2.6)). At the leading order every solution lies on the diagonal, $\Sigma_k = \Psi^k + O(g)$, by `eq:all:same-form` applied row by row from the top of the table. (C6)

### Commentary

- (4.0)–(4.4): the only inputs are the paper's displays `eq:hs7:action-6`, `eq:hs7:S7tilde`, `eq:hs8:S8tilde`, `eq:hs8:kinetic` and the variation rules (2.1)–(2.2).
- The table makes the two dressings of `02-6-octic.tex` visible as equations: the exchange term in the row of $\Sigma_k$ becomes the $g^2$ term of the dressed operator of $\Sigma_k$ once the next row is solved.

### Result

Equations (4.1)–(4.4), the equations of motion of the octic cubic action with every term explicit; the table, their triangular (block-tridiagonal) structure.

### Verification

`C5-octic-{psi,sigma2,sigma3,sigma4}`: (4.1)–(4.4) against the gradient of (4.0) in the model. `C6-closure-g{2..6}`: the order-by-order solution of (4.2)–(4.4) substituted in (4.0), with $\mathcal W_6, \mathcal W_7, \mathcal W_8$ fixed by `eq:all:diagonal`, reproduces $[g^m]S$ for $m \le 6$; `C6-break-undressed-W8` (closure fails at $g^6$ with $\mathcal W_8 = \mathcal V_8$) and `C6-break-coefficient` (fails with $1/56 \to 1/55$); `C6-top-first`: solving from the top at fixed $g$ equals the joint solve.

## Verification

Script: `codes/verify-all-orders-eom.py` (numpy; run from the project root with `uv run --no-sync python codes/verify-all-orders-eom.py [seed]`). Model: $\mathcal H = \mathbb R^3$, $\Sigma_k \in \mathrm{Sym}^k$ in an orthonormal basis ($D_2, D_3, D_4 = 6, 10, 15$), Euclidean pairing, $Q_B$ a random symmetric matrix, $\mathcal V_3, \mathcal V_4, \mathcal V_5, \mathcal V_6$ random fully symmetric tensors, $\mathcal V_7, \mathcal V_8, \mathcal V_9$ random sums of rank-one symmetric tensors; for the equation-of-motion checks (part A) the dressed forms $\mathcal W_6, \ldots, \mathcal W_9$ are random block-symmetric forms (symmetric matrices on $\mathrm{Sym}^k$, arrays symmetric in the two $\mathrm{Sym}^k$ slots), i.e. exactly the symmetry of A2; for the closure checks (part B) they are built by the diagonal rule `eq:all:diagonal` from the $\mathcal V_n$ (polynomial fit of the mismatch, polarization). Gradients of the action by complex step (exact to machine precision for a polynomial). Runs: seeds 20261018 and 41, **53/53 PASS** each, exit 0 (`agent/scratch/computator/computator-100-all-orders-eom-20261018T020000/run-{20261018,41}.log`); wall time 1.4 s, maximum resident set size 41 MB, one process.

| check | node | what is compared | result |
|---|---|---|---|
| `C1.1-series-equals-level-sum-K{2,3,4}-{odd,even}` | C1.1, C2.1 | action from the coefficients (1.2) against the level sum | PASS, $\le 4 \cdot 10^{-18}$ |
| `C3.1-psi-K{2,3,4}-{odd,even}` | C3.1 | (2.4) against $\partial \widetilde S/\partial\Psi$ | PASS, rel $\le 4 \cdot 10^{-16}$ |
| `C3.2-sigma{k}-K{K}-{odd,even}` | C3.2 | (2.5) $\times 2 a_k$ against $\partial\widetilde S/\partial\Sigma_k$, all $k \le K \le 4$, both truncations | PASS, rel $\le 3 \cdot 10^{-16}$ |
| `C4-septic-{psi,sigma2,sigma3}` | C4 | (3.1)–(3.3) against the gradient of $\widetilde S_{\le 7}$ | PASS |
| `C5-octic-{psi,sigma2,sigma3,sigma4}` | C5 | (4.1)–(4.4) against the gradient of (4.0) | PASS |
| `C3.2-break-coef56-detected`, `C3.2-break-sign-detected`, `C3.1-break-factor2-detected` | C3.1, C3.2 | $1/56 \to 1/55$, exchange sign flipped, $g^2/3! \to 2g^2/4!$: the comparison then fails (rel $6 \cdot 10^{-5}$, $7 \cdot 10^{-3}$, $2 \cdot 10^{-2}$) | PASS (detected) |
| `C3.4-eliminate-top-K{3,4}` | C3.4 | solution of the stated top equation has zero residual; the action on it equals `eq:all:eliminate-top` | PASS, $\le 10^{-14}$ |
| `C3.5-order-by-order`, `C3.5-leading-order-diagonal` | C3.5 | recursion (2.7) to $g^{14}$ summed at $g = 0.01$ against the exact stationary tower obtained from the action's gradient alone (linear solve); $[g^0]\Sigma_k = \Psi^k$ | PASS, rel $3 \cdot 10^{-15}$ |
| `C6-top-first` | C6 | solving (4.4), then (4.3) with `eq:hs8:dressed-3`, then (4.2) with `eq:hs8:dressed-2` at $g = 0.3$ against the joint solve | PASS, rel $2 \cdot 10^{-15}$ |
| `C4-sigma-first-order` | C4 | (3.4), including the $O(g^2)$ of $\Sigma_2^*$, against the recursion | PASS, rel $8 \cdot 10^{-16}$ |
| `C1.3-stabilization` | C1.3 | $K = 3$ (odd) against $K = 4$ (even): $[g^m]\Sigma_2^*$ equal for $m \le 3$, different at $m = 4$; $[g^m]$ value equal for $m \le 5$, different at $m = 6$ | PASS (differences $5 \cdot 10^{-3}$) |
| `C6-closure-g{0..6}` | C6, C2.2 | octic action, order-by-order solution of (4.2)–(4.4) substituted in (4.0), with $\mathcal W_6, \mathcal W_7, \mathcal W_8$ from the diagonal rule run on the lower towers: $[g^m] = \mathcal V_{m+2}(\Psi^{m+2})/(m+2)!$, fresh random $\Psi$ | PASS, $\le 10^{-7}$ (actual $\sim 10^{-14}$) |
| `C6-remainder-g7-nonzero-without-W9`, `C2.2-closure-g7-with-W9` | C2.2 | the even truncation misses $g^7$ (difference $0.8$); with $\mathcal W_9$ the odd truncation closes through $g^7$ | PASS |
| `C6-break-undressed-W8` | C6 | $\mathcal W_8 = \mathcal V_8$: $g^{\le 5}$ unchanged, $g^6$ fails by $6 \cdot 10^{-2}$ | PASS (detected) |
| `C6-break-diagonal-rule` | C6 | $n!$ of the rule halved for $\mathcal W_8$: $g^6$ fails by $3 \cdot 10^{-2}$ | PASS (detected) |
| `C6-break-coefficient-solution-not-value` | C6 | $1/56 \to 1/55$ in the recursion changes $[g^2]\Sigma_3$ by $9 \cdot 10^{-2}$ and the value through $g^6$ not at all ($3 \cdot 10^{-14}$; the change is $O(g^8)$ by stationarity, $g^7$ not computed) | PASS (as predicted) |

The last line records a limitation found while writing the break legs: by stationarity, a wrong coefficient in an auxiliary equation changes the value of the action only at second order in the induced error of the solution, here at $O(g^8)$; the closure checks therefore test the action (the dressed vertices, the collapse coefficient $1/(2k)!$) and not the equations, which are tested against the gradient in part A. Both kinds of check are present.

What the finite-dimensional model does not test: Grassmann parity and ghost number (every field is even, every pairing symmetric: the Koszul signs of `eq:conv:pairing-n` are trivial here, as they are for the even fields of the paper); the kernel condition and the quotient prescription (every $\mathcal W_{2k}$ of the model is invertible, so C3.3 and C1.2 are not exercised); the string-vertex origin of the forms (no relation among the $\mathcal V_n$ is used); the convergence of any series in $g$; dimensional analysis (the model is dimensionless; in the paper every term of (1.1) carries $g^{n-2}$ with $n$ strands, the homogeneity $\Psi \to t\Psi$, $\Sigma_k \to t^k\Sigma_k$, $g \to g/t$ noted in `03-all-orders.tex` is manifest in (1.2) and in (2.4)–(2.5), where every term of $\mathcal E_\Psi$ scales as $t$ and every term of $\mathcal E_{\Sigma_k}$ as $t^k$ under it).

Limiting cases checked by hand: $K = 2$ odd reduces (2.4)–(2.5) to `eq:hs5:eom`; $K = 2$ even, with the $\ell_4$ term of (2.4) and the odd term of (2.5) dropped (even-truncation boundary, after (2.5)), to `eq:hs4:eom`; $g = 0$ gives $\Sigma_k = \Psi^k$ and $\mathcal E_\Psi = Q_B\Psi$.

## For the writers

Displays ready to transcribe, with the macros of `03-all-orders.tex`. Labels are suggestions. Prose around them is the writer's; the record's claim is named for each.

**Finding to settle first (A3).** The paper uses two normalizations of the auxiliary equations: sections 2.2–2.6 define $\mathcal E_{\Sigma_k}$ with coefficient one on the source (`eq:hs4:eom-sigma`, `eq:hs5:eom-sigma`, `eq:hs6:eom-sigma2`, `eq:hs7:saddle-3`, `eq:hs8:saddle-4`), while `eq:all:eom-top` carries the prefactor $2\gs^{2K-2}/(2K)!$ inside $\mathcal E_{\Sigma_K}$. The displays below use the sections' convention, stated once as $\delta\caction = \pair{\delta\Psi}{\mathcal E_\Psi} + \sum_k \frac{2\gs^{2k-2}}{(2k)!}\pair[k]{\delta\Sigma_k}{\mathcal E_{\Sigma_k}}$. Recommendation: drop the prefactor from `eq:all:eom-top` (then it is the $k = K$ case of `eq:all:eom-sigma-dressed` below) and keep the sentence "up to the factor $\gs^2/12$" out.

**(C1) The action at $K = \infty$.**

```latex
\begin{equation}
  \label{eq:all:action-infty}
  \begin{aligned}
    \caction[\infty]
      &
      = S_{\le 3}
        + \sum_{k \ge 2} \Big[
          - \frac{\gs^{2 k - 2}}{(2 k)!} \, \pair[k]{\Sigma_k}{\kin{k}{}{2 k - 2}(\Sigma_k)}
          + \frac{2 \gs^{2 k - 2}}{(2 k)!} \, \pair[k]{\Sigma_k}{\kin{k}{}{2 k - 2}(\Psi \otimes \Sigma_{k - 1})}
      \\ &
      \qquad\qquad\quad
          + \frac{\gs^{2 k - 1}}{(2 k + 1)!} \, \dvertex{2 k + 1}(\Sigma_k, \Sigma_k, \Psi)
        \Big],
    \qquad
    \Sigma_1
      := \Psi,
  \end{aligned}
\end{equation}
```

Sense in which it is well defined (C1.1): it is a formal power series in $\gs$, $\caction[\infty] = \sum_{m \ge 0} \gs^m \, \widetilde{S}_{[m]}$, each coefficient a polynomial of degree at most three in finitely many fields, with exactly two terms at every even order and one at every odd order,

```latex
\begin{equation}
  \label{eq:all:orders}
  \widetilde{S}_{[2 k - 2]}
    = \frac{1}{(2 k)!} \Big[ 2 \, \pair[k]{\Sigma_k}{\kin{k}{}{2 k - 2}(\Psi \otimes \Sigma_{k - 1})} - \pair[k]{\Sigma_k}{\kin{k}{}{2 k - 2}(\Sigma_k)} \Big],
  \qquad
  \widetilde{S}_{[2 k - 1]}
    = \frac{1}{(2 k + 1)!} \, \dvertex{2 k + 1}(\Sigma_k, \Sigma_k, \Psi),
  \qquad
  k \ge 2,
\end{equation}
```

with $\widetilde S_{[0]} = \tfrac12 \pair{\Psi}{Q_B \Psi}$ and $\widetilde S_{[1]} = \tfrac{1}{3!}\vertex{3}(\Psi^3)$. The field $\Sigma_k$ enters at order $\gs^{2k-2}$ and the coefficient of $\gs^m$ involves $\Psi$, $\Sigma_{\lfloor m/2 \rfloor + 1}$ and, at even $m$, $\Sigma_{\lfloor m/2\rfloor}$ only; the auxiliary fields live on $\Hn{k}/\ker \kin{k}{}{2k-2}$ as before. Conditions (C1.2–C1.4, to be stated, not weakened): the same as at finite $K$ — bare operators invertible on their quotients, the condition `eq:hs8:kernel-condition`, each level introduced through one form `eq:all:square` — plus the existence of $\dvertex{n}$ for every $n$, which is the recursion `eq:all:diagonal`. At $K = \infty$ the nested operator `eq:all:nested` has no top and is defined coefficientwise, $[\gs^m]\kin{k}{\Psi}{\infty}$ involving the levels $\le k + \lfloor m/2 \rfloor$ only; its inverse exists as a formal series because its $\gs^0$ term is the bare operator, so no new invertibility assumption arises; what is given up is the finite-$K$ statement that the inverse exists for $\gs\Psi$ in a neighbourhood of zero. Stabilization (C1.3): $[\gs^m]$ of the operator of $\Sigma_k$, of $\Sigma_k^*$ and of the value are independent of $K$ for $K \ge k + \lfloor m/2 \rfloor$, $K \ge k + \lfloor m/2 \rfloor$ and $K \ge 1 + \lfloor m/2 \rfloor$ respectively, for the odd truncation $\caction[2K+1]$; for the even one $\caction[2K]$ replace $\lfloor m/2 \rfloor$ by $\lceil m/2 \rceil$ (the top level has no odd dressing); the bounds hold whenever the bare inverses exist on the quotients; hence (C1.4) $\caction[\infty]|_{\text{solution}} = S$ as formal power series, under the hypotheses of the matching statement.

**(C2) The truncation at $K$.**

```latex
\begin{equation}
  \label{eq:all:truncation}
  \caction[\le 2 K + 1]
    = \sum_{m = 0}^{2 K - 1} \gs^m \, \widetilde{S}_{[m]},
  \qquad
  \caction[\le 2 K]
    = \sum_{m = 0}^{2 K - 2} \gs^m \, \widetilde{S}_{[m]}
    = \caction[\le 2 K + 1] - \frac{\gs^{2 K - 1}}{(2 K + 1)!} \, \dvertex{2 K + 1}(\Sigma_K, \Sigma_K, \Psi).
\end{equation}
```

Sentence: the action with the fields $\Sigma_2, \ldots, \Sigma_K$ is the truncation of `eq:all:action-infty` at order $\gs^{2K-1}$, the even truncation at $\gs^{2K-2}$, which drops the odd coupling of $\Sigma_K$ alone; on the solution they reproduce $S_{\le 2K+1}$ up to $O(\gs^{2K})$ and $S_{\le 2K}$ up to $O(\gs^{2K-1})$, the remainder being the order of the first term left out (C2.2, `eq:all:recovered`, `eq:hs8:eliminate`).

**(C3) The general equations of motion** (normalization of A3 stated in the text; boundary cases in the sentence after).

```latex
\begin{subequations}
  \label{eq:all:eom}
  \begin{align}
    \label{eq:all:eom-psi}
    \mathcal E_\Psi
      &
      = Q_B \Psi
        + \frac{\gs}{2} \, \ell_2(\Psi^2)
        + \frac{\gs^2}{3!} \, \ell_3(\Psi, \Sigma_2)
        + \frac{\gs^3}{5!} \, \ell_4(\Sigma_2^2)
    \notag
    \\ &
    \quad
        + \sum_{k = 3}^{K} \Big[
          \frac{2 \gs^{2 k - 2}}{(2 k)!} \, \dvertex{2 k}(\, \cdot \, \otimes \Sigma_{k - 1}, \Sigma_k)
          + \frac{\gs^{2 k - 1}}{(2 k + 1)!} \, \dvertex{2 k + 1}(\Sigma_k, \Sigma_k, \, \cdot \,)
        \Big],
    \\
    \label{eq:all:eom-sigma}
    \mathcal E_{\Sigma_k}
      &
      = \kin{k}{}{2 k - 2}(\Psi \otimes \Sigma_{k - 1})
        - \kin{k}{}{2 k - 2}(\Sigma_k)
        + \frac{\gs}{2 k + 1} \, \dvertex{2 k + 1}(\, \cdot \,, \Sigma_k, \Psi)
        + \frac{\gs^2}{(2 k + 1) (2 k + 2)} \, \dvertex{2 k + 2}(\Psi \otimes \, \cdot \,, \Sigma_{k + 1}),
    \qquad
    2 \le k \le K,
  \end{align}
\end{subequations}
```

Boundary cases: at $k = 2$ the source is $\sprod{2}{2}(\Psi^2)$ and the odd term $\tfrac{\gs}{5}\sprod{3}{2}(\Psi, \Sigma_2)$; the $\Psi$ equation carries the level-2 terms with $\ell_3$ (coefficient $\gs^2/3!$ rather than $2\gs^2/4!$, because $\Psi$ fills two slots of the quartic source, the factor $2$ of (2.2)) and $\ell_4$ (the $k = 2$ odd term, generic coefficient $1/5!$); at $k = K < \infty$ the last term is absent; in the even truncation the odd term of $k = K$ is absent from both equations — from the $\Sigma_K$ equation and from the $\Psi$ equation, where at $K = 2$ it is the $\ell_4$ term, so that the quartic case `eq:hs4:eom-psi` has no $\ell_4$. The dot denotes the state paired with the open slot, as in `eq:hs6:eom`. With the dressed operator `eq:all:dressed-odd` and the transpose of the source,

```latex
\begin{equation}
  \label{eq:all:eom-sigma-dressed}
  \mathcal E_{\Sigma_k}
    = \kin{k}{}{2 k - 2}(\Psi \otimes \Sigma_{k - 1})
      - \kin{k}{\Psi}{2 k - 1}(\Sigma_k)
      + \frac{\gs^2}{(2 k + 1) (2 k + 2)} \, \dvertex{2 k + 2}(\Psi \otimes \, \cdot \,, \Sigma_{k + 1}),
\end{equation}
```

the row $k$ of the block-tridiagonal system `eq:all:tridiagonal`. Order by order (C3.5), with $\Sigma_k = \sum_m \gs^m \Sigma_k^{[m]}$ and $\Sigma_k^{[0]} = \Psi^k$,

```latex
\begin{equation}
  \label{eq:all:eom-orders}
  \kin{k}{}{2 k - 2}\big(\Sigma_k^{[m]}\big)
    = \kin{k}{}{2 k - 2}\big(\Psi \otimes \Sigma_{k - 1}^{[m]}\big)
      + \frac{1}{2 k + 1} \, \dvertex{2 k + 1}\big(\, \cdot \,, \Sigma_k^{[m - 1]}, \Psi\big)
      + \frac{1}{(2 k + 1) (2 k + 2)} \, \dvertex{2 k + 2}\big(\Psi \otimes \, \cdot \,, \Sigma_{k + 1}^{[m - 2]}\big),
\end{equation}
```

a finite recursion in $(m, k)$ at $K = \infty$: each coefficient needs the lighter field at the same order, the field itself one order down, the heavier field two orders down.

**(C4) First orders through $\Sigma_3$** ($K = 3$, the septic action; if displayed in section 3 they stop here, Harold's choice).

```latex
\begin{subequations}
  \label{eq:all:eom-3}
  \begin{align}
    \mathcal E_\Psi
      &
      = Q_B \Psi
        + \frac{\gs}{2} \, \ell_2(\Psi^2)
        + \frac{\gs^2}{3!} \, \ell_3(\Psi, \Sigma_2)
        + \frac{\gs^3}{5!} \, \ell_4(\Sigma_2^2)
        + \frac{2 \gs^4}{6!} \, \dvertex{6}(\, \cdot \, \otimes \Sigma_2, \Sigma_3)
        + \frac{\gs^5}{7!} \, \dvertex{7}(\Sigma_3, \Sigma_3, \, \cdot \,),
    \\
    \mathcal E_{\Sigma_2}
      &
      = \sprod{2}{2}(\Psi^2)
        - \sprod{2}{2}(\Sigma_2)
        + \frac{\gs}{5} \, \sprod{3}{2}(\Psi, \Sigma_2)
        + \frac{\gs^2}{30} \, \dvertex{6}(\Psi \otimes \, \cdot \,, \Sigma_3),
    \\
    \mathcal E_{\Sigma_3}
      &
      = \kin{3}{}{4}(\Psi \otimes \Sigma_2)
        - \kin{3}{}{4}(\Sigma_3)
        + \frac{\gs}{7} \, \dvertex{7}(\, \cdot \,, \Sigma_3, \Psi).
  \end{align}
\end{subequations}
```

**(C5) The octic instance** (section 2.6; `eq:hs8:saddle-4` becomes the last line).

```latex
\begin{subequations}
  \label{eq:hs8:eom}
  \begin{align}
    \label{eq:hs8:eom-psi}
    \mathcal E^{(6)}_\Psi
      &
      = Q_B \Psi
        + \frac{\gs}{2} \, \ell_2(\Psi^2)
        + \frac{\gs^2}{3!} \, \ell_3(\Psi, \Sigma_2)
        + \frac{\gs^3}{5!} \, \ell_4(\Sigma_2^2)
        + \frac{2 \gs^4}{6!} \, \dvertex{6}(\, \cdot \, \otimes \Sigma_2, \Sigma_3)
        + \frac{\gs^5}{7!} \, \dvertex{7}(\Sigma_3, \Sigma_3, \, \cdot \,)
        + \frac{2 \gs^6}{8!} \, \dvertex{8}(\, \cdot \, \otimes \Sigma_3, \Sigma_4),
    \\
    \label{eq:hs8:eom-sigma2}
    \mathcal E^{(6)}_{\Sigma_2}
      &
      = \sprod{2}{2}(\Psi^2)
        - \sprod{2}{2}(\Sigma_2)
        + \frac{\gs}{5} \, \sprod{3}{2}(\Psi, \Sigma_2)
        + \frac{\gs^2}{30} \, \dvertex{6}(\Psi \otimes \, \cdot \,, \Sigma_3),
    \\
    \label{eq:hs8:eom-sigma3}
    \mathcal E^{(6)}_{\Sigma_3}
      &
      = \kin{3}{}{4}(\Psi \otimes \Sigma_2)
        - \kin{3}{}{4}(\Sigma_3)
        + \frac{\gs}{7} \, \dvertex{7}(\, \cdot \,, \Sigma_3, \Psi)
        + \frac{\gs^2}{56} \, \dvertex{8}(\Psi \otimes \, \cdot \,, \Sigma_4),
    \\
    \label{eq:hs8:eom-sigma4}
    \mathcal E^{(6)}_{\Sigma_4}
      &
      = \kin{4}{}{6}(\Psi \otimes \Sigma_3)
        - \kin{4}{}{6}(\Sigma_4).
  \end{align}
\end{subequations}
```

Each term is the variation of one term of the octic action (4.0), in order: in the $\Psi$ equation the kinetic term and cubic vertex, the quartic source, the quintic coupling, the sextic source, the septic coupling, the octic source; in each auxiliary equation its source, its kinetic term, its odd coupling, and the source of the next field read the other way.

**(C6) The triangular structure**, as a sentence or the table of block 4: the auxiliary equations are linear in the tower and each couples $\Sigma_k$ to $\Sigma_{k-1}$ (its source), to itself (the operator dressed by the odd vertex), and to $\Sigma_{k+1}$ (the transpose of the next source, with $\gs^2$); the last equation has no heavier field and is solved first, $\Sigma_4 = \Psi \otimes \Sigma_3$; substituted in the equation of $\Sigma_3$ its exchange term becomes the $\gs^2/56$ term of `eq:hs8:dressed-3`, and the equation of $\Sigma_2$ then receives `eq:hs8:dressed-2`; the elimination from the top is the Gaussian elimination of a tridiagonal system, one inversion per level. Order by order, `eq:all:eom-orders` is strictly triangular in $(m, k)$. The $\Psi$ equation is the only non-linear one and the only one involving every field; with the tower eliminated it is the equation of motion of the recovered action, `eq:all:eom-recovered`.

**Two more remarks for the writers.** (i) `02-6-octic.tex` says of $\kin{4}{}{6}$ "it does not depend on the fields"; in the equations this is why `eq:hs8:eom-sigma4` has no $\gs$ at all. (ii) In `03-all-orders.tex` the sentence after `eq:all:nested`, "the coefficient of $\gs^m$ involves the levels $k \le m/2 + 2$ only", is the operator of $\Sigma_2$; for the value it is $k \le m/2 + 1$ and for $\Sigma_k^*$ it is $k + m/2$ (C1.3; with $\lfloor m/2 \rfloor$ for the odd truncation and $\lceil m/2 \rceil$ for the even one), should the writer want the bounds.

## Proposed ledger entries

Ledger section: ## Results

### R? — The cubic action at $K = \infty$ as a formal power series, its truncation at $K$, and the equations of motion of all fields [Proven – Verified (finite model)]

- **Source**: `agent/derivations/100-all-orders-action-eom.md#C1` (C1.1, C1.3), `#C2` (C2.1), `#C3` (C3.1, C3.2, C3.4, C3.5), `#C4`, `#C5`, `#C6` (structural part; its closure clause belongs to the next entry); blocks 1–4
- **Scope**: the cubic action `eq:all:action` of the paper with its block-symmetric dressed forms ($\mathcal W_{2k}$ symmetric on $\mathcal H^{\wedge k}$, $\mathcal W_{2k+1}$ symmetric in its two $\mathcal H^{\wedge k}$ slots), all fields Grassmann even; exact algebra, no hypothesis on the vertices; the quotient statement (C3.3), the existence of the solutions and the recursions of items (3)–(4) applied to the string objects need the kernel condition and the bare invertibility on the quotients (PH1, PH5, PH2 (b), record A5) and are not part of this entry's tag — items (3)–(4) are stated as identities valid whenever those inverses exist; machine-checked in a finite-dimensional model through $K = 4$ (ghost numbers, Grassmann signs, kernels not exercised)
- **Verification**:
  - 2026-10-18 – numerical check (complex-step gradients, tolerance $10^{-9}$, observed $\le 10^{-14}$) – `codes/verify-all-orders-eom.py`, 53/53 PASS, seeds 20261018 and 41, exit 0 (`agent/scratch/computator/computator-100-all-orders-eom-20261018T020000/run-*.log`): equations (2.4)–(2.5) against the complex-step gradient for $K = 2, 3, 4$, both truncations, with break legs; top-field elimination; order-by-order recursion against the exact stationary tower; series-coefficient form of the action

(1) $\widetilde S_\infty = S_{\le 3} + \sum_{k \ge 2}[\ldots]$ (record (1.1)–(1.2)) is a formal power series in $g_s$ with coefficient $\widetilde S_{[2k-2]} = \frac{1}{(2k)!}[2\langle\Sigma_k, k_{k,k}(\Psi\otimes\Sigma_{k-1})\rangle_k - \langle\Sigma_k, k_{k,k}\Sigma_k\rangle_k]$ and $\widetilde S_{[2k-1]} = \frac{1}{(2k+1)!}\mathcal W_{2k+1}(\Sigma_k, \Sigma_k, \Psi)$: two terms at each even order, one at each odd order, $\Sigma_k$ entering at $g_s^{2k-2}$; the truncation with $\Sigma_2, \ldots, \Sigma_K$ is the truncation of the series at $g_s^{2K-1}$ ($\widetilde S_{\le 2K+1}$) or $g_s^{2K-2}$ ($\widetilde S_{\le 2K}$, the odd coupling of $\Sigma_K$ dropped). (2) With $\delta\widetilde S = \langle\delta\Psi, \mathcal E_\Psi\rangle + \sum_k \frac{2g_s^{2k-2}}{(2k)!}\langle\delta\Sigma_k, \mathcal E_{\Sigma_k}\rangle_k$: $\mathcal E_\Psi = Q_B\Psi + \frac{g_s}{2}\ell_2(\Psi^2) + \frac{g_s^2}{3!}\ell_3(\Psi,\Sigma_2) + \frac{g_s^3}{5!}\ell_4(\Sigma_2^2) + \sum_{k\ge3}[\frac{2g_s^{2k-2}}{(2k)!}\mathcal W_{2k}(\cdot\otimes\Sigma_{k-1},\Sigma_k) + \frac{g_s^{2k-1}}{(2k+1)!}\mathcal W_{2k+1}(\Sigma_k,\Sigma_k,\cdot)]$ and $\mathcal E_{\Sigma_k} = k_{k,k}(\Psi\otimes\Sigma_{k-1}) - k_{k,k}(\Sigma_k) + \frac{g_s}{2k+1}\mathcal W_{2k+1}(\cdot,\Sigma_k,\Psi) + \frac{g_s^2}{(2k+1)(2k+2)}\mathcal W_{2k+2}(\Psi\otimes\cdot,\Sigma_{k+1})$ (last term absent at $k = K$); the $k = 2$ source is $p_{2,2}(\Psi^2)$, the $\Psi$ equation carries the factor-2 boundary effect of the quartic source. (3) The $\Sigma_k$ equations are the rows of the block-tridiagonal system `eq:all:tridiagonal`; order by order in $g_s$ they form a finite recursion in $(m, k)$ with $[g_s^0]\Sigma_k = \Psi^k$ (record (2.7)); the top-field elimination `eq:all:eom-top`, `eq:all:eliminate-top` is the $k = K$ case. (4) Stabilization, whenever the inverses exist on the quotients (A5): $[g_s^m]$ of the operator of $\Sigma_k$, of $\Sigma_k^*$ and of the value are independent of $K$ for $K \ge k + \lfloor m/2 \rfloor$, $K \ge k + \lfloor m/2\rfloor$, $K \ge 1 + \lfloor m/2 \rfloor$ for the odd truncation $\widetilde S_{\le 2K+1}$ (for the even one, $\lfloor m/2 \rfloor \to \lceil m/2 \rceil$); the $K = \infty$ objects are the coefficientwise limits, and a formal series with invertible constant term being invertible, no invertibility assumption beyond the finite-$K$ one is needed. (5) Octic instance, record (4.1)–(4.4), and septic instance (3.1)–(3.3), consistent with `eq:hs5:eom`, `eq:hs6:eom`, `eq:hs7:saddle-3`, `eq:hs8:saddle-4`. Remark for the writers (a paper defect, not a result; the clerk may drop it): `eq:all:eom-top` carries the prefactor $2g_s^{2K-2}/(2K)!$ that sections 2.2–2.6 leave out of $\mathcal E_{\Sigma_k}$.

Ledger section: ## Results

### R? — Closure of the $K = \infty$ cubic action as an identity of formal power series [Conditional(PH1, PH2 (b), PH5, PH14) + R70 – Proven]

- **Source**: `agent/derivations/100-all-orders-action-eom.md#C1.4` (with C1.3, C2.2, and the closure clause of C6 for the octic instance); blocks 1, 4
- **Scope**: within R26's ansatz and hypotheses (jointly Gaussian, shared-parent tower; finite-dimensional truncation, momenta fixed or discretized; tree level); the identity is coefficientwise, convergence of the continued fraction not addressed; the finite-$K$ analytic statement (inverses for $g_s\Psi$ near zero) is not claimed at $K = \infty$
- **Verification**:
  - 2026-10-18 – numerical check (tolerance $10^{-7}$, observed $\sim 10^{-14}$) – `codes/verify-all-orders-eom.py`, checks `C1.3-stabilization`, `C6-closure-g{0..6}`, `C2.2-closure-g7-with-W9`, `C6-break-undressed-W8`, `C6-break-diagonal-rule`: closure of the $K = 4$ tower through $g_s^7$ with the dressed vertices built by `eq:all:diagonal`, lower orders untouched by the new level, break legs detected

Under R26, $\widetilde S_\infty|_{\rm sol} = S$ as formal power series in $g_s$: by the stabilization bound (R? above, item 4), $[g_s^m]$ of the $K = \infty$ value equals that of any finite $K \ge 1 + \lfloor m/2 \rfloor$, where `eq:all:recovered` gives $[g_s^m]S$ since $m \le 2K - 1$. The truncations reproduce $S_{\le 2K+1} + O(g_s^{2K})$ and $S_{\le 2K} + O(g_s^{2K-1})$, the remainder sitting at the order of the first term left out and not vanishing in general (model: $0.8$ at $g_s^7$ for the even $K = 4$ truncation).
