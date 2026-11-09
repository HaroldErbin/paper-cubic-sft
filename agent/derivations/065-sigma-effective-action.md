# 065 — Integrating out $\Psi$: the classical $\Sigma$-only effective action

Brief: `agent/briefs/active-computator-sigma-effective-20261001T005500.md` (Task 18). Script: `codes/verify-sigma-effective.py`; log `agent/scratch/sigma-effective-run1.log`.

## Task and objective

**Literal task.** From R1's cubic action (and R17's quintic extension), eliminate $\Psi$ at tree level around $\Psi=0$ and obtain the classical $\Sigma$-only effective action $\Gamma_0[\Sigma]$, or establish why the elimination is trivial and what the nontrivial classical content is: the $\Sigma$-dependent kinetic operator $Q_\Sigma$, its kernel, the branch structure of the $\Psi$-equation at fixed $\Sigma$, $\Gamma_0$ on a nontrivial branch, and the equality of its stationary points with the joint critical points.

**Motivating objective.** Task 15 (mean field à la Weinberg): the classical counterpart of $\Gamma[\Sigma]$ and the operator whose $\operatorname{Tr}\log$ the one-loop term sees. Objective 2 of the close-out, read in the $\Sigma$ direction: whether the cubic theory has classical solutions the eliminated theory does not (060 C3 read it in the $\Psi$ direction).

## Conventions and assumptions

- $g\equiv g_s$. Physical ghost number, all classical fields even (the project conventions); conventions used: C1 (graded symmetry of $\omega_k$, for the $\omega$-symmetry of $Q_\Sigma$) and C4 (the $\ell_n$ normalisation, A2).
- **A1** Action coefficients of R1 verbatim, $S_2=\tfrac12V_2(\Psi^2)+\tfrac g{3!}V_3(\Psi^3)-\tfrac{g^2}{4!}V_4(\Sigma,\Sigma)+\tfrac{2g^2}{4!}V_4(\Sigma,\Psi^{\otimes2})$; at $S_3$ the R17 term $+\tfrac{g^3}{5!}V_5(\Sigma,\Sigma,\Psi)$. $V_n$ totally graded-symmetric multilinear forms; $V_4(\Sigma,\Sigma)$ is the bilinear form on $\mathrm{Sym}^2\mathcal H$ evaluated on $\Sigma$ twice.
- **A2** $V_2(A,B)=\omega(A,QB)$ and the $L_\infty$ normalisation $V_{n+1}(A_0,\dots,A_n)=\omega(A_0,\ell_n(A_1,\dots,A_n))$ (conventions **C4**, `knowledge/conventions.md`; first stated in 060 A4). $\ell_3(\Sigma,\cdot)$ denotes the linear extension of $\ell_3(A,B,\cdot)$ to $\Sigma\in\mathrm{Sym}^2\mathcal H$.
- **A3** Finite model (057 A1, 060 A1–A2): $\mathcal H=\mathbb R^N$, fields even, $\omega=\mathbb 1$ (so $Q=V_2$ as a matrix), $V_n$ generic real symmetric tensors (rational in the script), $\Sigma\in\mathrm{Sym}^2\mathcal H$ with $V_4$ invertible there. No $L_\infty$ relation holds in this model; the nilpotency statements of C2 are made in the $L_\infty$ model of 060 §2 or cited.
- **A4** String scope of the linear-algebra statements: Siegel gauge $b_0^+\Psi=0$ at generic momentum, where $Q$ is invertible on the gauge-fixed space ($Q^{-1}=b_0^+/L_0^+$); the on-shell kernel of $Q$ is excluded. **Consequence (scope):** this excludes a constant (zero-momentum, translation-invariant) background $\Sigma$, such as the condensate of Task 15's mean field: at zero momentum $L_0^+=0$ on the massless sector, which lies in $\ker Q$ at every level, so the gap of $Q$ in (1.2) is zero, $\Sigma=0$ itself lies on $D$, and every statement below "$\ker Q_\Sigma=0$ below the gap" (C1, C1.2, C3.1, (4.4), §5) is void there; the tachyon ($L_0^+=-1$) only makes $Q$ indefinite and is not the obstruction. Transfer of finite-model statements to the string vertices is Conditional(PH1, PH5) as in 060.
- Hypotheses: none declared.

## Claim tree

- **C0** Step 0 verdict: the $\Psi$-equation of $S_2$ is $Q\Psi+\tfrac g2\ell_2(\Psi,\Psi)+\tfrac{g^2}{6}\ell_3(\Sigma,\Psi)=0$, i.e. $c_4=\tfrac16$ in the $V_4$-form normalisation ($=\tfrac13$ of the $\ell_3$-part $\tfrac{g^2}2\ell_3(\Psi_*,\Psi_*,\cdot)$ of $Q_{\Psi_*}$ at the saddle, 060 C2.1: the two numbers of the plan's cards are the same coefficient in two normalisations). $\Psi=0$ solves it for every $\Sigma$ (no term of $S_2$ is linear in $\Psi$), so the tree-level elimination around $\Psi=0$ is trivial at $S_2$: $\Gamma_0[\Sigma]=-\tfrac{g^2}{4!}V_4(\Sigma,\Sigma)$, stationary at $\Sigma=0$ only. At $S_3$ the R17 term is a $\Psi$-tadpole $\tfrac{g^3}{5!}V_5(\Sigma,\Sigma,\cdot)$: $\Psi=0$ solves the $\Psi$-equation only on the quadric cone $\{V_5(\Sigma,\Sigma,\cdot)=0\}$, and the elimination around $\Psi=0$ is nontrivial (C4). [by C0.1, C0.2]
  - **C0.1** $c_4=\tfrac16$; equation (0.2). [by A1, A2; eq. (0.1)–(0.2)] [check: C0.1-c4]
  - **C0.2** $\Psi=0$ solves (0.2) for all $\Sigma$; at $S_3$ it solves (0.3) iff $V_5(\Sigma,\Sigma,\cdot)=0$. [by C0.1; eqs (0.2)–(0.3)] [check: C0.2-trivial, C0.2-S3-source]
- **C1** $Q_\Sigma:=Q+\tfrac{g^2}6\ell_3(\Sigma,\cdot)$ is the $\Psi$-Hessian of $S_2$ and $S_3$ at $\Psi=0$, $\omega$-symmetric; $\ker Q_\Sigma=0$ for $|g^2\Sigma|$ below the gap of $Q$ (A4), and $\ker Q_\Sigma\ne0$ exactly on the hypersurface $D=\{\det Q_\Sigma=0\}$, $g$-independent in $s=g^2\Sigma$, so $\Sigma=O(g^{-2})$ on $D$. [by C1.1–C1.3]
  - **C1.1** Hessian (1.1) and symmetry. [by A1, A2, C1 of the conventions ledger, R58; eq. (1.1)] [check: C1.1-hess]
  - **C1.2** Neumann bound (1.2), hypersurface (1.3), scaling; $D$ nonempty (explicit real point). [by A4, C1.1; eqs (1.2)–(1.3)] [check: C1.2-neumann, C1.2-D]
  - **C1.3** At $\Sigma=\Psi_*^{\otimes2}$: $Q_\Sigma$ is $Q_{\Psi_*}$ without the $\ell_2$ term and with one third of the $\ell_3$ term. [by C1.1, 060 C2.1 (critic-accepted, fix pass pending); §1]
- **C2** $Q_\Sigma^2=-\tfrac{g^2}6[\ell_3(Q^{(2)}\Sigma,\cdot)+\mathrm{Jac}_\Sigma]+\tfrac{g^4}{36}\ell_3(\Sigma,\ell_3(\Sigma,\cdot))$ (1.4)–(1.5): not nilpotent for a generic $\Sigma$, nor for a $Q$-closed $\Sigma$ unless the Jacobiator of $\ell_2$ vanishes on it (nonzero in the model, check C2-g2 $Q$-closed leg, and at the saddle by 060 C2.4), nor when the $O(g^2)$ term vanishes unless also $\ell_3(\Sigma,\cdot)^2=0$; not nilpotent at the saddle (060 C2). [by C1.1, 060 C2.3–C2.4; cited: Zwiebach1993 (4.112) for the $n=3$ relation; eqs (1.4)–(1.5)] [check: C2-g2, C2-g4 ($L_\infty$ model of 060)]
- **C3** Branch theorem (finite model exact; string Conditional(PH1, PH5) with A4): a branch of $\{\mathcal E_2=0\}$ through $(0,\Sigma)$ other than the trivial one exists iff $\ker Q_\Sigma\ne0$; "only if" by the IFT (2.1); "if" for corank one with $V_3(\chi^3)\ne0$ by Lyapunov–Schmidt (2.2)–(2.5), transcritical, $\Psi_*(\Sigma)=-\tfrac g3\tfrac{V_4(\Sigma-\Sigma_0,\chi,\chi)}{V_3(\chi^3)}\chi+O(\delta\Sigma^2)$; at $\Sigma_0$ exactly, $\Psi=0$ is a double root and no small nonzero solution exists (nonlinear caveat); field scales $\Sigma=O(g^{-2})$, $\Psi=O(g^{-1})$; $D$ is the $\Psi$-block dual of 060 C3's $\det K_\Psi=0$ (the two diagonal-block degeneracies of the joint Hessian, 060 C1.7). [by C3.1–C3.3]
  - **C3.1** Isolation off $D$ (2.1). [by C1.2; IFT] [check: C3-iso]
  - **C3.2** Transcritical branch (2.5) and the caveat. [by C1.2, C3.1; eqs (2.2)–(2.5)] [check: C3-branch, C3-double, C3-caveat]
  - **C3.3** Scales and duality with 060 C3. [by C1.2, C3.2, 060 C1.7, 060 C3; §2]
- **C4** $\Gamma_0$: on any branch of $S_2$, $\Gamma_0[\Sigma]=-\tfrac{g^2}{24}V_4(\Sigma,\Sigma)-\tfrac g{12}V_3(\Psi_*(\Sigma)^3)$ exactly (4.1); on the transcritical branch $\Gamma_0-\Gamma_0^{\rm triv}=\tfrac{g^4}{324}V_4(\delta\Sigma,\chi,\chi)^3/V_3(\chi^3)^2+O(\delta\Sigma^4)$ (4.2); at $S_3$ around $\Psi=0$, $\Gamma_0=-\tfrac{g^2}{24}V_4(\Sigma^2)-\tfrac{g^6}{28800}j_\Sigma^\top Q_\Sigma^{-1}j_\Sigma+O(g^{10})$ (4.3)–(4.4), the $\Psi$-exchange between two $V_5$ tadpoles. [by C4.1–C4.2]
  - **C4.1** (4.1)–(4.2). [by A1, C3.2; Euler identity, eqs (4.1)–(4.2)] [check: C4-exact, C4-leading]
  - **C4.2** (4.3)–(4.4). [by C0.2, C1.2; eqs (4.3)–(4.4)] [check: C4-S3]
- **C5** Envelope identity $d\Gamma_0=\partial_\Sigma S\vert_{\Psi_*(\Sigma)}$ (4.5): the stationary points of $\Gamma_0$ on a branch are the joint critical points of $S$ on it; at $S_2$ these are $(\Psi_c,\Psi_c^{\otimes2})$ with $dV^{(4)}_{\rm eff}(\Psi_c)=0$ (4.6), the same points the $\Sigma$-elimination sees; neither elimination misses a joint critical point at $S_2$ generically, i.e. off $\{\det K_{\Psi_c}=0\}$ for the $\Sigma$-elimination (here $K=V_4$, invertible) and off $\{\det(Q_{\Sigma_c}+g\ell_2(\Psi_c,\cdot))=0\}$ (the $\Psi$-Hessian at $\Psi_c$, not $D$) for the $\Psi$-elimination: a codimension-one condition on the finite joint critical set. [by C0.1, C3, R1; eqs (4.5)–(4.6)] [check: C5-joint, C5-envelope]
- **C6** Finite-model instance (§4): explicit $\Sigma_0\in D$, the branch and its slope, isolation off $D$, (4.1)–(4.2), (4.4) exactly, the critical-point equality with the $c_4$ break leg; nilpotency failure in the $L_\infty$ model. [by check: C1.2-D, C3-iso, C3-double, C3-branch, C4-exact, C4-leading, C4-S3, C5-joint, C5-envelope, C2-g2, C2-g4] (finite model)

Open gaps: none
Hypotheses in force: none in the finite model; transfer of C1.2, C2 (nonvanishing at the string saddle, from 060 C2.4), C3, C4.2 ((4.3)–(4.4) use $Q_\Sigma^{-1}$ and (1.2)) and C5 to the string vertices is Conditional(PH1, PH5) with A4 (Siegel gauge, generic momentum; zero-momentum backgrounds excluded), as in 060

## 0. The $\Psi$-equation and the Step 0 verdict (C0)

\subsection*{Setup}
A1, A2. $\ell_2(\Psi,\Psi)$, $\ell_3(\Sigma,\Psi)$ as in A2; $j_\Sigma:=V_5(\Sigma,\Sigma,\cdot)\in\mathcal H^*$ and $\omega^{-1}j_\Sigma$ its vector (equivalently $\ell_4(\Sigma,\Sigma)$, the linear extension of $\ell_4$ to $\mathrm{Sym}^2\otimes\mathrm{Sym}^2$).

\subsection*{Derivation}
Variation of $S_2$ with respect to $\Psi$, term by term ($V_n$ totally symmetric, fields even):
$$
\begin{aligned}
\delta\big[\tfrac12V_2(\Psi,\Psi)\big]&=V_2(\delta\Psi,\Psi)=\omega(\delta\Psi,Q\Psi),\\
\delta\big[\tfrac g{3!}V_3(\Psi^3)\big]&=\tfrac g2V_3(\delta\Psi,\Psi,\Psi)=\omega\big(\delta\Psi,\tfrac g2\ell_2(\Psi,\Psi)\big),\\
\delta\big[\tfrac{2g^2}{4!}V_4(\Sigma,\Psi\otimes\Psi)\big]&=\tfrac{g^2}{12}\cdot2\,V_4(\Sigma,\delta\Psi,\Psi)=\omega\big(\delta\Psi,\tfrac{g^2}6\ell_3(\Sigma,\Psi)\big).
\end{aligned}\tag{0.1}
$$
Hence the $\Psi$-equation of $S_2$ and its $S_3$ extension:
$$
\mathcal E_2(\Psi;\Sigma):=Q\Psi+\tfrac g2\ell_2(\Psi,\Psi)+\tfrac{g^2}6\ell_3(\Sigma,\Psi)=0,\qquad c_4=\tfrac16,\tag{0.2}
$$
$$
\mathcal E_3(\Psi;\Sigma):=\mathcal E_2(\Psi;\Sigma)+\tfrac{g^3}{5!}\,\omega^{-1}j_\Sigma=0 .\tag{0.3}
$$
At $\Psi=0$: $\mathcal E_2(0;\Sigma)=0$ identically in $\Sigma$; $\mathcal E_3(0;\Sigma)=\tfrac{g^3}{5!}\omega^{-1}j_\Sigma$, zero iff $V_5(\Sigma,\Sigma,\cdot)=0$ (a quadric cone in $\mathrm{Sym}^2\mathcal H$, generically a proper subset).

Tree-level elimination around $\Psi=0$ at $S_2$: $\Gamma_0[\Sigma]=S_2[0,\Sigma]=-\tfrac{g^2}{4!}V_4(\Sigma,\Sigma)$, a nondegenerate quadratic form (A3: $V_4$ invertible on $\mathrm{Sym}^2$; for the string, on the quotient by $\ker V_4$), stationary only at $\Sigma=0$. There is no tree diagram with only $\Sigma$ external legs beyond the quadratic term: $\Sigma$ couples through $V_4(\Sigma,\Psi,\Psi)$ only, and a $\Psi$-line must end on a $\Psi$-tadpole, which $S_2$ does not have.

\subsection*{Commentary}
- (0.1), third line: $V_4(\Sigma,\Psi\otimes\Psi)$ is quadratic in $\Psi$, the factor $2$ is the derivative of the square; $\tfrac{2}{4!}\cdot2=\tfrac16$. Cross-check against 060 C2.1: the $\Psi$-block of the Hessian at $\Sigma_0$ is $\tfrac{g^2}6V_4(\Sigma_0,\cdot,\cdot)$, the second derivative of $\tfrac{g^2}{12}V_4(\Sigma_0,\Psi,\Psi)$; at the saddle $\Sigma_0=P_0$ this is one third of $\tfrac{g^2}2V_4(P_0,\cdot,\cdot)=\mathrm{Hess}\,\tfrac{g^2}{4!}V_4(\Psi^4)$. So "$\tfrac13$" (the ratio to the $\ell_3$ part of $Q_{\Psi_*}$, i.e. the coefficient of $L_3=\tfrac12\ell_3$ in 060's notation) and "$\tfrac16$" (the coefficient of $V_4(\Sigma,\cdot,\cdot)$, equivalently of $\ell_3(\Sigma,\cdot)$) are the same number in two normalisations; the plan's cards do not disagree.
- (0.3): $V_5(\Sigma,\Sigma,\Psi)$ is linear in $\Psi$; its variation is the pure source $j_\Sigma$. This is the only place in $S_3$ where a $\Psi$-tadpole in a $\Sigma$-background arises.

\subsection*{Result}
$$\boxed{c_4=\tfrac16;\quad \Psi=0\ \text{solves (0.2) for every }\Sigma;\quad \Gamma_0^{S_2}[\Sigma]=-\tfrac{g^2}{4!}V_4(\Sigma,\Sigma)\ \text{(trivial elimination)};\quad \mathcal E_3(0;\Sigma)=\tfrac{g^3}{5!}\omega^{-1}V_5(\Sigma,\Sigma,\cdot)\neq0\ \text{generically.}}$$
The nontrivial classical content at $S_2$ sits elsewhere: in the $\Sigma$-dependence of the $\Psi$-Hessian $Q_\Sigma$ (§1–§2) and in the nontrivial branches it seeds (§3–§4); at $S_3$, in the $\Psi$-exchange induced by the tadpole (§4, (4.4)).

\subsection*{Verification}
Checks C0.1-c4 (symbolic gradient of $S_2$ in the finite model against (0.2), break: $c_4\to\tfrac13$ fails), C0.2-trivial ($\mathcal E_2(0;\Sigma)\equiv0$ as a polynomial in $\Sigma$), C0.2-S3-source ($\mathcal E_3(0;\Sigma)=\tfrac{g^3}{120}j_\Sigma$ symbolically, nonzero at a random $\Sigma$).

## 1. The $\Sigma$-dependent kinetic operator $Q_\Sigma$ (C1, C2)

\subsection*{Setup}
A1–A4. $Q_\Sigma:=Q+\tfrac{g^2}6\ell_3(\Sigma,\cdot)$, i.e. $\omega(A,Q_\Sigma B)=\omega(A,QB)+\tfrac{g^2}6V_4(\Sigma,A,B)$. $Q^{(2)}:=Q\otimes1+1\otimes Q$ on $\mathrm{Sym}^2\mathcal H$. $\mathrm{Jac}_\Sigma(C)$: the linear extension to $\Sigma$ of $\mathrm{Jac}(A,B,C)=\ell_2(\ell_2(A,B),C)+\ell_2(\ell_2(B,C),A)+\ell_2(\ell_2(C,A),B)$ (even inputs). Scaled variable $s=g^2\Sigma$.

\subsection*{Derivation}
*Hessian (C1.1).* The second $\Psi$-derivative of $S_2$ at $\Psi=0$ is read off (0.1): $\tfrac12V_2$ gives $\omega(\cdot,Q\cdot)$, $\tfrac g{3!}V_3(\Psi^3)$ gives $gV_3(\Psi,\cdot,\cdot)\vert_{\Psi=0}=0$, $\tfrac{g^2}{12}V_4(\Sigma,\Psi,\Psi)$ gives $\tfrac{g^2}6V_4(\Sigma,\cdot,\cdot)$:
$$
\partial_\Psi^2S_2\big\vert_{\Psi=0}=\omega(\cdot,Q_\Sigma\,\cdot),\qquad \partial_\Psi^2S_3\big\vert_{\Psi=0}=\partial_\Psi^2S_2\big\vert_{\Psi=0}\ \ (\text{the }V_5\text{ term is linear in }\Psi).\tag{1.1}
$$
Equivalently $Q_\Sigma=D_\Psi\mathcal E_2(0;\Sigma)$, the linearisation of (0.2) at the trivial solution. *Symmetry:* $\omega(A,QB)$ has the exchange sign of C1 ($Q$ is $\omega$-self-adjoint up to the graded sign), and $V_4(\Sigma,A,B)$ is graded symmetric in $(A,B)$ by total graded symmetry of $V_4$ (R58); the two terms carry the same sign on the even classical sector, so $\omega(\cdot,Q_\Sigma\cdot)$ is a (graded) symmetric bilinear form — in the finite model a symmetric matrix $V_2+\tfrac{g^2}6V_4(\Sigma)$.

*Kernel (C1.2).* $\ker Q_\Sigma=\{\chi:Q\chi=-\tfrac{g^2}6\ell_3(\Sigma,\chi)\}$. Under A4, $Q$ is invertible on the gauge-fixed space with $\|Q^{-1}\|=1/\min|L_0^+|$ (Siegel gauge, generic momentum; in the finite model $\|V_2^{-1}\|$), so
$$
\|\tfrac{g^2}6\ell_3(\Sigma,\cdot)\|<\|Q^{-1}\|^{-1}\ \Longrightarrow\ Q_\Sigma=Q\big(1+\tfrac{g^2}6Q^{-1}\ell_3(\Sigma,\cdot)\big)\ \text{invertible (Neumann series)},\ \ker Q_\Sigma=0 .\tag{1.2}
$$
Hence no kernel for $|s|=|g^2\Sigma|$ below the gap. The kernel is nonempty exactly on
$$
D:=\{\Sigma:\ \det Q_\Sigma=0\}=\{\Sigma:\ \det\big(Q+\tfrac16\ell_3(s,\cdot)\big)=0\},\qquad s=g^2\Sigma,\tag{1.3}
$$
a hypersurface in $s$-space (a polynomial of degree $\dim\mathcal H$ in $s$ in the finite model; for the string an infinite determinant, treated at finite level). $D$ is $g$-independent in $s$: every point of $D$ has $\Sigma=O(g^{-2})$. This is the scaling of the $\Sigma$-saddle at the tachyon vacuum ($\Sigma_*=\Psi_*^{\otimes2}$, $\Psi_*=O(1/g)$) and of 060 C3's locus: the whole action obeys $S=g^{-2}\hat S(g\Psi,g^2\Sigma)$ exactly (each $V_n$ term carries $g^{n-2}$ and $n$ legs, $\Sigma$ counting two), so nothing about $D$ is perturbative in $g$.

*At the saddle (C1.3).* For $\Sigma=P_*:=\Psi_*\otimes\Psi_*$, $Q_{P_*}=Q+\tfrac{g^2}6\ell_3(\Psi_*,\Psi_*,\cdot)$, while the shifted BRST operator of the quartic-truncated theory is $Q_{\Psi_*}=Q+g\ell_2(\Psi_*,\cdot)+\tfrac{g^2}2\ell_3(\Psi_*,\Psi_*,\cdot)$: $Q_{P_*}$ lacks the $\ell_2$ term (it is the Hessian at $\Psi=0$, not at $\Psi_*$) and carries one third of the $\ell_3$ term (060 C2.1, critic-accepted, fix pass pending). The operator Task 15 needs at the mean-field saddle is $Q_\Sigma$ at $\Sigma=P_*$ only if the mean field is taken around $\Psi=0$; the Hessian at the joint saddle $(\Psi_*,P_*)$ is 060 C2's $Q^{\rm cub}$, and the full $Q_{\Psi_*}$ is recovered only with the $\delta\Sigma$ exchange (060 C2).

*Nilpotency (C2).* With $M_\Sigma:=\ell_3(\Sigma,\cdot)$,
$$
Q_\Sigma^2=Q^2+\tfrac{g^2}6\{Q,M_\Sigma\}+\tfrac{g^4}{36}M_\Sigma^2=\tfrac{g^2}6\{Q,M_\Sigma\}+\tfrac{g^4}{36}M_\Sigma^2 .\tag{1.4}
$$
The $n=3$ $L_\infty$ relation on even inputs (Zwiebach 1993 (4.112) on the classical sector; 060 C2.3–C2.4) reads $Q\ell_3(A,B,C)+\ell_3(QA,B,C)+\ell_3(A,QB,C)+\ell_3(A,B,QC)=-\mathrm{Jac}(A,B,C)$ up to the convention-dependent overall sign of the Jacobiator; extended linearly to $\Sigma$:
$$
\{Q,M_\Sigma\}(C)=Q\ell_3(\Sigma,C)+\ell_3(\Sigma,QC)=-\ell_3(Q^{(2)}\Sigma,C)-\mathrm{Jac}_\Sigma(C).\tag{1.5}
$$
Consequently: (i) for a generic $\Sigma$ (not $Q^{(2)}$-closed) the $O(g^2)$ term of (1.4) contains $\ell_3(Q^{(2)}\Sigma,\cdot)\ne0$; (ii) for $Q^{(2)}\Sigma=0$ it reduces to $-\mathrm{Jac}_\Sigma$, which vanishes iff $\ell_2$ satisfies the Jacobi identity on $\Sigma$ — nonzero in the model (C2-g2, $Q$-closed leg) and at the saddle by 060 C2.4 ($\mathcal L(P_0)\neq0$, $\ker\mathcal L$ a proper subspace); by (1.5) with $Q^{(2)}\Sigma=0$, $\mathrm{Jac}_\Sigma=-\{Q,\ell_3(\Sigma,\cdot)\}$ is nonzero exactly when $\ell_3(\Sigma,\cdot)$ fails to be a chain map, which $\ell_3\ne0$ alone does not imply; (iii) the $O(g^4)$ term $M_\Sigma^2=\ell_3(\Sigma,\ell_3(\Sigma,\cdot))$ is constrained by no $L_\infty$ relation (those involve $\ell_3\circ\ell_3$ only together with $\ell_2\circ\ell_4$ and $Q\circ\ell_5$ at $n=5$, with different slot structure), and is nonzero in the model (check C2-g4). Only if $\mathrm{Jac}_\Sigma=0$, $Q^{(2)}\Sigma=0$ and $M_\Sigma^2=0$ simultaneously is $Q_\Sigma$ nilpotent: a proper subvariety of $\mathrm{Sym}^2\mathcal H$ containing $\Sigma=0$. At the saddle $P_*$ it fails already at $O(g^2)$ (060 C2, "$c=\tfrac13$ not nilpotent"); the $\ell_2$ term missing from $Q_{P_*}$ is what makes $Q_{\Psi_*}^2=0$ at MC points (060 C2.3).

\subsection*{Commentary}
- (1.2): standard Neumann bound; for the string the operator norm of $\ell_3(\Sigma,\cdot)$ on the Siegel-gauge space at fixed momentum is finite at every level (the vertex is a bounded map between level-truncated spaces), the all-level statement is A4/PH1 scope.
- (1.3): the polynomial $\det(Q+\tfrac16\ell_3(s,\cdot))$ in $s$ is not identically zero (its value at $s=0$ is $\det Q\ne0$ under A4), so $D$ is a proper hypersurface, nonempty over $\mathbb C$ and, in the model, over $\mathbb R$ (an explicit real point is built in §4 by a linear construction: prescribe the kernel vector and solve for $\Sigma$).
- (1.5): the sign of the Jacobiator relative to the $Q$-terms depends on the suspension convention and is immaterial for the claim, which is the nonvanishing of the right-hand side.
- Where the brief's phrase "only if $V_4(\Sigma,\cdot,\cdot)$ is $Q$-closed and squares to zero" is made precise: $Q$-closed must be read as $\ell_3(Q^{(2)}\Sigma,\cdot)+\mathrm{Jac}_\Sigma=0$ (the $\ell_3$ image of a $Q$-closed $\Sigma$ is not $Q$-closed in a non-DGLA), and "squares to zero" is $M_\Sigma^2=0$.

\subsection*{Result}
$$\boxed{Q_\Sigma=Q+\tfrac{g^2}6\ell_3(\Sigma,\cdot)=\partial^2_\Psi S\big\vert_{\Psi=0},\ \ \omega\text{-symmetric};\quad \ker Q_\Sigma\neq0\iff\Sigma\in D=\{\det(Q+\tfrac16\ell_3(g^2\Sigma,\cdot))=0\},\ \Sigma=O(g^{-2});\quad Q_\Sigma^2=-\tfrac{g^2}6\big[\ell_3(Q^{(2)}\Sigma,\cdot)+\mathrm{Jac}_\Sigma\big]+\tfrac{g^4}{36}\ell_3(\Sigma,\ell_3(\Sigma,\cdot))\neq0\ \text{generically.}}$$

\subsection*{Verification}
C1.1-hess (finite model: $\partial^2_\Psi S_2\vert_0=V_2+\tfrac{g^2}6V_4(\Sigma)$ symbolically, symmetric; break $\tfrac16\to\tfrac13$ fails); C1.2-neumann (random $\Sigma$, $g$ small: $\det Q_\Sigma\ne0$ and $\det Q_\Sigma\vert_{s}$ is $g$-independent in $s$); C1.2-D (the constructed $\Sigma_0$ of §4 lies on $D$ exactly, $Q_{\Sigma_0}\chi=0$). C2-g2, C2-g4 ($L_\infty$ model of 060 part 2, `LinfModel(21,[0,0,0,1,1],(1,),"T3")`, $Q_\Sigma=T_0+\tfrac{g^2}3T_2(\Sigma)$ on the retract, $T_2=\tfrac12\ell_3$: $\{T_0,T_2(\Sigma)\}\ne0$ for a random symmetric $\Sigma$ and for $\Sigma=\psi\otimes\psi$ with $T_0\psi=0$; $T_2(\Sigma)^2\ne0$; control: $T_0^2=0$ to $10^{-14}$, so the same code would report nilpotency if it held).

## 2. Branch structure of the $\Psi$-equation at fixed $\Sigma$ (C3)

\subsection*{Setup}
A1–A4, $S_2$. $\mathcal E_2(\Psi;\Sigma)$ of (0.2), a polynomial map quadratic in $\Psi$ and linear in $\Sigma$. Joint solution set $\mathcal Z=\{(\Psi,\Sigma):\mathcal E_2=0\}$; trivial branch $\mathcal Z_0=\{0\}\times\mathrm{Sym}^2\mathcal H\subset\mathcal Z$. Corank-one point $\Sigma_0\in D$ with $\ker Q_{\Sigma_0}=\mathbb R\chi$; by $\omega$-symmetry $\operatorname{coker}$ is spanned by $\omega(\chi,\cdot)$, and $\Pi$ denotes the projector on $\operatorname{im}Q_{\Sigma_0}=\{v:\omega(\chi,v)=0\}$ (finite model; $\omega(\chi,\chi)\ne0$ is not needed, a Euclidean complement is used for $w$ below). $\delta\Sigma:=\Sigma-\Sigma_0$.

\subsection*{Derivation}
*Only if (isolation).* $D_\Psi\mathcal E_2(0;\Sigma)=Q_\Sigma$ (1.1). If $\ker Q_\Sigma=0$, the implicit function theorem applied to $\mathcal E_2$ at $(0,\Sigma)$ gives a neighbourhood $U\ni(0,\Sigma)$ in which $\mathcal Z\cap U=\mathcal Z_0\cap U$: the trivial solution is isolated at fixed $\Sigma$ and no nontrivial branch passes through $(0,\Sigma)$. (Finite model: $\mathcal E_2$ polynomial, IFT exact. String: $Q_\Sigma$ invertible on the Siegel-gauge space under A4 for $|s|$ below the gap by (1.2), and off $D$ in general; the analytic IFT needs bounded inverses, PH1 scope.)
$$
\ker Q_\Sigma=0\ \Longrightarrow\ \{\Psi:\ \mathcal E_2(\Psi;\Sigma)=0,\ |\Psi|<r\}=\{0\}\ \text{for some }r>0.\tag{2.1}
$$
Nonzero solutions at such a $\Sigma$ exist ($\mathcal E_2=0$ is $\dim\mathcal H$ quadrics in $\dim\mathcal H$ unknowns) but at finite distance $|\Psi|\ge r$; by the exact scaling $r=O(1/g)$.

*If (Lyapunov–Schmidt at a corank-one point).* Write $\Psi=\epsilon\chi+w$, $w$ in a fixed complement of $\mathbb R\chi$, and split (0.2) by $\Pi$ and $1-\Pi$ at $\Sigma=\Sigma_0+\delta\Sigma$:
$$
\Pi:\quad Q_{\Sigma_0}w+\Pi\big[\tfrac{g^2}6\ell_3(\delta\Sigma,\epsilon\chi+w)+\tfrac g2\ell_2(\epsilon\chi+w,\epsilon\chi+w)\big]=0,\tag{2.2}
$$
$$
1-\Pi:\quad \phi(\epsilon,\delta\Sigma):=\tfrac{g^2}6V_4(\delta\Sigma,\chi,\epsilon\chi+w)+\tfrac g2V_3(\chi,\epsilon\chi+w,\epsilon\chi+w)=0 .\tag{2.3}
$$
(2.2) is solved for $w=w(\epsilon,\delta\Sigma)$ by the IFT ($Q_{\Sigma_0}$ invertible from the complement onto $\operatorname{im}Q_{\Sigma_0}$), with $w=O(\epsilon^2+\epsilon|\delta\Sigma|)$ and $w(0,\delta\Sigma)=0$. Inserting in (2.3):
$$
\phi(\epsilon,\delta\Sigma)=\epsilon\Big[\tfrac{g^2}6V_4(\delta\Sigma,\chi,\chi)+\tfrac g2\epsilon V_3(\chi,\chi,\chi)+O(\epsilon^2,\epsilon|\delta\Sigma|,|\delta\Sigma|^2)\Big].\tag{2.4}
$$
The factor $\epsilon$ is the trivial branch. The bracket $=0$ is solved for $\epsilon$ as a function of $\delta\Sigma$ by the IFT when $V_3(\chi^3)\ne0$:
$$
\epsilon(\delta\Sigma)=-\frac g3\,\frac{V_4(\delta\Sigma,\chi,\chi)}{V_3(\chi,\chi,\chi)}+O(|\delta\Sigma|^2),\qquad
\Psi_*(\Sigma)=\epsilon(\delta\Sigma)\,\chi+O(|\delta\Sigma|^2).\tag{2.5}
$$
This is a nontrivial branch, a graph over a neighbourhood of $\Sigma_0$ in $\Sigma$-space, meeting $\mathcal Z_0$ along $D$ (where $V_4(\delta\Sigma,\chi,\chi)=0$ to first order is the tangent of $D$ at $\Sigma_0$: $d\det Q_\Sigma=\det{}'\cdot\tfrac{g^2}6V_4(\delta\Sigma,\chi,\chi)$ for corank one) — a transcritical crossing. Both branches have dimension $\dim\mathrm{Sym}^2\mathcal H$.

*Nonlinear caveat.* At $\delta\Sigma=0$ exactly, (2.4) reads $\epsilon^2[\tfrac g2V_3(\chi^3)+O(\epsilon)]=0$: the only small solution is $\epsilon=0$ (a double root: $\Psi=0$ has multiplicity two at $\Sigma_0$). Small nonzero solutions at fixed $\Sigma_0\in D$ exist only if $V_3(\chi,\chi,\chi)=0$ (then the next order of (2.4) decides, and a genuine one-parameter family at fixed $\Sigma$ needs all orders to vanish: a flat direction, non-generic). So "a nontrivial branch exists iff $\ker Q_\Sigma\ne0$" is exact for the joint solution set (branches through $(0,\Sigma)$), and the linear kernel alone does not produce a nonzero $\Psi$ at that very $\Sigma$.

*Scales and duality.* On the nontrivial branch near $D$: $\Sigma_0=O(g^{-2})$ by (1.3), and by (2.5) $\Psi_*=O(g\,\delta\Sigma)=O(g^{-1}\,\delta s)$, $\delta s=g^2\delta\Sigma$: the tachyon-vacuum scaling $\Psi=O(1/g)$ with a small prefactor $\delta s$ near $D$. Dual statement: 060 C3 eliminates $\Sigma$ and finds $\Sigma$ non-eliminable where the $\Sigma$-block $-\tfrac{g^2}{12}K_\Psi$ is singular ($S_3$ only, at $\Psi=O(1/g)$); here $\Psi$ is eliminated around $\Psi=0$ and is non-eliminable (the trivial branch is not isolated) where the $\Psi$-block $\omega Q_\Sigma$ is singular — already at $S_2$, since $Q_\Sigma$ depends on $\Sigma$ while $K=V_4$ does not depend on $\Psi$ at $S_2$. The two loci are the two diagonal-block degeneracies of the same joint Hessian (060 C1.7), and neither is a joint critical point by itself. 057's fold is a degeneracy of the $\Sigma$-equation's Jacobian along a nontrivial branch (at $S_4$); its $\Psi$-side analogue is the singular locus of $Q_\Sigma+g\ell_2(\Psi_*,\cdot)$ along the nontrivial branch (2.5), where two nontrivial solutions merge (not treated).

\subsection*{Commentary}
- (2.2)–(2.4): standard Lyapunov–Schmidt reduction; the corank-one hypothesis is generic on $D$ (corank two is codimension three in $\Sigma$-space for symmetric $Q_\Sigma$).
- (2.4): the terms $O(\epsilon^2)$ come from $\tfrac g2V_3(\chi,w,\cdot)$ and $\tfrac{g^2}6V_4(\delta\Sigma,\chi,w)$ with $w=O(\epsilon^2+\epsilon|\delta\Sigma|)$; they do not change the leading slope.
- (2.5) has the one-dimensional model $a(\Sigma)\psi+\tfrac g2b\psi^2=0$, $\psi_*=-2a/(gb)$, $a=\tfrac{g^2}6V_4(\delta\Sigma,\chi,\chi)$, $b=V_3(\chi^3)$.

\subsection*{Result}
$$\boxed{\text{Branch theorem: }\ \mathcal Z\ \text{has a branch through }(0,\Sigma)\text{ other than }\mathcal Z_0\iff\ker Q_\Sigma\neq0;\quad \Psi_*(\Sigma)=-\tfrac g3\tfrac{V_4(\Sigma-\Sigma_0,\chi,\chi)}{V_3(\chi^3)}\chi+O(|\Sigma-\Sigma_0|^2)\ \text{(corank one, }V_3(\chi^3)\ne0);\quad \Psi_*(\Sigma_0)=0.}$$
The "if" is proved for corank one with $V_3(\chi^3)\ne0$; the "only if" is the IFT. Finite model: exact. String: Conditional(PH1, PH5) with A4.

\subsection*{Verification}
C3-iso (a $\Sigma_{\rm off}\notin D$: all nonzero solutions of (0.2), computed exactly by resultants in the five-field model, are at distance $\ge r$ from $0$ with $r$ independent of the approach $\Sigma_{\rm off}+\lambda\delta\Sigma$, $\lambda\to0$); C3-branch (at $\Sigma_0+\lambda\delta\Sigma$, the nontrivial root nearest $0$ has norm $\propto\lambda$ with the slope of (2.5), relative error $O(\lambda)$; break: the slope with $\tfrac13\to\tfrac16$ fails); C3-double (at $\Sigma_0$ exactly, $\Psi=0$ is a double root of the resultant and no other root lies within $r$); C3-caveat ($V_3(\chi^3)\ne0$ at the instance).

## 3. $\Gamma_0$ on a nontrivial branch and the critical-point equality (C4, C5)

\subsection*{Setup}
A1–A4. A branch $\Psi_*(\Sigma)$: a smooth map on an open set of $\Sigma$-space with $\mathcal E(\Psi_*(\Sigma);\Sigma)=0$ ($\mathcal E=\mathcal E_2$ or $\mathcal E_3$). $\Gamma_0[\Sigma]:=S[\Psi_*(\Sigma),\Sigma]$. $j_\Sigma$ as in §0.

\subsection*{Derivation}
*Exact value on a branch at $S_2$ (C4).* $S_2$ is cubic in $\Psi$; Euler's identity for the homogeneous pieces $S^{(1)}=\tfrac12\omega(\Psi,Q_\Sigma\Psi)$ (degree 2) and $S^{(2)}=\tfrac g6V_3(\Psi^3)$ (degree 3) gives $\omega(\Psi,\partial_\Psi S)=2S^{(1)}+3S^{(2)}$, and on a branch $\partial_\Psi S=0$:
$$
S^{(1)}\big\vert_{\Psi_*}=-\tfrac32S^{(2)}\big\vert_{\Psi_*}\quad\Longrightarrow\quad
\Gamma_0[\Sigma]=-\tfrac{g^2}{24}V_4(\Sigma,\Sigma)-\tfrac g{12}\,V_3\big(\Psi_*(\Sigma)^{3}\big)\qquad\text{(exact, }S_2).\tag{4.1}
$$
On the trivial branch $\Psi_*=0$ and (4.1) is C0's $\Gamma_0^{\rm triv}$. On the transcritical branch (2.5) near $\Sigma_0\in D$:
$$
\Gamma_0-\Gamma_0^{\rm triv}=-\tfrac g{12}\,\epsilon^3V_3(\chi^3)+O(\delta\Sigma^4)
=\frac{g^4}{324}\,\frac{V_4(\delta\Sigma,\chi,\chi)^3}{V_3(\chi,\chi,\chi)^2}+O(|\delta\Sigma|^4),\tag{4.2}
$$
using $\epsilon^3=-\tfrac{g^3}{27}V_4(\delta\Sigma,\chi,\chi)^3/V_3(\chi^3)^3$. The next order needs $\epsilon$ to $O(\delta\Sigma^2)$ and $w$ to $O(\epsilon^2)$ from (2.2)–(2.4); it is not written in closed form here — (4.1) supersedes it (all orders once $\Psi_*$ is known), and the check compares (4.1) with the direct value and (4.2) with the $\lambda^3$ scaling. The difference (4.2) is cubic and sign-indefinite in $\delta\Sigma$: the two branches cross, neither dominates. Both $\Gamma_0$'s scale as $g^{-2}\hat\Gamma_0(s)$.

*Perturbative $\Gamma_0$ at $S_3$ around $\Psi=0$ (C4).* With the source (0.3), $\Psi=0$ is not a solution; the perturbative branch is $\Psi_*=\Psi_1+O(g^7)$, $\Psi_1=-\tfrac{g^3}{5!}Q_\Sigma^{-1}\omega^{-1}j_\Sigma$ (the $\ell_2$ term contributes at $O(g\cdot g^6)$). Since $\partial_\Psi S_3(\Psi_1)=\tfrac g2\ell_2(\Psi_1,\Psi_1)=O(g^7)$, the error of $S_3$ at $\Psi_1$ against the true branch value is $O(g^7)\cdot O(g^7)=O(g^{14})$, and
$$
\Gamma_0^{S_3}[\Sigma]=-\frac{g^2}{24}V_4(\Sigma,\Sigma)-\frac{g^6}{2\,(5!)^2}\;j_\Sigma^{\top}Q_\Sigma^{-1}j_\Sigma+\frac g6V_3(\Psi_1^3)+O(g^{14}),\qquad
j_\Sigma^\top Q_\Sigma^{-1}j_\Sigma:=V_5(\Sigma,\Sigma,Q_\Sigma^{-1}\omega^{-1}j_\Sigma),\tag{4.3}
$$
the Gaussian value $-\tfrac12jK^{-1}j$ of $\tfrac12\omega(\Psi,Q_\Sigma\Psi)+\tfrac{g^3}{5!}j_\Sigma(\Psi)$. Expanding $Q_\Sigma^{-1}=Q^{-1}-\tfrac{g^2}6Q^{-1}\ell_3(\Sigma,\cdot)Q^{-1}+\dots$ (valid below the gap, (1.2)), through $O(g^9)$:
$$
\Gamma_0^{S_3}=-\frac{g^2}{24}V_4(\Sigma^2)-\frac{g^6}{28800}\,V_5(\Sigma^2,Q^{-1}V_5(\Sigma^2,\cdot))+\frac{g^8}{172800}\,V_4\big(\Sigma,Q^{-1}V_5(\Sigma^2,\cdot),Q^{-1}V_5(\Sigma^2,\cdot)\big)+O(g^{10}).\tag{4.4}
$$
Diagrammatically: the $g^6$ term is the $\Psi$-propagator between two $V_5(\Sigma\Sigma\Psi)$ tadpoles (a $\Sigma^4$ contact term of the eliminated theory), the $g^8$ term inserts one $V_4(\Sigma\Psi\Psi)$ on that line, and so on — $\Gamma_0^{S_3}$ is the sum of tree diagrams with $\Sigma$ legs only, which exist at $S_3$ because $V_5(\Sigma,\Sigma,\Psi)$ is a $\Psi$-tadpole in a $\Sigma$ background. At $S_2$ there is no tadpole and the sum is the quadratic term alone (C0). These terms are $O(g^6)$ at fixed $\Sigma$, i.e. $O(g^{-2}s^4)$ in the scaled variable: the same order as everything else once $s=O(1)$.

*Critical-point equality (C5).* On any branch, differentiating $\Gamma_0[\Sigma]=S[\Psi_*(\Sigma),\Sigma]$:
$$
d\Gamma_0=\partial_\Psi S\big\vert_{\Psi_*}\cdot d\Psi_*+\partial_\Sigma S\big\vert_{\Psi_*}=\partial_\Sigma S\big(\Psi_*(\Sigma),\Sigma\big),\tag{4.5}
$$
since $\partial_\Psi S(\Psi_*(\Sigma),\Sigma)=0$ by definition of the branch (envelope identity; the mirror of 060's $dV_{\rm eff}=\partial_\Psi S\vert_{\Sigma_*(\Psi)}$). Hence $\Sigma_c$ is stationary for $\Gamma_0$ iff $(\Psi_*(\Sigma_c),\Sigma_c)$ is a joint critical point of $S$. Conversely a joint critical point $(\Psi_c,\Sigma_c)$ with $\Psi$-Hessian $Q_{\Sigma_c}+g\ell_2(\Psi_c,\cdot)$ invertible (the Hessian at $\Psi_c$, not $D$, which is the degeneracy at $\Psi=0$) lies on a unique local branch $\Psi_*(\Sigma)$ (IFT), and is a stationary point of that branch's $\Gamma_0$. The $\Sigma$-elimination (R1, 060 C1.2) sees the joint critical points with $\det K_{\Psi_c}\ne0$ ($\Sigma_c=\Sigma_*(\Psi_c)$); the $\Psi$-elimination those with invertible $\Psi$-Hessian. At $S_2$ the joint critical set is
$$
\Sigma_c=\Psi_c^{\otimes2},\qquad Q\Psi_c+\tfrac g2\ell_2(\Psi_c,\Psi_c)+\tfrac{g^2}6\ell_3(\Psi_c,\Psi_c,\Psi_c)=0\quad(\text{R1; the second equation is }dV^{(4)}_{\rm eff}=0),\tag{4.6}
$$
$\tfrac{g^2}6\ell_3(\Psi^{\otimes2},\Psi)$ being the derivative of $\tfrac{g^2}{24}V_4(\Psi^4)$ ($4/24=1/6$, the same $c_4$). Every such point with $\Psi_c\ne0$ and invertible $\Psi$-Hessian at $\Psi_c$ (generic: one polynomial condition on a finite set) is on a nontrivial branch, and the trivial branch's only stationary point $\Sigma=0$ is the joint critical point $(0,0)$. So: on the common domain, the stationary points of $\Gamma_0$ (nontrivial branches) and of $V_{\rm eff}$ are the same points $(\Psi_c,\Psi_c^{\otimes2})$; neither elimination has stationary points the other lacks, except where the respective Hessian block degenerates — $D$ for the $\Psi$-elimination (§2), $\det K_\Psi=0$ for the $\Sigma$-elimination (060 C3, $S_3$ only). Objective 2 in the $\Sigma$ direction: the cubic theory's classical solutions are the joint critical points, and the $\Sigma$-eliminated theory misses none of them at $S_2$ ($K=V_4$ invertible everywhere); the $\Psi$-eliminated theory misses none generically, namely off $\{\det(Q_{\Sigma_c}+g\ell_2(\Psi_c,\cdot))=0\}$, the degeneracy locus of the $\Psi$-Hessian at $\Psi_c$ (for $\Psi_c=0$, $\Sigma_c=0$ and this reduces to $\det Q\ne0$); $D$ plays no role at $\Psi_c\ne0$.

\subsection*{Commentary}
- (4.1): Euler's identity is exact because $S_2$ is polynomial in $\Psi$ with the $\Sigma$-dependence sitting in the quadratic piece; at $S_3$ the linear piece $\tfrac{g^3}{5!}j_\Sigma(\Psi)$ adds $-\tfrac12\cdot$ itself: $\Gamma_0^{S_3}=-\tfrac{g^2}{24}V_4(\Sigma^2)+\tfrac{g^3}{2\cdot5!}j_\Sigma(\Psi_*)-\tfrac g{12}V_3(\Psi_*^3)$, exact on any $S_3$ branch.
- (4.3)–(4.4): $\tfrac1{2\cdot120^2}=\tfrac1{28800}$; the $g^8$ coefficient is $\tfrac{1}{28800}\cdot\tfrac16=\tfrac1{172800}$ with the sign from $-(-\tfrac16)$.
- (4.5): the envelope identity needs only that $\Psi_*$ solves the $\Psi$-equation; no Hessian condition. The Hessian condition enters only to make the branch a graph.

\subsection*{Result}
$$\boxed{\Gamma_0^{S_2}[\Sigma]=-\tfrac{g^2}{24}V_4(\Sigma,\Sigma)-\tfrac g{12}V_3(\Psi_*(\Sigma)^3)\ \text{(exact on any branch)};\quad d\Gamma_0=\partial_\Sigma S\vert_{\Psi_*(\Sigma)}\ \Rightarrow\ \text{stationary points}=\text{joint critical points on the branch}=\{(\Psi_c,\Psi_c^{\otimes2})\}\ \text{at }S_2\ \text{(generically: off }\det(Q_{\Sigma_c}+g\ell_2(\Psi_c,\cdot))=0);\quad \Gamma_0^{S_3}=-\tfrac{g^2}{24}V_4(\Sigma^2)-\tfrac{g^6}{28800}j_\Sigma Q_\Sigma^{-1}j_\Sigma+O(g^{10}).}$$

\subsection*{Verification}
C4-exact ((4.1) on the transcritical branch at three $\lambda$, 30 digits; break: an off-branch point fails); C4-leading ((4.2): ratio of $\Gamma_0-\Gamma_0^{\rm triv}$ to the predicted $\lambda^3$ term $\to1$, $|{\rm ratio}-1|=O(\lambda)$); C4-S3 (exact series in $g$ of $\Gamma_0^{S_3}$ through $g^9$ against (4.4), rational $\Sigma$; break: $\tfrac1{28800}\to\tfrac1{14400}$ fails); C5-joint (real nonzero joint critical points $(\Psi_c,\Psi_c^{\otimes2})$ of the five-field $S_2$, both gradients zero); C5-envelope ($d\Gamma_0$ by central differences on the branch through $(\Psi_c,\Sigma_c)$: zero at $\Sigma_c$, equal to $\partial_\Sigma S\ne0$ at a displaced $\Sigma$; break: the branch built with $c_4=\tfrac15$ gives $d\Gamma_0\ne0$ at $\Sigma_c$).

## 4. Finite-model instance (C6)

\subsection*{Setup}
A3, five-field model at $S_2$ ($\mathcal H=\mathbb R^2$, $\Sigma$ a symmetric $2\times2$ matrix, $\dim\mathrm{Sym}^2=3$), random rational $V_2,\dots,V_5$ with entries in $\{-5,\dots,5\}/3$, seed 20261001; the first $V_2$ draw is singular and is redrawn (A4: $Q$ invertible), $V_2=\begin{pmatrix}1&4/3\\4/3&-4/3\end{pmatrix}$, $\det V_2=-28/9$; $V_4$ on $\mathrm{Sym}^2$ has $\det=256/27$. $g=1$ throughout except C1.2-neumann and C4-S3 (exact scaling, §1).

\subsection*{Derivation}
*A point of $D$ (C1.2-D).* Prescribe $\chi=(\tfrac32,-1)$ and solve the two linear equations $(V_2+\tfrac16V_4(\Sigma))\chi=0$ for $(s_0,s_1)$ at $s_2=\tfrac13$: $\Sigma_0=(s_0,s_1,s_2)=(-\tfrac{847}{53},\tfrac{257}{318},\tfrac13)$, $Q_{\Sigma_0}\chi=0$ exactly, $\operatorname{rank}Q_{\Sigma_0}=1$. $V_3(\chi,\chi,\chi)=\tfrac{71}{24}\ne0$ (transcritical case).

*Branch (C3).* Along $\Sigma_0+\lambda\,\delta\Sigma$, $\delta\Sigma=(\tfrac12,\tfrac15,-\tfrac23)$: Newton (30 digits) from $\epsilon(\lambda)\chi$ converges to a nonzero solution of (0.2) with $|\Psi_*-\epsilon\chi|/|\epsilon\chi|=1.2\times10^{-3},\,5.8\times10^{-4},\,2.9\times10^{-4}$ at $\lambda=\tfrac1{100},\tfrac1{200},\tfrac1{400}$ (ratios $2.0$, $2.0$: the error is $O(\lambda)$, the slope of (2.5) exact); the slope with $\tfrac13\to\tfrac16$ is off by $50\%$. At $\Sigma_0$ exactly, the resultant of the two components of (0.2) has $t_0=0$ as a double root and every other solution at distance $\ge0.17$ (C3-double). At a generic $\Sigma_{\rm off}$ ($\det Q_{\Sigma_{\rm off}}=-\tfrac{146321}{46656}$), approached along $\lambda\to0$, the nearest nonzero solution stays at norm $1.527$ (C3-iso): no branch through $(0,\Sigma_{\rm off})$.

*$\Gamma_0$ (C4).* On the three branch points, (4.1) holds to $3\times10^{-31}$; a point displaced off the branch by $0.3\chi$ violates it by $5\times10^{-3}$. The ratio of $\Gamma_0-\Gamma_0^{\rm triv}$ to the $\lambda^3$ law (4.2) is $0.99709,\,0.99854,\,0.99927$: converging to $1$ linearly in $\lambda$. At $S_3$, $\Sigma=(\tfrac23,-\tfrac12,\tfrac57)$, the exact $g$-series of $\Gamma_0$ through $g^9$ (perturbative solution of (0.3) iterated to convergence in the truncated ring) equals (4.3) and (4.4) exactly; coefficients $[g^2]=\tfrac{1259}{31752}$, $[g^6]=-\tfrac{67431137}{470488435200}$, $[g^8]=\tfrac{279571993}{207485399923200}$, all odd orders zero; the coefficient $\tfrac1{14400}$ in place of $\tfrac1{28800}$ fails.

*Critical points (C5).* $V^{(4)}_{\rm eff}=S_2(\Psi,\Psi^{\otimes2})$ has two real nonzero critical points $\Psi_c$; at $(\Psi_c,\Psi_c^{\otimes2})$ the full gradient of $S_2$ vanishes to $2.5\times10^{-29}$ (C5-joint). On the branch through $(\Psi_c,\Sigma_c)$ (Newton continuation), the central-difference gradient of $\Gamma_0$ at $\Sigma_c$ is $1.9\times10^{-19}$ (step $10^{-10}$, 30 digits); at a displaced $\Sigma$ the same gradient equals $\partial_\Sigma S$ on the branch ($|\partial_\Sigma S|=5.9\times10^{-3}$, relative error $4\times10^{-17}$): the envelope identity (4.5), non-vacuous. With $c_4=\tfrac15$ in the action, the branch through $\Psi_c$ has $|d\Gamma_0(\Sigma_c)|=8.96$: the equality of the stationary point of $\Gamma_0$ with the $\Sigma$-elimination's $\Sigma_c=\Psi_c^{\otimes2}$ is a property of the R1 coefficients.

*Nilpotency in the $L_\infty$ model (C2).* 060's `LinfModel(21,[0,0,0,1,1],(1,),"T3")` (retract of a matrix Chern–Simons $L_\infty$ model; $T_0=Q$, $T_2(\Sigma)=\tfrac12\ell_3(\Sigma,\cdot)$ extended linearly to $\mathrm{Sym}^2$): $|T_0^2|/|T_0|^2=7\times10^{-17}$ (control), $|\{T_0,T_2(\Sigma)\}|/(|T_0||T_2|)=0.147$ for a random symmetric $\Sigma$ and $0.156$ for $\Sigma=\psi\otimes\psi$ with $T_0\psi=0$ to $4\times10^{-32}$ (the $Q$-closed case: the Jacobiator term of (1.5)); $|T_2(\Sigma)^2|/|T_2|^2=0.051$. Both terms of (1.4) are nonzero.

\subsection*{Result}
All finite-model checks pass: `codes/verify-sigma-effective.py`, 17 PASS, 0 FAIL, seed 20261001, log `agent/scratch/sigma-effective-run2.log` (run1 superseded by the C2-g2 logic fix).

\subsection*{Verification}
Checks named in §0–§3; break legs: C0.1-c4 ($\tfrac13$), C1.1-hess ($\tfrac13$), C3-branch (slope with $\tfrac16$), C3-iso (off-$D$ $\Sigma$: no branch), C4-exact (off-branch point), C4-S3 ($\tfrac1{14400}$), C5-envelope ($c_4=\tfrac15$; and the nonzero $\partial_\Sigma S$ at a displaced $\Sigma$ shows the finite-difference gradient is not identically small). C2 control: $T_0^2=0$ in the same code path.

## 5. Regime and interpretation for Task 15

$\Gamma_0[\Sigma]$ is the $\hbar\to0$ limit of the $\Sigma$-effective action $\Gamma[\Sigma]=-\hbar\log\int\mathcal D\Psi\,e^{-S[\Psi,\Sigma]/\hbar}$ evaluated around a branch: $\Gamma=\Gamma_0+\tfrac\hbar2\operatorname{Tr}\log\big(\partial^2_\Psi S\vert_{\Psi_*(\Sigma)}\big)+O(\hbar^2)$. Around the trivial branch at $S_2$, $\Gamma_0=-\tfrac{g^2}{24}V_4(\Sigma,\Sigma)$ carries no $\Sigma$-dynamics and the whole mean-field content is the one-loop term $\tfrac\hbar2\operatorname{Tr}\log Q_\Sigma$ — exactly Weinberg's BCS situation, where the auxiliary's classical action is the pure $-|\Delta|^2/g$ term and the gap equation comes entirely from the fermion $\operatorname{Tr}\log$ (there the classical elimination is empty for a different reason: Grassmann fields have no classical solutions). What the cubic action provides for Weinberg's construction is that $\Psi$ enters $S_2$ through the quadratic form $Q_\Sigma$ and nothing linear, so the Gaussian integral over $\Psi$ is well defined order by order and the one-loop mean-field equation is $\partial_\Sigma\big[-\tfrac{g^2}{24}V_4(\Sigma,\Sigma)+\tfrac\hbar2\operatorname{Tr}\log Q_\Sigma\big]=0$, i.e. $\tfrac{g^2}{12}V_4(\Sigma,\cdot)=\tfrac\hbar2\cdot\tfrac{g^2}6\operatorname{Tr}\big[Q_\Sigma^{-1}\ell_3(\cdot,\cdot)\big]$, a self-consistency equation of BCS type with $Q_\Sigma^{-1}$ the $\Sigma$-dressed propagator. What it does not provide: the fermions of BCS are exactly quadratic, while here $V_3(\Psi^3)$ makes the $\Psi$-integral non-Gaussian; $V_3$ must be treated perturbatively (two-loop and beyond in $\Gamma$, or by a further HS transformation of the cubic term, which is Route B's own tower read backwards). Two features specific to the bosonic $\Psi$ have no BCS counterpart: (i) the nontrivial classical branches of §2, which exist (by the theorem, for corank one and $V_3(\chi^3)\ne0$; only where $Q_\Sigma$ has a kernel) and which the one-loop expansion around $\Psi=0$ does not see (the $\operatorname{Tr}\log$ diverges on $D$ instead), and which carry the classical solutions of the theory (§3, C5); (ii) at $S_3$ the tadpole $V_5(\Sigma,\Sigma,\Psi)$ gives a nontrivial $\Gamma_0$ (4.4) already at tree level, so the mean-field equation at $S_3$ has a classical $\Sigma^3$ term beside the $\operatorname{Tr}\log$. **Scope (A4).** All "below the gap" statements of this section hold at generic momentum only. For a constant, zero-momentum background (the translation-invariant condensate of the BCS analogue) the massless sector is in $\ker Q$ at every level, $\Sigma=0$ lies on $D$, the gap of (1.2) is zero and the small-$s$ regime does not exist; the Task 15 brief must either keep generic momentum (no constant condensate) or treat the massless flat directions separately (they are lifted by $V_3$, $V_4$, as in level truncation), the "below the gap" regime then referring to the massive sector only. At generic momentum the regime in which the one-loop mean field around $\Psi=0$ is self-consistent is $|g^2\Sigma|$ below the gap of $Q$ (1.2), where $Q_\Sigma$ is invertible; the interesting mean-field solutions (BCS analogue: $\Delta\ne0$) sit at $s=g^2\Sigma=O(1)$, where the perturbative control of §1 is lost and $D$ is nearby (at zero momentum $D$ contains $\Sigma=0$) — this is the statement, in the $\Sigma$ direction, that the mean field of Task 15 is a strong-coupling question at the tachyon-vacuum scale, as 057/060 found in the $\Psi$ direction.

## Status

Complete, fix pass 1 applied (critic-065 REVISE light: #1–#7 applied, notes #8–#9 not acted on); script 17/17 PASS after the `C2-g2` logic fix (seed 20261001, log `agent/scratch/sigma-effective-run2.log`). Next: none (ledger row in the fix report).

**Annotation (2026-10-01, from record 069 / critic-069 #13).** Proposed text for `agent/derivations/065-sigma-effective-action.md` §5, to be inserted after its mean-field equation:  > **Sign note (2026-10-01, record 069 Conventions; critic-069 #13).** The mean-field equation above, $\tfrac{g^2}{12}V_4(\Sigma,\cdot)=\tfrac\hbar2\cdot\tfrac{g^2}6\operatorname{Tr}[Q_\Sigma^{-1}\ell_3(\cdot,\cdot)]$, is written with weight $e^{-S/\hbar}$. Since $\operatorname{Tr}[Q_\Sigma^{-1}\ell_3(\delta\Sigma,\cdot)]=-V_4(\delta\Sigma,G_\Sigma)$ with $G_\Sigma=(-\omega Q_\Sigma)^{-1}$, it is record 069's (1.6) with the opposite sign. Under C5 (weight $e^{S/\hbar}$) the correct equation is 069 (1.6), $V_4(\Sigma,\cdot)=\hbar\,V_4(G_\Sigma,\cdot)$, i.e. $\Sigma=\hbar G_\Sigma$ on $\mathrm{Sym}^2\mathcal H/\ker V_4$, and it supersedes this section's sign. Its Gaussian evaluation is the direct-channel third of the Hartree equation (R66), not the Hartree equation. R69's classical statements are unaffected (this section is interpretive).
