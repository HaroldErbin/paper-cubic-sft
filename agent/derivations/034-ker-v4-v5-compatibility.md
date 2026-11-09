# Derivation 034 — Is the quotient by ker V₄ compatible with V₅? (plan Task 15, Q1)

**Brief:** `agent/briefs/active-computator-ker-v4-v5-compat-20260919T163000.md`.
**Script:** `codes/verify-ker-v4-v5-compat.py`.

## Status

Status: done — items 1–5, verification (19/19 PASS) and established/open written; critic iteration 1 (3 Serious / 6 Concern / 6 Minor / 2 script gaps) resolved in full, see the resolution table at the end; no working notes outstanding. Critic iteration 2 (2026-09-19): ACCEPT; its three ledger-row corrections and two wording minors applied by the orchestrator. Promoted as R38.

## Task and objective

**Literal task.** The HS field lives in $\Sigma\in\mathcal S/N$, $\mathcal S:=\mathrm{Sym}^2\mathcal H_0$,
$N:=\ker V_4|_{\mathcal S}$ (R13 quotient). From $O(g_s^3)$ the action carries
$\tfrac{g_s^3}{5!}V_5(\Sigma,\Sigma,\Psi)$ (R17). Find the exact condition under which this is
well defined on the quotient and reproduces $S^{(5)}_{\rm eff}$ on-shell; what breaks without it;
remedies; structural origin of a kernel; the all-orders analogue and the ledger rows that depend on it.

**Motivating objective.** Every result from R17 on was verified with generic (kernel-free) $V_4$.
The notes use the quotient prescription. If the condition fails for the real vertices the
whole tower rests on an unverified step. Needed: the condition in a directly testable
finite-basis matrix form (for plan Task 15 Q2), what breaks, which remedy.

## Conventions and setup

- $\mathcal H_0$ finite-dimensional (algebraic layer), $\Psi\in\mathcal H_0$, $P:=\Psi^{\otimes2}\in\mathcal S$.
- $V_4$: symmetric bilinear form on $\mathcal S$ (Gram matrix $V_{4S}$ in an orthonormal Sym² basis,
  R14 housekeeping). $N=\ker V_4|_{\mathcal S}$, $\dim N=:\nu$.
- $V_5$: **totally symmetric** 5-linear form on $\mathcal H_0$ (closed-string vertex, Grassmann-even $\Psi$; the toy uses `sym_tensor`). This is an explicit assumption; the polarisation step of (1.6) needs it. $W_\Psi:=V_5(\cdot,\cdot,\Psi)$: symmetric bilinear form on $\mathcal S$, linear in $\Psi$.
  $v:=W_\Psi P=V_5(\cdot,P,\Psi)$ (covector on $\mathcal S$, cubic in $\Psi$).
- $O(g_s^3)$ action (011 eq. B.1), shared part dropped:
  $$F(\Sigma)=-\tfrac{g^2}{4!}V_4(\Sigma,\Sigma)+\tfrac{2g^2}{4!}V_4(\Sigma,P)+\tfrac{g^3}{5!}W_\Psi(\Sigma,\Sigma),
  \qquad F_{\rm eff}=\tfrac{g^2}{4!}V_4(P,P)+\tfrac{g^3}{5!}W_\Psi(P,P).$$
- Complement: $\mathcal S=C\oplus N$, projectors $\pi_C,\pi_N$ (along the other summand);
  $\Sigma=\sigma+\xi$, $P=P_C+P_N$. Block notation $V_{CC}$, $W_{CC},W_{CN},W_{NN}$.
  $V_{CC}$ is non-degenerate for every complement (if $V_4(c,C)=0$ then $V_4(c,\mathcal S)=0$, so $c\in C\cap N=0$).
- Harold's notation: $V_4(A,B)=\langle A,p_{2,2}B\rangle$, $V_5(A_1..A_5)=\langle A_1\otimes A_2,p_{3,2}(A_3,A_4,A_5)\rangle$;
  $N=\ker p_{2,2}|_{\mathrm{Sym}^2}$, $W_\Psi(A,B)=\langle A,p_{3,2}(B,\Psi)\rangle$.
- **Matching criterion.** "On-shell" means on-shell in $\Sigma$ only: $\Sigma$ is integrated out at its saddle and the result must equal $F_{\rm eff}$ as a functional of $\Psi$ **off-shell in $\Psi$**, order by order in $g$. This is the criterion of R10/R17 (the HS construction is an exact Gaussian identity, not an amplitude statement) and of the notes. The weaker criterion "equal tree amplitudes", which allows a $\Psi$-redefinition, is not used; see §3(d) for what it would change.
- Free constants: none. All normalisations are those of 011 (R17, critic-accepted); nothing is fitted.

## Item list

1. Exact condition (action route + diagram route); necessary / sufficient; weaker variants.
2. Failure mode: complement $C$ (on-shell mismatch, $C$-dependence); full-space dressed kernel.
3. Remedies (a) complement + multiplier for $N$; (b) Route C; (c) $O(g_s^3)$ source/kernel changes; (d) other.
4. Structural candidates for a kernel and whether $V_5$ inherits it.
5. Higher orders: $W_6$, all-orders tower; dependent ledger rows.

## Case list for item 4

(i) ghost number; (ii) momentum / any conserved $U(1)$ or discrete charge; (iii) level matching;
(iv) worldsheet parity / twist; (v) BRST-exactness ($m_2$ $Q$-exact, R6) and $L_\infty$ relations;
(vi) vertex-family (presentation) dependence of $\ker V_4$; (vii) zero-momentum / dilaton sector (flagged only);
(viii) all $\Sigma$-couplings factoring through a common linear map (structural, inherited kernel; R34 scalar toy) — added after critic iteration 1.

## Toy plan

- Basis: $\mathcal H_0=\mathbb R^n$, orthonormal Sym² basis as in `verify-b1-quintic.py`.
- Degenerate $V_4=\sum_{s=1}^r c_s w_s^{\otimes4}$ (totally symmetric, rank $r<D$).
- (i) failure: generic totally symmetric $V_5$; (ii) closure: $V_5$ a random element of the linear
  subspace $\{V_5\in\mathrm{Sym}^5:\ V_5(\Xi,\cdot,\cdot,\cdot)=0\ \forall\Xi\in N\}$.
- Checks: complement theory on-shell mismatch vs. closed form; $C$-dependence; full-space dressed
  kernel mismatch vs. closed form; closure case matches to $O(g^3)$ with $O(g^4)$ residual (log-slope);
  $\ker V_4=0$ limit reproduces R17; remedy (a) closes; each check broken on purpose once.

## 1. The exact condition

### 1.1 Well-definedness on the quotient (action route)

A function on $\mathcal S$ descends to $\mathcal S/N$ iff it is invariant under $\Sigma\to\Sigma+\Xi$, $\Xi\in N$.
The two $V_4$ terms of $F$ are invariant ($V_4(\Xi,\cdot)=0$). The $V_5$ term shifts by

$$
F(\Sigma+\Xi)-F(\Sigma)=\frac{g^3}{5!}\Big[2W_\Psi(\Xi,\Sigma)+W_\Psi(\Xi,\Xi)\Big].
\tag{1.1}
$$

Vanishing for all $\Sigma$ forces the linear term to vanish, $W_\Psi(\Xi,\cdot)=0$, which then kills the quadratic term. Hence

$$
\boxed{\ (\mathrm{C_{full}}):\quad V_5(\Xi,A,\Psi)=0\quad\forall\,\Xi\in N,\ A\in\mathcal S,\ \Psi\in\mathcal H_0\ }
\tag{1.2}
$$

is **necessary and sufficient** for $S_3$ to be a function on $\mathcal S/N$. Equivalent forms:

- $N\subseteq\ker W_\Psi$ for every $\Psi$; since $W_\Psi$ is linear in $\Psi$, it suffices to test $\Psi=e_a$ on a basis of $\mathcal H_0$.
- $\operatorname{range}W_{e_a}\subseteq\operatorname{range}V_4$ for every $a$ (both symmetric, so $\ker=\operatorname{range}^\perp$ in an orthonormal Sym² basis).
- **Testable matrix form** (level-truncated basis $\{\Lambda_I\}$ of $\mathrm{Sym}^2\mathcal H_0$, $\{e_a\}$ of $\mathcal H_0$):
  $$\Pi_N\,V_{5S}[:,:,a]=0\ \ \forall a,\qquad \Pi_N:=1-V_{4S}V_{4S}^{+}\ \text{(orthogonal projector on }\ker V_{4S}),$$
  equivalently $\operatorname{rank}\big[V_{4S}\,\big|\,V_{5S}[:,:,a]\big]=\operatorname{rank}V_{4S}$ for all $a$.
- Harold's notation: $\langle\Xi,p_{3,2}(A,\Psi)\rangle=0$ for all $\Xi\in\ker p_{2,2}$, i.e. $\operatorname{im}\big(p_{3,2}|_{\mathrm{Sym}^2\otimes\mathcal H_0}\big)\subseteq\operatorname{im}p_{2,2}$.

**Deformed shift symmetry.** The quotient at $O(g^2)$ is the statement that $\Sigma\to\Sigma+\Xi$, $\Xi\in N$, is a symmetry of the quadratic action (R11: "kernel shifts"). In SFT an $O(g^2)$ symmetry is generically corrected at the next order, so the right question at $O(g^3)$ is whether some deformation $\Sigma\to\Sigma+\Xi+g\,\eta$ (with $\Psi$ untransformed, as the matching criterion requires) (with $\eta=\eta(\Xi,\Psi)\in\mathcal S$ independent of $\Sigma$) is a symmetry, not whether the undeformed shift is. The $O(g^3)$ variation is

$$
\delta F=-\frac{g^3}{12}V_4(\Sigma-P,\eta)+\frac{g^3}{60}W_\Psi(\Xi,\Sigma)+\frac{g^3}{120}W_\Psi(\Xi,\Xi)+O(g^4).
\tag{1.2$'$}
$$

Vanishing for all $\Sigma$: the $\Sigma$-linear part requires $V_4(\cdot,\eta)=\tfrac15W_\Psi(\Xi,\cdot)$, solvable iff $W_\Psi(\Xi,\cdot)\in\operatorname{range}V_4$, i.e. $W_\Psi(\Xi,N)=0$ (this is (C_NN) of §1.2); the $\Sigma$-independent part then requires $\tfrac1{60}W_\Psi(\Xi,P)+\tfrac1{120}W_\Psi(\Xi,\Xi)=0$ for all $\Psi$, and with (C_NN) this is $W_\Psi(\Xi,P)=0$, i.e. (C_ver). By the collapse (1.6), (C_ver) is (1.2) again. (Allowing $\eta$ to depend on $\Sigma$ changes nothing: at $\Sigma=P$ the condition is $tW_\Psi(\Xi,P)+\tfrac{t^2}2W_\Psi(\Xi,\Xi)=0$ for the rescaled $t\Xi$, giving (C_ver) and $W_\Psi(\Xi,\Xi)=0$; the remaining condition $V_4(\Sigma-P,\eta(\Sigma))=\tfrac15W_\Psi(\Xi,\Sigma-P)$ is solvable for $\Sigma-P\notin N$ and forces (C_NN) for $\Sigma-P\in N$.) So deforming the shift closes no loophole: **(1.2) is the condition for the kernel shift to survive at $O(g^3)$, deformed or not.** By-product: when (1.2) holds, $\eta$ solves $V_4\eta=\tfrac15W_\Psi\Xi$ and the deformed direction $\Xi+g\eta$ satisfies $K_\Psi(\Xi+g\eta)=O(g^2)$ — it is $\ker K_\Psi$ to $O(g)$, which is the §2.2 statement that the dressed kernel is the deformation of $N$.

When (1.2) holds, $V_4$, $W_\Psi$, $K_\Psi$ and $v$ all descend to $\mathcal S/N$, $K_\Psi$ is invertible there for small $g$ (Neumann, 011 §2), and the whole of R17 (exact rewriting B.2, saddle $\tilde X=0$, feedback, gauge law B.3) holds verbatim on the quotient. **Sufficient for matching**; necessity (for matching in every complement) is shown in §1.2, (1.6).

### 1.2 Is (C_full) necessary for matching? Yes, for matching in every complement — the exact $O(g^3)$ condition given a complement, and the collapse of the hierarchy

If (1.2) fails, "the quotient" is not a theory: one must pick representatives, i.e. a complement $C$ and set $\Sigma\in C$. Then $F|_C$ has exactly the R17 form with $(V_4,W_\Psi,P)\to(V_{CC},W_{CC},P_C)$ and $V_{CC}$ invertible, so by R17 (B.2) applied on $C$:

$$
F|_C\big|_{\rm on\text{-}shell}=\frac{g^2}{4!}V_{CC}(P_C,P_C)+\frac{g^3}{5!}W_\Psi(P_C,P_C)+O(g^4),
\qquad V_{CC}(P_C,P_C)=V_4(P,P).
\tag{1.3}
$$

The on-shell mismatch is therefore

$$
\boxed{\ \Delta_C:=S_3|_{C,\rm on\text{-}shell}-S^{(5)}_{\rm eff}
=-\frac{g^3}{5!}\Big[V_5(P,P,\Psi)-V_5(\pi_CP,\pi_CP,\Psi)\Big]+O(g^4)
=-\frac{g^3}{5!}\Big[2W_\Psi(P_C,P_N)+W_\Psi(P_N,P_N)\Big]+O(g^4).\ }
\tag{1.4}
$$

(This is the brief's expected form; the sign is fixed by the orientation $S_3-S_{\rm eff}$.) It is a 5-point term at $O(g^3)$ — a genuine contamination of the 5-point tree amplitude, not a higher-point spill-over. Hence, **for a given complement $C$**, the necessary and sufficient condition for on-shell matching to $O(g^3)$ is

$$
(\mathrm{C}_{\rm ver},C):\qquad 2W_\Psi(\pi_CP,\pi_NP)+W_\Psi(\pi_NP,\pi_NP)=0\quad\forall\Psi .
\tag{1.5}
$$

Hierarchy. Define the intermediate conditions

$$
(\mathrm{C}_{\rm ver}):\ V_5(\Xi,\Psi^{\otimes2},\Psi)=0\ \ \forall\Xi\in N,\ \Psi\in\mathcal H_0,
\qquad
(\mathrm{C}_{NN}):\ V_5(\Xi,\Xi',\Psi)=0\ \ \forall\Xi,\Xi'\in N,\ \Psi\in\mathcal H_0 .
$$

Then

$$
(\mathrm{C_{full}})\ \Longleftrightarrow\ (\mathrm{C}_{\rm ver})\ \Longleftrightarrow\ (\mathrm{C}_{\rm ver},C)\ \forall C\ \Longrightarrow\ (\mathrm{C}_{\rm ver},C)\ \text{for one }C,
\qquad (\mathrm{C}_{\rm ver})\Rightarrow(\mathrm{C}_{NN})\ \text{(so }(\mathrm{C}_{NN})\text{ is redundant)}.
\tag{1.6}
$$

Proofs. (1.2)⇒(C_ver) trivially. **(C_ver)⇒(1.2) by polarisation** (this uses the total symmetry of $V_5$, stated in the setup): for fixed $\Xi\in N$ the map $T_\Xi(\Psi_1,\Psi_2,\Psi_3):=V_5(\Xi,\Psi_1,\Psi_2,\Psi_3)$ is a *symmetric* trilinear form on $\mathcal H_0$ and (C_ver) says its diagonal $T_\Xi(\Psi,\Psi,\Psi)$ vanishes identically; in characteristic $0$ a symmetric multilinear form is determined by its diagonal ($T_\Xi(\Psi_1,\Psi_2,\Psi_3)=\tfrac1{3!}\sum_{S\subseteq\{1,2,3\}}(-1)^{3-|S|}T_\Xi(\Psi_S,\Psi_S,\Psi_S)$, $\Psi_S:=\sum_{i\in S}\Psi_i$), so $T_\Xi\equiv0$. Since $\mathcal S=\mathrm{Sym}^2\mathcal H_0$ is spanned by the symmetrised products $\Psi_1\otimes\Psi_2+\Psi_2\otimes\Psi_1$, $T_\Xi\equiv0$ is $V_5(\Xi,A,\Psi)=0$ for all $A\in\mathcal S$, $\Psi\in\mathcal H_0$, i.e. (1.2). (C_ver)⇒(C_NN): apply the same polarisation with two $\Xi$ slots, or note that (1.2) contains (C_NN). (C_ver)⇒(C_ver,$C$) for every $C$: expand $W_\Psi(P,P)-W_\Psi(P_C,P_C)=2W_\Psi(P_C,P_N)+W_\Psi(P_N,P_N)$ and use $W_\Psi(\Xi,\cdot)=0$. (C_ver,$C$) for *every* $C$ ⇒ (C_ver): as $C$ varies, $\pi_NP$ ranges over all of $N$ whenever $P\notin N$, so (1.5) with $\xi:=\pi_NP$ arbitrary and rescaled $\xi\to t\xi$ gives $W_\Psi(P,\xi)=0$ and $W_\Psi(\xi,\xi)=0$ separately; the first is (C_ver). The only implication that is not reversible is the last one in (1.6): (C_ver,$C$) at one fixed $C$ is a $C$-dependent statement (script check 2) and is not a property of the theory. Script check 8 confirms the equality of the (C_ver) and (C_full) subspaces of $\mathrm{Sym}^5$ in the toy (both of dimension 20) and that the equality fails for non-symmetric $V_5$ (check 8b), which is the falsifier of the polarisation step.

**Verdict for item 1:** (C_full) is the condition for the *quotient prescription* (necessary and sufficient for the action to exist on $\mathcal S/N$) **and** is necessary and sufficient for on-shell matching at $O(g^3)$ in every complement (1.6); see §5 for the whole tower to go through unchanged. Consequently a failure of the matrix test at some truncation is a genuine failure of the quotient prescription at $O(g_s^3)$, not the failure of a merely sufficient condition. The only weaker condition, (C_ver,$C$) at one fixed $C$, buys $O(g^3)$ matching in a $C$-dependent presentation and is not a property of the theory. The recommended testable statement is (1.2) in matrix form.

### 1.3 Diagram route (011 §3 enumeration, degenerate $V_4$)

On $C$ the Feynman rules are those of 011 §3 with propagator $\tfrac{12}{g^2}V_{CC}^{-1}$ and source $\tfrac{g^2}{6}V_4(\cdot,q_{jk})|_C=\tfrac{g^2}{6}V_{CC}(\cdot,\pi_Cq_{jk})$ (the source covector kills $N$, R14 §6 / a4pt check 2). Classes (a), (b) are unchanged: the class-(b) telescoping $V_4V_{CC}^{-1}V_4=V_4$ holds on $C$ (R14 identity, slot-agnostic; the a4pt check-2 statement $V_4\,\mathrm{pinv}(m_2)G_2^{-1}V_4=V_4$ is its orthogonal-complement instance). Class (c): each source–propagator chain telescopes to $2\pi_Cq_{jk}$ instead of $2q_{jk}$, so per assignment

$$
2\cdot\frac{g^3}{5!}V_5(2\pi_Cq_{jk},2\pi_Cq_{lm},\Psi_i)=\frac{g^3}{15}V_5(\pi_Cq_{jk},\pi_Cq_{lm},\Psi_i),
\tag{1.7}
$$

and the 15 assignments sum to $g^3\,\mathrm{Pol}\big[V_5(\pi_CP,\pi_CP,\Psi)\big]$ — the polarisation of the $C$-projected contact term, versus the target $g^3\,\mathrm{Pol}[V_5(P,P,\Psi)]$. The difference is the polarisation of (1.4): the two routes agree (script check 2 compares the 15-assignment sum against the polarised closed form). Under (C_full), $V_5(\pi_C\cdot,\pi_C\cdot,\Psi)=V_5(\cdot,\cdot,\Psi)$ and the R17 count is recovered exactly with coefficient 1. No new diagram appears at $O(g^3)$ on $C$ (the 011 §3 exclusion list is unchanged; kernel directions carry no line at all).

## 2. What happens when (C_full) fails

### 2.1 Complement $C$ (representatives chosen)

Already derived in §1.2: the on-shell mismatch is (1.4), a 5-point $O(g^3)$ contamination, and it **depends on $C$** through $\pi_NP$. Script: check 1 (closed form vs. two-level Richardson extraction of the $g^3$ coefficient, relative agreement $6\times10^{-7}$; residual log-slope $4.007$), check 2 (two random complements give $c_3=-9.1\times10^{-3}$ and $-5.5\times10^{-2}$), check 3 (diagram route reproduces the polarised closed form to $10^{-14}$, differs from the target by $0.27$ at $g=0.3$). Since the $O(g^3)$ physics depends on an arbitrary choice, the complement prescription is not a theory; there is no distinguished $C$ (the orthogonal complement w.r.t. the Sym² Frobenius form is basis-dependent; the BPZ-orthogonal complement $N^{\perp_{\omega_2}}$ is canonical but (1.4) does not vanish for it either unless (1.5) happens to hold — nothing forces it).

### 2.2 Full $\mathrm{Sym}^2$ with the dressed kernel $K_\Psi=V_4-\tfrac g5W_\Psi$

Keep all of $\mathcal S$. The Σ-EOM is $K_\Psi\Sigma=V_4P$. In blocks $(C,N)$ for any complement (the source has no $N$-component, $V_4(N,P)=0$):

$$
\begin{aligned}
(C):&\quad \big(V_{CC}-\tfrac g5W_{CC}\big)\sigma-\tfrac g5W_{CN}\xi=V_{CC}P_C,\\
(N):&\quad W_{NC}\sigma+W_{NN}\xi=0\qquad(\text{the factor }-\tfrac g5\text{ divided out}).
\end{aligned}
\tag{2.1}
$$

The $N$-equation is $g$-independent: it is the constraint $W_\Psi(\Xi,\Sigma)=0$ $\forall\Xi\in N$. If $W_{NN}$ is invertible, $\xi=-W_{NN}^{-1}W_{NC}\sigma=O(g^0)$, i.e. the kernel component of the saddle is **not small** and is not $\pi_NP$. Substituting, $\sigma$ obeys the $C$-equation with the Schur complement $\tilde W:=W_{CC}-W_{CN}W_{NN}^{-1}W_{NC}$ in place of $W_{CC}$, so $\sigma=P_C+\tfrac g5V_{CC}^{-1}\tilde WP_C+O(g^2)$ and, using $F_*=\tfrac12 b^\top\Sigma_*$ for the quadratic form,

$$
F_*=\frac{g^2}{4!}V_4(P,P)+\frac{g^3}{5!}\tilde W(P_C,P_C)+O(g^4).
\tag{2.2}
$$

With $W(P,P)=W_{CC}(P_C,P_C)+2W_{CN}(P_C,P_N)+W_{NN}(P_N,P_N)$ the mismatch assembles into a perfect square:

$$
\boxed{\ \Delta_{\rm full}=-\frac{g^3}{5!}\,v_N^{\top}W_{NN}^{-1}v_N+O(g^4),\qquad v_N:=V_5(\cdot,P,\Psi)\big|_N .\ }
\tag{2.3}
$$

The same follows from the R17 identity (B.2), valid on the full space whenever $K_\Psi$ is invertible: the "feedback" $\tfrac{g^4}{600}vK_\Psi^{-1}v$ is no longer $O(g^4)$ because $(K_\Psi^{-1})_{NN}=-\tfrac5gW_{NN}^{-1}+O(1)$. Script check 4: closed form vs. numerics (residual log-slope $4.003$), and $\sigma_{\min}(K_\Psi)\propto g$ (log-slope $0.998$).

Properties of (2.3):

- **Independent of $C$** ($v_N$ and $W_{NN}$ are restrictions to $N$), unlike (1.4). It vanishes **if** $v_N=0$, i.e. under (C_ver) $=$ (C_full) by (1.6). The converse at a given $\Psi$ does not follow ($W_{NN}$ is symmetric but indefinite, being odd in $\Psi$, so $v_N^\top W_{NN}^{-1}v_N=0$ does not force $v_N=0$); as an identity in $\Psi$ the converse holds for $\nu=1$ ($v_N^2/W_{NN}\equiv0$ forces the polynomial $v_N\equiv0$) and is not shown for $\nu\ge2$.
- **Degree 5 in $\Psi$**, homogeneous ($v_N$ cubic twice, $W_{NN}^{-1}$ degree $-1$: $3+3-1=5$; script check 9), so (2.3) is $g^3\times$(degree 5) and *consistent* with the $g^{n-2}$ power counting of a 5-point term. What is pathological is that it is **rational, not polynomial** in $\Psi$: the $N$-block $W_{NN}\propto\Psi$ has no $\Psi$-independent part, so $W_{NN}^{-1}$ is not a Feynman propagator and the diagrammatic reading of §1.3 does not apply to the kernel directions (an $N$-line between two $V_5$ vertices carries $\tfrac{12}{g^2}\cdot(-\tfrac5g)W_{NN}^{-1}=O(g^{-3})$ and degree $-1$ in $\Psi$; the chain [src–$C$prop–$V_5$–$N$prop–$V_5$–$C$prop–src] has order $g^{2-2+3-3+3-2+2}=g^3$ and degree $2+2+1+1-1=5$). Higher orders bring rational terms of every degree.
- **Perturbation theory does not survive**: $W_{NN}\propto\Psi$, so at $\Psi=0$ the $N$-block of the quadratic form vanishes — there is no free propagator for the kernel modes, the expansion around the vacuum does not exist, and the "small-$g$" saddle above is only a formal statement at fixed $\Psi\neq0$ with $W_{NN}$ invertible.
- **Singular $W_{NN}$.** The Lagrange-multiplier picture ((2.1)(N) is a constraint on $\sigma$, $W_{NC}\sigma\in\operatorname{range}W_{NN}$, which $\sigma=P_C$ violates generically) is right, but a saddle still exists, with the kernel component blowing up as $1/g$. Extreme case $W_{NN}=0$: with $\xi=\xi_{-1}/g+O(1)$, (2.1)(C) at $O(g^0)$ gives $\sigma=P_C+\tfrac15V_{CC}^{-1}W_{CN}\xi_{-1}$, and (2.1)(N) $W_{NC}\sigma=0$ gives $\xi_{-1}=-5\,(W_{NC}V_{CC}^{-1}W_{CN})^{-1}W_{NC}P_C$, which exists whenever the $\nu\times\nu$ matrix $W_{NC}V_{CC}^{-1}W_{CN}$ is invertible (generic for $\nu\le\dim C$). Then $F_*=\tfrac12b^\top\Sigma_*=\tfrac{g^2}{24}V_{CC}(P_C,\sigma)$ (the source has no $N$-component) and

  $$
  \Delta_{\rm full}\big|_{W_{NN}=0}=-\frac{g^2}{24}\,(W_{NC}P_C)^\top\big(W_{NC}V_{CC}^{-1}W_{CN}\big)^{-1}(W_{NC}P_C)+O(g^3),
  \tag{2.4}
  $$

  an $O(g^2)$ mismatch — the 4-point tree is contaminated, one order worse than (2.3). (Script check 4c: $V_5$ chosen in the subspace $V_5(N,N,\Psi_0)=0$; (2.4) reproduced, residual $O(g^3)$.) For $W_{NN}$ singular but non-zero the same mechanism acts on $\ker W_{NN}$.

**Verdict item 2:** complement ⇒ $C$-dependent 5-point contamination (1.4); full space with dressed kernel ⇒ $C$-independent but non-perturbative, rational degree-5 contamination (2.3) at $O(g^3)$, no vacuum propagator, and an $O(g^2)$ contamination (2.4) when $W_{NN}$ is singular. Neither is acceptable.

## 3. Remedies when (C_full) fails

### (a) Complement + multiplier for the kernel directions — **works at $O(g^3)$** (toy-verified)

Keep $\Sigma=\sigma+\xi$ on the full $\mathcal S$ ($\sigma\in C$, $\xi\in N$) and add a multiplier $\lambda\in N^*$ enforcing the Veronese value of the kernel component:

$$
S_3^{(a)}=S_3\big|_{\Sigma=\sigma+\xi}+g^2\big\langle\lambda,\ \xi-\pi_N\Psi^{\otimes2}\big\rangle .
\tag{3.1}
$$

Every term has $\le3$ fields ($\langle\lambda,\xi\rangle$ quadratic, $\langle\lambda,\pi_N\Psi^{\otimes2}\rangle$ cubic): the action stays cubic. The $\lambda$-EOM gives $\xi=\pi_NP$ algebraically; the $\xi$-EOM fixes $\lambda$ (it appears in no other equation); the $\sigma$-EOM is the $C$-theory with the shifted source $V_{CC}(\cdot,P_C)+\tfrac g5W_{CN}(\cdot,P_N)$, so $\sigma_*=P_C+O(g)$ and $\Sigma_*=P+O(g)$ **exactly as in the kernel-free case**. On-shell,

$$
F^{(a)}_*=\frac{g^2}{4!}V_4(P,P)+\frac{g^3}{5!}W_\Psi(P,P)+O(g^4):
$$

the $O(g^3)$ term is the full $V_5(P,P,\Psi)$ because $\xi$ supplies the missing $P_N$. Script check 7: mismatch log-slope $4.007$ in the failure case; check 7b: dropping the multiplier restores (1.4). This is Route C (R13) applied to the kernel directions only, with HS on the rest — a hybrid: the $(\xi,\lambda)$ pair is a cotangent pairing, ultralocal, no inversion.

Limits of what is established: (i) the $O(g^4)$ feedback of (3.1) is $\tfrac{g^4}{600}v_C^{\top}(V_{CC}-\tfrac g5W_{CC})^{-1}v_C$ with $v_C=V_5(\cdot,P,\Psi)|_C$ and this **is $C$-dependent** when $v_N\neq0$ (check 7 detail: $O(g^4)$ coefficients $0.57$ vs $2.36$ for two complements). By R26 (the diagonal recursion is always solvable) the $O(g^4)$ dressing $W_6$ then absorbs it with a $C$-dependent $\mathcal C$-composite built from $V_{CC}^{-1}$ — presentation freedom in R19/R26's sense, physics $C$-independent order by order; **expected, not verified here**. (ii) $N_{\rm gh}(\lambda)$, reality, and the BV pairing of $(\xi,\lambda)$ are the R13/R34/R35 questions restricted to $N$: $N_{\rm gh}(\lambda)=6$ (R34: $N_{\rm gh}(\lambda_k)=3k$, saturation $N_{\rm gh}(\lambda)+N_{\rm gh}(\xi)=10$ with $N_{\rm gh}(\xi)=4$), reality $\lambda^\ddagger=\lambda$ by R35. (iii) Infinite-dimensional: needs $N$ closed and complemented (the standing R13 regularity item).

### (b) Route C throughout — **works** (R13), but is a different presentation

$S_C$ inverts nothing and imposes $\sigma_2=\Psi^{\otimes2}$ by a multiplier, so $\ker V_4$ never enters. The price is the standing R13 open items (BV structure, CMZ obstruction). If the HS Gaussian form is wanted (auxiliary field integrated out, $V_4^{-1}$ propagator), (b) is not that theory; (a) is the minimal hybrid that keeps HS on $\mathcal S/N$-worth of directions.

### (c) Modify the source or the quadratic term — **reduces to (a) or fails**

Did R17's uniqueness assume $\ker V_4=0$? Partly. The exclusions in 011 §1 are power-counting statements (an $O(g^3)$ tadpole or kernel correction contaminates a 3- or 4-point tree at $O(g^3)$) and hold regardless of the kernel. But the argument that *nothing else is needed* used the exact rewriting with $K_\Psi^{-1}$, i.e. $V_4$ invertible (011 §2 "invertibility scope"). With a kernel, an $O(g^2)$ modification is admissible if it is invisible on-shell: replace $V_4\to V_4+\kappa$ in both kinetic and source terms (so the saddle stays $\Sigma=P$) with $\kappa$ supported on $N$ (through some projector) and **Veronese-null**, $\kappa(\pi_NP,\pi_NP)=0$ $\forall\Psi$; then the on-shell value is unchanged at $O(g^2)$ and the $O(g^3)$ term becomes the full $W_\Psi(P,P)$. Requirements: $\kappa|_N$ non-degenerate (to give $N$ a propagator) and the image of $\Psi\mapsto\pi_N\Psi^{\otimes2}$ inside its null cone. A definite $\kappa$ cannot do this ($\pi_NP$ spans $N$ as $\Psi$ varies, since the Veronese cone spans $\mathcal S$); an indefinite one can only if the quadratic image lies on its null quadric. The one systematic solution is the split $N=N_1\oplus N_2$ with $\kappa$ an off-diagonal pairing $N_1\times N_2$ and the source valued in $N_1$ only — which is exactly the multiplier pair of (a) with $\xi\in N_1$, $\lambda\in N_2$. Other Veronese-null non-degenerate $\kappa$: not excluded, none found; **open**, and not needed. An $O(g^3)$ kernel modification on $N$ does not help: the $N$-propagator stays $O(g^{-3})$ (same disease as §2.2).

### (d) Other

- **Quotient by the joint kernel.** The directions that decouple from *everything* are $N_\infty:=\{\Xi\in N:\ T_n(\Xi,\dots)=0\ \text{for every }\Sigma\text{-coupling }T_n\}$ ($V_5(\Xi,\cdot,\Psi)$, $W_6(\Xi,\cdot,\cdot)$, …). The quotient by $N_\infty$ is always well defined at all orders (it is the R13 argument applied to the whole action). Only $N/N_\infty$ needs (a). Cleanest general statement: **quotient by $N_\infty$, multipliers on $N/N_\infty$**; (C_full) at all orders is the statement $N_\infty=N$.
- **Change the vertex family.** $\ker V_4$ is a property of the chosen $\mathcal V_4$ (region + $\mathcal V_3$ stubs), not of the theory; a different family (SL(2,C), minimal area, hyperbolic, or a stub deformation) generically has trivial kernel because degeneracy is codimension one in the space of symmetric forms. If a kernel is found numerically at some truncation for one family, the first thing to try is a stub-length or family change — cheaper than any of (a)–(c). Whether (C_full) holds for a given family is then a property of that family: it holds automatically when all $\Sigma$-couplings factor through a common map (§4 (viii)), and there is otherwise no symmetry that would force $V_5$ to annihilate $\ker V_4$ (§4 (i)–(vii)).
- **Weaken the criterion to amplitude matching** (not adopted). A $\Psi$-redefinition $\Psi\to\Psi+g^3\epsilon(\Psi)$ adds $2g^3\langle Q\Psi,\epsilon\rangle$ to the quartic-truncated action and could absorb $\Delta_C$ if $V_5(\Xi,P,\Psi)$ lay in the ideal generated by the $\Psi$ equations of motion — a BRST-type condition involving $Q$ and $V_3$, not a property of $(V_4,V_5)$ alone, and one that would only hold at the level of on-shell amplitudes. It is ruled out here because the project's criterion is off-shell equality in $\Psi$ (setup); the HS action is meant to be an exact rewriting of the quartic-truncated action, not an amplitude-equivalent theory. Recorded as open item (vi) for completeness.
- **Restrict to $\ker V_4=0$** (plan Task 15 Q2) and state it as an assumption of the paper, with the level-truncated Gram-matrix test as evidence.

**Recommendation:** test $\ker V_4=0$ first (Task 15 Q2). If a kernel is found: test (1.2) in matrix form; if (1.2) holds, the quotient prescription stands as is; if it fails, adopt (a) (multiplier on $N/N_\infty$) — it keeps the action cubic, the HS structure on the complement, and the saddle $\Sigma_*=P+O(g)$.

## 4. Structural angle: can $\ker V_4$ come from a selection rule that $V_5$ inherits?

General remark first. A selection rule is a grading of $\mathcal H_0$ by a group $G$ (charge $q$) under which every $V_n$ is invariant. It makes $V_4$ block-off-diagonal, pairing the Sym² sector of charge $q$ with the sector of charge $\bar q$; $V_5(\cdot,\cdot,\Psi)$ pairs $q$ with $\bar q\bar q_\Psi$. A selection rule produces a *kernel* only if some sector $\mathcal S_q$ has no partner $\mathcal S_{\bar q}$, or if the block $V_4|_{\mathcal S_q\times\mathcal S_{\bar q}}$ is itself degenerate. In the first case the same rule kills $V_5(\Xi,A,\Psi)$ only if there is also no $A\otimes\Psi$ of the conjugate charge — a separate counting condition. In the second case the rule says nothing about $V_5$. So **no selection rule forces (C_full)**; at best it makes (1.2) a block-wise statement. A selection rule is not the only structural mechanism, however: a kernel is forced *and inherited* whenever the $\Sigma$-couplings factor through a common map, case (viii) below. Candidate by candidate:

- **(i) Ghost number.** $\Sigma$ is taken at $N_{\rm gh}=4$ by definition, so within $\mathcal S$ ghost number is not a grading but a fixed value; $V_4(\Sigma,\Sigma)$ saturates $8$, $V_5(\Sigma,\Sigma,\Psi)$ saturates $10$ (R17). No kernel arises. (If one allowed all ghost numbers, the off-saturation directions would lie in $\ker V_4$ *and* in $\ker V_5(\cdot,\cdot,\Psi)$ for $N_{\rm gh}(\Psi)=2$ — inherited by saturation — but they are not in the field space.) Verdict: not a source; inherited trivially if it were.
- **(ii) Momentum, and any conserved $U(1)$ or discrete charge (KK, winding, $\mathbb Z_2$ orbifold charges).** Sector $k$ pairs with $-k$; BPZ non-degeneracy of $\omega_1$ already forces $\dim\mathcal H_{0,k}=\dim\mathcal H_{0,-k}$ level by level, hence equal dimensions of the Sym² sectors. No sector is unpaired, so no forced kernel; a kernel inside a block is not constrained by the charge. Verdict: not a source; (1.2) reduces to the block statement $\Pi_{N_k}V_5(\cdot,\cdot,e_a)|_{\mathcal S_{k'}}=0$ for $k+k'+k_a=0$.
- **(iii) Level matching / $b_0^-$.** Already imposed strand by strand in $\mathcal H_0$; $\mathcal S=\mathrm{Sym}^2\mathcal H_0$ carries no further constraint, and $V_4$ on $\mathcal S$ is the restriction of the full vertex. No mechanism for a kernel identified. Verdict: not a source.
- **(iv) Worldsheet parity $\Omega$ (twist).** If the vertex family is $\Omega$-symmetric, $V_n$ are $\Omega$-even and $\Omega$ is a $\mathbb Z_2$ grading of $\mathcal H_0$; (ii) applies with $\bar q=q$. Verdict: not a source. (A non-$\Omega$-symmetric family has no rule at all.)
- **(v) BRST / $L_\infty$ relations.** R6's $Q$-exactness of $m_2$ was **withdrawn** (R31: the augmented $(2,2,0)$ equation fails by $\tfrac12M_{2,2}$; the equation that holds is the non-augmented $B_{2,2}=0$), so there is no "$m_2=[Q,h]$" structure to inherit. What the cyclic $L_\infty$ relations do say: $V_4(Q\Lambda,A,B,C)+\dots=\pm V_3(V_3(\cdot,\cdot),\cdot,\cdot)$-terms, i.e. $V_4$ on $Q$-exact inputs is fixed by $V_3\circ V_3$, not zero; the next relation fixes $V_5$ on $Q$-exact inputs by $V_3\circ V_4$ and $V_4\circ V_3$ terms. Neither produces a kernel of $V_4$ on $\mathcal S$ (off-shell, $Q$ not set to zero) nor relates $\ker V_4$ to $V_5$. On $Q$-cohomology (on-shell external states) the $L_\infty$ relations do relate the two, but R9 fixed $\ker m_2$ off-shell. Verdict: not a source; no inheritance.
- **(vi) Vertex-family dependence.** $V_4$ depends on the choice of $\mathcal V_4$ (region in $\mathcal M_{0,4}$ + $\mathcal V_3$ stubs); $V_5$ on the corresponding $\mathcal V_5$. The geometric consistency conditions ($\partial\mathcal V_5=\mathcal V_4\times\mathcal V_3$ plumbing regions) constrain $V_5$ on the boundary of moduli space, not its values as a bilinear form on $\mathcal S$. A kernel of $V_4$ is a codimension-one accident of the family and is generically removed by a stub deformation or a change of family. Verdict: absent the factorisation mechanism of (viii), a kernel is an accidental degeneracy at a given family/truncation and nothing in the moduli-space consistency conditions ties $V_5$ to it; for such an accidental kernel the generic expectation is that (1.2) fails. (In the toy this is what happens: for the rank-8 $V_4$, generic $V_5$ violates (1.2); the closure subspace has dimension 20 in the 56-dimensional $\mathrm{Sym}^5$, codimension 36.)
- **(vii) Zero-momentum / ghost-dilaton sector** (flag only). Dilaton insertions in $V_n$ are governed by the ghost-dilaton theorem (derivatives of $V_{n-1}$ w.r.t. $g_s$ plus contact terms; companion SL(2,C) project), which produces relations, not zeros. Whether the zero-momentum block of $V_4$ on Sym² can be degenerate through such relations is not investigated here; it is the natural first place to look in the numerical test (Task 15 Q2). Verdict: open, out of scope.
- **(viii) All $\Sigma$-couplings factor through a common linear map** (structural; the mechanism behind the R34 scalar example). Suppose there is a linear $\rho:\mathcal S\to\mathcal S'$ with $V_4=V_4'\circ(\rho\otimes\rho)$ and $V_5(\cdot,\cdot,\Psi)=V_{5,\Psi}'\circ(\rho\otimes\rho)$ for some forms $V_4'$, $V_{5,\Psi}'$ on $\mathcal S'$. Then $\ker\rho\subseteq\ker V_4$ and $\ker\rho\subseteq\ker V_5(\cdot,A,\Psi)$ for all $A,\Psi$; if moreover $V_4'$ is non-degenerate on $\operatorname{im}\rho$, $N=\ker\rho$ exactly and (1.2) holds by construction — the kernel is large, forced, and inherited by every coupling that factors through $\rho$ (so $N_\infty=N$ in the sense of §3(d) and the quotient prescription is exact at all orders). R34's scalar $\phi^3+\phi^4$ toy is this case: contact vertices depend on the bilocal $\Sigma(x,y)$ only through its diagonal, $V_4(\Sigma,\Sigma')=\lambda_4\int dx\,\Sigma(x,x)\Sigma'(x,x)$ and $V_5(\Sigma,\Sigma',\psi)=\lambda_5\int dx\,\Sigma(x,x)\Sigma'(x,x)\psi(x)$, so $\rho:\Sigma\mapsto\Sigma(x,x)$, $\ker\rho=\{\Sigma:\Sigma(x,x)=0\}$ is the "large kernel" of the ledger row, $V_5$ inherits it, and $\mathcal S/\ker\rho$ is the space of local HS fields — the collapse recorded in R34. The mechanism is not tied to locality: any factorisation of the two $\Sigma$ legs of every vertex through one intermediate space does it. For string vertices $\rho$ would have to be a map that the $\mathcal V_4$- and $\mathcal V_5$-region surface states share on the two $\Sigma$ legs (e.g. a common $\mathcal V_3$-stub / propagator-strip structure on the pair of legs); none is known, and the moduli-space consistency conditions do not supply one (case (vi)). **Finite-basis test that distinguishes (viii) from an accidental kernel:** compute $N=\ker V_{4S}$ and $N_5:=\bigcap_a\ker V_{5S}[:,:,a]$ directly and compare. Since each $V_{5S}[:,:,a]$ is symmetric, $\Pi_NV_{5S}[:,:,a]=0\ \forall a$ is the inclusion $N\subseteq N_5$, i.e. (1.2); the structural case (viii) with non-degenerate $V_4'$ is $N=N_5$ (and $N=N_6$ for the $V_6$ slots, etc.), the accidental case is $N\not\subseteq N_5$, and $N\subsetneq N_5$ would signal a common map through which $V_5$ factors more than $V_4$. Verdict: **the one mechanism that forces a kernel and makes (1.2) hold automatically**; whether it operates for the real vertices is exactly the Task 15 Q2 test, in the form $N\subseteq N_5$.

**Verdict item 4:** no symmetry or selection rule of the closed string forces a kernel of $V_4$ on $\mathrm{Sym}^2\mathcal H_0$ (cases (i)–(vii)), and if the kernel is accidental nothing forces $V_5$ to annihilate it, so (1.2) is then expected to fail. The structural exception is case (viii): if all $\Sigma$-couplings factor through a common map, the kernel is forced, generically large, and inherited, and (1.2) holds by construction (R34 scalar toy). (1.2) is an independent, testable property of the vertex family; the finite-basis test $N\subseteq N_5$ decides between the two scenarios.

## 5. Higher orders and dependent ledger rows

### 5.1 The $O(g_s^4)$ vertex $W_6=V_6-\tfrac65\mathcal C$ (R19)

The action on $\mathcal S/N$ at this order needs two things:

1. $\tfrac{g^4}{6!}W_6(\Sigma^3)$ must descend: $W_6(\Xi,A,B)=0$ for $\Xi\in N$, all $A,B\in\mathcal S$. Since $\mathcal C(A,B,Z)=\sum_{\rm strands}\langle V_5(\cdot,A,z^{(1)}),V_4^{-1}V_5(\cdot,B,z^{(2)})\rangle$, the composite $\mathcal C$ is even *defined* on the quotient only if $V_5(\cdot,A,z)$ is a covector on $\mathcal S/N$ for every strand $z\in\mathcal H_0$ — which is exactly (1.2) with $\Psi\to z$. Given (1.2), $\mathcal C(\Xi,B,Z)=\sum\langle V_5(\cdot,\Xi,z^{(1)}),\dots\rangle=0$ automatically (the $\Xi$ sits in a $V_5$ slot). So the new condition is on the geometric part only:
   $$(\mathrm C^{(6)}):\qquad V_6(\Xi,A,B)=0\quad\forall\Xi\in N,\ A,B\in\mathcal S\qquad(\text{matrix form: }\Pi_NV_{6S}[:,:,:]=0\text{ in the first index}).$$
2. $K_6=K_\Psi-\tfrac{g^2}{10}T(\cdot,\cdot,P)$ invertible on the quotient: automatic (Neumann) once $V_4$ is invertible there and everything descends.

### 5.2 All orders (R25/R26 scheme B)

R26's Jacobi form has diagonal blocks $\hat M_k=\tilde M_k-\tfrac{g}{2k+1}T_{2k+1}(\cdot,\cdot,\Psi)$ on $\mathrm{Sym}^k$-type spaces and off-diagonal source maps $L_k(\Psi)$. The tower is well defined on $\bigoplus_k\mathcal S_k/N_k$, $N_k:=\ker\tilde M_k$, iff **every block entry vanishes on $N_k$ in its $\Sigma_k$ slots**:

$$
(\mathrm C_\infty):\qquad T_{2k+1}(N_k,\cdot,\Psi)=0,\qquad L_k(\Psi)\big|_{N_k}=0,\qquad L_{k}(\Psi)^\top\big|_{N_{k-1}}=0,\qquad\text{and every forced diagonal }T_n\text{ vanishes on each }N_k\text{ in its }\Sigma_k\text{ slots.}
$$

For $k=2$: $\tilde M_2=V_4$, $T_5=V_5$, giving (1.2); $T_6\to$ (C^{(6)}); etc. For $k\ge3$ the kinetic kernels $\tilde M_k$ ($=V_6|_{(3,3)}$ for $k=3$, R20/R25) bring their **own** (5.1)-type non-degeneracy question, one per level, and their own compatibility conditions with the couplings that follow. Because the dressed diagonals $T_n$ are built (R26 §4) by polarising the previous tower's mismatch, which contains $V_{2k}^{-1}$-composites, the descent conditions propagate: (C_∞) at level $k$ is needed for the level-$(k+1)$ dressings to be defined. The general escape is §3(d): quotient by the joint kernel $N_{k,\infty}$ of all $\Sigma_k$-couplings and multipliers (remedy (a)) on $N_k/N_{k,\infty}$ — R26's Gaussian/Schur structure is unaffected by cotangent pairs (they are exact Gaussians with no inverse), so the theorem is **expected** to go through in that hybrid form; not verified.

Where the kernel condition first enters each affected ledger row (one line each; "assumes" = uses $V_4^{-1}$ or the quotient without (1.2)):

| row      | dependence                                                                                                                                                                                                                                                                                 |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| R9       | states the quotient; no $V_5$ — unaffected.                                                                                                                                                                                                                                                |
| R10      | $O(g^2)$ integrating-out with $V_4^{-1}$ on the quotient/complement — unaffected (source $\perp N$, R14 §6, a4pt check 2).                                                                                                                                                                 |
| R11      | residual gauge freedom "kernel shifts $\delta\Sigma\in\ker V_4$": a symmetry at $O(g^2)$; survives at $O(g^3)$, deformed or not, iff (1.2) (§1.1, (1.2$'$)).                                                                                                                               |
| R13      | kernel-decoupling defusal at $O(g^2)$ — correct as stated but **does not extend to $O(g^3)$** without (1.2); the annotation on (5.1) should say so. Route C itself unaffected.                                                                                                             |
| R14      | telescoping with $V_4^{-1}$ at $O(g^2)$ — unaffected (pinv telescoping holds).                                                                                                                                                                                                             |
| R15      | Schwinger form of $V_4^{-1}$ — needs $V_4$ invertible on the quotient only (unaffected), but any use of it inside $V_5$-composites assumes (1.2).                                                                                                                                          |
| R17      | $K_\Psi^{-1}$, $\tilde X$, feedback: **assumes (1.2)** (011 §2 "invertibility scope" assumed $V_4$ invertible on the space where $V_5$ acts).                                                                                                                                              |
| R18      | gauge tower on the quotient: assumes (1.2) at $O(g^3)$ and beyond.                                                                                                                                                                                                                         |
| R19      | $\mathcal C$, $K_6^{-1}$: assumes (1.2) and (C^{(6)}).                                                                                                                                                                                                                                     |
| R20      | $\Sigma_2\oplus\Sigma_3$ presentation with $V_4^{-1}$: assumes (1.2); adds $\ker\tilde M_3$.                                                                                                                                                                                               |
| R21      | $N=\Phi^\top V_4^{-1}\Phi$, dressed action: assumes (1.2), (C^{(6)}).                                                                                                                                                                                                                      |
| R22      | BV class of the $\tilde X$-law uses $K_\Psi$ non-degenerate (contractible pair): assumes (1.2).                                                                                                                                                                                            |
| R24      | $\chi$-partner built on $K_\Psi^{-1}$: assumes (1.2).                                                                                                                                                                                                                                      |
| R25      | $\hat K^{-1},\tilde M^{-1},\hat M^{-1}$: assumes (C_∞) through $k=3$.                                                                                                                                                                                                                      |
| R26      | nested $\hat H_k^{-1}$: assumes (C_∞) at all levels (the theorem is stated for invertible $\tilde M_k$; with kernels it holds on the quotient iff (C_∞), or in the hybrid form of §3(d), expected).                                                                                        |
| R28      | $m_2^{-1}$ no local kernel: about $V_4^{-1}$ on its range only — unaffected.                                                                                                                                                                                                               |
| R29      | 4-point chain, degenerate case tested (check 2) — unaffected.                                                                                                                                                                                                                              |
| R30, R33 | geometry after a change of kinetic term, $K^{-1}$: assumes (1.2) wherever $V_5$-dressed kernels are inverted.                                                                                                                                                                              |
| R34      | item (2): "equations equivalent order by order … modulo $\ker V_4$" and "$O(g_s^3)$ completion = R17, mismatch exactly $O(g_s^4)$" presuppose that $V_5$ respects the quotient: **assumes (1.2)**. Its scalar example is the structural case §4 (viii), where (1.2) holds by construction. |
| R35      | reality of the tower uses $\hat M_k$, not their inverses — unaffected.                                                                                                                                                                                                                     |
| R36      | $L_\infty$-morphism test of the comparison map at quartic truncation (no $V_5$, $\Sigma$ has no $Q$-kinetic term) — examined, unaffected.                                                                                                                                                  |
| R37      | single-strand $\mathcal V_3'$ route: geometry of the three-vertex, no $V_4^{-1}$ and no quotient — examined, unaffected.                                                                                                                                                                   |

Rows not listed (R1–R8, R12, R16, R23, R27, R31, R32) were scanned for $V_4^{-1}$, $K_\Psi$, $\ker V_4$ and the quotient: none uses them (R27's "quotient" is the $\mathbb Z_2$-orbifold worldsheet, unrelated).

**Verdict item 5:** the all-orders condition is (C_∞), whose $k=2$ instances are (1.2) and (C^{(6)}); every row from R17 on that inverts a $V_5$-dressed kernel assumes (1.2). One ledger row (proposed, corrected after critic iteration 1): "**(5.1′)** the $\ker V_4$ quotient is compatible with the $O(g_s^3)$ coupling iff $V_5(\ker V_4,\mathrm{Sym}^2\mathcal H_0,\mathcal H_0)=0$ (matrix test $\Pi_NV_{5S}[:,:,a]=0$, $\Pi_N=1-V_{4S}V_{4S}^+$, equivalently $\ker V_{4S}\subseteq\bigcap_a\ker V_{5S}[:,:,a]$); for totally symmetric $V_5$ this is also necessary and sufficient for $O(g_s^3)$ matching (off-shell in $\Psi$) in every complement (polarisation), and for the kernel shift to survive at $O(g_s^3)$ deformed or not; without it the $O(g_s^3)$ 5-point tree is contaminated by $-\tfrac{g_s^3}{5!}[V_5(P,P,\Psi)-V_5(\pi_CP,\pi_CP,\Psi)]$, complement-dependent, and keeping the kernel modes with the dressed kernel gives a rational degree-5 term $-\tfrac{g_s^3}{5!}v_N^\top W_{NN}^{-1}v_N$ with an $O(g_s^{-3})$ kernel propagator and no vacuum propagator ($O(g_s^2)$ contamination if $W_{NN}$ is singular); holds automatically when all $\Sigma$-couplings factor through a common linear map $\rho$ with $V_4$ non-degenerate on $\operatorname{im}\rho$ (contact vertices, R34 scalar toy, $\rho:\Sigma\mapsto\Sigma(x,x)$); remedy: multiplier pair on $\ker V_4$ (hybrid Route C), cubic, closes at $O(g_s^3)$; $\ker V_4=0$ reproduces R17; R17–R22, R24–R26, R30, R33 and R34(2) assume the condition or $\ker V_4=0$ (R15 only where $V_4^{-1}$ enters $V_5$-composites)." — Condition, mismatches (1.4)/(2.3)/(2.4), remedy and limit: proven (finite-dimensional algebraic layer) + verified (numpy toy, rank-8/10 $V_4$, 19/19 PASS, break-on-purpose per check); deformed-shift closure, structural case and dependence table: argued, not machine-checked. `agent/derivations/034-ker-v4-v5-compatibility.md`, `codes/verify-ker-v4-v5-compat.py`. (Row text as corrected by critic iteration 2.)

## Verification

Script `codes/verify-ker-v4-v5-compat.py` (seed 20260919; `.venv/bin/python`, **19/19 PASS** after the critic-1 fix pass: 13 original + 4c/4d, 8/8b, 9/9b; the summary line prints the count). Toy: $n=4$, $\dim\mathrm{Sym}^2=10$, $V_4=\sum_{s=1}^8c_sw_s^{\otimes4}$ (rank 8, $\nu=2$), generic totally symmetric $V_5$ (failure) and a random element of the 20-dimensional closure subspace (built as the nullspace of $V_5\mapsto(\Xi_k^{ab}V_{5,abcde})_k$ in the 56-dimensional $\mathrm{Sym}^5$). On-shell values are exact linear solves (the action is quadratic in $\Sigma$); $g^3$ coefficients extracted by two-level Richardson at $g=10^{-3}$; residual orders by log-slopes between $g=10^{-3}$ and $5\times10^{-4}$ (smaller $g$ than 011 because $c_4/c_3\sim60$ here).

| check | claim                                      | method                                                                                                                                                                                                                                          | broken on purpose                                                                                                 |
| ----- | ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| 1     | (1.4)                                      | Richardson $c_3$ vs closed form, rel. $6\times10^{-7}$; residual slope 4.007                                                                                                                                                                    | 1b: dropping the $\pi_C$ term leaves slope 2.96 (i.e. $O(g^3)$)                                                   |
| 2     | $C$-dependence of (1.4)                    | two random complements, $c_3=-9.1\times10^{-3}$ vs $-5.5\times10^{-2}$                                                                                                                                                                          | — (a difference cannot be "broken"; it is the falsifier of $C$-independence)                                      |
| 3     | (1.7)                                      | 15 assignments with $V_{CC}^{-1}$ vs independent inclusion–exclusion polarisation of $V_5(\pi_CP,\pi_CP,\Psi)$, $10^{-14}$; differs from $g^3V_5(\psi_1..\psi_5)$ by 0.27                                                                       | 3b: Wick factor 1 fails                                                                                           |
| 4     | (2.3) and $\sigma_{\min}(K_\Psi)\propto g$ | residual slope 4.003; slope 0.998                                                                                                                                                                                                               | 4b: sign flip leaves $O(g^3)$                                                                                     |
| 4c    | (2.4), singular $W_{NN}$                   | $V_5$ in the subspace $V_5(N,N,\Psi_0)=0$ (nullspace of 3 constraints on $\mathrm{Sym}^5$); residual slope 3.000; $\|\xi_*\|$ slope $-1.005$; $c_2$ equal for two complements to $10^{-10}$                                                     | 4d: sign flip leaves $O(g^2)$                                                                                     |
| 5     | (1.2) ⇒ closure                            | $\|\Pi_NV_{5S}[:,:,a]\|=4\times10^{-15}$; mismatch slope 4.006; on-shell values for two complements agree to $10^{-16}$ at $g=0.3$                                                                                                              | 5b: $V_5^{\rm closure}+10^{-2}V_5^{\rm generic}$ gives $c_3=-9.1\times10^{-5}$ matching (1.4) to $2\times10^{-5}$ |
| 6     | $\ker V_4=0$ limit = R17                   | full-rank $V_4$: mismatch $-\tfrac{g^4}{600}vV_4^{-1}v=O(g^5)$, slope 5.000                                                                                                                                                                     | 6b: $1/500$ leaves $O(g^4)$                                                                                       |
| 7     | remedy (a) (3.1)                           | mismatch slope 4.007 in the failure case; $O(g^4)$ coefficient $C$-dependent (0.57 vs 2.36)                                                                                                                                                     | 7b: multiplier imposing $\xi=\tfrac12\pi_NP$ inside the remedy code leaves $O(g^3)$ (slope 2.92)                  |
| 8     | polarisation step of (1.6)                 | $(\mathrm C_{\rm ver})$ subspace of $\mathrm{Sym}^5$ built from the cubic $V_5(\Xi,\Psi^{\otimes3})$ at 40 sampled $\Psi$ (no symmetry used) vs the $(\mathrm C_{\rm full})$ nullspace: both dimension 20, projector distance $8\times10^{-15}$ | 8b: on non-symmetric 5-tensors the two spaces differ (984 vs 896 of 1024) — the step needs total symmetry         |
| 9     | (2.3) degree 5 in $\Psi$                   | $c_3(\lambda\Psi_0)=\lambda^5c_3(\Psi_0)$ for $\lambda=1.7,-0.6,2.3$ to $4\times10^{-15}$                                                                                                                                                       | 9b: $\lambda^6$ fails by $4.5$                                                                                    |

Not machine-checked: the deformed-shift argument (1.2$'$) (four-line algebra, in the text); §3(c) (argument only); §4 (arguments only, including (viii)); §5 (C_∞) beyond $k=2$ (stated, not tested). Dimensional / power-counting check: every $O(g^n)$ term is of degree $n+2$ in $\Psi$, including (2.3) (degree 5, check 9) and (2.4) (degree 4: $u$ cubic twice, the $\nu\times\nu$ matrix of degree 2); what (2.3) and (2.4) violate is polynomiality, not power counting. Limiting case: check 6.

## Established vs open

**Established (proven + toy-verified).**

- (1.2) (C_full) is necessary and sufficient for the $O(g_s^3)$ HS action to exist on $\mathrm{Sym}^2\mathcal H_0/\ker V_4$, and (for totally symmetric $V_5$, by polarisation) necessary and sufficient for $O(g_s^3)$ matching in every complement; it is sufficient for all of R17 to hold on the quotient. Testable form: $\Pi_N V_{5S}[:,:,a]=0$ for all basis states $e_a$, $\Pi_N=1-V_{4S}V_{4S}^+$, i.e. $\ker V_{4S}\subseteq\bigcap_a\ker V_{5S}[:,:,a]$.
- Without it, with a complement: 5-point $O(g_s^3)$ contamination (1.4), complement-dependent; the diagram route agrees (1.7).
- Without it, on the full Sym² with the dressed kernel: $C$-independent, rational, degree-5 contamination (2.3) at $O(g_s^3)$ (power counting respected, polynomiality lost), propagator $O(g_s^{-3})$ on the kernel, no vacuum propagator — perturbation theory does not survive; $O(g_s^2)$ contamination (2.4) if $W_{NN}$ is singular.
- Remedy (a) (multiplier pair on $N$) restores matching at $O(g_s^3)$ with a cubic action.
- $\ker V_4=0$ reproduces R17 exactly.

**Argued, not machine-checked.** The deformed-shift argument (1.2$'$); §3(c) reduction to (a); §4 no selection rule forces a kernel or (1.2), and the structural mechanism (viii); §5 (C_∞) and the row-by-row dependence table. (The polarisation step of (1.6) is proven in the text and its toy instance is check 8.)

**Self-review.** (1) Objective: answered — the condition is (1.2) in matrix form, now with its status settled (necessary and sufficient for the quotient prescription and for matching), the failure modes (1.4)/(2.3)/(2.4), the remedy (a), the structural scenario (viii) and the dependent rows. (2) Weakest step: the claim that (1.2) is the *right* criterion rests on the off-shell matching criterion (setup); under an amplitude-only criterion the condition could be weaker (open (vi)). Shored up by stating the criterion and its source (R10/R17). (3) Not checked: (C_∞) beyond $k=2$, the $O(g^4)$ closure of remedy (a), and the infinite-dimensional regularity — all flagged, none needed for the Task 15 Q2 test. (4) What a stronger physicist would find: whether the real $\mathcal V_4$/$\mathcal V_5$ share a common factor map (case (viii)) is a question about the geometry of the vertices that this algebraic record cannot answer; it is posed as the $N\subseteq N_5$ test.

**Open.** (i) Whether (a) closes at $O(g_s^4)$ and beyond with $C$-dependent dressings (expected by R26). (ii) Veronese-null non-degenerate $\kappa$ on $N$ other than the cotangent pair. (iii) Infinite-dimensional regularity ($N$ closed, complemented). (iv) The actual kernel size and (1.2) for the real vertices (Task 15 Q2). (v) $\ker\tilde M_k$ for $k\ge3$ (per-level (5.1)-type questions). (vi) Under an amplitude-only matching criterion (not the project's), whether $V_5(\ker V_4,P,\Psi)$ lies in the $\Psi$-EOM ideal (§3(d)). (vii) The converse of "(2.3) vanishes if $v_N=0$" as an identity in $\Psi$ for $\nu\ge2$ (§2.2).

## Critic iteration 1 — resolution

Critic report: `agent/reports/critic-034-ker-v4-v5-20260919T152000.md` (REVISE, 0 Fatal / 3 Serious / 6 Concern / 6 Minor + script items).

| id  | finding (short)                                                                                          | status | where fixed / reason if disputed                                                                                                                                                           |
| --- | -------------------------------------------------------------------------------------------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| S1  | hierarchy (1.6) collapses by polarisation; (1.2) necessary and sufficient for matching                   | fixed  | §1.1 closing sentence, §1.2 heading, (1.6) + proofs + verdict rewritten; restatements in §2.2, Established, ledger row (see S2, M4, C6); script check 8/8b                                 |
| S2  | (2.3) is degree 5 in $\Psi$, not sextic; no power-counting violation; singular $W_{NN}$ sentence         | fixed  | §2.2 properties list and verdict rewritten; (2.4) added; script checks 9/9b (homogeneity), 4c/4d (singular $W_{NN}$); restatements in Verification (M3), Established (M4), ledger row (C6) |
| S3  | §4 misses the structural kernel mechanism (common factor map, R34 scalar toy); verdicts too strong       | fixed  | §4 case (viii) added (mechanism, R34 example, finite-basis test $N\subseteq N_5$); general remark, case (vi) verdict, item-4 verdict, §3(d) sentence and the case list softened            |
| C1  | deformed shift symmetry $\Sigma\to\Sigma+\Xi+g\eta$ not considered in §1.1                               | fixed  | §1.1 paragraph "Deformed shift symmetry", (1.2$'$), re-derived; $\Sigma$-dependent $\eta$ also covered; R11 line added to the table                                                        |
| C2  | off-shell vs on-shell matching criterion not stated; $\Psi$-redefinition remedy                          | fixed  | setup bullet "Matching criterion" (off-shell in $\Psi$, R10/R17); §3(d) bullet "Weaken the criterion" (ruled out, open item (vi))                                                          |
| C3  | "vanishes iff $v_N=0$" — only "if" proven ($W_{NN}$ indefinite)                                          | fixed  | §2.2 first bullet: "if"; converse shown for $\nu=1$ only, open for $\nu\ge2$                                                                                                               |
| C4  | singular $W_{NN}$: "no saddle exists" false; saddle with $\xi=O(1/g)$, mismatch $O(g^2)$                 | fixed  | §2.2 bullet "Singular $W_{NN}$", (2.4), re-derived and toy-checked (check 4c)                                                                                                              |
| C5  | dependency table: R34 missing; R36–R37 not examined                                                      | fixed  | §5 table: R11, R34, R36, R37 lines added; scan of the unlisted rows stated                                                                                                                 |
| C6  | proposed ledger row: add necessity for matching and the structural case                                  | fixed  | §5 verdict, row rewritten (necessity, deformed shift, degree 5, (2.4), case (viii), R34)                                                                                                   |
| M1  | total symmetry of $V_5$ not stated as an assumption                                                      | fixed  | setup, $V_5$ bullet                                                                                                                                                                        |
| M2  | stale check count "14/14"                                                                                | fixed  | count is now 19/19 (13 original + 4c/4d, 8/8b, 9/9b), printed by the script; Status, Verification, ledger row                                                                              |
| M3  | "dimensional check … except (2.3)" wrong                                                                 | fixed  | Verification, power-counting sentence rewritten                                                                                                                                            |
| M4  | Established list: "sufficient for all of R17", "rational 6-point contamination"                          | fixed  | Established / Argued lists rewritten                                                                                                                                                       |
| M5  | self-review questions only implicit                                                                      | fixed  | "Self-review" paragraph before Open                                                                                                                                                        |
| M6  | script check 7b does not break check 7                                                                   | fixed  | `onshell_remedy_a(..., xi_scale)`; 7b uses $\xi=\tfrac12\pi_NP$, slope 2.92                                                                                                                |
| X1  | script: no check that the $(\mathrm C_{\rm ver})$ subspace equals the $(\mathrm C_{\rm full})$ nullspace | fixed  | checks 8/8b                                                                                                                                                                                |
| X2  | script: no $\lambda^5$ homogeneity check of the dressed-kernel mismatch                                  | fixed  | checks 9/9b; check 4c/4d (singular $W_{NN}$, (2.4)) added beyond the critic's list                                                                                                         |
