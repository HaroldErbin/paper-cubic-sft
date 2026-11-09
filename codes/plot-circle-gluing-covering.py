"""Figure for record 074 (R80 C1.2-C1.3): circle-gluing covering of V_{0,4}.

Plumbing region Q_V of the s-circle gluing of two rigid V_3' halves, mapped once onto V_{0,4}.

Geometry copied (not imported) from codes/verify-circle-gluing-inverse.py,
beta = 3/2: Z_4^{(s)}(q) = (q + 4 beta^2)^2 / (16 beta^2 q), membership of
V_{0,4} = min(|q_t|, |q_u|) > 1 (and |q_s| > 1), ray marching for sigma_V(theta).

Output: results/figures/circle-gluing-covering.{svg,pdf}.
Run: .venv/bin/python codes/plot-circle-gluing-covering.py
"""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

BETA = 1.5
B2 = BETA**2
LN_COLL = np.log(4 * B2)  # collision (fold) circle |q| = 4 beta^2

OUT = Path(__file__).resolve().parent / "output" / "figures"


# ---------------------------------------------------------------------------
# Geometry (copied from verify-circle-gluing-inverse.py)
# ---------------------------------------------------------------------------
def z_of_q(q):
    """s-channel puncture location, R2: Z = (q + 4 beta^2)^2 / (16 beta^2 q)."""
    return (q + 4 * B2) ** 2 / (16 * B2 * q)


def q_of_zs(zs):
    """Root of q^2 + (8 b^2 - 16 b^2 zs) q + 16 b^4 = 0 with |q| < 4 b^2 (032 (3.1))."""
    b = 8 * B2 - 16 * B2 * zs
    disc = np.sqrt(b * b - 4 * 16 * B2**2 + 0j)
    r1 = (-b + disc) / 2
    r2 = (-b - disc) / 2
    return np.where(np.abs(r1) < np.abs(r2), r1, r2)


def min_tu(z):
    """min(|q_t|, |q_u|) with the closures of 032 (3.1)."""
    qt = q_of_zs(z / (z - 1))
    qu = q_of_zs(1 - 1 / z)
    return np.minimum(np.abs(qt), np.abs(qu))


def region_labels(z):
    """0 = V_{0,4}; 1, 2, 3 = F_s, F_t, F_u (|q_x| <= 1)."""
    qs = np.abs(q_of_zs(z))
    qt = np.abs(q_of_zs(z / (z - 1)))
    qu = np.abs(q_of_zs(1 - 1 / z))
    lab = np.zeros(z.shape, dtype=int)
    lab[qu <= 1] = 3
    lab[qt <= 1] = 2
    lab[qs <= 1] = 1
    return lab


# ---------------------------------------------------------------------------
# Ray marching: sigma_V(theta), refined by bisection
# ---------------------------------------------------------------------------
n_theta, n_sigma = 1440, 6000
thetas = np.linspace(0, 2 * np.pi, n_theta, endpoint=False)
sigmas = np.linspace(1e-4, LN_COLL - 1e-4, n_sigma)
TH, SG = np.meshgrid(thetas, sigmas, indexing="ij")
inside = min_tu(z_of_q(np.exp(SG + 1j * TH))) > 1.0
prefix_len = np.argmin(inside, axis=1)
prefix_len = np.where(inside.all(axis=1), n_sigma, prefix_len)
at_cap = prefix_len == n_sigma
assert not np.array([inside[i, prefix_len[i] :].any() for i in range(n_theta)]).any(), (
    "re-entry: Q_V not star-shaped"
)

lo = sigmas[np.clip(prefix_len - 1, 0, n_sigma - 1)]
hi = sigmas[np.clip(prefix_len, 0, n_sigma - 1)]
for _ in range(40):
    mid = 0.5 * (lo + hi)
    ok = min_tu(z_of_q(np.exp(mid + 1j * thetas))) > 1.0
    lo = np.where(ok, mid, lo)
    hi = np.where(ok, hi, mid)
sigma_V = np.where(at_cap, LN_COLL, 0.5 * (lo + hi))


def sigma_of_theta(th):
    """sigma_V at arbitrary theta, linear interpolation of the ray data (2 pi-periodic)."""
    return np.interp(
        np.mod(th, 2 * np.pi),
        np.append(thetas, 2 * np.pi),
        np.append(sigma_V, sigma_V[0]),
    )


# Fold-arc endpoints: Z(4 b^2 e^{i th}) lies in V_{0,4} iff the point just inside
# the fold circle passes the criterion; scan a fine theta grid on [0, pi].
th_f = np.linspace(0, np.pi, 400001)
ok_f = min_tu(z_of_q(np.exp((LN_COLL - 1e-6) + 1j * th_f))) > 1.0
idx = np.flatnonzero(ok_f)
th1_num, th2_num = th_f[idx[0]], th_f[idx[-1]]
cos_th1_num, cos_th2_num = np.cos(th1_num), np.cos(th2_num)
sig_pi = float(sigma_V[n_theta // 2])

print(f"sigma_V(pi) = {sig_pi:.6f}   ln(9/4) = {np.log(9 / 4):.6f}")
print(
    f"fold arc (upper half-plane): theta in [{np.degrees(th1_num):.4f}, "
    f"{np.degrees(th2_num):.4f}] deg;  cos theta_1 = {cos_th1_num:.5f}, "
    f"cos theta_2 = {cos_th2_num:.5f};  7/25 = {7 / 25:.5f}"
)
print(f"max sigma_V = {sigma_V.max():.6f}   ln(4 beta^2) = {LN_COLL:.6f}")
assert abs(sig_pi - np.log(9 / 4)) < 1e-6
assert abs(cos_th1_num - 7 / 25) < 1e-4 and abs(cos_th2_num + 7 / 25) < 1e-4

# ---------------------------------------------------------------------------
# Figure
# ---------------------------------------------------------------------------
# Okabe-Ito colour-blind-safe palette
C_BLUE, C_ORANGE, C_GREEN, C_VERM = "#0072B2", "#E69F00", "#009E73", "#D55E00"
C_SKY, C_PINK, C_YEL = "#56B4E9", "#CC79A7", "#F0E442"

plt.rcParams.update({"font.size": 10, "mathtext.fontset": "cm"})
fig, (axL, axR) = plt.subplots(1, 2, figsize=(11.5, 5.4), constrained_layout=True)

# ----- left: q-plane
R = 4 * B2 * 1.08
th_fill = np.linspace(0, 2 * np.pi, 2001)
sV_fill = sigma_of_theta(th_fill)
xo, yo = np.exp(sV_fill) * np.cos(th_fill), np.exp(sV_fill) * np.sin(th_fill)
xi, yi = np.cos(th_fill), np.sin(th_fill)
axL.fill(
    np.concatenate([xo, xi[::-1]]),
    np.concatenate([yo, yi[::-1]]),
    color=C_SKY,
    alpha=0.45,
    lw=0,
    zorder=1,
)
axL.add_patch(plt.Circle((0, 0), 1, fc="#dddddd", ec="none", zorder=1))
axL.plot(xi, yi, color="k", lw=1.2, zorder=4)
axL.plot(xo, yo, color=C_BLUE, lw=1.6, zorder=4)
axL.plot(
    4 * B2 * np.cos(th_fill),
    4 * B2 * np.sin(th_fill),
    color="k",
    lw=1.0,
    ls=(0, (5, 3)),
    zorder=3,
)
# fold arcs: cos(theta) in (-7/25, 7/25), i.e. theta in (th1, th2) and (-th2, -th1)
fold_pieces = [(th1_num, th2_num), (-th2_num, -th1_num)]
for a, b in fold_pieces:
    t = np.linspace(a, b, 200)
    axL.plot(
        4 * B2 * np.cos(t),
        4 * B2 * np.sin(t),
        color=C_VERM,
        lw=4.5,
        zorder=6,
        solid_capstyle="butt",
    )
for th0, lab in [(0.0, r"$\theta=0$"), (np.pi, r"$\theta=\pi$")]:
    s0 = float(sigma_of_theta(th0))
    x0 = np.exp(s0) * np.cos(th0)
    axL.plot(x0, 0, "o", ms=7, mfc=C_ORANGE, mec="k", zorder=7)
    axL.annotate(
        lab + r", $\sigma_V=\ln\frac{9}{4}$",
        (x0, 0),
        xytext=(x0 + (0.5 if th0 == 0 else -0.5), -2.0 if th0 == 0 else -2.0),
        ha="left" if th0 == 0 else "right",
        fontsize=9,
        arrowprops=dict(arrowstyle="-", lw=0.6),
    )
axL.set_xlim(-R, R)
axL.set_ylim(-R, R)
axL.set_aspect("equal")
axL.set_xlabel(r"$\mathrm{Re}\,q$")
axL.set_ylabel(r"$\mathrm{Im}\,q$")
axL.set_title(r"$q$-plane: plumbing region $Q_V$", fontsize=11)
axL.legend(
    handles=[
        Patch(fc=C_SKY, alpha=0.6, label=r"$Q_V=\{1<|q|<e^{\sigma_V(\theta)}\}$"),
        Line2D([], [], color="k", lw=1.2, label=r"$|q|=1$"),
        Line2D([], [], color=C_BLUE, lw=1.6, label=r"$|q|=e^{\sigma_V(\theta)}$"),
        Line2D([], [], color="k", lw=1, ls=(0, (5, 3)), label=r"$|q|=4\beta^2$"),
        Line2D(
            [], [], color=C_VERM, lw=4.5, label=r"fold arcs ($\sigma_V=\ln 4\beta^2$)"
        ),
    ],
    loc="upper right",
    fontsize=8,
    framealpha=0.95,
)

# ----- right: Z-plane
x0_, x1_, y0_, y1_ = -2.1, 3.1, -2.6, 2.6
nx, ny = 1500, 1500
xs = np.linspace(x0_, x1_, nx)
ys = np.linspace(y0_, y1_, ny)
XX, YY = np.meshgrid(xs, ys)
with np.errstate(divide="ignore", invalid="ignore"):
    labs = region_labels(XX + 1j * YY)
cm = ListedColormap(["#f2f2f2", "#cfe3f1", "#f8dfb0", "#cfe9de"])
axR.imshow(
    labs,
    extent=(x0_, x1_, y0_, y1_),
    origin="lower",
    cmap=cm,
    vmin=0,
    vmax=3,
    interpolation="nearest",
    zorder=1,
)
axR.contour(
    XX, YY, labs, levels=[0.5, 1.5, 2.5], colors="#555555", linewidths=0.7, zorder=2
)

# image of Q_V: points q = exp(sigma + i theta), sigma = u * sigma_V(theta), u in (0,1)
n_th_img, n_u = 1440, 260
th_img = (np.arange(n_th_img) + 0.5) * 2 * np.pi / n_th_img
u = (np.arange(n_u) + 0.5) / n_u
sg_img = u[None, :] * sigma_of_theta(th_img)[:, None]
q_img = np.exp(sg_img + 1j * th_img[:, None])
z_img = z_of_q(q_img)
sc = axR.scatter(
    z_img.real.ravel(),
    z_img.imag.ravel(),
    c=sg_img.ravel(),
    s=1.0,
    cmap="viridis",
    vmin=0,
    vmax=LN_COLL,
    zorder=3,
    rasterized=True,
    linewidths=0,
)
cb = fig.colorbar(sc, ax=axR, fraction=0.046, pad=0.02)
cb.set_label(r"$\ln|q|$ of the preimage point")

# image of the unit circle and of the outer boundary |q| = e^{sigma_V}
for sfun, col, lw, _lab in [
    (lambda t: 0 * t, "k", 1.0, r"$Z(|q|=1)$"),
    (sigma_of_theta, C_BLUE, 1.4, r"$Z(|q|=e^{\sigma_V})$"),
]:
    t = np.linspace(0, 2 * np.pi, 4001)
    zz = z_of_q(np.exp(sfun(t) + 1j * t))
    axR.plot(zz.real, zz.imag, color=col, lw=lw, zorder=4)
# image of the fold arcs: Z = cos^2(theta/2) on the real axis, in (9/25, 16/25)
axR.plot([9 / 25, 16 / 25], [0, 0], color=C_VERM, lw=5, zorder=6, solid_capstyle="butt")
axR.set_xlim(x0_, x1_)
axR.set_ylim(y0_, y1_)
axR.set_aspect("equal")
axR.set_xlabel(r"$\mathrm{Re}\,Z$")
axR.set_ylabel(r"$\mathrm{Im}\,Z$")
axR.set_title(r"$Z$-plane: image of $Q_V$ covers $\mathcal{V}_{0,4}$ once", fontsize=11)
for xy, txt in [
    ((-0.1, 0.0), r"$\mathcal{F}_u$"),
    ((1.1, 0.0), r"$\mathcal{F}_t$"),
    ((-1.75, 2.25), r"$\mathcal{F}_s$"),
    ((2.75, -2.25), r"$\mathcal{F}_s$"),
    ((0.5, 0.95), r"$\mathcal{V}_{0,4}$"),
]:
    axR.text(
        *xy,
        txt,
        ha="center",
        va="center",
        fontsize=12,
        zorder=7,
        bbox=dict(fc="white", ec="none", alpha=0.7, pad=1.5),
    )
axR.legend(
    handles=[
        Patch(fc="#f2f2f2", ec="#555555", label=r"$\mathcal{V}_{0,4}$ (criterion)"),
        Patch(fc="#cfe3f1", ec="#555555", label=r"$\mathcal{F}_s$"),
        Patch(fc="#f8dfb0", ec="#555555", label=r"$\mathcal{F}_t$"),
        Patch(fc="#cfe9de", ec="#555555", label=r"$\mathcal{F}_u$"),
        Line2D([], [], color="k", lw=1, label=r"$Z(|q|=1)$"),
        Line2D([], [], color=C_BLUE, lw=1.4, label=r"$Z(|q|=e^{\sigma_V})$"),
        Line2D(
            [],
            [],
            color=C_VERM,
            lw=5,
            label=r"image of fold arcs $\subset(\frac{9}{25},\frac{16}{25})$",
        ),
    ],
    loc="upper right",
    fontsize=7.5,
    framealpha=0.95,
)

OUT.mkdir(parents=True, exist_ok=True)
for ext in ("svg", "pdf"):
    fig.savefig(OUT / f"circle-gluing-covering.{ext}", dpi=200)
print("saved", OUT / "circle-gluing-covering.svg")
