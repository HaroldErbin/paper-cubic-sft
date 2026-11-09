# Derivation 040 — Does the gauge algebra close only up to equations of motion at $O(g_s^3)$?

## 0. Task and objective

**Literal task.** Compute $[\delta_{\Lambda_1},\delta_{\Lambda_2}]$ through $O(g_s^3)$ on
$(\Psi,\Sigma_2)$ in the Hubbard–Stratonovich form of closed bosonic SFT truncated at the
quintic order, and decide whether the algebra closes off shell or only modulo equations of
motion; if only modulo, give the coefficient of the equation-of-motion term and classify the
resulting structure in BV terms.

**Motivating objective.** The quintic subsection of the notes needs this result. The
gauge-transformation paragraph needs to know whether the algebra is closed or open at this
order: the two demand different language, and an open algebra changes what must be said about
the BV structure of the auxiliary sector at $O(g_s^4)$ (record 015 §4). The working hypothesis
that the algebra closes only up to equations of motion *because of the
rotation term* is the hypothesis under test, not the answer to confirm.

**Scope / layer.** Algebraic layer: finite-dimensional $\mathcal H_0$, generic (unconstrained)
tensors for $\mathcal V_4,\mathcal V_5$, generic $L_\infty$ products with the $L_\infty$
relations imposed as symbolic substitution rules, formal power series in $g_s$. No worldsheet
input beyond the vertex symmetry and the ghost-number assignments.

## 1. Conventions

**Fields and parameters.** $\Psi\in\mathcal H_0$ with $N_{\rm gh}=2$ (Grassmann-even),
$\Lambda_1,\Lambda_2\in\mathcal H_0$ with $N_{\rm gh}=1$ (Grassmann-odd),
$\Sigma_2\in\operatorname{Sym}^2\mathcal H_0/\ker\mathcal V_4$ with $N_{\rm gh}=4$.
Normalisation $\braket{c_{-1}\bar c_{-1}c_0^-c_0^+c_1\bar c_1}=-1/2$, no factor $i$.

**Degree parity.** All sign bookkeeping below uses the $L_\infty$ *degree* parity of
[Erbin2023] ch. *Homotopy algebras*, $\deg x=1-N_{\rm gh}(x)$, which is **opposite to the
Grassmann parity**. Hence
$$
\abs{\Psi}=1,\qquad \abs{\Lambda_i}=0,\qquad \abs{Q_B\Psi}=0,\qquad\abs{Q_B\Lambda_i}=1 .
\tag{1.1}
$$
The products are graded **anti**symmetric in this grading,
$$
\ell_n(x_1,x_2,\dots)=(-1)^{1+\abs{x_1}\abs{x_2}}\,\ell_n(x_2,x_1,\dots),
\qquad \deg\ell_n=n-2 ,
\tag{1.2}
$$
[cited: Erbin2023 eq. (math:Linf-ln-sym), (math:eq:Linf-degree-ln)]. Two consequences used
constantly and stated once:

- **$\Psi$-entries commute freely**: swapping two entries of degree parity $1$ gives
  $(-1)^{1+1}=+1$, so $\ell_n(\Psi^{\otimes m},\dots)$ is well defined with the usual $1/m!$.
- **the two gauge parameters anticommute**: swapping $\Lambda_1,\Lambda_2$ (degree parity $0$)
  gives $(-1)^{1+0}=-1$. This is the single sign the brief warns about, and it is displayed at
  every use below. It is the *same* physical statement as "two Grassmann-odd parameters
  anticommute"; only its formalisation differs.
- mixed swaps: $\abs{\Psi}\abs{\Lambda}=0$, so $\ell(\dots,\Psi,\Lambda,\dots)
  =-\ell(\dots,\Lambda,\Psi,\dots)$; $\abs{Q\Lambda}\abs{\Psi}=1$, so
  $\ell(\dots,Q\Lambda,\Psi,\dots)=+\ell(\dots,\Psi,Q\Lambda,\dots)$.

**Commutator.** $[\delta_{\Lambda_1},\delta_{\Lambda_2}]
:=\delta_{\Lambda_1}\delta_{\Lambda_2}-\delta_{\Lambda_2}\delta_{\Lambda_1}$, acting on the
fields only ($\Lambda_1,\Lambda_2$ are field-independent). Both $\delta_{\Lambda_i}$ are
even operations on the field space, so no extra sign accompanies the commutator itself.

**Vertices.** $\mathcal V_4(A,B)\leftrightarrow\braket{A,p_{2,2}B}$ for $A,B\in\operatorname{Sym}^2
\mathcal H_0$, so $p_{2,2}:\operatorname{Sym}^2\to(\operatorname{Sym}^2)^*$;
$\mathcal V_5$ is totally symmetric in its five $\mathcal H_0$ legs and
$p_{3,2}:\operatorname{Sym}^3\mathcal H_0\to(\operatorname{Sym}^2\mathcal H_0)^*$ is
$\mathcal V_5$ with three legs filled, totally symmetric in those three entries. In particular
$v=p_{3,2}(\Psi^{\otimes3})$, $W=p_{3,2}(\Psi,\cdot\,,\cdot)$, and $p_{3,2}(X,u)$ for
$X\in\operatorname{Sym}^2$, $u\in\mathcal H_0$ means the two $X$ strands in two of the three
symmetric slots.

**Symmetrised product.** $A\odot B:=\tfrac12(A\otimes B+B\otimes A)$, so
$\delta\Psi\otimes\Psi+\Psi\otimes\delta\Psi=2\,\delta\Psi\odot\Psi$.

## 2. The two gauge laws as used here

**(2.1) The $\Psi$ law** (truncated $L_\infty$, quintic truncation, i.e. $\ell_n$ for
$n\le4$):
$$
u_i:=\delta_{\Lambda_i}\Psi
=\sum_{n\ge0}\frac{g_s^n}{n!}\,\ell_{n+1}(\Psi^{\otimes n},\Lambda_i)
=Q_B\Lambda_i+g_s\ell_2(\Psi,\Lambda_i)+\tfrac{g_s^2}{2}\ell_3(\Psi,\Psi,\Lambda_i)
+\tfrac{g_s^3}{3!}\ell_4(\Psi^{\otimes3},\Lambda_i)+O(g_s^4).
\tag{2.1}
$$
$u_i$ has degree parity $1$, like $\Psi$; it is Grassmann-even.

**(2.2) The $\Psi$ equation of motion** of the *effective* (nonpolynomial) action, truncated
the same way:
$$
\mathcal F(\Psi)=\sum_{n\ge1}\frac{g_s^{n-1}}{n!}\,\ell_n(\Psi^{\otimes n})
=Q_B\Psi+\tfrac{g_s}{2}\ell_2(\Psi,\Psi)+\tfrac{g_s^2}{6}\ell_3(\Psi^{\otimes3})
+\tfrac{g_s^3}{24}\ell_4(\Psi^{\otimes4})+O(g_s^4),
\tag{2.2}
$$
[cited: Erbin2023 eq. (bsft:eq:closed-eom-cl)]; $\abs{\mathcal F}=0$.

**(2.3) The $\Sigma_2$ law at $O(g_s^3)$** (the $O(g_s)$ truncation
of the exact law 011 (B.9) = R17). It is **linear in $\delta\Psi$**; write it as an operator
$\Phi$ depending on $(\Psi,\Sigma_2)$:
$$
\delta\Sigma_2=\Phi(u)
:=\underbrace{2\,u\odot\Psi}_{(\mathrm a)}
+\underbrace{\tfrac{3g_s}{5}\,p_{2,2}^{-1}p_{3,2}(u,\Psi,\Psi)}_{(\mathrm b)}
+\underbrace{\tfrac{g_s}{10}\,p_{2,2}^{-1}p_{3,2}(X,u)}_{(\mathrm c)}+O(g_s^2),
\qquad X:=\Sigma_2-\Psi^{\otimes2}.
\tag{2.3}
$$
Term (a) is taken in the **symmetrised** reading, following 039 (3.5); on
$\operatorname{Sym}^2\mathcal H_0$ the two readings agree, and §5.2 shows that the
unsymmetrised one, if extended to $\mathcal H_0^{\otimes2}$, fails closure at $O(g_s^0)$.

**(2.3) is a truncation, and an insufficient one.** The $\Sigma_2$ gauge law for the cubic
action $S_3$ is known **exactly** in $g_s$ — 011 (B.8)–(B.9) = R17 — and (2.3) is only its
relative-$O(g_s)$ truncation: term (c) carries $p_{2,2}^{-1}$ where the exact law carries
$K_\Psi^{-1}$, and $X$ where the exact law carries $\tilde X$. Both differences are relative
$O(g_s)$ inside a term already carrying $g_s/10$, hence *absolute* $g_s^2$ — the same absolute
order as the leading closure defect. (2.3) is therefore **not** adequate for the commutator,
and §5 uses the exact law (2.5) instead. The first pass of §5 used (2.3) throughout and
mis-graded its own remainder as a result; see the table (5.0).

**(2.5) The exact $\Sigma_2$ law** (011 (B.8)–(B.9), R17; exact in $g_s$ for $S_3$, off shell,
arbitrary $\delta\Psi$). With
$$
K_\Psi:=p_{2,2}-\tfrac{g_s}{5}\,p_{3,2}(\cdot,\cdot,\Psi),\qquad
v:=p_{3,2}(\Psi^{\otimes3}),\qquad
\Sigma_2^*(\Psi):=\Psi^{\otimes2}+\tfrac{g_s}{5}K_\Psi^{-1}v,\qquad
\tilde X:=\Sigma_2-\Sigma_2^*(\Psi),
$$
the law is
$$
\delta\Psi=u,\qquad
\delta\tilde X=R_u\tilde X,\qquad
R_u:=\tfrac{g_s}{10}K_\Psi^{-1}p_{3,2}(\cdot,\cdot,u)\big|_{\text{one slot eats }\tilde X},
\tag{2.5}
$$
equivalently $\delta\Sigma_2=D\Sigma_2^*[u]+R_u\tilde X=:\Phi_{\rm exact}(u)$, manifestly
linear in $u$. $R_u=O(g_s)$ and $\partial_\Psi R=O(g_s^2)$, since
$\partial_\Psi K_\Psi^{-1}=O(g_s)$. Expanding (2.5) to relative order $g_s$ and re-expressing
in $X=\Sigma_2-\Psi^{\otimes2}$ returns (2.3).

**(2.4) $\delta X$ is $O(g_s)$.** $\delta(\Psi^{\otimes2})=2u\odot\Psi$ is exactly term (a), so
$$
\delta X=\Phi(u)-2u\odot\Psi
=\tfrac{3g_s}{5}p_{2,2}^{-1}p_{3,2}(u,\Psi,\Psi)+\tfrac{g_s}{10}p_{2,2}^{-1}p_{3,2}(X,u)
+O(g_s^2)=O(g_s).
\tag{2.4}
$$
This is R11 ($\delta X=0$ at $O(g_s^2)$) plus the first correction, and it is what makes the
$\Sigma_2$ computation close at the order required.

## 3. $L_\infty$ substitution rules

No $L_\infty$ theory is re-derived. The generalised Jacobi identities are imposed as
substitution rules in the form of [Erbin2023] eq. (math:eq:Linf-gen-Jacobi),
$$
0=J_n(x_1,\dots,x_n)
=\sum_{\substack{i,j\ge1\\ i+j=n+1}}(-1)^{i(j-1)}
\sum_{\sigma\in{\rm Sh}(i,n-i)}(-1)^\sigma\epsilon(\sigma,\{x\})\,
\ell_j\big(\ell_i(x_{\sigma(1)},\dots,x_{\sigma(i)}),x_{\sigma(i+1)},\dots,x_{\sigma(n)}\big),
\tag{3.1}
$$
with $\epsilon$ the Koszul sign of the degree parities (1.1). **Prefactor.** With the sign
convention used here — the permutation signature and the Koszul sign merged into the single
transposition rule (1.2) — the printed value $(-1)^{i(j-1)}$ is inconsistent with the $n=2$
and $n=3$ identities displayed explicitly in the same subequation block of the source, namely
the derivation property of $\ell_1$ and the Jacobiator, which are the statements with
physical content. Requiring those two fixes the prefactor to $(-1)^i$ at
$(i,j)=(1,2),(2,1),(1,3),(2,2),(3,1)$. At $n=4$ the two candidate prefactors
$(-1)^{i(j-1)}$ and $(-1)^i$ **agree** ($i+j=5$ gives $(-,+,-,+)$ either way), so no choice is
made there and the $O(g_s^3)$ check `C1.2` tests the coefficients, not the prefactor
convention. This is a bookkeeping matter internal to the source's conventions and does not
affect any physical statement; it is recorded because the companion script depends on it. The two instances written out by
hand below are $J_2(\Lambda_1,\Lambda_2)$ and $J_3(\Psi,\Lambda_1,\Lambda_2)$; $J_4$ and the
$O(g_s^3)$ bookkeeping are handled by the companion script, which implements (3.1) verbatim
and checks membership of the residual in the linear span of the $J_n$ — i.e. the relations are
used as rewriting rules on unconstrained generic products, never as equations solved for
particular $\ell_n$ (METHOD NOTE, R16).

Written out ([cited: Erbin2023], same subequation block):
$$
J_2(x_1,x_2):\quad \ell_1\ell_2(x_1,x_2)=\ell_2(\ell_1x_1,x_2)+(-1)^{\abs{x_1}}\ell_2(x_1,\ell_1x_2),
\tag{3.2}
$$
$$
\begin{aligned}
J_3(x_1,x_2,x_3):\quad
&\ell_2(\ell_2(x_1,x_2),x_3)+(-1)^{(\abs{x_1}+\abs{x_2})\abs{x_3}}\ell_2(\ell_2(x_3,x_1),x_2)
+(-1)^{(\abs{x_2}+\abs{x_3})\abs{x_1}}\ell_2(\ell_2(x_2,x_3),x_1)
\\&=\ell_1\ell_3(x_1,x_2,x_3)+\ell_3(\ell_1x_1,x_2,x_3)+(-1)^{\abs{x_1}}\ell_3(x_1,\ell_1x_2,x_3)
+(-1)^{\abs{x_1}+\abs{x_2}}\ell_3(x_1,x_2,\ell_1x_3).
\end{aligned}
\tag{3.3}
$$

## Claim tree

- **A1** Algebraic layer: finite-dimensional $\mathcal H_0$, unconstrained generic tensors for
  $\mathcal V_4,\mathcal V_5$ and for the products $\ell_{n\le4}$, formal power series in
  $g_s$. No worldsheet input beyond total symmetry of the vertices and the ghost-number
  assignments.
- **A2** Conventions of §1: degree parity $\abs{x}=1-N_{\rm gh}$, graded antisymmetry (1.2),
  the Jacobi identities in the form (3.1), $[\delta_1,\delta_2]=\delta_1\delta_2-\delta_2\delta_1$.
- **A3** Quintic truncation: the action is $S_3$, known to $O(g_s^3)$, and the $\Psi$ law is
  taken to $\ell_4$. The $\Sigma_2$ law is **not** truncated: (2.5) = 011 (B.8)–(B.9) = R17 is
  exact in $g_s$ for $S_3$. The truncated form (2.3) is used only in §§5.1–5.8, where it is
  shown to be inadequate for the commutator.
- **A4** Term (a) of (2.3) is read symmetrised (039 (3.5)). On $\operatorname{Sym}^2\mathcal
  H_0$ the symmetrised and unsymmetrised readings agree (C2.1, C2.1-unsym); the symmetrised
  reading is the one (2.3) is written in, and nothing here decides a live convention.
- **A5** $p_{2,2}$ is invertible on $\operatorname{Sym}^2\mathcal H_0/\ker\mathcal V_4$ and
  $\mathcal V_5$ annihilates $\ker\mathcal V_4$, so that $p_{2,2}^{-1}p_{3,2}$ is well defined
  on the quotient. This is PH1 together with the R38 condition (PH5); it is inherited from the
  law (2.3) itself, not added here.
- **C1** Through $O(g_s^3)$, the $\Psi$ sector closes with the field-dependent parameter
  $\Lambda_{12}$ of (4.6) **up to a term proportional to the $\Psi$ equation of motion**
  $\mathcal F$, of coefficient $+1$ in the normalisation (4.7): the algebra is open already in
  the $\Psi$ sector, from $O(g_s^2)$ on. [by C1.1–C1.4]
  - **C1.1** $\Lambda_{12}=\sum_{n\ge0}\frac{g_s^{n+1}}{n!}\ell_{n+2}(\Lambda_1,\Lambda_2,\Psi^{\otimes n})$,
    antisymmetric in $\Lambda_1\leftrightarrow\Lambda_2$. [by A2; eq. (4.7)] [check: C1.1]
  - **C1.2** $\mathcal D_\Psi:=[\delta_1,\delta_2]\Psi-\delta_{\Lambda_{12}}\Psi
    =\sum_{n\ge0}\frac{g_s^{n+2}}{n!}\ell_{n+3}(\Psi^{\otimes n},\Lambda_1,\Lambda_2,\mathcal F)$,
    i.e. $g_s^2\ell_3(\Lambda_1,\Lambda_2,\mathcal F)+g_s^3\ell_4(\Psi,\Lambda_1,\Lambda_2,Q_B\Psi)+O(g_s^4)$.
    [by A2, A3; eqs. (4.4)–(4.6), (4.8), (4.9)] [by check: C1.2]
  - **C1.3** The orders $g_s^0,g_s^1$ carry no defect: at $g_s^0$ the commutator vanishes
    identically, at $g_s^1$ it is $Q_B\Lambda_{12}$ exactly. [by A2; eqs. (4.2), (4.3)] [check: C1.3]
  - **C1.4** C1.1–C1.2 agree with the literature statement of the closed-SFT gauge algebra,
    up to an ordering inconsistency in the cited equation which is itself flagged there.
    [cited: Erbin2023 eq. (bsft:eq:closed-gauge-alg-cl), after Zwiebach 1993 sec. 4]
- **C2** $[\delta_1,\delta_2]\Sigma_2=\delta_{\Lambda_{12}}\Sigma_2
  +\Phi_{\rm exact}(\mathcal D_\Psi)+\mathcal E$ with the **same** $\Lambda_{12}$ as in C1 and
  no new gauge parameter, where $\mathcal E=\tfrac{g_s^2}{100}[A_{u_1},A_{u_2}]\tilde X
  +O(g_s^3)$ is **proportional to the $\Sigma_2$ equation of motion** and sits at the same
  absolute order $g_s^2$ as the leading $\mathcal F$-proportional term. The auxiliary sector
  therefore contributes a defect of its own — an $E_\Sigma$-type $E$-structure function — but
  none off the equations of motion. [by C2.1–C2.9]
  - **C2.1** The cross terms of (a) cancel exactly in the antisymmetrisation, in the
    symmetrised reading; in the unsymmetrised reading, extended to
    $\mathcal H_0^{\otimes2}$, they leave $2(u_2\otimes u_1-u_1\otimes u_2)
    \in\Lambda^2\mathcal H_0$, which vanishes on $\operatorname{Sym}^2\mathcal H_0$. This
    confirms 039 (3.5); on $\operatorname{Sym}^2$ the two readings agree. [by A4; eq. (5.2)] [check: C2.1]
  - **C2.2** The cross terms of (b) cancel by total symmetry of $p_{3,2}$. [by A1; eq. (5.3)] [check: C2.2]
  - **C2.3** With the truncated law (2.3), term (c) contributes $\Phi$-linearly plus a
    remainder $\mathcal A$ at **absolute** order $g_s^2$. [by A3; eqs. (2.4), (5.4), (5.9)] [check: C2.3, C2.6]
  - **C2.4** $\Phi$ is linear in its argument, so the $\mathcal F$-proportional part of
    $\Delta_\Sigma$ is $\Phi(\mathcal D_\Psi)$, coefficient $+1$, explicitly (5.6)–(5.7).
    [by C1.2, C2.1–C2.3; eqs. (5.5), (5.6)] [check: C2.4, C2.12]
  - **C2.5** $[\delta_1,\delta_2]\Sigma_2^*(\Psi)=D\Sigma_2^*[[\delta_1,\delta_2]\Psi]$
    **exactly** in $g_s$: the second derivative of the saddle is symmetric in $(u_1,u_2)$ and
    drops. [by A3 (exact law), A2; eq. (5.10)] [check: C2.7]
  - **C2.6** $[\delta_1,\delta_2]\tilde X=R_{[\delta_1,\delta_2]\Psi}\tilde X+\mathcal E$
    **exactly**, with $\mathcal E=\{(\partial_\Psi R)_{[u_2}[u_{1]}]+[R_{u_2},R_{u_1}]\}
    \tilde X$ manifestly $\tilde X$-proportional. [by A3 (exact law); eq. (5.11)] [check: C2.8, C2.10]
  - **C2.7** $\mathcal E=\tfrac{g_s^2}{100}[A_{u_1},A_{u_2}]\tilde X+O(g_s^3)$, with no
    $g_s^1$ term, and the coefficient is generically nonzero. [by C2.6; eq. (5.12)] [check: C2.9, C2.9-g1, C2.9-nonzero]
  - **C2.8** Route 1's remainder (5.9) is neither complete nor correct as a statement about
    $\Delta_\Sigma$: its first bracket T7 is an artifact of using $X$ instead of $\tilde X$,
    and the $(\partial_\Psi R)$ contribution T9 is invisible to the truncated law. [by C2.6, C2.7; §5.8, (5.12)] [check: C2.11]
  - **C2.9** Composition: $\Delta_\Sigma=\Phi_{\rm exact}(\mathcal D_\Psi)+\mathcal E$ for
    whatever $\Lambda_{12}$ Part A supplies, $\delta_{\Lambda_{12}}\Sigma_2$ being formed
    explicitly as $\Phi_{\rm exact}(\delta_{\Lambda_{12}}\Psi)$. [by C1.1, C1.2, C2.4–C2.7; eq. (5.13)] [check: C2.12]
- **C3** The theory is an open gauge algebra in the BV sense with field-dependent structure
  functions, at $O(g_s^3)$. The $E$-type structure functions are
  $\lambda^{\Psi}=\ell_{n+3}(\Psi^n,\Lambda_1,\Lambda_2,\cdot)$ against $\mathcal F$ — in both
  rows, through $\Phi_{\rm exact}$ in the $\Sigma_2$ row — **and**
  $\lambda^{\Sigma}=-\tfrac{3}{25}[A_{u_1},A_{u_2}]p_{2,2}^{-1}+O(g_s)$ against $E_\Sigma$ in
  the $\Sigma_2$ row. None is of the trivial-symmetry type. Consistent with record 016/R22.
  [by C1, C2, C3.1–C3.2]
  - **C3.1** The rotation term passes through the commutator at *first* order in itself,
    because it is a compensator linear in $\delta\Psi$ acting homogeneously on $\tilde X$ —
    the property 016 uses to deny it the status of an independent symmetry. It fails to do so
    at *second* order in itself, which is the origin of $\mathcal E$. [by C2.5–C2.7, R22]
  - **C3.2** The working hypothesis that the rotation term is what makes the
    algebra close only up to equations of motion is **half right**: the openness against
    $\mathcal F$ pre-exists the auxiliary field and is not caused by the rotation term, but
    the rotation term does generate an independent $E_\Sigma$-proportional defect, at second
    order in itself and at the same $g_s^2$. [by C1, C2]
- **C4** Limiting case: at $g_s\to0$ both sides vanish identically and $\Sigma_2=\Psi^{\otimes2}$
  rigidly ($\delta X=0$), recovering R11. [by C1.3, C2; eq. (2.4)] [check: C4]

Open gaps: [GAP-1] the $O(g_s^3)$ term of $\mathcal E$ is not computed (not needed for C2/C3,
but the $E_\Sigma$-proportional part of $\Delta_\Sigma$ is therefore known only at $g_s^2$);
[GAP-2] non-vanishing of $[A_{u_1},A_{u_2}]$ is established for generic totally symmetric
$\mathcal V_4,\mathcal V_5$ at $N=2$, not for the actual string vertices (layer A1);
[GAP-3] $\mathcal E$ is computed for the R17/011 (B.8) *representative* of the $\Sigma_2$
gauge law: R22's invariance condition fixes only the $K_\Psi$-symmetric part of $R_u$, so an
admissible $K_\Psi$-antisymmetric $\Delta R_u=O(g_s)$ shifts the coefficient $\tfrac1{100}$;
whether an admissible redefinition of $R_u$ removes $\mathcal E$ is open and not decided here.
Hypotheses in force: PH1, PH5 (through A5, inherited from the gauge law (2.5) and from R17),
for C2 and C3 only; **C1 is unconditional** — §4 is pure $L_\infty$ bookkeeping and uses
neither.

## 4. Question 1 — the $\Psi$ sector

### Setup

Assumptions A1–A3. Baseline for question 2. Local notation: $u_i=\delta_{\Lambda_i}\Psi$ as in
(2.1); all terms are collected by powers of $g_s$.

### Derivation

**(4.1) The general term.** $\delta_{\Lambda_2}\Psi$ depends on $\Psi$ polynomially and on
$\Lambda_2$ linearly, so
$$
\delta_1\delta_2\Psi
=\sum_{n\ge1}\frac{g_s^n}{n!}\,n\,\ell_{n+1}(u_1,\Psi^{\otimes(n-1)},\Lambda_2)
=\sum_{n\ge1}\frac{g_s^n}{(n-1)!}\,\ell_{n+1}(u_1,\Psi^{\otimes(n-1)},\Lambda_2),
\tag{4.1}
$$
the factor $n$ because the $n$ insertions of $u_1$ into the $n$ $\Psi$-slots are equal:
$\abs{u_1}=\abs{\Psi}=1$ and a swap of two degree-odd entries costs $(-1)^{1+1}=+1$ by (1.2).

**(4.2) Order $g_s^0$.** $\delta_2\Psi|_{g^0}=Q_B\Lambda_2$ is field-independent, so
$\delta_1\delta_2\Psi|_{g^0}=0$ and $[\delta_1,\delta_2]\Psi|_{g^0}=0$.

**(4.3) Order $g_s^1$.** From (4.1), $\delta_1\delta_2\Psi|_{g^1}=g_s\ell_2(Q_B\Lambda_1,\Lambda_2)$, so
$$
[\delta_1,\delta_2]\Psi\big|_{g^1}
=g_s\big[\ell_2(Q_B\Lambda_1,\Lambda_2)-\ell_2(Q_B\Lambda_2,\Lambda_1)\big]
=g_s\big[\ell_2(Q_B\Lambda_1,\Lambda_2)+\ell_2(\Lambda_1,Q_B\Lambda_2)\big]
=g_s\,Q_B\ell_2(\Lambda_1,\Lambda_2).
\tag{4.2}
$$
The middle step is the swap $\ell_2(Q_B\Lambda_2,\Lambda_1)=(-1)^{1+\abs{Q_B\Lambda_2}\abs{\Lambda_1}}
\ell_2(\Lambda_1,Q_B\Lambda_2)=-\ell_2(\Lambda_1,Q_B\Lambda_2)$ by (1.2) with
$\abs{Q_B\Lambda_2}\abs{\Lambda_1}=1\cdot0=0$; the last step is $J_2(\Lambda_1,\Lambda_2)$,
eq. (3.2), with $\abs{\Lambda_1}=0$.

**(4.4) Order $g_s^2$.** From (4.1) with $n=1,2$ and $u_1|_{g^0}=Q_B\Lambda_1$,
$u_1|_{g^1}=g_s\ell_2(\Psi,\Lambda_1)$:
$$
\delta_1\delta_2\Psi\big|_{g^2}
=g_s^2\big[\ell_2(\ell_2(\Psi,\Lambda_1),\Lambda_2)+\ell_3(Q_B\Lambda_1,\Psi,\Lambda_2)\big]
=g_s^2\big[\ell_2(\ell_2(\Psi,\Lambda_1),\Lambda_2)+\ell_3(\Psi,Q_B\Lambda_1,\Lambda_2)\big],
\tag{4.3}
$$
the reordering being free, $(-1)^{1+\abs{Q_B\Lambda_1}\abs{\Psi}}=(-1)^{1+1}=+1$.
Antisymmetrising and using
$-\ell_3(\Psi,Q_B\Lambda_2,\Lambda_1)=+\ell_3(\Psi,\Lambda_1,Q_B\Lambda_2)$ (swap of
$Q_B\Lambda_2$, $\Lambda_1$: $(-1)^{1+0}=-1$),
$$
[\delta_1,\delta_2]\Psi\big|_{g^2}/g_s^2
=\ell_2(\ell_2(\Psi,\Lambda_1),\Lambda_2)-\ell_2(\ell_2(\Psi,\Lambda_2),\Lambda_1)
+\ell_3(\Psi,Q_B\Lambda_1,\Lambda_2)+\ell_3(\Psi,\Lambda_1,Q_B\Lambda_2).
\tag{4.4}
$$
Now apply $J_3(\Psi,\Lambda_1,\Lambda_2)$, eq. (3.3), with parities $(1,0,0)$: every explicit
sign in (3.3) is $+1$ except $(-1)^{\abs{x_1}}=(-1)^{\abs{x_1}+\abs{x_2}}=-1$ on the last two
$\ell_3$ terms, and $\ell_2(\ell_2(\Lambda_2,\Psi),\Lambda_1)=-\ell_2(\ell_2(\Psi,\Lambda_2),\Lambda_1)$.
So (3.3) reads
$$
\ell_2(\ell_2(\Psi,\Lambda_1),\Lambda_2)-\ell_2(\ell_2(\Psi,\Lambda_2),\Lambda_1)
+\ell_2(\ell_2(\Lambda_1,\Lambda_2),\Psi)
=Q_B\ell_3(\Psi,\Lambda_1,\Lambda_2)+\ell_3(Q_B\Psi,\Lambda_1,\Lambda_2)
-\ell_3(\Psi,Q_B\Lambda_1,\Lambda_2)-\ell_3(\Psi,\Lambda_1,Q_B\Lambda_2),
\tag{4.5}
$$
and substituting the first two terms of (4.5) into (4.4),
$$
[\delta_1,\delta_2]\Psi\big|_{g^2}/g_s^2
=Q_B\ell_3(\Psi,\Lambda_1,\Lambda_2)-\ell_2(\ell_2(\Lambda_1,\Lambda_2),\Psi)
+\ell_3(Q_B\Psi,\Lambda_1,\Lambda_2).
\tag{4.6}
$$

**(4.5) Reading off $\Lambda_{12}$.** Postulate $\Lambda_{12}=a_1g_s\ell_2(\Lambda_1,\Lambda_2)
+a_2g_s^2\ell_3(\Lambda_1,\Lambda_2,\Psi)+a_3g_s^3\ell_4(\Lambda_1,\Lambda_2,\Psi,\Psi)+O(g_s^4)$
and expand $\delta_{\Lambda_{12}}\Psi=Q_B\Lambda_{12}+g_s\ell_2(\Psi,\Lambda_{12})+\dots$:
$$
\delta_{\Lambda_{12}}\Psi\big|_{g^1}=a_1g_sQ_B\ell_2(\Lambda_1,\Lambda_2),\qquad
\delta_{\Lambda_{12}}\Psi\big|_{g^2}=g_s^2\big[a_2Q_B\ell_3(\Psi,\Lambda_1,\Lambda_2)
-a_1\ell_2(\ell_2(\Lambda_1,\Lambda_2),\Psi)\big],
$$
using $\ell_3(\Lambda_1,\Lambda_2,\Psi)=\ell_3(\Psi,\Lambda_1,\Lambda_2)$ (two swaps, each
$(-1)^{1+0}=-1$) and $\ell_2(\Psi,y)=-\ell_2(y,\Psi)$ for $\abs{y}=\abs{\ell_2(\Lambda_1,\Lambda_2)}=0$.
Comparison with (4.2) and (4.6) gives $a_1=a_2=1$, and the residue of (4.6) is
$+\ell_3(Q_B\Psi,\Lambda_1,\Lambda_2)$. Hence
$$
\boxed{\;\Lambda_{12}=\sum_{n\ge0}\frac{g_s^{n+1}}{n!}\,\ell_{n+2}(\Lambda_1,\Lambda_2,\Psi^{\otimes n})
=g_s\ell_2(\Lambda_1,\Lambda_2)+g_s^2\ell_3(\Lambda_1,\Lambda_2,\Psi)
+\tfrac{g_s^3}{2}\ell_4(\Lambda_1,\Lambda_2,\Psi^{\otimes2})+O(g_s^4)\;}
\tag{4.7}
$$
$$
\boxed{\;[\delta_{\Lambda_1},\delta_{\Lambda_2}]\Psi=\delta_{\Lambda_{12}}\Psi+\mathcal D_\Psi,
\qquad
\mathcal D_\Psi=\sum_{n\ge0}\frac{g_s^{n+2}}{n!}\,
\ell_{n+3}\big(\Psi^{\otimes n},\Lambda_1,\Lambda_2,\mathcal F(\Psi)\big)\;}
\tag{4.8}
$$
$$
\mathcal D_\Psi
=g_s^2\,\ell_3\big(\Lambda_1,\Lambda_2,Q_B\Psi\big)
+g_s^3\Big[\tfrac12\ell_3\big(\Lambda_1,\Lambda_2,\ell_2(\Psi,\Psi)\big)
+\ell_4\big(\Psi,\Lambda_1,\Lambda_2,Q_B\Psi\big)\Big]+O(g_s^4).
\tag{4.9}
$$
The $g_s^3$ coefficients of (4.7) and (4.9) are fixed by $J_4(\Psi,\Lambda_1,\Lambda_2)$ and
$J_4(\Psi,\Psi,\Lambda_1,\Lambda_2)$; they are established by the companion check `C1.2`,
which imposes (3.1) as rewriting rules on generic products rather than by a hand expansion of
$J_4$.

### Commentary

- (4.1): the only sign statement is that $u_1$ may be moved into any $\Psi$ slot for free.
  This is where a Grassmann-parity convention and a degree-parity convention could disagree;
  they do not, because both assign $u_1$ and $\Psi$ the same parity.
- (4.2)–(4.6): every reordering is displayed with its exponent. The two places where the
  answer would flip sign are the swap $\ell_2(Q_B\Lambda_2,\Lambda_1)\to\ell_2(\Lambda_1,Q_B\Lambda_2)$
  and the swap $\ell_3(\Psi,Q_B\Lambda_2,\Lambda_1)\to\ell_3(\Psi,\Lambda_1,Q_B\Lambda_2)$;
  both carry $\abs{Q_B\Lambda}\abs{\Lambda}=1\cdot0=0$ and so give $-1$ from the intrinsic
  $(-1)^1$ of (1.2), which is exactly what turns the antisymmetrised commutator into the
  *symmetric-looking* combinations that $J_2$ and $J_3$ close on.
- $\Lambda_{12}$ is antisymmetric under $\Lambda_1\leftrightarrow\Lambda_2$ (parity $0$
  entries in a graded-antisymmetric product), as it must be, and so is $\mathcal D_\Psi$. Both
  sides of (4.8) are therefore antisymmetric: this is a structural check that no relative sign
  has been dropped.
- Ghost numbers: $N_{\rm gh}(\Lambda_{12})=1$ ($\ell_{n+2}$ shifts by $3-2(n+2)$ and eats
  $1+1+2n$), $N_{\rm gh}(\mathcal D_\Psi)=2$ — both correct.
- **Comparison with the literature.** [Erbin2023] eq. (bsft:eq:closed-gauge-alg-cl), after
  Zwiebach (1993) sec. 4, states exactly (4.7)–(4.8). Its displayed form writes the commutator
  as $[\delta_{\Lambda_2},\delta_{\Lambda_1}]$, the parameter with the argument order
  $(\Lambda_1,\Lambda_2)$ and the anomaly with $(\Lambda_2,\Lambda_1)$; since both
  $\Lambda(\Lambda_1,\Lambda_2)$ and the anomaly are antisymmetric in the two parameters, the
  two terms as printed have opposite relative orderings and cannot both be right. The source
  (4.7)–(4.8) fix the ordering consistently: with $[\delta_{\Lambda_1},\delta_{\Lambda_2}]$ on
  the left, both right-hand terms carry $(\Lambda_1,\Lambda_2)$. This is a bookkeeping
  clarification, not a disagreement about content.

### Result

$[\delta_{\Lambda_1},\delta_{\Lambda_2}]\Psi=\delta_{\Lambda_{12}}\Psi+\mathcal D_\Psi$ with
(4.7) and (4.9). **The $\Psi$ sector does not close off shell.** The defect is proportional to
the $\Psi$ equation of motion $\mathcal F$, with coefficient $+1$ in the normalisation (4.8),
and it starts at $O(g_s^2)$ — before any auxiliary field is introduced, and independently of
the Hubbard–Stratonovich construction. This is the baseline against which question 2 is
judged.

### Verification

Script checks `C1.1`, `C1.2`, `C1.2-order2`, `C1.3`, with break legs; see §7.

## 5. Question 2 — the $\Sigma_2$ sector

### Setup

Assumptions A1–A5, and C1 for the $\Psi$ sector. Local notation: $u_i=\delta_{\Lambda_i}\Psi$,
$X=\Sigma_2-\Psi^{\otimes2}$, $\Phi$ the linear operator of (2.3). Note once and for all:
$u_1,u_2,X,\Sigma_2,\Psi$ are all Grassmann-**even**. The entire $\Sigma_2$ computation
therefore carries **no** reordering sign; every sign in the final answer comes from the
$\Psi$ sector through $[\delta_1,\delta_2]\Psi$.

### Derivation

**(5.0) Absolute-order table.** Every entry below is a *literal* power of $g_s$, with
$\Psi,\Lambda_i,\Sigma_2,X,\tilde X$ counted as $O(g_s^0)$ and $u_i=Q_B\Lambda_i+O(g_s)$.
This table is the order bookkeeping the first pass of this section lacked; the "relative
order" language of §2 grades the *law* $\Phi$, never $\Delta_\Sigma$, and the two must not be
mixed.

| # | term of $[\delta_1,\delta_2]\Sigma_2$ | absolute order | status |
|---|---|---|---|
| T1 | $2\big([\delta_1,\delta_2]\Psi\big)\odot\Psi$, $\delta_{\Lambda_{12}}$-part | $g_s^1$ | kept (in $\Phi(\delta_{\Lambda_{12}}\Psi)$) |
| T2 | $2(u_2\odot u_1-u_1\odot u_2)$, cross term of (a) | $g_s^0$ | **vanishes identically** ($\odot$ symmetric) |
| T3 | $2\,\mathcal D_\Psi\odot\Psi$ | $g_s^2$ | kept — leading defect |
| T4 | $\tfrac{3g_s}{5}p_{2,2}^{-1}p_{3,2}\big(2u_{(1},u_{2)},\Psi\big)$, cross term of (b) | $g_s^1$ | **vanishes identically** (symmetric in $1\!\leftrightarrow\!2$) |
| T5 | $\tfrac{3g_s}{5}p_{2,2}^{-1}p_{3,2}(\mathcal D_\Psi,\Psi,\Psi)$ | $g_s^3$ | kept |
| T6 | $\tfrac{g_s}{10}p_{2,2}^{-1}p_{3,2}(X,\mathcal D_\Psi)$ | $g_s^3$ | kept |
| T7 | $\tfrac{3g_s^2}{50}p_{2,2}^{-1}\big[p_{3,2}(p_{2,2}^{-1}p_{3,2}(u_1,\Psi,\Psi),u_2)-(1\!\leftrightarrow\!2)\big]$ = (5.9) piece 1 | $\mathbf{g_s^2}$ | **artifact** of the $X$ vs $\tilde X$ slip — absent in the exact variables (5.11) |
| T8 | $\tfrac{g_s^2}{100}p_{2,2}^{-1}\big[p_{3,2}(p_{2,2}^{-1}p_{3,2}(X,u_1),u_2)-(1\!\leftrightarrow\!2)\big]$ = (5.9) piece 2 = $[R_{u_2},R_{u_1}]\tilde X$ | $\mathbf{g_s^2}$ | **kept** — $\tilde X$-proportional |
| T9 | $\big[(\partial_\Psi R)_{u_2}[u_1]-(1\!\leftrightarrow\!2)\big]\tilde X=-2\,$T8 | $\mathbf{g_s^2}$ | **kept** — invisible to the truncated law (2.3), which carries $p_{2,2}^{-1}$ where the exact law carries $K_\Psi^{-1}$ |
| T10 | genuine tail: $\Phi_{\rm exact}-\Phi_{\rm trunc}$ applied to $\mathcal D_\Psi$ | $g_s^4$ | dropped |

**The order-counting error of the first pass.** T7–T9 carry $g_s^2$ — the same absolute order
as the leading retained defect T3, and one order *below* T5, T6, which were kept. Declaring
them $O(g_s^4)$ and dropping them is not a truncation. The first pass compounded this with a
second omission: T9 is a $g_s^2$ term that the truncated law (2.3) cannot see at all, so even
the printed remainder (5.9) was not the complete $g_s^2$ remainder. Both are repaired below by
working in the exact variables. Completeness at $g_s^2$ does not rest on this table but on
(5.11), which is exact in $g_s$.

**(5.1) What has to be varied.** $\Phi$ depends on the fields through $\Psi$ (in (a), (b),
(c) via $X$) and through $\Sigma_2$ (in (c) via $X$); $p_{2,2}$ and $p_{3,2}$ are
field-independent, $\mathcal V_4$ and $\mathcal V_5$ being fixed vertices. Hence
$$
\delta_1\big(\delta_2\Sigma_2\big)=\delta_1\big(\Phi(u_2)\big)
=\Phi(\delta_1u_2)+\big(\delta_1\Phi\big)(u_2),
\tag{5.1}
$$
where $(\delta_1\Phi)$ acts on the explicit field dependence of $\Phi$ only.

**(5.2) Term (a): exact cancellation, and the symmetrisation.** With the symmetrised reading
(A4),
$$
\delta_1\big[2\,u_2\odot\Psi\big]=2(\delta_1u_2)\odot\Psi+2\,u_2\odot u_1 ,
\qquad
\big[\,\cdot\,\big]_{\rm antisym}=2\big([\delta_1,\delta_2]\Psi\big)\odot\Psi
+2\big(u_2\odot u_1-u_1\odot u_2\big)
=2\big([\delta_1,\delta_2]\Psi\big)\odot\Psi ,
\tag{5.2}
$$
the last cross term vanishing because $\odot$ is symmetric and $u_1,u_2$ are even. In the
**unsymmetrised** reading $(\mathrm a)=2\,u\otimes\Psi$ the same step leaves
$2(u_2\otimes u_1-u_1\otimes u_2)\in\Lambda^2\mathcal H_0$, a nonzero element of
$\mathcal H_0^{\otimes2}$ at order $g_s^0$ that is not of the form $\Phi(\text{anything})$.
It vanishes identically in $\operatorname{Sym}^2\mathcal H_0$, so the physical answer is
unchanged. The honest statement: **on $\operatorname{Sym}^2\mathcal H_0$ the two readings
agree**, and an ill-posed extension of the unsymmetrised reading to
$\mathcal H_0^{\otimes2}$ fails closure by an element of $\Lambda^2\mathcal H_0$. Since
$\Sigma_2\in\operatorname{Sym}^2\mathcal H_0/\ker\mathcal V_4$ by construction (§1, R13) and
$\delta(\Psi^{\otimes2})=u\otimes\Psi+\Psi\otimes u$ is symmetric anyway, no live convention
is decided here: 039 (3.5) is **confirmed**, not sharpened.

**(5.3) Term (b): cancellation by total symmetry.** Since $p_{3,2}$ is totally symmetric in
its three $\mathcal H_0$ entries,
$$
\delta_1\Big[\tfrac{3g_s}{5}p_{2,2}^{-1}p_{3,2}(u_2,\Psi,\Psi)\Big]
=\tfrac{3g_s}{5}p_{2,2}^{-1}\big[p_{3,2}(\delta_1u_2,\Psi,\Psi)+2\,p_{3,2}(u_2,u_1,\Psi)\big],
\tag{5.3}
$$
and $p_{3,2}(u_2,u_1,\Psi)=p_{3,2}(u_1,u_2,\Psi)$ is symmetric in $1\leftrightarrow2$, so the
cross term drops out of the antisymmetrisation, leaving
$\tfrac{3g_s}{5}p_{2,2}^{-1}p_{3,2}([\delta_1,\delta_2]\Psi,\Psi,\Psi)$.

**(5.4) Term (c): $\Phi$-linear plus a relative $O(g_s^2)$ remainder.**
$$
\delta_1\Big[\tfrac{g_s}{10}p_{2,2}^{-1}p_{3,2}(X,u_2)\Big]
=\tfrac{g_s}{10}p_{2,2}^{-1}\big[p_{3,2}(X,\delta_1u_2)+p_{3,2}(\delta_1X,u_2)\big].
\tag{5.4}
$$
The first term antisymmetrises to $\tfrac{g_s}{10}p_{2,2}^{-1}p_{3,2}(X,[\delta_1,\delta_2]\Psi)$.
The second is $O(g_s^2)$ by (2.4) and is collected in (5.9).

**(5.5) Route 1 — the commutator with the truncated law (2.3).** Adding (5.2), (5.3), (5.4):
$$
[\delta_{\Lambda_1},\delta_{\Lambda_2}]\Sigma_2
=\Phi\big([\delta_{\Lambda_1},\delta_{\Lambda_2}]\Psi\big)+\mathcal A,
\qquad \mathcal A=O(g_s^2)\ \textbf{absolute}
\tag{5.5}
$$
— the commutator on the auxiliary field is the gauge law itself evaluated on the commutator of
the physical variations, **plus a remainder at absolute order $g_s^2$**. No term generated by
the $\Psi$-dependence of $\Phi$ survives the antisymmetrisation at orders $g_s^0,g_s^1$ (T2,
T4 of the table), but the $g_s^2$ entries T7, T8 do survive and are *not* negligible against
the leading defect T3.

**(5.6) The $\mathcal F$-proportional part of the defect.** $\Phi$ is linear, and
$\delta_{\Lambda_{12}}\Sigma_2=\Phi(\delta_{\Lambda_{12}}\Psi)$ by definition of the law, so
with (4.8)
$$
\Delta_\Sigma:=[\delta_{\Lambda_1},\delta_{\Lambda_2}]\Sigma_2-\delta_{\Lambda_{12}}\Sigma_2
=\Phi\big(\mathcal D_\Psi\big)+\mathcal A,
$$
$$
\Phi(\mathcal D_\Psi)
=2\,\mathcal D_\Psi\odot\Psi
+\tfrac{3g_s}{5}p_{2,2}^{-1}p_{3,2}(\mathcal D_\Psi,\Psi,\Psi)
+\tfrac{g_s}{10}p_{2,2}^{-1}p_{3,2}(X,\mathcal D_\Psi),
\tag{5.6}
$$
with $\mathcal D_\Psi$ of (4.9). Written out to $O(g_s^3)$, using
$\mathcal D_\Psi=g_s^2\ell_3(\Lambda_1,\Lambda_2,Q_B\Psi)+O(g_s^3)$:
$$
\Phi(\mathcal D_\Psi)=2g_s^2\,\ell_3(\Lambda_1,\Lambda_2,\mathcal F)\odot\Psi\Big|_{O(g_s^2),O(g_s^3)}
+g_s^3\Big[\tfrac35 p_{2,2}^{-1}p_{3,2}\big(\ell_3(\Lambda_1,\Lambda_2,Q_B\Psi),\Psi,\Psi\big)
+\tfrac1{10}p_{2,2}^{-1}p_{3,2}\big(X,\ell_3(\Lambda_1,\Lambda_2,Q_B\Psi)\big)\Big]
+O(g_s^4),
$$
$$
2g_s^2\,\ell_3(\Lambda_1,\Lambda_2,\mathcal F)\odot\Psi\Big|_{\le O(g_s^3)}
=2g_s^2\,\ell_3(\Lambda_1,\Lambda_2,Q_B\Psi)\odot\Psi
+g_s^3\Big[\ell_3\big(\Lambda_1,\Lambda_2,\ell_2(\Psi,\Psi)\big)
+2\,\ell_4(\Psi,\Lambda_1,\Lambda_2,Q_B\Psi)\Big]\odot\Psi .
\tag{5.7}
$$
Every term of $\Phi(\mathcal D_\Psi)$ carries $\mathcal F$ or one of its pieces, with the
coefficient $+1$ inherited from (4.8) and no free constant anywhere. **This settles the
$\mathcal F$-proportional part of $\Delta_\Sigma$, and nothing else**: the remainder
$\mathcal A$ is a separate $g_s^2$ object, and it is what §§5.8–5.11 determine.

**(5.7) Route 1's remainder.** By (2.4),
$$
\mathcal A=\tfrac{g_s}{10}p_{2,2}^{-1}\big[p_{3,2}(\delta_1X,u_2)-p_{3,2}(\delta_2X,u_1)\big]
=\underbrace{\tfrac{3g_s^2}{50}p_{2,2}^{-1}\big[p_{3,2}\big(p_{2,2}^{-1}p_{3,2}(u_1,\Psi,\Psi),u_2\big)-(1\!\leftrightarrow\!2)\big]}_{\text{T7}}
+\underbrace{\tfrac{g_s^2}{100}p_{2,2}^{-1}\big[p_{3,2}\big(p_{2,2}^{-1}p_{3,2}(X,u_1),u_2\big)-(1\!\leftrightarrow\!2)\big]}_{\text{T8}}
+O(g_s^3).
\tag{5.9}
$$
Both brackets carry $g_s^2$ and $N_{\rm gh}=4$: both are admissible terms of $\Delta_\Sigma$
at the *same* order as the leading term of (5.7).

**(5.8) Why route 1 cannot settle the question.** Two independent defects of (2.3):

1. T7 is proportional to nothing — neither to $\mathcal F$ nor to $X$ — which is already
   suspicious, since a closure defect of an *invariant* action must be supported on the
   equations of motion. It is an artifact: term (c) of (2.3) is written with
   $X=\Sigma_2-\Psi^{\otimes2}$, whose variation $\delta X$ contains the variation of the
   saddle $\tfrac{3g_s}{5}p_{2,2}^{-1}p_{3,2}(u,\Psi,\Psi)=\delta[\tfrac{g_s}{5}p_{2,2}^{-1}v]$.
   The exact law has $\tilde X$ there, and $\delta\tilde X$ is purely homogeneous. T7 is the
   image of that mismatch and disappears in the exact variables [check: `C2.11`].
2. $\mathcal A$ is *incomplete* at $g_s^2$. Term (c) of (2.3) carries $p_{2,2}^{-1}$ where
   the exact law carries $K_\Psi^{-1}$; the missing relative-$O(g_s)$ of that inverse
   contributes a further absolute-$g_s^2$ cross term, T9, which route 1 cannot see at all.

Both defects have the same cause — the truncated law — and both are repaired by redoing the
computation in $(\Psi,\tilde X)$.

**(5.9) Route 2 — the exact variables $(\Psi,\tilde X)$.** Use (2.5), exact in $g_s$. Write
$\delta_i\Sigma_2=D\Sigma_2^*[u_i]+R_{u_i}\tilde X$ and treat the two pieces separately.

*The saddle.* $\Sigma_2^*$ is a function of $\Psi$ alone, so
$\delta_1\big(D\Sigma_2^*[u_2]\big)=D^2\Sigma_2^*[u_1,u_2]+D\Sigma_2^*[\delta_1u_2]$. The
second derivative is symmetric in $(u_1,u_2)$ — both are Grassmann-even, so no sign
intervenes — and drops from the antisymmetrisation:
$$
[\delta_1,\delta_2]\,\Sigma_2^*(\Psi)=D\Sigma_2^*\big[[\delta_1,\delta_2]\Psi\big]
\qquad\textbf{exactly, to all orders in }g_s .
\tag{5.10}
$$
[check: `C2.7`]

*The deviation.* $R_u$ is linear in $u$ and depends on $\Psi$ through $K_\Psi^{-1}$ only, so
$\delta_1\big(R_{u_2}\tilde X\big)=(\partial_\Psi R)_{u_2}[u_1]\,\tilde X+R_{\delta_1u_2}\tilde X
+R_{u_2}R_{u_1}\tilde X$, and, using $\delta_1u_2-\delta_2u_1=[\delta_1,\delta_2]\Psi$,
$$
\boxed{\;
[\delta_1,\delta_2]\tilde X=R_{[\delta_1,\delta_2]\Psi}\tilde X+\mathcal E,
\qquad
\mathcal E=\Big\{(\partial_\Psi R)_{u_2}[u_1]-(1\!\leftrightarrow\!2)\Big\}\tilde X
+\big[R_{u_2},R_{u_1}\big]\tilde X \;}
\tag{5.11}
$$
— **exact, and manifestly proportional to $\tilde X$**. Adding (5.10) and (5.11),
$[\delta_1,\delta_2]\Sigma_2=\Phi_{\rm exact}([\delta_1,\delta_2]\Psi)+\mathcal E$ exactly.

**(5.10) $\mathcal E$ at order $g_s^2$.** Put $A_w:=p_{2,2}^{-1}p_{3,2}(\cdot,\cdot,w)$, a
linear operator on $\operatorname{Sym}^2\mathcal H_0$, self-adjoint with respect to the pairing
$p_{2,2}$. Then $K_\Psi^{-1}=\big(1-\tfrac{g_s}{5}A_\Psi\big)^{-1}p_{2,2}^{-1}$ and
$R_u=\tfrac{g_s}{10}\big(1+\tfrac{g_s}{5}A_\Psi\big)A_u+O(g_s^3)$, so
$$
(\partial_\Psi R)_{u_2}[u_1]=\tfrac{g_s^2}{50}A_{u_1}A_{u_2}+O(g_s^3),
\qquad
[R_{u_2},R_{u_1}]=\tfrac{g_s^2}{100}\big[A_{u_2},A_{u_1}\big]+O(g_s^3),
$$
and the two brackets of (5.11) give $\tfrac{g_s^2}{50}[A_{u_1},A_{u_2}]$ and
$-\tfrac{g_s^2}{100}[A_{u_1},A_{u_2}]$ respectively:
$$
\boxed{\;
\mathcal E=\frac{g_s^2}{100}\,\big[A_{u_1},A_{u_2}\big]\,\tilde X+O(g_s^3),
\qquad A_w=p_{2,2}^{-1}p_{3,2}(\cdot,\cdot,w),\quad u_i=Q_B\Lambda_i+O(g_s) \;}
\tag{5.12}
$$
[check: `C2.9`, `C2.9-g1`, `C2.10`]. There is no $g_s^1$ term; the two $g_s^2$ contributions
do **not** cancel — they add with opposite signs and unequal weights, $\tfrac1{50}-\tfrac1{100}
=\tfrac1{100}$ (the split itself, as opposed to the net $\tfrac1{100}$, is not machine-checked
— `C2.9` verifies only the net coefficient; the split was verified by hand) — and the
commutator $[A_{u_1},A_{u_2}]$ is generically nonzero: $A_{u_1}$ and
$A_{u_2}$ are two $p_{2,2}$-self-adjoint operators with no reason to commute, and they do not
for random totally symmetric $\mathcal V_4,\mathcal V_5$ [check: `C2.9-nonzero`]. Manifestly
antisymmetric in $\Lambda_1\leftrightarrow\Lambda_2$, and $N_{\rm gh}(\mathcal E)=4$ as it must
be ($A_w$ preserves the ghost number of its $\operatorname{Sym}^2$ argument).

**(5.11) The defect, final form.** Since $\Phi_{\rm exact}$ is linear and
$\delta_{\Lambda_{12}}\Sigma_2=\Phi_{\rm exact}(\delta_{\Lambda_{12}}\Psi)$,
$$
\boxed{\;
\Delta_\Sigma=\Phi_{\rm exact}\big(\mathcal D_\Psi\big)+\mathcal E,
\qquad
\Phi_{\rm exact}(\mathcal D_\Psi)=\Phi(\mathcal D_\Psi)+O(g_s^4)\ \text{of (5.6)–(5.7)},
\qquad
\mathcal E=\tfrac{g_s^2}{100}[A_{u_1},A_{u_2}]\tilde X+O(g_s^3) \;}
\tag{5.13}
$$
[check: `C2.12`, the composition check of Part C]. Using R22, $E_\Sigma=-\tfrac{g_s^2}{12}
K_\Psi\tilde X$, i.e. $\tilde X=-\tfrac{12}{g_s^2}K_\Psi^{-1}E_\Sigma$, the second term reads
$$
\mathcal E=-\tfrac{3}{25}\,\big[A_{u_1},A_{u_2}\big]\,p_{2,2}^{-1}E_\Sigma+O(g_s):
$$
**the auxiliary sector does contribute a defect of its own, at the same absolute order $g_s^2$
as the $\mathcal F$-proportional one, and it is proportional to the $\Sigma_2$ equation of
motion.** It carries no new gauge parameter — it is bilinear in the same $\Lambda_1,\Lambda_2$
— and it vanishes on the $\Sigma_2$ shell $\tilde X=0$.

**(5.12) Reconciliation of the two routes.** T8 of (5.9) is exactly $[R_{u_2},R_{u_1}]\tilde X$
(up to the $O(g_s)$ shift between $X$ and $\tilde X$, immaterial inside a $g_s^2$ term), i.e.
$-\mathcal E|_{g_s^2}$; T7 is absent from the exact remainder; and T9 — the
$(\partial_\Psi R)$ term, twice T8 with the opposite sign — is invisible to (2.3). So the
*Regime of validity* reading of the first pass, "(5.9) = the $(\partial_\Psi R)$ and $[R,R]$
terms of the completed-square route", holds for the second bracket only, and only as the
$[R,R]$ half. The two routes never agreed; route 2, which uses the exact law, is the one to keep.

### Commentary

- The structural reason for (5.10)–(5.11) is that the law is *linear in $\delta\Psi$* and
  that the deviation $\tilde X$ transforms *homogeneously*. Linearity is what lets the
  commutator pass through the law; homogeneity is what forces the whole remainder to be
  $\tilde X$-proportional. The compensator can obstruct closure only through its own
  $\Psi$-dependence ($\partial_\Psi R$) or its non-commutativity with itself ($[R,R]$), and
  both of those are $O(g_s^2)$ — *not* "beyond the truncation", since the law is known
  exactly.
- What went wrong in the first pass: the "relative order" grading of §2 grades the law
  $\Phi$, not $\Delta_\Sigma$. A term of relative order $g_s^2$ inside a law whose leading
  term is $O(g_s^0)$ still sits at absolute order $g_s^2$ in the commutator, because the
  fields it multiplies are $O(g_s^0)$. Table (5.0) is the fix: every term graded by its
  literal power of $g_s$.
- Ghost numbers: $N_{\rm gh}(\Delta_\Sigma)=4$. $\mathcal D_\Psi$ has $N_{\rm gh}=2$ and
  $\Phi$ maps $2\mapsto4$ (term (a): $2+2$; term (b): $p_{3,2}$ eats $2+2+2=6$ and
  $\mathcal V_5$ saturates at $10$, so $p_{2,2}^{-1}$ returns $4$). For $\mathcal E$:
  $p_{3,2}(\tilde X,u)$ eats $4+2=6$, leaving a covector dual to $N_{\rm gh}=4$, and
  $p_{2,2}^{-1}$ returns $4$; so $A_w$ preserves $N_{\rm gh}=4$ and $\mathcal E$ has
  $N_{\rm gh}=4$ ✓.
- Both $\Phi(\mathcal D_\Psi)$ and $\mathcal E$ are antisymmetric in
  $\Lambda_1\leftrightarrow\Lambda_2$, at every order, as they must be — for $\mathcal E$
  manifestly, through the operator commutator $[A_{u_1},A_{u_2}]$.
- **Limiting case $g_s\to0$** (C4): (2.5) collapses to $\delta\Sigma_2=\delta(\Psi^{\otimes2})$,
  $\delta\tilde X=0$ (R11), $[\delta_1,\delta_2]\Psi=0$ by (4.2), $\mathcal E=O(g_s^2)\to0$,
  and $\Lambda_{12}=O(g_s)$: the auxiliary field is rigidly slaved to $\Psi^{\otimes2}$ and
  the algebra is the free one.
- **Regime of validity, in the absolute grading.** (5.13) is complete through $g_s^3$ in the
  $\mathcal F$-proportional part — the terms (5.7) — and through $g_s^2$ in the
  $E_\Sigma$-proportional part, where the $g_s^3$ term of $\mathcal E$ was not extracted
  (the script's `part_C` already runs at `GORD=3`, so `E_exact` is exact through $g_s^3$ and
  `sp.diff(E_exact, g, 3)/6` is already computed by the script — the term is cheaper than
  "not computed" suggests, only unextracted; it is simply not needed for the statement).
  What is *not* a
  truncation artifact: the existence and the $\tilde X$-proportionality of $\mathcal E$,
  which follow from (5.11), an identity exact in $g_s$. What *is* limited: the action itself
  is the quintic truncation $S_3$ (A3), so nothing here speaks about $O(g_s^4)$ vertices.

### Result

$$
[\delta_{\Lambda_1},\delta_{\Lambda_2}]\Sigma_2=\delta_{\Lambda_{12}}\Sigma_2
+\Phi_{\rm exact}(\mathcal D_\Psi)+\mathcal E,
$$
with the **same** $\Lambda_{12}$ (4.7) as the $\Psi$ sector and no new gauge parameter. The
algebra does **not** close off shell. It closes modulo **both** equations of motion:

- a part proportional to the $\Psi$ equation of motion, $\Phi_{\rm exact}(\mathcal D_\Psi)$,
  the $\Phi$-image of the $\Psi$-sector defect (4.9) with coefficient $+1$, leading order
  $g_s^2$, written out in (5.6)–(5.7);
- a part proportional to the $\Sigma_2$ equation of motion,
  $\mathcal E=\tfrac{g_s^2}{100}[A_{u_1},A_{u_2}]\tilde X+O(g_s^3)$, at the **same** absolute
  order $g_s^2$, generically nonzero, produced by the rotation term's failure to commute with
  itself and with its own $\Psi$-dependence.

**Retraction.** The first pass of this section concluded that "the auxiliary sector adds no
independent defect, and in particular none proportional to the $\Sigma_2$ equation of motion".
Both clauses are **false**. The error was one of order counting, not of algebra: the remainder
$\mathcal A$ of (5.9) was dropped as $O(g_s^4)$ while carrying $g_s^2$, and the truncated law
(2.3) was used where the exact law (2.5) is available. What survives of the old statement is
the weaker and still useful fact that the auxiliary sector introduces **no new gauge
parameter** and **no defect off the equations of motion**.

### Verification

Script checks `C2.1`–`C2.4`, `C2.6` (route 1, truncated law) and `C2.7`–`C2.12`
(route 2, exact law, including the Part A / Part C composition check `C2.12`), with break
legs; see §7.

## 6. Question 3 — interpretation

### The structure the theory is in

Through $O(g_s^3)$ the pair $(\Psi,\Sigma_2)$ carries an **open gauge algebra with
field-dependent structure functions**, in the standard BV sense
([Erbin2023] app. *QFT tools*, §*Properties of gauge algebra*):
$$
[T_a,T_b]=F_{ab}^{\;c}(\phi)\,T_c+\lambda_{ab}^{\;i}\,\mathcal F_i(\phi).
$$
Reading off from (4.7)–(4.9) and (5.6), with $a,b$ the labels of $\Lambda_1,\Lambda_2$:

- the **field-dependent structure constants** $F$ are those of $\Lambda_{12}$ (4.7); they are
  the *same* in the $\Psi$ row and the $\Sigma_2$ row — there is one gauge parameter and one
  set of structure constants, not two;
- the **$E$-type structure functions** $\lambda_{ab}^{\;i}$ are nonzero against **both**
  equations of motion. Against $\mathcal F$: in the $\Psi$ row
  $\lambda^{\Psi}=\sum_n\frac{g_s^{n+2}}{n!}\ell_{n+3}(\Psi^{\otimes n},\Lambda_1,\Lambda_2,\cdot)$,
  in the $\Sigma_2$ row $\Phi_{\rm exact}\circ\lambda^{\Psi}$, the same object pushed through
  the gauge law. Against $E_\Sigma$: in the $\Sigma_2$ row
  $\lambda^{\Sigma}=-\tfrac{3}{25}[A_{u_1},A_{u_2}]p_{2,2}^{-1}+O(g_s)$, from (5.12)–(5.13).
  The component against the $\Sigma_2$ equation of motion is **nonzero**, at the same
  absolute order $g_s^2$ as the $\mathcal F$-proportional one. $\lambda^\Sigma$ carries
  $g_s^0$ and $\lambda^\Psi$ carries $g_s^2$ only because $E_\Sigma$ is normalised with an
  explicit $g_s^2$; the two defects themselves are of the same order, and neither should be
  read as "leading" relative to the other.

So the theory is open for two distinct reasons. The $\mathcal F$-proportional openness is the
one closed SFT already has — the quartic and higher string products $\ell_{n\ge3}$ — and owes
nothing to the Hubbard–Stratonovich construction; it is present in the effective theory where
no auxiliary field exists. The $E_\Sigma$-proportional openness is genuinely new: it is the
rotation term failing to commute with itself. Neither changes the BV treatment of the
auxiliary sector in kind — the $(\tilde X,\tilde X^+)$ contractible pair of R11/R22 stands,
since $\mathcal E$ vanishes on $\tilde X=0$ and carries no new parameter — but the
$\Sigma_2$ row of the gauge algebra is *not* a passive image of the $\Psi$ row, and the
$O(g_s^4)$ analysis must carry an $E_\Sigma$-proportional term from the start.

### Is the defect of the trivial-symmetry type?

No, and it could not be. A trivial gauge symmetry has the form
$\delta_\mu\phi^i=\mu^{ij}\mathcal F_j$ with $\mu$ graded-antisymmetric; record 016 (R22)
shows that the rotation term's forced generator
$\mu=-\tfrac{6}{5g_s}K_\Psi^{-1}p_{3,2}(\delta\Psi,\cdot)K_\Psi^{-1}$ is graded-**symmetric**
and therefore *not* of that type. The closure defect computed here is a different object
— it is a term in the commutator, not a transformation — and it is
$\mathcal F$-proportional with $\lambda^{\Psi}$ given by $\ell_{n+3}$, which is graded
symmetric in $(\Lambda_1,\Lambda_2)$ in the Grassmann grading, i.e. antisymmetric in the
degree grading (1.2). That is precisely the symmetry a genuine $E$-structure function has,
and it is what distinguishes it from a trivial symmetry.

**Consistency with record 016: full.** 016 argues that the rotation term is (i) not a trivial
symmetry, (ii) not a symmetry at all on its own ($\delta S=-\tfrac{g_s^3}{120}\mathcal V_5
(\tilde X,\tilde X,\delta\Psi)\neq0$ with $\Psi$ fixed), (iii) a compensator attached to
$\delta\Psi$, carrying no independent parameter, with the allowed ambiguity exactly the set of
trivial symmetries. Point (iii) is what this record turns into a computation: *because* the
rotation is a compensator — linear in $\delta\Psi$, with no free parameter of its own, acting
homogeneously on $\tilde X$ — it commutes with the antisymmetrisation *at first order in
itself*, and whatever it produces is forced to be $\tilde X$-proportional. (5.11) is the sharp
form: the compensator obstructs closure only through its own $\Psi$-dependence
($\partial_\Psi R$) and its non-commutativity with itself ($[R,R]$), both $O(g_s^2)$ and both
nonzero. A compensator that generated a defect at its own *leading* order, or a defect not
proportional to $E_\Sigma$, would have contradicted 016's classification; neither happens.

### The working expectation is half right as a mechanism

The working hypothesis was that the gauge algebra closes
only up to equations of motion because of this term. The computation splits this into a
true half and a half-true half.

- **True**: the algebra closes only up to equations of motion.
- **Half true**: *because of this term*. The $\mathcal F$-proportional part of the defect is
  the $\Phi$-image of the $\Psi$-sector $L_\infty$ defect (4.9), present at $O(g_s^2)$ already
  — before the rotation term exists, and in the effective theory where no auxiliary field has
  been introduced at all. That part owes nothing to the rotation term. But the rotation term
  *does* produce a defect of its own, $\mathcal E$ of (5.12), at the same order $g_s^2$ and
  proportional to $E_\Sigma$ — not at first order in the rotation, where it is transparent,
  but at second order, through $[R,R]$ and $\partial_\Psi R$.
- What fails in the informal argument: it infers a *closure* defect from the observation that
  the rotation term is not a symmetry with $\Psi$ frozen. But "not a symmetry with $\Psi$
  frozen" is a statement about $\delta S$, not about $[\delta_1,\delta_2]$. The two are
  independent: a compensator restores invariance of $S$ (which it does, exactly, by
  construction) and, being linear in the variation it compensates, is transparent to the
  commutator at first order in itself. The correct route to a defect is the one the informal
  argument did not take: the compensator is a $\Psi$-dependent *operator*, and two such
  operators evaluated at $u_1,u_2$ do not commute. That is where $E_\Sigma$ enters, and it
  enters at second order in the rotation.

### What this means for the notes and for $O(g_s^4)$

For the quintic subsection: the gauge-transformation paragraph should say that the algebra is
open — as it already is in the nonpolynomial theory, and for the same reason — that the
auxiliary field carries the same gauge parameter with the same field-dependent composition
law and adds no parameter of its own, and that the commutator closes **modulo both equations
of motion**: a $\Psi$-equation term inherited from the nonpolynomial theory, and a
$\Sigma_2$-equation term produced by the auxiliary-sector rotation failing to commute with
itself. It should **not** say that the auxiliary sector makes the algebra open (the openness
pre-exists), and it should **not** say that the auxiliary sector adds nothing (it adds the
$E_\Sigma$-proportional term).

For $O(g_s^4)$ (015 §4): two things change and must be watched. (i) the
$E_\Sigma$-proportional term $\mathcal E$ is already present at $O(g_s^2)$ and must be carried
along, not looked for at the next order;
(ii) the $O(g_s^4)$ $\Sigma_2$ law of 015 §4.2 is *implicit*,
$\delta Y_2=\mathcal K^{-1}[-\tfrac12(\delta\mathcal K)(\cdot,Y_2)
+\tfrac{g_s^2}{20}T(\cdot,Y_2,\delta Y_2)]$, and the $T$-term makes it **non-linear in
$\delta\Psi$** in the elementary presentation. The argument of §5 rests on linearity, so it
does not automatically extend there. In the dressed presentation $T_{\rm dr}=0$ and the law
stays linear in $\delta\Psi$, so the argument does extend: **in the dressed presentation the
auxiliary sector is expected to remain free of an independent closure defect at $O(g_s^4)$;
in the elementary presentation this is open.** That is a concrete prediction, falsifiable by
redoing §5 with the implicit law.

## 7. Verification

`codes/verify-gauge-algebra-ogs3.py`, seed `20260922`, all checks PASS, nonzero exit on any
failure. Two independent parts.

**Part A — the $\Psi$ sector (symbolic, generic products).** The products $\ell_{1..4}$ are
unconstrained formal symbols; words are canonicalised by the graded-antisymmetry rule (1.2);
the generalised Jacobi identities (3.1) are generated for every argument multiset
$\{\Psi^a,\Lambda_1^b,\Lambda_2^c\}$ with $a\le2$, $b,c\le1$, $2\le a+b+c\le4$, and the test
is exact rational membership of the residual in their linear span. This is the METHOD-NOTE
form: the relations are rewriting rules, never equations solved for particular $\ell_n$.

| check | statement | outcome |
|---|---|---|
| `C1.3` | $[\delta_1,\delta_2]\Psi$ has no $O(g_s^0)$ term | PASS (0 terms) |
| `C1.1` | residual through $O(g_s^1)$ in ${\rm span}\,J_n$ | PASS (3 residual words) |
| `C1.2-order2` | residual through $O(g_s^2)$ in ${\rm span}\,J_n$ | PASS (10 residual words) |
| `C1.2` | residual through $O(g_s^3)$ in ${\rm span}\,J_n$ | PASS (21 residual words, span rank 32) |
| `break-C1.1` | $\Lambda_{12}$'s $g_s^2$ coefficient $1\to2$ | correctly FAILS |
| `break-C1.2` | defect coefficient $+1\to-1$ | correctly FAILS |
| `break-C1.2-g3` | $\Lambda_{12}$'s $g_s^3$ coefficient $\tfrac12\to\tfrac13$ | correctly FAILS |

The $O(g_s^3)$ leg is strongly overdetermined (21 words against rank 32 with only the
displayed coefficients free), which is what makes the three break legs meaningful: each
perturbs one rational coefficient and the membership test then fails.

**Part B — the $\Sigma_2$ sector with the truncated law (2.3) (exact rational arithmetic,
$N=\dim\mathcal H_0=2$).** Superseded by Part C for everything concerning $\Delta_\Sigma$;
retained because `C2.1`, `C2.2`, `C2.1-unsym` are statements about that law, and because
`C2.6` is what exhibits the mis-graded remainder.

$\mathcal V_4,\mathcal V_5$ are random totally symmetric integer tensors;
$p_{2,2}^{-1}$ is the exact inverse on the three-dimensional space of symmetric matrices;
$u_1(\Psi),u_2(\Psi)$ are **arbitrary** inhomogeneous quadratic maps, not $L_\infty$ data —
so the identity tested is the one claimed, valid for any $\delta\Psi$ law. $\delta_i$ are
implemented as vector fields on $(\Psi,\Sigma_2)$ and the commutator is the exact vector-field
commutator; everything is polynomial in $(\Psi,\Sigma_2,g_s)$ and compared coefficient by
coefficient, not at sample points.

| check | statement | outcome |
|---|---|---|
| `C2.4` | $[\delta_1,\delta_2]\Sigma_2=\Phi([\delta_1,\delta_2]\Psi)+\mathcal A$, exact in $g_s$ and in the fields | PASS |
| `C2.1` | (a)'s cross terms cancel in the symmetrised reading | PASS |
| `C2.2` | (b)'s cross terms cancel by total symmetry of $p_{3,2}$ | PASS |
| `C2.3` | $\delta X=O(g_s)$ exactly | PASS |
| `C2.6` | the $g_s^2$ coefficient of $\mathcal A$ equals (5.9) — an **absolute** $g_s^2$ term | PASS |
| `C2.6-nonzero` | the T7 bracket of (5.9) is generically nonzero (it is the artifact, see `C2.11`) | PASS |
| `C4` | $g_s\to0$: commutator on $\Sigma_2$ is $2w\odot\Psi$, $\delta X=0$ | PASS |
| `C2.1-unsym` | unsymmetrised reading: residual is exactly $2(u_2\otimes u_1-u_1\otimes u_2)$ | PASS |
| `C2.1-unsym-nonzero` | that residual is nonzero in $\mathcal H_0^{\otimes2}$, antisymmetric, zero in $\operatorname{Sym}^2$ | PASS |
| `break-C2.4` | $\mathcal A\to2\mathcal A$ | correctly FAILS |
| `break-C2.4-coeff` | $\tfrac35\to\tfrac45$ in term (b) of $\Phi$ | correctly FAILS |

**Part C — the $\Sigma_2$ sector in the exact variables $(\Psi,\tilde X)$** (exact rational
arithmetic, $N=2$; $K_\Psi^{-1}$ expanded as a geometric series truncated at $g_s^3$, the only
approximation, one order above the $g_s^2$ where the new claims live). The law is 011
(B.8)–(B.9) = R17, exact in $g_s$; $u_1,u_2$ are again arbitrary polynomial maps, so the
identities hold for any $\delta\Psi$ law.

| check | statement | outcome |
|---|---|---|
| `C2.7` | $[\delta_1,\delta_2]\Sigma_2^*(\Psi)=D\Sigma_2^*[[\delta_1,\delta_2]\Psi]$, second derivative drops | PASS |
| `C2.8` | the remainder $\mathcal E$ of $[\delta_1,\delta_2]\tilde X$ has no $g_s^0$ term | PASS |
| `C2.9` | $\mathcal E\vert_{g_s^2}=\tfrac1{100}[A_{u_1},A_{u_2}]\tilde X$ (eq. (5.12)) | PASS |
| `C2.9-g1` | $\mathcal E$ has no $g_s^1$ term: the leading remainder is exactly $g_s^2$ | PASS |
| `C2.9-nonzero` | that coefficient is generically nonzero (single seed) | PASS |
| `C2.10` | **structural** (tautological from homogeneity of `comm_X` in $\tilde X$): $\mathcal E$ vanishes identically at $\tilde X=0$, consistent with $\mathcal E\propto E_\Sigma$ | PASS |
| `C2.11` | (5.9)'s first bracket T7 is nonzero but absent from $\mathcal E$ (the $X$ vs $\tilde X$ artifact) — the falsifiable content; its second conjunct ($\mathcal E\vert_{g_s^2}$ at $\tilde X=0$ vanishes) is **structural**, the same tautology as `C2.10` | PASS |
| `C2.12` | **composition**: $\Delta_\Sigma=\Phi_{\rm exact}(\mathcal D_\Psi)+\mathcal E$, with $\delta_{\Lambda_{12}}\Sigma_2$ formed explicitly | PASS |
| `break-C2.12` | $\mathcal E\to2\mathcal E$ | correctly FAILS |
| `break-C2.9` | $\tfrac1{100}\to\tfrac2{100}$ in (5.12) | correctly FAILS |

`C2.12` is the composition check the first pass lacked: it forms $\delta_{\Lambda_{12}}\Sigma_2$
as $\Phi_{\rm exact}(\delta_{\Lambda_{12}}\Psi)$ and tests the composition against the
vector-field commutator. The parameter variation is left arbitrary, so the identity holds for
whatever $\Lambda_{12}$ Part A returns; the $L_\infty$ content of $\Lambda_{12}$ and
$\mathcal D_\Psi$ remains Part A's. Parts A and C cannot be joined computationally — Part A
works with abstract $\ell_n$, Part C with explicit $N=2$ tensors. `C2.12` tests the
composition law and the linearity of $\Phi_{\rm exact}$; the identification of
$\mathcal D_\Psi$ with $\sum_n\frac{g_s^{n+2}}{n!}\ell_{n+3}(\Psi^{\otimes n},\Lambda_1,
\Lambda_2,\mathcal F)$ is Part A's alone (C1.2).

**Falsifiability.** Every check compares against an independently constructed object: the
$\Psi$-sector residual against the span of the Jacobi identities (which never sees the claimed
$\Lambda_{12}$ or defect), the $\Sigma_2$-sector commutator (computed as a vector-field
commutator from the law alone) against the closed-form right-hand side (5.5). Each has a break
leg that was run and that fails as required.

**Depth checks run.** Limiting case ($g_s\to0$, C4); a second derivation route for the central
claim (§5.9–5.11, the exact variables, *contradicting* the first route and superseding it,
with the disagreement reconciled term by term in §5.12); symmetry bookkeeping (antisymmetry in
$\Lambda_1\leftrightarrow\Lambda_2$ of both sides, at every order); ghost-number bookkeeping on
every term (§4 and §5 commentaries); regime of validity stated (§5 commentary); comparison
with a literature statement of the $\Psi$-sector algebra (§4 commentary); interpretation (§6).
**Not run**: a numerical cross-check against an explicitly constructed non-trivial $L_\infty$
algebra (e.g. by homotopy transfer) — the symbolic span test is stronger, since it uses
generic unconstrained products; no test of the actual string vertices (the layer A1 excludes
them), so the generic non-vanishing of $[A_{u_1},A_{u_2}]$ is GAP-2; and the $O(g_s^3)$ term
of $\mathcal E$ (GAP-1).

**Check count: 21 checks + 7 break legs** (Part A 4 + 3, Part B 9 + 2, Part C 8 + 2), seed
`20260922`.

## 8. Result

$$
\boxed{\;
\begin{aligned}
[\delta_{\Lambda_1},\delta_{\Lambda_2}]\Psi&=\delta_{\Lambda_{12}}\Psi+\mathcal D_\Psi,
\\
[\delta_{\Lambda_1},\delta_{\Lambda_2}]\Sigma_2&=\delta_{\Lambda_{12}}\Sigma_2
+\Phi_{\rm exact}(\mathcal D_\Psi)+\mathcal E,
\end{aligned}
\qquad
\begin{aligned}
\Lambda_{12}&=\sum_{n\ge0}\frac{g_s^{n+1}}{n!}\,\ell_{n+2}(\Lambda_1,\Lambda_2,\Psi^{\otimes n}),
\\
\mathcal D_\Psi&=\sum_{n\ge0}\frac{g_s^{n+2}}{n!}\,\ell_{n+3}(\Psi^{\otimes n},\Lambda_1,\Lambda_2,\mathcal F),
\\
\mathcal E&=\frac{g_s^2}{100}\big[A_{u_1},A_{u_2}\big]\tilde X+O(g_s^3).
\end{aligned}\;}
$$

**Verdict.** The gauge algebra of the cubic (Hubbard–Stratonovich) theory **does not close off
shell** at $O(g_s^3)$. It closes **modulo both equations of motion**, with both defects
starting at the same absolute order $g_s^2$:

- against the $\Psi$ equation of motion, coefficient $+1$ — explicitly
  $g_s^2\ell_3(\Lambda_1,\Lambda_2,\mathcal F)+g_s^3[\tfrac12\ell_3(\Lambda_1,\Lambda_2,
  \ell_2(\Psi,\Psi))+\ell_4(\Psi,\Lambda_1,\Lambda_2,Q_B\Psi)]$ in the $\Psi$ row and its
  $\Phi$-image (5.6)–(5.7) in the $\Sigma_2$ row;
- against the $\Sigma_2$ equation of motion, in the $\Sigma_2$ row only:
  $\mathcal E=\tfrac{g_s^2}{100}[A_{u_1},A_{u_2}]\tilde X+O(g_s^3)
  =-\tfrac{3}{25}[A_{u_1},A_{u_2}]p_{2,2}^{-1}E_\Sigma+O(g_s)$, generically nonzero.

Both sectors close with the **same** field-dependent parameter $\Lambda_{12}$.

**What the auxiliary sector adds, and what it does not.** It adds **no new gauge parameter**
and **no defect off the equations of motion**. It *does* add an independent,
$E_\Sigma$-proportional closure defect, at the same order as the inherited one. The mechanism
is second order in the rotation term: at first order the compensator is transparent to the
commutator (linear in $\delta\Psi$, homogeneous in $\tilde X$), but $[R_{u_2},R_{u_1}]$ and
$(\partial_\Psi R)$ do not cancel — they combine as $\tfrac1{50}-\tfrac1{100}=\tfrac1{100}$.
The working expectation is right about the conclusion and **half right about
the mechanism**: the $\mathcal F$-proportional openness pre-exists the auxiliary field, but the
rotation term does generate a defect of its own.

**Retraction (first pass of §5).** "The auxiliary sector adds no independent defect" and "none
proportional to the $\Sigma_2$ equation of motion" were stated in six places in the first
version of this record. Both are **false**. The cause was an order-counting error: the
remainder (5.9), carrying $g_s^2$, was relabelled $O(g_s^4)$ by converting a *relative* grading
of the law into an *absolute* grading of the commutator, and the truncated law (2.3) was used
where the exact law (2.5) = R17 is available. Every displayed equation of the first pass is
individually correct, including (5.9); the error is in the grading and in the choice of
variables. See the table (5.0) and §§5.8, 5.12.

**Scope.** Algebraic layer (A1); quintic action $S_3$ (A3) with the $\Sigma_2$ law **exact**
in $g_s$; $\operatorname{Sym}^2$-valued $\Sigma_2$ (A4); the quotient-and-inverse package
PH1 + PH5/R38 (A5), inherited from the gauge law itself, binding on the $\Sigma_2$ row only.
The $\Psi$ row (§4) is unconditional. Open gaps: GAP-1 ($O(g_s^3)$ term of $\mathcal E$),
GAP-2 (non-vanishing of $[A_{u_1},A_{u_2}]$ for the actual vertices, as opposed to generic
symmetric $\mathcal V_4,\mathcal V_5$ at $N=2$), GAP-3 ($\mathcal E$ computed for the R17/011
(B.8) representative of the $\Sigma_2$ law; the $K_\Psi$-antisymmetric part of $R_u$ is not
fixed by invariance of $S_3$, so $\tfrac1{100}$ is representative-dependent — not decided
here).

**Proposed ledger row 1 — $\Psi$ sector, unconditional (R44).**
*Gauge algebra at $O(g_s^3)$, $\Psi$ row.* In the HS form truncated at the quintic order,
$[\delta_{\Lambda_1},\delta_{\Lambda_2}]\Psi=\delta_{\Lambda_{12}}\Psi+\mathcal D_\Psi$ with
$\Lambda_{12}=\sum_n\frac{g_s^{n+1}}{n!}\ell_{n+2}(\Lambda_1,\Lambda_2,\Psi^{\otimes n})$ and
$\mathcal D_\Psi=\sum_n\frac{g_s^{n+2}}{n!}\ell_{n+3}(\Psi^{\otimes n},\Lambda_1,\Lambda_2,
\mathcal F)$, coefficient $+1$: the algebra is open already in the $\Psi$ sector, from
$O(g_s^2)$ on, for the reason closed SFT is open, before any auxiliary field exists. Fixes the
argument ordering left ambiguous in Erbin (2023) (bsft:eq:closed-gauge-alg-cl). Unconditional
(no PH). `Proven – Verified` (`codes/verify-gauge-algebra-ogs3.py` Part A, 4 checks + 3 break
legs, seed 20260922). Source: `agent/derivations/040-gauge-algebra-ogs3.md` §4.

**Proposed ledger row 2 — $\Sigma_2$ sector (R45).**
*Gauge algebra at $O(g_s^3)$, $\Sigma_2$ row.* With the **exact** $\Sigma_2$ law R17/011
(B.8)–(B.9), $[\delta_{\Lambda_1},\delta_{\Lambda_2}]\Sigma_2=\delta_{\Lambda_{12}}\Sigma_2
+\Phi_{\rm exact}(\mathcal D_\Psi)+\mathcal E$ with the **same** $\Lambda_{12}$ and no new
gauge parameter, where $\mathcal E=\{(\partial_\Psi R)_{[u_2}[u_{1]}]+[R_{u_2},R_{u_1}]\}
\tilde X$ is **exactly** $\tilde X$-proportional and equals
$\frac{g_s^2}{100}[A_{u_1},A_{u_2}]\tilde X+O(g_s^3)$,
$A_w:=p_{2,2}^{-1}p_{3,2}(\cdot,\cdot,w)$ — generically nonzero. **Carve-outs:** (i)
non-vanishing of $[A_{u_1},A_{u_2}]$ is established for generic totally symmetric
$\mathcal V_4,\mathcal V_5$ at $N=2$, not for the actual string vertices (GAP-2); (ii)
$\mathcal E$ is computed for the R17/011 (B.8) representative of the $\Sigma_2$ law, whose
$K_\Psi$-antisymmetric part of $R_u$ is not fixed by invariance of $S_3$ (R11 residual
freedom, R22 (2)); the coefficient $\tfrac1{100}$ is therefore representative-dependent, and
whether an admissible redefinition removes $\mathcal E$ is open and not decided here (GAP-3).
So the algebra closes modulo **both** equations of motion, the $E_\Sigma$-proportional defect
appearing at the same absolute order $g_s^2$ as the $\mathcal F$-proportional one, generated by
the rotation compensator at *second* order in itself ($[R,R]$ and $\partial_\Psi R$; it is
transparent at first order, being linear in $\delta\Psi$ and homogeneous in $\tilde X$). Open
BV algebra with $E$-structure functions in both rows; the $(\tilde X,\tilde X^+)$ contractible
pair of R11/R22 is untouched. On $\operatorname{Sym}^2\mathcal H_0$ the symmetrised and
unsymmetrised readings of $2\delta\Psi\odot\Psi$ agree (confirms 039 (3.5)). Corrects the
working expectation (conclusion right, mechanism half right) and supersedes the first pass
of this record, which mis-graded a $g_s^2$ remainder as $O(g_s^4)$.
`Conditional(PH1, PH5) – Verified` (`codes/verify-gauge-algebra-ogs3.py` Parts B and C,
17 checks + 4 break legs, seed 20260922, including the Part A / Part C composition check
`C2.12`). Source: `agent/derivations/040-gauge-algebra-ogs3.md` §5.

## Status

Complete after the §5 re-derivation of 2026-09-22 (second run). Questions 1, 2, 3 answered;
§4 unchanged and unconditional; §5 redone in the exact variables $(\Psi,\tilde X)$ with the
law R17/011 (B.8)–(B.9), superseding the first pass, whose $\Sigma_2$ conclusion is retracted
in §5 *Result* and §8. Claim tree: `Open gaps: GAP-1, GAP-2, GAP-3`;
`Hypotheses in force: PH1, PH5` for C2/C3 only, C1 unconditional. Companion script written,
linted (`ruff`) and passing: **21 checks + 7 break legs**, seed 20260922, exit 0.
Next: orchestrator review / second critic pass on §5 and on the two proposed ledger rows.
