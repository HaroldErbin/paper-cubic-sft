"""Verification: exact off-shell gauge invariance of the HS action (candidate R11).

Claim (Fable session 2026-07-01, knowledge/fable-2026-07-01-assessment-and-results.md):
with the COMPOSITE transformation

    delta Sigma = delta Psi (x) Psi + Psi (x) delta Psi        (infinitesimal)
    Sigma'      = Sigma + Psi' (x) Psi' - Psi (x) Psi          (finite)

the Sigma-dependent part of the HS action,

    D(Sigma, Psi) = S_HS - S_eff = -(g^2/4!) V4(X, X),   X = Sigma - Psi^{(x)2},

is EXACTLY invariant (off-shell, no EOM used), so delta S_HS = delta S_eff for ANY
delta Psi.  Hence S_HS inherits the full gauge symmetry of the quartic-truncated
action, with delta Psi the standard L_infty transformation and delta Sigma composite.

Toy model: H = R^n (n=2), H^{(x)2} = R^{n^2}; V4 = symmetric bilinear form M on
H^{(x)2} (this uses only the pair-exchange part of hypothesis H2, i.e. bilinear
symmetry M = M^T).  Fields are commuting symbols (physical N_gh even sector).

Checks:
 (1) completion of the square:  -Sig.M.Sig + 2 Sig.M.PP = -X.M.X + PP.M.PP  (R1 identity)
 (2) infinitesimal invariance:  O(eps) term of D under the composite law vanishes
     identically for symbolic OFF-SHELL Sigma (falsifiable: fails if source coeff != 2)
 (3) finite invariance:         D(Sigma', Psi') - D(Sigma, Psi) == 0 exactly
 (4) falsifiability:            with source coefficient c = 1 (instead of 2) the
     O(eps) variation does NOT vanish
 (5) kernel shift symmetry:     if M has a null vector xi (Sym^2 kernel), then
     Sigma -> Sigma + t xi leaves D invariant AND xi drops out of the Sigma-EOM
     (the decoupling that defuses residual (5.1))
"""

import sympy as sp

n = 2
N = n * n
g, eps, t, c = sp.symbols("g eps t c")

Psi = sp.Matrix(sp.symbols(f"p0:{n}"))
dPsi = sp.Matrix(sp.symbols(f"d0:{n}"))
Sig = sp.Matrix(sp.symbols(f"s0:{N}"))


def kron(a, b):
    return sp.Matrix([a[i] * b[j] for i in range(n) for j in range(n)])


# generic SYMMETRIC bilinear form on H^{(x)2}  (pair-exchange part of H2 only)
Msym = sp.Matrix(N, N, lambda i, j: sp.Symbol(f"m{min(i,j)}{max(i,j)}"))


def D(S, P, M, coeff=2):
    PP = kron(P, P)
    return (g**2 / 24) * ((-(S.T * M * S)) + coeff * (S.T * M * PP))[0]


def Deff(P, M):
    PP = kron(P, P)
    return (g**2 / 24) * (PP.T * M * PP)[0]


npass = 0
nfail = 0


def check(label, ok):
    global npass, nfail
    print(f"({label})  {'PASS' if ok else 'FAIL'}")
    npass += ok
    nfail += not ok


# (1) completion of the square
PP = kron(Psi, Psi)
X = Sig - PP
lhs = (-(Sig.T * Msym * Sig) + 2 * (Sig.T * Msym * PP))[0]
rhs = (-(X.T * Msym * X) + (PP.T * Msym * PP))[0]
check("1 completion of square", sp.expand(lhs - rhs) == 0)

# (2) infinitesimal invariance, OFF-SHELL symbolic Sigma
Psi2 = Psi + eps * dPsi
dSig = kron(dPsi, Psi) + kron(Psi, dPsi)
Sig2 = Sig + eps * dSig
Dfull = D(Sig2, Psi2, Msym) - Deff(Psi2, Msym) - (D(Sig, Psi, Msym) - Deff(Psi, Msym))
order1 = sp.expand(sp.diff(Dfull, eps).subs(eps, 0))
check("2 infinitesimal delta(S_HS - S_eff) = 0 off-shell", order1 == 0)

# (3) finite invariance with the finite composite law
SigF = Sig + kron(Psi2, Psi2).subs(eps, 1) - kron(Psi, Psi)
PsiF = (Psi + dPsi)
diff_fin = D(SigF, PsiF, Msym) - Deff(PsiF, Msym) - (D(Sig, Psi, Msym) - Deff(Psi, Msym))
check("3 finite invariance, exact", sp.expand(diff_fin) == 0)

# (4) falsifiability: source coefficient 1 instead of 2 breaks it
Dbad = D(Sig2, Psi2, Msym, coeff=1) - (D(Sig, Psi, Msym, coeff=1))
order1_bad = sp.expand(sp.diff(Dbad, eps).subs(eps, 0))
# subtract the c=1 'effective' piece consistently: with coeff 1 there is no clean
# completion of the square; the direct statement is that the O(eps) variation with the
# composite law does not reduce to a pure-Psi variation:
resid = sp.expand(order1_bad - sp.diff(Deff(Psi2, Msym) - Deff(Psi, Msym), eps).subs(eps, 0))
check("4 coeff 2 -> 1 destroys invariance (nonzero residual)", resid != 0)

# (5) kernel shift symmetry + EOM decoupling with a degenerate M
#     build M with null vector xi: M = v v^T + w w^T with xi orthogonal to v, w
v = sp.Matrix([1, 0, 0, 1])
w = sp.Matrix([0, 1, 1, 0])
xi = sp.Matrix([1, 0, 0, -1])  # M xi = 0; xi in Sym^2 (symmetric under swap)
Mdeg = v * v.T + w * w.T
assert (Mdeg * xi) == sp.zeros(N, 1)
shift_diff = D(Sig + t * xi, Psi, Mdeg) - D(Sig, Psi, Mdeg)
eom = sp.Matrix([sp.diff(D(Sig, Psi, Mdeg), s) for s in Sig])  # gradient wrt Sigma
eom_shifted = sp.Matrix([sp.diff(D(Sig + t * xi, Psi, Mdeg), s) for s in Sig])
ok5 = sp.expand(shift_diff) == 0 and sp.simplify(eom_shifted - eom) == sp.zeros(N, 1)
check("5 kernel direction: zero-action shift symmetry, absent from EOM", ok5)

print("=" * 60)
print(f"{npass}/{npass + nfail} PASS")
if nfail:
    raise SystemExit(1)
