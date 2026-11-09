---
description: Gauge unfixing of Sigma_2, candidate C1 in a strand model (3a) – for every field-independent c_0^-/L_0^- word D, im D misses H_0^2 (Lambda_2 never acts on the present components); ker(b_0^(1)+b_0^(2)) is always larger than H_0^2 and the per-strand slice is never a gauge slice; projector form on ker(b_0^(1)+b_0^(2)), for D = c_0^- f(L_0^-) symmetrized, exactly in the sectors with f(m1)+f(m2) != 0 (the c_0^- b_0^- words: sector types numerical, table rows DN, Dgen, Dgen0); residual gauge directions (type b) at f(m1) = -f(m2) never reach H_0^2; both yes/no verdict rules fire on D = 0 and are not verdicts
---

# 108 – Gauge unfixing of $\Sigma_2$: candidate C1 in a finite strand model, the constraint table

Plan: `agent/task-plans/gauge-unfixing-2026-10-13.md`, Task 3, sub-task 3a.
Brief: `agent/briefs/active-computator-gu-3a-c1-strand-model-20261018T095900.md`.
Script: `codes/verify-gauge-unfixing-c1.py`.
Inputs: record 102 after its fix pass (L1, model M, the building-block table, routes E1a, E1b, E2, E3); reviews of Erbin–Médevielle and Okawa–Sakaguchi on level matching (question (7)); `knowledge/conventions.md` C1, C6; `paper/sections/A-conventions.tex`, `eq:conv:pairing-n`, `eq:conv:pairing-symmetry`.

## Task and objective

Literal task (3a).
Build the strand model $\mathcal H^{\rm ext} = \bigoplus_m \mathcal H_m \otimes (\mathbb C \oplus \mathbb C \, c_0^-)$ with $L_0^- = m$ and $\{b_0^-, c_0^-\} = 1$, the present $\mathcal H_0 = \{m = 0, \ b_0^- = 0\}$ being model M of record 102; the full pairing (ghost number six per strand, Koszul signs explicit); the source term extended by zero.
For each field-independent $D$ of record 102's table built from $c_0^-$ and $L_0^-$ (row D1, symmetrized over strands), with $B_2 = b_0^-$ on a strand, compute the columns of criterion (i): $\dim \{q : q \circ D = 0, \ q|_{\mathcal H_0^{\wedge 2}} = p\}$, $\dim \mathcal P_D$ (the decoupled family, decision (A) of plan round 2), the non-transverse sectors, the kernel excess at a generic point, and the verdict.
Check the prediction from L1: $E = S \oplus \operatorname{im} D$ wherever $f \neq 0$, so that $D = c_0^-$ alone is "no".

Objective.
Decide whether relaxing level matching on the strands of $\Sigma_2$ gives, at the quadratic level and for a field-independent $D$, a $\Lambda_2$-invariant form $q$ that is not the projector construction of L1 – i.e. whether candidate C1 carries content (routes E1a, E1b of record 102) – before the worldsheet vertex is asked for (Task 7) and before the residual symmetry is computed (3b).
The falsifier of the plan: every row "no" means C1 is the projector construction at the quadratic level.

## Conventions and exclusions

- Physical ghost number and parity, $N_{\rm gh}(\Psi) = 2$, $N_{\rm gh}(\Sigma_2) = 4$, $N_{\rm gh}(\Lambda_2) = 3$, $N_{\rm gh}(c_0^-) = +1$, $N_{\rm gh}(b_0^-) = -1$ (the project conventions; record 102, *Conventions*).
- Restricted pairing $\omega_1(A, B) = \langle A \vert c_0^- \vert B \rangle$, graded symmetric with $s = +1$, $\mathrm{bpz}(c_0^\pm) = - c_0^\pm$, $\mathrm{bpz}(b_0^\pm) = b_0^\pm$: C1. Multi-string pairing with the Koszul sign $(-1)^{\sum_{i<j} \vert B_i \vert \vert A_j \vert}$: `eq:conv:pairing-n`.
- Symmetry type of two-strand states: C6 (input strands of $\Sigma_2$ and $\Lambda_2$ graded symmetric in the physical parity, with $c_0^-$ odd).
- Excluded: the lift of $Q_B$ to several strands appears nowhere in $q$, $D$, $B_2$ or the model (plan criterion (vi)); $Q_B$ does not enter sub-task 3a at all.

## Claim tree

- **A1** Exact linear algebra over $\mathbb Q$; all objects finite dimensional.
- **A2** (decision item) The strand model of section *Strand model*: $m \in \{-1, 0, 1\}$, $\mathcal H_0^- = $ M (dimensions $(1, 5, 5, 1)$ at ghost numbers $1$–$4$), $\mathcal H_{\pm 1}^-$ of dimensions $(1, 2, 2, 1)$; each strand space $V_m = \mathcal H_m^- \oplus c_0^- \mathcal H_m^-$; $\dim E = 132$, $\dim L = 36$, $\dim S_0 = 20$; six sectors $\{m_1, m_2\}$.
- **A3** The full pairing (M.2), fixed by $\langle\!\langle e_i, c_0^- e_j \rangle\!\rangle = \omega^{(m)}_{ij}$ and graded symmetry; two strands by (M.4).
- **A4** $E$ and $L$ graded symmetric in the physical parity, $c_0^-$ odd (C6, input strands).
- **A5** $q$ a symmetric bilinear form on $E$ with $q|_{S_0} = p$, $p$ the form of M (record 102, A4; M is an on-shell model, and its unseen part $U$ holds every field-dependent gauge parameter – irrelevant here, $D$ being field independent); no $L_0^-$ selection rule on $q$ (stand-in for the twist-dependent vertex; total-$L_0^-$ conservation would only shrink $\{q\}$ and leaves C2.1, C2.3, C2.4, C4 unchanged, these being sector-local). Source term extended by zero.
- **A6** $B_2 = b_0^{-(1)} + b_0^{-(2)}$, slice $S = \ker B_2$; variant $S_{\rm per}$ ($c$-count 0, the slice equal to $\mathcal H_0^{\wedge 2}$ in the sector $\{0,0\}$).
- **A7** (decision item) The $D$'s: every field-independent $D$ of record 102's row D1, $D = \sum_{i \neq j} c_0^{-(i)} \big[ \alpha(L_0^{-(i)}, L_0^{-(j)}) + \gamma(L_0^{-(i)}, L_0^{-(j)}) N^{(j)} \big]$ with $N = c_0^- b_0^-$ (the four shift-$+1$ words $c \otimes 1$, $1 \otimes c$, $c \otimes cb$, $cb \otimes c$ with arbitrary functions of the two $L_0^-$ on the model's range); nine rows, section *The D's tested*. Not tested: row D2 ($p_{2,2}$ on non-level-matched inputs, the vertex itself).
- **A8** Two yes/no rules are evaluated: criterion (i) with decision (A) of plan round 2 (the *literal* rule), and a *refined* rule relative to the slice $\ker B_2$, added after the literal table was seen to fire on $D = 0$ (C3). Neither discriminates – both give "yes" on the control $D = 0$ – so the refined rule is read only as the L1 transversality test on $\ker B_2$, and the result of 3a is the structural nodes C2.1, C2.3, C2.4, C4, not a yes/no column; section *Verdict rules*.
- **C1** The strand model is consistent and reproduces M and the ghost count of the plan. [by C1.1–C1.4]
  - **C1.1** (M.2) is graded symmetric, non-degenerate, supported at ghost sum 6 and equal $m$. [by A2, A3] [by check: C1.1-pairing]
  - **C1.2** The adjointness rules (M.3), $\mathrm{bpz}(c_0^-) = - c_0^-$, $\mathrm{bpz}(b_0^-) = b_0^-$, $L_0^-$ BPZ-even, follow from (M.2) with $\omega$ symmetric on its support. [eq. (C1.1)] [check: C1.2-adjoint]
  - **C1.3** $\omega_1(A, B) = \langle\!\langle A, c_0^- B \rangle\!\rangle$ on $\mathcal H_0$ is M's pairing, symmetric ($s = +1$, C1). [by A3] [check: C1.3-omega1]
  - **C1.4** (M.5): $\langle \Sigma, X \rangle_2 = - \langle\!\langle \Sigma, c_0^{-(1)} c_0^{-(2)} X \rangle\!\rangle_2$ for even $\Sigma$, hence $\hat q = - c_0^{-(1)} c_0^{-(2)} p_{2,2}$ on $\mathcal H_0^{\wedge 2}$ and $N_{\rm gh}(\hat q) = 4$. [eq. (C1.2)] [check: C1.4-two-strand]
- **C2** Structure of the solution set, for every $D$ of A7. [by C2.1–C2.4]
  - **C2.1** Every word of A7 raises the $c$-count by exactly one and preserves the sectors; hence $\operatorname{im} D \subseteq C$, $S_0 \cap \operatorname{im} D = 0$, the $\Lambda_2$ orbit never has a component along $\mathcal H_0^{\wedge 2}$, and the source term extended by zero is invariant. [eq. (C2.1)] [check: C2.1-raise]
  - **C2.2** $\{q\}$ is an affine space of dimension $\binom{n+1}{2} - \binom{s+1}{2}$, $n = \dim E - \operatorname{rank} D$, $s = 20$; $\mathcal P_D$ has dimension $\binom{c'+1}{2}$, $c' = \dim C - \operatorname{rank} D$; the difference is $s \, c'$, the coupling block. At a generic point the kernel excess is $- \dim \ker p$ (the coupling lifts $\ker p$), and $0$ in $\mathcal P_D$. [by A1, A5, C2.1; eqs. (C2.2)–(C2.4)] [check: C2.2-brute, C2.2-family]
  - **C2.3** Counting lemma: in every sector, $\dim E^{(1)}_\sigma = 2 \dim L^{(0)}_\sigma$, so $\operatorname{rank} (D|_{L^{(0)}}) \le \tfrac12 \dim E^{(1)}_\sigma$ and $S_{\rm per} + \operatorname{im} D \neq E_\sigma$ in every sector, for every $D$ of A7: the per-strand condition $b_0^- \Sigma_2 = 0$ is never a pure gauge fixing. [by A4, C2.1; eq. (C2.5)] [check: C2.3-count]
  - **C2.4** $S = \ker B_2 = E^{(0)} \oplus (S \cap E^{(1)})$ with $\dim (S \cap E^{(1)}_\sigma) = \dim L^{(0)}_\sigma$, independently of $D$: in the sector $\{0, 0\}$, $\dim S = 25 = 20 + 5$, so the slice is larger than $\mathcal H_0^{\wedge 2}$ in every case, and it contains the whole $c$-count-0 part of the sectors $m \neq 0$. [by A6; eq. (C2.6)] [check: C3-table (per-sector data)]
- **C3** The table of criterion (i): in every row, including the control $D = 0$, $\dim \{q\} - \dim \mathcal P_D = s \, c' > 0$ and the kernel excess is $- \dim \ker p \neq 0$, so the literal verdict is "yes" in every row and does not discriminate: the coupling block exists without any gauge symmetry. The "yes" rests on that block, and under A5's source term a generic coupling block breaks criterion (iv) – eliminating $\Sigma_2$ no longer returns $\mathcal V_4(\Psi^4)$ (eq. (C3.1)) – whenever $c' > \dim\ker p$, which holds in every row ($c' \ge 79$ against 6), so the parameters the literal rule counts are generically excluded by the record's own source term. [by C2.2, A5; block: table; eq. (C3.1)] [by check: C3-table]
- **C4** The prediction from L1, corrected: for $D = c_0^- f(L_0^-)$ symmetrized, the sector $\{m_1, m_2\}$ is transverse ($E_\sigma = S_\sigma \oplus \operatorname{im} D_\sigma$) iff $f(m_1) + f(m_2) \neq 0$; where $f(m_1) = f(m_2) = 0$ it is non-transverse of type (a) only (directions $W$, E1b); where $f(m_1) = - f(m_2) \neq 0$ of type (b) (E1a, $S \cap \operatorname{im} D \neq 0$). $D = c_0^-$ alone is transverse in every sector. The plan's wording "where $f(m) \neq 0$" is right on the diagonal sectors and wrong on seven off-diagonal ones. [by C4.1, C4.2]
  - **C4.1** $\{D, B_2\} = f(L_0^{-(1)}) + f(L_0^{-(2)})$ and $D^2 = B_2^2 = 0$; where it is invertible the Hodge decomposition gives transversality. [eqs. (C4.1)–(C4.3)] [check: C4-prediction]
  - **C4.2** Where it vanishes: $D_\sigma = 0$ (type (a)), or $D$ anticommutes with $B_2$ and maps $L^{(0)}_\sigma$ into $S_\sigma$ (type (b)). [eq. (C4.4)] [check: C4-prediction]
- **C5** Conclusion, as the conjunction of C2.1, C2.3, C2.4, C4 (no yes/no column; both rules fire on the control $D = 0$, C3): for every field-independent $c_0^-$, $L_0^-$ word at quadratic order, (i) $\operatorname{im} D \cap \mathcal H_0^{\wedge 2} = 0$ in every row – $\Lambda_2$ never moves the present components and every $D$ sends the composite parameter $\Lambda \otimes \Psi$ out of $\mathcal H_0^{\wedge 2}$; (ii) the slice $\ker B_2$ is strictly larger than $\mathcal H_0^{\wedge 2}$; (iii) the per-strand slice is never a gauge slice; (iv) L1 holds on $\ker B_2$ (projector form $q = P^{\mathsf T} (q|_S) P$) exactly in the sectors where $f(m_1) + f(m_2) \neq 0$ for $D = c_0^- f(L_0^-)$ symmetrized (C4); for the $N$-words by the table – every sector for Dc and generic D1 – while the other sectors carry E1b directions (type (a), no gauge symmetry acts) or, for odd $f$, residual gauge directions of type (b) in $\{-1, 1\}$ (dimension 4, $q$ vanishes on them), a gauge content at total $L_0^- = 0$ off level matching that never reaches $\mathcal H_0^{\wedge 2}$. C1 with these $D$'s is the projector construction on $\ker B_2$ plus auxiliary directions: the substance of the plan's falsifier. [by C2, C3, C4]

Open gaps: none
Hypotheses in force: none

## Strand model

Decision item of 3a (A2, A3).

**One strand.** For $m \in \{-1, 0, 1\}$, $\mathcal H_m^-$ is a graded space with basis $e_i$ of ghost numbers $g_i$ and a restricted pairing $\omega^{(m)}$, non-zero only at ghost sum 5, symmetric on its support and non-degenerate.
$\mathcal H_0^-$ is model M of record 102 (basis $\lambda$; $\chi, \varphi_{1,2,3}, \eta$; their antifields; $\lambda^*$; dimensions $(1, 5, 5, 1)$; $\omega^{(0)}$ the pairing of M); $\mathcal H_{\pm 1}^-$ has dimensions $(1, 2, 2, 1)$ with basis $u_0$; $u_1, u_2$; $u_3, u_4$; $u_5$ and $\omega^{(\pm 1)}(u_0, u_5) = \omega^{(\pm 1)}(u_1, u_3) = \omega^{(\pm 1)}(u_2, u_4) = 1$.
The strand space is $V_m = \mathcal H_m^- \oplus c_0^- \mathcal H_m^-$, basis $e_i$ (type 0) and $\bar e_i := c_0^- e_i$ (type 1, ghost $g_i + 1$, opposite parity); $\mathcal H^{\rm ext} = \bigoplus_m V_m$, 48 states.
The zero modes act by
$$c_0^- e_i = \bar e_i, \quad c_0^- \bar e_i = 0, \quad b_0^- e_i = 0, \quad b_0^- \bar e_i = e_i, \quad L_0^- = m \ \text{on} \ V_m , \tag{M.1}$$
so $\{b_0^-, c_0^-\} = 1$, $(b_0^-)^2 = (c_0^-)^2 = 0$, $[L_0^-, b_0^-] = [L_0^-, c_0^-] = 0$, and $N := c_0^- b_0^-$ projects onto type 1.
The present single-string space is $\mathcal H_0 = \{m = 0, \ b_0^- = 0\} = \mathcal H_0^-$, i.e. M.

**Full pairing (A3).** Ghost number six per strand, equal $m$ only:
$$\langle\!\langle e_i, \bar e_j \rangle\!\rangle := \omega^{(m)}_{ij}, \qquad \langle\!\langle \bar e_j, e_i \rangle\!\rangle := (-1)^{(g_j + 1) g_i} \, \omega^{(m)}_{ij}, \qquad \langle\!\langle e_i, e_j \rangle\!\rangle = \langle\!\langle \bar e_i, \bar e_j \rangle\!\rangle = 0 , \tag{M.2}$$
and zero between different $m$ ($L_0^-$ BPZ-even).
It is graded symmetric, $\langle\!\langle B, A \rangle\!\rangle = (-1)^{\vert A \vert \vert B \vert} \langle\!\langle A, B \rangle\!\rangle$, by construction, and $\omega_1(A, B) = \langle\!\langle A, c_0^- B \rangle\!\rangle$ on $\mathcal H_0$ is M's pairing (C1's definition of $\omega_1$).
The adjointness rules are consequences, not inputs (Derivation of C1 below):
$$\langle\!\langle c_0^- A, B \rangle\!\rangle = - (-1)^{\vert A \vert} \langle\!\langle A, c_0^- B \rangle\!\rangle, \qquad \langle\!\langle b_0^- A, B \rangle\!\rangle = (-1)^{\vert A \vert} \langle\!\langle A, b_0^- B \rangle\!\rangle, \qquad \langle\!\langle L_0^- A, B \rangle\!\rangle = \langle\!\langle A, L_0^- B \rangle\!\rangle , \tag{M.3}$$
i.e. $\langle\!\langle \mathcal O A, B \rangle\!\rangle = (-1)^{\vert \mathcal O \vert \vert A \vert} \langle\!\langle A, \mathrm{bpz}(\mathcal O) B \rangle\!\rangle$ with $\mathrm{bpz}(c_0^-) = - c_0^-$, $\mathrm{bpz}(b_0^-) = b_0^-$, as in C1 (ii).

**Two strands (A4).** Ordered tensors $x \otimes y$; a strand operator acts with the Koszul sign, $(1 \otimes \mathcal O)(x \otimes y) = (-1)^{\vert \mathcal O \vert \vert x \vert} x \otimes \mathcal O y$, and $\mathcal O^{(1)} := \mathcal O \otimes 1$, $\mathcal O^{(2)} := 1 \otimes \mathcal O$.
The two-string full pairing carries the sign of `eq:conv:pairing-n`,
$$\langle\!\langle x_1 \otimes x_2, y_1 \otimes y_2 \rangle\!\rangle_2 := (-1)^{\vert y_1 \vert \vert x_2 \vert} \langle\!\langle x_1, y_1 \rangle\!\rangle \langle\!\langle x_2, y_2 \rangle\!\rangle , \tag{M.4}$$
non-zero at ghost sum 12.
With the graded swap $\tau(x \otimes y) = (-1)^{\vert x \vert \vert y \vert} y \otimes x$, $E := \{ \Sigma \in (\mathcal H^{\rm ext} \otimes \mathcal H^{\rm ext})_4 : \tau \Sigma = \Sigma \}$ and $L := \{ \Lambda_2 \in (\mathcal H^{\rm ext} \otimes \mathcal H^{\rm ext})_3 : \tau \Lambda_2 = \Lambda_2 \}$ (C6, input strands, $c_0^-$ odd).
Basis of $E$: $x \otimes y + (-1)^{\vert x \vert \vert y \vert} y \otimes x$ for $x < y$ in a fixed order of the strand basis, and $x \otimes x$ for even $x$; a two-strand state is in the *sector* $\{m_1, m_2\}$ of its strands, and has *$c$-count* $k \in \{0, 1, 2\}$ (number of type-1 strands).
$S_0 := (\mathcal H_0^{\wedge 2})_4$ is the sector $\{0, 0\}$ at $c$-count 0: M's $\mathcal H_2^{\wedge 2} \oplus \mathcal H_1 \wedge \mathcal H_3$, of dimension $15 + 5 = 20$, with $p$ the form of M ($\mathcal V_4$ on $\mathcal H_2^{\wedge 2}$, zero on $\mathcal H_1 \wedge \mathcal H_3$; record 102, *Finite model M*, HS data).
$C$ denotes the span of the other basis states of $E$ (sector $\neq \{0, 0\}$ or $c$-count $\geq 1$), so $E = S_0 \oplus C$.

**Relation to the restricted two-string pairing.** For $\Sigma \in \mathcal H_0^{\wedge 2}$ of ghost number 4 and $X \in \mathcal H_0^{\otimes 2}$ of ghost number 6,
$$\langle \Sigma, X \rangle_2 = - \langle\!\langle \Sigma, c_0^{-(1)} c_0^{-(2)} X \rangle\!\rangle_2 , \tag{M.5}$$
so $q(\Sigma, \Sigma') = \langle\!\langle \Sigma, \hat q \, \Sigma' \rangle\!\rangle_2$ with $\hat q = - c_0^{-(1)} c_0^{-(2)} p_{2,2}$ on $\mathcal H_0^{\wedge 2}$: $N_{\rm gh}(\hat q) = 4 = N_{\rm gh}(p_{2,2}) + 2$, the two $c_0^-$ the restricted pairing hides (plan, observation 5a).

**Source term.** The present coupling extended by zero: $J_\Psi(\Sigma) := p(\pi_0 \Sigma, \Psi^2)$, $\pi_0$ the projection onto $S_0$ along $C$, and $\tilde S^{(4)} = \tfrac{g^2}{4!} \big[ - q(\Sigma_2, \Sigma_2) + 2 J_\Psi(\Sigma_2) \big]$ (record 102, (L2.1), with $p \to q$ in the kinetic term). $\Psi$ stays in $\mathcal H_0$.

**The gauge structure (A6, A7).** $\delta \Sigma_2 = D \Lambda_2$, $D \colon L \to E$ field independent, $N_{\rm gh}(D) = +1$; gauge condition $B_2 \Sigma_2 = 0$ with $B_2 = b_0^{-(1)} + b_0^{-(2)} \colon E \to L$, slice $S = \ker B_2$.
For graded-symmetric $\Sigma$, $b_0^{-(2)} \Sigma = \pm \tau \, b_0^{-(1)} \Sigma$, so $B_2 \Sigma$ is the graded symmetrization of $b_0^{-(1)} \Sigma$: $S \supseteq S_{\rm per} := \{ c\text{-count } 0 \}$, with equality only where the symmetrization is injective (computed per sector in C2).

## Block C1 (the strand model)

\subsection*{Setup}

A2, A3, A4. Strand basis states $e_i$, $\bar e_i = c_0^- e_i$ of section *Strand model*; $\omega = \omega^{(m)}$ symmetric on its support $g_i + g_j = 5$.

\subsection*{Derivation}

The only non-trivial case of the $c_0^-$ rule is $A = e_i$, $B = e_j$:
$$\langle\!\langle c_0^- e_i, e_j \rangle\!\rangle = \langle\!\langle \bar e_i, e_j \rangle\!\rangle = (-1)^{(g_i + 1) g_j} \omega_{ij} = (-1)^{g_j} \omega_{ij} = - (-1)^{g_i} \langle\!\langle e_i, c_0^- e_j \rangle\!\rangle , \tag{C1.1}$$
and of the $b_0^-$ rule $A = \bar e_i$, $B = \bar e_j$: $\langle\!\langle b_0^- \bar e_i, \bar e_j \rangle\!\rangle = \omega_{ij}$, $(-1)^{\vert \bar e_i \vert} \langle\!\langle \bar e_i, b_0^- \bar e_j \rangle\!\rangle = (-1)^{(g_i + 1)(1 + g_j)} \omega_{ij} = \omega_{ij}$.
For (M.5): $c_0^{-(1)} c_0^{-(2)} (y_1 \otimes y_2) = (-1)^{\vert y_1 \vert} \bar y_1 \otimes \bar y_2$, so by (M.4)
$$\langle\!\langle x_1 \otimes x_2, c_0^{-(1)} c_0^{-(2)} (y_1 \otimes y_2) \rangle\!\rangle_2 = (-1)^{\vert y_1 \vert + (\vert y_1 \vert + 1) \vert x_2 \vert} \omega(x_1, y_1) \, \omega(x_2, y_2) = (-1)^{\vert y_1 \vert + \vert x_2 \vert} \langle x_1 \otimes x_2, y_1 \otimes y_2 \rangle_2 , \tag{C1.2}$$
and on the support $\vert y_1 \vert = 1 + \vert x_1 \vert$ the sign is $- (-1)^{\vert x_1 \vert + \vert x_2 \vert} = -1$ for an even $\Sigma$.

\subsection*{Commentary}

- (C1.1): the two cases $g_j$ even and $g_j$ odd (then $g_i$ even) give $(-1)^{(g_i+1) g_j} = (-1)^{g_j}$; with $g_i + g_j$ odd this is $-(-1)^{g_i}$. All other type combinations vanish on both sides. The rule is $\langle\!\langle \mathcal O A, B \rangle\!\rangle = (-1)^{\vert \mathcal O \vert \vert A \vert} \langle\!\langle A, \mathrm{bpz}(\mathcal O) B \rangle\!\rangle$ with C1's $\mathrm{bpz}(c_0^-) = -c_0^-$: the model realizes C1 (ii) and $s = +1$ together; a pairing with $\omega$ antisymmetric on its support would give $\mathrm{bpz}(c_0^-) = + c_0^-$ (break leg of C1.2).
- (C1.2): the identity is the finite-model form of observation 5a: on level-matched strands the pairing hides one $c_0^-$ per strand, and the form $q$ on $E$ is $\langle\!\langle \Sigma, \hat q \Sigma' \rangle\!\rangle_2$ with an operator $\hat q$ of ghost number $12 - 4 - 4 = 4$, equal to $- c_0^{-(1)} c_0^{-(2)} p_{2,2}$ on $\mathcal H_0^{\wedge 2}$.

\subsection*{Result}

The strand model is a graded space with zero modes obeying $\{b_0^-, c_0^-\} = 1$, a full pairing realizing C1's BPZ rules, and the present content $\mathcal H_0 = $ M embedded as $\{m = 0, b_0^- = 0\}$ with its own pairing; $N_{\rm gh}(\hat q) = N_{\rm gh}(p_{2,2}) + 2$.

\subsection*{Verification}

C1.1-pairing, C1.2-adjoint, C1.3-omega1, C1.4-two-strand (section *Verification*).

## The D's tested

A7. Every $D$ is $\tau$-equivariant (check C2.1-raise) and has ghost number $+1$.

| row | $D$ | $\alpha(m_i, m_j)$ | $\gamma(m_i, m_j)$ |
| --- | --- | --- | --- |
| D0 | control, $D = 0$ | 0 | 0 |
| Dc | $c_0^-$ ($f = 1$) | 1 | 0 |
| DcL | $c_0^- L_0^-$ ($f(m) = m$) | $m_i$ | 0 |
| Dcd | $c_0^- \delta(L_0^-)$ | $\delta_{m_i, 0}$ | 0 |
| Dc1d | $c_0^- (1 - \delta(L_0^-))$ | $1 - \delta_{m_i, 0}$ | 0 |
| DcLo | $c_0^-$ on a strand times $L_0^-$ of the other | $m_j$ | 0 |
| DN | $c_0^- \otimes c_0^- b_0^-$, symmetrized | 0 | 1 |
| Dgen | generic D1 | random in $[1, 9] / [1, 4]$ | random |
| Dgen0 | generic D1 vanishing on $\{0, 0\}$ | random, $\alpha(0, 0) = 0$ | random, $\gamma(0, 0) = 0$ |

Rows Dc, DcL, Dcd, Dc1d are of the form $D = c_0^- f(L_0^-)$ symmetrized, the form of the plan's prediction.

## Verdict rules

*Literal (criterion (i), decision (A) of plan round 2).* $\mathcal P_D$ is the set of solutions whose block between $S_0 = \mathcal H_0^{\wedge 2}$ and its complement $C$ vanishes. Verdict "yes" iff $\dim \{q\} > \dim \mathcal P_D$ or the kernel excess $\dim \ker q - \operatorname{rank} D - \dim \ker p$ is non-zero, at a random point of the family (seed stated), $\dim \ker p$ counted on $S_0$ ($6$ in the generic variant of M, $10$ in the degenerate one) and $0$ elsewhere. The kernel excess is computed globally, since a generic $q$ couples the sectors.

*Refined (added after the literal table; the reason is C3).* Relative to the slice $S = \ker B_2$: "yes" iff $q$ has free parameters not determined by its restriction to the slice, $\dim \{q\} - \dim \{q|_S\} = \binom{n+1}{2} - \binom{\bar s + 1}{2} > 0$ with $\bar s = \dim S - \dim (S \cap \operatorname{im} D)$ (this is non-zero iff $S + \operatorname{im} D \neq E$, type (a)), or $S \cap \operatorname{im} D \neq 0$ (type (b), the gauge-fixed form forced to degenerate). A "no" is L1 on the extended slice: $q = P^{\mathsf T} (q|_S) P$. The rule is post hoc: it was added once the literal rule had been seen to fire on $D = 0$, and built from L1 and C1.4 of record 102; it compares $q$ with the gauge-fixed form on the slice the gauge condition actually selects, which the literal rule, comparing with $\mathcal H_0^{\wedge 2}$, cannot do when the slice is larger than $\mathcal H_0^{\wedge 2}$ (C2.4). (It coincides with the plan's own pre-round-2 definition of $\mathcal P_D$, "$q(x, y) = q(Px, Py)$ on the sectors where $E = S \oplus \operatorname{im} D$".)

*Neither rule is a verdict.* Both fire on the control $D = 0$ (literal: the coupling block; refined: excess 3828, all six sectors of type (a)), and the refined rule also says "yes" for DN (rank 6): its "yes" measures how small $\operatorname{im} D$ is, not content tied to the gauge symmetry, and its only "no" rows are the maximal-rank ones. The refined column is therefore read only as the L1 transversality test on $\ker B_2$ (a "no" row is one where L1 holds sector by sector). What 3a establishes, and what the go/no-go memo should carry, is the conjunction C2.1 + C2.3 + C2.4 + C4: per row, the transversality type of each sector and $\dim (\operatorname{im} D \cap \mathcal H_0^{\wedge 2}) = 0$, with D0 as the control.

## Block C2 (structure of the solution set)

\subsection*{Setup}

A1, A4–A7. $E^{(k)}$, $L^{(k)}$: the $c$-count-$k$ parts; $E_\sigma$, $L_\sigma$: the sector-$\sigma$ parts. $n = \dim E - \operatorname{rank} D$, $s = \dim S_0 = 20$, $c' = \dim C - \operatorname{rank} D$.

\subsection*{Derivation}

Each word of A7 is $c_0^{-(i)}$ times an even operator that preserves strand types and $L_0^-$ eigenvalues ($\alpha$, $\gamma N^{(j)}$); $c_0^-$ maps type 0 to type 1 and kills type 1, so
$$D \, L^{(k)}_\sigma \subseteq E^{(k+1)}_\sigma , \qquad \operatorname{im} D \subseteq C, \qquad S_0 \cap \operatorname{im} D = 0, \qquad \pi_0 \, D = 0 . \tag{C2.1}$$
A symmetric $q$ with $q(\operatorname{im} D, \cdot) = 0$ is the same as a symmetric form $\bar q$ on $\bar E = E / \operatorname{im} D$; $S_0$ injects into $\bar E$, and restriction of symmetric forms to a subspace is onto, so
$$\dim \{q : q \circ D = 0, \ q|_{S_0} = p\} = \binom{n+1}{2} - \binom{s+1}{2} . \tag{C2.2}$$
With the decoupling $q(S_0, C) = 0$ and $\operatorname{im} D \subseteq C$, $q = p \oplus r$ with $r$ a symmetric form on $C / \operatorname{im} D$:
$$\dim \mathcal P_D = \binom{c'+1}{2}, \qquad \dim \{q\} - \dim \mathcal P_D = \binom{s + c' + 1}{2} - \binom{s+1}{2} - \binom{c'+1}{2} = s \, c' . \tag{C2.3}$$
At a point of the family, $\bar q = \begin{pmatrix} p & b \\ b^{\mathsf T} & r \end{pmatrix}$ on $\bar S_0 \oplus (C / \operatorname{im} D)$; for $b$, $r$ generic and $c' \ge \dim \ker p$ it is non-degenerate, and with $b = 0$ its kernel is $\ker p$:
$$\text{kernel excess} = - \dim \ker p \ \ (\text{generic}), \qquad 0 \ \ (\mathcal P_D) . \tag{C2.4}$$
Counting lemma. A graded-symmetric state of $E^{(1)}_\sigma$ is fixed by its component $\bar x \otimes y$ with the $c_0^-$ on the first strand, $g_x + g_y = 3$; a state of $L^{(0)}_\sigma$ by an unordered pair $\{x, y\}$, $g_x + g_y = 3$ (never $g_x = g_y$). Hence
$$\dim E^{(1)}_\sigma = 2 \dim L^{(0)}_\sigma , \qquad \operatorname{im} D \cap E^{(1)}_\sigma = D(L^{(0)}_\sigma) \ \text{of dimension} \le \tfrac12 \dim E^{(1)}_\sigma . \tag{C2.5}$$
The slice. $\{ \tfrac12 c_0^{-(1)} + \tfrac12 c_0^{-(2)}, B_2 \} = 1$ makes the $B_2$ complex acyclic; $B_2 \colon E^{(1)}_\sigma \to L^{(0)}_\sigma$ is onto and $B_2$ is injective on $E^{(2)}$ (there is no $c$-count 3), so
$$S_\sigma = E^{(0)}_\sigma \oplus (S \cap E^{(1)}_\sigma), \qquad \dim (S \cap E^{(1)}_\sigma) = \dim L^{(0)}_\sigma , \tag{C2.6}$$
independently of $D$; in the sector $\{0, 0\}$, $\dim S = 20 + 5$.

\subsection*{Commentary}

- (C2.1) is the whole reason the literal rule does not discriminate: a shift-$+1$ word never reaches $c$-count 0, so $\Lambda_2$ never moves a component of $\Sigma_2$ along $\mathcal H_0^{\wedge 2}$, and every direction of $C$ outside $\operatorname{im} D$ is free to couple to $S_0$. In particular the composite parameter $\Lambda \otimes \Psi \in L^{(0)}_{\{0,0\}}$ is mapped to $c_0^- \Lambda \otimes \Psi \pm \Lambda \otimes c_0^- \Psi$, outside $\mathcal H_0^{\wedge 2}$: no $D$ of A7 can realize criterion 3c on the present content. The source term extended by zero is invariant for the same reason ($J(D \Lambda_2) = p(\pi_0 D \Lambda_2, \Psi^2) = 0$).
- (C2.2), (C2.3): verified by a direct solve of the linear system for $q$ in a smaller strand model (check C2.2-brute), the formula family being exact (check C2.2-family).
- (C2.5): the factor 2 is the choice of the strand carrying $c_0^-$. Since $D$ raises the $c$-count by exactly one, only $L^{(0)}$ feeds $E^{(1)}$: at least half of the $c$-count-1 directions of every sector are neither gauge directions nor in $(\ker b_0^-)^{\wedge 2}$, whatever $\alpha$ and $\gamma$ are. This is the statement that the per-strand condition $b_0^- \Sigma_2 = 0$, which is the one that returns $\mathcal H_0^{\wedge 2}$ in the sector $\{0,0\}$, is partly a constraint imposed beside the action, as in Erbin–Médevielle (answer (5) of the review: the constrained theory "cannot be reached by gauge fixing").
- (C2.6): the gauge condition that does fix the gauge, $B_2 \Sigma_2 = 0$ with $B_2$ mapping into the parameter space $L$, keeps the five $c$-count-1 states of $\ker B_2$ in the sector $\{0,0\}$ (combinations of $\bar\lambda \otimes \varphi$-type and $\lambda \otimes \bar\varphi$-type states) and every $b_0^-$-annihilated state of the sectors $m \neq 0$. The gauge-fixed theory always has more fields than the present one.

\subsection*{Result}

$$\boxed{\; \operatorname{im} D \subseteq C, \quad \dim \{q\} - \dim \mathcal P_D = s \, c', \quad \operatorname{rank} D|_{L^{(0)}_\sigma} \le \tfrac12 \dim E^{(1)}_\sigma, \quad \ker B_2 \cap E_{\{0,0\}} = \mathcal H_0^{\wedge 2} \oplus \mathbb Q^5 \;}$$

\subsection*{Verification}

C2.1-raise, C2.3-count, C2.2-brute, C2.2-family; the per-sector dimensions printed by C3-table.

## Table (criterion (i))

Strand model A2, generic variant of M ($\dim \ker p = 6$ on $S_0$); identical at seeds 20261018 and 20261019 (the random rows Dgen, Dgen0 and the random family points included). $\dim E = 132$, $\dim C = 112$, $s = 20$. "NT" lists the non-transverse sectors relative to $S = \ker B_2$ with (type, $\dim S \cap \operatorname{im} D$, $\dim W$); relative to $S_{\rm per}$ all six sectors are non-transverse in every row (C2.3). Kernel excess: generic point / point of $\mathcal P_D$; the degenerate variant ($\dim \ker p = 10$) gives $-10$ / $0$ in every row.

| row | rank $D$ | $\dim \{q\}$ | $\dim \mathcal P_D$ | NT sectors w.r.t. $\ker B_2$ | kernel excess | literal | refined excess | E1a dim | refined |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D0 | 0 | 8568 | 6328 | all six, (a): $\{-1,-1\}$ 3, $\{-1,0\}$ 8, $\{-1,1\}$ 5, $\{0,0\}$ 6, $\{0,1\}$ 8, $\{1,1\}$ 3 | $-6$ / $0$ | yes | 3828 | 0 | yes |
| Dc | 33 | 4740 | 3160 | none | $-6$ / $0$ | yes | 0 | 0 | **no** |
| DcL | 27 | 5355 | 3655 | $\{-1,1\}$ (b) 4, 4; $\{0,0\}$ (a) 6 | $-6$ / $0$ | yes | 1005 | 4 | yes |
| Dcd | 22 | 5895 | 4095 | (a): $\{-1,-1\}$ 3, $\{-1,1\}$ 5, $\{1,1\}$ 3 | $-6$ / $0$ | yes | 1155 | 0 | yes |
| Dc1d | 27 | 5355 | 3655 | $\{0,0\}$ (a) 6 | $-6$ / $0$ | yes | 615 | 0 | yes |
| DcLo | 27 | 5355 | 3655 | $\{-1,1\}$ (b) 4, 4; $\{0,0\}$ (a) 6 | $-6$ / $0$ | yes | 1005 | 4 | yes |
| DN | 6 | 7791 | 5671 | all six, (a): 2, 7, 4, 5, 7, 2 | $-6$ / $0$ | yes | 3051 | 0 | yes |
| Dgen | 33 | 4740 | 3160 | none | $-6$ / $0$ | yes | 0 | 0 | **no** |
| Dgen0 | 27 | 5355 | 3655 | $\{0,0\}$ (a) 6 | $-6$ / $0$ | yes | 615 | 0 | yes |

Column checks: $\dim \{q\} - \dim \mathcal P_D = s \, c'$ in every row (2240, 1580, 1700, 1800, 1700, 1700, 2120, 1580, 1700); $\dim (S \cap \operatorname{im} D) + \dim W$ per sector as printed by the script.

Per-sector data of Dc (sector: $\dim E_\sigma$, rank $D_\sigma$, $\dim S_\sigma$, $\dim S \cap E^{(1)}_\sigma$, $\dim E^{(1)}_\sigma$, $\dim L^{(0)}_\sigma$): $\{-1,-1\}$: 10, 3, 7, 2, 4, 2; $\{-1,0\}$: 32, 8, 24, 7, 14, 7; $\{-1,1\}$: 17, 5, 12, 4, 8, 4; $\{0,0\}$: 31, 6, 25, 5, 10, 5; $\{0,1\}$: 32, 8, 24, 7, 14, 7; $\{1,1\}$: 10, 3, 7, 2, 4, 2. In every sector $\dim E_\sigma = \dim S_\sigma + \operatorname{rank} D_\sigma$.

Reading. The yes/no columns are kept for the record; they are not verdicts (*Verdict rules*, *Neither rule is a verdict*).
- *Literal rule: "yes" in every row, including the control D0.* The clause $\dim \{q\} > \dim \mathcal P_D$ fires because of the coupling block $S_0 \times (C / \operatorname{im} D)$ (C2.2), which exists without any gauge symmetry, and the kernel excess $-6$ is the same coupling lifting $\ker p$. The literal falsifier ("every row no") is therefore not met, but vacuously: the rule measures the freedom to couple $\mathcal H_0^{\wedge 2}$ to any added direction, not content tied to $D$ (C3).
- *The literal "yes" is built from parameters criterion (iv) excludes.* At a point of $\{q\}$, $\bar q = \begin{pmatrix} p & b \\ b^{\mathsf T} & r \end{pmatrix}$ on $\bar S_0 \oplus (C / \operatorname{im} D)$, with A5's source $j = (p \Psi^2, 0)$. Stationarity of $- q(\Sigma_2, \Sigma_2) + 2 J_\Psi(\Sigma_2)$ gives $\Sigma_C = - r^{-1} b^{\mathsf T} \Sigma_0$ and $(p - b r^{-1} b^{\mathsf T}) \Sigma_0 = p \Psi^2$, so (Schur complement, $r$ invertible)
$$\tilde S^{(4)}\big|_{\rm elim} \propto j^{\mathsf T} \bar q^{-1} j = (p \Psi^2)^{\mathsf T} \big( p - b \, r^{-1} b^{\mathsf T} \big)^{-1} (p \Psi^2) , \qquad b = 0 : \ = p(\Psi^2, \Psi^2) = \mathcal V_4(\Psi^4) . \tag{C3.1}$$
For generic $b \neq 0$ the right-hand side is not $\mathcal V_4(\Psi^4)$ whenever $c' > \dim\ker p$ (the case of every row, $c' \ge 79$ against 6), so criterion (iv) fails (record 102's E1b Schur condition): the coupling block that produces the literal "yes" – and the kernel excess $-6$ it causes – is generically excluded by the record's own source term, and under A5 the admissible family is $\mathcal P_D$ plus the blocks whose coupling to $\operatorname{im}p$ is carried by directions of $C/\operatorname{im}D$ that also couple to $\ker p$ (here $b = (b_u; b_w)$ denotes the rows of $b$ along $\operatorname{im}p$ and $\ker p$; stationarity in $\ker p$ sets $b_w\Sigma_C = 0$; (iv) survives iff $b_u (r)^{-1} b_u^{\mathsf T}$ restricted to $\ker b_w$ vanishes on $\operatorname{im}p$) – a proper subvariety of $\{q\}$ when $c' > \dim\ker p$, the case of every row. The literal "yes" is vacuous twice over. (With the source $J = q(\Sigma_2, \Psi^2)$ any block is harmless; *Scope*.) (C3.1) is not machine-checked; it is the standard elimination formula.
- *Refined rule (L1 transversality test on $\ker B_2$).* Dc and Dgen are "no": transverse in every sector, $q$ is the projector form on the 99-dimensional slice $\ker B_2$, of which 20 dimensions are $\mathcal H_0^{\wedge 2}$ and 79 are added slice directions with free entries of $q$. Every other row is "yes" only through sectors where $D$ degenerates: type (a), where $D$ vanishes and the $c_0^-$ components are neither gauge nor slice (E1b, no gauge symmetry acts there at all), and, for the odd functions DcL, DcLo, type (b) in the sector $\{-1, 1\}$ (total $L_0^- = 0$, strands not level matched), where $D(L^{(0)})$ lies inside the slice (E1a, dimension 4) and $q$ vanishes on it: residual gauge directions of the gauge-fixed form, which never reach $\mathcal H_0^{\wedge 2}$.

## Block C4 (the prediction from L1)

\subsection*{Setup}

A6, A7 with $D = c_0^{-(1)} f(L_0^{-(1)}) + c_0^{-(2)} f(L_0^{-(2)})$ acting on all two-strand states (ghost numbers 3, 4, 5); $f_i := f(m_i)$ in the sector $\{m_1, m_2\}$.

\subsection*{Derivation}

With the Koszul convention, $\{c_0^{-(i)}, b_0^{-(j)}\} = \delta_{ij}$ and $\{c_0^{-(1)}, c_0^{-(2)}\} = 0$, so
$$\{D, B_2\} = f(L_0^{-(1)}) + f(L_0^{-(2)}) , \qquad D^2 = f_1 f_2 \{c_0^{-(1)}, c_0^{-(2)}\} = 0 , \qquad B_2^2 = 0 . \tag{C4.1}$$
If $h := f_1 + f_2 \neq 0$, every $x \in E_\sigma$ decomposes as
$$x = h^{-1} B_2 D x + h^{-1} D B_2 x , \qquad h^{-1} B_2 D x \in \ker B_2 , \quad h^{-1} D B_2 x \in \operatorname{im} D , \tag{C4.2}$$
and $y = D\lambda \in \ker B_2$ gives $y = h^{-1} B_2 D D \lambda = 0$:
$$E_\sigma = S_\sigma \oplus \operatorname{im} D_\sigma \quad (h \neq 0) . \tag{C4.3}$$
If $h = 0$: either $f_1 = f_2 = 0$, $D_\sigma = 0$ and $E_\sigma \neq S_\sigma$ (type (a), $W_\sigma = E_\sigma / S_\sigma$); or $f_1 = - f_2 \neq 0$, $\{D, B_2\} = 0$ on the sector, and for $\lambda \in L^{(0)}_\sigma$ ($B_2 \lambda = 0$)
$$B_2 D \lambda = - D B_2 \lambda = 0 , \qquad D(L^{(0)}_\sigma) \subseteq S_\sigma \cap \operatorname{im} D_\sigma \quad (\text{type (b)}) . \tag{C4.4}$$

\subsection*{Commentary}

- (C4.2) is the Hodge decomposition of the plan's prediction; the operator that must be invertible is $\{D, B_2\}$ on the two-strand sector, $f(m_1) + f(m_2)$, not $f$ on each strand. On the diagonal sectors the two coincide; off the diagonal the plan's wording ("in every sector where $f(m) \neq 0$") mispredicts: DcL is transverse in $\{-1,0\}$, $\{0,1\}$ ($f$ vanishes on one strand) and non-transverse in $\{-1,1\}$ ($f$ non-zero on both); Dcd, Dc1d are transverse in $\{-1,0\}$, $\{0,1\}$. Seven mismatches, all listed by check C4-prediction; the conclusion "$D = c_0^-$ alone is no" holds (relative to $\ker B_2$).
- (C4.4) is the only E1a mechanism among the $D$'s of A7, and it sits at total $L_0^- = 0$ with the strands not level matched: the analogue of Siegel's $L_0 = 0$ lies outside $\mathcal H_0^{\wedge 2}$. The forced degeneracy is of $q$ on $S \cap \operatorname{im} D$, which $q \circ D = 0$ already imposes; it does not touch $\ker p$, since $S_0 \cap \operatorname{im} D = 0$ (C2.1). The present $\ker p$ is never pure gauge for a $D$ of A7.

\subsection*{Result}

$$\boxed{\; E_{\{m_1, m_2\}} = \ker B_2 \oplus \operatorname{im} D \iff f(m_1) + f(m_2) \neq 0 ; \quad \text{type (a) at } f_1 = f_2 = 0, \ \text{type (b) at } f_1 = - f_2 \neq 0 \;}$$

\subsection*{Verification}

C4-prediction, on the four rows of the form $c_0^- f(L_0^-)$, every sector, both seeds.

## Conclusion (C5)

At the quadratic level and for every field-independent $D$ built from $c_0^-$ and $L_0^-$ (row D1 of record 102, all four words with arbitrary functions of the two $L_0^-$), with $B_2 = b_0^-$:

1. The $\Lambda_2$ orbit never has a component along $\mathcal H_0^{\wedge 2}$ (C2.1). The present components of $\Sigma_2$ are not gauge directions, the composite parameter $\Lambda \otimes \Psi$ is moved out of $\mathcal H_0^{\wedge 2}$, and the residual-symmetry question of 3b is trivial for these $D$: the composite law $2 \, \delta_\Lambda \Psi \otimes \Psi$ lies in $\mathcal H_0^{\wedge 2} \subset \ker B_2$ and needs no compensating $\Lambda_2$, but no $\Lambda_2$ mixes with it either (criterion 3c fails).
2. Gauge fixing alone never returns the present content. The slice $\ker B_2$ is $\mathcal H_0^{\wedge 2}$ plus five $c$-count-1 states in $\{0,0\}$ plus the $b_0^-$-annihilated states of the sectors $m \neq 0$ (C2.4); the per-strand slice, which is $\mathcal H_0^{\wedge 2}$ in $\{0,0\}$, is never complemented by $\operatorname{im} D$ (C2.3). The extra directions must be decoupled or eliminated (E1b), which is not a gauge mechanism – in agreement with both readings: Erbin–Médevielle impose the constraints beside the action (their (5)), and Okawa–Sakaguchi's vertex projects every input by $B c_0^-$ (their (7)), i.e. it is decoupled from the extra components by construction.
3. Where $D$ is transverse (Dc, generic D1) L1 holds on the extended slice: $q = P^{\mathsf T} (q|_S) P$, the information in $q$ beyond $\mathcal V_4$ sits in $q|_S$ on the added slice directions and their coupling to $\mathcal H_0^{\wedge 2}$, none of which is gauge related; under A5 that coupling is moreover generically excluded by criterion (iv) (C3.1).
4. Where $D$ degenerates the extra content is E1b (type (a), no gauge symmetry acts) or, type (b), residual gauge directions inside the slice at total $L_0^- = 0$ off level matching – gauge content, the analogue of Siegel's $L_0 = 0$ asked for by E1, but one that never reaches $\mathcal H_0^{\wedge 2}$.

The result is items 1–4 (C2.1, C2.4, C2.3, C4), not a yes/no column: both rules fire on $D = 0$, and the literal "yes" is built from the coupling block that A5's source term generically excludes (C3.1, $c' > \dim\ker p$ in every row). In substance C1 with these $D$'s is the projector construction on $\ker B_2$, sector by sector where $f(m_1) + f(m_2) \neq 0$ (for $D = c_0^- f(L_0^-)$ symmetrized; the $N$-words by the table), plus auxiliary directions (E1b) and residual gauge directions that never reach $\mathcal H_0^{\wedge 2}$ – what the plan's falsifier was written to detect. The routes left, as the plan states for this outcome: E2 (field-dependent $D$ at cubic order, Task 9), and the derived law of track (2) on this strand model (Task 24); in addition, not in the plan's list, field-independent $D$'s that lower the $c$-count, rows D1 + D2 of record 102 (the $12 + 12$ monomials; $c_0^- f(L_0^-) + b_0^- \hat p \, g(L_0^-)$, with $\hat p$ the extension of $p_{2,2}$ to non-level-matched inputs, is one representative). Within record 102's block list this is the only field-independent way for $\operatorname{im} D$ to reach $\mathcal H_0^{\wedge 2}$ – a field-independent two-in, two-out $D$ contains at most one power of $p_{2,2}$ (rows D1, D2), and only a shift-$(-1)$ word lowers the $c$-count. It also needs the extended vertex's output to leave $\ker b_0^-$ (carry a $c_0^-$ component): on level-matched inputs $p_{2,2}$ outputs level-matched states, where $b_0^-$ acts as zero. That is a property of the worldsheet vertex on non-level-matched states (E3, Task 7), not of the algebra.

### Scope of the exclusion (C5)

- *Class.* Field-independent $D$ of ghost number $+1$ built from the zero modes $c_0^-$, $b_0^-$ and functions of $L_0^-$ on two strands (row D1: every shift-$+1$ word), $B_2 = b_0^{-(1)} + b_0^{-(2)}$, $q$ an arbitrary symmetric form on the two-strand space of the strand model with $q|_{\mathcal H_0^{\wedge 2}} = p$, the source term extended by zero, quadratic order. Physical reason: these are all the field-independent $D$'s that ghost number allows without the vertex (record 102, table), i.e. the setting of L1 on the space that relaxing level matching produces. The structural statements C2.1, C2.3, C2.4, C4 are proven for arbitrary strand spaces; the dimensions are those of the model.
- *Physically relevant cases outside.* Row D2 and its sum with D1 (needs $p_{2,2}$ on non-level-matched inputs; can lower the $c$-count); field-dependent $D$ (E2, cubic order); other gauge conditions (the other words of row B1, e.g. $b_0^- \otimes c_0^- b_0^-$ symmetrized, or $b_0^- g(L_0^-)$ – not tested); a source term other than the extension by zero (with $J = q(\Sigma_2, \Psi^2)$ the elimination returns $\mathcal V_4(\Psi^4)$ for any coupling block, which makes the auxiliary directions harmless but still not gauge; not checked here, 3b).
- *Weakest relaxation that evades it.* A $D$ with a $c$-count-lowering part, rows D1 + D2 – the only one within record 102's block list – which is where the worldsheet vertex on non-level-matched states enters; it evades the exclusion only if that vertex's output leaves $\ker b_0^-$ (Conclusion, last paragraph).

## Verification

Script `codes/verify-gauge-unfixing-c1.py`, run from the project root as `uv run --no-sync python codes/verify-gauge-unfixing-c1.py <seed>` at seeds 20261018 and 20261019: 10/10 PASS at each, exit 0, about 1 min 20 s each, peak RSS 75 MB, one process.
Exact arithmetic over $\mathbb Q$ (Fractions) for every rank, null space, inverse and family point except the large homogeneous solve of C2.2-brute (modulo $2^{31} - 1$) and the kernel of $q$ at a family point (modulo the prime, upper bound, matched against the exact lower bound $\operatorname{rank} D$, resp. $\operatorname{rank} D + \dim \ker p$, given by vectors verified exactly to lie in the kernel).

| check | node | what it tests | break leg |
| --- | --- | --- | --- |
| C1.1-pairing | C1.1 | graded symmetry, rank 48/48, support | sign of $\langle\!\langle \bar e, e \rangle\!\rangle$ flipped: symmetry fails |
| C1.2-adjoint | C1.2 | (M.3) on all basis pairs | $\mathrm{bpz}(c_0^-) = + c_0^-$ fails |
| C1.3-omega1 | C1.3 | $\langle\!\langle A, c_0^- B \rangle\!\rangle$ against M's pairing table, symmetric | – |
| C1.4-two-strand | C1.4 | (M.5) on random $\Sigma$, $X$, against the restricted pairing built independently | the $+$ sign fails |
| C2.1-raise | C2.1 | $\tau$-equivariance, sectors, $c$-count $+1$, $\operatorname{im} D \subseteq C$, all nine rows | – |
| C2.3-count | C2.3 | $\dim E^{(1)}_\sigma = 2 \dim L^{(0)}_\sigma$, six sectors | – |
| C2.2-brute | C2.2 | direct solve for symmetric $q$ in a smaller strand model ($\dim E = 39$, six rows): nullities equal (C2.2), (C2.3) | $q$ not symmetric: nullity 932 against 297 |
| C2.2-family | C2.2 | random family points satisfy the constraints exactly | – |
| C3-table | C3, C2.4 | the table; literal "yes" in every row, control D0 included. In the main model the columns $\dim \{q\}$, $\dim \mathcal P_D$ are evaluated from the formulas (C2.2), (C2.3) and exact ranks, not solved (the formulas are proven and brute-forced in the small model, C2.2-brute), so the column check $\dim \{q\} - \dim \mathcal P_D = s c'$ is the formula twice; the kernel excess is the independent number per row (mod-$p$ upper bound against exact witnesses) | (the control row is the vacuity probe of both rules, not a test of a claim) |
| C4-prediction | C4 | transversality rule $f(m_1) + f(m_2) \neq 0$ and the types, four rows, six sectors; the plan's wording compared | the plan's rule, run as a predictor, mispredicts seven sectors |

What is not verified: (C3.1) (elimination at a generic family point; standard Schur-complement formula, not run); anything about the string vertex on non-level-matched states ($q$ is a generic stand-in); sub-task 3b (residual symmetry, compensating $\Lambda_2$, elimination); rows D2 and D1 + D2; other $B_2$ words; field-dependent $D$. The structural nodes C2.1, C2.3, C2.4, C4 have proofs in the record valid for arbitrary strand spaces; the checks confirm them on the model.

## Working notes

- Deviation from the plan's verdict rule (A8): the literal rule of criterion (i) with decision (A) is applied and reported; a refined rule was added after the literal one was seen to give "yes" for $D = 0$ (C3). The refined rule also gives "yes" for $D = 0$; after the critic (fix pass) neither is a verdict, and the recommendation is that the memo's C1 table show per row the transversality type of each sector and $\dim (\operatorname{im} D \cap \mathcal H_0^{\wedge 2}) = 0$, with D0 as the control, instead of the two yes/no columns.
- Deviation from the plan's slice: the plan names "$B_2 = b_0^-$ on a strand". Both readings are computed: $B_2 = b_0^{-(1)} + b_0^{-(2)}$ (maps into $L$, a gauge condition; primary) and the per-strand condition $S_{\rm per}$ (returns $\mathcal H_0^{\wedge 2}$; never complemented, C2.3).
- Model M's helper functions are copied into the new script (not into a `lib/` module): the project keeps its scripts in `codes/` and has no `lib/`; record 102's script is not edited.
- The time box (45 min) was exceeded by about 25 min, for the second slice reading and the refined rule.

## Proposed ledger entries

Ledger section: ## Results

### R? — excl. within field-independent zero-mode D's: candidate C1 at quadratic order is, for D = c_0^- f(L_0^-) symmetrized, in every sector where f(m_1) + f(m_2) ≠ 0, the projector form on ker(b_0^-(1) + b_0^-(2)) (the c_0^- b_0^- words: sector types numerical, table rows DN, Dgen, Dgen0); the per-strand slice is never a gauge slice; no D of the class acts on H_0^∧2 [Proven]
Promoted as R102 (2026-10-22).

- **Source**: `agent/derivations/108-gauge-unfixing-c1-strand-model.md#C5` (nodes C2.1, C2.3, C2.4, C4; table C3, D0 as control).
- **Scope**: field-independent $D$ of ghost number $+1$ built from $c_0^-$, $b_0^-$ and functions of $L_0^-$ on two strands (row D1 of record 102), $B_2 = b_0^-$ symmetrized, $q$ any symmetric form with $q|_{\mathcal H_0^{\wedge 2}} = p$, source term extended by zero, quadratic order; structural statements for arbitrary strand spaces, dimensions in the strand model of record 108 (model M at $m = 0$).
- **Verification**:
  - 2026-10-18 `codes/verify-gauge-unfixing-c1.py` C2.1-raise, C2.3-count, C2.2-brute, C2.2-family, C3-table, C4-prediction, seeds 20261018 and 20261019, 10/10 PASS (computator, record 108).

Every such $D$ raises the $c_0^-$ count by one, so $\operatorname{im} D$ never meets $\mathcal H_0^{\wedge 2}$: $\Lambda_2$ does not act on the present components of $\Sigma_2$ and no $D$ mixes $\Lambda_2$ with $\Lambda \otimes \Psi$. Relative to $\ker B_2$ a sector $\{m_1, m_2\}$ is transverse iff $\{D, B_2\} = f(m_1) + f(m_2)$ is invertible (for $D = c_0^- f(L_0^-)$); there $q = P^{\mathsf T} (q|_S) P$. The slice $\ker B_2$ is always larger than $\mathcal H_0^{\wedge 2}$ (five $c_0^-$ states in the level-matched sector of the model, all $b_0^-$-annihilated states with $L_0^- \neq 0$), and the per-strand slice is never complemented by $\operatorname{im} D$ ($\dim E^{(1)} = 2 \dim L^{(0)}$). The non-transverse sectors carry E1b directions (no gauge symmetry acts), or, for odd $f$, residual gauge directions inside the slice at total $L_0^- = 0$ off level matching ($f(m_1) = - f(m_2) \neq 0$), which never reach $\mathcal H_0^{\wedge 2}$. Neither yes/no rule discriminates: criterion (i) with the decoupled family, and the slice-relative rule, both give "yes" on $D = 0$; the literal "yes" rests on a coupling block between $\mathcal H_0^{\wedge 2}$ and the added directions which, with the source term extended by zero, generically breaks the elimination to $\mathcal V_4(\Psi^4)$ ($c' > \dim\ker p$ in every row). The only field-independent route to $\mathcal H_0^{\wedge 2}$ within record 102's block list is rows D1 + D2, and it requires the vertex on non-level-matched inputs to output states outside $\ker b_0^-$.

## Status

Sub-task 3a complete (2026-10-18), fix pass after critic gu-5 applied (2026-10-18), fix pass 3 after check critic-gu-check-108 applied (2026-10-22: C3 and C5 wording narrowed, conclusions unchanged; ready for promotion with the edited ledger draft): claim tree C1–C5 justified, table of criterion (i) with both yes/no rules (neither a verdict; the result is C2.1, C2.3, C2.4, C4), prediction from L1 checked and corrected, script 10/10 PASS at both seeds (script unchanged by the fix pass). Plan criterion (ii) (the constraint set as explicit equations for the rows kept) is open, deferred to 3b. Next: orchestrator decision on the memo's C1 table; 3b only for rows the orchestrator keeps (DcL, DcLo for the type-(b) sector), or the D1 + D2 extension.

## Revisions

Fix pass 2026-10-18 (brief `computator-gu-3-fix-20261018T104718`, critic `critic-gu-5-20261018T103840`):
- #1 [major] Applied: A8, *Verdict rules* (new paragraph *Neither rule is a verdict*), *Reading*, C5, Conclusion, Working notes, ledger body and frontmatter now state that both rules fire on $D = 0$ (and the refined one on DN), read the refined column as the L1 transversality test on $\ker B_2$, and make C2.1, C2.3, C2.4, C4 the result; memo recommendation in Working notes.
- #2 [minor] Applied: one account kept – the refined rule is post hoc, added after the literal table fired on $D = 0$ (*Verdict rules*, A8, Working notes).
- #3 [note] Applied: A5 states that total-$L_0^-$ conservation would only shrink $\{q\}$ and leaves the sector-local nodes unchanged.
- #4 [minor] Applied: type-(b) directions are now "residual gauge directions that never reach $\mathcal H_0^{\wedge 2}$", not "no gauge content" (C5, Conclusion item 4, *Reading*, frontmatter, ledger body).
- #5 [major] Applied: new bullet in *Reading* with eq. (C3.1) (Schur complement) and C3 extended: the literal "yes" rests on the coupling block, which under A5 breaks criterion (iv); the optional machine check was not added (standard formula; listed as not verified). (Wording narrowed to "generic" in fix pass 3, below.)
- #6 [minor] Applied: Conclusion and *Scope* state the class (record 102's block list), the condition that the vertex output leave $\ker b_0^-$, and "rows D1 + D2" with $c_0^- f + b_0^- \hat p \, g$ as one representative.
- #7 [major] Applied: ledger title, frontmatter and ledger body say "projector form on $\ker(b_0^{-(1)} + b_0^{-(2)})$ in the sectors with $f(m_1) + f(m_2) \neq 0$; per-strand slice never a gauge slice". (The $f$-rule restricted to the $c_0^- f(L_0^-)$ words in fix pass 3, below.)
- #8 [minor] Applied: Status names plan criterion (ii) as open.
- #9 [minor] Applied: the C3-table row of the Verification table says the main-model columns are formula-evaluated and the kernel excess is the independent number.
- #10 [note] Not applied: the dead code in `complement_projection` has no effect on any result, and editing the script would require a rerun the fix pass does not otherwise need.

Changed nodes: A8 (statement), C3 (statement extended by the criterion-(iv) clause; new justification eq. (C3.1)), C5 (statement reworded: conjunction of C2.1, C2.3, C2.4, C4; type-(b) wording). Dependents: C5 depends on C3 and still holds (its content no longer uses any yes/no column); C5 is the root, no further dependents. C1, C2.x, C4 unchanged.

Fix pass 3 2026-10-22 (brief `computator-gu-108-fix3-20261022T194958`, check `critic-gu-check-108-20261022T193154`, replacements (R1)–(R4)); statements narrowed, conclusions unchanged:
- #2 [major] Applied (R1), (R2): C3 and *Reading* say a *generic* coupling block breaks criterion (iv) whenever $c' > \dim\ker p$ (true in every row, $c' \ge 79$ against 6); the exception set "Schur-null blocks with $b \, r^{-1} b^{\mathsf T} = 0$ on $\operatorname{im} p$" is replaced by the blocks whose coupling to $\operatorname{im} p$ is carried by directions that also couple to $\ker p$ ($b_w \Sigma_C = 0$), a proper subvariety of $\{q\}$.
- #3 [minor] Applied (R3): the $f(m_1) + f(m_2)$ rule is stated for $D = c_0^- f(L_0^-)$ symmetrized (C4); for the $c_0^- b_0^-$ words the sector types are the table's numbers (C5, Conclusion, frontmatter, ledger title). The check's row list "Dcd, Dc1d, DN, Dgen, Dgen0" is corrected to "DN, Dgen, Dgen0": Dcd and Dc1d are of the form $c_0^- f(L_0^-)$ (*The D's tested*, C4 commentary, script lines 433–434).
- #4 [minor] Applied (R4): "excluded by criterion (iv)" / "breaks the elimination" read "generically" in Conclusion item 3 and last paragraph, and in the ledger body; the condition $c' > \dim\ker p$ is stated where the claim is restated.
- Not done: optional check #5 ((C3.1) machine check); no script change, no script run.

Changed nodes: C3 (statement narrowed: "a non-zero block breaks (iv)" becomes "a generic coupling block breaks (iv) whenever $c' > \dim\ker p$"; justification unchanged), C5 (statement narrowed in clause (iv) and in its use of C3.1; justification unchanged). A8 unchanged. Dependents: C5 depends on C3 and still holds (its conclusion uses neither the old universal nor the exception set); C5 is the root, no further dependents. C1, C2.x, C4 unchanged. Root claim unchanged; `Open gaps:` and `Hypotheses in force:` unchanged (none).
