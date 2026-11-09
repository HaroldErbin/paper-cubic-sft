---
description: Tasks 19a+19b – grading of the genus-zero IBL Maurer–Cartan equation (H1 refuted: CFL weight with Psi_2=m_{2,0} needs N_gh=5 order by order or across orders, N_gh(m_{2,g})=5+g across orders, the order-by-order criterion dressing-dependent; output-counting weight makes (Psi,Sigma_2) at (2,4) homogeneous order by order for any N_gh(hbar), across orders for N_gh(hbar)=-1) and the components E_1..E_4 with coefficients; H2 refuted within f=alpha Sigma_2+beta Psi^2, mismatch list M-a..M-s with the baseline items M-b=g_s p12(Psi) (CFL Lemma 9.2) and M-r0=g_s^2 p13(Psi) separated (the quartic SFT fails them with Psi_2=0 or any local Psi_2(Psi)); MC reading conditional on H-par (a single operator on EC, family and coefficient rule named on odd-letter words) and on the double-contraction relations (expected to fail at genus zero)
---

# 103 – Conventions, and the grading of the Maurer–Cartan equation of the raised family (Task 19a)

Brief: `agent/briefs/active-computator-gu-19a-mc-grading-20261018T073600.md`; plan `agent/task-plans/gauge-unfixing-2026-10-13.md`, *Track (2)* and *Task 19*.
Record number 103: 102 is reserved for Task 1 (running in parallel), 103 was free on 2026-10-18.
Script: `codes/verify-ibl-mc-conventions.py`.

## Task and objective

**Literal task (19a).** Build the grading table of the components $E_1$, $E_2$ of $\hat{\mathfrak p}(e^{\mathfrak m})=0$ for the genus-zero raised family, under two assignments of the ghost number of $\hbar$ (CFL degree with $|\hbar|=2d$, $d=\tfrac12$; physical ghost number with $N_{\rm gh}(g_s)=0$), answer H1 twice, and grade $\Lambda_1,\Lambda_2$ relative to $\delta\Psi_1=Q_B\Lambda_1+\dots$.

**Objective.** Harold's reframing (C-01-16): is the cubic theory a gauge-fixed form of a more general $\mathrm{IBL}_\infty$ structure? Its first step is whether $(\Psi,\Sigma_2)$ at ghost numbers $(2,4)$ is a Maurer–Cartan element of the raised family at all. The answer fixes which object plays $\Psi_2$ in Task 20 and under which $\hbar$ assignment.

## Conventions

- Physical ghost number throughout (the project conventions): $N_{\rm gh}(\Psi)=2$, $N_{\rm gh}(\Sigma_2)=4$, $N_{\rm gh}(p_{2,2})=+2$.
- C1 (pairing $\omega_1$, $\Omega(A,B)=(-1)^{|A|}\langle A,B\rangle$), C6 (symmetry types of $\mathcal H^{\wedge n}$, the strand parity of A9), C8 (rule K) – cited, not restated; 19a uses gradings only, 19b uses C6 for the strand parity and the relative coefficients of the components.
- The ghost-number assignments of $\hbar$ and $g_s$ are not in `knowledge/conventions.md`; A6–A8 and A11 below fix them and are proposed as a `local` convention entry.

## Claim tree

- **A1** CFL's $\mathrm{IBL}_\infty$ conventions: $E_kC$ built on $C[1]$; $|\mathfrak p_{k,\ell,g}|=-2d(k+g-1)-1$; $\hat{\mathfrak p}=\sum_{k,\ell\ge1,g\ge0}\hat{\mathfrak p}_{k,\ell,g}\hbar^{k+g-1}\tau^{k+\ell+2g-2}$, $|\hbar|=2d$, $|\tau|=0$; $\hat\phi$ of $\phi:E_kC\to E_\ell C$ is the order-$k$ differential operator of CFL (2.1). [R5 l. 531, l. 538; cited: CFL Def. 2.3 and (2.1)]
- **A2** Degree dictionary: $d=\tfrac12$, and every strand, input or output, has CFL degree $3-N_{\rm gh}$. Forced, not chosen, among role-independent affine dictionaries (one degree per strand of $C$, as in CFL's $E_kC$; with separate affine maps for inputs and outputs $\alpha$ would stay free – critic 21a2 #7): an affine strand degree $\alpha N_{\rm gh}+\beta$ reproduces $\lvert p_{k,\ell,0}\rvert=-2d(k-1)-1$ for all $k,\ell$ iff $3\alpha+\beta=0$, $-2\alpha-\beta=-2d$, $2d-1=0$, i.e. $d=\tfrac12$, $\alpha=-1$, $\beta=3$ (critic 21a F2). The alternative $2-N_{\rm gh}$ of block R is the per-strand $\hbar^{-1}$ dressing (R.1), so the suspension and the $\hbar$-weight are one convention (A2 + A5), not two. [R23 l. 826 (Scope), l. 833 (Reconciliation and Disclosure)]
- **A3** $N_{\rm gh}(p_{k,\ell,g})=3\ell-2k+g$ as a ghost-number shift (out minus in). [R23 l. 823, l. 833]
- **A4** The genus-zero raised family $p_{k,\ell}$ with $k,\ell\ge1$ (CFL's range), in either of R87's two families, $p^{\Omega}_{k,\ell}(B)=(-1)^{|B|}p_{k,\ell}(B)$; truncated at genus zero and $k+\ell\le4$ (with $g_s=\tau$ the weight is $\tau^{k+\ell+2g-2}$, so $p_{1,1,1}$ and $\mathfrak m_{1,1}$ also sit at $O(g_s^2)$: genus zero is an extra truncation, not implied by "through $O(g_s^2)$"; a genus-$g$ term adds $+g$ to both the ghost number and the $\hbar$-power and changes no grading statement). [R87 l. 1823, l. 1835; paper `eq:ibl:raised-family`, `eq:ibl:raised-vs-sprod`]
- **A5** Maurer–Cartan element at genus zero, two strands at most: $\mathfrak m=\hbar^{-1}(\Psi_1+\Psi_2)$, $\Psi_\ell=\mathfrak m_{\ell,0}\in E_\ell C$; the components are those of $e^{-\mathfrak m}\hat{\mathfrak p}(e^{\mathfrak m})$ in $E_1C$, $E_2C$. [cited: CFL Def. 9.1, (9.2), $|\mathfrak m_{\ell,g}|=-2d(g-1)$]
- **A6** $g_s$ is CFL's $\tau$ at genus zero: the generating function weights $p_{m,n}$ by $g_s^{m+n-2}=\tau^{k+\ell-2}$. [R87 l. 1835; paper `eq:ibl:generating`; A1]
- **A7** The two assignments. (a) CFL degree, $|\hbar|=2d=1$, $|\tau|=|g_s|=0$. (b) Physical ghost number, $N_{\rm gh}(g_s)=0$ and $N_{\rm gh}(\hbar)=0$: the assignment the plan asks to test (Task 19, criterion (ii-b)), not implied by the family. [A1, A6; decision recorded in the table, row 0]
- **A8** Gauge parameter $\lambda=\hbar^{-1}(\Lambda_1+\Lambda_2)$ (CFL-uniform weight), entering through $\delta e^{\mathfrak m}=[\hat{\mathfrak p},\lambda]e^{\mathfrak m}$; used for gradings only. [decision; motivation in block Λ]
- **A9** (19b) Tensor form of $E_\ell C$. CFL's $\mathfrak p_{k,\ell,0}$ on a word $c_1\cdots c_k$ is the project's $p_{k,\ell}(c_1,\dots,c_k)$ (the normalization of `eq:ibl:generating`: with $\Psi_2=0$ the $E_1$ component is the original equation of motion, check C8.1), and the paper's $\Psi^2=\Psi\otimes\Psi$ is $\Psi\cdot\Psi$. Strand parity: the registered convention C6 (input strands – fields $\Psi$, $\Psi_2$ and the unfed strands of a $\Psi_2$ – in the physical parity, output strands of the raised products in the shifted parity $N_{\rm gh}+1$); the fields have even strands, $\Psi\in\mathcal H_2$, $\Sigma_2$ with $(2,2)$ strands (`02-2-quartic.tex`, after `eq:hs4:quotient`). The role rule is the project's (C6), not CFL's: CFL's $E_kC$ (Def. 2.3) is one graded-symmetric algebra on $C[1]$, one parity per strand, which at $d=\tfrac12$ (shifted parity on every strand, by R23) annihilates the plain symmetric $\Sigma_2$ (check C8.1-par). The script's `eps_out` gives one-output blocks the physical parity, output letter included; on the sectors used the output strand and the field strand have opposite parities, for which C6's last clause gives the exchange sign $+1$ in either grading, so the difference is immaterial. `eps_out` gives two-output words the shifted parity on *every* letter, leftover field letters included, contrary to C6; this is immaterial for $E_2$, where two-output words have no leftover letters, and would matter for a literal extension to $E_3$, $E_4$ (in $\widehat{p_{2,2}}(\Psi_2,\Psi_2)$ of (MC.9) the two leftover ghost-2 strands would be antisymmetrized), which is why the $E_3$, $E_4$ checks measure ghost numbers on unsymmetrized tensors only (critic 21b2 #7). Multi-string equations of motion: $\mathcal E_\Sigma$ and $\mathcal M_2^{(6)}$ are raised outputs, hence output strands; C6's listing of "equations of motion" among the input strands holds for $\mathcal E_\Psi$ (one strand) and is to be amended for multi-string equations (read literally it would make the ghost-6 comparisons of block H2 compare zeros; critic 21b2 #4). [C6; R87 l. 1835; check C8.1-par]
- **A10** (19b) Ansatz class of H2: $f(\Sigma_2,\Psi)$ is a polynomial, linear in $\Sigma_2$ and of degree $\le2$ in $\Psi$, built from $\Sigma_2$, $\Psi$, the tensor product and the operations $p_{k,\ell}$ ($k,\ell\ge1$) of the family, with coefficients power series in $g_s$ (Laurent coefficients would bring $k+\ell>4$ terms into $O(g_s^2)$; block H2, Scope), independent of $\hbar$; no contraction with the pairing or its inverse, no inverse of $p_{2,2}$. [decision; motivation and what lies outside: block H2]
- **A11** $\hbar$ is an even, central formal variable with free powers; its CFL degree $1$ and its ghost number ($0$ in column (b), $-1$ in the output-counting form) are $\mathbb Z$-grading labels, not tied to Grassmann parity; strand parities follow C6 (A9), so the per-strand dressing $\varphi$ of block R changes no parity and no sign. The alternative – $\hbar$ odd at $d=\tfrac12$ as in a graded-commutative ring – gives $\hbar^2=0$ and makes $\hbar^{-2}\Sigma_2$ meaningless; it is not used. [decision, critic 21a #2; block 0 remark]
- **A12** Two homogeneity criteria: whole component (all $\hbar$-orders of a component at one grading) and order by order in $\hbar$ (each $\hbar$-order, a separate equation by A11, homogeneous on its own); both are answered in C4–C6. [decision, critic 21a #1; block H1 Setup]
- **H-par** (19b; labelled so because H1–H5 are the plan's questions in this record; restated after the last review, critic 21b2 #1, #8) *Setting.* Letters of a word in $EC$ carry a role and a parity (C6): an input-role letter (field, gauge parameter, unfed strand of a field) has the physical parity $\varepsilon$, an output-role letter (an output strand of a raised product) the shifted parity $\varepsilon+1$. *Extended operator.* For $\phi:E_kC\to E_\ell C$ of the genus-zero raised family, $\hat\phi$ on an arbitrary word (odd letters and output-role letters allowed) applies $\phi$ to every $k$-subset of letters – input-role letters directly, output-role letters through rule V – with the Koszul sign of moving those letters to the front computed in their role parities, and places the $\ell$ outputs, as output-role letters, at the front; on words of even input letters this is (MC.1). *Composition rule V (vertex form).* In vertex language every leg of $\mathcal V_{k+\ell}$ is an input in the physical parity, and an output strand of $p_{k,\ell}$ is a leg raised with the odd inverse pairing $\omega^{-1}$ (C1). When an output-role letter $o$ of $\hat\phi$ is taken as an argument by $\hat\phi'$, it is converted back to a vertex leg by $\omega$: the term is defined as the contraction of that leg of $\mathcal V_\phi$ with the corresponding leg of $\mathcal V_{\phi'}$ by $\omega^{-1}$ – the sewing of R87's classical master equation – with the sign of that sewing, R87's sign under the paper's coefficient rule (R87, C3; coefficients moved to the left, passing only basis states), for the `eq:conv:sprod` family – on words with odd letters the two families and the two coefficient rules give different signs, and the hypothesis is stated for this pair; the antibracket on odd inputs is R87's Argued part, so the discharge of H-par on such words also discharges it, and its remaining legs are restored to their roles. This makes $\hat{\mathfrak p}'\circ\hat{\mathfrak p}'$ well defined on all of $EC$, the gauge-parameter words of Task 20 included; the sign of the sewing depends only on the role parities and positions of the letters of the word, so that $\hat\phi$ is one operator on $EC$ and $\hat{\mathfrak p}'\circ\hat{\mathfrak p}'$ is its square. *Statement.* For every pair of operations of the genus-zero raised family with $k+\ell\le4$, the single-contraction part of $\hat\phi'\circ\hat\phi$ (one output of $\phi$ fed to $\phi'$ by rule V), on any word, equals with its sign and coefficient the lift by the extended operator of the corresponding term of R87's antibracket $\{S,S\}$ of the vertex functionals (family and coefficient rule as in rule V); summed over the family it therefore vanishes, i.e. CFL's operator form of the genus-zero relations holds in the C6 algebra. *Motivation.* R87 proves the genus-zero relations in vertex (generating-function) form, where all legs are physical inputs and outputs are legs raised by the odd $\omega^{-1}$; C6's shifted parity on output strands is exactly the parity transported by that odd map (record 076, the $k=2$ check: raised outputs pair non-trivially with input strands), so rule V is the operation C6 was built to pair, and what is hypothesised is only that the Koszul signs of the subset sum in role parities reproduce the antibracket signs term by term, and that the sign of the sewing is local to the word (rule V). *Falsified by:* a finite-model computation, with random graded-symmetric vertices saturating at $2n$ and $\omega$ of C1 (no $L_\infty$ relations needed: both sides are bilinear in the pair of vertices, so the statement is an identity term by term), that implements the extended operator with C6's role parities – not the script's `eps_out`, which differs from C6 on two-output words (A9) – and rule V, and finds, for some pair $(\phi,\phi')$ with $k+\ell\le4$ and some word containing odd letters or output-role letters, a single-contraction term that differs in sign or coefficient from the lifted antibracket term. *Discharged by* that check passing through $k+\ell\le4$, or by a proof. Not run: the existing engine has no role-parity bookkeeping, and adding it exceeds the time box. *Not covered by H-par, and failing in general:* the double-contraction part (two outputs of one operation fed to the next), which at full genus is cancelled by genus-one terms and in the genus-zero truncation requires the involutivity relations (e.g. $\mathfrak p_{2,1,0}\circ_2\mathfrak p_{1,2,0}=0$ in the $(1,1,1)$ relation, which sits at $\tau^2$, inside the truncation, and is cancelled in CFL's relation only by the dropped $p_{k,\ell,1}$), not implied by R87 (Task 17's review l. 161, l. 208). [declared, critics 21b #4, 21a #3, 21b2 #1, #8]
Registered as PH42 (2026-10-22): H-par = PH42.
- **C1** Row 0: in column (a) $\lvert\hbar\rvert=1$, $\lvert g_s\rvert=\lvert\tau\rvert=0$; in column (b) $N_{\rm gh}(\hbar)=N_{\rm gh}(g_s)=0$; $\lvert p_{k,\ell,0}\rvert=-k$ and $N_{\rm gh}(p_{k,\ell,0})=3\ell-2k$. [by A1, A2, A3, A6, A7; block 0] [check: C1]
- **C2** The $E_1$ component (terms 1–5 of block E): $\hbar$-powers $-1,-1,-1,0,0$, $g_s$-powers $k+\ell-2$, $N_{\rm gh}=3,3,3,y-1,y-1$, R87 twist $+1$ on $\Psi_1$-terms and $(-1)^y$ on $\Psi_2$-terms. [by C2.1–C2.3]
  - **C2.1** The list of connected terms and their $\hbar$-, $g_s$-powers. [by A1, A4, A5, A11; eq. (E.1)–(E.2)] [check: C2-C3]
  - **C2.2** Their ghost numbers. [by A3, C2.1; block E] [check: C1, C5]
  - **C2.3** Their twist. [by R87, C2.1] [check: TW]
- **C3** The $E_2$ component (terms 6–12): $\hbar$-powers $-1$ (6–10), $0$ (11–12); $N_{\rm gh}=y+1$ (6–8), $6$ (9–10), $y+2$ (11), $2y-3$ (12); term 6 is the lift of $p_{1,1}$, derived (CFL's $\hat p_{1,1}$ is a derivation), the only one in $E_1\oplus E_2$. [by C3.1–C3.3]
  - **C3.1** List and powers. [by A1, A4, A5, A11; eq. (E.1)–(E.2); cited: CFL Remark 2.2] [check: C2-C3]
  - **C3.2** Ghost numbers, and (E.3) $N_{\rm gh}=2L+\ell_p$ at $y=4$. [by A3, C3.1; eq. (E.3)] [check: C5.3]
  - **C3.3** Twist. [by R87, C3.1] [check: TW]
- **C4** H1 (ii-a): in CFL degree with $\lvert\hbar\rvert=1$ a value exists and is unique, $N_{\rm gh}(\Psi_2)=5\neq4$; H1 as stated is refuted in this column; "homogeneous" is the whole-component criterion of A12. [by A2, A11, A12, C2, C3; eq. (H.1)] [check: C4]
- **C5** H1 (ii-b): in physical ghost number with $N_{\rm gh}(\hbar)=N_{\rm gh}(g_s)=0$ and CFL's weight with $\Psi_2=\mathfrak m_{2,0}$ (A5's placement), no value makes the whole components homogeneous ($E_1$ requires $4$; $E_2$ none); order by order in $\hbar$ the unique value is $5$; $4$ fails both criteria for $\mathfrak m_{2,0}$ (for other dressings the order-by-order criterion differs, C5.4). [by C5.1–C5.4]
  - **C5.1** Whole component: $E_1$ homogeneous iff $y=4$; $E_2$ homogeneous for no $y$. [by A12, C2, C3; eq. (H.2)] [check: C5]
  - **C5.2** Over $N_{\rm gh}(\hbar)=x$ the unique pair making each component homogeneous across $\hbar$-orders is $(x,y)=(-1,5)$; CFL degree equals physical ghost number with $N_{\rm gh}(\hbar)=-1$ component by component. [by A12, C2, C3, A2; eq. (H.3)] [check: C5]
  - **C5.4** Order by order in $\hbar$: CFL's weight with $\Psi_2=\mathfrak m_{2,0}$ requires $y=5$ for every $x$; the output-counting weight (genus label $-1$) is homogeneous at $N_{\rm gh}(\Sigma_2)=4$ for every $x$ (and $\Lambda_2$ at $4$, resp. $3$); for any other integer dressing $\hbar^{-1-n}$, $n\notin\{0,1\}$ ($\mathfrak m_{2,g\ge1}$ included), every value is order-by-order homogeneous, for the components of $E_1\oplus E_2$, within the genus-zero truncation, while across orders $N_{\rm gh}(\mathfrak m_{2,g})=5+g$ with $N_{\rm gh}(\hbar)=-1$. [by A4, A11, A12, C2, C3, C7.1; eq. (H.2'), (H.2''), (H.3')] [check: C5-ord, C5-ord-n]
  - **C5.3** At $y=4$ the $E_2$ obstruction is exactly the one-output sector (the four lifts, ghost 5) against the two-output sector (ghost 6). [by C3.2] [check: C5.3]
- **C6** $\Lambda$ grading: $N_{\rm gh}(\Lambda_1)=1$ in both columns; CFL: $N_{\rm gh}(\Lambda_2)=4$; physical: $\delta\Psi_1$ requires $3$, $\delta\Psi_2$ is inhomogeneous across $\hbar$-orders for every value (already at $\Lambda_2=0$), and order by order (with $\Psi_2$ at $5$) requires $4$; $\hat Q\Lambda_2$ is a lift of $p_{1,1}$, derived under A8. [by A8, A3, A12, C4, C5; block Λ] [check: C6, C5-ord, TW]
- **C7** The second component and the consequence for Task 20. [by C7.1, C7.2]
  - **C7.1** Conjugation by $\varphi$ ($\hbar^{-L}$ on $E_LC$) turns CFL's weight $\hbar^{k+g-1}$ into $\hbar^{\ell+g-1}$; with $\mathfrak m=\hbar^{-1}\Psi+\hbar^{-2}\Sigma_2$, $\lambda=\hbar^{-1}\Lambda_1+\hbar^{-2}\Lambda_2$ and $N_{\rm gh}(\hbar)=-1$, $(\Psi,\Sigma_2;\Lambda_1,\Lambda_2)$ at $(2,4;1,3)$ is homogeneous and at genus zero the $\hbar$-order of a term is $\ell_p-1$; the price is genus label $-1$ on $\Sigma_2$ in CFL's expansion, outside CFL's $g\ge0$ and (9.1). [by A11, C2, C3, C6; eq. (R.1)] [check: C7.1]
  - **C7.2** With $\hbar$ ghost-neutral, the $E_2$ component at $N_{\rm gh}(\Sigma_2)=4$ is two equations, the one-output sector (R.2) at ghost 5 and the two-output sector at ghost 6. [by C5.3, C7.1; block R]
- **C8** (19b) The components with every coefficient, and H2 refuted: for no $f$ of A10 are the quartic-order equations of motion the components, with the mismatch list M-a–M-s, baseline items M-b, M-r0 separated. The exclusion is a statement about the expressions (MC.5)–(MC.9) and uses no hypothesis. Their reading as a gauge-covariant Maurer–Cartan equation needs H-par (as a single operator on $EC$) and the double-contraction relations; the latter fail for the genus-zero truncation unless genus-one terms $p_{k,\ell,1}$ are added, so that reading is conditional on H-par (as a single operator on $EC$) and on an open condition expected to fail (after the last review, critic 21b2 #2). [by C8.1–C8.3; the reading: H-par]
  - **C8.1** The components in the output-counting form are (MC.5) ($E_1$, ghost 3), (MC.6) ($E_2$, $\hbar^0$, ghost 5, the equation (R.2) with its powers of $g_s$) and (MC.7) ($E_2$, $\hbar^1$, ghost 6), every relative coefficient $+$, as tensor equations under C6's parity rule; with the $E_3$, $E_4$ components (MC.8)–(MC.9). [by C8.1.1–C8.1.5]
    - **C8.1.1** Coefficients from CFL (2.1) as the differential operator (MC.1) and the set-partition expansion (MC.2)–(MC.3). [by A1, A4, A9, C3.1; eq. (MC.1)–(MC.4)] [check: C8.1, C8.1-break, C8.2-action]
    - **C8.1.2** Every relative coefficient is $+$, given the operations as defined by the raised family and the parity rule C6: no Koszul sign can arise because all letters are even; the signs of the operations are inherited from R87, not tested (the break leg on the lift of $\ell_2(\Psi,\cdot)$ tests a coefficient). [by A9, R87; block MC, Commentary] [check: C8.1, C8.1-break]
    - **C8.1.3** Agreement with Task 17's question (2): its display, restricted to $k+\ell\le4$ and conjugated by $\mathfrak m_{2,0}=\hbar^{-1}\Sigma_2$, $\varphi^{-1}$, is (MC.5)–(MC.7) term by term. [cited: Task 17's review, l. 94, l. 97; by C7.1, C8.1.1] [check: C8.1-review]
    - **C8.1.5** The $E_3$, $E_4$ components (MC.8)–(MC.9): term list, $\hbar$-, $g_s$-powers and ghost numbers $2L+\ell_p$; coefficients by hand. [by A1, A4, A9, C7.1, eq. (MC.1)–(MC.2), (E.3)] [check: C2-C3-E34]
    - **C8.1.4** No single parity for $E_2C$ holds both $\Sigma_2$ and the two-output terms; with A9's rule every term is a nonzero tensor, and the three equations are separate by ghost number in $\mathcal H^{\otimes2}$ for any value of $\hbar$. [by A9, C5.3; block MC, Commentary] [by check: C8.1-par]
  - **C8.2** H2: no, in reading (I); the obstruction M-b persists in readings (II) and (III). [by C8.2.1–C8.2.9]
    - **C8.2.1** Within A10, $f=\alpha\Sigma_2+\beta\Psi^2$ (ghost counting (H2.1)). [by A10; eq. (H2.1)–(H2.2)]
    - **C8.2.2** $E_1$: (H2.3) requires $\alpha_0=0$ (term $g_s\ell_2(\Psi_2)$) and $\alpha_0=\tfrac16$ (term $\ell_3(\Psi,\Sigma_2)$): M-a. [by C8.1, C8.2.1; eq. (H2.3)] [check: C8.2, C8.2-break]
    - **C8.2.3** $E_2$, ghost 6: $g_sp_{1,2}(\Psi)$ is $f$-independent, present at $\Psi_2=0$ (CFL Lemma 9.2, baseline), and absent from $\mathcal E_\Sigma$ (M-b); without it, $\alpha+\beta=-\tfrac12$, against $0$ from $E_1$ (M-c). [by C8.1, C8.2.1, C8.2.2; eq. (H2.4)] [check: C8.2, C8.2-break]
    - **C8.2.4** $E_2$, ghost 5: (R.2) vanishes identically only for $f\equiv0$; it is a consequence of (H2.0) if $f$ vanishes on its solutions, which in A10 is $f=\alpha(\Sigma_2-\Psi^2)$ on the slice without kernel component (M-d). [by C8.1, C8.2.1, C8.2.6; eq. (H2.5)]
    - **C8.2.5** Reading (II): $f=0$ makes $\mathcal M_1$ an admissible combination and $\mathcal M_2^{(5)}\equiv0$; $\mathcal M_2^{(6)}$ keeps $g_sp_{1,2}(\Psi)$ at field degree one for every $f$. [by C8.2.1, C8.2.3, eq. (H2.1); block H2, reading (II)]
    - **C8.2.6** The quotient: (H2.0) is invariant under $\Sigma_2\to\Sigma_2+N$, $N\in\ker p_{2,2}$; the components are not, for $\alpha\neq0$ (M-q). [by C8.1; block H2, the quotient] [by check: C8.2-quot]
    - **C8.2.7** The composite law leaves $f=\alpha(\Sigma_2-\Psi^2)$ invariant; it is the only $f$ of A10 vanishing on the solutions of (H2.0), up to the kernel component. [by C8.2.1, C8.2.4; block H2, Commentary]
    - **C8.2.8** Reading (III): at first order in the amplitude of a free solution, (MC.7) is $g_sp_{1,2}(\Psi_0)=0$, false whenever $\mathcal V_3(\cdot,\cdot,\Psi_0)\neq0$ [check: C8.2-shell]; likewise the $\hbar^2$ part of (MC.8) is $g_s^2p_{1,3}(\Psi_0)=0$, false whenever $\mathcal V_4(\cdot,\cdot,\cdot,\Psi_0)\neq0$ (M-r0; by hand, not checked). [by C8.1.5, C8.2.3; block H2, reading (III)]
    - **C8.2.9** (MC.5) and (MC.7) are the Euler–Lagrange equations of $S_{\rm MC}$ (H2.6); M-a and M-b are the $\delta_\Psi$ and $\delta_{\Psi_2}$ variations of the coupling $g_s\mathcal V_3(\Psi_2,\Psi)$; the cubic action contains its $\beta$-part and lacks its $\alpha$-part; M-b (and M-r0) are present at $\Psi_2=0$ (CFL Lemma 9.2), so, with $\Psi_2=0$, or any $\Psi_2(\Psi)$ built locally from the family, the original quartic closed SFT is not a Maurer–Cartan element of the raised family either; a $\Psi_2(\Psi)$ containing $p_{2,2}^{-1}$ removes M-b at the price of a modified kinetic operator of $\Psi$ (case (i)). [by C8.1, C8.2.3; eq. (H2.6); scope: block H2, *The baseline*] [by check: C8.2-action]
  - **C8.3** The finite-model checks of C8.1 and C8.2 pass at two seeds, with break legs. [by check: C8.1, C8.1-break, C8.1-par, C8.1-review, C8.2, C8.2-break, C8.2-quot, C8.2-shell, C8.2-action]

Open gaps: none (C8.1–C8.3 closed by 19b; reading (II) rests on the derivation of block H2, not on a check)
Hypotheses in force: H-par (C8: the reading of the components as an $\mathrm{IBL}_\infty$ Maurer–Cartan equation, with $\hat{\mathfrak p}'$ as a single operator on $EC$; the identity comparisons of C8.2 are statements about the expressions (MC.5)–(MC.9) and do not use it); double-contraction relations: an open condition of the same reading, expected to fail for the genus-zero truncation (not a hypothesis: no motivation that they hold); H1 and H2 of the plan are the questions answered by C4, C5 and C8.2, not hypotheses used; A8, A11, A12 are conventions

## Block 0 – row 0: the ghost numbers of $\hbar$ and $g_s$

| | (a) CFL degree | (b) physical ghost number |
|---|---|---|
| $\hbar$ | $\lvert\hbar\rvert=2d=1$ – R5 l. 531 (Scope: "$\lvert\hbar\rvert=2d$"), R23 l. 833 (Disclosure: "$\lvert\hbar\rvert=1$, odd"), $d=\tfrac12$ from R23 l. 826 | $N_{\rm gh}(\hbar)=0$ – the assignment the plan asks to test (Task 19, criterion (ii-b)); not implied by the family: the powers of $\hbar$ come from CFL's weight and from $\mathfrak m$, and block R shows the ghost number of $\hbar$ is free, $-1$ being CFL's |
| $g_s$ | $\lvert\tau\rvert=0$, $g_s=\tau$ at genus zero (A6: R87 l. 1835 against CFL Def. 2.3) | $N_{\rm gh}(g_s)=0$ – decision: R23's formula (l. 823) is for the maps and carries no coupling; the action $\sum_n\tfrac{g_s^{n-2}}{n!}\mathcal V_n(\Psi^n)$, each $\mathcal V_n$ saturating at $\sum N_{\rm gh}=2n$ (R23 l. 833, "inputs at $N_{\rm gh}=2$"), is ghost-neutral term by term only if $g_s$ is |
| per strand | CFL degree $3-N_{\rm gh}$ on every strand (R23 l. 833) | $N_{\rm gh}$ |
| map $p_{k,\ell,0}$ | $\lvert p_{k,\ell,0}\rvert=-2d(k-1)-1=-k$ (R5 l. 538 at $d=\tfrac12$) | $N_{\rm gh}(p_{k,\ell,0})=3\ell-2k$ (R23 l. 823) |
| weight of $\hat p_{k,\ell,0}$ in $\hat{\mathfrak p}$ | $\hbar^{k-1}\tau^{k+\ell-2}$ (A1) | $g_s^{k+\ell-2}$; the $\hbar^{k-1}$ is kept as a label, of ghost number zero |
| $\mathfrak m$ | $\mathfrak m=\hbar^{-1}(\Psi_1+\Psi_2)$, $\lvert\mathfrak m\rvert=0$, so $\lvert\Psi_\ell\rvert=2d=1$ (CFL Def. 9.1) | $\Psi_1=\Psi$, $N_{\rm gh}=2$; $N_{\rm gh}(\Psi_2)$ is what H1 asks |

What R5, R23, R87 leave open, and is decided here: the value $N_{\rm gh}(\hbar)$ in column (b) (zero: the brief's assignment), $N_{\rm gh}(g_s)=0$ (not stated in R23; fixed by the ghost neutrality of the action), and the identification $g_s=\tau$ (A6).
A remark that column (a) needs: at $d=\tfrac12$, $\hbar$ is odd, so in a graded-commutative ring $\hbar^2=0$; this record takes $\hbar$ even, central, with free powers, its degree a $\mathbb Z$-label not tied to Grassmann parity (A11; R23 l. 826 and l. 833: $d=\tfrac12$ is outside CFL's integer-$d$ hypotheses).

## Block E – the terms of the $E_1$ and $E_2$ components

\subsection*{Setup}
A1, A4, A5, A6. Write $y:=N_{\rm gh}(\Psi_2)$. Truncation $k+\ell\le4$ (A4).

\subsection*{Derivation}
For $\phi:E_kC\to E_\ell C$, $\hat\phi$ acts on a product of strands by applying $\phi$ to every $k$-subset of them (CFL (2.1)). Hence
$$
\begin{aligned}
e^{-\mathfrak m}\hat{\mathfrak p}(e^{\mathfrak m})
&=\sum_{k,\ell}\hbar^{k-1}g_s^{k+\ell-2}\sum_{a,b}\frac{\hbar^{-a-b}}{a!\,b!}\,
\bigl[\hat p_{k,\ell}(\Psi_1^{a}\Psi_2^{b})\bigr]_{\rm conn},
\end{aligned}
\tag{E.1}
$$
where "conn" keeps the $k$-subsets that take at least one strand from each of the $a+b$ factors (the other subsets rebuild $e^{\mathfrak m}$ times lower terms and cancel against $e^{-\mathfrak m}$). A term in which $p_{k,\ell}$ takes $t_i\in\{1,2\}$ strands from the $i$-th factor $\Psi_2$ has
$$
\hbar\text{-power}=(k-1)-(a+b),\qquad
g_s\text{-power}=k+\ell-2,\qquad
L=\ell+\textstyle\sum_i(2-t_i)
\tag{E.2}
$$
output strands. Physical ghost number of a term: $N_{\rm gh}=\sum N_{\rm gh}(\text{factors})+3\ell-2k$ (A3). CFL degree of $\hbar^aX$, $X\in E_LC$: $a\lvert\hbar\rvert+3L-N_{\rm gh}(X)$ (A2).

$E_1$ component ($L=1$):

| # | term | coeff. (by hand) | $\hbar$ | $g_s$ | $N_{\rm gh}$, general $y$ | $N_{\rm gh}$ at $y=4$ | CFL degree ($\lvert\hbar\rvert=1$) | R87 twist $p^{\Omega}/p$ |
|---|---|---|---|---|---|---|---|---|
| 1 | $Q_B\Psi_1$ | $1$ | $\hbar^{-1}$ | $g_s^0$ | $3$ | $3$ | $-1$ | $+1$ |
| 2 | $\ell_2(\Psi_1,\Psi_1)$ | $\tfrac12$ | $\hbar^{-1}$ | $g_s^1$ | $3$ | $3$ | $-1$ | $+1$ |
| 3 | $\ell_3(\Psi_1,\Psi_1,\Psi_1)$ | $\tfrac16$ | $\hbar^{-1}$ | $g_s^2$ | $3$ | $3$ | $-1$ | $+1$ |
| 4 | $\ell_2(\Psi_2)$, both strands of $\Psi_2$ | $1$ | $\hbar^{0}$ | $g_s^1$ | $y-1$ | $3$ | $4-y$ | $(-1)^y$ |
| 5 | $\ell_3(\Psi_1,\Psi_2)$ | $1$ | $\hbar^{0}$ | $g_s^2$ | $y-1$ | $3$ | $4-y$ | $(-1)^y$ |

$E_2$ component ($L=2$):

| # | term | coeff. (by hand) | $\hbar$ | $g_s$ | $N_{\rm gh}$, general $y$ | $N_{\rm gh}$ at $y=4$ | CFL degree | R87 twist |
|---|---|---|---|---|---|---|---|---|
| 6 | $\hat Q\Psi_2:=(Q_B\otimes1+1\otimes Q_B)\Psi_2$ – **lift of $p_{1,1}$, derived** | $1$ | $\hbar^{-1}$ | $g_s^0$ | $y+1$ | $5$ | $4-y$ | $(-1)^{N_{\rm gh}(\text{fed strand})}$ |
| 7 | lift of $\ell_2(\Psi_1,\cdot)$ on one strand of $\Psi_2$ | $1$ | $\hbar^{-1}$ | $g_s^1$ | $y+1$ | $5$ | $4-y$ | same |
| 8 | lift of $\ell_3(\Psi_1,\Psi_1,\cdot)$ on one strand of $\Psi_2$ | $\tfrac12$ | $\hbar^{-1}$ | $g_s^2$ | $y+1$ | $5$ | $4-y$ | same |
| 9 | $p_{1,2}(\Psi_1)$ | $1$ | $\hbar^{-1}$ | $g_s^1$ | $6$ | $6$ | $-1$ | $+1$ |
| 10 | $p_{2,2}(\Psi_1,\Psi_1)$ | $\tfrac12$ | $\hbar^{-1}$ | $g_s^2$ | $6$ | $6$ | $-1$ | $+1$ |
| 11 | $p_{2,2}(\Psi_2)$ | $1$ | $\hbar^{0}$ | $g_s^2$ | $y+2$ | $6$ | $4-y$ | $(-1)^y$ |
| 12 | lift of $\ell_3(\Psi_2,\cdot)$ on one strand of a second $\Psi_2$ | $1$ | $\hbar^{0}$ | $g_s^2$ | $2y-3$ | $5$ | $9-2y$ | $(-1)^{y+N_{\rm gh}(\text{fed strand})}$ |

No other connected term with $k,\ell\ge1$, $k+\ell\le4$ lands in $E_1$ or $E_2$ (the enumeration of check C2-C3; e.g. $p_{2,1}$ with one strand from each of two $\Psi_2$ lands in $E_3$).

\subsection*{Commentary}
(E.1): $\hat{\mathfrak p}(e^{\mathfrak m})=e^{\mathfrak m}\cdot e^{-\mathfrak m}\hat{\mathfrak p}(e^{\mathfrak m})$, and $e^{\mathfrak m}$ is invertible, so the components of $e^{-\mathfrak m}\hat{\mathfrak p}(e^{\mathfrak m})$ vanish iff $\hat{\mathfrak p}(e^{\mathfrak m})=0$; the $E_2$ part of $\hat{\mathfrak p}(e^{\mathfrak m})$ itself is $\mathcal E_2+\hbar^{-1}\Psi_1\mathcal E_1$, which has the same grading content. CFL Lemma 9.2 is the special case $\Psi_2=0$, $p_{3,1}=p_{2,2}=0$: terms 1, 2, 9 with $\hbar^{-1}$ (CFL's displayed proof), which (E.2) reproduces.
Terms 6–8 and 12 are produced by $\hat p_{k,1}$ being an order-$k$ differential operator: when the $k$ inputs leave one strand of a $\Psi_2$ unfed, that strand stays as an output. For $k=1$ this is the derivation $\hat Q$ (CFL Remark 2.2: $\hat\phi$ is a derivation if $k=1$). Term 6 is the only occurrence of the lift of $p_{1,1}$ in the two components; it enters as a term of the equation, not as a kinetic term.
Coefficients: $1/(a!\,b!)$ from $e^{\mathfrak m}$, times the number of $k$-subsets realizing the configuration modulo the strand sum that defines the lift; by hand, not machine-checked (signs not tracked; 19b re-derives them).
R87 twist: $p^{\Omega}_{k,\ell}(B)=(-1)^{|B|}p_{k,\ell}(B)$ with $|B|$ the total parity of the fed strands, so the twist is $+1$ on the classical field, on $\Sigma_2$ with strands $(2,2)$ (`02-2-quartic.tex` l. 105: "Each strand carries ghost number two") and on every term at $y=4$ restricted to such strands; at $y=5$ it is $-1$ on terms 4, 5, 11 and component-dependent on the lifts. The grading does not depend on the family.

\subsection*{Result}
$E_1$: terms 1–3 at $\hbar^{-1}$, 4–5 at $\hbar^0$; $E_2$: terms 6–10 at $\hbar^{-1}$, 11–12 at $\hbar^0$; $g_s$-power $k+\ell-2$; ghost numbers as tabulated. With $y=N_{\rm gh}(\Psi_2)$, every term of $E_L$ has
$$
N_{\rm gh}=2L+\ell_p\quad\text{at }y=4,
\tag{E.3}
$$
with $\ell_p$ the number of outputs of the product used ($\ell_p=1$: terms 1–8, 12; $\ell_p=2$: terms 9–11). Proof: the factors carry $2$ per strand on average, so $\sum N_{\rm gh}(\text{factors})=2(k+L-\ell_p)$, and adding $3\ell_p-2k$ gives $2L+\ell_p$.

\subsection*{Verification}
C2-C3: the term list, $\hbar$- and $g_s$-powers of the two tables equal an independent enumeration of the connected configurations of (E.1) (PASS); its break leg (the perturbed rule $\hbar$-power $(k-1)-a-2b$) disagrees with the table (PASS, FAIL-as-expected). NV: no term of $E_1$, $E_2$ vanishes in the model at $y=4,5$, nor any gauge term at $(4,3)$, $(5,4)$, so the homogeneity sets of C4–C6 run over every term (PASS). C1: the shifts $3\ell-2k$ measured in a support-constrained model ($\dim=8$, ghosts $0$–$5$, pairing at $5$, $\mathcal V_n$ at $2n$), both families, two seeds (PASS: $1,4,7,-1,2,-3$ for $p_{11},p_{12},p_{13},p_{21},p_{22},p_{31}$). The ghost-number column is measured on the model for $y=2,\dots,6$ (C4, C5), and (E.3) is checked term by term at $y=4$ (C5.3). TW: the twist column (PASS).

## Block H1 – the two answers

\subsection*{Setup}
Block E; A7; A12. Two homogeneity criteria (A12), both answered:
- *whole component*: all terms of a component, every $\hbar$-order together, have one total grading, $\hbar$ included. This is what makes $\hat{\mathfrak p}(e^{\mathfrak m})$ a homogeneous element of degree $-1$ and CFL Prop. 9.3's twisted structure graded; it is the primary criterion for the comparison with CFL's degree;
- *order by order*: for a formal $\hbar$ each $\hbar$-order is a separate equation (A11), and each must be homogeneous on its own. This is the criterion of Task 17's review, question (1b) (l. 64, l. 70 of that review: "$(2,5)$ if homogeneity is required order by order").

\subsection*{Derivation}
(ii-a) CFL degree, $\lvert\hbar\rvert=1$. From the CFL-degree column: $E_1$ has $\{-1,\,4-y\}$, $E_2$ has $\{4-y,\,-1,\,9-2y\}$, so
$$
E_1\ \text{homogeneous}\iff y=5,\qquad E_2\ \text{homogeneous}\iff y=5 .
\tag{H.1}
$$
This is CFL's requirement $\lvert\mathfrak m_{2,0}\rvert=2d=1$ (Def. 9.1) read through A2: $(3-N_a)+(3-N_b)=1$, i.e. $N_a+N_b=5$.

(ii-b) Physical ghost number, $N_{\rm gh}(\hbar)=N_{\rm gh}(g_s)=0$. From the $N_{\rm gh}$ column: $E_1$ has $\{3,\,y-1\}$, homogeneous iff $y=4$; $E_2$ has $\{y+1,\,6,\,y+2,\,2y-3\}$, and $y+1\ne y+2$ for every $y$, so
$$
E_1\ \text{homogeneous}\iff y=4,\qquad E_2\ \text{homogeneous for no }y .
\tag{H.2}
$$
General assignment $N_{\rm gh}(\hbar)=x$: a term $\hbar^aX$ has total ghost number $N_{\rm gh}(X)+ax$. $E_1$ requires $y=4-x$; $E_2$ requires $y+1-x=6-x=y+2=2y-3$, i.e. $y=5$, $x=-1$. The unique solution is
$$
(x,y)=(-1,5),
\tag{H.3}
$$
so CFL's grading is, component by component, the physical ghost number with $N_{\rm gh}(\hbar)=-1$ (within $E_L$ the CFL degree is $a-N_{\rm gh}(X)+3L$, and $3L$ is fixed).

Order by order (second criterion of the Setup), CFL's weight: $E_1$ at $\hbar^{-1}$ is $\{3\}$, at $\hbar^0$ $\{y-1\}$, homogeneous for every $y$; $E_2$ at $\hbar^{-1}$ is $\{y+1,6\}$, at $\hbar^0$ $\{y+2,2y-3\}$, so
$$
\text{order by order (CFL weight)}:\ E_1\oplus E_2\ \text{homogeneous}\iff y=5,\ \text{for every }x;\qquad
\text{whole component}:\iff (x,y)=(-1,5).
\tag{H.2'}
$$
With $x=-1$ the orders of one component sit at one ghost number; with any other $x$ they are offset by $+(1+x)$ per power of $\hbar$ (from $\hbar^{-1}$ to $\hbar^0$ the total goes from $6-x$ to $7$ at $y=5$). In the output-counting weight of block R ($\Sigma_2=\hbar\Psi_2$ $\hbar$-independent, $\hbar^{\ell_p-1}$ per term), every $\hbar$-order of $E_L$ is homogeneous at $N_{\rm gh}(\Sigma_2)=4$ for every $x$ (by (E.3): $2L+1$ at $\hbar^0$, $2L+2$ at $\hbar^1$), so $(\Psi,\Sigma_2)$ at $(2,4)$ is order-by-order homogeneous also with a ghost-neutral $\hbar$; $x=-1$ is singled out by the whole-component criterion only.

*Dependence on the dressing of the two-string component* (after the last review, critic 21a2 #2). The order-by-order criterion is not a property of the grading alone: it depends on the power of $\hbar$ that dresses the two-string component. Let $\mathfrak m=\hbar^{-1}\Psi+\hbar^{-1-n}S$, $S$ $\hbar$-independent at ghost number $s$: $n=0$ is A5's $\mathfrak m_{2,0}$, $n=1$ is block R's $\Sigma_2$ (genus label $-1$), $n=-g$ is CFL's $\mathfrak m_{2,g}$. By (E.2) a term has $\hbar^{(k-1)-a-(1+n)b}$, and the terms of block E (ghost numbers with $y\to s$) sit at
$$
\begin{array}{c|cccccc}
\text{term} & 1\text{–}3 & 4,5 & 6\text{–}8 & 9,10 & 11 & 12\\\hline
\hbar\text{-power} & -1 & -n & -1-n & -1 & -n & -2n\\
N_{\rm gh} & 3 & s-1 & s+1 & 6 & s+2 & 2s-3
\end{array}
\tag{H.2''}
$$
Order by order: $n=0$ gives $s=5$ ((H.2')), $n=1$ gives $s=4$ (C5.4). For integer $n\notin\{0,1\}$ the four $\hbar$-powers $-1,-n,-1-n,-2n$ are pairwise distinct, so no two terms with different ghost numbers share an order (4–5 and 6–8 are internally equal), and **every $s$ is order-by-order homogeneous** (the components of $E_1\oplus E_2$, A5's truncation), for every $x$. Whole component, with $N_{\rm gh}(\hbar)=x$: $E_2$ requires $s+1-(1+n)x=6-x=s+2-nx=2s-3-2nx$, hence $x=-1$ and $s=5-n$, and $E_1$ ($3-x=s-1-nx$) agrees. So
$$
N_{\rm gh}(\mathfrak m_{2,g})=5+g\quad\text{with }N_{\rm gh}(\hbar)=-1,\ \text{for every dressing},
\tag{H.3'}
$$
which is CFL Def. 9.1, $\lvert\mathfrak m_{2,g}\rvert=-2d(g-1)=1-g$, read through A2 ($6-s=1-g$). In words: the order-by-order criterion fixes $N_{\rm gh}=5$ for $\mathfrak m_{2,0}$ and $4$ for the genus-label-$(-1)$ dressing, and nothing for any other dressing, $\mathfrak m_{2,g\ge1}$ included, within the genus-zero truncation (A4); the whole-component criterion is the invariant one. In particular $\Sigma_2=\mathfrak m_{2,1}$ ($n=-1$, inside CFL's range and CFL's uniform weight $\hbar^{g-1}$) at ghost number $4$ with a ghost-neutral $\hbar$ is order-by-order homogeneous ($E_1$: $3$ at $\hbar^{-1}$, $3$ at $\hbar^1$; $E_2$: $6$ at $\hbar^{-1}$, $5$ at $\hbar^0$, $6$ at $\hbar^1$, $5$ at $\hbar^2$) only because the family has no genus-one operations: $\mathfrak p_{1,2,1}(\Psi)$ would land at $\hbar^{1}\cdot\hbar^{-1}=\hbar^0$ with ghost number $2+4+1=7$, against $s+1$ from terms 6–8, and force $s=6=5+g$. CFL degree puts $\mathfrak m_{2,1}$ at $6$. The table and both conclusions were re-derived here before adoption; check C5-ord-n records them.

\subsection*{Commentary}
(H.2): the obstruction is (E.3): at $y=4$ the $E_2$ terms sit at $4+\ell_p$, i.e. at $5$ for the one-output terms 6, 7, 8, 12 (the lifts, among them the lift of $p_{1,1}$, derived) and at $6$ for the two-output terms 9, 10, 11. Removing the lifts would make $E_2$ homogeneous at $6$ (check C5.3), and the ghost-6 sector has the operations of `eq:hs4:eom-sigma` ($p_{2,2}(\Psi^2)$, $p_{2,2}(\Sigma_2)$) plus $p_{1,2}(\Psi_1)$. Raising $y$ to $5$ moves the lifts to $6$ but moves terms 4, 5 of $E_1$ to $4$ and term 11 to $7$.
(H.3) makes the plan reviewer's observation exact: the powers of $\hbar$ differ between the two $\ell_p$-sectors of $E_2$ ($\hbar^{-1}$ for terms 6–10, $\hbar^0$ for 11–12, at CFL's weight) and between the two parts of $E_1$, and only $x=-1$ compensates.

\subsection*{Result}
- **(ii-a)** In CFL degree with $\lvert\hbar\rvert=2d=1$: yes, a value exists and it is unique, $N_{\rm gh}(\Psi_2)=5$, **not** $4$. H1 as stated ($(2,4)$ homogeneous in CFL's grading) is refuted in this column.
- **(ii-b)** In physical ghost number with $N_{\rm gh}(g_s)=N_{\rm gh}(\hbar)=0$, CFL's weight. *Whole component*: **no** value makes both components homogeneous; $E_1$ alone requires $4$, $E_2$ is inhomogeneous for every value; at $N_{\rm gh}(\Psi_2)=4$ the $E_2$ component splits into a ghost-5 sector (the four lifts) and a ghost-6 sector (the two-output products). *Order by order in $\hbar$*: the unique value is $5$ (H.2'), the review's answer (1b), with the $\hbar^0$ part of each component one unit above its $\hbar^{-1}$ part. H1 ($4$) is refuted in this column under both criteria, for A5's placement $\Psi_2=\mathfrak m_{2,0}$; the refutation does not extend to $\Sigma_2$ at $4$ under every dressing: by (H.2''), $\mathfrak m_{2,1}$ at $4$ passes the order-by-order criterion within the genus-zero truncation.
- The only ghost number of $\hbar$ making each component homogeneous across $\hbar$-orders, with $N_{\rm gh}(\Psi_1)=2$, is $-1$, with $N_{\rm gh}(\Psi_2)=5$ (H.3). Order by order every $x$ works (with $y=5$ in CFL's weight, with $N_{\rm gh}(\Sigma_2)=4$ in the output-counting weight); $-1$ is not unique in that sense.

\subsection*{Verification}
C4: measured ghost numbers, scan $y\in\{2,\dots,6\}$, CFL degree: homogeneous set $\{5\}$ at both seeds (PASS); break legs $\lvert\hbar\rvert=0$ and $\lvert\hbar\rvert=2$ (the integer-$d$ value $d=1$) give the empty set (PASS, FAIL-as-expected). C5: $E_1$ alone $\{4\}$, $E_2$ alone $\varnothing$, both $\varnothing$; over $x\in\{-3,\dots,3\}$ the pairs are $\{(-1,5)\}$; CFL-homogeneity coincides with $x=-1$ at every $y$ (PASS, two seeds). C5.3: (E.3) term by term, the sector split and the homogeneity after removing the lifts (PASS, two seeds). C5-ord (A12): order by order, CFL's weight gives $\{5\}$, the output-counting weight $\{4\}$ for $\Sigma_2$; for $\Lambda_2$ $\{4\}$ (CFL, $y=5$) and $\{3\}$ (output, $y=4$); break leg: the orders merged at $x=0$ give $\varnothing$ (PASS, two seeds). C5-ord-n (final fix pass): dressing $\hbar^{-1-n}$, $n\in\{-2,\dots,3\}$, with the measured ghost numbers and the $\hbar$-powers of the enumeration: order by order $\{5\}$ ($n=0$), $\{4\}$ ($n=1$), the full scan $\{2,\dots,6\}$ otherwise; whole component over $x\in\{-3,\dots,3\}$ only $(-1,5-n)$ (PASS, two seeds); break leg: the rule $\hbar^{-n}$ at $n=1$ gives $\{5\}$, not $\{4\}$ (FAIL as expected). What a wrong result would have done: a wrong $\hbar$-power in block E would break C4 (CFL homogeneity is a theorem of CFL's construction, so the measured CFL degrees test the $\hbar$ column); a wrong $3\ell-2k$ would break C1.

## Block Λ – grading of $\Lambda_1$, $\Lambda_2$

\subsection*{Setup}
A8. Motivation of the weight: CFL Def. 9.7 defines gauge equivalence through a Maurer–Cartan element $\mathfrak M=\sum\mathfrak M_{\ell,g}\hbar^{g-1}$ of a path object, whose $dt$-component is the parameter, so the parameter inherits the uniform weight $\hbar^{g-1}$; for gradings any $\delta e^{\mathfrak m}$ built as $[\hat{\mathfrak p},\lambda]e^{\mathfrak m}$, linear in $\lambda$, gives the same table (Task 20 fixes the form). $\lvert\delta\mathfrak m\rvert=0$ and $\lvert\hat{\mathfrak p}\rvert=-1$ give $\lvert\lambda\rvert=1$. Write $z:=N_{\rm gh}(\Lambda_2)$; the $\hbar$-power below is that of $\delta\Psi_L$ (i.e. relative to $\delta(\hbar^{-1}\Psi_L)$).

\subsection*{Derivation}
Connected terms of $e^{-\mathfrak m}[\hat{\mathfrak p},\lambda]e^{\mathfrak m}$, enumerated as in block E with one factor $\lambda$ feeding at least one strand ($k+\ell\le4$; printed by the script):

| | term | $\hbar$ | $g_s$ | $N_{\rm gh}$ | at $(y,z)=(4,3)$ | at $(5,4)$ |
|---|---|---|---|---|---|---|
| $\delta\Psi_1$ | $Q_B\Lambda_1$ | $\hbar^0$ | $g_s^0$ | $2$ | $2$ | $2$ |
| | $\ell_2(\Psi_1,\Lambda_1)$ | $\hbar^0$ | $g_s^1$ | $2$ | $2$ | $2$ |
| | $\ell_3(\Psi_1,\Psi_1,\Lambda_1)$ | $\hbar^0$ | $g_s^2$ | $2$ | $2$ | $2$ |
| | $\ell_2(\Lambda_2)$ | $\hbar^1$ | $g_s^1$ | $z-1$ | $2$ | $3$ |
| | $\ell_3(\Psi_2,\Lambda_1)$ | $\hbar^1$ | $g_s^2$ | $y-2$ | $2$ | $3$ |
| | $\ell_3(\Psi_1,\Lambda_2)$ | $\hbar^1$ | $g_s^2$ | $z-1$ | $2$ | $3$ |
| $\delta\Psi_2$ | $\hat Q\Lambda_2$ – **lift of $p_{1,1}$, derived under A8** | $\hbar^0$ | $g_s^0$ | $z+1$ | $4$ | $5$ |
| | $p_{1,2}(\Lambda_1)$ | $\hbar^0$ | $g_s^1$ | $5$ | $5$ | $5$ |
| | lift of $\ell_2(\Lambda_1,\cdot)$ on $\Psi_2$ | $\hbar^0$ | $g_s^1$ | $y$ | $4$ | $5$ |
| | lift of $\ell_2(\Psi_1,\cdot)$ on $\Lambda_2$ | $\hbar^0$ | $g_s^1$ | $z+1$ | $4$ | $5$ |
| | $p_{2,2}(\Psi_1,\Lambda_1)$ | $\hbar^0$ | $g_s^2$ | $5$ | $5$ | $5$ |
| | $p_{2,2}(\Lambda_2)$ | $\hbar^1$ | $g_s^2$ | $z+2$ | $5$ | $6$ |
| | lift of $\ell_3(\Psi_1,\Lambda_1,\cdot)$ on $\Psi_2$ | $\hbar^0$ | $g_s^2$ | $y$ | $4$ | $5$ |
| | lift of $\ell_3(\Psi_1,\Psi_1,\cdot)$ on $\Lambda_2$ | $\hbar^0$ | $g_s^2$ | $z+1$ | $4$ | $5$ |
| | lift of $\ell_3(\Psi_2,\cdot)$ on $\Lambda_2$ | $\hbar^1$ | $g_s^2$ | $y+z-3$ | $4$ | $6$ |
| | lift of $\ell_3(\Lambda_2,\cdot)$ on $\Psi_2$ | $\hbar^1$ | $g_s^2$ | $y+z-3$ | $4$ | $6$ |

R87 twist: componentwise $(-1)^{N_{\rm gh}(\text{fed strands})}$, as in block E; it is $-1$ on the terms whose fed inputs are $\Lambda_1$ and $\Psi_1$ only ($\Lambda_1$ odd, R87 l. 1835 "differ by a sign on odd inputs (a gauge parameter) already at one output"), and on the lifts on $\Psi_2$ (lift of $\ell_2(\Lambda_1,\cdot)$, lift of $\ell_3(\Psi_1,\Lambda_1,\cdot)$) it is $(-1)^{1+N_{\rm gh}(\text{fed strand})}$, $-1$ only on $(2,2)$ strands.

\subsection*{Commentary}
$N_{\rm gh}(\Lambda_1)=1$ in both columns, from $\delta\Psi_1\ni Q_B\Lambda_1$ at the same $\hbar$- and $g_s$-power as $\delta\Psi_1$ itself. CFL column ($y=5$, $\lvert\hbar\rvert=1$, i.e. $x=-1$): $\delta\Psi_1$ requires $z-1=2+1$, $\delta\Psi_2$ requires $z+1+1=6$, so $z=4$; then $\lvert\hbar^{-1}\Lambda_2\rvert=-1+(6-4)=1=\lvert\lambda\rvert$. Physical column ($y=4$, $x=0$): $\delta\Psi_1$ requires $z=3$; $\delta\Psi_2$ contains $p_{1,2}(\Lambda_1)$ at $5$ and the lift of $\ell_2(\Lambda_1,\cdot)$ on $\Psi_2$ at $4$, both independent of $z$, so it is inhomogeneous for every $z$, already at $\Lambda_2=0$. The rule (E.3) becomes $N_{\rm gh}=2L+\ell_p-1$ for the gauge terms.

\subsection*{Result}
- CFL degree: $N_{\rm gh}(\Lambda_1)=1$, $N_{\rm gh}(\Lambda_2)=4$ (with $N_{\rm gh}(\Psi_2)=5$).
- Physical ghost number: $N_{\rm gh}(\Lambda_1)=1$; $\delta\Psi_1$ alone requires $N_{\rm gh}(\Lambda_2)=3$ (the paper's value, 07-ibl l. 342); no value makes $\delta\Psi_2$ homogeneous across $\hbar$-orders; order by order (CFL weight, with $N_{\rm gh}(\Psi_2)=5$) the value is $4$ (at $\hbar^0$: $z+1$, $5$, $y$; at $\hbar^1$: $z+2$, $y+z-3$); at $(4,3)$ $\delta\Psi_2$ splits into a ghost-4 sector (one-output terms, among them $\hat Q\Lambda_2$, lift of $p_{1,1}$, derived under A8) and a ghost-5 sector ($p_{1,2}(\Lambda_1)$, $p_{2,2}(\Psi_1,\Lambda_1)$, $p_{2,2}(\Lambda_2)$).

\subsection*{Verification}
C6: every enumerated term measured on the model, both seeds: CFL with $y=5$ gives $z\in\{4\}$; physical with $y=4$ gives $\{3\}$ for $\delta\Psi_1$ and $\varnothing$ for $\delta\Psi_2$ over $z\in\{1,\dots,5\}$ (PASS). TW covers the gauge terms at $(4,3)$ (PASS). Not checked: that $[\hat{\mathfrak p},\lambda]$ is the right transformation (Task 20).

## Block R – what the second component is (stop condition), and the reinterpretation

\subsection*{Setup}
Blocks E, H1, Λ. Let $\varphi$ be the algebra automorphism of $EC\{\hbar,\hbar^{-1}\}$ that multiplies $E_LC$ by $\hbar^{-L}$ (one $\hbar^{-1}$ per strand).

\subsection*{Derivation}
Since $\hat p_{k,\ell,g}$ takes $k$ strands and returns $\ell$,
$$
\varphi^{-1}\,\hat{\mathfrak p}_{k,\ell,g}\hbar^{k+g-1}\,\varphi=\hat{\mathfrak p}_{k,\ell,g}\hbar^{\ell+g-1},
\qquad
\hat{\mathfrak p}(e^{\varphi(\mathfrak m')})=\varphi\bigl(\hat{\mathfrak p}'(e^{\mathfrak m'})\bigr),
\quad
\hat{\mathfrak p}':=\sum\hat{\mathfrak p}_{k,\ell,g}\hbar^{\ell+g-1}.
\tag{R.1}
$$
Take $\mathfrak m'=\Psi+\Sigma_2$, $\hbar$-independent, so that $\mathfrak m=\varphi(\mathfrak m')=\hbar^{-1}\Psi+\hbar^{-2}\Sigma_2$, i.e. $\Sigma_2=\hbar\Psi_2$ in the notation of block E. By (E.2) with the factor weights $\hbar^{-1}$, $\hbar^{-2}$, a term of $E_L$ in $\hat{\mathfrak p}(e^{\mathfrak m})$ has $\hbar^{-L+\ell_p-1}$, hence $\hbar^{\ell_p-1}$ in $\hat{\mathfrak p}'(e^{\mathfrak m'})$. With (E.3) its total ghost number for $N_{\rm gh}(\hbar)=x$ is $2L+\ell_p+(\ell_p-1)x$, constant in $\ell_p$ iff $x=-1$. In degrees: $\varphi$ shifts the degree of $E_LC$ by $-L\lvert\hbar\rvert$, so in the $\hat{\mathfrak p}'$ picture the strand degree is $2-N_{\rm gh}$, $\Psi$ and $\Sigma_2$ have degree $0$, and $\lvert\hat p_{k,\ell,g}\hbar^{\ell+g-1}\rvert=-1$. The same conjugation on the parameter gives $\lambda=\hbar^{-1}\Lambda_1+\hbar^{-2}\Lambda_2$ with $N_{\rm gh}(\Lambda_2)=3$.

\subsection*{Commentary}
(R.1) is the statement that CFL's weight $\hbar^{k+g-1}$ (one $\hbar$ per input beyond the first) and the weight $\hbar^{\ell+g-1}$ (one $\hbar$ per output beyond the first) are conjugate by $\varphi$. Münster–Sachs (arXiv:1109.4101 supplement and arXiv:1208.5626) weight their operators by $x^{n+g-1}$ – output counting, the record's $\hat{\mathfrak p}'$ – and their Maurer–Cartan element $\mathfrak c=\sum x^{n+g-1}c^{n,g}$ enters through $e^{\mathfrak c}$ (review l. 154, l. 369). $\varphi$ maps their genus-zero element $c+\hbar g^{-1}$ to $\hbar^{-1}c+\hbar^{-1}g^{-1}$, CFL's uniform dressing ($n=0$ in (H.2'')), not reading 2 ($\mathfrak m'=\Psi+\Sigma_2$, $n=1$). With the project's family, which needs $N_{\rm gh}(\hbar)=-1$ in their degree-one grading, their convention puts the two-string component at $5$ (supplement l. 387); reading 2's $\Sigma_2$ at $4$ is their $c^{2,-1}$, outside their range as it is outside CFL's. Their own $N_{\rm gh}(g^{-1})=4$ with a neutral $\hbar$ comes from their only two-output datum $\omega_c^{-1}$, shift $2\ell-2k+1=5$ at $(k,\ell)=(0,2)$, while the raised vertices obey A3's $3\ell-2k$. So Münster–Sachs confirm the output-counting operator weight and the genus label $-1$ of reading 2's dressing in both frameworks, and give no precedent for $\Sigma_2$ at $4$ (after the last review, critic 21a2 #3; this replaces the earlier pointer to Task 16). The recommendation of the Consequence stands as a convention, equivalent to reading 1 via $\varphi$, departing from both literature dressings. The cost: $\mathfrak m=\varphi(\mathfrak m')$ has $\mathfrak m_{2,\cdot}=\hbar^{-1}\Sigma_2$, i.e. genus label $g=-1$ in CFL's expansion $\sum\mathfrak m_{\ell,g}\hbar^{g-1}$, outside CFL's range $g\ge0$ and its filtration condition (9.1); on the admissibility of the filtration, Task 17's review answers question (5) (Consequence for Task 20).

\subsection*{Result}
H1 is refuted in the physical-ghost-number column; per the stop condition, the second component is:
1. **with CFL's weight** ($\mathfrak m=\hbar^{-1}(\Psi_1+\Psi_2)$): a different field, a two-string state of total ghost number $5$ – the ghost number of the inverse pairing – with $\Lambda_2$ at $4$;
2. **$\Sigma_2$ itself, after a reinterpretation of the equation**: the output-counting weight (R.1), $\mathfrak m=\hbar^{-1}\Psi+\hbar^{-2}\Sigma_2$, with $N_{\rm gh}(\hbar)=-1$ (equivalently, CFL degree with strand degree $2-N_{\rm gh}$); $(\Psi,\Sigma_2;\Lambda_1,\Lambda_2)$ at $(2,4;1,3)$ is then homogeneous, and at genus zero the $\hbar$-order of each term is $\ell_p-1$ ($\ell_p+g-1$ at genus $g$). The strand degree $2-N_{\rm gh}$ is not an independent choice of suspension: at genus zero the dictionary $3-N_{\rm gh}$ is forced (A2), and $2-N_{\rm gh}$ is that dictionary composed with the per-strand dressing $\varphi$; the pair (CFL weight, $3-N_{\rm gh}$) gives $y=5$, the pair (output weight, $2-N_{\rm gh}$) gives $N_{\rm gh}(\Sigma_2)=4$.
When $\hbar$ carries no ghost number, the $E_2$ component at $N_{\rm gh}(\Sigma_2)=4$ is two equations, separated by ghost number in either weighting, and also by $\hbar$-order in reading 2 (or in reading 1 with $\Psi_2^{\rm CFL}=\hbar^{-1}\Sigma_2$); with CFL's weight and $\Psi_2=\Sigma_2$ $\hbar$-independent, terms 6–8 (ghost 5) and 9–10 (ghost 6) share the order $\hbar^{-1}$, and terms 11 (ghost 6) and 12 (ghost 5) the order $\hbar^0$, so only ghost number separates them. The one-output sector at ghost $5$,
$$
\hat Q\Sigma_2+\widehat{\ell_2(\Psi,\cdot)}\Sigma_2+\tfrac12\widehat{\ell_3(\Psi,\Psi,\cdot)}\Sigma_2+\widehat{\ell_3(\Sigma_2,\cdot)}\Sigma_2=0
\quad(\text{first term: lift of }p_{1,1}\text{, derived}),
\tag{R.2}
$$
and the two-output sector at ghost $6$, built from $p_{1,2}(\Psi)$, $p_{2,2}(\Psi,\Psi)$, $p_{2,2}(\Sigma_2)$ (coefficients and signs: 19b).

\subsection*{Verification}
C7.1: with the weights $\hbar^{-1}$, $\hbar^{-2}$ and measured ghost numbers at $(y,z)=(4,3)$, the four components $E_1$, $E_2$, $\delta\Psi_1$, $\delta\Psi_2$ are CFL-homogeneous and every MC term has $\hbar^{-L+\ell_p-1}$ (PASS, two seeds); break leg: CFL's uniform weight at $y=4$ is not homogeneous (PASS, FAIL-as-expected). The conjugation identity (R.1) is by hand.

## Summary table ($L=1,2$)

| object | CFL degree (CFL weight $\hbar^{-1}$) | $N_{\rm gh}$ required, column (a) | $N_{\rm gh}$ required, column (b) | output-counting form ($\hbar^{-L}$, $N_{\rm gh}(\hbar)=-1$) |
|---|---|---|---|---|
| $\hbar$ | $1$ | $-1$ (equivalent) | $0$ (assigned) | $-1$ |
| $g_s=\tau$ | $0$ | $0$ | $0$ | $0$ |
| $\mathfrak m_{1,0}=\Psi_1$ | $1$ | $2$ | $2$ | $2$, CFL degree $1$ |
| $\mathfrak m_{2,0}=\Psi_2$ | $1$ | $5$ | none across $\hbar$-orders ($E_1$: $4$; $E_2$: none); $5$ order by order | $\Sigma_2=\hbar\Psi_2$: $4$, CFL degree $2$ |
| $\Lambda_1$ | $2$ | $1$ | $1$ | $1$ |
| $\Lambda_2$ | $2$ | $4$ | none across $\hbar$-orders ($\delta\Psi_1$: $3$; $\delta\Psi_2$: none); $4$ order by order (with $\Psi_2$ at $5$) | $3$, CFL degree $3$ |

CFL degrees of an element of $E_LC$: $3L-N_{\rm gh}$ (A2); $\lvert\hbar^{-1}\Psi_L\rvert=0$ and $\lvert\hbar^{-1}\Lambda_L\rvert=1$ fix the second column; the last column uses $\lvert\hbar^{-L}\Sigma_L\rvert=0$, $\lvert\hbar^{-L}\Lambda_L\rvert=1$ (the index $L$ is the strand number, as in block R; the dressing exponent of (H.2'') is $n$, with $\hbar^{-1-n}$ for the second component, so the output-counting form is $n=1$).

## Block MC (19b) – the two components with coefficients and signs

\subsection*{Setup}
A1, A4, A6; the output-counting form of block R (C7.1), inherited verbatim: $\mathfrak m'=\Psi+\Psi_2$, $\hat{\mathfrak p}'=\sum\hat{\mathfrak p}_{k,\ell,0}\hbar^{\ell-1}g_s^{k+\ell-2}$, $N_{\rm gh}(\hbar)=-1$, $N_{\rm gh}(\Psi,\Psi_2)=(2,4)$; A9 (normalization, tensor form, parity of each strand by its role, field strands even). $\Psi_2$ is the second component; H2 sets $\Psi_2=f(\Sigma_2,\Psi)$ (block H2). Notation: $\Psi^2:=\Psi\otimes\Psi$ (the paper's), $\ell_3(\Psi,X)$ is $\ell_3$ with the two strands of $X\in\mathcal H^{\otimes2}$ in two of its slots (the paper's, `eq:hs4:delta-S`), and for a map $\phi$ with one free input
$$
\widehat{\phi}\,X:=(\phi\otimes1+1\otimes\phi)\,X,\qquad X\in\mathcal H^{\otimes2}\ \text{with even strands},
\tag{MC.0}
$$
the derivation extension of $\phi$ to two strands (CFL (2.1)). $\widehat{Q_B}=:\hat Q$ is the **lift of $p_{1,1}$, derived**. $\widehat{\ell_3(\Psi_2,\cdot)}\,\Psi_2$ is (MC.0) with $\phi=\ell_3(\Psi_2,\cdot)$ applied to a second copy of $\Psi_2$.

\subsection*{Derivation}
On words of even letters, CFL's extension (2.1) of $\phi:E_kC\to E_\ell C$ is the differential operator
$$
\hat\phi=\frac1{k!}\,\phi(e_{a_1},\dots,e_{a_k})\,\partial^{a_k}\cdots\partial^{a_1},
\tag{MC.1}
$$
since $\partial^{a_1}\cdots\partial^{a_k}$ on a word sums over ordered $k$-tuples of distinct positions, $k!$ per $k$-subset, and $\phi$ is symmetric on even inputs; the outputs stand to the left. Then $e^{-\mathfrak m'}\partial^{a_1}\cdots\partial^{a_k}e^{\mathfrak m'}$ is the sum over set partitions of $\{1,\dots,k\}$ of products of derivatives of $\mathfrak m'$, and with $\Psi=\psi^ae_a$, $\Psi_2=s^{ab}e_ae_b$ ($s$ symmetric):
$$
\partial^a\mathfrak m'=\psi^a+2s^{ab}e_b,\qquad
\partial^a\partial^b\mathfrak m'=2s^{ab},\qquad
\partial^3\mathfrak m'=0 .
\tag{MC.2}
$$
For $k=1,2,3$ the partitions give $\partial^a$; $\partial^a\partial^b+\partial^{ab}$; $\partial^a\partial^b\partial^c+3\,\partial^{ab}\partial^c$ (symmetrized), and inserting (MC.2) into (MC.1):
$$
\begin{aligned}
e^{-\mathfrak m'}\hat p_{1,\ell}e^{\mathfrak m'}&=p_{1,\ell}(\Psi)+\widehat{p_{1,\ell}}\,\Psi_2,\\
e^{-\mathfrak m'}\hat p_{2,\ell}e^{\mathfrak m'}&=\tfrac12p_{2,\ell}(\Psi^2)+p_{2,\ell}(\Psi_2)+\widehat{p_{2,\ell}(\Psi,\cdot)}\,\Psi_2+\bigl(\text{both strands of two }\Psi_2\text{ left: }E_{\ell+2}\bigr),\\
e^{-\mathfrak m'}\hat p_{3,\ell}e^{\mathfrak m'}&=\tfrac16p_{3,\ell}(\Psi^3)+p_{3,\ell}(\Psi,\Psi_2)+\tfrac12\widehat{p_{3,\ell}(\Psi,\Psi,\cdot)}\,\Psi_2+\widehat{p_{3,\ell}(\Psi_2,\cdot)}\,\Psi_2+\bigl(E_{\ge\ell+2}\bigr).
\end{aligned}
\tag{MC.3}
$$
The coefficients: $\tfrac12\cdot2=1$ for $p_{2,\ell}(\Psi_2)$; $\tfrac12\cdot2\cdot2s=\,$(MC.0) for the lift of $p_{2,\ell}(\Psi,\cdot)$; $\tfrac16\cdot3\cdot2=1$ for $p_{3,\ell}(\Psi,\Psi_2)$; $\tfrac16\cdot3\cdot2s=\tfrac12\,$(MC.0) for the lift of $p_{3,\ell}(\Psi,\Psi,\cdot)$; $\tfrac16\cdot3\cdot2s^{ab}\cdot2s^{cd}e_d=\,$(MC.0) for the lift of $p_{3,\ell}(\Psi_2,\cdot)$. Keeping $k,\ell\ge1$, $k+\ell\le4$, the weights $\hbar^{\ell-1}g_s^{k+\ell-2}$, and sorting by output length $L$ and by $\hbar$-order:
$$
e^{-\mathfrak m'}\hat{\mathfrak p}'(e^{\mathfrak m'})
=\mathcal M_1+\mathcal M_2^{(5)}+\hbar\,\mathcal M_2^{(6)}+\mathcal M_3+\mathcal M_4+O(g_s^3),
\tag{MC.4}
$$
$$
\boxed{\;\mathcal M_1:=Q_B\Psi+\frac{g_s}{2}\,\ell_2(\Psi^2)+\frac{g_s^2}{3!}\,\ell_3(\Psi^3)+g_s\,\ell_2(\Psi_2)+g_s^2\,\ell_3(\Psi,\Psi_2)\;}
\qquad(E_1,\ \hbar^0,\ N_{\rm gh}=3),
\tag{MC.5}
$$
$$
\boxed{\;\mathcal M_2^{(5)}:=\hat Q\,\Psi_2+g_s\,\widehat{\ell_2(\Psi,\cdot)}\,\Psi_2+\frac{g_s^2}{2}\,\widehat{\ell_3(\Psi,\Psi,\cdot)}\,\Psi_2+g_s^2\,\widehat{\ell_3(\Psi_2,\cdot)}\,\Psi_2\;}
\qquad(E_2,\ \hbar^0,\ N_{\rm gh}=5;\ \hat Q:\ \text{lift of }p_{1,1}\text{, derived}),
\tag{MC.6}
$$
$$
\boxed{\;\mathcal M_2^{(6)}:=g_s\,p_{1,2}(\Psi)+\frac{g_s^2}{2}\,p_{2,2}(\Psi^2)+g_s^2\,p_{2,2}(\Psi_2)\;}
\qquad(E_2,\ \hbar^1,\ N_{\rm gh}=6).
\tag{MC.7}
$$
The $E_3$ and $E_4$ components inside the truncation (from the same partitions: a singly fed $\Psi_2$ contributes $2s^{ab}e_b$, i.e. one (MC.0) lift; for $j$ singly fed $\Psi_2$ in one product, $\widehat\phi(\Psi_2,\dots,\Psi_2)$ denotes the sum over one strand of each, with coefficient $1/j!$ from (MC.1)):
$$
\begin{aligned}
\mathcal M_3&=g_s^2\hbar^2\,p_{1,3}(\Psi)
+\hbar\bigl[g_s\,\widehat{p_{1,2}}\,\Psi_2+g_s^2\,\widehat{p_{2,2}(\Psi,\cdot)}\,\Psi_2\bigr]
+\tfrac{g_s}2\,\widehat{\ell_2}(\Psi_2,\Psi_2)+\tfrac{g_s^2}2\,\widehat{\ell_3(\Psi,\cdot,\cdot)}(\Psi_2,\Psi_2)
\quad(\text{gh }9,\ 8,\ 7),
\end{aligned}
\tag{MC.8}
$$
$$
\mathcal M_4=g_s^2\hbar^2\,\widehat{p_{1,3}}\,\Psi_2+\tfrac{g_s^2}2\hbar\,\widehat{p_{2,2}}(\Psi_2,\Psi_2)+\tfrac{g_s^2}6\,\widehat{\ell_3}(\Psi_2,\Psi_2,\Psi_2)
\quad(\text{gh }11,\ 10,\ 9).
\tag{MC.9}
$$
No component beyond $E_4$ occurs ($L\le\ell_p+k\le4$). The term list, the $\hbar$-, $g_s$-powers and the ghost numbers ($2L+\ell_p$, (E.3)) are checked (C2-C3-E34); the coefficients $\tfrac12$, $\tfrac16$ are by hand from (MC.1), not machine-checked (the literal engine expands $e^{\pm\mathfrak m'}$ to word length $4$). The Maurer–Cartan equation through $O(g_s^2)$ at genus zero is $\mathcal M_1=\mathcal M_2^{(5)}=\mathcal M_2^{(6)}=0$ together with every $\hbar$-order of $\mathcal M_3$, $\mathcal M_4$. Every relative coefficient is $+$, given the operations as defined by the raised family and the parity rule C6; no Koszul sign can arise because all letters are even; the signs of the operations themselves are inherited from R87, not tested here.

\subsection*{Commentary}
(MC.1) is CFL (2.1), transplanted to the C6-graded algebra, with $\varepsilon(\rho)=+1$: all letters of $e^{\mathfrak m'}$ are even (A9), so permuting them costs no sign, and CFL's rule has no Koszul sign for $\phi$ passing letters. Outputs of odd maps ($Q_B$, $\ell_2$, $\ell_3$; the even $p_{1,2}$, $p_{2,2}$) stand to the left of the untouched even strands, and moving an odd output past an even strand is free, so (MC.0) has no sign either.
The parity of the strands (A9) needs a statement because the raised family does not respect a single one. The tensor $p_{1,2}(\Psi)$ satisfies $T^{c_2c_1}=(-1)^{(\epsilon_{c_1}+1)(\epsilon_{c_2}+1)}T^{c_1c_2}$: its output strands are graded-symmetric in the shifted parity, as any strand raised with the inverse pairing (ghost number $5$, odd) must be. Its $(3,3)$-strand part – the part that the variation of a $\Sigma_2$ with $(2,2)$ strands sees, through $\langle\delta\Sigma_2,\cdot\rangle_2$ – is a plain symmetric tensor of physically odd strands, and the physical-parity quotient annihilates it; the shifted-parity quotient annihilates the plain symmetric $\Sigma_2$ of physically even strands. With A9's rule every term of (MC.5)–(MC.7) is a nonzero tensor in the sectors used: $\mathcal M_1$ has one strand; the terms of $\mathcal M_2^{(5)}$ have one output strand (ghost number $3$) and one field strand (ghost number $2$), which are of opposite parity in both conventions, so their symmetrization is the plain one either way; $\mathcal M_2^{(6)}$ consists of raised outputs only. (MC.5)–(MC.7) are therefore equations between tensors of $\mathcal H^{\otimes L}$, and no choice of quotient enters them. This is the paper's statement that no single odd symplectic form covers both sectors (`07-ibl.tex`, the paragraph on the auxiliary component), seen in the symmetric algebra: the component $\Psi_2$ of the element and the two-output part $\mathcal M_2^{(6)}$ of its equation cannot both be nonzero in one graded-symmetric $E_2C$ (check C8.1-par). CFL's $EC$ carries one parity per strand; at $d=\tfrac12$ that parity (the shifted one, by R23) annihilates $\Sigma_2$, so this record works in the C6 grading, under hypothesis H-par (with its composition rule V, as a single operator on $EC$) and the double-contraction relations, expected to fail at genus zero, for the reading of the components as a Maurer–Cartan equation. In CFL's native grading the paper's $\Sigma_2\in\mathrm{Sym}^2$ is zero in $E_2C$; the comparison of block H2 exists only in the C6 grading. (MC.3) contains no term with $e^{-\mathfrak m'}$-corrections because the set-partition formula is already the connected part. The family: on even inputs $p^{\Omega}_{k,\ell}=p_{k,\ell}$ (R87, twist $+1$; 19a check TW), so (MC.5)–(MC.7) hold for either family.
The three equations are separate for two reasons, each sufficient: they sit at different $\hbar$-orders ((MC.6) and (MC.7)), and, in $\mathcal H^{\otimes2}$, at different ghost numbers ($5$ and $6$), so their sum vanishes iff each does, whatever value is given to $\hbar$ – also $\hbar=1$, the project's family with no $\hbar$.
Relation to 19a: (MC.5) is terms 1–5 of block E, (MC.6) is terms 6, 7, 8, 12 – the equation (R.2) with its powers of $g_s$ restored – and (MC.7) is terms 9, 10, 11; the coefficients of the tables are confirmed, the signs added.
CFL's uniform weight, $\Psi_2^{\rm CFL}=\hbar^{-1}\Sigma_2$ in $\mathfrak m=\hbar^{-1}(\Psi+\Psi_2^{\rm CFL})$: by (R.1) the components are $\hbar^{-L}$ times (MC.5)–(MC.7), identical equations; only the labels differ ($\mathcal M_2^{(5)}$ at $\hbar^{-2}$, $\mathcal M_2^{(6)}$ at $\hbar^{-1}$, genus label $-1$ on $\Sigma_2$). If instead $\Psi_2^{\rm CFL}$ is an $\hbar$-independent CFL component, it has ghost number $5$ (C4) and cannot be $f(\Sigma_2,\Psi)$ with ghost-neutral coefficients (block H2, (H2.1)): H2 has no content in that reading.

\subsection*{Result}
(MC.5)–(MC.7), with $\Psi_2=f(\Sigma_2,\Psi)$ for H2.

\subsection*{Verification}
See block V19b (checks C8.1, C8.1-break, C8.1-par, C8.1-review).

## Block H2 (19b) – the comparison with the quartic-order equations of motion

\subsection*{Setup}
A10; block MC. The equations of motion (`02-2-quartic.tex`, `eq:hs4:eom-psi`, `eq:hs4:eom-sigma`):
$$
\mathcal E_\Psi=Q_B\Psi+\frac{g_s}{2}\ell_2(\Psi^2)+\frac{g_s^2}{3!}\ell_3(\Psi,\Sigma_2),\qquad
\mathcal E_\Sigma=p_{2,2}(\Psi^2)-p_{2,2}(\Sigma_2),
\tag{H2.0}
$$
with $\Sigma_2\in\mathcal H^{\otimes2}/\ker p_{2,2}$ (`eq:hs4:quotient`) and the composite law $\delta_\Lambda\Sigma_2=2\,\delta_\Lambda\Psi\otimes\Psi$ (`eq:hs4:gauge-sigma`). Three readings of "the equations of motion are the two components for some $f$", from the strictest:
(I) identity: with $\Psi_2=f$, $\mathcal M_1=c_1\mathcal E_\Psi$ and $\mathcal M_2^{(5)}+\hbar\mathcal M_2^{(6)}=c_2\mathcal E_\Sigma$ identically in $(\Psi,\Sigma_2)$ through $O(g_s^2)$, $c_i$ field-independent, and $\mathcal M_3=\mathcal M_4=0$ identically (the equations of motion have no three- or four-strand equation);
(II) equivalence: each component is a combination of $\mathcal E_\Psi,\mathcal E_\Sigma$ with coefficients built from $\Psi$, $\Sigma_2$, the operations and the pairing (no inverse of $p_{2,2}$);
(III) solutions: every solution of (H2.0) gives, with $\Psi_2=f$, a solution of (MC.5)–(MC.7).
(I) is the reading of the brief and of the plan's criterion (iii); (II) and (III) are added to show that the answer does not depend on it.

\subsection*{Derivation}
*The ansatz.* For an expression of A10 with $L$ output strands, built with the products $p$ (each with $\ell_p\ge1$ outputs) from factors whose strands all have ghost number $2$:
$$
N_{\rm gh}=2L+\sum_p\ell_p ,
\tag{H2.1}
$$
since a product adds $3\ell_p-2k_p$ to the ghost number and $\ell_p-k_p$ to the strand count, hence $\ell_p$ to $N_{\rm gh}-2L$ (this is (E.3) for composites). $f$ has $L=2$ and $N_{\rm gh}=4$, so it contains no product, and the two-strand monomials linear in $\Sigma_2$ and of degree $\le2$ in $\Psi$ are $\Sigma_2$ and $\Psi^2$:
$$
f=\alpha\,\Sigma_2+\beta\,\Psi^2,\qquad \alpha=\sum_j\alpha_jg_s^j,\ \beta=\sum_j\beta_jg_s^j .
\tag{H2.2}
$$
*$E_1$.* Inserting (H2.2) into (MC.5), with $\ell_3(\Psi,\Psi^2)=\ell_3(\Psi^3)$:
$$
\mathcal M_1-\mathcal E_\Psi
=g_s\,\alpha\,\ell_2(\Sigma_2)+g_s^2\bigl(\alpha-\tfrac16\bigr)\ell_3(\Psi,\Sigma_2)
+g_s\,\beta\,\ell_2(\Psi^2)+g_s^2\bigl(\beta+\tfrac16\bigr)\ell_3(\Psi^3).
\tag{H2.3}
$$
$c_1=1$ is fixed by $Q_B\Psi$. The four maps are of different field degree ($\Sigma_2$; $\Psi\Sigma_2$; $\Psi^2$; $\Psi^3$), so (H2.3) vanishes through $O(g_s^2)$ iff each coefficient does order by order: the first term gives $\alpha_j=0$ for $j\le1$, the second $\alpha_0=\tfrac16$. **Contradiction**: the two $\Sigma_2$-terms of $\mathcal M_1$ come from the same factor $e^{\Psi_2}$ and carry the same $\alpha$, whereas $\mathcal E_\Psi$ has $\ell_3(\Psi,\Sigma_2)$ without $\ell_2(\Sigma_2)$. Without the term $g_s\ell_2(\Psi_2)$, (H2.3) would vanish for $\alpha=\tfrac16$, $\beta=-\tfrac16$, i.e. $f=\tfrac16(\Sigma_2-\Psi^2)$.

*$E_2$, ghost $6$.* Inserting (H2.2) into (MC.7):
$$
\mathcal M_2^{(6)}=g_s\,p_{1,2}(\Psi)+g_s^2\bigl(\tfrac12+\beta\bigr)p_{2,2}(\Psi^2)+g_s^2\,\alpha\,p_{2,2}(\Sigma_2).
\tag{H2.4}
$$
$g_s\,p_{1,2}(\Psi)$ is independent of $f$ and of degree one in $\Psi$; $\mathcal E_\Sigma$ has no such term, so $\mathcal M_2^{(6)}=c_2\mathcal E_\Sigma$ fails for every $f$. Without it, $\mathcal M_2^{(6)}=c_2\mathcal E_\Sigma$ holds iff $\tfrac12+\beta=-\alpha$ (with $c_2=g_s^2(\tfrac12+\beta)$), i.e. $\alpha+\beta=-\tfrac12$, which contradicts $\alpha+\beta=0$ from $E_1$: the source $\tfrac12g_s^2p_{2,2}(\Psi^2)$, with the weight of $e^{\Psi}$, is a third obstruction, independent of the first two.

*$E_2$, ghost $5$.* $\mathcal E_\Sigma$ has ghost number $6$, so in reading (I) $\mathcal M_2^{(5)}$ must vanish identically. With (H2.2):
$$
\mathcal M_2^{(5)}=\alpha\bigl[\hat Q\Sigma_2+g_s\widehat{\ell_2(\Psi,\cdot)}\Sigma_2+\tfrac{g_s^2}{2}\widehat{\ell_3(\Psi,\Psi,\cdot)}\Sigma_2\bigr]
+2\beta\,\Psi\cdot\bigl[Q_B\Psi+g_s\ell_2(\Psi^2)+\tfrac{g_s^2}{2}\ell_3(\Psi^3)\bigr]
+g_s^2\,\widehat{\ell_3(f,\cdot)}\,f ,
\tag{H2.5}
$$
using $\widehat\phi\,\Psi^2=2\,\phi(\Psi)\cdot\Psi$ (MC.0). Its parts of degree one ($\alpha\hat Q\Sigma_2$, lift of $p_{1,1}$, derived) and two in $\Psi$ ($2\beta\,Q_B\Psi\cdot\Psi$) vanish identically only for $\alpha=\beta=0$, which contradicts $\alpha_0=\tfrac16$. (R.2) has no counterpart among the equations of motion, and in reading (I) it is a fourth obstruction.

*The quotient.* Let $N\in\ker p_{2,2}$. $\mathcal E_\Sigma$ and $\mathcal E_\Psi$ are invariant under $\Sigma_2\to\Sigma_2+N$ (the second because $\langle\delta\Psi,\ell_3(\Psi,N)\rangle=\langle\delta\Psi\otimes\Psi,p_{2,2}(N)\rangle_2=0$, `eq:hs4:same-vertex`). With $\Psi_2=f$, $\mathcal M_1$ changes by $\alpha\,g_s\ell_2(N)$ and $\mathcal M_2^{(5)}$ by $\alpha\,\hat QN+\dots$ ($\hat Q$: lift of $p_{1,1}$, derived), which do not vanish for generic $N$ ($\ell_2$ and $\hat Q$ do not factor through $p_{2,2}$). For $\alpha\ne0$ the components are not defined on $\mathcal H^{\otimes2}/\ker p_{2,2}$; for $\alpha=0$ they do not contain $\Sigma_2$.

*Reading (II).* Allow recombinations. $\ell_3(\Psi,\Psi^2-\Sigma_2)$ is $\mathcal E_\Sigma$ contracted with $\Psi$ on one strand (`eq:hs4:same-vertex`), so $f=0$ gives $\mathcal M_1=Q_B\Psi+\tfrac{g_s}2\ell_2(\Psi^2)+\tfrac{g_s^2}{3!}\ell_3(\Psi^3)=\mathcal E_\Psi+\tfrac{g_s^2}{3!}\ell_3(\Psi,\Psi^2-\Sigma_2)$, an admissible combination, and $\mathcal M_2^{(5)}\equiv0$. $\mathcal M_2^{(6)}$ is not: its part of degree one in the fields is $g_s\,p_{1,2}(\Psi)+g_s^2\alpha\,p_{2,2}(\Sigma_2)$, and the part of degree one of a combination with ghost number $6$ and two strands is a multiple of $p_{2,2}(\Sigma_2)$ (the other equation of degree one, $Q_B\Psi$, would need a map $\mathcal H_3\to\mathcal H^{\otimes2}_6$ of ghost number $3$, and none built from the structure exists: with $D:=N_{\rm gh}-3L$, a product adds $k\ge1$ to $D$, a pairing contraction $+1$, an inverse-pairing insertion $-1$ with $\Delta L=+2$; from $Q_B\Psi$ ($L=1$, $D=0$) to $\mathcal H_6^{\otimes2}$ ($L=2$, $D=0$) the conditions $\Delta D=0$, $\Delta L=1$ force $\sum_i(k_i+\ell_i)=1$, impossible – robust also to the inverse pairing (critic 21b #10); only the $\Psi$ propagator, $\Delta D=-1$, evades it, case (v) of the Scope). The term $g_sp_{1,2}(\Psi)$ survives for every $f$.

*Reading (III).* Take a free solution $\Psi=\varepsilon\Psi_0$, $Q_B\Psi_0=0$, $\Sigma_2=\Psi^2$: (H2.0) holds at $O(\varepsilon)$ (and $\mathcal E_\Sigma=0$ exactly), $f=O(\varepsilon^2)$, and (MC.7) at $O(\varepsilon)$ is $g_s\,p_{1,2}(\Psi_0)=0$. This fails whenever the cubic vertex $\mathcal V_3(\cdot,\cdot,\Psi_0)$ does not vanish – for any $f$ of A10, and more generally for any $f$ with no term linear in $\Psi$ alone.

\subsection*{Commentary}
(H2.1) is the counting that makes A10 small; the excluded constructions are those that change it: a pairing contraction lowers $N_{\rm gh}-2L$ by one (scalars such as $\langle\Psi,Q_B\Psi\rangle$ times $\Sigma_2$, of field degree three, change nothing in (H2.3) at degree one and two), an $\hbar$-dependent $f$ moves terms between the $\hbar$-orders, which are separate equations anyway, and the inverse of $p_{2,2}$ – the propagator of $\Sigma_2$ – allows $f\ni-g_s^{-1}p_{2,2}^{-1}p_{1,2}(\Psi)$, which removes $p_{1,2}(\Psi)$ from (MC.7) and puts $-\ell_2\,p_{2,2}^{-1}p_{1,2}(\Psi)$ into $\mathcal M_1$ at $O(g_s^0)$: a change of the kinetic operator of $\Psi$, not $\mathcal E_\Psi$.
A unifying observation (the reason for the list): (MC.5) and (MC.7) are the Euler–Lagrange equations, for $\delta\Psi$ and $\delta\Psi_2$, of
$$
S_{\rm MC}(\Psi,\Psi_2)=\sum_{n\ge2}g_s^{n-2}\,\mathcal V_n\bigl((e^{\Psi+\Psi_2})_n\bigr)-\mathcal V_2(\Psi_2)
=S_{\le4}(\Psi)+g_s\,\mathcal V_3(\Psi_2,\Psi)+\frac{g_s^2}{2}\mathcal V_4(\Psi_2,\Psi^2)+\frac{g_s^2}{2}\mathcal V_4(\Psi_2,\Psi_2)+O(g_s^3),
\tag{H2.6}
$$
where $(e^{\Psi+\Psi_2})_n$ is the length-$n$ part of the exponential in the symmetric algebra and $\mathcal V_2(\Psi_2)$, which has no input ($p_{0,2}$), is excluded by CFL's $k\ge1$. Indeed $\delta_\Psi$ of the three added terms gives $g_s\ell_2(\Psi_2)+g_s^2\ell_3(\Psi,\Psi_2)$ and $\delta_{\Psi_2}$ gives (MC.7) through $\langle A\otimes B,p_{m,2}(X)\rangle_2=\mathcal V_{m+2}(A,B,X)$. The cubic action is instead $S_{\le4}(\Psi)-\tfrac{g_s^2}{4!}\mathcal V_4(\Sigma_2-\Psi^2,\Sigma_2-\Psi^2)$. The coupling $g_s\mathcal V_3(\Psi_2,\Psi)$ is the common origin of $g_s\ell_2(\Psi_2)$ in (MC.5) and $g_sp_{1,2}(\Psi)$ in (MC.7); $\mathcal M_2^{(5)}$ is not a variation of (H2.6) and comes from the lifts alone. At the level of actions the quadratic terms would also need $\tfrac{\alpha^2}{2}=-\tfrac1{4!}$, no real $\alpha$ – item M-s of the table, which does not enter readings (I)–(III) since $c_2$ absorbs the sign. Task 17's review (l. 103) calls $\mathfrak p_{2,1,0}(\mathfrak m_{2,0})$ – both strands of a two-string factor fed into one operation, M-a – a genus-one, one-loop term; in the output-counting form it sits at $\hbar^0$ next to tree terms because $\Sigma_2$ carries the genus label $-1$ (block R): whether $\Sigma_2$ is read as a composite of two strings (M-a a missing tree coupling) or as a two-boundary object (M-a a loop term) is exactly what that label hides.
The composite law: $f$ with $\alpha+\beta=0$, $f=\alpha(\Sigma_2-\Psi^2)$, is invariant under $\delta\Sigma_2=2\delta\Psi\otimes\Psi$ in $E_2C$ ($\pi(2\delta\Psi\otimes\Psi)=\pi(\delta(\Psi^2))$), and is the only $f$ of A10 that vanishes on the solutions of (H2.0), up to the kernel component. The composite law therefore acts trivially on the candidate second component, whereas the transformation of a Maurer–Cartan element has $\delta\Psi_2\ni g_s\,p_{1,2}(\Lambda_1)$ (block Λ); the comparison is Task 20's (H4).

\subsection*{Result}
**H2: no.** For no $f(\Sigma_2,\Psi)$ of A10 (linear in $\Sigma_2$, degree $\le2$ in $\Psi$, coefficients power series in $g_s$) are the quartic-order equations of motion the components (MC.5)–(MC.7) and the $E_3$, $E_4$ components (MC.8)–(MC.9), in reading (I); the obstruction (MC.7) $\ni g_sp_{1,2}(\Psi)$ persists in readings (II) and (III).
**The baseline.** M-b is independent of $f$ and of $\Sigma_2$ and present at $\Psi_2=0$: it is CFL Lemma 9.2's second condition, $\mathfrak p_{1,2,0}(\mathfrak m_{1,0})=0$, i.e. $p_{1,2}(\Psi)=0$, and with it the source $\tfrac{g_s^2}2p_{2,2}(\Psi^2)$ and $g_s^2p_{1,3}(\Psi)$ (M-r0). Scope of this negative statement: with $\Psi_2=0$, or any $\Psi_2(\Psi)$ built locally from the family, the original quartic closed SFT is not a Maurer–Cartan element of the raised family either; a $\Psi_2(\Psi)$ containing $p_{2,2}^{-1}$ removes M-b at the price of a modified kinetic operator of $\Psi$ (case (i)). At $\Psi_2=0$ the $E_2$, $E_3$ components are $g_sp_{1,2}(\Psi)+\tfrac{g_s^2}2p_{2,2}(\Psi^2)$ and $g_s^2p_{1,3}(\Psi)$, constraints that theory does not impose. M-b and M-r0 are therefore obstructions of the raised family against any tree-level closed SFT, not defects of the cubic action; removing them means switching the cobracket off on the classical field, i.e. the step back to the $L_\infty$ truncation $(\ell=1,g=0)$ of R5. The mismatches specific to the Hubbard–Stratonovich form are M-a ($\alpha$-part), M-c (the coefficient), M-d, M-e, M-q, the $f$-dependent part of M-r and the action-level item M-s.
The mismatch list, each item named by its operation (list complete for $E_1$–$E_4$ within genus zero, $k+\ell\le4$):

| # | term | side | where | removable by $f$? |
|---|---|---|---|---|
| M-a | $g_s\,\ell_2(\Psi_2)$: $\ell_2$ fed with both strands of the $2$-string component | MC only | $E_1$, $\hbar^0$, gh 3 | no: tied to $g_s^2\ell_3(\Psi,\Psi_2)$ by $e^{\Psi_2}$ (H2.3); its $\alpha$-part gives $\alpha_0=0$ against $\alpha_0=\tfrac16$, its $\beta$-part $g_s\beta\,\ell_2(\Psi^2)$ gives $\beta_0=0$ against $\beta_0=-\tfrac16$ from $\ell_3(\Psi^3)$ |
| M-b | $g_s\,p_{1,2}(\Psi)$: the cobracket (raised $\ell_2$, $\Delta\circ\ell_2$) on the classical field; present at $\Psi_2=0$ (CFL Lemma 9.2), baseline | MC only | $E_2$, $\hbar^1$, gh 6 | no: $f$-independent, every reading; the original quartic theory fails it too, with $\Psi_2=0$ or any local $\Psi_2(\Psi)$ (a $\Psi_2(\Psi)\ni p_{2,2}^{-1}$ removes it at the price of case (i)) |
| M-c | $\tfrac{g_s^2}{2}p_{2,2}(\Psi^2)$ with the weight of $e^{\Psi}$ against $g_s^2p_{2,2}(\Psi_2)$ | MC (coefficient) | $E_2$, $\hbar^1$, gh 6 | no: needs $\alpha+\beta=-\tfrac12$, $E_1$ needs $0$ |
| M-d | (R.2): $\hat Q\Psi_2$ (lift of $p_{1,1}$, derived), lifts of $\ell_2(\Psi,\cdot)$, $\tfrac12\ell_3(\Psi,\Psi,\cdot)$, $\ell_3(\Psi_2,\cdot)$ | MC only | $E_2$, $\hbar^0$, gh 5 | only by $f\equiv0$; a consequence of (H2.0) if $f$ vanishes on its solutions, which in A10 is $f=\alpha(\Sigma_2-\Psi^2)$ on the slice without kernel component |
| M-e | $\tfrac{g_s^2}{3!}\ell_3(\Psi,\Sigma_2)$ without $\ell_2(\Sigma_2)$; no $\ell_3(\Psi^3)$ | EOM only | $\mathcal E_\Psi$ | the $\ell_3$ part yes ($f=\tfrac16(\Sigma_2-\Psi^2)$), only once M-a is removed |
| M-q | invariance under $\Sigma_2\to\Sigma_2+N$, $N\in\ker p_{2,2}$ | EOM only | both | no for $\alpha\ne0$: $\ell_2(N)$, $\hat QN$ in the MC components |
| M-r0 | $g_s^2\,p_{1,3}(\Psi)$, (MC.8): the three-output product on the classical field; present at $\Psi_2=0$, baseline like M-b | MC only | $E_3$, $\hbar^2$, gh 9 | no: $f$-independent; false at first order on a free solution ($\mathcal V_4(\cdot,\cdot,\cdot,\Psi_0)\ne0$) |
| M-r | the $f$-dependent terms of (MC.8)–(MC.9): $g_s\hbar\,\widehat{p_{1,2}}\Psi_2$, $g_s^2\hbar\,\widehat{p_{2,2}(\Psi,\cdot)}\Psi_2$ ($E_3$, gh 8); $\tfrac{g_s}2\widehat{\ell_2}(\Psi_2,\Psi_2)$, $\tfrac{g_s^2}2\widehat{\ell_3(\Psi,\cdot,\cdot)}(\Psi_2,\Psi_2)$ ($E_3$, gh 7); $g_s^2\hbar^2\widehat{p_{1,3}}\Psi_2$ (gh 11), $\tfrac{g_s^2}2\hbar\,\widehat{p_{2,2}}(\Psi_2,\Psi_2)$ (gh 10), $\tfrac{g_s^2}6\widehat{\ell_3}(\Psi_2,\Psi_2,\Psi_2)$ (gh 9) ($E_4$) | MC only | $E_3$, $E_4$ | only by $f\equiv0$: the EOM have no three- or four-strand equation, so in reading (I) each must vanish identically; the parts of lowest field degree ($\alpha g_s\widehat{p_{1,2}}\Sigma_2$, $2\beta g_s\,p_{1,2}(\Psi)\cdot\Psi$) do so only for $\alpha=\beta=0$ |
| M-s | action level: the quadratic terms need $\tfrac{\alpha^2}2=-\tfrac1{4!}$, no real $\alpha$ | both | (H2.6) against the cubic action | outside readings (I)–(III), since $c_2$ absorbs the sign |

M-a ($\alpha$-part) and M-b are the $\delta_\Psi$ and $\delta_{\Psi_2}$ variations of $g_s\mathcal V_3(\Psi_2,\Psi)$ in $S_{\rm MC}$ (H2.6); with $\Psi_2=f$ the cubic action contains its $\beta$-part ($g_s\mathcal V_3(\beta\Psi^2,\Psi)$ renormalizes $\tfrac{g_s}{3!}\mathcal V_3(\Psi^3)$) and lacks its $\alpha$-part. M-b, the $\delta_{\Psi_2}$ variation, exists at $\Psi_2=0$ and is not tied to the coupling's $\Psi$-variation: in $S_{\rm MC}$ it is the response of the vertex functional to a two-string source, which the quartic theory has as well.

### Scope of the exclusion

- *Class.* $f$ of A10: polynomial, linear in $\Sigma_2$, of degree $\le2$ in $\Psi$, built from the fields, the tensor product and the operations of the family, coefficients power series in $g_s$ (a negative power would bring terms with $k+\ell>4$ down to $O(g_s^2)$, outside the truncation; the script's system with powers $-2,\dots,2$ has more unknowns and is inconsistent, so the power-series system is a fortiori), $\hbar$-independent; by (H2.1) this is $f=\alpha\Sigma_2+\beta\Psi^2$. Physical reason: these are the local redefinitions built from the theory's own data at the order of the truncation, and the brief's ansatz; the paper's on-shell value $\Sigma_2=\Psi^2$ and the fluctuation $\Sigma_2-\Psi^2$ are both in it. Genus zero, $k+\ell\le4$, $\Sigma_2$ with $(2,2)$ strands, C6's parity rule (A9).
- *Relevant cases outside.* (i) $f$ containing the propagator of $\Sigma_2$, $p_{2,2}^{-1}$ on the quotient: $f\ni-g_s^{-1}p_{2,2}^{-1}p_{1,2}(\Psi)$ removes M-b but puts $-\ell_2\,p_{2,2}^{-1}p_{1,2}$ into the kinetic operator of $\Psi$ in $\mathcal M_1$ – not the present equations, but a candidate to be judged by Task 25. (ii) $f$ with pairing contractions (scalars such as $\langle\Psi,Q_B\Psi\rangle$ times $\Sigma_2$): field degree three, no effect on (H2.3) at degrees one and two. (iii) $\hbar$-dependent $f$: moves terms between the $\hbar$-orders, which are separate equations by ghost number anyway. (iv) A different family: data added to the $p_{m,n}$ (C-01-16, Task 25) – outside by construction, and the purpose of the list. (v) $f$ or combination coefficients containing the $\Psi$ propagator $h=b_0/L_0$: $g_sp_{1,2}(\Psi)=g_sp_{1,2}(h\,\mathcal E_\Psi)+g_sp_{1,2}\bigl((1-hQ_B)\Psi\bigr)+O(g_s^2)$ removes $p_{1,2}$ of the non-harmonic part; reading (III) keeps the harmonic part $p_{1,2}(P\Psi)$, nonzero on a free solution.
- *Weakest relaxation that evades it.* No change of $f$ without a term linear in $\Psi$ alone evades M-b (reading (III)); the weakest one that does is (i), at the price of a modified kinetic operator. Otherwise the structure must change: a family in which the multi-output sector does not act on the classical field alone (no $p_{1,2}(\Psi)$ in the equation of $\Psi_2$, no $p_{1,3}(\Psi)$ in $E_3$). Such a family also changes the baseline: M-b and M-r0 are present at $\Psi_2=0$, so, with $\Psi_2=0$, or any $\Psi_2(\Psi)$ built locally from the family, the original quartic closed SFT is not a Maurer–Cartan element of the raised family either; a $\Psi_2(\Psi)$ containing $p_{2,2}^{-1}$ removes M-b at the price of a modified kinetic operator of $\Psi$ (case (i)), and removing them is the step back to the $L_\infty$ truncation. This list is the measurable form of "data to add to the $p_{m,n}$" (criterion 3b, Task 25): an $\mathrm{IBL}_\infty$ structure whose Maurer–Cartan equation is (H2.0) must remove M-a, M-c, M-d, M-r and supply M-e and M-q (the items specific to the Hubbard–Stratonovich form), and, as for any tree-level closed SFT, either remove the baseline items M-b, M-r0 or read them as equations the theory adds.

\subsection*{Verification}
See block V19b (checks C8.2, C8.2-break, C8.2-quot, C8.2-shell, C8.2-action).

## Block V19b – verification of 19b

Script `codes/verify-ibl-mc-conventions.py` (19a's checks unchanged), section `run_19b`; exact Fractions, the model of 19a ($\dim8$, ghosts $0$–$5$, pairing at $5$, $\mathcal V_n$ at $2n$, random graded-symmetric vertices, the $L_\infty$ relations not imposed: the component identities do not use them), seeds 20261018 and 20261019; 46/46 PASS after the final fix pass (42/42 after the first, 36/36 before), peak RSS 23 MB.

- **C8.1** – the independent path is the definition: $e^{-\mathfrak m'}\hat p_{k,\ell}e^{\mathfrak m'}$ computed literally in the symmetric algebra (CFL (2.1): $k$-subsets of letters, Koszul sign of the moves, outputs to the left; $e^{\pm\mathfrak m'}$ expanded to word length $4$), for $\mathfrak m'=t\Psi+u\Sigma_2$ at two $(t,u)$, equals (MC.3) block by block for every $(k,\ell)$ with $k+\ell\le4$ and $L=1,2$ (which also fixes the monomials in $t,u$, hence each coefficient); every block used is nonzero; with $\Psi_2=0$ the $E_1$ component is the original equation of motion. Break legs (FAIL as expected): the paper's $\tfrac1{3!}$ on $\ell_3(\Psi,\Psi_2)$, $\tfrac12$ on the lift of $\ell_3(\Psi_2,\cdot)$, the sign $-1$ on the lift of $\ell_2(\Psi,\cdot)$.
- **C8.1-par** – $p_{1,2}(\Psi)$ is graded-symmetric in the shifted parity and not in the physical one; its $(3,3)$-strand part is nonzero and the physical quotient kills it; the shifted quotient kills $\Sigma_2$. A first run with the physical parity on the outputs failed C8.1's non-vacuity leg (the two-output blocks vanished) and made $\mathcal M_2^{(6)}=c_2\mathcal E_\Sigma$ "solvable" with both sides zero; A9's rule is the repair, and this check pins its reason.
- **C8.1-review** – Task 17's display (2) (the review, l. 94 and l. 97, CFL weight, $\mathfrak m_{2,0}$ $\hbar$-independent), its coefficients evaluated with $\hat p$ and the connected part by inclusion–exclusion, equals the literal blocks for each of its twelve terms with $k+\ell\le4$ (its $\mathfrak p_{3,2,0}$ terms are outside the truncation); after $\mathfrak m_{2,0}=\hbar^{-1}\Sigma_2$ and $\varphi^{-1}$ each term sits at $\hbar^{\ell_p-1}$. The review's factor-2 notes (singly fed $\mathfrak m_{2,0}$) are the $s^{ab}e_ae_b$ normalization of (MC.2).
- **C8.2** – reading (I): the exact linear systems $\mathcal M_1(f)=c_1\mathcal E_\Psi$ and $\mathcal M_2^{(6)}(f)=c_2\mathcal E_\Sigma$, with $f=\alpha\Sigma_2+\beta\Psi^2$ and $\alpha,\beta,c_1,c_2$ Laurent in $g_s$ (powers $-2$ to $2$; a superset of the power-series class of A10, whose system is exact through $O(g_s^2)$, so its inconsistency carries over), through $O(g_s^2)$, sampled at four random $(\Psi,\Sigma_2)$, with the components from the literal path, are inconsistent separately and jointly.
- **C8.2-break** – the ladder that identifies the obstructions: without M-a the $E_1$ system is solvable; without M-b the ghost-6 system is; without both the joint system is still unsolvable (M-c); without M-a, M-b, M-c it is solvable, with $\alpha_0=\tfrac16$, $\beta_0=-\tfrac16$.
- **C8.2-quot** – model with $\mathcal V_4=0$ whenever $e_2$ occurs twice, so $N=e_2\otimes e_2\in\ker p_{2,2}$: $\mathcal E_\Psi$, $\mathcal E_\Sigma$ invariant under $\Sigma_2\to\Sigma_2+N$ (with $p_{2,2}$, $\ell_3(\Psi,\cdot)$ nonzero), the components with $f=\Sigma_2/6$ not; $\ell_2(N)\ne0$, $\hat QN\ne0$ (lift of $p_{1,1}$, derived).
- **C8.2-shell** – model with $\mathcal V_2(e_2,\cdot)=0$ on $\mathcal H_2$, so $Q_Be_2=0$: $(\varepsilon e_2,\varepsilon^2e_2^2)$ solves (H2.0) at $O(\varepsilon)$, and the $O(\varepsilon)$ part of (MC.7), literally computed, is $g_sp_{1,2}(e_2)\ne0$.
- **C8.2-action** – (H2.6): $\partial_\Psi S_{\rm MC}=\langle\cdot,\mathcal M_1\rangle$ and $\partial_{\Psi_2}S_{\rm MC}=\langle\cdot,\mathcal M_2^{(6)}\rangle_2$ at $g_s^0,g_s^1,g_s^2$, with $S_{\rm MC}$ built from the vertices on $e^{\Psi+\Psi_2}$ and exact derivatives; since $\langle x,\ell_{n-1}\rangle=\mathcal V_n$ is definitional in `raise_family`, its independent content is the combinatorics of the exponential, not the operations.

- **C2-C3-E34** (fix pass) – the $E_3$, $E_4$ terms of the enumeration equal the table of (MC.8)–(MC.9) (operation, $\hbar$-, $g_s$-powers), the output-counting order is $\ell_p-1$, and the measured ghost number at $N_{\rm gh}(\Psi_2)=4$ is $2L+\ell_p$ for each; break leg: the table with $p_{1,3}(\Psi)$ dropped is detected.
- The random data do not satisfy the $L_\infty$/IBL relations: acceptable for the component identities, but no check bears on H-par.

Not checked: H-par; the double-contraction relations; the coefficients of (MC.8)–(MC.9); genus $\ge1$ and $k+\ell>4$; $\Sigma_2$ with strands other than $(2,2)$; reading (II) beyond the degree-one argument of block H2 (it is a derivation, not a check); the absence of other structure-built maps $\mathcal H_3\to\mathcal H_6^{\otimes2}$ used in reading (II), argued by (H2.1).

## Consequence for Task 20

Task 20 should take $\Sigma_2$ itself as $\Psi_2$, in the output-counting form of block R: $\mathfrak m=\hbar^{-1}\Psi+\hbar^{-2}\Sigma_2$, $\lambda=\hbar^{-1}\Lambda_1+\hbar^{-2}\Lambda_2$, $N_{\rm gh}=(2,4;1,3)$, $\hbar$ an even, central formal parameter of ghost number $-1$ and CFL degree $1$, $\mathbb Z$-labels not tied to Grassmann parity (A11; strand parities by C6), so that the Maurer–Cartan equation and $[\hat{\mathfrak p},\lambda]$ are homogeneous and the paper's ghost number of $\Lambda_2$ (07-ibl l. 342) is recovered. CFL's uniform weight is the same structure under $\Psi_2^{\rm CFL}=\hbar^{-1}\Sigma_2$ (ghost number $5$) and $\Lambda_2^{\rm CFL}=\hbar^{-1}\Lambda_2$ (ghost number $4$), so Task 20 may work in either form but must not take $\Sigma_2$ at $4$ as A5's $\hbar$-independent $\mathfrak m_{2,0}$ with a ghost-neutral $\hbar$: there no element is homogeneous across $\hbar$-orders, and order by order the value is $5$, not $4$ (A12, (H.2')). The order-by-order criterion depends on the dressing (H.2''): $\Sigma_2$ at $4$ placed as $\mathfrak m_{2,1}$ (CFL's uniform weight $\hbar^{g-1}$ at genus label $1$) passes it with a ghost-neutral $\hbar$, but only because the genus-zero family has no genus-one operations; CFL degree puts $\mathfrak m_{2,1}$ at $6$, and the whole-component criterion gives $N_{\rm gh}(\mathfrak m_{2,g})=5+g$ with $N_{\rm gh}(\hbar)=-1$ (H.3'). Task 20 should therefore grade by the whole-component criterion, which does not depend on the dressing (after the last review, critic 21a2 #2). Two inputs Task 20 must carry. First, with $\hbar$ formal, at genus zero every component splits by $\hbar$-order into sectors labelled by the number of outputs of the product used (at genus $g$ the order is $\ell_p+g-1$): the $E_2$ equation contains the ghost-5 equation (R.2), headed by the lift of $p_{1,1}$, derived, which the cubic theory does not impose, and $\delta\Psi_2$ splits in the same way; whether the cubic theory's equations are the components after a redefinition is H2 (19b), and Task 20 waits for it. Second, the genus label $-1$ that $\Sigma_2$ receives in CFL's expansion puts it outside the filtration conditions of CFL (9.1). Task 17's review has answered its question (5) (l. 156–160): (9.1) fails with the trivial filtration and holds with $R=\mathbb Q[[g_s]]$ and fields of positive $g_s$-order; Def. 9.1 and Lemma 9.2 hold for the finite truncation, and Prop. 9.3 holds under the conditions of *Third* (H-par and the double-contraction relations; after the last review, critic 21a2 #4); Props. 9.6 (second part), 9.8 and 9.9 are outside their hypotheses. The review identifies CFL's $\hbar$ with the project's $g_s$ (l. 52, l. 156); this record identifies $g_s$ with $\tau$ (A6), since $\tau^{-\chi}$ at genus zero is $g_s^{m+n-2}$; the filtration answer is to be read with that identification. Third, $\hat{\mathfrak p}\circ\hat{\mathfrak p}=0$ on the genus-zero truncation: the raised family satisfies the single-contraction (genus-zero) relations (R87), and in the C6 grading their operator form – the single-contraction part of $\hat{\mathfrak p}'\circ\hat{\mathfrak p}'$ as the square of one operator on $EC$, with the family and coefficient rule of rule V on odd-letter words – is H-par; the double-contraction relations (e.g. $\mathfrak p_{2,1,0}\circ_2\mathfrak p_{1,2,0}=0$ in the $(1,1,1)$ relation, involutivity) are not implied, and in the output-counting form a double contraction of $p_{k,\ell}$ with $p_{k',\ell'}$ carries $\hbar^{\ell+\ell'-2}$, the order of a genus-zero relation with one more output, so the classical limit does not remove it. CFL Prop. 9.3 and the preservation of the Maurer–Cartan equation by $[\hat{\mathfrak p},\lambda]$ ($\delta\hat{\mathfrak p}(e^{\mathfrak m})=\hat{\mathfrak p}^2(\lambda e^{\mathfrak m})$ on shell) need both. Task 20's preservation check must impose the double-contraction relations on the model data, or restrict to the orders where they do not enter, or report a failure as this obstruction; random data satisfying only the genus-zero relations would misattribute it to the law. Fourth, the form $\delta e^{\mathfrak m}=[\hat{\mathfrak p},\lambda]e^{\mathfrak m}$ is A8, a decision; $\hat Q\Lambda_2$ (lift of $p_{1,1}$, derived under A8) and the whole $\Lambda$ table hold for that form.

Flags (lift of $p_{1,1}$ to two strands): term 6 of $E_2$ ($\hat Q\Psi_2$); its rewriting as the first term of (R.2) ($\hat Q\Sigma_2$); $\hat Q\Lambda_2$ in $\delta\Psi_2$ (block Λ, derived under A8). Each is produced by $\hat{\mathfrak p}_{1,1}$ acting as a derivation on a two-strand factor; none is posited as a kinetic term.

**Update after 19b (H2 answered).** H2 is refuted: no $f(\Sigma_2,\Psi)$ of A10 makes the quartic-order equations of motion the Maurer–Cartan components (MC.5)–(MC.9), and the term $g_s\,p_{1,2}(\Psi)$ of the ghost-6 sector obstructs every reading. That term is CFL Lemma 9.2's condition and is present at $\Psi_2=0$: with $\Psi_2=0$, or any $\Psi_2(\Psi)$ built locally from the family, the original quartic closed SFT is not a Maurer–Cartan element of the raised family either; a $\Psi_2(\Psi)$ containing $p_{2,2}^{-1}$ removes M-b at the price of a modified kinetic operator of $\Psi$ (case (i)); so M-b (with M-r0) is a property of the raised family against any tree-level closed SFT, and a family without $p_{1,2}(\Psi)$ in the $\Psi_2$ equation also changes the baseline theory. Task 20 therefore cannot derive "the present law as the member of the $\mathrm{IBL}_\infty$ gauge transformation" by restriction to a Maurer–Cartan element: $(\Psi,f)$ is not one, for any $f$ of the ansatz. Three inputs replace the hand-over above. (1) The object whose Maurer–Cartan equation is computed is (MC.5)–(MC.7) with $\Psi_2$ an independent two-string field at ghost number $4$ in the output-counting form; (MC.5), (MC.7) are the Euler–Lagrange equations of $S_{\rm MC}$ (H2.6) and (MC.6) is the additional sector of the lifts. The cubic action differs from $S_{\rm MC}$ by the items specific to the Hubbard–Stratonovich form (M-a $\alpha$-part, M-c, M-d, M-e, M-q, M-r, M-s), the quartic theory itself by the baseline items (M-b, M-r0), and H4 (the present law as the $\Lambda_2=0$ member) can be tested only on the structure that removes them: Task 25's question, with the list of block H2 as its input. (2) The only $f$ of A10 that vanishes on-shell is $f=\alpha(\Sigma_2-\Psi^2)$, invariant under the composite law; the Maurer–Cartan gauge transformation instead has $\delta\Psi_2\ni g_sp_{1,2}(\Lambda_1)$ (block Λ), the gauge counterpart of M-b. (3) The parity rule C6 (A9: field strands physical, output strands shifted) is needed for $[\hat{\mathfrak p},\lambda]$ as well; the single-parity symmetric algebra loses either $\Sigma_2$ or the two-output terms; that the single-contraction part of $\hat{\mathfrak p}'\circ\hat{\mathfrak p}'$ is the square of one operator on that algebra and vanishes is H-par (with rule V, which defines the composition on gauge-parameter words, and its locality clause), and that $\hat{\mathfrak p}'$ is a differential needs in addition the double-contraction relations (Third, above), which fail for the genus-zero truncation unless genus-one terms $p_{k,\ell,1}$ are added. Flags added by 19b (lift of $p_{1,1}$ to two strands): $\hat Q\Psi_2$ in (MC.6), $\alpha\hat Q\Sigma_2$ in (H2.5), $\hat QN$ in the quotient item; each derived, none posited as a kinetic term.

## Self-review

1. Objective: answered – $(\Psi,\Sigma_2)$ at $(2,4)$ is not a homogeneous Maurer–Cartan element with CFL's weight as $\mathfrak m_{2,0}$ in either column, under either homogeneity criterion (as $\mathfrak m_{2,1}$ it passes the order-by-order criterion only through the absence of genus-one operations, (H.2'')); with the output-counting weight it is homogeneous order by order for any $N_{\rm gh}(\hbar)$ and across orders for $N_{\rm gh}(\hbar)=-1$; the price is the splitting of $E_2$ into sectors.
2. Weakest step: the term list rests on reading CFL's $\hat\phi$ (2.1) and the connected part of $e^{-\mathfrak m}\hat{\mathfrak p}(e^{\mathfrak m})$; shored up by the independent enumeration (C2-C3) and by CFL homogeneity of the measured degrees at $y=5$ (C4), which a wrong $\hbar$-power would break.
3. Not checked: signs and coefficients (gradings only; 19b), the form of the gauge transformation (Task 20), the admissibility of CFL's filtration after the conjugation (R.1), genus $\ge1$ terms (they enter $E_\ell$ at $\hbar^0$ through $\mathfrak m_{\ell,1}$, $p_{k,\ell,1}$ and are outside the genus-zero truncation), $p_{0,n}$ (excluded by CFL's $k\ge1$; $p_{0,2}$ would enter $E_2$ at $\hbar^{-1}$ with $N_{\rm gh}=6$, in the two-output sector).
4. What a stronger physicist would note: the obstruction is structural (E.3), $N_{\rm gh}=2L+\ell_p$: for the raised family (A3, shifts $3\ell-2k$) with ghost-neutral $\hbar$, a multi-string Maurer–Cartan component sees the one-output and multi-output products at different ghost numbers. The record states it for $L\le2$ and $k+\ell\le4$; the derivation of (E.3) holds for every $L$, $k$, $\ell$ with $N_{\rm gh}(\Sigma_n)=2n$. It is not a property of every IBL reading: Münster–Sachs' structure with a neutral $\hbar$ has a homogeneous two-string element at $4$, because its only two-output datum $\omega_c^{-1}$ has shift $2\ell-2k+1=5$ at $(k,\ell)=(0,2)$, not A3's $3\ell-2k$ (critic 21a2 #3, #6).

### Self-review (19b)

1. Objective: answered – the present equations are not the components of CFL's Maurer–Cartan expression $e^{-\mathfrak m'}\hat{\mathfrak p}'(e^{\mathfrak m'})$ of the raised family for any $f$ of A10 (these components are forced by CFL (2.1) on even words; the exclusion does not depend on whether a reading as an $\mathrm{IBL}_\infty$ Maurer–Cartan equation closes), and the mismatch is a list of nine named items (M-a–M-e, M-q, M-r0, M-r, M-s). Two of them, M-b and M-r0, are present at $\Psi_2=0$ (CFL Lemma 9.2): with $\Psi_2=0$, or any $\Psi_2(\Psi)$ built locally from the family, the original quartic closed SFT is not a Maurer–Cartan element of the raised family either; a $\Psi_2(\Psi)$ containing $p_{2,2}^{-1}$ removes M-b at the price of a modified kinetic operator of $\Psi$ (case (i)); so they measure the distance between the raised family and any tree-level closed SFT, not a defect of the cubic action; the items specific to the Hubbard–Stratonovich form are M-a ($\alpha$-part), M-c, M-d, M-e, M-q, M-r, M-s. This is the measurable form of "data to add to the $p_{m,n}$" that C-01-16 asks for, with the baseline separated.
2. Weakest step: reading (II), whose claim that no structure-built map $\mathcal H_3\to\mathcal H^{\otimes2}_6$ of ghost number $3$ exists rests on the counting (H2.1) extended to pairing contractions, not on a check; readings (I) and (III) are checked. A second weak point was the parity of the strands, which the first run of the script exposed (C8.1-par records it).
3. Not checked: $f$ outside A10 (with the propagator $p_{2,2}^{-1}$ of $\Sigma_2$: removes M-b and changes the kinetic operator of $\Psi$, argued in block H2), $\hbar$-dependent $f$ (moves terms between separate equations), $\Sigma_2$ with strands other than $(2,2)$, genus $\ge1$, $k+\ell>4$.
4. What a stronger physicist would note: (H2.6) says that the raised family's Maurer–Cartan equation is, in two of its three sectors, the field equation of the vertex functional on $e^{\Psi+\Psi_2}$ – the classical action evaluated on a total field in which $\Psi_2$ counts as two strands; the Hubbard–Stratonovich action is a different completion of the same $S_{\le4}$. Whether a field redefinition outside A10, or a different family (Task 25), maps one to the other is the open question this record hands on.

## Proposed ledger entries

Ledger section: new: IBL Maurer–Cartan reading of the cubic theory

### R? — Grading of the genus-zero IBL Maurer–Cartan equation: with CFL's weight the second component has ghost number 5, with the output-counting weight it is $\Sigma_2$ at ghost number 4 [Verified]

- **Source**: `agent/derivations/103-ibl-mc-conventions.md`, claim-tree nodes C2–C7, blocks E, H1, Λ, R
- **Scope**: genus zero and $k,\ell\ge1$ (CFL's range), $k+\ell\le4$, $\mathfrak m$ with one- and two-string components; gradings only; $d=\tfrac12$ dictionary of R23 (forced at genus zero); $\hbar$ even, central, its degree a $\mathbb Z$-label; two homogeneity criteria (whole component, order by order in $\hbar$); gauge transformation taken of the form $[\hat{\mathfrak p},\lambda]$ for the grading of $\Lambda_n$ only; the conjugated form puts $\Sigma_2$ at genus label $-1$ in CFL's expansion, outside CFL (9.1)
- **Verification**:
  - 2026-10-18 – exact check – `codes/verify-ibl-mc-conventions.py` C1, C2-C3 (+break), C4 (+break), C5, C5.3, C6, C7.1 (+break), TW; 18/18 PASS at seeds 20261018 and 20261019; support-constrained model ($\dim8$, ghosts $0$–$5$), both R87 families, measured ghost numbers
  - 2026-10-18 – exact check (fix pass) – same script, NV (non-vacuity), C5-ord (+break), C2-C3 with a perturbed-rule break leg; 42/42 PASS with the 19b checks at both seeds
  - 2026-10-18 – exact check (final fix pass) – same script, C5-ord-n (+break): dependence of the order-by-order criterion on the dressing $\hbar^{-1-n}$, whole-component value $5-n$; 46/46 PASS at both seeds

For $\mathfrak m=\hbar^{-1}(\Psi_1+\Psi_2)$ (CFL Def. 9.1) and the genus-zero raised family, the $E_1$ component has terms $Q_B\Psi_1,\tfrac12\ell_2(\Psi_1^2),\tfrac16\ell_3(\Psi_1^3)$ at $\hbar^{-1}$ and $\ell_2(\Psi_2),\ell_3(\Psi_1,\Psi_2)$ at $\hbar^0$; the $E_2$ component has the lifts of $p_{1,1}$, $\ell_2(\Psi_1,\cdot)$, $\tfrac12\ell_3(\Psi_1^2,\cdot)$ on one strand of $\Psi_2$, $p_{1,2}(\Psi_1)$, $\tfrac12p_{2,2}(\Psi_1^2)$ at $\hbar^{-1}$ and $p_{2,2}(\Psi_2)$, the lift of $\ell_3(\Psi_2,\cdot)$ on a second $\Psi_2$ at $\hbar^0$; $g_s=\tau$ weights $g_s^{k+\ell-2}$. In CFL degree ($\lvert\hbar\rvert=1$) homogeneity requires $N_{\rm gh}(\Psi_2)=5$, $N_{\rm gh}(\Lambda_2)=4$. In physical ghost number with $\hbar$ and $g_s$ ghost-neutral: no value makes the whole components homogeneous ($E_1$ requires $4$; at $4$ every term of $E_L$ has $N_{\rm gh}=2L+\ell_p$, so $E_2$ splits into the one-output sector at $5$ and the two-output sector at $6$); order by order in $\hbar$ the unique value is $5$ (with $\Lambda_2$ at $4$), for $\Psi_2=\mathfrak m_{2,0}$; the order-by-order criterion depends on the dressing of the two-string component and fixes nothing for $\mathfrak m_{2,g\ge1}$ within the genus-zero truncation, while across orders $N_{\rm gh}(\mathfrak m_{2,g})=5+g$ with $N_{\rm gh}(\hbar)=-1$. The unique $N_{\rm gh}(\hbar)$ making each component homogeneous across $\hbar$-orders is $-1$; order by order every value works. Conjugating by $\hbar^{-L}$ on $E_LC$ turns CFL's weight $\hbar^{k+g-1}$ into $\hbar^{\ell+g-1}$, in which $(\Psi,\Sigma_2;\Lambda_1,\Lambda_2)$ at $(2,4;1,3)$ is homogeneous order by order for any $N_{\rm gh}(\hbar)$ and across orders for $N_{\rm gh}(\hbar)=-1$, and at genus zero the $\hbar$-order of a term is the number of outputs of its product minus one. Either way $N_{\rm gh}(\mathfrak m_{2,0})=4$ is excluded; as $\mathfrak m_{2,g\ge1}$ the value $4$ is excluded across orders ($5+g$) and unconstrained order by order within the genus-zero truncation. The rescaling and suspension caveat was checked among dictionaries that treat input and output strands alike and changes nothing. The obstruction is a property of the raised family: in Münster–Sachs' structure, whose two-output datum is $\omega_c^{-1}$, a two-string element at 4 is homogeneous with a neutral $\hbar$.

Ledger section: new: IBL Maurer–Cartan reading of the cubic theory

## C? — Ghost numbers of $\hbar$ and $g_s$ in the IBL reading

- **Statement.** Local to the IBL reading of record 103. $g_s$ is CFL's $\tau$ at genus zero ($g_s^{k+\ell-2}=\tau^{k+\ell-2}$) and has ghost number $0$ and CFL degree $0$. CFL's $\hbar$ is an even, central formal variable; its CFL degree $2d=1$ is a $\mathbb Z$-label not tied to Grassmann parity, and in physical ghost number it is equivalent, component by component across $\hbar$-orders, to $N_{\rm gh}(\hbar)=-1$. With $\hbar$ ghost-neutral, $\Psi_1\neq0$ at ghost number $2$ and $\Psi_2=\mathfrak m_{2,0}\neq0$ (at most two strings, $k+\ell\le4$), no Maurer–Cartan element is homogeneous across $\hbar$-orders. Across orders the grading is that of $N_{\rm gh}(\hbar)=-1$ for every dressing of the two-string component ($N_{\rm gh}(\mathfrak m_{2,g})=5+g$); order by order the criterion depends on the dressing: it fixes $5$ for $\mathfrak m_{2,0}$, $4$ for genus label $-1$, and nothing for any other dressing within the genus-zero truncation. The strand degree $3-N_{\rm gh}$ is forced at genus zero; the alternative $2-N_{\rm gh}$ is the per-strand $\hbar^{-1}$ dressing, not an independent convention.
- **Conventions it rests on.** Physical ghost number (the project conventions); C6 (strand parities); R5 ($\lvert\hbar\rvert=2d$); R23 ($d=\tfrac12$, strand degree $3-N_{\rm gh}$, $N_{\rm gh}(p_{k,\ell,g})=3\ell-2k+g$); R87 (the generating function's $g_s^{m+n-2}$).
- **Sources.** CFL Def. 2.3 and Def. 9.1; record 103 block 0, A2, A11, (H.3), (H.2'); Task 17's review (1b).
- **Checked on.** The homogeneity of the $E_1$, $E_2$ components in a support-constrained model (record 103, checks C4, C5, C5-ord, C5-ord-n).

Ledger section: new: IBL Maurer–Cartan reading of the cubic theory

### PH? — Operator form of the genus-zero IBL relations on the C6 role-graded symmetric algebra: rule V's single-contraction composition equals the lifted antibracket term by term, and is the square of one operator [open]

- **Source**: `agent/derivations/103-ibl-mc-conventions.md`, node H-par
- **Verification**:
  - none (declared 2026-10-18; no check bears on it)

On the C6 role-graded symmetric algebra $EC$ at $d=\tfrac12$ (input-role letters in the physical parity, output-role letters in the shifted parity), extend CFL's (2.1) to every word by applying $\phi$ to $k$-subsets of letters – input-role letters directly, output-role letters through rule V – with Koszul signs in the role parities, and compose by rule V: an output letter fed to a later operation is converted back to a vertex leg by $\omega$, i.e. the term is the sewing of the two vertices with the odd $\omega^{-1}$, with the sign of that sewing, R87's sign under the paper's coefficient rule (R87, C3; coefficients moved to the left, passing only basis states), for the `eq:conv:sprod` family – on words with odd letters the two families and the two coefficient rules give different signs, and the hypothesis is stated for this pair; the antibracket on odd inputs is R87's Argued part, so the discharge of H-par on such words also discharges it; the sign of the sewing depends only on the role parities and positions of the letters of the word, so that $\hat\phi$ is one operator on $EC$ and $\hat{\mathfrak p}'\circ\hat{\mathfrak p}'$ is its square. Hypothesis: for every pair of genus-zero operations with $k+\ell\le4$ the single-contraction part of $\hat\phi'\circ\hat\phi$ equals, with sign and coefficient, the lifted term of R87's antibracket $\{S,S\}$, so CFL's operator form of the genus-zero relations holds in this algebra. Motivation: R87's vertex-form proof, in which all legs are physical inputs and outputs are legs raised by the odd $\omega^{-1}$, and C6's shifted output parity as the parity that odd map transports (record 076). Falsified by a finite-model computation with random graded-symmetric vertices (an identity term by term, no $L_\infty$ data needed) implementing C6's role parities – not the script's `eps_out` – and rule V, finding a single-contraction term that differs in sign or coefficient from the lifted antibracket term. Not covered, and failing in general for the genus-zero truncation: the double-contraction (involutivity) relations.

Ledger section: new: IBL Maurer–Cartan reading of the cubic theory

### R? — excl. within local redefinitions $f=\alpha\Sigma_2+\beta\Psi^2$: the quartic-order equations of motion are not the components of CFL's Maurer–Cartan expression $e^{-\mathfrak m'}\hat{\mathfrak p}'(e^{\mathfrak m'})$ of the raised family; the components with coefficients, and the mismatch list with the baseline separated [mixed]

- **Source**: `agent/derivations/103-ibl-mc-conventions.md#C8`, blocks MC, H2, V19b
- **Scope**: genus zero, $k,\ell\ge1$, $k+\ell\le4$ (through $O(g_s^2)$), components $E_1$–$E_4$; output-counting form of record 103 block R ($\mathfrak m'=\Psi+\Psi_2$, weight $\hbar^{\ell-1}g_s^{k+\ell-2}$, $N_{\rm gh}(\Psi,\Psi_2)=(2,4)$); field strands at ghost number $2$ ($\Sigma_2$ with $(2,2)$ strands); strand parity C6; ansatz A10 ($f$ linear in $\Sigma_2$, degree $\le2$ in $\Psi$, built from the family, power series in $g_s$, $\hbar$-independent; equivalently $f=\alpha\Sigma_2+\beta\Psi^2$); reading (I) checked, reading (III) checked at first order in the amplitude of a free solution, reading (II) argued; the exclusion uses no hypothesis; the reading of the components as a gauge-covariant Maurer–Cartan equation is conditional on PH? (H-par, as a single operator on $EC$) and on the double-contraction relations, an open condition expected to fail for the genus-zero truncation unless genus-one terms $p_{k,\ell,1}$ are added; coefficients of $E_3$, $E_4$ by hand
- **Verification**:
  - 2026-10-18 – exact check – `codes/verify-ibl-mc-conventions.py` C8.1 (+break: coefficient), C8.1-par, C8.1-review, C8.2 (+break ladder), C8.2-quot, C8.2-shell, C8.2-action; 36/36 PASS (with 19a's checks) at seeds 20261018 and 20261019; support-constrained model ($\dim8$), literal CFL (2.1) in the symmetric algebra as the independent path; Task 17's display (2) reproduced
  - 2026-10-18 – exact check (fix pass) – same script, C2-C3-E34 (+break): $E_3$, $E_4$ term list, powers and ghost numbers; 42/42 PASS at both seeds
- **Status**: reading (I) and the components (MC.5)–(MC.7) with coefficients – Verified (C8.1, C8.2 with break ladders); reading (III) at first order on a free solution – Verified for M-b (C8.2-shell), Argued for M-r0; reading (II) – Argued (degree-one counting of block H2); $E_3$, $E_4$ components (MC.8)–(MC.9) – term list and gradings Verified (C2-C3-E34), coefficients Argued (by hand); the baseline for any local $\Psi_2(\Psi)$ – Argued (counting); the reading of the components as a gauge-covariant Maurer–Cartan equation – Conditional on PH? (H-par) and on the double-contraction relations, expected to fail at genus zero

The components of $e^{-\mathfrak m'}\hat{\mathfrak p}'(e^{\mathfrak m'})=0$ through $O(g_s^2)$ are $\mathcal M_1=Q_B\Psi+\tfrac{g_s}2\ell_2(\Psi^2)+\tfrac{g_s^2}{3!}\ell_3(\Psi^3)+g_s\ell_2(\Psi_2)+g_s^2\ell_3(\Psi,\Psi_2)$ (ghost $3$), $\mathcal M_2^{(5)}=\hat Q\Psi_2+g_s\widehat{\ell_2(\Psi,\cdot)}\Psi_2+\tfrac{g_s^2}2\widehat{\ell_3(\Psi,\Psi,\cdot)}\Psi_2+g_s^2\widehat{\ell_3(\Psi_2,\cdot)}\Psi_2$ (ghost $5$, $\hbar^0$; $\hat Q$ the lift of $p_{1,1}$, derived), $\mathcal M_2^{(6)}=g_sp_{1,2}(\Psi)+\tfrac{g_s^2}2p_{2,2}(\Psi^2)+g_s^2p_{2,2}(\Psi_2)$ (ghost $6$, $\hbar^1$), and the $E_3$, $E_4$ components (MC.8)–(MC.9), headed by $g_s^2\hbar^2p_{1,3}(\Psi)$ (ghost $9$); every relative coefficient $+$, given the operations of the raised family and C6 (no Koszul sign arises, all letters even; the signs of the operations are R87's). $\mathcal M_1$ and $\mathcal M_2^{(6)}$ are the Euler–Lagrange equations of $S_{\le4}(\Psi)+g_s\mathcal V_3(\Psi_2,\Psi)+\tfrac{g_s^2}2\mathcal V_4(\Psi_2,\Psi^2)+\tfrac{g_s^2}2\mathcal V_4(\Psi_2,\Psi_2)$. For no $\Psi_2=\alpha\Sigma_2+\beta\Psi^2$ ($\alpha,\beta$ power series in $g_s$) are $\mathcal E_\Psi$, $\mathcal E_\Sigma$ of `eq:hs4:eom` these components: $E_1$ needs $\alpha_0=0$ and $\beta_0=0$ (from $g_s\ell_2(\Psi_2)$) against $\alpha_0=\tfrac16$, $\beta_0=-\tfrac16$; the ghost-6 sector contains the $f$-independent $g_sp_{1,2}(\Psi)$, absent from $\mathcal E_\Sigma$, and without it requires $\alpha+\beta=-\tfrac12$ against $0$; the ghost-5 sector vanishes identically only for $f=0$; the components are not invariant under $\Sigma_2\to\Sigma_2+N$, $N\in\ker p_{2,2}$, for $\alpha\neq0$; $E_3$, $E_4$ have no counterpart. $g_sp_{1,2}(\Psi)$ and $g_s^2p_{1,3}(\Psi)$ are independent of $f$ and present at $\Psi_2=0$ (CFL Lemma 9.2): with $\Psi_2=0$, or any $\Psi_2(\Psi)$ built locally from the family, the original quartic closed SFT is not a Maurer–Cartan element of the raised family either; a $\Psi_2(\Psi)$ containing $p_{2,2}^{-1}$ removes M-b at the price of a modified kinetic operator of $\Psi$ (case (i)), and these baseline items measure the distance between the raised family and any tree-level closed SFT; the items specific to the Hubbard–Stratonovich form are the $\alpha$-part of $g_s\ell_2(\Psi_2)$, the coefficient mismatch, the ghost-5 sector, the $f$-dependent $E_3$, $E_4$ terms, the kernel non-invariance and the action-level sign. At first order in the amplitude of a free solution the Maurer–Cartan equation requires $p_{1,2}(\Psi_0)=0$, for any such $f$. In CFL's single-parity $E_2C$ at $d=\tfrac12$ the plain symmetric $\Sigma_2$ is zero; the comparison exists only in the C6 grading. These components are forced by CFL (2.1) on even words and are the Maurer–Cartan equation of any IBL reading of the raised family in the C6 grading; the exclusion does not depend on whether such a reading closes. Read as a gauge-covariant Maurer–Cartan equation, these components are conditional on PH? (H-par, as a single operator on $EC$) and on the double-contraction relations, which fail for the genus-zero truncation unless genus-one terms $p_{k,\ell,1}$ are added. Exclusion scope: record 103, block H2, *Scope of the exclusion* (outside: $f$ with the propagator $p_{2,2}^{-1}$ or the $\Psi$ propagator, which remove $p_{1,2}$ of all or of the non-harmonic part of $\Psi$; a different family).

The former proposed entry "Parity of the strands in the symmetric algebra of the raised family" is withdrawn: it duplicated the registered convention C6 (critic 21b #3). Suggested addition to C6's *Checked on* line, for the orchestrator: record 103 check C8.1-par (raised outputs of $p_{1,2}(\Psi)$ graded-symmetric in the shifted parity, not the physical one; the physical quotient kills its $(3,3)$-strand part, the shifted quotient kills $\Sigma_2$).

## Revisions

Fix pass 2026-10-18 (brief `agent/briefs/active-computator-gu-19-fix-20261018T101514.md`), after critics `agent/reports/critic-gu-21a-20261018T095900.md` (21a) and `agent/reports/critic-gu-21b-20261018T095900.md` (21b). One line per finding.

- 21a #1 [major] – applied. A12 (two criteria); (H.2') order by order: $y=5$ for every $x$ in CFL's weight, $(2,4)$ homogeneous for every $x$ in the output-counting weight; "no homogeneous element" and the uniqueness of $-1$ restricted to "across $\hbar$-orders" in C5, C5.2, H1 Result, summary table, block Λ, Consequence, ledger entries; Task 17's (1b) cited. New node C5.4, check C5-ord.
- 21b #9 [major] – applied. M-b identified as CFL Lemma 9.2, present at $\Psi_2=0$, failed by the original quartic theory: H2 Result (*The baseline*), M-b row, C8.2.3, C8.2.9, sentence after the table, Scope (*weakest relaxation*), Self-review 19b, Consequence, ledger entry and description rewritten; baseline items (M-b, M-r0) separated from the Hubbard–Stratonovich-specific ones.
- 21a #2 [major] – applied. A11 ($\hbar$ even, central, degree a $\mathbb Z$-label; parities by C6); block 0 remark, Consequence and C? entry cite it.
- 21a #3 [major] – applied. Consequence, *Third*: $\hat{\mathfrak p}\circ\hat{\mathfrak p}=0$ on the genus-zero truncation needs the double-contraction relations, not implied by R87, same $\hbar$-order as a genus-zero relation; Task 20's preservation check must impose them, restrict, or report the failure as this obstruction. Recorded in H-par's "not covered" clause.
- 21b #3 [major] – applied. A9 cites C6 for the parity, the role rule is no longer attributed to CFL; the proposed C? parity entry is withdrawn (one-line pointer for C6's *Checked on*); the Conventions list no longer says signs are unused.
- 21b #4 [major] – applied by declaration (option (a)): hypothesis H-par (statement, motivation, falsifier), carried into C8, *Hypotheses in force*, the MC Commentary (misattributing sentence replaced), the Consequence, the 19b ledger entry (now `Conditional(PH? = H-par) – Verified`) and a PH? entry. The falsifier check (data satisfying the $L_\infty$ relations) was not run: the time box did not allow building such data; the identity comparisons of C8.2 do not use H-par.
- 21b #5 [major] – applied. (MC.8)–(MC.9): the $E_3$, $E_4$ components (five and three terms), rows M-r0 ($g_s^2p_{1,3}(\Psi)$, baseline) and M-r ($f$-dependent); node C8.1.5; check C2-C3-E34 (term list, powers, measured ghost numbers; coefficients by hand).
- 21a minors: #4, #5, #6, #7, #8, #10, #11 applied (block 0 row, block R sentence, Λ twist wording, "derived under A8" flags, genus-zero truncation in A4/C7.1/block R/Consequence, Task 17's answer to (5) handed over with the $\hbar$/$g_s$ identification named, A2 forced); #9 applied in the script (NV check; C2-C3-break now a perturbed rule); note #12 applied (A11, A12 as A-nodes).
- 21b minors: #2, #6, #7, #8, #10, #11, #13 applied (relative coefficients wording, item count nine with M-s labelled, $\beta_0$ in M-a and power-series class, "iff" → "if", case (v) and the inverse-pairing robustness, $\beta$-part qualification, C8.2-action caveat, `eps_out` note, ledger tag conditional); note #12 applied (one sentence on M-a as tree or loop); notes #1, #14 need no change.
- Statuses changed: C4 unchanged; C5, C5.2, C6 statements narrowed to "across $\hbar$-orders" (argument: (H.2'), check C5-ord); new C5.4, C8.1.5; C8 and its ledger entry become conditional on H-par (argument: 21b #4); C8.2.3, C8.2.4, C8.2.9 statements reworded (baseline; "if"; $\beta$-part), verdict H2 unchanged.
- Script: 42/42 PASS at seeds 20261018, 20261019 (exit 0; peak RSS 23 MB); break tests of the new checks (perturbed (E.3) rule, wrong expected order-by-order set) FAIL as expected.

Final fix pass 2026-10-18 (brief `agent/briefs/active-computator-gu-19-fix2-20261018T115346.md`), after critics `agent/reports/critic-gu-21a2-20261018T114158.md` (21a2) and `agent/reports/critic-gu-21b2-20261018T114158.md` (21b2). Every change below is after the last review: no critic has read it.

- 21a2 #2 [major, blocking] – applied after re-deriving the critic's table. (H.2'') and (H.3') added to block H1: the order-by-order criterion fixes $5$ for $\mathfrak m_{2,0}$, $4$ for genus label $-1$, nothing for other integer dressings ($\mathfrak m_{2,g\ge1}$ included) within the genus-zero truncation; whole component $N_{\rm gh}(\mathfrak m_{2,g})=5+g$ with $N_{\rm gh}(\hbar)=-1$. Consequence sentence and C? sentence corrected; C5, C5.4, H1 Result, R? body and description name $\mathfrak m_{2,0}$; Task 20 told that $\mathfrak m_{2,1}$ at $4$ passes order by order only through the absence of genus-one operations (CFL degree $6$) and should grade by the whole-component criterion. New check C5-ord-n (+break).
- 21a2 #1 [major] – applied: A11 cited by C2.1, C3.1, C4, C7.1; A12 by C4.
- 21b2 #1 [major, blocking] – applied: H-par restated with the extended operator (role parities, all words) and composition rule V (fed output converted back to a vertex leg by $\omega$, i.e. the sewing with odd $\omega^{-1}$, R87's sign), statement as a term-by-term identity with the lifted antibracket, falsifier in C6 terms (random vertices suffice; `eps_out` excluded). PH? entry rewritten. Falsifier not run (no role-parity bookkeeping in the engine; over the 10-minute bound).
- 21b2 #2 [major] – applied: the double-contraction relations in *Hypotheses in force* as an open condition expected to fail; C8, MC Commentary, Consequence (3), ledger scope and body say the MC reading needs H-par and those relations.
- 21b2 #3 [major] – applied: the baseline negative statement scoped ($\Psi_2=0$ or any local $\Psi_2(\Psi)$; $p_{2,2}^{-1}$ removes M-b at the price of case (i)) in the H2 Result, the M-b row, Scope, Update, Self-review 19b, C8.2.9, ledger body, description.
- 21b2 #4 [major] – applied: A9 states that $\mathcal E_\Sigma$, $\mathcal M_2^{(6)}$ are output strands and that C6's listing of equations of motion as input strands is to be amended (pointer for the orchestrator in the report).
- 21b2 #5 [major] – applied: C8.1.5 cites A9, C7.1 (A5 dropped).
- 21a2 minors: #3 (block R on Münster–Sachs, from the Münster–Sachs supplement; pointer to Task 16 removed), #4 (Prop. 9.3's status in *Second*), #5 (offset $+(1+x)$), #6 (C? narrowed, Self-review 4 "for the raised family (A3)" with the Münster–Sachs counterexample) applied; note #7 applied in A2 ("among role-independent dictionaries").
- 21b2 minors: #6 (reading (I) includes $\mathcal M_3=\mathcal M_4=0$; M-r0 in C8.2.8, by hand), #7 (A9 and the script docstring on `eps_out` for two-output words), #8 (H-par motivation, in its restatement), #9 (19b R? tagged [Verified], the MC reading as a conditional sentence) applied; notes #10, #11 need no change.
- Statuses changed: C8 statement (the exclusion unconditional, the MC reading conditional on H-par and on the double-contraction relations); 19b R? tag `Conditional(PH? = H-par) – Verified` → `Verified`; C4, C5, C5.4 statements narrowed to $\mathfrak m_{2,0}$ / extended to other dressings (C5.4); C8.2.8 extended (M-r0, by hand); C8.2.9 restated with scope; H-par restated (statement changed, still open). Dependents: C8's restatements (ledger 19b R?, Consequence, Self-review 19b) updated; C5's (summary table, H1 Result, R?) updated; C4's dependents unchanged.
- Script: 46/46 PASS at seeds 20261018, 20261019 (exit 0, peak RSS 23 MB); new break leg C5-ord-n-break FAILs as expected.

Fix pass 3, 2026-10-22 (brief `agent/briefs/active-computator-gu-103-fix3-20261022T195114.md`), mechanical, after the Fable checks `agent/reports/critic-gu-check-103a-20261022T193154.md` (103a) and `agent/reports/critic-gu-check-103b-20261022T193154.md` (103b). Only the critic-supplied replacement texts were put in; no derivation, no script change, no script run. Report: `agent/reports/computator-gu-103-fix3-20261022T195114.md`.

- 103a #2 [minor] – applied: "of $E_1\oplus E_2$" in C5.4 and after "every $s$ is order-by-order homogeneous" in block H1 below (H.2''). Statement of C5.4 narrowed to its class (the $E_3$, $E_4$ components with two $S$ factors are not in the table); justification unchanged.
- 103a #4 [minor] – applied: the summary-table index renamed $n\to L$ (header, last column, note), the dressing exponent of (H.2'') staying $n$; one clause tells the reader the output-counting form is $n=1$.
- 103a #6 [major in consequence] – applied: closing sentence of the grading R? draft narrowed to $\mathfrak m_{2,0}$ (and $\mathfrak m_{2,g\ge1}$ across orders / unconstrained order by order).
- 103a #7 [minor] – applied: H1 Result, referent of the "read as" sentence replaced.
- 103a #8 [minor] – applied: C5-ord-n added to the C? draft's *Checked on*.
- 103b #1 [major] – applied: H-par (rule V) and the PH? draft name R87's sign under the paper's coefficient rule for the `eq:conv:sprod` family on odd-letter words, with the Argued status of the antibracket on odd inputs; the Statement points to it.
- 103b #2 [major] – applied: the extended operator acts on every $k$-subset of letters (output-role letters through rule V); locality clause at the end of rule V (also named in the Motivation); PH? title replaced. Restatements aligned: C8, *Hypotheses in force*, the MC Commentary (l. 380), Consequence *Third* and Update (3) – "$\hat{\mathfrak p}'$ is a differential" no longer attributed to H-par: H-par gives the single-contraction part of $\hat{\mathfrak p}'\circ\hat{\mathfrak p}'$ as the square of one operator, the differential property needs in addition the double-contraction relations –, the H2 R? body and scope, the description. H-par stays open; its statement (not only its justification) changed.
- 103b #6 [major] – applied: H2 R? tagged `[mixed]`, with the *Status* bullet of the report.
- 103b #7 [minor] – applied, both options: the H2 R? title speaks of CFL's Maurer–Cartan expression $e^{-\mathfrak m'}\hat{\mathfrak p}'(e^{\mathfrak m'})$ and the body gains the clause that the components are forced by CFL (2.1) on even words and the exclusion does not depend on whether a reading closes; Self-review 1 carries the same clause.
- Not applied (notes, no replacement text in the brief): 103a #1 (optional line on $\Psi\cdot\Psi$ in CFL's native grading), 103b #5 (counting sentence for the local $\Psi_2(\Psi)$ baseline in block H2 *Scope*), 103b #3, #4, #8–#10 (observations).
- Nodes held out: none failed. H-par has verdict "cannot decide / holds as a hypothesis" (open, entered as `[open]`); per the 103b verdict the paper may state the gradings and the exclusion within local redefinitions with its scope, and may not state that $(\Psi,\Sigma_2)$ is a Maurer–Cartan element of an $\mathrm{IBL}_\infty$ structure of the raised family.
- Dependents of the changed nodes: C5.4 → C5, C6, C7.1, summary table, H1 Result, Consequence (l. 507), Self-review 1, description, grading R? and C? drafts (all consistent per 103a); H-par → C8, *Hypotheses in force*, MC Commentary, Consequence *Third*, Update (3), Self-review 19b, H2 R? and PH? drafts, description (aligned above). C8.1.x, C8.2.x (the exclusion) do not use H-par and are unchanged.

Fix pass 4, 2026-10-22 (brief `agent/briefs/active-computator-gu-103-fix4-20261022T195734.md`), mechanical – the two S4 qualifiers of `agent/reports/critic-gu-proposal-20261022T185327.md` (#7, corrected wording of S4) appended verbatim to the body of the grading R? draft (role-independent dictionaries, A2; Münster–Sachs counter-case, Self-review 4); no node, derivation or script change. Report: `agent/reports/computator-gu-103-fix4-20261022T195734.md`.

Fix pass 5, 2026-10-22 (brief `agent/briefs/active-computator-gu-103-fix5-20261022T200253.md`), mechanical – the C? draft put into the level-2 form of `knowledge/conventions.md` (heading `## C? — …` without tag, local status "Local to the IBL reading of record 103." opening the *Statement*; the four bullets *Statement*, *Conventions it rests on*, *Sources*, *Checked on* unchanged in content; no *Where the project was loose* bullet, the draft has no such text); no claim, node, derivation or script change. Report: `agent/reports/computator-gu-103-fix5-20261022T200253.md`.

## Status

Fix pass 3 (2026-10-22) complete: the replacement texts of the Fable checks 103a and 103b are in (Revisions); no node held out, H-par open. Next: orchestrator promotion of the R?, C?, PH? drafts (the H2 R? as `[mixed]`).
