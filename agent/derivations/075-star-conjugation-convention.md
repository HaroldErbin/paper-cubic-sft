# 075 — Reality conditions of the cubic theory in the book's star-conjugation convention

**Date:** 2026-10-03 (Fable, computator; briefs
`agent/briefs/done-computator-075-star-conjugation-20261003T174500.md` (skeleton, cut) and
`agent/briefs/active-computator-075-star-conjugation-cont-20261003T204500.md` (continuation)).
**Machine check:** `agent/computations/verify-075-star-conjugation.py` (see §Verification).
**Inputs (read by line range):** book [Erbin 2023]
(`chapters/cft_operator_formalism.tex` l. 700–760, 860–970, 1095–1135, 1183–1345, 1470–1510,
1670–1710, 2070–2200, 2430–2500; `chapters/formulas.tex` l. 140–210; `chapters/conventions.tex`
l. 790–815; `chapters/cft_systems.tex` l. 1230–1290; `chapters/bsft_free_brst.tex` l. 215–260,
1340–1370; `includes/commands.tex` l. 77, 93–95); record 028 §1 and addendum P.1–P.7;
`knowledge/conventions.md` C1, C3; `knowledge/results.md` R35, R58, PH7;
`paper/sections/A-conventions.tex` (Pairing, Multi-string pairing, Vertices, Reality);
Zwiebach 1993 (hep-th/9206084).

## Task and objective

**Literal task.** Define the book's star conjugation $A^\star := (A^t)^\dagger = (A^\dagger)^t$
on the states of the closed-string Fock space (modes, momentum, $c$-numbers, words, tensor
products); relate it to the paper's $A^\ddagger = (-1)^{N_{\rm gh}(A)+1}\mathrm{bpz}^{-1}(\mathrm{hc}(A))$;
write the reality condition of every field of the paper as $X^\star = \varepsilon_X X$; rewrite the
equivariance statements (pairing, $n$-string pairing, $Q_B$, vertices, products) with $\star$; check
on explicit states with a companion script.

**Objective.** Appendix A of the paper states the conventions with $\star$ (no sign in the
conjugation, as in the book and as in Zwiebach (3.6)) and appendix B derives the reality
conditions from them. Every sign of the paper's reality statements must trace to this record.

**Summary of the outcome.** $\star = \mathrm{bpz}^{-1}\circ\mathrm{hc}$ acts on a creation word by (1.3) (coefficient conjugated, momentum flipped, sign $(-1)^{k_o(k_o-1)/2}\prod s_{O_i}$), $\star^2 = 1$; the former $\ddagger = (-1)^{N_{\rm gh}+1}\star$. Reality: $\Psi^\star = -\Psi$, $\Lambda^\star = -\Lambda$ (its interaction part under H1 = PH6), $\Sigma_k^\star = (-1)^k\Sigma_k$ and $\Upsilon_2^\star = \Upsilon_2$ (forced through the sources under H1, via R35), $\Theta_k^\star = \Theta_k$. Equivariance: pairing $-1$, $\omega_n$ $(-1)^n$, $(Q_BA)^\star = (-1)^{|A|+1}Q_BA^\star$, vertices $(-1)^{n+\sum_{i<j}|A_i||A_j|}$ (under H1 for $n\ge3$; the products and the reality of the actions likewise). The wrong-sign partner is written $\Upsilon_2$ (the paper's name; appendix A's $\Xi_2$ at l. 287–304 is to be renamed). Script 79/79 PASS (2026-10-04; 76/76 on 2026-10-03 before the fix pass). See §Result for the per-display signs of appendix A.

## Conventions and assumptions

- **A1** Sphere normalisation, ghost numbers, $c_0^\pm$, $b_0^\pm$: the project conventions and C1(iv):
  $\langle c_{-1}\bar c_{-1}c_0\bar c_0c_1\bar c_1\rangle = -1$, hence
  $\langle c_{-1}\bar c_{-1}c_0^-c_0^+c_1\bar c_1\rangle = -\tfrac12$; physical ghost number,
  $|A| = N_{\rm gh}(A) \bmod 2$.
- **A2** BPZ conjugation: C1(ii)–(iii) (the $I^-$ mode rule $\phi_n^t = (-1)^h(-1)^n\phi_{-n}$;
  on a creation word, order kept, no conjugation of $c$-numbers; as an operator map, the graded
  anti-automorphism $(XY)^t = (-1)^{|X||Y|}Y^tX^t$, book l. 1147–1154, 028 P.4). The book's
  closed-string table uses $I^+$, $\phi_n^t = (-1)^h\phi_{-n}$; the two agree on level-matched
  states (028 P7.5), and every state of this record is level-matched. On a ket built on a
  momentum state, $\mathrm{bpz}(O_1\cdots O_k|0,p\rangle) = \langle 0,-p|\,O_1^t\cdots O_k^t$
  (book `cft_systems.tex` l. 1258–1264, $\langle -k| = |k\rangle^t$; Zwiebach (3.8)).
- **A3** Hermitian conjugation $\mathrm{hc}$: the book's Euclidean Hermitian adjoint
  `cft:eq:conj-herm` (Wick rotation of the Lorentzian adjoint `cft:eq:conj-herm-lorentz`), on modes
  $\phi_n^\dagger = \phi_{-n}^+$ with $\phi^+ = \phi$ for the Hermitian fields $b$, $c$, $i\partial X$
  (`cft:eq:chiral-modes-adj`; closed-string table `bos_worldsheet_cft.tex` l. 1130–1213:
  $c_n^\dagger = c_{-n}$, $b_n^\dagger = b_{-n}$, $\alpha_n^\dagger = \alpha_{-n}$, barred alike);
  on a ket, $\mathrm{hc}(\lambda\,O_1\cdots O_k|0,p\rangle) = \lambda^*\langle 0,p|\,O_k^\dagger\cdots O_1^\dagger$
  (order reversed, no sign, $c$-number conjugated; `formulas.tex` l. 193; Zwiebach (2.32)–(2.34)).
  This is the book's $\eadj{(\cdot)}$, typeset $^\ddagger$ there — a bra, not the paper's involution.
- **A4** $Q_B^\dagger = Q_B$, $Q_B^t = -Q_B$, $|Q_B| = 1$ (book `bos_worldsheet_cft.tex` l. 1244–1247);
  $(c_0^\pm)^\dagger = c_0^\pm$, $(c_0^\pm)^t = -c_0^\pm$ (`bos:eq:conjugation-c0pm-b0pm`).
- **A5** (convention fixed here, candidate ledger entry) On a tensor product $\star$ acts strand by
  strand, $(A_1\otimes\cdots\otimes A_k)^\star := A_1^\star\otimes\cdots\otimes A_k^\star$, without a
  Koszul reordering sign (same choice as 028 (C2) and the paper's current text). The alternative,
  with the sign $(-1)^{\sum_{i<j}|A_i||A_j|}$, is discussed in §6.
- **A6** All fields of the paper carry commuting ($\mathbb C$-valued) coefficients on states of fixed
  ghost number (`A-conventions.tex` l. 49–55): $\Psi$ ($N_{\rm gh}=2$), $\Lambda$ (1), $\Sigma_k$ and
  $\Upsilon_2$ (strands at 2; the wrong-sign partner, written $\Xi_2$ in appendix A l. 287–304), $\Theta_k$ (strands at 3). Zwiebach's Grassmann-odd coefficients on odd
  states appear only in the translation step C4.3 and in the antifield remark.
- **A7** Pairing: $\langle A,B\rangle := \langle A|c_0^-|B\rangle$, $\langle A|=\mathrm{bpz}(A)$, symmetric on
  its support (C1, R58). $n$-string pairing: $\omega_n(\otimes A_i,\otimes B_i) =
  (-1)^{\sum_{i<j}|B_i||A_j|}\prod_i\langle A_i,B_i\rangle$ (paper `eq:conv:pairing-n`, R58).
  Vertices $\mathcal V_n$ graded symmetric, nonzero only for $\sum_i N_{\rm gh}(A_i)=2n$;
  $\mathcal V_n(A_1,\dots,A_n) = \langle A_1,\ell_{n-1}(A_2,\dots,A_n)\rangle$, $\mathcal V_2(A,B) := \langle A,Q_BB\rangle$;
  $\mathcal V_{m+n}(A_1..A_n,B_1..B_m) = \omega_n(\otimes A_i,\, m^n_m(B_1..B_m))$ (paper `eq:conv:vertex`, `eq:conv:sprod`).

## Hypotheses

- **H1** (= PH6, Zwiebach's hermiticity of the string vertices, in its original form) For every
  $n\ge3$ and every family of Grassmann-even total fields $\mathcal A_i = \sum_s|\Phi_s\rangle\psi_{i,s}$
  (Grassmann-odd coefficients on odd states) obeying Zwiebach's reality
  $\langle\mathcal A_{i,hc}| = -\langle\mathcal A_i|$ (Zwiebach (3.6)), the vertex
  $\{\mathcal A_1,\dots,\mathcal A_n\}$ is real, $\{\cdots\}^\dagger = \{\cdots\}$.
  Motivation: Zwiebach 1993 (7.84)–(7.98) proves it for the minimal-area vertices from the mirror
  property (c) of §5.1; the paper assumes it for the vertex family in use (PH6 (b), shown for the
  vertex family in use at $n=4$ only, R56). Falsified or discharged by: a vertex region not invariant under
  the mirror map, or a direct check on the vertex family in use at $n=3,5$. Cited here as PH6.
  Identification used with it: Zwiebach's bracket $\{\mathcal A_1,\dots,\mathcal A_n\}$ on states is the paper's
  $\mathcal V_n(A_1,\dots,A_n)$ with no parity-dependent relative sign and a real positive factor (the paper's
  `eq:conv:action` cites his (4.105)–(4.112)); a coefficient-left convention or a different slot ordering on his
  side would change the Koszul part of (4.4), not its even-argument sign $(-1)^n$ (the only odd-argument use in
  this record is $\Lambda$ in (3.3), through (4.8)).

## Claim tree

- **C1** The star conjugation of a ket is $\big(\lambda\,O_1\cdots O_k|0,p\rangle\big)^\star
  = \lambda^*\,O_k^\star\cdots O_1^\star|0,-p\rangle = \lambda^*(-1)^{k_o(k_o-1)/2}\prod_i s_{O_i}\;O_1\cdots O_k|0,-p\rangle$,
  with $O^\star = s_O\,O$, $s_O = (-1)^h(\pm1)^n$ real, and $k_o$ the number of odd modes; it is an
  antilinear involution preserving ghost number and parity. [by C1.1–C1.4]
  - **C1.1** On modes, $(\phi_n^\dagger)^t = (\phi_n^t)^\dagger = (-1)^h(\pm1)^n\phi_n$: closed string
    ($I^+$) $c_n^\star = -c_n$, $b_n^\star = b_n$, $\alpha_n^\star = -\alpha_n$, $(c_0^\pm)^\star = -c_0^\pm$,
    $(b_0^\pm)^\star = b_0^\pm$, barred alike; with $I^-$ an extra $(-1)^n$ per mode, invisible on level-matched
    states. [by A2, A3; eq. (1.1)] [check: C1.1]
  - **C1.2** On a ket, $\mathrm{bpz}^{-1}(\mathrm{hc}(v))$ reverses the word (from hc) and conjugates
    each mode in place (from BPZ): eq. (1.2); restoring the original order costs $(-1)^{k_o(k_o-1)/2}$;
    the momentum flips. [by A2, A3; eq. (1.2)–(1.3)] [check: C1.2]
  - **C1.3** The book's state-level definition $|\phi^\star\rangle := \phi^\star(0)|0\rangle$
    (`cft:eq:state-star-phi`) equals $\mathrm{bpz}^{-1}(\mathrm{hc}(|\phi\rangle))$
    (`cft:eq:state-equivalence-star-hermitian`); on words this is eq. (1.2). [cited: Erbin2023 `cft:eq:state-equivalence-star-hermitian`; eq. (1.2)]
  - **C1.4** $\star^2 = 1$ on every state (even or odd) with commuting coefficients. [by C1.2; eq. (1.4)] [check: C1.4]
- **C2** Relation to the paper's involution: $A^\ddagger = (-1)^{N_{\rm gh}(A)+1}A^\star$ on single strands,
  $X^\ddagger = (-1)^{k(N+1)}X^\star$ on $k$ strands of ghost number $N$; the two orders of composition
  agree, $\mathrm{bpz}^{-1}\circ\mathrm{hc} = \mathrm{hc}^{-1}\circ\mathrm{bpz}$ on kets, so no further sign
  arises on odd states. [by C1; eq. (2.1)–(2.2)] [check: C2]
- **C3** Reality conditions (table (3.1)): $\Psi^\star = -\Psi$, $\Lambda^\star = -\Lambda$,
  $\Sigma_k^\star = (-1)^k\Sigma_k$, $\Upsilon_2^\star = \Upsilon_2$, $\Theta_k^\star = \Theta_k$ (table (3.1));
  C3.2's interaction part and C3.3 (through R35) hold under H1. [by C3.1–C3.5; H1 through C3.2, C3.3]
  - **C3.1** $\Psi^\star = -\Psi$ is Zwiebach (3.6); on the tachyon it is $\phi(p)^* = \phi(-p)$. [by C1; eq. (3.2)] [check: C3.1]
  - **C3.2** $\Lambda^\star = -\Lambda$ is the condition under which every gauge transformation
    preserves $\Psi^\star = -\Psi$ (free term by C4.3; interaction terms by C4.5); it is Zwiebach (3.18). [by C3.1, C4.3, C4.5; eq. (3.3)]
  - **C3.3** $\Sigma_k^\star = (-1)^k\Sigma_k$ and $\Upsilon_2^\star = \Upsilon_2$: forced by $(\Psi^{\otimes k})^\star = (-1)^k\Psi^{\otimes k}$
    through the sources, as in 028 Step 2.4 and §3 (R35), translated by C2; eq. (3.4). [by A5, C2, C3.1, R35 (Conditional(PH6))] [check: C3.4-Sigma-star-sign]
  - **C3.4** $\Theta_k^\star = \Theta_k$ makes the multiplier term $\omega_k(\Theta_k,\Sigma_k-\Psi^{\otimes k})$ real,
    and is forced on the directions it reaches; (3.5) uses $\Sigma_k^\star = (-1)^k\Sigma_k$ only as the definition of the
    real slice, so this node does not inherit H1 from C3.3. [by A5, C3.3 (as a definition of the slice), C4.2; eq. (3.4)–(3.5)] [check: C3.4]
  - **C3.5** Open versus closed: the open string field is star-real, $\Phi^\star = \Phi$ (book
    `bsft_free_brst.tex` l. 237–241, $\mathrm{hc}(\Phi) = \mathrm{bpz}(\Phi)$), the closed one star-imaginary;
    the relative sign is the reversal sign of the two odd modes $c_1\bar c_1$, equivalently the
    anti-Hermiticity of the closed-string normalisation (Zwiebach (2.37)). [by C1.1, C1.2, A1; eq. (3.5)]
- **C4** Equivariance statements in the $\star$ convention; C4.4 for $n\ge3$, C4.5 and C4.6 hold under H1. [by C4.1–C4.6; H1 through C4.4–C4.6]
  - **C4.1** $\langle A^\star,B^\star\rangle = -\langle A,B\rangle^*$ on every pair (anti-equivariant). [by A1, A4, A7, C1; eq. (4.0)–(4.1)] [check: C4.1]
  - **C4.2** $\omega_n(X^\star,Y^\star) = (-1)^n\omega_n(X,Y)^*$. [by A5, A7, C4.1; eq. (4.2)] [check: C4.2]
  - **C4.3** $(Q_BA)^\star = (-1)^{|A|+1}Q_BA^\star$; more generally $(OA)^\star = (-1)^{|O||A|}O^\star A^\star$
    for any operator $O$. [by A2, A3, A4; eq. (4.3)] [check: C4.3]
  - **C4.4** Under H1, $\mathcal V_n(A_1^\star,\dots,A_n^\star) = (-1)^{n+\sum_{i<j}|A_i||A_j|}\,\mathcal V_n(A_1,\dots,A_n)^*$
    for $n\ge3$ on the support; for $n=2$ the same formula follows from C4.1 and C4.3 without H1. [by H1 (with its identification of $\{\cdots\}$ and $\mathcal V_n$), A6, C1, C4.1, C4.3; eq. (4.4)–(4.7)] [check: C4.4]
  - **C4.5** Under H1, $\ell_m(A_1^\star,\dots,A_m^\star) = (-1)^{m+\sum_i|A_i|+\sum_{i<j}|A_i||A_j|}\,\ell_m(A_1,\dots,A_m)^\star$;
    for even inputs $m^n_m(B^\star) = (-1)^m\,m^n_m(B)^\star$. [by H1, A7, C4.1, C4.2, C4.4; eq. (4.8)–(4.9)]
  - **C4.6** Under H1, the nonpolynomial action and the cubic action are real on the real slice (3.1). [by H1, C3, C4.1–C4.5; eq. (4.10)–(4.12)]

Open gaps: none
Hypotheses in force: H1 (= PH6) – C3.2 (interaction part), C3.3 (through R35), C4.4 ($n\ge3$), C4.5, C4.6, and their parents C3, C4 on these parts; C3.4 uses C3.3 only as the definition of the real slice and is not conditional

## 1. Definition on states (item 1)

\subsection*{Setup}

Assumptions A2, A3 (the mode rules of BPZ and Hermitian conjugation, the word rules on kets). Block-local: a *creation word* is $v = \lambda\,O_1\cdots O_k\,|0,p\rangle$ with $\lambda\in\mathbb C$ and each $O_i$ a creation mode on the $\mathrm{SL}(2,\mathbb C)$ vacuum ($c_n,\bar c_n$ with $n\le1$; $b_n,\bar b_n$ with $n\le-2$; $\alpha_n,\bar\alpha_n$ with $n\le-1$); $k_o$ is the number of Grassmann-odd (ghost) modes in the word. For a mode $O$ with $O^\star = s_O\,O$ the real number $s_O$ is its *star sign*. Upper signs are the $I^+$ rule (book, closed string), lower signs the $I^-$ rule (ledger C1(ii), paper `eq:conv:bpz-modes`).

\subsection*{Derivation}

Star conjugation on a single mode, in both orders of composition:
$$
\begin{aligned}
(\phi_n^\dagger)^t &= (\phi_{-n})^t = (-1)^h(\pm1)^{-n}\,\phi_n = (-1)^h(\pm1)^n\,\phi_n,\\
(\phi_n^t)^\dagger &= (-1)^h(\pm1)^n\,(\phi_{-n})^\dagger = (-1)^h(\pm1)^n\,\phi_n,
\end{aligned}\tag{1.1}
$$
so $\phi_n^\star = (-1)^h(\pm1)^n\phi_n$ with no order ambiguity. Table ($\phi^+ = \phi$ for $b$, $c$, $i\partial X$; barred modes alike):

| mode | $h$ | $\phi_n^\star$, $I^+$ | $\phi_n^\star$, $I^-$ |
|---|---|---|---|
| $c_n$, $\bar c_n$ | $-1$ | $-c_n$ | $-(-1)^n c_n$ |
| $b_n$, $\bar b_n$ | $2$ | $+b_n$ | $(-1)^n b_n$ |
| $\alpha_n$, $\bar\alpha_n$ | $1$ | $-\alpha_n$ | $-(-1)^n\alpha_n$ |
| $c_0^\pm$ | | $-c_0^\pm$ | $-c_0^\pm$ |
| $b_0^\pm$ | | $+b_0^\pm$ | $+b_0^\pm$ |
| $\hat p^\mu$ | | $-\hat p^\mu$ | $-\hat p^\mu$ |

The momentum operator: $\hat p^\dagger = \hat p$, $\hat p^t = -\hat p$ (Zwiebach (2.41): $\mathrm{bpz}$ reverses the momentum, $\mathrm{bpz}(|0,p\rangle) = \langle 0,-p|$), hence $\hat p^\star = -\hat p$ and $|0,p\rangle^\star = \mathrm{bpz}^{-1}(\langle 0,p|) = |0,-p\rangle$.

On a creation word, apply A3 then A2. Hermitian conjugation reverses the word and conjugates the coefficient,
$$
\mathrm{hc}(v) = \lambda^*\,\langle 0,p|\,O_k^\dagger\cdots O_1^\dagger .
$$
The ket $w = \mu\,O'_1\cdots O'_k|0,-p\rangle$ with $\mathrm{bpz}(w) = \mu\,\langle 0,p|\,O'^{\,t}_1\cdots O'^{\,t}_k$ equal to $\mathrm{hc}(v)$ has $\mu = \lambda^*$ and $O'^{\,t}_i = O^\dagger_{k+1-i}$, i.e. $O'_i = (O^\dagger_{k+1-i})^t = O^\star_{k+1-i}$ (BPZ is involutive on modes, $(\phi_n^t)^t = \phi_n$). Therefore
$$
v^\star := \mathrm{bpz}^{-1}(\mathrm{hc}(v)) = \lambda^*\,O_k^\star\cdots O_1^\star\,|0,-p\rangle .\tag{1.2}
$$
Each $O^\star_i = s_{O_i}O_i$ is a real multiple of the same mode; restoring the original order moves $k_o$ odd modes through each other, $\binom{k_o}{2}$ transpositions:
$$
\boxed{\;v^\star = \lambda^*\,(-1)^{k_o(k_o-1)/2}\,\prod_{i=1}^k s_{O_i}\;O_1\cdots O_k\,|0,-p\rangle\;}\tag{1.3}
$$
Applying (1.3) twice: the coefficient returns to $\lambda$, the sign squares to one, the momentum to $p$:
$$
(v^\star)^\star = v\qquad\text{on every creation word, even or odd.}\tag{1.4}
$$
Since $\star$ maps each monomial to a real multiple of itself (opposite momentum), it preserves the ghost number, the parity and the level, and is antilinear on linear combinations. On a tensor product it is extended strand by strand (A5).

\subsection*{Commentary}

- (1.1): the two orders of composition agree on modes because $\dagger$ and $t$ both map $\phi_n$ to a real multiple of $\phi_{-n}$; this is the equality $(A^t)^\dagger = (A^\dagger)^t$ of `cft:eq:conj-star`, checked on modes (check `C1.1-order-*`). The $I^\pm$ rules differ by $(-1)^n$ per mode, which multiplies a level-matched word by $(-1)^{N+\bar N} = 1$ (check `C1.2-Ipm-agree-level-matched`); every state of this record is level-matched, so the table's two columns agree wherever they are used.
- (1.2) is the book's operator rule "star conjugation reverses the order of the operators without any sign" (`cft:eq:conj-star` paragraph) applied to the word, with $|0\rangle^\star = |0\rangle$: the reversal comes from $\dagger$, BPZ keeps the order (C1(iii), `cft_operator_formalism.tex` l. 1134–1146). On a single mode $\phi_{-h}|0\rangle$ it is the book's `cft:eq:state-star-phi`, $|\phi^\star\rangle = (\mp1)^h\phi^+_{-h}|0\rangle$: $s_{\phi_{-h}} = (-1)^h(\pm1)^{-h} = (\mp1)^h$ in both columns.
- (1.3) against record 028's wording "conjugate each mode in place, no reordering sign": that sentence describes the BPZ step alone (A2). The composite $\star$ does carry the reversal sign $(-1)^{k_o(k_o-1)/2}$; 028's own computation (addendum P.3, "$\ddagger = \eta\,\mathrm{bpz}^{-1}\circ\mathrm{hc}$ maps each mode monomial to a real multiple of itself") includes it, and the values quoted there ($A_1 = c_1\bar c_1|0\rangle$ with $A_1^\ddagger = A_1$ for $\eta = -1$) are reproduced by (1.3): $(c_1\bar c_1|0\rangle)^\star = (-1)^{1}(-1)(-1)\,c_1\bar c_1|0\rangle = -c_1\bar c_1|0\rangle$. The break leg `break-C1.2-no-reversal-sign-*` (the formula without the reversal sign) fails on the 64 ghost words, so the sign is not optional.
- Which Hermitian conjugation: the paper's $\mathrm{hc}$ is the book's Euclidean adjoint `cft:eq:conj-herm` (the Wick rotation of `cft:eq:conj-herm-lorentz`), written $\eadj{(\cdot)}$ on states in the book. On the modes of the Hermitian fields $b$, $c$, $i\partial X$ both adjoints give $\phi_n^\dagger = \phi_{-n}$ (`cft:eq:chiral-modes-adj`); they differ only in how they act on the coordinate $z$, which no statement of the paper uses. The book typesets the Euclidean-adjoint *bra* as $\langle\phi^\ddagger|$; this is not the paper's former involution $\ddagger$ of C3 (item 2).
- (1.4) is PH7 in the $\star$ convention, for commuting coefficients (check `C1.4-star-squared`).

\subsection*{Result}

Star conjugation on a creation word is (1.3): antilinear, momentum-reversing, diagonal on mode monomials with the real sign $(-1)^{k_o(k_o-1)/2}\prod_i s_{O_i}$, where $s_c = -1$, $s_b = +1$, $s_\alpha = -1$ ($I^+$; an extra $(-1)^n$ per mode for $I^-$, invisible on level-matched states), and $\star^2 = 1$. On tensors: strand by strand, no Koszul sign (A5).

\subsection*{Verification}

Checks `C1.1-*` (mode signs, both inversions, both orders), `C1.2-word-formula-I+`, `C1.2-word-formula-I-` (64 ghost monomials, random complex coefficient, against the independent matrix implementation of hc and bpz), `break-C1.2-no-reversal-sign-I±` (fail as required), `C1.2-Ipm-agree-level-matched`, `C1.2-star-diagonal`, `C1.4-star-squared`, `C1.4-antilinear`. The matter modes and the momentum are not in the matrix model: the rule (1.1) for $\alpha_n$ follows the same two-line computation and is not machine-checked.

## 2. Relation to the paper's former involution $\ddagger$ (item 2)

\subsection*{Setup}

A2, A3, C3 (the former definition $A^\ddagger := (-1)^{N_{\rm gh}(A)+1}\,\mathrm{bpz}^{-1}(\mathrm{hc}(A))$ on single strands, componentwise on $\mathcal H^{\otimes k}$), eq. (1.2). Notation: the wrong-sign partner of $\Sigma_2$ is written $\Upsilon_2$ here and in the paper's body ($\Xi_2$ is Harold's same-sign field; appendix A l. 287–304 still writes $\Xi_2$ for the partner, to be renamed).

\subsection*{Derivation}

On a ket, (1.2) is $A^\star = \mathrm{bpz}^{-1}(\mathrm{hc}(A))$: the composite in C3 *is* star conjugation, so on a state of definite ghost number
$$
\boxed{\;A^\ddagger = (-1)^{N_{\rm gh}(A)+1}\,A^\star\;}\tag{2.1}
$$
and on $X\in\mathcal H^{\otimes k}$ with every strand at ghost number $N$ (componentwise $\ddagger$, strand-by-strand $\star$, A5)
$$
X^\ddagger = (-1)^{k(N+1)}\,X^\star .\tag{2.2}
$$
The other order of composition gives the same map. For a creation word $v$, $\mathrm{bpz}(v) = \lambda\,\langle 0,-p|\,O_1^t\cdots O_k^t$ (A2), and the inverse of the Hermitian conjugation of A3 on a bra is $\mathrm{hc}^{-1}(\mu\,\langle 0,q|P_1\cdots P_k) = \mu^*\,P_k^\dagger\cdots P_1^\dagger\,|0,q\rangle$, so
$$
\mathrm{hc}^{-1}(\mathrm{bpz}(v)) = \lambda^*\,(O_k^t)^\dagger\cdots(O_1^t)^\dagger\,|0,-p\rangle = \lambda^*\,O_k^\star\cdots O_1^\star\,|0,-p\rangle = v^\star ,\tag{2.3}
$$
by (1.1). No extra sign arises on odd states: the two compositions agree on every monomial (checks `C2-hcinv-bpz-equals-bpzinv-hc`, both inversions). In the matrix model, $\star = \overline{(\cdot)}\circ M$ with $M$ real, and the equality of the two compositions is $M^2 = 1$, i.e. the same identity as $\star^2 = 1$ (C1.4); the two checks are one statement in two forms.

For the fields of the paper, (2.1)–(2.2) read
$$
\Psi^\ddagger = -\Psi^\star,\quad \Lambda^\ddagger = +\Lambda^\star,\quad \Sigma_k^\ddagger = (-1)^k\,\Sigma_k^\star,\quad \Upsilon_2^\ddagger = +\Upsilon_2^\star,\quad \Theta_k^\ddagger = +\Theta_k^\star .\tag{2.4}
$$

\subsection*{Commentary}

- (2.1) is the definition of C3 read with (1.2); nothing is computed beyond the identification of the composite. The sign $(-1)^{N_{\rm gh}+1}$ was introduced in 028 P.6 to make the pairing equivariant; in the $\star$ convention that sign migrates into the equivariance statements (§4) and into the reality signs (§3).
- (2.3): Zwiebach's (3.6) is stated as $\langle\Psi_{hc}| = -\langle\Psi|$, i.e. in the form $\mathrm{hc}(\Psi) = -\mathrm{bpz}(\Psi)$; applying $\mathrm{hc}^{-1}$ gives $\Psi = -\mathrm{hc}^{-1}(\mathrm{bpz}(\Psi)) = -\Psi^\star$ by (2.3), and applying $\mathrm{bpz}^{-1}$ gives $\Psi^\star = -\Psi$ directly. Both readings coincide, which is the content of (2.3).
- The former $\ddagger$ was defined on states only; the book's $\star$ is also an operator map, $(XY)^\star = Y^\star X^\star$ (`cft:eq:conj-star` paragraph), and (1.2) is that rule on words. Item 4 uses the operator form for $Q_B$ and $c_0^-$.

\subsection*{Result}

$A^\ddagger = (-1)^{N_{\rm gh}(A)+1}A^\star$ on single strands, $X^\ddagger = (-1)^{k(N+1)}X^\star$ on $k$ strands of ghost number $N$; $\mathrm{bpz}^{-1}\circ\mathrm{hc} = \mathrm{hc}^{-1}\circ\mathrm{bpz}$ on kets. Every statement of records 028, 039 and of ledger C3, R35 translates by (2.4).

\subsection*{Verification}

Checks `C2-hcinv-bpz-equals-bpzinv-hc`, `C2-hcinv-bpz-equals-bpzinv-hc-I-` (random vector, both inversions), `consistency-C2-ddagger-implementation` (64 monomials; an implementation guard – `ddagger()` is defined as $(-1)^{N+1}\star$ and re-evaluated – not a check of the claim), `C2-A1-star`, `C2-B1-star`, `C2-A1-B1-ddagger` (the C3 ledger values $A_1^\ddagger = A_1$, $B_1^\ddagger = B_1$ reproduced from $A_1^\star = -A_1$, $B_1^\star = B_1$).

## 3. Reality conditions of the fields (item 3)

\subsection*{Setup}

A1, A5, A6, A7; eqs. (1.3), (2.1)–(2.4); the equivariance rules of §4 ((4.1)–(4.3), (4.8)) are used forward, with their hypothesis where they carry one. The paper's gauge law is $\delta\Psi = Q_B\Lambda + \sum_{m\ge2}\tfrac{g_s^{m-1}}{(m-1)!}\,\ell_m(\Psi^{m-1},\Lambda)$ with real $g_s$; the multiplier presentation carries the term $\omega_k(\Theta_k,\Sigma_k - \Psi^{\otimes k})$ (R13, R35).

\subsection*{Derivation}

**Table (3.1).** Reality conditions in the $\star$ convention, $X^\star = \varepsilon_X X$, with the former $\ddagger$ sign for comparison (by (2.4)):

| field | strands | $N_{\rm gh}$ per strand | $\varepsilon_X$ ($X^\star = \varepsilon_X X$) | former ($X^\ddagger = \pm X$) | fixed by |
|---|---|---|---|---|---|
| $\Psi$ | 1 | 2 | $-1$ | $+$ | Zwiebach (3.6); tachyon (3.2) |
| $\Lambda$ | 1 | 1 | $-1$ | $-$ | gauge law preserves $\Psi^\star = -\Psi$, (3.3); Zwiebach (3.18) |
| $\Sigma_k$ | $k$ | 2 | $(-1)^k$ | $+$ | $(\Psi^{\otimes k})^\star = (-1)^k\Psi^{\otimes k}$ through the sources, (3.4) |
| $\Upsilon_2$ | 2 | 2 | $+1$ | $+$ | same as $\Sigma_2$ (R35, $\chi^\ddagger = \chi$ translated) |
| $\Theta_k$ | $k$ | 3 | $+1$ | $+$ | multiplier term real, (3.5) |

*(3.2) The string field.* Zwiebach's (3.6), $\langle\Psi_{hc}| = -\langle\Psi|$, is $\mathrm{hc}(\Psi) = -\mathrm{bpz}(\Psi)$, i.e. $\Psi^\star = \mathrm{bpz}^{-1}(\mathrm{hc}(\Psi)) = -\Psi$. On the tachyon component $\Psi_T = \int\!\frac{d^Dp}{(2\pi)^D}\,\phi(p)\,c_1\bar c_1|0,p\rangle$, (1.3) with $k_o = 2$, $s_{c_1}s_{\bar c_1} = +1$ gives
$$
\Psi_T^\star = -\int\!\frac{d^Dp}{(2\pi)^D}\,\phi(p)^*\,c_1\bar c_1|0,-p\rangle = -\int\!\frac{d^Dp}{(2\pi)^D}\,\phi(-p)^*\,c_1\bar c_1|0,p\rangle ,
\qquad
\Psi_T^\star = -\Psi_T \iff \phi(-p)^* = \phi(p),\tag{3.2}
$$
the reality of a real scalar (Zwiebach after (3.8)). A coefficient $i\phi$ with $\phi$ real would give $\Psi_T^\star = +\Psi_T$ (break leg `break-C3.1-tachyon-imag-coeff`).

*(3.3) The gauge parameter.* Free term: by (4.3) with $|\Lambda| = 1$, $(Q_B\Lambda)^\star = (-1)^{1+1}Q_B\Lambda^\star = Q_B\Lambda^\star$. The variation is star-odd like $\Psi$ iff $Q_B\Lambda^\star = -Q_B\Lambda$, i.e. $\Lambda^\star = -\Lambda$ modulo $\ker Q_B$; for $\Lambda^\star = +\Lambda$ the free variation is star-even and breaks $\Psi^\star = -\Psi$ unless $Q_B\Lambda = 0$. Interaction terms, under H1: by (4.8) with $m-1$ even inputs and one odd, $\sum_i|A_i| = 1$ and no odd pair,
$$
\ell_m\big((\Psi^\star)^{m-1},\Lambda^\star\big) = (-1)^{m+1}\,\ell_m(\Psi^{m-1},\Lambda)^\star ;
\quad
\Psi^\star = -\Psi,\ \Lambda^\star = -\Lambda
\ \Rightarrow\
\ell_m(\Psi^{m-1},\Lambda)^\star = (-1)^{m}(-1)^{m+1}\,\ell_m(\Psi^{m-1},\Lambda) = -\ell_m(\Psi^{m-1},\Lambda).\tag{3.3}
$$
So every term of $\delta\Psi$ is star-odd for $\Lambda^\star = -\Lambda$ and real $g_s$. This is Zwiebach's (3.18), $\langle\Lambda_{hc}| = -\langle\Lambda|$, whose coefficients are commuting (his $\lambda_r$ are Grassmann even on odd states), the same reading as A6.

*(3.4) The auxiliary fields.* By A5 and (3.2), $(\Psi^{\otimes k})^\star = (\Psi^\star)^{\otimes k} = (-1)^k\,\Psi^{\otimes k}$. R35 (028 Step 2.4, §3): the sources force $\Sigma_k = \Psi^{\otimes k}$ on-shell and $\Sigma_k^\ddagger = \Sigma_k$ level by level up to source-kernel directions, and $\chi^\ddagger = \chi$ for the wrong-sign partner ($\Upsilon_2$ here); on the directions no source reaches the condition is imposed. Translating by (2.2) with $N = 2$:
$$
\Sigma_k^\star = (-1)^k\,\Sigma_k ,\qquad \Upsilon_2^\star = +\Upsilon_2 ,\tag{3.4}
$$
which is also what $(\Psi^{\otimes k})^\star = (-1)^k\Psi^{\otimes k}$ says directly on the on-shell value. The reality of the auxiliary action rests on R35, hence on PH6 (= H1); the translation itself does not.

*(3.5) The multipliers.* With $X := \Sigma_k - \Psi^{\otimes k}$, $X^\star = (-1)^kX$ by (3.4). By (4.2), $\omega_k(\Theta_k^\star,X^\star) = (-1)^k\,\omega_k(\Theta_k,X)^*$. If $\Theta_k^\star = \varepsilon\,\Theta_k$,
$$
\varepsilon\,(-1)^k\,\omega_k(\Theta_k,X) = (-1)^k\,\omega_k(\Theta_k,X)^*
\quad\Longrightarrow\quad
\omega_k(\Theta_k,X)\in\mathbb R \iff \varepsilon = +1 .\tag{3.5}
$$
So $\Theta_k^\star = \Theta_k$; it is forced on the directions of $\Theta_k$ that $\omega_k$ pairs with the range of $X$ (from generic complex data projected onto the two star eigenspaces: the term is real for $\Theta_k^\star = +\Theta_k$ and purely imaginary for $\Theta_k^\star = -\Theta_k$, checks `C3.4-multiplier-term-real-k2/k3`, `C3.4-multiplier-term-not-real-Theta-odd-k2/k3`, `break-C3.4-opposite-slice-sign-k2/k3`), imposed on the rest. Translation of R35's $\lambda_k^\ddagger = \lambda_k$ by (2.2) with $N = 3$: $(-1)^{4k} = 1$, the same.

*(3.6) Open versus closed.* The open string field is star-real, $\mathrm{hc}(\Phi) = \mathrm{bpz}(\Phi)$ (book `bsft_free_brst.tex` l. 237–241), with the $I^-$ rule $c_1^t = c_{-1}$, for which $s_{c_1} = (c_{-1})^t = +c_1$. On the open tachyon $\int T(k)\,c_1|0,k\rangle$, (1.3) with $k_o = 1$ (no reversal sign) gives $\Phi^\star = \int T(-k)^*\,c_1|0,k\rangle$, so $\Phi^\star = \Phi \iff T(-k)^* = T(k)$, the book's l. 1353. The closed tachyon has $k_o = 2$: the reversal sign $(-1)^{k_o(k_o-1)/2} = -1$ is the whole difference, $\Psi^\star = -\Psi$ with the same real scalar. (The open-string state $c_1|0,k\rangle$ is not level-matched, so there the $I^\pm$ choice is visible: with $I^+$, $s_{c_1} = -1$ and the star-real condition would read $T(-k)^* = -T(k)$; the book's $I^-$ is the one that makes the real tachyon star-real.) The same count explains the pairing: the open-string normalisation $\langle c_{-1}c_0c_1\rangle = 1$ is Hermitian ($(c_{-1}c_0c_1)^\dagger = c_{-1}c_0c_1$) while the closed one $\langle c_{-1}\bar c_{-1}c_0\bar c_0c_1\bar c_1\rangle = -1$ is anti-Hermitian (the dagger returns the six modes with each $(c,\bar c)$ pair swapped, three transpositions), which is Zwiebach's (2.37) and the source of the minus sign in (4.1); with the Hermitian open-string pairing, $\langle\Phi,Q_B\Phi\rangle^* = \langle\Phi^\star,(Q_B\Phi)^\star\rangle = \langle\Phi,Q_B\Phi\rangle$ for $\Phi^\star = \Phi$, $|\Phi| = 1$, by the same steps as (4.10) without the minus sign. The open-string pairing equivariance is a hand computation here (the script's Fock space is closed-string).

*Remark (antifields; not a claim of this record).* For a single-strand antifield $\Psi^+$ ($N_{\rm gh} = 3$) and the ghost $c$ of $\Lambda$ read with commuting coefficients and $c^\star = -c$, the term $\langle\Psi^+,Q_Bc\rangle$ is real iff $\Psi^{+\star} = +\Psi^+$, by (4.1) and (4.3) exactly as in (3.5). Whether section 4 of the paper reads its BV fields with commuting or shifted-parity coefficients is the open point of appendix A l. 349; the sign is immediate only under the commuting reading and is not entered in table (3.1).

\subsection*{Commentary}

- The $\ddagger$ column of (3.1) shows why the former convention looked uniform ($+$ on every field but $\Lambda$): the sign $(-1)^{N_{\rm gh}+1}$ built into $\ddagger$ absorbed the $-1$ of $\Psi$ and the $(-1)^k$ of $\Sigma_k$. In the $\star$ convention the signs are the honest ones: a field is star-odd exactly when it is a product of an odd number of star-odd strands ($\Psi$, $\Sigma_{2j+1}$), and $\Lambda$ follows $\Psi$ through $Q_B$.
- (3.3) uses (4.8) at $m \ge 2$, hence H1 for the interaction terms; the free term is unconditional. The former-convention version is the C3 *Rechecked* bullet ($\Lambda^\ddagger = -\Lambda$), to which (3.3) translates by (2.4) with the same sign.
- (3.4): the translation is exact; the content (forced by the sources, imposed on kernel directions) is R35's and is not re-derived.

\subsection*{Result}

Table (3.1): $\Psi^\star = -\Psi$, $\Lambda^\star = -\Lambda$, $\Sigma_k^\star = (-1)^k\Sigma_k$, $\Upsilon_2^\star = \Upsilon_2$, $\Theta_k^\star = \Theta_k$. The interaction part of (3.3) and the reality of the auxiliary action behind (3.4) are conditional on H1 (= PH6).

\subsection*{Verification}

`C3.1-tachyon-real-coeff`, `break-C3.1-tachyon-imag-coeff`, `C3.1-ghost1-state-in-H`, `C3.1-ghost1-star` ($c_0^+|0\rangle$, $N_{\rm gh} = 1$, star-odd with a real coefficient), `C3.1-ghost3-star` ($c_0^+c_1\bar c_1|0\rangle$, star-even), `C3.4-Theta-star-even-k2/k3`, `C3.4-Sigma-star-sign-k2/k3`, `C3.4-multiplier-term-real-k2/k3` ($\Theta_+ = \tfrac12(Y+Y^\star)$ from complex $Y$ on the ghost-3 monomials, $X = \tfrac12(Z+(-1)^kZ^\star)$ from complex $Z$ on their pairing partners: value $\ne0$, imaginary part $0$), `C3.4-multiplier-term-not-real-Theta-odd-k2/k3` ($\Theta_- = \tfrac12(Y-Y^\star)$: real part $0$, imaginary part $\ne0$), `break-C3.4-opposite-slice-sign-k2/k3`. The wrong result these catch is the opposite slice sign for $\Theta_k$: with $\Theta_-$ in place of $\Theta_+$ the real-part check FAILs (broken on purpose once in the fix pass of 2026-10-04, values $+0.6611i$, $+0.8500i$, then restored). The earlier version of this check used real coefficients, for which the value is real under any star signs; it was vacuous and is replaced. `C3.4-Theta-star-even-k2/k3`, `C3.4-Sigma-star-sign-k2/k3` are A5 plus `C2-A1-star`/`C2-B1-star` on the explicit strands, kept as such. Not machine-checked: the momentum dependence (3.2) (the matrix model has no momentum), the open-string comparison (3.6).

## 4. Equivariance statements in the $\star$ convention (item 4)

\subsection*{Setup}

A1–A7, H1; eqs. (1.2)–(1.3), (2.3). Block-local: for a creation word $A = U|0\rangle$ the operator $U$ is the word of modes (momentum suppressed: it enters only through $\langle 0,p|0,q\rangle \propto \delta(p-q)$ and the flip $p\to-p$ of (1.1), which commute with everything below); $\eta$ is the Hermiticity sign of the vacuum functional, $\overline{\langle 0|W|0\rangle} = \eta\,\langle 0|W^\dagger|0\rangle$ for every word $W$ of modes; $k_o$ the number of odd arguments of a vertex, $\mathrm{kos}(A_1..A_n) := \sum_{i<j}|A_i||A_j| \equiv \binom{k_o}{2} \pmod 2$.

\subsection*{Derivation}

*Hermiticity sign of the vacuum.* $W\mapsto\overline{\langle 0|W|0\rangle}$ and $W\mapsto\langle 0|W^\dagger|0\rangle$ are both antilinear functionals on the mode algebra that vanish on every word beginning with a mode that annihilates $\langle 0|$ or ending with one that annihilates $|0\rangle$ ($\dagger$ is an antilinear anti-automorphism of the mode algebra, $\{b_m,c_n\}^\dagger = \{c_{-n},b_{-m}\} = \delta_{m+n,0}$, exchanging the two annihilation conditions). The vacuum functional is unique up to scale under these conditions, so the two are proportional, $\overline{\langle W\rangle} = \eta\,\langle W^\dagger\rangle$, and $\eta$ is read off one word. With A1, $W_0 = c_{-1}\bar c_{-1}c_0\bar c_0c_1\bar c_1$, $W_0^\dagger = \bar c_{-1}c_{-1}\bar c_0c_0\bar c_1c_1 = -W_0$, $\langle W_0\rangle = -1$:
$$
\overline{\langle W_0\rangle} = -1,\qquad \langle W_0^\dagger\rangle = +1,\qquad \eta = -1 .\tag{4.0}
$$
This is Zwiebach's (2.37), $(A,B)^\dagger = -(B,A)$.

*(4.1) Pairing.* With $A = U|0\rangle$ and $B^\star = V'|0\rangle$, using $\mathrm{bpz}(A^\star) = \mathrm{hc}(A)$ (1.2) and $\mathrm{hc}(B^\star) = \mathrm{bpz}(B)$ (2.3), $(c_0^-)^\dagger = c_0^-$ (A4), and the symmetry of the pairing (A7):
$$
\begin{aligned}
\langle A^\star,B^\star\rangle &= \langle\mathrm{bpz}(A^\star)|\,c_0^-\,|B^\star\rangle = \langle 0|\,U^\dagger c_0^- V'\,|0\rangle
= \eta\,\overline{\langle 0|\,V'^\dagger c_0^- U\,|0\rangle}\\
&= \eta\,\overline{\langle\mathrm{hc}(B^\star)|\,c_0^-\,|A\rangle} = \eta\,\overline{\langle\mathrm{bpz}(B)|\,c_0^-\,|A\rangle} = \eta\,\overline{\langle B,A\rangle} = \eta\,\overline{\langle A,B\rangle},
\end{aligned}
$$
$$
\boxed{\;\langle A^\star,B^\star\rangle = -\,\langle A,B\rangle^*\quad\text{for all }A,B\;}\tag{4.1}
$$

*(4.2) $n$-string pairing.* On product tensors, A5 and A7: $\star$ preserves every parity, so the Koszul sign is unchanged and
$$
\omega_n(X^\star,Y^\star) = (-1)^{\sum_{i<j}|B_i||A_j|}\prod_i\langle A_i^\star,B_i^\star\rangle = (-1)^n\,\omega_n(X,Y)^* ,\tag{4.2}
$$
extended to all tensors by antilinearity of both sides.

*(4.3) Operators and $Q_B$.* The book's rearrangement rule `cft:eq:bpz-product-rearrangement`, $\langle A,OB\rangle = (-1)^{|O||A|}\langle O^tA,B\rangle$, is the bra identity $\mathrm{bpz}(A)\,O = (-1)^{|O||A|}\,\mathrm{bpz}(O^tA)$. Apply it to $A^\star$ and $O^\dagger$, with $\mathrm{hc}(OA) = \mathrm{hc}(A)\,O^\dagger$ (A3) and $(O^\dagger)^t = O^\star$:
$$
\mathrm{hc}(OA) = \mathrm{bpz}(A^\star)\,O^\dagger = (-1)^{|O||A|}\,\mathrm{bpz}(O^\star A^\star)
\quad\Longrightarrow\quad
(OA)^\star = (-1)^{|O||A|}\,O^\star A^\star .\tag{4.3a}
$$
For $Q_B$: $Q_B^\star = (Q_B^\dagger)^t = Q_B^t = -Q_B$ (A4), $|Q_B| = 1$, hence
$$
\boxed{\;(Q_BA)^\star = (-1)^{|A|+1}\,Q_B\,A^\star\;}\tag{4.3}
$$
($-$ on even $A$, $+$ on odd $A$); likewise $(c_0^\pm A)^\star = -(-1)^{|A|}c_0^\pm A^\star$, $(b_0^\pm A)^\star = (-1)^{|A|}b_0^\pm A^\star$.

*(4.4) Vertices, under H1.* Let $\mathcal A_i = \sum_s\Phi_s\,\psi_{i,s}$ be Zwiebach's total fields: a basis $\Phi_s$ of star eigenstates, $\Phi_s^\star = \epsilon_s\Phi_s$ ($\epsilon_s = \pm1$; such a basis exists because $\star$ is an antilinear involution, $\tfrac12(\Phi\pm\Phi^\star)$ and $\tfrac{i}{2}(\Phi\mp\Phi^\star)$; at $p = 0$ (1.3) gives it on monomials, at $p\ne0$ the monomials are not eigenstates since $|p\rangle\mapsto|-p\rangle$), coefficients $\psi_{i,s}$ of statistics $|\Phi_s|$ written to the right of the state. His reality $\langle\mathcal A_{hc}| = -\langle\mathcal A|$ with $(\Phi_s\psi_s)^\dagger = \psi_s^\dagger\,\mathrm{hc}(\Phi_s) = \psi_s^\dagger\,\mathrm{bpz}(\Phi_s^\star)$ and $\mathrm{bpz}$ linear reads, after moving $\psi_s^\dagger$ past the odd bra $\mathrm{bpz}(\Phi_s^\star)$ when $|\Phi_s| = 1$,
$$
\epsilon_s\,(-1)^{|\Phi_s|}\,\psi_s^\dagger = -\psi_s \quad\text{for every }s .\tag{4.4a}
$$
A vertex on total fields is $\{\mathcal A_1,\dots,\mathcal A_n\} = \sum_{s_1..s_n}(-1)^{\mathrm{kos}(\Phi_{s_1}..\Phi_{s_n})}\,\mathcal V_n(\Phi_{s_1},\dots,\Phi_{s_n})\,\psi_{1,s_1}\cdots\psi_{n,s_n}$ (the Koszul sign of pulling each coefficient past the later states). The monomials in independent coefficients are linearly independent, so H1 ($\{\cdots\}^\dagger = \{\cdots\}$ for all real total fields) holds term by term. With $(\psi_1\cdots\psi_n)^\dagger = \psi_n^\dagger\cdots\psi_1^\dagger = (-1)^{\binom{k_o}{2}}\psi_1^\dagger\cdots\psi_n^\dagger$ and (4.4a):
$$
\overline{\mathcal V_n(\Phi_s)}\,(-1)^{\binom{k_o}{2}}\,(-1)^{n}\,(-1)^{k_o}\prod_i\epsilon_{s_i} = \mathcal V_n(\Phi_s)
\quad\Longleftrightarrow\quad
\mathcal V_n(\Phi_{s_1}^\star,\dots,\Phi_{s_n}^\star) = (-1)^{\,n+k_o+\binom{k_o}{2}}\;\overline{\mathcal V_n(\Phi_{s_1},\dots,\Phi_{s_n})} .\tag{4.4b}
$$
Both sides are antilinear in each slot, so (4.4b) on the basis is the identity on all arguments; on the support $\sum_iN_{\rm gh}(A_i) = 2n$ the number $k_o$ of odd arguments is even, and
$$
\boxed{\;\mathcal V_n(A_1^\star,\dots,A_n^\star) = (-1)^{\,n+\sum_{i<j}|A_i||A_j|}\;\mathcal V_n(A_1,\dots,A_n)^*\;}\qquad(n\ge3,\ \text{under H1}).\tag{4.4}
$$
For $n = 2$, (4.1) and (4.3) give it without H1: $\mathcal V_2(A^\star,B^\star) = \langle A^\star,Q_BB^\star\rangle = (-1)^{|B|+1}\langle A^\star,(Q_BB)^\star\rangle = (-1)^{|B|}\,\mathcal V_2(A,B)^*$, and $|A||B| \equiv |B|$ on the support $|A| + |B| \equiv 0$. Cross-check with PH6's component form in the former convention, $V_n(A^\ddagger) = (-1)^{\binom{k_o}{2}}V_n(A)^*$: by (2.1), $V_n(A^\ddagger) = (-1)^{\sum_i(N_i+1)}V_n(A^\star) = (-1)^nV_n(A^\star)$ on the support, which is (4.4).

*(4.5) Products.* From $\mathcal V_{m+1}(A_0,A_1..A_m) = \langle A_0,\ell_m(A_1..A_m)\rangle$ (A7), (4.4) and (4.1), with $|A_0| \equiv \sum_{i\ge1}|A_i|$ on the support so that $|A_0|\sum_i|A_i| \equiv \sum_i|A_i|$:
$$
\langle A_0^\star,\ell_m(A^\star)\rangle = (-1)^{m+1+\mathrm{kos}(A)+\sum_i|A_i|}\,\overline{\langle A_0,\ell_m(A)\rangle} = (-1)^{m+\mathrm{kos}(A)+\sum_i|A_i|}\,\langle A_0^\star,\ell_m(A)^\star\rangle
$$
for every $A_0$; both $\ell_m(A^\star)$ and $\ell_m(A)^\star$ have the ghost number $3 - 2m + \sum N_i$ and the pairing is non-degenerate on the level-matched space (R58), hence
$$
\ell_m(A_1^\star,\dots,A_m^\star) = (-1)^{\,m+\sum_i|A_i|+\sum_{i<j}|A_i||A_j|}\;\ell_m(A_1,\dots,A_m)^\star ,\qquad \ell_m(B^\star) = (-1)^m\,\ell_m(B)^\star\ \text{for even }B .\tag{4.8}
$$
For $m^n_m$ with even inputs $B$ (A7, `eq:conv:sprod`): $\omega_n(X^\star,m^n_m(B^\star)) = \mathcal V_{m+n}(X^\star,B^\star) = (-1)^{m+n+\mathrm{kos}(X)}\overline{\omega_n(X,m^n_m(B))} = (-1)^{m+\mathrm{kos}(X)}\,\omega_n(X^\star,m^n_m(B)^\star)$ by (4.2), with the general sign $(-1)^{m+\mathrm{kos}(X)}$; the paper defines $m^n_m$ with output strands of ghost number three (`A-conventions.tex` l. 198), so the strands of $X$ that pair with its outputs are even and $\mathrm{kos}(X) = 0$ (the support alone does not give this: for $m = n = 2$ with inputs at ghost number two, $\mathcal V_4$ admits $(N_{A_1},N_{A_2}) = (1,3)$, $\mathrm{kos}(X) = 1$, and that component would carry the opposite sign):
$$
m^n_m(B_1^\star,\dots,B_m^\star) = (-1)^m\,m^n_m(B_1,\dots,B_m)^\star\qquad(\text{even inputs}).\tag{4.9}
$$

*(4.6) Reality of the actions, under H1.* Nonpolynomial action, real couplings: by (4.4) on even arguments and $\Psi^\star = -\Psi$,
$$
\overline{\mathcal V_n(\Psi^n)} = (-1)^n\,\mathcal V_n\big((\Psi^\star)^n\big) = (-1)^n(-1)^n\,\mathcal V_n(\Psi^n) = \mathcal V_n(\Psi^n)\qquad(n\ge2).\tag{4.10}
$$
Cubic action: every vertex term is a real multiple of $\mathcal V_N$ on tensors whose $N$ strands each have ghost number two and star sign $-1$ ($\Psi$, the strands of $\Sigma_k$ and $\Upsilon_2$ with $\varepsilon_{\Sigma_k} = (-1)^k$, $\varepsilon_{\Upsilon_2} = +1$, table (3.1)): the product of the strand signs is $(-1)^N$ and cancels the $(-1)^N$ of (4.4),
$$
\overline{\mathcal V_N(\Sigma_{a},\Sigma_{b},\Psi^{c})} = (-1)^N(-1)^{a}(-1)^{b}(-1)^{c}\,\mathcal V_N(\Sigma_a,\Sigma_b,\Psi^c) = \mathcal V_N(\Sigma_a,\Sigma_b,\Psi^c),\quad N = a+b+c ,\tag{4.11}
$$
and the same for $V_4(\Upsilon_2,\Upsilon_2)$, $V_5(\Upsilon_2,\Sigma_2,\Psi)$ and every source $\mathcal V_N(\Sigma_k,\Psi^{N-k})$. The multiplier terms are real by (3.5), the Gaussian kinetic terms of the tower by R35 translated through (2.4):
$$
S_{\rm cubic}[\Psi,\Sigma_k,\Upsilon_2,\Theta_k]\in\mathbb R\quad\text{on the real slice (3.1)}.\tag{4.12}
$$

\subsection*{Commentary}

- (4.0) and (4.1) are where the closed-string sign lives. The book's `cft:eq:bpz-product-hermitian` and `cft:eq:bpz-product-star`, $\overline{\langle A|O|B\rangle} = \langle B^\star|O^\dagger|A^\star\rangle$, are derived with $\eta = +1$ (`computation[cft:eq:bpz-product-hermitian]`, step "$\langle 0|(\cdots)^\dagger|0\rangle$"; the same step sits in `computation[cft:eq:hermitian-product-rearrangement]`, l. 2444–2457); with the closed-string normalisation `bos:eq:ws-closed-vacuum-normalization` ($-1$, real, on an anti-Hermitian insertion) they hold with an extra factor $\eta = -1$. This is reported as a discrepancy with the book (a missing closed-string qualifier), not corrected silently. The open string ($\langle c_{-1}c_0c_1\rangle = 1$, Hermitian insertion) has $\eta = +1$ and the book's formulas as written.
- (4.1) was found in 028 P.6 item 1 as "anti-equivariance for a constant $\eta$"; the derivation here is its proof. The 64 nonvanishing monomial pairs of the matrix model give $\varepsilon_S\varepsilon_T = -1$ on every pair (check `C4.1-anti-equivariant`); the break leg with $+$ fails on all of them.
- (4.3a) is the operator rule $(XY)^\star = Y^\star X^\star$ of the book turned into a rule on kets; the graded sign is the price of writing $O^\star$ to the left of $A^\star$. It is checked on $c_0^\pm$, $b_0^+$, $c_1$, $b_{-1}$ (an annihilator, where the naive "reverse the word" reading would give zero) and the even composite $c_1\bar c_1$ with $(c_1\bar c_1)^\star = -c_1\bar c_1$.
- (4.4b): the term-by-term step uses that the monomials $\psi_{1,s_1}\cdots\psi_{n,s_n}$ for distinct index tuples are independent, which holds for independent Grassmann generators (odd) and independent numbers (even); the script realises exactly this in a Grassmann algebra on a four-state toy (two even, two odd states) with a generic multilinear $F$ carrying the claimed component sign, and shows the vertex is Hermitian with that sign and not with the uniform $(-1)^n$, not without the Koszul term, not with the opposite sign (`C4.4-*`, `break-C4.4-*`, $n = 3, 4$). The toy tests the bookkeeping from Zwiebach's hermiticity to (4.4), not the hermiticity itself: that is H1. (4.4a) is likewise an input of the toy – `psi` is built to satisfy it and the assert checks the construction – so the step from Zwiebach's (3.6) in state form to (4.4a) is by hand only (recomputed in the node check of 2026-10-03).
- (4.8)–(4.9) use the non-degeneracy of the pairing (R58) to strip $A_0$; (4.9) is stated for even inputs only, the case of every product the paper applies to $\Psi$ and the auxiliary fields, and its $\mathrm{kos}(X) = 0$ rests on the paper's definition of $m^n_m$ with ghost-three outputs, not on the support of $\mathcal V_{m+n}$.
- (4.11) explains the pattern of table (3.1): the cubic action is real precisely because each strand of ghost number two is star-odd, so the auxiliary field replacing $\Psi^{\otimes k}$ must carry $(-1)^k$ – not because $\Sigma_k$ is "real" in a uniform sense.

\subsection*{Result}

$\langle A^\star,B^\star\rangle = -\langle A,B\rangle^*$ (all $A,B$); $\omega_n(X^\star,Y^\star) = (-1)^n\omega_n(X,Y)^*$; $(Q_BA)^\star = (-1)^{|A|+1}Q_BA^\star$; under H1 for $n\ge3$ (unconditionally for $n=2$), $\mathcal V_n(A^\star) = (-1)^{n+\sum_{i<j}|A_i||A_j|}\mathcal V_n(A)^*$, i.e. $(-1)^n$ on even arguments; $\ell_m(A^\star) = (-1)^{m+\sum|A_i|+\sum_{i<j}|A_i||A_j|}\ell_m(A)^\star$, $m^n_m(B^\star) = (-1)^mm^n_m(B)^\star$ on even inputs; the nonpolynomial and the cubic actions are real on the slice (3.1).

\subsection*{Verification}

`C4.1-pairing-value` ($\langle A_1,B_1\rangle = \langle B_1,A_1\rangle = -\tfrac12$, the C1 ledger value, as the anchor of the matrix model), `C4.1-anti-equivariant`, `break-C4.1-equivariant`, `C4.1-random`; `C4.2-n-pairing-sign-k2/k3` (six nonvanishing trials each, strands of both parities), `break-C4.2-opposite-sign-k2/k3`; `C4.3-OA-rule-*`, `break-C4.3-ungraded-*`, `C4.3-Q-rule-stand-in-c0+`; `C4.4-vertex-sign-n3/n4`, `break-C4.4-uniform-sign-*`, `break-C4.4-no-koszul-*`, `break-C4.4-opposite-*`; `C4.4-n2-stand-in-c0+` ((4.4) at $n = 2$ with the stand-in $O = c_0^+$ for $Q_B$, $\langle A^\star,OB^\star\rangle = (-1)^{|A||B|}\overline{\langle A,OB\rangle}$ on the 16 nonvanishing monomial pairs), `break-C4.4-n2-opposite`. Not machine-checked: (4.0) beyond the ghost zero-mode sector (the argument is the uniqueness of the vacuum functional), $Q_B$ itself (the stand-in $c_0^+$ shares $O^\dagger = O$, $O^t = -O$, $|O| = 1$), (4.8)–(4.12) (consequences by substitution).

## 5. Check on explicit states and companion script (item 5)

\subsection*{Setup}

Matrix model of `agent/computations/verify-075-star-conjugation.py`: the ghost Fock space on $|0\rangle$ truncated to the creation modes $c_1,c_0,c_{-1},\bar c_1,\bar c_0,\bar c_{-1}$ (Jordan–Wigner, 64 states; $b_{\mp1}, b_0$ and barred as the transposes, $\{b_m,c_n\} = \delta_{m+n,0}$ asserted), $\langle 0|$ fixed by A1. $\mathrm{hc}$ and $\mathrm{bpz}$ are implemented *independently of (1.3)*, as the bra maps of A3 and A2 (reversed word with $c_n^\dagger = c_{-n}$; kept word with $c_n^t = (-1)^h(\pm1)^nc_{-n}$), and $\star := \mathrm{bpz}^{-1}\circ\mathrm{hc}$ by linear algebra. States: $A_1 = c_1\bar c_1|0\rangle$ (tachyon type, $N_{\rm gh} = 2$), $L_1 = c_0^+|0\rangle$ ($N_{\rm gh} = 1$, $b_0^-L_1 = 0$), $B_1 = c_0^+c_1\bar c_1|0\rangle$ ($N_{\rm gh} = 3$, $b_0^-B_1 = 0$).

\subsection*{Derivation}

By hand, from (1.3) ($I^+$ column; identical with $I^-$, all three are level-matched):
$$
A_1^\star = (-1)^{1}(-1)(-1)\,A_1 = -A_1,\qquad
L_1^\star = -L_1,\qquad
B_1^\star = (-1)^{3}(-1)^3\,B_1 = +B_1 ,\tag{5.1}
$$
($B_1$: $k_o = 3$, $\binom32 = 3$, three $c$ modes). Pairing: $\mathrm{bpz}(B_1) = \langle 0|(-c_0^+)(-c_{-1})(-\bar c_{-1}) = -\langle 0|c_0^+c_{-1}\bar c_{-1}$, so
$$
\langle B_1,A_1\rangle = -\langle 0|c_0^+c_{-1}\bar c_{-1}\,c_0^-\,c_1\bar c_1|0\rangle = -\langle 0|c_{-1}\bar c_{-1}\,c_0^+c_0^-\,c_1\bar c_1|0\rangle = +\langle c_{-1}\bar c_{-1}c_0^-c_0^+c_1\bar c_1\rangle = -\tfrac12 ,\tag{5.2}
$$
$\langle A_1,B_1\rangle = -\tfrac12$ likewise (C1 ledger value). Then $\langle A_1^\star,B_1^\star\rangle = \langle -A_1,B_1\rangle = +\tfrac12 = -\overline{\langle A_1,B_1\rangle}$: (4.1) on the explicit pair. Two-string states: $\Theta_2 = \theta\,B_1\otimes B_1$ ($\theta\in\mathbb R$), $\Sigma_2 = \sigma\,A_1\otimes A_1$: $\Theta_2^\star = \Theta_2$, $\Sigma_2^\star = (+1)\Sigma_2$, $\omega_2(\Theta_2,\Sigma_2) = \theta\sigma\langle B_1,A_1\rangle^2 = \tfrac14\theta\sigma\in\mathbb R$; three strands: $\Sigma_3^\star = -\Sigma_3$, $\omega_3(\Theta_3,\Sigma_3) = -\tfrac18\theta\sigma\in\mathbb R$, and $i\Theta_k$ makes both imaginary: (3.5) on explicit states. $Q_B$ rule on $L_1$: $(c_0^+L_1)^\star$ – the stand-in – vanishes ($c_0^+c_0^+ = 0$); on $A_1$: $(c_0^+A_1)^\star = B_1^\star = B_1 = -c_0^+A_1^\star$, the $(-1)^{|A|+1} = -1$ of (4.3) at even $A$.

\subsection*{Result}

The hand values (5.1)–(5.2) are the script's `C2-A1-star`, `C2-B1-star`, `C3.1-ghost1-star`, `C4.1-pairing-value`, `C3.4-*`, `C4.3-Q-rule-stand-in-c0+`. Script fixes made in this run (the skeleton's run was 66/75): the mode-partner table of `partner()` was inverted (it mapped $c_n\mapsto c_n$, so `hc` and `bpz` were both wrong while their composite $\star$ was right by cancellation – every pairing check of the first run was on a wrong bilinear form); the antilinearity check was a garbled line; the composite $c_1\bar c_1$ carried $s = +1$ instead of $-1$; the $n$-string break legs were vacuous (random strands with vanishing pairings) and now draw the second tensor from the duals of the first and require a nonvanishing value. Final run of 2026-10-03, seed 20261003, 76/76 PASS. Fix pass of 2026-10-04 (node check `critic-075-node-20261003T213500`): `C3.4-multiplier-term-real-k2/k3` rewritten with complex data projected onto the star eigenspaces (plus `C3.4-multiplier-term-not-real-Theta-odd-*` and `break-C3.4-opposite-slice-sign-*`), `C2-ddagger-relation` renamed `consistency-C2-ddagger-implementation` (implementation guard), `C4.4-n2-even` (a tautology) replaced by `C4.4-n2-stand-in-c0+` and `break-C4.4-n2-opposite`. Run of 2026-10-04, seed 20261003, 79/79 PASS, exit 0:

```
PASS C1.1-c1-I+  [c_n^star = -1 c_n]
PASS C1.1-c1-I-  [c_n^star = +1 c_n, n = 1]
PASS C1.1-c0-I+  [c_n^star = -1 c_n]
PASS C1.1-c0-I-  [c_n^star = -1 c_n, n = 0]
PASS C1.1-cm1-I+  [c_n^star = -1 c_n]
PASS C1.1-cm1-I-  [c_n^star = +1 c_n, n = -1]
PASS C1.1-cb1-I+  [c_n^star = -1 c_n]
PASS C1.1-cb1-I-  [c_n^star = +1 c_n, n = 1]
PASS C1.1-cb0-I+  [c_n^star = -1 c_n]
PASS C1.1-cb0-I-  [c_n^star = -1 c_n, n = 0]
PASS C1.1-cbm1-I+  [c_n^star = -1 c_n]
PASS C1.1-cbm1-I-  [c_n^star = +1 c_n, n = -1]
PASS C1.1-c0pm
PASS C1.1-order-c1
PASS C1.1-order-c0
PASS C1.1-order-cm1
PASS C1.1-order-cb1
PASS C1.1-order-cb0
PASS C1.1-order-cbm1
PASS C1.2-word-formula-I+  [64 monomials, random complex lambda]
PASS break-C1.2-no-reversal-sign-I+
PASS C1.2-word-formula-I-  [64 monomials, random complex lambda]
PASS break-C1.2-no-reversal-sign-I-
PASS C1.2-Ipm-agree-level-matched  [24 monomials]
PASS C1.2-star-diagonal
PASS C1.4-star-squared
PASS C1.4-antilinear
PASS break-C1.4-linear
PASS C2-hcinv-bpz-equals-bpzinv-hc
PASS C2-hcinv-bpz-equals-bpzinv-hc-I-
PASS consistency-C2-ddagger-implementation  [implementation guard, not a claim]
PASS C2-A1-star  [c_1 cb_1|0> is star-odd]
PASS C2-B1-star  [c_0^+ c_1 cb_1|0> is star-even]
PASS C2-A1-B1-ddagger
PASS C3.1-tachyon-real-coeff
PASS break-C3.1-tachyon-imag-coeff
PASS C3.1-ghost1-state-in-H
PASS C3.1-ghost1-star  [c_0^+|0> is star-odd]
PASS C3.1-ghost3-star  [c_0^+ c_1 cb_1|0> is star-even]
PASS C4.1-pairing-value
PASS C4.1-anti-equivariant  [64 nonvanishing monomial pairs]
PASS break-C4.1-equivariant
PASS C4.1-random
PASS C4.2-n-pairing-sign-k2  [(-1)^2, 6 nonvanishing trials]
PASS break-C4.2-opposite-sign-k2
PASS C4.2-n-pairing-sign-k3  [(-1)^3, 6 nonvanishing trials]
PASS break-C4.2-opposite-sign-k3
PASS C3.4-Theta-star-even-k2
PASS C3.4-Sigma-star-sign-k2
PASS C3.4-multiplier-term-real-k2  [Theta^star = +Theta: value -1.8320+0.0000j]
PASS C3.4-multiplier-term-not-real-Theta-odd-k2  [Theta^star = -Theta: value +0.0000+0.6611j (imaginary)]
PASS break-C3.4-opposite-slice-sign-k2
PASS C3.4-Theta-star-even-k3
PASS C3.4-Sigma-star-sign-k3
PASS C3.4-multiplier-term-real-k3  [Theta^star = +Theta: value -2.4097+0.0000j]
PASS C3.4-multiplier-term-not-real-Theta-odd-k3  [Theta^star = -Theta: value +0.0000+0.8500j (imaginary)]
PASS break-C3.4-opposite-slice-sign-k3
PASS C4.3-OA-rule-c0+
PASS break-C4.3-ungraded-c0+
PASS C4.3-OA-rule-c0-
PASS break-C4.3-ungraded-c0-
PASS C4.3-OA-rule-b0+
PASS break-C4.3-ungraded-b0+
PASS C4.3-OA-rule-c1
PASS break-C4.3-ungraded-c1
PASS C4.3-OA-rule-b1
PASS break-C4.3-ungraded-b1
PASS C4.3-OA-rule-c1cb1
PASS C4.3-Q-rule-stand-in-c0+  [(QA)^star = (-1)^{|A|+1} Q A^star]
PASS C4.4-vertex-sign-n3  [{A}^dagger = {A} with the claimed component sign]
PASS break-C4.4-uniform-sign-n3
PASS break-C4.4-no-koszul-n3
PASS break-C4.4-opposite-n3
PASS C4.4-vertex-sign-n4  [{A}^dagger = {A} with the claimed component sign]
PASS break-C4.4-uniform-sign-n4
PASS break-C4.4-no-koszul-n4
PASS break-C4.4-opposite-n4
PASS C4.4-n2-stand-in-c0+  [16 nonvanishing pairs]
PASS break-C4.4-n2-opposite

seed 20261003: 79/79 PASS
```

## 6. The tensor-product convention (A5) and its alternative

A5 extends $\star$ strand by strand. The alternative, suggested by the book's operator rule "reverse the order without a sign" read on $A_1\otimes\cdots\otimes A_k$ as a product, is $(A_1\otimes\cdots\otimes A_k)^{\star'} := (-1)^{\sum_{i<j}|A_i||A_j|}A_1^\star\otimes\cdots\otimes A_k^\star$, the Koszul sign of reversing the strands. The two agree whenever at most one strand is odd, hence on every tensor of this record except $\Theta_k$ ($\Psi^{\otimes k}$, $\Sigma_k$, $\Upsilon_2$: even strands; $\Theta_k$: odd strands, where they differ by $(-1)^{k(k-1)/2}$, 028 (C2)). Under $\star'$ the table (3.1) changes only at $\Theta_k$: $\Theta_k^{\star'} = (-1)^{k(k-1)/2}\Theta_k^\star$, so $\Theta_k^{\star'} = (-1)^{k(k-1)/2}\Theta_k$ for the same field, and (4.2) acquires the same factor on both sides of the multiplier term (it cancels in (3.5)); nothing physical moves (055 C3.3: a conjugation-convention sign, not an exchange sign). A5 is the choice of the paper's text (appendix A, "On a tensor it acts strand by strand, without a reordering sign") and of C3; this record keeps it and reports it as a `local` convention candidate.

## Result

**Sign table (3.1), verbatim.** $X^\star = \varepsilon_X X$ with
$$
\varepsilon_\Psi = -1,\qquad \varepsilon_\Lambda = -1,\qquad \varepsilon_{\Sigma_k} = (-1)^k,\qquad \varepsilon_{\Upsilon_2} = +1,\qquad \varepsilon_{\Theta_k} = +1 .
$$

**Relation to the former involution (2.1)–(2.2).** $A^\ddagger = (-1)^{N_{\rm gh}(A)+1}A^\star$ on single strands, $X^\ddagger = (-1)^{k(N+1)}X^\star$ on $k$ strands of ghost number $N$; no further sign on odd states ($\mathrm{bpz}^{-1}\circ\mathrm{hc} = \mathrm{hc}^{-1}\circ\mathrm{bpz}$ on kets).

**Per-display signs for appendix A** (`paper/sections/A-conventions.tex`, paragraph "Reality"; line numbers of the current file):

| display | lines | sign to write | status |
|---|---|---|---|
| `eq:conv:pairing-equivariance` | 266–268 | $\pair{A^\star}{B^\star} = -\,\pair{A}{B}^*$, for all $A$, $B$ (no ghost-number dependence; "up to a sign fixed by the ghost numbers" → "up to a minus sign") | (4.1), unconditional |
| `eq:conv:QB-star` | 272–274 | $(Q_BA)^\star = (-1)^{\abs{A}+1}\,Q_BA^\star$ ($-$ on even $A$, $+$ on odd $A$) | (4.3), unconditional |
| `eq:conv:vertex-reality` | 278–280 | $\vertex{n}(A_1,\ldots,A_n)^* = (-1)^{\,n+\sum_{i<j}\abs{A_i}\abs{A_j}}\,\vertex{n}(A_1^\star,\ldots,A_n^\star)$; on even arguments $(-1)^n$ | (4.4): $n=2$ unconditional, $n\ge3$ under PH6 (the paragraph's existing "we assume it for every $n$") |
| multi-string pairing (sentence l. 286, no display) | 286 | $\pair[n]{X^\star}{Y^\star} = (-1)^n\,\pair[n]{X}{Y}^*$ | (4.2), unconditional |
| `eq:conv:reality-fields` | 288–303 | $\Psi^\star = -\Psi$, $\Sigma_k^\star = (-1)^k\Sigma_k$, $\Upsilon_2^\star = +\Upsilon_2$ (rename $\Xi_2\to\Upsilon_2$ at l. 295–296, 306, 310, 312), $\Theta_k^\star = +\Theta_k$, $\Lambda^\star = -\Lambda$ | (3.1); the interaction part of $\Lambda$'s derivation and the auxiliary-field reality under PH6 |
| `\agcomment{gap: …}` | 305 | remove | – |
| sentence "It is antilinear and squares to one … up to a sign" | 258 | the sign is $(-1)^{k_o(k_o-1)/2}\prod_i s_{O_i}$ with $s_c = -1$, $s_b = +1$, $s_\alpha = -1$ (optional precision) | (1.3) |

**Discrepancy with the book (to report, not corrected).** `cft:eq:bpz-product-hermitian` and `cft:eq:bpz-product-star` ($\overline{\langle A|O|B\rangle} = \langle B^\star|O^\dagger|A^\star\rangle$), and the same step in `computation[cft:eq:hermitian-product-rearrangement]` (l. 2444–2457), are derived with a Hermitian vacuum functional; with the closed-string normalisation `bos:eq:ws-closed-vacuum-normalization` the functional is anti-Hermitian ((4.0), $\eta = -1$, Zwiebach (2.37)) and both formulas carry an extra minus sign for the closed string. The open string ($\langle c_{-1}c_0c_1\rangle = 1$) is as written.

**Proposed ledger entries.**

- *Conventions, `local` candidate (replacing C3).* "C3′ — Reality conjugation (star). $A^\star := \mathrm{bpz}^{-1}(\mathrm{hc}(A)) = \mathrm{hc}^{-1}(\mathrm{bpz}(A))$ on kets (Erbin 2023 `cft:eq:conj-star`, `cft:eq:state-equivalence-star-hermitian`; live LaTeX 1dbb721), strand by strand on $\mathcal H^{\otimes k}$ without Koszul sign (028 (C2)). On a creation word, $\star$ conjugates the coefficient, flips the momentum and multiplies the monomial by $(-1)^{k_o(k_o-1)/2}\prod_i s_{O_i}$, $s_c = -1$, $s_b = +1$, $s_\alpha = -1$ ($I^+$; $I^-$ adds $(-1)^n$ per mode, invisible on level-matched states); $\star^2 = 1$. Former $\ddagger = (-1)^{N_{\rm gh}+1}\star$ (record 075 (2.1)). Pairing anti-equivariant, $\langle A^\star,B^\star\rangle = -\langle A,B\rangle^*$ (Zwiebach (2.37)); $\omega_n$: $(-1)^n$; $(Q_BA)^\star = (-1)^{|A|+1}Q_BA^\star$. Reality: $\Psi^\star = -\Psi$ (Zwiebach (3.6)), $\Lambda^\star = -\Lambda$ (3.18; compatible with the interaction terms under PH6), $\Sigma_k^\star = (-1)^k\Sigma_k$, $\Upsilon_2^\star = \Upsilon_2$ (R35's content translated, under PH6), $\Theta_k^\star = \Theta_k$. Checked on $A_1 = c_1\bar c_1|0\rangle$ (star-odd), $B_1 = c_0^+c_1\bar c_1|0\rangle$ (star-even), $\langle A_1,B_1\rangle = -\tfrac12$; `agent/computations/verify-075-star-conjugation.py`, 79/79 (2026-10-04)."
- *Results.* "R? — Reality conditions and equivariance signs of the cubic theory in the star convention [Verified (C1, C2, C3.1, C3.4, C4.1–C4.3; C4.4 bookkeeping for $n = 3, 4$ and (4.4) at $n = 2$ with the $c_0^+$ stand-in); derived by hand from these ((4.8)–(4.12), C3.2's free part, C3.5); Conditional(PH6) for (4.4) at $n\ge3$, (4.8)–(4.12), the interaction part of $\Lambda$'s condition and the auxiliary-field reality through R35]. Source: `agent/derivations/075-star-conjugation-convention.md#C1`–`#C4`." Verification lines: C1.1–C1.4, C2, C3.1, C3.4, C4.1–C4.4 as named in §5 (79/79, 2026-10-04).

**Self-review.** (1) The objective – every sign of appendix A's reality statements traced – is met by the per-display table; the auxiliary-field signs rest on R35's content (forced by sources, imposed on kernel directions), translated, not re-derived. (2) Weakest step: (4.4b)'s term-by-term independence of coefficient monomials, which is Zwiebach's own reading of the hermiticity of the vertices and is realised in the Grassmann toy; and (4.0)'s uniqueness-of-the-vacuum-functional argument, machine-checked only on the zero-mode sector. (3) Not checked: the matter sector and the momentum (argued from the mode rule (1.1)); $Q_B$ itself (stand-in $c_0^+$); the open-string comparison (3.6) (hand computation). (4) A stronger reader would ask whether the book's `cft:eq:bpz-product-star` and this record's (4.1) can both be right: they can, the book's derivation assumes $\eta = +1$; this is reported.

## Status

Complete (items 1–5, §6, Result); node check passed (2026-10-03); fix pass applied (2026-10-04, brief `computator-075-fix-pass-20261004T021100`). Script 79/79 PASS (seed 20261003). Next: appendix A edits by the science-writer from the per-display table; ledger C3′/R81 count references (76/76) to be refreshed by the orchestrator.

## Annotation (orchestrator, 2026-10-03)

Node check `agent/reports/critic-075-node-20261003T213500.md`: C1–C4 hold; its wording fixes, the H1 naming at C3/C4 and in the summary, and the script fixes (`C3.4-multiplier-term-real` vacuous — falsifiable rewrite in the report; `C2-ddagger-relation`, `C4.4-n2-even` tautologies) are pending a short fix pass. Ledger: C3′ (`knowledge/conventions.md`) and R81 (`knowledge/results.md`) written from this record with the labels the node check allows.

2026-10-04 (computator fix pass, brief `computator-075-fix-pass-20261004T021100`): H1 named at C3 and C4, in the summary and in the `Hypotheses in force:` line (C3.4 not conditional: (3.5) uses $\Sigma_k^\star = (-1)^k\Sigma_k$ only as the definition of the slice); the node check's wording fixes applied (identification of Zwiebach's bracket with $\mathcal V_n$ in H1, cited in C4.4; star eigenbasis at $p\ne0$; (4.9)'s justification from the paper's definition of $m^n_m$; (4.4a) an input of the toy; the third book equation in the discrepancy note; §6 sentence; C2/C1.4 same identity); script: `C3.4-multiplier-term-real` rewritten as falsifiable (broken once on purpose, FAIL confirmed, restored), `C2-ddagger-relation` → `consistency-C2-ddagger-implementation`, `C4.4-n2-even` → `C4.4-n2-stand-in-c0+` with a break leg; 76/76 → 79/79 PASS. Ledger labels of R81 and C3′ checked against the node check's table: no overclaim, nothing changed there.
