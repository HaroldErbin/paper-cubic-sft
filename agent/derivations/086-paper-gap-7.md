# 086 — The two forms of the $(2,2)$ relation of the raised family, their configurations and weights (paper gap 7)

## Status

Fix pass (critic iteration 1) complete (2026-10-04): findings #1–#5 applied (C4 rewritten with $T_1,\dots,T_4$ display and the superfield-reading sentence; note (ii) corrected; C1.2/Block 2 wording; script normalisation $\vertex3=2f$ noted; l. 132 vs `eq:ibl:generating` flagged for the orchestrator). Script unchanged, 17/17 PASS as before. Next: critic confirmation that #1 and #4 landed, then science-writer transcription.

## Task and objective

**Literal task.** For the paper's IBL section (`paper/sections/07-ibl.tex` l. 170–188, gap comment l. 188): write (C1) the $(2,2)$ relation among the operations with inputs and outputs only as a display, its four configurations and weights; (C2) the $(2,2)$ part of the polarized master equation `eq:ibl:polarized-master` (the raised-family form, with the operations $\sprod{m}{0}$, $\sprod{0}{n}$), its configurations and weights, and the origin of the factor $\tfrac12$; (C3) the difference `eq:ibl:residual-22` and the counterexample $\mathfrak{sl}_2\oplus\mathfrak{sl}_2^*$ at ghost numbers 1 and 4, re-checked; (C4) a transcription-ready statement (two displays, three sentences) in the paper's notation.

**Objective.** The paper's gap route needs a record that a critic can pass before the gap comment is replaced. Nothing new: the content is record 026 §3.1–§3.2 (R16, R31), re-derived here in the paper's conventions (symmetric pairing, odd form $\Omega$, $\Omega^{-1}$ raising), which differ from 026's ($\omega_1$ antisymmetric there; C1 corrected it later).

## Conventions

- C1: $\pair{A}{B}=\langle A|c_0^-|B\rangle$ graded symmetric, plainly symmetric on its support $\Ngh(A)+\Ngh(B)=5$. Components $g_{ab}:=\pair{e_a}{e_b}=g_{ba}$, inverse $g^{ab}$, $g_{ab}g^{bc}=\delta_a{}^c$.
- Paper `eq:conv:odd-symplectic` (= C1/C2 bullet): $\Omega(A,B)=(-1)^{\abs A}\pair AB$. Components $\Omega_{ab}=(-1)^{\varepsilon_a}g_{ab}$, inverse $(\Omega^{-1})^{ab}=g^{ab}(-1)^{\varepsilon_b}$ ($\Omega_{ab}(\Omega^{-1})^{bc}=\delta_a{}^c$).
- Paper `eq:conv:vertex`: $\vertex n(A_1,\dots,A_n)=\pair{A_1}{\ell_{n-1}(A_2,\dots,A_n)}$, $\ell_1=Q_B$, $\vertex2(A,B)=\pair A{Q_BB}$.
- Paper `eq:ibl:generating`, `eq:ibl:polarized-master` (quoted in the derivation blocks).

## Claim tree

- **A1** Finite-dimensional graded space $\Hs$, basis $e_a$, ghost numbers $n_a$, parity $\varepsilon_a=n_a\bmod2$; pairing, $\Omega$, $\Omega^{-1}$ as in *Conventions* (C1; paper `eq:conv:odd-symplectic`). The string field enters in the formal sense of the paper (`eq:ibl:polarized-master` paragraph): $\Omega^{-1}$ a sum over a basis.
- **A2** Superfields $\Psi=\Psi^ae_a$, $\Psi'=\Psi'^ae_a$ with $\abs{\Psi^a}=\abs{\Psi'^a}=\varepsilon_a$ (both even). Multilinear maps are evaluated on superfields by pulling the coefficients to the left, each coefficient Koszul-passing the basis vectors to its left only (rule K). The superfield output $\ell_n(\Psi^i,\Psi'^j)=:L^ce_c$ is defined by $\pair{e_a}{L}=\vertex{n+1}(e_a,\Psi^i,\Psi'^j)$ for all $a$, read with rule K. $\Omega$ on superfields is read with rule K. Rule K is not stated by the paper (inherited from 026 (3.11) commentary); C4 states it in a sentence after Display A (critic #1).
- **A3** Vertices $\vertex n$, $n\ge2$, graded symmetric in $\varepsilon$, no $\vertex1$; $S(u)=\sum_{n\ge2}\frac{\gs^{n-2}}{n!}\vertex n(u^n)$ (paper `eq:conv:action`).
- **C1** The $(2,2)$ relation among the operations with at least one input and one output is $\mathcal R_{2,2}=T_1+T_2+T_3+T_4=0$ with the four configurations of eq. (086.6), each with weight one. [by C1.1–C1.3]
  - **C1.1** Every contraction of $\partial^r_{\Psi^a}F\,(\Omega^{-1})^{ab}\,\partial^l_{\Psi'^b}G$ of two bidegree pieces is a pairing $\Omega(L_1,L_2)$ of two odd superfields, $\Omega(L_1,L_2)=g_{cd}L_1^cL_2^d$. [by A1, A2; eq. (086.1)–(086.4), (086.8)] [check: C1.1]
  - **C1.2** The inputs-and-outputs-only relation at $(2,2)$ is taken in its generating-function form: the bidegree-$(2,2)$ part of the same contraction applied to $H_0=S(\Psi+\Psi')-S(\Psi)-S(\Psi')$. Its configurations and weights coincide with those of CFL Def. 2.3 (CFL Prop. 7.2 at leading $\hbar$, in CFL's grading); the signed identity is not CFL's relation verbatim, the translation of Prop. 7.2 to bare physical variables not having been done (026 §1.3). [cited: 026 §1.3 decision, (0.2)–(0.3); CFL Prop. 7.2, as used in R16] [check: C1.3]
  - **C1.3** Exactly four ordered compositions $\sprod{k_1}{\ell_1}\circ\sprod{k_2}{\ell_2}$ with $k_i,\ell_i\ge1$ reach $(2,2)$, with the weights of (086.6). [by A3, C1.1; eq. (086.5)–(086.6)] [check: C1.3]
- **C2** The $(2,2)$ part of `eq:ibl:polarized-master`, divided by two, is $T_1+T_2+T_3+\tfrac12T_4=0$; the factor $\tfrac12$ is the symmetry factor of the self-mirror configuration. [by C2.1–C2.3]
  - **C2.1** Seven ordered configurations reach $(2,2)$ when $\sprod{m}{0}$ and $\sprod{0}{n}$ are included; the three new ones are the mirrors of $T_1,T_2,T_3$; cases exhaustive: $k_1\in\{1,2,3\}$, $\ell_1\in\{0,1,2\}$ minus the two needing $\vertex1$. [by A3, C1.1; eq. (086.7), (086.9) commentary] [check: C2.1]
  - **C2.2** Mirror symmetry: exchanging the roles of the two products leaves a configuration unchanged, $T(\bar t)=T(t)$, because $\Omega(L,K)=\Omega(K,L)$ on odd superfields; with plain $g^{-1}$ raising the mirror pairs are opposite instead. [by C1.1; eq. (086.8)] [check: C2.2, C2.2-break]
  - **C2.3** $T_4$ is its own mirror; hence the full sum is $2(T_1+T_2+T_3)+T_4$. [by C2.1, C2.2; eq. (086.9)–(086.10)] [check: C2.3, C2.3-break]
- **C3** $\mathcal R_{2,2}-\tfrac12E_{2,2}=\tfrac12\Omega(\ell_2(\Psi,\Psi'),\ell_2(\Psi,\Psi'))$ identically; on a cyclic $L_\infty$ algebra $E_{2,2}=0$ and the inputs-and-outputs-only relation reduces to the vanishing of this residual, which fails on $\mathfrak{sl}_2\oplus\mathfrak{sl}_2^*$ at ghost numbers 1 and 4. [by C3.1–C3.3]
  - **C3.1** The identity (086.11), no $L_\infty$ relation used. [by C1, C2] [check: C3.1, C3.1-break]
  - **C3.2** $E\equiv0$ for a cyclic $L_\infty$ algebra, hence (086.12). [by R31; cited: 026 (3.8)–(3.9)] [check: C3.2-sl2, C3.2-break]
  - **C3.3** On $\mathfrak{sl}_2\oplus\mathfrak{sl}_2^*$ (ghost 1, 4) $E\equiv0$ and $\mathcal R_{2,2}=\tfrac12T_4\ne0$; on the Heisenberg algebra both forms hold. [by R16; cited: 026 (3.18)–(3.19); by check: C3.3-sl2, C3.3-heis]
- **C4** Transcription statement (configuration display, Displays A, B, the superfield-reading sentence, three sentences) restates (086.6), (086.10), (086.11) in the paper's notation, with the weights visible as multipliers of $T_1,\dots,T_4$. [by A2, C1, C2, C3]

Open gaps: none
Hypotheses in force: none

Note for the orchestrator (critic #5, outside the passage, not a gap of this record): paper l. 132 says the $\Omega^{-1}$-raised family "differs [from `eq:conv:sprod`] by an overall sign for one output" on inputs of ghost number two, while `eq:ibl:generating` (l. 138) writes $S(\Psi+\Psi')$ with $\pair[n]{\Psi'^n}{\sprod{m}{n}(\Psi^m)}$ for that family and l. 140 identifies only the $n=0$, $m=0$, $m+n=2$ terms; if the one-output sign held on unrestricted superfields, the $n=1$ terms of `eq:ibl:generating` would carry $-\vertex{m+1}$. This record does not depend on it (Block 2 uses $H_{k,\ell}=\gs^{k+\ell-2}\vertex{k+\ell}(\Psi^k,\Psi'^\ell)/(k!\,\ell!)$, the binomial expansion of $S$); the $\sprod{k}{\ell}$-form quoted in the Block 2 Setup is the paper's and was not checked here. The restriction "on inputs of ghost number two" may resolve it. Paper not edited.

## Derivation

### Block 1 — every contraction is a pairing $\Omega(L_1,L_2)$ of two odd superfields (C1.1, C2.2)

\subsection*{Setup}
A1–A3. Bidegree pieces $H_{k,\ell}:=\frac{\gs^{k+\ell-2}}{k!\,\ell!}\vertex{k+\ell}(\Psi^k,\Psi'^\ell)$, $k+\ell\ge2$, so $S(\Psi+\Psi')=\sum_{k,\ell}H_{k,\ell}$ (paper `eq:ibl:generating`, the $\sprod{k}{\ell}$-form). For two even functions $F,G$ of $(\Psi,\Psi')$:
$$\mathcal C(F,G):=\frac{\pd^rF}{\pd\Psi^a}\,(\Omega^{-1})^{ab}\,\frac{\pd^lG}{\pd\Psi'^b},\qquad X_a:=\frac{\pd^lF}{\pd\Psi^a},\quad Y_b:=\frac{\pd^lG}{\pd\Psi'^b}.$$
`eq:ibl:polarized-master` is $E:=\mathcal C(S(\Psi+\Psi'),S(\Psi+\Psi'))=0$.

\subsection*{Derivation}
$$\mathcal C(F,G)=(-1)^{\varepsilon_a}X_a\,g^{ab}(-1)^{\varepsilon_b}\,Y_b=-\,g^{ab}X_aY_b.\tag{086.1}$$
$$X_a=c_F\,\vertex{n+1}(e_a,A_1,\dots,A_n)=\pair{e_a}{L_F},\quad L_F:=c_F\,\ell_n(A_1,\dots,A_n)=L_F^c\,e_c,\qquad \abs{L_F^c}=\varepsilon_c+1.\tag{086.2}$$
$$X_a=(-1)^{\abs{L_F^c}\varepsilon_a}\,L_F^c\,g_{ac}=(-1)^{\varepsilon_a}\,g_{ac}\,L_F^c,\qquad Y_b=(-1)^{\varepsilon_b}\,g_{bd}\,L_G^d.\tag{086.3}$$
$$\mathcal C(F,G)=-(-1)^{\varepsilon_a+\varepsilon_b}\,g_{ca}g^{ab}g_{bd}\,L_F^cL_G^d=g_{cd}\,L_F^c\,L_G^d.\tag{086.3'}$$
$$\Omega(L,K)=L^c(-1)^{\abs{K^d}\varepsilon_c}K^d\,\Omega_{cd}=(-1)^{(\varepsilon_d+1)\varepsilon_c+\varepsilon_c}\,g_{cd}\,L^cK^d=g_{cd}\,L^cK^d\qquad(L,K\ \text{odd}).\tag{086.4}$$
$$\boxed{\;\mathcal C(F,G)=\Omega(L_F,L_G),\qquad \Omega(L,K)=\Omega(K,L)\ \ (L,K\ \text{odd}).\;}\tag{086.8}$$

\subsection*{Commentary}
(086.1): $\pd^r=(-1)^{\varepsilon_a}\pd^l$ on an even function ($\pd^rF/\pd\Psi^a=(-1)^{\varepsilon_a(\abs F+1)}\pd^lF/\pd\Psi^a$); $(\Omega^{-1})^{ab}=g^{ab}(-1)^{\varepsilon_b}$; on the support of $g^{ab}$, $\varepsilon_a+\varepsilon_b=1$. $F=H_{k,\ell}$ is even: $\vertex{n}$ is nonzero only at total ghost number $2n$.
(086.2): $\pd^l_{\Psi^a}$ of $\vertex{n+1}(\Psi^{i+1},\Psi'^j)$ is $(i+1)\vertex{n+1}(e_a,\Psi^i,\Psi'^j)$ — with rule K the coefficient of the first slot passes nothing, and graded symmetry with $\Psi$ even moves any slot first at no cost; the second equality is A2 (the definition `eq:conv:vertex` read on superfields). $X_a$ has parity $\varepsilon_a$ and $g_{ac}\ne0$ forces $\varepsilon_c=\varepsilon_a+1$, so $\abs{L^c}=\varepsilon_a=\varepsilon_c+1$: $L$ is an odd superfield, as it must be, $\ell_n$ having odd ghost number $3-2n$ (`eq:conv:ghost-numbers`).
(086.3): rule K, $L^c$ passing $e_a$; $\abs{L^c}\varepsilon_a=\varepsilon_a^2=\varepsilon_a$.
(086.3'): $g$ symmetric (C1), $g_{ca}g^{ab}=\delta_c{}^b$; $(-1)^{\varepsilon_a+\varepsilon_b}=-1$; $g_{ac}$ are numbers.
(086.4): rule K for $\Omega$, $K^d$ passing $e_c$; $\Omega_{cd}=(-1)^{\varepsilon_c}g_{cd}$; on the support $\varepsilon_d+1=\varepsilon_c$, so the exponent is $2\varepsilon_c$.
(086.8): first identity, (086.3') = (086.4). Second: $L^c$, $K^d$ have parities $\varepsilon_c+1$, $\varepsilon_d+1$, one of them even on the support, so they commute; $g$ symmetric. It agrees with the graded antisymmetry of $\Omega$ (`eq:conv:odd-symplectic`), $\Omega(B,A)=-(-1)^{\abs A\abs B}\Omega(A,B)=+\Omega(A,B)$ for odd $A,B$.
**Plain $\Delta$ instead of $\Omega^{-1}$.** With $(\Omega^{-1})^{ab}$ replaced by $g^{ab}$ the same steps give $-(-1)^{\varepsilon_d}g_{cd}L_F^cL_G^d$, which changes sign under $F\leftrightarrow G$ (the factor $(-1)^{\varepsilon_d}$ becomes $(-1)^{\varepsilon_c}=-(-1)^{\varepsilon_d}$): mirror configurations cancel and the polarized equation is empty. This is the paper's l. 130 remark (the raising that closes the antibracket) and 026 (3.3) commentary; check `C2.2-break`.

\subsection*{Result}
Every term of $E$ and of the inputs-and-outputs-only relation is $\Omega(L_1,L_2)$ with $L_1=\pd^l_\Psi$-output of the first piece and $L_2=\pd^l_{\Psi'}$-output of the second, both odd superfields, and it is symmetric under exchange of the two.

\subsection*{Verification}
Check `C1.1` (exact, Grassmann polynomials over $\mathbb Q$, random graded-symmetric $\vertex2,\vertex3,\vertex4$ not satisfying the master equation): every one of the seven $(2,2)$ contractions computed from right and left derivatives of $H_{k,\ell}$ with the numerically inverted $\Omega$ equals $\Omega(L_1,L_2)$ computed from the superfield outputs with rule K. Check `C2.2`: mirror pairs equal; `C2.2-break`: with $g^{-1}$ they are opposite.

### Block 2 — the configurations at $(2,2)$ and their weights in both forms (C1.2, C1.3, C2.1, C2.3)

\subsection*{Setup}
Block 1. A configuration is an ordered pair $(k_1,\ell_1;k_2,\ell_2)$ with the term $\mathcal C(H_{k_1,\ell_1},H_{k_2,\ell_2})$. By `eq:ibl:generating` (as the paper writes it; not checked here, see the note under the claim tree, critic #5), $H_{k,\ell}=\frac{\gs^{k+\ell-2}}{k!\ell!}\pair[\ell]{\Psi'^\ell}{\sprod{k}{\ell}(\Psi^k)}$ — used only to label configurations; all computations use the vertex form: $\pd_\Psi$ opens an input of $\sprod{k_1}{\ell_1}$, $\pd_{\Psi'}$ opens an output of $\sprod{k_2}{\ell_2}$, and $\Omega^{-1}$ joins them — the configuration is the composition $\sprod{k_1}{\ell_1}\circ\sprod{k_2}{\ell_2}$ through one strand, with $k_1+k_2-1$ inputs and $\ell_1+\ell_2-1$ outputs. The inputs-and-outputs-only relation is $\mathcal R:=\mathcal C(H_0,H_0)$, $H_0:=\sum_{k,\ell\ge1}H_{k,\ell}=S(\Psi+\Psi')-S(\Psi)-S(\Psi')$ (026 (0.2)–(0.3); this is the generating-function form. CFL Prop. 7.2 at leading $\hbar$ identifies its configurations and multiplicities with those of CFL Def. 2.3 among the $\sprod{k}{\ell}$, $k,\ell\ge1$, in CFL's grading; the translation to bare physical variables was not done (026 §1.3), so as a signed identity $\mathcal R$ is the generating-function form, not CFL Def. 2.3 verbatim — critic #2). The overall $\gs^2$ of the $(2,2)$ part is dropped.

\subsection*{Derivation}
$$\text{bidegree of }\mathcal C(H_{k_1,\ell_1},H_{k_2,\ell_2})=(k_1+k_2-1,\ \ell_1+\ell_2-1),\qquad L_1=\frac{\ell_{k_1+\ell_1-1}(\Psi^{k_1-1},\Psi'^{\ell_1})}{(k_1-1)!\,\ell_1!},\quad L_2=\frac{\ell_{k_2+\ell_2-1}(\Psi^{k_2},\Psi'^{\ell_2-1})}{k_2!\,(\ell_2-1)!}.\tag{086.5}$$
Configurations with $k_1,\ell_1,k_2,\ell_2\ge1$ at $(2,2)$ ($k_1+k_2=3$, $\ell_1+\ell_2=3$):
$$\begin{aligned}
T_1&:=\mathcal C(H_{1,1},H_{2,2})=\tfrac12\,\Omega\bigl(Q_B\Psi',\ \ell_3(\Psi,\Psi,\Psi')\bigr) &&[Q_B\circ\sprod22],\\
T_2&:=\mathcal C(H_{2,2},H_{1,1})=\tfrac12\,\Omega\bigl(\ell_3(\Psi,\Psi',\Psi'),\ Q_B\Psi\bigr) &&[\sprod22\circ Q_B],\\
T_3&:=\mathcal C(H_{1,2},H_{2,1})=\tfrac14\,\Omega\bigl(\ell_2(\Psi',\Psi'),\ \ell_2(\Psi,\Psi)\bigr) &&[\sprod12\circ\ell_2],\\
T_4&:=\mathcal C(H_{2,1},H_{1,2})=\Omega\bigl(\ell_2(\Psi,\Psi'),\ \ell_2(\Psi,\Psi')\bigr) &&[\ell_2\circ\sprod12],
\end{aligned}\qquad \mathcal R_{2,2}=T_1+T_2+T_3+T_4.\tag{086.6}$$
Configurations at $(2,2)$ with $\sprod{m}{0}=\vertex m$ or $\sprod{0}{n}$ (that is $k_2=0$ or $\ell_1=0$):
$$\begin{aligned}
\bar T_1&:=\mathcal C(H_{3,1},H_{0,2})=\tfrac12\,\Omega\bigl(\ell_3(\Psi,\Psi,\Psi'),\ Q_B\Psi'\bigr) &&[\ell_3\circ\sprod02],\\
\bar T_2&:=\mathcal C(H_{2,0},H_{1,3})=\tfrac12\,\Omega\bigl(Q_B\Psi,\ \ell_3(\Psi,\Psi',\Psi')\bigr) &&[\sprod20\circ\sprod13],\\
\bar T_3&:=\mathcal C(H_{3,0},H_{0,3})=\tfrac14\,\Omega\bigl(\ell_2(\Psi,\Psi),\ \ell_2(\Psi',\Psi')\bigr) &&[\sprod30\circ\sprod03],
\end{aligned}\tag{086.7}$$
$$E_{2,2}=T_1+T_2+T_3+T_4+\bar T_1+\bar T_2+\bar T_3=2\,(T_1+T_2+T_3)+T_4.\tag{086.9}$$
$$\boxed{\;\tfrac12E_{2,2}=T_1+T_2+T_3+\tfrac12\,T_4,\qquad \mathcal R_{2,2}=T_1+T_2+T_3+T_4.\;}\tag{086.10}$$

\subsection*{Commentary}
(086.5): block 1 (086.2) with $F=H_{k_1,\ell_1}$ differentiated in $\Psi$ (one fewer $\Psi$, factor $k_1$ cancelling one in $k_1!$) and $G=H_{k_2,\ell_2}$ in $\Psi'$; the remaining arguments fill $\ell_{n}$ with $n=k+\ell-1$ through `eq:conv:vertex`; $\ell_1=Q_B$ through $\vertex2(A,B)=\pair A{Q_BB}$.
(086.6): enumeration with $k_1\in\{1,2\}$, $\ell_1\in\{1,2\}$ ($k_2=3-k_1\ge1$, $\ell_2=3-\ell_1\ge1$): four ordered configurations, $k\ell=4$ (026 W8 count). Coefficients from (086.5): e.g. $T_3$: $L_1=\ell_2(\Psi'^2)/(0!\,2!)$, $L_2=\ell_2(\Psi^2)/(2!\,0!)$. Each enters $\mathcal R$ once, with coefficient one: $H_0$ contains each $H_{k,\ell}$ once and $\mathcal C$ is bilinear.
(086.7): the full sum adds $k_1=3$ ($k_2=0$) or $\ell_1=0$ ($\ell_2=3$). Exhaustiveness: $k_1\in\{1,2,3\}$ (at least one $\Psi$ to differentiate), $\ell_1\in\{0,1,2\}$ ($\ell_2\ge1$), nine pairs minus $(k_1,\ell_1)=(1,0)$ and $(k_2,\ell_2)=(0,1)$, which would need $\vertex1$ (A3, no tadpole): seven, $(k+1)(\ell+1)-2=7$ (026 W8).
(086.9): the mirror of a configuration exchanges $L_1$ and $L_2$: $(k_1,\ell_1;k_2,\ell_2)\mapsto(k_2+1,\ell_2-1;k_1-1,\ell_1+1)$. It sends $T_1\mapsto\bar T_1$, $T_2\mapsto\bar T_2$, $T_3\mapsto\bar T_3$, and $T_4=(2,1;1,2)\mapsto(2,1;1,2)$, itself. By (086.8), $\bar T_i=T_i$.
(086.10): divide (086.9) by two. **Origin of the $\tfrac12$:** in the full relation every configuration and its mirror both occur, and they are equal; three of the four classes have two members, the class of $T_4$ — one $\Psi$ and one $\Psi'$ in each cubic product — has one, because its mirror is itself. It is the symmetry factor of a configuration invariant under exchange of the two products. In $\mathcal R$ the mirror members $\bar T_{1,2,3}$ are absent (each contains $\sprod{m}{0}$ or $\sprod{0}{n}$), so every class has one member.

\subsection*{Result}
(086.10): the $(2,2)$ part of `eq:ibl:polarized-master` is $2(T_1+T_2+T_3)+T_4$ — weights $1,1,1,\tfrac12$ after division by two — and the inputs-and-outputs-only relation is $T_1+T_2+T_3+T_4$, weights $1,1,1,1$.

\subsection*{Verification}
Checks `C1.3` (four $\mathcal R$ configurations, coefficients of (086.6), sum equals $\mathcal C(H_0,H_0)_{2,2}$), `C2.1` (seven configurations, sum equals $E_{2,2}$ computed from $S(\Psi+\Psi')$ directly), `C2.3` ((086.9) on generic data, every $T_i\ne0$), with break `C2.3-break` (weight of $T_4$ set to 2 in (086.9): fails).

### Block 3 — the residual and the counterexample (C3)

\subsection*{Setup}
Blocks 1–2. A cyclic $L_\infty$ algebra: $E\equiv0$ at every bidegree (R31; 026 (3.8)–(3.9): $E=\mathcal C(S(u),S(u))$ is the antibracket $\tfrac12(S,S)$ — normalisation aside — evaluated at $u=\Psi+\Psi'$, by the chain rule $\pd_{\Psi^a}S(\Psi+\Psi')=\pd_{\Psi'^a}S(\Psi+\Psi')=(\pd_aS)(u)$). Counterexample data (paper l. 184; 026 (3.19)): $\Hs=\mathfrak g_{(1)}\oplus\mathfrak g^*_{(4)}$, basis $c_i$ (ghost 1, odd), $c^{*i}$ (ghost 4, even), $\pair{c_i}{c^{*j}}=\pair{c^{*j}}{c_i}=\delta_i{}^j$, $\vertex3(c^{*i},c_j,c_k)=f_{jk}{}^i$ extended graded-symmetrically, $Q_B=0$, $\ell_{n\ge3}=0$.

\subsection*{Derivation}
$$\mathcal R_{2,2}-\tfrac12E_{2,2}=\tfrac12\,T_4=\tfrac12\,\Omega\bigl(\ell_2(\Psi,\Psi'),\ell_2(\Psi,\Psi')\bigr)\qquad\text{(identically, any graded-symmetric vertices)}.\tag{086.11}$$
$$\text{cyclic }L_\infty:\quad \mathcal R_{2,2}=\tfrac12\,\Omega\bigl(\ell_2(\Psi,\Psi'),\ell_2(\Psi,\Psi')\bigr)=-(T_1+T_2+T_3).\tag{086.12}$$
$$\text{cyclic dg Lie }(\ell_{n\ge3}=0):\quad T_1=T_2=0,\qquad E_{2,2}=2T_3+T_4=0,\qquad \mathcal R_{2,2}=\tfrac12T_4=-T_3.\tag{086.13}$$
$$\mathcal R_{2,2}\equiv0\iff\Omega\bigl(\ell_2(A,B),\ell_2(C,D)\bigr)=0\ \forall A,B,C,D\iff\ell_2(\ell_2(A,B),C)=0\ \forall A,B,C.\tag{086.14}$$
$$\mathfrak g=\mathfrak{sl}_2:\quad[\mathfrak g,[\mathfrak g,\mathfrak g]]=\mathfrak g\ne0\ \Longrightarrow\ \mathcal R_{2,2}\ne0;\qquad \mathfrak g=\text{Heisenberg}:\ [\mathfrak g,[\mathfrak g,\mathfrak g]]=0\ \Longrightarrow\ \mathcal R_{2,2}=0.\tag{086.15}$$

\subsection*{Commentary}
(086.11): (086.10), subtracted. No $L_\infty$ relation is used.
(086.12): $E_{2,2}=0$ in (086.11) and (086.9).
(086.13): $T_1,T_2$ contain $Q_B$ and $\ell_3$ (086.6); here $Q_B=0$ and $\ell_3=0$.
(086.14): 026 (3.18), cited and not re-derived here: the coefficient of $\Psi'^\mu\Psi'^\nu\Psi^\rho\Psi^\sigma$ in $T_3$ is a non-zero sign times $\Omega(\ell_2(e_\mu,e_\nu),\ell_2(e_\rho,e_\sigma))$, then cyclicity of $\vertex3$ and non-degeneracy. This is the paper's l. 186 sentence ("only when $\ell_2(\ell_2(A,B),C)=0$"); 026 (3.18) is in 026's sign conventions, where only signs per component differ, so the vanishing statement transfers.
(086.15): 026 (3.19): $\Omega(\ell_2(x,y),\ell_2(z,\xi))\propto\langle\xi,[z,[x,y]]\rangle$ for $x,y,z\in\mathfrak g$, $\xi\in\mathfrak g^*$. Re-checked here in the paper's conventions with an independent implementation (checks `C3.2-sl2`, `C3.3-sl2`, `C3.3-heis`). On $\mathfrak{sl}_2$ the script gives $T_1=T_2=0$, $T_3\ne0$, $T_4=-2T_3\ne0$ (12 monomials in $\mathcal R_{2,2}$, e.g. coefficient $16$ of $\psi^h\xi_e\psi'^e\psi'^h$ in the basis $(e,f,h)$, $\psi^i$ the odd ghost-1 coefficients, $\xi_i$ the even ghost-4 ones). **Normalisation (critic #3):** the script's `lie_model` sums over all permutations of a base triple for both entries $(j,k,i)$ and $(k,j,i)=-(j,k,i)$ of `structure()`, so it uses $\vertex3(c^{*i},c_j,c_k)=2f_{jk}{}^i$, not $f_{jk}{}^i$ as stated in the Setup; the quoted 16 is for $\vertex3=2f$ (with $\vertex3=f$ it is $\pm4$, every $T_i$ being quadratic in $\vertex3$). No claim changes: everything tested is homogeneous in $\vertex3$.
**Scope of the counterexample** (as R16): it lives at ghost numbers 1 and 4, not on the physical sector (both inputs at ghost 2); there the failure is numerical (026 generator (iv), $|P_{2,2}|=20.3$), and for the closed-string vertices the residual is not evaluated (paper l. 191, 026 §9.4).

\subsection*{Result}
$$\boxed{\;\mathcal R_{2,2}-\tfrac12E_{2,2}=\tfrac12\,\Omega\bigl(\ell_2(\Psi,\Psi'),\ell_2(\Psi,\Psi')\bigr)\;}$$
— the display `eq:ibl:residual-22`, with the direction "inputs-and-outputs-only minus half the polarized equation". On a cyclic $L_\infty$ algebra the inputs-and-outputs-only relation at $(2,2)$ is the vanishing of this residual, which fails on $\mathfrak{sl}_2\oplus\mathfrak{sl}_2^*$.

\subsection*{Verification}
`C3.1` (generic data, (086.11) exact), `C3.1-break` (weight 1 instead of $\tfrac12$: fails); `C3.2-sl2` ($E=0$ at every bidegree), `C3.2-break` ($[h,f]=-3f$ violates Jacobi: $E\ne0$); `C3.3-sl2` ($\mathcal R_{2,2}\ne0$, $=\tfrac12T_4$); `C3.3-equal` (the brief's leg: weight of $T_4$ in the full form set equal to the others, the difference vanishes — given C2.3 this is the same statement read backwards, not an independent test); `C3.3-min1` ($\mathcal R_{3,1}=\mathcal R_{1,3}=0$ on $\mathfrak{sl}_2$: the two forms agree at $\min(k,\ell)=1$, paper l. 175); `C3.3-heis` (Heisenberg: $E=\mathcal R=0$, $\ell_2(\Psi,\Psi')\ne0$; every $T_i$ vanishes individually there, so this control shows agreement of the two forms, not a cancellation among non-zero terms — the non-hollow test of the weights is the generic-data block).

## Verification

Script `codes/verify-paper-gap-7.py` (exact Grassmann polynomials over $\mathbb Q$, independent of 026's code), run `uv run --no-sync python codes/verify-paper-gap-7.py`, 2026-10-04:

```text
seed 20261004
[PASS] C2.1-nonhollow: all seven T nonzero: T1:97/2, T2:97/2, T3:72, T4:584/3, Tb1:97/2, Tb2:97/2, Tb3:72
[PASS] C1.1: contraction == Omega(L1, L2) for all seven configurations
[PASS] C1.1-break: Omega read without the rule-K sign does NOT match T4 (expected)
[PASS] C2.2: Tbar_i == T_i
[PASS] C2.2-break: plain g^{-1}: Tbar_i == -T_i (mirror pairs cancel), T1 != 0
[PASS] C2.1: E_(2,2) == sum of seven configurations, |E22| = 608/3
[PASS] C2.3: E_(2,2) == 2(T1+T2+T3) + T4
[PASS] C2.3-break: weight 2 on T4 does NOT match (expected)
[PASS] C1.3: R_(2,2) == T1+T2+T3+T4, |R22| = 184
[PASS] C3.1: R - E/2 == (1/2) Omega(l2(Psi,Psi'), l2(Psi,Psi'))
[PASS] C3.1-break: R - E/2 == Omega(l2,l2) (weight 1) fails (expected)
[PASS] C3.2-sl2: master relation E == 0 at every bidegree (18 V3 components)
[PASS] C3.2-break: Jacobi-violating [h,f] = -3f: E != 0, |E| = 128
[PASS] C3.3-sl2: R_(2,2) != 0 (12 monomials, |R22| = 128) and == T4/2
[PASS] C3.3-equal: weights set equal (T4 counted twice in the full form): R - (full)/2 == 0
[PASS] C3.3-min1: sl2: R_(3,1) = R_(1,3) = 0 (min(k,l) = 1 forms agree)
  sample R_(2,2) monomials (sl2): [((2, 3, 6, 8), Fraction(16, 1)), ((0, 5, 7, 8), Fraction(-8, 1)), ((2, 4, 7, 8), Fraction(16, 1))]
[PASS] C3.3-heis: Heisenberg: E == 0 and R == 0 (both forms hold), l2(Psi,Psi') != 0; T sizes T1:0, T2:0, T3:0, T4:0, Tb1:0, Tb2:0, Tb3:0
  sl2 T sizes: T1:0, T2:0, T3:128, T4:256, Tb1:0, Tb2:0, Tb3:128
summary: 17/17 PASS (seed 20261004)
```

Falsifiability: each identity has a break leg that fails as it should (`C1.1-break`: $\Omega$ without the rule-K sign; `C2.2-break`: plain $g^{-1}$ raising; `C2.3-break`, `C3.1-break`: the weight of $T_4$ changed; `C3.2-break`: Jacobi violated). The generic data do not satisfy the master equation, and every configuration is non-zero there (`C2.1-nonhollow`), so the weights are tested on non-vanishing terms. Not machine-checked: (086.14) (cited from 026 (3.18)); the equivalence of $\mathcal C(H_0,H_0)=0$ with CFL Def. 2.3 (CFL Prop. 7.2, cited via 026 §1.3).

## Statement for transcription (C4)

For the science-writer, to replace the gap comment at `paper/sections/07-ibl.tex` l. 188 (placement: after "…written with two fields." or after the sentence on the four configurations; the overall factor $\gs^2$ is dropped). Paper notation, every term a pairing of two odd fields.

Configuration display (fix #4), the four configurations with the factors of the Taylor expansion of $S(\Psi+\Psi')$:
```latex
\begin{equation}
  \label{eq:ibl:configurations-22}
  \begin{aligned}
    T_1 &= \tfrac{1}{2} \, \Omega(Q_B \Psi', \ell_3(\Psi, \Psi, \Psi')), &
    T_2 &= \tfrac{1}{2} \, \Omega(\ell_3(\Psi, \Psi', \Psi'), Q_B \Psi), \\
    T_3 &= \tfrac{1}{4} \, \Omega(\ell_2(\Psi', \Psi'), \ell_2(\Psi, \Psi)), &
    T_4 &= \Omega(\ell_2(\Psi, \Psi'), \ell_2(\Psi, \Psi')),
  \end{aligned}
\end{equation}
```
with one clause: "the numerical factors are those of the Taylor expansion of $S(\Psi + \Psi')$".

Display A, the degree-$(2,2)$ part of `eq:ibl:polarized-master`, divided by two:
```latex
\begin{equation}
  \label{eq:ibl:polarized-22}
  T_1 + T_2 + T_3 + \tfrac{1}{2} \, T_4
    = 0.
\end{equation}
```
Sentence to follow Display A (fix #1, required — the paper does not state how $\Omega$ and the products act on fields with Grassmann coefficients, and its most literal reading makes the residual vanish identically):
```latex
Here the products and $\Omega$ are evaluated on $\Psi$ and $\Psi'$ with the coefficients moved to the left, each coefficient passing only the basis states to its left; for two odd fields $L = L^a e_a$ and $K = K^b e_b$ this gives $\Omega(L, K) = \pair{e_a}{e_b} \, L^a K^b$, symmetric in $L$ and $K$.
```
Display B, introduced as the same contraction restricted to the operations with at least one input and one output (generating-function form, as announced in the paper's l. 157–158; not CFL Def. 2.3 verbatim, fix #2):
```latex
\begin{equation}
  \label{eq:ibl:io-22}
  T_1 + T_2 + T_3 + T_4
    = 0.
\end{equation}
```
Three sentences:
1. $T_1, \dots, T_4$ are the compositions $Q_B \circ \sprod{2}{2}$, $\sprod{2}{2} \circ Q_B$, $\sprod{1}{2} \circ \ell_2$ and $\ell_2 \circ \sprod{1}{2}$, each written as the pairing of the two products joined by the contracted strand.
2. In `eq:ibl:polarized-master` each of $T_1$, $T_2$, $T_3$ also appears with the roles of the two products exchanged, as $\ell_3 \circ \sprod{0}{2}$, $\sprod{2}{0} \circ \sprod{1}{3}$ and $\sprod{3}{0} \circ \sprod{0}{3}$, with the same value, whereas $T_4$ is its own mirror image and appears once; after division by two, $T_4$ therefore enters Display A with half the weight of $T_1$, $T_2$, $T_3$.
3. The relation among the operations with inputs and outputs only contains none of the mirror terms, so $T_1, \dots, T_4$ enter with the same weight, and Display B minus Display A is $\tfrac12 T_4$, the residual `eq:ibl:residual-22`.

Notes for the writer: (i) the paper's claim (l. 180) that the $\Omega(\ell_2(\Psi,\Psi'),\ell_2(\Psi,\Psi'))$ configuration "enters with half the weight of the three others" holds as stated once mirror pairs are grouped; with the seven ordered configurations listed, the weights are $2,2,2,1$. (ii) $\Omega$ on the odd fields $\ell_n(\dots)$ is read with the coefficients pulled to the left (A2); in components $\Omega(L,K)=\pair{e_c}{e_d}L^cK^d$, symmetric in $L,K$ — this is why $\Omega(\ell_2(\Psi,\Psi'),\ell_2(\Psi,\Psi'))$ need not vanish although $\Omega$ is graded antisymmetric. Stating it in the paper is required, not optional (fix #1): the appendix defines $\Omega(A,B)=(-1)^{\abs A}\pair AB$ and its antisymmetry only on homogeneous states, and does not imply the superfield reading. On two odd superfields the readings differ — (i) rule K: $\Omega(L,K)=g_{cd}L^cK^d$, symmetric; (ii) $\Omega$ as an odd form with the coefficients Koszul-passing it: $-g_{cd}L^cK^d$, symmetric, opposite sign; (iii) the definition read literally with $\abs A$ the superfield parity: $-(-1)^{\varepsilon_c}g_{cd}L^cK^d$, antisymmetric, so $\Omega(L,L)\equiv0$ and `eq:ibl:residual-22` would read as identically zero (this coincides with the plain-$\Delta$ contraction the paper rejects at l. 130). The record's $\mathcal R_{2,2}$ and $E_{2,2}$ are computed from derivatives of $S(\Psi+\Psi')$ and do not depend on the reading; only the notation $\Omega(\ell_2(\Psi,\Psi'),\ell_2(\Psi,\Psi'))$ does. The sentence after Display A fixes the reading. Rule K is inherited from 026 ((3.11) commentary) and is a candidate `local` entry for `knowledge/conventions.md` (orchestrator). (iii) The residual's direction is Display B minus Display A.

## Fix pass (critic iteration 1)

Critic report `agent/reports/critic-086-20261004T124200.md`; one line per finding, applied in order #1, #4, #2, #3, #5. Script unchanged; no claim's statement changes.

- #1 [major] Superfield reading of $\Omega$: the critic's sentence added after Display A in C4; note (ii) corrected (required, not implied by the appendix; readings (i)–(iii) listed). Changed: C4 justification text only. Dependents: none (C4 is the root's leaf for transcription; C1–C3 computed reading-independently from $S(\Psi+\Psi')$ and still hold).
- #4 [major] Weights invisible in the displays: C4 now has the configuration display naming $T_1,\dots,T_4$ (critic's LaTeX, label `eq:ibl:configurations-22`, with the Taylor-factor clause), then Display A $T_1+T_2+T_3+\tfrac12T_4=0$ and Display B $T_1+T_2+T_3+T_4=0$; sentences 1–3 refer to $T_i$, sentence 2 says relative to what the weight is half, sentence 3 gives B − A $=\tfrac12T_4$. Changed: C4 statement (presentation; content identical to (086.6), (086.10), (086.11)); A2 now notes that rule K is not the paper's and is stated in C4. Dependents: none.
- #2 [minor] Display B introduced as the same contraction restricted to operations with at least one input and one output (generating-function form), not as CFL Def. 2.3 verbatim; C1.2 and Block 2 Setup reworded accordingly (weights from CFL Prop. 7.2 in CFL's grading, signed identity = generating-function form). Changed: C1.2 justification only (statement unchanged). Dependents: C1 (holds — weights unaffected), C3 (holds), C4 (holds; wording updated).
- #3 [minor] Script normalisation: (086.15) commentary now states that the script uses $\vertex3=2f_{jk}{}^i$ (confirmed by reading `lie_model`/`structure`), so the quoted coefficient 16 is for the doubled vertex ($\pm4$ with $\vertex3=f$). Script unchanged. Changed: C3.3 justification text only. Dependents: C3 (holds), C4 (holds).
- #5 [minor, outside the passage] Note added under the claim tree for the orchestrator: paper l. 132 ("overall sign for one output") may conflict with `eq:ibl:generating` at $n=1$; Block 2 Setup now marks its $\sprod{k}{\ell}$-form as the paper's, unchecked, and used only for labels. Paper not edited. Changed: Block 2 Setup wording. Dependents: none (all computations use the vertex form of $H_{k,\ell}$).

Changed nodes: A2 (justification text), C1.2 (justification), C3.3 (justification), C4 (statement presentation). Statements of C1, C2, C3 unchanged; all dependents hold. Open gaps: none.
