---
id: 029-morphism-check
agent: computator
brief: agent/briefs/active-computator-9b-morphism-20260914T051500.md
created: 2026-09-14T05:20
script: codes/verify-morphism-check.py
depends: R7, R8, R11; agent/derivations/026-linfty-to-ibl-repackaging.md §5.4 (5.23)
---

# 029 — The $L_\infty$-morphism relations for the comparison map $(\phi_1,\phi_2)$ at $O(g_s^2)$

**Literal task (T5 / plan Task 9b).** Write the $L_\infty$-morphism identities, order by order up to
three inputs, for the candidate comparison map $\phi=(\phi_1,\phi_2)$, $\phi_1=$ inclusion
$\mathcal H_0\hookrightarrow\mathcal H_0\oplus\mathrm{Sym}^2\mathcal H_0$, $\phi_2=\cdot^{\otimes2}$
into the $\mathrm{Sym}^2$ summand, between the quartic-truncated cyclic $L_\infty$ algebra
$(\mathcal H_0;Q,\ell_2,\ell_3)$ and the algebra of presentation (b) read off `eq:SHS`. Decide the
direction, which $\phi_n$ are needed, whether $(\phi_1,\phi_2)$ alone can satisfy the identities,
and check on a toy. Uniqueness is not claimed.

**Motivating objective.** Settle in what precise sense the cubic (HS) theory and the
quartic-truncated $L_\infty$ theory are equivalent: an $L_\infty$ (quasi-)morphism — which direction,
which components — or only equality on shell (R8) plus the gauge map (R11).

## §0 Verdict table

| Question | Verdict (details in §2) |
|---|---|
| Direction | The candidate is $F:\ \text{truncated}\to\text{enlarged}$, $\Psi\mapsto(\Psi,\Psi^{\otimes2})$ — the on-shell value of $\Sigma$ (R8). The reverse direction is the projection $\pi(\Psi,\Sigma)=\Psi$; see §2.5. |
| Identity, 1 input | Holds: $\phi_1=\iota$ is a chain map ($\tilde\ell_1\iota=\iota Q$). |
| Identity, 2 inputs | $\mathcal H_0$-component holds. $\mathrm{Sym}^2$-component **fails at $O(g_s^0)$**: LHS $\equiv0$, RHS $=\phi_2(Q\Psi_1,\Psi_2)+\phi_2(\Psi_1,Q\Psi_2)\neq0$. Cause: $\Sigma$ has no $Q$-kinetic term, so $\tilde\ell_1|_{\mathrm{Sym}^2}\propto g_s^2 m_2$ is not $\hat Q$. |
| Identity, 3 inputs | $\mathcal H_0$-component holds exactly (this is R8's $\Psi$-EOM identity, polarised). $\mathrm{Sym}^2$-component fails again at $O(g_s)$: $\phi_2(\ell_2(\Psi,\Psi),\Psi)$ unmatched (no $\tilde\ell_3$, $\tilde\ell_2(\Psi,\Sigma)$ lands in $\mathcal H_0$). |
| Components needed | For any $\phi_2$ with $\phi_1=\iota$ the two-input $O(g_s^0)$ identity forces $\phi_2^{\mathrm{Sym}^2}|_{g^0}$ to be $\hat Q$-closed (proof: $\phi_3$ cannot enter at two inputs; the operator mismatch $\hat Q$ vs $m_2$ is convention-independent). That a $\hat Q$-closed $\phi_2$ is then incompatible with the three-input $\mathcal H_0$ identity even with a $\phi_3$ is a generic-data argument (§2), not tested on the toy ($\phi_3=0$, $\phi_2^{\mathcal H_0}=0$ in check F). |
| On-shell vs strict | Not a strict $L_\infty$-morphism. The full defect equals $dF|_\Psi[\mathcal L(\Psi)]$ restricted to $\mathrm{Sym}^2$, i.e. it is proportional to the truncated EOM: $F$ maps Maurer–Cartan elements to Maurer–Cartan elements (R8) and intertwines gauge transformations through the composite law (R11), and that is all. |
| Grading caveat | $Q$ raises $N_{\rm gh}$ by 1, $m_2$ by 2, so $\tilde\ell_1=Q\oplus(-\tfrac{g_s^2}{12}m_2)$ is homogeneous neither in $N_{\rm gh}$ nor in the parity $N_{\rm gh}\bmod2$ (R7's uniform shift does not change this). With $\deg_{\mathcal H_0}=N_{\rm gh}-2$, $\deg_{\mathrm{Sym}^2}=(N_{\rm gh}-4)/2$ every bracket of (1.5) has degree $+1$ and $\omega_2$ degree $-1$ on the classical complex ($\mathcal H_0$ at gh $\{2,3\}$, $\mathrm{Sym}^2$ at gh $\{4,6\}$): there every bracket of (1.5) has degree $+1$ and $\omega_2$ degree $-1$, so the $L_\infty$ structure of 026 §5.4 is $\mathbb Z$-graded cyclic on the classical complex, in the $O(g_s^3)$-truncated sense of assumption (i). Off the classical complex no ghost-number-based $\mathbb Z$ or $\mathbb Z_2$ grading of $\mathrm{Sym}^2$ makes (1.5) homogeneous (§1 (ii); script check G). All "holds" in this table are in the $O(g_s^3)$-truncated sense. |

## §1 The two algebras and the candidate map

\subsection*{Setup — conventions}

Physical ghost number throughout: $N_{\rm gh}(\Psi)=2$, $N_{\rm gh}(\Sigma)=4$, both Grassmann-even;
$Q$ has $N_{\rm gh}=+1$, $\ell_n$ has $N_{\rm gh}=3-2n$, $m_2$ has $N_{\rm gh}=+2$. Pairings:
$\omega_1(A,B)=\langle A|c_0^-|B\rangle_{\rm bpz}$ on $\mathcal H_0$, $\omega_2=\omega_1^{\otimes2}$ on
$\mathrm{Sym}^2\mathcal H_0$ (graded symmetric in physical statistics, R7; the cyclic grading used in this record is (1.7);
R7's parity shift $\omega_2^{\rm symp}$ is not used here). Vertices $V_3(A,B,C)=\omega_1(A,\ell_2(B,C))$, $V_4(A,B,C,D)=\omega_1(A,\ell_3(B,C,D))$;
$V_4(A_2,B_2)=\omega_2(A_2,m_2B_2)$ for $A_2,B_2\in\mathrm{Sym}^2\mathcal H_0$, so that
$m_2=\Delta\circ\ell_3$ with $\Delta=\omega_1^{-1}$ (R8). $g\equiv g_s$.

**Suspension, shown once.** An $L_\infty$-morphism is a family $\phi_n:\ (sV)^{\odot n}\to sW$ of
degree $0$ between the suspended, graded-symmetric coalgebras, commuting with the codifferentials.
For even inputs (fields $\Psi$ of even $N_{\rm gh}$, formal even coefficients) the suspension signs are
trivial and the whole system of identities is equivalent to a single generating-function identity
(the device of 026 §3: $L_\infty$ identities on all inputs $\Leftrightarrow$ identities of even
superfields with formal even coefficients). With
$$\mathcal L(\Psi):=\sum_{n\ge1}\frac{g^{n-1}}{n!}\ell_n(\Psi^n),\qquad
F(\Psi):=\sum_{n\ge1}\frac1{n!}\phi_n(\Psi^n),\qquad
\tilde{\mathcal L}(\Phi):=\sum_{n\ge1}\frac1{n!}\tilde\ell_n(\Phi^n),\tag{1.1}$$
$\phi$ is an $L_\infty$-morphism iff
$$\boxed{\ \tilde{\mathcal L}\big(F(\Psi)\big)=dF\big|_\Psi\big[\mathcal L(\Psi)\big]
=\sum_{n\ge0}\frac1{n!}\phi_{n+1}\big(\mathcal L(\Psi),\Psi^n\big)\ }\tag{1.2}$$
for all even $\Psi$ (push-forward of the homological vector field). Expanding (1.2) in the number
of $\Psi$'s gives the identities at $1,2,3,\dots$ inputs; the odd-input sectors (gauge parameters
$\Lambda$, $N_{\rm gh}=1$) follow by polarisation with odd formal coefficients and carry only
the suspension signs. All statements below are in this even-polarised form.

\subsection*{The truncated algebra $\mathsf T$}

$\mathsf T=(\mathcal H_0;\,Q,\ell_2,\ell_3)$, cyclic w.r.t. $\omega_1$, $L_\infty$ to the order
needed ($[Q,\ell_3]+\ell_2\circ_1\ell_2=0$; $\ell_4$ and higher dropped). None of the identities
(2.1)–(2.7) uses these relations, and the toy of §3 does not impose them; the no-repair argument of §2
does invoke $[Q,\ell_3]\neq0$ "for generic data", so its genericity is partly that of non-$L_\infty$
data — one more reason it is Argued, not proven. Action and EOM
$$S_{\rm eff}=\tfrac12\omega_1(\Psi,Q\Psi)+\tfrac g{3!}V_3(\Psi^3)+\tfrac{g^2}{4!}V_4(\Psi^4),\qquad
\mathcal L(\Psi)=Q\Psi+\tfrac g2\ell_2(\Psi,\Psi)+\tfrac{g^2}6\ell_3(\Psi,\Psi,\Psi).\tag{1.3}$$

\subsection*{The enlarged algebra $\mathsf E$ (presentation (b))}

Field $\Phi=(\Psi,\Sigma)\in\mathcal H_0\oplus\mathrm{Sym}^2\mathcal H_0$. From `eq:SHS`,
$$S_{\rm HS}=\tfrac12\omega_1(\Psi,Q\Psi)+\tfrac g6V_3(\Psi^3)-\tfrac{g^2}{24}\omega_2(\Sigma,m_2\Sigma)
+\tfrac{g^2}{12}\omega_2(\Sigma,m_2\Psi^{\otimes2}),\tag{1.4}$$
and $V_4(\Sigma,\Psi^{\otimes2})=\omega_2(\Sigma,m_2\Psi^{\otimes2})=\omega_1(\Psi,\ell_3(\Sigma,\Psi))$,
where $\ell_3(\Sigma,\Psi)$ denotes $\ell_3$ with two slots filled by the strands of $\Sigma$.
Varying (1.4) and matching to $\tilde{\mathcal L}(\Phi)=\tilde\ell_1\Phi+\tfrac12\tilde\ell_2(\Phi,\Phi)$
(there is no $\tilde\ell_3$: the theory is cubic) gives the brackets of 026 §5.4 eq. (5.23):
$$\begin{aligned}
\tilde\ell_1(\Psi,\Sigma)&=\big(Q\Psi,\ -\tfrac{g^2}{12}m_2\Sigma\big),\\
\tilde\ell_2\big((\Psi,\Sigma),(\Psi,\Sigma)\big)&=\big(g\,\ell_2(\Psi,\Psi)+\tfrac{g^2}3\ell_3(\Sigma,\Psi),\ \tfrac{g^2}6m_2(\Psi^{\otimes2})\big),\\
\tilde\ell_1\Phi+\tfrac12\tilde\ell_2(\Phi,\Phi)&=\Big(Q\Psi+\tfrac g2\ell_2(\Psi,\Psi)+\tfrac{g^2}6\ell_3(\Sigma,\Psi),\ -\tfrac{g^2}{12}m_2\big(\Sigma-\Psi^{\otimes2}\big)\Big).
\end{aligned}\tag{1.5}$$
Polarised: $\tilde\ell_2(\Psi,\Sigma')=\tfrac{g^2}6\ell_3(\Sigma',\Psi)$ (in $\mathcal H_0$),
$\tilde\ell_2(A,B)|_{\mathrm{Sym}^2}=\tfrac{g^2}{12}m_2(A\otimes B+B\otimes A)$ for $A,B\in\mathcal H_0$,
$\tilde\ell_2(\Sigma,\Sigma)=0$. The last line of (1.5) is the pair of EOMs (R8).

**Two assumptions carried.** (i) $\tilde\ell_1^2=Q^2\oplus\tfrac{g^4}{144}m_2^2$: on the full
$\mathrm{Sym}^2\mathcal H_0$ this vanishes only mod $O(g^4)$ — consistent with "$L_\infty$ to $O(g^3)$"
(R11, 026 §5.4) — and exactly on the classical complex where $\Sigma$-sector states are kept at
$N_{\rm gh}\in\{4,6\}$ only. (ii) Grading. $Q$ raises $N_{\rm gh}$ by 1 (odd), $m_2$ raises the total
$N_{\rm gh}$ of a $\mathrm{Sym}^2$ state by 2 (even), so $\tilde\ell_1=Q\oplus(-\tfrac{g^2}{12}m_2)$ is
homogeneous neither in $N_{\rm gh}$ nor in the parity $N_{\rm gh}\bmod2$; R7's uniform one-unit shift
of the $\Sigma$-sector leaves $m_2$ even and does not help. The grading that works is the
*half* ghost number on $\mathrm{Sym}^2$:
$$\deg_{\mathcal H_0}=N_{\rm gh}-2,\qquad \deg_{\mathrm{Sym}^2}=\tfrac12(N_{\rm gh}-4).\tag{1.7}$$
On the classical complex — $\mathcal H_0$ at gh $\{2,3\}$ (fields, EOM slot), $\mathrm{Sym}^2$ at gh
$\{4,6\}$ (the truncation of assumption (i)) — every bracket of (1.5) has degree $+1$:
$Q$: gh $2\to3$, $0\to1$; $\ell_2$: $(2,2)\to3$, $0+0\to1$; $\tilde\ell_2(\Psi,\Sigma)=\tfrac{g^2}6\ell_3(\Sigma,\Psi)$:
$(4;2)\to3$, $0+0\to1$; $m_2$: gh $4\to6$, $0\to1$; $\tilde\ell_2(\Psi,\Psi)|_{\mathrm{Sym}^2}\propto m_2(\Psi^{\otimes2})$:
$(2,2)\to6$, $0+0\to1$. The pairings are nonzero only on $\deg A+\deg B=1$ ($\omega_1$: gh 2 with 3;
$\omega_2$: gh 4 with 6), i.e. both have degree $-1$. So on the classical complex every bracket of (1.5) has degree $+1$ and both pairings degree $-1$ —
the $L_\infty$ structure of 026 §5.4 is $\mathbb Z$-graded cyclic there, as $\mathsf T$ is — and all identities below are
$\mathbb Z$-graded identities there. Off the classical complex (1.7) fails in two ways. (a) On
odd-ghost-number $\mathrm{Sym}^2$ states — the composite gauge direction $\Lambda\otimes\Psi$ at gh 3, the
$\Lambda\otimes\Sigma$-type states — the degree is half-integer. (b) Taking (1.5) as the definition of
the brackets on all of $\mathcal H_0\oplus\mathrm{Sym}^2\mathcal H_0$, the two $m_2$-built brackets
impose incompatible constraints (slope and offset) on any grading $h(N_{\rm gh})$ of $\mathrm{Sym}^2$: $m_2$ needs $h(n+2)=h(n)+1$,
while $\tilde\ell_2(A,B)|_{\mathrm{Sym}^2}=\tfrac{g^2}{12}m_2(A\otimes B+B\otimes A)$ for $A,B\in\mathcal H_0$
of gh $a,b$ needs $h(a+b+2)=(a-2)+(b-2)+1$, i.e. $h(n)=n-5$, slope 1; likewise $\ell_3(\Sigma,\Psi)$
needs $h(n)=n-4$. The three agree only at the classical values $h(4)=0$, $h(6)=1$. Already
$\Lambda\otimes\Lambda$ (gh 2, even) gives $h(4)=-1$ from $\tilde\ell_2(\Lambda,\Lambda)$ against $h(4)=0$,
and mod 2 the same conflict remains ($m_2$ needs $h(n+2)\neq h(n)$, the $\mathrm{Sym}^2$-valued
bracket needs $h(n)\equiv n+1$, so $h(n+2)\equiv h(n)$). Hence with gauge directions included the
brackets (1.5) are homogeneous in no ghost-number-based $\mathbb Z$ or $\mathbb Z_2$ grading; the
identities of §2 are then read as identities of even superfields with formal even coefficients
(the device of 026 §3), which is grading-free. Toy check G verifies both halves (§3). Recorded as
a finding (Working notes); it sharpens, and partly corrects, R7.

\subsection*{The candidate map and its direction}

The $\Sigma$-EOM is solved by $\Sigma=\Psi^{\otimes2}$ (R8), and $\Psi\mapsto\Psi^{\otimes2}$
is the composite gauge law's finite form (R11). The candidate is therefore
$$F:\mathsf T\to\mathsf E,\qquad F(\Psi)=\big(\Psi,\ \Psi^{\otimes2}\big),\qquad
\phi_1=\iota,\quad \phi_2(A,B)=\big(0,\ A\otimes B+B\otimes A\big),\quad \phi_{n\ge3}=0,\tag{1.6}$$
so that $\tfrac12\phi_2(\Psi,\Psi)=\Psi^{\otimes2}$ (a general normalisation $c\,\Psi^{\otimes2}$
is kept in §2 as a falsifier). The direction $\mathsf T\to\mathsf E$ is the one in which the
enlarged field is *expressed through* the truncated one; the reverse direction is the
projection $\pi_1(\Psi,\Sigma)=\Psi$, which is what "integrating $\Sigma$ out" means at the level
of maps, and is discussed in §2.5.

## §2 The morphism identities

\subsection*{Derivation — the generating-function identity for $F(\Psi)=(\Psi,c\,\Psi^{\otimes2})$}

Insert $F(\Psi)=(\Psi,\ c\Psi^{\otimes2})$, $c$ a constant (possibly a formal series in $g$),
into (1.2). By (1.5), the left side is
$$\tilde{\mathcal L}\big(F(\Psi)\big)=\Big(\,Q\Psi+\tfrac g2\ell_2(\Psi,\Psi)+c\,\tfrac{g^2}6\ell_3(\Psi,\Psi,\Psi),\quad
-\tfrac{g^2}{12}(c-1)\,m_2(\Psi^{\otimes2})\Big).\tag{2.1}$$
The right side, with $dF|_\Psi[X]=(X,\ c(X\otimes\Psi+\Psi\otimes X))$, is
$$dF\big|_\Psi\big[\mathcal L(\Psi)\big]=\Big(\mathcal L(\Psi),\quad
c\big(\mathcal L(\Psi)\otimes\Psi+\Psi\otimes\mathcal L(\Psi)\big)\Big).\tag{2.2}$$
The defect $D(\Psi):=\tilde{\mathcal L}(F(\Psi))-dF|_\Psi[\mathcal L(\Psi)]$ has components
$$D_{\mathcal H_0}=(c-1)\tfrac{g^2}6\ell_3(\Psi^3),\qquad
D_{\mathrm{Sym}^2}=-\tfrac{g^2}{12}(c-1)m_2(\Psi^{\otimes2})-c\big(\mathcal L(\Psi)\otimes\Psi+\Psi\otimes\mathcal L(\Psi)\big).\tag{2.3}$$

\subsection*{Order by order in the number of inputs}

Expanding (2.3) in powers of $\Psi$ (equivalently in $g$, since $\mathcal L$ is homogeneous:
$n$ inputs $\leftrightarrow g^{n-1}$):

*One input* ($g^0$, linear). $D_{\mathcal H_0}^{(1)}=0$: $\tilde\ell_1\iota\Psi=Q\Psi=\iota\,Q\Psi$,
$\phi_1$ is a chain map. $D_{\mathrm{Sym}^2}^{(1)}=0$ trivially ($\phi_1$ has no $\mathrm{Sym}^2$ component).

*Two inputs.* Unpolarised form of the standard identity
$\tilde\ell_1\phi_2(\Psi,\Psi)+\tilde\ell_2(\phi_1\Psi,\phi_1\Psi)=\phi_1\ell_2(\Psi,\Psi)+2\phi_2(Q\Psi,\Psi)$:
$$D_{\mathcal H_0}^{(2)}=0,\qquad
D_{\mathrm{Sym}^2}^{(2)}=-\tfrac{g^2}{12}(c-1)m_2(\Psi^{\otimes2})\;-\;c\,\big(Q\Psi\otimes\Psi+\Psi\otimes Q\Psi\big).\tag{2.4}$$
The $m_2$ term is the *only* $\mathrm{Sym}^2$-valued contribution of $\tilde\ell_1\phi_2$ and
$\tilde\ell_2(\phi_1,\phi_1)$; it cancels iff $c=1$ (R8's completion of the square). The
$Q$ term is $\phi_2(Q\Psi,\Psi)+\phi_2(\Psi,Q\Psi)=\hat Q\,\phi_2(\Psi,\Psi)$, the would-be
"$\tilde\ell_1\phi_2$" if the $\Sigma$-sector carried the differential $\hat Q=Q\otimes1+1\otimes Q$.
It does not — $\Sigma$ has no $Q$-kinetic term (R11) — and nothing on the left side of (1.2) is
$g$-independent in the $\mathrm{Sym}^2$ slot. Hence
$$\boxed{\ D^{(2)}_{\mathrm{Sym}^2}\big|_{g^0}=-c\,\hat Q(\Psi^{\otimes2})\neq0\quad\text{for every }c\neq0,\ }\tag{2.5}$$
and $c=0$ is excluded by the three-input $\mathcal H_0$ identity below. **The two-input identity fails.**

*Three inputs* ($g^2$). $D^{(3)}_{\mathcal H_0}=(c-1)\tfrac{g^2}6\ell_3(\Psi^3)$: the $\mathcal H_0$-component
holds iff $c=1$. Its terms are $\tilde\ell_2(\phi_1\Psi,\tfrac12\phi_2(\Psi,\Psi))=\tfrac{g^2}6c\,\ell_3(\Psi^{\otimes2},\Psi)$
on the left against $\phi_1\ell_3(\Psi^3)\tfrac{g^2}6$ on the right — the $\Sigma$–$\Psi$ bracket
$\tilde\ell_2(\Sigma,\Psi)$ plays the role of $\ell_3$; no $\phi_3$ is needed *in this component*
(with $c=1$ it holds exactly, to all numbers of inputs, since $D_{\mathcal H_0}\equiv0$). The
$\mathrm{Sym}^2$-component at $g^1$ (three inputs):
$$D^{(3)}_{\mathrm{Sym}^2}=-c\,\tfrac g2\big(\ell_2(\Psi,\Psi)\otimes\Psi+\Psi\otimes\ell_2(\Psi,\Psi)\big)\neq0,\tag{2.6}$$
unmatched: $\tilde\ell_3=0$, $\tilde\ell_2(\Psi,\Sigma)$ is $\mathcal H_0$-valued, and a $\phi_3$ would enter
only through $\tilde\ell_1\phi_3=-\tfrac{g^2}{12}m_2\phi_3$ ($O(g^2)$, $m_2$-built) — order and
operator mismatch with (2.6). Four inputs ($g^2$): $D^{(4)}_{\mathrm{Sym}^2}=-c\tfrac{g^2}6(\ell_3(\Psi^3)\otimes\Psi+\ldots)$,
same pattern.

\subsection*{Can other components repair it?}

Let $\phi_2^{\mathrm{Sym}^2}(\Psi,\Psi)=B(\Psi,\Psi)=B_0+gB_1+g^2B_2+\dots$ be an arbitrary symmetric
bilinear map and allow $\phi_3$, $\phi_1=\iota$ fixed. The $\mathrm{Sym}^2$-component of (1.2) at two
inputs, order $g^0$, reads $0=\hat QB_0(\Psi,\Psi)$: $B_0$ must be $\hat Q$-closed, which
$\Psi^{\otimes2}$ is not for generic $Q$ (the toy, §3, exhibits it). But the three-input
$\mathcal H_0$-component at $g^2$ requires $\ell_3(\tfrac12B_0(\Psi,\Psi)-\Psi^{\otimes2},\Psi)$ to be
cancelled by $\phi_3$-terms, $Q\phi_3(\Psi^3)-3\phi_3(Q\Psi,\Psi,\Psi)=[\hat Q,\phi_3](\Psi^3)$,
i.e. to be $Q$-exact as a trilinear map — not the case for generic $(Q,\ell_3)$ since
$[Q,\ell_3]=-\ell_2\circ_1\ell_2\neq0$. So for generic data the two requirements on $B_0$ are
incompatible; the obstruction is structural (the $\Sigma$-sector is not a $Q$-complex), not a
normalisation. Uniqueness or a full no-go over all $(\phi_n)$ is **not claimed**; the argument
is generic-data, and a special-data escape ($\ker m_2$, $Q$-exact $\ell_3$) is not excluded.

\subsection*{2.5 The reverse direction: the projection}

$\pi_1(\Psi,\Sigma)=\Psi$, $\pi_{n\ge2}$ to be found. Identity (1.2) with $F\to\pi$, $\mathcal L\leftrightarrow\tilde{\mathcal L}$:
one input, $Q\pi_1=\pi_1\tilde\ell_1$ holds. Two inputs, $\mathcal H_0$-valued, at $g^2$: the mismatch
$\tfrac{g^2}6\ell_3(\Sigma-\Psi^{\otimes2},\Psi)$ between $\pi_1\tilde{\mathcal L}$ and $\mathcal L\pi_1$
must be absorbed by $\pi_2(\Psi,\tilde{\mathcal L}_\Sigma)=\pi_2(\Psi,-\tfrac{g^2}{12}m_2(\Sigma-\Psi^{\otimes2}))$,
which fixes $\pi_2(\Psi,\Sigma')=2\,\ell_3(m_2^{-1}\Sigma',\Psi)$ on the image of $m_2$ — the
homological-perturbation ("integrate out with propagator $m_2^{-1}$") form. It requires
$m_2$ invertible on the $\Sigma$-space (I3, open) and, at $g^0$, $[\hat Q,\pi_2]=0$, i.e.
$Q\ell_3(m_2^{-1}\Sigma,\Psi)=\ell_3(m_2^{-1}\Sigma,Q\Psi)$, again false for generic data because
the $\Sigma$-sector has no $\hat Q$ to move across. So the projection is not a strict morphism
with $(\pi_1,\pi_2)$ either; the same missing $\hat Q$ blocks both directions.

\subsection*{Commentary}

(2.1): the $\mathrm{Sym}^2$ component is exactly the $\Sigma$-EOM of R8 evaluated at $\Sigma=c\Psi^{\otimes2}$.
(2.2): $dF$ is the tangent map of the polynomial $F$; for even $\Psi$ no signs.
(2.5): the decisive term. The convention-invariant statement is the operator mismatch: the term is
$\hat Q$-built while every $\mathrm{Sym}^2$-valued bracket of $\mathsf E$ is $m_2$-built, and
$\hat Q\Psi^{\otimes2}$, $m_2\Psi^{\otimes2}$ are linearly independent for generic data. The order
counting ("$g$-independent vs $O(g^2)$") depends on the normalisation of $\Sigma$ — $\Sigma\to g^{-1}\Sigma$
moves both to $O(g)$ without curing anything — so the paper should use the operator mismatch.
(2.3) with $c=1$: $D=(0,\ -\hat{\mathcal L}\text{-term})$ where the term is $dF[\mathcal L(\Psi)]|_{\mathrm{Sym}^2}$,
linear in the truncated EOM $\mathcal L(\Psi)$: it vanishes on shell. Hence

\subsection*{Result}

$$\boxed{\ \tilde{\mathcal L}\big(F(\Psi)\big)=\big(\mathcal L(\Psi),\,0\big),\qquad
dF|_\Psi[\mathcal L(\Psi)]=\big(\mathcal L(\Psi),\ \mathcal L(\Psi)\otimes\Psi+\Psi\otimes\mathcal L(\Psi)\big).\ }\tag{2.7}$$
$F=(\iota,\cdot^{\otimes2})$ maps Maurer–Cartan elements of $\mathsf T$ to Maurer–Cartan elements of $\mathsf E$
(R8) and, by R11, intertwines the gauge transformations through the composite law (the $(\Lambda,\Psi)$
polarisation of $\phi_2$; not re-derived here, the odd-input sector is not written), but is **not** an
$L_\infty$-morphism: the two-input identity fails at
$O(g^0)$ in the $\mathrm{Sym}^2$ component by $\hat Q(\Psi^{\otimes2})$; no normalisation of $\phi_2$ (constant or
$g$-dependent) repairs it, and for generic $(Q,\ell_3)$ neither does a $\phi_3$ (generic-data argument
of §2; $\phi_3$-repair untested on the toy). The defect is proportional to the EOM of $\mathsf T$
(on-shell morphism only).

## §3 Toy check

`codes/verify-morphism-check.py` (seed 2029 default; also run with seed 7; 9c added checks G–G3): graded toy space with
$N_{\rm gh}=(1,2,2,3,3,4)$, odd graded-antisymmetric $\omega_1$ saturating $N_{\rm gh}=5$,
$\Delta=\omega_1^{-1}$; $Q=\Delta K$ with $K$ a rank-1 symmetric form on the gh-2 block (so $Q$ is
cyclic, maps gh 2 → gh 3, and has a one-dimensional kernel on gh 2); $V_3,V_4$ random
graded-symmetric tensors saturating gh 6, 8; $\ell_2=\Delta V_3$, $\ell_3=\Delta V_4$,
$m_2=\Delta^{\otimes2}V_4$ on the first two slots. No $L_\infty$ relations are imposed on
$(Q,\ell_2,\ell_3)$: none of the identities (2.1)–(2.7) uses them, so generic data is the
non-hollow choice (cf. 220 script). $g=0.7$; $\Psi$ random in gh 2.

| Check | What | Result |
|---|---|---|
| A / A′ | $\omega$-dual of the directional derivative of $S_{\rm HS}$ (1.4) equals $\tilde{\mathcal L}(\Phi)$ of (1.5), both components (fixes the coefficients $1/12,1/6,1/3$); wrong source coefficient detected | PASS ($10^{-9}$) / PASS |
| B / B′ | $D_{\mathcal H_0}=0$ at $c=1$; $\neq0$ at $c=1.3$ | PASS ($10^{-16}$) / PASS |
| C / C′ | $\tilde{\mathcal L}(F)|_{\mathrm{Sym}^2}=0$ at $c=1$ (R8); $\neq0$ at $c=1.3$ | PASS (exact) / PASS |
| D0 | full $\mathrm{Sym}^2$ defect $\neq0$ at $c=1$: strict morphism fails | PASS (max 6.8) |
| D / D′ | $g=0$: defect $=-\hat Q(\Psi^{\otimes2})$, nonzero; vanishes for $\Psi\in\ker Q$ | PASS / PASS |
| E | $g^1$ coefficient of the $\mathrm{Sym}^2$ defect equals (2.6), nonzero | PASS |
| G / G′ / G′′ / G3 | grading (1.7): on the classical complex every bracket of (1.5) has degree $+1$, $\omega_2$ degree $-1$ (G); $\Lambda\otimes\Psi$ has degree $-\tfrac12$ (G′); on the full toy space the mixed brackets take shifts $\{\tfrac12,1,\tfrac32\}$ (G′′); a ghost-number grading $h(n)$ of $\mathrm{Sym}^2$ exists on the classical complex (residual $10^{-14}$) and none on the full space, integer (residual $4.9$) or mod 2 (enumeration) (G3) | PASS ×4 |
| F0 / F | least squares over all symmetric bilinear gh-4-valued $B=\phi_2^{\mathrm{Sym}^2}$: the $\ell_3$-family alone is solved by $B=2\Psi^{\otimes2}$ (residual $10^{-14}$); adding $\hat QB=0$ leaves residual $3.1$ (seed 7: $6.0$) out of $|b|\approx20$ — no repair with $\phi_3=0$ | PASS / PASS |

16/16 PASS on both seeds. What the toy does **not** establish: odd-input sectors; the $\phi_3$-exact
escape in F; anything about the actual CFT $V_4$ (generic tensors only).

## Working notes

**What this settles for the paper.** The sentence "the cubic theory and the quartic-truncated
$L_\infty$ theory are related by the $L_\infty$-morphism $\Psi\mapsto(\Psi,\Psi^{\otimes2})$" is
**not available**. What is available: (i) $F$ sends solutions to solutions and, restricted to the
$\Psi$ component, the two EOMs coincide identically (R8, here re-derived as $D_{\mathcal H_0}\equiv0$,
$\tilde{\mathcal L}(F)|_{\mathrm{Sym}^2}\equiv0$); (ii) $F$ intertwines gauge transformations through the
composite law (R11 — the $(\Lambda,\Psi)$ polarisation of $\phi_2$); (iii) the defect of the
morphism identity is $dF[\mathcal L(\Psi)]$, i.e. proportional to the truncated EOM: an "on-shell
morphism", nothing more. The structural reason is that the $\Sigma$-sector is not a $Q$-complex
($\Sigma$ has no $Q$-kinetic term), so no map into it built from $\Psi$ can be a chain map on the gauge directions (it is one on the classical complex, where every bracket of (1.5) has degree $+1$); the same
missing $\hat Q$ blocks the projection direction (§2.5). The honest $L_\infty$ formulation of
"integrating $\Sigma$ out" is the homological-perturbation construction with propagator $m_2^{-1}$,
which needs I3 and is not attempted here. Recommended wording for the paper: equality of actions
after eliminating $\Sigma$ by its algebraic EOM (R8/R10) plus the gauge map (R11); no
quasi-isomorphism claim.

**Grading finding (new; re-derived 9c, script check G).** $\tilde\ell_1=Q\oplus(-\tfrac{g^2}{12}m_2)$
raises $N_{\rm gh}$ by 1 on $\mathcal H_0$ and by 2 on $\mathrm{Sym}^2\mathcal H_0$, so it is homogeneous
neither in ghost number nor in the parity $N_{\rm gh}\bmod2$, R7-shifted or not. With
$\deg_{\mathcal H_0}=N_{\rm gh}-2$, $\deg_{\mathrm{Sym}^2}=(N_{\rm gh}-4)/2$ (1.7) every bracket of (1.5) has
degree $+1$ and $\omega_2$, like $\omega_1$, degree $-1$ on the classical complex ($\mathcal H_0$ at gh
$\{2,3\}$, $\mathrm{Sym}^2$ at gh $\{4,6\}$): there every bracket of (1.5) has degree $+1$ and $\omega_2$ degree $-1$ (the $L_\infty$
structure of 026 §5.4 is $\mathbb Z$-graded cyclic on the classical complex). The obstruction lies off the classical complex: (1.7) is half-integer on
odd-ghost $\mathrm{Sym}^2$ states ($\Lambda\otimes\Psi$, the composite gauge direction), and no
ghost-number-based grading of $\mathrm{Sym}^2$, integer or mod 2, makes $m_2$ (slope $\tfrac12$) and
the $\mathrm{Sym}^2$-valued bracket $m_2(A\otimes B)$ (slope 1) simultaneously homogeneous once
$\Lambda\otimes\Lambda$ or gh-$\neq4$ $\Sigma$ states are admitted (§1 (ii)). R7's content — the exchange
sign of $\omega_2$ on gh-4/gh-6 states is symmetric where an odd symplectic form wants
antisymmetric, so a BV parity must be declared — is untouched; its *grading* statement should be
read on the classical complex with (1.7). Also $\tilde\ell_1^2\neq0$ on the full
$\mathrm{Sym}^2\mathcal H_0$ ($O(g^4)$, $m_2^2$), consistent with R11's "to $O(g^3)$": beyond that
order $\mathsf E$ is an $L_\infty$ algebra only after truncation to gh $\{4,6\}$.

**Proposed ledger row.** R36 — *Comparison map is not an $L_\infty$-morphism*: $F=(\iota,\cdot^{\otimes2})$,
$\mathsf T\to\mathsf E$, satisfies the $\mathcal H_0$-component of the morphism identity exactly and the
$\mathrm{Sym}^2$-component only on shell; the two-input identity fails at $O(g^0)$ by $\hat Q(\Psi^{\otimes2})$
(no $Q$-kinetic term for $\Sigma$); not repaired by any normalisation of $\phi_2$ (proof, operator
mismatch $\hat Q$ vs $m_2$); repair by $\phi_3$ excluded for generic $(Q,\ell_3)$ by the generic-data
argument of §2 only (least-squares no-repair in the $\phi_3=0$, $\phi_2^{\mathcal H_0}=0$ ansatz;
$\phi_3$ untested); projection direction blocked by the same term and needs $m_2^{-1}$ (I3). Status:
Verified for the morphism failure and the on-shell identity (toy, 16/16, two seeds); the no-repair
(with $\phi_3$) and grading sub-claims are Argued. Pending critic iteration 2. Annotation to R11:
"the composite gauge law is the $(\Lambda,\Psi)$ component of $\phi_2$; $\phi_2$ is not an
$L_\infty$-morphism component (029)". Annotation to R7: "$\tilde\ell_1$ is not parity-homogeneous in $N_{\rm gh}\bmod2$; the grading under which every bracket of (1.5) restricted to the classical complex has degree $+1$ and $\omega_2$ degree $-1$ (so the $L_\infty$ structure of 026 §5.4 is $\mathbb Z$-graded cyclic there) is
$\deg_{\mathcal H_0}=N_{\rm gh}-2$, $\deg_{\mathrm{Sym}^2}=(N_{\rm gh}-4)/2$, half-integer on the gauge
directions $\Lambda\otimes\Psi$; (1.7) is not R7's uniform shift (gh 4 even, gh 6 odd; $\omega_2$ degree $-1$ with $\omega_1$'s exchange sign); no ghost-number-based $\mathbb Z$ or $\mathbb Z_2$ grading makes the brackets (1.5) homogeneous on the full space (029 §1 (ii), check G). Status: Argued (grading bookkeeping; toy check G)".

## Verification

Symbolic: (2.1)–(2.7) are one-line polynomial identities given (1.5); (1.5) itself is verified
numerically against the action (check A, both components, falsifiable via A′). Numerical: all
boxed claims evaluated at random generic points, two seeds, 16/16 PASS; break-on-purpose legs
A′, B′, C′; the no-repair claim F is falsifiable (F0 shows the same solver returns residual 0
when the obstruction is removed). Dimensional: all terms of (2.3) carry $g^{n-1}$ for $n$ inputs; in the grading
(1.7) the $\mathcal H_0$ terms of (2.3) have degree 1 (gh 3) and the $\mathrm{Sym}^2$ term
$m_2\Psi^{\otimes2}$ degree 1 (gh 6), but $\mathcal L\otimes\Psi+\Psi\otimes\mathcal L$ — hence the failing
term $\hat Q\Psi^{\otimes2}$ — sits at gh 5, degree $\tfrac12$, *off* the classical complex: the
defect lives in the odd-ghost $\mathrm{Sym}^2$ sector where (1.7) is half-integer. Equivalently,
$\phi_2=\cdot\otimes\cdot$ has degree $0$ under (1.7) only on inputs of total gh 4 (it sends
$\deg a+\deg b$ to $\tfrac12(\deg a+\deg b)$), so $F$ is not a graded map off the field slot; the
two-input failure (2.5) is, at bottom, the operator mismatch $\hat Q$ vs $m_2$ (§2), of which this
grading defect is a second face.
Grading: check G (classical complex: degree $+1$/$-1$; break legs G′, G′′, G3).
Not verified: odd-input sectors, $\phi_3$-exact escape, CFT data, uniqueness.

## Status

9c fixes applied (grading paragraph re-derived, §0/§1(ii)/Working notes/R7 annotation/Verification rewritten; no-repair hedged in §0, Result, proposed row (R36); 5 minors; script 16/16 PASS, seeds 2029 and 7); record closed 2026-09-14: critic iteration 2 ACCEPT (residues applied by the orchestrator); promoted to ledger R36 + annotations R7/R11; next: none
