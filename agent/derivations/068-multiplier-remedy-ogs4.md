# 068 — The multiplier remedy on $\ker V_4$ at $O(g_s^4)$: finite-model decision

Brief: `agent/briefs/active-computator-multiplier-ogs4-20261001T040500.md` (Task 23). Script: `codes/verify-multiplier-ogs4.py`; logs `agent/scratch/multiplier-ogs4-run1.log` (iteration 0, 42/42) and `agent/scratch/multiplier-ogs4-run2.log` (after the critic-068 fix pass, 52/52). Fix brief: `agent/briefs/active-computator-068-fix-20261001T054000.md` (critic report `agent/reports/critic-068-20261001T052000.md`).

## Status

Complete after the critic-068 fix pass (iteration 1): every finding applied (1 major, 9 minor, 5 notes), 52/52 checks PASS (`agent/scratch/multiplier-ogs4-run2.log`), record consolidated, report `agent/reports/computator-068-fix-20261001T054000.md` written. Next: none (further critic pass at the orchestrator's discretion; the `Hypotheses in force:` line changed, see the fix log).

## 0. Task and objective

**Literal task.** In a finite model with $V_4$ of corank $r\ge1$ on $\operatorname{Sym}^2\mathcal U$, a $V_5$ that violates R38 ($V_5(\ker V_4,\cdot,\cdot)\ne0$) and a generic $V_6$, add R38's multiplier pair on the kernel directions (034 §3(a)), reproduce the $O(g^3)$ matching, and decide whether the eliminated action matches $S^{(6)}_{\rm eff}$ at $O(g^4)$ with a complement-dependent dressed vertex $W_6^{(C)}$; if so give $W_6^{(C)}$ explicitly, if not name the obstruction.

**Motivating objective.** The open-problems entry *Does the multiplier remedy on $\ker p_{2,2}$ survive beyond $O(g_s^3)$?* The paper's construction must say what it does when $\ker V_4\ne0$ (unknown at $L\ge1$; $\ker V_4=0$ at level 0, R53). The $O(g^3)$ remedy without its $O(g^4)$ continuation is the referee's question.

**Notation.** $C$ (roman) is a complement of $N:=\ker V_4$ in $\mathcal S:=\operatorname{Sym}^2\mathcal U$; $\mathcal C$ (calligraphic) is R19's $\Sigma$-channel exchange composite. The brief's "$\mathcal C$-dependence" is complement dependence.

## Conventions and assumptions

- **A1** Finite model, as in 013/053 (`codes/verify-b3-sextic.py` l. 79–190) but with $\mathcal S$-level tensors: $\mathcal U=\mathbb Q^n$, $\mathcal S=\operatorname{Sym}^2\mathcal U$ with the basis $E_{aa}$, $E_{ab}+E_{ba}$ ($D=n(n+1)/2$; not orthonormal, no inner product is used); $V_4$ a symmetric bilinear form on $\mathcal S$ with $\dim\ker V_4=r$; $V_5$ a tensor on $\mathcal S\times\mathcal S\times\mathcal U$ symmetric in the two $\mathcal S$ slots; $V_6$ a symmetric trilinear form on $\mathcal S$. $V_5(\Psi^5):=V_5(P,P,\Psi)$, $V_6(\Psi^6):=V_6(P,P,P)$, $P=\Psi\otimes\Psi$. Total symmetry on $\mathcal U^{\otimes 5,6}$ is not imposed (R38's necessity statement needs it; the remedy does not).
- **A2** Action normalisation of 013/R19 (C4): $S_4=-\tfrac{g^2}{24}V_4(\Sigma,\Sigma)+\tfrac{g^2}{12}V_4(\Sigma,P)+\tfrac{g^3}{5!}V_5(\Sigma,\Sigma,\Psi)+\tfrac{g^4}{6!}W_6(\Sigma^3)$ (shared $\Psi$-only terms dropped), $S^{(6)}_{\rm eff}=\tfrac{g^2}{4!}V_4(P,P)+\tfrac{g^3}{5!}V_5(\Psi^5)+\tfrac{g^4}{6!}V_6(\Psi^6)$.
- **A3** Multiplier pair (034 (3.1)): $S^{(C)}=S_4+g^2\langle\lambda,\Pi^{(C)}_N(\Sigma-P)\rangle$, $\lambda\in N^*$, $\Pi^{(C)}_N$ the projector on $N$ along $C$. A complement is encoded by $\mu\in\operatorname{Hom}(\mathcal S,N)$ with $\mu\vert_N=\mathrm{id}$: $\Pi_N^{(C)}=\Xi\mu$ ($\Xi$ a basis of $N$), $C=\ker\mu$.
- **A4** Matching criterion of R10/R17/R19: the eliminated action as a function of $\Psi$, off shell, tree level, order by order in $g$.
- **A5** Exact rational arithmetic; the saddle is a truncated power series in $g$ (order $\le6$), obtained by fixed-point iteration, so every Taylor coefficient is exact.

No hypothesis is in force in the finite model. The transfer to the string vertices is Conditional(PH1, PH14 [$O(g_s^4)$, exclusion legs only]) + R13 regularity; it applies when PH5's second clause fails and reduces to R19 when it holds (PH5 is not a hypothesis of the result: PH1 supplies $V_4$ non-degenerate on the quotient, equivalently on any complement, with the kernel stable; PH14 at $O(g_s^4)$ is needed only for the exclusion legs "$V_6$ alone fails", not for the existence of $W_6^{(C)}$; R13's regularity: $N$ closed and complemented).

## Candidate formula (written before computing)

With $G_C:=\iota_C\,(V_4\vert_{C\times C})^{-1}\,\iota_C^{\rm T}:\mathcal S^*\to\mathcal S$ (the symmetric reflexive generalised inverse with image $C$, kernel the annihilator $C^0$: $V_4G_CV_4=V_4$, $G_CV_4G_C=G_C$, $\operatorname{im}G_C=C$, $\ker G_C=C^0$; the first two identities and the image alone do not fix it — reflexive inverses with image $C$ form a family indexed by a complement of $N^0$ in $\mathcal S^*$, and they give different $\langle v,G'v\rangle$ exactly when $v_N\ne0$),

$$
W_6^{(C)}=V_6-\tfrac65\,\mathcal C^{(C)},\qquad
\mathcal C^{(C)}(A,B,Z)=\operatorname{sym}\sum_{e,f}Z^{ef}\,\big\langle V_5(\cdot,A,e),\,G_C\,V_5(\cdot,B,f)\big\rangle ,
\tag{0.1}
$$

R19's composite with $V_4^{-1}$ replaced by $G_C$, so that $\mathcal C^{(C)}(P,P,P)=\langle v,G_Cv\rangle$, $v=V_5(\cdot,P,\Psi)$. Expected: the eliminated action equals $S^{(6)}_{\rm eff}+O(g^5)$ for every complement; $W_6^{(C)}$ depends on $C$ iff $v_N=V_5(\Xi,\Psi^{\otimes2},\Psi)\not\equiv0$ (034's $(C_{\rm ver})$ fails; $=$ R38's (1.2) for totally symmetric $V_5$); no single $W_6$ serves two complements with $\langle v,(G_C-G_{C'})v\rangle\ne0$ *with the constraint (1.1) undeformed and $V_5(\Sigma,\Sigma,\Psi)$ the only $O(g^3)$ coupling* — an $O(g^3)$ composite coupling $g^3\langle\lambda,Z_C(\Sigma,\Psi)\rangle$ can carry the complement dependence instead (weakest relaxation, §2 (2.5)–(2.6)).

## Claim tree

- **A1–A5** above.
- **C1** Eliminating $\lambda$ and the kernel component of $\Sigma$ from $S^{(C)}$ is the restriction of $S_4$ to the affine slice $\Sigma=P+c$, $c\in C$; the on-shell value is $F^{(C)}_*(\Psi)=\operatorname{ext}_{c\in C}S_4(P+c)$, and its exact form is $F^{(C)}_*=S^{(6)}_{\rm eff}+\tfrac{g^4}{6!}[W_6(P^3)-V_6(P^3)]+\tfrac{g^4}{600}\,v_6^{\rm T}(K_6^{CC})^{-1}v_6+\tfrac{g^4}{6!}W_6(c_*^3)$ with $K_6=V_4-\tfrac g5V_5(\cdot,\cdot,\Psi)-\tfrac{g^2}{10}W_6(\cdot,\cdot,P)$, $v_6=v+\tfrac g4W_6(\cdot,P,P)$, both restricted to $C$. On shell $\lambda_*=-\tfrac g{60}v_N+O(g^2)$. [block: 1] [check: C1 (tests (1.3); the constraint holds by construction), C1-lambda]
- **C2** $O(g^3)$ (R38 reproduced): $F^{(C)}_*=S^{(5)}_{\rm eff}+O(g^4)$ for every complement; without the multiplier (linear slice $\Sigma\in C$) the $g^3$ mismatch is $-\tfrac1{5!}[V_5(P,P,\Psi)-V_5(\pi_CP,\pi_CP,\Psi)]$, 034 (1.4). [by check: C2, C2-break]
- **C3** $O(g^4)$: the remedy survives with $W_6^{(C)}$ of (0.1). [by C3.1–C3.6]
  - **C3.1** $G_C$ is the symmetric reflexive generalised inverse of $V_4$ with image $C$ (kernel $C^0$); for $C=\{c+Lc\}$, $L\in\operatorname{Hom}(C_0,N)$, $\langle w,G_Cw'\rangle=(w_{C_0}+L^{\rm T}w_N)^{\rm T}(V_4^{C_0C_0})^{-1}(w'_{C_0}+L^{\rm T}w'_N)$. [block: 2] [check: C3.1]
  - **C3.2** With the undressed $W_6=V_6$ the $g^4$ coefficient of $F^{(C)}_*-S^{(6)}_{\rm eff}$ is $\tfrac1{600}\langle v,G_Cv\rangle$. [by C1; block: 2] [check: C3.2]
  - **C3.3** That coefficient depends on $C$ iff $v_N=V_5(\Xi,\Psi^{\otimes2},\Psi)\ne0$; as an identity in $\Psi$, iff 034's $(C_{\rm ver})$ fails (under A1; $=$ R38's (1.2) for totally symmetric $V_5$); the dependence on $L$ is the quadratic of C3.1, non-constant when $v_N\ne0$ (one-line proof below (2.2)). [by C3.1, C3.2; block: 2] [check: C3.3]
  - **C3.4** With $W_6=W_6^{(C)}$ the $g^4$ coefficient vanishes for every complement (two random complements and a one-parameter family); it does not vanish with $\theta\ne\tfrac65$, with $V_6$ alone, with $\mathcal C^{(C')}$ of another complement, or with the Moore–Penrose composite in a non-orthogonal complement; without the multiplier the $g^3$ coefficient fails even with $W_6^{(C)}$. [by C1, C3.2; block: 2] [by check: C3.4, C3.4-break-*; $r=0$ limit ($G_C=V_4^{-1}$, R19 verbatim): C3.4-r0, C3.4-r0-break]
  - **C3.5** When R38 holds ($V_5(\Xi,\cdot,\cdot)=0$), the full tensor $\mathcal C^{(C)}$ is independent of $C$ and equals R19's composite on the quotient ($G_C\vert_{N^0}=\bar V_4^{-1}$, by (2.1)): R19 is recovered. [by C3.1; block: 2] [check: C3.5; C3.1 for $V_4G_CV_4=V_4$]
  - **C3.6** Within the class $\mathsf K$ (constraint (1.1) undeformed, $V_5(\Sigma,\Sigma,\Psi)$ the only $O(g^3)$ coupling, $W_6(\Sigma^3)$ the only $O(g^4)$ coupling), no complement-independent $W_6$ serves two complements with $\langle v,(G_C-G_{C'})v\rangle\ne0$ (such pairs exist when $v_N\ne0$, C3.3). Outside $\mathsf K$, an $O(g^3)$ composite coupling $g^3\langle\lambda,Z_C(\Sigma,\Psi)\rangle$ leaves $g^2$, $g^3$ untouched and shifts $[g^4]$ by $-\tfrac1{60}v_N^{\rm T}Z_C(P,\Psi)$, and with $Z_L$ of (2.6) the fixed vertex $W_6^{(C_a)}$ matches every complement: the complement dependence moves between the constraint sector and the vertex, it is not removed, and the presentation datum is the triple $(\mu,Z,W_6)$. [by C3.2, C3.3, C3.4; block: 2, (2.5)–(2.6)] [check: C3.6, C3.6-relax, C3.6-relax-shift, C3.6-relax-break]
- **C4** The $g^5$ residual with $W_6^{(C)}$ is 013's $A_5$ with $V_4^{-1}\to G_C$: $\tfrac1{600}[\tfrac12W_6^{(C)}(G_Cv,P,P)+\tfrac15\langle v,G_CW_\Psi G_Cv\rangle]$, $W_\Psi=V_5(\cdot,\cdot,\Psi)$ — the input of the next dressing (R25) in the same form. [by C1] [by check: C4]
- **C5** C2–C4 hold at corank 2 with the same formulas ($\Xi$ a $D\times2$ basis, $\mu$ a $2\times D$ matrix with $\mu\Xi=1$). [by check: C5-*]

Open gaps: none
Hypotheses in force: none (finite model); string transfer Conditional(PH1, PH14 [$O(g_s^4)$, exclusion legs only]) + R13 regularity; applies when PH5's second clause fails, reduces to R19 when it holds

## 1. Elimination of the multiplier pair and the exact on-shell form (C1)

\subsection*{Setup}
A1–A5. $\Xi$ a $D\times r$ basis of $N$, $\mu$ an $r\times D$ matrix with $\mu\Xi=1_r$, $B$ a $D\times(D-r)$ basis of $C=\ker\mu$, $\pi_C=1-\Xi\mu$. $W_\Psi:=V_5(\cdot,\cdot,\Psi)$, $v:=V_5(\cdot,P,\Psi)=W_\Psi P$. Covector restrictions $w_C:=B^{\rm T}w$, $w_N:=\Xi^{\rm T}w$.

\subsection*{Derivation}
$$
S^{(C)}(\Sigma,\lambda)=S_4(\Sigma)+g^2\,\lambda^{\rm T}\mu(\Sigma-P),\qquad \lambda\in\mathbb Q^r .
\tag{1.1}
$$
$$
\partial_\lambda S^{(C)}=0\ \Longleftrightarrow\ \mu(\Sigma-P)=0\ \Longleftrightarrow\ \Sigma=P+c,\ c=By\in C .
\tag{1.2}
$$
$$
\partial_\Sigma S^{(C)}=0\ \Longleftrightarrow\ E(\Sigma)+g^2\mu^{\rm T}\lambda=0,\quad E:=\partial_\Sigma S_4 ;\qquad
\lambda=-g^{-2}\,\Xi^{\rm T}E,\qquad \text{residual } \pi_C^{\rm T}E=0\ \Longleftrightarrow\ B^{\rm T}E=0 .
\tag{1.3}
$$
So the pair is solved exactly by the stationary point of $S_4$ on the affine slice $P+C$, and the multiplier term vanishes on shell: $F^{(C)}_*(\Psi)=\operatorname{ext}_{c\in C}S_4(P+c)$. On shell, $\Xi^{\rm T}E(\Sigma_*)=\tfrac{g^3}{60}\Xi^{\rm T}W_\Psi\Sigma_*+O(g^4)=\tfrac{g^3}{60}v_N+O(g^4)$ (as $\Xi^{\rm T}V_4=0$), so $\lambda_*=-\tfrac g{60}v_N+O(g^2)$: $O(g)$ in A3's normalisation ($O(g^3)$ in R13's, without the $g^2$ prefactor), switched on exactly by $v_N\ne0$, with no $g^{-1}$ piece — the failure mode 034 §2.2 found for the dressed-kernel alternative does not occur (check C1-lambda). Substituting $\Sigma=P+c$ in A2,
$$
S_4(P+c)=S^{(6)}_{\rm eff}+\tfrac{g^4}{6!}\big[W_6(P^3)-V_6(P^3)\big]+g^3\,\ell(c)-\tfrac{g^2}{24}K_6(c,c)+\tfrac{g^4}{6!}W_6(c^3),
\tag{1.4}
$$
$$
\ell(c)=\tfrac1{60}\,v_6(c),\quad v_6=v+\tfrac g4W_6(\cdot,P,P),\qquad
K_6=V_4-\tfrac g5W_\Psi-\tfrac{g^2}{10}W_6(\cdot,\cdot,P).
\tag{1.5}
$$
The stationary point over $c\in C$ is $c_*=\tfrac g5\,B(K_6^{CC})^{-1}(v_6)_C+O(g^4)$ (the cubic term feeds back at relative $O(g^3)$), $K_6^{CC}=B^{\rm T}K_6B=V_4^{CC}+O(g)$ invertible for small $g$ since $V_4^{CC}$ is. The on-shell value:
$$
F^{(C)}_*=S^{(6)}_{\rm eff}+\tfrac{g^4}{6!}\big[W_6(P^3)-V_6(P^3)\big]+\tfrac{g^4}{600}\,(v_6)_C^{\rm T}(K_6^{CC})^{-1}(v_6)_C+\tfrac{g^4}{6!}W_6(c_*^3)+O(g^{10}) ,\qquad \tfrac{g^4}{6!}W_6(c_*^3)=O(g^7).
\tag{1.6}
$$

\subsection*{Commentary}
(1.3): contracting the EOM with $\Xi$ and using $\mu\Xi=1$ isolates $\lambda$; what remains is the EOM evaluated on $C$ only — the kernel direction of $\Sigma$ is fixed by (1.2), not by dynamics. (1.4): the two $V_4$ terms give $\tfrac{g^2}{24}V_4(P,P)-\tfrac{g^2}{24}V_4(c,c)$ because $V_4(P+c,P+c)-2V_4(P+c,P)=V_4(c,c)-V_4(P,P)$; the $V_5$ and $W_6$ terms are expanded binomially and the linear, quadratic and cubic parts in $c$ collected. (1.6): value of a quadratic-plus-cubic function at its stationary point, $\tfrac12g^3\ell(c_*)=\tfrac{g^3}{120}v_6(c_*)=\tfrac{g^4}{600}(v_6)_C(K_6^{CC})^{-1}(v_6)_C$; the last term is $O(g^7)$, and the $O(g^4)$ shift of $c_*$ due to the cubic term enters the value at $O(g^{10})$ (stationarity of the quadratic part), as in 013 §4. This is R17/R19's exact rewriting (011 (B.2), 013 §4) with every inverse taken on $C$.

\subsection*{Result}
$$
\boxed{F^{(C)}_*-S^{(6)}_{\rm eff}=\tfrac{g^4}{6!}\big[W_6(P^3)-V_6(P^3)\big]+\tfrac{g^4}{600}\,\langle v,G_Cv\rangle+O(g^5),\qquad G_C:=B\,(B^{\rm T}V_4B)^{-1}B^{\rm T}.}
\tag{1.7}
$$
At $O(g^2)$, $O(g^3)$ the mismatch is zero for every complement (C2). Without the multiplier (linear slice $\Sigma=c\in C$) the $O(g^2)$ saddle is $c_0=G_CV_4P=\pi_CP$ and the $O(g^3)$ mismatch is $-\tfrac{g^3}{5!}[V_5(P,P,\Psi)-V_5(\pi_CP,\pi_CP,\Psi)]$, 034 (1.4) (C2-break).

## 2. The generalised inverse $G_C$ and the absorption at $O(g^4)$ (C3, C4)

\subsection*{Setup}
As in §1. Reference complement $C_0=\ker\mu_0$ with basis $B_0$; every complement is $C_L=\operatorname{col}(B_0+\Xi L)$ for a unique $L\in\operatorname{Hom}(C_0,N)\cong\mathbb Q^{r\times(D-r)}$.

\subsection*{Derivation}
$$
V_4G_CV_4=V_4,\qquad G_CV_4G_C=G_C,\qquad \operatorname{im}G_C=C,\qquad G_CV_4=\pi_C,\qquad G_C^{\rm T}=G_C,\qquad \ker G_C=C^0 .
\tag{2.1}
$$
$$
(B_0+\Xi L)^{\rm T}V_4(B_0+\Xi L)=B_0^{\rm T}V_4B_0\ \Rightarrow\ 
\langle w,G_{C_L}w'\rangle=(w_{C_0}+L^{\rm T}w_N)^{\rm T}(V_4^{C_0C_0})^{-1}(w'_{C_0}+L^{\rm T}w'_N).
\tag{2.2}
$$
Hence $\langle v,G_{C_L}v\rangle$ is a quadratic polynomial in $L$, constant iff $v_N=\Xi^{\rm T}v=V_5(\Xi,P,\Psi)=0$ (C3.3). *Only if:* with $A_0=(V_4^{C_0C_0})^{-1}$ non-degenerate and $v_N\ne0$, $y:=L^{\rm T}v_N$ sweeps all of $C_0^*$ as $L$ varies (take $L^{\rm T}=u\,\eta^{\rm T}$ with $\eta^{\rm T}v_N=1$), and $q(v_{C_0}+y)$, $q$ the quadratic form of $A_0$, is non-constant in $y$ (a non-degenerate quadratic form is non-constant on the affine line $v_{C_0}+ty$ for any $y$ with $q(y)\ne0$). As an identity in $\Psi$ the condition is $V_5(\Xi,\Psi^{\otimes2},\Psi)\equiv0$, 034's $(C_{\rm ver})$ (034 §1.2); it equals R38's (1.2) only for totally symmetric $V_5$ (034 §1.2 polarisation), which A1 does not impose — under A1, (1.2) can fail with $(C_{\rm ver})$ holding, and then the diagonal is complement-independent while the off-diagonal tensor is not (the difference is Veronese-null). *Quotient identification (C3.5):* for $w=V_4x$, $w'=V_4x'$ (all of $N^0=\operatorname{im}V_4$), $\langle V_4x,G_CV_4x'\rangle=V_4(x,\pi_Cx')=V_4(x,x')$ by (2.1), i.e. $G_C\vert_{N^0}=\bar V_4^{-1}$ on $\mathcal S/N$ for every $C$. With (1.7), the $O(g^4)$ matching condition for every $\Psi$ reads $W_6(P,P,P)=V_6(P,P,P)-\tfrac65\langle v,G_Cv\rangle$, and since $\langle v,G_Cv\rangle=\mathcal C^{(C)}(P,P,P)$ for the composite (0.1), it is solved by
$$
\boxed{W_6^{(C)}=V_6-\tfrac65\,\mathcal C^{(C)},\qquad \mathcal C^{(C)}=\mathcal C\big|_{V_4^{-1}\to G_C}.}
\tag{2.3}
$$
The $O(g^5)$ residual with $W_6^{(C)}$ follows from (1.6) by expanding $(K_6^{CC})^{-1}=(V_4^{CC})^{-1}[1+\tfrac g5W_\Psi^{CC}(V_4^{CC})^{-1}+\dots]$ and $v_6$:
$$
[g^5]\big(F^{(C)}_*-S^{(6)}_{\rm eff}\big)=\tfrac1{600}\Big[\tfrac12W_6^{(C)}(G_Cv,P,P)+\tfrac15\langle v,G_CW_\Psi G_Cv\rangle\Big]=A_5\big|_{V_4^{-1}\to G_C}.
\tag{2.4}
$$
*Relaxation of the class of C3.6 (critic-068 #1, hand algebra there; machine-checked here).* Add to $S^{(C)}$ the cubic, ghost-saturating composite coupling $g^3\langle\lambda,Z(\Sigma,\Psi)\rangle$, $Z:\mathcal S\times\mathcal U\to N$ linear in $\Sigma$, built from $V_5$ and an inverse on a complement (the class of $\mathcal C$). The $\lambda$-EOM becomes $\mu(\Sigma-P)+gZ(\Sigma,\Psi)=0$; on shell all multiplier terms vanish and $F=S_4$ at the constrained extremum on the deformed surface. With $\Sigma=P+c+\Xi\eta$, $c\in C$, $\eta=-gZ(P,\Psi)+O(g^2)$, and $\Xi^{\rm T}E=\tfrac{g^3}{60}v_N+O(g^4)$:
$$
S_4(P+c+\Xi\eta)=S_4(P+c)+\eta^{\rm T}\Xi^{\rm T}E+O(\eta^2)\ \Rightarrow\
F^{(C,Z)}_*-F^{(C)}_*=-\tfrac{g^4}{60}\,v_N^{\rm T}Z(P,\Psi)+O(g^5),
\tag{2.5}
$$
$g^2$, $g^3$ untouched. By (2.2) with reference $C_a$, $A_a=(B_a^{\rm T}V_4B_a)^{-1}$, $\langle v,G_{C_L}v\rangle-\langle v,G_{C_a}v\rangle=v_N^{\rm T}LA_a(2B_a+\Xi L)^{\rm T}v$ is of the form $v_N^{\rm T}(\text{linear in }v)$, so
$$
Z_L(\Sigma,\Psi)=\tfrac1{10}\,LA_a(2B_a+\Xi L)^{\rm T}\,V_5(\cdot,\Sigma,\Psi)
\quad\Longrightarrow\quad [g^4]\big(F^{(C_L,Z_L)}_*-S^{(6)}_{\rm eff}\big)=0\ \text{with the fixed vertex } W_6^{(C_a)},
\tag{2.6}
$$
and in general the $O(g^4)$ matching condition reads $W_6(P^3)=V_6(P^3)-\tfrac65\langle v,G_Cv\rangle+12\,v_N^{\rm T}Z(P,\Psi)$.

\subsection*{Commentary}
(2.1): for $x\in\mathcal S$, $B^{\rm T}V_4x=B^{\rm T}V_4\pi_Cx$ since $V_4N=0$, so $G_CV_4x=\pi_Cx$; the other identities follow. $B^{\rm T}V_4B$ is invertible: $B^{\rm T}V_4Bx_C=0$ makes $V_4Bx_C$ vanish on $C$ and on $N$, hence $V_4Bx_C=0$, $Bx_C\in N\cap C=0$. $G_C$ is symmetric by construction and $\ker G_C=\ker B^{\rm T}=C^0$; since $C^0\cap N^0=(C+N)^0=0$, this fixes $G_C$ within the family of reflexive inverses with image $C$ (which is indexed by a complement of $N^0$ in $\mathcal S^*$, the kernel). (2.2): $V_4\Xi=0$ kills every $L$-dependence of the restricted form; only the restricted covectors move, by $L^{\rm T}w_N$. The Moore–Penrose inverse of the coordinate representation is $G_{N^\perp}$ (image and kernel both the coordinate-orthogonal complement), one member of the family, with no distinguished role — the string field has no auxiliary inner product (PH1). (2.3): the condition fixes $W_6$ on the Veronese cone only, as in R19; (0.1) is the choice with R19's strand-split structure. Its $C$-dependence is not a Veronese-null form: $W_6^{(C)}(P^3)-W_6^{(C')}(P^3)=-\tfrac65\langle v,(G_C-G_{C'})v\rangle\ne0$ (C3.6, within the class $\mathsf K$ of the Result). What is complement-independent is the eliminated action, not the vertex: the pair (constraint $\mu$, vertex $W_6^{(C)}$) is the presentation within $\mathsf K$, and the triple $(\mu,Z,W_6)$ once an $O(g^3)$ constraint coupling is allowed ((2.5)–(2.6)). (2.4): 013's $A_5$ verbatim, so R25's $O(g_s^5)$ dressing is expected to proceed with the same replacement (not verified: R25's closure uses $\Sigma_3$ with $\tilde M_3$, $L_3$ and its own kernel questions, PH2 (b), untouched here). (2.5): $\Xi^{\rm T}V_4=0$ makes $\Xi^{\rm T}E$ start at $g^3$; the $O(\eta^2)$ term is $O(g^2)\cdot O(g^3)$, and the re-extremisation over $c$ on the deformed surface enters at second order by stationarity. (2.6): $\tfrac1{60}\cdot\tfrac1{10}=\tfrac1{600}$ cancels the difference of the (1.7) feedback terms between $C_L$ and $C_a$; the $12$ of the general condition is $\tfrac{720}{60}$. This presentation freedom is specific to the hybrid: R17's uniqueness table has no $\lambda$.

\subsection*{Result}
The remedy survives at $O(g^4)$ with (2.3); no complement-independent $W_6$ exists when $v_N\ne0$ *with the constraint (1.1) undeformed and $V_5(\Sigma,\Sigma,\Psi)$ the only $O(g^3)$ coupling* — an $O(g^3)$ composite coupling $g^3\langle\lambda,Z_C(\Sigma,\Psi)\rangle$ can carry the complement dependence instead ((2.5)–(2.6), weakest relaxation), so the presentation datum is $(\mu,Z,W_6)$ with $W_6(P^3)=V_6(P^3)-\tfrac65\langle v,G_Cv\rangle+12\,v_N^{\rm T}Z(P,\Psi)$; under R38 ($v_N=0$ for all $\Psi$, i.e. $V_5(\Xi,\cdot,\cdot)=0$) the whole tensor $\mathcal C^{(C)}$ is complement-independent by (2.2) and equals R19's composite on the quotient ($G_C\vert_{N^0}=\bar V_4^{-1}$): R19's quotient statement is recovered (C3.5). Neither R38's (1.2) nor 034's (C$^{(6)}$) is needed in the hybrid: $\Sigma$ lives on the full $\mathcal S$ and nothing has to descend.

### Scope of the exclusion

- **Class.** $\mathsf K$: the constraint (1.1) with the undeformed Veronese value, the $O(g^3)$ sector $V_5(\Sigma,\Sigma,\Psi)$ only, the $O(g^4)$ sector $W_6(\Sigma^3)$ only. Reason for the class: it is the hybrid presentation 034 §3(a) proposed (R13's multiplier pair restricted to $N$, 034 (3.1)), continued from $O(g^3)$ with only the new coupling $O(g^4)$ brings, $W_6(\Sigma^3)$.
- **Relevant cases outside.** $O(g^3)$ composite couplings of the constraint sector, $g^3\langle\lambda,Z(\Sigma,\Psi)\rangle$ with $Z$ built from $V_5$ and an inverse on a complement (the class of $\mathcal C$); they are invisible at $O(g^2)$, $O(g^3)$ and shift $[g^4]$ by (2.5).
- **Weakest relaxation that evades it.** Admitting that coupling: with $Z_L$ of (2.6) every complement $C_L$ matches with the single vertex $W_6^{(C_a)}$ (check C3.6-relax, corank 1 and 2, complements $C_L$, $C_{2L}$, $C_b$; without $Z$ the same complements fail, C3.6-relax-break). The complement dependence is moved between the constraint sector and the sextic vertex, not removed: the reference complement $C_a$ is still a choice, and no canonical member appears.

## 3. Result, scope, self-review

**Verdict.** The multiplier remedy survives at $O(g^4)$. With the multiplier pair on $\ker V_4$ (constraint $\mu(\Sigma-P)=0$, complement $C=\ker\mu$) and the dressed vertex $W_6^{(C)}=V_6-\tfrac65\mathcal C^{(C)}$, $\mathcal C^{(C)}$ being R19's composite with $V_4^{-1}$ replaced by the symmetric reflexive generalised inverse $G_C=B(B^{\rm T}V_4B)^{-1}B^{\rm T}$ (image $C$, kernel the annihilator $C^0$), the eliminated action equals $S^{(6)}_{\rm eff}+O(g^5)$ for every complement, off shell in $\Psi$ (as an identity in $\Psi$ after solving the $\Sigma$ and $\lambda$ equations, A4). The $O(g^5)$ residual is 013's $A_5$ with the same replacement, so the next dressing (R25) is expected to proceed with $V_4^{-1}\to G_C$ (not verified: R25's closure has its own kernel questions, PH2 (b)). In the hybrid neither R38's (1.2) nor 034's (C$^{(6)}$) is needed.

**What is complement-dependent.** The vertex: $\langle v,G_{C_L}v\rangle=(v_{C_0}+L^{\rm T}v_N)^{\rm T}(V_4^{C_0C_0})^{-1}(v_{C_0}+L^{\rm T}v_N)$ is a non-constant quadratic in $L\in\operatorname{Hom}(C_0,N)$ exactly when $v_N=V_5(\Xi,P,\Psi)\ne0$ — as an identity in $\Psi$, when 034's $(C_{\rm ver})$ fails (= R38's (1.2) for totally symmetric $V_5$) — and its difference between two complements is not a Veronese-null form (C3.6): no single $W_6$ serves two complements *with the constraint (1.1) undeformed and $V_5(\Sigma,\Sigma,\Psi)$ the only $O(g^3)$ coupling*; an $O(g^3)$ composite coupling $g^3\langle\lambda,Z_C(\Sigma,\Psi)\rangle$ can carry the complement dependence instead ((2.5)–(2.6), weakest relaxation), so the presentation datum is $(\mu,Z,W_6)$ with $W_6(P^3)=V_6(P^3)-\tfrac65\langle v,G_Cv\rangle+12\,v_N^{\rm T}Z(P,\Psi)$. The physics is not: every member of the family (constraint $\mu$, vertex $W_6^{(C)}$) gives the same $S_{\rm eff}$ through $O(g^4)$. This is the "presentation freedom" of 034 §3(a), made explicit and larger than R19's (the constraint moves with the vertex); the eliminated action is complement-independent through $O(g^4)$, the $O(g^5)$ residual (2.4) is $C$-dependent until the next dressing. Under R38, (2.2) makes the entire tensor $\mathcal C^{(C)}$ complement-independent and R19 is recovered.

**Regime.** Finite model, exact rationals: $n=3$ ($D=6$), corank 1 and 2 (and the $r=0$ limit), two random complements plus a one-parameter family, two $\Psi$ points, absolute orders $g^2$–$g^5$ exact. Generic $V_5$, $V_6$ on $\mathcal S$ (symmetric in the $\mathcal S$ slots; total symmetry on $\mathcal U^{\otimes n}$ not imposed and not used). Not covered: the gauge law of the hybrid action (R19's implicit law plus a $\delta\lambda$; not asked), the $O(g^5)$ closure and beyond (the $O(g^5)$ residual is covered, (2.4)), the BV pairing and ghost number of $(\xi,\lambda)$ (034 §3(a) item (ii): $N_{\rm gh}(\lambda)=6$, $\lambda^\ddagger=\lambda$ by R34/R35, unchanged here), and the string vertices: there the statement is Conditional(PH1, PH14 [$O(g_s^4)$, exclusion legs only]) + R13 regularity ($N$ closed and complemented); it applies when PH5's second clause fails and reduces to R19 when it holds. In the string case the complement must be chosen compatibly with the gradings (ghost number, level, momentum) and with whatever symmetry $\ker V_4$ carries; since $V_4$ is homogeneous, $N$ is graded and a graded complement exists.

**Self-review.** (1) The objective — what the construction does when $\ker V_4\ne0$ at $O(g_s^4)$ — is answered: the same dressed vertex with $V_4^{-1}\to G_C$. (2) Weakest step: the transfer of "generalised inverse on a complement" to the infinite-dimensional $\operatorname{Sym}^2\mathcal H_0$, where a complement of $\ker V_4$ must be chosen without an inner product; in the finite model this is a free $L$, in the string case it is the same R13 regularity question. (3) Not checked: the gauge law; the complement family was varied along one line $tL$ and two random points, not over all of $\operatorname{Hom}(C_0,N)$ — (2.2) and the one-line non-constancy proof below it cover the rest algebraically. The $r=0$ limit is run (C3.4-r0: $G_C=V_4^{-1}$, R19 recovered). (4) A stronger physicist would note that the dependence of $W_6^{(C)}$ on $C$ is a field redefinition in disguise: shifting the complement by $L$ moves the fixed kernel component $\xi=\Xi\mu P$ and the vertex together. This is R18(2)/034 §1.1: kernel shifts $\delta\Sigma\in N$ are an exact symmetry at $O(g^2)$ and survive at $O(g^3)$ iff (1.2) (034's (1.2′) row for R11); the constraint is a gauge fixing of that shift, and when (1.2) fails the fixing is no longer a symmetry choice, which is why $W_6$ has to move with it (or $Z$, (2.5)–(2.6)). A canonical choice would need extra structure (e.g. a $V_5$-adapted complement, $C=\ker\mu$ with $\mu$ built from $v$), which no data of the project singles out. Noted, not pursued.

### Proposed ledger row and texts (critic-068 § *Proposed texts (R75)*; row updated to the post-fix run, see the fix log)

**Row R75 — the multiplier remedy on $\ker V_4$ survives at $O(g_s^4)$ [Proven (finite-dimensional algebraic layer) – Verified (finite model)].** Source: `agent/derivations/068-multiplier-remedy-ogs4.md` C1–C5, §1–§3; `codes/verify-multiplier-ogs4.py`, 52/52 PASS (`agent/scratch/multiplier-ogs4-run2.log`), seed 20261001, exact rationals, $n=3$, corank 1 and 2 (13 break legs per corank) and the $r=0$ limit ($G_C=V_4^{-1}$, R19 recovered; C3.4-r0). With the multiplier pair $g_s^2\langle\lambda,\Pi_N^{(C)}(\Sigma-\Psi^{\otimes2})\rangle$ on $N=\ker V_4$ (034 (3.1); $C$ a complement of $N$, $\Pi_N^{(C)}$ the projector on $N$ along $C$) and the dressed vertex $W_6^{(C)}=V_6-\tfrac65\mathcal C^{(C)}$, $\mathcal C^{(C)}$ being R19's $\Sigma$-channel composite with $V_4^{-1}$ replaced by $G_C=B(B^{\rm T}V_4B)^{-1}B^{\rm T}$, the symmetric reflexive generalised inverse of $V_4$ with image $C$ ($V_4G_CV_4=V_4$, $G_CV_4G_C=G_C$, $G_CV_4=\pi_C$), the eliminated action equals $S^{(6)}_{\rm eff}+O(g_s^5)$ as an identity in $\Psi$ for every complement; the $O(g_s^5)$ residual is 013's $A_5$ with the same replacement. Neither R38's (1.2) nor 034's (C$^{(6)}$) is needed: $\Sigma$ stays on $\operatorname{Sym}^2\mathcal H_0$ and nothing descends. The vertex is complement-dependent iff $V_5(\ker V_4,\Psi^{\otimes2},\Psi)\not\equiv0$ (R38's (1.2) for totally symmetric $V_5$): $\langle v,G_{C_L}v\rangle$ is a non-constant quadratic in $L\in\operatorname{Hom}(C_0,\ker V_4)$ (068 (2.2)), and no complement-independent $W_6$ serves two complements *with the constraint undeformed and $V_5(\Sigma,\Sigma,\Psi)$ the only $O(g_s^3)$ coupling*; an $O(g_s^3)$ composite coupling $g_s^3\langle\lambda,Z_C(\Sigma,\Psi)\rangle$ can carry the complement dependence instead (068 (2.5)–(2.6); check C3.6-relax, corank 1 and 2), so the presentation datum is (constraint, $O(g_s^3)$ constraint coupling, vertex) and the eliminated action is complement-independent through $O(g_s^4)$. Under R38 the composite tensor is complement-independent and R19 is recovered; the Moore–Penrose inverse is one member of the family with no distinguished role (PH1: no auxiliary inner product). String transfer: Conditional(PH1, PH14 [$O(g_s^4)$, for the exclusion legs]) plus R13's regularity of $\ker V_4$ (closed, complemented, graded complement); applies in the branch where PH5's second clause fails. Not covered: the hybrid's gauge law and BV pairing (R13's open item restricted to $N$), the $O(g_s^5)$ closure and beyond.

**Open-problems entry** *Does the multiplier remedy on $\ker p_{2,2}$ survive beyond $O(g_s^3)$?* — Closed 2026-10-01 at $O(g_s^4)$ in the finite-dimensional algebraic layer (R75, record 068): yes, with $W_6^{(C)}=V_6-\tfrac65\mathcal C^{(C)}$, $V_4^{-1}\to G_C$ on the chosen complement; the $O(g_s^5)$ residual has 013's $A_5$ form with the same replacement, so the continuation is expected to be R25/R26's scheme with $V_4^{-1}\to G_C$ throughout (not verified beyond the $g_s^5$ residual). What remains is folded into R13's open item: the BV structure of the $(\xi,\lambda)$ pair and the hybrid's gauge law. (Move the closed text to `knowledge/decisions.md` per the TODO rule.)

**R38 annotation (2026-10-01, R75).** Remedy (a) continues at $O(g_s^4)$: with the dressed vertex $W_6^{(C)}=V_6-\tfrac65\mathcal C\vert_{V_4^{-1}\to G_C}$ the hybrid matches $S^{(6)}_{\rm eff}$ in every complement; the $O(g_s^4)$ feedback of §3(a) item (i), $\tfrac{g_s^4}{600}\langle v,G_Cv\rangle$, is quadratic in the complement parameter $L$ and constant iff $(C_{\rm ver})$ holds. The "expected, not verified" of item (i) is discharged; the (1.2) condition remains that of the *quotient* presentation.

**R19 annotation (2026-10-01, R75).** When $\ker V_4\ne0$ and (1.2) fails, $W_6$ exists in the hybrid presentation with $V_4^{-1}\to G_C$ (R75); the 2026-10-01 annotation's (C$^{(6)}$) is a condition of the quotient presentation only and is moot in the hybrid.

**PH5 annotation addendum (2026-10-01, R75).** The second clause and the proposed third clause are requirements of the quotient presentation of $\Sigma$; the hybrid presentation (R75) needs neither, at the price of a complement choice carried by the constraint and the sextic vertex. They condition how the construction is *presented* when $\ker V_4\ne0$, not whether it exists.

## Verification

Script `codes/verify-multiplier-ogs4.py`, seed 20261001, exact rationals, truncated series to absolute $O(g^5)$; current log `agent/scratch/multiplier-ogs4-run2.log`, 52/52 PASS, exit 0, 5.8 s (`OMP_NUM_THREADS=1`). Checks and break legs as listed in the script docstring, named after the tree nodes: C1 (+break), C1-lambda, C2 (+break: 034 (1.4) reproduced exactly), C3.1 (+break), C3.2 (+break: $1/600\ne1/720$), C3.3 (+break), C3.4 (+5 breaks: $\theta=1$, $V_6$ alone, other complement's composite, Moore–Penrose composite in a non-orthogonal complement, no multiplier), C3.5 (+break), C3.6, C4 (+break: factor $\tfrac12\to1$), C3.6-relax, C3.6-relax-shift, C3.6-relax-break; all repeated at corank 2 (C5-*); then the $r=0$ limit, C3.4-r0 (+break). C2, C3.2, C3.4, C3.6-relax, C3.6-relax-shift, C3.4-r0 and C4 compare exact Taylor coefficients of the eliminated action against independently written formulas ((1.7), (2.4), (2.5), (2.6), 034 (1.4), R19's vertex); C1, C1-lambda, C3.1, C3.3, C3.5, C3.6 are identity or inequality checks on $G_C$, $\lambda_*$ and the constraint ((1.3), (2.1), (2.2)). None asserts an expression against itself. C1: the constraint half $\mu(\Sigma-P)=0$ holds by construction ($\Sigma=P+By$, $B=\ker\mu$) and the restricted saddle is the assert inside `eliminate`, so C1 tests the $\lambda$ formula (1.3). C3.6-relax implements the deformed constraint exactly: $\mu(\Sigma-P)+gZ(\Sigma,\Psi)=0$ with $Z=M\Sigma$ is solved by $\Sigma=R(g)(P+By)$, $R=1-g\Xi(1+gM\Xi)^{-1}M$, and the saddle is taken over $y$ on that surface; the complements are $C_L$, $C_{2L}$ and $C_b$ ($L_b=-\mu_bB_a$), the vertex is $W_6^{(C_a)}$ throughout. The script's reference complement of the family is $C_a$ (the record's $C_0$); no consequence. The new legs draw from separate seeded generators, so the 42 original checks run on the same data as run 1 (identical PASS lines).
Each new leg was broken once on purpose (scratch copy, not saved): $\tfrac1{10}\to\tfrac1{12}$ in $Z_L$, the sign of the $-\tfrac1{60}$ shift, $\tfrac1{60}\to\tfrac1{50}$ in $\lambda_*$, $\tfrac1{600}\to\tfrac1{720}$ in the $r=0$ break: all seven affected checks FAIL, as required.

Run history: the first run failed C1 and C5-C1 because the constraint test subtracted $P$ from every order of the $\Sigma_*$ series instead of the zeroth (a check typo, diagnosed before any change to the result); corrected, rerun, 42/42 (`multiplier-ogs4-run1.log`; the orchestrator's rerun log is identical). Fix pass (critic-068): legs C1-lambda, C3.6-relax(-shift, -break), C3.4-r0(-break) added and C3.1 strengthened ($G_C=G_C^{\rm T}$, $\ker G_C=C^0$); `eliminate` generalised to a deformed constraint surface (the undeformed path is $R=1$, same algebra); two full runs, both 52/52 (the second after a message change and `ruff format`; its log is `multiplier-ogs4-run2.log`), plus one perturbed run in scratch. No result changed.

Not verified by machine: the gauge law of the hybrid; the infinite-dimensional transfer.

## Fix log (critic-068 iteration 1, 2026-10-01)

Changed nodes, and whether the statement or only the justification changed:

- **C1** statement extended ($\lambda_*=-\tfrac g{60}v_N+O(g^2)$, #13) and check scope stated (C1 tests (1.3), #15); new check C1-lambda.
- **C3.1** statement sharpened: "a reflexive generalised inverse" → "the symmetric reflexive generalised inverse … (kernel $C^0$)" (#5); C3.1 check strengthened.
- **C3.3** statement changed: "iff R38 fails" → $v_N\ne0$, as an identity in $\Psi$ 034's $(C_{\rm ver})$ (= R38's (1.2) for totally symmetric $V_5$) (#7); justification extended by the only-if line (#6).
- **C3.4** justification only: $r=0$ legs added (#4).
- **C3.5** justification only: $G_C\vert_{N^0}=\bar V_4^{-1}$ written (#8).
- **C3.6** statement changed: scoped to the class $\mathsf K$, relaxation (2.5)–(2.6) added, citation of C3.3 added (#1, #9); new checks C3.6-relax, -shift, -break.
- `Hypotheses in force:` line changed: string transfer Conditional(PH1, PH14 [$O(g_s^4)$, exclusion legs only]) + R13 regularity, PH5 removed as a hypothesis (#2). No node of the finite model is conditional on it.

Dependents (transitively to the root C3):

- C3.2 (by C1) — holds: uses (1.6)–(1.7) only, unchanged.
- C3.4 (by C1, C3.2) — holds: unchanged algebra; rerun PASS.
- C4 (by C1) — holds: (2.4) unchanged; rerun PASS.
- C3.3 (by C3.1) — holds with its new statement.
- C3.5 (by C3.1) — holds.
- C3.6 (by C3.2, C3.3, C3.4) — holds with its new statement; the relaxation is machine-checked.
- C3 (by C3.1–C3.6) — holds as written: its statement (the remedy survives with $W_6^{(C)}$) does not use the exclusion of C3.6.
- C5 (by checks C5-*) — holds: all corank-2 legs, old and new, PASS.

Restatements updated: candidate-formula paragraph, §2 Commentary and Result, §3 Verdict / complement-dependence / Regime / Self-review, proposed row and texts, Verification block.
