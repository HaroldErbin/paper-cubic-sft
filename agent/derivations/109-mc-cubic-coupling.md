---
description: Task 19c (revised after critic) – the coupling g_s V_3(Sigma_2,Psi) that the Maurer–Cartan components require (c = 1/6, Psi_2 = Sigma_2/6) is a Psi–Sigma_2 mixing; eliminating Sigma_2 gives S_2 + 6c^2 W at O(g_s^0) in the full action (W = <p12 Psi, p22^{-1} p12 Psi>_2; higher orders only in the quartic truncation, since Sigma_2* = O(1/g_s) moves higher sections down); under H-W, excl. within Sigma_2-sector rescalings, Sigma_2 redefinitions, Psi redefinitions trivial at g_s=0, Psi-only counterterms keeping Q_B Psi at g_s^0: no compensation restores closed SFT at O(g_s^0); g_s-independent linear redefinitions open; kernel directions become Lagrange multipliers
---

# 109 – The cubic coupling $g_s\mathcal V_3(\Sigma_2,\Psi)$ required by the Maurer–Cartan form (Task 19c)

Brief: `agent/briefs/active-computator-gu-19c-cubic-coupling-20261018T103222.md`.
Inherits record 103 as revised (`agent/derivations/103-ibl-mc-conventions.md`, *Revisions*).
Script: `codes/verify-mc-cubic-coupling.py`.

## Task and objective

**Literal task.** Add $c\,g_s\mathcal V_3(\Sigma_2,\Psi)$ to the cubic action of the quartic section, fix $c$ by M-a and M-b, eliminate $\Sigma_2$ at tree level, say whether the result is closed SFT and what could compensate the difference, then gauge invariance and the downstream consequences; stop if no compensation exists.

**Objective.** The question (decisions, 2026-10-18, about 10:10): what the term that the Maurer–Cartan components require does to the theory, as a footnote or paragraph of the paper – why the term is needed, and what it changes.

## Conventions

- Record 103's conventions verbatim (its A1–A12, the output-counting form, C6 for strand parities through its A9, hypothesis H-par for the reading of the components as a Maurer–Cartan equation).
- Physical ghost number (the project conventions). The paper's normalizations of `02-2-quartic.tex` (A2 below).

## Claim tree

- **A1** Record 103 as revised: the components (MC.5)–(MC.7) in the output-counting form, the action $S_{\rm MC}$ (H2.6) whose Euler–Lagrange equations are (MC.5), (MC.7), the mismatch list M-a–M-s. [by 103 C8.1, C8.2.9]
- **A2** The action $S=\tilde S_{\le4}=S_2+S_3-\tfrac{g_s^2}{4!}\mathcal V_4(\Sigma_2^2)+\tfrac{2g_s^2}{4!}\mathcal V_4(\Sigma_2,\Psi^2)$, $S_2=\tfrac12\langle\Psi,Q_B\Psi\rangle$, $S_3=\tfrac{g_s}{3!}\mathcal V_3(\Psi^3)$, $S_4=\tfrac{g_s^2}{4!}\mathcal V_4(\Psi^4)$ (`eq:hs4:S4tilde`, `eq:hs4:action-tilde`); $\mathcal V_3(\Sigma_2,\Psi)$ is $\mathcal V_3$ with the two strands of $\Sigma_2$ in two slots; $\langle A\otimes B,p_{m,2}(X)\rangle_2=\mathcal V_{m+2}(A,B,X)$, $\langle\delta\Psi,\ell_2(\Sigma_2)\rangle=\mathcal V_3(\delta\Psi,\Sigma_2)$ (`eq:hs4:same-vertex` and its cubic analogue). [cited: paper `02-2-quartic.tex`; by R87]
- **A3** $p_{2,2}$ is invertible on the space of $\Sigma_2$ (the paper's invertibility assumption with the Feynman rules; R1's premise); $G:=p_{2,2}^{-1}$; the propagator of $\Sigma_2$ is $-\tfrac{12}{g_s^2}G$ in this sign convention (the Hessian of $-\tfrac{g_s^2}{24}K$ is $-\tfrac{g_s^2}{12}p_{2,2}$; R64: the auxiliary form is indefinite). On the continuum A3 is not established (H-W, open points). Where a kernel is kept, C3.3 replaces A3. [decision; paper `02-2-quartic.tex`, Feynman rules]
- **H-W** The bilinear form $W(\Psi,\Psi')=\langle p_{1,2}(\Psi),G\,p_{1,2}(\Psi')\rangle_2$ on $\mathcal H_2$ is not identically zero (and is finite) for the closed-string vertices. Motivation: (i) the level-zero, zero-strand-momentum truncation of $W$ is $\mathcal V_3(T^3)^2/\mathcal V_4(T^4)\,t^2\neq0$ ($\Psi=t\,T$, $\Sigma_2=s\,T\otimes T$; this inverts the $1\times1$ block of $p_{2,2}$ on $T\otimes T$, not $G$, so it is a truncation of $W$, not $W$ at $\Psi=T$; block 2, Commentary); (ii) no structural reason for isotropy of $\operatorname{im}p_{1,2}$ under $G$ is known – this is the absence of a known obstruction, not an argument that none exists. The finite models (C4.5) have random vertices without the $L_\infty$ relations and are no evidence here. Open points inside H-W: for $\Psi$ of momentum $k$, $p_{1,2}(\Psi)$ is supported on strand momenta $(q,k-q)$ for all $q$, and $p_{2,2}$ connects pairs of equal total momentum, so $W(k)=\int\!\mathrm dq\,\mathrm dq'\,\mathcal V_3(\Psi_k;q,k-q)\,G_k(q,q')\,\mathcal V_3(\Psi'_{-k};q',-k-q')$ (schematic) is a strand-momentum integral – the bubble; its finiteness is not established (the off-shell vertices are expected to fall off in $q$ through the local-coordinate factors, while $G=p_{2,2}^{-1}$ grows where $p_{2,2}$ falls off, so convergence depends on comparing the two), nor is A3 on the continuum (a bounded inverse of $p_{2,2}$ as a kernel in the relative momentum). If $W$ diverges, "$W\not\equiv0$" is the wrong question and the $g_s^0$ term needs a regularization first. Falsified or discharged by: a level truncation of $W(k)$ that keeps the strand-momentum dependence (at level zero, the tachyon-pair block $K_P(s)$ of R53 is the first ingredient), at more than one level – not R64's five-field truncation, which is at zero momentum; cheaper and sharper, in a finite model with the $L_\infty$ relations imposed: whether $S_2+6c^2W$ is invariant under $\delta\Psi=Q_B\Lambda$, i.e. whether $W(Q_B\Lambda,\Psi)=0$ for all $\Lambda,\Psi$ (a nonzero value also discharges H-W in that model and bears on the Scope's case (i)). Used by C4.1, C4.3, C4.4.
- **C1** $c=\tfrac16$ in the paper's normalization, fixed by the Maurer–Cartan action independently of the equivalence under test: $S_{\rm MC}\ni g_s\mathcal V_3(\Psi_2,\Psi)+\tfrac{g_s^2}2\mathcal V_4(\Psi_2,\Psi^2)$ from $e^{\Psi+\Psi_2}$, against $\tfrac{2g_s^2}{4!}\mathcal V_4(\Sigma_2,\Psi^2)$, gives $\Psi_2=\Sigma_2/6$ and $c=\tfrac16$; M-a and M-b each give the same value. [by A1, A2; eq. (1.1)–(1.3)] [check: C1, C2]
- **C2** The equations of motion of $S'$ and the mismatch list: M-a ($\alpha$-part) and M-b supplied; M-q removed by losing the kernel invariance; M-c, M-d, M-e ($\ell_3(\Psi^3)$ part), M-r0, M-r, M-s remain. [by C1, A1; eq. (1.4)–(1.6)] [check: C2]
  - **C2.1** The added term is bilinear in the fields: a mixing between $\Psi$ and $\Sigma_2$, not an interaction. [by A2; block 1]
- **C3** Tree-level elimination. In the quartic truncation $\tilde S_{\le4}+c\,g_s\mathcal V_3(\Sigma_2,\Psi)$: $\Sigma_2^*=\Psi^2+\tfrac{12c}{g_s}G\,p_{1,2}(\Psi)$ and $S'[\Psi]=S_{\le4}+6c\,S_3+6c^2W(\Psi)$, at $c=\tfrac16$ $S_2+\tfrac16W+2S_3+S_4$. In the full action with the coupling, only the $O(g_s^0)$ part, $S_2+6c^2W$, is a statement about the theory (C3.4). [by C3.1–C3.4]
  - **C3.1** The elimination formula. [by A2, A3; eq. (2.1)–(2.4)] [check: C3]
  - **C3.2** The "two $\mathcal V_3$ joined by $p_{2,2}^{-1}$" term is quadratic in $\Psi$ and independent of $g_s$ (the $\Sigma_2$ propagator carries $g_s^{-2}$). In the quartic truncation only, $\mathcal V_4(\Psi^4)$ is reproduced and the cubic coupling is multiplied by $1+6c=2$; these $O(g_s)$, $O(g_s^2)$ statements do not survive in the full action (C3.4). [by C3.1; eq. (2.4)] [check: C3]
  - **C3.3** Without A3: the $\Sigma_2$ equation is solvable iff $\mathcal V_3(N,\Psi)=0$ for every $N\in\ker p_{2,2}$; otherwise the kernel components of $\Sigma_2$ are Lagrange multipliers for these constraints on $\Psi$, and $S'$ is not invariant under $\Sigma_2\to\Sigma_2+N$: the quotient `eq:hs4:quotient` is not available. [by A2; eq. (2.5)] [check: C3.3]
  - **C3.4** Order counting in the full action (the paper's sections with the coupling added): with $\Sigma_2^*=O(g_s^{-1})$, a term $g_s^{n-2}\mathcal V_n(\Sigma_2^k,\Psi^{n-2k})$ contributes to $S'[\Psi]$ first at order $g_s^{n-2-k}$, so order $g_s^p$ receives terms from every section with $n\le2p+4$. At $O(g_s^0)$ only $n\le4$ enters and $S'[\Psi]|_{g_s^0}=S_2+6c^2W$ is complete; at $O(g_s)$ the quintic term $\tfrac{g_s^3}{5!}\mathcal V_5(\Sigma_2^2,\Psi)$ adds $\tfrac{144c^2}{5!}g_s\mathcal V_5((Gp_{1,2}\Psi)^2,\Psi)=\tfrac1{30}g_s\mathcal V_5((Gp_{1,2}\Psi)^2,\Psi)$ at $c=\tfrac16$, and higher sections add more. [by C3.1, A2; block 2, *Order counting*]
- **C4** Under H-W, excl. within (a)–(d) of block 2 (Scope): for $c\neq0$, no compensation makes $S'$ equivalent to closed SFT at $O(g_s^0)$ while keeping M-a, M-b and the $g_s^0$ part $Q_B\Psi$ of (MC.5) (with $\Sigma_2$ counted as $O(1)$). Not covered: $g_s$-independent linear redefinitions of $\Psi$, to which mixed redefinitions $\Psi\to\Psi+g_sf(\Sigma_2)$ reduce (Scope (i), open for the closed string). [by C3.4, C4.1–C4.5]
  - **C4.1** Under H-W, (a) rescalings of the two coefficients of the $\Sigma_2$ sector, with the operator $p_{2,2}$ of (MC.7) kept: the $O(g_s^0)$ induced term is $\tfrac{c^2}{2a}W$, independent of the source coefficient; it vanishes only for $c=0$. [by H-W, C3.1, C3.4; eq. (2.6)]
  - **C4.2** (b) A redefinition of $\Sigma_2$, invertible in $\Sigma_2$, leaves $S'[\Psi]$ unchanged. [by C3.1; block 2, Commentary (b)]
  - **C4.3** Under H-W, (c) a redefinition $\Psi\to\Psi+O(g_s)$ leaves the $O(g_s^0)$ part of the action equal to $S_2$, so it cannot remove $6c^2W$. [by H-W, C3.4; eq. (2.7)]
  - **C4.4** Under H-W, (d) counterterms in $\Psi$ alone: $-6c^2W$ restores $S_2$ at $O(g_s^0)$ (with $-6cS_3$ it restores $S_{\le4}$ in the quartic truncation), and it keeps M-a ($c\,g_s\ell_2(\Sigma_2)$ stays in $\mathcal E''_\Psi$) and M-b ($\mathcal E''_\Sigma$ unchanged); what excludes it is the criterion that the $g_s^0$ part of the $\Psi$ equation, $\Sigma_2$ counted as $O(1)$, is $Q_B\Psi$ – it is $Q_B\Psi-12c^2D\Psi$. The criterion is the filtration: the $g_s^0$ part of a Maurer–Cartan equation with fields of nonnegative order is the differential being deformed, while the residuals of $S'$ at $O(g_s^2)$ (M-e) are mismatches of the deformation. Equivalently the counterterm undoes the coupling by $\Sigma_2\to\Sigma_2-\tfrac{12c}{g_s}Gp_{1,2}(\Psi)$, record 103's Scope (i). [by H-W, C3.1, C3.4, A1; eq. (2.8)] [check: C4.4]
  - **C4.5** $W\not\equiv0$ and $D\Psi\neq0$ in the finite models, at both seeds. The model vertices are random and do not satisfy the $L_\infty$ relations, so this is no evidence against a structural vanishing of $W$; it only shows the identities are not empty. [by check: C4.5]
- **C5** Outside the class of C4: in a finite model with $Q^2=0$, $Q(\mathcal H_1)=0$ at ghost $2$ and $\operatorname{rank}B_Q=1$ on $\mathcal H_2$, $\operatorname{rank}(B_Q+12c^2B_D)=2$ at $c=\tfrac16$, so no $g_s$-independent linear redefinition (congruence) maps the free part of $S'[\Psi]$ to that of closed SFT there. [by check: C5]

Open gaps: none (C5 is a finite-model statement; its closed-string form, the decisive open case of the Scope (i), is argued, not claimed)
Hypotheses in force: H-W (C4 and its children C4.1, C4.3, C4.4); A3 is a decision whose continuum form is open (H-W, point (ii)); H-par of record 103 only for reading (MC.5)–(MC.7) as a Maurer–Cartan equation – C1, C2 compare with these expressions and do not use it

## Block 1 – the modified action, its equations of motion, the mismatch list (step 1)

\subsection*{Setup}
A1, A2. Free constants of the assembly (protocol *Free constants*): $c$ (the new coupling), $\alpha$ in $\Psi_2=\alpha\Sigma_2$ (the identification), and the paper's two coefficients $-\tfrac1{4!}$, $\tfrac2{4!}$. The paper's coefficients are fixed by the paper; $\alpha$ and $c$ are fixed by the Maurer–Cartan action $S_{\rm MC}$ (103, (H2.6)), whose coefficients come from the exponential $e^{\Psi+\Psi_2}$ alone. None is fitted from the equivalence tested in block 2.

\subsection*{Derivation}
The Maurer–Cartan action through $O(g_s^2)$ (103, (H2.6)):
$$
S_{\rm MC}(\Psi,\Psi_2)=S_{\le4}(\Psi)+g_s\,\mathcal V_3(\Psi_2,\Psi)+\frac{g_s^2}{2}\,\mathcal V_4(\Psi_2,\Psi^2)+\frac{g_s^2}{2}\,\mathcal V_4(\Psi_2,\Psi_2).
\tag{1.1}
$$
The modified action:
$$
S'=S+c\,g_s\,\mathcal V_3(\Sigma_2,\Psi)
=S_2+S_3+c\,g_s\,\mathcal V_3(\Sigma_2,\Psi)+\frac{2g_s^2}{4!}\,\mathcal V_4(\Sigma_2,\Psi^2)-\frac{g_s^2}{4!}\,\mathcal V_4(\Sigma_2,\Sigma_2).
\tag{1.2}
$$
With $\Psi_2=\alpha\Sigma_2$, the terms of (1.1) linear in $\Psi_2$ are $\alpha g_s\mathcal V_3(\Sigma_2,\Psi)+\tfrac{\alpha g_s^2}{2}\mathcal V_4(\Sigma_2,\Psi^2)$. The mixed term fixes $\alpha$: $\tfrac\alpha2=\tfrac2{4!}$, and the coupling fixes $c=\alpha$:
$$
\alpha=\tfrac16,\qquad c=\tfrac16 .
\tag{1.3}
$$
The variations (A2):
$$
\begin{aligned}
\mathcal E'_\Psi&=Q_B\Psi+\frac{g_s}{2}\,\ell_2(\Psi^2)+c\,g_s\,\ell_2(\Sigma_2)+\frac{g_s^2}{3!}\,\ell_3(\Psi,\Sigma_2),\\
\mathcal E'_\Sigma&=c\,g_s\,p_{1,2}(\Psi)+\frac{g_s^2}{12}\bigl[p_{2,2}(\Psi^2)-p_{2,2}(\Sigma_2)\bigr],
\end{aligned}
\tag{1.4}
$$
with $\delta S'=\langle\delta\Psi,\mathcal E'_\Psi\rangle+\langle\delta\Sigma_2,\mathcal E'_\Sigma\rangle_2$; in the paper's normalization of `eq:hs4:eom-sigma`, $\tfrac{12}{g_s^2}\mathcal E'_\Sigma=\tfrac{2}{g_s}p_{1,2}(\Psi)+p_{2,2}(\Psi^2)-p_{2,2}(\Sigma_2)$ at $c=\tfrac16$. Against the components with $\Psi_2=\Sigma_2/6$, using (MC.5), (MC.7):
$$
\mathcal E'_\Psi-\mathcal M_1=-\frac{g_s^2}{3!}\,\ell_3(\Psi^3)+\bigl(c-\tfrac16\bigr)g_s\,\ell_2(\Sigma_2),
\tag{1.5}
$$
$$
\mathcal E'_\Sigma-\tfrac16\,\mathcal M_2^{(6)}=\bigl(c-\tfrac16\bigr)g_s\,p_{1,2}(\Psi)-\frac{g_s^2}{9}\,p_{2,2}(\Sigma_2),
\tag{1.6}
$$
and at the level of actions
$$
S_{\rm MC}(\Psi,\Sigma_2/6)-S'(\Psi,\Sigma_2)=S_4+\frac{g_s^2}{18}\,\mathcal V_4(\Sigma_2,\Sigma_2)+\bigl(\tfrac16-c\bigr)g_s\,\mathcal V_3(\Sigma_2,\Psi).
\tag{1.7}
$$

\subsection*{Commentary}
(1.3): the two conditions of the brief are one condition at the level of the action. M-a ($g_s\ell_2(\Psi_2)$ in $E_1$) and M-b ($g_sp_{1,2}(\Psi)$ in $E_2$) are the two variations of $g_s\mathcal V_3(\Psi_2,\Psi)$, and the terms they are measured against, $g_s^2\ell_3(\Psi,\Psi_2)$ in $E_1$ and $\tfrac{g_s^2}2p_{2,2}(\Psi^2)$ in $E_2$, are the two variations of $\tfrac{g_s^2}2\mathcal V_4(\Psi_2,\Psi^2)$. The ratio $1:\tfrac12$ of the two couplings in (1.1) is the ratio of the length-3 and length-4 parts of $e^{\Psi+\Psi_2}$ linear in $\Psi_2$ ($\Psi_2\Psi$ and $\tfrac12\Psi_2\Psi^2$); in (1.2) it must be $c:\tfrac1{12}$. So M-a against the $\ell_3$ term and M-b against the source term give the same $c=\tfrac16$, and the identification is $\Psi_2=\Sigma_2/6$, not $\Psi_2=\Sigma_2$: the brief's $\Psi_2=\Sigma_2$ names the object, (1.3) fixes the normalization. With $\Sigma_2$ rescaled to $\Psi_2$ the coupling reads $g_s\mathcal V_3(\Psi_2,\Psi)$ with coefficient one, and the paper's mixed term reads $\tfrac{g_s^2}{2}\mathcal V_4(\Psi_2,\Psi^2)$.
(C2.1) $\mathcal V_3(\Sigma_2,\Psi)$ has one slot filled by $\Psi$ and two by the strands of one $\Sigma_2$: it is bilinear in the fields. In the action it is a quadratic term, a mixing between the one-string and the two-string field, of order $g_s$; the brief's name "cubic coupling" refers to the vertex $\mathcal V_3$, not to the degree in the fields. Its variation M-b, $c\,g_sp_{1,2}(\Psi)$, is accordingly linear in the fields (103, reading (III)).
The mismatch list of 103 with $S'$ in place of $S$, $\Psi_2=\Sigma_2/6$, $c=\tfrac16$:

| # | status with $S'$ | reason |
|---|---|---|
| M-a | supplied ($\alpha$-part) | (1.5): no $\ell_2(\Sigma_2)$ residual at $c=\tfrac16$; the $\beta$-part ($\beta=0$ here) is not at issue |
| M-b | supplied | (1.6): no $p_{1,2}(\Psi)$ residual at $c=\tfrac16$; it is now the $\delta\Sigma_2$ variation of an action term, not a constraint on $\Psi$ alone (block 2) |
| M-c | remains | (1.6): $p_{2,2}(\Sigma_2)$ with $-\tfrac{1}{12}$ in $\mathcal E'_\Sigma$ against $+\tfrac1{36}$ in $\tfrac16\mathcal M_2^{(6)}$; reading (I) with $c_2$ free needs $\alpha=-\tfrac12$ against $\tfrac16$ |
| M-d | remains | (MC.6), the ghost-5 sector of the lifts, is not the variation of any action (103, H2.6 Commentary); $S'$ adds nothing to it |
| M-e | remains for $\ell_3(\Psi^3)$ | (1.5): $\mathcal E'_\Psi$ has $\tfrac{g_s^2}{3!}\ell_3(\Psi,\Sigma_2)$, matched by $\alpha=\tfrac16$, and no $\tfrac{g_s^2}{3!}\ell_3(\Psi^3)$; $\beta=-\tfrac16$ would supply it at the price of $-\tfrac{g_s}6\ell_2(\Psi^2)$ in $E_1$ (103, M-a $\beta$-part) |
| M-q | removed, by loss | $S'$ and $\mathcal E'_\Psi$ change by $c\,g_s\mathcal V_3(N,\Psi)$, $c\,g_s\ell_2(N)$ under $\Sigma_2\to\Sigma_2+N$, $N\in\ker p_{2,2}$: the equations lose the invariance the components never had (C3.3) |
| M-r0 | remains | $g_s^2p_{1,3}(\Psi)$ in $E_3$; $S'$ has no three-string field (baseline, CFL Lemma 9.2) |
| M-r | remains | the $f$-dependent $E_3$, $E_4$ terms; no three- or four-string equation in $S'$ |
| M-s | remains | (1.7): $\mathcal V_4(\Sigma_2,\Sigma_2)$ with $-\tfrac1{24}$ in $S'$ against $+\tfrac1{72}$ in $S_{\rm MC}(\Psi,\Sigma_2/6)$ |

(1.7) is the whole list at the level of the action: with $c=\tfrac16$ the two actions differ by the quartic contact term $S_4$ (M-e) and by the coefficient of $\mathcal V_4(\Sigma_2,\Sigma_2)$ (M-c, M-s); M-d, M-r0, M-r are not visible in actions of $(\Psi,\Sigma_2)$.

\subsection*{Result}
$$
\boxed{\;S'=\tilde S_{\le4}+\tfrac{g_s}{6}\,\mathcal V_3(\Sigma_2,\Psi),\qquad \Psi_2=\tfrac16\Sigma_2\;}
$$
supplies M-a and M-b and removes M-q (by loss of the kernel invariance); M-c, M-d, M-e ($\ell_3(\Psi^3)$ part), M-r0, M-r, M-s remain.

\subsection*{Verification}
Checks C1 (action level, (1.7), against $S_{\rm MC}$ built from the exponential), C2 ((1.5), (1.6) against the literal components of 103's engine), with break legs; block V.

## Block 2 – elimination of $\Sigma_2$ and the compensations (step 2)

\subsection*{Setup}
A2, A3 (C3.3 without A3); block 1. $K(A,B):=\mathcal V_4(A,B)=\langle A,p_{2,2}B\rangle_2$ on two-string states with $(2,2)$ strands, symmetric; $G=p_{2,2}^{-1}$, so $\langle Gx,y\rangle_2=\langle x,Gy\rangle_2$; $W(\Psi):=\langle p_{1,2}(\Psi),G\,p_{1,2}(\Psi)\rangle_2$, $D:=\ell_2\,G\,p_{1,2}:\mathcal H_2\to\mathcal H_3$, so that $\delta W=2\langle\delta\Psi,D\Psi\rangle$ (A2: $\langle p_{1,2}(\delta\Psi),Y\rangle_2=\mathcal V_3(Y,\delta\Psi)=\langle\delta\Psi,\ell_2(Y)\rangle$).

\subsection*{Derivation}
The $\Sigma_2$-dependent part of (1.2) is a source and a quadratic form:
$$
S'=S_2+S_3+\langle\Sigma_2,j\rangle_2-\frac{g_s^2}{24}\,K(\Sigma_2,\Sigma_2),\qquad
j:=c\,g_s\,p_{1,2}(\Psi)+\frac{g_s^2}{12}\,p_{2,2}(\Psi^2).
\tag{2.1}
$$
$\mathcal E'_\Sigma=j-\tfrac{g_s^2}{12}p_{2,2}(\Sigma_2)=0$ gives
$$
\Sigma_2^*=\frac{12}{g_s^2}\,G\,j=\Psi^2+\frac{12c}{g_s}\,G\,p_{1,2}(\Psi),
\tag{2.2}
$$
and, since $K(\Sigma_2^*,\Sigma_2^*)=\tfrac{12}{g_s^2}\langle\Sigma_2^*,j\rangle_2$,
$$
S'[\Psi]=S_2+S_3+\tfrac12\langle\Sigma_2^*,j\rangle_2=S_2+S_3+\frac{6}{g_s^2}\,\langle j,G\,j\rangle_2 .
\tag{2.3}
$$
Expanding with $\langle G\,p_{1,2}(\Psi),p_{2,2}(\Psi^2)\rangle_2=\langle p_{1,2}(\Psi),\Psi^2\rangle_2=\mathcal V_3(\Psi^3)$ and $\langle\Psi^2,p_{2,2}(\Psi^2)\rangle_2=\mathcal V_4(\Psi^4)$:
$$
\boxed{\;S'[\Psi]=S_{\le4}[\Psi]+6c\,S_3+6c^2\,W(\Psi)\;\overset{c=1/6}{=}\;S_2+\tfrac16\,W(\Psi)+2S_3+S_4\;}
\tag{2.4}
$$
*Kernel.* Without A3, let $N\in\ker p_{2,2}$. Since $K(N,\cdot)=0$,
$$
S'(\Psi,\Sigma_2+\lambda N)-S'(\Psi,\Sigma_2)=\lambda\,c\,g_s\,\mathcal V_3(N,\Psi),
\tag{2.5}
$$
so the component of $\Sigma_2$ along $N$ enters linearly: a Lagrange multiplier for $\mathcal V_3(N,\Psi)=\langle N,p_{1,2}(\Psi)\rangle_2=0$. Equivalently, $\mathcal E'_\Sigma=0$ requires $j\in\operatorname{im}p_{2,2}=(\ker p_{2,2})^\perp$ (finite dimension, $K$ symmetric), and $\langle N,j\rangle_2=c\,g_s\mathcal V_3(N,\Psi)$.
*Compensations.* (a) Coefficients of the $\Sigma_2$ sector: replace $-\tfrac{g_s^2}{24}K$ by $-\tfrac{a g_s^2}{2}K$ and $\tfrac{g_s^2}{12}$ in $j$ by $b\,g_s^2$; the same steps give
$$
S''[\Psi]=S_2+S_3+\frac{c^2}{2a}\,W(\Psi)+\frac{cb}{a}\,g_s\,\mathcal V_3(\Psi^3)+\frac{b^2}{2a}\,g_s^2\,\mathcal V_4(\Psi^4),
\tag{2.6}
$$
whose $O(g_s^0)$ part beyond $S_2$ is independent of $b$ and vanishes, for $W\not\equiv0$, only at $c=0$.
(c) For any redefinition $\Psi=\Psi'+g_sF(\Psi';g_s)$, $S_{\le4}(\Psi)=S_2(\Psi')+O(g_s)$, so
$$
S'[\Psi]\big|_{g_s^0}=S_2+6c^2W\neq S_2=S_{\le4}\big|_{g_s^0}\quad(W\not\equiv0)
\tag{2.7}
$$
cannot be matched. A $g_s$-independent redefinition with linear part $M$ needs $M^{\rm t}(B_Q+12c^2B_D)M=B_Q$ for the forms $B_Q(\Psi,\Psi')=\langle\Psi,Q_B\Psi'\rangle$, $B_D(\Psi,\Psi')=\langle\Psi,D\Psi'\rangle$ on $\mathcal H_2$; in finite dimension this needs equal ranks.
(d) Counterterms in $\Psi$ alone: $S'-6c^2W-6cS_3$ eliminates to $S_{\le4}$ by (2.4), and its $\Psi$ equation is
$$
\mathcal E''_\Psi=Q_B\Psi-12c^2\,D\Psi+(1-6c)\frac{g_s}{2}\,\ell_2(\Psi^2)+c\,g_s\,\ell_2(\Sigma_2)+\frac{g_s^2}{3!}\,\ell_3(\Psi,\Sigma_2)
=Q_B\Psi+c\,g_s\,\ell_2\!\Bigl(\Sigma_2-\tfrac{12c}{g_s}Gp_{1,2}(\Psi)\Bigr)+\dots
\tag{2.8}
$$
whose $O(g_s^0)$ part $Q_B\Psi-12c^2D\Psi$ is not that of (MC.5), $Q_B\Psi$.
*Order counting in the full action (C3.4).* (2.1)–(2.4) use the quartic truncation. Set $\sigma:=g_s\Sigma_2$, so that $\sigma^*=12c\,Gp_{1,2}(\Psi)+g_s\Psi^2$ is of order one. A term of the paper's action, or of the coupling,
$$
g_s^{n-2}\,\mathcal V_n(\Sigma_2^k,\Psi^{n-2k})=g_s^{n-2-k}\,\mathcal V_n(\sigma^k,\Psi^{n-2k}),
\tag{2.9}
$$
contributes first at order $g_s^{n-2-k}$; since $k\le n/2$, order $g_s^p$ receives terms from every section with $n\le2p+4$. At $p=0$: $n\le4$, the terms $S_2$, $c\,g_s\mathcal V_3(\Sigma_2,\Psi)$ ($n=3$, $k=1$) and $-\tfrac{g_s^2}{4!}\mathcal V_4(\Sigma_2^2)$ ($n=4$, $k=2$), all present in (2.1): $S'[\Psi]|_{g_s^0}=S_2+6c^2W$ holds in the full action. At $p=1$, the first-order change of $\sigma^*$ does not change the stationary value, so the $O(g_s)$ part is the $O(g_s)$ part of the action at $\sigma^*|_{g_s^0}$; besides $(1+6c)S_3$ from (2.4), the quintic term $\tfrac{g_s^3}{5!}\mathcal V_5(\Sigma_2^2,\Psi)$ ($n=5$, $k=2$) gives
$$
\frac{(12c)^2}{5!}\,g_s\,\mathcal V_5\bigl((Gp_{1,2}\Psi)^2,\Psi\bigr)\overset{c=1/6}{=}\frac{1}{30}\,g_s\,\mathcal V_5\bigl((Gp_{1,2}\Psi)^2,\Psi\bigr),
\tag{2.10}
$$
and any $n=6$ term with three $\Sigma_2$ adds more. At $p=2$: the cross term of $\mathcal V_5(\Sigma_2^2,\Psi)$ with $\sigma^*=g_s\Psi^2$, the sextic $\mathcal V_6(\Psi^2,\Sigma_2^2)$ term, and others. So the "doubled cubic coupling" and the reproduction of $S_4$ in (2.4) are properties of the quartic truncation, not of the theory with the coupling. What (2.10) does (Argued, counting only): it is a cubic, nonlocal self-coupling of $\Psi$ at the order of $S_3$, built from two bubble insertions $Gp_{1,2}\Psi$ on a quintic vertex, so the $O(g_s)$ cubic coupling of $S'[\Psi]$ is $2S_3$ plus nonlocal terms from every section with $n\le6$, and nothing in the record says whether they combine into $S_3$.

\subsection*{Commentary}
(2.2): the solution has a part of order $g_s^{-1}$, linear in $\Psi$: the source M-b is of order $g_s$ while the $\Sigma_2$ propagator, $-\tfrac{12}{g_s^2}G$ in this sign convention (the Hessian of $-\tfrac{g_s^2}{24}K$ is $-\tfrac{g_s^2}{12}p_{2,2}$; R64: the auxiliary form is indefinite), is of order $g_s^{-2}$. This is the mechanism of the whole block. With $\Sigma_2$ an independent field, M-b is no longer a constraint on $\Psi$ (as it is for the quartic theory at $\Psi_2=0$, 103's baseline): it is solved for $\Sigma_2$. The price is the $g_s^{-1}$ part of $\Sigma_2^*$, which M-a feeds back into the $\Psi$ equation at order $g_s\cdot g_s^{-1}=g_s^0$. In the Maurer–Cartan reading the same solution is $\Psi_2^*=\Sigma_2^*/6$, of negative $g_s$-order, outside the filtration of CFL (9.1) as answered by Task 17's review (fields of positive $g_s$-order; 103, *Consequence*, Second).
(2.4), (C3.2): the term built from two couplings $\mathcal V_3(\Sigma_2,\Psi)$ and one $\Sigma_2$ propagator is $\tfrac{6c^2}{g_s^2}\cdot g_s^2\,W$: quadratic in $\Psi$, of order $g_s^0$, not a quartic term. As a string diagram it reads, heuristically, as a bubble: both strands of the $\Sigma_2$ line leave one cubic vertex and enter the other, through the inverse of the quartic vertex, so the two strands close a loop. $G$ is the inverse of a four-point vertex, not a pair of propagators, so the genus-one reading is a heuristic; what it gets right is that $W$ carries an integral over the strand momentum (H-W, point (ii)). Compare the one-loop topology that Task 17's review assigns to $\mathfrak p_{2,1,0}(\mathfrak m_{2,0})$ (M-a), here produced by a tree-level elimination because $\Sigma_2$ is a two-strand field. In the quartic truncation (not in the full action, (2.9)), the cross term of the coupling with the source $\tfrac{g_s^2}{12}p_{2,2}(\Psi^2)$ gives $c\,g_s\mathcal V_3(\Psi^3)=6c\,S_3$, so the cubic coupling becomes $(1+6c)\tfrac{g_s}{3!}=2\cdot\tfrac{g_s}{3!}$; the square of the source gives back $S_4$ exactly, as in `eq:hs4:eliminate`. At level zero, $\Psi=tT$, $\Sigma_2=s\,T\otimes T$: $S'\ni c\,g_s\mathcal V_3(T^3)\,st-\tfrac{g_s^2}{24}\mathcal V_4(T^4)s^2$, and eliminating $s$ gives $6c^2\,\mathcal V_3(T^3)^2/\mathcal V_4(T^4)\,t^2$, a shift of the tachyon mass term at order $g_s^0$. This restricts $\Sigma_2$ to the single state $T\otimes T$ at zero strand momenta: it inverts the $1\times1$ block of $p_{2,2}$, not $G$, and is the level-zero, zero-strand-momentum truncation of $W$, not $W$ at $\Psi=T$ (H-W's motivation, as restated).
(2.5): the parallel of R38, where the quotient is compatible with $\mathcal V_5$ iff $\mathcal V_5(\ker\mathcal V_4,\dots)=0$; here the quotient is compatible with the new coupling iff $\mathcal V_3(\ker\mathcal V_4,\mathcal H_2)=0$. Without that, the kernel directions are no longer pure redundancy (`eq:hs4:kernel`: "drops out of every equation"): they impose $p_{1,2}(\Psi)\in(\ker p_{2,2})^\perp$ on $\Psi$. The condition $\mathcal V_3(\ker\mathcal V_4,\mathcal H_2)=0$ is the cubic analogue of PH5's second clause ($\mathcal V_5$, $\mathcal V_6$ annihilate the kernel); PH5's first clause (no kernel at generic momentum, supported at level zero by R53) makes it vacuous. When the kernel is nonzero, A3 fails: (2.2)–(2.4) then hold on the quotient only if the condition holds, and otherwise only on the constraint surface $p_{1,2}(\Psi)\perp\ker p_{2,2}$, with $G$ the inverse of $p_{2,2}$ on the complement of the kernel.
(2.6): the source coefficient $b$ moves only the cubic and quartic induced terms; the $g_s^0$ term is fixed by $c$ and by the operator of the quadratic term. The class keeps that operator equal to $p_{2,2}$, as the Maurer–Cartan component (MC.7) requires (its operator on $\Psi_2$ is $p_{2,2}$, only its coefficient is wrong, M-c). Replacing it by another invertible operator $A$ gives $\tfrac{c^2}{2a}\langle p_{1,2}\Psi,A^{-1}p_{1,2}\Psi\rangle_2$, which vanishes if the image of $p_{1,2}$ on $\mathcal H_2$ is isotropic for $A^{-1}$; this is outside the class and incompatible with (MC.7) (Scope).
(b): a redefinition $\Sigma_2\to\Sigma_2'(\Sigma_2,\Psi)$ invertible in $\Sigma_2$ does not change the value of $S'$ at its stationary point in $\Sigma_2$, so $S'[\Psi]$ is unchanged; in particular the shift $\Sigma_2\to\Sigma_2-\tfrac{12c}{g_s}Gp_{1,2}(\Psi)$, which removes the coupling from (2.1), moves $-6c^2W-6cS_3$ into the $\Psi$ sector: it is (d).
(2.7): equivalence of interacting theories with the same free limit is by redefinitions $\Psi\to\Psi+O(g_s)$; these cannot touch the $g_s^0$ part. A $g_s$-independent redefinition changes the free theory's description: it needs a congruence of the free Hessians; with $Q_B$ nilpotent, $B_Q$ is degenerate on $\mathcal H_2$ (pure gauge and physical directions), and if $B_D$ is nonzero on $\ker B_Q$ the rank of $B_Q+tB_D$ exceeds that of $B_Q$ for all but finitely many $t$: the free gauge invariance or the free spectrum changes (C5, finite model; argued for the closed string).
(2.8): the counterterms reproduce closed SFT exactly, but they are the inverse of the coupling: in $\mathcal E''_\Psi$ the coupling enters only through the combination $\Sigma_2-\tfrac{12c}{g_s}Gp_{1,2}(\Psi)$, which vanishes on the $p_{1,2}$-part of the solution (2.2). The term $g_s\ell_2(\Psi_2)$ of (MC.5) is then present with the field shifted by a $g_s^{-1}$ nonlocal function of $\Psi$, and the $g_s^0$ part of the $\Psi$ equation is not $Q_B\Psi$: this is 103's Scope (i), case (d) here, with the same conclusion.

\subsection*{Result}
(2.4), (2.9): in the full action with the coupling, $S'[\Psi]=S_2+\tfrac16W+O(g_s)$: it differs from closed SFT by $\tfrac16W$ at order $g_s^0$ (a nonlocal correction of the kinetic term). The $O(g_s)$ and $O(g_s^2)$ coefficients of (2.4) – a doubled cubic coupling, $S_4$ reproduced – hold in the quartic truncation only; in the full action the higher sections contribute at these orders, (2.10). The stop condition holds at $O(g_s^0)$: within (a) rescalings of the $\Sigma_2$-sector coefficients with the operator $p_{2,2}$ kept, (b) redefinitions of $\Sigma_2$, (c) redefinitions $\Psi\to\Psi+O(g_s)$, (d) counterterms in $\Psi$ alone that keep M-a, M-b and the $g_s^0$ part $Q_B\Psi$ of (MC.5), no compensation makes $S'$ equivalent to closed SFT, provided $W\not\equiv0$ (H-W). Equivalence under a $g_s$-independent linear redefinition of $\Psi$ is open for the closed string (Scope (i)). The obstruction is the order: M-b is a source of order $g_s$ for a field whose propagator is of order $g_s^{-2}$.

### Scope of the exclusion

- *Class.* (a)–(d) above, the $O(g_s^0)$ part of the full action (complete by (2.9)), genus zero, the paper's action with $\Sigma_2$ on $(2,2)$ strands; physical reason: these are the compensations the brief names (a change of the quartic sector, of the source, a field redefinition) restricted to those that keep the operator $p_{2,2}$ of (MC.7) and the $g_s^0$ part $Q_B\Psi$ of (MC.5), i.e. compatible with the Maurer–Cartan components the coupling was added for. Class (d) taken as "counterterms compatible with (MC.5)" would be empty by definition; its content is the criterion of C4.4 (the counterterm keeps M-a and M-b and fails only the $g_s^0$ part $Q_B\Psi$, which the filtration makes the defining one, as in 103's Scope (i)). (c) is the standard notion of equivalence of two perturbative expansions around the same free theory.
- *Relevant cases outside.* (i) – the decisive open case – $g_s$-independent redefinitions of $\Psi$ with a nontrivial linear part. Mixed redefinitions $\Psi\to\Psi+g_sf(\Sigma_2)$, in none of (a)–(d), can cancel the part of the mixing that couples to $Q_B\Psi$; after elimination, $\Sigma_2^*\simeq\tfrac{12c}{g_s}Gp_{1,2}\Psi$, they amount to $\Psi\to\Psi+12c\,f(Gp_{1,2}\Psi)+O(g_s)$, a $g_s$-independent redefinition, i.e. this case (Argued). Excluded when the Hessian rank changes: C5 in a finite model with random vertices; for the closed string the rank argument is not meaningful in infinite dimension, so the case is open. The way to close it is the free gauge-invariance test of H-W (whether $W(Q_B\Lambda,\Psi)=0$): if $S_2+6c^2W$ loses the invariance $\delta\Psi=Q_B\Lambda$ without a replacement, no redefinition of this kind maps it to $S_2$. (ii) A quadratic operator $A\neq\lambda p_{2,2}$ for $\Sigma_2$ with $\operatorname{im}p_{1,2}$ isotropic for $A^{-1}$: removes $W$, but replaces the operator on $\Psi_2$ in (MC.7), and the quartic term then needs $\langle p_{2,2}\Psi^2,A^{-1}p_{2,2}\Psi^2\rangle$ to reproduce $\mathcal V_4(\Psi^4)$; not explored. (iii) A $g_s$-dependent rescaling of $\Sigma_2$ ($\sigma=g_s\Sigma_2$ makes the coupling order $g_s^0$ and the mixing manifest); it changes no statement at $O(g_s^0)$, and it is the variable in which the truncation is visibly inconsistent beyond $g_s^0$ ((2.9): the higher sections fall to lower orders). (iv) Additional fields (a three-string field for M-r0, M-r) or a different family (Task 25).
- *Weakest relaxation that evades it.* Dropping the coupling ($c=0$, the paper's action) or giving it the order $g_s^n$ with $n\ge2$ (then (2.2) has no negative power and $W$ enters at $O(g_s^{2n-2})$, at $n=2$ the order of a one-loop self-energy); the Maurer–Cartan components fix it at order $g_s$, so the relaxation is a change of the weight $g_s^{k+\ell-2}$ of the family, i.e. of the identification $g_s=\tau$ (103, A6).

\subsection*{Verification}
Checks C3 (elimination by an exact linear solve at six values of $g_s$, Laurent coefficients extracted, against (2.4) with $W$ from the engine's raised products), C3.3 (kernel model), C4.4, C4.5, C5, with break legs; block V.

## Block V – verification

Script `codes/verify-mc-cubic-coupling.py`, run from the project root with `uv run --no-sync python codes/verify-mc-cubic-coupling.py`: 14/14 PASS at seeds 20261018 and 20261019 (one run covers both), exit 0, peak RSS 27 MB (`/usr/bin/time -v`). Engine: record 103's `Data` (model $\dim8$, ghosts $0$–$5$, pairing at $5$, $\mathcal V_n$ at $2n$, random graded-symmetric vertices), its literal CFL path `mc_block`, and `raise_family`; exact Fractions. The action $S'$ is evaluated by tensor contraction of the vertices; the components and the raised operations come from the other side of the engine, so each check compares two paths.

- **C1** – (1.7): $S_{\rm MC}(\Psi,\Sigma_2/6)$, built from the vertices on $e^{\Psi+\Psi_2}$ in the symmetric algebra (minus $\mathcal V_2(\Psi_2)$), minus $S'$ at $c=\tfrac16$ equals $S_4+\tfrac{g_s^2}{18}\mathcal V_4(\Sigma_2,\Sigma_2)$ at three values of $g_s$. Break legs FAIL: $\Psi_2=\Sigma_2$; the difference without $S_4$.
- **C2** – (1.5), (1.6): the gradients of $S'$ (exact finite differences of the action polynomial, along $e_x$ and along the symmetric $(2,2)$ basis tensors) equal the literal (MC.5) and $\tfrac16$(MC.7) at $\Psi_2=\Sigma_2/6$ plus the predicted residuals ($-\tfrac{g_s^2}{6}\ell_3(\Psi^3)$, $-\tfrac{g_s^2}{9}p_{2,2}(\Sigma_2)$, from the raised operations); the tensor form of (MC.7) equals the literal block. Break legs FAIL: $c=\tfrac13$; residuals dropped.
- **C3** – (2.4): the $\Sigma_2$ equation solved exactly at six values of $g_s$, the stationary value fitted by Laurent coefficients $g_s^{-2}$ to $g_s^3$: $g_s^{-2},g_s^{-1},g_s^3$ vanish, $g_s^0=S_2+6c^2W$ with $W$ from the raised $p_{1,2}$ and the inverse of the raised $p_{2,2}$ on the $(2,2)\to(3,3)$ sector, $g_s^1=(1+6c)\mathcal V_3/6$, $g_s^2=\mathcal V_4/24$; the $g_s^0$ excess scales by $4$ under $\Psi\to2\Psi$. Break legs FAIL: $3c^2W$; scaling by $16$ (a quartic term).
- **C3.3** – kernel model ($\mathcal V_4$ on the ghost-2 sector replaced by a sum of two fourth powers, $K$ of rank $2$ on $\mathrm{Sym}^2$): $N\in\ker K$ nonzero; (2.5) at two $\lambda$; the $\Sigma_2$ equation inconsistent for the random $\Psi$, consistent on $\mathcal V_3(N,\Psi)=0$, and consistent at $c=0$ (control).
- **C4.4** – the content is the first leg (`restored`): $S'-6c^2W-6cS_3$ eliminates to $S_{\le4}$ exactly (Laurent coefficients), against the independently built $S_{\le4}$. The second leg (`okq`: its $g_s^0$ $\Psi$ equation is the literal (MC.5) at $g_s=0$ minus $12c^2D\Psi$) is near-tautological – it differentiates $S_2-6c^2W$ with $W$ from the same raised products and tests only the symmetry of $W$ and that (MC.5) at $g_s=0$ is $Q_B\Psi$; it is a consistency leg, not a test of (2.8). Break leg FAILs: the counterterm $-3c^2W$.
- **C4.5** – $W(\Psi)\neq0$ and $D\Psi\neq0$ at the random $\Psi$, both seeds.
- **C5** – free model ($\mathcal V_2(\text{gh }1,\text{gh }3)=0$, $\mathcal V_2$ of rank one on the ghost-2 sector): $Q^2=0$ on every basis state, $Q$ from ghost 1 vanishes, so $\ker B_Q$ on $\mathcal H_2$ is a physical state $\psi_0$; $\operatorname{rank}B_Q=1$, $\operatorname{rank}(B_Q+12c^2B_D)=2$ at $c=\tfrac16$, $W(\psi_0)\neq0$; control $c=0$.

What the checks establish: the algebraic identities (1.5)–(1.7), (2.4), (2.5), (2.8) for the quartic-truncated action $\tilde S_{\le4}+c\,g_s\mathcal V_3(\Sigma_2,\Psi)$ in a finite model whose vertices are random cyclic data, with the components taken from 103's literal path. The higher-section contributions (2.9), (2.10) are not checked (none could be within $\tilde S_{\le4}$); only the $g_s^0$ coefficient of (2.4) carries over to the full action, by the counting (2.9). Not checked: H-W for the closed-string vertices; the $L_\infty$ relations (not imposed; the identities do not use them; C5's model has $Q^2=0$ but random $\mathcal V_3$, $\mathcal V_4$); gauge invariance (step 3, not done); genus $\ge1$; $\Sigma_2$ with strands other than $(2,2)$; the Scope's case (ii).

## Steps 3–4 (stop condition)

The stop condition of the brief holds (block 2, Result): steps 3 and 4 are not carried out. The consequences already derived in block 2, one line each:

- *Quotient by $\ker p_{2,2}$.* Not available with the coupling unless $\mathcal V_3(\ker\mathcal V_4,\mathcal H_2)=0$ (the cubic analogue of PH5's second clause; vacuous under PH5's first clause); otherwise the kernel directions are Lagrange multipliers for $p_{1,2}(\Psi)\in(\ker p_{2,2})^\perp$, and (2.4) holds only on that constraint surface with $G$ the inverse on the complement (C3.3, derived).
- *IBL reading (section 7).* The solution $\Psi_2^*=\Sigma_2^*/6$ has a part of order $g_s^{-1}$, outside CFL's filtration (9.1) with fields of positive $g_s$-order (block 2, Commentary; Argued).
- *Gauge invariance (step 3).* Not examined. Indication only (Argued): under the composite law the coupling varies at $O(g_s)$ by $c\,g_s\mathcal V_3(\Sigma_2,Q_B\Lambda)$ plus terms proportional to the free equation of motion, and the first is not proportional to $\mathcal E'_\Sigma$, whose leading part is $\tfrac{g_s^2}{12}p_{2,2}(\Sigma_2)$; cancelling it through $\delta\Sigma_2$ needs a term of order $g_s^{-1}$, the same mechanism as (2.2), unless a $Q_B$-exact rearrangement through the $L_\infty$ relation $p_{1,2}Q_B=-Q_{(2)}p_{1,2}$ moves it onto $\mathcal E'_\Sigma$ or the free equation – not examined. Not for the paper.
- *Higher orders.* Not examined beyond the counting (2.9), (2.10).

## Plain statement for the paper (step 6)

Status: steps 1 and 2 derived and verified in finite models (Verified for the identities of the quartic truncation); the statements about the full action are at $O(g_s^0)$ only, and conditional on H-W (the quadratic term $W$ nonzero and finite for the closed-string vertices; motivated by its level-zero truncation, not computed).

> The Maurer–Cartan equation of the raised family contains, besides the equations of motion of the cubic action, the two variations of one more coupling, $g_s\mathcal V_3(\Psi_2,\Psi)$, in which $\Psi$ fills one slot of the cubic vertex and the two strands of the two-string component fill the other two. In the cubic action this term is $\tfrac{g_s}{6}\mathcal V_3(\Sigma_2,\Psi)$, with $\Psi_2=\Sigma_2/6$ (the normalization in which the source term $\tfrac{2g_s^2}{4!}\mathcal V_4(\Sigma_2,\Psi^2)$ is the Maurer–Cartan term $\tfrac{g_s^2}{2}\mathcal V_4(\Psi_2,\Psi^2)$). It is bilinear in the fields: a mixing of order $g_s$ between $\Psi$ and an auxiliary field whose propagator, $-12\,p_{2,2}^{-1}/g_s^2$, is of order $g_s^{-2}$. The solution for $\Sigma_2$ therefore has a part of order $g_s^{-1}$, and eliminating $\Sigma_2$ changes the action already at order $g_s^0$: it adds the nonlocal quadratic term $\tfrac16\langle p_{1,2}(\Psi),p_{2,2}^{-1}p_{1,2}(\Psi)\rangle_2$, an integral over the momenta of the two strands. Heuristically it is a bubble in which both strands of the auxiliary line join the two cubic vertices; since $p_{2,2}^{-1}$ is the inverse of a quartic vertex and not a pair of propagators, the picture is only suggestive. The same part of order $g_s^{-1}$ brings the higher terms of the cubic action down to lower orders, so beyond order $g_s^0$ the elimination cannot be read off the quartic terms alone. If the bubble term is not identically zero (its truncation to the tachyon at zero strand momentum is nonzero), no field redefinition that reduces to the identity at $g_s=0$ removes it, and the counterterm that would remove it puts the same term into the zeroth-order equation of $\Psi$, where the Maurer–Cartan equation has only $Q_B\Psi$; whether a redefinition independent of $g_s$ can absorb it is open. If the quartic vertex has a kernel on which the cubic vertex does not vanish, the coupling also forbids the quotient by that kernel: the kernel directions become Lagrange multipliers for $\mathcal V_3(N,\Psi)=0$. We do not include this coupling. The term it would supply, $g_s\,p_{1,2}(\Psi)$, is a condition that closed string field theory itself does not satisfy: either it constrains $\Psi$ (without the coupling), or it is absorbed by $\Sigma_2$ at the price of the term of order $g_s^0$ (with it).

## Self-review

1. Objective: answered – why the term is needed (M-a and M-b are its two variations, one coupling fixed at $c=\tfrac16$ by the exponential of the Maurer–Cartan action), and what it changes (a mixing that, after elimination, adds the nonlocal quadratic term $6c^2W$ at $O(g_s^0)$ in the full action, and removes the quotient unless $\mathcal V_3(\ker\mathcal V_4,\mathcal H_2)=0$). Beyond $O(g_s^0)$ the record gives only the counting (2.9), (2.10): the doubled cubic coupling of the first version was an artefact of the quartic truncation. The brief's expectation of a quartic term from two couplings joined by $p_{2,2}^{-1}$ is corrected: the term is quadratic.
2. Weakest step: the extension of the exclusion to the closed string rests on H-W ($W\not\equiv0$ and finite), motivated only by its level-zero, zero-strand-momentum truncation; the strand-momentum integral and A3 on the continuum are open. Next: case (i) of the Scope ($g_s$-independent linear redefinitions), open for the closed string, which the gauge-invariance test of H-W would settle. Second: the class (a) keeps the operator $p_{2,2}$; the Scope's case (ii) (another operator with an isotropic image) is not explored.
3. Not checked: gauge invariance (stop condition), H-W with closed-string data, the $L_\infty$ relations in the model data (the identities do not use them), $g_s$-independent nonlinear redefinitions beyond the rank statement C5.
4. What a stronger physicist would note: the $g_s^{-1}$ part of $\Sigma_2^*$ reorders the whole expansion (2.9), so a truncated-action computation is reliable only at the lowest order – the error of the first version. Further, the obstruction is an order-counting statement, not a detail of the vertices – a source of order $g_s$ for a field with propagator of order $g_s^{-2}$ always feeds back at $g_s^0$. The same counting says the Maurer–Cartan weight $g_s^{k+\ell-2}$ with $g_s=\tau$ (103, A6) places $p_{1,2}$ one order too low for a tree-level auxiliary field; if the identification of $g_s$ with $\tau$ were $g_s^2\propto\tau$, or $\Sigma_2$ were read as a one-loop object (103: genus label $-1$), the bubble (a heuristic picture, block 2) would sit at loop order. That is the question to hand to Task 20 and Task 25.

## Proposed ledger entries

Ledger section: new: IBL Maurer–Cartan reading of the cubic theory

### R? — excl. within Σ-sector rescalings, Σ redefinitions, Ψ redefinitions trivial at g_s=0 and Ψ-only counterterms keeping Q_BΨ at g_s^0: the Maurer–Cartan coupling $\tfrac{g_s}6\mathcal V_3(\Sigma_2,\Psi)$ adds a nonlocal quadratic term at $O(g_s^0)$ after elimination [Conditional(PH? = H-W) – Verified]

- **Source**: `agent/derivations/109-mc-cubic-coupling.md#C4` (nodes C1–C5, blocks 1, 2)
- **Scope**: genus zero, the cubic action with $\Sigma_2$ on $(2,2)$ strands; full-action statements at $O(g_s^0)$ only (complete there by the counting $g_s^{n-2-k}$), the identities at $O(g_s)$, $O(g_s^2)$ for the quartic truncation only; $p_{2,2}$ invertible (A3) except in C3.3; compensations (a)–(d) of block 2, (d) meaning counterterms that keep M-a, M-b and the $g_s^0$ part $Q_B\Psi$ of (MC.5); $g_s$-independent linear redefinitions of $\Psi$ (and mixed redefinitions $\Psi\to\Psi+g_sf(\Sigma_2)$, which reduce to them) not covered, open for the closed string; the components and their conventions as in record 103 (H-par only for the Maurer–Cartan reading)
- **Verification**:
  - 2026-10-18 – exact check – `codes/verify-mc-cubic-coupling.py` C1, C2, C3, C3.3, C4.4, C4.5, C5 (break legs on C1, C2, C3, C4.4; controls on C3.3, C5); 14/14 PASS at seeds 20261018 and 20261019; record 103's engine (model $\dim8$, literal CFL components, raised operations, random vertices without the $L_\infty$ relations), exact Fractions, quartic-truncated action

The two Maurer–Cartan items M-a ($g_s\ell_2(\Psi_2)$ in $E_1$) and M-b ($g_sp_{1,2}(\Psi)$ in $E_2$) are the variations of one term, which in the cubic action is $c\,g_s\mathcal V_3(\Sigma_2,\Psi)$ with $c=\tfrac16$ and $\Psi_2=\Sigma_2/6$, fixed by the ratio $1:\tfrac12$ of $\mathcal V_3(\Psi_2,\Psi)$ and $\mathcal V_4(\Psi_2,\Psi^2)$ in $e^{\Psi+\Psi_2}$. With it, M-c, M-d, M-e ($\ell_3(\Psi^3)$ part), M-r0, M-r and M-s remain and M-q disappears because the equations lose the kernel invariance. The term is bilinear in the fields. Eliminating $\Sigma_2$ gives $\Sigma_2^*=\Psi^2+\tfrac{12c}{g_s}p_{2,2}^{-1}p_{1,2}(\Psi)$; since this is of order $g_s^{-1}$, a term $g_s^{n-2}\mathcal V_n(\Sigma_2^k,\Psi^{n-2k})$ contributes at order $g_s^{n-2-k}$, and the eliminated action is $S'[\Psi]=S_2+\tfrac16W+O(g_s)$ with $W=\langle p_{1,2}\Psi,p_{2,2}^{-1}p_{1,2}\Psi\rangle_2$, a nonlocal quadratic term (a strand-momentum integral). In the quartic truncation alone the $O(g_s)$, $O(g_s^2)$ parts are $2S_3+S_4$; in the full action the quintic term adds $\tfrac1{30}g_s\mathcal V_5((p_{2,2}^{-1}p_{1,2}\Psi)^2,\Psi)$ at $O(g_s)$, and higher sections more. Under H-W, no rescaling of the $\Sigma_2$-sector coefficients, no redefinition of $\Sigma_2$, no redefinition $\Psi\to\Psi+O(g_s)$, and no counterterm in $\Psi$ alone that keeps $Q_B\Psi$ as the $g_s^0$ part of (MC.5) restores closed SFT at $O(g_s^0)$ while keeping M-a and M-b. Without invertibility, the kernel directions of $p_{2,2}$ become Lagrange multipliers for $\mathcal V_3(N,\Psi)=0$, and the quotient is not available unless $\mathcal V_3(\ker\mathcal V_4,\mathcal H_2)=0$ (cubic analogue of PH5's second clause).

Ledger section: new: IBL Maurer–Cartan reading of the cubic theory

### PH? — H-W: the bubble form $\langle p_{1,2}\Psi,p_{2,2}^{-1}p_{1,2}\Psi\rangle_2$ is finite and not identically zero for the closed-string vertices [open]

- **Source**: `agent/derivations/109-mc-cubic-coupling.md`, node H-W
- **Verification**:
  - 2026-10-18 – exact check (finite models with random vertices, no $L_\infty$ relations; not evidence on the closed-string vertices) – `codes/verify-mc-cubic-coupling.py` C4.5, PASS at seeds 20261018 and 20261019

Motivation: the level-zero, zero-strand-momentum truncation of $W$ (the $1\times1$ block of $p_{2,2}$ on $T\otimes T$) is $\mathcal V_3(T^3)^2/\mathcal V_4(T^4)\,t^2\neq0$; no structural reason for isotropy of $\operatorname{im}p_{1,2}$ under $p_{2,2}^{-1}$ is known. Open inside it: $W(k)$ is an integral over the strand momenta, whose finiteness, and the invertibility of $p_{2,2}$ on the continuum, are not established. Discharged or falsified by: a level truncation of $W(k)$ that keeps the strand momenta (starting from R53's tachyon-pair block), at more than one level; or, sharper, whether $W(Q_B\Lambda,\Psi)=0$ in a finite model with the $L_\infty$ relations imposed.

## Revisions

2026-10-18, fix pass after `agent/reports/critic-gu-19c-20261018T110304.md`:

- #1 [critical]: new node C3.4 and block 2 *Order counting* ((2.9), (2.10)): $g_s^{n-2-k}$ rule, $O(g_s)$ quintic term $\tfrac1{30}g_s\mathcal V_5((Gp_{1,2}\Psi)^2,\Psi)$ named with one Argued line on what it does; C3, C3.2, C4 (now "at $O(g_s^0)$"), block 2 Result, Scope *Class* and (iii), frontmatter, Self-review 1, paper paragraph and R-entry restricted: $2S_3+S_4$ is a property of the quartic truncation; "second copy of the cubic vertex" removed. Statements changed (C3, C3.2, C4); justifications of C4.1, C4.3, C4.4 now cite C3.4.
- #2 [major]: H-W restated (statement now includes finiteness): motivation (i) is the level-zero, zero-strand-momentum truncation, not $W$; (ii) isotropy stated as absence of a known obstruction; strand-momentum integral, its finiteness and A3 on the continuum as open points; C4.5 relabelled as no evidence; falsifier replaced (level truncation of $W(k)$ with strand momenta; finite-model gauge test $W(Q_B\Lambda,\Psi)=0$ with the $L_\infty$ relations). Not run (time box).
- #3 [major]: paper paragraph rewritten with H-W, the kernel condition, $O(g_s^0)$ only, case (i) open, propagator sign, heuristic bubble, and "We do not include this coupling" instead of a consequence.
- #4 [major]: C4 and C4.4 carry the explicit criterion ($g_s^0$ part $Q_B\Psi$, by the filtration, and why the $O(g_s^2)$ residuals M-e do not disqualify); Scope (i) made the decisive open case, with mixed redefinitions $\Psi\to\Psi+g_sf(\Sigma_2)$ reduced to it (Argued) and the gauge test as the way to close it. Statement of C4 changed.
- #5 [minor]: applied – PH5 link and constraint-surface statement in block 2 Commentary (2.5) and Steps 3–4; C3.3 statement unchanged.
- #6 [minor]: applied – propagator $-\tfrac{12}{g_s^2}G$ in A3, Commentary (2.2), paper paragraph.
- #7 [minor]: applied – bubble marked heuristic in Commentary (2.4), Self-review 4, paper paragraph.
- #8 [minor]: applied – C4.4's `okq` leg relabelled near-tautological in Block V (record only; the script is unchanged, no status changed, so not re-run); truncation caveat added to Block V.
- #9 [note]: no action (confirmation of C1, C2).
- Dependents: C3 (statement changed) – C4 uses only its $g_s^0$ part, holds; C3.2 (statement changed) – no dependent left (C4.3 now cites C3.4); H-W (statement and justification changed) – C4.1, C4.3, C4.4 hold under the restated H-W; C4 (statement changed) – no parent; C5 unchanged; C1, C2, C3.1, C3.3, C4.2 unchanged.
- #10 [minor]: applied – clause on the $Q_B$-exact rearrangement through $p_{1,2}Q_B=-Q_{(2)}p_{1,2}$ in Steps 3–4; the indication is marked not for the paper.

## Status

Fix pass complete 2026-10-18 (critic gu-19c: all ten findings applied or answered, *Revisions*); statuses unchanged, script not re-run (unchanged). Next: orchestrator (re-review of C3.4, C4, H-W, paper paragraph).
