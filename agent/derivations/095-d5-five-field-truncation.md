# 095 — The order-$d^5$ term of the five-field truncation against the sister's quintic dilaton identity

Brief: `agent/briefs/active-computator-095-d5-five-field-20261006T182212.md`.
Companion script: `codes/verify-d5-five-field.py`.

## Status

2026-10-06 19:25. Complete: §1–§4, Verification, Result, proposed ledger entry; fix pass on critic iteration 1 applied (see `## Fix pass`); script 58/58 PASS (seed 20261006; 56 checks that test a claim + 2 arithmetic lines C4.1-arith-*). Next: none (report).

## Task and objective

**Literal task.** In the five-field truncation (record 059: $\Psi=tT+dD$ at level (1,1), zero momentum, $\Sigma\in\mathrm{Sym}^2\{T,D\}$) extended to R61's quintic action $S_3$, compute the $d^5$ coefficient of the tree-level effective potential along the dilaton after eliminating $t$ and $\Sigma$, in book normalisation, at $\beta=\tfrac32,2$; express it through the sister's brackets and compare with $120V^{(5)}=\{D^5\}^{\rm contact}+5\{DDT\}\{TD^3\}-5\{DDf_1\}\{f_1D^3\}$, which the sister's $d^5$ identity sets to zero.

**Objective.** (1) Consistency check at $n=5$ of the action's normalisation (R1's $2g^2/4!$, R61's $g^3/5!$, $V_2(T,T)$, the sign conventions) against the sister's $d^5$ identity, under the factorisation rule for $C_5^{\rm book}$ (part of PH27; R43 covers $n\le4$): our action must reproduce the sister's $T$-exchange term with its factor $5$ and sign, and its contact term with the right factor. This does not test $\lambda_5$ or $C_5$ (§4). (2) Physical: is the truncated $d^5$ coefficient the dropped $f_1$ exchange, $+5\{DDf_1\}\{f_1D^3\}$ in $120V^{(5)}$ units (the $d^5$ analogue of R64 (iv)), and does the cubic HS route add anything at $d^5$?

## Conventions and assumptions

- **A1** Book normalisation, sister → book $V_n\times\tfrac12$ per sphere correlator, signs unchanged; equivalently $S_{\rm book}(\Psi;g)=\tfrac12S_{\rm sister}(\Psi;g)$ at equal field values and equal coupling. R43 is cited for $n\le4$ only (Verified there); at $n=5$ the factor $\lambda_5=\tfrac12$ is an input fixed by the factorisation rule of PH27 (C4, conditional). [R43; 059 A1]
- **A2** Potential side $\mathcal V:=-S$ at zero momentum, action-side vertices $V_n=-\{\cdot\}_{\rm pot}$, so $V_n^{\rm book}=-\tfrac12\{\cdot\}$. [C5; 059 A2]
- **A3** Five-field model and the action $S_3=\tfrac12V_2(\Psi^2)+\tfrac g{3!}V_3(\Psi^3)-\tfrac{g^2}{4!}V_4(\Sigma,\Sigma)+\tfrac{2g^2}{4!}V_4(\Sigma,P)+\tfrac{g^3}{5!}V_5(\Sigma,\Sigma,\Psi)$, $P=\Psi^{\otimes2}$, $\mathcal S=\mathrm{Sym}^2\{T,D\}$, $A=V_4\vert_{\mathcal S}$ invertible. [R1, R61; 057 Conventions, §3; 059 A3]
- **A4** Level-(1,1) data in book normalisation: $V_2(T,T)=1$, $V_2(T,D)=V_2(D,D)=0$; $V_3(T^3)=$ (companion value, not reproduced here), $V_3(TD^2)=$ (companion value, not reproduced here), $V_3(T^2D)=V_3(D^3)=0$ (chiral ghost number); $h_k=V_4(T^{4-k}D^k)$. Sign check against A2: the sister's potential brackets (059 (1.3); values from the companion SL(2,C) computation, not reproduced here) give $V_3^{\rm book}=-\tfrac12\{\cdot\}$, i.e. the signs of $V_3(T^3)$ and $V_3(TD^2)$ ($V_3(T^3)$ does not enter $c_5$). [059 C1, (1.2)–(1.3); R64]
- **A5** Sister data (its normalisation, potential side, declared section, Convention P `SL: C3`): $\{D^5\}^{\rm contact}$, $\{DDT\}=$ (companion value, not reproduced here), $\{DDf_1\}=$ (companion value, not reproduced here), $\{TD^3\}$ (`SL: R44`), $\{f_1D^3\}$ (`SL: R69`), $\Pi_T=+\tfrac12$, $\Pi_{f_1}=-\tfrac12$ (`SL: 060` A2); the numerical values of $\{D^5\}^{\rm contact}$, $\{TD^3\}$ and $\{f_1D^3\}$ come from the companion SL(2,C) computation and are not reproduced here. [cited: `SL: R44`, `SL: R64`, `SL: R69`; `SL: 060` A2, (1.3)]
- **A6** Tree level, zero momentum; $\Sigma$ eliminated on the perturbative branch $\Sigma_*=P+O(g)$; Taylor coefficients in $d$ are formal (R61 scope). Convention C7 (Mandelstam sign) is inert at zero momentum.
- **PH27** (cited, not redeclared): the kept HS vertices, $V_5$ included, are the truncation of a consistent genus-zero family; used to identify our $V_5(D^5)$ with the sister's $\{D^5\}^{\rm contact}$ (book: $V_5(D^5)=-\tfrac12\{D^5\}^{\rm contact}$). The content of PH27 includes the normalisation factorisation: a consistent genus-zero family fixes the normalisation of $V_5$ relative to $V_3$, $V_4$ through the recursion, $C_5^{\rm book}=(C_4^{\rm book})^2/C_3^{\rm book}$ (so $\lambda_5=\tfrac12$; first used in §4 and C4). Not computed for the book (the sister states it for its side).
- **SL: PH5** (the sister's hypothesis, cited by its sister label): the five-point vertex extends the family consistently at the chain level; the sister's numerical closure $V^{(5)}=0$ is conditional on it.

### Free constants (fixed before assembling)

| Constant | Value | Independent source |
|---|---|---|
| coefficient of $V_5$ in $S_3$ | $g^3/5!$ | R17/R61 (057 Conventions) |
| $V_2(T,T)$ (book, action side) | $1$ | 059 (1.2): $L_0^+=-2$, $g(T,T)=-\tfrac12$ |
| sister → book factor for $V_5$, $\lambda_5$ | $\tfrac12$ | factorisation rule $C_5=C_4^2/C_3$ on each side (part of PH27), $\tfrac{(1/2)^2}{1/2}=\tfrac12$; the same statement as R43's uniform scaling per sphere correlator ($n\le4$ there), not a second fixing |
| action ↔ potential sign | $V_n=-\{\cdot\}$ | C5 |
| sister propagator $\Pi_T$ | $+\tfrac12$ | `SL: 060` A2 |

No constant is fitted; nothing is fitted from the identity. $\lambda_5$ is an input under PH27's factorisation rule, not an output of the identity.

## Claim tree

- **A1–A6** as above. Hypotheses: PH27 (ours, including the normalisation factorisation $C_5=C_4^2/C_3$ in the book normalisation), SL: PH5 (the sister's), both cited.
- **C0** (root) Under PH27 (including the normalisation factorisation, so $\lambda_5=\tfrac12$) and SL: PH5: in the five-field truncation of $S_3$ (A3), the tree-level $d^5$ coefficient of $\mathcal V_{\rm eff}=-S_{\rm eff}$ (book) is $g^3c_5$ with $c_5=-\tfrac{V_5(D^5)}{120}+\tfrac{V_3(TD^2)V_4(TD^3)}{12V_2(T,T)}=\tfrac1{240}\big[\{D^5\}^{\rm contact}+5\{DDT\}\{TD^3\}\big]$, half the sister's $V^{(5)}$ without its $f_1$ term; it equals $\tfrac1{48}\{DDf_1\}\{f_1D^3\}=$ (companion value, not reproduced here) to (companion value, not reproduced here) relative to the contact term, and $c_5>0$ (numerical values not reproduced here); the cubic HS structure contributes nothing at $d^5$. [by C1–C4]
  - **C1** Only three structures can reach $d^5$: the contact $V_5(D^5)$, the $T$ exchange $V_3(TD^2)\times V_4(TD^3)$, and the $T$–$T$ caterpillar through $V_3(T^2D)$, which vanishes. [by C1.1–C1.3]
    - **C1.1** Eliminating $\Sigma$ from $S_3$ gives $S^{(5)}_{\rm eff}\vert_{\mathcal U}$ plus terms of degree $\ge6$ in $\Psi$, the first being R61's $\tfrac{g^4}{600}v_S^\top A^{-1}v_S$, nonzero for generic data; so $\Sigma$ adds nothing at $d^5$ beyond $\tfrac{g^3}{5!}V_5(\Psi^5)$. [by A3, R61; eq. (1.2)] [check: C1.1-sigma-degree6-*, C1.1-break-cross-coupling-*, C1.2-V5-encoding-*]
    - **C1.2** Weight counting: along the dilaton $t_*=O(gd^2)$, a monomial $t^jd^m$ reaches $d^{m+2j}$; weight $\le5$ leaves $t^2$ (propagator), $td^2$, $td^3$, $t^2d$, $d^4$, $d^5$; $t^3$, $t^2d^2$ and all of C1.1's remainder are weight $\ge6$. This uses $V_2(T,D)=V_2(D,D)=0$ and $V_3(D^3)=0$ (A4), without which $t$ would be sourced at $O(d)$ or $d$ would not be flat. [by A4, C1.1; eq. (1.3)]
    - **C1.3** $V_3(T^2D)=0$ (chiral ghost number, 059 (1.3)), so the $t^2d$ term, which would contribute $-\tfrac{V_3(T^2D)V_3(TD^2)^2}{8V_2(T,T)^2}$ to $c_5$, does not enter. [by A4; eq. (1.4)] [check: C2.1-routeA-closed-form-* with generic $V_3(T^2D)$]
  - **C2** Closed form and translation: $c_5=\tfrac1{240}\big[\{D^5\}+5\{DDT\}\{TD^3\}+\tfrac{15}4\{DDT\}^2\{TTD\}\big]$, the $T$-sector part of the sister's (1.3) times $\tfrac12$; factor $5$ and sign by the elimination (route A) and by the Feynman count of the same elimination (route B). [by C2.1–C2.3]
    - **C2.1** Route A (elimination): exact elimination of $\Sigma$ and of $t$ from $S_3$ at random rational couplings ($V_3(T^2D)\ne0$ kept generic) gives eq. (1.4); the $d^5$ coefficient is independent of $t$'s $O(d^3)$ term ($2n+1$ rule). [by A3, C1; eq. (1.4)] [by check: C2.1-routeA-closed-form-*, C2.1-2n+1-*] [check: C2.1-d4-*]
    - **C2.2** Route B (the same $t$-elimination counted by channels, sister side; not an independent derivation – its agreement with route A restates C1.1 plus the sign conventions A2): $10=\binom52$ one-propagator channels, $15$ two-propagator trees (both by enumeration), $\Pi_T=-1/\{TT\}=+\tfrac12$, then $\times\tfrac12$ (A1) and the action→potential sign (A2), equal to route A. [by A1, A2, A5; eq. (2.1)–(2.3)] [by check: C2.2-routeB-*]
    - **C2.3** The comparison is falsifiable: factor $4$ or $6$ in place of $5$, the sign of the exchange flipped, or the contact doubled (the missing $\tfrac12$ on $V_5$ alone) each fail route A (closed-form perturbations); the action-level break, the coefficient $g^3/4!$ in place of R61's $g^3/5!$ inside the elimination, makes route A disagree with route B (C2.2 fails) – this is the falsifier of the factor-5 claim. [by check: C2.3-break-*, C2.3-break-action-v5-coeff-*]
  - **C3** Numbers: with the sister's printed values (not reproduced here), $240c_5=\{D^5\}+5\{DDT\}\{TD^3\}$ agrees with $5\{DDf_1\}\{f_1D^3\}$ ($\beta=\tfrac32,2$) to (companion value, not reproduced here) of $\lvert\{D^5\}\rvert$ – the sister's own residual, reproduced. So the truncated coefficient is the dropped $f_1$ exchange. [by C2, A5; SL: PH5 for the input $\{D^5\}^{\rm contact}$ and the identity; §3] [by check: C3.1-identity-*, C3.1-positive-*] [check: C3.1-break-*, C3.3-h3-059-*, C3.2-d4-*]
  - **C4** Normalisation at $n=5$: consistency, not a test. Under the factorisation rule $C_5^{\rm book}=(C_4^{\rm book})^2/C_3^{\rm book}$ (part of PH27; stated by the sister for its side, argued and not computed for the book), $\lambda_5=\tfrac12$, and our action reproduces the sister's $d^5$ structure term by term at uniform weight $\tfrac12$; every term of the identity carries net weight one sphere correlator, so given the sister's identity the book-side identity is equivalent to the factorisation rule ($\lambda_5=\lambda_3\lambda_4/\lambda_2=\tfrac12$; a non-uniform $\lambda_5$ gives an $O(1)$ residual, which only confirms that a non-uniform rescaling of a vanishing sum does not vanish). The result is consistent with a uniform ratio at $V_5$ under the factorisation rule (assumed); it neither fixes $\lambda_5$ independently of that rule nor measures $C_5$. What it does check: R1's $\tfrac{2g^2}{4!}$ and R61's $\tfrac{g^3}{5!}$ are mutually consistent with the Feynman rules and the sign conventions (C2). [by PH27, R43 ($n\le4$), C2, C3; §4] [by check: C3.1-break-lambda5=*, C2.3-break-action-v5-coeff-*; bookkeeping only: C4.1-arith-*]
- **C5** (remark, cited) Adding the single level-(2,2) field $f_1=c_{-1}\bar c_{-1}\lvert0\rangle$ to the truncation makes the tree-level $d^4$ and $d^5$ coefficients equal to the sister's full ones, which vanish ($d^4$ exactly; $d^5$ under SL: PH5, numerically): $f_1$ is the Riesz representer of the two-dilaton coupling on level $(2,2)$, the tower terminates there, and $\{TDf_1\}=\{f_1Df_1\}=0$. HS: nothing new at $d^5$ for this enlarged $\mathcal U$ either. [by C1.1; cited: SL: R63, SL: R64 (060 (1.3), (2.1)–(2.2)); §4]

Open gaps: none
Hypotheses in force: PH27 (including the normalisation factorisation $C_5=C_4^2/C_3$ in the book normalisation), SL: PH5

## 1. Elimination of $\Sigma$ and $t$ along the dilaton (C1, C2.1)

\subsection*{Setup}
A3, A4, A6. $m:=V_2(T,T)$, $a:=V_3(T^3)$, $c:=V_3(T^2D)$, $b:=V_3(TD^2)$, $h_k:=V_4(T^{4-k}D^k)$, $f_k:=V_5(T^{5-k}D^k)$; $W(\Psi):=V_5(\cdot,\cdot,\Psi)\vert_{\mathcal S}$, $W_{ij}=t\,f_{i+j-2}+d\,f_{i+j-1}$ in the basis $e_1,e_2,e_3$ (the legs of $e_i$ carry $i-1$ dilatons; $e_2=\tfrac12(TD+DT)$ gives $V_5(e_2,\dots)=V_5(T,D,\dots)$). $S_{\le3}(\Psi):=\tfrac12V_2(\Psi^2)+\tfrac g{3!}V_3(\Psi^3)$. $c$ is kept symbolic until (1.4) to answer the brief's question; A4 sets it to $0$.

\subsection*{Derivation}
$$
\begin{aligned}
S_3&=\tfrac12mt^2+\tfrac g6\big(at^3+3c\,t^2d+3b\,td^2\big)-\tfrac{g^2}{24}\sigma^\top A\sigma+\tfrac{g^2}{12}\sigma^\top Ap+\tfrac{g^3}{120}\sigma^\top W\sigma, &&(1.1)\\
\sigma_*&=K_S^{-1}Ap,\quad K_S=A-\tfrac g5W,\qquad
S_3\vert_{\sigma_*}=S_{\le3}(\Psi)+\tfrac{g^2}{24}\,p^\top A K_S^{-1}Ap
=S_{\le3}(\Psi)+\tfrac{g^2}{24}\Big[p^\top Ap+\sum_{k\ge1}\big(\tfrac g5\big)^k\,p^\top W(A^{-1}W)^{k-1}p\Big]\\
&=S^{(5)}_{\rm eff}\vert_{\mathcal U}+\tfrac{g^4}{600}\,v_S^\top A^{-1}v_S+O(g^5\Psi^7),\qquad v_S=Wp, &&(1.2)\\
t_*&=-\frac{g\,b}{2m}\,d^2+O(d^3),\quad J(d)=\tfrac g2b\,d^2+\tfrac{g^2}6h_3d^3,\qquad S_{\rm eff}(d)=\tfrac{g^2}{24}h_4d^4+\tfrac{g^3}{120}f_5d^5-\frac{J^2}{2m}+\tfrac g2c\,t_*^2d+O(d^6), &&(1.3)\\
\Big[\mathcal V_{\rm eff}\Big]_{g^3d^5}&=c_5=-\frac{f_5}{120}+\frac{b\,h_3}{12\,m}-\frac{c\,b^2}{8\,m^2}\;\overset{c=0,\,m=1}{=}\;-\frac{V_5(D^5)}{120}+\frac{V_3(TD^2)V_4(TD^3)}{12}. &&(1.4)
\end{aligned}
$$

\subsection*{Commentary}
- (1.2): 057 (3.2) is exact: $W$ is linear in $\Psi$ and $p$ quadratic, so the $k$-th term of the Neumann series of $K_S^{-1}$ has degree $4+k$; $k=1$ is $\tfrac{g^3}{120}V_5(P,P,\Psi)=\tfrac{g^3}{120}V_5(\Psi^5)$, $k\ge2$ is degree $\ge6$. The series converges for $\lVert\tfrac g5A^{-1}W(\Psi)\rVert<1$; as Taylor coefficients the statement is exact (A6). Check `C1.1-sigma-degree6-*` confirms at random rational data that $S_3\vert_{\sigma_*}-S^{(5)}_{\rm eff}$ has no monomial of degree $\le5$ and a nonzero degree-6 one; the break (R1's cross coupling $\tfrac{2g^2}{4!}$ replaced by $\tfrac{g^2}{4!}$) leaves a degree-4 term.
- (1.3): $\partial_tS=mt+J(d)+gc\,td+O(t^2,\,g^2t\,d^2)$ with $J(d)=\tfrac g2b\,d^2+\tfrac{g^2}6h_3d^3$; with $V_2(T,D)=0$ there is no $O(d)$ source, so $t_*=O(gd^2)$, and $S_{\rm eff}$ through $d^5$ is $\tfrac m2t_*^2+t_*J+\tfrac g2c\,t_*^2d+\dots$ evaluated on $t_2=-\tfrac{gb}{2m}$, which gives $-J^2/2m$ at the orders kept. The $O(d^3)$ correction $t_3$ of $t_*$ multiplies $\partial_tS\vert_{O(d^2)}=0$ at order $d^5$ ($2n+1$ rule; check `C2.1-2n+1-*`). The remaining weight-$\le5$ monomials are listed in C1.2.
- (1.4): $-J^2/2m$ gives $-\tfrac{g^2b^2}{8m}d^4-\tfrac{g^3bh_3}{12m}d^5$; $\tfrac g2c\,t_*^2d=\tfrac{g^3cb^2}{8m^2}d^5$; $\mathcal V=-S$ (A2). The $d^4$ part is 059 C3.5's $h_4/24-b^2/8$ in $S$ ($b^2/8-h_4/24$ in $\mathcal V$; $m=1$), a regression of the same code path (`C2.1-d4-*`, `C3.2-d4-*`).
- $V_3(T^3)$, $V_4(T^2D^2)$, $V_4(T^3D)$, $V_4(T^4)$ and $V_5(T^{5-k}D^k)$, $k\le4$, do not enter $c_5$ (weight $\ge6$). The $t^2$ terms enter only as the propagator $1/m$.

\subsection*{Result}
$$\boxed{\;\mathcal V_{\rm eff}(d)\supset g^3c_5\,d^5,\qquad c_5=-\frac{V_5(D^5)}{120}+\frac{V_3(TD^2)\,V_4(TD^3)}{12\,V_2(T,T)}\;}$$
exact (formal Taylor coefficient), with no contribution from $\Sigma$ beyond the $V_5(\Psi^5)$ it reproduces.

\subsection*{Verification}
`C2.1-routeA-closed-form-*` (three seeded sets of random rationals, $c\neq0$, $m\neq1$, $g\neq1$): exact elimination of $\sigma$ by `sympy.solve` and of $t$ by series in $d$ with stationarity order by order, against (1.4), exact equality. Breaks `C2.3-break-*` (factor $\tfrac45$, $\tfrac65$ on the exchange, its sign, contact doubled) all differ from route A.

## 2. Translation to the sister's brackets; second route (C2.2)

\subsection*{Setup}
A1, A2, A5. Book action-side vertices from sister potential brackets: $V_X^{\rm book}=-\tfrac12\{X\}$, so $m=-\tfrac12\{TT\}=1$, $b=-\tfrac12\{DDT\}$ (companion value, not reproduced here), $c=-\tfrac12\{TTD\}$, $h_3=-\tfrac12\{TD^3\}$, $f_5=-\tfrac12\{D^5\}$.

\subsection*{Derivation}
$$
\begin{aligned}
c_5&=\frac{\{D^5\}}{240}+\frac{\tfrac14\{DDT\}\{TD^3\}}{12\cdot(-\tfrac12\{TT\})}+\frac{\tfrac12\{TTD\}\tfrac14\{DDT\}^2}{8\cdot\tfrac14\{TT\}^2}
=\frac12\cdot\frac1{120}\Big[\{D^5\}+10\,\Pi_T\{DDT\}\{TD^3\}+15\,\Pi_T^2\{DDT\}^2\{TTD\}\Big], &&(2.1)\\
\Pi_T&=-\{TT\}^{-1}=+\tfrac12\quad(\text{sister 060 A2: }G_{TT}=-1,\ L_0^+=-2), &&(2.2)\\
240\,c_5&=\{D^5\}^{\rm contact}+5\{DDT\}\{TD^3\}+\tfrac{15}4\{DDT\}^2\{TTD\},\qquad \{TTD\}=0. &&(2.3)
\end{aligned}
$$

\subsection*{Commentary}
- (2.1), first equality: substitution of the Setup into (1.4), $\{TT\}=-2$. Second equality: algebra with $\Pi_T=-1/\{TT\}$; the coefficients $10$ and $15$ are what the sister's (1.3) carries as channel counts ($\binom52$ pairs on the cubic vertex; $15$ trivalent trees with five labelled leaves). Route B in the script builds (2.1)'s right side from the enumeration (`itertools`: 10 pairs, 15 unordered pairs of disjoint pairs), the propagator (2.2) and the conversions, and compares with route A's eliminated coefficient: equal at three random rational data sets (`C2.2-routeB-*`). Route B is the standard Feynman count, i.e. the same elimination of $t$ written as a channel count ($10\,\Pi_T/120=\Pi_T/12$ is $-J^2/2\{TT\}$ at $d^5$); its agreement with route A restates C1.1 (after $\Sigma$-elimination the action is a standard $\sum\tfrac1{n!}V_n$ potential) plus the sign conventions A2, and is not an independent derivation. What constrains the factor $5$ is the coefficient of $V_5$ in $S_3$: with $g^3/4!$ in place of $g^3/5!$ inside the elimination route A no longer matches route B (`C2.3-break-action-v5-coeff-*`).
- Sign: the exchange enters $120V^{(5)}$ with $+5\{DDT\}\{TD^3\}$ because $\Pi_T>0$ on the potential side, i.e. because $T$ is tachyonic ($L_0^+=-2$) with $G_{TT}=-1$; in our variables because $V_2(T,T)=+1$ in $S$ and $\mathcal V=-S$. The $f_1$ term enters with $-5$ through $\Pi_{f_1}=-\tfrac12$ ($L_0^+=+2$, $G=-1$).
- (2.3) is the $T$ sector of the sister's (1.3) times $\tfrac12$ (A1), plus the $T$–$T$ caterpillar that the sister's §2 sets to zero by the cubic chiral rule ($N=-1$ term, $\{TTD\}=0$; $N:=L_0^+/2$ labels the level, $T$ has $N=-1$, $f_1$ has $N=1$). Every structure of the truncation has its counterpart in the sister's formula with the same coefficient; the only term of the sister's formula absent from (2.3) is the $f_1$ exchange.

## 3. Numbers and the identification of the residual (C3)

\subsection*{Setup}
A5 values (sister normalisation, declared section): $\{DDT\}=$ (companion value, not reproduced here); $\{DDf_1\}=$ (companion value, not reproduced here); the numerical values of $\{D^5\}^{\rm contact}$, $\{TD^3\}$ and $\{f_1D^3\}$ at $\beta=\tfrac32,2$ come from the companion SL(2,C) computation and are not reproduced here.

\subsection*{Derivation}

The two sides $240c_5=\{D^5\}+5\{DDT\}\{TD^3\}$ and $5\{DDf_1\}\{f_1D^3\}$ differ, relative to $\lvert\{D^5\}\rvert$, by (companion value, not reproduced here) at $\beta=\tfrac32$ and at $\beta=2$ (the numerical values of the two sides and of $c_5$ are not reproduced here).

$$
c_5=\frac{\{DDf_1\}\{f_1D^3\}}{48}\quad(\text{under SL: PH5}),\qquad
g^2\mathcal V_{\rm eff}\big\vert_{\rm valley}=(\text{companion value, not reproduced here})\,\delta^4+c_5\,\delta^5+O(\delta^6),\ \delta=gd. \tag{3.1}
$$

\subsection*{Commentary}
- The difference is the sister's own residual $\mathcal R$: relative to its scale $\mathcal S\approx\lvert\{D^5\}\rvert+5\lvert\{DDT\}\{TD^3\}\rvert$ it agrees with the sister's own residual up to the rounding of the printed inputs. Nothing new is measured here; the identification "truncated $=$ $f_1$ exchange" is the identity rearranged, and its numerical support is the sister's.
- The two pieces kept by the truncation cancel to a small fraction of the contact term; what is left is entirely the level-(2,2) exchange. Same pattern as at $d^4$ (R64 (iv)): there the residual (companion value, not reproduced here) is $\tfrac12\cdot\tfrac1{24}\cdot\tfrac32\{DDf_1\}^2$ (`C3.2-d4-f1-*`), the $f_1$ exchange of the $d^4$ identity.
- Sign and shape: $c_5>0$ at both $\beta$ (companion values, not reproduced here), so the truncated valley, lifted at $\delta^4$, is tilted at $\delta^5$: up for $\delta>0$, down for $\delta<0$. $c_5$ is of the same order as the $\delta^4$ coefficient, so the two are comparable only at $\lvert\delta\rvert\sim1$, outside the formal regime (A6); the stationary point of (3.1), of order one, is not a statement about the truncation.
- Section: $c_5$ is section-dependent through $\{f_1D^3\}$ (or $\{D^5\}$, $\{TD^3\}$). With the sister's harmonic-section $\{f_1D^3\}$ (`SL: R69`; values not reproduced here) the right side of (3.1) takes different values; the identity has not been tested in that section (sister R64, option O1), so these are not values of $c_5$ there.

## 4. Normalisation at $n=5$: consistency, not a test (C4), and the six-field remark (C5)

**What is assumed.** $\lambda_5=\tfrac12$: (i) R43 shows (for $n\le4$) that the discrepancy is the sphere vacuum normalisation, entering once per sphere correlator, and $V_5$ is one sphere correlator integrated over $\mathcal V_{0,5}$; (ii) the measure constants obey $C_N=C_3(C_4/C_3)^{N-3}$ on each side. This factorisation rule is part of the content of PH27 (a consistent genus-zero family fixes the normalisation of $V_5$ relative to $V_3$, $V_4$ through the recursion): the sister states it for its side (value not reproduced here); for the book it is argued by the same factorisation that fixed $C_4^{\rm book}=-1/\pi$ from $C_3^{\rm book}=1$ in 062, here on the faces $\mathcal V_{0,3}\circ\mathcal V_{0,4}$ of $\mathcal V_{0,5}$ – not computed. So $C_5^{\rm book}/C_5^{\rm sister}=\tfrac{(1/2)^2}{1/2}=\tfrac12$ (arithmetic, `C4.1-arith-*`). Nothing is fitted; (i) and (ii) are one statement (uniform scaling per correlator), not two independent fixings.

**What the comparison establishes.** (a) Our action's coefficients (R1's $\tfrac{2g^2}{4!}$, R61's $\tfrac{g^3}{5!}$, $V_2(T,T)=1$, the action-side signs of C5) reproduce the sister's $d^5$ formula term by term, factor $5$ and sign of the $T$ exchange included, by the elimination (route A) and by the Feynman count of the same elimination (route B, which restates C1.1 plus the sign conventions; C2). (b) Every term of the identity has net weight one sphere correlator ($\{D^5\}$: one; $\{DDT\}\{TD^3\}\Pi_T$: two vertices, one inverse kinetic term), so under a uniform $\lambda$ the identity is covariant, and with $\lambda_{2,3,4}=\tfrac12$ (R43) the book-side identity holds iff $\lambda_5=\tfrac12$; $\lambda_5=1$ or $\tfrac14$ leaves an $O(1)$ residual (`C3.1-break-lambda5=*`, (companion value, not reproduced here) of the contact scale), which only shows that a non-uniform rescaling of a vanishing sum does not vanish. Given the sister's identity, the dilaton theorem in book normalisation is equivalent to the factorisation rule for $C_5^{\rm book}$; nothing here fixes $\lambda_5$ independently of that rule. (c) What it does not establish: an independent value of $C_5$ in either normalisation (the book has no $V_5$), nor anything about the family's existence at $n=5$ (PH27, SL: PH5 stay open). What (a) does test: R1's $\tfrac{2g^2}{4!}$ and R61's $\tfrac{g^3}{5!}$, with the signs of C5, are consistent with the Feynman rules (action-level break `C2.3-break-action-v5-coeff-*`). R43's uniform ratio is consistent with a uniform ratio at $V_5$ under the factorisation rule (assumed); it is not extended by this record.

**Six-field remark (C5).** On the level-(2,2) Siegel space the two-dilaton coupling is $\kappa_1G(f_1,\cdot)$ with $f_1=c_{-1}\bar c_{-1}\lvert0\rangle$, $G(f_1,f_1)=-1$ (`SL: R63`), so the full level-(2,2) exchange equals the single-field one: $J_2\Pi J_2=\tfrac{J_2(f_1)^2}{2G(f_1,f_1)}$, $J_3\Pi J_2=\tfrac{J_2(f_1)J_3(f_1)}{2G(f_1,f_1)}$, giving $-\tfrac32\{DDf_1\}^2$ and $-5\{DDf_1\}\{f_1D^3\}$ in the sister's normalisation. With $\mathcal U=\mathrm{span}\{T,D,f_1\}$ the weight count of C1.2 is unchanged ($f_1$ is sourced at $O(d^2)$), $\{TDf_1\}=\{f_1Df_1\}=0$ by the cubic chiral rule (ghost bidegrees $(1,1)+(2,0)+(1,1)\neq(3,3)$), and no level $N\ge2$ or $L_0=0$ state is sourced (`SL: R63`, `SL: R64`). The six-field truncation therefore has $d^4$ and $d^5$ coefficients equal to the full tree-level ones: $0$ at $d^4$ (exact, all $\beta\ge\tfrac32$, `SL: R63`), and $V^{(5)}$, numerically $0$ under SL: PH5, at $d^5$. C1.1 holds for any $\mathcal U$ with $\mathcal S=\mathrm{Sym}^2\mathcal U$, so the HS form adds nothing there either. Not computed here: the six-field action itself ($V_4(f_1D^3)$ etc. in book normalisation) – a statement about its $d^{\le5}$ coefficients only.

## Verification

`codes/verify-d5-five-field.py`, run from the project root with `.venv/bin/python` under `/usr/bin/time -v`: 58 lines, 0 FAIL, seed 20261006, exit 0, peak RSS 73 MB, 53 s (logs `agent/scratch/computator/computator-095-d5-five-field-20261006T182212/run{1,2}.log` for the original 55; `agent/scratch/computator/computator-095-fix-20261006T190631/run1.log` for the 58 after the fix pass). Of the 58, 56 test a claim and 2 (`C4.1-arith-*`) are bookkeeping: the arithmetic of the assumed factorisation rule, which no wrong physical result would fail. Exact (sympy rationals): C1.1, C1.2, C2.1, C2.2, C2.3, C3.2. Numerical (30-digit floats on 13-digit inputs): C3.1, C3.3. Break legs firing: C1.1 cross coupling (degree-4 residue), C2.3 factor 4, 6, sign, contact doubled (closed-form perturbations compared with route A), C2.3 action-level break (coefficient $g^3/4!$ in place of $g^3/5!$ inside the elimination; route B then disagrees with route A, the leg counts PASS when the disagreement is detected – the falsifier of the factor-5 claim), C3.1 factor 4, 6 ((companion value, not reproduced here) of the contact scale), sign (companion value, not reproduced here), $\lambda_5=1$ (companion value, not reproduced here), $\lambda_5=\tfrac14$ (companion value, not reproduced here), against a pass threshold $10^{-12}$. Not verified: $\lambda_5$ and $C_5$ (an input under PH27's factorisation rule), the sister's inputs and identity (cited), PH27, SL: PH5; C5 rests on the sister's representer statement and is not machine-checked here.

## Result

Under PH27 (including the normalisation factorisation $C_5=C_4^2/C_3$, so $\lambda_5=\tfrac12$) and SL: PH5: the tree-level $d^5$ coefficient of the level-(1,1) five-field truncation of the cubic HS action is
$$\mathcal V_{\rm eff}\supset g^3c_5d^5,\qquad c_5=-\frac{V_5(D^5)}{120}+\frac{V_3(TD^2)V_4(TD^3)}{12V_2(T,T)}=\frac{\{D^5\}^{\rm contact}+5\{DDT\}\{TD^3\}}{240}=\frac{\{DDf_1\}\{f_1D^3\}}{48},$$
$c_5>0$ at $\beta=\tfrac32$ and $\beta=2$, declared section (numerical values not reproduced here). The cubic HS structure adds nothing at $d^5$ (its first own term is R61's $O(g^4\Psi^6)$ Schur term); $V_3(T^2D)$ would enter but vanishes; the $t^2$ terms enter only as the propagator. The nonzero $c_5$ is the level-(2,2) $f_1$ exchange that the truncation drops, as at $d^4$; adding $f_1$ alone restores both. Normalisation: the agreement of the factor $5$ and of the signs is a consistency check, under the factorisation rule, that R1's $\tfrac{2g^2}{4!}$ and R61's $\tfrac{g^3}{5!}$ are consistent with the Feynman rules and the sign conventions; it does not test $\lambda_5$ or $C_5$.

### Scope of the exclusion

The negative statement is "the level-(1,1) truncation has no flat dilaton direction at $d^5$". Class: the five-field truncation $\{T,D\}$, $\mathrm{Sym}^2\{T,D\}$, at zero momentum and tree level, declared section, $\beta\in\{\tfrac32,2\}$; the class is the one of record 059/R64, chosen as the lowest level containing the dilaton. Physically relevant cases outside: the six-field truncation $\{T,D,f_1\}$ (flat through $d^5$, C5), any higher level truncation (also flat through $d^5$, since nothing beyond $N=1$ is sourced; cited, SL: R63/R64, at $d^5$ under SL: PH5), other sections (value of $c_5$ changes, its non-vanishing not established there although $\{f_1D^3\}\neq0$ in the harmonic section too). Weakest relaxation that evades it: add the single field $f_1=c_{-1}\bar c_{-1}\lvert0\rangle$.

## Proposed ledger entry

**R89 — Five-field truncation at quintic order: the $d^5$ dilaton coefficient is the dropped $f_1$ exchange; HS adds nothing at $d^5$** [Conditional(PH27, SL: PH5) – mixed; PH27 includes the normalisation factorisation $C_5=C_4^2/C_3$ in the book normalisation]

- **Source**: `agent/derivations/095-d5-five-field-truncation.md` C0–C5
- **Scope**: excl. within the level-(1,1) five-field truncation (zero momentum, tree level, declared section, $\beta\in\{\tfrac32,2\}$, formal Taylor coefficients); sister inputs cited, not reproduced
- **Verification**:
  - 2026-10-06 – exact check – `codes/verify-d5-five-field.py` C1.1, C1.2, C2.1–C2.3, C3.2 (route A elimination vs route B Feynman count of the same elimination, three random rational data sets; closed-form breaks on factor 4/6, sign, contact $\times2$; action-level break with $g^3/4!$ in place of $g^3/5!$, the falsifier of the factor-5 claim), 58/58 PASS of which 2 are arithmetic only (`C4.1-arith-*`, the assumed factorisation rule, not checks), seed 20261006
  - 2026-10-06 – numerical check – same script C3.1: $240c_5$ vs $5\{DDf_1\}\{f_1D^3\}$ to (companion value, not reproduced here) of $\lvert\{D^5\}\rvert$ (the sister's residual, reproduced from its printed values)

Text: $\mathcal V_{\rm eff}\supset g^3c_5d^5$, $c_5=-\tfrac{V_5(D^5)}{120}+\tfrac{V_3(TD^2)V_4(TD^3)}{12V_2(T,T)}=\tfrac1{240}[\{D^5\}^{\rm contact}+5\{DDT\}\{TD^3\}]$ (exact; factor $5$ and sign by elimination and by channel count – Verified); $\Sigma$ adds nothing below degree 6, $V_3(T^2D)=0$ removes the only other weight-5 structure (Proven, Verified on random data); under SL: PH5 $c_5=\tfrac1{48}\{DDf_1\}\{f_1D^3\}>0$ (Numerical, declared section; values not reproduced here). Normalisation: $\lambda_5=\tfrac12$ is an input under the factorisation rule $C_5^{\rm book}=(C_4^{\rm book})^2/C_3^{\rm book}$, part of PH27 (R43 covers $n\le4$); given the sister's identity, the book-side identity is equivalent to that rule, so the agreement of the factor $5$ and the signs is a consistency check (R1's $\tfrac{2g^2}{4!}$ and R61's $\tfrac{g^3}{5!}$ against the Feynman rules and the sign conventions), not a test of $\lambda_5$ or $C_5$; it is consistent with a uniform ratio at $V_5$ under the factorisation rule (assumed). Annotation for R64 (iv): the $d^5$ analogue of the valley residual, and adding $f_1$ alone makes $d^4$, $d^5$ exact.

## Fix pass (critic iteration 1)

Critic report `agent/reports/critic-095-20261006T185457.md`; brief `computator-095-fix-20261006T190631`.
No number, formula or conclusion of §1–§3 changed; no node statement changed except C4 (restated) and C0's hypothesis line (statement of the hypotheses in force only).

| Finding | Action | Status |
|---|---|---|
| #1 major | Factorisation rule cited under PH27 (stated in PH27's entry, §4 "What is assumed", C4); `Hypotheses in force:` line now "PH27 (including the normalisation factorisation $C_5=C_4^2/C_3$ in the book normalisation), SL: PH5", also in C0's header, claim-tree line, Result and ledger tag note; A1 cites R43 for $n\le4$ only, $n=5$ by C4 conditional; free-constants row for $\lambda_5$ rewritten (an input, not a second fixing). No local hypothesis declared (orchestrator decision). | applied |
| #2 major | §4 retitled "consistency, not a test"; (b)'s last sentence replaced by the critic's wording; "independent fixings" dropped; (c)'s "PH24's discharge extends to $V_5$" replaced by "consistent with a uniform ratio under the factorisation rule (assumed); not extended"; C4 restated; Objective (1), Result and ledger entry (title tag, body, verification lines) rewritten accordingly. | applied |
| #3 note | C8 mention removed from A6. | applied |
| #4 minor | Route B described as the same $t$-elimination counted by channels, agreement restates C1.1 + A2, in C2, C2.2 and §2 commentary ("Two independent paths" removed). | applied |
| #5 note | "in $S$" ($b^2/8-h_4/24$ in $\mathcal V$) added to the §1 commentary. | applied |
| #6 minor | A1 qualified (R43, $n\le4$); see #1. | applied |
| #7 note | One line in A4: $\{T^3\}_{\rm pot}=$ (companion value, not reproduced here), $\{TD^2\}_{\rm pot}=$ (companion value, not reproduced here) (059 (1.3)) with $V_3^{\rm book}=-\tfrac12\{\cdot\}$ give A4's signs. The critic's "$\{T^3\}_{\rm sis}=$ (companion value, not reproduced here)" is the action-side sign; no discrepancy. | applied |
| #8 note | $N:=L_0^+/2$ defined at first use (§2 commentary): $T$ has $N=-1$, $f_1$ has $N=1$. | applied |
| #9 minor | Scope line: "(cited, SL: R63/R64, at $d^5$ under SL: PH5)". | applied |
| #10 minor | `v5_coeff` argument added to `hs_action`; break leg `C2.3-break-action-v5-coeff-*` ($g^3/4!$; route B then disagrees with route A, counted PASS when detected, 3 legs); stated as the falsifier of the factor-5 claim in C2.3, §2 commentary and the Verification block. | applied |
| #11 minor | C4.1 relabelled `C4.1-arith-*`, "bookkeeping, not a check", excluded from the count (58 lines = 56 claim checks + 2 arithmetic); in the Verification block, ledger line and script docstring. | applied |
| #12 minor | Unused `eps` entries deleted. | applied |

Findings not applied: none. Script re-run after the edits: 58 lines, 0 FAIL, seed 20261006 (log `agent/scratch/computator/computator-095-fix-20261006T190631/run1.log`).
