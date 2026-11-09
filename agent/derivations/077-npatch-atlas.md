# 077 — The $n$-puncture patch in the atlas / transition-function picture of closed SFT: counts, ghost numbers, limits, and the generalised tree

Brief: `agent/briefs/active-computator-077-npatch-atlas-20261004T100000.md` (time box 30 min).
Model: claude/fable. Date: 2026-10-04.

## Status

2026-10-04 11:05. Complete: §1–§6 written, `codes/verify-npatch-atlas.py` 27/27 PASS (14 checks + 13 break legs, seed 20261004; re-run after the fix pass, unchanged). Fix pass (critic iteration 1) applied: all 12 findings and the notes, listed in `## Fix pass (critic iteration 1)`. Narrow confirmation pass (critic iteration 2, `agent/reports/critic-077-confirm-20261004T105000.md`): promotable; four minor residues #R1–#R4 and note #N2 applied by the orchestrator 2026-10-04 10:39 ((2.5) group label, PH31 on the quintic-composite clause of §6.1, the asymmetric-region sentence of §6.1 para 2 replaced by the open question, §6.4's C5 status, §4 Commentary). Last completed step: residues applied. Next step: promotion (orchestrator).

## Task and objective

**Literal task.** Place the $n$-puncture patch (a chart containing $n$ puncture discs with its own coordinate, the circle of records 071/074) in the atlas / transition-function description of a closed-string worldsheet, and state with counts what it does to that picture: which object replaces the three-punctured sphere, where the moduli sit (inside the patch versus in the transition functions), what the transition functions become, and what is established versus proposed.

**Motivating objective.** The paper's worldsheet section has to say in one paragraph, in the language of ordinary SFT (atlas, transition functions, plumbing), what the Hubbard–Stratonovich theory ($\Sigma_k\in\mathrm{Sym}^k\mathcal H$, kinetic forms $p_{k,k}$ on the $2k$-punctured sphere, trinion couplings on multi-punctured spheres) does to the standard picture. Records 071 (R79) and 074 (R80) settle $n=2$; this record places them and states what general $n$ requires. Success = §6.1 (the answer) supported by counted or proven claims, with the $n\ge3$ statements marked as necessary conditions on an object ($\mathcal V'_{n+1}$ with internal moduli) that this project has not constructed.

## Conventions and assumptions

- **A1** Project conventions: physical ghost number, $N_{\rm gh}(\Psi)=2$, $N_{\rm gh}(\Sigma_k)=2k$; sphere ghost-number anomaly $6$; pairing sign C1 (not load-bearing: every statement below is a count). Closed bosonic string, genus zero, tree level, flat background.
- **A2** Plumbing (074 A2, Erbin 2023 `bos:eq:q-s-th`): two discs with coordinates $w_L,w_R$ are glued by $w_Lw_R=q$, $q=e^{-s+i\theta}$; the gluing is realised on $\mathcal H$ by $\mathcal S(q)=e^{-sL_0^+}e^{i\theta L_0^-}$ with the BPZ pairing, with Schiffer antighosts $b(\partial_s)=-b_0^+$, $b(\partial_\theta)=ib_0^-$ (032 (4.4)), one antighost per real modulus. A gluing edge therefore carries one complex modulus and ghost number $-2$.
- **A3** The $n$-patch (071 A3): one $(n+1)$-punctured sphere with one special puncture whose coordinate $w_0$ is fixed exactly, global coordinate $u=1/w_0$ (the Möbius form $w_0=1/u$ of the special coordinate, $u$ a global coordinate, is the definition of a chart — a chart needs a coordinate on the whole disc; the asymmetric vertex region $\mathcal V'_{n+1}$ of 071 A3 at $n\ge3$ need not have a special coordinate of this form, and the moduli counts (3.1), (4.1), (4.4) do not depend on it, while C2's germ statement and the decomposition of the redundancy are specific to it), the $n$ ordinary punctures at $u=z_i$ with local maps $f_i$, their unit discs pairwise disjoint and inside $|u|<1$ (vertex condition). *Rigid* patch: one such surface (no moduli integral). *Patch with internal moduli*: a family of such surfaces over a region $\mathcal V'_{n+1}\subset\mathcal M_{0,n+1}$ together with a section of local coordinates (special coordinate included); for $n\ge3$ this object is **not constructed** in this project (TODO §2), and every statement that uses it is a necessary condition on it, not a construction. At $n=2$ the rigid patch is R2's $\mathcal V_3'$ (074 A4).
- **A4** Standard closed SFT at genus zero: symmetric vertices $\mathcal V_{0,N}\subset\hat{\mathcal P}_{0,N}$ (regions with a section of local coordinates), the Feynman regions being the plumbings of lower vertices over $|q|\le1$; $\dim_{\mathbb C}\mathcal M_{0,N}=N-3$ for $N\ge3$, virtual dimension $N-3$ for $N\le2$ (036 C1.1). The circle state $\Phi_n$ and its properties are taken from R79; the fixed-halves model of $p_{2,2}$ and its inverse from R80.
- **A5** Trees: a tree graph with $N$ labelled leaves (external punctures) and internal vertices of valence $k\ge3$; $V_k$ the number of $k$-valent internal vertices, $V=\sum_kV_k$, $E$ the number of edges, $E_{\rm int}=E-N$ the number of internal edges. A puncture disc attached to a vertex by its fixed local coordinate is a leaf (no transition-function modulus); an $n$-patch with $n\ge2$ is an internal vertex of valence $n+1$ (its $n$ puncture leaves and its special leg).

No new hypothesis is declared. PH10 and PH5 are cited where R79's statements carry them (C4.4, C5.2 of 071); PH31 where R80's inverse is cited (C2.1's last clause, C4 of 074). Free constants: none (every claim is a count or a cited identity).

## Claim tree

- **A1–A5** as above.
- **C1** The standard atlas of a genus-zero $N$-punctured surface in a Feynman region is $N$ puncture discs plus $N-2$ rigid three-punctured spheres (pants) with $N-3$ transition functions $w_aw_b=q_{ab}$ on the internal edges, carrying the $N-3$ complex moduli and the $2(N-3)$ antighosts; at genus zero a global coordinate makes the pants charts dispensable, and the physical content of the atlas is the $N$ local coordinates at the punctures and the clustering (the tree with its collar circles); the chart coordinates on the pants and the position of each circle in its collar are bookkeeping. [by C1.1–C1.3]
  - **C1.1** Trivalent tree with $N$ leaves: $V=N-2$, $E_{\rm int}=N-3$. [eq. (1.1)] [check: C1.1-trivalent]
  - **C1.2** Ghost-number bookkeeping of the Feynman region: $2N-2(N-3)=6$; second route $\hat d=S-6=n_b-n_c$ with $S=2N$, $n_c=0$, $n_b=2(N-3)$. [by A1, A2, C1.1; R40/036 C1.1; eq. (1.2)] [check: C1.2-ghost]
  - **C1.3** Physical versus bookkeeping data of the atlas. [by A2, A4; eq. (1.3)]
- **C2** The $n$-patch is a chart: an $(n+1)$-punctured sphere with one special puncture (the chart boundary) whose special coordinate is $1/u$ for a global coordinate $u$, hence determined by the scale and centre of $u$ (its 2-jet); its automorphisms compatible with the gluing form $w_Lw_R=q$ are the $\mathbb C^*$ of dilation and rotation of the circle; two $n$-patches glued by one transition function over-parametrise the glued surface by four complex parameters: the Möbius freedom of the global coordinate (the two chart centres and the dilation fixing them, this dilation with $q$ fixed being the seam) and the rescaling of one special coordinate compensated in $q$; the group is $\mathrm{PSL}(2,\mathbb C)\times\mathbb C^*_\kappa$, the seam being the dilation subgroup of the first factor, not a direct factor. [by C2.1–C2.3]
  - **C2.1** Parameter count of the two-patch presentation: $2n+1$ complex parameters for $2n-3$ moduli, redundancy of complex dimension $4$. [eq. (2.1)–(2.3)] [check: C2.1-redundancy]
  - **C2.2** The seam $\mathbb C^*$: $(w_L,w_R,q)\mapsto(\lambda w_L,\lambda^{-1}w_R,q)$ moves the collar circle and re-splits the surface between the two charts without changing it; the two circle states change by $\lambda^{\pm L_0}$ with the pairing invariant. [by A2; eq. (2.4); R79 (071 C1.4) for the statement that the circle choice is the seam] [check: C2.2-seam]
  - **C2.3** Rigid patches fix the $\mathbb C^*$ of each chart coordinate by convention, leaving $q$ unambiguous and the circle position as the only (bookkeeping) seam freedom; at $n=2$ this is 074's $s$-circle $|w_1|=r$, $|q|/2\beta<r<2\beta$. [by A3, C2.2; R80 (074 A4)]
- **C3** Moduli count of the kinetic sphere and of the trinion couplings. Two rigid $n$-patches glued by one transition function give one complex modulus, equal to $\dim_{\mathbb C}\mathcal M_{0,2n}=2n-3$ iff $n=2$; for $n\ge3$ the count closes iff each patch carries exactly $n-2$ complex internal moduli, the dimension of $\mathcal M_{0,n+1}$ — a *necessary condition* on the $n$-patch (an asymmetric vertex region $\mathcal V'_{n+1}$), not a construction. General tree: $\sum_k(k-2)V_k=N-2$, $E_{\rm int}=V-1$, and $\sum_kV_k(k-3)+E_{\rm int}=N-3$ for every tree. Three $n$-patches on a rigid pants give $(a-1)+(b-1)+(c-1)=a+b+c-3$. [by C3.1–C3.4]
  - **C3.1** Rigid two-patch count: $1=2n-3\iff n=2$; with internal moduli $d$ per patch, $2d+1=2n-3\iff d=n-2$. [eq. (3.1)] [check: C3.1-kinetic]
  - **C3.2** General tree identity. [eq. (3.2)–(3.3)] [check: C3.2-tree-formula, C3.2-enumeration ($N=4,6,8$)]
  - **C3.3** Trinion couplings: three patches on a pants, $a+b+c-3$. [by C3.2; eq. (3.4)] [check: C3.3-trinion]
  - **C3.4** Matching condition for $n\ge3$: the $q$-region of the gluing fibred over the two internal regions must cover $\mathcal V_{0,2n}$ once (the analogue of 074's determined cutoff $\sigma_V(\theta)$); established at $n=2$ at the level of surfaces in the fixed-halves model — covering Proven (R80 C1.2, a.e.), shape of the region Numerical (R80 C1.3, $\beta=3/2$), on-shell exactness Proven modulo one measure step Argued (R80 C1.4) — stated as a condition at $n\ge3$. [by A3, A4, C3.1; R80]
- **C4** Ghost number of the patch state and the transition function. $\Phi_n$ has $N_{\rm gh}=2n$ (R79 C1.3); dressed with the $2(n-2)$ antighosts of the patch's internal moduli it has ghost number $4$ for every $n\ge2$; two dressed patch states glued by the $b_0^+b_0^-$-dressed plumbing give $4+4-2=6$; second route $\hat d=4n-6=n_b$ split as $2(n-2)+2(n-2)+2$. The transition function of the HS kinetic gluing is the standard plumbing acting on the patch states, with (i) a vertex-region range (reversed plumbing range at $n=2$), (ii) non-level-matched transported states, the twist integral acting sector by sector, (iii) an inverse $p_{n,n}^{-1}$ that is not a gluing (R80 C2.3 at $n=2$), so the generalised tree has edges of two kinds, a $\Sigma_k$-propagator edge removing $2k-3$ complex moduli and carrying $4k-6$ $c$'s. [by C4.1–C4.4]
  - **C4.1** Dressed patch state ghost number $2n-2(n-2)=4$, $n\ge2$; at $n=1$ the virtual count gives $-2$ antighosts $=$ two $c$'s, 036 (1.2)'s CKV pair of the two-punctured sphere. [by A1, A3, C3.1; R79 C1.3; R40 (036 C1.1–C1.2); eq. (4.1)] [check: C4.1-dressed]
  - **C4.2** Pairing counts: kinetic sphere $4+4-2=6$; standard rigid pants with two $\Psi$'s gives $\Phi_2(\Psi,\Psi)$ of ghost number 4 pairing with ghost number 2. [by A1, A2, C4.1; eq. (4.2)] [check: C4.2-pairing]
  - **C4.3** Second route, the $S-6$ calculus, including the trinion couplings. [by C3.3, C4.1; R40 (036 (1.1)); eq. (4.3)] [check: C4.3-S6]
  - **C4.4** Transition function of the HS edge: (i)–(iii) established at $n=2$ with the statuses of R79/R80 ((i) R80 C1.2 covering Proven, C1.3 shape Numerical; (ii) R79 C2; (iii) R80 C2.3, in the fixed-halves model, projector clause Conditional(PH31)), (i)–(ii) read on shell or at finite level in the model (the off-shell level sum of $\Phi_2$ sewn on the reversed range is PH10's domain, 071 C4.4, not used here); counts only at $n\ge3$; the $\Sigma_k$-edge count. [by A2, C4.1; R79, R80, R40 (036 (1.3)–(1.4)), R39; eq. (4.4)] [check: C4.4-sigma-edge]
- **C5** Limits and consistency: $n=1$ is the standard picture (puncture disc, propagator leg, $\Phi_1=U_{f_1}$); $n=2$ reproduces 071 (A.1)–(A.3), (A.9) at $(2,2,0)$ and 074 (1.1)–(1.4) verbatim; the HS Feynman trees reproduce the moduli count of the standard trees at four and six points. [by C5.1–C5.3]
  - **C5.1** $n=1$. [by A3, A5, C4.1; R79 C6] [check: C5.1-n1]
  - **C5.2** $n=2$. [by C2.3, C3.1, C4.4; R79, R80]
  - **C5.3** HS trees at $N=4,6$ against standard trees. [by C3.2, C4.4; eq. (5.1)] [check: C5.3-hs-trees]
- **C6** Answer (§6.1): the effect of the $n$-patch and the generalisation, in words; every sentence of §6.1 restates a node of C1–C5 or a cited R79/R80 statement, with the $n\ge3$ sentences marked as conditions/proposal. [by C1–C5; R79, R80]

Open gaps: none
Hypotheses in force: none for any count or root claim of this record; PH31 enters only through the cited R80 projector clause in C4.4 (iii) (and PH10, PH5 through R79's conditional clauses, which no node here uses: C4.4 (i)–(ii) stay outside PH10 only because they are read on shell, R80 C1.4, or at finite level in the model; the off-shell level sum on the reversed range is PH10's domain, 071 C4.4)

## §1 The standard atlas with counts (C1)

\subsection*{Setup}
A1, A2, A4, A5. Standard material (Zwiebach 1993, hep-th/9206084, plumbing of vertices; Erbin 2023, the Feynman-region section). $T$ is a trivalent tree with $N$ labelled leaves; the Feynman region $\mathcal F_T\subset\mathcal M_{0,N}$ is the set of surfaces obtained by plumbing $N-2$ copies of the cubic vertex $\mathcal V_3$ along the internal edges of $T$ with $|q_e|\le1$.

\subsection*{Derivation}
*(1.1) Vertex and edge count.* In a tree $E=V+N-1$ (number of vertices $V+N$, minus one). Summing the degrees, $3V+N=2E$. Hence
$$
3V+N=2(V+N-1)\ \Longrightarrow\ V=N-2,\qquad E_{\rm int}=E-N=V-1=N-3 .
\tag{1.1}
$$
Each internal edge carries one transition function $w_aw_b=q_e$ (A2), one complex parameter; the leaves carry none (the puncture's local coordinate is the vertex's own coordinate on that leg: the transition function is the identity, or rather is the datum "$f_i$" itself, with no free parameter). So the Feynman region has $E_{\rm int}=N-3=\dim_{\mathbb C}\mathcal M_{0,N}$ complex parameters, the right number for an open region of $\mathcal M_{0,N}$. [C1.1]

*(1.2) Ghost bookkeeping, two routes.* Route 1, by charts: the $N$ external states carry $2N$; each pants is a bare sphere surface state (anomaly 6, no antighost); each gluing edge carries two antighosts $b_0^+b_0^-$ (A2), ghost number $-2$. A sphere correlator is non-zero at total ghost number 6, and the glued object is one sphere, so the condition reads
$$
2N-2E_{\rm int}=2N-2(N-3)=6 .
\tag{1.2a}
$$
Route 2, by the calculus of 036 (1.1): $\hat d=S-6=n_b-n_c$ with $S=2N$ (the ghost number of the inserted states), $n_c=0$ on a stable sphere, so $n_b=2N-6=2(N-3)=2E_{\rm int}$: two antighosts per internal edge, i.e. one per real modulus. [C1.2]
$$
n_b=2N-6=2E_{\rm int}.
\tag{1.2b}
$$

*(1.3) Physical versus bookkeeping data.* The glued surface is a sphere; a global coordinate $z$ exists and each pants chart is the restriction of $z$ to the complement of the three discs (at genus zero the pants charts are not needed in practice). What the surface state depends on is (i) the marked surface, i.e. the positions of the $N$ punctures modulo $\mathrm{PSL}(2,\mathbb C)$, and (ii) the $N$ local coordinates $f_i$ at the punctures (off shell; on shell only (i)). Both are determined by the tree $T$, the vertex data of each pants (its three local coordinates, rigid) and the $N-3$ transition functions: in the global coordinate the $f_i$ are the compositions of the pants' local coordinates with the transition functions along the path from the puncture to the chart carrying $z$. The remaining data of the atlas — which coordinate is used on each pants chart, and where in each collar annulus $\{|q_e|<|w_a|<1\}$ the circle separating the two charts is placed — do not enter (i) or (ii): the collar circle can be moved anywhere in its annulus, and the transported coordinates and positions are unchanged, because $w_aw_b=q_e$ is the same identification whatever circle one cuts along. Hence
$$
\text{physical: } (T,\ \{f_i\}_{i=1}^N,\ \{q_e\}_{e\in E_{\rm int}})\ \text{modulo global }\mathrm{PSL}(2,\mathbb C);\qquad
\text{bookkeeping: pants chart coordinates, circle positions in the collars.}
\tag{1.3}
$$
The clustering, i.e. the tree $T$ together with the choice of which circle encloses which punctures, is physical in a weaker sense: it labels which Feynman region the surface is assigned to, and across the boundary of a Feynman region a surface changes tree (the same surface has two atlas descriptions on the boundary); on the interior of $\mathcal F_T$ the description is unique for $|q_e|<1$, since the plumbing map is injective there (the factorisation property of $\mathcal V_{0,N}$'s construction, A4). [C1.3]

\subsection*{Commentary}
(1.1): standard Euler-characteristic counting; stated so that the general-valence version (3.2) can be compared. (1.2a) is the chart route, (1.2b) the calculus route; they agree because both are the sphere anomaly, but the second is the one that extends to a patch with internal moduli (§4), where the chart route has to be told what the patch carries. (1.3): the statement "pants charts dispensable at genus zero" is about the *coordinates* on the pants, not about the pants as a vertex: the rigid vertex data (three local coordinates up to the overall $\mathrm{PSL}(2,\mathbb C)$) is what fixes the $f_i$, and remains.

\subsection*{Result}
A genus-zero $N$-point Feynman region is $N$ puncture discs, $N-2$ rigid pants, $N-3$ transition functions carrying the $N-3$ complex moduli and the $2(N-3)$ antighosts; the physical atlas data are the $N$ local coordinates and the transition functions along the tree; the pants chart coordinates and the circle positions in the collars are bookkeeping. [C1]

\subsection*{Verification}
`C1.1-trivalent` (enumeration of all trivalent trees with $N\le8$ leaves against (1.1), with a broken variant $V=N-1$ as the break leg), `C1.2-ghost` ((1.2a) against (1.2b) for $N=3..10$). Both are exact integer checks; what they establish is the bookkeeping, not the surface statement (1.3), which is a definition-level argument and not machine-checkable.

## §2 The $n$-patch as a chart (C2)

\subsection*{Setup}
A2, A3. A patch $P$ is the unit disc $|u|<1$ in its coordinate $u=1/w_0$, carrying $n$ ordinary punctures at $u=z_i$ with local maps $f_i$ (A3); its boundary circle $|w_0|=1$ is the special puncture's coordinate curve. Two patches $P_L,P_R$ are glued by $w_Lw_R=q$ in their special coordinates (A2). Positions are counted in complex units; the local maps $f_i$ are carried along and counted separately (they are off-shell data, not moduli).

\subsection*{Derivation}
*(2.1) The patch is an $(n+1)$-punctured sphere with the special coordinate fixed exactly.* Completing the disc by the point $u=\infty$ gives a sphere with punctures $\{z_1,\dots,z_n,\infty\}$ and the coordinate $w_0=1/u$ at $\infty$. A Möbius map preserving $\infty$ and the germ $w_0=1/u$ exactly is the identity (071 A3): the $n$ positions $z_i$ are all parameters of the patch, none is removed by an automorphism. Of these, $n-2=\dim_{\mathbb C}\mathcal M_{0,n+1}$ are moduli of the underlying $(n+1)$-punctured sphere and $2$ are the affine freedom $u\mapsto au+b$ absorbed into the choice of $w_0$ (a change $w_0\mapsto w_0/(a+bw_0)$ of the special coordinate's germ at second order). So the patch carries
$$
\#\{\text{parameters}\}=n\ =\ \underbrace{(n-2)}_{\mathcal M_{0,n+1}}+\underbrace{2}_{\text{germ of }w_0\text{: scale }a\text{ and centre }b}.
\tag{2.1}
$$

*(2.2) Two patches glued: redundancy of the presentation.* In the coordinate $u_R$, extended over the glued surface ($u_L=1/(qu_R)$ by A2), the $2n$ punctures sit at
$$
\{z^R_j\}_{j=1}^n\ \cup\ \{1/(q\,z^L_i)\}_{i=1}^n .
\tag{2.2}
$$
The triple $(z^L,z^R,q)$ has $2n+1$ complex parameters; the marked surface has $2n-3$. The redundancy is the group of transformations of the triple leaving the configuration (2.2) fixed modulo $\mathrm{PSL}(2,\mathbb C)$: every Möbius map $g$ of $u_R$ produces a new triple (read off the new $u'_R$-positions as $z'^R$, and the new $u'_L:=1/(q'u'_R)$-positions as $z'^L$, for any $q'\ne0$), hence $\dim_{\mathbb C}\mathrm{PSL}(2,\mathbb C)+1=4$, and the count closes:
$$
(2n+1)-4=2n-3=\dim_{\mathbb C}\mathcal M_{0,2n}.
\tag{2.3}
$$
Explicitly, write an element of the redundancy group as $(g,\kappa)$, $g$ a Möbius map of $u_R$ and $\kappa=q'/q$; it acts by $(z^L,z^R,q)\mapsto\big(1/(\kappa q\,g(1/(qz^L))),\,g(z^R),\,\kappa q\big)$, and since the $u_R$-configuration transforms by $g$ alone and $q$ by $\kappa$ alone, the group is the direct product $G=\mathrm{PSL}(2,\mathbb C)\times\mathbb C^*_\kappa$. The first factor contains the choice of the two points $u_L=\infty$, $u_R=\infty$ of the surface that serve as centres of the two charts (two complex parameters: the coaxial family of circles of the collar is the pencil through these two limit points) and the dilation of the global coordinate fixing them, $g_\lambda(u)=\lambda u$ with $q$ held fixed, which is the seam $(z^L/\lambda,\lambda z^R,q)$ of (2.4). The central factor $\mathbb C^*_\kappa$ rescales one chart's special coordinate and compensates in $q$: $(z^L/\kappa,z^R,\kappa q)$. The seam is not a normal subgroup of $G$ (it does not commute with the translations that move the centres), so it is not a direct factor. [C2.1]

*(2.4) The seam.* With both centres fixed, the transformations preserving the gluing form are $(w_L,w_R)\mapsto(\lambda w_L,\lambda^{-1}w_R)$, $q$ unchanged: the same identification $w_Lw_R=q$, the same surface, the same transported local coordinates, but the circle $|w_L|=1$ along which the surface is split between the two charts is moved to $|w_L|=|\lambda|^{-1}$ in the old coordinate (any circle separating the two patches' puncture discs: with $r_L,r_R<1$ the radii bounding the puncture discs of $P_L$, $P_R$ in their own coordinates, $|u_L|<r_L$ and $|u_R|<r_R$, i.e. $|w_L|>1/r_L$ and $|w_L|=|q|/|w_R|<|q|r_R$, the separating circles are $|q|r_R<|w_L|<1/r_L$; for $|q|<1$ this contains the collar $|q|<|w_L|<1$, and on the reversed range $|q|>1$ it is non-empty iff $|q|<1/(r_Lr_R)$, the disc-extension bound of R30/R37 ($4\beta^2$ at $n=2$, $r_L=r_R=1/2\beta$)) and the two coordinates are rotated oppositely by $\arg\lambda$. On the states: the circle state of each patch is read in its own special coordinate, so
$$
\Phi^{(L)}\mapsto\lambda^{L_0}\bar\lambda^{\bar L_0}\Phi^{(L)},\qquad \Phi^{(R)}\mapsto\lambda^{-L_0}\bar\lambda^{-\bar L_0}\Phi^{(R)},\qquad
\langle\Phi^{(R)}|\,\mathcal S(q)\,|\Phi^{(L)}\rangle\ \text{invariant},
\tag{2.4}
$$
since $\mathcal S(q)=q^{L_0}\bar q^{\bar L_0}$ commutes with $\lambda^{L_0}\bar\lambda^{\bar L_0}$ and the BPZ pairing of $\lambda^{L_0}A$ with $\lambda^{-L_0}B$ is that of $A$ with $B$. This is the atlas form of 071 C1.4's statement that the choice of circle over the region is the seam: the surface does not know where the circle is; the split of the surface into two circle states does. [C2.2]

*(2.5) Rigid patches.* A rigid patch fixes its configuration $\{z_i,f_i\}$ in its coordinate by convention (R2's $\mathcal V_3'$: $z_{1,2}=\pm2\beta'$ in $w$), which fixes the germ of $w_0$ including its scale: the group $G$ of (2.3) is no longer available as a change of the chart data; in particular $\mathbb C^*_\kappa$ is fixed, so $q$ is unambiguous. What remains of the seam is only the bookkeeping choice of which circle of the collar the two circle states are read on; at $n=2$ this is 074 A4's $s$-circle $|w_1|=r$, $|q|/2\beta<r<2\beta$ (any radius separating the two copies' puncture discs), and the pairing (1.3) of 074 is independent of $r$ by (2.4). For a patch with internal moduli the scale convention of $w_0$ has to be chosen *per surface* of $\mathcal V'_{n+1}$ (a section over the region), and two sections differing by $\lambda(m)$, $m\in\mathcal V'_{n+1}$, give the same surfaces with $q\mapsto\lambda_L(m_L)\lambda_R(m_R)q$: the region of $q$ over which the gluing is integrated (C3.4) is defined only together with the sections. [C2.3]

\subsection*{Commentary}
(2.1): the count $n=(n-2)+2$ is the statement that "a patch" is more than "a surface": it carries the germ of the chart coordinate, which within the Möbius class of A3 is determined by its 2-jet ("fixed to second order" means "fixed within the Möbius class", not "higher jets free"), and this is exactly what the gluing form $w_Lw_R=q$ consumes. (2.3): the redundancy is $4$, not $2$: besides the dilation fixing the centres (the seam) and the rescaling of one chart coordinate against $q$ (the factor $\mathbb C^*_\kappa$), the two centres of the charts are a choice (which points of the surface the charts are "centred on"); moving them changes both configurations and $q$ while keeping the surface. (2.4) is elementary; it is recorded because it is the only place where the seam of R79 C1.4 is a *proven* redundancy — at the level of a fixed surface split along one circle. The higher-order seam (the gluing of local circle choices across a region where clusters move and cross, 071 C1.4) is the statement that no continuous section of circle choices exists over the whole region, which is not addressed here.

\subsection*{Result}
A patch is an $(n+1)$-punctured sphere whose special coordinate is $1/u$ for a global coordinate $u$, hence determined by the scale and centre of $u$ (its 2-jet) ($n$ parameters $=(n-2)+2$); two patches glued by one transition function present the $2n$-punctured sphere with a $4$-dimensional redundancy, $\mathrm{PSL}(2,\mathbb C)\times\mathbb C^*_\kappa$: the Möbius freedom of the global coordinate (the two chart centres and the dilation fixing them, this dilation with $q$ fixed being the seam: circle position and relative rotation of the two coordinates, invisible on the surface and on the glued pairing (2.4)) and the rescaling of one special coordinate compensated in $q$; rigid patches remove it as chart data and leave it as the choice of reading circle. [C2]

\subsection*{Verification}
`C2.1-redundancy`: for $n=2,3,4$ and random complex $(z^L,z^R,q)$, the configuration (2.2) is transformed by a random Möbius map and a random $q'$, the new triple is read off, and the cross-ratios of the two configurations are compared (equal: PASS); the break leg replaces $g$ by a non-Möbius map ($u\mapsto u^2$ on the configuration), which changes the cross-ratios. `C2.2-seam`: the $u_R$-configuration (2.2) is invariant under $(z^L,z^R,q)\mapsto(z^L/\lambda,\lambda z^R,q)$ up to the global dilation, checked on cross-ratios; the break leg uses $(z^L/\lambda,z^R,q)$, which is a different surface. The operator statement (2.4) is the $L_0$ covariance of R79 C2.1/`C2.1-rotation` and is not re-checked. Scope of these two checks: both are tautological for the claims of C2 — they confirm the Möbius invariance of cross-ratios (a textbook fact), and their break legs only show that cross-ratios detect a change of surface; they do not test that the four parameters act effectively or that the redundancy is not larger (the count $(2n+1)-(2n-3)$ is asserted as a literal). C2.1–C2.2 are established by the argument of (2.2)–(2.4), not by these checks.

## §3 Moduli counts (C3)

\subsection*{Setup}
A3–A5. $d_n$ denotes the number of complex internal moduli of an $n$-patch ($d_n=0$ for a rigid patch). In a tree, an $n$-patch with $n\ge2$ is a vertex of valence $n+1$; the pants is a vertex of valence $3$ with $d=0$; a puncture disc is a leaf.

\subsection*{Derivation}
*(3.1) The kinetic sphere.* $p_{n,n}$ is a form on the $2n$-punctured sphere, $\dim_{\mathbb C}\mathcal M_{0,2n}=2n-3$. Two $n$-patches glued by one transition function carry $2d_n+1$ complex parameters. For rigid patches,
$$
2d_n+1=1=2n-3\iff n=2;\qquad\text{in general}\quad 2d_n+1=2n-3\iff d_n=n-2=\dim_{\mathbb C}\mathcal M_{0,n+1}.
\tag{3.1}
$$
So at $n=2$ two rigid patches and one $q$ suffice (and do: R80 C1.2–C1.3, $\mathcal V_{0,4}$ is the $q$-region $Q_V$ of that gluing at the level of surfaces). For $n\ge3$ a rigid patch is excluded by the count, and the patch must carry exactly the moduli of an $(n+1)$-punctured sphere: the $n$-patch is then a family over a region $\mathcal V'_{n+1}\subset\mathcal M_{0,n+1}$ with a section of local coordinates — the asymmetric vertex of 071 A3, with internal moduli. (3.1) is a necessary condition on that object; it is exact (no slack: fewer moduli undercount, and a patch cannot carry more than $\dim\mathcal M_{0,n+1}$ surface moduli, the two further parameters of (2.1) being chart data absorbed by the redundancy of (2.3)). This project has not constructed $\mathcal V'_{n+1}$ for $n\ge3$ (TODO §2: build asymmetric vertices from higher-order symmetric vertices). [C3.1]

*(3.2) General tree.* For a tree with $N$ leaves and $V_k$ internal vertices of valence $k\ge3$: $E=V+N-1$ and $\sum_kkV_k+N=2E$, so
$$
\sum_k(k-2)V_k=N-2,\qquad E_{\rm int}=V-1 .
\tag{3.2}
$$
Assign to a $k$-valent vertex $k-3$ complex internal moduli (a $k$-punctured sphere region, $\dim\mathcal M_{0,k}=k-3$) and to each internal edge one transition-function modulus. Then
$$
\sum_kV_k(k-3)+E_{\rm int}=\sum_k(k-3)V_k+\sum_kV_k-1=\sum_k(k-2)V_k-1=N-3=\dim_{\mathbb C}\mathcal M_{0,N},
\tag{3.3}
$$
for *every* tree: the moduli count is insensitive to how the surface is cut into vertices, provided each vertex carries the moduli of its own punctured sphere and each internal edge one plumbing parameter. Low cases ($N=4$): $V_4=1$ (one quartic vertex, $1+0=1$); $V_3=2$, $E_{\rm int}=1$ ($0+1=1$). ($N=6$): $V_6=1$ ($3$); $V_4=1,V_3=2$, $E_{\rm int}=2$ ($1+2=3$); $V_5=1,V_3=1$ ($(5-2)+(3-2)=4=N-2$), $E_{\rm int}=1$ ($2+0+1=3$); $V_4=2$, $E_{\rm int}=1$ ($1+1+1=3$); $V_3=4$, $E_{\rm int}=3$ ($3$). The enumeration for $N=4,6,8$ is in the script (`C3.2-enumeration`). [C3.2]

*(3.4) Trinion couplings.* $V_{a+b+c}(\Sigma_a,\Sigma_b,\Sigma_c)$ factorises pointwise through three circles on a bare pants (R79 C1.4): in the atlas, one rigid pants ($d=0$) with three patches attached, the $n$-patch contributing $d_n=n-2$ internal moduli and one transition function for $n\ge2$, and nothing for $n=1$ (a leaf, fixed local coordinate). Uniformly, an $n$-patch leg contributes $n-1$ complex moduli for every $n\ge1$ ($n-2+1$ for $n\ge2$; $0$ for $n=1$), so
$$
d(V_{a+b+c})=(a-1)+(b-1)+(c-1)=a+b+c-3=\dim_{\mathbb C}\mathcal M_{0,a+b+c}.
\tag{3.4}
$$
Checks: $(2,1,1)$: $1$ ($V_4(\Sigma_2,\Psi,\Psi)$: one transition function, 071 C1.4's slice); $(3,1,1)$: $2$; $(2,2,1)$: $2$; $(2,2,2)$: $3$. The three transition functions of (3.4) are, in R79 C1.4, absorbed into the pants' three coordinate curves (the circles are given with their coordinates); the count is the same, since a bare pants with three prescribed circle coordinates is a rigid vertex whose three legs' coordinates are read off the glued surface. [C3.3]

*(3.5) The matching condition for $n\ge3$.* Counting is not covering. At $n=2$ the gluing family $q\mapsto Z_4^{(s)}(q)$ of two rigid $\mathcal V_3'$ maps $Q_V=\{1<|q|<e^{\sigma_V(\theta)}\}$ bijectively (a.e.) onto $\mathcal V_{0,4}$ (R80 C1.2, Proven; the star-shaped form with the cutoff $\sigma_V(\theta)$ is R80 C1.3, Numerical at $\beta=3/2$): the region of the transition function is *determined* by the requirement that the kinetic sphere's region be $\mathcal V_{0,4}$. For $n\ge3$ the analogous requirement is that the map
$$
\mathcal V'_{n+1}\times\mathcal V'_{n+1}\times Q\ \longrightarrow\ \mathcal M_{0,2n},\qquad (m_L,m_R,q)\mapsto\text{glued surface},
\tag{3.5}
$$
be a bijection (a.e.) onto $\mathcal V_{0,2n}$ for some region $Q=Q(m_L,m_R)$ of the transition function, fibred over the internal moduli, with the local coordinates of $\mathcal V_{0,2n}$ reproduced (off shell) or at least the surfaces (on shell). The dimension count (3.1) is the necessary condition $\dim(\text{source})=\dim(\text{target})$; the bijection, the shape of $Q$ (074's $\sigma_V(\theta)$ at $n=2$) and the fate of the local coordinates (074 C1.5: at $n=2$ already the fixed halves' coordinates must move with $q$ off shell) are the content of a construction that does not exist here. The sections of C2.3 enter: $Q$ is defined only together with the scale conventions of the special coordinates over $\mathcal V'_{n+1}$. [C3.4]

\subsection*{Commentary}
(3.1): the equality $d_n=n-2$ says that the $n$-patch *is* an asymmetric vertex region in $\mathcal M_{0,n+1}$, nothing smaller: an $n$-patch with fixed internal configuration is enough only at $n=2$, where $\mathcal M_{0,3}$ is a point. (3.3): the general identity is the reason the HS trees and the standard trees agree in moduli count whatever the vertex content (used in §5). (3.4): the uniform "$n-1$ per leg" rule is what makes the $n=1$ leg (a plain puncture, no transition function) and the $n\ge2$ legs (a patch, one transition function) sit in one formula. (3.5): "covering once" is the vertex condition of the standard theory (A4) transported to the two-patch presentation; at $n=2$ it holds at the level of surfaces (R80), with the local coordinates failing off shell (074 C1.5).

\subsection*{Result}
$$
\boxed{\ d_n=n-2\ \ (\text{necessary, exact}),\qquad \sum_kV_k(k-3)+E_{\rm int}=N-3\ \ (\text{every tree}),\qquad d(V_{a+b+c})=a+b+c-3\ }
$$
Two rigid patches cover the kinetic sphere's moduli only at $n=2$ (where R80 proves the covering at the level of surfaces); for $n\ge3$ each patch must be an asymmetric vertex region $\mathcal V'_{n+1}$ with $n-2$ internal moduli, and the transition function's region must be fibred over the internal moduli so that (3.5) covers $\mathcal V_{0,2n}$ once — a condition, not a construction. [C3]

\subsection*{Verification}
`C3.1-kinetic` ((3.1) for $n=1..8$, with the break leg $d_n=n-3$), `C3.2-tree-formula` ((3.3) symbolically in sympy from (3.2) for symbolic $V_3,\dots,V_8$), `C3.2-enumeration` (all valence vectors $(V_3,\dots,V_N)$ solving (3.2) for $N=4,6,8$, each checked against $N-3$; the break leg assigns $k-2$ internal moduli per vertex), `C3.3-trinion` ((3.4) on all $(a,b,c)$ with $a+b+c\le8$, break leg: $n-2$ per leg for all $n$, which fails at $n=1$). (3.5) is a stated condition; nothing to check.

## §4 Ghost number and the transition function (C4)

\subsection*{Setup}
A1–A3. $\Phi_n$ is R79's circle state, $N_{\rm gh}(\Phi_n(\Sigma_n))=2n$ (071 C1.3); $\Phi_n^{[b]}$ the patch state dressed with the Schiffer antighosts of the patch's internal moduli (071 C1.4's $b$-dressed circle states), one antighost per real internal modulus. $S$ is the total ghost number of the inserted states, $n_b$, $n_c$ the numbers of antighost and ghost insertions (036 (1.1)).

\subsection*{Derivation}
*(4.1) The dressed patch state.* A patch with $d_n=n-2$ complex internal moduli (3.1) carries $2(n-2)$ real moduli, hence $2(n-2)$ antighost insertions inside the patch (their Schiffer contours surround the ordinary punctures and cannot be moved onto the boundary circle, 071 C1.4), so
$$
N_{\rm gh}\big(\Phi_n^{[b]}\big)=2n-2(n-2)=4\qquad(n\ge2),
\tag{4.1}
$$
independent of $n$. At $n=1$ the formula reads $2-2(-1)=4$: the virtual dimension $d_1=\dim\mathcal M_{0,2}=-1$ corresponds to $-2$ antighosts, i.e. two $c$-insertions, the CKV pair $(c_0^-$ and the $c$ of $Q_B)$ of the two-punctured sphere in 036 (1.2); the actual state $\Phi_1=\Psi$ has ghost number $2$, and the ghost-number-4 object is $c_0^-Q_B\Psi$ of the kinetic term $\langle\Psi,c_0^-Q_B\Psi\rangle$ (036 (1.2): $2+2=4$, pairing with $\Psi$ to $6$) — which is why a $1$-patch is a leaf (no transition function) and not a vertex: its gluing is the kinetic term, not a plumbing. [C4.1]

*(4.2) Pairing counts.* Two dressed patch states glued by the $b_0^+b_0^-$-dressed plumbing (A2):
$$
4+4-2=6 ,
\tag{4.2a}
$$
the sphere anomaly: the kinetic sphere $p_{n,n}$ is a non-vanishing sphere correlator for every $n\ge2$, with $2n-3$ complex moduli all accounted for by antighosts ($2(n-2)$ inside each patch, $2$ on the edge). In standard sewing, a rigid pants with two external $\Psi$'s is the undressed $2$-patch state $\Phi_2(\Psi,\Psi)$, ghost number $4$ (R79 C1.3), a bra pairing with ghost number $6-4=2$, i.e. with a string field; the Feynman propagator $b_0^+b_0^-\delta(L_0^-)/L_0^+$ (ghost number $-2$) maps it to a ghost-number-2 state, a field, as it must. The HS gluing differs only in the range of the transition function, not in the ghost arithmetic:
$$
\text{standard: }\ 4\ \xrightarrow{\ b_0^+b_0^-,\ |q|\le1\ }\ 2\ \text{(a field)};\qquad\text{HS: }\ \langle\Phi_n^{[b]}|\,b_0^+b_0^-\mathcal S(q)\,|\Phi_n^{[b]}\rangle,\ 4+4-2=6 .
\tag{4.2b}
$$
[C4.2]

*(4.3) Second route: the $S-6$ calculus.* For the kinetic sphere $S=4n$, $n_c=0$ (stable for $n\ge2$), so $n_b=4n-6=2(2n-3)$, and the split by location is
$$
n_b=4n-6=\underbrace{2(n-2)}_{P_L}+\underbrace{2(n-2)}_{P_R}+\underbrace{2}_{\text{edge}} .
\tag{4.3a}
$$
For the trinion coupling with clusters $(a,b,c)$: $S=2(a+b+c)$, $n_b=2(a+b+c)-6$, split as $2(a-2)+2(b-2)+2(c-2)$ inside the patches plus $2$ per transition function of an $n\ge2$ leg, i.e. with the uniform rule $2(n-1)$ per leg ($0$ for $n=1$):
$$
n_b=2(a-1)+2(b-1)+2(c-1)=2(a+b+c)-6 .
\tag{4.3b}
$$
This is R79 C1.4's leg ghost numbers $2a-|S_A|$ summing to 6: the dressed leg $A$ has $N_{\rm gh}=2a-|S_A|$ and $|S_A|+|S_B|+|S_C|=p=2(a+b+c-3)$; in the slice with one fixed puncture per cluster $|S_A|=2(a-1)$ and the legs have ghost number $(2,2,2)$ — the "$2(n-1)$ per leg" rule of (4.3b) with the edge antighosts counted on the leg. [C4.3]

*(4.4) The transition function of the HS edge, and the $\Sigma$-propagator edge.* The HS edge is the plumbing $w_Lw_R=q$ acting on the patch states exactly as in A2 — $\mathcal S(q)$ with $b_0^+b_0^-$, 074 (1.1)–(1.3) at $n=2$ — with three differences from a propagator edge, each established at $n=2$ with R79/R80's statuses (the covering Proven, the shape of the range Numerical, the inverse in the fixed-halves model with its projector clause Conditional(PH31)) and stated by counting at $n\ge3$: (i) *range*: the integral runs over a vertex region — at $n=2$ the reversed plumbing range $Q_V=\{1<|q|<e^{\sigma_V(\theta)}\}$ (R80 C1.2–C1.3) — not over $|q|\le1$; (ii) *states*: the transported states are not level-matched (R79 C2: positional failure at every momentum), so the twist integral $\int d\theta\,e^{i\theta L_0^-}$ over a $\theta$-dependent range acts sector by sector in $L_0^-$ and does not reduce to $\delta(L_0^-)$ (074 §2: $\hat f_m(h)$ for every even $m$); (iii) *inverse*: the $\Sigma_n$ propagator $p_{n,n}^{-1}$ is not a gluing over any region — $b$-dressed gluings do not compose, and the inverse of a region integral is not the integral over the inverse region (R80 C2.3); in the fixed-halves model it is the circle's CKV pair $c_0^-c_0^+$ times the reciprocal of the region's Laplace–Fourier transform times the projector onto the circle states (R80 C2.1–C2.2, the projector clause under PH31). So the generalised tree has two kinds of edges, with the counts
$$
\begin{aligned}
&\text{gluing edge }(\Psi\text{ propagator over }|q|\le1,\ \text{or HS kinetic edge over }Q):&& \Delta d=+1,\ \ \Delta N_{\rm gh}=-2;\\
&\Sigma_k\text{-propagator edge }(p_{k,k}^{-1}):&& \Delta d=-(2k-3),\ \ \Delta N_{\rm gh}=+(4k-6),
\end{aligned}
\tag{4.4}
$$
the second line from 036 (1.3): $p_{k,k}$ has $\hat d=4k-6$ antighosts on $2k-3$ complex moduli, and its inverse has $\hat d_B=-(4k-6)$ (R39's inverse lemma, cited through R40). A composite $\mathcal V_{N_1}\,p_{k,k}^{-1}\,\mathcal V_{N_2}$ then has $(N_1-3)+(N_2-3)-(2k-3)=(N_1+N_2-2k)-3$ complex moduli and $2(N_1-3)+2(N_2-3)-(4k-6)=2(N_1+N_2-2k)-6$ antighosts: the counts of a $(N_1+N_2-2k)$-point sphere, for every $k$. At $k=2$: $\Delta d=-1$, two $c$'s, and $p_{2,2}p^{-1}p_{2,2}=p_{2,2}$ is 074 C3's telescoping ($1+1-1=1$); $\mathcal V_5p^{-1}\mathcal V_5$ has $2+2-1=3=\dim\mathcal M_{0,6}$ (074 C4, in the fixed-halves toy). At $k\ge3$ the $\Sigma_k$ edge removes the full moduli of a kinetic sphere, $2(k-2)+1$: the two patches' internal moduli and the gluing — in the atlas picture, the $\Sigma_k$ edge *contracts* a kinetic sphere, it does not add a collar; its $4k-6$ $c$'s are read as the CKV pair of the circle plus $2(k-2)$ $c$'s per patch, the duals of the patches' internal antighosts (a reading: the count fixes only the total). Only $k=2$ is established (R80, model A5); the $k\ge3$ line of (4.4) is a count. [C4.4]

\subsection*{Commentary}
(4.1): the independence of $n$ is the atlas reading of 071 C1.4's "$(2,2,2)$ in the slice with one fixed puncture per cluster": a dressed patch is a ghost-number-4 object for every $n\ge2$, the same as the undressed $2$-patch, which is why the $n=2$ case needs no dressing and why the trinion legs look alike. (4.2b): the only arithmetic difference between the standard propagator and the HS edge is none; the differences are in the range and in the level-matching projection. (4.4): the $\Sigma_k$ edge's $\Delta d=-(2k-3)$ is forced by the composite count; the $k=2$ value $-1$ agrees with R80. The reading "CKV pair plus $2(k-2)$ duals of internal antighosts" is a split consistent with the model at $k=2$ and the count at $k\ge3$, not the only one: the $k=2$ model fixes that two of the $4k-6$ $c$'s are the circle's zero modes, the count fixes only the total, and "2 circle $+$ $4k-8$ unassigned" or "2 circle $+$ $2(k-2)$ on the internal moduli of the glued configuration" are equally consistent; the per-patch assignment is a reading, not a derivation of $p_{k,k}^{-1}$.

\subsection*{Result}
$$
\boxed{\ N_{\rm gh}(\Phi_n^{[b]})=4\ (n\ge2),\qquad 4+4-2=6,\qquad n_b=4n-6=2(n-2)+2(n-2)+2,\qquad \Sigma_k\text{ edge: }\Delta d=-(2k-3),\ \Delta N_{\rm gh}=4k-6\ }
$$
The transition function of the HS edge is the standard plumbing on patch states, over a vertex region, on non-level-matched states, with an inverse that is not a gluing: the generalised tree has gluing edges and contraction edges. Established at $n=2$ with R79/R80's statuses (covering Proven, shape of the region Numerical, the inverse in the fixed-halves model with its projector clause Conditional(PH31)); counts at $n\ge3$. [C4]

\subsection*{Verification}
`C4.1-dressed` ((4.1) for $n=1..8$, with the $n=1$ virtual value; break leg: dressing with $2(n-1)$ antighosts, which gives $2$), `C4.2-pairing` ((4.2a)), `C4.3-S6` ((4.3a) and (4.3b) for all $(a,b,c)$, $a+b+c\le8$, against $S-6$; break leg: $2(n-2)$ per leg for all $n$), `C4.4-sigma-edge` (composite moduli and antighost counts for $N_1,N_2\le8$, $k\le3$, against the $(N_1+N_2-2k)$-point sphere; break leg: $\Delta d=-1$ for all $k$, which fails at $k=3$). Statements (i)–(iii) are cited from R79/R80, not re-checked.

## §5 Limits and consistency (C5)

\subsection*{Setup}
A3–A5, C2–C4.

\subsection*{Derivation}
*(5.1) $n=1$.* The $1$-patch is a disc with one puncture at $u=0$ and local map $f_1$: $\Phi_1=U_{f_1}$, the identity for $f_1=\mathrm{id}$ (R79 C6). It has $d_1=-1$ virtual moduli, carries no transition function of its own (A5: a leaf), and the ghost arithmetic (4.1) at $n=1$ is 036 (1.2)'s CKV count. Glued to a vertex by its fixed local coordinate it is the standard external leg; glued to another $1$-patch by $w_1w_2=q$ over $|q|\le1$ with $b_0^+b_0^-$ it is the standard propagator, the $\mathbb C^*$ orbit of 036 (1.2) half-integrated. Nothing of §2–§4 is new at $n=1$: C2's redundancy count gives $2\cdot1+1-4=-1=\dim\mathcal M_{0,2}$ (virtual), C3's (3.1) gives $2d_1+1=-1=2n-3$ (virtual, consistent), and C4.1 gives the two $c$'s. [C5.1]

*(5.2) $n=2$.* The rigid $2$-patch is R2's $\mathcal V_3'$ (A3, 074 A4): C2.3's reading circle is 074 A4's $s$-circle $|w_1|=r$; C3.1 is the count $1=1$ with the covering supplied by R80 C1.2 ($Q_V\to\mathcal V_{0,4}$ bijective a.e., Proven) and the region's shape by R80 C1.3 (Numerical, $\beta=3/2$); C4.1 needs no dressing ($d_2=0$), $\Phi_2$ has ghost number 4 (071 (A.5)); C4.2's gluing is 074 (1.1)–(1.3), the pairing $\langle\Phi_2^{(34)}|\,b_0^+b_0^-\,e^{-sL_0^+}e^{i\theta L_0^-}\,|\Phi_2^{(12)}\rangle$ over $Q_V$, i.e. 071 (A.9) at $(2,2,0)$ with the pants degenerated to the annulus; C4.4 (i) is 074 (1.4), (ii) is 071 C2 with 074 §2's $\hat f_m$, (iii) is 074 C2.1–C2.3. The off-shell qualification carries over verbatim: on shell $p^{\rm circ}=p_{2,2}$ (074 C1.4), off shell the halves' local coordinates must move with $q$ (074 C1.5), so the rigid $2$-patch picture is exact on shell and a model off shell. [C5.2]

*(5.3) HS trees against standard trees.* Vertices of the HS Feynman expansion in the atlas picture: trinion couplings $V_{a+b+c}$ (a pants with three patches) and, since the kinetic form with one leg on $\Psi^{\otimes k}$ is a coupling ($V_4(\Psi^4)=p_{2,2}(\Psi^2,\Psi^2)$ exactly), kinetic spheres with external $\Psi$'s on both patches; edges: $\Psi$ propagators, HS kinetic edges, $\Sigma_k$ contraction edges (4.4). By (3.3) every tree of patches and gluing edges has $N-3$ moduli, and by (4.4) a contraction edge between two $k$-patch legs subtracts exactly the $2k-3$ moduli of the kinetic sphere it contracts; so every HS diagram with $N$ external $\Psi$'s has $N-3$ complex moduli and $2N-6$ antighosts, as does every standard diagram.
$$
\begin{array}{lll}
N=4:& \text{standard } \mathcal V_4\ (1);\ \ \mathcal V_3\!-\!\mathcal V_3\ (0+0+1);&
\text{HS } p_{2,2}(\Psi^2,\Psi^2)=\mathcal V_3'\!-\!\mathcal V_3'\ (0+1+0);\ \ p_{2,2}\,p_{2,2}^{-1}\,p_{2,2}\ (1+1-1);\\
N=6:& \mathcal V_6\ (3);\ \mathcal V_4\!-\!\mathcal V_3\!-\!\mathcal V_3\ (1+2);\ \mathcal V_3^{\,4}\ (3);&
p_{3,3}(\Psi^3,\Psi^3)=\mathcal V_4'\!-\!\mathcal V_4'\ (1+1+1);\ \ V_{2+2+2}(\Sigma_2^3)\to\text{pants}+3\,\mathcal V_3'\ (3);\ \ \mathcal V_5\,p_{2,2}^{-1}\,\mathcal V_5\ (2+2-1).
\end{array}
\tag{5.1}
$$
All entries equal $N-3$; they are spot-checked by `C5.3-hs-trees` (valence vectors and single $k=2$ contraction edges at $N=4,6$; the general statement rests on (3.3) and (4.4)). What the count does *not* say: that the regions of the HS diagrams cover $\mathcal M_{0,N}$ once (this is the covering question, R80 C1.2 at $N=4$, 074 C4's signed density at $N=6$ in the toy, open in general), nor that the $\Sigma_k$ edge at $k\ge3$ has the structure of (4.4)'s reading. [C5.3]

\subsection*{Commentary}
(5.1): the $n=1$ limit is the consistency check that the uniform rules of §3–§4 (a leaf carries $n-1=0$ moduli, the virtual $d_1=-1$ pairs with two $c$'s) reproduce the standard propagator and external leg without special-casing. (5.2): every statement of §2–§4 at $n=2$ is a citation of 071/074; nothing is re-derived. (5.3): the count is tree-independent by (3.3), which is why it cannot distinguish the HS expansion from the standard one — the distinction lives in the regions and in the local coordinates.

\subsection*{Result}
$n=1$ is the standard picture, $n=2$ is 071/074 verbatim (equations named above), and the HS diagrams have the moduli and antighost counts of the standard diagrams at every $N$, with the explicit table (5.1) at $N=4,6$. [C5]

\subsection*{Verification}
`C5.1-n1` (the three virtual counts at $n=1$), `C5.3-hs-trees` (a spot check: valence vectors, as in `C3.2-enumeration`, and two-vertex composites with a single $k=2$ contraction edge at $N=4,6$, against $N-3$ — no $k=3$ contraction, no mixed gluing/contraction trees, no chains; break leg: a contraction edge counted as $\Delta d=0$; the general statement is proven in the text by (3.3) and (4.4) and does not rest on it). Scope of the literal-arithmetic checks: `C3.1-kinetic`, `C4.1-dressed`, `C4.2-pairing`, `C4.3-S6`, `C5.1-n1` and the table part of `C5.3-hs-trees` verify that the record's formulas evaluate to the numbers written next to them; their break legs are a different formula giving a different number. They are transcription checks of the arithmetic and carry no independent weight; the genuine enumerations against a formula include `C1.1-trivalent`, `C3.2-enumeration`, `C3.2-tree-formula` and `C4.4-sigma-edge`.

## §6 Result, answer, self-review, proposed ledger entry

### 6.1 Answer (in words, no IDs)

In ordinary closed string field theory a sphere with $N$ punctures, in the region of moduli space covered by Feynman diagrams, is described by $N$ coordinate discs around the punctures and $N-2$ three-punctured spheres, joined along $N-3$ collars by the transition functions $w_aw_b=q$; the $N-3$ complex moduli are the $q$'s, each collar carrying the two antighosts of its dilation and rotation. At genus zero a global coordinate exists and the three-punctured spheres are not needed as charts, but they remain as vertices: their three local coordinates are what fix the coordinates at the punctures. What the atlas really carries is the $N$ local coordinates at the punctures and the clustering of the punctures into collars. The position of each collar circle and the coordinates used on the three-punctured spheres are bookkeeping.

An $n$-puncture patch is a chart with $n$ puncture discs inside it: as far as moduli and antighosts go, the same thing as the chart of a higher vertex with $n+1$ punctures, one of whose legs is distinguished – it carries the chart's own coordinate, its transition function runs over a vertex-type range, and the state read on it is not level-matched. What is genuinely new beyond these three features is that the patch's region with its local coordinates need not be the symmetric vertex region – whether the symmetric region with one leg's coordinate made special will do is open – and that the propagator of the auxiliary field acts on it as a contraction rather than a gluing (both below). As a surface it is an $(n+1)$-punctured sphere whose extra puncture is the boundary of the chart, with the coordinate there fixed exactly; the state read on the boundary circle is the state obtained from the $n$ inserted states by their repeated operator product in the chart coordinate, with the total momentum in the zero mode and the relative momenta in the level content. Two such patches joined along their boundary circles by the usual transition function $w_Lw_R=q$ present the $2n$-punctured sphere of the kinetic term of the auxiliary field $\Sigma_n$. The presentation is redundant by four complex parameters: the two centres of the charts, the normalisation of a chart coordinate against $q$, and the position of the circle in the collar together with the relative rotation of the two coordinates; this last freedom is the seam: moving the circle re-splits the surface between the two patches without changing it, and the two circle states change by opposite dilations that cancel in the pairing.

The counts decide what the patch must contain. Two rigid patches and one transition function give one complex modulus; the $2n$-punctured sphere has $2n-3$. They agree only for $n=2$, where the two patches are the asymmetric cubic vertex and the region of the transition function is determined: the surfaces of the quartic vertex region are reached once, on shell exactly up to one measure identity argued by hand, off shell in a model with fixed halves; the region is the reversed plumbing range $1<|q|<e^{\sigma(\theta)}$ with an angle-dependent cutoff, computed numerically. For $n\ge3$ the count forces each patch to carry $n-2$ complex internal moduli, the full moduli of an $(n+1)$-punctured sphere: the $n$-patch is not a rigid surface but an asymmetric vertex region, with its own section of local coordinates, and the transition function's region must be fibred over the internal moduli so that the three together cover the vertex region of the kinetic sphere once. This is a necessary condition on an object that has not been constructed here, not a construction; the one case where the covering is proven is $n=2$, at the level of surfaces.

In this picture the building block attached to each cluster is the asymmetric vertex region with one special puncture; the three-punctured sphere survives twice, as the rigid patch at $n=2$ and as the bare sphere carrying the trinion couplings. The moduli sit in two places: inside each patch (its internal moduli, with one antighost per real modulus, whose contours surround the patch's punctures and cannot be moved to the boundary circle) and in the transition functions (one complex modulus each, with the circle's two antighost zero modes). The dressed state on a patch boundary has ghost number four for every $n\ge2$: the $2n$ of the inserted fields less the $2(n-2)$ antighosts of the internal moduli; two of them joined by a transition function give the sphere's six. The trinion couplings of the auxiliary fields are a rigid three-punctured sphere with three patches attached, each patch leg contributing $n-1$ complex moduli (its $n-2$ internal ones and its transition function; a single puncture contributes none), and the count closes for every triple of cluster sizes. For any tree of such vertices the number of moduli is the number of punctures minus three, exactly as for the ordinary trivalent trees, so the counting cannot distinguish the two expansions; the difference lies in the regions and in the local coordinates.

The transition functions themselves are the ordinary plumbing, acting on the patch states, with three differences. Their range is a vertex region rather than the propagator's unit disc. The states they transport are not level-matched, so the twist integral acts sector by sector and does not reduce to the level-matching projector. And the propagator of the auxiliary field is not a transition function at all: it is not a gluing over any region of the plumbing parameter. At $n=2$, in the model with fixed halves, it is the pair of ghost zero modes dual to the circle's dilation and rotation, times the reciprocal of the region's transform (the Laplace–Fourier transform, in the plumbing variables $s$ and $\theta$, of the indicator function of the region, taken separately in each sector of $L_0^\pm$), restricted to the states the circles produce – the restriction resting on an assumption about the circle map on fields of unbounded level. The generalised tree therefore has two kinds of edges: gluing edges, which add one complex modulus and two antighosts, and contraction edges, which remove the whole kinetic sphere they sit on — $2n-3$ complex moduli, $4n-6$ antighosts replaced by as many ghosts (the inverse of a form with $4n-6$ antighost insertions carries $4n-6$ ghost insertions instead); at $n=2$ this is proven for two copies of the kinetic sphere, where the two regions telescope into one; between two quintic vertices, in a toy model with fixed halves and under the same assumption on the circle map, the composite is a signed density whose neck measure collapses to a single region only when one neck width equals the kinetic one, and at $n\ge3$ it is a count.

What is established: the atlas counts, the redundancy of the two-patch presentation and the seam, the ghost arithmetic, and all of the $n=2$ statements, each with the standing it has where it was derived: the covering of the surfaces proven, the shape of the region numerical, the inverse a model statement off shell. What is a proposal: the $n$-patch as an asymmetric vertex region for $n\ge3$, with the covering condition on its transition function, and the reading of the auxiliary propagator at $n\ge3$ as the duals of the patches' internal antighosts together with the circle's zero modes.

### 6.2 Scope and regime of validity

Genus zero, tree level, flat background (A1). Every claim of §1–§5 is a count, a definition-level statement about an atlas, or a citation of R79/R80. Rigid patch at $n=2$ with the R2 family: covering proven, region's shape numerical, exact on shell up to one measure identity argued by hand, a model (fixed halves) off shell; the inverse's projector clause conditional on PH31. Patch with internal moduli: an object whose existence is not established here; (3.1), (3.5), (4.1), (4.4) are necessary conditions on it. The HS Feynman expansion's covering of $\mathcal M_{0,N}$ is not addressed (the counts are tree-independent by (3.3) and cannot address it). Not addressed either, and the first thing C3.4's condition would be tested on: whether $\mathcal V'_{n+1}$ can be taken to be the symmetric $\mathcal V_{0,n+1}$ with one leg's local coordinate replaced by a Möbius special coordinate (TODO §2's candidate, asymmetric vertices built from higher-order symmetric vertices). Hypotheses are inherited only through citations: PH10 and PH5 through R79's conditional clauses (071 C4.4, C5.2 — not used by any count here; C4.4 (i)–(ii) hold on shell, or at finite level in the model; the off-shell level sum on the reversed range is PH10's domain, 071 C4.4), PH31 through R80's inverse (the projector clause of C4.4 (iii), cited as R80 states it). No count of this record depends on a hypothesis.

### 6.3 Self-review (research skill §5)

1. *Objective versus literal task.* The objective is a paragraph in the language of ordinary SFT (§6.1) resting on counted claims; delivered. The literal task's "generalisation" is answered as a necessary-condition statement, which is what the brief asked for ($\mathcal V'_{n+1}$ not constructed).
2. *Weakest step.* C2.1's identification of the redundancy group as $\mathrm{PSL}(2,\mathbb C)\times\mathbb C^*_\kappa$ (seam inside the first factor) rests on reading off a new triple from an arbitrary Möbius image of the configuration — established by the argument of (2.2)–(2.4) (the action of $(g,\kappa)$ written out); `C2.1-redundancy` only confirms the Möbius invariance of cross-ratios at random points and is not independent evidence; and C4.4's $k\ge3$ line, which is a count forced by the composite's dimension, with no model behind it: marked as such everywhere.
3. *Not checked.* The covering (3.5) at $n\ge3$ (no object to check); the operator identity (2.4) (R79 C2.1's covariance, cited); the off-shell dressing of the patch states by the motion of local coordinates with the internal moduli (074 C1.5 at $n=2$; for $n\ge3$ the dressing would add antighost contours inside the patch without changing the count, as 074 (1.5) shows at $n=2$).
4. *What a stronger physicist would find.* That the uniform rule "$n-1$ moduli per leg" (3.4) and the ghost number 4 of every dressed patch state (4.1) say the same thing — a patch leg of any size looks like a two-puncture leg — which is the structural reason the trinion couplings factorise through a bare pants (R79 C1.4), and which suggests that the whole HS tower could be presented as cubic vertices on bare pants whose legs carry ghost number 2 (R79 C1.4's $(2,2,2)$, the record's (4.3); the 4 is the dressed patch state before its edge's $b_0^+b_0^-$); the record states this as an observation in §4's commentary and does not develop it.

### 6.4 Proposed ledger entry

**R? — The $n$-puncture patch in the atlas picture: counts and the generalised tree [Proven (counts); the $n\ge3$ object is a necessary-condition statement]**

- Source: `agent/derivations/077-npatch-atlas.md` C1–C5, §1–§5; `codes/verify-npatch-atlas.py` 27/27 PASS, seed 20261004 (14 checks + 13 break legs).
- Scope: genus zero, tree level; counts and atlas-level statements; $n=2$ statements cited from R79/R80 (fixed-halves model off shell); $\mathcal V'_{n+1}$ for $n\ge3$ not constructed — (3.1), (3.5), (4.1), (4.4) are necessary conditions on it.
- Statement: a genus-zero Feynman region is $N$ discs, $N-2$ rigid pants, $N-3$ transition functions carrying the moduli and antighosts (C1); an $n$-patch is an $(n+1)$-punctured sphere whose special coordinate is $1/u$ for a global coordinate $u$, hence determined by the scale and centre of $u$ (its 2-jet), two patches glued by one transition function present the $2n$-punctured sphere with redundancy $\mathrm{PSL}(2,\mathbb C)\times\mathbb C^*_\kappa$ of complex dimension 4 — the Möbius freedom of the global coordinate, whose dilation subgroup fixing the two chart centres (with $q$ fixed) is the seam, and the rescaling of one special coordinate compensated in $q$ (C2); rigid patches cover the kinetic sphere's moduli only at $n=2$, and for $n\ge3$ each patch must carry $d_n=n-2$ internal moduli with the transition function's region fibred over them (C3); the dressed patch state has ghost number 4 for every $n\ge2$, $4+4-2=6$, and the generalised tree has gluing edges ($+1$ modulus, $-2$ ghost number) and $\Sigma_k$ contraction edges ($-(2k-3)$, $+(4k-6)$) (C4); $n=1$ and $n=2$ limits and the $N=4,6$ tables (C5).
- Status: C1, C2, C3.1–C3.3, C4.1–C4.3, C5 — Proven (counts and the $n=1$, $n=2$ identifications, C5.2's cited $n=2$ content keeping R79/R80's statuses; the script is a transcription check of the arithmetic, its genuine enumerations including `C1.1-trivalent`, `C3.2-enumeration`, `C3.2-tree-formula`, `C4.4-sigma-edge`, and its C2 checks confirming only the Möbius invariance of cross-ratios); C3.4 and C4.4's $k\ge3$ line — necessary conditions on an unconstructed object (not results about it); C4.4 (i)–(iii) at $n=2$ — cited from R79/R80 with their statuses (R80's projector clause Conditional(PH31)).
- Origin: the $n$-puncture patch question of 2026-10-04 (the $n$-puncture patch in the atlas / transition-function picture); the paragraph for the paper is §6.1.

## Fix pass (critic iteration 1)

Brief `agent/briefs/active-computator-077-fix-20261004T104000.md`; findings of `agent/reports/critic-077-20261004T101800.md`, applied in the brief's order. No node statement with dependents changed in substance (see each line); no count, check or number changed.

- **#3** (redundancy group mislabelled): C2 node, (2.3) explicit decomposition, (2.3) commentary, §2 Result, §6.4 Statement, §6.1 para 2, §6.3 item 2 — group rewritten as $\mathrm{PSL}(2,\mathbb C)\times\mathbb C^*_\kappa$ with the action $(g,\kappa)$; the seam is the dilation subgroup of the Möbius factor ($q$ fixed), not a direct factor; the former $\mathbb C^*_\mu$ ($=(g_{\mu^{-1}},\kappa=\mu)$, a mixture) removed; §6.1 now counts four parameters (centres, normalisation against $q$, circle position with relative rotation). C2: statement wording changed (group structure), count 4 and dependents (C2.1–C2.3, C5.1) unchanged.
- **#7** (Möbius form of the special coordinate): A3 gains the clause that the Möbius form is the definition of a chart and that the counts (3.1), (4.1), (4.4) do not depend on it; C2 node, §2 Result, §6.4 Statement read "special coordinate $1/u$ for a global $u$, determined by its 2-jet"; (2.1) commentary says "fixed to second order" means "within the Möbius class". Justification-level change only.
- **#6** ((2.4) separating-circle range inverted): (2.4) parenthetical now reads $|q|r_R<|w_L|<1/r_L$, non-empty on the reversed range iff $|q|<1/(r_Lr_R)$ ($4\beta^2$ at $n=2$), consistent with C2.3's $|q|/2\beta<r<2\beta$. Not load-bearing for any count; no node statement changed.
- **#4** (uncited dependencies): C4.1 cites C3.1 ($d_n=n-2$); C4.3 cites C3.3 (uniform $n-1$ per leg) and C4.1 (dressed count); C4.4 cites R40 (036 (1.3)–(1.4)) and R39 (inverse lemma). Justification-only change; no statement changed.
- **#8** ("only split" not shown): (4.4) body now says the $4k-6$ $c$'s "are read as" CKV pair plus $2(k-2)$ per patch ("a reading: the count fixes only the total"); §4 Commentary says "a split consistent with", naming the two alternative splits. The C4 node carries no reading clause (only the totals), so no node statement changed; §6.1 para 6 already lists the reading as a proposal.
- **#11** (PH10's domain): C4.4 node, the claim tree's `Hypotheses in force:` line and §6.2 now state that C4.4 (i)–(ii) are read on shell (R80 C1.4) or at finite level in the model, the off-shell level sum of $\Phi_2$ on the reversed range being PH10's domain (071 C4.4). Scope clarification; no statement changed.
- **#1** (statuses of the $n=2$ inputs dropped): §6.1 paras 3, 5, 6 rewritten with the critic's replacement text (covering proven, shape numerical, on-shell exactness up to one argued measure identity, off shell a fixed-halves model, the inverse at $n=2$ only, in the model, its restriction resting on an assumption about the circle map at unbounded level); the same statuses carried into C3.4, (3.5), (4.4) body, C4.4, §4 Result, (5.2), §6.2. §6.4 Status already correct. C3.4 and C4.4: justification/status wording only; their statements (a condition at $n\ge3$, counts at $n\ge3$) unchanged, dependents C5.2, C5.3 unaffected.
- **#2** (telescoping overstated): §6.1 para 5's contraction-edge sentence now carries R80 C4's trichotomy (telescoping proven for two kinetic spheres; between two quintic vertices, in the fixed-halves toy (status added, R80 A5′), a signed density collapsing to one region only when one neck width equals the kinetic one). The body (4.4) was already correct; no node changed.
- **#5** (patch as "a chart of a new kind" / pants "replaced"; the later duplicate "not level-matched" clause of para 2 dropped): §6.1 para 1 gains "not needed as charts, but they remain as vertices: their three local coordinates fix the coordinates at the punctures" (the (1.3) commentary point); para 2 opens with the critic's sentence (the patch is, for moduli and antighosts, the chart of an $(n+1)$-point higher vertex with one distinguished leg: chart coordinate, vertex-type range, non-level-matched state) plus one sentence assembling the remaining differences already in the record (asymmetric region, contraction edge); para 4 opens with the critic's sentence (pants survive twice: rigid patch at $n=2$, bare sphere of the trinion couplings); §6.2 names the open test case ($\mathcal V'_{n+1}$ as the symmetric $\mathcal V_{0,n+1}$ with one leg's coordinate made Möbius special, TODO §2). No node changed.
- **#9** (ghost number four at $n=1$): §6.1 para 4 "whatever $n$ is" → "for every $n\ge2$" (C4.1 already states $n\ge2$; at $n=1$ the 4 is the virtual count).
- **#12** (undefined terms in §6.1 para 5): "the region's transform" defined in one parenthesis (Laplace–Fourier transform in $(s,\theta)$ of the region's indicator, sector by sector in $L_0^\pm$); "antighosts replaced by as many ghosts" explained in one parenthesis (the inverse of a form with $4n-6$ antighost insertions carries $4n-6$ ghost insertions).
- **#10** (verification scope): `[check: C5.1-n1]` tag added to C5.1; §2 Verification states that `C2.1-redundancy`, `C2.2-seam` are tautological for C2 (Möbius invariance of cross-ratios) and that C2.1–C2.2 rest on the argument of (2.2)–(2.4); §5 Verification calls `C5.3-hs-trees` a spot check (with what it does not enumerate) and names the literal-arithmetic checks as transcription checks; (5.3) body "enumeration over all HS vertex contents" → "spot-checked"; §6.3 item 2 no longer cites `C2.1-redundancy` as evidence; §6.4 Status reads "Proven (counts; the script is a transcription check of the arithmetic …)". No check added or removed; script re-run: 27/27 PASS (14 checks + 13 break legs, seed 20261004), unchanged.
- **Notes**: §6.3 item 4 reworded (the pants legs carry ghost number 2, R79 C1.4's $(2,2,2)$; 4 is the dressed patch state before its edge's $b_0^+b_0^-$); §1 Setup cites the standard atlas (Zwiebach 1993, hep-th/9206084; Erbin 2023, Feynman-region section) as the missing-reference note suggests. The notes on A5's leaf rule and on (2.4)'s operator form required no edit.

Dependents of changed nodes: C2 (wording of the group structure; count 4 unchanged) → C2.1–C2.3, C5.1, C5.2, C6 still hold; C3.4, C4.4 (status wording, citations) → C5.2, C5.3, C6 still hold; C4.1, C4.3 (citations only) → C4.2, C4.4, C5.1 still hold; C5.1 (check tag only). Restatements updated in §2/§3/§4 Results, §6.1–§6.4. Open gaps: none.

## Residues of the confirmation pass (critic iteration 2), applied by the orchestrator

- #R1 (2.5): stale $\mathbb C^*_\lambda$ label → the group $G$ of (2.3), $\mathbb C^*_\kappa$ fixed so $q$ unambiguous.
- #R2 §6.1 para 5: the quintic-composite clause now carries PH31 ("under the same assumption on the circle map").
- #R3 §6.1 para 2: "the region of the patch is asymmetric, not the symmetric vertex region" → need not be the symmetric region; whether the symmetric region with one leg's coordinate made special will do is open.
- #R4 §6.4 Status: C5's cited $n=2$ content keeps R79/R80's statuses.
- #N2 §4 Commentary: "whatever it contains" → for every $n\ge2$.
