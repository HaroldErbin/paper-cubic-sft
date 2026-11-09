# Derivation 061 — PH2 (a): the nested-kernel conditions of the dressed tower, reduced to PH1 and to statements on $\tilde M_k$

- **Brief:** `agent/briefs/active-computator-ph2a-20260926T103500.md` (Task 10a).
- **Script:** `codes/verify-ph2a.py`; logs `agent/scratch/ph2a-run1.log` (original), `agent/scratch/ph2a-run2.log` (fix pass 1).
- **Author:** computator (Opus), 2026-09-26. Fix pass 1: computator (Opus), 2026-10-01, on `agent/reports/critic-061-20260930T233500.md` (§8).

## Status

Status: fix pass 2 done (critic `agent/reports/critic-061-iter2-20261001T023000.md`, all 10 findings + 1 note applied, §9; script untouched, no run). Before that: fix pass 1 done (critic `agent/reports/critic-061-20260930T233500.md`, all 16 findings applied, §8). Script 57/57 PASS on seeds 20260926 and 41 (`agent/scratch/ph2a-run2.log`), 17 break legs. Claim tree updated (changed nodes marked *[fix pass 1: …]*), §3–§7 consolidated. Next: promotion by the orchestrator (final ledger texts in `agent/scratch/061-ledger-texts.md`); the critic asks only a grep confirmation.

## Task and objective

**Literal task.** List the nested invertibility conditions of R26's dressed tower level by level, write each kernel as $\hat H_k(g,\Psi)=\tilde M_k+O(g)$ with $\tilde M_k$ explicit, prove that at $g=0$ the level-$k$ condition is PH1 ($k=2$) or the invertibility of $\tilde M_k$ on its quotient ($k\ge3$), prove the extension to a neighbourhood of $g=0$, say what "stable kernel" must mean for that and whether PH1 implies it, and identify the $O(g^0)$ term of every condition or the term the reduction misses. Machine check in the finite model with a break leg.

**Motivating objective.** PH2 is a standing hypothesis of R26 (all-orders tower). Reducing it to PH1 plus a finite list of named operator statements shortens the tower's hypothesis list and makes each remaining item checkable.

## Conventions

- Notation of record 019 (R26): $a_k=g^{2k-2}/(2k)!$, $P_k=\Psi^{\otimes k}$, $\mathcal S_k:=\operatorname{Sym}^k\mathcal H_0$, parents $T_n$ ($T_4=V_4$, $T_5=V_5$, $T_n$ for $n\ge6$ from R26's recursion), kinetic $\tilde M_k=T_{2k}\rvert_{(k|k)}$, source map $L_k(\Psi):\mathcal S_{k-1}\to\mathcal S_k^{*}$, $L_k(\Psi)\Sigma_{k-1}=T_{2k}(\,\cdot_{k}\,;\Sigma_{k-1},\Psi)$, $\tilde u_2=V_4(\cdot,P_2)$, odd coupling $T_{2k+1}(\Sigma_k,\Sigma_k,\Psi)$.
- No project convention (`knowledge/conventions.md` C1, C2: pairing and antibracket signs) enters: the statements are about symmetric bilinear forms of the Jacobi operator, not about ghost signs.

## Claim tree

- **A1** Algebraic layer of R26: $\mathcal H_0$ finite-dimensional — R26's finite-dimensional class (real multilinear $V_n$, parents in the shared-parent class; genericity not assumed); for the string vertices, a level truncation *with the momenta fixed or discretised* (a fixed level alone still carries continuous momenta, PH3, R53) —, the $V_n$ and the parents $T_n$ real multilinear forms, tower truncated at a finite $K\ge2$ (019 §1). Every statement is at fixed $(L,K)$ unless said otherwise, $L$ denoting a finite-dimensional truncation in this sense. For the string vertices at a fixed level with continuous momenta, the determinant and neighbourhood statements (3.3), (3.6) are not covered. *[fix pass 1: statement changed, #1; fix pass 2: wording, #6]*
- **A2** Shared-parent class of R26 (019 §4): $\tilde M_k$ and $L_k$ are the $(k|k)$ and $(k|k{-}1,1)$ restrictions of one parent $T_{2k}$. The values of the forced diagonals play no role below; the finite model draws the parents at random within the class.
- **A3** "Invertible on the quotient $\mathcal S_k/N$" for a symmetric form $B$ with $N\subseteq\operatorname{rad}B$: the induced form on $\mathcal S_k/N$ is non-degenerate, i.e. $\operatorname{rad}B=N$. Quotients are taken by subspaces satisfying the descent condition (D) of §3 (joint kernels, 034 §5.2 (C$_\infty$)); the canonical choice is $N_k=N_{k,\infty}$, eq. (3.1).
- **C1** (root) At fixed $(L,K)$ ($L$ a finite-dimensional truncation, A1), in the shared-parent class: $\hat H_k(g,\Psi)$ depends on $g\Psi$ only; with quotients satisfying the descent condition (D), the nested conditions of R26 hold at $g=0$ iff $\operatorname{rad}\tilde M_k=N_k$ for $k=2,\dots,K$, which forces the canonical quotient $N_k=N_{k,\infty}=\ker\tilde M_k$; the $k=2$ instance is PH1's invertibility clause on $\operatorname{Sym}^2\mathcal H_0/\ker V_4$, consistent with the tower iff (3.5) ($V_5(\ker V_4,\mathcal S_2,\Psi)=0$ and, for $K\ge3$, $T_6(\cdot_3;\ker V_4,\Psi)=0$, which is a presentation condition only modulo a vertex condition: it is satisfiable only if the forced diagonal vanishes on $\operatorname{Sym}^6\mathcal H_0\cap(\mathcal S_3\otimes\ker V_4\otimes\mathcal H_0)$, e.g. $V_6(\chi^6)=0$ when $\chi\otimes\chi\in\ker V_4$, the diagonal part of 034's (C$^{(6)}$); (C$^{(6)}$) with R38 suffices; vacuous at level 0). They then hold on $\lvert g\Psi\rvert<r_{L,K}$ for any norm on $\mathcal H_0$ (the argument gives no bound uniform in $L$ or $K$; uniformity would need a norm across levels, which PH1 does not fix), and R26's formal-series statement uses only the $g=0$ form. The $O(g^0)$ term of $\hat H_k$ is $\tilde M_k$ under these conditions. Every term a level-by-level reduction can miss requires a higher level that already fails at $g=0$; (4.5) gives them for a one-dimensional excess with pole order $\le2$ along the ray, (4.5′) for orders 3 and 4 (not checked); such a failure generically (whenever $T_7(n,P_3,\cdot)\not\equiv0$) enters the value as a term rational in $\Psi$: for a block-symmetric parent ($\ell=0$) at $n=6$ for pole order 2 and at $n=7$ for a simple pole (C1.10), otherwise already at $n=4$ (order 2) or $n=5$ (simple pole), by (4.5) (not machine-checked in the value), even where it is invisible in $\hat H_2(0)$. The stability needed is descent (D): stability in $g$, (S$_g$), together with the source clause $L_k(\Psi)^\top N_k=0$ (necessary; automatic at $k=2$ and for block-symmetric parents) (D2 up to the definiteness proviso of (4.1)); it is not implied by PH1, and PH2 strictly extends PH1 across the class. [by C1.1–C1.10] *[fix pass 1: statement changed, #1, #2, #4, #5, #6, #7; fix pass 2: statement changed (scope of the $n=6,7$ entry, $T_6$ clause, (D) proviso, (4.5′) unchecked), #1, #2, #3, #4]*
  - **C1.1** $\hat H_k(g,\Psi)=H_k(g\Psi)$, a rational matrix function of $\varphi=g\Psi$. [eqs. (2.1)–(2.2)] [check: C1.1-scaling]
  - **C1.2** If $\tilde M_{k+1},\dots,\tilde M_K$ are invertible, $\hat H_k=\tilde M_k-\tfrac{g}{2k+1}T_{2k+1}(\cdot,\cdot,\Psi)-g^2c_kL_{k+1}^\top\tilde M_{k+1}^{-1}L_{k+1}+O(g^3)$; in particular $\det\hat H_k(g)\to\det\tilde M_k$. [by C1.1; eq. (2.3)] [check: C1.2-series-k2, C1.2-series-k3, C1.2-series-k4, C1.2-coeff0-*, C1.2-coeff1-*, C1.2-limit, C1.2-jacobi-rescaling]
  - **C1.3** Under (D) every $H_k(\varphi)$ descends to $Q_k=\mathcal S_k/N_k$ and the $N_k$ components drop out of the action; a quotient by $N\not\subseteq N_{k,\infty}$ is not a function on $Q_k$. [by A3; eqs. (3.1)–(3.2)] [check: C1.3-stable-kernel, C1.3-descent-D3, C1.3-complement-indep, C1.3-descent-D2] *[fix pass 1: coverage only, #12]*
  - **C1.4** Under (D): $(\mathrm N_2),\dots,(\mathrm N_K)$ at $g=0$ $\iff$ $\operatorname{rad}\tilde M_k=N_k$ for all $k$, and then $N_k=N_{k,\infty}=\ker\tilde M_k$; at $k=2$ with $N_2=\ker V_4$ this is PH1's invertibility clause (automatic at fixed finite-dimensional $L$; the content is the choice of quotient), and the quotient is consistent iff $V_5(\ker V_4,\mathcal S_2,\Psi)=0$ and, for $K\ge3$, $L_3(\Psi)\ker V_4=0$, i.e. $T_6(\cdot_3;\ker V_4,\Psi)=0$, satisfiable only if the forced diagonal vanishes on $\operatorname{Sym}^6\mathcal H_0\cap(\mathcal S_3\otimes\ker V_4\otimes\mathcal H_0)$ (vacuous at level 0); at $K=2$ this is R38 (1.2) exactly. [by A3, C1.2, C1.3, R38; eqs. (3.3)–(3.5)] [check: C1.4-quotient-det, C1.4-H2-at-0, C1.4-kerV4-descent, C1.4-kerV4-R38-break, C1.4-kerV4-T6-break, C1.4-kerV4-T6-order, C1.4-K2-limit] *[fix pass 1: statement changed (canonical quotient forced, $K\ge3$ qualifier, $K=2$ limit), coverage added, #2, #12, #15; fix pass 2: $T_6$ clause qualified, #2]*
  - **C1.5** Under (D) and C1.4's condition, all $(\mathrm N_k)$ hold on $\lvert g\Psi\rvert<r_{L,K}$; for any norm on the finite-dimensional $\mathcal H_0$; no bound uniform in $L$ follows from this argument (PH1 declines a bounded inverse and fixes no norm across levels); the formal-series inverse used by R26 needs only the $g=0$ condition. [by C1.1, C1.3, C1.4; eq. (3.6), §3(e)] [check: C1.5-radius-k2, C1.5-radius-k3, C1.5-radius-k4] *[fix pass 1: wording (norm), content unchanged, #6]*
  - **C1.6** The continuity argument needs stability in $g$, (S$_g$): $N_k\subseteq\operatorname{rad}\hat H_k(g,\Psi)$ near $g=0$; (D) implies it, D1 is necessary, D2 is necessary when $\tilde M_{k+1}$ is definite on $Q_{k+1}$. (S$_g$) contains no counterpart of D3 ($L_k(\Psi)^\top N_k=0$), which is also necessary: without it the level-$(k-1)$ Schur term needs $\hat H_k^{-1}$ on a covector outside $N_k^\perp$ (the Gaussian in $\Sigma_k$ has a linear term along a flat direction); D3 is automatic at $k=2$ and for block-symmetric parents (3.7). The stability required is therefore (D) = (S$_g$) + D3, up to the definiteness proviso for D2. PH1 (a statement on $V_4$, on $\tilde M_k$ and on stability in the level $L$) does not imply (D), nor conversely. [by C1.3, C1.9; eq. (4.1), §4(a)–(b)] [check: C1.6-kernel-moves, C1.3-complement-indep-break, C1.3-descent-D2-break] *[fix pass 1: statement changed, #4, #11]*
  - **C1.7** If level $k+1$ fails at $g=0$ by a one-dimensional excess kernel $n$ with $\ell=L_{k+1}(\Psi)^\top n$: $[g^1]\hat H_k$ acquires $-c_k\ell\ell^\top/\alpha_1$ (pole order 1), $[g^0]\hat H_k$ acquires $-c_k\ell\ell^\top/\alpha_2$ (pole order 2), direction-dependent in $\Psi$. For block-symmetric parents $\ell=0$, and $[g^0],[g^1]$ are unchanged when the pole along the ray has order $\le2$; orders 3 and 4 shift $[g^1]$ and $[g^0]$ by $-c_kuu^\top/\alpha_p$, $u=-J_{k+1}(\Psi)^\top w$, $w=A(n,\cdot)$ (4.5′). [by C1.9; eqs. (4.2)–(4.5′)] [check: C1.7-protected, C1.7-missed-g1, C1.7-missed-g0, C1.7-direction] *[fix pass 1: statement changed (pole-order proviso carried, orders 3, 4 stated, not checked), #5]*
  - **C1.8** PH2 strictly extends PH1: there are shared-parent towers with $V_4$ non-degenerate and the Jacobi operator invertible at small $g\ne0$, in which $\det\hat H_3$ vanishes at $g=0$ (a statement on logical strength within the class, not a claim that PH2 fails for the string vertices). [by check: C1.8-break-PH1-holds, C1.8-break-level3-fails] *[fix pass 1: scope sentence, content unchanged, #16]*
  - **C1.9** For a parent symmetric in its last $k$ slots (in particular fully polarized), $L_k(\Psi)=\tilde M_kJ_k(\Psi)$; hence $L_k^\top\operatorname{rad}\tilde M_k=0$, and under C1.4's condition with canonical quotients $\operatorname{Sym}(N_{k,\infty}\otimes\mathcal H_0)\subseteq N_{k+1,\infty}$ (the inclusion in $\ker\tilde M_{k+1}$ is automatic; only "$\subseteq N_{k+1,\infty}$" uses C1.4's condition). [eqs. (3.7)–(3.8)] [check: C1.9-factor-k3, C1.9-factor-k4, C1.9-factor-break, C1.3-descent-D2-break] *[fix pass 1: precision, content unchanged, #9]*
  - **C1.10** Level 3, block-symmetric parent, $K=3$, a kernel $n$ of $\tilde M_3$ outside $N_3$ (levels below regular, i.e. $\tilde M_j$ invertible for $2\le j<k$; here $k=3$): the kernel enters the value $S=\tfrac12V_2+\tfrac g{3!}V_3+\tfrac{g^2}{4!}\tilde u_2^\top\hat H_2^{-1}\tilde u_2$ (019 §2) as a term rational in $\Psi$ — at $g^4$ ($n=6$) if $T_7(n,n,\cdot)\equiv0$ (pole order 2), $\Delta S\rvert_{g^4}=-\frac{g^4}{6!}\,T_7(n,P_3,\Psi)^2/\big(T_7(n,\cdot,\Psi)^\top\tilde M_3^+T_7(n,\cdot,\Psi)\big)$; first at $g^5$ ($n=7$) for a simple pole, $\Delta S\rvert_{g^5}=-\frac{g^5}{7!}\,T_7(n,P_3,\Psi)^2/T_7(n,n,\Psi)$ — while the regular part reproduces the collapse value $a_3T_6(\Psi^6)$ for any generalised inverse. The general-$k$ form (4.9) follows by the collapse identity (019 §3) and is not checked; it needs $\tilde M_j$ invertible for $2\le j<k$. The $n=6,7$ entry is the block-symmetric case ($\ell=0$); for other parents the failure enters earlier (C1.7, (4.5)). [by C1.7, C1.9, 019 §2–§3; eqs. (4.6)–(4.9)] [check: C1.10-order2-g2, C1.10-order2-collapse, C1.10-order2-value-n6, C1.10-order2-rational, C1.10-order1-g2, C1.10-order1-g3, C1.10-order1-value] *[fix pass 1: new node, replaces the §4 remark, #7; fix pass 2: scope $\ell=0$ stated, #1, #5]*

Open gaps: none
Hypotheses in force: none (PH1 and PH5 are the statements C1 reduces PH2 to, not premises of C1)

## 1. The nested conditions, level by level

Source: 019 §1–§2 (R26 (1)–(2)); 034 §5.2 for the quotient form. The Jacobi operator of the scheme-B action truncated at $K$ is block-tridiagonal on $\bigoplus_{k=2}^K\mathcal S_k$,

$$
\mathcal A_{kk}=a_k\hat M_k,\qquad
\hat M_k=\tilde M_k-\tfrac{g}{2k+1}\,T_{2k+1}(\cdot,\cdot,\Psi),\qquad
\mathcal A_{k,k-1}=-a_kL_k(\Psi),
\tag{1.1}
$$

and the nested kernels are its successive Schur complements, eliminated top-down,

$$
\hat H_K=\hat M_K,\qquad
\hat H_k=\hat M_k-g^2c_k\,L_{k+1}(\Psi)^{\top}\hat H_{k+1}^{-1}L_{k+1}(\Psi),\qquad
c_k:=\frac{(2k)!}{(2k+2)!}=\frac{a_{k+1}}{g^2a_k}.
\tag{1.2}
$$

The nested condition at level $k$ is: **$(\mathrm N_k)$ $\hat H_k(g,\Psi)$ is invertible on the quotient $\mathcal S_k/N_k$ for $g$ in a neighbourhood of $0$.** It presupposes $(\mathrm N_{k+1}),\dots,(\mathrm N_K)$, since $\hat H_k$ is only defined once $\hat H_{k+1}^{-1}$ is. The list, with the $g=0$ operator of each (the claim $\hat H_k(0,\Psi)=\tilde M_k$ is C1.2, proved in §2):

| level | $\hat H_k$ | $O(g)$ term | $O(g^2)$ term | $\tilde M_k=\hat H_k(0)$ | first enters the value at |
|---|---|---|---|---|---|
| $k=2$ | $V_4-\tfrac g5V_5(\cdot,\cdot,\Psi)-\tfrac{g^2}{30}L_3^\top\hat H_3^{-1}L_3$ | $-\tfrac15V_5(\cdot,\cdot,\Psi)$ | $-\tfrac1{30}L_3^\top\tilde M_3^{-1}L_3$ | $V_4\rvert_{\mathcal S_2}$ (R1, R17: $K_\Psi=V_4-\tfrac g5W$) | $g^2$ ($n=4$) |
| $k=3$ | $\tilde M_3-\tfrac g7T_7(\cdot,\cdot,\Psi)-\tfrac{g^2}{56}L_4^\top\hat H_4^{-1}L_4$ | $-\tfrac17T_7(\cdot,\cdot,\Psi)$ | $-\tfrac1{56}L_4^\top\tilde M_4^{-1}L_4$ | $T_6\rvert_{(3\mid3)}$, $T_6=-6!\operatorname{Pol}(A_4)$ (019 §4) in the polarized presentation, R21's block composite $\Phi^\top V_4^{-1}\Phi$ in the canonical one (same Veronese diagonal, 019 §4 point 3) | $g^4$ ($n=6$) |
| $k=4$ | $\tilde M_4-\tfrac g9T_9(\cdot,\cdot,\Psi)-\tfrac{g^2}{90}L_5^\top\hat H_5^{-1}L_5$ | $-\tfrac19T_9(\cdot,\cdot,\Psi)$ | $-\tfrac1{90}L_5^\top\tilde M_5^{-1}L_5$ | $T_8\rvert_{(4\mid4)}$ (R26 (6)) | $g^6$ ($n=8$) |
| general $k$ | (1.2) | $-\tfrac1{2k+1}T_{2k+1}(\cdot,\cdot,\Psi)$ | $-c_kL_{k+1}^\top\tilde M_{k+1}^{-1}L_{k+1}$ | $T_{2k}\rvert_{(k\mid k)}$, $T_{2k}=-(2k)!\operatorname{Pol}(A_{2k-2})$ | $g^{2k-2}$ ($n=2k$) |
| $k=K$ (top) | $\hat M_K$ (affine in $g$) | $-\tfrac1{2K+1}T_{2K+1}(\cdot,\cdot,\Psi)$ | none | $T_{2K}\rvert_{(K\mid K)}$ | $g^{2K-2}$ |

($c_2=\tfrac1{30}$, $c_3=\tfrac1{56}$, $c_4=\tfrac1{90}$.) The quotients: $N_2=\ker V_4\rvert_{\mathcal S_2}$ as in PH1; for $k\ge3$, $N_k$ is the subspace quotiented at level $k$, fixed in §3.

011 §6 holds no further condition: it is the superseded $O(g_s^4)$ spec, with the single kernel $V_4$ (level 2); its content is the $k=2$ row.

## 2. Scaling and the $O(g^0)$ term

\subsection*{Setup}
A1, A2. Put $\varphi:=g\Psi\in\mathcal H_0$. All maps below are multilinear in $\Psi$; $\tilde M_k$ carries no $\Psi$.

\subsection*{Derivation}

$$
\begin{aligned}
\hat M_k(g,\Psi)&=\tilde M_k-\tfrac1{2k+1}T_{2k+1}(\cdot,\cdot,\varphi),\\
g^2L_{k+1}(\Psi)^{\top}X\,L_{k+1}(\Psi)&=L_{k+1}(\varphi)^{\top}X\,L_{k+1}(\varphi)\quad\text{for any }X,
\end{aligned}
\tag{2.1}
$$

so that, by downward induction from $k=K$,

$$
\hat H_k(g,\Psi)=H_k(\varphi),\qquad
H_K(\varphi)=\tilde M_K-\tfrac{T_{2K+1}(\cdot,\cdot,\varphi)}{2K+1},\qquad
H_k(\varphi)=\tilde M_k-\tfrac{T_{2k+1}(\cdot,\cdot,\varphi)}{2k+1}-c_k\,L_{k+1}(\varphi)^{\top}H_{k+1}(\varphi)^{-1}L_{k+1}(\varphi).
\tag{2.2}
$$

If $H_{k+1}(0)=\tilde M_{k+1}$ is invertible, $H_{k+1}(\varphi)^{-1}=\tilde M_{k+1}^{-1}+O(\varphi)$ is analytic at $\varphi=0$ and, since $L_{k+1}(0)=0$,

$$
\hat H_k(g,\Psi)=\tilde M_k
-\frac{g}{2k+1}\,T_{2k+1}(\cdot,\cdot,\Psi)
-g^2c_k\,L_{k+1}(\Psi)^{\top}\tilde M_{k+1}^{-1}L_{k+1}(\Psi)+O(g^3).
\tag{2.3}
$$

\subsection*{Commentary}
(2.1): multilinearity; the Schur factor $g^2$ is exactly two powers of $g$, one for each source map. (2.2) is the operator form of 019 §4 point 1 (the scaling $\Psi\to t\Psi$, $g\to g/t$ fixes $\varphi$). $H_k$ is a rational matrix function of $\varphi$. (2.3) follows by induction: the top level is affine in $\varphi$, and each Schur step keeps analyticity at $0$ as long as the level above is invertible there.

\subsection*{Result}
$$\boxed{\hat H_k(g,\Psi)=H_k(g\Psi),\qquad [g^0]\hat H_k=\tilde M_k\ \text{ whenever }\tilde M_{k+1},\dots,\tilde M_K\text{ are invertible.}}$$
The $O(g)$ term is the odd coupling alone, the $O(g^2)$ term the first Schur rung.

\subsection*{Verification}
Checks `C1.1-scaling` (exact, $K=4$, with a break leg: $g^1$ in place of $g^2$ in the Schur term) and `C1.2-*` (§6).

## 3. Quotients, the reduction at $g=0$, and the neighbourhood

\subsection*{Setup}
A1–A3. For $k\ge2$ define the **joint kernel** of level $k$,

$$
N_{k,\infty}:=\Big\{n\in\mathcal S_k:\ \tilde M_kn=0,\ \ T_{2k+1}(n,\cdot,\Psi)=0,\ \ L_{k+1}(\Psi)\,n=0,\ \ L_k(\Psi)^{\top}n=0\ \ \forall\Psi\Big\},
\tag{3.1}
$$

(for $k=2$ the last clause reads $\tilde u_2(n)=V_4(n,P_2)=0$, automatic from $\tilde M_2n=0$). It is the set of $\Sigma_k$ directions annihilated by every block of the Jacobi operator (1.1) in which $\Sigma_k$ appears: 034 §5.2 (C$_\infty$), which writes the two source clauses as $L_k(\Psi)\rvert_{N_k}=0$, $L_k(\Psi)^\top\rvert_{N_{k-1}}=0$ in the transposed convention for $L_k$; after transposition the clauses agree, and 034's further clause on the forced diagonals is redundant on the Jacobi blocks. Labels for the three non-kinetic clauses of (3.1): **D1** the odd clause $T_{2k+1}(n,\cdot,\Psi)=0$; **D2** the upward clause $L_{k+1}(\Psi)n=0$; **D3** the source clause $L_k(\Psi)^\top n=0$. A choice of quotients $N_k\subseteq\mathcal S_k$ satisfies the **descent condition** (D) if $N_k\subseteq N_{k,\infty}$ for every $k$. Write $Q_k:=\mathcal S_k/N_k$.

At the top level $k=K$ the clause D2 does not exist, so $N_{K,\infty}$ depends on $K$ and can shrink when the tower is extended: (D) at truncation $K$ does not give the level-$K$ condition at $K+1$. The parents $T_{n\ge6}$ are built from mismatches that contain the lower $\hat H^{-1}$ (019 §4), so (3.4) at the lower truncations is what makes them defined (034 §5.2: "(C$_\infty$) at level $k$ is needed for the level-$(k+1)$ dressings to be defined"); the finite model draws the parents at random in the class (A2) and sidesteps this.

\subsection*{Derivation}

**(a) Descent.** Under (D) every term of (2.2) annihilates $N_k$ in each slot: $\tilde M_k$ and $T_{2k+1}(\cdot,\cdot,\varphi)$ by (3.1), the Schur term because $L_{k+1}(\varphi)n=0$. The Schur term needs $H_{k+1}^{-1}$ only on $L_{k+1}(\varphi)\mathcal S_k\subseteq N_{k+1}^{\perp}=Q_{k+1}^{*}$ (clause $L_{k+1}^{\top}N_{k+1}=0$), where the inverse of the induced form $Q_{k+1}\to Q_{k+1}^{*}$ is defined. Hence

$$
H_k(\varphi)\ \text{descends to }Q_k\text{ wherever it is defined, and the }N_k\text{ components of }\Sigma_k\text{ drop out of the action.}
\tag{3.2}
$$

**(b) Reduction at $g=0$.** By (2.3) on the quotients: if $\tilde M_j$ is non-degenerate on $Q_j$ for $j=k+1,\dots,K$, then $H_k(0)=\tilde M_k$ on $Q_k$, and

$$
(\mathrm N_k)\text{ at }g=0\iff\tilde M_k\text{ non-degenerate on }Q_k\iff\operatorname{rad}\tilde M_k=N_k .
\tag{3.3}
$$

Downward induction from $k=K$ gives the conjunction

$$
(\mathrm N_2),\dots,(\mathrm N_K)\ \text{at }g=0\iff\operatorname{rad}\tilde M_k=N_k\quad(k=2,\dots,K).
\tag{3.4}
$$

With the canonical quotients $N_k=N_{k,\infty}$ (the largest ones (D) allows), (3.4) reads: **every null vector of the level-$k$ kinetic is a joint null vector**, $\ker\tilde M_k=N_{k,\infty}$. The canonical choice is in fact forced: under (D), $N_k\subseteq N_{k,\infty}\subseteq\ker\tilde M_k=\operatorname{rad}\tilde M_k$ (the first clause of (3.1)), so (3.4) gives $N_k=N_{k,\infty}=\ker\tilde M_k$; the freedom to take "any (D) quotient" is only apparent.

**(c) Level 2 and PH1.** $\tilde M_2=V_4\rvert_{\mathcal S_2}$. With $N_2=\ker V_4$ (PH1's quotient), (3.3) at $k=2$ is PH1's clause "the descended $m_2$ is invertible on the truncated quotient" (at a fixed finite-dimensional truncation, A1, the radical quotient is non-degenerate by construction; the content of PH1 there is which kernel is quotiented, and its stability clause; at a fixed level with continuous momenta, injective is not invertible and this step is not covered). The quotient $\operatorname{Sym}^2\mathcal H_0/\ker V_4$ is consistent with the tower iff $\ker V_4\subseteq N_{2,\infty}$:

$$
V_5(\ker V_4,\mathcal S_2,\Psi)=0\ \ \text{(R38 (1.2))},\qquad
L_3(\Psi)\ker V_4=0\ \ \text{i.e. }T_6(\,\cdot_3\,;\ker V_4,\Psi)=0\ \ (K\ge3).
\tag{3.5}
$$

Neither is part of PH1. The first is PH5's second clause (D1 at $k=2$). The second (D2 at $k=2$) is in no hypothesis row. It is necessary when $\tilde M_3$ is definite on $Q_3$, and generically otherwise: if $L_3(\Psi)n\ne0$ for some $n\in\ker V_4$, the Schur term lifts $n$ at $O(g^2)$, $\hat H_2(g)n=-g^2c_2L_3^\top\tilde M_3^{-1}L_3n+O(g^3)\ne0$ generically (check `C1.4-kerV4-T6-order`). It constrains the $(3|2,1)$ block of the parent $T_6$, i.e. $T_6=0$ on $W:=\mathcal S_3\otimes\ker V_4\otimes\mathcal H_0$. Off the Veronese diagonal that block is presentation freedom (R26 (4)), but the clause is not purely a presentation condition: the forced diagonal fixes $T_6$ on $\operatorname{Sym}^6\mathcal H_0$, so a presentation satisfying the clause exists only if the forced diagonal vanishes on $\operatorname{Sym}^6\mathcal H_0\cap W$ (symmetric 6-tensors all of whose 2-slices lie in $\ker V_4$). If $\ker V_4\ni\chi\otimes\chi$ (rank one), then $\chi^{\otimes6}\in W$ and the clause at $(\chi^3;\chi\chi,\chi)$ reads $T_6(\chi^6)=0$; with R38, $V_5(\cdot,\chi\chi,\chi)=0$, so the composite part of the diagonal vanishes there and the clause requires $V_6(\chi^6)=0$, the diagonal part of 034's (C$^{(6)}$) ($\Xi=A=B=\chi\chi$). If the $(3|3)$ block is swap-symmetric, the clause also forces $\chi^3\in\ker\tilde M_3$ ($\tilde M_3(\sigma,\chi^3)=T_6(\sigma;\chi\chi\otimes\chi)=0$), a level-3 kernel that PH2 (b) must then quotient. If the intersection is zero the clause is pure presentation freedom (the script's case: $\dim\mathcal H_0=2$, $m=(2,-1,3)$ of rank 2). So the clause is a presentation condition modulo a vertex condition; (C$^{(6)}$) with R38 suffices for it to be satisfiable in some presentation, and (C$^{(6)}$) is not necessary for it in a given presentation: 034 §5.2 states "$T_6\to$ (C$^{(6)}$)" in one line, and in the fully polarized presentation the two legs of $n$ can split across the two $V_5$ factors of the composite part of $A_4$, which (1.2) does not kill. The clause belongs with PH2 (b), not with PH5 (a hypothesis on the vertices), but its vertex-side part is carried by neither; it is vacuous at level 0 ($\ker V_4=0$, R53). D3 at $k=2$ is $\tilde u_2(n)=V_4(n,P_2)=0$, automatic. Both clauses of (3.5) are vacuous if $\ker V_4=0$ (PH5's first clause; at level 0 on the tachyon-pair block, R53: $\ker K_P(s)=\{0\}$).

*$K=2$ limit.* At $K=2$, $\hat H_2=V_4-\tfrac g5V_5(\cdot,\cdot,\Psi)$ exactly, the $T_6$ clause is absent, and (3.5) reduces to $V_5(\ker V_4,\mathcal S_2,\Psi)=0$: R38 (1.2) verbatim (check `C1.4-K2-limit`).

**(d) Neighbourhood.** Assume (D) and $\operatorname{rad}\tilde M_k=N_k$ for $k=2,\dots,K$ at fixed $(L,K)$. Fix complements $C_k\cong Q_k$. By (3.2) the matrix of $H_k(\varphi)\rvert_{C_k}$ represents the induced form on $Q_k$, for every $\varphi$ at which it is defined. Downward induction: $\det H_K(\varphi)\rvert_{C_K}$ is a polynomial in $\varphi$ with value $\det\tilde M_K\rvert_{C_K}\neq0$ at $0$, hence non-zero on a ball $\lvert\varphi\rvert<r_K$; on it $H_{K-1}(\varphi)$ is defined and rational, with $\det H_{K-1}(0)\rvert_{C_{K-1}}=\det\tilde M_{K-1}\rvert_{C_{K-1}}\neq0$, hence non-zero on $\lvert\varphi\rvert<r_{K-1}\le r_K$; and so on. With $r_{L,K}:=r_2$,

$$
(\mathrm N_k)\ \text{holds for all }k\text{ and all }(g,\Psi)\text{ with }\lvert g\Psi\rvert<r_{L,K};\ \text{for fixed }\Psi:\ \lvert g\rvert<r_{L,K}/\lvert\Psi\rvert .
\tag{3.6}
$$

**(e) Formal series.** In the ring of formal power series in $g$ with matrix coefficients, $\hat H_k$ is invertible iff its constant term is invertible on $Q_k$. R26's theorem is a formal-series statement (019 §4). It therefore uses (3.4) and nothing else; the neighbourhood (3.6) is automatic at each $(L,K)$ and matters only for a non-perturbative reading of the continued fraction (R26 carve-out (b)).

**(f) Block-symmetric parents.** If $T_{2k}$ is symmetric in its last $k$ slots (true for fully polarized parents, $T_{2k}=-(2k)!\operatorname{Pol}(A_{2k-2})$), then $T_{2k}(\Sigma_k;\Sigma_{k-1},\Psi)=T_{2k}(\Sigma_k;\operatorname{Sym}(\Sigma_{k-1}\otimes\Psi))$, i.e.

$$
L_k(\Psi)=\tilde M_k\,J_k(\Psi),\qquad J_k(\Psi)\Sigma_{k-1}:=\operatorname{Sym}(\Sigma_{k-1}\otimes\Psi)\in\mathcal S_k .
\tag{3.7}
$$

Consequences: the clause $L_k^{\top}n=0$ of (3.1) is automatic for $n\in\operatorname{rad}\tilde M_k$; and the clause $L_{k+1}(\Psi)n=0$ becomes $J_{k+1}(\Psi)n\in\operatorname{rad}\tilde M_{k+1}$. Under (3.4) with canonical quotients this forces

$$
\operatorname{Sym}\big(N_{k,\infty}\otimes\mathcal H_0\big)\subseteq N_{k+1,\infty}:
\tag{3.8}
$$

a kernel at level $k$ propagates to every level above. In particular a level-2 kernel is compatible with the descent only if $\tilde M_3$ vanishes on $\operatorname{Sym}(\ker V_4\otimes\mathcal H_0)$.

\subsection*{Commentary}
(3.2): the Schur complement of a block operator that annihilates a subspace in every block annihilates it too; the inverse is only ever applied to covectors in $N_{k+1}^\perp$. (3.3): a symmetric form is non-degenerate on $\mathcal S/N$ iff its radical is $N$ (given $N\subseteq\operatorname{rad}$). (3.6): continuity of a determinant on a fixed finite-dimensional space; (D) is what makes the space fixed. No bound on $r_{L,K}$ uniform in $L$ or $K$ follows: it would need a bound on $\lVert\tilde M_k^{-1}\rVert$ on $Q_k$ uniform in $L$, which PH1 explicitly declines ("no bounded inverse"), and a norm fixed across levels, which PH1 does not fix. The statement is that the argument gives no uniform bound, not that the radius is non-uniform. (3.8): if $n\in N_{k,\infty}$, then $\tilde M_{k+1}J_{k+1}(\Psi)n=L_{k+1}(\Psi)n=0$, so $J_{k+1}(\Psi)n\in\operatorname{rad}\tilde M_{k+1}=N_{k+1,\infty}$.

\subsection*{Result}
Under (D), at fixed $(L,K)$: PH2 at $g=0$ $\iff$ $\operatorname{rad}\tilde M_k=N_k$ for $k=2,\dots,K$, which forces $N_k=N_{k,\infty}=\ker\tilde M_k$; the $k=2$ instance is PH1's invertibility clause on $\operatorname{Sym}^2\mathcal H_0/\ker V_4$, whose consistency is (3.5); PH2 at $g=0$ implies PH2 on $\lvert g\Psi\rvert<r_{L,K}$, and R26 uses only the $g=0$ form.

\subsection*{Verification}
`C1.3-*` (descent leg: kernel stable, complement independence; break leg: complement dependence without D1; fix pass 1: `C1.3-descent-D2`, $K=4$ with the kernel at level 3, $\hat H_3(g)n=0$ including the level-4 Schur term and complement independence of $\hat H_2$ iff $L_4(\Psi)n=0$, break leg with a block-symmetric $T_8$), `C1.4-*` (quotient determinant, $H_2(0)=V_4$; fix pass 1: the (3.5) leg with $\ker V_4\ne0$, both clauses, break legs for each, the $O(g^2)$ order of the $T_6$ lift, and the $K=2$ limit), `C1.5-radius-*` (smallest zero of $\det\hat H_k(g)$ at fixed $\Psi$ is at $\lvert g\rvert>0$), `C1.9-factor-*` ((3.7) from the tensor contraction, break leg with a non-block-symmetric parent).

## 4. What "stable kernel" must mean, and the term the reduction misses

\subsection*{Setup}
A1–A3, §3. Two different stability notions are in play.

- **(S$_g$) stability in $g$:** $N_k\subseteq\operatorname{rad}\hat H_k(g,\Psi)$ for all $\Psi$ and all $g$ near $0$, so that the quotient on which the determinant is taken does not move with $(g,\Psi)$.
- **(S$_L$) stability in the truncation level** (PH1 as restated 2026-09-22): $\ker V_4^{(L)}=\ker V_4\cap\{\text{level}\le L\}$ for $L$ large (same for $\tilde M_k$).

\subsection*{Derivation}

**(a) The continuity argument needs (S$_g$).** §3(d) takes the determinant on a fixed $Q_k$; this is meaningful only if every $H_k(\varphi)$ descends to it, which is (S$_g$). (D) implies (S$_g$) by (3.2). Conversely, expanding (2.2) in $\varphi$ (levels above regular):

$$
[\varphi^1]:\ T_{2k+1}(N_k,\cdot,\varphi)=0\ \ \text{is necessary};\qquad
[\varphi^2]:\ N_k\subseteq\operatorname{rad}\big(L_{k+1}(\varphi)^{\top}\tilde M_{k+1}^{-1}L_{k+1}(\varphi)\big),
\tag{4.1}
$$

the second implied by $L_{k+1}(\varphi)N_k=0$ and equivalent to it when $\tilde M_{k+1}$ is definite on $Q_{k+1}$ (then $n$ in the radical gives $\tilde M_{k+1}^{-1}(L_{k+1}n,L_{k+1}n)=0$, hence $L_{k+1}n=0$). Without (S$_g$) the quotient determinant is not defined for $g\neq0$ and the "quotient" Schur value depends on the complement chosen (check `C1.3-complement-indep-break`); on the full $\mathcal S_k$ a kernel direction of $\tilde M_k$ is lifted at $O(g)$ (check `C1.6-kernel-moves`) and $\hat H_k^{-1}$ has a pole at $g=0$.

**(b) The source clause, and the relation to PH1.** (S$_g$) is a statement on $\hat H_k$ alone and has no counterpart of D3, $L_k(\Psi)^\top N_k=0$. D3 is nevertheless necessary for the quotient prescription: if $L_k^\top n\ne0$ for some $n\in N_k$, the level-$(k-1)$ Schur term $L_k^\top\hat H_k^{-1}L_k$ needs $\hat H_k^{-1}$ on covectors $L_k\Sigma_{k-1}\notin N_k^\perp$, where the inverse of the induced form is not defined; equivalently, the Gaussian in $\Sigma_k$ has a linear term along a flat direction and no saddle. D3 is automatic at $k=2$ ($\tilde u_2(n)=V_4(n,P_2)=0$) and for block-symmetric parents ((3.7): $L_k^\top n=J_k^\top\tilde M_kn=0$). The stability the reduction needs is therefore **descent (D): (S$_g$) together with D3**; (S$_g$) is equivalent to the kinetic, odd and upward clauses of (D) up to the definiteness proviso of (4.1).

(S$_L$) concerns the limit $L\to\infty$ of the quotients and plays no role at fixed $L$. PH1 constrains $V_4$, and through its stability clause the kernels of $\tilde M_k$ as $L$ grows; it does not constrain $V_5$, the source restrictions of $T_6$, or $T_{2k+1},T_{2k+2}$, which (D) involves at every level, so it does not imply (D) (independence of the data in the class). (D) does not imply (S$_L$) either. The "stable kernel" of PH2 must therefore be read as **(D) at each truncation $L$, plus (S$_L$)** for the level-by-level quotients to have a limit. (D) is an extra condition, not implied by PH1; it is vacuous where the kernels vanish.

**(c) The term the reduction misses.** Let level $k+1$ fail at $g=0$: $n\in\operatorname{rad}\tilde M_{k+1}$, $n\notin N_{k+1}$ (take the excess one-dimensional, levels above $k+1$ regular). Along the ray $\varphi=g\Psi$,

$$
\hat H_{k+1}(g)=\tilde M_{k+1}+gA+g^2B+O(g^3),\qquad A=-\tfrac{T_{2k+3}(\cdot,\cdot,\Psi)}{2k+3},\quad B=-c_{k+1}L_{k+2}^{\top}\tilde M_{k+2}^{-1}L_{k+2}.
\tag{4.2}
$$

Split $\mathcal S_{k+1}=\mathbb Rn\oplus C$. The Schur complement on $\mathbb Rn$ is $s(g)=g\alpha_1+g^2\alpha_2+O(g^3)$ with

$$
\alpha_1=A(n,n),\qquad
\alpha_2=B(n,n)-w^{\top}\tilde M_{k+1}^{+}w\quad(\text{if }\alpha_1=0),\qquad w:=A(n,\cdot),
\tag{4.3}
$$

($\alpha_1=0$ puts $w$ in the range of $\tilde M_{k+1}$, so $w^\top\tilde M^+w$ does not depend on $C$), and

$$
\hat H_{k+1}^{-1}=(\text{regular at }g=0)+\frac{v\,v^{\top}}{s(g)},\qquad v=n+O(g).
\tag{4.4}
$$

With $\ell:=L_{k+1}(\Psi)^{\top}n\in\mathcal S_k^{*}$ (the coupling of the kernel direction to $\Sigma_k$), the Schur term of $\hat H_k$ contributes $-g^2c_k(L^{\top}v)(v^{\top}L)/s(g)$:

$$
\begin{aligned}
\alpha_1\neq0:&\quad [g^0]\hat H_k=\tilde M_k,\qquad [g^1]\hat H_k=-\tfrac{T_{2k+1}(\cdot,\cdot,\Psi)}{2k+1}-c_k\,\frac{\ell\,\ell^{\top}}{\alpha_1},\\
\alpha_1=0,\ \alpha_2\neq0:&\quad [g^0]\hat H_k=\tilde M_k-c_k\,\frac{\ell\,\ell^{\top}}{\alpha_2}.
\end{aligned}
\tag{4.5}
$$

The second line is **the missed $O(g^0)$ term**. It is homogeneous of degree $0$ in $\Psi$ ($\ell$ linear, $\alpha_2$ quadratic), so $H_k(\varphi)$ has a direction-dependent limit at $\varphi=0$: it is not continuous there, and the continuity argument of §3(d) has nothing to start from. A pole of order $\ge3$ makes $\hat H_k$ itself singular at $g=0$.

**(d) Protection for block-symmetric parents, pole order $\le2$.** By (3.7), $\ell=J_{k+1}^{\top}\tilde M_{k+1}n=0$. For $\alpha_1=0$ (pole order $p\ge2$) write $v=n+gv_1+O(g^2)$, $v_1=-\tilde M_{CC}^{-1}w_C$; since $w(n)=\alpha_1=0$, $\tilde M_{k+1}v_1=-w$ and
$$
L_{k+1}(\Psi)^{\top}v=g\,u+O(g^2),\qquad u:=-J_{k+1}(\Psi)^{\top}w=\tfrac1{2k+3}J_{k+1}(\Psi)^{\top}T_{2k+3}(n,\cdot,\Psi),
$$
independent of the complement $C$. The singular part of the Schur term is $-g^2c_k\,g^2uu^{\top}/(g^p\alpha_p)\,(1+O(g))$, $\alpha_p$ the leading coefficient of $s(g)$:
$$
\begin{aligned}
p=2:&\quad [g^0],[g^1]\hat H_k\ \text{unchanged},\quad [g^2]\hat H_k\ni-c_k\,\frac{uu^{\top}}{\alpha_2};\\
p=3:&\quad [g^1]\hat H_k\ni-c_k\,\frac{uu^{\top}}{\alpha_3};\qquad
p=4:\quad [g^0]\hat H_k\ni-c_k\,\frac{uu^{\top}}{\alpha_4};\qquad p\ge5:\ \hat H_k\ \text{singular at }g=0.
\end{aligned}
\tag{4.5′}
$$
(For $p=1$ the singular part is $O(g^3)$.) Orders $p\ge3$ occur along the rays where $\alpha_1(\Psi)=\alpha_2(\Psi)=0$ ($\alpha_1$ linear, $\alpha_2$ quadratic in $\Psi$; the joint null set is non-empty for $\dim\mathcal H_0\ge3$ when $\alpha_2$ is indefinite on $\{\alpha_1=0\}$). So block-symmetric parents protect $[g^0],[g^1]$ only for pole order $\le2$; the $p=3,4$ lines are one-line consequences of (4.4) and are not machine-checked. The $\ell\ne0$ missed terms (4.5) need a presentation whose parent is not symmetric in the source block — admissible in the shared-parent class (the collapse only needs the parent on $P_{k-1}\otimes\Psi$, which is symmetric).

**(e) Where the reduction is complete.** The missed terms exist only when a higher level already fails at $g=0$. Under the reduced hypotheses — (3.4) at every level — every $\hat H_j(0)$ is regular and $[g^0]\hat H_k=\tilde M_k$ at every level with nothing missed. What (c)–(d) show is that the levels are not independent tests: a failure at level $k+1$ can be invisible in $\hat H_k(0)$ ((d) for $p\le3$, and the $\alpha_1\ne0$ line of (4.5)) or can shift it (the $\alpha_2$ line of (4.5), $p=4$ in (4.5′)). So checking PH1 ($\hat H_2(0)=V_4$ non-degenerate) never certifies level 3. It is visible in the value, (f).

**(f) First entry of a level-3 kernel into the value.** Take $k=2$, $K=3$, a block-symmetric parent ($\ell=0$), $n$ spanning $\ker\tilde M_3$, $n\notin N_3$; $V_4$ non-degenerate. The value is $S=\tfrac12V_2+\tfrac g{3!}V_3+\tfrac{g^2}{4!}\tilde u_2^\top\hat H_2^{-1}\tilde u_2$ (019 §2), $\tilde u_2=V_4P_2$. Write $\hat H_2=V_4+gA_2+g^2B_2+g^3B_3+O(g^4)$, $A_2=-\tfrac15V_5(\cdot,\cdot,\Psi)$. Then
$$
\tilde u_2^{\top}\hat H_2^{-1}\tilde u_2=V_4(P_2,P_2)-g\,A_2(P_2,P_2)+g^2\big[(A_2P_2)^{\top}V_4^{-1}(A_2P_2)-B_2(P_2,P_2)\big]+O(g^3).
\tag{4.6}
$$
Laurent-expand $\hat H_3^{-1}=(\tilde M_3+gA)^{-1}$ at $g=0$, $A=-\tfrac17T_7(\cdot,\cdot,\Psi)$, $w=An$. The coefficients are complement-independent, and the identities $\hat H_3\hat H_3^{-1}=\hat H_3^{-1}\hat H_3=1$ order by order, sandwiched by $L_3=\tilde M_3J_3$ ((3.7)), give:
$$
\begin{aligned}
p=1\ (\alpha_1=w(n)\ne0):&\quad \hat H_3^{-1}=\frac{nn^{\top}}{g\alpha_1}+R_0+gR_1+\dots,\quad \tilde M_3R_0\tilde M_3=\tilde M_3,\quad \tilde M_3R_1\tilde M_3=-A+\frac{ww^{\top}}{\alpha_1},\\
&\quad B_2=-c_2J_3^{\top}\tilde M_3J_3,\qquad B_3=c_2J_3^{\top}AJ_3-c_2\,\frac{J_3^{\top}ww^{\top}J_3}{\alpha_1};\\
p=2\ (\alpha_1\equiv0):&\quad \hat H_3^{-1}=\frac{nn^{\top}}{g^2\alpha_2}+\frac{R_{-1}}g+R_0+\dots,\quad \tilde M_3R_{-1}=-\frac{wn^{\top}}{\alpha_2},\quad \tilde M_3R_0=1-AR_{-1},\\
&\quad B_2=-c_2J_3^{\top}\tilde M_3J_3-c_2\,\frac{uu^{\top}}{\alpha_2},\qquad u=-J_3^{\top}w,\ \ \alpha_2=-w^{\top}\tilde M_3^{+}w.
\end{aligned}
\tag{4.7}
$$
The first term of $B_2$ is the generalised-inverse (regular) reading: with $J_3P_2=P_3$ it contributes $+c_2\tilde M_3(P_3,P_3)=c_2T_6(\Psi^6)$ to (4.6), i.e. the collapse value $\tfrac{g^4}{4!}c_2T_6(\Psi^6)=a_3T_6(\Psi^6)$, for any generalised inverse. The remainder, with $u(P_2)=-w(P_3)=\tfrac17T_7(n,P_3,\Psi)$, $\alpha_1=-\tfrac17T_7(n,n,\Psi)$, $\alpha_2=-\tfrac1{49}T_7(n,\cdot,\Psi)^{\top}\tilde M_3^{+}T_7(n,\cdot,\Psi)$, is
$$
\begin{aligned}
p=2:&\quad \Delta S\rvert_{g^4}=\frac{g^4}{4!}\,c_2\,\frac{u(P_2)^2}{\alpha_2}=-\frac{g^4}{6!}\,\frac{T_7(n,P_3,\Psi)^2}{T_7(n,\cdot,\Psi)^{\top}\tilde M_3^{+}T_7(n,\cdot,\Psi)},\\
p=1:&\quad \Delta S\rvert_{g^4}=0,\qquad \Delta S\rvert_{g^5}=\frac{g^5}{4!}\,c_2\,\frac{w(P_3)^2}{\alpha_1}=-\frac{g^5}{7!}\,\frac{T_7(n,P_3,\Psi)^2}{T_7(n,n,\Psi)}.
\end{aligned}
\tag{4.8}
$$
Both are homogeneous in $\Psi$ of the degree of their order ($6$ and $7$) and rational, not polynomial: the denominators are a quadratic and a linear form in $\Psi$ that do not divide the numerators generically (check `C1.10-order2-rational`). For $K\ge4$ replace $\alpha_2$ by (4.3), which adds $B(n,n)=-c_3(L_4n)^{\top}\tilde M_4^{-1}(L_4n)$. For a level-$k$ kernel ($k\ge3$, levels below regular, i.e. $\tilde M_j$ invertible for $2\le j<k$ (with lower-level quotients the singular shift $\propto J^\top ww^\top J$ need not descend), block-symmetric parents, top level or $L_{k+1}n=0$), the value's first-order response to a shift $\delta\hat H_{k-1}$ is $-a_{k-1}\,\delta\hat H_{k-1}(P_{k-1},P_{k-1})$ by the collapse identity (019 §3, $L_jP_{j-1}=\tilde M_jP_j$), and $a_{k-1}g^2c_{k-1}=a_k$, so
$$
\Delta S\rvert_{g^{2k-2}}=-\frac{g^{2k-2}}{(2k)!}\,\frac{T_{2k+1}(n,P_k,\Psi)^2}{T_{2k+1}(n,\cdot,\Psi)^{\top}\tilde M_k^{+}T_{2k+1}(n,\cdot,\Psi)}\ \ (p=2),\qquad
\Delta S\rvert_{g^{2k-1}}=-\frac{g^{2k-1}}{(2k+1)!}\,\frac{T_{2k+1}(n,P_k,\Psi)^2}{T_{2k+1}(n,n,\Psi)}\ \ (p=1),
\tag{4.9}
$$
derived for $k=3$ and checked there; the general-$k$ form is argued by this collapse step and not checked.

\subsection*{Commentary}
(4.3)–(4.4): block inversion with the Schur complement on the one-dimensional excess; $v=(1,-\hat H_{CC}^{-1}\hat H_{Cn})$ in the split. (4.5): $L^{\top}v=\ell+O(g)$ and $1/s=1/(g^p\alpha_p)\,(1+O(g))$; the regular part of (4.4) contributes at $O(g^2)$. The $O(g)$ corrections to $v$ and to $s$ only affect orders beyond those displayed.

\subsection*{Result}
The stability the reduction needs is descent (D): stability in $g$, (S$_g$), together with the source clause D3, $L_k(\Psi)^\top N_k=0$; D3 is automatic at $k=2$ and for block-symmetric parents, and (S$_g$) is equivalent to the other clauses of (D) up to the definiteness proviso of (4.1). (D) is an extra condition beyond PH1. The $O(g^0)$ term of every nested condition is $\tilde M_k$ whenever the levels above satisfy (3.4); otherwise the reduction misses $-c_k\lim_{g\to0}g^2L_{k+1}^{\top}\hat H_{k+1}^{-1}L_{k+1}$, which is $-c_k\ell\ell^{\top}/\alpha_2$ for pole order 2 with $\ell\ne0$, and $-c_kuu^\top/\alpha_4$ for pole order 4 with $\ell=0$ (block-symmetric parents); block-symmetric parents protect $[g^0],[g^1]$ for pole order $\le2$ only. A failed level generically (whenever $T_7(n,P_3,\cdot)\not\equiv0$) enters the value as a term rational in $\Psi$: for a block-symmetric parent ($\ell=0$) at $n=6$ for pole order 2 and at $n=7$ for a simple pole (4.8); for other parents already at $n=4$ (order 2) or $n=5$ (simple pole), by (4.5), not machine-checked in the value.

\subsection*{Verification}
`C1.6-kernel-moves`, `C1.7-protected`, `C1.7-missed-g1`, `C1.7-missed-g0`, `C1.7-direction`, `C1.8-break-*`; fix pass 1: `C1.10-*` for (4.7)–(4.8) at $k=3$ — exact $[g^2]\hat H_2$ (pole order 2) and $[g^2],[g^3]\hat H_2$ (pole order 1) against (4.7), the regular part against the collapse value, $[g^4]S$ and $[g^5]S$ minus the regular value against (4.8), rationality and degree-6 homogeneity of the $n=6$ term; break legs: singular part dropped (both orders), sign flipped, the rationality detector on the polynomial $T_6(\Psi^6)$ (§6). Not checked: (4.5′) ($p=3,4$) and (4.9) for $k\ge4$.

*(The earlier remark here — "a kernel of $\tilde M_k$ is invisible at the first-entry order $g^{2k-2}$", "for $k=3$ a kernel of $\tilde M_3$ matters first at $n=7$" — is withdrawn: it covered the regular part of $\hat H_k^{-1}$ only, and holds as stated for a simple pole only. Replaced by (f) and node C1.10.)*

## 5. Result and proposed PH2 wording

**Result (C1).** At fixed finite-dimensional truncation $L$ (A1: for the string vertices, a level truncation with the momenta fixed or discretised) and tower truncation $K$, in R26's shared-parent class:

1. $\hat H_k(g,\Psi)=H_k(g\Psi)$ (C1.1), and if the levels above are non-degenerate at $g=0$, $\hat H_k=\tilde M_k-\tfrac{g}{2k+1}T_{2k+1}(\cdot,\cdot,\Psi)-g^2c_kL_{k+1}^\top\tilde M_{k+1}^{-1}L_{k+1}+O(g^3)$ (C1.2). The $O(g^0)$ term of every nested condition is the level-$k$ kinetic $\tilde M_k=T_{2k}\rvert_{(k|k)}$ (§1 table).
2. With quotients by subspaces that every Jacobi block containing $\Sigma_k$ annihilates (descent (D); canonical: the joint kernels $N_{k,\infty}$), PH2 at $g=0$ is equivalent to $\operatorname{rad}\tilde M_k=N_k$ for $k=2,\dots,K$, which forces $N_k=N_{k,\infty}=\ker\tilde M_k$ (C1.4). At $k=2$ the radical clause is PH1's invertibility clause on $\operatorname{Sym}^2\mathcal H_0/\ker V_4$, automatic at a fixed finite-dimensional truncation; the content is the consistency of that quotient, (3.5): $V_5(\ker V_4,\cdot,\cdot)=0$ (R38; PH5's second clause) and, for $K\ge3$, $T_6(\,\cdot_3\,;\ker V_4,\Psi)=0$ (necessary when $\tilde M_3$ is definite on $Q_3$, generically otherwise; a condition on the $(3|2,1)$ block of the presentation, satisfiable only if the forced diagonal vanishes on $\operatorname{Sym}^6\mathcal H_0\cap(\mathcal S_3\otimes\ker V_4\otimes\mathcal H_0)$, e.g. $V_6(\chi^6)=0$ for $\chi\otimes\chi\in\ker V_4$, implied by 034's (C$^{(6)}$) with R38; in no hypothesis row). At $K=2$, (3.5) is R38 (1.2) exactly. Both clauses are vacuous if $\ker V_4=0$.
3. PH2 at $g=0$ implies PH2 on $\lvert g\Psi\rvert<r_{L,K}$ for any norm on $\mathcal H_0$ (C1.5). The argument gives no bound uniform in $L$ or $K$; uniformity is not even defined without a norm fixed across levels, which PH1 does not fix. R26 is a formal-series statement and uses only the $g=0$ form, so the neighbourhood clause of PH2 costs nothing at the algebraic layer.
4. The stability required is descent (D): stability in $g$, (S$_g$), together with the source clause $L_k(\Psi)^\top N_k=0$ (D3), which is necessary and automatic at $k=2$ and for block-symmetric parents; (S$_g$) is equivalent to the other clauses of (D) up to the definiteness proviso of (4.1) (C1.6). (D) is not implied by PH1, whose stability clause is stability in $L$, a separate requirement for the $L\to\infty$ limit.
5. Nothing is missed under the reduced conditions. If a higher level fails, the Schur term can shift $[g^1]$ or $[g^0]$ of the level below ((4.5); (4.5′) for pole orders 3, 4), and a level-3 failure can be invisible in $\hat H_2(0)$ (C1.7); in particular PH2 strictly extends PH1 across the class (C1.8). For block-symmetric parents (fully polarized included) the source factorises through the kinetic (C1.9): $\ell=0$, the missed terms at $[g^0],[g^1]$ vanish for pole order $\le2$ along the ray, and kernels propagate upward, $\operatorname{Sym}(N_{k,\infty}\otimes\mathcal H_0)\subseteq N_{k+1,\infty}$.
6. A failed level is generically visible in the value (whenever $T_7(n,P_3,\cdot)\not\equiv0$). For a block-symmetric parent ($\ell=0$), a kernel $n$ of $\tilde M_3$ outside $N_3$ enters $S$ as a term rational in $\Psi$: at $n=6$, $-\frac{g^4}{6!}T_7(n,P_3,\Psi)^2/(T_7(n,\cdot,\Psi)^\top\tilde M_3^+T_7(n,\cdot,\Psi))$, if $T_7(n,n,\cdot)\equiv0$ (pole order 2); first at $n=7$, $-\frac{g^5}{7!}T_7(n,P_3,\Psi)^2/T_7(n,n,\Psi)$, for a simple pole (C1.10, (4.8); general $k$ (4.9), argued, with $\tilde M_j$ invertible for $2\le j<k$). For other parents the failure enters earlier, at $n=4$ (order 2) or $n=5$ (simple pole), by (4.5) (not machine-checked in the value).

**Interpretation.** The target action has a polynomial vertex $V_n(\Psi^n)$ at each order, and R26's tower reproduces it order by order because every Gaussian elimination collapses onto a Veronese contact term. A level that fails at $g=0$ breaks this: a direction $n$ with no kinetic term at $g=0$ gets its quadratic term only from the background, $g\,T_7(n,n,\Psi)$ or, if that vanishes, $g^2\alpha_2(\Psi)$, i.e. a field-dependent mass. Integrating it out divides by that mass, and the effective vertex acquires the denominators of (4.8) (6- or 7-point for a block-symmetric parent; 4- or 5-point otherwise, by (4.5)): it is rational in $\Psi$, and the limits of $\hat H_k$ at $\varphi=0$ can be direction-dependent (4.5). PH2 (b) is therefore the statement that the HS tower reproduces a *polynomial-vertex* action order by order; its failure is observable as a non-polynomial term in an effective vertex, not only as a singular operator.

**Proposed ledger wording (for the orchestrator).**

- **PH2 (a) → new R row. Tag: Proven (finite-dimensional algebraic layer).** Machine-checked in the finite model, `codes/verify-ph2a.py`, 57/57 PASS on seeds 20260926 and 41 (`agent/scratch/ph2a-run2.log`): C1.1, C1.2, C1.3 (descent at the top level, and one level below with the upward clause D2), C1.4 ((3.5): both clauses with break legs, the $O(g^2)$ order of the $T_6$ lift, the $K=2$ limit), C1.7 (one-dimensional excess, pole order $\le2$), C1.9, C1.10 ($k=3$). Not machine-checked: pole orders 3, 4 (4.5′); (4.9) for $k\ge4$; multi-dimensional excess kernels; about 20 of the 57 checks hold by construction or are implied by their break legs (§6); the rationality of the $n=6$ term is checked at one $\Psi$ per seed (proved in §4(f)). Text:

  "In a finite-dimensional model of R26's algebraic layer (shared-parent class, tower truncated at $K$, quotient prescription), the nested kernels depend on $g\Psi$ only. Take the level-$k$ quotient by a subspace annihilated by every Jacobi block in which $\Sigma_k$ appears (descent; the joint kernel $N_{k,\infty}$, 034 (C$_\infty$) after transposing $L_k$). Then the nested conditions hold at $g=0$ iff $\ker\tilde M_k=N_{k,\infty}$ for $k=2,\dots,K$, which forces the canonical quotient. At $k=2$ the radical clause is automatic, and the content is $\ker V_4\subseteq N_{2,\infty}$: $V_5(\ker V_4,\operatorname{Sym}^2\mathcal H_0,\Psi)=0$ (R38) and, for $K\ge3$, $T_6(\cdot_3;\ker V_4,\Psi)=0$, a condition on the $(3|2,1)$ block of the chosen presentation, satisfiable only if the forced diagonal vanishes on $\operatorname{Sym}^6\mathcal H_0\cap(\mathcal S_3\otimes\ker V_4\otimes\mathcal H_0)$ (non-zero e.g. when $\ker V_4\ni\chi\otimes\chi$, where it requires $V_6(\chi^6)=0$; implied by 034's (C$^{(6)}$) with R38); at $K=2$ this is R38 exactly. The conditions then hold for $\lvert g\Psi\rvert<r_{L,K}$ (any norm; the argument gives no bound uniform in $L$ or $K$), and R26's formal-series statement uses only the $g=0$ form; $[g^0]\hat H_k=\tilde M_k$ at every level. The required stability is descent: stability in $g$ together with $L_k^\top N_k=0$ (necessary; automatic at $k=2$ and for block-symmetric parents); the upward clause is necessary when the kinetic of the level above is definite on its quotient, generically otherwise. PH1 does not imply it. PH1 does not imply PH2 across the class: a singular $\tilde M_3$ with $V_4$ non-degenerate is admissible, and with a simple pole it is invisible in $\hat H_2(0)$ along each ray (a statement on logical strength within the class, not a claim that PH2 fails for the string vertices). Such a failure is generically visible in the value as a term rational in $\Psi$: for a block-symmetric parent at $n=6$ (pole order 2) or $n=7$ (simple pole), otherwise already at $n=4$ or $n=5$. For the string vertices, where a fixed level still carries continuous momenta, the determinant and neighbourhood statements are not covered; PH1 is read as the ledger reads it." Source: `agent/derivations/061-ph2a-nested-kernels.md#C1`.

- **PH2 (b) (replaces PH2; open).**
  - **Statement.** "In the presentation used (R21: the block composite $\tilde M=M-\tfrac65\Phi^\top V_4^{-1}\Phi$; R25: scheme B's canonical kernels; R26, R35: at least one presentation of R26's shared-parent class), for every $k\ge3$, every null vector of $\tilde M_k=T_{2k}\rvert_{(k|k)}$ is annihilated by every Jacobi block in which $\Sigma_k$ appears ($\ker\tilde M_k=N_{k,\infty}$). If $\ker V_4\ne0$ and $K\ge3$, the same presentation must also satisfy $T_6(\cdot_3;\ker V_4,\Psi)=0$. This is a condition on the $(3|2,1)$ block of the parent, satisfiable only if the forced diagonal vanishes on $\operatorname{Sym}^6\mathcal H_0\cap(\mathcal S_3\otimes\ker V_4\otimes\mathcal H_0)$, a condition on $V_6$ there given R38 (e.g. $V_6(\chi^6)=0$ for $\chi\otimes\chi\in\ker V_4$), which 034's (C$^{(6)}$) implies. For block-symmetric parents $\operatorname{Sym}(N_{k-1,\infty}\otimes\mathcal H_0)\subseteq\ker\tilde M_k$ is automatic, and the hypothesis requires it to lie in $N_{k,\infty}$. First instance: $\tilde M_3$ at level 0 (momenta fixed or discretised). For a block-symmetric parent, a kernel with a simple pole enters the value first at $n=7$, and at $n=6$ if $T_7(n,n,\cdot)\equiv0$; for other parents already at $n=5$ or $n=4$; in each case generically as a term rational in $\Psi$ (061 C1.7, C1.10)."
  - **Motivation.** "Off the Veronese diagonal, $\tilde M_k$ ($k\ge3$) and the source blocks are presentation freedom (R26 (4); 019 §4 point 3). An accidental kernel of $\tilde M_k$ is a codimension-one condition on that freedom and is expected to be removable by a Veronese-null change of parent (061 §7.4: expected, not shown) – the mechanism of PH5's stub deformation, acting on a presentation choice rather than on the vertices; the $T_6$ clause is presentation freedom only off $\operatorname{Sym}^6\mathcal H_0\cap(\mathcal S_3\otimes\ker V_4\otimes\mathcal H_0)$ (vacuous at level 0, R53). At level 0, $\ker V_4=0$ (R53), so (3.8) forces nothing upward from $k=2$. Failing (b), 034's remedy (a) – multiplier pairs on $\ker\tilde M_k/N_{k,\infty}$ (hybrid Route C: cotangent pairs, exact Gaussians with no inverse) – is the known fallback, expected to preserve R26's Schur structure (034 §5.2, not verified)."
  - **Would be falsified by.** "A level-0 null vector of $\tilde M_3$ on which $T_7(\cdot,\cdot,\Psi)$, $L_4(\Psi)$ or $L_3(\Psi)^\top$ does not vanish, in every admissible presentation; or $\ker V_4\ne0$ with the forced diagonal non-zero on $\operatorname{Sym}^6\mathcal H_0\cap(\mathcal S_3\otimes\ker V_4\otimes\mathcal H_0)$. Signature: a non-polynomial term in an effective vertex, at $n=6,7$ for block-symmetric parents and $n=4,5$ otherwise (061 C1.7, C1.10)."
  - **Used by.** R21, R25, R26, R35 (R21 and R25 in their named presentations, see the qualifier in the Statement).
- **PH5**: unchanged. Its second clause ("$V_5$ annihilates the kernel") is the $V_5$ half of (3.5); the $T_6$ half sits in PH2 (b); its vertex-side part (the forced diagonal on $\operatorname{Sym}^6\mathcal H_0\cap(\mathcal S_3\otimes\ker V_4\otimes\mathcal H_0)$) is implied by (C$^{(6)}$), which PH5 does not carry (see the R19/R21 annotation).
- **Re-pointing the rows that cite PH2** (Used by: R21, R25, R26, R35, R46). Rows that only need levels $\le2$ get the new row plus PH1, PH5; rows that need $k\ge3$ also get PH2 (b).
  - **R26**: Conditional(PH1, PH2 (b), PH5, PH14 [through $A_6$]) plus the new row. PH5 carries only the $V_5$ half of (3.5); the $T_6$ half sits in PH2 (b).
  - **R21** (1a), (1b) (dressed $\Sigma_3$ with the level-3 kernel inverted, $O(g_s^4)$): PH2 → PH2 (b) [in the row's presentation: the block composite $\tilde M=M-\tfrac65\Phi^\top V_4^{-1}\Phi$] + the new row.
  - **R25** ($\Sigma_2,\Sigma_3$, $O(g_s^5)$): PH2 → PH2 (b) [in the row's presentation: scheme B's canonical kernels] + the new row.
  - **R35** (parents $T_{n\ge6}$ and fixed point incl. the $\ker V_{2k}$ quotient, all levels): Conditional(PH6, PH1, PH2 (b), PH5) + the new row (old PH2 carried the $k=2$ consistency, PH1's quotient and the $V_5$ half of (3.5), which is PH5's second clause).
  - **R46** (non-perturbative line, quintic truncation $K=2$): status line "non-perturbative within the quintic truncation, on the set of $(g_s,\Psi)$ where $K_\Psi$ is invertible on $W_q$ (the domain of the statement, not a hypothesis; it contains $\lvert g_s\Psi\rvert<r_{L,2}$, new row): Conditional(PH6 [n=4,5], PH1, PH5) – Proven"; no PH2 (b), no unregistered condition (the only other content of old PH2 at $K=2$ is $K_\Psi$'s descent to $W_q$, R38/PH5, C1.4's $K=2$ limit).
  - Outside 061 (critic note): per 034 §5.1, R19 and R21 assume 034's (C$^{(6)}$), and their rows do not record it.

### Scope of the exclusion

C1.8 (PH2 does not follow from PH1) is a statement within the class of finite-dimensional shared-parent towers, the class R26 is proved in (physical reason: it is the algebraic layer of the tower at a finite-dimensional truncation). It is a statement on logical strength within the class, not a claim that PH2 fails for the string vertices. Relevant cases outside it: the untruncated limit $L\to\infty$ and a fixed level with continuous momenta (where PH1's stability clause and the determinant statements enter), and presentations outside the shared-parent class, all outside R26 too. Weakest relaxations evading it: leaving the pure-quotient prescription A3 for 034's multiplier remedy (a) on the excess kernel $\ker\tilde M_k/N_{k,\infty}$, or choosing a presentation (019 §4 point 3) in which $\tilde M_3$ is non-degenerate.

## 6. Verification

`codes/verify-ph2a.py`, exact rational arithmetic (sympy), $\dim\mathcal H_0=2$, $d_2,d_3,d_4=3,4,5$, tower $K=4$ for the regular legs and the D2 leg, $K=3$ for the other kernel legs, $K=2$ for the R38 limit. Run: `OMP_NUM_THREADS=1 .venv/bin/python -u codes/verify-ph2a.py [seed]`; logs `agent/scratch/ph2a-run1.log` (original, 37 checks) and `agent/scratch/ph2a-run2.log` (fix pass 1). **57/57 PASS, 0 FAIL, exit 0, on seeds 20260926 and 41** (fix pass 1; 20 new checks, all passed on their first run). Seventeen break-on-purpose legs, each confirmed to FAIL: the original eight — wrong Schur power $g^1$ (C1.1), flipped odd-coupling sign in the Jacobi formula at $k=2,3,4$ (C1.2), $c_2\to2c_2$ in the recursion (C1.2), doubled $[g^4]$ in the remainder scaling (C1.2), complement dependence without D1 (C1.3), non-block-symmetric parent for the factorisation (C1.9) — and nine added in fix pass 1: singular part dropped at $[g^2]$ (pole order 2) and at $[g^3]$ (pole order 1), the $n=6$ term omitted (the withdrawn §4 remark) and sign-flipped, the $n=7$ term omitted, the rationality detector run on the polynomial $T_6(\Psi^6)$ (C1.10); $V_5(\ker V_4,\cdot,\cdot)\ne0$ and block $T_6$ with $L_3\ker V_4\ne0$ (C1.4); block $T_8$ with $L_4n\ne0$ (C1.3). Plus the brief's break leg (C1.8) and the $V_5\ne0$ conjunct inside `C1.4-K2-limit`.

**Checks that hold by construction** (they confirm the model is set up as stated; they test no claim): `C1.3-stable-kernel` ($\hat H_3n=\tilde M_3n+gAn$ with both imposed zero), `C1.3-descent-D3` (automatic for block parents, (3.7), whose content `C1.9-*` tests), `C1.6-kernel-moves` ($An\ne0$ for a random $A$), `C1.4-quotient-det` ($\hat H_3(0)=\tilde M_3$), `C1.4-H2-at-0`, `C1.2-coeff0-k2..k4` (block-triangular at $g=0$), `C1.5-radius-k2..k4` ($r>0$ follows from the asserted $\det\tilde M_k\ne0$; ignores poles from the levels above), `C1.2-limit` and its break leg (test `taylor` against the function it expanded), `C1.8-break-PH1-holds`, `C1.8-break-level3-fails` (an existence example: valid as such, not a test). Fifteen of 57 wholly; in addition `C1.10-order2-collapse` (`vIreg` is built from the asserted $JP_2=P_3$, $\tilde u_2=V_4P_2$: the collapse algebra itself), the homogeneity conjunct of `C1.10-order2-rational` (degree $8-2$ of the formula), and the positive conjuncts of `C1.4-kerV4-descent`, `C1.4-K2-limit` and `C1.3-descent-D2` (immediate once $L_3m=0$, resp. $L_4n=0$, and D1 are imposed; their content is carried by the break legs) — about 20 of 57. The closed form of the $n=6$ term is matched to the computed $[g^4]S$ at one $\Psi$ per seed only; its rationality in $\Psi$ is proved (§4(f)) and checked at that point. **"Verified" is scoped to the nodes with genuine checks:** C1.1, C1.2 (series, $[g^1]$, rescaling), C1.3 (complement independence at the top level and with D2 one level below), C1.4 ((3.5) both clauses, the $O(g^2)$ order of the $T_6$ lift, the $K=2$ limit), C1.7 (pole order $\le2$), C1.9, C1.10 ($k=3$).

- **C1.10 (fix pass 1, #7).** On the `C1.7-protected` configuration (block parent, $T_7(n,n,\cdot)\equiv0$, $K=3$): exact $[g^2]\hat H_2$ from the rational nested kernel equals $-c_2(J_3^\top\tilde M_3J_3+uu^\top/\alpha_2)$, (4.7); the value coefficient $[g^4]S$, from the exact Taylor coefficients of $\hat H_2$ and a series inverse, minus the regular (generalised-inverse) value equals the closed form (4.8), $-T_7(n,P_3,\Psi)^2/(6!\,T_7(n,\cdot,\Psi)^\top\tilde M_3^+T_7(n,\cdot,\Psi))$ ($=38339560750573/92111340150$ at seed 20260926, $14199492456/1010321125$ at seed 41), and the regular part equals the collapse value $\tfrac1{4!}(A_2P_2)^\top V_4^{-1}(A_2P_2)+\tfrac1{6!}T_6(\Psi^6)$; with $\Psi$ symbolic, the $n=6$ term has a non-constant reduced denominator and is homogeneous of degree 6. On the C1.8 configuration (block parent, generic $T_7$, simple pole): $[g^2]\hat H_2$ is the regular one (the kernel is invisible at $n=6$), $[g^3]\hat H_2=c_2J_3^\top AJ_3-c_2J_3^\top ww^\top J_3/\alpha_1$, and $[g^5]S$ minus the regular value is $-T_7(n,P_3,\Psi)^2/(7!\,T_7(n,n,\Psi))$.
- **C1.4, the (3.5) leg (fix pass 1, #12).** $V_4$ with $\ker V_4=\operatorname{span}(m)$ (block parent), $V_5$ annihilating $m$, $T_6$ a dense parent with $\tilde M_3=B_3$ non-degenerate and $T_6(\cdot_3;m,\Psi)=0$, built by exact projection of a random rational tensor onto the two linear constraints: $\hat H_2(g)m\equiv0$ and the quotient value $\tilde u_C^\top(C^\top\hat H_2C)^{-1}\tilde u_C$ identical for two complements, as rational functions of $g$. Each clause broken separately makes the quotient inconsistent; with only the $T_6$ clause broken (block $T_6$, $L_3m=B_3J_3m$), $\hat H_2m=O(g^2)$ with $[g^2]=-c_2L_3^\top\tilde M_3^{-1}L_3m$, exact. At $K=2$, descent holds with the R38 clause and fails without it.
- **C1.3, the D2 leg (fix pass 1, #12).** $K=4$, $\tilde M_3$ with kernel $n$ (block $T_6$, so D3 automatic), $T_7(n,\cdot,\Psi)=0$, $T_8$ a dense parent with $\tilde M_4=B_4$ non-degenerate and $L_4(\Psi)n=0$: $\hat H_3(g)n\equiv0$ including the level-4 Schur term, and $\hat H_2$ built on the level-3 quotient is identical for two complements. Break: block $T_8$, where $L_4n=\tilde M_4J_4n\ne0$ (the (3.8) propagation not satisfied).
- **C1.2, the two routes.** The nilpotent-$g$ route (truncated matrix series, $g^5=0$, recursion (1.2), determinant by $\det H_0\exp\operatorname{tr}\log$) is compared, coefficient by coefficient and exactly, with the full-Jacobi route: $\prod_{j\ge k}\det\hat H_j=\det\mathcal A'_{k..K}$ with $\mathcal A'=\operatorname{diag}(1/a_k)\mathcal A$, an exact polynomial in $g$ obtained by interpolation of exact determinants, with no Schur recursion; the rescaling is itself checked against $\det\mathcal A$ at $g=2/9$. $[g^0]\det\hat H_k=\det\tilde M_k$ at $k=2,3,4$ comes from the full-Jacobi route. $[g^1]$ is compared with the Jacobi formula $\det\tilde M_k\operatorname{tr}(\tilde M_k^{-1}A_k)$. Convergence: $\det\hat H_2(10^{-6})$ within $10^{-4}$ relative of $\det\tilde M_2$, and the remainder of the order-4 Taylor polynomial scales as $g^5$ (ratio $9.990\times10^{9}$ between $g=10^{-4}$ and $10^{-6}$, expected $10^{10}$).
  - First run of C1.2-limit FAILED (ratio $98.69$ against $100\pm1$ for the first-order remainder at $g=10^{-3},10^{-5}$). Diagnosis: the tolerance ignored the $O(g)$ relative correction ($c_2/c_1\cdot10^{-3}\approx1.3\%$), a defect of the check, not of the result. Replaced by the sharper remainder-scaling test above, with its own break leg.
- **C1.3/C1.4, descent leg.** $\tilde M_3$ with a kernel $n$ in the joint kernel (block parent, $T_7(n,\cdot,\Psi)=0$): $\det\hat H_3(g)\equiv0$ on $\mathcal S_3$ and $\hat H_3(g)n=0$ (kernel stable in $g$); $\hat H_2$ built on the quotient is identical for two complements; $[g^0]\det\hat H_3\rvert_Q=\det\tilde M_3\rvert_Q\neq0$; $\hat H_2(0)=V_4$.
- **C1.5.** Smallest $\lvert g\rvert$ zero of $\det\hat H_k(g)$ at the fixed $\Psi$: $0.072$, $0.112$, $0.302$ for $k=2,3,4$ (seed 20260926). This illustrates $r_{L,K}>0$ at one $(L,K)$, nothing more.
- **C1.7.** Exact Taylor coefficients of the rational $\hat H_2(g)$ with a singular $\tilde M_3$ are compared with the predictions (4.5): protected case (block parent, pole order 2), missed $O(g)$ (non-block source, $\alpha_1\ne0$), missed $O(g^0)$ (non-block source, $\alpha_1=0$, $\alpha_2=-w^\top\tilde M_3^+w$), and two $\Psi$ directions giving different $\hat H_2(g\to0)$.
- **C1.8.** $\det V_4=-21$ (seed 20260926), $\det\mathcal A(1/100)\neq0$, $\det\hat H_3=0\cdot g^0+\tfrac{8792}{45}g+\dots$
- **Not checked:** C1.4's and C1.6's general statements beyond one-dimensional kernels (proved in §3–§4; the script tests one-dimensional kernels only); pole orders 3, 4 (4.5′); (4.9) for $k\ge4$; the necessity of D3 for non-block-symmetric parents (proved in §4(b), no leg); anything on the string vertices (momenta, level limit); $\dim\mathcal H_0>2$. Dimensional analysis is not applicable (all objects are dimensionless multilinear forms of the algebraic layer); the $g\Psi$ scaling (C1.1) and the degree-6 homogeneity of the $n=6$ term are the relevant homogeneity checks.

## 7. Self-review

1. *Objective.* PH2 becomes PH1 + (D) + one kernel statement per level $k\ge3$ (PH2 (b)), the neighbourhood clause is shown to be automatic at a finite-dimensional truncation and unused by R26, and the part of (D) not already in the ledger (the $T_6$ half of (3.5), a presentation condition modulo a vertex condition) is named and machine-checked. Fix pass 1 adds the observable consequence of a failed level (a rational term in the $n=6$ or $n=7$ effective vertex, C1.10), which is what makes PH2 (b) falsifiable from vertex data. This shortens and sharpens the list; it does not discharge PH2 (b).
2. *Weakest step.* (i) The identification of the $k=2$ instance with PH1: at a finite-dimensional truncation PH1's invertibility clause is automatic for the radical quotient, so the equivalence has content only through the choice of the quotient, (3.5); stated in §3(c). (ii) The transfer to the string vertices: a fixed level carries continuous momenta, and the determinant and neighbourhood statements are not covered there (A1); the row says so.
3. *Not checked.* Multi-dimensional excess kernels in (4.5) (the one-dimensional formula generalises by replacing $\ell\ell^\top/\alpha_p$ with $\ell^\top(\alpha_p)^{-1}\ell$ on the excess block; not written out, not checked); pole orders 3, 4 (4.5′); the general-$k$ form (4.9).
4. *What a stronger reader would add.* Whether a presentation choice (019 §4 point 3: Veronese-null additions to the parent) can always remove an accidental kernel of $\tilde M_3$, and the $T_6(\cdot_3;\ker V_4,\Psi)$ block, without violating (D) elsewhere. Plausible (degeneracy is codimension one, and the $(3|2,1)$ block is free off the Veronese diagonal) and it would turn PH2 (b) into a presentation choice rather than a hypothesis; this is now PH2 (b)'s motivation, stated as expected, not attempted here. Failing it, 034's multiplier remedy (a) is the fallback.

## 8. Fix pass 1 (critic iteration 1)

Source: `agent/reports/critic-061-20260930T233500.md` (REVISE: 0 critical, 7 major, 7 minor, 2 notes). Nothing the critic re-derived is disputed. Line numbers are those of this version of the record.

| # | severity | finding | applied at | status |
|---|---|---|---|---|
| 1 | major | A1 "finite-dimensional" at fixed level ignores momenta | A1 (l. 24), C1 (l. 27), §3(c) (l. 158), §5 Result (l. 323), row (l. 336, last sentence) | applied |
| 2 | note | (3.4) forces the canonical quotient | C1, C1.4 (l. 31), §3(b) (l. 156), §3 Result, row | applied |
| 3 | minor | $N_{K,\infty}$ depends on $K$; parents need lower-level (3.4) | §3 Setup (l. 131) | applied |
| 4 | major | stability needed = (D) = (S$_g$) + source clause D3 | C1, C1.6 (l. 33), §4(b) (l. 224), §4 Result (l. 314), §5 item 4, row | applied |
| 5 | major | protection only for pole order $\le2$; orders 3, 4 | C1, C1.7 (l. 34), §4(d) (4.5′) (l. 262), §4(e), §4 Result, §5 item 5 | applied (orders 3, 4 stated, not checked) |
| 6 | minor | "radius not uniform" unproved; norm | C1, C1.5, §3 Commentary (l. 196), §5 item 3, row | applied |
| 7 | major | §4 remark false for pole order 2 | §4(f) (4.6)–(4.9) (l. 279), remark withdrawn (l. 319), new node C1.10 (l. 37), §5 item 6, PH2 (b) text; checks `C1.10-*` | applied, checked |
| 8 | minor | $T_6$ clause vs 034 (C$^{(6)}$) loose; presentation condition → PH2 (b) | (3.5) and §3(c) (l. 158), §5 PH5 bullet, PH2 (b) statement | applied |
| 9 | minor | "$\subseteq\ker\tilde M_k$" automatic; content "$\subseteq N_{k,\infty}$" | C1.9 (l. 36), PH2 (b) statement | applied |
| 10 | major | PH2 (b) motivation and falsifier | §5 PH2 (b) (l. 340), §7 item 4 | applied (critic's text, from §7.4 + 034 remedy (a)) |
| 11 | minor | D1–D3 undefined; PH1 misquoted in §4(b); 034 transposition | §3 Setup (l. 129), §4(b) (l. 224), C1.6 | applied |
| 12 | major | (3.5) and D2 unchecked; "Verified" scope | script: `C1.4-kerV4-*`, `C1.4-K2-limit`, `C1.3-descent-D2(-break)`; §6 (l. 362: by-construction list, Verified scope); row | applied, checked |
| 13 | major | PH2 users R21, R25, R35, R46 not re-pointed; no Used-by | §5 re-pointing list (l. 346), PH2 (b) Used-by | applied |
| 14 | minor | scope item (3): multiplier remedy | §5 Scope of the exclusion (l. 354), PH2 (b) motivation | applied |
| 15 | minor | $K=2$ limit; physical interpretation | §3(c) $K=2$ limit (l. 168), check `C1.4-K2-limit`; §5 Interpretation (l. 332) | applied |
| 16 | note | C1.8 logically trivial; "strictly extends" is class-level | C1.8 (l. 35), row, scope | applied |

**Nodes changed, and dependents.**

- Statement changed: A1 (#1), C1 (root: #1, #2, #4, #5, #6, #7), C1.4 (#2, #15, $K\ge3$ qualifier), C1.6 (#4, #11), C1.7 (#5). New node: C1.10 (#7).
- Wording or precision only, content unchanged: C1.5 (norm, #6), C1.8 (scope sentence, #16), C1.9 (#9).
- Coverage tags only: C1.3 (new check `C1.3-descent-D2`), C1.4, C1.6, C1.9 (new checks).
- Unchanged: A2, A3, C1.1, C1.2.
- Dependents: every node is cited by the root C1 only, and C1.9 by C1.6, C1.7, C1.10. A1 is cited implicitly by all nodes: its change restricts the transfer to the string vertices and leaves every finite-dimensional proof as it was. C1.7's changed statement is used by C1.10 in the pole-order-2 branch only, where the proviso holds. C1 holds as rewritten. `Hypotheses in force:` unchanged (none). By the schema this is a **full re-review** case (root statement changed).

## 9. Fix pass 2 (critic iteration 2)

Source: `agent/reports/critic-061-iter2-20261001T023000.md` (all nodes hold; 0 critical, 3 major, 7 minor, 1 note, all mechanical). Nothing disputed; script untouched, no run. Line numbers are those of this version.

| # | severity | finding | applied at | status |
|---|---|---|---|---|
| 1 | major | $n=6,7$ entry unscoped ($\ell=0$); "never invisible" | C1 (l. 27), C1.10 (l. 37), §4 Result (l. 314), §5 item 6 (l. 330), Interpretation (l. 332), row (l. 336), PH2 (b) Statement and Falsifier (l. 340) | applied: "block-symmetric ($\ell=0$): $n=6,7$; otherwise $n=4,5$ by (4.5), not machine-checked in the value"; "generically (whenever $T_7(n,P_3,\cdot)\not\equiv0$)" |
| 2 | major | $T_6$ clause is a presentation condition modulo a vertex condition | C1 (l. 27), C1.4 (l. 31), §3(c) (l. 158), §5 item 2 (l. 326), row (l. 336), PH2 (b) Statement, Motivation, Falsifier, PH5 bullet (l. 345) | applied: forced diagonal on $\operatorname{Sym}^6\mathcal H_0\cap(\mathcal S_3\otimes\ker V_4\otimes\mathcal H_0)$; $V_6(\chi^6)=0$; (C$^{(6)}$) + R38 suffice; vacuous at level 0 |
| 3 | minor | (D) "needed"/"necessary" without the D2 proviso | C1 (l. 27), §3(c) (l. 158), §5 item 2, row | applied |
| 4 | minor | (4.5′) unchecked in the root | C1 (l. 27) | applied |
| 5 | minor | $\tilde M_j$ invertible for $2\le j<k$ before (4.9) | §4(f) before (4.9) (l. 300), C1.10 (l. 37), §5 item 6 | applied |
| 6 | minor | A1 "generic symmetric tensors" | A1 (l. 24) | applied |
| 7 | major | PH2 (b) existential; R21, R25 named presentations | PH2 (b) Statement and Used-by (l. 340), re-pointing R21, R25 (l. 346 ff.) | applied |
| 8 | minor | R35: Conditional(PH6, PH1, PH2 (b), PH5) + new row | re-pointing list | applied |
| 9 | minor | R46 status line carries its domain | re-pointing list | applied |
| 10 | minor | by-construction count; one-$\Psi$ rationality | §6 (l. 362), row (l. 336) | applied: about 20 of 57; one point per seed |

**Nodes changed.** Statement: C1 (#1–#4), C1.4 ($T_6$ clause qualified, #2), C1.10 (scope $\ell=0$ stated, $\tilde M_j$ proviso, #1, #5). Wording only: A1 (#6). Unchanged: A2, A3, C1.1–C1.3, C1.5–C1.9. **Dependents.** C1.4's change restricts when the $T_6$ clause is satisfiable, not its necessity or the descent argument; C1.5 (radius) cites C1.4's condition and is unchanged. C1.10's change adds scope text; its derivation, (4.6)–(4.8) and the checks are as before. C1 holds as rewritten; `Open gaps:` and `Hypotheses in force:` unchanged.
