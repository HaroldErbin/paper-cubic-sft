"""
Companion checks for derivation record 071 (circle map Phi_n, n = 2 tachyon pair).

What is verified (exact sympy arithmetic, random rational momenta, seed printed):

- C4.1-prefactor: the oscillator-algebra prefactor of
  e^{i k1 X(z1)} e^{i k2 X(z2)} |0>, obtained from the commutator
  [i k1.X_+(z1), i k2.X_-(z2)] and the zero modes, equals |z12|^{alpha' k1.k2}
  as a series in z2/z1 (holomorphic half, orders 1..8).
- C4.2-matter-L1, C4.2-matter-L2: the level-1 and level-2 holomorphic matter
  coefficients of Phi_2 from route A (exponential of creation operators, A1 of
  the record) agree with route B (Ward-identity contour integrals of dX
  insertions in the plane-wave correlator, book cft:eq:scalar-ope-dX-V), for
  z1 = z, z2 = -z. Includes the mixed (1,1) level.
- C4.2-ghost-generic, C4.2-ghost-pm: the expansion of c(z1) c(z2)|0> in modes
  from the mode algebra agrees with the bc three-point function
  <c(u1)c(u2)c(u3)> = (u1-u2)(u1-u3)(u2-u3) (holomorphic sector,
  <c_{-1}c_0c_1> = 1) for the c_0c_1, c_{-1}c_1, c_{-1}c_0 coefficients, for
  generic z1, z2 and for z, -z. C4.2-ghost-L2: the coefficients quoted in
  (B.7) against the mode algebra (transcription check only).
- C4.2-ghost-b-insertion: the c_{-2}c_1 coefficient (invisible to a three-c
  bra) from the mode algebra agrees with <0|c_{-1} c_0 b_2 c(z1) c(z2)|0>
  evaluated as nested contour integrals of the bc five-point function
  <b(v) c(u1)..c(u4)> = sum_i (-1)^(i-1)/(v-u_i) prod_{j<k, j,k!=i}(u_j-u_k)
  (simple poles from b(v)c(u) ~ 1/(v-u), O(v^-4) at infinity).
- C2.3-L10: the holomorphic level-(1,0) coefficient is sqrt(alpha'/2) z (k1-k2)
  (route B value); it does not vanish for k1 != k2.
- C2.3-sym-L20: at k1 = k2 (symmetric input, Delta = 0) the (1,0) coefficient
  vanishes (route B) but the (2,0) matter coefficient sqrt(alpha'/2) z^2 k
  (route B) and the (2,0) ghost coefficients C_{-2,1} = 2 z^3 (b-insertion
  route), C_{-1,0} = -2 z^3 (three-point route) are non-zero: level matching
  fails on symmetric inputs; the break leg drops the (2,0) terms and must FAIL.
- C2.1-rotation: under z -> lam z (|lam| = 1) the route-B level-(N, Nbar)
  coefficients scale as lam^(N - Nbar), record (A.6).
- C3-exchange: the route-B coefficients at (k2, k1) equal (-1)^(N - Nbar) times
  those at (k1, k2), record (A.8), through level 2 and the mixed (1,1) level.
  Scope: matter coefficients of the tachyon pair only (no ghost sector, no odd
  inputs); the ghost sign rests on the hand argument of the record.
- Break legs: each check is re-run with a deliberately perturbed expression and
  must FAIL.

Not verified: the general-n statements (C4.1 beyond the prefactor, C1-C3, C5),
the antiholomorphic sector (identical algebra with zbar), the convergence
statements, and anything about V_4 or the ledger's sewing results.

Conventions (record 071, A1): X = x - i (alpha'/2) p ln|u|^2
+ i sqrt(alpha'/2) sum_{m != 0} (1/m)(alpha_m u^{-m} + c.c.),
[alpha_m^mu, alpha_n^nu] = m delta^{mu nu} delta_{m+n},
dX(u) = -i sqrt(alpha'/2) sum_m alpha_m u^{-m-1},
dX(u) e^{ikX}(z) ~ -i (alpha'/2) k/(u-z) e^{ikX}(z).
"""

from __future__ import annotations

import random
import sys

import sympy as sp

SEED = 20261001
random.seed(SEED)
print(f"seed = {SEED}")

ap = sp.Symbol("alpha_p", positive=True)  # alpha'
s = sp.sqrt(ap / 2)
D = 3  # number of target components used (any D works; D=3 keeps it small)


def rand_rational() -> sp.Rational:
    """Random rational in [-9, 9] with denominator <= 5 (seeded)."""
    return sp.Rational(random.randint(-9, 9), random.randint(1, 5))


def rand_vec() -> list[sp.Rational]:
    """Random D-component rational momentum."""
    return [rand_rational() for _ in range(D)]


def dot(a: list, b: list) -> sp.Expr:
    """Euclidean dot product of two component lists."""
    return sum(x * y for x, y in zip(a, b, strict=True))


results: list[tuple[str, bool]] = []


def report(name: str, ok: bool, detail: str = "") -> None:
    """Record and print one PASS/FAIL line."""
    results.append((name, ok))
    print(f"{'PASS' if ok else 'FAIL'}  {name}  {detail}")


# ----------------------------------------------------------------------------
# C4.1-prefactor: commutator series vs |z12|^{alpha' k1.k2} (holomorphic half)
# ----------------------------------------------------------------------------
# [i k1.X_+(z1), i k2.X_-(z2)] = -k1.k2 [X_+(z1), X_-(z2)],
# [X_+(z1), X_-(z2)]_hol = (alpha'/2) sum_{m>=1} (1/m) (z2/z1)^m  (A1 modes).
# Zero modes give |z1|^{alpha' k1.k2}. Product should be |z1 - z2|^{alpha' k1.k2}.
x = sp.Symbol("x")  # x = z2/z1
kk = sp.Symbol("kk", real=True)  # k1.k2
NMAX = 8
comm_hol = (ap / 2) * sum(x**m / m for m in range(1, NMAX + 1))
# e^{A} e^{B} = e^{B} e^{A} e^{[A,B]}: factor exp(-kk * comm) multiplies |z1|^{ap kk}
route_a = sp.series(sp.exp(-kk * comm_hol), x, 0, NMAX + 1).removeO()
target = sp.series((1 - x) ** (ap * kk / 2), x, 0, NMAX + 1).removeO()
diff = sp.simplify(sp.expand(route_a - target))
report("C4.1-prefactor", diff == 0, f"series diff through x^{NMAX}: {diff}")
# break leg: wrong exponent sign
wrong = sp.series((1 - x) ** (-ap * kk / 2), x, 0, NMAX + 1).removeO()
report(
    "C4.1-prefactor-break",
    sp.simplify(sp.expand(route_a - wrong)) != 0,
    "(must FAIL-detect)",
)

# ----------------------------------------------------------------------------
# Route A: oscillator expansion of exp(sum_n (s/n) sum_i k_i.alpha_{-n} z_i^n)
# through level 2 (holomorphic), plus the (1,1) mixed level.
# Coefficients are taken on the orthogonal monomial basis
#   level 1: alpha_{-1}^mu,  level 2: alpha_{-2}^mu, alpha_{-1}^mu alpha_{-1}^nu.
# ----------------------------------------------------------------------------
z = sp.Symbol("z")
zb = sp.Symbol("zb")  # zbar, treated as an independent symbol
k1, k2 = rand_vec(), rand_vec()
if k1 == k2:
    k2 = [c + 1 for c in k2]
pos = {1: z, 2: -z}
posb = {1: zb, 2: -zb}
ks = {1: k1, 2: k2}


def route_a_lin(n: int, mu: int, hol: bool = True) -> sp.Expr:
    """Coefficient of alpha_{-n}^mu (or bar) in the exponent (linear term)."""
    p = pos if hol else posb
    return sp.expand(s / n * sum(ks[i][mu] * p[i] ** n for i in (1, 2)))


def route_a_quad11(mu: int, nu: int) -> sp.Expr:
    """Coefficient of alpha_{-1}^mu alpha_{-1}^nu (mu<nu) or 1/2 (alpha_{-1}^mu)^2."""
    a, b = route_a_lin(1, mu), route_a_lin(1, nu)
    return sp.expand(a * b) if mu != nu else sp.expand(a * b / 2)


def route_a_mixed(mu: int, nu: int) -> sp.Expr:
    """Coefficient of alpha_{-1}^mu bar-alpha_{-1}^nu (holomorphic x anti)."""
    return sp.expand(route_a_lin(1, mu) * route_a_lin(1, nu, hol=False))


# ----------------------------------------------------------------------------
# Route B: Ward-identity contour integrals.
# <P| alpha_n^mu |Phi> = i sqrt(2/ap) oint_{|u|>|z|} du/(2 pi i) u^n <P| dX^mu(u) ... |0>
# with <dX^mu(u) prod e^{ikX}> = -i (ap/2) sum_i k_i^mu/(u - z_i) <prod e^{ikX}>.
# Two insertions: product of single-insertion factors + contraction
#   -(ap/2) eta^{mu nu}/(u-v)^2, contours |u|>|v|>|z|.
# Mode normalisation: <P|alpha_n^mu alpha_{-n}^nu|P> = n eta^{mu nu}.
# ----------------------------------------------------------------------------
u, v = sp.symbols("u v")


def outer_residue(expr: sp.Expr, var: sp.Symbol, poles: list) -> sp.Expr:
    """oint_{|var| > all poles} d var/(2 pi i) expr = sum of residues at the poles."""
    return sp.simplify(sum(sp.residue(expr, var, p0) for p0 in poles))


def ward_single(mu: int, var: sp.Symbol, kd: dict | None = None) -> sp.Expr:
    """Ward factor of one dX^mu(var) insertion: -i (ap/2) sum_i k_i^mu/(var - z_i)."""
    kd = ks if kd is None else kd
    return -sp.I * (ap / 2) * sum(kd[i][mu] / (var - pos[i]) for i in (1, 2))


def route_b_lin(n: int, mu: int, kd: dict | None = None) -> sp.Expr:
    """Coefficient of alpha_{-n}^mu in Phi_2 from <P|alpha_n^mu|Phi_2>/n (route B)."""
    integrand = sp.I * sp.sqrt(2 / ap) * u**n * ward_single(mu, u, kd)
    val = outer_residue(integrand, u, [z, -z])
    return sp.expand(sp.simplify(val / n))  # divide by <alpha_n alpha_{-n}> = n


def route_b_quad11(mu: int, nu: int, kd: dict | None = None) -> sp.Expr:
    """<P|alpha_1^mu alpha_1^nu|Phi> via two dX insertions, |u|>|v|>|z|."""
    pref = (sp.I * sp.sqrt(2 / ap)) ** 2
    integrand = (
        u
        * v
        * (
            ward_single(mu, u, kd) * ward_single(nu, v, kd)
            - (ap / 2) * (1 if mu == nu else 0) / (u - v) ** 2
        )
    )
    inner = sp.simplify(
        sum(sp.residue(integrand, u, p0) for p0 in [z, -z, v])
    )  # |u|>|v|: u encloses v too
    val = pref * outer_residue(inner, v, [z, -z])
    # <P| a_1^mu a_1^nu (C a_{-1}^mu a_{-1}^nu)|P> = C (1 + delta^{mu nu}) for mu != nu basis
    # coefficient C of the ordered monomial: for mu != nu the bra picks C exactly;
    # for mu == nu, state carries C (a_{-1}^mu)^2 with <a_1 a_1 a_{-1} a_{-1}> = 2.
    return sp.expand(sp.simplify(val / (1 if mu != nu else 2)))


# level 1 (holomorphic)
ok = True
details = []
for mu in range(D):
    a, b = route_a_lin(1, mu), route_b_lin(1, mu)
    ok &= sp.simplify(a - b) == 0
    details.append(str(sp.simplify(a - b)))
report("C4.2-matter-L1", ok, f"diffs {details}")
# break leg: flip the Ward sign
bad = sp.expand(-route_b_lin(1, 0))
report(
    "C4.2-matter-L1-break",
    sp.simplify(route_a_lin(1, 0) - bad) != 0,
    "(must FAIL-detect)",
)

# level 2: alpha_{-2} and alpha_{-1}alpha_{-1}
ok = True
details = []
for mu in range(D):
    a, b = route_a_lin(2, mu), route_b_lin(2, mu)
    ok &= sp.simplify(a - b) == 0
    details.append(str(sp.simplify(a - b)))
for mu in range(D):
    for nu in range(mu, D):
        a, b = route_a_quad11(mu, nu), route_b_quad11(mu, nu)
        ok &= sp.simplify(a - b) == 0
        details.append(str(sp.simplify(a - b)))
report("C4.2-matter-L2", ok, f"diffs {details}")
# break leg: drop the 1/2 on the diagonal quadratic term
bad = sp.expand(route_a_lin(1, 0) ** 2)
report(
    "C4.2-matter-L2-break",
    sp.simplify(bad - route_b_quad11(0, 0)) != 0,
    "(must FAIL-detect)",
)

# mixed (1,1) level: route B with one dX and one dXbar insertion factorises
# (no contraction between dX and dXbar); check against route A product
ok = True
for mu in range(D):
    for nu in range(D):
        b = sp.expand(route_b_lin(1, mu) * route_b_lin(1, nu).subs(z, zb))
        ok &= sp.simplify(route_a_mixed(mu, nu) - b) == 0
report("C4.2-matter-L11", ok, "mixed (1,1) level")

# C2.3-L10: the (1,0) coefficient is s z (k1 - k2); nonzero for k1 != k2
c10 = [route_b_lin(1, mu) for mu in range(D)]
expected = [sp.expand(s * z * (k1[mu] - k2[mu])) for mu in range(D)]
ok = all(sp.simplify(a - b) == 0 for a, b in zip(c10, expected, strict=True)) and any(
    e != 0 for e in expected
)
report(
    "C2.3-L10",
    ok,
    f"(1,0) coefficient = s z (k1-k2), nonzero: {[sp.simplify(e / (s * z)) for e in expected]}",
)

# C2.1-rotation: z -> lam z, zb -> zb/lam (|lam| = 1): level (N, Nbar) picks lam^(N - Nbar)
lam = sp.Symbol("lam", nonzero=True)
ok = True
for n in (1, 2):
    for mu in range(D):
        ok &= (
            sp.simplify(
                route_b_lin(n, mu).subs(z, lam * z) - lam**n * route_b_lin(n, mu)
            )
            == 0
        )
for mu in range(D):
    for nu in range(mu, D):
        ok &= (
            sp.simplify(
                route_b_quad11(mu, nu).subs(z, lam * z)
                - lam**2 * route_b_quad11(mu, nu)
            )
            == 0
        )
        mixed = route_b_lin(1, mu) * route_b_lin(1, nu).subs(z, zb)
        ok &= (
            sp.simplify(
                mixed.subs({z: lam * z, zb: zb / lam}, simultaneous=True) - mixed
            )
            == 0
        )
report(
    "C2.1-rotation",
    ok,
    "levels (1,0), (2,0), (1,1): lam^(N-Nbar) on the route-B coefficients",
)
bad = sp.simplify(route_b_lin(2, 0).subs(z, lam * z) - lam * route_b_lin(2, 0)) == 0
report(
    "C2.1-rotation-break", not bad, "(must FAIL-detect: wrong phase lam^1 on level 2)"
)

# C3-exchange: (k2, k1) vs (k1, k2): (-1)^(N - Nbar) level by level (route B residues)
ks_sw = {1: k2, 2: k1}
ok = True
for mu in range(D):
    ok &= (
        sp.simplify(route_b_lin(1, mu, ks_sw) + route_b_lin(1, mu)) == 0
    )  # (1,0): sign flip
    ok &= (
        sp.simplify(route_b_lin(2, mu, ks_sw) - route_b_lin(2, mu)) == 0
    )  # (2,0): even
    for nu in range(mu, D):
        ok &= (
            sp.simplify(route_b_quad11(mu, nu, ks_sw) - route_b_quad11(mu, nu)) == 0
        )  # (2,0): even
        m_sw = route_b_lin(1, mu, ks_sw) * route_b_lin(1, nu, ks_sw).subs(z, zb)
        m0 = route_b_lin(1, mu) * route_b_lin(1, nu).subs(z, zb)
        ok &= sp.simplify(m_sw - m0) == 0  # (1,1): even
report(
    "C3-exchange",
    ok,
    "Phi_2(A2,A1) = (-1)^{L_0^-} Phi_2(A1,A2) through level 2 + mixed (1,1)",
)
bad = all(
    sp.simplify(route_b_lin(1, mu, ks_sw) - route_b_lin(1, mu)) == 0 for mu in range(D)
)
report(
    "C3-exchange-break", not bad, "(must FAIL-detect: exchange = +1 on the (1,0) level)"
)

# ----------------------------------------------------------------------------
# Ghosts: c(z1) c(z2)|0> by the mode algebra vs the bc three-point function.
# c(u) = sum_n c_n u^{-n+1}; c_n|0> = 0 for n >= 2; <c_{-1} c_0 c_1> = 1 (hol.).
# ----------------------------------------------------------------------------
z1, z2 = sp.symbols("z1 z2")


def mode_product(
    za: sp.Expr, zbb: sp.Expr, nmax: int
) -> dict[tuple[int, int], sp.Expr]:
    """
    Expansion of c(za) c(zbb)|0> as {(m, n): coeff} with m < n <= 1 (c_m c_n|0>), levels <= nmax.

    Level of c_m c_n|0> is -(m + n) relative to |0>; keep -(m+n) <= nmax + ... we
    simply keep all pairs with m, n >= -nmax - 1.
    """
    out: dict[tuple[int, int], sp.Expr] = {}
    rng = range(-nmax - 2, 2)
    for m in rng:
        for n in rng:
            if m == n:
                continue
            coeff = za ** (-m + 1) * zbb ** (-n + 1)
            key, sign = ((m, n), 1) if m < n else ((n, m), -1)
            out[key] = sp.expand(out.get(key, 0) + sign * coeff)
    return out


def three_point_coeff(a: int, za: sp.Expr, zbb: sp.Expr) -> sp.Expr:
    """
    <0| c_a c(za) c(zbb) |0> from <c(u)c(za)c(zbb)> = (u-za)(u-zbb)(za-zbb).

    c_a = oint du/(2 pi i) u^{a-2} c(u) on |u| > |za|,|zbb|: the coefficient of u^{1-a}.
    """
    poly = sp.Poly(sp.expand((u - za) * (u - zbb) * (za - zbb)), u)
    return poly.coeff_monomial(u ** (1 - a)) if 1 - a >= 0 else sp.Integer(0)


def bra_on_modes(a: int, state: dict[tuple[int, int], sp.Expr]) -> sp.Expr:
    """<0| c_a sum C_{mn} c_m c_n |0> using <c_{-1}c_0c_1> = 1 and antisymmetry."""
    total = sp.Integer(0)
    for (m, n), coeff in state.items():
        trip = (a, m, n)
        if sorted(trip) != [-1, 0, 1]:
            continue
        # sign of the permutation taking (a, m, n) to (-1, 0, 1)
        perm = [(-1, 0, 1).index(t) for t in trip]
        sign = sp.combinatorics.Permutation(perm).signature()
        total += sign * coeff
    return sp.expand(total)


def check_ghost(za: sp.Expr, zbb: sp.Expr, label: str) -> None:
    """Compare mode algebra and three-point function for the bras c_{-1}, c_0, c_1."""
    st = mode_product(za, zbb, 2)
    ok = True
    details = []
    for a in (
        -1,
        0,
        1,
    ):  # bras reaching levels 1, 2 (c_{-1}: C_{01}; c_0: C_{-1,1}; c_1: C_{-1,0})
        lhs = bra_on_modes(a, st)
        rhs = three_point_coeff(a, za, zbb)
        d = sp.simplify(lhs - rhs)
        ok &= d == 0
        details.append(f"a={a}: {sp.factor(lhs)} vs {sp.factor(rhs)}")
    report(label, ok, "; ".join(details))


check_ghost(z1, z2, "C4.2-ghost-generic")
check_ghost(z, -z, "C4.2-ghost-pm")
# explicit coefficients quoted in the record for z, -z:
st = mode_product(z, -z, 2)
quoted = {(0, 1): 2 * z, (-1, 1): 0, (-2, 1): 2 * z**3, (-1, 0): -2 * z**3}
ok = all(sp.simplify(st.get(key, 0) - val) == 0 for key, val in quoted.items())
report(
    "C4.2-ghost-L2",
    ok,
    f"C01={st.get((0, 1))}, C-11={st.get((-1, 1))}, C-21={st.get((-2, 1))}, C-10={st.get((-1, 0))}",
)
# break leg: wrong relative sign between c_{-2}c_1 and c_{-1}c_0
bad = dict(st)
bad[(-1, 0)] = -bad[(-1, 0)]
report(
    "C4.2-ghost-L2-break",
    sp.simplify(bra_on_modes(1, bad) - three_point_coeff(1, z, -z)) != 0,
    "(must FAIL-detect)",
)


# ----------------------------------------------------------------------------
# C4.2-ghost-b-insertion: the c_{-2}c_1 coefficient via <0|c_{-1} c_0 b_2 c(z1)c(z2)|0>
# from the bc five-point function (independent of the mode algebra).
# b_2 c_m c_n|0> = delta_{m,-2} c_n - delta_{n,-2} c_m; with the bra <0|c_{-1}c_0
# only c_{-2}c_1|0> survives: the pairing equals C_{-2,1}.
# Contours: c_a = oint du u^{a-2} c(u), b_2 = oint dv v^3 b(v), |u1|>|u2|>|v|>|z|.
# ----------------------------------------------------------------------------
u1, u2 = sp.symbols("u1 u2")


def five_point(vv: sp.Symbol, us: list) -> sp.Expr:
    """<b(v) c(u_1) c(u_2) c(u_3) c(u_4)>: simple poles with Vandermonde residues."""
    tot = sp.Integer(0)
    for i, ui in enumerate(us):
        rest = [uj for uj in us if uj is not ui]
        vand = sp.prod([rest[j] - rest[k] for j in range(3) for k in range(j + 1, 3)])
        tot += (-1) ** i * vand / (vv - ui)
    return tot


def b_insertion_coeff(za: sp.Expr, zbb: sp.Expr) -> sp.Expr:
    """<0| c_{-1} c_0 b_2 c(za) c(zbb) |0> by nested contour integrals."""
    # <c(u1)c(u2)b(v)c(za)c(zbb)> = <b(v)c(u1)c(u2)c(za)c(zbb)> (b past two c's)
    f = five_point(v, [u1, u2, za, zbb])
    g = sum(sp.residue(v**3 * f, v, p0) for p0 in (za, zbb))  # poles inside |v| < |u_i|
    g = sp.expand(sp.simplify(g))
    g2 = sp.Poly(g, u2).coeff_monomial(u2**1)  # oint u2^{-2}: coefficient of u2^1
    return sp.expand(sp.Poly(sp.expand(g2), u1).coeff_monomial(u1**2))  # oint u1^{-3}


ok = True
details = []
for za, zbb, lab in ((z1, z2, "generic"), (z, -z, "pm")):
    lhs = mode_product(za, zbb, 2).get((-2, 1), 0)
    rhs = b_insertion_coeff(za, zbb)
    d = sp.simplify(lhs - rhs)
    ok &= d == 0
    details.append(f"{lab}: modes {sp.factor(lhs)} vs b-insertion {sp.factor(rhs)}")
report("C4.2-ghost-b-insertion", ok, "; ".join(details))
bad = sp.simplify(sp.expand(z1**3 + z2**3) - b_insertion_coeff(z1, z2)) == 0
report(
    "C4.2-ghost-b-insertion-break",
    not bad,
    "(must FAIL-detect: wrong relative sign z1^3 + z2^3)",
)

# ----------------------------------------------------------------------------
# C2.3-sym-L20: level matching fails on symmetric inputs (k1 = k2, Delta = 0):
# (1,0) vanishes but the (2,0) matter and ghost coefficients do not.
# ----------------------------------------------------------------------------
ks_same = {1: k1, 2: k1}
l10_same = [route_b_lin(1, mu, ks_same) for mu in range(D)]
l20_same = [route_b_lin(2, mu, ks_same) for mu in range(D)]
l20_route_a = [
    sp.expand(s / 2 * sum(ks_same[i][mu] * pos[i] ** 2 for i in (1, 2)))
    for mu in range(D)
]
ghost_pm = mode_product(z, -z, 2)
g21, g10 = ghost_pm.get((-2, 1), 0), ghost_pm.get((-1, 0), 0)
ok = all(sp.simplify(c) == 0 for c in l10_same)  # (1,0) cancels at Delta = 0
ok &= all(sp.simplify(a - b) == 0 for a, b in zip(l20_route_a, l20_same, strict=True))
ok &= any(sp.simplify(c) != 0 for c in l20_same)  # matter (2,0) non-zero (P != 0)
ok &= sp.simplify(g21 - b_insertion_coeff(z, -z)) == 0 and sp.simplify(g21) != 0
ok &= (
    sp.simplify(bra_on_modes(1, ghost_pm) - three_point_coeff(1, z, -z)) == 0
    and sp.simplify(g10) != 0
)
report(
    "C2.3-sym-L20",
    ok,
    f"(1,0) at k1=k2: {[sp.simplify(c) for c in l10_same]}; (2,0) matter: {[sp.factor(c) for c in l20_same]}; ghost C-21={g21}, C-10={g10}",
)
# break leg: the withdrawn claim "level-matched through level 2 on symmetric inputs":
# drop the (2,0) terms (route A matter coefficient and ghost C_{-2,1}, C_{-1,0} set to 0)
# and compare with the independent routes; the comparison must detect the mismatch.
dropped_matter = [sp.Integer(0)] * D
dropped_ghost = dict(ghost_pm)
dropped_ghost[(-2, 1)] = sp.Integer(0)
dropped_ghost[(-1, 0)] = sp.Integer(0)
agree = all(
    sp.simplify(a - b) == 0 for a, b in zip(dropped_matter, l20_same, strict=True)
)
agree &= sp.simplify(dropped_ghost[(-2, 1)] - b_insertion_coeff(z, -z)) == 0
agree &= sp.simplify(bra_on_modes(1, dropped_ghost) - three_point_coeff(1, z, -z)) == 0
report("C2.3-sym-L20-break", not agree, "(must FAIL-detect: (2,0) terms dropped)")

# ----------------------------------------------------------------------------
n_pass = sum(1 for _, ok in results if ok)
print(f"\n{n_pass}/{len(results)} checks PASS (seed {SEED})")
sys.exit(0 if n_pass == len(results) else 1)
