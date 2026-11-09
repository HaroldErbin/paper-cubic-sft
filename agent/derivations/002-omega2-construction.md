# Derivation record 002 — The two-output symplectic form ω₂

Date: 2026-06-24
Author agent: computator
Brief: agent/briefs/done-computator-omega2-physical-20260624T153000.md (Revision-2);
originally agent/briefs/done-computator-omega2-20260624T122953.md (Revision-0/1).
Verification scripts:

- codes/verify-omega2-physical.py (sympy 1.14.0, physical-grading toy + n=3) — **authoritative**
- codes/verify-omega2-construction.py (sympy 1.14.0, suspended-grading toy, 14/14 PASS) — superseded by Revision-2 for the sign verdict

> **REVISION-2 (2026-06-24) — read this first.** This supersedes the central
> (anti)symmetry claim of the older Revision-0/1 text below. The earlier text
> derived antisymmetry of $\omega_2=\omega_1^{\otimes2}$ in a *suspended* grading
> from an asserted postulate (S.2: "$\Sigma$ carries one odd suspension unit").
> Re-derived here **directly from physical Grassmann statistics + the single
> $c_0^-$ + BPZ**, the verdict changes in framing:
>
> **In the physical $N_{\mathrm{gh}}$ parametrization, $\omega_2=\omega_1\otimes\omega_1$
> is graded SYMMETRIC, not antisymmetric.** It is therefore **not** a symplectic
> form on $\mathcal H^{\otimes2}$ in physical statistics. DC6 — read as "is the
> naive $\omega_2=\omega_1^{\otimes2}$ a graded-antisymmetric form?" — **stands**:
> the answer is no, physically.
>
> The earlier suspended-grading conclusion was the *correct shadow* of this:
> $\omega_1^{\otimes2}$ is even-as-an-operation (two $c_0^-$), so it is the natural
> *Poisson/symmetric* pairing, and **becomes** graded *antisymmetric* only after one shift
> of the whole $\Sigma$-field, $(\mathcal H^{\otimes2})[1]$; the form stays even (step 4′, D4.9): an even symplectic form, not the odd BV one. The suspension was a correct bookkeeping
> device; it was carrying the load-bearing sign, exactly as the brief feared. The
> physical object that is graded antisymmetric (and even) is $\omega_2^{\rm symp}(sX,sY):=\omega_2(X,Y)$ on $\big(\mathcal H^{\otimes2}\big)[1]$, one $s$ per argument of the form; the strand-wise $(s\otimes s)$ shifts $\Sigma$ by two and leaves it symmetric (D4.8). An odd $\Sigma$-pairing, whose inverse could be an antibracket, needs a grading whose parity is not a function of $\epsilon$ (R36).
>
> Net effect on the programme: $\omega_1^{\otimes2}$ is still the unique natural
> pairing fixed by the HS kinetic term, $m_2=\mathfrak p_{2,2,0}$ is still cyclic
> w.r.t. it, non-degeneracy is unchanged. What changes is the *label*: the
> two-output structure on $\Sigma$ is even/symmetric in physical statistics (graded
> symmetric *like* the $\mathfrak p_{1,2,0}$ cobracket sector — the same physical parity
> under the dictionary, a grading analogy, not the operadic identity $\omega_2=\mathfrak
> p_{1,2,0}$ — consistent with
> the $\IBL$ degree bookkeeping R5 *under the suspended↔physical dictionary of step 4*;
> R5 itself gives the odd *suspended* degree $|\mathfrak p_{1,2,0}|=-1$, and the even
> physical parity follows only via that dictionary), and the suspended grading is the
> bridge to the BV presentation: strand-wise it makes $\Omega_1$ the odd symplectic form of each strand; on $\Sigma$ a uniform shift gives at most an even antisymmetric form (step 4′). See the **Revision-2** derivation below; the
> Revision-0/1 text is retained beneath it, with its sign conclusion flagged as
> superseded.

---

## REVISION-2 — physical-statistics derivation of the ω₂ exchange sign

### R2.Setup — physical statistics of closed-string states

**Assumptions/conventions.** Erbin (2023): metric $(-,+,+,+)$, $\hbar=c=1$,
$\alpha'$ explicit, bra–ket. Classical $g=0$, $O(g_s^2)$, $n=2$. All states are
level-matched, $\phi\in\ker L_0^-\cap\ker b_0^-$, and all final objects are in the
**physical** $N_{\mathrm{gh}}$ parametrization ($\Psi$ at $N_{\mathrm{gh}}=2$,
$\Sigma\in\mathcal H^{\otimes2}$ at $N_{\mathrm{gh}}=4$, eq.`Sigexpand`).

**Grassmann parity (the relation adopted, and its source).** For the closed
*bosonic* string there is no worldsheet matter fermion number; the only source of
Grassmann grading is the $bc\,\bar b\bar c$ ghost sector. The Grassmann parity of a
state is therefore its ghost number mod 2 (Erbin 2023 §11–13; Zwiebach 1993,
Nucl.Phys. B390):
$$\epsilon(\phi)=N_{\mathrm{gh}}(\phi)\bmod 2.\tag{R2.1}$$
This is **not** the suspension shift — it is the spacetime statistics read off the
worldsheet ghost content, fixed independently of any complex-degree convention.
Consequences:
$$\epsilon(\Psi)=2\bmod2=0\ (\text{even});\qquad
\epsilon(\Sigma)=4\bmod2=0\ (\text{even, two copies}).\tag{R2.2}$$
The mode $c_0^-=\tfrac12(c_0-\bar c_0)$ is Grassmann-**odd**, $N_{\mathrm{gh}}(c_0^-)=1$.

### R2.Derivation, step 2 — exchange symmetry of $\omega_1$, physically

$$\omega_1(A,B)=\langle A|\,c_0^-\,|B\rangle_{\mathrm{bpz}}.\tag{R2.3}$$
Sphere ghost-number anomaly: a non-vanishing correlator on $S^2$ saturates at
$N_{\mathrm{gh}}=6$. The kinetic term $\tfrac12\langle\Psi|c_0^-Q_B|\Psi\rangle$
balances $2+1_{(c_0^-)}+1_{(Q_B)}+2=6$. Hence $\omega_1(A,B)\neq0$ requires
$$N_{\mathrm{gh}}(A)+1+N_{\mathrm{gh}}(B)=6
\;\Longleftrightarrow\; N_{\mathrm{gh}}(A)+N_{\mathrm{gh}}(B)=5\ (\text{odd}),\tag{R2.4}$$
so on its support
$$\epsilon(A)+\epsilon(B)\equiv 5\equiv 1\pmod2\quad(\text{opposite physical parity}).\tag{R2.5}$$
In particular $\omega_1(\Psi,\Psi)=0$ ($2+2=4\neq5$): $\Psi$ pairs with the
$N_{\mathrm{gh}}=3$ antifield sector, as a symplectic form must.

**Exchange sign.** The BPZ inner product is graded-symmetric on the states it
pairs, $\langle A|B'\rangle_{\mathrm{bpz}}=(-1)^{\epsilon(A)\epsilon(B')}\langle B'|A\rangle_{\mathrm{bpz}}$.
Write $B'=c_0^-B$; moving the **single** odd $c_0^-$ ($\epsilon=1$) back across $A$
and $B$ and using $(c_0^-)$ self-BPZ-conjugacy gives one extra minus sign relative
to the symmetric BPZ rule:
$$\omega_1(A,B)=-(-1)^{\epsilon(A)\epsilon(B)}\,\omega_1(B,A).\tag{R2.6}$$
$\omega_1$ is **graded antisymmetric**, and the sign is carried entirely by the
**one** $c_0^-$ + the BPZ rule — no suspension unit appears. As an *operation*
$\omega_1$ is odd: it pairs opposite-parity states (R2.5). This is the template the
two-output case must follow.

*Correction 2026-09-26 (record 055, critic-055-20260926T032500):* R2.6 is wrong.
The one-line argument above drops one of two signs: $\mathrm{bpz}(c_0^-)=-c_0^-$
(book `bos:eq:conjugation-c0pm-b0pm`) together with passing $c_0^-$ across $B$ and
the shifted parity of $B'=c_0^-B$. The correct bookkeeping (order-preserving BPZ
product rule, `cft_operator_formalism.tex` l.1134–1146): $\langle B'|=\langle0|\,
\mathrm{bpz}(c_0^-)\,\mathrm{bpz}(B)=-\langle0|c_0^-\,\mathrm{bpz}(B)=
-(-1)^{|B|}\langle B|c_0^-$, giving $\omega_1(A,B)=(-1)^{|A|(|B|+1)}\cdot(-1)\cdot
(-1)^{|B|}\omega_1(B,A)=(-1)^{(1+|A|)(1+|B|)}\omega_1(B,A)$, which on support
($|A|+|B|$ odd) is $\omega_1(A,B)=(-1)^{\epsilon(A)\epsilon(B)}\omega_1(B,A)$ —
**graded symmetric**, the opposite of R2.6. Confirmed independently by an explicit
mode computation (055 B3.4) with no rearrangement identity. The $k=2$ conclusion
R2.10 stands unaffected ($s^2=1$).

### R2.Derivation, step 3 — exchange symmetry of $\omega_2=\omega_1\otimes\omega_1$ (the decisive sign)

With the Koszul sign for reordering $x_2$ past $y_1$,
$$W(X,Y)\equiv\omega_2(X,Y)=(-1)^{\epsilon(x_2)\epsilon(y_1)}\,
\omega_1(x_1,y_1)\,\omega_1(x_2,y_2),\qquad X=x_1\otimes x_2,\;Y=y_1\otimes y_2.\tag{R2.7}$$
Exchange $X\leftrightarrow Y$ and apply (R2.6) in each slot:
$$\begin{aligned}
W(Y,X)
&=(-1)^{\epsilon(y_2)\epsilon(x_1)}\,\omega_1(y_1,x_1)\,\omega_1(y_2,x_2)\\
&=(-1)^{\epsilon(y_2)\epsilon(x_1)}\,
\big[-(-1)^{\epsilon(x_1)\epsilon(y_1)}\omega_1(x_1,y_1)\big]
\big[-(-1)^{\epsilon(x_2)\epsilon(y_2)}\omega_1(x_2,y_2)\big]\\
&=(-1)^{\epsilon(y_2)\epsilon(x_1)+\epsilon(x_1)\epsilon(y_1)+\epsilon(x_2)\epsilon(y_2)}\,
\omega_1(x_1,y_1)\,\omega_1(x_2,y_2).
\end{aligned}\tag{R2.8}$$
The two minus signs from the two antisymmetric $\omega_1$'s multiply to $+1$: this
$(-1)(-1)=+1$ is the **evenness of the two-$c_0^-$ product as an operation** — it is
*not* the exchange sign of $W$, which is computed next and carries a genuine
$(-1)^{\epsilon(X)\epsilon(Y)}$. Dividing by (R2.7),
$$W(Y,X)=(-1)^{\,\Xi}\,W(X,Y),\qquad
\Xi=\epsilon(y_2)\epsilon(x_1)+\epsilon(x_1)\epsilon(y_1)+\epsilon(x_2)\epsilon(y_2)-\epsilon(x_2)\epsilon(y_1).\tag{R2.9}$$
On the support, each slot is pinned by (R2.5): $\epsilon(y_i)=\epsilon(x_i)+1$. Write
$a_i=\epsilon(x_i)$ ($a_i^2=a_i$, arithmetic mod 2). Term by term:
$$\begin{aligned}
\epsilon(y_2)\epsilon(x_1)&=(a_2+1)a_1=a_1a_2+a_1,\\
\epsilon(x_1)\epsilon(y_1)&=a_1(a_1+1)=2a_1\equiv0,\\
\epsilon(x_2)\epsilon(y_2)&=a_2(a_2+1)=2a_2\equiv0,\\
-\epsilon(x_2)\epsilon(y_1)&\equiv a_2(a_1+1)=a_1a_2+a_2.
\end{aligned}$$
The **two $a_1a_2$ cross terms cancel** ($2a_1a_2\equiv0$), leaving
$$\Xi\equiv a_1+a_2=\epsilon(X)\pmod2.\tag{R2.10a}$$
On support $\epsilon(Y)=\epsilon(X)$ (opposite parity in each of the two slots
$\Rightarrow$ same total parity), so $\epsilon(X)\equiv\epsilon(X)^2=\epsilon(X)\epsilon(Y)$,
giving the genuine **graded-symmetric** exchange relation
$$\boxed{\;W(Y,X)=(-1)^{\epsilon(X)\epsilon(Y)}\,W(X,Y)\quad\text{on }\operatorname{supp}(W).\;}\tag{R2.10}$$
This is a graded symmetry: a true $-1$ on the odd–odd sector
($\epsilon(X)=\epsilon(Y)=1$), $+1$ on even sectors — *not* an ungraded
"$+1$" symmetry. **$\omega_2=\omega_1^{\otimes2}$ is graded SYMMETRIC in the physical
parity.** The sympy toy tests precisely this graded relation: P1 reports
sym-violations $=0$ (R2.10 holds on every entry, vacuously off support via P2) and
anti-violations $=16$ (it is *not* antisymmetric — this count is over the
on-support entries; off-support entries are $0=0$ and violate neither relation);
off support $W=0$ (P2).

This is **outcome (b)** of the brief: $\omega_1^{\otimes2}$ alone is **not** a
graded-antisymmetric (symplectic) $\omega_2$ in physical statistics; it is graded
*symmetric*. The decisive physical reason is **(i) the operation parity alone**:
**two** $c_0^-$ insertions make the product even-as-an-operation (the explicit
$(-1)(-1)=+1$ in R2.8) — one odd $c_0^-$ gives graded antisymmetry, two give graded
symmetry — and this holds for *any* support parity. The robustness check **Rob**
(even saturation, sum $=4$, same-parity pairing) confirms the symmetric *type* does
not depend on the precise sphere-anomaly value. The opposite-parity support condition
(R2.5), $\epsilon(Y)=\epsilon(X)$, is then one consistent instantiation of the route:
it makes the two $a_1a_2$ cross terms in the Koszul + antisymmetry signs cancel so the
exchange exponent reduces to $\epsilon(X)\epsilon(Y)$ — but it is *not* load-bearing for
the headline (the Rob check gives the same symmetric verdict).

### R2.Derivation, step 4 — the suspended↔physical dictionary (reconciling $A_c=s^{-2}\tilde A_c$)

The Münster–Sachs/CFL convention $A_c=s^{-2}\tilde A_c$ shifts the *complex degree*
of a single closed field by $-2$ (an **even** integer shift), so it leaves the
$\mathbb Z_2$ Grassmann parity (R2.1) **unchanged**: $s^{-2}$ is parity-even. Their
$\omega_c=(\cdot,c_0^-\cdot)_{\mathrm{bpz}}\circ(s^2\otimes s^2)$ is presented as an
*odd* symplectic form because the **odd** symplectic structure lives on the
suspended complex $C[1]$, where each entry of the form carries one extra $[1]$ (one
odd unit) relative to the physical state. The dictionary is:

*Superseded 2026-09-26 (brief computator-002-dictionary-20260926T104500): the
$\omega_1$ and $\omega_2$ rows of the table below; the corrected table follows it
directly, the derivation is (D4.1)–(D4.9) further down. The sentence above ("each
entry of the form carries one extra $[1]$") yields an odd symplectic form only
together with the Koszul décalage sign $(-1)^{|A|}$ (D4.3–D4.5): the $[1]$ alone
does not change the exchange type of $\omega_1$ on its support (D4.2).*

| object | physical ($N_{\mathrm{gh}}$, $\epsilon$) | suspended (CFL degree, $|\cdot|_s$) |
| --- | --- | --- |  |  |
| field grade | $\epsilon=N_{\mathrm{gh}}\bmod2$ | $|\cdot|_s=\epsilon+1$ (one $[1]$ per slot of the form's complex) |
| $\omega_1$ | graded **antisym** (one $c_0^-$), pairs opp. parity | odd symplectic (built-in by $s^2$) |  |  |
| $\omega_2=\omega_1^{\otimes2}$ | graded **SYMMETRIC** (R2.10) | graded **antisym** (but **even**) after one shift of the whole $\Sigma$-field, $(\mathcal H^{\otimes2})[1]$; not an odd form in any uniform grading (step 4′, D4.9; this table is superseded) |  |  |

**Corrected dictionary (2026-09-26).** Notation: $\epsilon$ physical parity (R2.1),
$\deg_s=\epsilon+1$ the suspended degree of one strand; on $\Sigma$ two suspended
gradings are possible, strand-wise $(\mathcal H[1])^{\otimes2}$ with
$\deg_s X=\deg_s x_1+\deg_s x_2\equiv\epsilon(X)$, and the one-unit shift
$(\mathcal H^{\otimes2})[1]$ of R7's $\omega_2^{\rm symp}$ with $\deg_S X=\epsilon(X)+1$.
"Odd"/"even" form = non-zero only on pairs of opposite/equal degree mod 2.

| object | physical parity $\epsilon$ | suspended degree |
| --- | --- | --- |
| $\omega_1=\langle A,B\rangle=\langle A\rvert c_0^-\lvert B\rangle$ | graded **symmetric** on support (C1, D4.1); odd form | graded **symmetric** in $\deg_s$, identically (D4.2; the book's convention $\omega(\tilde x_1,\tilde x_2)=\omega(x_1,x_2)$); odd form; **not** symplectic in either grading |
| $\Omega_1=(-1)^{\epsilon(A)}\langle A,B\rangle$ (Koszul décalage of $\omega_1$) | graded **antisymmetric**, identically (D4.3); odd form | graded **antisymmetric** (D4.4); odd form: **the odd symplectic form** of the BV presentation (EKS; book `homotopy_algebra.tex` l.493) |
| $\omega_2=\omega_1^{\otimes2}$ (055 A4 Koszul) | graded **symmetric** (R2.10, R58); even form | strand-wise $\deg_s$: graded **symmetric**; one-unit shift $\deg_S$ ($c_s=1$): graded **antisymmetric**; even form in both (D4.8–D4.9) |
| $\Omega_2=\Omega_1^{\otimes2}$ (055 A4 Koszul) $=(-1)^{\epsilon(X)}\omega_2$ | graded **symmetric**, identically (D4.6–D4.7); even form | same as $\omega_2$ (D4.8); with the tensor Koszul sign also taken in $\deg_s$, $\Omega_1^{\otimes2}=\omega_2$ on support (D4.8a) |

*Correction 2026-09-26 (record 055, critic-055-20260926T032500):* the $\omega_1$
row above is wrong on the physical side — $\omega_1$ is graded **symmetric** in
$\epsilon$ (see the R2.6 correction above), and also graded symmetric in the
suspended degree $\epsilon+1$; the BV odd symplectic form is
$(-1)^{|A|}\langle A,B\rangle$ per strand, not $\langle A,B\rangle$ itself. This row
needs to be redone against that object; flagged open (055 B4).
*Resolved 2026-09-26 (brief computator-002-dictionary-20260926T104500):* corrected
table above, derivation (D4.1)–(D4.9) below, check `codes/verify-002-dictionary.py`.

#### Step 4′ (2026-09-26) — exchange symmetry of the BV odd symplectic form $\Omega_1$ and of $\Omega_2=\Omega_1^{\otimes2}$

\subsection*{Setup}
$\langle A,B\rangle:=\omega_1(A,B)=\langle A\rvert c_0^-\lvert B\rangle$ (R2.3);
$\lvert A\rvert:=\epsilon(A)=N_{\rm gh}(A)\bmod2$ (R2.1); $\lvert A\rvert_s:=\lvert A\rvert+1$,
the suspended degree ($\deg\tilde x=\deg x+1$, book `homotopy_algebra.tex`, suspension
subsection). Inputs, all cited: the book rearrangement relation, valid on every
homogeneous pair (C1; 055 B3.1; `bos:eq:closed-product-rearrangement`)
$$\langle B,A\rangle=(-1)^{(1+\lvert A\rvert)(1+\lvert B\rvert)}\langle A,B\rangle;\tag{D4.0}$$
the support $\lvert A\rvert+\lvert B\rvert\equiv1$ (R2.5); the odd symplectic form of the
BV literature (EKS NS–NS, recorded in the book's comment at `homotopy_algebra.tex`
l.493; 055 B3)
$$\Omega_1(A,B):=(-1)^{\lvert A\rvert}\langle A,B\rangle;$$
and $\Omega_2:=\Omega_1^{\otimes2}$ with the Koszul sign of 055 A4 in physical parity,
$\Omega_2(X,Y)=(-1)^{\epsilon(y_1)\epsilon(x_2)}\Omega_1(x_1,y_1)\,\Omega_1(x_2,y_2)$,
$X=x_1\otimes x_2$, $Y=y_1\otimes y_2$. Arithmetic in exponents mod 2.

\subsection*{Derivation}
$$\begin{aligned}
\langle B,A\rangle
&=(-1)^{1+\lvert A\rvert+\lvert B\rvert}(-1)^{\lvert A\rvert\lvert B\rvert}\langle A,B\rangle
\;\stackrel{\rm supp}{=}\;(-1)^{\lvert A\rvert\lvert B\rvert}\langle A,B\rangle,
\end{aligned}\tag{D4.1}$$
$$\langle B,A\rangle=(-1)^{\lvert A\rvert_s\lvert B\rvert_s}\langle A,B\rangle\quad\text{(identically)},\tag{D4.2}$$
$$\begin{aligned}
\Omega_1(B,A)
&=(-1)^{\lvert B\rvert}\langle B,A\rangle\\
&=(-1)^{\lvert B\rvert+(1+\lvert A\rvert)(1+\lvert B\rvert)}\langle A,B\rangle\\
&=(-1)^{\lvert A\rvert+\lvert B\rvert+(1+\lvert A\rvert)(1+\lvert B\rvert)}\,\Omega_1(A,B)\\
&=(-1)^{1+\lvert A\rvert\lvert B\rvert}\,\Omega_1(A,B)\quad\text{(identically)},
\end{aligned}\tag{D4.3}$$
$$\begin{aligned}
\Omega_1(B,A)
&=(-1)^{\lvert A\rvert_s\lvert B\rvert_s+\lvert A\rvert_s+\lvert B\rvert_s}\,\Omega_1(A,B)
\;\stackrel{\rm supp}{=}\;-(-1)^{\lvert A\rvert_s\lvert B\rvert_s}\,\Omega_1(A,B).
\end{aligned}\tag{D4.4}$$
Variants of the twist, on support:
$$(-1)^{\lvert B\rvert}\langle A,B\rangle=-\Omega_1(A,B),\qquad
(-1)^{\lvert A\rvert_s}\langle A,B\rangle=-\Omega_1(A,B),\qquad
(-1)^{\lvert A\rvert+\lvert B\rvert}\langle A,B\rangle=-\langle A,B\rangle.\tag{D4.5}$$
Two strands. Since $\Omega_1(x,y)=(-1)^{\epsilon(x)}\omega_1(x,y)$,
$$\Omega_2(X,Y)=(-1)^{\epsilon(y_1)\epsilon(x_2)}(-1)^{\epsilon(x_1)+\epsilon(x_2)}\,\omega_1(x_1,y_1)\,\omega_1(x_2,y_2)=(-1)^{\epsilon(X)}\,\omega_2(X,Y)\quad\text{(identically)},\tag{D4.6}$$
$$\begin{aligned}
\Omega_2(Y,X)
&=(-1)^{\epsilon(Y)}\,\omega_2(Y,X)
=(-1)^{\epsilon(Y)+\epsilon(X)\epsilon(Y)}\,\omega_2(X,Y)
=(-1)^{\epsilon(X)+\epsilon(Y)}(-1)^{\epsilon(X)\epsilon(Y)}\,\Omega_2(X,Y)\\
&\stackrel{\rm supp}{=}(-1)^{\epsilon(X)\epsilon(Y)}\,\Omega_2(X,Y).
\end{aligned}\tag{D4.7}$$
Suspended gradings of $\Sigma$, on support ($\epsilon(X)=\epsilon(Y)$), uniform shift
$\deg_c X:=\epsilon(X)+c$:
$$(-1)^{\deg_cX\,\deg_cY}=(-1)^{\epsilon(X)\epsilon(Y)+c(\epsilon(X)+\epsilon(Y))+c}
\stackrel{\rm supp}{=}(-1)^{c}(-1)^{\epsilon(X)\epsilon(Y)}
\;\Longrightarrow\;
\Omega_2(Y,X)=(-1)^{c}\,(-1)^{\deg_cX\,\deg_cY}\,\Omega_2(X,Y).\tag{D4.8}$$
Strand-wise suspension is $c=2\equiv0$; R7's one-unit shift is $c=1$. With the tensor
Koszul sign also in the suspended degree,
$$\Omega^{(s)}_2(X,Y):=(-1)^{\lvert y_1\rvert_s\lvert x_2\rvert_s}\,\Omega_1(x_1,y_1)\,\Omega_1(x_2,y_2)
=(-1)^{\epsilon(y_1)\epsilon(x_2)+\epsilon(y_1)+\epsilon(x_2)+1+\epsilon(x_1)+\epsilon(x_2)}\,\omega_1\omega_1
\stackrel{\rm supp}{=}\omega_2(X,Y).\tag{D4.8a}$$
Parity of the $\Sigma$-form: on support $\epsilon(X)+\epsilon(Y)\equiv0$, so
$\deg_cX+\deg_cY\equiv0$ for every $c$:
$$\omega_2,\ \Omega_2\ \text{are even forms in every grading } \epsilon+c.\tag{D4.9}$$

\subsection*{Commentary}
(D4.1) is C1 restated. (D4.2): $(1+\lvert A\rvert)(1+\lvert B\rvert)=\lvert A\rvert_s\lvert B\rvert_s$
term by term, so the book relation *is* graded symmetry in $\deg_s$, with no support
condition. On support exactly one of $A,B$ is even in $\epsilon$ and exactly one is even in
$\deg_s$, so both graded signs are $+1$: on the support of a single-strand form, graded
symmetry in $\epsilon$ and in $\epsilon+1$ are the same statement (plain symmetry), and
no degree shift alone can turn $\omega_1$ into an antisymmetric form. (D4.3): the
exponent is $\lvert A\rvert+\lvert B\rvert+1+\lvert A\rvert+\lvert B\rvert+\lvert A\rvert\lvert B\rvert=1+\lvert A\rvert\lvert B\rvert$;
the twist $(-1)^{\lvert A\rvert}$ is not exchange-invariant on support
($(-1)^{\lvert A\rvert}\ne(-1)^{\lvert B\rvert}$), and this is the whole mechanism. (D4.4):
$\lvert A\rvert\lvert B\rvert=\lvert A\rvert_s\lvert B\rvert_s+\lvert A\rvert_s+\lvert B\rvert_s+1$, and $\lvert A\rvert_s+\lvert B\rvert_s\equiv1$
on support; off support $\Omega_1=0$, so the graded antisymmetry holds on every
homogeneous pair. (D4.5): a twist by the parity of one argument gives $\pm\Omega_1$;
a twist by an exchange-invariant sign does nothing. $(-1)^{\lvert A\rvert}$ is the Koszul
sign of $(s\otimes s)(A\otimes B)=(-1)^{\lvert A\rvert}sA\otimes sB$, the standard
décalage of a form from $\mathcal H$ to $\mathcal H[1]$; the book instead sets
$\omega(\tilde x_1,\tilde x_2)=\omega(x_1,x_2)$ (no décalage sign), which is why its
suspended form stays graded symmetric (D4.2). (D4.6): the twists multiply to
$(-1)^{\epsilon(x_1)+\epsilon(x_2)}=(-1)^{\epsilon(X)}$. (D4.7): second equality R2.10
(R58 with $s=+1$), last step $\epsilon(Y)=\epsilon(X)$ on support. Independent route: by
(D4.3) $\Omega_1$ has exchange sign $s=-1$ in 055's parametrisation, and 055 (B1.4)
gives $\Omega_2(Y,X)=(-1)^2(-1)^{\epsilon(X)\epsilon(Y)}\Omega_2(X,Y)$ on every homogeneous
pair. (D4.8): $c^2\equiv c$ and $\epsilon(X)+\epsilon(Y)\equiv0$ on support. (D4.8a):
$(\epsilon(y_1)+1)(\epsilon(x_2)+1)$ expanded; on support $\epsilon(y_1)=\epsilon(x_1)+1$
and the extra exponent is $2\epsilon(x_1)+2\epsilon(x_2)+2\equiv0$. (D4.9): the $k=2$
support pairs equal total parities, since each strand pairs opposite parities.

\subsection*{Result}
$$\boxed{\;\Omega_1(B,A)=-(-1)^{\lvert A\rvert\lvert B\rvert}\Omega_1(A,B)=-(-1)^{\lvert A\rvert_s\lvert B\rvert_s}\Omega_1(A,B),\qquad
\Omega_2(Y,X)=(-1)^{\epsilon(X)\epsilon(Y)}\Omega_2(X,Y)=-(-1)^{\deg_SX\,\deg_SY}\Omega_2(X,Y)\;}$$
(first equalities identically, second on support; $\deg_S=\epsilon+1$ the one-unit
shift of $\Sigma$). $\Omega_1$ is the odd symplectic form: graded antisymmetric in both
gradings, odd. $\omega_1$ is graded symmetric in both. $\Omega_2$ and $\omega_2$ differ by
the exchange-invariant sign $(-1)^{\epsilon(X)}$ and have the same exchange law: graded
symmetric in $\epsilon$ and in the strand-wise suspended degree, graded antisymmetric
only after one further shift of the whole $\Sigma$-field ($c_s=1$), and even in every
uniform grading. Corollary for general $k$ (055 B1.4 with $s=-1$):
$\Omega_k=(-1)^{\epsilon(X)}\omega_k$ and $\Omega_k(Y,X)=(-1)^k(-1)^{\epsilon(X)\epsilon(Y)}\Omega_k(X,Y)$.

\subsection*{Verification}
`codes/verify-002-dictionary.py`, 35/35 PASS (seed 20260926; also seed 7), log
`agent/scratch/002-dictionary-run1.log`. Representation: the Grassmann algebra of the
six ghost zero modes $c_{\pm1},\bar c_{\pm1},c_0,\bar c_0$ on the SL(2,C) vacuum, BPZ by
$\mathrm{bpz}(c_n)=(-1)^{n-1}c_{-n}$ order-preserving, $\langle c_{-1}\bar c_{-1}c_0^-c_0^+c_1\bar c_1\rangle=-\tfrac12$
(check N0); the pairing is computed, no rearrangement identity is used. Checks: C1 pair
($\omega_1=-\tfrac12$ both orders, $\Omega_1=\mp\tfrac12$) and a level-matched pair with the
other parity order ($A=c_0^+\lvert0\rangle$, $B=c_{-1}\bar c_{-1}c_1\bar c_1\lvert0\rangle$);
(D4.0)–(D4.5) on all $64\times64$ monomial pairs (64 on support); (D4.6)–(D4.9)
exhaustively on the 12 level-matched $\ker b_0^-$ states ($144^2$ tensor pairs) and on
20000 sampled pairs of the full algebra, with 055's `omega_k` imported (AST extraction
from `codes/verify-omega-k.py`); $k=3$ corollary sampled. Break legs: BRK-a the untwisted
$\langle A,B\rangle$ violates odd-symplectic antisymmetry on all 64 support pairs; BRK-b
with $\mathrm{bpz}(c_0)=+c_0$ the form $\omega_1$ turns graded antisymmetric ($s=-1$), so
(D4.1) is falsifiable in this representation; BRK-c $\Omega_2$ graded antisymmetric in
$\epsilon$ fails on every non-zero pair, as does antisymmetry in $\epsilon+0$ ($c_s=0$).
Finding (check REV): reversing the order of the BPZ product leaves the exchange sign
unchanged on this sector (each bra of $r$ odd modes gets $(-1)^{r(r-1)/2}$, and
$r_A+r_B=5$ makes the product $+1$); on the zero-mode sector $s=-\sigma_0$ with
$\mathrm{bpz}(c_0)=\sigma_0c_0$. Not checked: states with $b$-modes or $c_n$, $\lvert n\rvert\ge2$
(the matter factor is an even symmetric product and cannot change an exchange sign).
REV does not extend there: with one further $b$–$c$ pair ($r_A+r_B=7$) the non-graded reversed rule flips the exchange sign; (D4.0) and $s=-\sigma_0$ hold on all sectors. Order reversal leaves $s$ unchanged on the zero-mode sector only.
Not checked also: the Münster–Sachs $(\cdot,\cdot)_{\rm bpz}$ conventions.

The shift $c_s$ relating the two presentations is fixed by R2.10 *conditionally* (toy
check **Dict**): **if** one demands a graded-*antisymmetric* form (symplectic, but even: D4.9),
$W(Y,X)=-(-1)^{(\epsilon(X)+c_s)(\epsilon(Y)+c_s)}W(X,Y)$ on support forces $c_s=1$.
So $c_s=1$ is **not** a derived worldsheet fact about $\Sigma$; it is the **choice of
the shifted (BV-motivated) presentation** — the same convention by which Münster–Sachs'
$\omega_c$ is "made antisymmetric by the degree shift" (WBEIHWFU review l.305:
"the apparent symmetry of the BPZ product is removed by the suspension") [2026-09-26:
for one strand the shift alone leaves $\langle\cdot,\cdot\rangle$ symmetric on its support
(D4.2); the antisymmetry comes from the décalage sign $(-1)^{\lvert A\rvert}$ that goes with
it (D4.3). With $\Omega_2$ in place of $\omega_2$ the conclusion $c_s=1$ is unchanged, since
$\Omega_2=(-1)^{\epsilon(X)}\omega_2$ has the same exchange law (D4.6–D4.8)]. The old S.2
("$\Sigma$ carries one odd suspension unit") is the *correct shadow* of the physical
computation **once that presentation is chosen**: it is the degree shift mapping the
physical **symmetric** pairing $\omega_1^{\otimes2}$ to the suspended **antisymmetric**
symplectic form. The previous note's error was not the count but the **headline**: it
presented the suspended antisymmetry as the physical content. Physically the
$\Sigma$-pairing is **graded symmetric**; the antisymmetry is a feature of the
$[1]$-shifted presentation (graded antisymmetric but even, D4.9), not of the
spacetime statistics. The tension the
critic flagged ("$s^{-2}$ is even, so how does one odd unit appear?") is resolved: the
$-2$ integer shift is even and irrelevant to $\mathbb Z_2$ parity; the **single** $[1]$
that flips the symmetry is a shift of the whole $\Sigma$-field, $(\mathcal H^{\otimes2})[1]$
— the strand-wise suspension $(\mathcal H[1])^{\otimes2}$ that makes $\Omega_1$ odd
symplectic shifts $\Sigma$ by two and flips nothing (D4.8) — a presentation choice, not a
theorem about $\Sigma$. The antisymmetric $\Sigma$-form it produces is even (D4.9); an
odd $\Sigma$-pairing needs a grading that is not a function of $\epsilon$ (R36,
$\deg_{\mathrm{Sym}^2}=(N_{\rm gh}-4)/2$).

### R2.Derivation, step 5 — cyclicity, non-degeneracy, uniqueness (physical grading)

**Cyclicity (reuses R6 only as a *separate* fact; does not insert $\ell_3$).**
$m_2=\mathfrak p_{2,2,0}=\Delta\circ\ell_3$ is defined by
$W(X,m_2Y)=V_4(x_1,x_2,y_1,y_2)$ (eq.`V4ell3`). $V_4$ is fully graded-symmetric in
physical parity (closed cyclic vertex). Cyclicity = self-adjointness of $m_2$ for
$\omega_2=W$:
$$W(X,m_2Y)=W(m_2X,Y),\tag{R2.11}$$
equivalent to the pair-exchange symmetry of $V_4$, which holds because $V_4$ is
fully graded-symmetric. $N_{\mathrm{gh}}(m_2)=-2$ (eq.`mtwo`), so $m_2$ is
**parity-even**, and on the support no Koszul sign appears in (R2.11). Toy checks
**Cyc-a/Cyc-b** confirm it (cyclicity-violations $=0$), using **only** $V_4$ — no
$\ell_3=\mathfrak p_{3,1,0}$ insertion, so the $(2,2,0)$ relation R6 (a $Q$-exactness
statement, reused verbatim) is untouched. Cyclicity holds for $\omega_2$ regardless
of whether it is presented symmetrically or antisymmetrically: it is a self-adjointness
of the *bilinear* pairing, insensitive to the overall $\mathbb Z_2$ relabel. **This
is the one acceptance criterion that survives outcome (b) intact.**

**Non-degeneracy.**
$$\boxed{\;\det\omega_2=\big(\det\omega_1\big)^{2\dim\mathcal H}\neq0\quad
\text{(finite-dim toy; inf-dim level-matched non-degeneracy inherited from }\omega_1
\text{ on }\ker L_0^-\cap\ker b_0^-,\ \textbf{open}).\;}$$
Toy check **Det** confirms $\det W=a^{16}b^{16}=(\det\omega_1)^{2\cdot4}$.

**Uniqueness (demoted, per critic Concern).** $\omega_1^{\otimes2}$ is the
**natural pairing fixed by the HS kinetic term** $-\tfrac{g_s^2}{4!}V_4(\Sigma,\Sigma)
=-\tfrac{g_s^2}{4!}W(\Sigma,m_2\Sigma)$: given that $V_4$ and $m_2$ are defined
through $W$, the pairing must be $W$. **Full uniqueness is not proven** (the
automorphism group of $\mathcal H^{\otimes2}$ preserving cyclicity is not
characterised here); "$\omega_2=\omega_1^{\otimes2}$ is the natural choice, full
uniqueness open."

### R2.Verdict on DC6

**(b) DC6-stands.** In the physical $N_{\mathrm{gh}}$ parametrization, the naive
$\omega_2=\omega_1^{\otimes2}$ is graded **symmetric**, not antisymmetric (R2.10,
toy P1). It is therefore not graded antisymmetric on the physical $\mathcal H^{\otimes2}$, and even in every grading $\epsilon+c$ (D4.9). The graded-antisymmetric object is $\omega_2^{\rm symp}$, $\omega_2$ read on $\big(\mathcal H^{\otimes2}\big)[1]$ (one shift of the whole $\Sigma$), an even symplectic form — equivalently, $\omega_1^{\otimes2}$ is the
physical **symmetric** pairing $G_2$ (the cobracket/$\mathfrak p_{1,2,0}$-side,
graded symmetric in physical statistics — consistent with R5's odd *suspended* degree
$|\mathfrak p_{1,2,0}|=-1$ under the step-4 dictionary), and its graded-antisymmetric (even)
partner is obtained by the one-unit suspension (a presentation choice). The previous "DC6 is a grading artefact" was **half right**:
the *count* (one shift of the whole $\Sigma$) is what graded antisymmetry requires, but the *physical symmetry type*
of $\omega_1^{\otimes2}$ is symmetric, so DC6's worry — that the naive object has the
wrong symmetry for a symplectic form — is **vindicated, not dissolved**. The naive
$\omega_2=\omega_1^{\otimes2}+\cdots$ guess is symmetric; promoting it to a symplectic
form *requires* the degree shift, which is a genuine structural choice, not a no-op; the result is even; an odd (BV) $\Sigma$-pairing needs a grading whose parity is not a function of $\epsilon$ (R36).

### R2.Symbolic verification (physical-grading toy + n=3)

Script: `codes/verify-omega2-physical.py` (sympy 1.14.0). The toy is graded by the
**physical** parity $\epsilon=N_{\mathrm{gh}}\bmod2$; the suspension appears only as a
*conditional* relabelling in check **Dict** (the BV-presentation choice).
$\dim\mathcal H=4$, $N_{\mathrm{gh}}=[2,3,2,3]$, $\epsilon=[0,1,0,1]$, $\omega_1$
pairing $N_{\mathrm{gh}}=2\leftrightarrow3$.

| ID | Checks | Method | Outcome | Scope |
| --- | --- | --- | --- | --- |
| P0a/b | $\omega_1$ graded-antisym (physical) & non-degenerate | build & simplify | PASS | toy $\omega_1$ — *Correction 2026-09-26 (record 055): models the toy's $s=-1$, the wrong physical sign (physical is $s=+1$, graded symmetric; 055 B3.4)* |
| Sup1p/p' | $\omega_1$ pairs only ghost-saturating states; parity correlation $\epsilon(A)+\epsilon(B)$ constant $=1$ on support | scan support | PASS | models R2.4–R2.5 |
| **P1** | **DECISIVE:** $\omega_2=W$ graded-**SYMMETRIC** in physical parity, $W(Y,X)=(-1)^{\epsilon(X)\epsilon(Y)}W(X,Y)$ (sym-viol $0$, anti-viol $16$) | count grade violations | PASS | the DC6 verdict (b); tests exactly R2.10 |
| P2 | $W$ vanishes off support (non-saturating slot) | scan $192$ off-support entries | PASS | makes P1 everywhere |
| Dict | demanding graded antisymmetry in a uniform grading $\epsilon+c_s$ forces $c_s=1$; the form stays even (D4.9) — a presentation **choice**, not a fact about $\Sigma$ | scan both shifts | PASS | reconciles $s^{-2}$ |
| Det | $\det\omega_2=(\det\omega_1)^{2\dim\mathcal H}$ | matrix det | PASS | finite-dim only |
| **Rob** | $\omega_2=W$ graded-**symmetric** also for EVEN saturation ($N_{\mathrm{gh}}$ sum $4$, same-parity pairing) | second toy, count violations | PASS | verdict (b) robust to anomaly value |
| Cyc-a/b | $V_4$ fully graded-sym; $m_2$ cyclic $W(X,m_2Y)=W(m_2X,Y)$, no $\ell_3$ | $m_2=W^{-1}V_4$, compare | PASS | cyclicity $\neq$ R6 |
| n3 | $\omega_3=\omega_1^{\otimes3}$ physical exchange + suspended shift | count violations on $\mathcal H^{\otimes3}$ | PASS (informational) | **preliminary** |

**n=3 finding (preliminary).** $\omega_3=\omega_1^{\otimes3}$ is graded **symmetric**
in physical parity (sym-viol $0$, anti-viol $64$); both suspended shifts $c_s\in\{0,1\}$
give antisym-viol $0$ on this particular toy (degenerate because all support states
share the same parity pattern), so the $n=3$ suspended count is **not** fixed by this
toy alone — flagged preliminary, consistent with $n>2$ kept open. The robust $n=3$
statement is only the **physical symmetry** ($\omega_3$ symmetric); the suspended
relabelling for $n=3$ needs a richer toy.

*Correction 2026-09-26 (record 055, critic-055-20260926T032500):* "(sym-viol $0$,
anti-viol $64$)" above is a transcription error against the script's own output and
its own next sentence. The script's re-run (055 C3.2) prints **sym-viol $64$,
anti-viol $0$** under the script's $s=-1$ toy — i.e. graded **antisymmetric** under
that toy's (wrong) sign convention, consistent with 055's general-$k$ law (B1) at
$k=3$: on support $\omega_3(Y,X)=s^3\omega_3(X,Y)=s\,\omega_3(X,Y)$. Under the
physical $s=+1$, $\omega_3$ is symmetric, matching the physical conclusion this
paragraph states in prose.

**Scope note (no over-claim).** The toy verifies the **sign/parity algebra** under
the physical statistics (R2.1, R2.4–R2.6); it does **not** compute the worldsheet
$c_0^-$, $\ell_3$, $V_4$ on the level-matched $\mathcal H$, nor prove the
abstract closed-string statement — that is an independent CFT-level / numerical-verifier
task. The decisive physical fact P1 (symmetric) is robust to the saturation parity:
the committed script tests both the physically correct odd saturation
($N_{\mathrm{gh}}$ sum $=5$, opposite-parity pairing, P1) **and** an even saturation
($=4$, same-parity pairing, check **Rob**); $\omega_2=W$ is graded symmetric in both.
This shows the verdict hinges only on the **two** $c_0^-$ being even-as-operation, not
on the precise sphere anomaly value.

---

## Revision-0/1 (superseded for the sign verdict; suspended-grading argument)

> **Superseded note.** Everything below uses the *suspended* grading and concludes
> $\omega_2$ is antisymmetric "on the suspended $\mathcal H^{\otimes2}$." Revision-2
> shows that conclusion is the *suspended-presentation* statement; in the **physical**
> grading $\omega_2=\omega_1^{\otimes2}$ is **symmetric** (R2.10). The support
> argument, the $\det$ exponent $2\dim\mathcal H$, the cyclicity-$\neq$-R6 finding,
> and the brief-candidate-is-a-no-op finding below remain correct and are reused. The
> headline "DC6 is a grading artefact / the result stands" is **withdrawn** in favour
> of Revision-2's verdict (b).

---

### (legacy header) Revised 2026-06-24 after blind-critic REVISE

The result stands; the central sign
step is now stated as a conditional lemma + support argument (the support of
$\omega_2$ forces $a+b$ even on every non-zero entry), the off-support vanishing of
$W$ is verified explicitly (Sup2), the determinant exponent is corrected to
$2\dim\mathcal H$, and cyclicity is kept distinct from the $(2,2,0)$ relation R6.

This record constructs the two-output symplectic form
$\omega_2:\mathcal H^{\otimes2}\otimes\mathcal H^{\otimes2}\to\mathbb C$ for the
auxiliary field $\Sigma\in\mathcal H^{\otimes2}$, resolving open-question Q1 /
draftcomment DC6 of `knowledge/cubic-sft-overview.tex`. The acceptance criteria
are: $\omega_2$ graded antisymmetric, non-degenerate, and rendering
$m_2=\mathfrak p_{2,2,0}=\Delta\circ\ell_3$ cyclic w.r.t.
$\omega=\omega_1+\omega_2$. Ledger results **R5** and **R6** are reused verbatim;
$\ell_3=\mathfrak p_{3,1,0}$ is **not** inserted into the $(2,2,0)$ relation.

The central finding overturns the premise of the DC6 draftcomment in one precise
way: $\omega_2=\omega_1^{\otimes2}$ is the **correct** form once the suspension
grading is tracked; the "wrong sign symmetry" of $\omega_1^{\otimes2}$ is an
artefact of using the un-suspended (internal) grading. No antisymmetrisation and
no correction terms are required. The construction is unique given the vertex
pairing.

---

## Setup

### Assumptions and conventions

- **Sector.** Classical $g=0$, order $g_s^2$ (quartic truncation), $n=2$
  ($\Sigma\in\mathcal H^{\otimes2}$). SFT conventions of Erbin (2023); metric
  $(-,+,+,+)$, $\hbar=c=1$, $\alpha'$ explicit; bra–ket.
- **Single-string symplectic form.** From WBEIHWFU App. A (Münster–Sachs),
  $$\omega_1(A,B)=\langle A\,|\,c_0^-\,|\,B\rangle_{\mathrm{bpz}},\qquad
  \omega_c=(\cdot,c_0^-\cdot)_{\mathrm{bpz}}\circ(s^2\otimes s^2).\tag{S.1}$$
  $\omega_1$ is **odd** and **graded antisymmetric**,
  $\omega_1(A,B)=-(-1)^{|A||B|}\omega_1(B,A)$, and non-degenerate on the
  level-matched space $\mathcal H\cap\ker L_0^-\cap\ker b_0^-$. Its oddness is
  carried by the **single** $c_0^-$ insertion (a Grassmann-odd, ghost-number-$1$
  mode): the bare BPZ pairing $\langle A|B\rangle_{\mathrm{bpz}}$ is even
  (graded-symmetric for ghost-saturating states), and one $c_0^-$ flips it to odd
  antisymmetric. The inverse is $\Delta=\omega_1^{-1}$ (note `eq:V4ell3`).
- **Level-matching (Harold's correction).** Every field, physical or auxiliary,
  lives in $\ker L_0^-\cap\ker b_0^-$; $\omega_2$ is defined on the level-matched
  $\mathcal H^{\otimes2}$. No "$\ker L_0^-$ complement" restriction is imposed.
- **Suspension.** CFL build $E_kC$ on $C[1]$; Münster–Sachs place fields in
  degree zero after $A_c=s^{-2}\tilde A_c$ (review caveats; note "Convention
  traps"). The symplectic form on the suspended complex is odd. **Crucially**,
  $\Sigma\in\mathcal H^{\otimes2}$ is a **single** field of the enlarged complex:
  it carries **one** suspension unit, not one per $\mathcal H$-factor. Its
  suspended parity is
  $$|X|_s=\big(|x_1|+|x_2|+1\big)\bmod 2,\qquad X=x_1\otimes x_2,\tag{S.2}$$
  where $|x_i|$ is the (suspended) parity of the $\mathcal H$-factor. The "$+1$"
  is the extra odd suspension unit of the $\Sigma$-field.

### Component expansion of Σ (note `eq:Sigexpand`)

$$\ket{\Sigma}=\sum_{r,s}\!\int\!\frac{\mathrm d^Dk_1}{(2\pi)^D}\frac{\mathrm d^Dk_2}{(2\pi)^D}\,
\sigma_{rs}(k_1,k_2)\,\ket{\phi_r(k_1)}\otimes\ket{\phi_s(k_2)},\qquad
N_{\mathrm{gh}}(\Sigma)=4.\tag{S.3}$$
Two copies of the $N_{\mathrm{gh}}=2$ field $\Psi$. The component label
$I=(r,k_1;s,k_2)$ runs over a basis of $\mathcal H^{\otimes2}$; below I write
$X=x_1\otimes x_2$ for a generic basis element.

### Building blocks (brief, step 2)

- $\omega_1$ and its inverse $\Delta$ on each $\mathcal H$-factor.
- The **product form**
  $$W:=\omega_1\otimes\omega_1,\qquad
  W(x_1\otimes x_2,\,y_1\otimes y_2)=(-1)^{|x_2||y_1|}\,\omega_1(x_1,y_1)\,\omega_1(x_2,y_2),\tag{S.4}$$
  with the Koszul sign for reordering $x_2$ past $y_1$.
- The graded **swap** $\tau$ of the two $\mathcal H$-slots,
  $\tau(u\otimes v)=(-1)^{|u||v|}v\otimes u$, with pull-back
  $(\tau^\ast W)(X,Y)=W(\tau X,\tau Y)$.
- The $c_0^-$ insertion already carried by each $\omega_1$.

### The two-output product m₂ (note `eq:mtwo`, `eq:V4ell3`)

$$m_2\equiv\mathfrak p_{2,2,0}=\Delta\circ\ell_3:\mathcal H^{\otimes2}\to\mathcal H^{\otimes2},\qquad
N_{\mathrm{gh}}(m_2)=-2,\tag{S.5}$$
defined by raising the first index of $\ell_3:\mathcal H^{\otimes3}\to\mathcal H$
with $\Delta$. Equivalently, with the product pairing $W$,
$$W\big(A_1\otimes A_2,\,m_2(A_3,A_4)\big)=V_4(A_1,A_2,A_3,A_4)
=\langle A_1|\ell_3(A_2,A_3,A_4)\rangle.\tag{S.6}$$
$V_4$ is **fully graded-symmetric** in its four arguments (closed cyclic vertex).
**R6 is respected**: $\ell_3=\mathfrak p_{3,1,0}$ enters only *after* $(2,2,0)$ in
the signature ordering, so it does not appear in the $(2,2,0)$ cyclicity relation.

---

## Derivation

### Parity of the product form (the DC6 obstruction, made precise)

$\omega_1$ is odd. The product $W=\omega_1\otimes\omega_1$ inserts $c_0^-$
**twice**, hence is **even**. An even bilinear form built from two odd
antisymmetric factors is graded **symmetric** in the *internal* grading $|X|_i$:

$$W(Y,X)=(-1)^{\,|X|_i\,|Y|_i}\,W(X,Y),\qquad |X|_i=(|x_1|+|x_2|)\bmod 2.\tag{D.1}$$

Reading $\omega_2=\omega_1^{\otimes2}$ as a form on the *un-suspended*
$\mathcal H^{\otimes2}$ therefore gives the **wrong** (symmetric) exchange
symmetry. This is exactly the obstruction recorded as DC6 and as note open-Q1.

### Resolution: the suspended grading, via a support argument

The symplectic form lives on the **suspended** complex, where the field $\Sigma$
carries one extra odd unit (S.2). Re-grading by $|X|_s=|X|_i+1$, the sign required
for antisymmetry is $-(-1)^{|X|_s|Y|_s}$; matching it against the actual exchange
rule (D.1) reduces to the sign identity

$$(-1)^{\,|X|_i|Y|_i}\overset{?}{=}-(-1)^{\,(|X|_i+1)(|Y|_i+1)}.\tag{D.2, conditional}$$

**Equation (D.2) is conditional, not an identity.** With $a=|X|_i$, $b=|Y|_i\in\{0,1\}$,
expanding $(a+1)(b+1)=ab+a+b+1$ gives
$$-(-1)^{(a+1)(b+1)}=(-1)^{ab}\,(-1)^{a+b},$$
so (D.2) holds **iff $a+b$ is even** — true for $(a,b)=(0,0),(1,1)$, **false** for
the mixed cases $(1,0),(0,1)$. The bare assertion "(D.2) for all $a,b$" is *wrong*;
it must be supplemented by a support argument.

The support argument is the actual core of the proof. Because $\omega_1$ is
**odd**, it pairs only states of opposite suspended parity:
$\omega_1(x_i,y_i)\neq0\Rightarrow |x_i|+|y_i|$ **odd**. For
$W=\omega_1\otimes\omega_1$ to be non-zero this must hold in **both** slots, whence
$$\big(|x_1|+|y_1|\big)+\big(|x_2|+|y_2|\big)\ \text{even}
\;\Longleftrightarrow\; a+b=|X|_i+|Y|_i\ \text{even}.\tag{D.2′}$$
Consequently:

- **On** $\operatorname{supp}(\omega_2)$: $a+b$ even, (D.2) holds, and
  $\omega_2(Y,X)=-(-1)^{|X|_s|Y|_s}\,\omega_2(X,Y)$.
- **Off** $\operatorname{supp}(\omega_2)$ (mixed parity, $a+b$ odd): $W=0$, so both
  sides of the antisymmetry relation vanish identically ($0=0$).

The two cases together give graded antisymmetry on **all** of
$\mathcal H^{\otimes2}\otimes\mathcal H^{\otimes2}$ — non-trivially on the support,
vacuously off it:

> **SUPERSEDED (symmetry headline withdrawn).** The box (D.3) below states the
> *suspended-presentation* antisymmetry. In the **physical** grading the exchange
> relation is the graded-**symmetric** R2.10, $W(Y,X)=(-1)^{\epsilon(X)\epsilon(Y)}W(X,Y)$;
> the antisymmetric form is the BV-presentation partner $\omega_2^{\rm symp}=W\circ(s\otimes s)$.
> Read (D.3) as the suspended/BV presentation only.

$$\boxed{\;\omega_2=\omega_1\otimes\omega_1\quad\text{on the suspended }\mathcal H^{\otimes2},\quad
\omega_2(Y,X)=-(-1)^{|X|_s|Y|_s}\,\omega_2(X,Y).\;}\tag{D.3, suspended presentation; superseded}$$

No antisymmetrisation, no correction terms, no extra operator insertion are
needed. The "$\cdots$" of the note guess $\omega_2=\omega_1^{\otimes2}+\cdots$ is
empty; the content of DC6 is the suspension bookkeeping (D.3), made rigorous by the
support argument (D.2′) — **not** the bare unconditional identity (D.2), which is
false off support.

### Fate of the brief's candidate

The brief proposed $\omega_2=\tfrac12(W-\tau^\ast W)$. In the Koszul convention
(S.4), $\tau^\ast W\neq W$, so the candidate is non-zero and non-degenerate; but
it has the **same symmetry class** as $W$ — graded antisymmetric in the suspended
grading, graded symmetric in the internal grading (verified, W3). The
$\tau$-antisymmetrisation is therefore a **no-op at the level of the symmetry
type**: it cannot turn an internally-symmetric form into an internally-
antisymmetric one, because parity is set by the number of odd ($c_0^-$)
insertions, not by symmetrisation. This confirms that the fix is the grading, and
disposes of the antisymmetrisation route.

### Cyclicity of m₂ — distinct from the (2,2,0) structure equation R6

Cyclicity of $m_2$ w.r.t. $\omega=\omega_1+\omega_2$ on the $\mathcal H^{\otimes2}$
sector is the statement that $m_2$ is self-adjoint w.r.t. $\omega_2=W$:
$$W\big(X,\,m_2 Y\big)=W\big(m_2 X,\,Y\big),\qquad X,Y\in\mathcal H^{\otimes2}.\tag{D.4}$$
By the defining relation (S.6), $W(X,m_2 Y)=V_4(x_1,x_2,y_1,y_2)$. Self-adjointness
(D.4) is thus equivalent to the **pair-exchange symmetry** of $V_4$,
$$V_4(x_1,x_2,y_1,y_2)=(-1)^{\,|X|_i|Y|_i}\,V_4(y_1,y_2,x_1,x_2),\tag{D.5}$$
which holds because $V_4$ is **fully** graded-symmetric. Hence $m_2$ is cyclic.
**Cyclicity follows from the graded symmetry of $V_4$ alone** — it is a property of
the pairing $\omega_2$ and the vertex, requiring nothing beyond (D.5).

**Cyclicity is not the $(2,2,0)$ structure equation R6.** These are two distinct
statements and must not be conflated:

- *Cyclicity* (D.4): $m_2$ is self-adjoint for the form $\omega_2$. A symmetry
  property of the bilinear pairing, proved here from (D.5).
- *The $(2,2,0)$ relation* (R6, note `eq:IBLrels`):
  $\hat{\mathfrak p}_{1,1,0}\!\circ_1\!\mathfrak p_{2,2,0}+\mathfrak p_{2,2,0}\!\circ_1\!\hat{\mathfrak p}_{1,1,0}
  +\mathfrak p_{1,2,0}\!\circ_1\!\mathfrak p_{2,1,0}+\hat{\mathfrak p}_{2,1,0}\!\circ_1\!\hat{\mathfrak p}_{1,2,0}=0$,
  i.e. $m_2=\mathfrak p_{2,2,0}$ is a $Q$-homotopy ($Q$-exact, $=-[Q,\mathfrak p_{2,2,0}]$,
  **not** zero) for the cobracket–bracket composition. This is a relation among the
  IBL operations $Q,\ell_2$, the cobracket, and $m_2$ — a statement about the
  master equation, **not** about the symmetry of $\omega_2$.

R6 is **reused verbatim** and not re-derived here. The cyclicity check (D.4)/(D.5)
uses **only** $V_4$ (equivalently $W$ and $m_2$); $\ell_3=\mathfrak p_{3,1,0}$ is
never inserted, consistent with the signature ordering of R6 (which places
$(2,2,0)\prec(3,1,0)$). Cyclicity and R6 are independent acceptance facts that the
construction satisfies; neither implies the other.

### Uniqueness

Given the vertex pairing $W=\omega_1\otimes\omega_1$ that **defines** $m_2$ and
$V_4$ (S.6) — i.e. given that the kinetic term of $\Sigma$ in $S_{\mathrm{HS}}$ is
$-\tfrac{g_s^2}{4!}V_4(\Sigma,\Sigma)=-\tfrac{g_s^2}{4!}W(\Sigma,m_2\Sigma)$ —
the symplectic form $\omega_2$ must be $W$ (composed with the suspension iso that
sets the parity). Any other graded-antisymmetric non-degenerate form $\omega_2'$
differs from $W$ by an $m_2$-cyclic automorphism of $\mathcal H^{\otimes2}$; the
requirement that the action $S=\omega\circ\hat{\mathfrak p}(e^\Psi)$ reproduce the
HS kinetic term fixes $\omega_2'=W$. No free parameter remains beyond the overall
normalisation already carried by $\omega_1$.

---

## Commentary

- **(S.1)–(S.2).** The whole resolution turns on a single bookkeeping fact: the
  *oddness* of $\omega_1$ comes from the $c_0^-$ insertion, while the *grading* on
  the symmetric/cyclic complex comes from the suspension. These are two different
  $\mathbb Z_2$-data. $W$ has even $c_0^-$-parity but is graded antisymmetric once
  $\Sigma$ is counted as one suspended field. Mixing the two — counting two
  suspensions (one per $\mathcal H$) instead of one, or forgetting the suspension
  — produces the spurious "wrong symmetry" of DC6.
- **(D.2)/(D.2′).** The sign step $(-1)^{ab}=-(-1)^{(a+1)(b+1)}$ is **conditional**
  — it holds iff $a+b$ is even and fails for mixed parity. The proof does **not**
  rely on it unconditionally: the support of $\omega_2$ forces $a+b$ even on every
  non-zero entry (D.2′), because each $\omega_1$ pairs only opposite-parity states.
  On support the (correct, restricted) identity applies; off support $W=0$ and the
  relation is $0=0$. The algebraic content is that adding *one* odd suspension unit
  to each argument flips the exchange sign **on the support** — which is why one
  extra suspension unit (not two, nor zero) is exactly right.
- **(D.4)–(D.5).** The cyclicity of $m_2$ is **inherited** from the
  graded-symmetry of the closed cyclic vertex $V_4$; it is not an extra condition
  on $\omega_2$ once $\omega_2=W$. This is the cleanest possible outcome: the
  acceptance criteria (antisymmetry, non-degeneracy, cyclicity) are all met by the
  single natural object $W$, with the suspension supplying the parity.
- **Generalisation to $\mathcal H^{\otimes n}$ (structural, with a caveat).** For a
  single suspended field in $\mathcal H^{\otimes n}$, suspended parity
  $|X|_s=(\sum_i|x_i|+1)\bmod 2$, and $\omega_n=\omega_1^{\otimes n}$ inserts
  $c_0^-$ $n$ times. The support argument carries over: $\omega_n\neq0$ forces
  $|x_i|+|y_i|$ odd in each of the $n$ slots, so on support
  $|X|_i+|Y|_i\equiv n\pmod 2$. The exchange parity of the **bare** form $\omega_n$
  is **not uniform in $n$**: a finite-dimensional toy check ($\dim\mathcal H=4$,
  `scratchpad`) finds $\omega_2$ graded-**symmetric** in the internal grading (as
  in the main text), but $\omega_3$ already graded-**antisymmetric** in the
  internal grading, because the full slot-reversal of three odd factors plus the
  Koszul signs flips the parity relative to two. Both $\omega_2$ and $\omega_3$
  come out graded-**antisymmetric in the suspended grading** on their toys, but via
  *different* internal parities — so the single-suspension argument must be checked
  $n$ by $n$, not asserted once. Hence the construction generalises *structurally*
  (same support mechanism) while the parity bookkeeping is $n$-dependent; a full
  proof for $n>2$ — including the cyclicity of the higher $\mathfrak p_{k,k,0}$ and
  the $n$-parity of $\omega_n$ — is **not** carried out here (kept open).

---

## Result (Revision-0/1 — superseded for the symmetry headline; see Revision-2 Result above)

> **SUPERSEDED (symmetry headline withdrawn).** The boxed object and the
> "graded antisymmetric in the suspended grading" wording below are the
> *suspended/BV-presentation* statement. The authoritative physical result is in
> the Revision-2 Result block above: $\omega_2=\omega_1^{\otimes2}$ is graded
> **symmetric** in physical statistics (R2.10), and the antisymmetric symplectic
> form is the degree-shift partner $\omega_2^{\rm symp}=\omega_1^{\otimes2}\circ(s\otimes s)$.

$$\boxed{\;
\omega_2=\omega_1\otimes\omega_1\ \big(=\,(\cdot,c_0^-\cdot)_{\mathrm{bpz}}^{\otimes2}\big)
\ \text{on the suspended }\mathcal H^{\otimes2},\qquad
\omega=\omega_1+\omega_2.
\;}$$

In components, with $X=x_1\otimes x_2$, $Y=y_1\otimes y_2$,
$$\omega_2(X,Y)=(-1)^{|x_2||y_1|}\,\omega_1(x_1,y_1)\,\omega_1(x_2,y_2),$$
graded antisymmetric in the suspended grading **on its support** (S.2) [superseded:
physically graded *symmetric*, R2.10], via the
support argument (D.2′); non-degenerate, with
$\det\omega_2=\det(\omega_1\otimes\omega_1)=(\det\omega_1)^{2\dim\mathcal H}\neq0$
(the standard determinant of a self-tensor-product: each factor contributes
$(\det\omega_1)^{\dim\mathcal H}$); and rendering $m_2=\mathfrak p_{2,2,0}$ cyclic
via (D.4).

### What is established vs. open

**Established (toy-verified algebra) — Revision-0/1 wording, superseded headline.**

- $\omega_2=\omega_1^{\otimes2}$ is graded antisymmetric in the suspended grading,
  on its support; off support both sides vanish ($0=0$). The proof is the support
  argument (D.2′), **not** an unconditional sign identity. [SUPERSEDED: physically
  it is graded *symmetric* (R2.10); the antisymmetric form is the shift partner
  $\omega_2^{\rm symp}$.]
- DC6 is a grading artefact; no antisymmetrisation/correction term is needed.
  [SUPERSEDED: Revision-2 verdict is **(b) DC6 stands physically** — $\omega_1^{\otimes2}$
  is not antisymmetric in physical statistics.]
- $\omega_2$ is non-degenerate, $\det\omega_2=(\det\omega_1)^{2\dim\mathcal H}$.
- $m_2=\mathfrak p_{2,2,0}$ is **cyclic** w.r.t. $\omega_2$ (self-adjoint), as a
  consequence of the full graded symmetry of $V_4$. This is distinct from the
  $(2,2,0)$ structure equation R6, which is reused verbatim and not re-derived; the
  cyclicity check uses only $V_4$, with no $\ell_3=\mathfrak p_{3,1,0}$ insertion.
- Uniqueness given the vertex pairing.

**Open (not settled here).**

- The abstract closed-string statement: the toy verifies only the sign/grading
  algebra; the worldsheet content of $c_0^-$, $\ell_3$, $V_4$ on the level-matched
  $\mathcal H$ is modelled, not computed. An independent CFT-level check (e.g. on a
  truncated mode set, or against the explicit $\omega_c$ of WBEIHWFU) is the
  numerical-verifier's job.
- Non-degeneracy of $\omega_2$ **on the full level-matched** $\mathcal H^{\otimes2}$
  (the toy shows it follows from non-degeneracy of $\omega_1$, which holds on
  $\ker L_0^-\cap\ker b_0^-$; an infinite-dimensional subtlety is the same one as
  for $\omega_1$ itself).
- Extension to $\mathcal H^{\otimes n}$, $n>2$ (structural argument given; no
  proof).
- Invertibility of $m_2$ (note Q6 / DC1) — **deliberately kept open** (brief P6).

---

## Verification

Script: `codes/verify-omega2-construction.py` (sympy 1.14.0, **14/14 PASS**). Two
finite-dimensional graded toys ($\dim\mathcal H=4$, parities $[0,1,0,1]$ in the
script; a second pattern $[0,1,1,0]$ run as a robustness check, same verdict).
Each check is an internal algebraic self-check, **not** an independent
re-derivation of the closed-string result.

| ID  | Checks | Method | Outcome |
| --- | --- | --- | --- |
| W0a/b | $\omega_1$ odd graded-antisym & non-degenerate | build & simplify | PASS |
| **S1** | bare sign identity (D.2) is **conditional**: holds iff $a+b$ even; **fails** for $(1,0),(0,1)$ | enumerate $a,b\in\{0,1\}$ | PASS |
| **Sup1** | $\omega_1$ odd $\Rightarrow$ pairs only opposite-parity states | scan nonzero entries | PASS |
| **Sup2** | $W$ **vanishes off support**: every mixed-parity ($a+b$ odd) entry has $W=0$ | scan 128 off-support entries | PASS (0 nonzero) |
| **Sup3** | on $\operatorname{supp}(W)$: $a+b$ even for all 16 nonzero entries (so D.2 applies) | scan nonzero entries | PASS |
| W1 | $\omega_1^{\otimes2}$ graded-**symmetric** in internal grading on supp (DC6 obstruction) | count grade violations | PASS (sym 0, anti>0) |
| W2 | $\omega_2=\omega_1^{\otimes2}$ graded-**antisym** in suspended grading, **all entries** | count grade violations | PASS (anti 0, sym>0) |
| W3a/b | brief candidate $\tfrac12(W-\tau^\ast W)$ has same symmetry class as $W$, non-degenerate | count violations, $\det$ | PASS |
| W4 | $\omega_2$ non-degenerate, $\det=(\det\omega_1)^{2\dim\mathcal H}$ | matrix $\det$ vs $(\det\omega_1)^{2N}$ | PASS ($a^{16}b^{16}=(\det\omega_1)^{8}$) |
| W5a | generic $V_4$ fully graded-symmetric | $S_4$-symmetrise & simplify | PASS |
| W5b | $m_2=\mathfrak p_{2,2,0}$ **cyclic**: $W(X,m_2Y)=W(m_2X,Y)$ | $m_2=W^{-1}V_4$, compare 16×16 | PASS (0 nonzero) |
| W6 | cyclicity $\Leftrightarrow$ $V_4$ pair-exchange symmetry; uses only $V_4$, no $\ell_3$ (R6 untouched) | pair-exchange symmetry of $V_4$ | PASS |

**Scope per check (no over-claim).**

- **S1** verifies the *negative* fact that the bare sign step (D.2) is conditional
  and fails for mixed parity — it does **not** establish antisymmetry by itself.
- **Sup1–Sup3** verify the *support argument* that rescues the proof: $\omega_1$
  odd $\Rightarrow$ $W=0$ off support (Sup2, the 128 mixed-parity entries that W2
  alone never exercises), and $a+b$ even on support (Sup3). This is what makes W2's
  "all-entries" antisymmetry sound rather than vacuous-by-restriction.
- **W1/W2** verify the *parity arithmetic* of the product form: on its support, $W$
  is internally symmetric (DC6) and suspended-antisymmetric (resolution). W2 holds
  on all entries — non-trivially on support, vacuously ($0=0$) off it via Sup2.
- **W4** verifies non-degeneracy *as a matrix identity on the toy* ($\det\neq0$,
  exponent $2\dim\mathcal H$), **not** on the infinite-dimensional
  $\mathcal H^{\otimes2}$.
- **W5b/W6** verify the *cyclicity identity* $W(X,m_2Y)=W(m_2X,Y)$ as an algebraic
  consequence of $V_4$ being graded-symmetric. They verify **cyclicity**, which is
  distinct from the $(2,2,0)$ structure equation R6 ($Q$-exactness of $m_2$); R6 is
  reused, not re-derived. They do **not** prove $V_4$ is graded-symmetric in the
  actual CFT (the closed cyclic vertex property, assumed) nor that $m_2$ is
  invertible (open).
- The abstract closed-string statement is **not** proven by the toy; the toy tests
  the algebraic/sign identities only. An independent CFT-level cross-check is the
  numerical-verifier's job.

## Status

R2.6 is superseded by record 055 (critic-055-20260926T032500, 2026-09-26): $\omega_1$
is graded **symmetric** ($s=+1$), not antisymmetric; see the dated corrections above
at R2.6, the step-4 dictionary row, P0a, and the n=3 finding. R2.10 ($k=2$) stands
unaffected. Step-4 dictionary redone 2026-09-26 against the BV odd symplectic form
$\Omega_1=(-1)^{\lvert A\rvert}\langle A,B\rangle$ (step 4′, (D4.1)–(D4.9);
`codes/verify-002-dictionary.py` 35/35 PASS): $\Omega_1$ graded antisymmetric in both
gradings (odd symplectic), $\omega_1$ graded symmetric in both; $\Omega_2$ and $\omega_2$
graded symmetric in $\epsilon$ and in the strand-wise suspended degree, antisymmetric
only after one shift of the whole $\Sigma$ ($c_s=1$ stands), even in every uniform
grading; order reversal leaves $s$ unchanged on the zero-mode sector only. Open: none in this record's convention trail; R7's suspended-degree clause
awaits the orchestrator's ledger edit.
