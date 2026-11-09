# 088 — Which family the IBL generating function encodes: the sign at one output, and how the raising enters the relations

## Status

Fix pass (critic iteration 1) complete (2026-10-04 16:30, text only). C1–C3 are unchanged in statement, and C1–C4 established. The raised family is renamed $p^{\Omega}_{m,n}$. The replacement text is revised and now also covers l. 172, 205–206 and 228. Check `C3.0` (node C3.1) is written and not yet run. The script last ran before the fix, at 20/20 PASS. The revised LaTeX is not compiled. Next:
- the orchestrator runs `codes/verify-ibl-generating-sign.py` and expects 22/22;
- a narrow confirmation critic;
- transcription into `paper/sections/07-ibl.tex`, with a compile.

## Task and objective

**Literal task.** Paper `paper/sections/07-ibl.tex` l. 128–141, 156, 160: (a) sign relation between the $\Omega^{-1}$-raised family and the family of `eq:conv:sprod` at $n=1,2$ (and $n=3$), on unrestricted superfields and on ghost-number-two inputs; is l. 132 ("overall sign for one output") right, and under which restriction; (b) which family `eq:ibl:generating` holds for verbatim; (c) whether sorting `eq:ibl:polarized-master` by degree gives the genus-zero IBL relations of the $\Omega^{-1}$-raised family when the generating function is read with the `eq:conv:sprod` family, and whether the sign differences are an overall sign per relation or relative signs. Then replacement text for l. 128–141 (and l. 156, 160 if needed).

**Objective.** The paper claims: the $\Omega^{-1}$-raised family satisfies the genus-zero IBL relations iff the $\ell_n$ form a cyclic $L_\infty$ algebra (R31). Record 086's critic (#5) found the passage defines the family and its generating function in two ways that disagree by a sign at one output. The fix must make the passage consistent without weakening the theorem.

## Conventions

As record 086 *Conventions* (C1 of `knowledge/conventions.md`; paper `eq:conv:odd-symplectic`): $g_{ab}=\pair{e_a}{e_b}=g_{ba}$, support $\varepsilon_a+\varepsilon_b=1$; $\Omega_{ab}=(-1)^{\varepsilon_a}g_{ab}$; $(\Omega^{-1})^{ab}=g^{ab}(-1)^{\varepsilon_b}$. Parity operator $P$ on $\Hs$: $Pe_a=(-1)^{\varepsilon_a}e_a$ (acts on basis vectors, not on Grassmann coefficients). Multi-string pairing `eq:conv:pairing-n`: $\pair[n]{A_1\otimes\cdots\otimes A_n}{B_1\otimes\cdots\otimes B_n}=(-1)^{\sum_{i<j}\abs{B_i}\abs{A_j}}\prod_i\pair{A_i}{B_i}$. For a homogeneous tensor, $\abs{\cdot}$ is the total parity of its strands (of the states, never of coefficients). The sprod family is written $p_{m,n}$, the $\Omega^{-1}$-raised family $p^{\Omega}_{m,n}$ (one-output member $\ell^{\Omega}_m$; written $\hat p_{m,n}$, $\hat\ell_m$ before the fix pass: the hat is the paper's mark for the extension to the symmetric algebra, 07-ibl l. 228–232, critic #7), the $\Omega'$-raised family $p^{\Omega'}_{m,n}$.

## Decomposition: the sign questions, expected answers, falsifiers

Written before computing (brief constraint); outcomes in brackets.

- **Q1 (a, definition).** l. 130: $\Omega^{-1}$ "differs from $\Delta$ by a sign $-1$ on that leg" when the raised leg is odd. Raising slot $a$: $(\Omega^{-1})^{ca}=g^{ca}(-1)^{\varepsilon_a}$, sign $-1$ when the *slot* is odd, i.e. $-P$ on the output strand. Family raised this way on every leg: A4. Expected $\Omega_n(X,Y)=(-1)^{\abs X}\pair[n]XY$, $p^{\Omega}_{m,n}=(-P)^{\otimes n}p_{m,n}$. [confirmed, C1.1]
- **Q2 (a, ghost two).** Expected: agree for every $n$ on ghost-two inputs; l. 132 wrong. Twist by the second argument ($\Omega'=-\Omega$): $(-1)^n$, overall sign at each $n$. [confirmed, C1.3; sharper form found: $p^{\Omega}_{m,n}(B)=(-1)^{\abs B}p_{m,n}(B)$, C1.2]
- **Q3 (a, unrestricted).** Expected component-dependent from $n=1$. [confirmed, C1.4]
- **Q4 (b).** Expected: `eq:ibl:generating` verbatim for the sprod family; $p^{\Omega}$ with $\Omega_n$; the paper's formula with $p^{\Omega}$ fails at $n=1$. [confirmed, C2]
- **Q5 (c).** Expected: in a family's own form the family enters a relation only through the raising of the contracted strand; $p^{\Omega}$: $-E_{m,n}$ term by term; sprod with plain composition: identically zero by mirror cancellation. [confirmed, C3.1–C3.3]
- **Q6 (c, theorem).** Expected: theorem right for $p^{\Omega}$; relative (mirror) signs, not overall, between the readings. [confirmed, C3.4]
- **Q7 (rule K).** Expected: (a) rule-independent; (b) holds for any rule applied uniformly; (c) uses rule K. [confirmed for (a), (b); (c) checked under rule K only]

## Claim tree

- **A1** Finite-dimensional graded space, basis $e_a$, ghost numbers $n_a$, $\varepsilon_a=n_a\bmod2$; $g$, $\Omega$, $\Omega^{-1}$, $P$ as in *Conventions* (C1). String field in the formal sense of the paper.
- **A2** Superfields and rule K as record 086 A2 (stated in the paper at l. 204): $\Psi=\Psi^ae_a$, $\Psi'=\Psi'^ae_a$, $\abs{\Psi^a}=\abs{\Psi'^a}=\varepsilon_a$; multilinear maps and forms evaluated by pulling coefficients to the left, each passing the basis vectors to its left.
- **A3** Vertices $\vertex n$, $n\ge2$, graded symmetric and even (nonzero only at total ghost number $2n$, `eq:conv:ghost-numbers`); $S(u)=\sum_{n\ge2}\frac{\gs^{n-2}}{n!}\vertex n(u^n)$; $\mathcal C(F,G):=\pd^r_{\Psi^a}F\,(\Omega^{-1})^{ab}\,\pd^l_{\Psi'^b}G$; $E:=\mathcal C(S(\Psi+\Psi'),S(\Psi+\Psi'))$ (`eq:ibl:polarized-master`), $E_{m,n}$ its bidegree-$(m,n)$ part; $H_{k,\ell}:=\frac{\gs^{k+\ell-2}}{k!\,\ell!}\vertex{k+\ell}(\Psi^k,\Psi'^\ell)$.
- **A4** Definition of the $\Omega^{-1}$-raised family: $\vertex{m+n}(A_1,\dots,A_n,B_1,\dots,B_m)=:\Omega_n(A_1\otimes\cdots\otimes A_n,p^{\Omega}_{m,n}(B_1,\dots,B_m))$, $\Omega_n$ the tensor power of $\Omega$ with the Koszul sign of `eq:conv:pairing-n`. Variant $\Omega'=-\Omega$ (twist by the second argument, `eq:conv:odd-symplectic` l. 344) gives $p^{\Omega'}_{m,n}$. A composition "in the family's own form" is read in generating-function language (as the paper, l. 158, and 086 C1.2): the operator-level signs of CFL Def. 2.3 are not addressed.
- **C1** (a) $p^{\Omega}_{m,n}(B)=(-1)^{\abs B}\,p_{m,n}(B)$: the two families coincide on inputs of ghost number two (more generally of even total parity) for every number of outputs, and differ by a component-dependent sign on unrestricted inputs from one output on; l. 132 is wrong for the family l. 130 describes, and its "component-dependent from three outputs on" is wrong for either twist. [by C1.1–C1.4]
  - **C1.1** $\Omega_n(X,Y)=(-1)^{\abs X}\pair[n]XY$ on homogeneous $X$, and $p^{\Omega}_{m,n}=(-P)^{\otimes n}\,p_{m,n}$ componentwise; $p^{\Omega'}_{m,n}=P^{\otimes n}p_{m,n}$. [by A1, A4; eq. (088.1)–(088.2)] [check: C1.1, C1.1-break, C1-def]
  - **C1.2** $p^{\Omega}_{m,n}(B)=(-1)^{\abs B}p_{m,n}(B)$ and $p^{\Omega'}_{m,n}(B)=(-1)^{n+\abs B}p_{m,n}(B)$ on homogeneous inputs $B$. [by C1.1, A3; eq. (088.3)] [check: C1.1-input]
  - **C1.3** On ghost-two inputs $p^{\Omega}_{m,n}=p_{m,n}$ for every $n$; $p^{\Omega'}_{m,n}=(-1)^np_{m,n}$, an overall sign at each $n$, never component-dependent. [by C1.2; eq. (088.4)] [check: C1.2, C1.2-break]
  - **C1.4** On unrestricted superfields $p^{\Omega}_{m,n}(\Psi^m)=p_{m,n}((P\Psi)^m)\ne\pm p_{m,n}(\Psi^m)$, already at $n=1$; on ghost-two $\Psi$, $\ell^{\Omega}_m(\Psi^m)=+\ell_m(\Psi^m)$ and $p^{\Omega'}_{m,1}(\Psi^m)=-\ell_m(\Psi^m)$. [by C1.2, A2; eq. (088.5)] [check: C1.3, C1.3-superfield]
- **C2** (b) `eq:ibl:generating` holds verbatim for the sprod family $p_{m,n}$; for $p^{\Omega}_{m,n}$ it holds with $\Omega_n$ in place of $\pair[n]{\cdot}{\cdot}$, term by term equal to the first. [by C2.1–C2.3]
  - **C2.1** $\frac{1}{m!\,n!}\pair[n]{\Psi'^n}{p_{m,n}(\Psi^m)}$ is the bidegree-$(m,n)$ term of $S(\Psi+\Psi')$ at $\gs=1$, every $(m,n)$; this needs only that $\vertex{}$, $p$ and the pairing are extended to superfields by the same rule. [by A2, A3; eq. (088.6)–(088.7)] [check: C2.1, C2.1-break, C2.4]
  - **C2.2** $\frac{1}{m!\,n!}\Omega_n(\Psi'^n,p^{\Omega}_{m,n}(\Psi^m))$ is the same term. [by A4, C2.1] [check: C2.2]
  - **C2.3** The paper's formula with $p^{\Omega}$ inserted is $\vertex{m+n}(\Psi'^n,(P\Psi)^m)$: at $n=1$ not $\pm\vertex{m+1}(\Psi',\Psi^m)$ on unrestricted superfields; on ghost-two $\Psi$ it is $+\vertex{m+1}$ for $p^{\Omega}$ and $-\vertex{m+1}$ for $p^{\Omega'}$ (the critic's concern holds for the $\Omega'$ reading only). [by C1.4, C2.1; eq. (088.8)] [check: C2.3]
- **C3** (c) Read in a family's own form, a configuration of the polarized master equation is a composition of two products of that family, and the family enters only through the raising of the contracted strand: for $p^{\Omega}$ the relation at $(m,n)$ is $-E_{m,n}$ term by term (one overall sign, the same for all $(m,n)$); for the sprod family with plain composition every relation vanishes identically (mirror configurations enter with opposite signs). The theorem of l. 160 holds as stated for $p^{\Omega}$. [by C3.1–C3.4]
  - **C3.1** In family $F$'s own form, the composition at configuration $(k_1,\ell_1;k_2,\ell_2)$ is $\frac{1}{(k_1-1)!\,\ell_1!\,k_2!\,(\ell_2-1)!}\vertex{k_1+\ell_1}(\Psi'^{\ell_1},Z^F,\Psi^{k_1-1})$, $Z^F:=p^F_{k_2+\ell_2-1,1}(\Psi'^{\ell_2-1},\Psi^{k_2})$: only the one-output member $p^F_{\cdot,1}$, which raises the contracted strand, depends on $F$. [by A2, A3, A4; eq. (088.9)] [check: C3.0, C3.0-break — written in the fix pass 2026-10-04, not yet run]
  - **C3.2** $R^{\Omega}_{m,n}=-E_{m,n}$ and $R^{\Omega'}_{m,n}=+E_{m,n}$, configuration by configuration, every $(m,n)$. [by C1.1, C3.1, 086 (086.4), (086.8); eq. (088.10)–(088.11)] [check: C3.1, C3.1-prime, C3.1-break]
  - **C3.3** $R^{p}_{m,n}\equiv0$ for plain compositions of the sprod family, and $\mathcal C_\Delta(S(\Psi+\Psi'),S(\Psi+\Psi'))\equiv0$: a configuration and its mirror enter with opposite signs; a self-mirror configuration vanishes alone. The difference between the two readings inside a relation is a relative sign, not an overall one. [by C3.1, 086 (086.9) mirror map; eq. (088.12)] [check: C3.2, C3.2-break, C3.2-delta]
  - **C3.4** $R^{\Omega}_{m,n}=0$ for all $(m,n)$ iff the $\ell_n$ form a cyclic $L_\infty$ algebra; the same holds for the products $p_{m,n}$ joined by $\Omega^{-1}$ (the paper's (2,2) displays, l. 175–207), not for $p_{m,n}$ with plain composition, whose relations are empty. [by C3.2, C3.3, R31; paper l. 155] [check: C3.3]
- **C4** Replacement text for l. 128–141, 156, 160, 172, 205–206 and 228 (section *Replacement text*; l. 157 kept), restating C1.2, C1.4, C2, C3.2–C3.4 in the paper's notation, with $p^{\Omega}_{m,n}$ for the raised family. [by C1–C3] (Statement widened in the fix pass, critic iteration 1: before it, l. 128–141, 156–157, 160 and C1.2, C2, C3.2–C3.4.)

Open gaps: none
Hypotheses in force: none

## Derivation

### Block 1 — the two families compared (C1)

\subsection*{Setup}
A1, A3, A4. On basis inputs, $p_{m,n}(e_{b_1},\dots,e_{b_m})=p^{c_1\cdots c_n}{}_{b}\,e_{c_1}\otimes\cdots\otimes e_{c_n}$ with numerical components, and likewise $p^{\Omega}$; $V_{a_1\cdots a_nb_1\cdots b_m}:=\vertex{m+n}(e_{a_1},\dots,e_{b_m})$.

\subsection*{Derivation}
$$\Omega_n(e_{a_1}\otimes\cdots\otimes e_{a_n},e_{c_1}\otimes\cdots\otimes e_{c_n})=(-1)^{\sum_{i<j}\varepsilon_{c_i}\varepsilon_{a_j}}\prod_i(-1)^{\varepsilon_{a_i}}g_{a_ic_i}=(-1)^{\abs a}\,\pair[n]{e_a}{e_c}.\tag{088.1}$$
$$\pair[n]{e_a}{p(e_b)}=V_{ab}=\Omega_n(e_a,p^{\Omega}(e_b))=(-1)^{\abs a}\pair[n]{e_a}{p^{\Omega}(e_b)}\ \ \forall a\quad\Longrightarrow\quad (p^{\Omega})^{c}{}_b=(-1)^{n+\abs c}\,p^{c}{}_b=\Bigl(\textstyle\prod_i\bigl(-(-1)^{\varepsilon_{c_i}}\bigr)\Bigr)p^c{}_b.\tag{088.2}$$
$$V_{ab}\ne0\Rightarrow\abs a+\abs b=0,\qquad \abs c=\abs a+n\quad\Longrightarrow\quad(-1)^{n+\abs c}=(-1)^{\abs b}:\qquad \boxed{p^{\Omega}_{m,n}(B)=(-1)^{\abs B}\,p_{m,n}(B)}.\tag{088.3}$$
$$\abs B=0\ \text{(ghost-two inputs)}:\quad p^{\Omega}_{m,n}=p_{m,n}\ \ \forall n;\qquad \Omega'_n=(-1)^n\Omega_n\ \Rightarrow\ p^{\Omega'}_{m,n}(B)=(-1)^{n+\abs B}p_{m,n}(B)\ \to\ (-1)^n.\tag{088.4}$$
$$p^{\Omega}_{m,n}(\Psi^m)=\sum_b(\pm)_K\,\Psi^{b_1}\cdots\Psi^{b_m}(-1)^{\varepsilon_{b_1}+\cdots+\varepsilon_{b_m}}p_{m,n}(e_b)=p_{m,n}\bigl((P\Psi)^m\bigr),\qquad P\Psi=\textstyle\sum_a(-1)^{\varepsilon_a}\Psi^ae_a.\tag{088.5}$$

\subsection*{Commentary}
(088.1): $\Omega_{ac}=(-1)^{\varepsilon_a}g_{ac}$; the Koszul factor is the one of `eq:conv:pairing-n` (A4). This is the conventions ledger's $\Omega_k=(-1)^{\epsilon(X)}\omega_k$ (C1, bullet *The BV odd symplectic form*).
(088.2): both definitions on the same basis tensor $e_a$; nondegeneracy of $\pair[n]{\cdot}{\cdot}$ on each component. On the support each strand pairs opposite parities, $\varepsilon_{a_i}=\varepsilon_{c_i}+1$, so $\abs a=\abs c+n$. The per-strand factor $-(-1)^{\varepsilon_{c_i}}=(-1)^{\varepsilon_{a_i}}$ is $-1$ exactly when the slot $a_i$ of the vertex holds an odd state — the sign of l. 130, $(\Omega^{-1})^{ca}=g^{ca}(-1)^{\varepsilon_a}$, read on the vertex slot.
(088.3): the vertices are even (A3), so the total parity of the outputs is fixed by that of the inputs. The ratio is a function of the input parity alone: it never distinguishes components with the same input parity.
(088.4): $\Omega'(A,B):=(-1)^{\abs B}\pair AB=-\Omega(A,B)$ on the support (paper l. 344). The $\Omega'$ pattern $-,+,-$ at $n=1,2,3$ on ghost-two inputs is what l. 132 states for $n=1,2$; at $n=3$ it is again an overall sign. A component-dependent sign on ghost-two inputs would need a Koszul rule for the $n$-fold form other than that of `eq:conv:pairing-n`; the paper has none.
(088.5): rule K signs depend only on the parities of coefficients and basis vectors, which $P$ does not change; the factor $(-1)^{\varepsilon_b}$ of each input component is absorbed into $P\Psi$. For $\Psi$ with components of both parities $P\Psi\ne\pm\Psi$, so $p^{\Omega}(\Psi^m)\ne\pm p(\Psi^m)$; on ghost-two $\Psi$, $P\Psi=\Psi$.

\subsection*{Result}
The $\Omega^{-1}$-raised family is the sprod family precomposed with the parity of the inputs, (088.3). The two coincide on every input of even total parity (in particular on $\Psi$ and $\Sigma_k$, hence on every product the action applies to its fields), for every number of outputs, and differ by $-1$ on inputs of odd total parity (e.g. one gauge parameter $\Lambda$ among even fields); on a superfield of unrestricted ghost number the sign varies from component to component. l. 132 is wrong on both counts for the family l. 130 defines; under the opposite twist it is right at $n=1,2$ and wrong at $n\ge3$.

\subsection*{Verification}
`C1.1`: families built by raising every leg with the inverse matrix of $g$, $\Omega$, $-\Omega$ (not from the claimed formula); ratio $(-P)^{\otimes n}$ resp. $P^{\otimes n}$ on every component, $(m,n)$ with $m+n\le4$, $n\ge1$; `C1.1-break` ($P^{\otimes n}$ for $p^{\Omega}$) fails. `C1-def`: each family satisfies its defining relation. `C1.1-input`: (088.3) and its $\Omega'$ form on every component. `C1.2`: ratio set on ghost-two inputs $\{+1\}$ for $p^{\Omega}$ at $(m,n)\in\{(1,1),(2,1),(1,2),(3,1),(2,2),(1,3)\}$, $\{(-1)^n\}$ for $\Omega'$; `C1.2-break`. `C1.3`: both signs at $n=1$ on unrestricted inputs, $m=1,2,3$. `C1.3-superfield`: (088.5) consequences on superfields.

### Block 2 — the generating function (C2)

\subsection*{Setup}
A2, A3, A4, Block 1. $\gs=1$ (it only multiplies each bidegree).

\subsection*{Derivation}
$$S(\Psi+\Psi')=\sum_{N\ge2}\frac1{N!}\vertex N\bigl((\Psi+\Psi')^N\bigr)=\sum_{\substack{m+n\ge2}}\frac{1}{m!\,n!}\,\vertex{m+n}(\Psi'^n,\Psi^m).\tag{088.6}$$
$$\vertex{m+n}(\Psi'^n,\Psi^m)=\pair[n]{\Psi'^n}{p_{m,n}(\Psi^m)}=\Omega_n\bigl(\Psi'^n,p^{\Omega}_{m,n}(\Psi^m)\bigr).\tag{088.7}$$
$$\pair[n]{\Psi'^n}{p^{\Omega}_{m,n}(\Psi^m)}=\pair[n]{\Psi'^n}{p_{m,n}((P\Psi)^m)}=\vertex{m+n}\bigl(\Psi'^n,(P\Psi)^m\bigr).\tag{088.8}$$

\subsection*{Commentary}
(088.6): multilinearity and graded symmetry; $\Psi,\Psi'$ even superfields commute with everything, so the binomial coefficients are the plain ones.
(088.7): `eq:conv:sprod` resp. A4 read on superfields. With rule K the coefficient signs on the two sides coincide: on the left, each $\Psi'$ coefficient passes the earlier $e_a$, each $\Psi$ coefficient passes all $e_a$ and the earlier $e_b$; on the right, the first two come from $\Psi'^{\otimes n}$ and $p(\Psi^m)$, the passage of the $\Psi$ coefficients past all $e_a$ from the rule-K sign of the pairing. The same holds for any coefficient rule applied to all three objects (check `C2.4` with no Koszul signs at all). The second equality is (088.1)–(088.2).
(088.8): (088.5). At $n=1$, $\vertex{m+1}(\Psi',(P\Psi)^m)$ is not $\pm\vertex{m+1}(\Psi',\Psi^m)$ for unrestricted $\Psi$; for ghost-two $\Psi$ it is $+\vertex{m+1}$. With $p^{\Omega'}$ instead it is $(-1)^n\vertex{m+n}(\Psi'^n,(P\Psi)^m)$, i.e. $-\vertex{m+1}$ at $n=1$ on ghost-two $\Psi$: the critic's reading.

\subsection*{Result}
`eq:ibl:generating` as written holds, verbatim and term by term, for the family of `eq:conv:sprod`; l. 140's $\sprod11=Q_B$ is that family's ($p^{\Omega}_{1,1}(B)=(-1)^{\abs B}Q_BB$). For the $\Omega^{-1}$-raised family the generating function holds with $\Omega_n$, each term equal to the corresponding term of the paper's form. Inserting $p^{\Omega}$ into the paper's formula is wrong on unrestricted fields.

\subsection*{Verification}
`C2.1` (12 bidegrees $m+n\le4$, $n=0,\dots,4$, all terms nonzero; also equal to 086's `H(m,n)`), `C2.1-break` (sprod family read through $\Omega_1$ misses), `C2.2` ($p^{\Omega}$ with $\Omega_n$, $p^{\Omega'}$ with $\Omega'_n$), `C2.3` ((088.8) at $n=1$, $m=1,2,3$), `C2.4` (rule independence of C2.1).

### Block 3 — where the raising enters the relations (C3)

\subsection*{Setup}
A2–A4, Blocks 1–2; record 086 (086.2)–(086.9): for a configuration $t=(k_1,\ell_1;k_2,\ell_2)$, $k_1+k_2-1=m$, $\ell_1+\ell_2-1=n$, $\mathcal C(H_{k_1,\ell_1},H_{k_2,\ell_2})=\Omega(L_1,L_2)$ with odd superfields $L_1=\ell(\Psi^{k_1-1},\Psi'^{\ell_1})/((k_1-1)!\,\ell_1!)$, $L_2=\ell(\Psi^{k_2},\Psi'^{\ell_2-1})/(k_2!\,(\ell_2-1)!)$, symmetric in $L_1,L_2$; the mirror $\bar t=(k_2+1,\ell_2-1;k_1-1,\ell_1+1)$ exchanges $L_1$ and $L_2$. For odd superfields with rule K, $\pair LK=(-1)^{\varepsilon_c}g_{cd}L^cK^d$ (one of $L^c,K^d$ even on the support, $\abs{K^d}=\varepsilon_c$).

\subsection*{Derivation}
Composition of two products of a family $F$ (form $F_n$, one-output member $p^F_{K,1}$), read in $F$'s own form:
$$F_{\ell_2}\bigl(A\otimes\Psi'^{\ell_2-1},p^F_{k_2,\ell_2}(\Psi^{k_2})\bigr)=\vertex{k_2+\ell_2}(A,\Psi'^{\ell_2-1},\Psi^{k_2})=F_1(A,Z^F),\qquad Z^F=p^F_{k_2+\ell_2-1,1}(\Psi'^{\ell_2-1},\Psi^{k_2}),$$
$$R^F(t):=\frac{1}{(k_1-1)!\,\ell_1!\,k_2!\,(\ell_2-1)!}\,F_{\ell_1}\bigl(\Psi'^{\ell_1},p^F_{k_1,\ell_1}(Z^F,\Psi^{k_1-1})\bigr)=\frac{\vertex{k_1+\ell_1}(\Psi'^{\ell_1},Z^F,\Psi^{k_1-1})}{(k_1-1)!\,\ell_1!\,k_2!\,(\ell_2-1)!}.\tag{088.9}$$
$$F=p^{\Omega}:\quad Z=-PL_2\ (\text{up to the factorials}),\quad R^{\Omega}(t)=\pair{-PL_2}{L_1}=-g_{cd}L_2^cL_1^d=-\Omega(L_2,L_1)=-\mathcal C(H_{k_1,\ell_1},H_{k_2,\ell_2}).\tag{088.10}$$
$$F=p^{\Omega'}:\quad Z=+PL_2,\qquad R^{\Omega'}(t)=+\mathcal C(H_{k_1,\ell_1},H_{k_2,\ell_2}).\tag{088.11}$$
$$F=p:\quad Z=L_2,\qquad R^{p}(t)=\pair{L_2}{L_1}=-\pair{L_1}{L_2}=-R^{p}(\bar t)\quad\Longrightarrow\quad \sum_tR^p(t)=0;\qquad \mathcal C_\Delta(H_1,H_2)=\pair{L_1}{L_2}.\tag{088.12}$$
$$\boxed{\;R^{\Omega}_{m,n}=-E_{m,n},\qquad R^{\Omega'}_{m,n}=E_{m,n},\qquad R^{p}_{m,n}\equiv0\equiv E^{\Delta}_{m,n}.\;}$$

\subsection*{Commentary}
(088.9): first line, the defining relation of the family with the slots reordered by graded symmetry ($\Psi,\Psi'$ even), and the factorisation of $F_{\ell_2}$ into $F_1\otimes F_{\ell_2-1}$ with no Koszul sign because $\Psi'^{\ell_2-1}$ is even: pairing the other output strands with $\Psi'$ frees the contracted strand as the superfield $Z^F$. Second line, the same with the outputs of the receiving product paired with $\Psi'^{\ell_1}$. The factorials are those of $\mathcal C(H_{k_1,\ell_1},H_{k_2,\ell_2})$ (086.5): one $\Psi$ removed from $H_{k_1,\ell_1}$, one $\Psi'$ from $H_{k_2,\ell_2}$. Every strand other than the contracted one is read through $F$'s own form and gives back the vertex; the family survives only in $Z^F$, the raising of the contracted strand. This is the generating-function reading of "composition" (A4).
(088.10): $\ell^{\Omega}=-P\ell$ by (088.2) at $n=1$, componentwise on superfields (rule K signs unchanged by $P$). $\vertex{}(\Psi'^{\ell_1},Z,\Psi^{k_1-1})=\vertex{}(Z,\Psi'^{\ell_1},\Psi^{k_1-1})=\pair{Z}{\ell(\Psi'^{\ell_1},\Psi^{k_1-1})}$ by graded symmetry and `eq:conv:vertex` read with rule K (the first slot's coefficient passes nothing). $\pair{PL}{K}=g_{cd}L^cK^d=\Omega(L,K)$ by the formula in the Setup and (086.4); then (086.8).
(088.12): $\pair KL=(-1)^{\varepsilon_d}g_{cd}L^cK^d=-\pair LK$ since $\varepsilon_d=\varepsilon_c+1$. The mirror map is an involution of the set of configurations at fixed $(m,n)$ (086 (086.9) commentary: $k_1\ge1$, $\ell_2\ge1$ are preserved), so the sum vanishes; a self-mirror configuration ($L_1=L_2$, e.g. $T_4$ at $(2,2)$, or the single configuration at $(0,2)$, $\Omega(Q_B\Psi',Q_B\Psi')$) vanishes alone. $\mathcal C_\Delta$: (086.1)–(086.3) with $g^{ab}$ for $(\Omega^{-1})^{ab}$ give $(-1)^{\varepsilon_c}g_{cd}L_1^cL_2^d$; this is 086's `C2.2-break`, now at every bidegree.
**Overall versus relative.** In (088.10) the factor $-1$ is common to every configuration and every $(m,n)$: it does not change a relation that vanishes. Between $p^{\Omega}$ and $p$, by contrast, the difference sits on the contracted strand, an input of the receiving product whose parity varies from component to component (088.3); summed over configurations it turns the mirror-symmetric $E$ into the mirror-antisymmetric, identically vanishing $R^p$. It is a relative sign.

\subsection*{Result}
Read through $\Omega_n$, the $(m,n)$ part of `eq:ibl:polarized-master` is minus the sum of the compositions of two products of $p^{\Omega}$ through one strand, each ordered configuration once: the relations of l. 157 for the family of l. 160. Read through the paper's form of `eq:ibl:generating`, the same scalar relation joins the products $p_{m,n}$ through $\Omega^{-1}$ — which is how l. 175–207 write the $(2,2)$ configurations, $T_i=\Omega(\cdot,\cdot)$ of $\ell$-outputs. With $\Delta$ on the joined strand every relation is empty. By R31 and the paper's l. 155 ($E\equiv0$ iff cyclic $L_\infty$), the theorem of l. 160 holds as stated for $p^{\Omega}$.

\subsection*{Verification}
`C3.0` (node C3.1, added in the fix pass, **written, not yet run**): both sides of (088.9) for $F\in\{p,p^{\Omega},p^{\Omega'}\}$. First line: the freed strand of the $\ell_2$-output member read through $F_{\ell_2}$ against $F_1(e_a,Z^F)$ from the one-output member and against $V$, on every basis state $e_a$. Second line: the receiving member applied to the odd superfield $Z^F$ and read through $F_{\ell_1}$ against $V(\Psi'^{\ell_1},Z^F,\Psi^{k_1-1})$, at every configuration with $\ell_1\ge2$ or $\ell_2\ge2$. Non-hollow at $\ell_2\ge2$ and $\ell_1\ge2$. `C3.0-break` perturbs the computation: the sprod strand, and separately the sprod receiving member, read in the $\Omega$ form. Before the fix pass, C3.1 had no check: `C3.1` below evaluates only the right-hand side of (088.9) (critic #13).
`C3.1` ($R^{\Omega}_{m,n}=-E_{m,n}$) and `C3.1-prime` ($R^{\Omega'}=+E$) at all 25 bidegrees $m+n=2,\dots,6$ of generic data ($E$ from 086's contraction of $S(\Psi+\Psi')$ with numerically inverted $\Omega$ and right/left derivatives from monomial order; $R$ from the right-hand side of (088.9), with $Z^F$ from explicitly raised one-output components and rule-K vertex evaluation — independent paths); `C3.1-break` ($+E$ fails). `C3.2`: $R^p\equiv0$ at every bidegree, with at least two nonzero terms wherever $E$ has two, the lone self-mirror term vanishing at $(0,2)$, $(2,0)$, $(0,6)$, $(6,0)$; `C3.2-break` (drop one term: nonzero); `C3.2-delta` ($E$ with $g^{-1}$: identically $0$, while $\abs E=19796/9$ with $\Omega^{-1}$). `C3.3`: $\mathfrak{sl}_2\oplus\mathfrak{sl}_2^*$ (cyclic dg Lie): $E=0$, $R^{\Omega}=0$; Jacobi-violating variant: $E\ne0$ ($\abs E=128$), $R^{\Omega}=-E$; $R^p=0$ on both — the plain-composition relations of the sprod family cannot detect the failure.

## Verification

Script `codes/verify-ibl-generating-sign.py` (engine imported from `codes/verify-paper-gap-7.py`, not edited), seed 20261004, run 2026-10-04 with `.venv/bin/python` from the project root, ~4 s:

```text
[PASS] C1.1: pO = (-P)^n p and pO' = P^n p on every component, (m,n) in [(1, 1), (0, 2), (2, 1), (1, 2), (0, 3), (3, 1), (2, 2), (1, 3), (0, 4)]
[PASS] C1.1-break: pO = P^n p (wrong twist) fails somewhere (expected)
[PASS] C1.1-input: pO_{m,n}(B) = (-1)^{|B|} p_{m,n}(B), pO' = (-1)^{n+|B|} p, every component
[PASS] C1-def: each family satisfies its defining relation on basis states
[PASS] C1.2: ghost-two inputs: pO/p = +1 for n = 1,2,3; pO'/p = (-1)^n, one value each
[PASS] C1.2-break: claim 'pO = -l at one output on ghost-two inputs' fails (expected)
[PASS] C1.3: unrestricted inputs: pO/p takes both signs at n = 1, m = 1,2,3
[PASS] C1.3-superfield: pO_{m,1}(Psi^m) != +-l_m(Psi^m) generic; ghost-two Psi: pO = +l, pO' = -l
[PASS] C2.1: sprod family in <.,.>_n reproduces every term of S(Psi+Psi'), [12 bidegrees m+n<=4]
[PASS] C2.1-break: sprod family read through Omega_1 misses V (expected)
[PASS] C2.2: Omega family in Omega_n, Omega' family in Omega'_n: same terms
[PASS] C2.3: Omega family in the paper's formula: n=1 terms != +-V generic; ghost-two Psi: +V (Omega), -V (Omega')
[PASS] C2.4: naive rule (no Koszul signs) applied uniformly: C2.1 still holds
[PASS] C3.1: R^Omega_{m,n} == -E_{m,n} at every bidegree (generic data)
[PASS] C3.1-prime: R^Omega'_{m,n} == +E_{m,n} at every bidegree
[PASS] C3.1-break: R^Omega == +E fails where E != 0 (expected)
[PASS] C3.2: R^sprod_{m,n} == 0 identically (plain composition, Delta on the strand); >= 2 nonzero terms where E has >= 2, the lone self-mirror term vanishes
[PASS] C3.2-break: dropping one term of R^sprod leaves it nonzero
[PASS] C3.2-delta: polarized master equation contracted with Delta = g^{-1}: identically 0, all bidegrees (with Omega^{-1}: |E| = 19796/9)
[PASS] C3.3: sl2: E = R^O = 0; Jacobi-violating: |E| = 128, R^O = -E, R^sprod = 0 on both
summary: 20/20 PASS (seed 20261004)
```

Full output in `agent/scratch/computator/computator-088-ibl-generating-sign-20261004T153600/run.txt`.
**Fix pass (2026-10-04, text only, script not run).** The output above is the pre-fix run. Two changes since then. Check `C3.0` and `C3.0-break` (node C3.1, critic #13) are new, written and not yet run: the script now has 22 checks, and its next run should print `22/22 PASS` with both new lines before `C3.1`. The docstring now gives, for every check label, the node it tests (critic #14). The labels are not node IDs, and the brackets agree with the tree's tags. The labels are kept, so the quoted output stays valid; renaming them to node IDs would mean re-running the script.

**Orchestrator run (2026-10-04 16:37, after the fix pass).** `.venv/bin/python codes/verify-ibl-generating-sign.py`, single process, one thread: **22/22 PASS** (seed 20261004), `C3.0` and `C3.0-break` included and passing; the 20 earlier checks unchanged; 7 s wall clock, 18 MB peak; log `agent/scratch/orchestrator/verify-ibl-generating-sign-20261004T1637.log`; `ruff format` leaves the script unchanged. The "written, not yet run" tags on `C3.0` above and in the fix-pass section refer to the state before this run.
Label → node: `C1.1`, `C1.1-break`, `C1-def` → C1.1; `C1.1-input` → C1.2; `C1.2`, `C1.2-break` → C1.3; `C1.3`, `C1.3-superfield` → C1.4; `C2.1`, `C2.1-break`, `C2.4` → C2.1; `C2.2` → C2.2; `C2.3` → C2.3; `C3.0`, `C3.0-break` → C3.1; `C3.1`, `C3.1-prime`, `C3.1-break` → C3.2; `C3.2`, `C3.2-break`, `C3.2-delta` → C3.3; `C3.3` → C3.4.
The `-break` legs `C1.1-break`, `C1.2-break`, `C2.1-break` and `C3.1-break` check that the negation of the claim fails on the data. They are non-hollowness checks, not perturbations of the computation (critic #12). `C3.2-break` and `C3.0-break` are perturbations.
One failure during development: `C3.2` first required two nonzero $R^p$ terms wherever $E\ne0$; it failed at $(0,2)$, $(2,0)$, $(0,6)$, $(6,0)$, where the only configuration is self-mirror and its $\Delta$-term vanishes alone, as (088.12) predicts. Diagnosis: the check's criterion was wrong, not the result ($R^p=0$ held at every bidegree); criterion corrected.
Model: ghost numbers $(1,2,2,3,3,4)$, random graded-symmetric $\vertex2,\vertex3,\vertex4$ over $\mathbb Q$ not satisfying the master equation (086's `generic_model`). Not checked: rule dependence of C3 (rule K only); closed-string vertices; CFL operator-level signs.

## Replacement text

For transcription into `paper/sections/07-ibl.tex` (revised in the fix pass, critic iteration 1). Notation: $p^{\Omega}_{m,n}$, written `p^{\Omega}_{m, n}`, for the raised family; a separate symbol is needed because the two families differ on odd inputs. The hat is taken: 07-ibl l. 228–232 define $\hat p_{m,n}$ as the extension of $\sprod{m}{n}$ to the symmetric algebra, and the hat marks multi-string extensions ($\hat Q_B$, 07-ibl l. 98, 99, 234). Grep of `paper/sections/` (2026-10-04 16:14): no `p^{\Omega}`, `p^\Omega`, `\tilde p` or `\Omega_n` in use; `\hat{p}` only at 07-ibl l. 228, 232. `\abs`, `\pair`, `\Hn`, `\sprod`, `\vertex`, `\gs`, `\IBL`, `\Loo` are the paper's macros.

### Replaces l. 128–141 (from "and iterating produces" to "background $\Psi'$.")

```latex
and iterating produces every $\sprod{m}{n}$ from the $\ell_n$ alone.
This is the content of the definition~\eqref{eq:conv:sprod}: reading $n$ slots of $\vertex{m+n}$ through the $n$-string pairing is raising $n$ indices with $\Delta$.
The raising that closes the antibracket uses instead the inverse of the odd symplectic form $\Omega$ of~\eqref{eq:conv:odd-symplectic}, which differs from $\Delta$ by a sign $-1$ on every slot of the vertex that holds an odd state.
Raising every slot in this way defines the family $p^{\Omega}_{m, n}$,
\begin{equation}
  \label{eq:ibl:raised-family}
  \vertex{m+n}(A_1, \ldots, A_n, B_1, \ldots, B_m)
    =: \Omega_n \bigl( A_1 \otimes \cdots \otimes A_n, p^{\Omega}_{m, n}(B_1, \ldots, B_m) \bigr),
\end{equation}
where, for $X$ of definite parity, $\Omega_n(X, Y) := (-1)^{\abs{X}} \, \pair[n]{X}{Y}$, extended by linearity, which we take as the $n$-th tensor power of $\Omega$, with the Koszul sign of~\eqref{eq:conv:pairing-n}.
Here $\abs{X}$ is the parity of the states, not of their coefficients, so that on a string field of unrestricted ghost number the sign acts component by component.
The relations below are written for this family.
Since the pairing joins states of opposite parity and the vertices are even, it differs from the family of~\eqref{eq:conv:sprod} by the parity of the inputs,
\begin{equation}
  \label{eq:ibl:raised-vs-sprod}
  p^{\Omega}_{m, n}(B_1, \ldots, B_m)
    = (-1)^{\abs{B_1} + \cdots + \abs{B_m}} \, \sprod{m}{n}(B_1, \ldots, B_m).
\end{equation}
The two families coincide on inputs whose states have even total parity, whatever the number of outputs, in particular on the classical fields $\Psi$ and $\Sigma_k$, whose states all have even ghost number; on inputs of odd total parity, such as a single gauge parameter, they differ by a sign, already for one output.
On the string fields of unrestricted ghost number used below, whose components carry both parities, the sign changes from component to component, and the two families are different maps.
We include in the family the vertices themselves, $p^{\Omega}_{m, 0} = \sprod{m}{0} = \vertex{m}$, read with no output, and the fully raised vertices $p^{\Omega}_{0, n} = \sprod{0}{n} \in \Hn{n}$, with no input.
The whole family is encoded in the action evaluated at the sum of two fields $\Psi$ and $\Psi'$,
\begin{equation}
  \label{eq:ibl:generating}
  \begin{aligned}
    S(\Psi + \Psi')
      &
      = \sum_{\substack{m, n \ge 0 \\ m + n \ge 2}} \frac{\gs^{m+n-2}}{m! \, n!} \, \Omega_n \bigl( \Psi'^n, p^{\Omega}_{m, n}(\Psi^m) \bigr)
    \\
      &
      = \sum_{\substack{m, n \ge 0 \\ m + n \ge 2}} \frac{\gs^{m+n-2}}{m! \, n!} \, \pair[n]{\Psi'^n}{\sprod{m}{n}(\Psi^m)},
  \end{aligned}
\end{equation}
where each family is read through its own form and the two sums agree term by term, each term being $\tfrac{\gs^{m+n-2}}{m! \, n!} \, \vertex{m+n}(\Psi'^n, \Psi^m)$.
Here the terms with $n = 0$ are the vertices, $\tfrac{\gs^{m-2}}{m!} \, \vertex{m}(\Psi^m)$, those with $m = 0$ are $\tfrac{\gs^{n-2}}{n!} \, \vertex{n}(\Psi'^n)$, and the three terms with $m + n = 2$ are built from $\vertex{2}(A, B) = \pair{A}{Q_B B}$, with $\sprod{1}{1} = Q_B$.
Up to the factor $\gs^{m+n-2} / n!$, the product $\sprod{m}{n}$ is the $m$-th derivative at $\Psi = 0$ of the term of order $n$ in $\Psi'$, and the sum of these terms over $n$ is the $m$-point function in the background $\Psi'$.
```

Changes against the current text: l. 130 made precise (the sign sits on the vertex slot, which is what $(\Omega^{-1})^{ab}$ in `eq:ibl:polarized-master` does to slot $b$); l. 131–132 replaced by the definition `eq:ibl:raised-family` and the comparison `eq:ibl:raised-vs-sprod`; l. 133 names both families; `eq:ibl:generating` gains the $\Omega_n$ form (as a two-line `aligned`) and a sentence; l. 140–141 unchanged. Fix pass: symbol $p^{\Omega}$ (#7); componentwise reading of $\Omega_n$ and "which we take as" the tensor power (#8, #9); the comparison sentence restricted to the classical fields and followed by the statement for unrestricted fields (#2). The pre-fix version was compiled with stub macros in `agent/scratch/computator/computator-088-ibl-generating-sign-20261004T153600/test-replacement.tex`; the revised text is not compiled (text-only pass).

### Replaces l. 156 (keeps l. 157–158)

```latex
Sorting~\eqref{eq:ibl:polarized-master} by the degrees $(m, n)$ in $(\Psi, \Psi')$ gives one relation per pair $(m, n)$.
In each of its terms the derivative with respect to $\Psi'$ frees an output strand of one product, $\Omega^{-1}$ carries it into an input of another product, freed by the derivative with respect to $\Psi$, and the remaining strands stay paired with $\Psi'$.
Read through the first form of~\eqref{eq:ibl:generating}, the strand enters the second product as the output of the first, since $\Omega^{-1}$ inverts $\Omega$, and the relation at $(m, n)$ is, up to an overall sign common to all $(m, n)$, the sum of the compositions of two products of the family $p^{\Omega}_{m, n}$.
Read through the second form, the same relation joins the products $\sprod{m}{n}$ by $\Omega^{-1}$, which is how the configurations are written below.
With $\Delta$ in place of $\Omega^{-1}$, a configuration and its mirror image, in which the two products exchange their roles, would enter with opposite signs, and every relation would hold identically.
```

l. 157 ("The relation at $(m, n)$ states that the sum over all ways of composing two products of the family …") then reads correctly for $p^{\Omega}$ and is kept.

### Replaces the statement at l. 160

```latex
We thus have: \emph{the family $p^{\Omega}_{m, n}$ obtained from the vertices by raising every index with $\Omega^{-1}$, with $m + n \ge 2$, satisfies the genus-zero \IBL{} relations at every $(m, n)$ if and only if the products $\ell_n$ form a cyclic $\Loo$ algebra, in the standard Koszul convention for the odd maps $\ell_n$.}
```

The symbol and the final clause are added; the statement was correct. The clause (critic #11) fixes what "$\Loo$ algebra" means once two extensions to Grassmann coefficients are in play: the rule of l. 204 (rule K) gives an odd map no sign when it passes a coefficient, the standard Koszul extension gives it $(-1)^{\abs\lambda}$, and at one output the two differ by $(-1)^{\abs B}$ on the inputs, which is (088.3). Hence $\ell^{\Omega}$ under rule K is $\ell$ under the Koszul extension, and the relations of the $\ell_n$ that the master equation is equivalent to (l. 145) are the standard ones; a reader testing them under rule K would find a mismatch on odd inputs.

### Replaces l. 172 (fix pass, critic #5)

```latex
At $(1, n)$ they are the relations among the operations with one input, which at $(1, 2)$ state that $p^{\Omega}_{1, 1}$ and the cobracket $p^{\Omega}_{1, 2}$, equal to $Q_B$ and $\sprod{1}{2}$ on inputs of even parity, are compatible.
```

At $(1,2)$ the operations of the family are $p^{\Omega}_{1,1}=Q_B(-1)^{N_{\rm gh}}$ and $p^{\Omega}_{1,2}$, equal to $Q_B$ and $\sprod{1}{2}$ on inputs of even parity by `eq:ibl:raised-vs-sprod`; the relation itself involves odd inputs. The old wording named the sprod members, which the replacement now distinguishes from the family's.

### Replaces l. 205–206 (fix pass, critic #3)

l. 206 is a single sentence, so "l. 205 and the first sentence of l. 206" is the two lines whole.

```latex
The four terms are the configurations in which an output of $\sprod{2}{2}$ enters $Q_B$, an output of $Q_B$ enters $\sprod{2}{2}$, an output of $\ell_2$ enters $\sprod{1}{2}$ and an output of $\sprod{1}{2}$ enters $\ell_2$, the joined strand being raised with $\Omega^{-1}$, each written as the pairing of the two products joined by the contracted strand.
In~\eqref{eq:ibl:polarized-master} each of $T_1$, $T_2$, $T_3$ also appears with the roles of the two products exchanged, an output of $\sprod{0}{2}$ entering $\ell_3$, of $\sprod{1}{3}$ entering $\sprod{2}{0}$ and of $\sprod{0}{3}$ entering $\sprod{3}{0}$, with the same value, whereas $T_4$ is its own mirror image and appears once.
```

Directions checked against record 086's labelling ($L_1$ from the receiving product $(k_1,\ell_1)$, $L_2$ from the supplying product $(k_2,\ell_2)$, $\mathcal C(H_{k_1,\ell_1},H_{k_2,\ell_2})=\Omega(L_1,L_2)$, mirror $\bar t=(k_2+1,\ell_2-1;k_1-1,\ell_1+1)$), on the four displays of `eq:ibl:configurations-22`:
- $T_1=\tfrac12\Omega(Q_B\Psi',\ell_3(\Psi,\Psi,\Psi'))$: $t=(1,1;2,2)$, $\sprod22$ supplies, $Q_B$ receives; mirror $(3,1;0,2)$: $\sprod02$ supplies, $\ell_3$ receives.
- $T_2=\tfrac12\Omega(\ell_3(\Psi,\Psi',\Psi'),Q_B\Psi)$: $t=(2,2;1,1)$, $Q_B$ supplies, $\sprod22$ receives; mirror $(2,0;1,3)$: $\sprod13$ supplies, $\sprod20$ receives.
- $T_3=\tfrac14\Omega(\ell_2(\Psi',\Psi'),\ell_2(\Psi,\Psi))$: $t=(1,2;2,1)$, $\ell_2$ supplies, $\sprod12$ receives; mirror $(3,0;0,3)$: $\sprod03$ supplies, $\sprod30$ receives.
- $T_4=\Omega(\ell_2(\Psi,\Psi'),\ell_2(\Psi,\Psi'))$: $t=(2,1;1,2)$, $\sprod12$ supplies, $\ell_2$ receives; self-mirror.

All twelve product names and directions match the supplied text. "With the same value" holds because the joined strand is raised with $\Omega^{-1}$ (C3, $\mathcal C$ symmetric under $L_1\leftrightarrow L_2$); with plain composition ($\Delta$) the mirror would enter with the opposite sign (088.12). The old text read "the compositions $Q_B\circ\sprod22$, …": once $\sprod{m}{n}$ is unambiguously the family of `eq:conv:sprod` and $\circ$ plain composition (appendix A; 07-ibl l. 126), those are the $R^p$ terms, and "with the same value" at l. 206 contradicts the new l. 156. The replacement removes $\circ$ and "compositions" from the two lines.

### Replaces l. 228 (fix pass, critic #10)

```latex
Extending each $\sprod{m}{n}$ of~\eqref{eq:conv:sprod} to an operator $\hat{p}_{m, n}$ on the symmetric algebra, as for an \IBL{} algebra, and summing them with a formal parameter,
```

Only "of~\eqref{eq:conv:sprod}" is added. The family extended in the converse direction is the sprod family, and it must be, for four reasons:
- After the replacement, `\sprod{m}{n}` at l. 228 names that family explicitly, and the components l. 234 names, $\hat Q_B$ (the extension of $\sprod11=Q_B$) and $\sprod{2}{2}$, are its members.
- l. 252–253 reduce the criterion `eq:ibl:brace-criterion`, at leading order in $\hbar$ and on single-output components, to "the theorem above". In the brace setting, $\mathcal D$ is a differential operator on a graded-commutative algebra and $a$ an even element with auxiliary Grassmann parameters, so the one-output relations come out in the standard Koszul convention. Those are the $L_\infty$ relations of $\pm\ell_n$, i.e. the right-hand side of the theorem (with the #11 clause). For the raised family's one-output member $\ell^{\Omega}_n(B)=(-1)^{\abs B}\ell_n(B)$ they are different relations. At $n=2$, with $x$ even and $y$ odd, the Koszul relation of $\ell^{\Omega}$ is $-[Q_B\ell_2(x,y)-\ell_2(Q_Bx,y)+\ell_2(x,Q_By)]$, while that of $\ell$ is $Q_B\ell_2(x,y)+\ell_2(Q_Bx,y)+\ell_2(x,Q_By)$; the two differ by $2\ell_2(Q_Bx,y)$, so the first fails on a cyclic $L_\infty$ algebra with $\ell_2(Q_Bx,y)\ne0$. By hand, this pass; not machine-checked.
- Record 026's family, the setting of R31 and R32, is (026 (1.6), (8.1)–(8.6)) $\tilde\Delta$-raised with $\tilde\Delta^{ab}=(-1)^{\varepsilon_a}\Delta_{026}^{ab}$ and $\Delta_{026}=\omega_1^{-1}$. Here $\omega_1$ is graded antisymmetric and has the support of $g$, so it is $\pm\Omega$ up to normalisation: an antisymmetric form $f(\varepsilon_a,\varepsilon_b)\,g_{ab}$ on a support with $\varepsilon_a+\varepsilon_b=1$ needs $f=\pm(-1)^{\varepsilon_a}$. Hence $\tilde\Delta\propto\mp\Delta$ of the paper, and 026's one-output member $\tilde\Delta\circ V_{n+1}$ is the paper's $\ell_n$ up to an overall constant, which is what 026 §5′.5 (W6) checked to arity 3. At two or more outputs 026's convention (1.6) differs from `eq:conv:sprod` by its interleaving sign (026 (8.9)), but there the paper claims only the exclusion of l. 256. That exclusion covers slot-uniform raising maps of definite parity, $\Delta$ and $\Omega^{-1}$ alike.
- The criterion itself (Theorem B′, R32) holds for any finite-order differential operator and does not depend on the family.

The clause is therefore optional. It prevents the reading, natural after the theorem of l. 160, that the converse extends $p^{\Omega}_{m,n}$. Not added: a clause "rather than $p^{\Omega}_{m,n}$", which would put the $n=2$ argument above into the paper as an unverified claim.

### Not changed, checked for consistency

- l. 150–154, l. 157–158: unchanged. l. 157 ("composing two products of the family") now refers to $p^{\Omega}_{m,n}$, named in the replaced l. 131 and l. 156.
- l. 166–171, l. 173: "the family" is $p^{\Omega}_{m,n}$. "At $(m,1)$ they are the $\Loo$ relations" holds under the #11 reading ($\ell^{\Omega}$ under rule K is $\ell$ under the Koszul extension).
- l. 175–204, 207–226: the $(2,2)$ displays $T_i$ are $\Omega$-pairings of $\ell$-outputs, i.e. the second reading of the new l. 156 (products $\sprod{m}{n}$ joined by $\Omega^{-1}$). l. 175 "$[Q_B,\ell_3]+\ell_2\circ\ell_2=0$ of the $\ell_n$" is the standard $L_\infty$ notation (the #11 clause). l. 204 states rule K for the products and $\Omega$ on $\Psi$, $\Psi'$, which is how $T_i$ are evaluated. *Correction (fix pass):* the pre-fix version of this list included l. 205–206 here as "consistent with the second reading". That was wrong: see the l. 205–206 replacement above.
- l. 227, 229–234, 240–258: consistent with the l. 228 clause. l. 252 "sums of the $\sprod{n}{k}$" is the sprod family, as at l. 228.
- l. 263–266: $\sprod{2}{2}=\Delta\circ\ell_3$ is plain raising (sprod family) and is correct as written.

## Transcription into the paper (2026-10-04, orchestrator)

After the confirmation critic (`agent/reports/critic-088-confirm-20261004T163300.md`: transcribe after edits #3 (a)–(c), #1 optional; 0 critical, 1 major, 1 minor), the replacement text above was transcribed into `paper/sections/07-ibl.tex` with these four changes, all in the critic's exact wording; the paper is now the authoritative text:
- #3 (a): after l. 153, the coefficient rule stated where the unrestricted fields are introduced ("Products and forms are evaluated on them with the coefficients moved to the left, each coefficient passing only the basis states to its left; for an odd map this differs from the standard Koszul extension, in which the map also passes each coefficient and picks up its parity."); l. 204 kept, it restates the rule.
- #3 (b): the theorem reads "… satisfies the genus-zero IBL relations at every $(m,n)$, in the generating-function form above, if and only if the products $\ell_n$ form a cyclic $L_\infty$ algebra, in the standard Koszul convention for the odd maps $\ell_n$."
- #3 (c): l. 170 reads "For $\min(m,n)=1$, read in the same generating-function form, they coincide with the ones above, and both hold."
- #1: "in particular on the classical string field, of ghost number two, and on the auxiliary fields $\Sigma_k$, of ghost number $2k$;" and "at the sum of two string fields $\Psi$ and $\Psi'$ of unrestricted ghost number".

Not done (optional, critic note #2): moving the $\Delta$ sentence of the new l. 156 after l. 157.
Self-review addendum (critic #3): **C3 depends on the coefficient rule.** Under rule K (the paper's rule, now stated at l. 153), $R^{\Omega}=-E$; under a uniform Koszul evaluation the one-output relations of $p^{\Omega}$ are the Koszul relations of $\ell^{\Omega}$, which differ from those of $\ell$ by $2\ell_2(Q_Bx,y)$ at $(2,1)$ ($x$ even, $y$ odd; by hand, confirmed by hand by the confirmation critic; not machine-checked). Hence the theorem's left-hand side is a statement in the generating-function form under rule K, as the paper now says.
Open, not blocking: which family CFL Def. 2.3 selects at operator level in CFL's sign conventions at $\min(m,n)=1$ (a check of the $(2,1)$, $(1,2)$ operator relations of both families on a model with $Q_B\ne0$); the paper's l. 170 is now qualified so that it does not depend on it.
Compile: scratch copy of `paper/`, `latexmk` 0 errors, 0 undefined references, no overfull box in the IBL section, 145 pages. Grep of `07-ibl.tex`: none of the replaced formulations survives ("overall sign for one output", "component-dependent signs from three outputs", "each is a relation among the products", "the compositions $Q_B\circ\dots$", "the classical fields $\Psi$ and $\Sigma_k$", the old theorem wording).

## Self-review

1. **Objective.** Answered: the passage was inconsistent because l. 131–132 described a family and `eq:ibl:generating` wrote another; the replacement defines the family precisely, gives both generating forms, and states where the raising enters. The theorem is not weakened (C3.4); its statement gains a symbol and, after the fix pass, the clause fixing the Koszul convention of the $\ell_n$ (critic #11).
2. **Weakest step.** C3.1's notion of "composition in the family's own form" is the generating-function one (A4); the operator-level Koszul signs of CFL's composition are not derived, as in record 086 C1.2. The paper itself claims only the generating-function form (l. 158). Shored up by two independent computational routes for $E$ and $R$ (C3.1).
3. **Not checked.** Rule dependence of C3 (only rule K, the rule the paper's $\Psi=\Psi^ae_a$ and l. 204 fix; for odd maps it differs from the standard Koszul extension by $(-1)^{\abs B}$ at one output, critic #11); closed-string vertices (the statements are algebraic in the graded-symmetric vertices and the support of the pairing, which the string vertices share); a model satisfying the master equation with $Q_B\ne0$ and $\ell_3\ne0$ (C3.2 is an identity $R=-E$ on generic data, which makes the model choice for C3.3 a consistency illustration only).
4. **What a stronger reader would find.** That the whole sign question collapses to (088.3): the raised family is the sprod family precomposed with $(-1)^{N_{\rm gh}}$ on the inputs. Recorded and used in the replacement text. A reader might also prefer the alternative of not introducing $p^{\Omega}$ at all and stating the theorem for the products $\sprod{m}{n}$ joined by $\Omega^{-1}$; that would change the theorem's wording and the paragraph title ("raising indices"), so it is mentioned in the report as an option, not proposed as text.

## Fix pass (critic iteration 1)

Critic report `agent/reports/critic-088-20261004T155700.md` (REVISE: 0 critical, 3 major, 6 minor, 5 notes; science of C1–C3 confirmed). Brief `agent/briefs/active-computator-088-fix-20261004T161300.md`: mechanical, text only, no script run. One line per finding; state at the end of the line.

- #7 [major] rename $\hat p_{m,n}\to p^{\Omega}_{m,n}$ everywhere — **applied**. Record above this section: $\hat p\to p^{\Omega}$, $\hat\ell\to\ell^{\Omega}$, $R^{\hat p}\to R^{\Omega}$ (matching the script's `R^Omega`), $\hat p^{\,c}{}_b\to(p^{\Omega})^c{}_b$; no `\hat p` or `\hat\ell` left above this section; *Conventions* records the old name. Replacement text: `p^{\Omega}_{m, n}` with the paper's spacing. Grep of `paper/sections/`: `p^{\Omega}`, `p^\Omega`, `\tilde p`, `\Omega_n` unused; `\hat{p}` only at 07-ibl l. 228, 232 (the symmetric-algebra extension, which keeps its hat). Changed nodes: none in statement (notation only, all nodes C1–C4).
- #2 [major] sentence "in particular on $\Psi$" of the replacement for l. 128–141 — **applied verbatim** (the critic's two sentences replace the one sentence). C1.4 is now in the text ("the two families are different maps" on unrestricted fields). Changed node: C4 (its text restates C1.4 in addition to C1.2).
- #3 [major] l. 205–206 added to the replacement text; *checked for consistency* entry corrected — **applied verbatim**: the critic's two sentences (block *Replaces l. 205–206*). l. 206 is one sentence, so the replacement covers l. 205–206 whole. All twelve product names and directions of the supplied text checked against 086's labelling and the mirror map, in four lines under the block. The old entry "l. 175–207 … consistent with the second reading" is withdrawn and marked as corrected in the new *Not changed* list, which now covers l. 150–266 line by line. Changed node: C4 (scope).
- #4 [minor] "minus the sum of the compositions" in the replacement for l. 156 — **applied, with one deviation**: "is minus the sum" → "is, up to an overall sign common to all $(m, n)$, the sum" (critic's first option, verbatim). Deviation: "the strand is inserted as it is" also replaced, by "the strand enters the second product as the output of the first", because the critic's own computation shows that under rule K the strand is not inserted "as it is" (the derivative signs produce the overall $-1$); the new wording states only what (088.9) establishes ($Z^F$ is the output of the supplying product's one-output member) and leaves the sign to the added clause. Changed node: C4 (wording); C3.2's statement ($R^{\Omega}=-E$) unchanged and consistent with "up to an overall sign".
- #5 [minor] l. 172 — **applied, with a one-word deviation**: block *Replaces l. 172*, the critic's wording with "the cobracket" kept before $p^{\Omega}_{1, 2}$, as in the current l. 172, so that the sentence still names the operation. Changed node: C4 (scope).
- #8 [minor] componentwise reading of $\Omega_n$ — **applied**, the critic's text split into two sentences (one sentence per source line, the original sentence was already long): "for $X$ of definite parity … extended by linearity" in the first, "so that on a string field of unrestricted ghost number the sign acts component by component" attached to the existing "$\abs{X}$ is the parity of the states" in the second. Note #9 folded into the same sentence ("which we take as the $n$-th tensor power"), since the sentence was being rewritten anyway; it fixes the Koszul rule as a stated choice.
- #10 [minor] converse direction l. 227–234 — **resolved; optional clause supplied**. Read l. 220–258. The family extended is the sprod family, the correct one; reasons in the block *Replaces l. 228*:
  - l. 228 and l. 234 name its members.
  - The single-output reduction of l. 252–253 needs the $\pm\ell_n$, not $\ell^{\Omega}_n$. The two Koszul-convention relations differ at $n=2$ by $2\ell_2(Q_Bx,y)$; worked by hand in this pass, not machine-checked.
  - By 026 (8.1)–(8.6), 026's $\tilde\Delta$ is $\mp\Delta$ up to normalisation, so R31's and R32's one-output member is $\propto\ell_n$.
  - The criterion is family-independent.
  Supplied: "of~\eqref{eq:conv:sprod}" after $\sprod{m}{n}$ at l. 228, with no new claim. Not supplied: "rather than $p^{\Omega}_{m,n}$" (unverified claim). No node changed; C4's scope gains l. 228.
- #11 [note] Koszul clause in the theorem of l. 160 — **applied**: ", in the standard Koszul convention for the odd maps $\ell_n$" appended to the statement, the critic's phrase verbatim; the reason is recorded under the replacement block. Consistency: l. 175 and l. 266 write $[Q_B, \ell_3] + \ell_2 \circ \ell_2 = 0$, the standard form, so they agree with the clause. Self-review item 3 said rule K "is the Koszul extension"; corrected to "the rule the paper fixes at l. 204", since for odd maps rule K and the Koszul extension differ (#11). Changed node: C4 (text). C3.4's statement unchanged: "cyclic $L_\infty$" in the record always meant the standard relations (those equivalent to the master equation, R31).
- #13 [minor] script check `C3.0` for node C3.1 — **written, not run** (brief: no compute run in this pass), in `codes/verify-ibl-generating-sign.py`.
  - New helpers `tensor`, `basis_field`, `freed_strand`, `receiving`. They use only `raise_family`, `apply`, `tpow`, `form_n` and the engine's `M.vertex`; the engine is not edited.
  - The check runs for all three families, before the `C3.1` block. `C3.0-break` is a genuine perturbation.
  - Node C3.1 is tagged `[check: C3.0, C3.0-break — … not yet run]`, and Block 3 *Verification* says so.
  - Not formatted with `ruff format`: no `ruff` binary on the PATH or in `.venv/bin`, and installing one is outside a text-only pass. Lines checked by eye to stay ≤ 88 characters in the new code.
  - No syntax or name check was run either (a `py_compile` call would execute the interpreter). The orchestrator's first run is also the first syntax check.
  - Expected cost: well under a minute; the heaviest call is `freed_strand` at $(k_2,\ell_2)=(0,4)$, with ≈ 1.7 × 10⁶ basis-pair lookups.
- #14 [minor] script docstring labels — **applied, critic's second option**. The heading now says the labels are not node IDs, and every label carries its node in brackets, matching the tree's tags. Labels not renamed, because the quoted 20/20 output would no longer match a script that cannot be re-run in this pass. The docstring also states the #12 distinction (non-hollowness legs vs perturbation legs).
- #1 [note] no action: A4 already declares the generating-function reading of "composition".
- #6 [note] no change to C3.4. Recorded under #10: by 026 (8.1)–(8.6), R31's $\tilde\Delta$ is $\mp\Delta$ of the paper, not $\Omega^{-1}$. R31's family is therefore the sprod family up to normalisation at one output, with relations "in generating-function form", i.e. the polarized master equation with the BV bracket. That is the second reading of C3.4 (products $p_{m,n}$ joined by $\Omega^{-1}$), which C3.4 already states; the first reading ($p^{\Omega}$ in its own form) is the same scalar equation by C3.2. The critic's conditional ("if $\tilde\Delta=\Omega^{-1}$") does not hold, and no contradiction arises.
- #9 [note] folded into #8 ("which we take as").
- #12 [note] recorded in the *Verification* section and the script docstring.

### Changed nodes and dependents

- **C1, C1.1–C1.4, C2, C2.1–C2.3, C3, C3.2–C3.4**: statement and justification unchanged; notation only ($\hat p\to p^{\Omega}$, $\hat\ell\to\ell^{\Omega}$, $R^{\hat p}\to R^{\Omega}$).
- **C3.1**: statement unchanged; coverage tag added (`C3.0`, `C3.0-break`, written, not run). Its justification [by A2, A3, A4; (088.9)] is unchanged. The critic confirmed the step by hand (Logic section). Dependents C3.2, C3.3 → C3, C4: still hold, nothing in them changed.
- **C4**: statement changed (scope widened to l. 172, 205–206, 228; restates C1.4 as well). C4 has no dependents: no node cites it.
- Root-level claims C1–C3 unchanged. `Open gaps: none` and `Hypotheses in force: none` unchanged.
- By the schema, the only node whose statement changed has no dependents, and the root claims are unchanged. A narrow confirmation pass is in scope: the replacement text, l. 172, 205–206 and 228, plus C3.1's new check once run.

## Proposed convention entry

Ledger section: none (top level, after C7)

## C? — Rule K: evaluation of multilinear maps and forms on string fields with Grassmann-odd coefficients

- **Statement.** On string fields of unrestricted ghost number, $\Psi=\Psi^ae_a$, whose components carry the Grassmann parity that makes the field even ($\abs{\Psi^a}=\varepsilon_a$), multilinear maps and forms (vertices $\mathcal V_n$, products, the pairings $\langle\cdot,\cdot\rangle_n$, $\Omega_n$) are evaluated with the coefficients moved to the left, each coefficient passing only the basis states to its left. The first slot's coefficient passes nothing. For an odd map this differs from the standard Koszul extension, in which the map also passes each coefficient and picks up its parity; at one output the two differ by $(-1)^{\abs B}$ on the inputs. The rule fixes the sign of the IBL generating identity at one output: under rule K, $p^{\Omega}_{m,n}(\Psi^m)=p_{m,n}\bigl((P\Psi)^m\bigr)$ with $P\Psi=\sum_a(-1)^{\varepsilon_a}\Psi^ae_a$ (the signs depend only on the parities of coefficients and basis states, which $P$ does not change); $p^{\Omega}_{m,n}(B)=(-1)^{\abs B}p_{m,n}(B)$ on homogeneous inputs (R87). For two odd superfields, rule K gives $\Omega(L,K)=g_{cd}L^cK^d$, symmetric in $L$ and $K$; the Koszul passage of the coefficients through $\Omega$ as an odd form gives the opposite sign. Under rule K the polarised master equation at bidegree $(m,n)$ is, up to one overall sign common to all $(m,n)$, the sum of the compositions of $p^{\Omega}$ (R87, $R^{\Omega}=-E$). Under a uniform Koszul evaluation the one-output relations of $p^{\Omega}$ are the Koszul relations of $\ell^{\Omega}$, which differ from those of $\ell$ by $2\ell_2(Q_Bx,y)$ at $(2,1)$ ($x$ even, $y$ odd), so the theorem reads "in the standard Koszul convention for the odd maps $\ell_n$" while the generating-function form is read with rule K. On ghost-two fields alone ($P\Psi=\Psi$) the rule is immaterial.
- **Conventions it rests on.** C1 ($\Omega_n(X,Y)=(-1)^{\abs X}\langle X,Y\rangle_n$, the $n$-fold form with the Koszul sign of `eq:conv:pairing-n`); C6 (string fields as even superfields); physical ghost number (the project conventions).
- **Sources.** Record 086 A2 (rule K defined; "not stated by the paper, inherited from 026 (3.11) commentary") and its note (ii) on the readings of $\Omega$ on odd superfields; record 088 A2, (088.5), (088.7), (088.8), Q7, C1.4, and the fix-pass and self-review passages on the rule dependence of C3 (critic #3, #11); R87; paper `paper/sections/07-ibl.tex`, the sentences after `eq:ibl:polarized-master` (l. 170–180 in the version of 2026-10-10), which state the rule in the text.
- **Checked on.** Record 088 `C1.3-superfield` ((088.5) consequences on superfields: $p^{\Omega}(\Psi^m)\ne\pm p(\Psi^m)$ for components of both parities, already at $n=1$), `C2.4` (the generating identity holds with rule K and with no Koszul signs at all, so it is rule-independent), `C3.2` ($R^{\Omega}=-E$ under rule K) and `C3.0`, `C3.0-break`, all in `codes/verify-ibl-generating-sign.py` (22/22 PASS, 2026-10-04, exact Grassmann-polynomial model over $\mathbb Q$). Not machine-checked: the rule dependence of C3, i.e. the $2\ell_2(Q_Bx,y)$ discrepancy at $(2,1)$, done by hand twice (record 088 and the confirmation critic). Not checked: C3 under another rule applied uniformly; the operator-level signs of CFL Def. 2.3.
- **Where the project was loose.** Record 086 found rule K not stated by the paper (inherited from 026 (3.11) commentary) and flagged it as a candidate `local` entry; the paper states it in the text since 2026-10-04 (R87, Scope), and record 086 fixed the reading of $\Omega$ on odd superfields by a sentence after Display A. Record 088's self-review wrote that rule K "is the Koszul extension"; for odd maps the two differ (critic #11), which is why the theorem carries the clause "in the standard Koszul convention for the odd maps $\ell_n$". The paper's earlier statement that the raised family "differs by an overall sign for one output, and by component-dependent signs from three outputs on" was wrong (R87: the factor is $(-1)^{\abs B}$ at every $n$).
