# 055 – Graded exchange symmetry of $\omega_k=\omega_1^{\otimes k}$ for general $k$

Brief: `agent/briefs/active-computator-omega-k-20260926T025500.md` (Task 9d).
Script: `codes/verify-omega-k.py`. Log: `agent/scratch/omega-k-run1.log`.

## Task and objective

- **Literal task.** Derive the exchange sign $\sigma_k$ in $\omega_k(Y,X)=(-1)^{\epsilon(X)\epsilon(Y)+\sigma_k}\omega_k(X,Y)$ for $\omega_k=\omega_1^{\otimes k}$ on $\mathcal H^{\otimes k}$, physical statistics $\epsilon=N_{\rm gh}\bmod2$, all $k$; restrict to $\mathrm{Sym}^k\mathcal H_0$ and to the Route C pairing; list the ledger consequences.
- **Objective.** Remove R12's carve-out "$k\ge3$ expected, unchecked" and settle whether R13's Route C and 028 §4's signs depend on the symmetry type of $\omega_k$ at each $k$.
- *Correction 2026-09-26 (critic-055-20260926T032500):* R12's carve-out is stated on $\mathcal H^{\otimes k}$ and is closed by C1+C3.1 below; it is not vacuous as worded. Vacuity holds only for the restriction to $\mathrm{Sym}^k\mathcal H_0\times\mathrm{Sym}^k\mathcal H_0$ (C2.2).

## Conventions and setup

- **A1** (physical statistics, 002 R2.1). $\epsilon(\phi)=N_{\rm gh}(\phi)\bmod2$; $c_0^-$ odd; $N_{\rm gh}(\Psi)=2$.
- **A2** (support, 002 R2.4–R2.5). $\omega_1(A,B)=\langle A|c_0^-|B\rangle\neq0$ only if $N_{\rm gh}(A)+N_{\rm gh}(B)=5$, hence $\epsilon(A)+\epsilon(B)=1$ on support.
- **A3** (exchange sign of $\omega_1$, parametrised). $\omega_1(B,A)=s\,(-1)^{\epsilon(A)\epsilon(B)}\,\omega_1(A,B)$ on support, $s\in\{+1,-1\}$. 002 R2.6 / R7 state $s=-1$; the book states $\langle A,B\rangle=(-1)^{(1+|A|)(1+|B|)}\langle B,A\rangle$ [Erbin 2023 live LaTeX, `bos:eq:closed-product-rearrangement`, commit 1dbb7217], which on support is $s=+1$. The general-$k$ result is derived for both values; which one holds is settled in C3.1.
- **A4** (Koszul tensor of forms, 002 R2.7). For homogeneous $X=x_1\otimes\cdots\otimes x_k$, $Y=y_1\otimes\cdots\otimes y_k$:
  $\omega_k(X,Y):=(-1)^{\kappa(X,Y)}\prod_{i=1}^k\omega_1(x_i,y_i)$, $\kappa(X,Y)=\sum_{i<j}\epsilon(y_i)\epsilon(x_j)$ – the Koszul sign of the shuffle $x_1\cdots x_ky_1\cdots y_k\to(x_1y_1)\cdots(x_ky_k)$. At $k=2$ this is 002's R2.7. Extended bilinearly.
- **A5** (Koszul $S_k$ action). $\pi\cdot(x_1\otimes\cdots\otimes x_k)=\pm\,x_{\pi^{-1}(1)}\otimes\cdots$ with the Koszul sign; $\mathrm{Sym}^k$ = invariants. On $\mathcal H_0$ (all strands at $N_{\rm gh}=2$, even) this is the ordinary symmetric power, as in R12.
- No `knowledge/conventions.md` exists in the project; A1–A5 are local. Candidate ledger entry: A4 (the Koszul definition of $\omega_1^{\otimes k}$), A3 once C3.1 is accepted ($s=+1$), and **A6** the order-preserving BPZ product rule $\mathrm{bpz}(AB)=\mathrm{bpz}(A)\,\mathrm{bpz}(B)$ (no graded sign; Sen 2016, cited by the book at `cft_operator_formalism.tex` l.1134–1146) — on creation monomials this is the graded anti-involution, not an independent choice. *Correction 2026-09-30 (002 step 4′):* $s$ turns on the zero-mode sign (ii), $s=-\sigma_0$; 002 R2.6 violated (ii) ('self-BPZ-conjugacy' of $c_0^-$, i.e. $\sigma_0=+1$), not A6.

## Claim tree

Assumptions: A1–A5 above. Hypotheses: none.

- **C1** For every $k\ge1$ and all homogeneous $X,Y\in\mathcal H^{\otimes k}$ (on or off support):
  $\omega_k(Y,X)=s^k(-1)^{\epsilon(X)\epsilon(Y)}\omega_k(X,Y)$, i.e. $\sigma_k\equiv k\cdot\tfrac{1-s}{2}\pmod2$. [by C1.1–C1.3]
  - **C1.1** The exchange exponent of the Koszul tensor (A4) is $\sum_{i,j}\epsilon(x_i)\epsilon(y_j)=\epsilon(X)\epsilon(Y)$ plus one factor $s$ per strand. [eq. (B1.4); by check: C1.1]
  - **C1.2** Grouping the $k$ odd $c_0^-$ as a tensor of odd maps, or as the operator $(c_0^-)^{\otimes k}$ acting on $Y$ followed by the BPZ tensor pairing, gives the same exchange law on support. [eq. (B1.6); by check: C1.2]
  - **C1.3** The only grouping-dependent sign is a normalisation: the odd-map grouping equals A4 times the constant $(-1)^{k(k-1)/2}$ on support, which is exchange-invariant. The brief's expected $\sigma_k=k(k-1)/2$ is this constant, not an exchange sign. [eq. (B1.5); by check: C1.3, BRK2]
- **C2** Restrictions. [by C2.1–C2.3]
  - **C2.1** On support, $\omega_k(\pi X,\pi Y)=\mathrm{sgn}(\pi)\,\omega_k(X,Y)$ for the Koszul $S_k$ action (A5), for either $s$. [eq. (B2.1); by check: C2.1]
  - **C2.2** $\omega_k$ vanishes identically on $\mathcal H_0^{\otimes k}\times\mathcal H_0^{\otimes k}$ (per strand $2+2\neq5$): its exchange symmetry on $\mathrm{Sym}^k\mathcal H_0$ alone is vacuous. *(This vacuity is specific to the $\mathrm{Sym}^k\mathcal H_0\times\mathrm{Sym}^k\mathcal H_0$ restriction; R12's carve-out, stated on the full $\mathcal H^{\otimes k}$, is not vacuous — see the Correction under Task and objective.)* [by A2; by check: C2.2]
  - **C2.3** The $\omega_k$-dual of $\mathrm{Sym}^k\mathcal H_0$ inside $\mathcal H_3^{\otimes k}$ is the Koszul-antisymmetric part (component arrays symmetric); the Koszul-symmetric part pairs to zero; the pairing is non-degenerate on the finite toy (rank $=\dim\mathrm{Sym}^k\mathcal H_0$). [by C2.1; by check: C2.3]
- **C3** Consequences. [by C3.1–C3.4]
  - **C3.1** $s=+1$ on support, established by two convention-independent routes: (a) the book's rearrangement formula (B3.1), and (b) an explicit mode computation on $A=c_1\bar c_1|0\rangle$, $B=c_0^+c_1\bar c_1|0\rangle$ (B3.4), using only the mode-level BPZ rules (ii)–(iii) and no rearrangement identity. The kinetic-term argument (B3.2) is a *consistency check* of the pair (exchange sign $s$, BRST adjointness sign), not a third independent determination: both signs are fixed by the zero-mode sign of (ii) and flip together under $\sigma_0\to-\sigma_0$, leaving the kinetic term non-vanishing in both cases. Hence $\omega_k$ is graded symmetric for every $k$ ($\sigma_k=0$), and 002 R2.6 ($s=-1$) is in conflict with the book. [cited: Erbin2023 live LaTeX `bos:eq:closed-product-rearrangement` (commit 1dbb7217); Zwiebach (1993), Nucl. Phys. B390, §2 (original source of the bilinear form and its exchange relation); Sen (2016) for the order-preserving BPZ product rule (iii); eq. (B3.1), (B3.4); by check: C3.1, C3.1b]
  - **C3.2** R7's headline ($\omega_2$ graded symmetric) holds for both $s$ ($s^2=1$); its stated reason ("one $c_0^-$ antisymmetric, two symmetric") holds only if $s=-1$. 002's "$n=3$ preliminary: $\omega_3$ symmetric" misreports its own script output (sym-viol 64, anti-viol 0, i.e. antisymmetric under the script's $s=-1$), consistent with C1. [by C1, C3.1; script output of `codes/verify-omega2-physical.py` re-run 2026-09-26]
  - **C3.3** Route C: $\omega_k(\sigma_k,\lambda_k)=s^k\omega_k(\lambda_k,\sigma_k)=\omega_k(\lambda_k,\sigma_k)$ (C3.1); $N_{\rm gh}(\lambda_k)=3k$ follows from per-strand saturation and does not depend on the exchange sign; 028 (4.1) is unaffected; 028's $(-1)^{k(k-1)/2}$ is the Koszul sign of reversing $k$ odd strands, i.e. C2.1 at $\pi=$ reversal, a conjugation-convention sign and not an exchange sign. [by C1, C2.1, C3.1; by check: C3.2, C3.3]
  - **C3.4** R26's kinetic terms $a_k\hat M_k$ are symmetric bilinear forms built from $\tilde M_k$ and $T_{2k+1}$ on $\mathrm{Sym}^k\mathcal H_0$ (019 l.109–120), with no $\omega_k$: no tower sign depends on $\sigma_k$. [by C2.2; 019 l.109–120]

Open gaps: none
Hypotheses in force: none

## Derivation

### B1 – Exchange sign for general $k$

\subsection*{Setup}
A1–A5. $a_i=\epsilon(x_i)$, $b_i=\epsilon(y_i)$, arithmetic mod 2; $p_i=a_i+b_i$ (pair parity, $p_i=1$ on support by A2).

\subsection*{Derivation}
$$\begin{aligned}
\omega_k(X,Y)&=(-1)^{\sum_{i<j}b_ia_j}\prod_i\omega_1(x_i,y_i),\\
\omega_k(Y,X)&=(-1)^{\sum_{i<j}a_ib_j}\prod_i\omega_1(y_i,x_i)\\
&=(-1)^{\sum_{i<j}a_ib_j}\prod_i\big[s\,(-1)^{a_ib_i}\omega_1(x_i,y_i)\big]\\
&=s^k(-1)^{\sum_{i<j}a_ib_j+\sum_ia_ib_i+\sum_{i<j}b_ia_j}\,\omega_k(X,Y)\\
&=s^k(-1)^{\sum_{i,j}a_ib_j}\,\omega_k(X,Y)=s^k(-1)^{\epsilon(X)\epsilon(Y)}\,\omega_k(X,Y).
\end{aligned}\tag{B1.1–B1.4}$$
Other groupings of the $k$ odd insertions. (i) Tensor of $k$ odd maps $\omega_1:\mathcal H\otimes\mathcal H\to\mathbb C$: the $j$-th $\omega_1$ passes the pairs $1,\dots,j-1$,
$$\omega_k^{\rm map}(X,Y)=(-1)^{\sum_{i}(k-i)p_i}\,\omega_k(X,Y)\;\stackrel{\rm supp}{=}\;(-1)^{k(k-1)/2}\,\omega_k(X,Y).\tag{B1.5}$$
The prefactor depends on $X,Y$ only through the $p_i$, which are exchange-symmetric, so the exchange law is unchanged. (ii) Operator insertion $(c_0^-)^{\otimes k}$ on $Y$ (the $j$-th $c_0^-$ passes $y_1,\dots,y_{j-1}$) followed by the BPZ tensor pairing (even form, Koszul shuffle with $\epsilon(c_0^-y_i)=b_i+1$):
$$\omega_k^{\rm op}(X,Y)=(-1)^{\delta(X,Y)}\omega_k(X,Y),\quad
\delta(X,Y)=\sum_i(k-i)b_i+\sum_j(j-1)a_j,\quad
\delta(X,Y)+\delta(Y,X)=(k-1)\sum_ip_i\stackrel{\rm supp}{\equiv}k(k-1)\equiv0.\tag{B1.6}$$

\subsection*{Commentary}
(B1.3) uses A3 in each slot; the $s^k$ is the only place where the ghost-number content of $c_0^-$ enters. (B1.4): the three partial sums ($i<j$, $i=j$, $i>j$ after relabelling the Koszul term of $\omega_k(X,Y)$) cover all pairs $(i,j)$, so the result holds on every homogeneous pair, not only on support; 002's term-by-term cancellation of the $a_1a_2$ cross terms (R2.10a) is the $k=2$ case of this identity combined with the support relation. (B1.5): with $p_i=1$, $\sum_{i=1}^k(k-i)=k(k-1)/2$ – this is where the brief's expected $k(k-1)/2$ lives: an overall, exchange-invariant normalisation of $\omega_1^{\otimes k}$, not an exchange sign. (B1.6): the operator grouping differs from A4 by an $X,Y$-dependent sign, but its exchange-symmetrised exponent is even on support.

\subsection*{Result}
$$\boxed{\;\omega_k(Y,X)=s^k\,(-1)^{\epsilon(X)\epsilon(Y)}\,\omega_k(X,Y),\qquad\sigma_k\equiv k\,\tfrac{1-s}{2}\pmod 2,\;}$$
independent of how the $k$ insertions of $c_0^-$ are grouped (up to the exchange-invariant constant (B1.5)). On support $\epsilon(Y)=\epsilon(X)+k$, so for odd $k$ $\epsilon(X)\epsilon(Y)=0$ and the statement is plain (anti)symmetry $\omega_k(Y,X)=s\,\omega_k(X,Y)$.

\subsection*{Verification}
`codes/verify-omega-k.py` C1.1 (both $s$, $k=1..5$, 1500 random basis-tensor pairs each, on and off support), C1.2 (both groupings), C1.3 (constant $(-1)^{k(k-1)/2}$). Break legs: BRK1 the nearest-neighbour extension $\sum_ib_ia_{i+1}$ of R2.7 fails at $k=3$ (~500 violations for each $s$); BRK2 the guess $\sigma_k=k(k-1)/2$ fails at $k=2,3$ ($s=+1$) and $k=2,5$ ($s=-1$); BRK3 the wrong power $s^{k+1}$ fails at $k=3$ for $s=-1$ (1092 violations; vacuous for $s=+1$, as it must be).

### B2 – Restrictions: $S_k$ covariance, $\mathrm{Sym}^k\mathcal H_0$, Route C dual

\subsection*{Setup}
A2, A5. $\epsilon_\pi(X)$ the Koszul sign of $\pi$ on $X$.

\subsection*{Derivation}
The Koszul sign of a permutation of the $2k$ strands is path-independent. Going from $x_1\cdots x_ky_1\cdots y_k$ to the ordered pairs $(x_{\pi(1)}y_{\pi(1)})\cdots$ either via $(\pi X,\pi Y)$ or via the pairs in original order and then permuting the pairs:
$$\epsilon_\pi(X)\,\epsilon_\pi(Y)\,(-1)^{\kappa(\pi X,\pi Y)}=(-1)^{\kappa(X,Y)}\,(-1)^{\sum_{\text{inversions }(i,j)\text{ of }\pi}p_ip_j}
\;\Rightarrow\;\omega_k(\pi X,\pi Y)\stackrel{\rm supp}{=}\mathrm{sgn}(\pi)\,\omega_k(X,Y).\tag{B2.1}$$
Take $X=\Sigma\in\mathrm{Sym}^k\mathcal H_0$ ($\pi\Sigma=\Sigma$, no Koszul sign since all strands are even) and $\Lambda\in\mathcal H_3^{\otimes k}$. Then $\omega_k(\Sigma,\Lambda)=\mathrm{sgn}(\pi)\,\omega_k(\Sigma,\pi\Lambda)$, so only the part with $\pi\Lambda=\mathrm{sgn}(\pi)\Lambda$ (Koszul action) pairs with $\mathrm{Sym}^k\mathcal H_0$. For all-odd strands the Koszul action is $\pi\Lambda=\mathrm{sgn}(\pi)\,\Lambda^{\rm plain}_\pi$, so this is the part whose component array is plain-symmetric, i.e. the Koszul-antisymmetric part $\Lambda^k_{\rm gr}\mathcal H_3$. (B2.2)

\subsection*{Commentary}
(B2.1) is independent of $s$: permuting pairs does not exchange $x$ with $y$. It is the décalage statement $\mathrm{Sym}^k(V)\leftrightarrow\Lambda^k(V[1])$: $\omega_1$ has odd degree, so its tensor powers are $S_k$-covariant only up to $\mathrm{sgn}$. (B2.2): in 028 §4.2 "the $\mathrm{Sym}^k$-dual part of $\lambda_k$" is therefore the Koszul-antisymmetric part of $\mathcal H_3^{\otimes k}$ – equivalently, components $\lambda^{i_1\cdots i_k}$ symmetric in the indices; with commuting toy components (028's script) the two descriptions coincide, so 028's toy is unaffected.

\subsection*{Result}
On support $\omega_k$ is $\mathrm{sgn}$-covariant under simultaneous Koszul permutations; its exchange symmetry restricted to $\mathrm{Sym}^k\mathcal H_0\times\mathrm{Sym}^k\mathcal H_0$ is vacuous ($\omega_k\equiv0$ there); the Route C pairing is $\mathrm{Sym}^k\mathcal H_0\times\Lambda^k_{\rm gr}\mathcal H_3$, non-degenerate iff $\omega_1$ is (toy: rank $=\binom{n+k-1}{k}$).

\subsection*{Verification}
C2.1 ($k=2..4$, random permutations, both $s$), C2.2, C2.3 (rank of $P_{\rm Sym}^\top M P_{\Lambda_{\rm gr}}$ equals $\dim\mathrm{Sym}^k\mathcal H_0$ = 3, 4, 5 at $k=2,3,4$, $n=2$; the Koszul-symmetric block is exactly 0 – the "wrong-dual" claim fails, C2.3-brk).

### B3 – Which $s$: book relation and kinetic-term argument

\subsection*{Setup}
A1–A3. $\langle A,B\rangle:=\omega_1(A,B)$ [Erbin 2023], $|A|=\epsilon(A)$.

\subsection*{Derivation}
Book (live LaTeX, `bos:eq:closed-product-rearrangement` and its computation block, commit 1dbb7217):
$$\langle A,B\rangle=-(-1)^{|A|(1+|B|)}(-1)^{|B|}\langle B,A\rangle=(-1)^{(1+|A|)(1+|B|)}\langle B,A\rangle
=(-1)^{1+|A|+|B|}(-1)^{|A||B|}\langle B,A\rangle\;\stackrel{\rm supp}{=}\;(-1)^{|A||B|}\langle B,A\rangle.\tag{B3.1}$$
*Correction 2026-09-26 (critic-055-20260926T032500):* the following was originally presented as an independent argument for $s=+1$; it is a consistency argument only, since the adjointness sign it uses is fixed by the same zero-mode sign (ii) as $s$ (see B3.4 below for the independent determination). Consistency argument: the adjointness relation $\langle A,Q_BB\rangle=(-1)^{|A|}\langle Q_BA,B\rangle$ (same book equation, derived from $\mathrm{bpz}(Q_B)=-Q_B$, same conventions) forces $s$ to equal the adjointness sign at even $A$; with the book's $(-1)^{|A|}$ this is $s=+1$. For Grassmann-even $\Psi_1,\Psi_2$ at $N_{\rm gh}=2$:
$$\langle\Psi_1,Q_B\Psi_2\rangle=\langle Q_B\Psi_1,\Psi_2\rangle\stackrel{\rm A3}{=}s\,(-1)^{1\cdot0}\langle\Psi_2,Q_B\Psi_1\rangle=s\,\langle\Psi_2,Q_B\Psi_1\rangle.\tag{B3.2}$$
With $s=-1$ the bilinear form $\langle\Psi_1,Q_B\Psi_2\rangle$ is antisymmetric and the free action $\tfrac12\langle\Psi,Q_B\Psi\rangle$ (c-number coefficients) vanishes identically. Under the opposite zero-mode sign $\sigma_0=+1$, which forces $\mathrm{bpz}(Q_B)=+Q_B$ through the $c_0L_0$ term, both the adjointness sign and $s$ flip together, and the kinetic term is again symmetric — so (B3.2)–(B3.3) fixes "$s$ equals the adjointness sign", not the value of $s$ on its own. (B3.3)

**(B3.4) Independent determination: explicit mode computation, no rearrangement formula used.** Take $|A\rangle=c_1\bar c_1|0\rangle$ ($N_{\rm gh}=2$, even) and $|B\rangle=c_0^+c_1\bar c_1|0\rangle$ ($N_{\rm gh}=3$, odd). By (ii)–(iii) [$\mathrm{bpz}(c_n)=(-1)^{n-1}c_{-n}$, $\mathrm{bpz}(b_n)=(-1)^nb_{-n}$, hence $\mathrm{bpz}(c_0^\pm)=-c_0^\pm$; BPZ conjugation of a product of modes is order-preserving with no graded sign], $\langle A|=\langle0|c_{-1}\bar c_{-1}$ and $\langle B|=\langle0|\,\mathrm{bpz}(c_0^+)\,\mathrm{bpz}(c_1)\,\mathrm{bpz}(\bar c_1)=-\langle0|c_0^+c_{-1}\bar c_{-1}$. Using $\langle c_{-1}\bar c_{-1}c_0^-c_0^+c_1\bar c_1\rangle=-\tfrac12$:
$$\omega_1(A,B)=\langle0|c_{-1}\bar c_{-1}c_0^-c_0^+c_1\bar c_1|0\rangle=-\tfrac12,$$
$$\omega_1(B,A)=-\langle0|c_0^+c_{-1}\bar c_{-1}c_0^-c_1\bar c_1|0\rangle=-\langle0|c_{-1}\bar c_{-1}c_0^+c_0^-c_1\bar c_1|0\rangle=+\langle0|c_{-1}\bar c_{-1}c_0^-c_0^+c_1\bar c_1|0\rangle=-\tfrac12$$
(moving $c_0^+$ past the two odd modes $c_{-1}\bar c_{-1}$ costs no sign; $c_0^+c_0^-=-c_0^-c_0^+$). So $\omega_1(A,B)=\omega_1(B,A)$ with $\epsilon(A)\epsilon(B)=0$: $s=+1$. Had the bras been built with reversed order, both $\langle A\vert=\langle0\vert c_{-1}\bar c_{-1}$ and $\langle B\vert$ would change sign, leaving $s=+1$ (002 step 4′, check REV). What decides $s$ is the zero-mode sign (ii): $\mathrm{bpz}(c_0^\pm)=+c_0^\pm$ gives $s=-1$ (check BRK-b). Beyond the zero modes the non-graded reversed rule has no uniform exchange sign, so it is not a convention alternative. This route uses no rearrangement identity and is independent of (B3.1); it agrees with (B3.1) at $(|A|,|B|)=(0,1)$: $(-1)^{1\cdot2}=+1$.

\subsection*{Commentary}
(B3.1): the book's relation is graded symmetric in the suspended degree $|A|+1$ everywhere; on the support ($|A|+|B|$ odd) it is graded symmetric in the physical parity. 002 R2.6 claims the opposite, $\omega_1(A,B)=-(-1)^{\epsilon(A)\epsilon(B)}\omega_1(B,A)$, with a one-line argument ("moving the single odd $c_0^-$ gives one extra minus sign") that omits the BPZ conjugation sign of $c_0^-$ (the book's `bos:eq:conjugation-c0pm-b0pm`) and the ordering reversal; the book's computation block carries both.

*Correction 2026-09-26 (critic-055-20260926T032500):* the two determinations of $s$ that are convention-independent of each other are (a) the book's rearrangement formula (B3.1) and (b) the explicit mode computation on $A=c_1\bar c_1|0\rangle$, $B=c_0^+c_1\bar c_1|0\rangle$ (B3.4). (B3.2)–(B3.3), the kinetic-term argument, is *not* independent of the book's BPZ bookkeeping — it is a cross-check of the pair (exchange sign $s$, BRST adjointness sign), both fixed by the same conventions (ii)–(iii). The symplectic form of the BV literature is $(-1)^{|A|}\langle A,B\rangle$ (book, `homotopy_algebra.tex` l.493 comment, EKS), which is graded antisymmetric in the suspended degree – that is the object 002's step-4 dictionary should be compared with, not $\langle A,B\rangle$ itself.

\subsection*{Result}
$s=+1$: $\omega_1$ is graded symmetric in the physical parity on its support, and by B1
$$\boxed{\;\omega_k(Y,X)=(-1)^{\epsilon(X)\epsilon(Y)}\,\omega_k(X,Y)\quad\text{for every }k\ge1,\qquad\sigma_k=0.\;}$$

\subsection*{Verification}
C3.1 (toy: $Q$ built generically subject to the adjointness relation; $s=-1$ gives $\max|K|=10^{-15}$, $s=+1$ gives $O(1)$) — *Correction 2026-09-26:* this check encodes the consistency condition (B3.2)/(B3.3), i.e. "$s=-1$ + book adjointness sign $\Rightarrow$ vanishing kinetic form", not an independent determination of $s$; it corroborates (B3.4)'s value but does not establish it. C3.1b (the book's derivation line equals the stated relation for all four parity pairs, and gives $s=+1$ at $(0,1)$) is a transcription guard on (B3.1). The independent determination of $s$ is the mode computation (B3.4), machine-checkable only as a representation (explicit $6$-mode Fock states); not machine-checked here. Not machine-checked: the book's BPZ sign of $c_0^-$ itself (cited).

### B4 – Consequences for R7, R12, R13, 028, R26

- **R12** carve-out: closed. $\omega_k$ graded symmetric for every $k$ (B3 result), and C2 fixes what "on $\mathrm{Sym}^k$" means.
- **R7**: the headline (graded symmetric at $k=2$) stands for either $s$. The reason in R7 ("two odd $c_0^-$ ⇒ even operation", by contrast with a graded-antisymmetric $\omega_1$) rests on 002 R2.6, which conflicts with the book (B3). R7's wording should be amended; its downstream statements that use only "$\omega_2$ graded symmetric" are unaffected. Statements that use "$\omega_1$ graded antisymmetric in physical parity" (002 step 4 dictionary table; R7 "one odd suspension unit") need a separate check – out of scope here, flagged.
- **002 n3 note**: the record says "$\omega_3$ symmetric (sym-viol 0, anti-viol 64)"; the script prints sym-viol 64, anti-viol 0 (re-run 2026-09-26) – antisymmetric under the script's $s=-1$, as B1 predicts. Transcription error in 002; under the book's $s=+1$, $\omega_3$ is symmetric.
- **R13 / 028 §4**: $N_{\rm gh}(\lambda_k)=3k$ comes from per-strand saturation $5$ with $N_{\rm gh}(\sigma_k\text{ strand})=2$; the exchange sign is irrelevant to it. Ordering of the multiplier term: $\omega_k(\sigma_k,\lambda_k)=\omega_k(\lambda_k,\sigma_k)$ ($s^k=1$). 028 (4.1) $\lambda_k^\ddagger=\lambda_k$ (componentwise) unchanged: it uses only equivariance of $\omega_k$. 028's $(-1)^{k(k-1)/2}$ under reversed-order h.c. is the Koszul reversal sign of $k$ odd strands (C3.3), the $\pi=$reversal case of (B2.1); it is consistent with, and unrelated to, the exchange sign. Add to 028 §4.2: the $\mathrm{Sym}^k$-dual part of $\lambda_k$ is the Koszul-antisymmetric part of $\mathcal H_3^{\otimes k}$ (component-symmetric).
- **R26**: no $\omega_k$ in the kinetic blocks $a_k\hat M_k$ (019 l.109–120: $\tilde M_k$, $T_{2k+1}$ symmetric forms on $\mathrm{Sym}^k$). No sign of the tower action depends on $\sigma_k$.

## Regime of validity and self-review

- Holds on homogeneous tensors of any ghost numbers; the support statement uses the sphere saturation 5 of A2 only in the odd-$k$ reduction and in B2. The $s=+1$ conclusion rests on the book relation and on B3.2, both on the level-matched $\ker b_0^-$ space.
- Weakest step: B3's diagnosis of *why* 002 R2.6 is wrong (missing BPZ sign of $c_0^-$) is read off the book's computation block; it is now corroborated mode by mode in (B3.4), which is independent of the book's rearrangement formula. *Correction 2026-09-26:* the conclusion $s=+1$ rests on (B3.1) and (B3.4), two convention-independent routes; (B3.2) is a consistency check of the pair (exchange sign, adjointness sign), not a third independent route.
- Not checked: Grassmann-odd component coefficients of $\lambda_k$ at odd $k$ (toy components commute; 028 §4.3 item 2 unchanged); the consequences of $s=+1$ for 002's step-4 dictionary and R7's suspended-degree statements.

## Status

Complete. B1–B4 entered; `codes/verify-omega-k.py` 89/89 PASS (seed 20260926, log `agent/scratch/omega-k-run1.log`). Fix pass applied 2026-09-26 per `agent/reports/critic-055-20260926T032500.md` (verdict: $s=+1$ confirmed, one [major] wording overclaim on B3.2's independence): added (B3.4) explicit mode computation as the second independent determination of $s$; reworded l.35 (C3.1), l.104, l.109, l.116, l.129 so B3.2 is a consistency check, not a second determination; clarified the R12 carve-out wording (l.9, l.32); added Zwiebach (1993) and Sen (2016) citations; added A6 (order-preserving BPZ product rule) to the candidate convention entries. No script change, no re-run (counts unchanged at 89/89). Next: orchestrator applies the R7/R12/R13 ledger edits and the 002/028 fix pass listed in the critic report.

*Correction 2026-09-30 (node check of 002 step 4′, `agent/reports/critic-002-step4-node-20260930T234000.md`):* $s$ is fixed by the zero-mode sign (ii), $s=-\sigma_0$, not by the order rule (iii); (iii) is the graded anti-involution on creation monomials and not an independent choice. A6, B3.3, B3.4, C3.1 and l. 105 reworded accordingly. The conclusion $s=+1$ and every $\omega_k$ statement are unchanged.
