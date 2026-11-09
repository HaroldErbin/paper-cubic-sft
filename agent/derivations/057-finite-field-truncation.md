# 057 — Finite-field truncation of the cubic theory, part A: the algebra of the two-field and five-field models

Brief: `agent/briefs/active-computator-truncation-a-20260926T045500.md` (Task 12a).
Script: `codes/verify-truncation-structure.py` (log `agent/scratch/truncation-a-run2.log`; run 1 superseded).
Fix pass: `agent/briefs/active-computator-057-fix-20260926T064000.md` after `agent/reports/critic-057-20260926T061000.md`.
Part B (§4, nodes C4.x): `agent/briefs/active-computator-truncation-b-20260926T100000.md` (Task 12b); checks `C4.*` in the same script, log `agent/scratch/truncation-b-run1.log`.

## Status

Complete after fix pass 1 (critic-057 findings applied: C1 two $W_6$ definitions, new nodes C2.9 fold and C3.6 $W_6^{(\mathcal S)}$, C2.5 withdrawn to a remark, interpretation and limits, check labels = node IDs); script 45/45 PASS, exit 0, log `agent/scratch/truncation-a-run2.log`. Next: narrow critic confirmation, then promotion; part B (see `## Next`).

2026-09-26: confirmation node check (`critic-057-confirm-20260926T065500`) — all nodes hold; six wording edits applied; promoted to ledger R61.

Part B (2026-09-26, brief `computator-truncation-b-20260926T100000`): complete — §4 (table, H1, components, absorption, theorem C4.5, verification), tree nodes A4, H1, C4–C4.5; script 81/81 PASS (36 new C4.\* checks), exit 0, log `agent/scratch/truncation-b-run1.log`. §1–§3 and the R61 content unchanged. Next: critic pass on §4 (C4 nodes), then promotion (new row + PH for H1); Task 13 uses §4.3 *Scope and interpretation*.

Part B fix pass 1 (2026-10-01, brief `computator-057-partB-fix-20261001T010500`, after `critic-057-partB-20260930T233100`: all nodes hold, 9 minor, 5 notes): all mechanical findings applied (l. 383 order, theorem (c) and hypothesis wording, momentum sentence, $\mathbb Z_N$ correction, A4 caveat, counts 81/81 and 11 `-break` labels = 7 + 4, $D=0$, sourcing chain, final PH28 entry and row). No node statement changed except wording in A4, H1, C4.3.1, C4.5; justifications unchanged; script not re-run. Next: narrow confirmation, then promotion as a new row with PH28.

## Task and objective

**Literal task.** Define a field-content truncation of the cubic theory, work out the $(t,\sigma)$ model through the sextic order and the five-field model $(t,d;\sigma_{TT},\sigma_{TD},\sigma_{DD})$ at quartic and quintic order, and state/check the general exactness theorem with its first deviation.

**Objective.** Objective 2(a) (decision 2026-09-26): solutions of the cubic EOM in a finite truncation and their relation to the tachyon-vacuum computations of the nonpolynomial theory. Part A fixes the algebra: where the truncation is exact, what it adds beyond, and where it degenerates.

## Conventions

- Ledger notation: $V_n$ totally symmetric, $\Sigma\equiv\Sigma_2$, $P=\Psi^{\otimes2}$, $g\equiv g_s$, coefficient $g^{n-2}/n!$ on $V_n$. Harold's notation: $\mathcal V_4(A_1,\dots,A_4)=\langle A_1\otimes A_2,p_{2,2}(A_3,A_4)\rangle$, so $V_4(\Sigma,\Sigma)=\langle\Sigma,p_{2,2}\Sigma\rangle$ and $p_{2,2}=m_2=G_2^{-1}V_4$ (reading map §1, line 22); $V_n\leftrightarrow\mathcal V_n$ throughout.
- Actions (shared terms $\tfrac12V_2(\Psi^2)+\tfrac g{3!}V_3(\Psi^3)$ written once as $A(\Psi)$):
  - $S_2=A-\tfrac{g^2}{4!}V_4(\Sigma,\Sigma)+\tfrac{2g^2}{4!}V_4(\Sigma,P)$ (R1);
  - $S_3=S_2+\tfrac{g^3}{5!}V_5(\Sigma,\Sigma,\Psi)$ (R17), $K_\Psi=V_4-\tfrac g5V_5(\cdot,\cdot,\Psi)$, $v=V_5(\cdot,P,\Psi)$;
  - $S_4=S_3+\tfrac{g^4}{6!}W_6(\Sigma^3)$, $W_6=V_6-\tfrac65\mathcal C$ (R19), $\mathcal C(P,P,P)=vV_4^{-1}v$ with the **full** $V_4^{-1}$ on $\mathrm{Sym}^2\mathcal H_0$ ("full-$\mathcal C$ vertex"); the $\mathcal S$-consistent alternative $W_6^{(\mathcal S)}=V_6-\tfrac65\mathcal C_{\mathcal S}$ is defined in §1.
- Target (nonpolynomial theory): $S^{(n)}_{\rm eff}(\Psi)=A(\Psi)+\sum_{k=4}^n\tfrac{g^{k-2}}{k!}V_k(\Psi^k)$.
- Ghost-number conventions: the project conventions; C1 (`knowledge/conventions.md`) not needed here (all fields Grassmann-even, physical grading).

## Claim tree

- **A1** $\mathcal H_0$ is replaced by a finite-dimensional real space $\mathcal H$ (algebraic layer, as in R17/R19/R26); $V_n$ are totally symmetric real tensors; all fields Grassmann-even.
- **A2** $V_4$ restricted to the auxiliary subspace $\mathcal S$ is invertible (for $\mathcal S=\mathrm{Sym}^2\mathcal U$: $\det V_4\vert_{\mathcal S}\neq0$); where the full inverse is used, $V_4$ is invertible on $\mathrm{Sym}^2\mathcal H$ (the R13 quotient taken as a restriction to a complement).
- **A3** The action coefficients are those of R1, R17, R19 verbatim (Conventions above).
- Hypotheses: none declared. PH14 scopes R19's exclusion (why $W_6$ must be dressed), not the identities used here.
- **C1** A field-content truncation $(\mathcal U,\mathcal S)$ of the cubic theory is the restriction of $S_n$ with $V_2,\dots,V_5$ unchanged and $W_6$ taken either as the full-$\mathcal C$ vertex or as the $\mathcal S$-consistent $W_6^{(\mathcal S)}$ (two definitions, §1); it has an auxiliary axis $\mathcal S$ with no counterpart in the worldsheet-level truncation of the nonpolynomial theory, with which it shares $\mathcal U$ and the vertex order. [by A1–A3, C1.1, C1.2; block: §1]
  - **C1.1** $\mathcal S$ must contain $\mathrm{Sym}^2\mathcal U$ (Veronese closure) for quartic-order exactness; a Veronese-incomplete $\mathcal S$ fails generically (non-generic exceptions exist since $V_4$ is indefinite). [by C3.1] [check: C3.1-sym, C3.1-generic]
  - **C1.2** Under A2, the $\ker V_4$ quotient is replaced by restriction to $\mathcal S$; the choice of complement matters exactly when $V_5$ does not annihilate $\ker V_4\vert_{\mathcal S}$ (R38's question, not settled here). [by A2, R38; block: §1]
- **C2** $(t,\sigma)$ model: at $S_3$, $\sigma_*=V_4t^2/(V_4-\tfrac g5V_5t)$ and $V_{\rm eff}$ is the rational function (2.7), equal to $S^{(5)}_{\rm eff}+\tfrac{g^4}{600}V_5^2t^6/K$; simple pole at $t_{\rm pole}=5V_4/(gV_5)$ with no finite saddle there (an $S_3$ statement); at $S_4$ two branches, the perturbative one giving (2.13), which end at a fold where $W_6V_4>0$. [by C2.1–C2.4, C2.6–C2.9]
  - **C2.1** $\sigma_*$ (2.6), identical to R17's $\Sigma_*$. [by A3, R17; eq. (2.6)] [check: C2.1]
  - **C2.2** $V_{\rm eff}$ closed form (2.7) and R17 form (2.8). [by C2.1; eq. (2.7)–(2.8)] [check: C2.2]
  - **C2.3** Expansion: target through $t^5$, then the geometric tail starting with $\tfrac{g^4}{600}V_5^2t^6/V_4$. [by C2.2; eq. (2.9)] [check: C2.3]
  - **C2.4** At $S_3$: pole (2.10); at $t_{\rm pole}$ the $\sigma$-EOM is violated (no saddle, no degenerate branch in this model); every joint critical point is a critical point of $V_{\rm eff}$, at most three nontrivial. [by C2.2; block: §2 Pole, Joint critical points] [check: C2.4-pole, C2.4-nosaddle, C2.4-residue, C2.4-count]
  - **C2.5** ~~With $\dim\mathcal S\ge2$ a degenerate branch is non-generic~~ [withdrawn: a counting remark, not a claim; kept as the Remark after §2 Result (Task 14 seed)]
  - **C2.6** $S_4$: quadratic $\sigma$-EOM (2.11), perturbative branch (2.12), non-perturbative branch $g^2\sigma_+\to20V_4/W_6$. [by A3, R19; eq. (2.11)–(2.12)] [check: C2.6]
  - **C2.7** For the full-$\mathcal C$ vertex: $V^{(4)}_{\rm eff}=S^{(6)}_{\rm eff}+\tfrac{g^4}{600}(V_5^2/V_4-\mathcal C_{TT})t^6+O(g^5)$; matched when $\mathcal U=\mathcal H$. [by C2.6, R19; eq. (2.13)] [check: C2.7, C2.7-full (corollary of C2.7), C2.7-R19]
  - **C2.8** Everything is $g$-independent in $(\tau,s)=(gt,g^2\sigma)$, exactly at $S_3$ and $S_4$: pole, fold, cubic tachyon vacuum and $\sigma_+$ at the same field scale $\tau=O(1)$, where matching of Taylor coefficients in $g$ carries no accuracy statement. [by A3; block: §2 Scaling, Interpretation] [check: C2.8]
  - **C2.9** $S_4$ singularity structure: the $S_3$ pole is replaced by a fold at $K(t)^2=\tfrac{g^2}5W_6V_4t^2$, $\tau_{\rm fold}=5V_4/(V_5\pm\sqrt{5W_6V_4})$, real iff $W_6V_4>0$; at $t_{\rm pole}$ a finite real saddle exists iff $W_6V_4<0$. [by C2.6; block: §2 Fold] [check: C2.9-fold±, C2.9-pole]
- **C3** For $\mathcal S=\mathrm{Sym}^2\mathcal U$, $A=V_4\vert_{\mathcal S}$ invertible: exact at quartic order; formally matched (Taylor coefficients) through $O(g^3)$ at $S_3$; truncated feedback $\tfrac{g^4}{600}v_S^\top A^{-1}v_S$; at $S_4$ with the full-$\mathcal C$ vertex the deviation is $-\tfrac{g^4}{600}w^\top M^{-1}w$, with $W_6^{(\mathcal S)}$ it is zero at $O(g^4)$. [by C3.1–C3.6]
  - **C3.1** Quartic exactness (3.1), five-field and general. [by A2, A3; eq. (3.1)] [check: C3.1-sym, C3.1-generic]
  - **C3.2** Quintic: (3.2)–(3.3). [by C3.1, R17; eq. (3.2)–(3.3)] [check: C3.2, C3.2-exact]
  - **C3.3** Schur formula (3.4)–(3.5); $w^\top M^{-1}w\neq0$ for generic tensors only (for the real vertices $w$ may vanish by selection rules: Task 13). [by A2; eq. (3.4)] [check: C3.3]
  - **C3.4** For the full-$\mathcal C$ vertex: sextic deviation (3.6). [by C3.2, C3.3, R19; eq. (3.6)] [check: C3.4, C3.4-full]
  - **C3.5** For the full-$\mathcal C$ vertex: the deviation vanishes if $\mathcal S\supseteq\mathrm{span}\{V_4^{-1}V_5(\cdot,P,\Psi)\}$; pointwise, $w=0\iff V_4^{-1}v\in\mathcal S$. [by C3.3; block: §3 Commentary (3.6)] [check: C3.5]
  - **C3.6** With the $\mathcal S$-consistent vertex $W_6^{(\mathcal S)}=V_6-\tfrac65\mathcal C_{\mathcal S}$: $V^{(4)}_{\rm eff}=S^{(6)}_{\rm eff}\vert_{\mathcal U}+O(g^5)$ for $\mathcal S=\mathrm{Sym}^2\mathcal U$, without enlarging $\mathcal S$; $\mathcal C_{\mathcal S}$ is computable from vertices with all legs in $\mathcal U$. [by C3.2, C1; eq. (3.7)] [check: C3.6-CS, C3.6]
- **A4** (Part B) $\mathcal H=\mathcal U\oplus\mathcal U^\perp$ with $V_2(\mathcal U,\mathcal U^\perp)=0$ (§4.1). A theorem between levels ($V_2$ is diagonal in $L_0^+$); same-level out-of-Siegel-gauge directions are not covered (§4.3 *Not covered*); under H1 (which includes $n=2$) it follows for $\mathcal U^\perp\cap\mathcal H_{nu}$.
- **H1** (Part B only; proposed PH) One-leg selection rule for the declared SL(2,C) section: every elementary $V_n$, $n=2,\dots,6$, vanishes with exactly one leg in the zero-momentum non-universal space $\mathcal H_{nu}$ and all others in the universal space $\mathcal H_u$. Motivation: Sen's universality argument (conformal maps and $b$-insertions preserve the matter Virasoro module of each leg; a sphere correlator with a single non-identity-module leg vanishes), family-independent; a standard Ward-identity consequence, written out in §4.1. Covers the zero-momentum block of $\mathcal U^\perp$ only: nonzero-momentum states satisfy the one-leg rule and A4 by momentum conservation. Falsified by: a nonzero sister value of $V_3(T,T,x)$, $V_4(T^3,x)$, $V_4(T^2D,x)$, $V_5(T^4,x)$ with $x\in\mathcal H_{nu}$ (first test $x=\eta_{\mu\nu}\alpha^\mu_{-1}\bar\alpha^\nu_{-1}\lvert0\rangle$), or a zero-momentum normalisation failure (PH24). Discharged by: a proof for the declared section, or those sister values vanishing. Full text §4.1.
- **C4** Part B. For $\mathcal S=\operatorname{Sym}^2\mathcal U$, $A$ invertible, A4: a truncated solution violates, in the untruncated $S_n$, (a) the $\Psi$-EOM along $\mathcal U^\perp$ from $O(g)$ and, at $S_3,S_4$ only, (b) the $\Sigma$-EOM along $\mathcal S^c$ at relative $O(g)$ with coefficient $-w/5$; under H1 with $\mathcal U^\perp\subset\mathcal H_{nu}$, (a) vanishes identically and the only violated component at $S_3$ is (b) along $\operatorname{Sym}^2\mathcal U^\perp$; relaxing $\mathcal S^c$ reproduces 057's Schur term, which $W_6^{(\mathcal S)}$ absorbs at $O(g^4)$. Conditional on H1 for its part 2. [by C4.1–C4.5]
  - **C4.1** (a), generic: $[g^0]=0$ (A4), $[g^1]=\tfrac12V_3(\Psi^2,\cdot)\vert_{\mathcal U^\perp}$; equals $\partial S^{(4)}_{\rm eff}$ exactly at $S_2$, $\partial S^{(5)}_{\rm eff}$ through $O(g^2)$ at $S_3,S_4$ with $[g^3]$ deviation $-\tfrac1{30}w\cdot(\Psi\odot x)$. [by A1–A4, R17; eq. (4.2)–(4.4)] [check: C4.1-g0, C4.1-g1, C4.1-A4, C4.1-S2, C4.1-g3]
  - **C4.2** (b), generic: $e_c\equiv0$ at $S_2$; $e_c=-\tfrac g5w+O(g^2)$ at $S_3$ and at $S_4$ (both $W_6$); $V_5\to0$ removes it. [by A1–A3, C3.3; eq. (4.5)] [check: C4.2-S2, C4.2-g0, C4.2-g1, C4.2-V5zero]
  - **C4.3** Under H1: (a) $\equiv0$ as an identity on $\mathcal U\times\mathcal S$ ($S_2$–$S_4$); (b1) $\equiv0$ at $S_2,S_3$, at relative $O(g^2)$ with coefficient $\tfrac3{50}\mathcal C(P,P,\cdot)$ at $S_4$; (b2) not removed; relaxed saddle violates (a) first at $O(g^4)$ ($S_3$, (4.7)) and $O(g^5)$ ($S_4$). [by H1, C4.1, C4.2, R17, R19; eq. (4.6)–(4.7)] [check: C4.3-oneleg-a, C4.3-oneleg-b1, C4.3-oneleg-S4, C4.3-oneleg-relaxed]
    - **C4.3.1** $\mathbb Z_2$ class ($\mathcal U$ even, $\mathcal U^\perp$ odd, all $V_n$ invariant — a class with a physical reason: genuine symmetries such as $X\to-X$ or $\mathbb C/\mathbb Z_2$ with $\mathcal U$ the untwisted sector; for $\mathbb Z_N$ the quantum symmetry is a $\mathbb Z_N$ grading, one-leg but not $\mathbb Z_2$; not conditional on H1, which it implies): every odd EOM component vanishes identically at the truncated and the relaxed configuration, $S_2$–$S_4$, both $W_6$; one broken $V_n$ ($n=3,4,5$) switches (a) on at exactly $O(g^{n-2})$, broken $V_6$ switches (b1) on at relative $O(g^2)$. [block: §4.2 *The $\mathbb Z_2$ class*] [check: C4.3-a, C4.3-b1, C4.3-b2, C4.3-relaxed, C4.3-break3, C4.3-break4, C4.3-break5, C4.3-break6]
    - **C4.3.2** Two axes: for $\mathcal U\subsetneq\mathcal H_u$, H1 removes (a) along $\mathcal H_{nu}$ only; along $\mathcal H_u\ominus\mathcal U$ (a) is the generic C4.1, the level-truncation error. The worldsheet-level cutoff of $\mathcal H$ is a separate axis, not addressed beyond the finite layer. [by H1, C4.1; block: §4.2 *The two axes*] [check: C4.3-level]
  - **C4.4** Absorption: at fixed $\Psi$, $V^{\rm full}_{\rm eff}-V^{\rm trunc}_{\rm eff}=\tfrac{g^2}{24}e_c^\top(K_\Psi^{-1})_{cc}e_c$ exactly at $S_3$; $=\tfrac{g^4}{600}w^\top M^{-1}w+O(g^5)$ at $S_3$ and $S_4$ full-$\mathcal C$; $0$ at $S_2$; $O(g^5)$ for $W_6^{(\mathcal S)}$ against R19's $S_4$, at the price of the $\Sigma$-EOM along $\mathcal S$ violated at relative $O(g^2)$ by $\tfrac3{50}(\mathcal C-\mathcal C_{\mathcal S})(P,P,\cdot)$. [by C4.2, C3.3, C3.6, R17, R19; eq. (4.8)–(4.10)] [check: C4.4-S2, C4.4-S3, C4.4-S4C, C4.4-S4S, C4.4-response, C4.4-finite, C4.4-exact, C4.4-cS]
  - **C4.5** Theorem (§4.3 *Result*): parts 1 and 3 for generic tensors (part 1 now includes component (c) for $W_6^{(\mathcal S)}$), part 2 under H1 with $\mathcal U^\perp\subset\mathcal H_{nu}$; the order statements are formal (Taylor coefficients at fixed $\Psi$; $g$-independent in scaled variables, C2.8), the identities (4.6), the $S_2$ exactness and (4.8) hold at any field value where the inverses exist. Part 2 under H1. [by H1, C4.1–C4.4, C2.8]

Open gaps: none
Hypotheses in force: C1–C3 none; C4.3, C4.3.2 and part 2 of C4.5 (hence the root C4 for that part): H1 (registered as PH28 on promotion; zero-momentum block of $\mathcal U^\perp$, nonzero momenta by momentum conservation). C4.1, C4.2, C4.4, parts 1 and 3 of C4.5, and the class statement C4.3.1 are unconditional. PH14 dropped: it scopes R19's exclusion (why $W_6$ must be dressed), while every identity here holds for arbitrary tensors and takes $W_6$ (either definition) as a given vertex.

## 1. Definition (C1)

\subsection*{Setup}
A1–A3. $\mathcal U\subset\mathcal H$ finite-dimensional, $\mathcal S\subseteq\mathrm{Sym}^2\mathcal H$ finite-dimensional.

\subsection*{Definition}
A **field-content truncation** $(\mathcal U,\mathcal S)$ of the cubic theory at order $n$ is the restriction of $S_n(\Psi,\Sigma)$ to $\Psi\in\mathcal U$, $\Sigma\in\mathcal S$, with $V_2,\dots,V_5$ evaluated as in the untruncated theory, and $W_6$ at $n=4$ given by one of two definitions:

- **full-$\mathcal C$ vertex** $W_6=V_6-\tfrac65\mathcal C$, $\mathcal C(P,P,P)=vV_4^{-1}v$ with $V_4^{-1}$ on all of $\mathrm{Sym}^2\mathcal H_0$ (R19 verbatim). Its components on $\mathcal S$ need $V_4^{-1}$ on the whole auxiliary space, so it is **not computable as defined** inside a truncation; any implementation approximates $V_4^{-1}$ by a truncation of its own.
- **$\mathcal S$-consistent vertex** $W_6^{(\mathcal S)}=V_6-\tfrac65\mathcal C_{\mathcal S}$, $\mathcal C_{\mathcal S}$ the symmetrised trilinear form on $\mathcal S$ built as $\mathcal C$ but with $A^{-1}=(V_4\vert_{\mathcal S})^{-1}$: $\mathcal C_{\mathcal S}(\Sigma_1,\Sigma_2,\Sigma_3)=\mathrm{Sym}\,V_5(\Sigma_1,e_M,\cdot)\,(A^{-1})^{MN}\,V_5(\Sigma_2,e_N,\cdot)\cdot\Sigma_3$, so $\mathcal C_{\mathcal S}(P,P,P)=v_S^\top A^{-1}v_S$. For $\mathcal S=\mathrm{Sym}^2\mathcal U$ every leg lies in $\mathcal U$: computable from truncation data.

§2 holds for any $W_6$ (C2.6, C2.8, C2.9) or the full-$\mathcal C$ vertex (C2.7); §3 treats both; C2.7, C3.4, C3.5 are statements about the full-$\mathcal C$ vertex, C3.6 about $W_6^{(\mathcal S)}$. **Task 13 uses $W_6^{(\mathcal S)}$**: it is computable from the same data as the rest of the truncated action, and it restores the $O(g^4)$ Taylor match without enlarging $\mathcal S$ (C3.6); the full-$\mathcal C$ vertex would have to be approximated anyway, and its truncation-dependence is exactly the Schur term (3.6). $\mathcal U$ is a Siegel-gauge subspace in the level-truncation comparison; elimination of $\Sigma$ commutes with restricting $\Psi$, so nothing here depends on it (the $\Psi$-EOM along gauge-fixed directions is part B). Two choices of $\mathcal S$:

- $\mathcal S=\mathrm{Sym}^2\mathcal U$, **Veronese-closed**: the Veronese map $\Psi\mapsto P=\Psi^{\otimes2}$ sends $\mathcal U$ into $\mathcal S$, so the perturbative saddle $\Sigma_*=P+O(g)$ of the untruncated theory is representable at leading order.
- $\mathcal S=\mathrm{Sym}^2\mathcal U\oplus\mathcal S'$: extra auxiliary directions (e.g. pairs with one leg outside $\mathcal U$). $\mathcal S'$ enters the eliminated potential through $V_4$-mixing with $\mathrm{Sym}^2\mathcal U$ (§3).

A $\mathcal S$ **not** containing $\mathrm{Sym}^2\mathcal U$ (Veronese-incomplete) generically fails already at the quartic order (C3.1, break legs of checks C3.1-sym, C3.1-generic); non-generic exceptions exist because $V_4$ is indefinite.

**The two axes.** The Moeller–Sen–Zwiebach / Yang–Zwiebach level truncation (Moeller, Sen, Zwiebach 2000, hep-th/0005036; Yang, Zwiebach 2005, hep-th/0506077) is a truncation of the nonpolynomial theory: $\Psi\in\mathcal U_L$ (all states up to level $L$), *every* $V_k(\Psi^k)$ kept on $\mathcal U_L$, the series in $k$ cut at a chosen vertex order. Its potential at vertex order $n$ is $S^{(n)}_{\rm eff}\vert_{\mathcal U}$. The field-content truncation of the cubic theory has a second axis — the auxiliary space $\mathcal S$ — and an order $n$ of the cubic tower. The comparison statement (C3) is: for $\mathcal S=\mathrm{Sym}^2\mathcal U$, the eliminated cubic-truncated potential equals $S^{(n)}_{\rm eff}\vert_{\mathcal U}$ through $O(g^3)$ at $n=3$ (as in the untruncated theory, R17) and, at $n=4$, through $O(g^3)$ with the full-$\mathcal C$ vertex (one order less than the untruncated $O(g^4)$ of R19, the difference being a Schur complement measuring what $\mathcal S$ misses) or through $O(g^4)$ with $W_6^{(\mathcal S)}$. All these are formal statements on Taylor coefficients in $g$ at fixed $\Psi$ (see *Interpretation* in §2). The level $L$ of $\mathcal U$ is shared; the vertex order $n$ is shared; $\mathcal S$ has no counterpart on the nonpolynomial side.

**The $\ker V_4$ quotient.** The ledger takes $\Sigma\in\mathrm{Sym}^2\mathcal H_0/\ker V_4$; the notes flag that the quotient's compatibility with $V_5$ is open. In a truncation the quotient is replaced by the restriction to $\mathcal S$ under A2 ($V_4\vert_{\mathcal S}$ invertible); if a given $\mathcal S$ has $\ker V_4\vert_{\mathcal S}\neq0$, one restricts to a complement in $\mathcal S$, and the result depends on that choice exactly when $V_5$ does not annihilate the kernel — the same open point (R38/034), not settled here.

## 2. The $(t,\sigma)$ model (C2)

\subsection*{Setup}
A1–A3. $\mathcal U=\mathrm{span}(T)$, $T$ the zero-momentum tachyon; $\mathcal S=\mathrm{span}(e_1)=\mathrm{Sym}^2\mathcal U$, $e_1=T\otimes T$. Fields $\Psi=t\,T$, $\Sigma=\sigma\,e_1$. Symbolic couplings $V_n:=V_n(T^n)$, $n=2,\dots,6$, $\mathcal C_{TT}:=\mathcal C(e_1,e_1,e_1)$ (full $V_4^{-1}$), $W_6:=W_6(e_1^3)=V_6-\tfrac65\mathcal C_{TT}$. Then $P=t^2e_1$, $V_4(\Sigma,\Sigma)=V_4\sigma^2$, $V_4(\Sigma,P)=V_4\sigma t^2$, $V_5(\Sigma,\Sigma,\Psi)=V_5\sigma^2t$, $W_6(\Sigma^3)=W_6\sigma^3$:

$$
\begin{aligned}
S_2(t,\sigma)&=\tfrac12V_2t^2+\tfrac g6V_3t^3-\tfrac{g^2}{24}V_4\sigma^2+\tfrac{g^2}{12}V_4\sigma t^2, &&\text{(2.1)}\\
S_3(t,\sigma)&=S_2+\tfrac{g^3}{120}V_5\sigma^2t, &&\text{(2.2)}\\
S_4(t,\sigma)&=S_3+\tfrac{g^4}{720}W_6\sigma^3. &&\text{(2.3)}
\end{aligned}
$$

\subsection*{Derivation}

*Quintic order.* The $\sigma$-EOM of (2.2) is linear:

$$
\begin{aligned}
\partial_\sigma S_3&=-\tfrac{g^2}{12}V_4\sigma+\tfrac{g^2}{12}V_4t^2+\tfrac{g^3}{60}V_5\sigma t
=-\tfrac{g^2}{12}\big[K(t)\,\sigma-V_4t^2\big], &&\text{(2.4)}\\
K(t)&:=V_4-\tfrac g5V_5t\;=\;K_\Psi\vert_{e_1}, &&\text{(2.5)}\\
\sigma_*(t)&=\frac{V_4t^2}{V_4-\tfrac g5V_5t}=t^2+\tfrac g5K^{-1}v,\qquad v=V_5t^3. &&\text{(2.6)}
\end{aligned}
$$

Writing $S_3=A+B\sigma-\tfrac12C\sigma^2$ with $B=\tfrac{g^2}{12}V_4t^2$, $C=\tfrac{g^2}{12}K$, the saddle value is $A+B^2/2C$:

$$
\begin{aligned}
V_{\rm eff}(t)&=S_3(t,\sigma_*)=\tfrac12V_2t^2+\tfrac g6V_3t^3+\frac{g^2}{24}\,\frac{V_4^2t^4}{V_4-\tfrac g5V_5t} &&\text{(2.7)}\\
&=S^{(5)}_{\rm eff}(t)+\frac{g^4}{600}\,\frac{V_5^2t^6}{K(t)} &&\text{(2.8)}\\
&=\tfrac12V_2t^2+\tfrac g6V_3t^3+\frac{g^2}{24}V_4t^4\sum_{k\ge0}\Big(\frac{gV_5t}{5V_4}\Big)^k
=S^{(5)}_{\rm eff}+\frac{g^4}{600}\frac{V_5^2}{V_4}t^6+O(t^7). &&\text{(2.9)}
\end{aligned}
$$

*Pole.* $V_{\rm eff}$ has a simple pole at the zero of the dressed kernel,

$$
t_{\rm pole}=\frac{5V_4}{gV_5},\qquad \operatorname{Res}_{t_{\rm pole}}V_{\rm eff}=-\frac{5g}{24}\frac{V_4^2t_{\rm pole}^4}{V_5}=-\frac{3125\,V_4^6}{24\,g^3V_5^5}. \tag{2.10}
$$

At $t=t_{\rm pole}$ the $\sigma$-EOM (2.4) reduces to $\tfrac{g^2}{12}V_4t_{\rm pole}^2=\tfrac{25V_4^3}{12V_5^2}\neq0$: it is $\sigma$-independent **and violated**. There is no finite saddle at the pole; $\sigma_*\to\infty$ as $t\to t_{\rm pole}$.

*Joint critical points.* Every stationary point of $S_3(t,\sigma)$ has $K(t)\neq0$ (previous line), hence $\sigma=\sigma_*(t)$ and $V_{\rm eff}'(t)=0$. Clearing denominators, $K^2V_{\rm eff}'=t\times(\text{cubic in }t)$ (check C2.4-count): at most three nontrivial extrema, the same count as for the quintic polynomial $S^{(5)}_{\rm eff}$.

*Sextic order.* With (2.3) the $\sigma$-EOM becomes quadratic,

$$
V_4t^2-K(t)\,\sigma+\tfrac{g^2}{20}W_6\,\sigma^2=0, \tag{2.11}
$$

with roots $\sigma_\mp=\tfrac{10}{g^2W_6}\big[K\mp\sqrt{K^2-\tfrac{g^2}5W_6V_4t^2}\big]$, $\sigma_+\sigma_-=\tfrac{20V_4t^2}{g^2W_6}$. The branch continuous with $\sigma=t^2$ (for $K>0$, $\sigma_-$ with the principal root) is the power series

$$
\sigma_{\rm pert}=t^2+\frac{gV_5}{5V_4}t^3+g^2\Big(\frac{V_5^2}{25V_4^2}+\frac{W_6}{20V_4}\Big)t^4+O(g^3); \tag{2.12}
$$

the other, $\sigma_+=\tfrac{20K}{g^2W_6}-\sigma_-$, has $g^2\sigma_+\to20V_4/W_6$: a non-perturbative saddle, $\sigma\sim g^{-2}$ at fixed $t$. The eliminated potential on the perturbative branch is

$$
V^{(4)}_{\rm eff}(t)=S^{(6)}_{\rm eff}(t)+\frac{g^4}{600}\Big(\frac{V_5^2}{V_4}-\mathcal C_{TT}\Big)t^6+O(g^5). \tag{2.13}
$$

In the untruncated one-dimensional theory ($\mathcal U=\mathcal H$, so $\mathcal C_{TT}=V_5^2/V_4$) the $t^6$ term matches: R19's closure. With $\mathcal U\subsetneq\mathcal H$, $\mathcal C_{TT}t^6=vV_4^{-1}v$ with the full inverse, and (2.13) carries the deviation (3.6) of §3.

*Scaling.* With $\tau=gt$, $s=g^2\sigma$: $g^2S_4=\tfrac12V_2\tau^2+\tfrac16V_3\tau^3-\tfrac1{24}V_4s^2+\tfrac1{12}V_4s\tau^2+\tfrac1{120}V_5s^2\tau+\tfrac1{720}W_6s^3$, $g$-free (check C2.8). So $t_{\rm pole}$, the cubic-order tachyon vacuum $\tau_0=-2V_2/V_3$ and $\sigma_+$ all sit at the **same** scale $\tau=O(1)$, i.e. $t=O(1/g)$: the pole is not parametrically far from the tachyon vacuum. Whether it lies between the perturbative vacuum and the tachyon vacuum is a question about the numbers $V_2,\dots,V_5$ (Task 13), not about $g$.

*Fold at $S_4$.* The discriminant of (2.11) is $\Delta(t)=K(t)^2-\tfrac{g^2}5W_6V_4t^2$. Where $\Delta=0$ the perturbative branch ($\sigma_-$ for $V_4>0$) and $\sigma_+$ collide (double root $\sigma=10K/(g^2W_6)$); beyond it both are complex. In $\tau=gt$: $(V_4-\tfrac15V_5\tau)^2=\tfrac15W_6V_4\tau^2$, i.e. $V_4=\tau(\tfrac{V_5}5\pm\sqrt{W_6V_4/5})$,

$$
\tau_{\rm fold}^\pm=\frac{5V_4}{V_5\pm\sqrt{5W_6V_4}},\qquad \tau_{\rm pole}=\frac{5V_4}{V_5}, \tag{2.14}
$$

real iff $W_6V_4>0$; the fold on the side of $\tau_{\rm pole}$ is the one with $\lvert\tau_{\rm fold}\rvert<\lvert\tau_{\rm pole}\rvert$ (the root with $\pm=\operatorname{sign}V_5$), so the perturbative branch ends before the would-be pole. At $t=t_{\rm pole}$ ($K=0$) (2.11) reads $V_4t_{\rm pole}^2+\tfrac{g^2}{20}W_6\sigma^2=0$: a finite real saddle $\sigma=\pm t_{\rm pole}\sqrt{-20V_4/(g^2W_6)}$ exists iff $W_6V_4<0$ (then $\Delta>0$ everywhere and no fold occurs). So "no finite saddle at the pole" (C2.4) is an $S_3$ statement only: at $S_4$ the pole is replaced by a fold ($W_6V_4>0$) or smoothed into a regular saddle ($W_6V_4<0$). As $W_6\to0$, $\tau^\pm_{\rm fold}\to\tau_{\rm pole}$ and the $S_3$ pole is recovered. (Checks C2.9-fold±, C2.9-pole.)

*Interpretation.* The scaling is exact at $S_3$ and $S_4$, so $t_{\rm pole}$, $t_{\rm fold}$, the cubic-order tachyon vacuum and $\sigma_+$ all sit at $\tau=gt=O(1)$. There every "order in $g$" is $O(1)$: "$V^{(3)}_{\rm eff}$ matches $S^{(5)}_{\rm eff}$ through $O(g^3)$" means only "same Taylor coefficients through $\Psi^5$", and says nothing about the accuracy of the vacuum energy or location. Level truncation at the same vertex order drops $V_6,V_7,\dots$, the cubic truncation replaces them by the rational tail of (2.7) (or the $S_4$ branch): both are $O(1)$ modifications at the vacuum and compete there; which is closer to the full theory is a numerical question (Task 13), not settled by the order counting. Whether the pole lies between the perturbative and the tachyon vacuum: $\operatorname{sign}\tau_{\rm pole}=\operatorname{sign}\tau_0$ and $\lvert\tau_{\rm pole}\rvert<\lvert\tau_0\rvert$, i.e. $0<\tau_{\rm pole}/\tau_0=-\tfrac{5V_4V_3}{2V_2V_5}<1$.

*Limits.* $g\to0$ at fixed $t$: everything perturbative, $\sigma_*\to t^2$, $t_{\rm pole},t_{\rm fold}\to\infty$, $\sigma_+\to\infty$. $V_5\to0$: $t_{\rm pole}\to\infty$ and $V_{\rm eff}\to$ the quartic potential (exact, C3.1). $W_6\to0$: $\sigma_-\to\sigma_*$ (the $S_3$ saddle), $\sigma_+\to\infty$, the fold goes to the pole.

\subsection*{Commentary}

- (2.6): the second form is R17's $\Sigma_*=P+\tfrac g5K_\Psi^{-1}v$ on $\mathcal S=\mathrm{span}(e_1)$, $v=V_5(\cdot,P,\Psi)=V_5t^3$; the factor $\tfrac g5=\tfrac{4!}{5!}g$ is the ratio of $\partial_\sigma$ of $\tfrac{g^3}{5!}V_5\sigma^2t$ to $\partial_\sigma$ of $\tfrac{g^2}{4!}V_4\sigma^2$.
- (2.8): R17's exact rewriting on-shell ($\tilde X=0$), $vK_\Psi^{-1}v=V_5^2t^6/K$; checked independently of (2.7) (C2.2-R17).
- (2.9): the tail beyond $t^5$ is a geometric series in $gV_5t/(5V_4)$ with radius $\lvert t_{\rm pole}\rvert$; its first term is R17's feedback with $V_4^{-1}\to1/V_4$.
- (2.11)–(2.12): from $\tfrac{12}{g^2}\partial_\sigma S_4$; the series branch is built by fixed-point iteration, independently of the closed-form root (C2.6-perturbative, C2.6-branch).
- (2.13): envelope argument — $\tfrac{g^4}{720}W_6\sigma^3$ at $\sigma=t^2$ contributes $\tfrac{g^4}{720}(V_6-\tfrac65\mathcal C_{TT})t^6$, the $S_3$ part contributes $\tfrac{g^4}{600}\tfrac{V_5^2}{V_4}t^6$; $\tfrac{6}{5\cdot720}=\tfrac1{600}$.

\subsection*{Result}
$$\boxed{\sigma_*=\frac{V_4t^2}{V_4-\tfrac g5V_5t},\qquad V_{\rm eff}=\tfrac12V_2t^2+\tfrac g6V_3t^3+\frac{g^2}{24}\frac{V_4^2t^4}{V_4-\tfrac g5V_5t},\qquad t_{\rm pole}=\frac{5V_4}{gV_5}}$$
and, at sextic order, (2.12)–(2.13).

**Remark (former C2.5, withdrawn as a node; correction to the brief, mean-field seed).** The brief anticipated, at the pole, "the $\sigma$-EOM degenerate, $\sigma$ free, the $\Psi$-EOM then a quadratic in $\sigma$". In the $(t,\sigma)$ model this branch does not exist: at $K=0$ the $\sigma$-EOM is the nonzero constant $\tfrac{g^2}{12}V_4t_{\rm pole}^2$. With $\dim\mathcal S\ge2$ the degenerate branch requires, at a point $\Psi_0$ with $\det K_{\Psi_0}=0$ and null vector $n$, also $n\cdot u(\Psi_0)=0$, $u=V_4(\cdot,P)\vert_{\mathcal S}$ (solvability of $K_{\Psi_0}\Sigma=u$); then $\Sigma=\Sigma_p+\lambda n$ with $\lambda$ free, and the $\Psi$-EOM is quadratic in $\lambda$ (through $V_5(\Sigma,\Sigma,\cdot)$). The locus $\{\det K_\Psi=0,\ n\cdot u=0\}$ has codimension 2 in $\mathcal U$ and is generically non-empty for $\dim\mathcal U\ge2$; what is non-generic is a joint critical point on it: $\dim\mathcal U+1$ unknowns $(\Psi_0,\lambda)$ against $\dim\mathcal U+2$ conditions, overdetermined by one. It needs a tuned coupling or a selection rule forcing $n\cdot u\equiv0$ on $\det K_\Psi=0$ (possible for the real vertices). That condition is the seed for Task 14; nothing further is claimed. (Counting argument only, no machine check.)

\subsection*{Verification}
`codes/verify-truncation-structure.py`, checks C2.1–C2.9 (labels = node IDs; sympy, symbolic couplings, plus five seeded complex points): $\sigma_*$ from `solve` and against R17 (break: $g/4$ fails); (2.7) and (2.8) (break: feedback $1/720$ fails); (2.9) through $t^6$ and the geometric coefficient up to $k=8$; pole, residue, EOM at the pole (asserted nonzero); C2.4-count the degree count; (2.11), both roots, the series branch and its coefficients, $g^2\sigma_+\to20V_4/W_6$ as a limit of the closed-form root (replaces the tautological Vieta test); (2.13) with generic $\mathcal C_{TT}$ (break: dropping the deviation fails); C2.7-full the $\mathcal U=\mathcal H$ limit (a corollary of C2.7, not independent); C2.7-R19 the one-field specialisation of R19's exact rewriting (4); C2.8 the $g$-scaling; C2.9-fold± the discriminant of (2.11) vanishes at $\tau^\pm_{\rm fold}$ with a double root (break: $t_{\rm pole}$ is not a zero of $\Delta$), C2.9-pole a real saddle at $t_{\rm pole}$ for $W_6V_4<0$ (break: sign of $W_6V_4$ flipped, no real root). All PASS (run 2).

## 3. The five-field model and the general statement (C3)

\subsection*{Setup}
A1–A3. Five-field model: $\mathcal U=\mathrm{span}(T,D)$ ($D$ the zero-momentum level-$(1,1)$ partner in the sister's basis), $\Psi=tT+dD$; $\mathcal S=\mathrm{Sym}^2\mathcal U=\mathrm{span}(e_1,e_2,e_3)$, $e_1=T\otimes T$, $e_2=\tfrac12(T\otimes D+D\otimes T)$, $e_3=D\otimes D$, $\Sigma=\sigma_{TT}e_1+\sigma_{TD}e_2+\sigma_{DD}e_3$. With $h_k:=V_4(T^{4-k}D^k)$, the block $A:=V_4\vert_{\mathcal S}$ is the Hankel matrix $A_{ij}=h_{i+j-2}$ ($i,j=1,2,3$); $P=t^2e_1+2td\,e_2+d^2e_3$. Cubic couplings: $V_3(T^2D)=V_3(D^3)=0$ by ghost-number selection; $V_3(TD^2)$ is not sourced here and may be nonzero; the cubic couplings sit in $A(\Psi)$ and never enter the elimination. **Basis.** $e_i$ is the sister's *coordinate* basis (not orthonormal); $\sigma_*=(t^2,2td,d^2)$ are coordinates in it, the factor 2 coming from the $\tfrac12$ in $e_2$ (in $e_2'=(TD+DT)/\sqrt2$ it would be $\sqrt2\,td$). Task 13 must enter the sister's $3\times3$ $V_4$ in this basis, with $\times\tfrac12$ (R43). The Gram matrix $G_2$ of this basis does not enter the action, which uses $V_4$ as a bilinear form; it enters only $m_2=G_2^{-1}V_4$, whose invertibility is that of $A$. General statement: $\mathcal U\subset\mathcal H$ arbitrary, $\mathrm{Sym}^2\mathcal H=\mathcal S\oplus\mathcal S^c$, $V_4=\begin{pmatrix}A&B\\B^\top&D_c\end{pmatrix}$, $W:=V_5(\cdot,\cdot,\Psi)\vert_{\mathcal S}$, $u:=V_4(\cdot,P)\vert_{\mathcal S}=Ap$ ($p$ = components of $P\in\mathcal S$), $v=V_5(\cdot,P,\Psi)$ on $\mathrm{Sym}^2\mathcal H$ with components $(v_S,v_c)$.

\subsection*{Derivation}

*Quartic order, exact.* Because $P\in\mathcal S$ (Veronese closure), the square completes inside $\mathcal S$:

$$
S_2\vert_{(\mathcal U,\mathcal S)}=A(\Psi)-\tfrac{g^2}{24}V_4(\Sigma-P,\Sigma-P)+\tfrac{g^2}{24}V_4(P,P),\qquad
\Sigma_*=P,\qquad V^{(2)}_{\rm eff}=A(\Psi)+\tfrac{g^2}{4!}V_4(\Psi^4). \tag{3.1}
$$

This needs only $P\in\mathcal S$ and $A$ invertible, and it is exact (no higher terms: $S_2$ has none). In the five-field model: $\sigma_*=(t^2,2td,d^2)$ and $V_4(\Psi^4)=\sum_k\binom4kh_kt^{4-k}d^k$. For a Veronese-incomplete $\mathcal S$ (no $P$-component in some direction), $\Sigma_*=A^{-1}u$ with $u=V_4(\cdot,P)\vert_{\mathcal S}$, $u\neq Ap$, and $V^{(2)}_{\rm eff}-A=\tfrac{g^2}{24}u^\top A^{-1}u\neq\tfrac{g^2}{24}V_4(P,P)$ generically.

*Quintic order.* $S_3$ restricted: the $\Sigma$-EOM is $K_S\Sigma=u$, $K_S:=A-\tfrac g5W$, and

$$
V^{(3)}_{\rm eff}=A(\Psi)+\tfrac{g^2}{24}\,u^\top K_S^{-1}u
=A+\tfrac{g^2}{24}\Big[p^\top Ap+\tfrac g5\,p^\top Wp+\tfrac{g^2}{25}\,p^\top WA^{-1}Wp+O(g^3)\Big], \tag{3.2}
$$

with $p^\top Ap=V_4(\Psi^4)$, $p^\top Wp=V_5(P,P,\Psi)=V_5(\Psi^5)$, $Wp=v_S$. Hence

$$
V^{(3)}_{\rm eff}=S^{(5)}_{\rm eff}\vert_{\mathcal U}+\frac{g^4}{600}\,v_S^\top A^{-1}v_S+O(g^5), \tag{3.3}
$$

a rational function of $\Psi$ with denominator $\det K_S(\Psi)$ (degree $\le\dim\mathcal S$ in $\Psi$). The untruncated theory has $\tfrac{g^4}{600}vV_4^{-1}v$ in its place (R17).

*Schur complement.* Block inversion of $V_4$ on $\mathcal S\oplus\mathcal S^c$:

$$
v^\top V_4^{-1}v=v_S^\top A^{-1}v_S+w^\top M^{-1}w,\qquad M:=D_c-B^\top A^{-1}B,\qquad w:=v_c-B^\top A^{-1}v_S. \tag{3.4}
$$

$M$ is invertible when $A$ and $V_4$ are ($\det V_4=\det A\,\det M$). So

$$
\frac{g^4}{600}\Big[v_S^\top A^{-1}v_S-vV_4^{-1}v\Big]=-\frac{g^4}{600}\,w^\top M^{-1}w. \tag{3.5}
$$

*Sextic order.* $S_4$ restricted, with $W_6$ carrying the full $\mathcal C$: by the envelope argument of (2.13), $\tfrac{g^4}{720}W_6(P^3)=\tfrac{g^4}{720}V_6(\Psi^6)-\tfrac{g^4}{600}vV_4^{-1}v$ and the $S_3$ part adds $\tfrac{g^4}{600}v_S^\top A^{-1}v_S$:

$$
V^{(4)}_{\rm eff}=S^{(6)}_{\rm eff}\vert_{\mathcal U}-\frac{g^4}{600}\,w^\top M^{-1}w+O(g^5). \tag{3.6}
$$

In the $(t,\sigma)$ model $w^\top M^{-1}w=(\mathcal C_{TT}-V_5^2/V_4)t^6$, which is (2.13).

*Sextic order, $\mathcal S$-consistent vertex.* Replace $W_6$ by $W_6^{(\mathcal S)}$ (§1). The envelope argument is unchanged (the $O(g^2)$ shift of the saddle enters only at $O(g^6)$), and $\mathcal C_{\mathcal S}(P,P,P)=v_S^\top A^{-1}v_S$, so

$$
\begin{aligned}
V^{(4,\mathcal S)}_{\rm eff}-S^{(5)}_{\rm eff}\vert_{\mathcal U}
&=\tfrac{g^4}{720}V_6(\Psi^6)-\tfrac{g^4}{720}\cdot\tfrac65\,v_S^\top A^{-1}v_S+\tfrac{g^4}{600}v_S^\top A^{-1}v_S+O(g^5)\\
&=\tfrac{g^4}{720}V_6(\Psi^6)+O(g^5),
\end{aligned}\tag{3.7}
$$

i.e. $V^{(4,\mathcal S)}_{\rm eff}=S^{(6)}_{\rm eff}\vert_{\mathcal U}+O(g^5)$: the truncated feedback of $S_3$ is cancelled by the truncated composite exactly as R19's full feedback is cancelled by the full composite. The $O(g^4)$ match is restored without enlarging $\mathcal S$, and the Schur term of (3.6) is a property of the full-$\mathcal C$ definition, not of the truncation. (Checks C3.6-CS, C3.6.)

*The $d=0$ slice.* The five-field model at $d=0$ is **not** the $(t,\sigma)$ model beyond quartic order: with $p=(t^2,0,0)$, $u=t^2(h_0,h_1,h_2)$ and $V_5(e_1,e_2,T)=\{T^4D\}$ source $\sigma_{TD},\sigma_{DD}$ at $O(g)$; and $d=0$ is not a consistent truncation of the $\Psi$-EOM ($\partial_d$ at $d=0$ contains $\tfrac{g^2}6h_1t^3\neq0$). One-field numbers must not be read as the $d=0$ slice.

\subsection*{Commentary}

- (3.1): the only input is $P\in\mathcal S$; this is why $\mathrm{Sym}^2\mathcal U$ is the minimal auxiliary space. The break legs remove $e_2$ (five-field, symbolic) or replace a $\mathrm{Sym}^2\mathcal U$ direction by an off-$\mathcal U$ pair (generic tensors); both fail.
- (3.2): Neumann expansion $K_S^{-1}=A^{-1}+\tfrac g5A^{-1}WA^{-1}+\dots$ with $u=Ap$; the $g^3$ and $g^4$ terms reproduce the untruncated coefficients $\tfrac1{5!}=\tfrac1{24}\cdot\tfrac15$ and $\tfrac1{600}=\tfrac1{24}\cdot\tfrac1{25}$.
- (3.4): standard block inverse; $w$ is the part of $v$ that $\mathcal S$ cannot absorb once the $\mathcal S$–$\mathcal S^c$ mixing $B$ is projected out. $w=0$ iff $v_c=B^\top A^{-1}v_S$; for $B=0$ it is simply $v_c=V_5(\cdot,P,\Psi)\vert_{\mathcal S^c}$, the pairs with at least one leg outside $\mathcal U$.
- (3.6): the truncated $S_3$ and $S_4$ both match through $O(g^3)$; the untruncated $S_4$ matches through $O(g^4)$ (R19). The deviation vanishes when $x:=V_4^{-1}v\in\mathcal S$ (then $v_S=Ax$, $v_c=B^\top x$, so $w=0$): an enlarged $\mathcal S=\mathrm{Sym}^2\mathcal U\oplus\mathcal S'$ removes the $O(g^4)$ deviation for every $\Psi\in\mathcal U$ if $\mathcal S\supseteq\mathrm{span}\{V_4^{-1}V_5(\cdot,P,\Psi):\Psi\in\mathcal U\}$ — the exchanged $\Sigma$-propagator image of the quintic source. This is the precise sense in which $\mathcal S'$ matters **for the full-$\mathcal C$ vertex**; pointwise, $w=0\iff V_4^{-1}v\in\mathcal S$ (if $w=0$, $x_S=A^{-1}v_S$ gives $V_4(x_S,0)=(v_S,B^\top A^{-1}v_S)=v$). The scalar $w^\top M^{-1}w$ can vanish with $w\neq0$ since $M$ is indefinite. With $W_6^{(\mathcal S)}$ no enlargement is needed at $O(g^4)$ (3.7).
- (3.7): $\tfrac65\cdot\tfrac1{720}=\tfrac1{600}$, the same coefficient identity as in (2.13).

\subsection*{Result}
For $\mathcal S=\mathrm{Sym}^2\mathcal U$ and $A=V_4\vert_{\mathcal S}$ invertible:
$$\boxed{\begin{aligned}&V^{(2)}_{\rm eff}=S^{(4)}_{\rm eff}\vert_{\mathcal U}\ \text{exactly};\qquad V^{(3)}_{\rm eff}=S^{(5)}_{\rm eff}\vert_{\mathcal U}+\tfrac{g^4}{600}v_S^\top A^{-1}v_S+O(g^5);\\
&V^{(4)}_{\rm eff}\big\vert_{W_6\ \text{full-}\mathcal C}-S^{(6)}_{\rm eff}\vert_{\mathcal U}=-\tfrac{g^4}{600}\,w^\top M^{-1}w+O(g^5);\qquad V^{(4)}_{\rm eff}\big\vert_{W_6^{(\mathcal S)}}=S^{(6)}_{\rm eff}\vert_{\mathcal U}+O(g^5)\end{aligned}}$$
with $M=D_c-B^\top A^{-1}B$, $w=v_c-B^\top A^{-1}v_S$; $w^\top M^{-1}w\neq0$ for **generic** tensors only (for the real vertices $w$ may vanish by selection rules). All matchings are formal (Taylor coefficients in $g$ at fixed $\Psi$, i.e. through $\Psi^5$ or $\Psi^6$); at the tachyon vacuum, $gt=O(1)$, they carry no accuracy statement (§2 *Interpretation*).

\subsection*{Verification}
Checks (labels = node IDs; renamed from run 1). C3.1-sym: five-field, symbolic Hankel $h_0,\dots,h_4$, `solve` of the three $\sigma$-EOMs; (3.1) exact (break: $\mathcal S=\mathrm{span}(e_1,e_3)$ fails). C3.1-generic: generic symmetric tensors, $\mathcal H=\mathbb R^4$, $\mathcal U=\mathbb R^2$ ($\dim\mathcal S=3$ inside $\dim\mathrm{Sym}^2\mathcal H=10$), Newton saddle: deviation $0.0$ (break: Veronese-incomplete $\mathcal S$, deviation $7.9\times10^{-2}$). C3.2: truncated $S_3$ on-shell mismatch$/g^4$, Richardson-extrapolated from $g=10^{-2},5\cdot10^{-3}$: $-0.229154$ vs $v_S^\top A^{-1}v_S/600=-0.229293$ (tol $10^{-3}$ rel.; break: the full-inverse value $+0.2554$ fails). C3.3: (3.4) at $10^{-10}$, $w^\top M^{-1}w=290.8\neq0$ (break: sign flip fails). C3.4: truncated $S_4$ (full $\mathcal C$ in $W_6$) mismatch$/g^4\to-0.48438$ vs $-w^\top M^{-1}w/600=-0.48465$ (break: the $S_3$ value fails; numerical Richardson only, plausible coefficient errors are $\ge20\%$ effects; the exact-series upgrade was not done in this pass); C3.4-full: untruncated ($\mathcal S=\mathrm{Sym}^2\mathcal H$) log-slope $4.90$, i.e. $O(g^5)$ as R19. C3.5: $\mathcal S=\mathrm{Sym}^2\mathcal U+\mathrm{span}(V_4^{-1}v)$ closes the deviation (break: a random extra direction does not). C3.6-CS: $\mathcal C_{\mathcal S}(P,P,P)=v_S^\top A^{-1}v_S=-137.58$. C3.6: truncated $S_4$ with $W_6^{(\mathcal S)}$, Newton saddle, mismatch$/g^4$ Richardson from $g=2\cdot10^{-3},10^{-3}$: $-8.0\times10^{-6}$, against the Schur scale $0.4846$ (tol $10^{-3}$ rel.); break: the full-$\mathcal C$ $W_6$ at the same $g$ gives $-0.48463$, fails. C3.2-exact: five-field $S_3$ with random rational $h_k$, $V_5(T^{5-k}D^k)$ at a rational $(t,d)$, exact series in $g$: $[g^2],[g^3]$ = target, $[g^4]=v_S^\top A^{-1}v_S/600$ exactly.

## 4. Part B: which untruncated EOM components a truncated solution violates (C4)

Task (brief 12b): for a solution $(\Psi_*,\Sigma_*)$ of the truncated EOM at $S_2,S_3,S_4$, list the components of the untruncated EOM off $(\mathcal U,\mathcal S)$ and the order in $g$ at which each is violated; state what a universality selection rule removes; derive the consistency theorem. Objective 2(a): the statement a paper can quote ("the truncation solves the full EOM up to …"), and the hypothesis on the vertex family that Task 13 needs.

### 4.0 EOM-component table (C4.1–C4.4)

Normalisations (§4.1): $E_x$ is the $\Psi$-EOM $\partial S/\partial\Psi$ along $x$; $e:=-\tfrac{12}{g^2}\,\partial S/\partial\Sigma=V_4(\Sigma-P)-\tfrac g5V_5(\Sigma,\cdot,\Psi)-\tfrac{g^2}{20}W_6(\Sigma,\Sigma,\cdot)$ is the $\Sigma$-EOM, normalised so that its leading term is $V_4(\Sigma-P)$; "relative $O(g^k)$" means $e=O(g^k)$ in this normalisation. Orders are Taylor orders in $g$ at fixed $\Psi_*\in\mathcal U$ with $\Sigma_*=\Sigma_*(\Psi_*;g)$ the truncated perturbative saddle; they hold on the whole truncated $\Sigma$-shell, so in particular at a truncated solution. $\mathcal S^c=(\mathcal U\odot\mathcal U^\perp)\oplus\operatorname{Sym}^2\mathcal U^\perp$; $w=v_c-B^\top A^{-1}v_S$, $M=D_c-B^\top A^{-1}B$ as in (3.4). For $S_4$ with $W_6^{(\mathcal S)}$ the untruncated theory is R19's $S_4$ (full-$\mathcal C$ $W_6$ on $\operatorname{Sym}^2\mathcal H$): $W_6^{(\mathcal S)}$ has no definition off $\mathcal S$.

| component of the untruncated EOM | $S_2$ | $S_3$ | $S_4$, full-$\mathcal C$ | $S_4$, $W_6^{(\mathcal S)}$ (vs R19 $S_4$) | under H1 (one-leg rule) |
| --- | --- | --- | --- | --- | --- |
| (a) $\Psi$-EOM along $\mathcal U^\perp$ (A4) | $O(g)$: $\tfrac12V_3(\Psi^2,\cdot)$; equals $\partial S^{(4)}_{\rm eff}$ exactly | $O(g)$; equals $\partial S^{(5)}_{\rm eff}$ through $O(g^2)$, $[g^3]$ deviation $-\tfrac1{30}w(\Psi\odot x)$ | as $S_3$ | as $S_3$ | $\equiv0$ (identity in the fields, all $S_n$) |
| (b1) $\Sigma$-EOM along $\mathcal U\odot\mathcal U^\perp$ | $\equiv0$ | relative $O(g)$: $-\tfrac15w\vert_{\mathcal U\odot\mathcal U^\perp}$ | as $S_3$ | as $S_3$ | $\equiv0$ at $S_2,S_3$; relative $O(g^2)$ at $S_4$ through $\mathcal C$ ($\equiv0$ in the $\mathbb Z_2$ class) |
| (b2) $\Sigma$-EOM along $\operatorname{Sym}^2\mathcal U^\perp$ | $\equiv0$ | relative $O(g)$: $-\tfrac15w\vert_{\operatorname{Sym}^2\mathcal U^\perp}$ | as $S_3$ | as $S_3$ | **not removed**: relative $O(g)$, $-\tfrac15w\vert_{\operatorname{Sym}^2\mathcal U^\perp}$ |
| (c) $\Psi$-EOM along $\mathcal U$; $\Sigma$-EOM along $\mathcal S$ | $\equiv0$ (truncated EOM) | $\equiv0$ | $\equiv0$ | $\Psi$: $\equiv0$; $\Sigma$ along $\mathcal S$: relative $O(g^2)$, $\tfrac3{50}(\mathcal C-\mathcal C_{\mathcal S})(P,P,\cdot)\vert_{\mathcal S}$ | same |
| (d) relaxing $\mathcal S^c$ at fixed $\Psi$: $V^{\rm full}_{\rm eff}-V^{\rm trunc}_{\rm eff}$ | $0$ exactly | $\tfrac{g^4}{600}w^\top M^{-1}w+O(g^5)$; exactly $\tfrac{g^2}{24}e_c^\top(K_\Psi^{-1})_{cc}e_c$ | $\tfrac{g^4}{600}w^\top M^{-1}w+O(g^5)$ | $O(g^5)$ | same, $w$ supported on $\operatorname{Sym}^2\mathcal U^\perp$; the relaxed saddle violates (a) first at $O(g^4)$ ($S_3$), $O(g^5)$ ($S_4$); $\equiv0$ in the $\mathbb Z_2$ class |

Reading: at $S_2$ a truncated solution violates only (a); at $S_3$ and $S_4$ it violates (a) and (b) at $O(g)$ (relative for (b)). A universal $\mathcal U$ (H1) removes (a) identically and the $\mathcal U\odot\mathcal U^\perp$ part of (b) at $S_2,S_3$; what is left is (b2), the pairs of non-universal states, which no single-leg selection rule can remove. Checks: C4.1-\*, C4.2-\*, C4.3-\*, C4.4-\* (81/81 PASS with part A, log `agent/scratch/truncation-b-run1.log`).

### 4.1 Setup, and the selection rule (H1)

\subsection*{Setup}
A1–A3, and **A4**: $\mathcal H=\mathcal U\oplus\mathcal U^\perp$ with $V_2(\mathcal U,\mathcal U^\perp)=0$. In the string application $V_2=\langle\cdot,c_0^-Q\,\cdot\rangle$ is diagonal in $L_0^+$, so A4 holds for $\mathcal U$ a union of levels with $\mathcal U^\perp$ the other levels; for generic tensors it fixes $\mathcal U^\perp$ as the $V_2$-orthogonal complement. $\mathcal S=\operatorname{Sym}^2\mathcal U$, $A=V_4\vert_{\mathcal S}$ invertible (A2), $\operatorname{Sym}^2\mathcal H=\mathcal S\oplus\mathcal S^c$, $\mathcal S^c=(\mathcal U\odot\mathcal U^\perp)\oplus\operatorname{Sym}^2\mathcal U^\perp$. Blocks $A,B,D_c$, $v=(v_S,v_c)$, $w$, $M$ as in (3.4); $W:=V_5(\cdot,\cdot,\Psi)$ on $\operatorname{Sym}^2\mathcal H$, $K_\Psi=V_4-\tfrac g5W$. For $x\in\mathcal U^\perp$, $\Psi\odot x\in\mathcal U\odot\mathcal U^\perp$ is the symmetrised pair, so $V_4(\Sigma,\Psi,x)=V_4(\Sigma,\Psi\odot x)$. The EOMs of $S_4$ (R1, R17, R19 coefficients; $S_2,S_3$ by dropping terms):

$$
E_x=V_2(\Psi,x)+\tfrac g2V_3(\Psi,\Psi,x)+\tfrac{g^2}6V_4(\Sigma,\Psi,x)+\tfrac{g^3}{120}V_5(\Sigma,\Sigma,x),\qquad
e=V_4(\Sigma-P,\cdot)-\tfrac g5V_5(\Sigma,\cdot,\Psi)-\tfrac{g^2}{20}W_6(\Sigma,\Sigma,\cdot). \tag{4.1}
$$

The truncated EOM are $E_x=0$ for $x\in\mathcal U$ and $e\vert_{\mathcal S}=0$; the truncated perturbative saddle has the Taylor series

$$
\Sigma_*=p+\tfrac g5A^{-1}v_S+O(g^2)\quad(S_3,S_4),\qquad \Sigma_*=p\ \text{exactly}\quad(S_2), \tag{4.2}
$$

from $K_S\Sigma=Ap$ (3.2); $W_6$ enters $\Sigma_*$ at $O(g^2)$.

\subsection*{The selection rule}
**Sen's universality argument (stated from memory; no cached copy of Sen hep-th/9911116 was available; the argument is a standard Ward-identity consequence, written out in H1 below, not an appeal to authority).** Sen (1999) shows for open strings that the string field can be restricted consistently to the *universal subspace* — states built from the zero-momentum $SL(2,\mathbb R)$ vacuum by ghost oscillators and matter Virasoro generators — because any term of the action linear in a field outside it (with all other legs inside) is a correlator with exactly one matter leg in a non-identity Virasoro module and vanishes; so setting the outside fields to zero solves their EOM exactly, and the tachyon potential is background-independent. The same argument is the one used for the closed-string tachyon vacuum in level truncation (Yang–Zwiebach 2005, hep-th/0506077: ghost dilaton kept, matter primaries dropped). The orbifold case is intermediate: on $\mathbb C/\mathbb Z_2$ the quantum symmetry is a genuine $\mathbb Z_2$ grading with $\mathcal U$ the untwisted (even) sector; for $\mathbb Z_N$ it is a $\mathbb Z_N$ grading (untwisted charge 0, twisted sector $k$ charge $k$), which gives the one-leg rule for $\mathcal U$ untwisted, $\mathcal U^\perp$ twisted, but allows three-twisted-leg couplings ($1+1+(N-2)$), so it is not the $\mathbb Z_2$ class unless $N=2$. A restriction to twisted fields alone is not consistent: a twisted pair sources untwisted fields (charge $k+(-k)=0$).

The two forms of the rule for a subspace $\mathcal U\subset\mathcal H$, with complement $\mathcal U^\perp$:

- **one-leg rule:** $V_n(u_1,\dots,u_{n-1},x)=0$ for all $u_i\in\mathcal U$, $x\in\mathcal U^\perp$, $n=2,\dots,6$ (Sen's form);
- **$\mathbb Z_2$ class:** a linear involution with $\mathcal U$ even and $\mathcal U^\perp$ odd leaves every $V_n$ invariant, so every coupling with an odd number of $\mathcal U^\perp$ legs vanishes (a genuine symmetry: $X\to-X$ parity with $\mathcal U^\perp$ its odd sector, or $\mathbb C/\mathbb Z_2$ with $\mathcal U$ the untwisted sector).

The $\mathbb Z_2$ class implies the one-leg rule; the converse fails as soon as a coupling with three $\mathcal U^\perp$ legs is nonzero, which for the universal subspace of the closed string is the generic situation (e.g. three zero-momentum non-universal states of level $(2,2)$ with six holomorphic oscillators: a nonzero Wick contraction; stated as an expectation, not computed).

- **H1** (proposed PH; one-leg rule for the declared section). Let $\mathcal H_u\subset\mathcal H_0$ be the zero-momentum universal subspace of the closed string (matter part in the Virasoro module of the identity, any ghost excitation; level-matched, ghost number 2) and $\mathcal H_{nu}$ the zero-momentum states whose matter part lies in the other Virasoro modules. Every elementary vertex $V_n$, $n=2,\dots,6$, of the declared SL(2,C) section vanishes when exactly one leg is in $\mathcal H_{nu}$ and all others are in $\mathcal H_u$. **Motivation:** Sen's argument above; the vertices of any family built from local coordinates are moduli integrals of sphere correlators of conformally transformed states with $b$-ghost insertions; conformal maps act by exponentials of the total Virasoro generators, which preserve the matter module of each leg, and the $b$-insertions act on the ghost factor only, so the matter factor is a correlator of identity-module states with one non-identity-module state, which vanishes; nothing in the argument depends on the family (Strebel, hyperbolic, SL(2,C)). **Falsified by:** a nonzero sister-project value of $V_3(T,T,x)$, $V_4(T^3,x)$, $V_4(T^2,D,x)$ or $V_5(T^4,x)$ with $x$ a zero-momentum non-universal state (the matter primary $\eta_{\mu\nu}\alpha^\mu_{-1}\bar\alpha^\nu_{-1}\lvert0\rangle$ at level $(1,1)$ is the first test); or a failure of the argument at zero momentum in the non-compact flat matter CFT (the $\delta(0)$ factors of PH24). **Discharged by:** a written proof for the declared section including the zero-momentum normalisation, or the vanishing of those sister values. Scope: H1 is the statement for the zero-momentum block, where no conservation law helps. The nonzero-momentum states of $\mathcal U^\perp$ satisfy the one-leg rule and A4 by momentum conservation (a coupling with exactly one nonzero-momentum leg and all others at $k=0$ carries $\delta^{26}(k)$ and vanishes), so they need no hypothesis; part 2 of C4.5 uses H1 for the zero-momentum block of $\mathcal U^\perp$ and momentum conservation for the rest. H1 is about $\mathcal H_u$ as a whole; a finite $\mathcal U\subset\mathcal H_u$ (such as $\operatorname{span}(T,D)$, if $D$ is the ghost dilaton — Task 13 confirms the sister's $D$ has no matter oscillator) inherits it only towards $\mathcal H_{nu}$, not towards $\mathcal H_u\ominus\mathcal U$ (C4.3.2).

### 4.2 The components (C4.1–C4.3)

\subsection*{Derivation}

*(a) $\Psi$-EOM along $\mathcal U^\perp$, generic.* Let $x\in\mathcal U^\perp$; A4 removes $V_2(\Psi,x)$. At $S_2$, $\Sigma_*=P$ exactly and

$$
E_x\big\vert_{S_2}=\tfrac g2V_3(\Psi^2,x)+\tfrac{g^2}6V_4(\Psi^3,x)=\partial_xS^{(4)}_{\rm eff}(\Psi), \tag{4.3}
$$

the residual of the nonpolynomial level truncation at quartic vertex order, to all orders. At $S_3$ and $S_4$, insert (4.2); with $\lambda:=\Psi\odot x\in\mathcal U\odot\mathcal U^\perp\subset\mathcal S^c$, $V_4(\sigma_S,\Psi,x)=\sigma_S^\top B\lambda$ and $V_5(P,P,x)=V_5(\Psi^4,x)=v_c\cdot\lambda$:

$$
\begin{aligned}
E_x\big\vert_{S_{3,4}}
&=\tfrac g2V_3(\Psi^2,x)+\tfrac{g^2}6V_4(\Psi^3,x)+\tfrac{g^3}{30}(A^{-1}v_S)^\top B\lambda+\tfrac{g^3}{120}v_c\cdot\lambda+O(g^4)\\
&=\partial_xS^{(5)}_{\rm eff}(\Psi)+\tfrac{g^3}{30}\big[(A^{-1}v_S)^\top B\lambda-v_c\cdot\lambda\big]+O(g^4)
=\partial_xS^{(5)}_{\rm eff}(\Psi)-\tfrac{g^3}{30}\,w\cdot(\Psi\odot x)+O(g^4).
\end{aligned}\tag{4.4}
$$

$W_6$ has no $\Psi$ leg and moves $\Sigma_*$ at $O(g^2)$, so it enters $E_x$ at $O(g^4)$: (4.4) holds for both $S_4$ definitions.

*(b) $\Sigma$-EOM along $\mathcal S^c$, generic.* For $\Sigma_*\in\mathcal S$, $e_c=B^\top(\Sigma_*-p)-\tfrac g5W_{cS}\Sigma_*-\tfrac{g^2}{20}W_6(\Sigma_*,\Sigma_*,\cdot)_c$, with $W_{cS}p=v_c$. At $S_2$: $e_c=0$ exactly. At $S_3,S_4$, by (4.2):

$$
e_c=\tfrac g5\big(B^\top A^{-1}v_S-v_c\big)+O(g^2)=-\tfrac g5\,w+O(g^2). \tag{4.5}
$$

*(c) Under the one-leg rule.* Every term of $E_x$ in (4.1) at $\Psi\in\mathcal U$, $\Sigma\in\mathcal S$ is a $V_n$ with $n-1$ legs in $\mathcal U$ and the leg $x$ in $\mathcal U^\perp$; every term of $e(\varepsilon)$ with $\varepsilon\in\mathcal U\odot\mathcal U^\perp$ except the composite is likewise ($V_4(\Sigma-P,\varepsilon)$, $V_5(\Sigma,\varepsilon,\Psi)$, $V_6(\Sigma,\Sigma,\varepsilon)$). Hence, as identities in $(\Psi,\Sigma)\in\mathcal U\times\mathcal S$, not order by order:

$$
E_x\equiv0\ \ (S_2,S_3,S_4),\qquad e\vert_{\mathcal U\odot\mathcal U^\perp}\equiv0\ \ (S_2,S_3),\qquad e\vert_{\mathcal U\odot\mathcal U^\perp}=\tfrac{3g^2}{50}\,\mathcal C(P,P,\cdot)\vert_{\mathcal U\odot\mathcal U^\perp}+O(g^3)\ \ (S_4). \tag{4.6}
$$

The last entry: $\mathcal C$ contains $V_4^{-1}$ on all of $\operatorname{Sym}^2\mathcal H$, and $V_4$ couples $\mathcal U\odot\mathcal U^\perp$ to $\operatorname{Sym}^2\mathcal U^\perp$ through components with three $\mathcal U^\perp$ legs, which the one-leg rule allows; so the composite carries a single external $\mathcal U^\perp$ leg through an internal $\mathcal U^\perp$ pair. (Coefficient: $-\tfrac{g^2}{20}\cdot(-\tfrac65)=\tfrac{3g^2}{50}$; check C4.3-oneleg-S4 tests the order and the coefficient.) The $\operatorname{Sym}^2\mathcal U^\perp$ part of $w$, $v_{22}-B_{S,22}^\top A^{-1}v_S$, is built from couplings with two $\mathcal U^\perp$ legs and is not constrained: (b2) survives.

*The relaxed configuration.* Let $\Sigma^{\rm full}(\Psi)$ be the untruncated saddle at fixed $\Psi\in\mathcal U$. By the envelope theorem $E_x(\Psi,\Sigma^{\rm full})=\partial_xV^{\rm full}_{\rm eff}(\Psi)$, and $V^{\rm full}_{\rm eff}=S^{(n+2)}_{\rm eff}+(\text{feedback beyond the matched order})$ (R17, R19). The one-leg rule kills $\partial_xS^{(k)}_{\rm eff}\vert_{\mathcal U}=\sum_m\tfrac{g^{m-2}}{(m-1)!}V_m(\Psi^{m-1},x)$ for every $k$, so

$$
E_x(\Psi,\Sigma^{\rm full})=\begin{cases}\tfrac{g^4}{300}\,(\partial_xv)^\top V_4^{-1}v+O(g^5)&S_3\\ O(g^5)&S_4\ (\text{full-}\mathcal C)\end{cases} \tag{4.7}
$$

nonzero generically, since $\partial_xv=V_5(\cdot,x\odot\Psi,\Psi)+\dots$ has components with two and three $\mathcal U^\perp$ legs.

*The $\mathbb Z_2$ class.* If an involution with $\mathcal U$ even and $\mathcal U^\perp$ odd leaves all $V_n$ invariant, then $V_4$ and $W$ are block-diagonal in parity on $\operatorname{Sym}^2\mathcal H=(\mathcal S\oplus\operatorname{Sym}^2\mathcal U^\perp)_{\rm even}\oplus(\mathcal U\odot\mathcal U^\perp)_{\rm odd}$, so are $V_4^{-1}$, $\mathcal C$ and $\mathcal C_{\mathcal S}$; the source $V_4P$ is even, hence $\Sigma^{\rm full}$ is even, and every odd component of every EOM vanishes identically at the truncated and at the relaxed configuration, $S_2$ to $S_4$, both $W_6$. Breaking the symmetry in a single $V_n$ ($n=3,4,5$) switches (a) on at $O(g^{n-2})$, the first order at which $V_n$ enters $E_x$ in (4.1) with $\Sigma_*=P+O(g)$; breaking it in $V_6$ leaves (a) at zero and switches (b1) on at relative $O(g^2)$.

*The two axes (C4.3.2).* Let $\mathcal H_u=\mathcal U\oplus\mathcal U'$ be closed under the rule and $\mathcal U\subsetneq\mathcal H_u$ (the tachyon–dilaton truncation inside the universal subspace: $\mathcal U'$ = the universal states outside $\operatorname{span}(T,D)$, higher levels and any other level-$(1,1)$ universal state). The rule constrains couplings with one leg in $\mathcal H_{nu}$ only: (a) along $\mathcal H_{nu}$ vanishes identically, (a) along $\mathcal U'$ is the generic (4.3)–(4.4), starting at $O(g)$ with $\tfrac12V_3(\Psi^2,x)$ — the ordinary level-truncation error, with the same coefficients as in the nonpolynomial theory through $O(g^2)$. The field-content axis ($\mathcal U$ inside $\mathcal H_u$, $\mathcal S$ inside $\operatorname{Sym}^2\mathcal H$) and the level axis (the finite $\mathcal H=\mathcal H^{(L)}$ inside $\mathcal H_0$) are independent: everything in §4 is exact at fixed $\mathcal H$, and the $L\to\infty$ behaviour of $w$, $M$ and $(K_\Psi^{-1})_{cc}$ (inverses on $\operatorname{Sym}^2\mathcal H^{(L)}$) is the PH1/PH3/PH21 question, not addressed here. A finite worldsheet-level truncation of $\mathcal H$ adds exactly two things: $\mathcal U'$ and $\mathcal H_{nu}$ are cut at level $L$ (so the residuals (a) along $\mathcal U'$ and (b) along $\mathcal S^c$ are only computed up to level $L$), and $V_4^{-1}$ in $\mathcal C$ is replaced by its level-$L$ inverse (the full-$\mathcal C$ vertex is then level-dependent; $W_6^{(\mathcal S)}$ is not).

### 4.3 Absorption and the theorem (C4.4, C4.5)

\subsection*{Derivation}

*Relaxation at $S_3$, exact.* $S_3$ is quadratic in $\Sigma$ with Hessian $-\tfrac{g^2}{12}K_\Psi$. At the truncated saddle its gradient is $(0,-\tfrac{g^2}{12}e_c)$ on $\mathcal S\oplus\mathcal S^c$; the stationary value over all of $\operatorname{Sym}^2\mathcal H$ at fixed $\Psi$ therefore differs from the truncated one by

$$
V^{\rm full}_{\rm eff}-V^{\rm trunc}_{\rm eff}=-\tfrac12\Big(\tfrac{g^2}{12}\Big)^2e_c^\top\Big(-\tfrac{12}{g^2}\Big)(K_\Psi^{-1})_{cc}\,e_c=\tfrac{g^2}{24}\,e_c^\top(K_\Psi^{-1})_{cc}\,e_c\qquad(S_3,\ \text{exact}), \tag{4.8}
$$

wherever $K_\Psi$ and $K_S$ are invertible; $(K_\Psi^{-1})_{cc}=M_\Psi^{-1}$, $M_\Psi$ the Schur complement of $K_S$ in $K_\Psi$, $M_{\Psi}\to M$ as $g\to0$. With (4.5), the leading term is $\tfrac{g^2}{24}\cdot\tfrac{g^2}{25}w^\top M^{-1}w=\tfrac{g^4}{600}w^\top M^{-1}w$: 057's Schur term (3.5), now read as the second-order response of the action to the violated component.

*Relaxation at $S_4$.* The $W_6$ term changes the Hessian at relative $O(g^2)$ and adds a cubic term in the shift $\delta\Sigma=O(g)$ of order $g^4\delta\Sigma^3=O(g^7)$, so with the full-$\mathcal C$ vertex $V^{\rm full}_{\rm eff}-V^{\rm trunc}_{\rm eff}=\tfrac{g^4}{600}w^\top M^{-1}w+O(g^5)$, consistent with (3.6) and R19 ($V^{\rm full}_{\rm eff}=S^{(6)}_{\rm eff}+O(g^5)$). With $W_6^{(\mathcal S)}$, compared with R19's untruncated $S_4$: the two truncated actions differ by $\tfrac{g^4}{720}(W_6^{(\mathcal S)}-W_6)(\Sigma^3)$, which moves the saddle at $O(g^2)$ (Hessian $\propto g^2$) and hence the value, at second order, only at $O(g^2\cdot(g^2)^2)=O(g^6)$, so

$$
V^{\rm R19,full}_{\rm eff}-V^{(4,\mathcal S)}_{\rm eff}=\tfrac{g^4}{600}w^\top M^{-1}w-\tfrac{g^4}{720}\cdot\tfrac65(\mathcal C-\mathcal C_{\mathcal S})(P^3)+O(g^5)=\tfrac{g^4}{600}\big[w^\top M^{-1}w-vV_4^{-1}v+v_S^\top A^{-1}v_S\big]+O(g^5)=O(g^5) \tag{4.9}
$$

by (3.4). The price is (c): $W_6^{(\mathcal S)}$ is not the restriction of R19's $W_6$, so the untruncated $\Sigma$-EOM along $\mathcal S$ is violated,

$$
e\vert_{\mathcal S}=-\tfrac{g^2}{20}(W_6-W_6^{(\mathcal S)})(\Sigma_*,\Sigma_*,\cdot)\vert_{\mathcal S}=\tfrac{3g^2}{50}(\mathcal C-\mathcal C_{\mathcal S})(P,P,\cdot)\vert_{\mathcal S}+O(g^3), \tag{4.10}
$$

and the two violations — (b) along $\mathcal S^c$ at relative $O(g)$, (c) along $\mathcal S$ at relative $O(g^2)$ — cancel in the potential through $O(g^4)$ (4.9).

\subsection*{Commentary}

- (4.3): at $S_2$ the cubic theory's truncated $\Psi$-EOM residual is *identical* to that of the nonpolynomial theory truncated to $\mathcal U$ at quartic vertex order, because $\Sigma_*=P$ exactly.
- (4.4): the $O(g^3)$ deviation from the nonpolynomial residual is the same $w$ as in (4.5), contracted with the pair $\Psi\odot x$: the truncated saddle misses $V_4^{-1}v$ exactly in the direction $w$. Coefficient: $\tfrac1{120}-\tfrac1{24}=-\tfrac1{30}$ and $\tfrac16\cdot\tfrac15=\tfrac1{30}$; the bracket is $-w\cdot\lambda$ because $\lambda\in\mathcal S^c$ ($\lambda_S=0$).
- (4.5): the only input is (4.2) and $W_{cS}p=v_c$; at $S_2$ the vanishing is exact because $P\in\mathcal S$ (Veronese closure, C1.1).
- (4.6): the identities hold for all $(\Psi,\Sigma)\in\mathcal U\times\mathcal S$, not only on shell and not only order by order: they survive at the vacuum scale $\tau=O(1)$.
- (4.7): envelope theorem plus R17's exact rewriting $V^{(3)}_{\rm eff}=S^{(5)}_{\rm eff}+\tfrac{g^4}{600}vK_\Psi^{-1}v$; the derivative of $K_\Psi^{-1}$ is $O(g^5)$.
- (4.8): exact because $S_3$ is quadratic in $\Sigma$; the sign of $w^\top M^{-1}w$ is indefinite ($M$ indefinite), so relaxing may raise or lower the potential.
- (4.9): the first equality combines (3.6) and the envelope argument; the second uses $(\mathcal C-\mathcal C_{\mathcal S})(P^3)=vV_4^{-1}v-v_S^\top A^{-1}v_S$ (C3.6-CS) and $\tfrac65\cdot\tfrac1{720}=\tfrac1{600}$; the third is (3.4).

\subsection*{Result}

**Theorem (C4.5).** Let $\mathcal S=\operatorname{Sym}^2\mathcal U$, $A=V_4\vert_{\mathcal S}$ invertible, A4, and let $(\Psi_*,\Sigma_*)$ solve the truncated EOM of $S_n$ on the perturbative branch; orders are Taylor orders in $g$ at fixed $\Psi_*$.

1. *(Generic vertices.)* In the untruncated $S_n$, the violated components are (a) the $\Psi$-EOM along $\mathcal U^\perp$ from $O(g)$, equal to the level-truncation residual of the nonpolynomial theory exactly at $S_2$ and through $O(g^2)$ at $S_3,S_4$, with the $O(g^3)$ deviation $-\tfrac{g^3}{30}w\cdot(\Psi\odot x)$; and (b), at $S_3$ and $S_4$ only, the $\Sigma$-EOM along $\mathcal S^c$ at relative $O(g)$, $e_c=-\tfrac g5w+O(g^2)$; and (c), for the $W_6^{(\mathcal S)}$ truncation only, the $\Sigma$-EOM along $\mathcal S$ at relative $O(g^2)$, (4.10). At $S_2$ the $\Sigma$-EOM holds exactly.
2. *(Under H1, with $\mathcal U^\perp\subset\mathcal H_{nu}$: the zero-momentum block by H1, the nonzero-momentum block by momentum conservation; for $\mathcal U=\mathcal H_u\cap\mathcal H$ in the finite layer A1.)* (a) vanishes identically at every order; at $S_2$ the truncated solution is an exact solution of the untruncated $S_2$; at $S_3$ the only violated component is the $\Sigma$-EOM along $\operatorname{Sym}^2\mathcal U^\perp$, at relative $O(g)$, sourced by $w$; at $S_4$ the $\Sigma$-EOM along $\mathcal U\odot\mathcal U^\perp$ is violated in addition at relative $O(g^2)$ through the composite $\mathcal C$ (zero in the $\mathbb Z_2$ class).
3. *(Absorption.)* Relaxing the violated $\mathcal S^c$ components at fixed $\Psi_*$ changes the potential by $\tfrac{g^2}{24}e_c^\top(K_\Psi^{-1})_{cc}e_c$ (exact at $S_3$), i.e. $\tfrac{g^4}{600}w^\top M^{-1}w+O(g^5)$ at $S_3$ and at $S_4$ full-$\mathcal C$, which is 057's Schur term; with $W_6^{(\mathcal S)}$ the change is $O(g^5)$: the truncated potential equals R19's fully relaxed potential through $O(g^4)$. The truncated solution is thus consistent through the matched order ($O(g^3)$ at $S_3$, $O(g^4)$ at $S_4$ with $W_6^{(\mathcal S)}$), and its failure at the next order is the $\mathcal S^c$ feedback; under H1 alone the relaxed configuration violates (a) first at exactly that order, $O(g^4)$ at $S_3$ and $O(g^5)$ at $S_4$ (4.7).

\subsection*{Scope and interpretation}

- *Class.* Generic real symmetric tensors in a finite $\mathcal H$ (A1), perturbative branch (Taylor coefficients); part 2 conditional on H1 (zero-momentum block of $\mathcal U^\perp$; "untruncated $S_2$" is $S_2$ on $\mathcal H$, the residual along $\mathcal H_u\ominus\mathcal H$ being C4.3.2's). The exact statements — (4.6), the $S_2$ exactness, (4.8) — hold at any field value where the inverses exist; the order statements are formal.
- *At the vacuum.* All of $S_n$ is $g$-independent in $(\tau,s)=(g\Psi,g^2\Sigma)$ (C2.8), so "violated at relative $O(g)$" becomes "violated at $O(1)$ in scaled units": at a tachyon-vacuum candidate $\tau_*=O(1)$, the $\Sigma$-EOM residual along $\operatorname{Sym}^2\mathcal U^\perp$ is $-\tfrac15w(\tau_*)$ plus higher terms of the same size, and the quantity that measures what the truncation misses is the exact relaxation energy (4.8) evaluated at $\tau_*$ (at $S_3$; at $S_4$ the action is cubic in $\Sigma$ and no closed formula exists, so it is the difference of the two saddle values, computed numerically, as C4.4-S4C does in series form). That number, not an order count, is what Task 13 should report next to the vacuum energy.
- *What a paper can quote.* "Under the universality selection rule, a solution of the tachyon–dilaton truncation of the cubic theory solves the $\Psi$-equations of motion along all non-universal directions exactly; along the universal directions of higher level it has the level-truncation error of the nonpolynomial theory; the auxiliary equations are violated only along pairs of non-universal states, and eliminating those auxiliaries changes the potential by the relaxation energy (4.8), of order $g_s^4\Psi^6$ in the perturbative regime and cancelled at that order by the $\mathcal S$-consistent sextic vertex."
- *Not covered: gauge-fixed directions.* In the string application $\mathcal U$ lies in Siegel gauge; the non-Siegel ghost-number-2 states of the same levels belong to $\mathcal U^\perp$, are universal (H1 does not remove them), and A4 is not established for them ($V_2$ is level-diagonal but need not be block-diagonal between Siegel and non-Siegel states of one level). Their EOM components are the out-of-gauge equations of level truncation; if A4 fails there, (a) along them starts at $O(1)$ in the counting. Settling this needs the explicit kinetic operator at levels $0$ and $(1,1)$ — Task 13 input, not done here. The gauge structure of $\Sigma$ (PH12) is likewise untouched.
- *Sourcing chain (why the violations sit at the unmatched order).* Under the one-leg rule alone the universal sector of the cubic theory is not closed at $S_3$: a non-universal pair $\Sigma_{22}=O(g)$ is sourced by $w$, it sources the mixed sector through the three-$\mathcal U^\perp$-leg block of $V_4$, and that feeds (a) at $O(g^4)$; the nonpolynomial theory's universal sector is closed. The two agree exactly through the matched order because the chain telescopes ($V_4V_4^{-1}v\cdot\lambda=V_5(\Psi^4,x)=0$ under H1, R17), so the violations at $S_n$ are the feedback beyond the matched order and nothing else.
- *$D=0$.* The $(t,\sigma)$ model of §2 is the $\mathcal U=\operatorname{span}(T)$ instance of §4: the dilaton lies in $\mathcal U'$ (universal, C4.3.2), so (a) along $D$ is $\tfrac g2V_3(T^2,D)+\tfrac{g^2}6V_4(T^3,D)+\dots$, the Yang–Zwiebach dilaton equation, and (b2) is along $\operatorname{Sym}^2$ of everything else.
- *Limits.* $g\to0$: every residual vanishes ($[g^0]$ checks). $V_5\to0$: $S_3=S_2$, $\Sigma_*=P$, (b) vanishes to all orders (C4.2-V5zero). $\mathcal U=\mathcal H$: $\mathcal U^\perp=\mathcal S^c=0$, nothing is violated, and C4.5 reduces to the untruncated statements R17/R19 (not machine-checked: the check would compare empty arrays).

### 4.4 Verification (checks C4.\*)

\subsection*{Verification}
Script `codes/verify-truncation-structure.py`, block C4 (appended; part A untouched), log `agent/scratch/truncation-b-run1.log`: **81/81 PASS** (45 part A + 36 part B; of the 11 checks labelled `-break` in the log, 7 are falsifying legs, `expect_fail`, and 4 are the positive symmetry-breaking checks C4.3-break3/4/5/6 of C4.3.1), exit 0. Model: generic real symmetric $V_2,\dots,V_6$ on $\mathcal H=\mathbb R^6$, $\dim\mathcal U=2$ ($\dim\mathcal S=3$, $\dim\mathcal S^c=18$), $V_2$ block-diagonal (A4), seeds 20260927–20260929, $\Psi$ a random unit vector in $\mathcal U$. **Method:** exact Taylor coefficients in $g$ through $g^6$ — $g$ nilpotent of order 7, i.e. truncated power series, the one-variable form of the `MD` technique of `codes/verify-gauge-algebra-ogs4.py` (deviation from the brief's wording: one nilpotent variable of order 7 rather than products of first-order duals; same content, cheaper). The saddle series is computed from the EOM by recursion ($\Sigma$-EOM solved order by order), the EOM residuals and potentials are then evaluated from (4.1) and the actions; predicted coefficients ($w$, $M$ from (3.4), $\partial S^{(n)}_{\rm eff}$, $\mathcal C$, $\mathcal C_{\mathcal S}$) are computed separately from their definitions. Break legs are strict: the wrong statement must fail on every seed and every theory.

- C4.1: $[g^0]$ of (a) $=0$ and $[g^1]=\tfrac12V_3(\Psi^2,\cdot)\neq0$ at $S_2,S_3,S_4^{\mathcal C},S_4^{(\mathcal S)}$ (break: $V_2(\mathcal U,\mathcal U^\perp)\neq0$ switches (a) on at $O(1)$, detected); (4.3) at all orders at $S_2$; (4.4) $[g^3]$ deviation $=-\tfrac1{30}w\cdot(\Psi\odot x)$ (break: opposite sign fails).
- C4.2: $e_c\equiv0$ at $S_2$ through $g^6$; $[g^0]=0$, $[g^1]=-w/5$ at $S_3$ and both $S_4$ (break: $+w/5$ fails); $V_5=0$ gives $e_c\equiv0$ at $S_3$.
- C4.3 ($\mathbb Z_2$ class): (a) and (b1) vanish through $g^6$ at all four theories; (b2) $[g^1]=-w_{22}/5\neq0$; the relaxed saddle has no $\mathcal U\odot\mathcal U^\perp$ component and (a) $\equiv0$ there. Breaking the symmetry in $V_3$, $V_4$, $V_5$ alone switches (a) on at exactly $g^1,g^2,g^3$ (all lower coefficients zero); in $V_6$ alone, (a) stays zero and (b1) appears at exactly $g^2$. One-leg class: (a) $\equiv0$ at all theories, (b1) $\equiv0$ at $S_2,S_3$, (b1) at $S_4$ first at $g^2$ with coefficient $\tfrac3{50}\mathcal C(P,P,\cdot)$ (4.6); relaxed saddle: (a) first at $g^4$ ($S_3$, coefficient (4.7), break $\tfrac12$(4.7) fails) and $g^5$ ($S_4^{\mathcal C}$). Level axis ($\mathcal U\oplus\mathcal U'$ even, $\dim\mathcal U'=2$): (a) $\equiv0$ along the odd sector, $\neq0$ at $g^1$ along $\mathcal U'$.
- C4.4: $V^{\rm full}_{\rm eff}-V^{\rm trunc}_{\rm eff}$ (both from the series): $\equiv0$ at $S_2$; zero through $g^3$ and $[g^4]=w^\top M^{-1}w/600$ at $S_3$ and $S_4^{\mathcal C}$; zero through $g^4$ for $W_6^{(\mathcal S)}$ against R19's $S_4$ (break: the Schur value is not found there); response form $\tfrac1{24}e_{1,c}^\top M^{-1}e_{1,c}=w^\top M^{-1}w/600$; series-independent route: exact linear $S_3$ saddles at $g=2\cdot10^{-3},10^{-3}$, Richardson, $\Delta V/g^4\to w^\top M^{-1}w/600$ at $10^{-5}$ of the cancellation-free scale $\lVert w\rVert^2\lVert M^{-1}\rVert/600$ (values $0.017003$, $-0.000381$, $0.008286$; $M$ indefinite, so $w^\top M^{-1}w$ is much smaller than its scale on two seeds; break: opposite sign fails); (4.8) exact at $g=0.3$ to $10^{-10}$ (break: the leading Schur term alone is not exact there); (4.10): $e\vert_{\mathcal S}$ zero at $g^0,g^1$ and $[g^2]=\tfrac3{50}(\mathcal C-\mathcal C_{\mathcal S})(P,P,\cdot)\vert_{\mathcal S}\neq0$.

Not machine-checked: H1 itself (a property of the string vertices; no CFT value computed); the $\mathcal U=\mathcal H$ limit (empty); anything beyond the finite algebraic layer (level $L\to\infty$); the non-perturbative branch of $S_4$.

## Next

Part B (separate brief): the consistency theorem — for a solution $(\Psi_*,\Sigma_*)$ of the truncated EOM, which components of the untruncated EOM off $(\mathcal U,\mathcal S)$ are violated and at which order. Pointers from §3: the $\Sigma$-EOM components along $\mathcal S^c$ are sourced through $B$ and $v_c$ (the combination $w$ of (3.4)); the $\Psi$-EOM components off $\mathcal U$ are $V_n(\Psi_*^{n-1},\cdot)\vert_{\mathcal U^\perp}$ as in level truncation. Task 13: insert the sister numbers and locate $\tau_{\rm pole}$ and $\tau^\pm_{\rm fold}$ relative to the tachyon vacuum ($\tau_{\rm pole}/\tau_0=-5V_4V_3/(2V_2V_5)$). Numbers needed: $V_2$, $V_3(T^3)$ (and $V_3(TD^2)$), $h_0,\dots,h_4$ in the $e_i$ coordinate basis (R43), $\{T^{5-k}D^k\}$, $k=0..5$ (missing), and $W_6^{(\mathcal S)}$ on $\mathrm{Sym}^2\mathcal U$: $V_6(T^{6-k}D^k)$ and $\mathcal C_{\mathcal S}$ from $V_5$ and $A^{-1}$.

Part B done (§4). For Task 13: (i) confirm that the sister's $D$ has no matter oscillator (ghost dilaton), so that $\operatorname{span}(T,D)\subset\mathcal H_u$ and H1 applies towards $\mathcal H_{nu}$; (ii) report, next to the vacuum energy, the relaxation energy (4.8) at $\tau_*$ — this needs $V_4$, $V_5$ on the pairs $\operatorname{Sym}^2\mathcal U^\perp$ at the lowest level (non-universal pairs and universal level-$(2,2)$ partners), not available; without them, state the truncated solution's $\mathcal S^c$ residual as the open error term; (iii) the level-axis residual (a) along universal states of level $(2,2)$ is the ordinary level-truncation error and is estimated as in Yang–Zwiebach, not by the cubic theory.

## Proposed ledger row

"Finite-field truncation of the cubic HS theory (algebraic layer, generic real symmetric tensors). For $\mathcal U\subset\mathcal H$ and $\mathcal S=\mathrm{Sym}^2\mathcal U$ with $A=V_4\vert_{\mathcal S}$ invertible, eliminating $\Sigma$ gives: at $S_2$, exactly the level-$\mathcal U$ quartic potential; at $S_3$, a rational potential with denominator $\det K_{\mathcal S}(\Psi)$, equal to $S^{(5)}_{\rm eff}\vert_{\mathcal U}+\tfrac{g^4}{600}v_S^\top A^{-1}v_S+O(g^5)$; at $S_4$, with R19's $W_6$ built on the full $V_4^{-1}$ (not computable inside a truncation), $S^{(6)}_{\rm eff}\vert_{\mathcal U}-\tfrac{g^4}{600}w^\top M^{-1}w+O(g^5)$, the Schur term nonzero for generic tensors, and $w=0$ iff pointwise $V_4^{-1}V_5(\cdot,P,\Psi)\in\mathcal S$ (the scalar $w^\top M^{-1}w$ can also vanish with $w\neq0$, $M$ being indefinite); with the $\mathcal S$-consistent composite $W_6^{(\mathcal S)}=V_6-\tfrac65\mathcal C_{\mathcal S}$ ($A^{-1}$ in place of $V_4^{-1}$; the vertex to use in truncations), $S^{(6)}_{\rm eff}\vert_{\mathcal U}+O(g^5)$ without enlarging $\mathcal S$. One-field model: $\sigma_*=V_4t^2/(V_4-\tfrac g5V_5t)$, simple pole at $t_{\rm pole}=5V_4/(gV_5)$ at $S_3$ with no finite saddle there; at $S_4$, on the perturbative branch, the pole is replaced by a fold at $\tau^\pm_{\rm fold}=5V_4/(V_5\pm\sqrt{5W_6V_4})$ (real iff $W_6V_4>0$; for $W_6V_4<0$ a finite saddle exists at $t_{\rm pole}$). All these scales are at $gt=O(1)$ (exact scaling), so the matchings are formal (Taylor coefficients through $\Psi^5$ or $\Psi^6$), not accuracy statements at the tachyon vacuum."
Status: **Proven – Verified** (script 45/45 PASS, run 2), within the algebraic layer. No PH (PH14 dropped: it scopes why R19's $W_6$ is dressed, while every identity here holds for arbitrary tensors with $W_6$ given). Task 14: the degenerate-branch condition of the Remark after §2 Result (former C2.5).

### Part B (§4): proposed as a new row, not an addendum to R61 (final text after fix pass 1)

R61 is unconditional; part B carries a hypothesis for its part 2 and answers a different question, so a new row is cleaner, with R61 cited. The row and PH28 entry below are the critic's text; the ID R62 is the critic's placeholder, the orchestrator assigns the registered ID.

**Row (R62, replacing the record's draft; changes: A4 caveat, $\mathcal U^\perp\subset\mathcal H_{nu}$, component (c), momentum sentence).**

"Finite-field truncation II — which untruncated EOM a truncated solution solves (derivation 057 §4, algebraic layer, generic real symmetric tensors, perturbative branch; orders = Taylor orders in $g$ at fixed $\Psi$). For $\mathcal S=\operatorname{Sym}^2\mathcal U$, $A=V_4\vert_{\mathcal S}$ invertible and $V_2(\mathcal U,\mathcal U^\perp)=0$ (true between levels; same-level out-of-Siegel-gauge directions not covered): a solution of the truncated EOM of $S_n$ violates in the untruncated $S_n$ (a) the $\Psi$-EOM along $\mathcal U^\perp$ from $O(g)$, equal to the nonpolynomial level-truncation residual exactly at $S_2$ and through $O(g^2)$ at $S_3,S_4$ (deviation $-\tfrac{g^3}{30}w\cdot(\Psi\odot x)$), and (b), at $S_3,S_4$ only, the $\Sigma$-EOM along $\mathcal S^c$ at relative $O(g)$, $e_c=-\tfrac g5w+O(g^2)$ with R61's $w$; at $S_2$ the $\Sigma$-EOM holds exactly. Relaxing $\mathcal S^c$ at fixed $\Psi$ changes the potential by $\tfrac{g^2}{24}e_c^\top(K_\Psi^{-1})_{cc}e_c$ (exact at $S_3$) $=\tfrac{g^4}{600}w^\top M^{-1}w+O(g^5)$, R61's Schur term; with $W_6^{(\mathcal S)}$ the truncated potential equals R19's fully relaxed one through $O(g^4)$, at the price of (c): the untruncated $\Sigma$-EOM along $\mathcal S$ violated at relative $O(g^2)$ by $\tfrac3{50}(\mathcal C-\mathcal C_{\mathcal S})(P,P,\cdot)$. Under the one-leg universality rule (PH28) with $\mathcal U^\perp$ inside the zero-momentum non-universal space (nonzero momenta drop out by momentum conservation): (a) vanishes identically in the fields; the truncated $S_2$ solution solves the untruncated $S_2$ exactly; at $S_3$ the only violated component is the $\Sigma$-EOM along pairs of non-universal states, sourced by $w$; at $S_4$ also the $\Sigma$-EOM along universal–non-universal pairs at relative $O(g^2)$ through $\mathcal C$; the relaxed configuration violates (a) first at the first unmatched order, $O(g^4)$ at $S_3$, $O(g^5)$ at $S_4$. In the $\mathbb Z_2$ class (a genuine grading, $\mathcal U$ even, $\mathcal U^\perp$ odd, e.g. $X\to-X$ or $\mathbb C/\mathbb Z_2$ with $\mathcal U$ untwisted) every odd component vanishes identically, relaxed configuration included. For a finite $\mathcal U\subsetneq\mathcal H_u$ (tachyon–dilaton) the rule acts towards $\mathcal H_{nu}$ only; along higher universal levels (a) is the ordinary level-truncation error. At the vacuum scale $gt=O(1)$ the order counting is formal; the exact statements are the identities under the rule, the $S_2$ exactness and the relaxation energy."

Status: **Proven – Verified** (C4.1, C4.2, C4.4; C4.3.1 for the $\mathbb Z_2$ class) and **Conditional(PH28) – Verified** (C4.3, C4.3.2, C4.5 part 2); `codes/verify-truncation-structure.py` 81/81 PASS, seed 20260926, log `agent/scratch/truncation-b-run1.log`; critic `agent/reports/critic-057-partB-20260930T233100.md` (0 critical, 0 major, 9 minor). Scope sentence: algebraic layer at fixed finite $\mathcal H$; the level axis ($L\to\infty$ behaviour of $w$, $M$, $(K_\Psi^{-1})_{cc}$) is PH1/PH3/PH21; same-level out-of-Siegel-gauge directions, the identity of the sister's $D$ with the ghost dilaton, and (4.8) at the vacuum not covered.

**PH28 (in the ledger's section format, not a table row):**

```
### PH28 (057 H1) — One-leg universality selection rule for the declared SL(2,C) section [open]

- **Source**: `agent/derivations/057-finite-field-truncation.md` §4.1 (H1), claim-tree node H1
- **Scope**: zero-momentum, level-matched, ghost-number-2 sector; H_u = matter part in the identity Virasoro module (any ghost part), H_nu = matter part in another module; nonzero-momentum legs are covered by momentum conservation, not by this hypothesis
- **Verification**:
  - 2026-09-30 – critic review – `agent/reports/critic-057-partB-20260930T233100.md` – declared with motivation and falsifier; carried in every dependent node
- **Motivation**: Sen's universality argument (hep-th/9911116; Yang–Zwiebach hep-th/0506077 for closed strings), which is a Ward-identity statement: every V_n is a moduli integral of a sphere correlator of conformally transformed states with b-insertions; conformal maps preserve the matter module of each leg and b-insertions act on the ghost factor, so the matter factor is a correlator of identity-module states with one non-identity state, which vanishes; independent of the vertex family. Strictly weaker than a Z_2 grading (three-non-universal-leg couplings are allowed and generically nonzero).
- **Would be falsified by**: a nonzero sister-project value of V_3(T,T,x), V_4(T^3,x), V_4(T^2 D,x) or V_5(T^4,x) with x in H_nu (first test x = eta_{mu nu} alpha^mu_{-1} alphabar^nu_{-1}|0>); a failure of the argument at zero momentum in the non-compact matter CFT (PH24's delta(0) factors)
- **Discharged by**: a written proof for the declared section including the zero-momentum normalisation, or those sister values vanishing
- **Used by**: R62 (C4.3, C4.3.2, C4.5 part 2)
```

