---
id: 037-hpt-transfer-sigma
agent: computator
brief: agent/briefs/active-computator-037-hpt-transfer-20260921T153500.md
created: 2026-09-21T15:40
script: codes/verify-hpt-transfer.py
depends: R7, R8, R9, R10, R11, R22, R30, R36; agent/derivations/029-morphism-check.md §1–§3
---

# 037 — Integrating $\Sigma$ out as a homological-perturbation transfer (finite-dimensional model)

**Literal task.** On the classical complex of the cubic (HS) theory $\mathsf E$ at $O(g_s^2)$, with
differential $\tilde\ell_1=Q\oplus(-\tfrac{g^2}{12}m_2)$ of 029 (1.5), treat the $\Sigma$ sector as a
contractible piece ($m_2$ invertible), write the contraction data $(p,i,h)$ with $h$ built from
$m_2^{-1}$, compute the transferred brackets on the $\Psi$ sector through arity 3, and decide (i)
whether they equal the brackets of the quartic-truncated theory $\mathsf T=(\mathcal H_0;Q,\ell_2,\ell_3)$
and (ii) whether the induced map $\mathsf T\to\mathsf E$ is an $L_\infty$ quasi-isomorphism — giving its
components $\phi_1,\phi_2,\phi_3$ and comparing with $(\iota,\cdot^{\otimes2})$ of 029.

**Motivating objective.** R36 carries the paper directive "no quasi-isomorphism claim", issued when
the transfer had never been tried. Decide whether the paper may say that the cubic and the
quartic-truncated theory are quasi-isomorphic — in the finite-dimensional model and conditionally
on PH1 beyond it — or whether a real obstruction stands.

**Conventions.** Those of 029 §1, verbatim: physical ghost number, $N_{\rm gh}(\Psi)=2$,
$N_{\rm gh}(\Sigma)=4$; $\omega_1(A,B)=\langle A|c_0^-|B\rangle$, $\omega_2=\omega_1^{\otimes2}$;
$V_3(A,B,C)=\omega_1(A,\ell_2(B,C))$, $V_4(A,B,C,D)=\omega_1(A,\ell_3(B,C,D))$,
$V_4(A_2,B_2)=\omega_2(A_2,m_2B_2)$, $m_2=\Delta\circ\ell_3$; $g\equiv g_s$. Degree convention (029
(1.7)): $\deg_{\mathcal H_0}=N_{\rm gh}-2$, $\deg_{\mathrm{Sym}^2}=\tfrac12(N_{\rm gh}-4)$; every bracket
has degree $+1$, every pairing degree $-1$, every morphism component $\phi_n$ degree $0$.
Notation $A\odot B:=A\otimes B+B\otimes A$. Generating-function (even-polarised) form of the
$L_\infty$ and morphism identities as in 029 (1.1)–(1.2).

## Objects to compute (planned before any algebra)

1. The classical complex of $\mathsf E$ and of $\mathsf T$, and the degrees of every bracket on it.
2. The contraction $(p,i,h)$: explicit $h$, the four side conditions, and its uniqueness.
3. $\ell^{\rm tr}_1,\ell^{\rm tr}_2,\ell^{\rm tr}_3$ (and $\ell^{\rm tr}_{n\ge4}$) from the tree
   recursion, with the sign convention fixed by derivation, not quoted.
4. The morphism components $\phi_1,\phi_2,\phi_3$ of the transfer map $F$.
5. The morphism identities on the classical complex; the quasi-isomorphism statement.
6. The obstruction off the classical complex, its class, and the weakest relaxation evading it.
7. Cyclicity of $h$ and hence of the transferred structure.

**First falsifier.** The transfer does *not* reproduce $\mathsf T$ if
$\ell^{\rm tr}_3\neq g^2\ell_3$ — concretely, if the numerical evaluation of
$-\tfrac12\,p\,\tilde\ell_2\big(i\psi,\ h\,\tilde\ell_2(i\psi,i\psi)\big)$ differs from
$\tfrac{g^2}{6}\ell_3(\psi,\psi,\psi)$ at generic $\psi$ by anything other than round-off — a wrong
sign or a wrong rational factor both count. A second falsifier: $\ell^{\rm tr}_4\neq0$ would mean the
transferred theory is not the quartic truncation.

## Claim tree

- **A1** Conventions of 029 §1 (above), finite-dimensional model of 029 §3 (same data as
  `codes/verify-morphism-check.py`): graded toy space, $N_{\rm gh}=(1,2,2,3,3,4)$, generic
  $\omega_1,V_3,V_4$, $Q=\Delta K$ with $K$ rank one on the gh-2 block, $\ell_2=\Delta V_3$,
  $\ell_3=\Delta V_4$, $m_2=\Delta^{\otimes2}V_4$.
- **A2** *Classical complex* means: truncate $\mathcal H_0$ to $\mathcal H_0^{\rm cl}:=
  \mathcal H_0|_{N_{\rm gh}\in\{2,3\}}$ **first**, and build the $\Sigma$ sector as the symmetric square
  of the truncated space,
  $$S^{(4)}:=\mathrm{Sym}^2\big(\mathcal H_0^{(2)}\big),\qquad
    S^{(6)}:=\mathrm{Sym}^2\big(\mathcal H_0^{(3)}\big),\qquad
    \mathcal H_0^{(n)}:=\mathcal H_0|_{N_{\rm gh}=n},$$
  with all brackets of 029 (1.5) followed by the projector $P$ onto this space ($\Pi$ on the
  $\mathcal H_0$ strand, $\Pi_2=\Pi\otimes\Pi$ on the $\mathrm{Sym}^2$ strands, along the ghost-number
  block decomposition). In particular the $\Sigma$-sector differential is
  $-\tfrac{g^2}{12}m_2^{\rm cl}$ with $m_2^{\rm cl}:=\Pi_2m_2|_{S^{(4)}}:S^{(4)}\to S^{(6)}$. Degrees
  $\{0,1\}$ in 029 (1.7). Neither $S^{(4)}$ nor $S^{(6)}$ is defined through $m_2$: bijectivity of
  $m_2^{\rm cl}$ is a statement about $V_4$ (C1.0), not a definition. The gh-4 states excluded from
  $S^{(4)}$ are $\Lambda\odot X^{(3)}=\mathcal H_0^{(1)}\odot\mathcal H_0^{(3)}$, which carries a
  gauge parameter, and $\mathcal H_0^{(0)}\odot\mathcal H_0^{(4)}$; both belong to the extension
  discussed in §4. This is the class on which $\mathsf E$ is a $\mathbb Z$-graded $L_\infty$ algebra
  at all (029 §0, §1 (ii)) — not a class chosen to make a theorem provable.
  The sector $S^{(5)}=\mathcal H_0^{(2)}\odot\mathcal H_0^{(3)}$ is *field-built* — it contains no gauge
  parameter — and is nonetheless excluded, purely because 029 (1.7) assigns it half-integer degree.
  Since the defect of the morphism identity lives exactly there (3.4), the record states plainly: the
  sector carrying the defect is removed by a grading convention, not by a statement about the field
  content of the theory. What that convention is worth is the subject of §4.
- **A3** $\mathsf T$ and $\mathsf E$ are truncated at $O(g^3)$ ($\ell_{n\ge4}=0$, $\tilde\ell_{n\ge3}=0$),
  as in 029.
- **H1 = PH1** (restated 2026-09-22, brief `computator-h1-restate-20260922T110500`; the
  earlier wording was "$m_2$ has a bounded inverse on $\mathrm{Sym}^2\mathcal H_0/\ker V_4$",
  which is dropped, together with the auxiliary inner product it presupposed.) On
  $\mathrm{Sym}^2\mathcal H_0/\ker V_4$, the inverse of $m_2$ exists level by level with a
  **stable kernel**: $\ker V_4^{(L)}=\ker V_4\cap\{\text{level}\le L\}$ for $L$ large enough
  at the external data considered, so that the quotient and the inverse defined on it have a
  level limit; and at the momenta used the truncated determinant on the quotient has no zero
  persisting with the level. Motivation and falsifier: the ledger entry PH1 (brief's PH-a) as
  restated; the content is algebraic at every finite level; in the finite-dimensional
  model the *level-uniform* half is vacuous — a single fixed dimension, no level
  sequence — while the injectivity half (non-degeneracy of $V_4$ on $S^{(4)}$, C1.0)
  remains a genuine condition there and is what check C1-rank tests. No norm and no bounded inverse are assumed.
  A homological-perturbation statement in a *topological* sense — a contraction of
  topological complexes, with continuity of $h$ in a stated topology — would need more than
  this, and is not claimed anywhere in this record.
- **C1** Under H1, on the classical complex $(V,\tilde\ell_1)$ carries a contraction $(p,i,h)$ onto
  $(\mathcal H_0,Q)$ with $h=-\tfrac{12}{g^2}(m_2^{\rm cl})^{-1}$ on $S^{(6)}$, $h$ is unique, and
  $\iota$ is a quasi-isomorphism of complexes. [by C1.0–C1.4]
  - **C1.0** $\omega_2$ identifies $S^{(6)}\cong(S^{(4)})^*$, and under that identification
    $m_2^{\rm cl}$ *is* the bilinear form $V_4|_{S^{(4)}\times S^{(4)}}$. Hence $m_2^{\rm cl}$ is
    **injective iff** $V_4$ is non-degenerate on $S^{(4)}$; **in the finite-dimensional model**
    (equal dimensions, $S^{(6)}\cong(S^{(4)})^*$) injectivity is equivalent to bijectivity. Beyond
    the model, non-degeneracy on $S^{(4)}$ is the injectivity half of PH1 (R9); what the
    contraction needs in addition is not a bounded inverse but the level-uniform half of PH1 as
    restated (2026-09-22): the inverse on the quotient must exist level by level with a stable
    kernel, so that $h$ has a level limit (R10's "strictly stronger than R9" is read this way
    from now on).
    [by A1, A2; eq. (1.2)] [by check: C1.0-dual, C1-rank, break leg C1-rank']
  - **C1.1** With A2, $\tilde\ell_1$ has degree $+1$, $\tilde\ell_1^2=0$, and $\tilde\ell_2$ vanishes on
    inputs of total degree $\ge1$; so $\mathsf E^{\rm cl}$ is a $\mathbb Z$-graded $L_\infty$ algebra.
    On a complex concentrated in degrees $\{0,1\}$ this statement is in fact vacuous — see C4.1 —
    and is recorded only to license the degree bookkeeping used below.
    [by A2, A3; eq. (1.3)–(1.4)] [cited: 029 §1 (ii), check G]
  - **C1.2** Under H1, $(p,i,h)$ of (1.5) satisfies the five contraction relations (1.6).
    [by H1, C1.0, C1.1; eq. (1.6)] [by check: C1-sidecond, break leg C1-sidecond']
  - **C1.3** Under H1, $h$ is the unique solution of (1.6). [by H1, C1.2; §1 *Uniqueness*]
    [check: C1-unique]
  - **C1.4** Under H1, the $\Sigma$ sector is acyclic and $\iota_*$ is an isomorphism on cohomology.
    Injectivity of $m_2^{\rm cl}$ and surjectivity onto $S^{(6)}$ both follow from C1.0; neither is
    built into A2. [by H1, C1.0; eq. (1.7)] [by check: C1-acyclic, break legs C1-acyclic',
    C1-acyclic'']
  - **C1.5** $m_2S^{(4)}\neq S^{(6)}$ as subspaces of $\mathrm{Sym}^2\mathcal H_0$: the untruncated
    $m_2$ spreads into $\mathcal H_0^{(2)}\odot\mathcal H_0^{(4)}$, so the projector $\Pi_2$ of A2 is
    not vacuous. This is why the earlier definition $S^{(6)}:=m_2S^{(4)}$ was not "the field-built
    gh-6 part". [by A1, A2; §1 *Why the projector is needed*] [by check: C1.5-span]
- **C2** Under H1, the transferred brackets are exactly those of $\mathsf T$:
  $(Q,\ g\ell_2,\ g^2\ell_3,\ 0)$. [by C2.1–C2.4]
  - **C2.1** Under H1, $\ell^{\rm tr}_1=Q$ and $\ell^{\rm tr}_2=g\ell_2$. [by C1.2; eq. (2.3), (2.5)]
    [check: C2.1, C2.2]
  - **C2.2** Under H1, $\ell^{\rm tr}_3=g^2\ell_3$ — one $\Sigma$-exchange tree, the propagator
    $(m_2^{\rm cl})^{-1}$ cancelling against the source vertex. [by H1, C1.2; eq. (2.7)]
    [check: C2.3, break legs C2.3', C2.3''; limiting case C2-V3zero; scaling C2-gscale]
  - **C2.3** Under H1, $\ell^{\rm tr}_{n\ge4}=0$. [by C2.4; eq. (2.8)] [check: C2.4]
  - **C2.4** Under H1, $F^{(n)}=0$ for $n\ge3$, because the order-3 source is $\mathcal H_0$-valued
    and $\tilde\ell_2(\Sigma,\Sigma)=0$. [by C1.2; eq. (2.6)] [check: C3.1]
  - **C2.5** C2.2 is a *second* route to R10 — the propagator route (B), whose tree combinatorics
    R10 assumed and (2.7) computes. It is not independent of route (A): both read the same
    $S_{\rm HS}$, and this one additionally needs $(m_2^{\rm cl})^{-1}$, so it is strictly more
    conditional (H1) than R10's route (A). [by C2.2, R10]
- **C3** Under H1, the transfer map is $F=(\iota,\cdot^{\otimes2})$ exactly: $\phi_1=\iota$,
  $\phi_2=\odot$, $\phi_{n\ge3}=0$ — the comparison map of 029/R36 is *derived*, and its
  normalisation $c=1$ is fixed by the contraction data (1.6), i.e. by the $\Sigma$ kinetic and source
  coefficients of $S_{\rm HS}$, and not by the morphism identity it is used to test.
  [by H1, C1.2, C2.4; eq. (2.4), (2.9)] [check: C3.1]
- **C4** Under H1, $F$ is a cyclic $L_\infty$ quasi-isomorphism
  $\mathsf T^{\rm cl}\to\mathsf E^{\rm cl}$, with the morphism identities holding *exactly, not merely
  on shell*. [by C4.1–C4.3]
  - **C4.0** On a complex concentrated in degrees $\{0,1\}$ with all brackets of degree $+1$, every
    $L_\infty$ relation lands in degree $2$ and is empty: *any* collection of degree-$+1$ multilinear
    maps is an $L_\infty$ algebra there, and likewise any degree-$0$ $\phi_n$ with $\phi_1$ a chain
    map is an $L_\infty$ morphism. The content of C1.1, C4 and the proposed ledger row is therefore
    exactly three statements: (i) $\ell^{\rm tr}=\ell^{\mathsf T}$ (C2), (ii) $\iota_*$ an isomorphism
    on $\tilde\ell_1$-cohomology (C1.4), (iii) cyclicity (C4.3). [by A2, C1.1; eq. (3.2)]
  - **C4.1** All morphism identities with an input of degree $\ge1$ are vacuous on a complex
    concentrated in degrees $\{0,1\}$. [by A2, C1.1, C4.0; eq. (3.2)]
  - **C4.2** The identities with all inputs of degree $0$ hold exactly: 029's defect
    $-\mathcal L(\psi)\odot\psi$ lies at $N_{\rm gh}=5$ in $\mathrm{Sym}^2$, outside A2.
    [by A2, C2, C3; eq. (3.3)–(3.5)] [by check: C4.1, C4.2; C4.1-nonvac, C4.1-supp, break leg C4.1']
  - **C4.3** Under H1, $h$ is cyclic w.r.t. $\omega_2$, so the transferred structure is cyclic w.r.t.
    $\omega_1$ and its action is $S_{\rm eff}$. [by H1, C1.0, R7, R8; §3 *Cyclicity*]
    [check: C4.4, break leg C4.4'; C4.5 (transferred action against $S_{\rm eff}$)]
- **C5** The transfer does not extend to a complex admitting $\mathcal H_0$ states at
  $N_{\rm gh}=1$ (gauge parameters) or at $N_{\rm gh}=4$ (antifields), within the class (i)–(iii) of
  §4; both cases are derived in §4, the first from the $\Lambda\odot\Lambda$ row at $n=4$, the
  second from $h(8)=3$ against $h(8)=2$. Other values of $N_{\rm gh}\notin\{2,3\}$ are expected to
  fail the same way but are not enumerated. [by C5.1, C5.2]
  - **C5.1** No grading of $\mathrm{Sym}^2\mathcal H_0$ by total ghost number, over $\mathbb Z$,
    $\tfrac12\mathbb Z$ or $\mathbb Z_2$, makes the brackets 029 (1.5) homogeneous once gh-1 states
    (or gh-4 states) are admitted. [cited: 029 §1 (ii), check G3; eq. (4.1)]
    [by check: C5.1, break leg C5.1']
  - **C5.2** The invariant content of C5.1 is $N_{\rm gh}(m_2)=+2$ against the $+1$ a differential
    compatible with the slope-one $\phi_2=\odot$ requires. [by C5.1; eq. (4.2)]
  - **C5.2a** *Remark, not derived.* This mismatch and R7's parity mismatch have a common source —
    the two $c_0^-$ insertions of $\omega_2=\omega_1^{\otimes2}$ — but they are different invariants
    and are **not** one obstruction counted twice: R7's is a parity, removed by a uniform one-unit
    degree shift; C5.2's is a slope, which no uniform shift can change. [by C5.2, R7; eq. (4.3)]
    [not derived: that the two are the same obstruction — see §4 *Relation to R7*]
  - **C5.3** Under H1, no freedom remains that could repair C5.1: $h$ is unique (C1.3), $c=1$ is
    forced (C3), $\phi_{n\ge3}=0$ is forced (C2.4). [by C1.3, C2.4, C3]
  - **C5.4** The weakest relaxation evading C5: a factorisation $m_2=\mathcal B\mathfrak m$ with
    $\mathcal B$ invertible of $N_{\rm gh}=-1$. Whether such a $\mathcal B$ exists for the closed-string
    $V_4$ kernel is not settled here. [GAP]

Open gaps: C5.4 (existence of the ghost-number-$(-1)$ factorisation; it is a proposed route, not a
support of any claim above); C5.2a is a remark explicitly labelled not derived and supports no claim
Hypotheses in force: H1 (= PH1)

## §1 The classical complex and the contraction data

\subsection*{Setup}

Uses A1, A2, A3, H1. *Equation labels.* In this record, equations of 029 are always cited as
"029 (x.y)"; a bare (x.y) is this record's own. Write
$V:=\mathcal H_0^{\rm cl}\oplus\big(S^{(4)}\oplus S^{(6)}\big)$ with $\mathcal H_0^{\rm cl}$,
$S^{(4)}$, $S^{(6)}$ as in A2, and decompose by the degree 029 (1.7):
$$V^0=\mathcal H_0^{(2)}\oplus S^{(4)},\qquad V^1=\mathcal H_0^{(3)}\oplus S^{(6)},\qquad
S^{(4)}=\mathrm{Sym}^2\mathcal H_0^{(2)},\quad S^{(6)}=\mathrm{Sym}^2\mathcal H_0^{(3)}.\tag{1.1}$$
$W:=\mathcal H_0^{\rm cl}$, $W^0=\mathcal H_0^{(2)}$, $W^1=\mathcal H_0^{(3)}$.
$V$ and $W$ are concentrated in degrees $\{0,1\}$.

\subsection*{Derivation}

*Bijectivity of the $\Sigma$-sector differential is a statement about $V_4$.* $\omega_1$ is
non-degenerate and pairs $\mathcal H_0^{(2)}$ with $\mathcal H_0^{(3)}$ (ghost numbers summing to the
saturation value $5$). Hence $\omega_2=\omega_1^{\otimes2}$ restricts to a non-degenerate pairing
$S^{(4)}\times S^{(6)}\to\mathbb C$ and identifies $S^{(6)}\cong(S^{(4)})^*$. Moreover $\omega_2(A_2,\cdot)$
with $A_2\in S^{(4)}$ annihilates every gh-6 block other than $S^{(6)}$ — a $\mathcal H_0^{(2)}
\odot\mathcal H_0^{(4)}$ element pairs to zero against $\mathrm{Sym}^2\mathcal H_0^{(2)}$, since neither
$\omega_1(\text{gh }2,\text{gh }2)$ nor $\omega_1(\text{gh }2,\text{gh }4)$ is nonzero. Therefore, for
$A_2,B_2\in S^{(4)}$,
$$\omega_2\big(A_2,\ m_2^{\rm cl}B_2\big)=\omega_2\big(A_2,\ m_2B_2\big)=V_4(A_2,B_2),\qquad
m_2^{\rm cl}=\Pi_2m_2\big|_{S^{(4)}},\tag{1.2}$$
i.e. under the identification $S^{(6)}\cong(S^{(4)})^*$ the operator $m_2^{\rm cl}$ *is* the bilinear
form $V_4|_{S^{(4)}\times S^{(4)}}$. Consequently
$$m_2^{\rm cl}\ \text{injective}\iff V_4|_{S^{(4)}}\ \text{non-degenerate}\iff
\ker V_4\cap S^{(4)}=0,$$
and, **in the finite-dimensional model of A1** (where $\dim S^{(6)}=\dim S^{(4)}$ and
$S^{(6)}\cong(S^{(4)})^*$ as finite-dimensional spaces), injectivity is equivalent to bijectivity, so
$$\text{(finite dimension)}\quad m_2^{\rm cl}\ \text{bijective}\iff V_4|_{S^{(4)}}\
\text{non-degenerate}.$$
Beyond the model the two halves separate, and the record keeps the distinction R9 and R10 carry
explicitly. Non-degeneracy of $V_4$ on $S^{(4)}$ gives **injectivity** of $m_2^{\rm cl}$ (R9's
statement); the contraction (1.5) additionally needs $(m_2^{\rm cl})^{-1}$ to exist on all of
$S^{(6)}$ *level by level, with a kernel that stabilises*, so that $h$ has a level limit — the
extra content of PH1 as restated on 2026-09-22 (R10: "strictly stronger than R9 injectivity",
read without the bounded-inverse wording it used to carry; a contraction of *topological*
complexes, with $h$ continuous in a stated topology, would need more and is not claimed).
In infinite dimensions a non-degenerate bilinear
form induces an injective map, not a bijective one, and $\omega_2$ non-degenerate does not give
$S^{(6)}\cong(S^{(4)})^*$ either. So: non-degeneracy of $V_4$ on $S^{(4)}$ is the injectivity half of
H1 = PH1, and everything below that uses $h$ uses the whole of PH1.
Neither injectivity nor surjectivity is definitional: both sides of (1.2) are fixed by the vertex.

*Why the projector is needed.* $m_2$ raises the total ghost number by $2$ but does **not** preserve the
truncation: $m_2S^{(4)}$ has components in every gh-6 block of $\mathrm{Sym}^2\mathcal H_0$, in
particular in $\mathcal H_0^{(2)}\odot\mathcal H_0^{(4)}$ whenever $\mathcal H_0$ carries gh-4 states (it
does in the model of A1, and it does in the closed-string $\mathcal H_0$). So
$m_2S^{(4)}\neq S^{(6)}$ (C1.5), and the differential of the classical complex is the *projected*
$m_2^{\rm cl}$, not $m_2$. By (1.2) the projection costs nothing at the level of the pairing: the
part removed by $\Pi_2$ is $\omega_2$-orthogonal to $S^{(4)}$, so $V_4$ on $S^{(4)}$ — the quantity the
HS action actually contains — is untouched. Nor does the projection change the *equations of
motion*: the full $\Sigma$-EOM is $m_2(\Sigma-\Psi^{\otimes2})=0$ on the whole gh-6 block, of which
the truncated theory imposes only $\Pi_2m_2(\Sigma-\Psi^{\otimes2})=0$; but
$\Sigma-\Psi^{\otimes2}\in S^{(4)}$ and $\Pi_2m_2|_{S^{(4)}}=m_2^{\rm cl}$ is injective there by
(1.2) and H1, so both conditions have the same solution set $\Sigma=\Psi^{\otimes2}$. The projected
theory is not a different theory.

*Degrees of the brackets.* With 029 (1.7), 029 §1 (ii) (script check G) establishes that every bracket
of 029 (1.5) has degree $+1$ on $V$ and both pairings degree $-1$. Two consequences used throughout:

$$\tilde\ell_1:V^0\to V^1,\qquad \tilde\ell_1^2=0\ \text{identically (no degree 2 in }V).\tag{1.3}$$
$$\tilde\ell_2\big(V^{d_1},V^{d_2}\big)=0\ \text{whenever }d_1+d_2\ge1,\tag{1.4}$$
because the image would sit in degree $\ge2$, which is not in $V$. Explicitly, the components of
$\tilde\ell_2$ that (1.4) removes are $g\ell_2(\psi^{(2)},\psi^{(3)})$ (gh 5),
$\tfrac{g^2}{12}m_2(\psi^{(2)}\odot\psi^{(3)})$ (gh 7), $\tfrac{g^2}6\ell_3(\Sigma^{(4)},\psi^{(3)})$
(gh 4 in $\mathcal H_0$) and $\tfrac{g^2}6\ell_3(\Sigma^{(6)},\psi^{(2)})$ (gh 5): all outside A2.
So on the classical complex $\mathsf E$ is an honest $\mathbb Z$-graded $L_\infty$ algebra, and every
bracket is determined by its restriction to degree-zero inputs.

*The contraction.* Take
$$i:W\hookrightarrow V,\ \ i\psi=(\psi,0);\qquad p:V\to W,\ \ p(\psi,\Sigma)=\psi;\qquad
h:V^1\to V^0,\ \ h(\psi^{(3)},\Sigma^{(6)})=\Big(0,\ -\tfrac{12}{g^2}\,(m_2^{\rm cl})^{-1}\Sigma^{(6)}\Big),\tag{1.5}$$
$h$ zero on $V^0$. $(m_2^{\rm cl})^{-1}:S^{(6)}\to S^{(4)}$ exists by (1.2) and H1. Then
$$p\,i=\mathrm{id}_W,\qquad \tilde\ell_1h+h\,\tilde\ell_1=\mathrm{id}_V-i\,p,\qquad
h^2=0,\qquad h\,i=0,\qquad p\,h=0.\tag{1.6}$$
Verification of the second relation, component by component. On $\mathcal H_0$: $h=0$ there and
$h\tilde\ell_1\psi=h(Q\psi)=0$ since $h$ kills $\mathcal H_0^{(3)}$, while $\mathrm{id}-ip=0$ on
$\mathcal H_0$. On $S^{(4)}$: $\tilde\ell_1h=0$ and
$h\tilde\ell_1\Sigma^{(4)}=h\big(-\tfrac{g^2}{12}m_2^{\rm cl}\Sigma^{(4)}\big)
=-\tfrac{12}{g^2}(m_2^{\rm cl})^{-1}\big(-\tfrac{g^2}{12}m_2^{\rm cl}\Sigma^{(4)}\big)=\Sigma^{(4)}
=(\mathrm{id}-ip)\Sigma^{(4)}$.
On $S^{(6)}$: $h\tilde\ell_1=0$ (nothing above degree 1) and
$\tilde\ell_1h\Sigma^{(6)}=-\tfrac{g^2}{12}m_2^{\rm cl}\big(-\tfrac{12}{g^2}(m_2^{\rm cl})^{-1}\Sigma^{(6)}\big)=\Sigma^{(6)}$.
The three side conditions are immediate from (1.5): $h$ lands in $S^{(4)}\subset\ker h\cap\ker p$, and
$\mathrm{im}\,i\subset\mathcal H_0\subset\ker h$.

*Uniqueness.* Any $h'$ obeying (1.6) differs from $h$ by $\eta:=h'-h$ with
$\tilde\ell_1\eta+\eta\tilde\ell_1=0$, $\eta i=0$, $p\eta=0$, so $\eta$ maps $V^1\to V^0$ and lands in
$S^{(4)}$ and kills $\mathcal H_0^{(3)}$ — i.e. $\eta=\rho$ with $\rho:S^{(6)}\to S^{(4)}$ and
$\tilde\ell_1\rho=-\tfrac{g^2}{12}m_2^{\rm cl}\rho=0$ on $S^{(6)}$, hence $\rho=0$ since
$m_2^{\rm cl}$ is injective ((1.2), H1). So $h$ is unique: no freedom is left that could be used to
repair anything later.

*Acyclicity.* $H^\bullet(V,\tilde\ell_1)=H^\bullet(\mathcal H_0^{\rm cl},Q)\oplus
H^\bullet(S,-\tfrac{g^2}{12}m_2^{\rm cl})$ and the second summand vanishes because
$m_2^{\rm cl}:S^{(4)}\to S^{(6)}$ is bijective — by (1.2) and H1, *not* by the choice of $S^{(6)}$.
Hence
$$\iota_*=p_*^{-1}:\ H^\bullet(\mathcal H_0^{\rm cl},Q)\ \xrightarrow{\ \sim\ }\ H^\bullet(V,\tilde\ell_1).\tag{1.7}$$

*What fails if $S^{(6)}$ is the whole gh-6 part of $\mathrm{Sym}^2\mathcal H_0$.* This is the natural
alternative to A2 and it does not work, for a reason worth recording as part of the regime of validity.
Take $S^{(6)}_{\rm full}:=\mathrm{Sym}^2\mathcal H_0|_{N_{\rm gh}=6}$ (dimension $5$ in the model of A1
against $\dim S^{(4)}=3$) and the unprojected $m_2$ as the differential. Then:
(i) $h=-\tfrac{12}{g^2}m_2^{-1}$ is undefined on any complement of $\operatorname{im}m_2$, and no
extension repairs the contraction: $\tilde\ell_1h+h\tilde\ell_1$ always lands in
$\operatorname{im}m_2$, while $\mathrm{id}-ip=\mathrm{id}$ on $S^{(6)}_{\rm full}$, so the second
relation of (1.6) fails on the complement whatever $h$ is chosen to be there — this argument uses
no dimension count and therefore survives in infinite dimension;
(ii) in the finite-dimensional model, additionally, $m_2:S^{(4)}\to S^{(6)}_{\rm full}$ cannot be
surjective for dimensional reasons, so $H^1$ of the $\Sigma$ sector is $\operatorname{coker}m_2\neq0$
and $\iota$ is **not** a quasi-isomorphism;
(iii) the extra states are $\mathcal H_0^{(2)}\odot\mathcal H_0^{(4)}$ and
$\mathcal H_0^{(1)}\odot\mathcal H_0^{(5)}$, i.e. exactly the ones A2 removes together with the gauge
parameters. The truncation of $\mathcal H_0$ *before* taking $\mathrm{Sym}^2$ is therefore not a
convenience: it is what makes the $\Sigma$ sector a two-term complex with equal-dimensional terms.

\subsection*{Commentary}

(1.2): this is the repair of the record's first version, where $S^{(6)}$ was *defined* as $m_2S^{(4)}$.
With that definition surjectivity held by construction and H1 was credited with a property half of
which had been built in. In the present form both halves come from the same source, the
non-degeneracy of $V_4$ on $S^{(4)}$, and that source is PH1 — an assumption about the vertex, falsifiable
by a null vector of $V_4$ in $\mathrm{Sym}^2\mathcal H_0^{(2)}$ that is not already in $\ker V_4$.
(1.3): the reason $\tilde\ell_1^2=0$ here is the truncation A2, not an identity of $m_2$ — on the full
$\mathrm{Sym}^2\mathcal H_0$ one has $\tilde\ell_1^2=\tfrac{g^4}{144}m_2^2\neq0$ (029 assumption (i)).
This is why the classical complex is the only class on which homological perturbation theory can even
be posed here; A2 is forced by the structure, not chosen for convenience.
(1.5): the factor $-12/g^2$ is fixed by (1.6) and by nothing else; note that it carries $g^{-2}$, so
$h$ is *not* a formal power series in $g$ — the transfer is a rearrangement at fixed $g$, and the
$g$-counting of the transferred brackets below comes out right only because the $g^{-2}$ of $h$
cancels the $g^2$ of the $\mathrm{Sym}^2$-valued bracket. Standard homological-perturbation statements
(Kadeishvili; Kajiura, arXiv:math/0306332; Hohm & Zwiebach, arXiv:1701.08824 §4; Arvanitakis, Hohm,
Hull & Lekeu, arXiv:2007.07942) assume the perturbation to be a formal series in a deformation
parameter, which $h\propto g^{-2}$ is not. This record therefore does not invoke those theorems: the
recursion (2.1) is solved explicitly, it terminates at order 3, and the morphism identities are
checked directly (§3), so no convergence or formality argument is needed. The one place where a
theorem would ordinarily be used — cyclicity of the transferred structure — is replaced by the
explicit statement that $h$ is cyclic and that the transferred brackets *are* $\mathsf T$'s, whose
cyclicity is R8.
*Uniqueness*: this is what makes the later exclusion (C5) sharp — there is no alternative homotopy.

\subsection*{Result}

$$\boxed{\ \text{On the classical complex, }(p,i,h)\text{ of }(1.5)\text{ is a contraction of }
(V,\tilde\ell_1)\text{ onto }(\mathcal H_0^{\rm cl},Q),\ h\text{ unique, }\iota\text{ a quasi-isomorphism of complexes.}\ }\tag{1.8}$$

\subsection*{Verification}

Checks C1.0-dual (the matrix of $m_2^{\rm cl}$ in the bases of $S^{(4)},S^{(6)}$ equals
$\Omega_2^{-1}V_4|_{S^{(4)}}$, i.e. (1.2), with $\Omega_2$ the $\omega_2$ pairing matrix),
C1-rank ($m_2^{\rm cl}$ injective, hence bijective in the model, with break leg C1-rank' making $V_4|_{S^{(4)}}$ degenerate and
turning both C1-rank and C1-acyclic into FAIL), C1.5-span ($m_2S^{(4)}\neq S^{(6)}$, so the projector
$\Pi_2$ is not vacuous), C1-sidecond (the five relations of (1.6) at generic data, break leg
C1-sidecond' perturbing the $-12/g^2$ factor), C1-acyclic (the cohomology of
$(V,\tilde\ell_1)$ computed as $\dim\ker-\dim\operatorname{im}$ from the explicit matrix of
$\tilde\ell_1$ on $V$, compared with $H(\mathcal H_0^{\rm cl},Q)$; break legs C1-acyclic' and
C1-acyclic''). The uniqueness of $h$ (C1.3) has no check of its own: the reduction of $\eta=h'-h$ to
$\ker m_2^{\rm cl}$ is an argument, and its only numerical input is the injectivity C1-rank already
reports; the script prints that datum again under the label C1-rank/unique and does not count it.
What C1-rank establishes is injectivity, equal to bijectivity only because
$\dim S^{(4)}=\dim S^{(6)}$ in the model; the level-uniform half of PH1 (stable $\ker V_4^{(L)}$,
no persistent on-shell zero) is not checked and cannot be in a model of one fixed dimension. See `codes/verify-hpt-transfer.py`.

## §2 The transfer: recursion, transferred brackets, transfer map

\subsection*{Setup}

Uses A1–A3, H1, C1. Write $\tilde{\mathcal L}(\Phi)=\tilde\ell_1\Phi+B(\Phi)$,
$B(\Phi):=\tfrac12\tilde\ell_2(\Phi,\Phi)$, and likewise
$\mathcal L^{\rm tr}(\psi)=\sum_{n\ge1}\tfrac1{n!}\ell_n^{\rm tr}(\psi^n)$ on $W$. All inputs are even
(A1), so no suspension signs appear (029 §1, "Suspension, shown once").

\subsection*{Derivation — the recursion and its sign}

Rather than quote a tree formula (whose sign depends on the convention for $dh+hd$), fix the
transfer by its defining recursion, compatible with the convention $\tilde\ell_1h+h\tilde\ell_1
=\mathrm{id}-ip$ of (1.6):
$$F(\psi)=i\psi-h\,B\big(F(\psi)\big),\qquad
\mathcal L^{\rm tr}(\psi):=p\,\tilde{\mathcal L}\big(F(\psi)\big).\tag{2.1}$$
The recursion terminates order by order in $\psi$ because $h$ raises the polynomial degree of the
argument. Two identities are used repeatedly:
$$p\,\tilde\ell_1h=p(\mathrm{id}-ip-h\tilde\ell_1)=p-(pi)p-(ph)\tilde\ell_1=0,\qquad h\,i=0.\tag{2.2}$$

*Order 1.* $F^{(1)}=i\psi$, and $\mathcal L^{\rm tr}\big|_1=p\,\tilde\ell_1i\psi=Q\psi$, so
$$\ell^{\rm tr}_1=Q=\ell_1^{\mathsf T}.\tag{2.3}$$

*Order 2.* $F^{(2)}=-h\,PB(i\psi)$. From 029 (1.5),
$B(i\psi)=\tfrac12\tilde\ell_2(i\psi,i\psi)=\big(\tfrac g2\ell_2(\psi,\psi),\ \tfrac{g^2}{12}m_2\psi^{\otimes2}\big)$,
with $\psi^{\otimes2}\in S^{(4)}$; projecting on the classical complex (A2) replaces $m_2$ by
$m_2^{\rm cl}$, so
$$F^{(2)}=-\Big(0,\ -\tfrac{12}{g^2}(m_2^{\rm cl})^{-1}\cdot\tfrac{g^2}{12}m_2^{\rm cl}\psi^{\otimes2}\Big)
=\big(0,\ \psi^{\otimes2}\big).\tag{2.4}$$
The projector cancels out of $F^{(2)}$ entirely: $h$ inverts the *same* truncated operator that the
source vertex produces, so the A2 repair leaves (2.4) — and therefore every result of §2 — unchanged.
The transferred bracket: $\mathcal L^{\rm tr}\big|_2=p\,\tilde\ell_1F^{(2)}+p\,B(i\psi)
=0+\tfrac g2\ell_2(\psi,\psi)$ by (2.2), hence
$$\tfrac12\ell^{\rm tr}_2(\psi,\psi)=\tfrac g2\ell_2(\psi,\psi)\ \Longrightarrow\
\ell^{\rm tr}_2=g\,\ell_2=\ell_2^{\mathsf T}.\tag{2.5}$$

*Order 3.* The cubic part of $B(F)$ is $\tilde\ell_2\big(F^{(1)},F^{(2)}\big)
=\tilde\ell_2\big(i\psi,(0,\psi^{\otimes2})\big)=\big(\tfrac{g^2}6\ell_3(\psi^{\otimes2},\psi),\,0\big)
=\big(\tfrac{g^2}6\ell_3(\psi^3),\,0\big)$, purely $\mathcal H_0$-valued, so
$$F^{(3)}=-h\big(\tfrac{g^2}6\ell_3(\psi^3),0\big)=0\tag{2.6}$$
($h$ kills $\mathcal H_0$). The transferred bracket:
$\mathcal L^{\rm tr}\big|_3=p\,\tilde\ell_1F^{(3)}+p\,\tilde\ell_2(F^{(1)},F^{(2)})
=0+\tfrac{g^2}6\ell_3(\psi^3)$, hence
$$\tfrac16\ell^{\rm tr}_3(\psi^3)=\tfrac{g^2}6\ell_3(\psi^3)\ \Longrightarrow\
\ell^{\rm tr}_3=g^2\ell_3=\ell_3^{\mathsf T}.\tag{2.7}$$
In tree form the same statement reads
$\tfrac16\ell^{\rm tr}_3(\psi^3)=-\tfrac12\,p\,\tilde\ell_2\big(i\psi,\ h\,\tilde\ell_2(i\psi,i\psi)\big)$,
one tree with one internal $h$-line, the three shuffles of $\{1,2,3\}$ being identical on the
diagonal; the internal line carries $h\,\tilde\ell_2(i\psi,i\psi)=(0,-2\psi^{\otimes2})$, in which the
propagator $(m_2^{\rm cl})^{-1}$ has cancelled against the source vertex $\tfrac{g^2}{12}m_2^{\rm cl}$ — the
$\Sigma$-exchange diagram, with no inverse surviving in the answer.

*Orders $\ge4$.* By (2.6), $F^{(3)}=0$; the quartic part of $B(F)$ is
$\tilde\ell_2(F^{(1)},F^{(3)})+\tfrac12\tilde\ell_2(F^{(2)},F^{(2)})$, and both vanish — the first by
(2.6), the second because $\tilde\ell_2(\Sigma,\Sigma)=0$ (029 (1.5)). Inductively
$F^{(n)}=0$ and $\mathcal L^{\rm tr}\big|_n=0$ for all $n\ge4$, so
$$\ell^{\rm tr}_{n\ge4}=0.\tag{2.8}$$

\subsection*{Result}

$$\boxed{\
F(\psi)=\big(\psi,\ \psi^{\otimes2}\big)\ \text{exactly}:\quad \phi_1=\iota,\quad
\phi_2(A,B)=\big(0,\ A\odot B\big),\quad \phi_{n\ge3}=0,
\ }\tag{2.9}$$
$$\boxed{\
\big(\ell^{\rm tr}_1,\ell^{\rm tr}_2,\ell^{\rm tr}_3,\ell^{\rm tr}_{\ge4}\big)
=\big(Q,\ g\ell_2,\ g^2\ell_3,\ 0\big)=\mathsf T\ \text{exactly, with the project normalisation.}
\ }\tag{2.10}$$

\subsection*{Commentary}

(2.4) is the point of the whole record: the homological-perturbation transfer map is not merely
*compatible with* the comparison map of 029 — it **is** $(\iota,\cdot^{\otimes2})$, and it fixes the
normalisation $c=1$ of 029 (1.6) from the contraction data instead of from the $\Sigma$-EOM. Free-constants
bookkeeping, stated precisely: $c$ is fixed by the side condition (1.6), which sets $h$'s normalisation
from the $\Sigma$ kinetic coefficient $-\tfrac{g^2}{12}m_2$, together with the source coefficient
$\tfrac{g^2}{12}$ of $\tilde\ell_2|_{\mathrm{Sym}^2}$. So $c=1$ is *not* fitted from the morphism
identity it is then used to test (029's falsifier) — that is the sense in which it is determined here
and was free in 029. It is *not* an independent determination of the $2{:}1$ source-to-kinetic ratio of
$S_{\rm HS}$: that ratio is the input, and R11 records its falsifier ("equality fails for source
coefficient $\neq2$").
(2.6) is why $\phi_3=0$ is a derived statement and not the ansatz of 029: the order-3 source is
$\mathcal H_0$-valued and $h$ annihilates $\mathcal H_0$.
(2.7) versus R10: R10 obtained $V_4^{\rm transf}=V_4$ by completing the square in $\Sigma$ in the
*action*, and flagged that its route (B), the propagator form, was a diagrammatic restatement whose
tree combinatorics were assumed rather than computed. Equation (2.7) computes those combinatorics:
one tree, factor $-\tfrac12\cdot(-2)\cdot\tfrac{g^2}{6}\cdot\ldots$ assembling to $+\tfrac{g^2}6$.
This is therefore the second route R10 was missing, at the level of brackets rather than of the
action. It is a second *route*, not an independent *check*: it reads the same $S_{\rm HS}$ as route
(A) and, unlike route (A), it requires $(m_2^{\rm cl})^{-1}$ and is therefore conditional on H1.

\subsection*{Verification}

Checks C2.1–C2.3 ($\ell^{\rm tr}_n$ against $\mathsf T$ at generic $\psi$, arities 1–3, with the
whole recursion evaluated numerically and not symbolically re-substituted), C2.4 ($\ell^{\rm tr}_4=0$),
C3.1 ($F^{(2)}=\psi^{\otimes2}$, $F^{(3)}=0$), break legs C2.3' (propagator rescaled by 2 ⇒ FAIL) and
C2.3'' ($h$ sign flipped ⇒ FAIL), limiting case C2-V3zero ($\ell_2=0$: $\ell^{\rm tr}_3$ unchanged),
and C2-gscale (the transferred brackets recomputed at four values of $g$ and the exponents fitted from
$\log|\ell^{\rm tr}_n|$ versus $\log g$: $n-1$ for $n=1,2,3$, so the $g^{-2}$ of $h$ does cancel the
$g^2$ of the $\mathrm{Sym}^2$-valued bracket).

## §3 The morphism identities on the classical complex; quasi-isomorphism

\subsection*{Setup}

Uses A1–A3, H1, C1–C3. $\mathsf T^{\rm cl}$, $\mathsf E^{\rm cl}$ denote the two algebras restricted
to the classical complex (A2). The morphism components of $F$ on $\mathsf T^{\rm cl}$ are those of
(2.9) followed by the truncation projector $P$ onto $V$:
$$\phi_1=\iota,\qquad \phi_2=P\circ\odot,\qquad\phi_{n\ge3}=0.\tag{3.1}$$

\subsection*{Derivation}

*Which identities are non-vacuous.* Every term of the $n$-input morphism identity — LHS
$\tilde\ell_k(\phi_{i_1},\dots,\phi_{i_k})$, RHS $\phi_k(\ell_j(\cdots),\cdots)$ — is a map
$W^{\odot n}\to V$ of degree $\sum_a\deg x_a+1$, since brackets have degree $+1$ and the $\phi_n$
degree $0$. $W$ and $V$ are concentrated in degrees $\{0,1\}$ (1.1). Hence
$$\text{if any input has }\deg x_a=1,\ \text{both sides land in degree}\ \ge2\ \text{and vanish}.\tag{3.2}$$
The only non-vacuous identities are those with all inputs in $W^0=\mathcal H_0^{(2)}$, and by
polarisation (characteristic zero, even inputs) they are equivalent to the single
generating-function identity at $\psi\in W^0$.

The same counting applies to the $L_\infty$ *relations*, and this must be said plainly (C4.0), because
it bounds what the headline claim is worth. On a complex concentrated in degrees $\{0,1\}$ every
$L_\infty$ relation also lands in degree $2$: any collection of degree-$+1$ multilinear maps is an
$L_\infty$ algebra there, and any collection of degree-$0$ maps with $\phi_1$ a chain map is an
$L_\infty$ morphism. Hence "$\mathsf E^{\rm cl}$ is an $L_\infty$ algebra" (C1.1) and "$F$ is an
$L_\infty$ morphism" (C4) carry no information by themselves; the information is entirely in three
statements: (i) the transferred brackets equal those of the quartic theory, $\ell^{\rm tr}
=\ell^{\mathsf T}$ (§2); (ii) $\iota_*$ is an isomorphism on $\tilde\ell_1$-cohomology (§1); (iii)
cyclicity. Everything below should be read against that bound.

*The identity at $\psi\in W^0$.* With $F(\psi)=(\psi,\psi^{\otimes2})$ and
$\mathcal L^{\rm tr}=\mathcal L$ by (2.10), 029 (2.7) gives
$$\tilde{\mathcal L}\big(F(\psi)\big)=\big(\mathcal L(\psi),\,0\big),\qquad
dF\big|_\psi\big[\mathcal L(\psi)\big]=\big(\mathcal L(\psi),\ \mathcal L(\psi)\odot\psi\big),\tag{3.3}$$
so the defect is $\big(0,-\mathcal L(\psi)\odot\psi\big)$ — 029's obstruction. For $\psi$ at
$N_{\rm gh}=2$, $\mathcal L(\psi)$ sits at $N_{\rm gh}=3$ and
$$\mathcal L(\psi)\odot\psi\ \in\ S^{(5)},\qquad S^{(5)}\cap V=0\ \text{ by A2},\tag{3.4}$$
i.e. the defect is *identically outside the classical complex*, and $P\big(\mathcal L(\psi)\odot\psi\big)=0$.
Hence on $\mathsf T^{\rm cl}\to\mathsf E^{\rm cl}$ the defect vanishes and
$$\tilde{\mathcal L}\big(F(\psi)\big)=dF\big|_\psi\big[\mathcal L^{\rm tr}(\psi)\big]\quad\text{exactly.}\tag{3.5}$$

*Quasi-isomorphism.* $\phi_1=\iota$ induces the isomorphism (1.7) on $\tilde\ell_1$-cohomology,
because $m_2^{\rm cl}:S^{(4)}\to S^{(6)}$ is bijective ((1.2), H1). So $F$ is an $L_\infty$-morphism
$\mathsf T^{\rm cl}\to\mathsf E^{\rm cl}$ whose linear part is a quasi-isomorphism of complexes:
an $L_\infty$ quasi-isomorphism. Note that $F$ is *not* strict — $\phi_2=\odot\neq0$; what is true,
and what distinguishes this from 029, is that the identities hold **exactly, not merely on shell**.

*Cyclicity.* $\omega_2(A,m_2^{\rm cl}B)=V_4(A,B)$ by (1.2), and $V_4$ is graded symmetric on the even
sector (R7, R8: full graded symmetry of $V_4$ is a vertex property). Two distinct exchange signs
enter, and both are $+$ on the even sector; written out, with $x=m_2^{\rm cl}A$, $y=m_2^{\rm cl}B$
and $A,B\in S^{(4)}$:
$$\omega_2\big((m_2^{\rm cl})^{-1}x,\,y\big)=\omega_2(A,m_2^{\rm cl}B)
\overset{(1.2)}{=}V_4(A,B)\overset{\rm(s1)}{=}V_4(B,A)=\omega_2(B,m_2^{\rm cl}A)=\omega_2(B,x)
\overset{\rm(s2)}{=}\omega_2\big(x,(m_2^{\rm cl})^{-1}y\big).$$
Sign (s1) is the graded symmetry of the vertex $V_4$ under exchange of its two $\mathrm{Sym}^2$
slots (R7, R8), $+$ on even inputs. Sign (s2) is the exchange symmetry of $\omega_2$ itself:
$\omega_2=\omega_1^{\otimes2}$, so swapping its two $\mathrm{Sym}^2$ arguments produces the *square*
of $\omega_1$'s exchange sign, hence $+$ regardless of whether $\omega_1$ is symmetric or
antisymmetric. They are different statements and only their product matters here; both being $+$,
$h$ of (1.5) is a
*cyclic* homotopy with respect to $\omega_1\oplus\omega_2$; the transferred structure is then cyclic
with respect to $\omega_1$, as $\mathsf T$ is, and the transferred action equals
$S_{\rm eff}$ of 029 (1.3) — the bracket-level counterpart of R10's action-level equality.

\subsection*{Commentary}

(3.2) is the whole content of "the classical complex": an $L_\infty$ algebra concentrated in degrees
$\{0,1\}$ has no gauge directions and no antifields, so every bracket and every morphism component
is determined by its restriction to the field slot, and every identity with a higher-degree input is
empty. The quasi-isomorphism of (3.5) is therefore a statement about *fields and equations of
motion* and their cohomology, not about the gauge algebra — which R11 handles separately, through
the composite law.
(3.4) resolves the apparent conflict with R36. 029's defect is real and 029's conclusion stands on
the space 029 works on; it lives at $N_{\rm gh}=5$ in $\mathrm{Sym}^2$, i.e. precisely in the sector
where 029 §1 (ii) already showed the grading 029 (1.7) to be half-integer and $\mathsf E$ not to be a
graded $L_\infty$ algebra at all. On the classical complex, where $\mathsf E$ *is* one, the defect is
not there to cancel — it is absent. What that costs is stated in A2: the excluded sector $S^{(5)}$ is
field-built, and the exclusion is a grading convention, not a statement about the field content.
Cyclicity: the sign convention of the exchange is R7's (graded symmetric $\omega_2$ on the even
sector); the statement used here is only that $(m_2^{\rm cl})^{-1}$ inherits whatever exchange sign
$m_2^{\rm cl}$ has, which is sign-convention independent.

\subsection*{Result}

$$\boxed{\
\text{Under H1, }F=(\iota,\cdot^{\otimes2})\text{ is a cyclic }L_\infty\text{ quasi-isomorphism }
\mathsf T^{\rm cl}\to\mathsf E^{\rm cl}\text{, the identities holding exactly, not on shell.}\ }\tag{3.6}$$

\subsection*{Verification}

Checks C4.1 (defect of (3.3) projected on $V$ vanishes at generic $\psi$, while the unprojected
defect does not — the same quantity 029 check D0 finds nonzero), C4.2 (the same identity at a generic
superposition of four $W^0$ vectors, repeated ten times; this is a genericity test of the same
polynomial identity as C4.1, not a separate test of arities $1,\dots,4$ — by polarisation the
arity-resolved statements follow from it, but the check does not resolve them), C4.4 (cyclicity of
$h$ with respect to $\omega_2$, with break leg C4.4' composing $h$ with a non-symmetric map in the
$S^{(4)}$ basis ⇒ FAIL), C4.5 (the primitive in $t$ of $\omega_1(\psi,\mathcal L^{\rm tr}(t\psi))$
compared with $S_{\rm eff}(t\psi)$ *assembled from the raw vertices*
$\tfrac12\omega_1(\psi,Q\psi)+\tfrac g{3!}V_3+\tfrac{g^2}{4!}V_4$ of 029 (1.3) — a second method for
C4.3, since it additionally tests that a primitive exists and fixes the relative cubic/quartic
weight; break leg C4.5' rescales $V_4$ by $1.5$ ⇒ FAIL),
break leg C4.1' ($\phi_2$ rescaled to $1.3\,\cdot^{\otimes2}$ ⇒ the identity FAILS). The cohomology
statement is checked by C1-acyclic (§1), not by a check named C4.3.

## §4 The obstruction off the classical complex

\subsection*{Setup}

Uses A1, A3, H1, C1–C4, and 029 §1 (ii). The question: can the contraction, hence the transfer, be
extended to a complex containing the gauge directions — $\Lambda\in\mathcal H_0$ at $N_{\rm gh}=1$,
degree $-1$ — and the composite states $\Lambda\odot\psi$, $\Lambda\odot\Lambda$ they force into
$\mathrm{Sym}^2\mathcal H_0$?

\subsection*{Derivation}

An extension needs a grading $h(n)$ of $\mathrm{Sym}^2\mathcal H_0$ by total ghost number $n$ such that
every bracket of 029 (1.5) has degree $+1$ and every $\phi_n$ degree $0$. With
$\deg_{\mathcal H_0}=N_{\rm gh}-2$ the three constraints are (029 §1 (ii), rewritten as slopes):
$$\text{(a) } m_2:\ h(n+2)=h(n)+1\ \ (\text{slope }\tfrac12);\qquad
\text{(b) } \tilde\ell_2(A,B)\big|_{\mathrm{Sym}^2}:\ h(n)=n-5;\qquad
\text{(c) } \tilde\ell_2(\psi,\Sigma):\ h(n)=n-4,\tag{4.1}$$
(b) and (c) of slope $1$. On the classical complex the three constraints are realised at disjoint
arguments — (c) only at $n=4$, (b) only at $n=6$, (a) only on $4\mapsto6$ — and are satisfied
together by $h(4)=0,\ h(6)=1$, which is (1.7). Admitting $\Lambda$ at $N_{\rm gh}=1$ makes them
overlap and inconsistent: (b) at $a=b=1$ ($\Lambda\odot\Lambda$, $n=4$) demands $h(4)=-1$ against
(c)'s $h(4)=0$; and (a) with slope $\tfrac12$ against (b)–(c)'s slope $1$ fails at every second
value once the ghost-number support of $\mathrm{Sym}^2$ has more than the two classical values. The
mod-2 reduction fails as well (029 §1 (ii); script check G3 there).

*The antifield case, in two lines.* Admit instead $\mathcal H_0$ states at $N_{\rm gh}=4$ (the
antifields of the gh-2 fields, $\deg=2$), with no gauge parameter. Then $\mathrm{Sym}^2$ acquires
$n=8$ through $\mathcal H_0^{(4)}\odot\mathcal H_0^{(4)}$, and constraint (b) applies there via
$\tilde\ell_2(\psi^{(2)},\psi^{(4)})|_{\mathrm{Sym}^2}=\tfrac{g^2}{12}m_2(\psi^{(2)}\odot\psi^{(4)})$,
whose output sits at $n=2+4+2=8$: $h(8)=8-5=3$. But (b) at $a=b=2$ already fixes $h(6)=1$, and (a)
applied to $m_2:\mathrm{Sym}^2_6\to\mathrm{Sym}^2_8$ then forces $h(8)=h(6)+1=2$. Three against two:
the same slope-$\tfrac12$ versus slope-$1$ conflict, one step to the right. So C5 is derived for
both classes of extension named in (i) — gauge parameters at $N_{\rm gh}=1$ and antifields at
$N_{\rm gh}=4$ — and not merely for the gauge parameters.

There is no freedom left to repair this: $h$ is unique (C1), $c=1$ is forced (2.4), and
$\phi_{n\ge3}=0$ is forced (2.6) — the three degrees of freedom that 029 had to leave open are all
fixed by the contraction data.

The invariant form of the obstruction, free of any choice of grading. A morphism component
$\phi_2=\odot$ is a *slope-one* operation: it sends a pair of $\mathcal H_0$ degrees to their sum. A
differential on $\mathrm{Sym}^2\mathcal H_0$ compatible with it must raise total ghost number by
**one**. The $\Sigma$-sector differential produced by the Hubbard–Stratonovich step is
$-\tfrac{g^2}{12}m_2$ with $N_{\rm gh}(m_2)=+2$. Hence
$$\boxed{\ \text{obstruction}\ =\ N_{\rm gh}(m_2)=+2\ \text{where a differential compatible with }
\phi_2=\odot\ \text{needs}\ +1.\ }\tag{4.2}$$

### Relation to R7 — a common source, not one obstruction counted twice

The first version of this record asserted that (4.2) "is R7's parity mismatch counted twice". That
identification is **not derived** and is demoted here to the weaker statement that survives scrutiny.
What is common is the source. Both defects come from the $\mathrm{Sym}^2$ structure carrying two
copies of the $\mathcal H_0$ data: $\omega_2=\omega_1^{\otimes2}$ has two $c_0^-$ insertions where an
odd symplectic form wants one (R7), and $m_2=\Delta^{\otimes2}V_4$ has two $\Delta$'s, hence
$N_{\rm gh}(m_2)=2N_{\rm gh}(\Delta)+N_{\rm gh}(V_4)$ giving $+2$ where $N_{\rm gh}(\ell_3)$ gives
$+1$. In both cases the offending $2$ is the number of strands.

What is *not* common is the invariant, and this is why the identification fails. R7's mismatch is a
**parity**: it is cured by the uniform one-unit shift $\omega_2^{\rm symp}=\omega_1^{\otimes2}\circ
(s\otimes s)$, after which $m_2$ is cyclic with respect to the shifted form. The mismatch of (4.2) is
a **slope**: constraint (a) of (4.1) reads $h(n+2)-h(n)=1$ while (b)–(c) read $h(n+1)-h(n)=1$, and a
uniform shift $h(n)\mapsto h(n)+s$ leaves every *difference* $h(n+k)-h(n)$ untouched. Hence
$$\text{no uniform degree shift changes (4.1); R7's cure is unavailable here.}\tag{4.3}$$
An obstruction that a shift removes and one that survives every shift are different invariants of the
same underlying two-strand structure. The statement retained is therefore: *both trace to the two
$c_0^-$ insertions of $\omega_2$ (equivalently, the two $\Delta$'s of $m_2$)*; whether they are two
faces of a single obstruction is open and is not claimed.

### Scope of the exclusion

*Class covered.* Any extension of the classical complex that (i) admits $\mathcal H_0$ states of
ghost number other than $\{2,3\}$ — in particular the gauge parameters at $N_{\rm gh}=1$ and the
antifields — with $\deg=N_{\rm gh}-2$, (ii) grades $\mathrm{Sym}^2\mathcal H_0$ by a function of total
ghost number, over $\mathbb Z$, $\tfrac12\mathbb Z$ or $\mathbb Z_2$, and (iii) keeps the brackets 029
(1.5) as read off $S_{\rm HS}$ and $\phi_2$ of slope one. The physical reason for the class is that
(i)–(iii) are exactly the data of the BV formulation of the HS theory as it stands; nothing weaker
would be a statement about *this* theory.

*Relevant cases outside the class.* The physically first one, and the one a reader asks about
immediately, is condition (iii): **any presentation in which the $\Sigma$ sector has a $Q$-kinetic
term.** 029 and R36 trace the whole defect to the fact that in presentation (b) the $\Sigma$-sector
differential is $-\tfrac{g^2}{12}m_2$ — an algebraic operator of $N_{\rm gh}=+2$ — and not a BRST-like
operator of $N_{\rm gh}=+1$. If a different Hubbard–Stratonovich presentation, a stub-deformed one, or
the dressed tower of PH2 gives $\Sigma$ a differential containing a $Q$-like piece, then (4.1) is a
different linear system, the slope-one constraint (a) is met by construction, and nothing derived in
§4 applies. The project has already built such presentations and studied them geometrically: R30
(derivation 030, the Erbin–Fırat mechanism transplanted to the closed string) replaces the auxiliary
kinetic operator by $\mathcal K=Q_BL_0^+/(e^{\sigma L_0^+}-1)$, which carries $Q_B$ explicitly and is
therefore of $N_{\rm gh}=+1$ on the nose; its options (α-rev), (β2), (α-neck) are exactly the
$Q$-kinetic presentations meant here, and the question left open there is geometric (does the neck
family cover the vertex region), not the grading question of §4. No external reference is needed for
this escape: R30 is it. Such a presentation is *not* excluded by C5; it is the most promising direction the
exclusion leaves open, and it is close to the weakest relaxation below (a factorisation
$m_2=\mathcal B\mathfrak m$ is one way of manufacturing a slope-one $\Sigma$-differential from the
data one already has).
Further outside the class: gradings of $\mathrm{Sym}^2\mathcal H_0$ that are not functions of
total ghost number (for instance a grading by the pair of individual ghost numbers, i.e. a
$\mathbb Z^2$- or level-refined grading); and a $\phi_2$ that is not the symmetric square. Both are
untested here, and both are more exotic than the $Q$-kinetic case.

*Weakest relaxation that evades it.* Factor the $\Sigma$-sector kernel as $m_2=\mathcal B\,\mathfrak m$
with $N_{\rm gh}(\mathcal B)=-1$ and $N_{\rm gh}(\mathfrak m)=+1$, take $\mathfrak m$ as the
$\Sigma$-sector differential and $\omega_2':=\omega_2(\cdot,\mathcal B\,\cdot)$ as the $\Sigma$-sector
pairing. The HS action is unchanged — $\omega_2'(\Sigma,\mathfrak m\Sigma)=\omega_2(\Sigma,m_2\Sigma)$ —
while in the slope-one grading $h(n)=n-4$ both (a) and (b)–(c) of (4.1) become $\deg\mathfrak m=+1$,
$\deg\omega_2'=-1$, $\deg\phi_2=0$: the conflict disappears. The price is that $\mathcal B$ must be
*invertible* of ghost number $-1$, which requires the ghost-number support of the $\Sigma$-space to
be shift-invariant; a $b$-ghost insertion ($b_0^\pm$, nilpotent) does not qualify. Whether such a
factorisation of the closed-string $V_4$ kernel exists is open and is the single question on which
the full-BV quasi-isomorphism turns.

\subsection*{Result}

$$\boxed{\ \text{Excl. within the class (i)–(iii) above: the transfer of §2 does not extend off the
classical complex; obstruction (4.2).}\ }\tag{4.4}$$

\subsection*{Verification}

Check C5.1 (the linear system (4.1) with $\Lambda$ at $N_{\rm gh}=1$ admitted has no solution over
$\mathbb Z$ — least-squares residual bounded away from zero — nor over $\mathbb Z_2$ by enumeration;
this reproduces and extends 029 check G3), break leg C5.1' (the same system restricted to the
classical complex is solvable, residual $0$). The uniqueness of $h$ used by C5.3 is check C1-unique
(§1). The row assembler of the check admits gh-5 $\mathrm{Sym}^2$ pairs into the system, which A2
excludes; ghost-number arithmetic removes those rows, so the system solved is A2's, but the check is
not *restricted* to A2 by construction and the script comment says so.

## §5 Answer to the objective, and what the paper may say

**Direct answer.** Yes, with a stated scope. Under H1 (= PH1) and in the finite-dimensional model,
integrating $\Sigma$ out *is* a homological-perturbation transfer, it reproduces the
quartic-truncated theory exactly, and the resulting map is an $L_\infty$ quasi-isomorphism — on the
**classical complex**, i.e. on fields and equations of motion (degrees $\{0,1\}$). It is **not** one
on any extension admitting gauge parameters. PH8 is **confirmed in the finite-dimensional model**
(C1–C4 under H1 and A2); PH8's statement on $\mathrm{Sym}^2\mathcal H_0/\ker V_4$ itself is not
established here, and its falsifier ("the grading obstruction persisting on the classical complex")
does not trigger. R36's directive "no quasi-isomorphism claim" is right for the unqualified claim and
too strong for the qualified one.

Two qualifications belong in the same breath. First, on a complex concentrated in degrees $\{0,1\}$
the $L_\infty$ relations and morphism identities are themselves vacuous (C4.0): the words "$L_\infty$
quasi-isomorphism" carry exactly three statements here — transferred brackets equal to
$\mathsf T$'s, $\iota_*$ an isomorphism on cohomology, and cyclicity. Second, the map is **not
strict** ($\phi_2=\odot\neq0$); what is exact rather than on-shell is the *validity* of the
identities, which is the contrast with 029.

**Three findings, in order of value.**

1. The transfer map is not a new map: it is exactly $(\iota,\cdot^{\otimes2})$, with $\phi_3=0$
   (C3, C2.4). 029's candidate was the right one; what 029 lacked was the class on which it works.
   The normalisation $c=1$, which 029 kept free as a falsifier of the morphism identity, is here
   fixed by the contraction data — i.e. by the $\Sigma$ kinetic and source coefficients of
   $S_{\rm HS}$, not by the identity under test. It is not an independent determination of the
   $2{:}1$ source-to-kinetic ratio; that ratio is an input (R11 records its falsifier).
2. $\ell^{\rm tr}_3=g^2\ell_3$ (C2.2) is the second route R10 explicitly flagged as missing: R10's
   route (B) assumed the tree combinatorics reproduce route (A)'s $1/4!$; (2.7) computes them. It is
   a second route, not an independent one — same $S_{\rm HS}$, and conditional on H1 where route (A)
   is not. The check is falsifiable (C2.3', C2.3'': rescaling or flipping the propagator breaks it).
3. The obstruction is a single number: $N_{\rm gh}(m_2)=+2$ where a differential compatible with
   $\phi_2=\odot$ needs $+1$ (C5.2). It shares its source with R7's parity mismatch — the two
   $c_0^-$ insertions of $\omega_2$, equivalently the two $\Delta$'s of $m_2$ — but it is a different
   invariant: R7's is cured by a uniform degree shift, this one is a slope and no shift changes it
   (4.3). That the two are one obstruction is *not* claimed.

**Recommended wording for the paper.** Keep R10/R11/R22 as the primary statement (elimination of an
algebraic auxiliary field). The quasi-isomorphism may now be *added* in one qualified sentence: on
the classical complex — fields and equations of motion, the sector on which the cubic theory carries
a $\mathbb Z$-graded $L_\infty$ structure at all — the elimination of $\Sigma$ is a homological-
perturbation transfer whose transfer map is $\Psi\mapsto(\Psi,\Psi^{\otimes2})$ and which is a cyclic
$L_\infty$ quasi-isomorphism onto the quartic-truncated theory, conditionally on the quartic form
being invertible on the quotient by its kernel level by level, with a kernel that stabilises with
the level — a statement we verify in a finite-dimensional model of the vertex data, and which
beyond it rests on that level-uniformity. The sentence must not be extended to the gauge algebra or to the BV complex,
where the ghost-number counting of the quartic kernel obstructs it; there the gauge statement is
R11's composite law.

**What this does *not* buy.** An $L_\infty$ algebra concentrated in degrees $\{0,1\}$ has no gauge
directions, so the quasi-isomorphism of (3.6) controls the equations of motion — the solution sets
of $\mathcal L^{\rm tr}$ and $\tilde{\mathcal L}$ correspond, and their linearisations $\ker Q$ and
$\ker\tilde\ell_1$ do too — and nothing else. It says nothing about the gauge algebra, and nothing
about the physical (BRST) spectrum: $H^0$ of the truncated complex is $\ker Q|_{\mathcal H_0^{(2)}}$
*without* the quotient by $Q\mathcal H_0^{(1)}$, because A2 deleted the gh-1 states, so it is the
space of linearised solutions and not linearised solutions modulo gauge. Comparing physical spectra
would require acyclicity of the $\Sigma$ sector on a complex containing gh 1 and gh 4 — exactly what
§4 excludes within class (i)–(iii).
The qualified claim strengthens R8/R10, but by less than the three-item list suggests. Of C4.0's
items, genuinely new here is (i): the transferred brackets equal those of the quartic theory by an
explicit tree computation (R10's route (B) combinatorics, computed rather than assumed), together
with $\phi_{n\ge3}=0$ derived and the normalisation $c=1$ fixed by the contraction data. Item (ii),
"$\iota_*$ an isomorphism on cohomology", reduces — since $\phi_1=\iota$ is the identity on the
$\mathcal H_0$ factor — to acyclicity of the $\Sigma$ sector, i.e. to H1 = PH1 restated. Item (iii)
is R8 once (i) is known, the new part being only cyclicity of $h$. The
interesting open question is C5.4.

## Proposed ledger row

R41 — *Integrating $\Sigma$ out is a homological-perturbation transfer; quasi-isomorphism on the
classical complex, obstructed off it* (derivation 037, script `codes/verify-hpt-transfer.py`,
31/31 report lines PASS on seeds 2037, 7, 11 — 30 distinct checks, one line restating C1-rank). Classical complex (037 A2): $\mathcal H_0$ truncated to
$N_{\rm gh}\in\{2,3\}$ **first**, $\Sigma$ sector its symmetric square,
$S^{(4)}=\mathrm{Sym}^2\mathcal H_0^{(2)}$, $S^{(6)}=\mathrm{Sym}^2\mathcal H_0^{(3)}$, brackets
projected accordingly. There, $\omega_2$ identifies $S^{(6)}\cong(S^{(4)})^*$ and the $\Sigma$-sector
differential $m_2^{\rm cl}=\Pi_2m_2$ *is* the form $V_4|_{S^{(4)}}$, so its **injectivity** is exactly
non-degeneracy of $V_4$ on $S^{(4)}$ (R9's half of PH1) — not a definition; in the
finite-dimensional model injectivity is bijectivity, while beyond it the contraction also needs the
level-uniform half PH1 asserts as restated 2026-09-22 — the inverse on the quotient existing level
by level with a stable kernel, so that $h$ has a level limit (R10, strictly stronger than R9); no
bounded inverse and no auxiliary inner product are assumed, and a contraction in a topological
sense would need more and is not claimed. On that complex the
contraction $(p,i,h)$ with $h=-\tfrac{12}{g^2}(m_2^{\rm cl})^{-1}$ on $S^{(6)}$ exists and $h$ is
unique; the transferred brackets are $(Q,g\ell_2,g^2\ell_3,0)$, i.e. $\mathsf T$ exactly; the transfer
map is $(\iota,\cdot^{\otimes2})$ with $\phi_{n\ge3}=0$ *derived*, and $c=1$ fixed by the contraction
data (the $\Sigma$ kinetic and source coefficients of $S_{\rm HS}$) rather than fitted from the
identity under test; $F$ is a cyclic $L_\infty$ quasi-isomorphism there, the morphism identities
holding **exactly, not on shell**. $F$ is *not* strict ($\phi_2=\odot\neq0$). Scope caveat carried with
the row: on a complex concentrated in degrees $\{0,1\}$ the $L_\infty$ relations and morphism
identities are themselves vacuous, so the content is exactly (i) transferred brackets $=\mathsf T$'s,
(ii) $\iota_*$ an isomorphism on cohomology, (iii) cyclicity — and of these only (i) is new, together
with $\phi_{n\ge3}=0$ derived and $c=1$ fixed: (ii) is PH1 restated (with $\phi_1=\iota$ the identity
on the $\mathcal H_0$ factor, it *is* acyclicity of the $\Sigma$ sector), and (iii) is R8 once (i) is
known, the new part being only cyclicity of $h$. The cohomology statement is about the truncated
complex ($H^0=\ker Q|_{\mathcal H_0^{(2)}}$, no quotient by $Q\mathcal H_0^{(1)}$): it controls the
equations of motion and their linearisation, **not** the physical BRST spectrum and not the gauge
algebra. 029/R36's defect
$-\mathcal L(\Psi)\odot\Psi$ sits at $N_{\rm gh}=5$ in $\mathrm{Sym}^2$, outside the classical complex —
a sector that is field-built and excluded by a grading convention, not by the field content.
*Excl. within the class* (i)–(iii) of 037 §4 (extensions admitting $\mathcal H_0$ states of
$N_{\rm gh}\notin\{2,3\}$, gradings of $\mathrm{Sym}^2$ by total ghost number, brackets as read off
$S_{\rm HS}$; derived for gauge parameters at $N_{\rm gh}=1$ and for antifields at $N_{\rm gh}=4$,
other ghost numbers not enumerated): the transfer does not extend; invariant obstruction
$N_{\rm gh}(m_2)=+2$ against the
required $+1$; no freedom remains to repair it. This obstruction and R7's parity mismatch **both
trace to the two $c_0^-$ insertions of $\omega_2$** (equivalently the two $\Delta$'s of $m_2$), but
they are different invariants — R7's is cured by a uniform degree shift, this one is a slope and no
shift changes it (037 (4.3)); that they are one obstruction is *not* claimed. Outside the class and
not excluded, first in physical relevance: any presentation giving $\Sigma$ a $Q$-kinetic term — the
project's own R30 (derivation 030, Erbin–Fırat mechanism, $\mathcal K=Q_BL_0^+/(e^{\sigma L_0^+}-1)$,
options (α-rev)/(β2)/(α-neck)) builds exactly these, and what is open there is geometric, not the
grading question of §4; also stub deformations and the dressed tower of PH2. Weakest relaxation: an invertible
$\mathcal B$ of $N_{\rm gh}=-1$ with $m_2=\mathcal B\mathfrak m$ — open (037 C5.4). Second route to R10
at the level of brackets (R10's route (B) combinatorics computed, not assumed; same $S_{\rm HS}$ and
conditional on PH1, so not an independent check). Status:
`Conditional(PH1) – Verified (finite-dimensional model)` for C1–C4;
`Conditional(PH1) – Verified (finite-dimensional model)` for the exclusion C5 within its stated class.
Annotation to R36: "the transfer was attempted (037): it reproduces $\mathsf T$ exactly and gives a
quasi-isomorphism on the classical complex — in the finite-dimensional model and conditionally on
PH1 — while R36's failure is the same map read off that complex, at $N_{\rm gh}=5$. The paper
directive becomes: no *unqualified* quasi-isomorphism claim; a qualified one is allowed, and it must
carry (a) the classical-complex restriction, (b) PH1, and (c) the fact that the map is not strict."
Annotation to PH8: confirmed in the finite-dimensional model (037 C1–C4), with the extension off the
classical complex excluded (037 C5); PH8's statement on $\mathrm{Sym}^2\mathcal H_0/\ker V_4$ itself
remains a hypothesis.

## Verification

Symbolic: (1.2)–(1.6), (2.1)–(2.10), (3.1)–(3.5) and (4.1)–(4.3) are one-line consequences of
029 (1.5) and of the degree bookkeeping; each is re-evaluated numerically. Numerical:
`codes/verify-hpt-transfer.py`, **31 report lines, 31/31 PASS on seeds 2037, 7 and 11 — 30 distinct
checks**, the extra line (C1-rank/unique) being a restatement of C1-rank for the uniqueness claim,
labelled as such in the script and excluded from the count it prints; generic random data. The transfer is run as a *numerical fixed-point recursion* and the brackets extracted by a
Vandermonde fit of $\mathcal L^{\rm tr}(t\psi)$ — the closed forms (2.4), (2.7), (2.9) are never
substituted into their own checks. The cohomology is computed from the assembled matrix of
$\tilde\ell_1$ on $V$ by ranks (C1-dmat verifies that the matrix is the operator; C1-acyclic takes the
ranks); no cohomology formula is hard-coded. Break-on-purpose legs: C1-rank' ($V_4$ given a null
direction on $S^{(4)}$), C1-sidecond' ($h\to2h$), C1-acyclic' (same null direction),
C1-acyclic'' (one column of $\tilde\ell_1$ removed), C2.3' ($h\to2h$), C2.3'' ($h\to-h$), C4.1'
($\phi_2\to1.3\,\cdot^{\otimes2}$), C4.4' ($h$ composed with a non-symmetric map on $S^{(4)}$),
C4.5' ($V_4$ rescaled by $1.5$),
C5.1' (the grading system restricted to the classical complex is solvable). Each turns the
corresponding PASS into a FAIL, so no check is vacuous. Limiting case: C2-V3zero ($\ell_2=0$;
$\ell^{\rm tr}_3$ unchanged, $\ell^{\rm tr}_2=0$). Second method: C2.2 against R10, agreeing in sign
and coefficient; C4.5 integrates the transferred equation of motion and recovers $S_{\rm eff}$ as
assembled from the raw vertices $V_3,V_4$ (neither $\mathcal L_{\rm trunc}$ nor the closed forms of
§2 enter its right-hand side). Dimensional/grading:
C2-gscale **measures** the $g$-counting — the transferred brackets are recomputed at
$g\in\{0.4,0.55,0.7,0.9\}$ and the fitted exponents of $\|\ell^{\rm tr}_n\|$ versus $g$ come out
$0,1,2$ to $10^{-6}$, confirming that the $g^{-2}$ of $h$ cancels the $g^2$ of the
$\mathrm{Sym}^2$-valued bracket; degrees are $+1$ in 029 (1.7); the defect is shown to be supported at
$N_{\rm gh}=5$ only (check C4.1-supp).
*Scope of C4.2:* it evaluates the identity at ten generic superpositions of four gh-2 vectors. That
is a genericity test of the same polynomial identity as C4.1; by polarisation the arity-resolved
statements follow, but the check does not resolve arities separately.
**Not verified:** anything about the actual CFT $V_4$ (generic random tensors only); the odd-input
suspension signs (all inputs even here, as in 029); gradings of $\mathrm{Sym}^2\mathcal H_0$ that are
not functions of the total ghost number, and $\phi_2$ of slope $\neq1$ — both outside the exclusion's
class; the existence of the factorisation $m_2=\mathcal B\mathfrak m$ (C5.4, open); the
infinite-dimensional statement, which is H1 = PH1 — in particular the level-uniform half (stable
$\ker V_4^{(L)}$, so that $h$ has a level limit; R10's half of PH1, restated 2026-09-22 without the
bounded-inverse wording), of which the model can only exhibit the injectivity half (R9);
extensions of the complex at $N_{\rm gh}\notin\{1,2,3,4\}$ (not enumerated in §4); whether the obstruction (4.2) and R7's parity
mismatch are one obstruction (C5.2a, explicitly not derived); presentations giving $\Sigma$ a
$Q$-kinetic term (outside the exclusion's class, §4).

## Self-review

1. *Objective or literal task?* Both: the objective (may the paper say "quasi-isomorphic"?) is
   answered with a qualified yes and an explicit scope.
2. *Weakest step.* A2, the choice of the classical complex. In the first version it was worse than
   weak: $S^{(6)}$ was *defined* as $m_2S^{(4)}$, which made the surjectivity half of acyclicity true
   by construction and credited H1 with it. Repaired in this pass: $S^{(4)}$ and $S^{(6)}$ are the
   symmetric squares of the truncated $\mathcal H_0$, and *injectivity* of the (projected)
   differential is (1.2) — the non-degeneracy of $V_4$ on $S^{(4)}$, i.e. the R9 half of PH1; in the
   model, equal dimensions turn it into bijectivity, while beyond the model what the contraction
   needs is PH1's level-uniform half as restated 2026-09-22 (the inverse on the quotient existing
   level by level with a stable kernel, so that $h$ has a level limit; R10), not a bounded inverse
   — a contraction of topological complexes would need more and is not claimed. What remains weak is the truncation
   itself: the excluded sector $S^{(5)}$ is field-built and is removed by a grading convention, which
   §4 then shows cannot be relaxed within class (i)–(iii). A reader who keeps the whole gh-6 block
   gets $\dim S^{(6)}>\dim S^{(4)}$, a nonzero $\operatorname{coker}m_2$, and no contraction at all
   (§1, *What fails if $S^{(6)}$ is the whole gh-6 part*) — the §4 obstruction arriving one step
   earlier, not a different answer.
3. *Not checked, and why acceptable.* The odd-input suspension signs: all objects here are even and
   029 settled the reduction; the CFT data, because the model is explicitly a toy and H1 carries the
   infinite-dimensional statement. Also not checked, and explicitly not claimed: that (4.2) and R7's
   parity mismatch are the same obstruction (C5.2a).
4. *What a stronger physicist would find in five minutes.* C5.4 — whether the closed-string
   $V_4$ kernel admits a ghost-number-$(-1)$ invertible factor. That is the one question that would
   turn the qualified claim into the unqualified one, and it is left open. Next to it, the
   $Q$-kinetic-term presentations of §4: cheaper to test and outside the exclusion.

## Status

Skeleton written (task, conventions, objects, first falsifier, claim-tree stubs) 2026-09-21T15:40;
§1 (contraction data, C1), §2 (transferred brackets and transfer map, C2/C3), §3 (morphism identities
and quasi-isomorphism, C4), §4 (obstruction off the classical complex, C5), §5 (answer to the
objective), claim tree, proposed ledger row R41, Verification and Self-review written 2026-09-21.
Fix pass after `agent/reports/critic-037-20260921T164500.md` completed 2026-09-21T17:40–18:25:
A2 repaired (new nodes C1.0, C1.5, C4.0, C5.2a; §1 rewritten and renumbered, brackets and transfer
map unchanged — (2.4) verified to be projector-independent), R7 identification demoted to a remark
with the shift/slope distinction derived (4.3), $Q$-kinetic-term case added to the scope, script
rewritten (cohomology from the matrix, $g$-scaling, surjectivity/duality and span checks, C4.4',
C4.5): 30 named checks, **30/30 PASS on seeds 2037, 7, 11**.
Second (light) fix pass after `agent/reports/critic-037-iter2-20260921T190000.md` completed
2026-09-21T20:00–20:30, no re-derivation: major 1 — the bijectivity/non-degeneracy "iff" of §1,
C1.0 and the proposed row restricted to the finite-dimensional model, with non-degeneracy identified
as the injectivity half of PH1 (R9) and the bounded inverse with closed range as its extra content
(R10); major 2 — §5's "linearised spectrum" replaced by what the truncated cohomology actually
controls (equations of motion and their linearisation; $H^0=\ker Q|_{\mathcal H_0^{(2)}}$ without the
quotient by $Q\mathcal H_0^{(1)}$). Minors: projected vs unprojected $\Sigma$-EOM shown equivalent
(§1); C5 derived for antifields at $N_{\rm gh}=4$ as well ($h(8)=3$ against $2$, §4) and restricted
to the two derived cases; the two exchange signs of the cyclicity argument written out (§3); the
model caveat restored in §5's paper sentence; "genuine strengthening" recalibrated in §5 and in the
row's scope caveat ((ii) is PH1 restated, (iii) is R8 plus cyclicity of $h$); the $Q$-kinetic escape
now cites the project's R30 instead of unnamed literature. Script: C4.5 made a real second method
(primitive of the transferred EOM against $S_{\rm eff}$ assembled from the raw $V_3,V_4$) with break
leg C4.5'; C1-unique relabelled C1-rank/unique and excluded from the count; the summary line prints
the counts. **31/31 report lines PASS on seeds 2037, 7, 11 — 30 distinct checks.**
**2026-09-22 — PH1 restated, propagated here** (brief
`computator-h1-restate-20260922T110500`; no re-derivation, no numerical change). H1 = PH1 no longer
reads "bounded inverse on $\mathrm{Sym}^2\mathcal H_0/\ker V_4$" and fixes no auxiliary inner
product: it reads "the inverse on the quotient exists level by level with a stable kernel
($\ker V_4^{(L)}=\ker V_4\cap\{\text{level}\le L\}$ for large $L$), so that the quotient, the
propagator and $h$ have a level limit; and no zero of the truncated determinant on the quotient
persists with the level at the momenta used". Reason: the BPZ form is indefinite and a
positive-definite Fock form is neither Lorentz- nor BRST-invariant, so quantitative statements made
in it are frame dependent; and nothing in this record uses continuity of $m_2^{-1}$. Edited
locations: A1-block hypothesis H1, C1.0, §1 ("Why the projector is needed" paragraph preceding it),
§1 Verification note, the proposed row R41, the *Not verified* list, and Self-review item 2. Added
in each place: a homological-perturbation statement in a **topological** sense (a contraction of
topological complexes with $h$ continuous in a stated topology) would need more than PH1 as
restated, and is not claimed. Script re-run: 31/31 report lines PASS on seeds 2037, 7, 11.

2026-09-22: wording fix D5 of `agent/reports/critic-h1-restate-20260922T120000.md` applied —
the A1-block H1 bullet no longer calls PH1 "automatic in the finite-dimensional model"; only
the level-uniform half is vacuous there, the injectivity half (non-degeneracy of $V_4$ on
$S^{(4)}$, C1.0) is a genuine condition tested by C1-rank. No algebra, no numerical change.

Next: critic iteration 3 / promotion of R41.
