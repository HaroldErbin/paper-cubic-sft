# 066 — The Hessian of the cubic action is affine in the background: fluctuation spectra from low vertices only

Brief: `agent/briefs/active-computator-hessian-affine-20261001T022500.md` (Task 21).
Script: `codes/verify-hessian-affine.py` (log `agent/scratch/hessian-affine-run1.log`).

## Status

Fix pass after critic iteration 1 applied (2026-10-01): #1 (momentum remark made conditional, four places), #2–#5, #7, #9–#13, row renumbered R71 and replaced by the critic's draft; script break leg replaced, run 2: 32 PASS / 0 FAIL, log `agent/scratch/hessian-affine-run2.log`. Claim tree updated; node statements unchanged, justifications and restatements changed (see the fix-pass list at the end of the claim tree). Next: promotion of R71 by the orchestrator.

## Task and objective

**Literal task.** For the cubic Hubbard–Stratonovich action with auxiliaries $\Sigma_2,\Sigma_3,\dots$ (R1 at quartic, R17 at quintic, R19 / R26 at sextic and beyond), state and prove that the Hessian at a background $(\Psi_0,\Sigma_{2,0},\Sigma_{3,0},\dots)$ is affine in the background, give the order at which each block receives its last term, and conclude that the fluctuation spectrum around any solution of the cubic equations is the generalised eigenproblem of one matrix assembled from $V_2,\dots,V_{k+2}$ contracted once with the background — no $V_{\rm eff}$ Hessian, no matrix inverse. Then state the equivalence with the eliminated theory's spectrum through R65's congruence (inertia and zero modes, where the auxiliary blocks are invertible).

**Objective.** Task 21: the computational use of record 060's Schur identity. Around a truncated solution (059's critical points, a level-truncated tachyon vacuum with higher-rank $\Sigma$'s) the fluctuation analysis needs only the low vertices contracted once with the background — what level-truncation codes compute — and the nonpolynomial theory's Hessian (dressed vertices, $V_4^{-1}$) is never formed. A paper-level remark for the consistency-and-applications section; Task 14b instantiates it at level (1,1).

**Flag on the brief's statement (restated task vs. what is true).** The brief reads the $\Sigma_k\Sigma_k$ blocks as *constant* at every order. They are not: the mechanism the brief invokes (a cubic action has second derivatives at most linear in the fields) gives *affine*, and the $\Sigma_2\Sigma_2$ block is $\Psi_0$-linear from quintic order on — it is $-\tfrac{g^2}{12}K_{\Psi_0}$ with R17's dressed kernel $K_{\Psi_0}=V_4-\tfrac g5V_5(\cdot,\cdot,\Psi_0)$ (060 (1.4), R65) — and, in R19's $(\Psi,\Sigma_2)$ presentation, also $\Sigma_{2,0}$-linear at sextic order through $W_6(\Sigma_2^3)$. What is constant is the block at the order at which the field first appears: $-\tfrac{g^2}{12}V_4$ at quartic order (R68, 064 C4.2), $-\tfrac{g^4}{6!}\cdot2\tilde M_3$ for $\Sigma_3$ at sextic order. The objective is unaffected: every block is affine in the background, assembled from the vertices contracted once with one background field, with no inverse. The record states the correct version.

## Conventions and assumptions

- **A1** Finite cubic HS model of records 057/060: $\mathcal H=\mathbb R^N$, $\mathcal U\subseteq\mathcal H$, $\Sigma_k\in\mathrm{Sym}^k\mathcal U$ with coordinates the independent components ($a\le b$, $a\le b\le c$); vertices $V_n$, $T_n$ generic real totally symmetric tensors; symmetric (not graded) bilinear forms. C1/C4 fix the string-side identification $H(x,y)=\omega(x,\mathcal Ty)$, $V_{n+1}=\omega(\cdot,\ell_n)$; only the normalisation $V_{n+1}=\omega(\cdot,\ell_n)$ of C4 is used, in §2.
- **A2** Actions in the record's conventions (R1, R17, R19; 060 Part 1 docstring): $S_2=\tfrac12V_2(\Psi^2)+\tfrac g{3!}V_3(\Psi^3)-\tfrac{g^2}{4!}V_4(\Sigma_2,\Sigma_2)+\tfrac{2g^2}{4!}V_4(\Sigma_2,\Psi^{\otimes2})$; $S_3=S_2+\tfrac{g^3}{5!}V_5(\Sigma_2,\Sigma_2,\Psi)$; $S_4=S_3+\tfrac{g^4}{6!}W_6(\Sigma_2^3)$. Tower presentation (R26, scheme B, 019 §1) truncated at $K=3$: $S^{\rm tow}_3=\tfrac12V_2+\tfrac g{3!}V_3+\sum_{k=2}^3\big[a_k(-\tilde M_k(\Sigma_k,\Sigma_k)+2\langle\tilde u_k(\Sigma_{k-1}),\Sigma_k\rangle)+\tfrac{g^{2k-1}}{(2k+1)!}T_{2k+1}(\Sigma_k,\Sigma_k,\Psi)\big]$, $a_k=\tfrac{g^{2k-2}}{(2k)!}$, $\tilde M_2=V_4$, $T_5=V_5$, $\tilde u_2=V_4(\cdot,\Psi^{\otimes2})$, $\tilde u_3(\Sigma_2)=T_6(\cdot,\Sigma_2,\Psi)$ (partition $6=3+2+1$), $T_7(\Sigma_3,\Sigma_3,\Psi)$ (partition $7=3+3+1$). In the model $\tilde M_3$, $T_6$, $T_7$ are generic symmetric tensors (their forced values, R26, play no role in the block structure); likewise $W_6$ is generic in the model (R19's forced sextic vertex in the text), as are $V_4,V_5$.
- **A3** Order grading (R26 scaling grading): a monomial with strand numbers $(k_a,k_b,k_c)$ is an $n$-point term, $n=k_a+k_b+k_c$, with coupling $g^{n-2}$; "$n$-th order" below means this $n$ (quartic $=4$, quintic $=5$, sextic $=6$).
- **A4** Backgrounds $(\Psi_0,\Sigma_{2,0},\Sigma_{3,0})$ are arbitrary points of field space unless stated; "the saddle" means $\Sigma_0=\Sigma_*(\Psi_0)$ on a branch of the $\Sigma$-equations with the auxiliary block invertible; a "critical point" is a joint critical point of the cubic action.
- Hypotheses: none in the finite model. The transfer to the string vertices is Conditional(PH1, PH5), as in R65 (the on-shell matchings R1, R17, R19 that identify the Schur complement with the nonpolynomial Hessian); the affine structure itself (C1) needs no hypothesis at the vertices, being a statement about the polynomial degree of the action.

## Claim tree

- **A1–A4** as above. Hypotheses: none (finite model); PH1, PH5 for the transfer clauses of C2.4 and C4.
- **C1** (Affine Hessian.) For any action polynomial of degree $\le3$ in the fields, $H(\phi_0)=S^{(2)}+S^{(3)}(\phi_0,\cdot,\cdot)$: every block is affine in the background, each term linear in exactly one background field, and $H(\phi_0)$ is the linearised EOM operator. In the HS presentations of A2 the blocks are Table 1.1 (R19 presentation through $S_4$) and Table 1.2 (tower, $K=3$), each block receiving its last term at the order listed; the general-$k$ pattern is (1.5)–(1.6), (1.6) for $k\ge3$ ($k=2$ is (1.4)). [by C1.1–C1.3]
  - **C1.1** Proposition (1.1)–(1.2): cubic $\Rightarrow$ affine, with the order rule (1.3). [eq. (1.1)–(1.3)]
  - **C1.2** Table 1.1: the blocks of $S_2,S_3,S_4$ at $(\Psi_0,\Sigma_{2,0})$, 060 (1.2)–(1.4) with the $\Sigma_{2,0}$-term of $W_6$; $\Psi\Psi$ exhausted at $n=4$, $\Sigma_2\Psi$ at $n=5$, $\Sigma_2\Sigma_2$ at $n=6$, and no cubic monomial in $(\Psi,\Sigma_2)$ exists beyond $n=6$. [by R65, C1.1; eq. (1.4)] [check: C1.2-blocks-S3, C1.2-blocks-S4, C1.2-affine-S3, C1.2-affine-S4, C1.2-scaling-S3, C1.2-scaling-S4, C1.2-break-quartic-term, C1.2-break-coefficient]
  - **C1.3** Table 1.2: the tower blocks at $(\Psi_0,\Sigma_{2,0},\Sigma_{3,0})$, (1.5); the $\Sigma_k\Sigma_k$ block is constant at $n=2k$ and $\Psi_0$-linear at $n=2k+1$, never $\Sigma$-dependent in scheme B; $(\Sigma_k,\Sigma_{k-1})$ is $\Psi_0$-linear at $n=2k$ only; $(\Sigma_k,\Psi)$ receives $\Sigma_{k-1,0}$ at $2k$, $\Sigma_{k,0}$ at $2k+1$, $\Sigma_{k+1,0}$ at $2k+2$. [by A2, A3, C1.1; eq. (1.5)–(1.6)] [check: C1.3-blocks-tower, C1.3-affine-tower, C1.3-scaling-tower]
- **C2** (Spectrum.) The fluctuation operator around any background is $\mathcal T=G^{-1}H$, $G=\omega_1\oplus\omega_2\oplus\omega_3$ (C4), the pencil $(H,G)$; $G$ is indefinite (its factor $\omega_1$ has $g(T,T)<0<g(D,D)$; R68 records the indefinite $\Sigma$ block at level (1,1), R64 the five-field truncation), so the congruence invariants of $H$ — inertia and kernel — are the meaningful counts, not the signs of pencil eigenvalues. Wherever the auxiliary block $H_{\rm aux}$ is invertible: $\mathrm{In}(H)=\mathrm{In}(H_{\rm eff})+\mathrm{In}(H_{\rm aux})$ and $\ker H=\{(x,\Sigma_*'x):x\in\ker H_{\rm eff}\}$, with $H_{\rm eff}=\mathrm{Hess}\,V_{\rm eff}$ on the saddle; the pencil eigenvalues are not equal (congruent, not isospectral). [by C2.1–C2.4]
  - **C2.1** The congruence of R65 for $(\Psi,\Sigma_2)$ extends verbatim to the tower (block $LDL^\top$ over the whole auxiliary block $-2\mathcal A$): (2.2). [by R65; eq. (2.1)–(2.3)] [check: C2.1-critical-point-S3, C2.1-critical-point-tower, C2.1-inertia-S3, C2.1-inertia-tower, C2.1-inertia-break-psi-block-S3, C2.1-inertia-break-psi-block-tower, C2.1-inertia-break-sign-tower]
  - **C2.2** Zero modes: $L$ invertible maps $\ker H$ onto $\ker H_{\rm eff}\oplus0$; the joint zero mode is $(x,\Sigma_*'x)$, the fluctuation that follows the saddle; $(x,0)$ is not a zero mode unless $H_{\Sigma\Psi}x=0$. [by C2.1; eq. (2.4)] [check: C2.2-kernel-Heff-S3, C2.2-kernel-Heff-tower, C2.2-zero-mode-S3, C2.2-zero-mode-tower, C2.2-zero-mode-break-S3, C2.2-zero-mode-break-tower]
  - **C2.3** Eigenvalues of $G^{-1}H$ differ from those of $G_1^{-1}H_{\rm eff}\oplus G_{\rm aux}^{-1}H_{\rm aux}$ in general (the congruence $L$ is not $G$-orthogonal); only $\mathrm{In}$ and $\dim\ker$ are shared. [eq. (2.5); by check: C2.3-not-isospectral-S3, C2.3-not-isospectral-tower]
  - **C2.4** On the saddle, $H_{\rm eff}=\mathrm{Hess}V_{\rm eff}$ exactly (R65 (1.8)), so the counts of C2.1–C2.2 are those of the eliminated theory; at the vertices, $\mathrm{Hess}V_{\rm eff}=\mathrm{Hess}S^{(n+2)}_{\rm eff}$ to the matched order, Conditional(PH1, PH5). [by R65, PH1, PH5] [check: C2.4-schur-equals-HessVeff-S3, C2.4-schur-equals-HessVeff-tower]
- **C3** (Fold.) At $S_4$ on the fold locus $\det\mathcal K=0$ of 057, the joint Hessian is regular and affine (continuous through the fold) while $\mathrm{Hess}V_{\rm eff}$ diverges; the decomposition of C2.1 fails only because $H_{\rm aux}$ is singular there. In the one-field model: $\det H=-H_{t\sigma}^2\ne0$ at the fold, $\mathrm{In}(H)=(1,1)$. [eq. (3.1)–(3.3)] [check: C3-fold-regular, C3-fold-Veff-diverges]
- **C4** (Interpretation.) Around any solution of the cubic equations, truncated or not, the fluctuation operator is one affine matrix in the low vertices contracted once with the background; the eliminated theory's negative- and zero-mode counts are $\mathrm{In}(H)-\mathrm{In}(H_{\rm aux})$ and $\dim\ker H$, with $H_{\rm aux}$ known in closed form; at the vertices Conditional(PH1, PH5) for the identification with the nonpolynomial theory. [by C1, C2, C3]

Open gaps: none
Hypotheses in force: none in the finite model; PH1, PH5 for C2.4 and the transfer clause of C4

Fix pass (critic iteration 1): changed restatements only, node statements unchanged. C1.3 statement: (1.6) restricted to $k\ge3$ (statement narrowed to what was proved; $k=2$ is (1.4), C1.2). C2.2/C2.3 momentum remark and C4 paper paragraph: restated as conditional on $H_{\rm aux}(k)$ invertible (justification and wording). C3: sheet-exchange clause (justification). C2.4/C4: transfer as R65's scope. Ledger IDs R64 to R68 for record 064. Dependents of C1.3 ((1.5), C2.1): still hold ($k\ge3$ rule never used for $k=2$). Dependents of the momentum remark: none among nodes (declared untested).

## 1. The affine Hessian and the orders table (C1)

\subsection*{Setup}
A1–A4. Fields collectively $\phi=(\Psi,\Sigma_2,\Sigma_3,\dots)$ with coordinates $\phi^i$; fluctuations $x$ ($\Psi$), $y$ ($\Sigma_2$), $z$ ($\Sigma_3$). $S^{(2)}$, $S^{(3)}$ the quadratic and cubic parts of the action as symmetric multilinear forms, $S=S^{(1)}(\phi)+\tfrac12S^{(2)}(\phi,\phi)+\tfrac1{3!}S^{(3)}(\phi,\phi,\phi)$. $V_n(\Sigma_{2,0},\cdot,\cdot)$ denotes the bilinear form obtained by contracting two legs of $V_n$ with the symmetric tensor $\Sigma_{2,0}$, and likewise for $\Sigma_{3,0}$ on three legs.

\subsection*{Derivation}
*Proposition (cubic $\Rightarrow$ affine).* For a polynomial action of degree $\le3$,
$$
H_{ij}(\phi_0):=\frac{\partial^2S}{\partial\phi^i\partial\phi^j}(\phi_0)=S^{(2)}_{ij}+S^{(3)}_{ijk}\,\phi_0^k ,
\tag{1.1}
$$
since the second derivative of a cubic monomial is linear in the fields and that of a quadratic one is constant. Equivalently, $H(\phi_0)$ is the linearisation of the cubic equations of motion $\partial_iS=S^{(1)}_i+S^{(2)}_{ij}\phi^j+\tfrac12S^{(3)}_{ijk}\phi^j\phi^k$ at $\phi_0$:
$$
H(\phi_0)\,\delta\phi=\partial S(\phi_0+\delta\phi)-\partial S(\phi_0)-\tfrac12S^{(3)}(\delta\phi,\delta\phi,\cdot),
\tag{1.2}
$$
the last term being the only nonlinearity of the cubic EOM. Each block $(a,b)$ of $H$ receives, from every cubic monomial $\phi_a\phi_b\phi_c$ of $S$, one term linear in the background field $\phi_{c,0}$, and nothing else. With the order grading A3, a monomial with strand numbers $(k_a,k_b,k_c)$ is a $(k_a+k_b+k_c)$-point term, so
$$
\text{block }(k_a,k_b)\ \text{receives from the background field }\Sigma_{k_c}\ \text{a term at order }n=k_a+k_b+k_c\ (\text{coupling }g^{n-2}),
\tag{1.3}
$$
and the block is exhausted at $n=k_a+k_b+k_{\max}$, $k_{\max}$ the largest strand number of a field that appears in a monomial together with $\Sigma_{k_a}\Sigma_{k_b}$. There is no other source of background dependence: no inverse, no dressed vertex, no derivative of $\Sigma_*(\Psi)$.

*Table 1.1 — the $(\Psi,\Sigma_2)$ presentation through $S_4$ (R1, R17, R19).* From A2 by (1.1), at $(\Psi_0,\Sigma_{2,0})$ (060 (1.2)–(1.4), R65):
$$
\begin{aligned}
H_{\Psi\Psi}&=\underbrace{V_2}_{n=2}+\underbrace{g\,V_3(\Psi_0,\cdot,\cdot)}_{n=3}+\underbrace{\tfrac{g^2}{6}\,V_4(\Sigma_{2,0},\cdot,\cdot)}_{n=4}, &&\text{exhausted at }n=4,\\
H_{\Sigma_2\Psi}(y,x)&=\underbrace{\tfrac{g^2}{6}\,V_4(y,\Psi_0,x)}_{n=4}+\underbrace{\tfrac{g^3}{60}\,V_5(y,\Sigma_{2,0},x)}_{n=5}, &&\text{exhausted at }n=5,\\
H_{\Sigma_2\Sigma_2}&=\underbrace{-\tfrac{g^2}{12}\,V_4}_{n=4,\ \text{constant}}+\underbrace{\tfrac{g^3}{60}\,V_5(\cdot,\cdot,\Psi_0)}_{n=5}+\underbrace{\tfrac{g^4}{120}\,W_6(\Sigma_{2,0},\cdot,\cdot)}_{n=6}, &&\text{exhausted at }n=6 .
\end{aligned}
\tag{1.4}
$$
At $S_3$ the auxiliary block is $-\tfrac{g^2}{12}K_{\Psi_0}$ with R17's dressed kernel; at $S_4$ it is $-\tfrac{g^2}{12}\mathcal K(\Psi_0,\Sigma_{2,0})$ of 060 (1.4). Beyond $n=6$ there is no cubic monomial in $(\Psi,\Sigma_2)$ at all: three strand numbers from $\{1,2\}$ sum to at most $6$. So the $(\Psi,\Sigma_2)$ cubic theory's Hessian is exhausted at sextic order in every block, and any higher order needs $\Sigma_3$ ($7=3+3+1=3+2+2$), which is the tower.

*Table 1.2 — the tower presentation, $K=3$ (R26 scheme B, A2).* At $(\Psi_0,\Sigma_{2,0},\Sigma_{3,0})$, with $a_2=\tfrac{g^2}{24}$, $a_3=\tfrac{g^4}{720}$:
$$
\begin{aligned}
H_{\Psi\Psi}&=V_2+g\,V_3(\Psi_0)+\tfrac{g^2}{6}V_4(\Sigma_{2,0}) &&(n=2,3,4;\ \text{exhausted at }4),\\
H_{\Sigma_2\Psi}(y,x)&=\tfrac{g^2}{6}V_4(y,\Psi_0,x)+\tfrac{g^3}{60}V_5(y,\Sigma_{2,0},x)+\tfrac{g^4}{360}T_6(\Sigma_{3,0},y,x) &&(n=4,5,6;\ \text{exhausted at }6),\\
H_{\Sigma_2\Sigma_2}&=-\tfrac{g^2}{12}V_4+\tfrac{g^3}{60}V_5(\cdot,\cdot,\Psi_0)=-\tfrac{g^2}{12}K_{\Psi_0} &&(n=4,5;\ \text{exhausted at }5),\\
H_{\Sigma_3\Psi}(z,x)&=\tfrac{g^4}{360}T_6(z,\Sigma_{2,0},x)+\tfrac{g^5}{2520}T_7(z,\Sigma_{3,0},x) &&(n=6,7;\ \text{exhausted at }7\text{ for }K=3,\ 8\text{ with }\Sigma_4),\\
H_{\Sigma_3\Sigma_2}(z,y)&=\tfrac{g^4}{360}T_6(z,y,\Psi_0) &&(n=6;\ \text{exhausted at }6),\\
H_{\Sigma_3\Sigma_3}&=-\tfrac{g^4}{360}\tilde M_3+\tfrac{g^5}{2520}T_7(\cdot,\cdot,\Psi_0)=-\tfrac{g^4}{360}\hat M_3(\Psi_0) &&(n=6,7;\ \text{exhausted at }7).
\end{aligned}
\tag{1.5}
$$
General $k\ge3$ in scheme B (monomials $(k,k,1)$, $(k,k-1,1)$ and $(1,1,2)$ only; for $k=2$ the $(1,1,2)$ monomial contains $\Psi$ twice, so the $\Sigma_2\Psi$ and $\Sigma_2\Sigma_1$ lines of the rule double-count and are replaced by (1.4): $H_{\Sigma_2\Psi}=\tfrac{g^2}6V_4(\cdot,\Psi_0,\cdot)+\dots$, not $\tfrac{g^2}{12}$; checked at $k=3$ against (1.5)):
$$
\begin{aligned}
H_{\Sigma_k\Sigma_k}&=-2a_k\hat M_k(\Psi_0)=-2a_k\tilde M_k+\tfrac{2g^{2k-1}}{(2k+1)!}T_{2k+1}(\cdot,\cdot,\Psi_0) &&(n=2k\ \text{constant},\ 2k+1\ \Psi_0\text{-linear}),\\
H_{\Sigma_k\Sigma_{k-1}}&=2a_k\,T_{2k}(\cdot,\cdot,\Psi_0) &&(n=2k\ \text{only}),\\
H_{\Sigma_k\Psi}&=2a_kT_{2k}(\cdot,\Sigma_{k-1,0},\cdot)+\tfrac{2g^{2k-1}}{(2k+1)!}T_{2k+1}(\cdot,\Sigma_{k,0},\cdot)+2a_{k+1}T_{2k+2}(\Sigma_{k+1,0},\cdot,\cdot) &&(n=2k,2k+1,2k+2),\\
H_{\Sigma_k\Sigma_j}&=0\quad(|k-j|\ge2), \qquad H_{\Psi\Psi}\ \text{as in (1.4)}.
\end{aligned}
\tag{1.6}
$$
The auxiliary block of the tower is $-2\mathcal A(\Psi_0)$, the block-tridiagonal Jacobi operator of R26 (1): $\Psi_0$-linear, never $\Sigma$-dependent. In R24's presentation with the wrong-sign partner $\chi$ the same rule gives $H_{\chi\chi}=+\tfrac{g^2}{12}V_4$ (constant), $H_{\chi\Sigma_2}=\tfrac{g^3}{60}V_5(\cdot,\cdot,\Psi_0)$, $H_{\chi\Psi}=\tfrac{g^3}{60}V_5(\cdot,\Sigma_{2,0},\cdot)$, $H_{\Sigma_2\Sigma_2}=-\tfrac{g^2}{12}V_4+\tfrac{g^3}{60}V_5(\cdot,\cdot,\Psi_0)+\tfrac{g^4}{120}V_6(\Sigma_{2,0},\cdot,\cdot)$.

\subsection*{Commentary}
- (1.1) is the whole proof; (1.2) says the same thing as the linearised EOM, which is how a level-truncation code would compute it (the Jacobian of the residual). Nothing about the vertices enters: (1.1) holds for the string action with the same words, with $H$ the graded-symmetric second variation and the blocks the vertices contracted once with the background.
- (1.3): the order rule is R26's scaling grading ($\Sigma_k\sim\Psi^k$, $n$-point vertex $\propto g^{n-2}$), used here only to label the orders; the affinity does not depend on it.
- Table 1.1 vs the brief: the $\Sigma_2\Sigma_2$ block is constant at $n=4$ only. Its $n=5$ term is R17's dressing, and it is the term that makes the fluctuation propagator of $\delta\Sigma$ background-dependent (060 §1, "the dressed kernel is the propagator of the $\Sigma$-fluctuation"); its $n=6$ term exists in the $(\Psi,\Sigma_2)$ presentation (R19's $W_6(\Sigma^3)$ is cubic in $\Sigma_2$) and is absent in the tower, where the sextic data sit in $\tilde M_3$, $T_6$ instead.
- The exhaustion orders are presentation facts (R17's and R19's uniqueness for Table 1.1; the scheme-B monomial list for Table 1.2), not consequences of (1.1). What (1.1) guarantees in every presentation is that no block ever receives a term of higher than first degree in the background.

\subsection*{Result}
$$\boxed{H(\phi_0)=S^{(2)}+S^{(3)}(\phi_0,\cdot,\cdot):\ \text{every block affine in the background, each term one vertex contracted once with one background field; Tables 1.1–1.2 with their exhaustion orders.}}$$

## 2. The spectrum statement (C2)

\subsection*{Setup}
A1, A4; C4 for the identification of forms with operators. Joint fluctuation $\delta\phi=(x,y,z)$; $H$ the joint Hessian of §1; $H_{\rm aux}$ its auxiliary block ($H_{\Sigma_2\Sigma_2}=-\tfrac{g^2}{12}\mathcal K$ in the $(\Psi,\Sigma_2)$ presentation; the block-tridiagonal $-2\mathcal A(\Psi_0)$ of (1.6) in the tower); $H_{\Sigma\Psi}$ the column of mixed blocks; $H_{\rm eff}:=H_{\Psi\Psi}-H_{\Sigma\Psi}^\top H_{\rm aux}^{-1}H_{\Sigma\Psi}$ the Schur complement. $G:=\omega_1\oplus\omega_2\oplus\omega_3$ the kinetic pairing on $(\delta\Psi,\delta\Sigma_2,\delta\Sigma_3)$, $\omega_k=\omega_1^{\otimes k}$ (R58).

\subsection*{Derivation}
*The operator.* By C4, a symmetric form on field space is turned into an operator by the pairing: $H(\delta\phi,\delta\phi')=G(\delta\phi,\mathcal T\delta\phi')$, $\mathcal T=G^{-1}H$, and the quadratic action of the fluctuations is $\tfrac12G(\delta\phi,\mathcal T\delta\phi)$. On the $\Psi$ block, $\omega_1^{-1}H_{\Psi\Psi}=Q+g\ell_2(\Psi_0,\cdot)+\tfrac{g^2}3L_3(\Sigma_{2,0})$ (R66); on the $\Sigma_2$ block at quartic order, $\omega_2^{-1}H_{\Sigma_2\Sigma_2}=-\tfrac{g^2}{12}m_2$ with R1's $m_2=\omega_2^{-1}V_4$ (064 C3.2: the pencil $(A,G_2)$). "Spectrum" therefore means the pencil $(H,G)$, $Hv=\lambda Gv$:
$$
\mathcal T=G^{-1}H(\phi_0),\qquad H(\phi_0)=S^{(2)}+S^{(3)}(\phi_0,\cdot,\cdot)\ \text{(1.1)}: \quad\text{one affine matrix, no inverse, no dressed vertex.}
\tag{2.1}
$$
$G$ is indefinite ($\omega_1$ itself has $g(T,T)<0<g(D,D)$, which suffices; R68, record 064, quotes inertia $(2,1)$ for the level-(1,1) $\Sigma$ block, and whether that is the inertia of the kinetic pairing $G_2$ or of the action block $A=V_4\vert_{\mathcal S}$ is not decided from the ledger headings and is not used here), so $\mathcal T$ is $G$-self-adjoint but not symmetric, its eigenvalues need not be real, and their signs are not a count of unstable directions. What is invariant under a change of basis of field space, and what R65's congruence controls, is the inertia and the kernel of the form $H$ (Sylvester), and the kernel of $\mathcal T$, which equals that of $H$ since $G$ is invertible.

*Congruence for the tower (C2.1).* Wherever $H_{\rm aux}$ is invertible, the block $LDL^\top$ factorisation of 060 (1.15) applies verbatim with the whole auxiliary column in place of the $\Sigma_2$ column:
$$
H=L^\top\big(H_{\rm eff}\oplus H_{\rm aux}\big)L,\qquad L=\begin{pmatrix}1&0\\H_{\rm aux}^{-1}H_{\Sigma\Psi}&1\end{pmatrix},\qquad \det L=1 ,
\tag{2.2}
$$
$$
\mathrm{In}(H)=\mathrm{In}(H_{\rm eff})+\mathrm{In}(H_{\rm aux}),\qquad \det H=\det H_{\rm aux}\,\det H_{\rm eff},\qquad \dim\ker H=\dim\ker H_{\rm eff}.
\tag{2.3}
$$
Nothing in (2.2) uses the tridiagonal structure of the tower or the number of auxiliaries; it is the completion of the square in the auxiliary fluctuation $y'=y+H_{\rm aux}^{-1}H_{\Sigma\Psi}x$. The invertibility required is that of the joint block $H_{\rm aux}=-2\mathcal A(\Psi_0)$; it is not R26's nested condition (each $\hat M_k$ invertible in sequence along the continued fraction), the two failing on different codimension-one sets, so $V_{\rm eff}$ being the Gaussian of R26 (2) does not import the nested conditions.

*Zero modes (C2.2).* $L$ is invertible, so $\ker H=L^{-1}(\ker H_{\rm eff}\oplus0)$:
$$
\ker H=\big\{(x,\,\Sigma_*'x):\ x\in\ker H_{\rm eff}\big\},\qquad \Sigma_*'=-H_{\rm aux}^{-1}H_{\Sigma\Psi}\ \ (060\ (1.6)):
\tag{2.4}
$$
the joint zero mode is the $\Psi$ zero mode of the eliminated theory dressed by the fluctuation of the auxiliary that follows the saddle; the naive lift $(x,0)$ is a zero mode only if $H_{\Sigma\Psi}x=0$.

*Not isospectral (C2.3).* $L$ is not $G$-orthogonal ($L^\top GL\ne G$ in general), so the pencil $(H,G)$ and the pencil $(H_{\rm eff}\oplus H_{\rm aux},\,G)$ have different eigenvalues:
$$
\operatorname{spec}\big(G^{-1}H\big)\ne\operatorname{spec}\big(\omega_1^{-1}H_{\rm eff}\big)\cup\operatorname{spec}\big(G_{\rm aux}^{-1}H_{\rm aux}\big)\ \text{in general};\qquad \text{shared: } \mathrm{In},\ \dim\ker .
\tag{2.5}
$$
Only the invariants of (2.3) transfer between the cubic and the eliminated theory. In the string theory, with the momentum dependence restored, the physical statement is the one about kernels: a mass shell is a momentum at which the fluctuation operator has a zero mode, and (2.4) says that at momenta $k$ where $H_{\rm aux}(k)$ is invertible the mass shells of the cubic theory around the background are those of $H_{\rm eff}(k)$. This is conditional: R67's locus is a locus in field space, whereas with momentum restored $\det H_{\rm aux}(k)$ is a function of $k$ at fixed background, and whether it vanishes at some $k\ne0$ (propagating $\Sigma$ modes) is the open item of R68; such zeros are not excluded, and would be mass shells of the cubic theory absent from $H_{\rm eff}$.

*On the saddle (C2.4).* At $\Sigma_0=\Sigma_*(\Psi_0)$ on a branch with $H_{\rm aux}$ invertible, $H_{\rm eff}=\mathrm{Hess}\,V_{\rm eff}(\Psi_0)$ exactly (R65 (1.8), the envelope theorem at second order; for the tower the same proof, $V_{\rm eff}$ being the Gaussian of R26 (2)). So around a joint critical point of the cubic theory — which projects to a critical point of $V_{\rm eff}$ —
$$
\mathrm{In}(\mathrm{Hess}\,V_{\rm eff})=\mathrm{In}(H)-\mathrm{In}(H_{\rm aux}),\qquad \ker\mathrm{Hess}\,V_{\rm eff}=\pi_\Psi(\ker H),
\tag{2.6}
$$
with $H$ the affine matrix (2.1) and $H_{\rm aux}$ known in closed form ((1.4), (1.6)); at the string vertices $\mathrm{Hess}V_{\rm eff}=\mathrm{Hess}S^{(n+2)}_{\rm eff}+O(g^{\text{next}})$ to the matched order, Conditional(PH1, PH5) (R65's scope). Where $H_{\rm aux}$ is singular — R67's locus at $S_3$, the fold of 057 at $S_4$ (§3) — the Schur complement does not exist and (2.6) is not defined; $H$ itself is.

\subsection*{Commentary}
- (2.1): $G^{-1}$ is the inverse of the kinetic pairing, not of a vertex; at level truncation it is the inverse of a fixed block-diagonal Gram matrix, and the generalised eigenproblem $Hv=\lambda Gv$ needs no inverse at all.
- (2.2)–(2.3): Haynsworth's inertia additivity; the auxiliary summand has no kinetic operator and is an algebraic, non-propagating sector (060 §1).
- (2.5) is the reason the record speaks of counts and kernels, not of eigenvalues: the brief's "generalised eigenproblem" gives the same mass shells and the same inertia as the eliminated theory, not the same off-shell eigenvalues.
- The momentum remark after (2.5) is stated for the string theory and is not tested in the model (no momentum); it is conditional on $H_{\rm aux}(k)$ being invertible: contact vertices give $H_{\rm aux}$ no pole, but its determinant can vanish at isolated momenta, and zeros of $\det H_{\rm aux}(k)$ at $k\ne0$ are not excluded (R68's unexamined propagating $\Sigma$ modes). Where they occur (2.2) fails and the cubic theory has extra mass shells.

\subsection*{Result}
$$\boxed{\mathcal T=G^{-1}\big[S^{(2)}+S^{(3)}(\phi_0,\cdot,\cdot)\big];\quad \mathrm{In}(H)=\mathrm{In}(H_{\rm eff})+\mathrm{In}(H_{\rm aux}),\ \ \ker H=\{(x,\Sigma_*'x)\},\ \ H_{\rm eff}=\mathrm{Hess}V_{\rm eff}\ \text{on the saddle},\ \text{where }H_{\rm aux}\text{ is invertible; congruent, not isospectral.}}$$

## 3. The fold of $S_4$ (C3) and the finite-model checks

\subsection*{Setup}
A1, A2. One-field model of 057 ($\dim\mathcal U=\dim\mathcal S=1$) at $S_4$, $g=1$: $S=\tfrac{v_2}2t^2+\tfrac{v_3}6t^3-\tfrac a{24}\sigma^2+\tfrac a{12}\sigma t^2+\tfrac w{120}\sigma^2t+\tfrac W{720}\sigma^3$.

\subsection*{Derivation}
The $\sigma$-equation $E_\sigma=\tfrac a{12}t^2+\sigma(-\tfrac a{12}+\tfrac w{60}t)+\tfrac W{240}\sigma^2=0$ is quadratic, with two sheets $\sigma_\pm(t)$; the fold is where they meet, i.e. where $E_\sigma=0$ and $\partial_\sigma E_\sigma=H_{\sigma\sigma}=0$ together:
$$
H_{\sigma\sigma}=-\tfrac a{12}+\tfrac w{60}t+\tfrac W{120}\sigma=0,\qquad E_\sigma\big|_{H_{\sigma\sigma}=0}=\tfrac a{12}t^2-\tfrac W{240}\sigma^2=0\ \Rightarrow\ \sigma_f^2=\tfrac{20a}{W}t_f^2 ,
\tag{3.1}
$$
real iff $aW>0$. At the fold the joint Hessian is affine, hence finite and continuous, and
$$
\det H=H_{tt}H_{\sigma\sigma}-H_{t\sigma}^2=-H_{t\sigma}^2<0,\qquad H_{t\sigma}=\tfrac a6t_f+\tfrac w{60}\sigma_f\ne0\ \text{generically}:\qquad \mathrm{In}(H)=(1,1,0).
\tag{3.2}
$$
On either sheet, $V_{\rm eff}''(t)=H_{tt}-H_{t\sigma}^2/H_{\sigma\sigma}$ (Schur), and $H_{\sigma\sigma}\to0$ linearly in $\sigma-\sigma_f\propto\sqrt{|t-t_f|}$ along the sheet, so
$$
|V_{\rm eff}''(t)|\sim|t-t_f|^{-1/2}\to\infty\quad(t\to t_f):
\tag{3.3}
$$
the eliminated theory's fluctuation operator diverges at the fold while the cubic theory's is regular. The congruence (2.2) fails there only because $H_{\rm aux}$ is singular: the count $\mathrm{In}(H)$ is regular at the fold, and the two summands of (2.3) exchange one unit between the two sheets meeting at the fold (at the same $t$, on $\sigma_-$ one has $H_{\sigma\sigma}<0$ and $V''_{\rm eff}>0$, on $\sigma_+$ the reverse; $H_{\rm aux}$ changes sign across the pair, one eigenvalue of $H_{\rm eff}$ passes through infinity) — an exchange along the curve through the fold point parametrised by $\sigma$, not along $t$ on one sheet. The fold is a property of the elimination, not of the cubic theory.

\subsection*{Commentary}
- (3.1): the fold condition is a discriminant; the factor $20a/W$ is chosen a perfect square ($a=1$, $W=\tfrac54$) in the check so that the fold points are rational.
- (3.3): the exponent $-\tfrac12$ is the generic square-root branch point of $\sigma_\pm(t)$; the check measures the growth of $|V''_{\rm eff}|$ by a factor $\approx10$ per factor $100$ in $|t-t_f|$ (9.53, 9.94).

\subsection*{Verification}
`codes/verify-hessian-affine.py`, run 1 (seed 20261001, 30 PASS / 0 FAIL, log `agent/scratch/hessian-affine-run1.log`) and, after the fix pass replaced the vacuous sign leg, run 2 (same seed, `OMP_NUM_THREADS=1`): 32 PASS / 0 FAIL, log `agent/scratch/hessian-affine-run2.log`. Exact sympy rationals throughout; inertia from mpmath eigenvalues at 50 digits with the zero count fixed by the exact rank; the pencil eigenvalues of C2.3 in float64.

- *C1.2 / C1.3 (Tables 1.1–1.2, affinity).* Untruncated model $N=2$ ($\Sigma_2\in\mathrm{Sym}^2$, dim 3; $\Sigma_3\in\mathrm{Sym}^3$, dim 4). `C1.2-blocks-S3`, `C1.2-blocks-S4`, `C1.3-blocks-tower`: the hand blocks (1.4)/(1.5) assembled from the vertices and a random rational background equal the sympy Hessian of the action, exactly, at all orders in $g$ (dims 5, 5, 9). `*-affine-*`: every entry of the symbolic Hessian has total degree exactly 1 in the fields. `*-scaling-*`: $H(\lambda\phi_0)$ has vanishing second $\lambda$-difference and nonvanishing first. Break legs: `C1.2-break-quartic-term` (a quartic monomial added to $S_3$ gives degree-2 entries); `C1.2-break-coefficient` ($\tfrac{g^3}{48}$ for $\tfrac{g^3}{60}$ fails the block comparison).
- *C2.1, C2.2, C2.4 (inertia, zero modes, saddle).* Engineered joint critical points: $S_3$ with $\dim\mathcal U=3$ (dim 9) and the tower with $\dim\mathcal U=2$ (dim 9). Construction: with $V_2$ left free, $\mathrm{Hess}V_{\rm eff}$ and $\nabla V_{\rm eff}$ at $\Psi_0$ are computed by an $\epsilon$-expansion of the eliminated action (series solve of the linear auxiliary equations to $\epsilon^2$, independent of the Schur formula); $V_2$ is then the symmetric matrix solving $V_2\Psi_0=-\nabla V_{\rm eff}|_{V_2=0}$ and $(V_2+N)x_k=0$ for a rational $x_k\perp(b-N\Psi_0)$ (R67's surjectivity argument), so that the point is critical and $\mathrm{Hess}V_{\rm eff}$ has a one-dimensional kernel. `C2.1-critical-point-*`: the joint gradient vanishes exactly. `C2.4-schur-equals-HessVeff-*`: Schur complement of the joint Hessian $=$ the $\epsilon$-expansion Hessian, exactly. `C2.1-inertia-*`: $\mathrm{In}(H)=(4,4,1)=(1,1,1)+(3,3,0)$ at $S_3$; $(3,5,1)=(0,1,1)+(3,4,0)$ in the tower. Break legs: `C2.1-inertia-break-psi-block-*` (the mean-field $\Psi$ block in place of $\mathrm{Hess}V_{\rm eff}$ miscounts: $(1,2,0)$, $(0,2,0)$); `C2.1-inertia-break-sign-tower` (sign of $H_{\rm aux}$ flipped, $(4,3,0)$: sum $\ne\mathrm{In}(H)$); at $S_3$ the sign leg is vacuous for the seed ($\mathrm{In}(H_{\rm aux})=(3,3,0)$ balanced) and stays an INFO line; it is complemented by the never-vacuous `C2.1-inertia-break-shift-S3/tower` ($H_{\rm eff}\to H_{\rm eff}+10^{-12}\mathbb 1$: inertia $(2,1,0)$ resp. $(1,1,0)$ with no zero, so the sum with $\mathrm{In}(H_{\rm aux})$ has no zero while $\mathrm{In}(H)$ has one; fails for every seed), two more PASS. `C2.2-zero-mode-*`: $\dim\ker H=1$ by exact rank and $(x_k,\Sigma_*'x_k)$, with $\Sigma_*'$ the first-order saddle shift of the $\epsilon$-expansion, is annihilated by $H$ exactly; break `C2.2-zero-mode-break-*`: $(x_k,0)$ is not.
- *C2.3 (not isospectral).* Random indefinite $\omega_1=\mathrm{diag}(\pm)$, $\omega_k=\omega_1^{\otimes k}$ on the symmetric coordinates: $\max|\operatorname{spec}(G^{-1}H)-\operatorname{spec}(\text{direct sum})|=0.34$ ($S_3$), $0.095$ (tower), both spectra with exactly one zero eigenvalue.
- *C3 (fold).* `C3-fold-regular`: two real rational fold points ($t_f=\tfrac65,-6$); $\det H=-H_{t\sigma}^2<0$ exactly, $H_{\sigma\sigma}=0$; $\det H=-H_{t\sigma}^2$ is an identity once $H_{\sigma\sigma}=0$ is imposed, so the content tested is the existence of real rational fold points with $H_{t\sigma}\ne0$, and inertia $(1,1)$ is inferred from $\det<0$, not computed. `C3-fold-Veff-diverges`: $|V''_{\rm eff}|$ on the real sheet at $|t-t_f|=10^{-2},10^{-4},10^{-6}$: $14.1$, $134$, $1334$.
- Not checked: the string vertices (finite model only); the exhaustion orders of Tables 1.1–1.2 (presentation facts, R17/R19/R26); the momentum-dependent mass-shell remark after (2.5) (conditional on $H_{\rm aux}(k)$ invertible; zeros of $\det H_{\rm aux}(k)$ at $k\ne0$ not examined).

## 4. Interpretation, the paper-level remark, the proposed ledger row (C4)

**Regime.** Finite cubic HS model, generic real symmetric tensors, any background (C1) and any background at which the auxiliary block is invertible (C2); at the string vertices, C1 and (2.2)–(2.4) hold with the same words (they use only the polynomial degree of the action and linear algebra), and the identification of $\mathrm{Hess}V_{\rm eff}$ with the nonpolynomial Hessian to the matched order is Conditional(PH1, PH5) through R1, R17, R19 (R65's scope). Excluded: the degenerate locus of R67 and the fold of 057, where $H_{\rm aux}$ is singular and the cubic Hessian is the only one defined. Not delivered: Task 22's ghost/antifield extension, nilpotency and the graded signs of the second variation (the record gives the field-level restriction of $\mathcal T=G^{-1}H$ at ghost number 2 in the symmetric grading; as R66's scope). The momentum-dependent mass-shell reading is conditional on $H_{\rm aux}(k)$ invertible (§2).

**Limits.** $g\to0$: $H_{\rm aux}\propto g^2\to0$, so $\mathrm{In}(H)$ jumps at $g=0$ (to $\mathrm{In}(V_2)+(0,0,\dim\mathcal S)$: the auxiliaries become flat directions) while $\mathrm{In}(H_{\rm eff})$ is continuous; the physical count is the difference $\mathrm{In}(H)-\mathrm{In}(H_{\rm aux})$, not $\mathrm{In}(H)$. One auxiliary: R65 (stated in C2.1). Tower truncated at $\Sigma_2$: Table 1.1 without $W_6$.

**What the manuscript can assert (agent-facing draft of the remark, one paragraph, for the science-writer).** Because the action is cubic, its second variation at any background is affine in that background: each block is a vertex contracted once with one background field, (1.1), Tables 1.1–1.2. Around any solution of the cubic equations of motion — a level-truncated tachyon vacuum with its auxiliaries, a critical point of a truncation such as record 059's — the fluctuation operator is therefore the generalised eigenproblem of one matrix built from $V_2,\dots,V_{k+2}$ and the background, with the kinetic pairing on the right: the quantities a level-truncation code already computes, with no dressed vertex, no $V_4^{-1}$, no Hessian of the effective potential. The joint operator is not the eliminated theory's operator, but it is congruent to its direct sum with the auxiliary block, so the two agree on what is basis-independent: the inertia (the count of negative and zero directions) and the zero modes; once momentum is restored, at momenta where $H_{\rm aux}(k)$ is invertible the mass shells of the cubic theory are those of $H_{\rm eff}(k)$, and whether $\det H_{\rm aux}(k)$ vanishes at some $k\ne0$ is open (propagating auxiliary modes), so such zeros are not excluded. The eliminated theory's counts are read off as $\mathrm{In}(H)-\mathrm{In}(H_{\rm aux})$ and $\ker H$, with $H_{\rm aux}$ in closed form — constant at the order at which each auxiliary enters ($-\tfrac{g^2}{12}V_4$, $-\tfrac{g^4}{360}\tilde M_3$), linear in $\Psi_0$ one order later (the dressed kernels). Conditions: the auxiliary block invertible (else the auxiliary is not eliminable and only the cubic operator exists — at the fold the cubic Hessian is regular while the eliminated theory's diverges); the kinetic pairing indefinite: the inertia and the kernel are what the two descriptions share; the mass shells are the kernels once momentum is restored, and the eigenvalues of neither operator are directly physical (the inertia of an indefinite-pairing form is not a stability count); and, for the identification with the nonpolynomial theory, the on-shell matchings R1, R17, R19 under PH1, PH5. Two corrections of expectations the remark should not repeat: the auxiliary blocks are not constant beyond their first order, and the pencil eigenvalues of the joint and of the eliminated operator differ.

**Proposed ledger row.** *R71 — Mean field II: the Hessian of the cubic action is affine in the background; fluctuation counts and zero modes from the low vertices only, for any number of auxiliaries [Proven; C2.3 Verified (finite model)].* Source: record 066 C1–C4, §1–§3. Scope: finite cubic HS model, generic real symmetric tensors; C1 for any cubic action (the exhaustion orders of Tables 1.1–1.2 are presentation facts of R17/R19 and R26's scheme B; the general-$k$ rule (1.6) for $k\ge3$); C2 wherever the joint auxiliary block is invertible (R67's locus and 057's fold excluded); at the vertices C1 and (2.2)–(2.4) hold verbatim, the identification with $S^{(n+2)}_{\rm eff}$ to the matched order as R65's scope (Conditional(PH1, PH5) through R1, R17, R19); the mass-shell reading of the kernel at momenta where $H_{\rm aux}(k)$ is invertible (auxiliary zeros at $k\ne0$: R68's open item). Verification: 2026-10-01 – exact/numerical check – `codes/verify-hessian-affine.py`, run 1: 30 PASS / 0 FAIL, seed 20261001 (exact rationals; inertia at 50 digits with exact rank; `C2.1-inertia-break-sign-S3` vacuous for the seed, INFO); orchestrator re-run `agent/scratch/hessian-affine-rerun-orchestrator-2026-10-01.log` identical; 2026-10-01 – critic review – `agent/reports/critic-066-20261001T034000.md`, all nodes hold, 1 major (momentum remark) and minors, mechanical. Fix pass 2026-10-01 – script break leg replaced (`C2.1-inertia-break-shift-*`, never vacuous): run 2, 32 PASS / 0 FAIL, `agent/scratch/hessian-affine-run2.log`. Statement: $H(\phi_0)=S^{(2)}+S^{(3)}(\phi_0,\cdot,\cdot)$; blocks (1.4) for $(\Psi,\Sigma_2)$ through $S_4$ ($\Psi\Psi$ exhausted at $n=4$, $\Sigma_2\Psi$ at $5$, $\Sigma_2\Sigma_2$ at $6$; no cubic monomial in $(\Psi,\Sigma_2)$ beyond $6$) and (1.5)–(1.6) for the tower ($\Sigma_k\Sigma_k=-2a_k\hat M_k(\Psi_0)$: constant at $2k$, $\Psi_0$-linear at $2k+1$, never $\Sigma$-dependent in scheme B; $\Sigma_k\Sigma_{k-1}$ at $2k$; $\Sigma_k\Psi$ at $2k,2k+1,2k+2$); fluctuation operator $G^{-1}H$, $G=\bigoplus\omega_k$ indefinite; congruence $H=L^\top(H_{\rm eff}\oplus H_{\rm aux})L$ for any number of auxiliaries, $\mathrm{In}(H)=\mathrm{In}(H_{\rm eff})+\mathrm{In}(H_{\rm aux})$, $\ker H=\{(x,\Sigma_*'x)\}$, $H_{\rm eff}=\mathrm{Hess}V_{\rm eff}$ on the saddle, pencil eigenvalues not shared (measured); at the fold of $S_4$ the joint Hessian is regular ($\det H=-H_{t\sigma}^2$, inertia $(1,1)$ in the one-field model) while $\mathrm{Hess}V_{\rm eff}$ diverges as $|t-t_f|^{-1/2}$. Corrects the expectation that the auxiliary blocks are constant beyond the order at which each auxiliary enters.

## Result

$$\boxed{\begin{aligned}&H(\phi_0)=S^{(2)}+S^{(3)}(\phi_0,\cdot,\cdot)\ \text{(affine; Tables 1.1–1.2, exhaustion orders as listed)};\qquad \mathcal T=G^{-1}H(\phi_0);\\ &\mathrm{In}(H)=\mathrm{In}(\mathrm{Hess}V_{\rm eff})+\mathrm{In}(H_{\rm aux}),\quad \ker H=\{(x,\Sigma_*'x):x\in\ker\mathrm{Hess}V_{\rm eff}\}\ \text{on the saddle, }H_{\rm aux}\text{ invertible; congruent, not isospectral.}\end{aligned}}$$
