# 085 — Paper gaps 3 and 4: the recovered equation of motion and closure under the universality rule

## Status

2026-10-04, fix pass after critic iteration 1 complete (all 15 findings applied, see `## Fix pass (critic iteration 1)`); script 20/20 PASS. Changed node statements: C1 (converse off shell), C2.3 (ghost-number isotropy), C2.4 (eliminated theory through the matched order); justifications: C1.4, C2, C2.1. Next: confirmation critic on C1, C2.3, C2.4, then the science-writer fills gaps 3 and 4 with the writer notes of the paragraph-ready section.

## Task and objective

**Literal task** (brief `computator-085-paper-gaps-3-4-20261004T122500`).
Gap 3 (`paper/sections/03-all-orders.tex` l. 436–446): derive that the $\Psi$-equation of the cubic action evaluated at the auxiliary solution is the equation of motion of the eliminated action (stationarity kills the chain-rule term), and that it is independent of the representative of $\Sigma_k^*$ modulo the bare kernels exactly when the kernel condition `eq:hs8:kernel-condition` holds.
Gap 4 (`paper/sections/04-gauge-bv-spectrum.tex` l. 414–424): a truncation to a subspace on which every vertex with exactly one leg outside vanishes has products closing on the subspace and inherits the $L_\infty$ relations; state the caveats.

**Motivating objective.** The paper's gap route requires a record with a critic "holds" before the two `gap` comments are filled; the deliverable is two derivations a science-writer can transcribe into one paragraph each, in the paper's notation.

## Conventions and assumptions

Paper notation: $\caction[\le 2K+1]$ the cubic action (`eq:all:action`), $\kin{k}{}{2k-2}$ the bare kinetic operator of $\Sigma_k$ (`eq:all:kinetic`), $\dvertex{2k+1}$ the dressed odd vertex, $\pair[k]{\cdot}{\cdot}$ the $k$-string pairing (C1, C6), $\ell_n$ the products (`eq:hs1:vertex-product`, C4), $\mathcal E_\Psi$ the $\Psi$-equation defined by $\delta S = \pair{\delta\Psi}{\mathcal E_\Psi}$ (`eq:hs1:eom-psi`).

- **A1** Fixed level truncation, momenta fixed or discretized: every space is finite-dimensional and every map is a finite matrix; derivatives are ordinary derivatives.
- **A2** Tower truncated at $K$: fields $\Sigma_2,\dots,\Sigma_K$, action `eq:all:action` (truncation at odd order $2K+1$; the even truncation $2K$ drops the top odd coupling).
- **A3** The bare operators $\kin{k}{}{2k-2}$ are symmetric for $\pair[k]{\cdot}{\cdot}$ (`eq:all:kinetic`, $\dvertex{2k}$ symmetric) and invertible on $\Hn{k}/\ker\kin{k}{}{2k-2}$; the pairings $\pair[k]{\cdot}{\cdot}$ are nondegenerate on $\Hn{k}$.
- **A4** Statements are formal power series in $\gs$ at tree level; at fixed truncation the solution is rational in $\gs$ and analytic at $\gs\Psi=0$ (paper, below `eq:all:nested`).
- **A5** (gap 4) A cyclic $L_\infty$ algebra $(\mathcal H,\ell_n,\omega)$ with $\omega$ nondegenerate, vertices $\vertex{n+1}(A_0,\dots,A_n)=\omega(A_0,\ell_n(A_1,\dots,A_n))$ (`eq:hs1:vertex-product`, C4).
- **A1′** (gap 4, replaces A1 there; fix pass #8) $\Hs$ is the full state space (all levels), graded by level and (fixed or discretized) momentum into finite-dimensional pieces; $\omega$ pairs the piece of level $L$ and momentum $p$ perfectly with the piece of level $L$ and momentum $-p$; $U$ is spanned by states of definite level and momentum. A1 and A5 cannot hold together for strings: a level-truncated SFT is not a cyclic $L_\infty$ algebra (the paper's l. 409–413), so the lemma is about subspaces of the full theory, not about a level truncation.

No new hypotheses. The kernel condition `eq:hs8:kernel-condition` is the premise of C1.1 (existence) and C1.3 (⇐); for the string vertices it is, at $k=2$, PH5's $V_5$ clause (clause 1) and PH2 (b)'s $T_6$ clause (clause 2) (R26 annotation 2026-10-01), at $k\ge3$ the paper's standing assumption. C1.4 cites the matching statement `eq:all:recovered` (R26, conditional on PH1, PH2 (b), PH5, PH14, with R70), as the paper does ("the assumptions are those of the matching statement").

## Claim tree

- **C1** (gap 3) Under A1–A4: the $\Psi$-equation of the cubic action at the auxiliary solution is the equation of motion of the eliminated action; under `eq:hs8:kernel-condition` it is the same for every representative of the solution modulo the bare kernels; conversely, $\mathcal E_\Psi$ is invariant under kernel shifts at arbitrary values of the auxiliary fields if and only if the condition holds, read on the field spaces (the converse is off shell: on the solution curve the argument gives only one combination of the two clauses, and without the condition $\Sigma^* + N$ is in general not a solution); conditionally on the matching statement `eq:all:recovered` (R26, Conditional(PH1, PH2 (b), PH5, PH14) + R70) it equals `eq:all:eom-recovered`. [by C1.1–C1.4]
  - **C1.1** For any solution $\Sigma^*(\Psi)$ of all auxiliary equations, stationary in every direction of $\Hn{k}$ and differentiable in $\Psi$, $\mathcal E[F] = \mathcal E_\Psi(\Psi, \Sigma^*)$; such a solution exists under A3, A4 and the kernel condition. [by A1, A3, A4, C1.3; eq. (1.2)] [check: C1.1, C1.1-break, C1.1-kernel, C1.1-kernel-break]
  - **C1.2** $\mathcal E_\Psi$ sees the $\Sigma_k$ only through the sources $J_k$ and the odd couplings $O_k$; the kernel shift changes the action by $D$ of (1.4), homogeneous of degree one in $\Psi$, with the own-source and kinetic contributions vanishing by the symmetry of $\kin{k}{}{2k-2}$. [by A2, A3; eq. (1.1), (1.3), (1.4)] [check: C1.2-clause1, C1.2-clause2; consistency only: C1.2-euler-clause1, C1.2-euler-clause2]
  - **C1.3** $\mathcal E_\Psi(\Psi, \Sigma+N) = \mathcal E_\Psi(\Psi, \Sigma)$ for all $\Psi, \Sigma, N$ $\iff$ $D \equiv 0$ $\iff$ the kernel condition (clause 1 for $k \le K$, clause 2 for $k \le K-1$, $B$ in the field space); under it $\mathcal E_{\Sigma_k}$ and $F$ are representative-independent as well. [by A3, C1.2; eq. (1.5)–(1.7)] [check: C1.3, C1.3-break-clause1, C1.3-break-clause2, C1.3-separation-k2, C1.3-separation-k3, C1.3-separation-break, C1.3-top-clause1]
  - **C1.4** Conditionally on `eq:all:recovered`, (1.8) holds as a formal series: the $O(\gs^{2K})$ remainder of the value has an $O(\gs^{2K})$ $\Psi$-derivative by the $\gs\Psi$ scaling; R26 (kernel-free generic tensors) applies through the restriction to a fixed complement of the bare kernels, where the bare operators are invertible, and C1.3 (⇐) carries the result to every representative. [by R26, A4, C1.1, C1.3; eq. (1.8)]
- **C2** (gap 4) Under A1′, A5: the rule (2.0), with "outside" meaning $U^\perp$, is equivalent to $\ell_n(U^{\otimes n}) \subset U$ for all $n$; then the restricted products satisfy the $L_\infty$ relations and are cyclic for $\omega|_U$, and when $U \cap U^\perp = 0$ the truncated action satisfies the classical master equation. [by C2.1–C2.4]
  - **C2.1** (R$_U$) $\iff$ closure, using $(U^\perp)^\perp = U$ (level-and-momentum grading, A1′); with a non-orthogonal complement in place of $U^\perp$ the implication fails. [by A1′, A5; eq. (2.2)] [check: C2.1 (illustration), C2.1-break, C2.1-nonorthogonal]
  - **C2.2** $\mathcal R_n^U = \mathcal R_n|_U = 0$; relations up to arity $M-1$ are inherited if the rule holds for vertices up to $M$ legs. [by C2.1; eq. (2.3)] [check: C2.2, C2.2-break]
  - **C2.3** Master-equation reading needs $\omega|_U$ nondegenerate. The pairing joins ghost numbers 2 and 3, so a subspace of string fields alone is isotropic, contained in its orthogonal, and (R$_U$) would force every vertex to vanish on it; since $\ell_n$ maps fields (ghost 2) to ghost 3, closure itself, not only the master-equation reading, needs the antifield partners in $U$: the lemma concerns subspaces containing fields and antifields together, as $\mathcal U_{\rm all}$ does. [by C2.2, A5; Step 3; cited: paper sec. 7 (cyclic $L_\infty$ $\iff$ classical master equation, Zwiebach 1993)]
  - **C2.4** Cases: $U = \mathcal U_{\rm all}$ (full closure, (2.4)(a)); $U$ a finite set of universal states: closure only towards $\mathcal N$, $\ell_n(\mathcal U^{\otimes n}) \subset \mathcal U_{\rm all}$ ((2.4)(b)); the eliminated theory is covered through the matched order only; the cubic theory's multi-string legs are not covered by the per-strand rule, and its truncation enters through elimination with the truncated quadratic form's kernel as the proviso. [by C2.1, C2.3; eq. (2.4); Commentary of C2]

Open gaps: none
Hypotheses in force: PH1, PH2 (b), PH5, PH14 – through R26 in C1.4 (the explicit form `eq:all:eom-recovered`); C1.1 (existence) and C1.3 (⇐), applied to the string vertices, take the kernel condition as premise: at $k=2$ this is PH5 (the $V_5$ half, clause 1) and PH2 (b) (the $T_6$ half, clause 2), at $k\ge3$ the paper's standing assumption (`03-all-orders.tex` l. 443, "the condition on the nested kernels"); C1.3 as an equivalence and C2 use none

## C1 — Gap 3: the equation of motion of the recovered action

\subsection*{Setup}

A1–A4. Write $\Sigma := (\Sigma_2, \dots, \Sigma_K)$, $\Sigma_1 := \Psi$, and the three kinds of terms of level $k$ in `eq:all:action`,
$$
\begin{aligned}
T^{\rm kin}_k &:= \pair[k]{\Sigma_k}{\kin{k}{}{2k-2}(\Sigma_k)}, \\
J_k(\Psi; \Sigma_k, \Sigma_{k-1}) &:= \pair[k]{\Sigma_k}{\kin{k}{}{2k-2}(\Psi \otimes \Sigma_{k-1})}, \\
O_k(\Psi; \Sigma_k) &:= \dvertex{2k+1}(\Sigma_k, \Sigma_k, \Psi),
\end{aligned}
\qquad
a_k := \frac{\gs^{2k-2}}{(2k)!}, \quad b_k := \frac{\gs^{2k-1}}{(2k+1)!},
\tag{1.0}
$$
so that $\caction[\le 2K+1] = S_{\le 3}(\Psi) + \sum_{k=2}^K \big[ - a_k T^{\rm kin}_k + 2 a_k J_k + b_k O_k \big]$.
Variations are written through the pairings: $\delta \caction = \pair{\delta\Psi}{\mathcal E_\Psi} + \sum_k \pair[k]{\delta\Sigma_k}{\mathcal E_{\Sigma_k}}$.
$N_k$ denotes an element of the bare kernel $\ker \kin{k}{}{2k-2}$, a subspace that does not depend on $\Psi$.

\subsection*{Derivation}

**Step 1 (which terms carry $\Psi$).** $T^{\rm kin}_k$ does not contain $\Psi$; hence
$$
\mathcal E_\Psi(\Psi, \Sigma)
  = Q_B \Psi + \frac{\gs}{2}\, \ell_2(\Psi^2)
  + \sum_{k=2}^{K} \Big[ 2 a_k\, \frac{\delta J_k}{\delta \Psi} + b_k\, \frac{\delta O_k}{\delta \Psi} \Big],
\tag{1.1}
$$
where $\delta J_k / \delta\Psi$ is defined by $\delta_\Psi J_k = \pair{\delta\Psi}{\delta J_k/\delta\Psi}$ (at $k = 2$ both strands of $\Psi \otimes \Sigma_1 = \Psi^2$ are varied), and the first two terms are the variation of $S_{\le 3}$ (`eq:hs1:eom-psi`).
The equation sees $\Sigma_k$ only through $J_k$, $J_{k+1}$ (where $\Sigma_k$ is the lighter field of the source) and $O_k$.

**Step 2 (chain rule).** Let $\Sigma^*(\Psi)$ solve $\mathcal E_{\Sigma_k}(\Psi, \Sigma^*) = 0$ for $k = 2, \dots, K$, in every direction of $\Hn{k}$, and be differentiable in $\Psi$. Put $F(\Psi) := \caction[\le 2K+1](\Psi, \Sigma^*(\Psi))$. For a variation $\Psi \to \Psi + t\,\delta\Psi$,
$$
\begin{aligned}
\frac{\dd}{\dd t} F(\Psi + t\,\delta\Psi) \Big|_{t=0}
  &= \pair{\delta\Psi}{\mathcal E_\Psi(\Psi, \Sigma^*)}
   + \sum_{k=2}^{K} \pair[k]{\dot\Sigma_k^*}{\mathcal E_{\Sigma_k}(\Psi, \Sigma^*)}
\\
  &= \pair{\delta\Psi}{\mathcal E_\Psi(\Psi, \Sigma^*)},
\qquad
\dot\Sigma_k^* := \frac{\dd}{\dd t} \Sigma_k^*(\Psi + t\,\delta\Psi) \Big|_{t=0}.
\end{aligned}
\tag{1.2}
$$
Hence the equation of motion of the eliminated action, $\mathcal E[F]$ defined by $\delta F = \pair{\delta\Psi}{\mathcal E[F]}$, is $\mathcal E_\Psi(\Psi, \Sigma^*(\Psi))$.
A differentiable solution exists: on a fixed complement of the bare kernels the solution `eq:all:saddles` is unique and rational in $\Psi$ near $\gs\Psi = 0$ (A3, A4), and Step 4 shows that it then solves the equations in the kernel directions too.

**Step 3 (the kernel shift).** Shift $\Sigma_k \to \Sigma_k + N_k$, $k = 2, \dots, K$, with arbitrary $N_k \in \ker \kin{k}{}{2k-2}$, and let $D(\Psi; \Sigma, N) := \caction(\Psi, \Sigma + N) - \caction(\Psi, \Sigma)$. Term by term, using the symmetry of $\kin{k}{}{2k-2}$ (A3) and $\kin{k}{}{2k-2} N_k = 0$:
$$
\begin{aligned}
\Delta T^{\rm kin}_k
  &= 2 \pair[k]{N_k}{\kin{k}{}{2k-2}\Sigma_k} + \pair[k]{N_k}{\kin{k}{}{2k-2} N_k}
   = 0,
\\
\Delta J_k
  &= \pair[k]{N_k}{\kin{k}{}{2k-2}(\Psi \otimes (\Sigma_{k-1} + N_{k-1}))}
   + \pair[k]{\Sigma_k}{\kin{k}{}{2k-2}(\Psi \otimes N_{k-1})}
   = \pair[k]{\Sigma_k}{\kin{k}{}{2k-2}(\Psi \otimes N_{k-1})},
\\
\Delta O_k
  &= 2\, \dvertex{2k+1}(N_k, \Sigma_k, \Psi) + \dvertex{2k+1}(N_k, N_k, \Psi),
\end{aligned}
\tag{1.3}
$$
with $N_1 := 0$ ($\Sigma_1 = \Psi$ is not shifted). Hence
$$
D(\Psi; \Sigma, N)
  = \sum_{k=2}^{K-1} 2 a_{k+1}\, \pair[k+1]{\Sigma_{k+1}}{\kin{k+1}{}{2k}(\Psi \otimes N_k)}
  + \sum_{k=2}^{K} b_k \big[ 2\, \dvertex{2k+1}(N_k, \Sigma_k, \Psi) + \dvertex{2k+1}(N_k, N_k, \Psi) \big].
\tag{1.4}
$$
Every term of $D$ is linear in $\Psi$; at $k = 2$ the quartic source $J_2$, the only term quadratic in $\Psi$, drops out by the first line of (1.3).

**Step 4 (the equivalence).** Since $N$ does not depend on $\Psi$,
$$
\mathcal E_\Psi(\Psi, \Sigma + N) - \mathcal E_\Psi(\Psi, \Sigma) = \frac{\delta D}{\delta \Psi},
\qquad
\mathcal E_{\Sigma_k}(\Psi, \Sigma + N) - \mathcal E_{\Sigma_k}(\Psi, \Sigma) = \frac{\delta D}{\delta \Sigma_k}.
\tag{1.5}
$$
(⇐) If `eq:hs8:kernel-condition` holds, each term of (1.4) vanishes: the first clause with $(A, B) = (\Sigma_k, \Psi)$ and $(N_k, \Psi)$, the second with $B = \Psi$. Then $D \equiv 0$ for all $(\Psi, \Sigma, N)$, so by (1.5) $\mathcal E_\Psi$ and every $\mathcal E_{\Sigma_k}$ are the same at $\Sigma$ and $\Sigma + N$: the solutions form cosets of the kernels, the stationarity in the kernel directions holds automatically ($\pair[k]{N_k}{\mathcal E_{\Sigma_k}} = \frac{\dd}{\dd t} \caction(\Sigma + tN)|_0 = 0$), $F$ has the same value on every representative, and $\mathcal E_\Psi(\Psi, \Sigma^*)$ is the same for every representative.

(⇒) Suppose $\mathcal E_\Psi(\Psi, \Sigma + N) = \mathcal E_\Psi(\Psi, \Sigma)$ for all $\Psi, \Sigma, N$. Then $\delta D / \delta\Psi = 0$, and since $D$ is homogeneous of degree one in $\Psi$ (Euler),
$$
D(\Psi; \Sigma, N) = \pair{\Psi}{\tfrac{\delta D}{\delta \Psi}} = 0 .
\tag{1.6}
$$
Keep a single $N_k \neq 0$ and rescale it, $N_k \to \lambda N_k$: the terms of $D$ of order $\lambda^2$ and $\lambda$ vanish separately,
$$
\dvertex{2k+1}(N_k, N_k, \Psi) = 0,
\qquad
2 a_{k+1} \pair[k+1]{\Sigma_{k+1}}{\kin{k+1}{}{2k}(\Psi \otimes N_k)} + 2 b_k\, \dvertex{2k+1}(N_k, \Sigma_k, \Psi) = 0 .
\tag{1.7}
$$
Setting $\Sigma_{k+1} = 0$ gives $\dvertex{2k+1}(N_k, A, \Psi) = 0$ for every $A$ (first clause, $k \le K$); setting $\Sigma_k = 0$ and using the nondegeneracy of $\pair[k+1]{\cdot}{\cdot}$ (A3) gives $\kin{k+1}{}{2k}(\Psi \otimes N_k) = 0$ (second clause, $k \le K-1$). Both clauses are linear in $B$, and $\Psi$ ranges over the field space, so they hold for $B$ in its span.

**Step 5 (the recovered equation).** By Step 2 and Step 4, $\mathcal E_\Psi|_{\Sigma = \Sigma^*} = \mathcal E[F]$, independently of the representative. By Step 4 (⇐) the action depends on each $\Sigma_k$ only through its class modulo $\ker\kin{k}{}{2k-2}$; on a fixed complement of the bare kernels the tower has invertible (compressed) bare operators, which is the setting of the matching statement — R26 is stated for generic, hence kernel-free, tensors, and its recursion uses only the invertibility — so `eq:all:recovered` applies there and, by representative independence, to $F$. It gives $F = S_{\le 2K+1} + R$ with $R = O(\gs^{2K})$. By the scaling of the action (each term of order $\gs^{n-2}$ is homogeneous of degree $n$ in $\Psi$; `eq:all:rescaling`), $F(\Psi) = \gs^{-2} f(\gs\Psi)$ with $f$ analytic at $0$ at fixed truncation (A4), so $R = \gs^{-2} r(\gs\Psi)$ with $r = O((\gs\Psi)^{2K+2})$ and $\delta R / \delta\Psi = \gs^{-1} r'(\gs\Psi) = O(\gs^{2K})$. Since $\mathcal E[S_{\le 2K+1}] = Q_B\Psi + \sum_{n=2}^{2K} \frac{\gs^{n-1}}{n!} \ell_n(\Psi^n)$ (`eq:hs1:eom-psi`: the term $\gs^{n-1}$ is the variation of $S_{n+1}$, $n + 1 \le 2K + 1$),
$$
\mathcal E_\Psi \big|_{\Sigma_k = \Sigma_k^*}
  = Q_B \Psi + \sum_{n=2}^{2K} \frac{\gs^{n-1}}{n!}\, \ell_n(\Psi^n) + O(\gs^{2K}),
\tag{1.8}
$$
which is `eq:all:eom-recovered`.

\subsection*{Commentary}

- (1.2) needs $\mathcal E_{\Sigma}$ to vanish along $\dot\Sigma^*$ only (stationarity in every direction, as stated in C1.1, is sufficient, not necessary). For a solution on a fixed complement this is stationarity along the complement and holds without the kernel condition; for a representative that moves along the kernels with $\Psi$ it requires stationarity along the kernels, which the condition supplies (Step 4, ⇐). What fails without the condition is the complement-independence of $F$, not the chain rule (this is the complement dependence of the paper's quintic paragraph); the paper's sentence at `03-all-orders.tex` l. 433 is safe as written.
- (1.3), second line: the source of level $k$ is shifted through both of its fields; the part with $N_k$ in the slot of $\Sigma_k$ vanishes by symmetry, the part with $N_{k-1}$ in the slot of $\Psi \otimes \Sigma_{k-1}$ is the second clause one level down. This is why the first two terms of the paper's list (odd coupling, source of $\Sigma_{k+1}$) are the ones constrained and the own source is free.
- (1.6): the Euler step makes the converse hold for the equation alone, not only for the action: requiring the $\Psi$-equation to be unchanged by kernel shifts at arbitrary values of the auxiliary fields is already the full kernel condition, because every term in which a kernel direction could enter is linear in $\Psi$. This converse is off shell: at $\Sigma = \Sigma^*(\Psi)$ the $\lambda^1$ part of (1.7) gives only the combination $2a_{k+1}\pair[k+1]{\Sigma^*_{k+1}}{\kin{k+1}{}{2k}(\Psi\otimes N_k)} + 2b_k\dvertex{2k+1}(N_k,\Sigma^*_k,\Psi) = 0$, since $\Sigma^*_k$, $\Sigma^*_{k+1}$ are fixed functions of $\Psi$; and without the condition $\Sigma^* + N$ is in general not a solution, so "the representatives of the solution" is not a well-defined set.
- (1.7): the scaling separation uses that $\Sigma_k$, $\Sigma_{k+1}$ and $N_k$ are independent variables; at the top level $k = K$ there is no source of $\Sigma_{K+1}$ and only the first clause is obtained, and for the even truncation $2K$ the top odd coupling is absent and the first clause at $k = K$ is not needed.
- Field space vs. $\Hs$: the equivalence of Step 4 holds with $A$, $B$ and $N_k$ in the field spaces (ghost numbers $2k$, $2$, $2k$); the converse yields the clauses only for $N_k$ in the field-space part of the kernel. The paper's display, for all $A \in \Hn{k}$ and $B \in \Hs$, is a genuinely stronger sufficient condition: for $B$ of ghost number $\neq 2$, $\kin{k+1}{}{2k}(B \otimes N_k)$ is not killed by ghost counting. Not checked here: whether the paper's gauge paragraph (ghost-number-1 parameters, `03-all-orders.tex` l. 448ff.) uses the stronger form.
- Step 5 is the only place where the matching enters; Steps 1–4 are pure algebra and hold for any vertices with the stated symmetries.

\subsection*{Result}

$$
\boxed{\;
\mathcal E[F] = \mathcal E_\Psi(\Psi, \Sigma^*),
\qquad
\Big( \mathcal E_\Psi(\Psi, \Sigma + N) = \mathcal E_\Psi(\Psi, \Sigma) \ \forall\, \Psi, \Sigma, N \Big)
\iff D \equiv 0 \iff \text{eq:hs8:kernel-condition (field-space form)}
\;}
$$
and, under the matching statement `eq:all:recovered`, (1.8).

## C2 — Gap 4: closure under the universality rule

\subsection*{Setup}

A1′, A5. $\omega(A, B) = \pair{A}{B}$ is nondegenerate and graded symmetric on $\Hs$ (C1); $\ell_1 = Q_B$; $\vertex{2}(A_0, A_1) := \omega(A_0, Q_B A_1)$ is the kinetic term. For a subspace $U \subset \Hs$ let $U^\perp := \{ y \in \Hs : \omega(y, u) = 0 \ \forall u \in U \}$. "A leg outside $U$" means a leg in $U^\perp$: the rule is
$$
\text{(R}_U\text{)} \qquad
\vertex{n+1}(y, u_1, \dots, u_n) = 0,
\qquad
y \in U^\perp, \ u_i \in U, \ n \ge 1 .
\tag{2.0}
$$
The $L_\infty$ relation of arity $n$ is
$$
\mathcal R_n(A_1, \dots, A_n)
  := \sum_{i + j = n + 1} \ \sum_{\sigma \in {\rm Sh}(i, n - i)} \epsilon(\sigma; A)\,
     \ell_j\big( \ell_i(A_{\sigma(1)}, \dots, A_{\sigma(i)}), A_{\sigma(i+1)}, \dots, A_{\sigma(n)} \big)
  = 0,
\tag{2.1}
$$
with $\epsilon$ the Koszul sign of the unshuffle, which depends only on the degrees of the $A$'s (conventions of `app:conventions`; the argument does not use their form).

\subsection*{Derivation}

**Step 1 (closure).** For $u_i \in U$ and every $y \in U^\perp$, by `eq:hs1:vertex-product` and (2.0),
$$
\omega\big( y, \ell_n(u_1, \dots, u_n) \big) = \vertex{n+1}(y, u_1, \dots, u_n) = 0,
\qquad\text{so}\qquad
\ell_n(u_1, \dots, u_n) \in (U^\perp)^\perp = U .
\tag{2.2}
$$
The last equality holds piece by piece (A1′): $U = \oplus_{(L,p)} U_{L,p}$, $U^\perp = \oplus_{(L,p)} \{ y \in \Hs_{L,-p} : \omega(y, U_{L,p}) = 0 \}$, and on each pair of finite-dimensional pieces paired perfectly by $\omega$, $\dim U_{L,p}^\perp = \dim\Hs_{L,p} - \dim U_{L,p}$, $U_{L,p} \subset (U_{L,p}^\perp)^\perp$, equal dimensions. Without the grading (an infinite-dimensional space with a nondegenerate but not perfect pairing) $(U^\perp)^\perp$ can be larger than $U$. Conversely $\ell_n(U^{\otimes n}) \subset U$ implies (2.0). So (R$_U$) is equivalent to the closure of all products on $U$; at $n = 1$ it says $Q_B U \subset U$.

**Step 2 (relations).** Let $\ell_n^U := \ell_n|_{U^{\otimes n}} \colon U^{\otimes n} \to U$, well defined by (2.2). For $A_1, \dots, A_n \in U$, every inner product $\ell_i(A_{\sigma(1)}, \dots)$ in (2.1) lies in $U$ by (2.2), so every outer $\ell_j$ has all its inputs in $U$, and each term of (2.1) equals the same term written with the $\ell^U$, with the same sign. Hence
$$
\mathcal R_n^U(A_1, \dots, A_n) = \mathcal R_n(A_1, \dots, A_n) = 0,
\qquad A_i \in U .
\tag{2.3}
$$
The restricted products are cyclic for $\omega|_U$, since $\omega|_U(u_0, \ell^U_n(u_1, \dots)) = \vertex{n+1}(u_0, \dots, u_n)$ restricted to $U$, graded symmetric. If the rule holds only for $n + 1 \le M$, the relations $\mathcal R_n$ with $n \le M - 1$ are inherited (they contain only $\ell_i$, $\ell_j$ with $i, j \le n$): in the order counting of `eq:gauge:master-equation-order` the truncation then preserves the master equation through the order of $\mathcal R_{M-1}$.

**Step 3 (reading as the master equation).** When $\omega|_U$ is nondegenerate ($U \cap U^\perp = 0$), $(U, \ell^U, \omega|_U)$ is a cyclic $L_\infty$ algebra and the restricted action $S|_U = \sum_n \frac{\gs^{n-2}}{n!} \vertex{n}|_U$ has $\ell^U$ as its products, so the classical master equation of the truncated theory holds (the equivalence of cyclic $L_\infty$ relations and the classical master equation, as in the paper's Section 7). If $\omega|_U$ is degenerate, (2.2)–(2.3) still hold, but $\omega|_U$ defines no antibracket on $U$, and the truncated master equation is not defined on $U$ alone.

**Step 4 (the two cases of the paper).** Let $\mathcal U_{\rm all}$ be the universal states (matter in the identity Virasoro module, all ghost content) and $\mathcal N$ the non-universal ones, $\Hs = \mathcal U_{\rm all} \oplus \mathcal N$. The pairing does not mix matter modules (paper, below `eq:sol:universality`), so $\omega(\mathcal U_{\rm all}, \mathcal N) = 0$, and by nondegeneracy and dimension count piece by piece (A1′; both subspaces are graded)
$$
\mathcal U_{\rm all}^\perp = \mathcal N,
\qquad
\mathcal N^\perp = \mathcal U_{\rm all},
\qquad
\omega|_{\mathcal U_{\rm all}} \text{ nondegenerate}.
\tag{2.4}
$$
(a) $U = \mathcal U_{\rm all}$: (R$_U$) is `eq:sol:universality` for every $n$ with $\mathcal U = \mathcal U_{\rm all}$, and Steps 1–3 apply in full: the truncation to the universal states preserves the master equation.
(b) $U = \mathcal U$ a finite set of universal states (tachyon, ghost dilaton): $\mathcal U^\perp = \mathcal N \oplus (\mathcal U_{\rm all} \cap \mathcal U^\perp)$, and the rule `eq:sol:universality` kills the vertex only for $y \in \mathcal N$. Step 1 then gives $\ell_n(\mathcal U^{\otimes n}) \subset \mathcal N^\perp = \mathcal U_{\rm all}$: the products have no component towards the non-universal states, while the equations of motion along the universal states outside $\mathcal U$ (higher-level universal states, out-of-gauge universal states) carry the ordinary level-truncation error (as in `05-solutions.tex` l. 80, "the $\Psi$-equation along $\mathcal U^c$"; for a ghost-2 $\mathcal U$ the products have ghost number 3 and no component along any field).

\subsection*{Commentary}

- (2.2) uses only $(U^\perp)^\perp = U$; it does not need $U \cap U^\perp = 0$. "Outside" must be read as "in $U^\perp$", not "in a complement of $U$": with a non-orthogonal complement the statement fails (check C2.1-break-nonorthogonal).
- Ordinary level truncation (corollary, supports the paper's expectation at l. 410): take $U$ = all states of level $\le L$, all ghost numbers. Then $U^\perp$ is the states of level $> L$, and $\vertex{n+1}(y, u_1, \dots)$ with one leg of higher level is generically nonzero, so the rule fails and the lemma gives no closure, consistent with the expected generic failure of the master equation under level truncation.
- Ghost number: $\omega = \langle \cdot | c_0^- | \cdot \rangle$ joins ghost numbers 2 and 3 (for the kinetic term $2 + 3 + 1 = 6$), so a subspace of string fields alone is isotropic and contained in its orthogonal, and (R$_U$) would force every vertex to vanish on it; moreover $\ell_n$ maps fields to ghost number 3, so closure itself requires the ghost-3 partners in $U$. The lemma concerns subspaces containing fields and antifields together, as $\mathcal U_{\rm all}$ does. A finite set of Siegel-gauge string fields enters only through case (b), which uses the rule for $y \in \mathcal N$ alone.
- Cubic theory: its fields $\Sigma_k$ have multi-string legs, and a leg is outside $U^{\wedge k}$ when it lies in $(U^{\wedge k})^\perp$, which contains the components with two or more strands in $\mathcal N$. The rule `eq:sol:universality` is a statement per strand: it kills $\vertex{4}(u, u', u'', x)$ but not $\vertex{4}(u, u', x, x')$, $x, x' \in \mathcal N$, which is the kinetic term of $\Sigma_2$ between $U^{\wedge 2}$ and $\mathcal N^{\wedge 2}$ (the same holds for the source couplings to $\mathcal N^{\wedge 2}$ and for the odd coupling $\vertex{5}(x, x', u, u', u'')$: the universality rule's Ward-identity motivation, a single matter leg outside the identity module, gives nothing for two legs in conjugate modules, whose matter two-point function is nonzero). So the closure lemma, fed by the universality rule, applies to the truncation of the original theory, and to that of the eliminated theory only through the order at which it equals the original one (`eq:all:recovered`, $\le 2K+1$ legs): beyond it the remainder's vertices contain chains such as $\vertex{4}(u, u, a, b)\, K^{-1}\, \vertex{4}(a, b, u, x)$ with $(a, b) \in \mathcal N^{\wedge 2}$, which the per-strand rule does not kill (C2.2's partial-inheritance clause then gives the relations through the matched order); for the cubic theory with $\Sigma_2$ truncated to $U^{\wedge 2}$ the comparison goes through elimination, where the kernel of the truncated quadratic form enters: at quartic order the source $\sprod{2}{2}(\Psi^2)$, $\Psi^2 \in U^{\wedge 2}$, is the compressed form applied to $\Psi^2$, and the value is $\vertex{4}(\Psi^4)$ whatever the kernel of the compressed form; at quintic order the quintic vertex must vanish on that kernel (the paper's proviso "provided the truncated quadratic form has no kernel or the quintic vertex vanishes on it"; it is `eq:hs5:kernel-condition` for the compressed form, whose kernel need not be $\ker\sprod{2}{2} \cap U^{\wedge 2}$). This caveat qualifies the scope of the lemma as the paper states it at `04-gauge-bv-spectrum.tex` l. 420–422, not the expectation at l. 410 ("for the original theory and for the cubic theory alike"), which concerns the generic failure of the master equation under level truncation and with which it agrees; l. 410 is not to be edited. This is consistent with `sec:solutions` (l. 114–116), where the $\Sigma_2$-equation of the truncated cubic theory is violated along $\mathcal N \otimes \mathcal N$ from quintic order on.

\subsection*{Result}

$$
\boxed{\;
\text{(R}_U\text{)} \iff \ell_n(U^{\otimes n}) \subset U \ \forall n
\ \Longrightarrow\
\mathcal R_n^U = \mathcal R_n|_U = 0,
\quad
\text{master equation of } S|_U \text{ if } U \cap U^\perp = 0
\;}
$$
with the two cases (2.4)(a), (b), and the scope: subspaces of the full graded theory containing fields and antifields together (A1′, C2.3); the original theory, and the eliminated theory through the order at which it equals the original one; the cubic theory only through elimination, with the truncated quadratic form's kernel as the proviso.

## Verification

Script `codes/verify-paper-gaps-3-4.py`, run from the project root with `uv run --no-sync python codes/verify-paper-gaps-3-4.py` (seed 20261004, about 3 s), 20/20 PASS (fix pass, 2026-10-04; was 15/15):

```
[PASS] C1.1: dF/dt = -651.948362816, v.E_psi(s*) = -651.948362816
[PASS] C1.1-break: non-stationary sigma: v.E_psi = -535.97063626 != dF/dt (expected)
[PASS] C1.1-kernel: full gradient in sigma = 0 at s*
[PASS] C1.1-kernel-break: clause 1 violated: n2.dS/ds2 = -0.122, n3.dS/ds3 = -0.001284 at the complement solution (nonzero expected)
[PASS] C1.3: E_psi, E_sigma, F unchanged under s* -> s* + N
[PASS] C1.3-break-clause1: |Delta E_psi|_inf = 8.435e-02 (nonzero expected)
[PASS] C1.2-clause1: D = (1.4), homogeneous of degree one in psi, nonzero
[PASS] C1.2-euler-clause1: psi.dD/dpsi = D (consistency; implied by homogeneity)
[PASS] C1.3-break-clause2: |Delta E_psi|_inf = 2.801e-02 (nonzero expected)
[PASS] C1.2-clause2: D = (1.4), homogeneous of degree one in psi, nonzero
[PASS] C1.2-euler-clause2: psi.dD/dpsi = D (consistency; implied by homogeneity)
[PASS] C1.3-separation-k2: lam^2 coeff = b_k V(n,n,psi), lam^1 coeff = 2 a_{k+1} <s_{k+1}, K T(psi,n)> + 2 b_k V(n,s_k,psi); s_{k+1}=0 / s_k=0 isolate the clauses; 0 in the good model
[PASS] C1.3-separation-break: coefficient a_3 in place of 2 a_3 in (1.7): mismatch detected
[PASS] C1.3-separation-k3: lam^2 coeff = b_k V(n,n,psi), lam^1 coeff = 2 a_{k+1} <s_{k+1}, K T(psi,n)> + 2 b_k V(n,s_k,psi); s_{k+1}=0 / s_k=0 isolate the clauses; 0 in the good model
[PASS] C1.3-top-clause1: clause 1 broken at k = 3 only: |Delta E_psi| along n3 = 1.169e-04 (nonzero), along n2 = 0
[PASS] C2.1: max|V(y,u,u')| = 0.0e+00, closure defect 0.0e+00, Jacobi on U 0.0e+00, max|V(u,y,y')| = 6.00 (nonzero)
[PASS] C2.1-break: U' not closed: max|V(y,u,u')| = 24.266, projected Jacobi 130.063
[PASS] C2.1-nonorthogonal: Y-component of l2(U,U) = 0.178 (nonzero: outside must mean U^perp)
[PASS] C2.2: R_n|_U = R_n^U: dev 0.0e+00, outside-U part 0.0e+00 (scale 7.1e+03)
[PASS] C2.2-break: rule violated: projected relations differ, dev 2.176e+02 (scale 1.6e+02)
20/20 PASS
```

- Gap-3 model: the cubic action (1.0) with $K = 3$, $\dim\Psi = 3$, $\dim\Sigma_2 = 4$, $\dim\Sigma_3 = 5$, one kernel direction per level, exact rationals at $\gs = 3/10$. C1.1 compares $v \cdot \mathcal E_\Psi(\Sigma^*)$ with the total $t$-derivative of the action along $(\Psi_0 + tv, \Sigma^*(t))$, where $\dot\Sigma^*$ comes from the linear solve (not from the stationarity argument); exact equality, $\dot\Sigma^* \neq 0$. Break legs: $\mathcal E_\Psi$ at a non-stationary point differs; violating clause 1 alone or clause 2 alone makes $\mathcal E_\Psi$ representative-dependent (necessity at instance level: one random off-shell point), and there $D$ matches (1.4) term by term and is homogeneous of degree one in $\Psi$; the Euler legs (C1.2-euler-*) are consistency checks implied by that homogeneity and cannot fail on their own. C1.1 tests the chain rule, which holds for a complement solution with or without the condition (Commentary of (1.2)); C1.1-kernel-break shows that with clause 1 violated the complement solution is not stationary along the kernels (falsifier of the existence clause). The (⇒) content is tested by C1.3-separation-k2, -k3: for a single shift $N_k = \lambda n_k$, $\lambda$ symbolic, in a model violating both clauses, the $\lambda^2$ and $\lambda^1$ coefficients of $D$ (computed from the action) are the two sides of (1.7), no other power occurs, and $\Sigma_{k+1} = 0$, $\Sigma_k = 0$ isolate the clause-1 and clause-2 terms (each nonzero there, zero in the good model); C1.3-separation-break (coefficient $a_3$ for $2a_3$) fails as it should, and a mutation of the $b_k$ coefficient (scratch, `mut1.py`) makes both separation checks FAIL. C1.3-top-clause1 isolates necessity at the top level $k = K$: clause 1 broken only at $k=3$, a shift along $n_3$ changes $\mathcal E_\Psi$ and one along $n_2$ does not.
- Gap-4 models: $\mathfrak{sl}(3)$ with the trace form and $U = \mathfrak{so}(3)$ (an illustration, not a test of the lemma: the Cartan decomposition of a symmetric pair satisfies rule, closure and Jacobi by Lie theory, so C2.1 fails only on a coding error; C2.2 is the substantive test; rule holds, closure and Jacobi on $U$, two-legs-outside vertices nonzero so the test is not a decoupled sum); a seeded random 5-dimensional $U'$ (rule fails, projected bracket fails Jacobi); a random cyclic structure where the vertices vanish with one leg in a non-orthogonal complement (no closure); random $\ell_1, \ell_2, \ell_3$ from vertices obeying or violating the rule (compositions of the shape of $\mathcal R_1, \mathcal R_2, \mathcal R_3$ on $U$ agree with their restricted versions iff the rule holds).
- Found while writing the break leg: for $\ell_2$ alone, a bracket cyclic for a nondegenerate form on a space of dimension $\le 4$ is always Lie (every 3-form in dimension $\le 4$ is decomposable), so a projected truncation to so small a subspace satisfies Jacobi by accident; the break leg uses dimension 5. Not relevant to the paper's statement, which is the implication rule ⇒ relations.
- The gap-4 numbers changed from the 15/15 run (e.g. C2.1-break 18.332 → 24.266) because the new gap-3 legs draw from the shared seeded generator before gap 4; the checks and their outcomes are unchanged.
- Not machine-checked: Step 5 of C1 (the matching statement is cited, the scaling argument is two lines); the graded signs of the string-field relations (the argument of (2.3) is sign-blind); the universality rule itself; the ghost-number isotropy remark of C2.3 (ghost counting of the pairing); the graded double orthogonal of A1′ (finite-dimensional linear algebra piece by piece).

## Paragraph-ready statements

Paper notation; no record IDs. Each is one paragraph for the science-writer.
Writer notes (fix pass): in the same pass, `03-all-orders.tex` l. 441 should read "modulo the kernels of the bare kinetic operators $\kin{k}{}{2k-2}$" (not "of the quartic and of the nested kinetic operators"); the converse sentence of gap 3 may be dropped, since the paper needs only the forward direction; `04-gauge-bv-spectrum.tex` l. 410 is left as it is (the caveat on the cubic theory qualifies the lemma at l. 420–422, not the expectation at l. 410); case (a) of gap 4 is a truncation to all levels of the universal states, not a level truncation, and should not be presented as one under the paragraph heading "Level truncation".

**Gap 3 (replaces the `gap` comment after `eq:all:eom-recovered`).**
Let $F(\Psi)$ be the cubic action evaluated at a solution $\Sigma_k^*(\Psi)$ of all the auxiliary equations. Varying $\Psi$, the variation of $F$ is the variation of the cubic action at fixed auxiliary fields plus the auxiliary equations contracted with $\delta\Sigma_k^*$; the latter vanish, so the equation of motion of $F$ is $\mathcal E_\Psi$ evaluated at the solution. The solution is defined only modulo the bare kernels. A shift $\Sigma_k \to \Sigma_k + N_k$, $N_k \in \ker\kin{k}{}{2k-2}$, leaves the kinetic term and the own source of each level unchanged by the symmetry of $\kin{k}{}{2k-2}$, and changes the action by the shift of the odd couplings, $\gs^{2k-1}/(2k+1)!\,[2\dvertex{2k+1}(N_k, \Sigma_k, \Psi) + \dvertex{2k+1}(N_k, N_k, \Psi)]$, and of the source of the next level, $2\gs^{2k}/(2k+2)!\,\pair[k+1]{\Sigma_{k+1}}{\kin{k+1}{}{2k}(\Psi \otimes N_k)}$. Since the kinetic term and the own source do not change, these are the only terms through which a kernel shift can reach $\mathcal E_\Psi$, and all of them are linear in $\Psi$. The condition `eq:hs8:kernel-condition` says precisely that they vanish, so the $\Psi$-equation, the auxiliary equations and the value are the same for every representative. Conversely, since the shift is linear in $\Psi$, a $\Psi$-equation that is unchanged by every kernel shift at arbitrary values of the auxiliary fields forces the shift of the action itself to vanish, and with it the two clauses of `eq:hs8:kernel-condition`, read with $A$ and $B$ in the spaces of the fields. Combined with `eq:all:recovered`, whose remainder is $\gs^{-2}$ times a function of $\gs\Psi$, of order $\gs^{2K}$, so that its $\Psi$-derivative is of the same order, this gives `eq:all:eom-recovered`.

**Gap 4 (replaces the `gap` comment after the closure paragraph).**
"Outside the subspace $U$" means in its orthogonal $U^\perp$ for the pairing, $U$ containing with each string field its antifield partner. If $\vertex{n+1}(y, u_1, \dots, u_n) = 0$ for $y \in U^\perp$ and $u_i \in U$, then $\pair{y}{\ell_n(u_1, \dots, u_n)} = 0$ for every $y \in U^\perp$, so $\ell_n(u_1, \dots, u_n)$ lies in the orthogonal of $U^\perp$, which is $U$ since the pairing is nondegenerate level by level and $U$ is spanned by states of definite level and momentum; the converse holds as well. Each term of an $L_\infty$ relation evaluated on elements of $U$ is then a composition of products whose inputs all lie in $U$, so the relations hold for the restricted products, which are cyclic for the restricted pairing; when the pairing stays nondegenerate on $U$, this is the master equation of the truncated action. For the full universal subspace the orthogonal is the space of non-universal states, since the pairing does not mix matter modules, and the rule is the universality assumption for every $n$. For a finite set of universal states the orthogonal also contains the universal states left out, on which the rule says nothing: the products then have no component towards the non-universal states, and the equations of motion along the omitted universal states carry the ordinary level-truncation error. The argument concerns the original theory, and the eliminated theory through the order at which it equals the original one: for the cubic theory a two-string leg is outside $\mathcal U^{\wedge 2}$ also when both strands are non-universal, a case the universality rule does not cover, and the truncated cubic theory is compared through elimination, where the kernel of the truncated quadratic form enters as stated above.

## Self-review

1. Objective: both gaps get a derivation and a paragraph in the paper's notation; the forward direction of C1, which is what the paper's sentence needs, holds; the converse is proved in its off-shell form (invariance of $\mathcal E_\Psi$ under kernel shifts at arbitrary auxiliary fields), not on the solution (fix pass, #3). The writer may drop the converse from the paper.
2. Weakest step: the field-space vs. $\Hs$ reading of the clauses in C1.3 (the equivalence is with the clauses on the field spaces; the paper's form for all $B \in \Hs$ is stronger) and the remark that the cubic theory's truncation is not covered by C2 — this qualifies the scope of the lemma at `04-gauge-bv-spectrum.tex` l. 420–422, not the sentence at l. 410, which stays as it is (fix pass, #9).
3. Not checked: C1.4's input (cited), string-field signs (argument sign-blind).
4. A stronger reader would ask whether the closure statement transfers to the truncated cubic theory; it does not by the per-strand rule (C2.4), consistent with the paper's solutions section, where the $\Sigma_2$-equation is violated along pairs of non-universal states from quintic order.

## Fix pass (critic iteration 1)

Critic report `agent/reports/critic-085-20261004T140000.md` (1 major, 12 minor, notes). One line per finding; "statement" or "justification" says what changed in the node.

- #3 [major] C1 root: statement changed. Forward direction stated on the solution, converse stated off shell ("invariant under kernel shifts at arbitrary values of the auxiliary fields iff the condition, on the field spaces"), with the on-shell obstruction ($\lambda^1$ combination only) in the node and the Commentary of (1.6). Gap-3 paragraph "Conversely" sentence replaced by the critic's text; Self-review 1 updated. C1.3 unchanged (it already stated the off-shell form). Dependents: C1.4 (uses only the forward direction, still holds); the paragraph-ready gap 3 (updated). The Result box already had the off-shell form ($\forall\,\Psi,\Sigma,N$).
- #4 [minor] Gap-3 paragraph: "the only terms through which $\mathcal E_\Psi$ sees the auxiliary fields" replaced by the critic's text (the only terms through which a *kernel shift* can reach $\mathcal E_\Psi$, the kinetic term and own source being unchanged). Paragraph only; C1.2's node already lists the own source $J_k$.
- #1 [minor] `Hypotheses in force:` line and the Conventions paragraph: the kernel condition, premise of C1.1 (existence) and C1.3 (⇐), is for the string vertices PH5 ($V_5$ half, clause 1) plus PH2 (b) ($T_6$ half, clause 2) at $k=2$ and the paper's standing assumption (l. 443) at $k\ge3$; C1.3 as an equivalence and C2 use none. No node statement changed (the premise was already explicit in C1.1 and C1.3); the hypotheses line is the restatement updated.
- #2 [minor] Step 5 and C1.4 node (justification only): R26's scope is kernel-free generic tensors; by C1.3 (⇐) the action depends on $\Sigma_k$ only through its class, on a fixed complement the bare operators are invertible, which is all R26's recursion uses, so `eq:all:recovered` applies there and, by representative independence, to $F$.
- #5 [note] Commentary of (1.2) replaced by the critic's rewrite: the chain rule needs $\mathcal E_\Sigma$ to vanish only along $\dot\Sigma^*$; a fixed-complement solution does not need the condition for (1.2), a kernel-moving representative does. C1.1's "stationary in every direction" is sufficient and is kept (no statement change).
- #6 [minor] Commentary "Field space vs. $\Hs$" replaced: the equivalence is with $A$, $B$, $N_k$ in the field spaces; the paper's form for all $B\in\Hs$ is a genuinely stronger sufficient condition (not "formally" stronger); the gauge-paragraph question is recorded as not checked.
- #12 [minor] For the writer (not edited here, paper is read-only for this record): `03-all-orders.tex` l. 441 "modulo the kernels of the quartic and of the nested kinetic operators" should read "modulo the kernels of the bare kinetic operators $\kin{k}{}{2k-2}$", to match the fill (the two coincide under the condition near $\gs\Psi = 0$, `02-6-octic.tex` l. 137, 173–174). Recorded also in the header of the paragraph-ready statements.
- #15 [minor] Gap-3 paragraph: remainder is "$\gs^{-2}$ times a function of $\gs\Psi$, of order $\gs^{2K}$, so that its $\Psi$-derivative is of the same order" (critic's text). Step 5 already had this form.
- #7 [minor] C2.3 node: statement changed. The isotropy comes from ghost number ($\omega$ joins ghost numbers 2 and 3), not from Siegel gauge; a subspace of fields alone is isotropic, (R$_U$) would kill every vertex on it, and closure itself (ghost 2 → ghost 3) needs the antifield partners in $U$. Commentary item replaced by the critic's text; gap-4 paragraph: the condition moved into the first sentence ("$U$ containing with each string field its antifield partner"), the parenthetical removed. Dependents: C2 root (scope sentence in the Result updated), C2.4 (case (a) contains both; case (b) uses the rule for $y\in\mathcal N$ only, unaffected).
- #8 [minor] New assumption A1′ for gap 4 (full graded $\Hs$, perfect pairing piece by piece, $U$ graded), replacing A1 there; A1 and A5 cannot hold together for strings (a level-truncated SFT is not cyclic $L_\infty$, paper l. 409–413). Step 1's justification of $(U^\perp)^\perp=U$ and (2.4)'s dimension count rewritten piece by piece; C2 and C2.1 cite A1′ (justification only). Gap-4 paragraph: "nondegenerate level by level and $U$ is spanned by states of definite level and momentum". Writer note: case (a) is a truncation to all levels of the universal states, not a level truncation. Added the critic's corollary as a Commentary item (level-$\le L$ truncation fails the rule; supports l. 410).
- #9 [minor] Caveat 2 now says it qualifies the lemma at `04-gauge-bv-spectrum.tex` l. 420–422, not l. 410 (Commentary of C2, Self-review 2, writer note: l. 410 not to be edited); examples completed (source couplings to $\mathcal N^{\wedge2}$, $\vertex{5}(x,x',u,u',u'')$). Notation: $U\otimes U$ → $\mathcal U^{\wedge2}$ in the paragraph, $\mathrm{Sym}^k U$ → $U^{\wedge k}$ in the record.
- #10 [minor] "(and of the eliminated theory)" replaced in the Commentary of C2, the Result line, C2.4 and the gap-4 paragraph by "the eliminated theory through the order at which it equals the original one", with the chain $\vertex{4}(u,u,a,b)K^{-1}\vertex{4}(a,b,u,x)$, $(a,b)\in\mathcal N^{\wedge2}$, as the reason; matches C2.2's partial-inheritance clause. C2.4: statement narrowed.
- #11 [note] (2.4)(b) and the gap-4 paragraph: "components along the omitted universal states" → "the equations of motion along the omitted universal states carry the ordinary level-truncation error" (`05-solutions.tex` l. 80).
- #13 [minor] Script: Euler legs relabelled `C1.2-euler-*` (consistency, implied by homogeneity). New legs `C1.3-separation-k2`, `C1.3-separation-k3` test the $\lambda$-separation (1.7) and the two specialisations for a single $N_k$ against $D$ computed from the action; `C1.3-separation-break` (wrong coefficient) fails as it should; a scratch mutation of $b_k$ makes both separation legs FAIL. `C1.3-top-clause1` isolates necessity of clause 1 at $k=K$. C1.3 node check list updated; statement unchanged.
- #14 [minor] Script: `C1.1-kernel-break` added (clause 1 violated ⇒ complement solution not stationary along the kernels, $n_2\cdot\partial_{s_2}S = -0.122$); docstring and Verification note that C1.1 tests the chain rule only, `C2.1` is an illustration and `C2.2` the real test of the lemma.
- Unnumbered notes: corollary on ordinary level truncation added (#8 line); the gauge-paragraph question of #6 recorded as not checked.
- Re-run: `uv run --no-sync python codes/verify-paper-gaps-3-4.py`, 20/20 PASS, seed 20261004, about 3 s.

## Confirmation-pass residuals applied by the orchestrator (2026-10-04, `agent/reports/critic-085-confirm-20261004T141500.md`)

- R3 (C2.3 and the Commentary near l. 228): "$U$ containing with each string field its antifield partner" is necessary, not sufficient — for $U$ = ghost-2 fields plus ghost-3 antifields, $\ell_2(u_2,u_3)$ has ghost number 4 and leaves $U$ (equivalently the rule would force the gauge coupling $V_3$(ghost 1, ghost 2, ghost 3) to vanish); $U$ must contain every ghost number the products reach, as $\mathcal U_{\rm all}$ does. C2.3's clause is read with this correction; the gap-4 paragraph's sentences 1 and 5 are transcribed in the corrected form (the writer's brief carries the replacement text).
- R4 (A1′, l. 24, and the fix-pass line): "A1 and A5 cannot hold together" is the paper's l. 410 expectation, not a fact; A1′ does not need the claim. Read as withdrawn.
- R1: the gap-3 paragraph's sentence 6 reads "makes each of them vanish" (no equivalence); the converse sentence, if kept, adds "at the levels present in the truncation"; the C1 root takes the same addition.
- Note: on the solution the argument also gives $V_{2k+1}(N_k,N_k,\Psi)=0$.

