#!/usr/bin/env python3
"""Prototype Fig.2 — Cartopy faceted small multiples (journal layout test).

Panel (a): world, Robinson. Panel (b): Europe zoom, Robinson with extent.
Same variable (log10 POP_EST), same 5 quantile classes, ONE shared colourbar
(standard 1: facets share legend and scale). Panel letters a/b + small titles.

Run from journal-figure-pipeline/ with the geovis venv:
  ../geovis/venv/bin/python prototype/fig2_cartopy_facets.py
Outputs: figures/pipeline_fig2_cartopy_facets.png + .caption.txt
"""
import numpy as np
import geopandas as gpd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import colormaps
from matplotlib.colors import BoundaryNorm
from matplotlib.font_manager import FontProperties, fontManager
import cartopy.crs as ccrs
import cartopy.feature as cfeature

DATA = "../geovis/tmpdata/ne_110m_admin_0_countries.geojson"
OUT = "figures/pipeline_fig2_cartopy_facets.png"

# CJK font (matplotlib default DejaVu has no CJK; verified pitfall, geovis report)
fontManager.addfont("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc")
plt.rcParams["font.family"] = "Noto Sans CJK SC"
plt.rcParams["font.size"] = 10

gdf = gpd.read_file(DATA)
gdf["logpop"] = np.log10(gdf["POP_EST"].clip(lower=1))
pop_year = int(gdf["POP_YEAR"].mode().iloc[0])
breaks = np.quantile(gdf["logpop"], [0, 0.2, 0.4, 0.6, 0.8, 1.0])
cmap = colormaps["YlGnBu"]
norm = BoundaryNorm(breaks, cmap.N)

# Journal single-column design width (~17 cm): fonts are true point sizes only
# when the figure is printed at this width. A 12 in wide figure with 8 pt
# fonts would print at ~55% scale and fail standard 5.
fig = plt.figure(figsize=(7.2, 3.9), dpi=300)
fig.suptitle("World population by country — world view and Europe detail",
             fontsize=11, fontweight="bold", y=0.98)

# Deterministic 3-row layout: panels / colourbar / footer. The earlier
# subplots_adjust + pad-based colourbar let the colourbar label collide
# with the footer (verified 2026-11-14); GridSpec reserves each row.
gs = fig.add_gridspec(3, 2, height_ratios=[8, 0.7, 1.0], hspace=0.5,
                      left=0.02, right=0.98, top=0.86, bottom=0.02)
ax_a = fig.add_subplot(gs[0, 0], projection=ccrs.Robinson())
ax_a.set_title("(a) World", fontsize=10, loc="left")
ax_a.add_feature(cfeature.OCEAN, color="#D6EAF8", zorder=0)
ax_a.add_feature(cfeature.LAND, color="#F2F2F2", zorder=0)
gdf.plot(ax=ax_a, column="logpop", cmap=cmap, norm=norm,
         edgecolor="black", linewidth=0.25, transform=ccrs.PlateCarree())
ax_a.gridlines(draw_labels=False, color="gray", alpha=0.4, linestyle="--")
# manual north arrow (Cartopy has no built-in one) + manual scale bar.
# Scale bar drawn in map coordinates along the equator in the Pacific
# (lon -170..-125, all ocean): 5 x 9-degree segments = 5 x 1000 km at the
# equator (1 deg = 111.32 km). A black underlay gives the white segments an edge.
ax_a.annotate("N", xy=(0.94, 0.90), xycoords="axes fraction", fontsize=12,
              fontweight="bold", ha="center")
ax_a.annotate("", xy=(0.94, 0.97), xytext=(0.94, 0.90), xycoords="axes fraction",
              textcoords="axes fraction",
              arrowprops=dict(arrowstyle="-|>", color="black", lw=1.5))
ax_a.plot([-170, -125], [0, 0], color="black", lw=5, solid_capstyle="butt",
          transform=ccrs.PlateCarree(), zorder=5)
for i in range(5):
    lo, hi = -170 + 9 * i, -170 + 9 * (i + 1)
    ax_a.plot([lo, hi], [0, 0], color="black" if i % 2 == 0 else "white",
              lw=3.5, solid_capstyle="butt", transform=ccrs.PlateCarree(),
              zorder=6)
ax_a.text(-170, -7, "0", transform=ccrs.PlateCarree(), fontsize=8,
          ha="center", va="top", zorder=6)
ax_a.text(-125, -7, "5000 km", transform=ccrs.PlateCarree(), fontsize=8,
          ha="center", va="top", zorder=6)

ax_b = fig.add_subplot(gs[0, 1], projection=ccrs.Robinson())
ax_b.set_title("(b) Europe detail", fontsize=10, loc="left")
ax_b.set_extent([-25, 45, 35, 72], crs=ccrs.PlateCarree())
ax_b.add_feature(cfeature.OCEAN, color="#D6EAF8", zorder=0)
ax_b.add_feature(cfeature.LAND, color="#F2F2F2", zorder=0)
gdf.plot(ax=ax_b, column="logpop", cmap=cmap, norm=norm,
         edgecolor="black", linewidth=0.25, transform=ccrs.PlateCarree())
ax_b.gridlines(draw_labels=False, color="gray", alpha=0.4, linestyle="--")

# ONE shared colourbar for both facets (standard 1), in its own GridSpec row
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cax = fig.add_subplot(gs[1, :])
cbar = fig.colorbar(sm, cax=cax, orientation="horizontal", ticks=breaks)
cbar.set_label("log10(population, persons) — 5-class quantile", fontsize=9)
cbar.ax.tick_params(labelsize=9)

fig.text(0.5, 0.055,
         "Source: Natural Earth 110m, 177 countries, POP_EST 2019  |  "
         "Robinson  |  5-class quantile log10(POP_EST)",
         ha="center", fontsize=8)
fig.text(0.5, 0.012,
         "Software: Cartopy 0.26.0 / matplotlib / GeoPandas  |  "
         "Colours: ColorBrewer YlGnBu",
         ha="center", fontsize=8)
plt.savefig(OUT, dpi=300)
print("saved", OUT)

caption = f"""Figure 2 — World population by country, faceted: (a) world view, (b) Europe detail.
Data: Natural Earth 110m admin_0_countries, N = {len(gdf)} countries; POP_EST year {pop_year}.
Method: log10(POP_EST), 5-class quantile classification; breaks (log10): {", ".join(f"{b:.2f}" for b in breaks)}.
Both panels share one colourbar and one classification (standard 1); panel (b) is a geographic zoom, not a second variable.
Map elements: shared legend (horizontal colour bar), manual scale bar (panel a, 1000 km at equator), manual north arrow (panel a); panel (b) has no separate scale bar — same projection, scale noted in caption.
Colours: ColorBrewer YlGnBu (sequential, colourblind-safe set).
Software: Cartopy 0.26.0 / matplotlib / GeoPandas; CJK font Noto Sans CJK SC (registered explicitly).
Limits: scale bar and north arrow are hand-drawn (Cartopy has no built-in scale bar / north arrow); panel (b) extent is PlateCarree degrees on a Robinson base.
Reproduction: run prototype/fig2_cartopy_facets.py from journal-figure-pipeline/ with the geovis venv.
"""
open("figures/pipeline_fig2_cartopy_facets.caption.txt", "w", encoding="utf-8").write(caption)
