#!/usr/bin/env python3
"""Prototype Fig.1 — PyGMT main map (journal-ready static choropleth).

Data: Natural Earth 110m countries (177), variable log10(POP_EST),
5-class quantile classification, ColorBrewer YlGnBu (colorblind-safe
sequential). Target: the 8 journal standards (see REPORT.md §4).

Run from journal-figure-pipeline/ with the geovis venv:
  ../geovis/venv/bin/python prototype/fig1_pygmt_main.py
Outputs: figures/pipeline_fig1_pygmt.png + figures/pipeline_fig1_pygmt.caption.txt
"""
import numpy as np
import geopandas as gpd
import matplotlib
matplotlib.use("Agg")
from matplotlib import colormaps
import pygmt

DATA = "../geovis/tmpdata/ne_110m_admin_0_countries.geojson"
OUT = "figures/pipeline_fig1_pygmt.png"

gdf = gpd.read_file(DATA)
gdf["logpop"] = np.log10(gdf["POP_EST"].clip(lower=1))
pop_year = int(gdf["POP_YEAR"].mode().iloc[0])

# 5-class quantile breaks (standard 2: <= 5-7 classes)
breaks = np.quantile(gdf["logpop"], [0, 0.2, 0.4, 0.6, 0.8, 1.0])
cmap = colormaps["YlGnBu"]
colors = [matplotlib.colors.to_hex(cmap(f)) for f in (0.15, 0.35, 0.55, 0.75, 0.95)]
cls = np.digitize(gdf["logpop"], breaks[1:-1])  # 0..4

with pygmt.config(
    FONT_TITLE="14p,Helvetica-Bold,black",
    FONT_LABEL="10p,Helvetica,black",
    FONT_ANNOT_PRIMARY="9p,Helvetica,black",
    MAP_FRAME_TYPE="plain",
):
    fig = pygmt.Figure()
    fig.basemap(
        region="d",
        projection="R15c",
        frame=["a30g30", "+tWorld population by country"],
    )
    fig.coast(shorelines=False, water="#D6EAF8", land="#F2F2F2")
    for i in range(len(gdf)):
        fig.plot(data=gdf.iloc[[i]], fill=colors[cls[i]], pen="0.25p,black")
    # Legend = colorbar with ticks at the class breaks.
    # Note (verified 2026-11-14): pygmt 0.19 makecpt accepts GMT CPT names and
    # a few matplotlib names (viridis works) but NOT "YlGnBu"/"ylgnbu"; a
    # hand-written CPT file is used so legend and map classes match exactly.
    def _rgb(hexcolor):
        h = hexcolor.lstrip("#")
        return f"{int(h[0:2], 16)}/{int(h[2:4], 16)}/{int(h[4:6], 16)}"

    cpt_lines = ["# COLOR_MODEL = RGB",
                 "# YlGnBu 5-class, ColorBrewer (colorblind-safe sequential)"]
    for i in range(5):
        cpt_lines.append(
            f"{breaks[i]:.4f}  {_rgb(colors[i])}  {breaks[i + 1]:.4f}  {_rgb(colors[i])}")
    cpt_lines += ["B  128/128/128", "F  255/255/255", "N  128/128/128"]
    cpt_path = "prototype/ylgnbu5.cpt"
    open(cpt_path, "w", encoding="utf-8").write("\n".join(cpt_lines) + "\n")
    pygmt.makecpt(cmap=cpt_path, series=[breaks[0], breaks[-1]])
    fig.colorbar(
        frame=["a1f0.5", "x+lLog10 population (persons)"],
        position="JMR+o0.6c/0c+w8c/0.4c",
    )
    # Scale bar (standard 4), drawn manually in map coordinates.
    # GMT's own scalebar/rose decorations clip at the frame edge on a global
    # Robinson map (verified 2026-11-14: new-API scalebar draws a diagonal line
    # across the figure; old-API -L/-T clip at the frame edge), so the pipeline
    # draws them as data: 5 x 9-degree segments along the equator
    # (9 deg = 1000 km at the equator, 5 segments = 5000 km), alternating
    # black/white, with end labels. Same for the north arrow (triangle + "N").
    import pandas as pd
    seg_lons = [(-175 + 9 * i, -175 + 9 * (i + 1)) for i in range(5)]
    for i, (lo, hi) in enumerate(seg_lons):
        seg = pd.DataFrame({
            "lon": [lo, hi, hi, lo, lo],
            "lat": [-3, -3, 3, 3, -3],
        })
        fig.plot(x=seg["lon"].values, y=seg["lat"].values,
                 fill="black" if i % 2 == 0 else "white", pen="0.5p,black")
    fig.text(x=-175, y=-7, text="0", font="8p,Helvetica,black",
             justify="CT")
    fig.text(x=-130, y=-7, text="5000 km", font="8p,Helvetica,black",
             justify="CT")
    fig.text(x=-152.5, y=-12, text="scale at equator", font="7p,Helvetica,black",
             justify="CT")
    # North arrow: triangle + "N", placed in the North Pacific where Robinson
    # meridians are near-vertical (at lon 150 the triangle renders as a slanted
    # blade because meridians converge — verified 2026-11-14).
    arrow = pd.DataFrame({"lon": [-155, -158.5, -151.5, -155],
                          "lat": [50, 38, 38, 50]})
    fig.plot(x=arrow["lon"].values, y=arrow["lat"].values,
             fill="black", pen="0.5p,black")
    fig.text(x=-155, y=55, text="N", font="12p,Helvetica-Bold,black",
             justify="BC")
    fig.savefig(OUT, dpi=200)

caption = f"""Figure 1 — World population by country (choropleth, Robinson projection).
Data: Natural Earth 110m admin_0_countries, N = {len(gdf)} countries; POP_EST year {pop_year}; source: naturalearth (nvkelso/natural-earth-vector).
Method: log10(POP_EST), 5-class quantile classification; breaks (log10): {", ".join(f"{b:.2f}" for b in breaks)}.
Colours: ColorBrewer YlGnBu (sequential, colourblind-safe set); class colours sampled at 0.15/0.35/0.55/0.75/0.95 of the ramp.
Map elements: legend (colour bar, 5 discrete class blocks), scale bar (hand-drawn: 5 x 1000 km segments along the equator, total 5000 km), north arrow (hand-drawn triangle + "N"), graticule 30 deg.
Footer line (source / projection / software) is appended below the map by prototype/assemble.py (PIL strip), because GMT fig.text with a negative offset falls outside the saved page and a positive offset lands on Antarctica (verified 2026-11-14).
Software: PyGMT 0.19.0 / GMT 6.5.0; Python 3.12; geopandas (data handling).
Reading: the map shows spatial distribution only; numerical comparison belongs in a table (standard 6). Antarctica (POP_EST 140) falls in the lowest class.
Reproduction: run prototype/fig1_pygmt_main.py from journal-figure-pipeline/ with the geovis venv; input ../geovis/tmpdata/ne_110m_admin_0_countries.geojson.
"""
open("figures/pipeline_fig1_pygmt.caption.txt", "w", encoding="utf-8").write(caption)
print("saved", OUT)
print("breaks:", [round(float(b), 2) for b in breaks])
