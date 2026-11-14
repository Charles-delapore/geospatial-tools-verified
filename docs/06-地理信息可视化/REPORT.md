# 地理信息可视化（geovisualization）领域报告

- **核验日期：2026-11-14**（所有 star 数、最近推送时间均为该日 GitHub API 快照；另有说明处除外）
- **领域范围**：静态制图、交互地图、3D/时空可视化、制图美学、dashboard、WebGIS 前端
- **项目总数：30 个**（对应 29 个仓库；pydeck 与 deck.gl 共享同一仓库 `visgl/deck.gl`，分列两条）
- **仓库本地位置**：`geovis/repos/<项目名>/`（`git clone --depth 1`）；**出图位置**：`geovis/figures/`；**实测环境**：`geovis/venv/`（Python 3.12，`--system-site-packages`，另装 geopandas 1.2.0 / folium 0.20.0 / lonboard 0.17.0 / cartopy 0.26.0 / geoplot 0.5.1 / pydeck 0.9.3 / datashader 0.19.1 / leafmap 0.64.7 / holoviews 1.23.2 / geoviews 1.16.0 / pyarrow 26.0.1；补验新增 pygmt 0.19.0 / geovista 0.5.3 / pyvista 0.49.2 / osmnx 2.1.1 / vsketch 1.2.0 / opencv-python-headless 5.0.0.93 / rioxarray 0.23.0 / scikit-image 0.26.0）；系统级：GMT 6.5.0（apt，含 libgmt6t64）、libegl-mesa0 25.2.8、libosmesa6 25.1.7、Xvfb 已装
- **共享实测数据**：Natural Earth 110m 世界国家（177 国，2026-11-14 自 `nvkelso/natural-earth-vector` 下载），分级变量为 `POP_EST` 的对数 `log10(人口估计)`；datashader 用 20 万合成聚类点。**同一份数据跑遍各库**，以便横向比较默认出图。
- **本机约束如实记录**：共享虚拟机内存紧张（实测时可用内存常 <500 MB）、无 headless 浏览器（无 Chromium/Playwright），且与其它分域任务并行抢占网络与 CPU，git clone 与 pip 安装均显著变慢；JS 类工具因此只生成独立 HTML 演示并做 Node 语法校验，**未做浏览器截图**（见“验证小结”）。补验（2026-11-14）时网络有所恢复，第二批 13 个克隆全部完成，GMT/osmnx/vsketch/EGL/OSMesa 均已装上（见文末“补验说明”）。

## 方法与口径

- **检索**：以 GitHub API（`api.github.com/repos/...`，2026-11-14）取 stars/许可证/最近推送/最近发版为准；许可证另核对仓库内 `LICENSE*` 文件头与 npm `package.json` 的 `license` 字段，API 返回 `NOASSERTION` 的逐个复核（见表中备注）。
- **“最近更新”**：用 API `pushed_at`（默认分支最新推送），另列本地 clone 的 HEAD 提交日期，两者不一致时以脚注说明（如 geoplot、mapsf）。
- **验证状态分级**：`✅ 实测出图`（本地渲染出 PNG 或可交互 HTML 并目视/语法检查过）；`✅ 代码验证`（import/对象创建/API 调用通过，无出图）；`⚠️ 部分验证`（HTML 已生成但仅做语法校验，未浏览器截图）；`📄 文档核查`（只读了 README/关键代码与 API 元数据，未本地运行）；`❌ 未跑通`（写明原因）。
- **不编造**：用例/采用者只写 README、官方文档或检索到的公开报道中能找到的；查不到写“未查到”。同名项目已区分：`map3d` 指 `cartesiancs/map3d`（OSM 3D 城市），非其它同名 3D 库；`GeoLibre` 指 `opengeos/GeoLibre`，非同名小工具；`PMTiles` 指 `protomaps/PMTiles` 规范与参考实现。

## 项目总表

| # | 项目 | 仓库 | 许可证 | Stars（2026-11-14） | 最近推送 | 用途一句话 | 验证状态 |
|---|---|---|---|---|---|---|---|
| 1 | GeoPandas（`.plot` / `.explore`） | geopandas/geopandas | BSD-3-Clause | 5,297 | 2026-10-31 | Python 地理数据框的静态绘图与交互探索 | ✅ 实测出图（01 PNG、02 HTML） |
| 2 | Folium | python-visualization/folium | MIT（仓库 LICENSE.txt 实测为 MIT 文本；API 返回 NOASSERTION） | 7,420 | 2026-11-13 | Python 调 Leaflet 的交互地图 | ✅ 实测出图（03 HTML） |
| 3 | leafmap | opengeos/leafmap | MIT | 3,801 | 2026-11-12 | Jupyter 里一行代码做交互制图/分析的多后端封装 | ✅ 实测出图（10 HTML）；本地装 0.64.7 |
| 4 | lonboard | developmentseed/lonboard | MIT | 977 | 2026-11-13 | Jupyter 里基于 deck.gl + GeoArrow 的高速交互地图 | ✅ 实测出图（07 HTML）；本地装 0.17.0 |
| 5 | pydeck | visgl/deck.gl（与 deck.gl 同库） | MIT | 14,757（与 deck.gl 同库） | 2026-11-13 | deck.gl 的 Python 绑定 | ✅ 实测出图（08 HTML）；本地装 0.9.3 |
| 6 | Plotly.py（地图） | plotly/plotly.py | MIT | 18,899 | 2026-11-13 | 声明式交互图表与地图（含 choropleth） | ✅ 实测出图（04 HTML；PNG 因缺 kaleido 未出） |
| 7 | Datashader | holoviz/datashader | BSD-3-Clause | 3,573 | 2026-11-09 | 大数据点/线栅格化聚合渲染 | ✅ 实测出图（09 PNG）；本地装 0.19.1 |
| 8 | hvPlot | holoviz/hvplot | BSD-3-Clause | 1,363 | 2026-11-10 | pandas/GeoPandas 的一行代码交互绘图 | ✅ 实测出图（17 HTML，需另装 geoviews 1.16.0） |
| 9 | Cartopy | SciTools/cartopy | BSD-3-Clause | 1,627 | 2026-11-10 | matplotlib 上的投影/海岸线制图库 | ✅ 实测出图（05 PNG）；本地装 0.26.0 |
| 10 | geoplot | ResidentMario/geoplot | MIT | 1,214 | 2026-06-08（API）；本地 HEAD 提交 2023-07-04，见注 | matplotlib 上的高层专题制图 | ✅ 实测出图（06 PNG）；本地装 0.5.1 |
| 11 | PyGMT | GenericMappingTools/pygmt | BSD-3-Clause | 882 | 2026-11-10 | GMT 的 Python 接口，出版级制图 | ✅ 实测出图（18 PNG；补验装 GMT 6.5.0 后跑通，见验证小结） |
| 12 | GeoVista | bjlittle/geovista | BSD-3-Clause | 234 | 2026-11-13 | PyVista 上的 3D 制图渲染与网格分析 | ✅ 实测出图（20 PNG；补验装 libosmesa6 后离屏渲染跑通；`add_base_layer` 仍失败，见验证小结） |
| 13 | prettymaps | marceloprates/prettymaps | AGPL-3.0（仓库 LICENSE 文件实测；旧文曾称 CC-BY-NC，已过期） | 14,339 | 2026-07-30 | OSM 数据画艺术风/海报风地图 | ✅ 实测出图（19 PNG，巴黎 800 m 真实 OSM 取数；pip 安装仍失败，改走源码导入，见深挖第 5 节） |
| 14 | prettymapp | chrieke/prettymapp | MIT | 2,838 | 2026-07-08 | prettymaps 的 Streamlit 网页版+重写版 | 📄 文档核查（未本地运行 Streamlit） |
| 15 | ipyleaflet | jupyter-widgets/ipyleaflet | MIT | 1,546 | 2026-05-07 | Jupyter 里的 Leaflet 桥接 widget | ✅ 代码验证（Map/GeoJSON 对象创建通过，无导出接口） |
| 16 | MapLibre GL JS | maplibre/maplibre-gl-js | BSD-3-Clause（npm package.json 实测；API 返回 NOASSERTION） | 12,084 | 2026-11-13 | 开源矢量瓦片 WebGL 地图（Mapbox GL 的社区分叉） | ⚠️ 部分验证（12 HTML 演示，Node 语法校验通过，未浏览器截图） |
| 17 | Leaflet | Leaflet/Leaflet | BSD-2-Clause | 45,923 | 2026-11-13 | 最轻量的移动友好交互地图库 | ⚠️ 部分验证（11 HTML 演示，语法校验通过，未浏览器截图） |
| 18 | OpenLayers | openlayers/openlayers | BSD-2-Clause | 12,658 | 2026-11-13 | 企业级 GIS 浏览器库，格式与 OGC 支持最全 | ⚠️ 部分验证（13 HTML 演示，语法校验通过，未浏览器截图） |
| 19 | deck.gl | visgl/deck.gl | MIT | 14,757 | 2026-11-13 | WebGL2 大数据地理可视化框架（60+ 图层） | ⚠️ 部分验证（14 HTML 演示，语法校验通过，未浏览器截图） |
| 20 | Kepler.gl | keplergl/kepler.gl | MIT | 12,091 | 2026-11-13 | 无代码大规模地理数据分析/仪表盘 | 📄 文档核查（v3.3 升级 deck.gl 9.2；未本地构建） |
| 21 | CesiumJS | CesiumGS/cesium | Apache-2.0 | 15,949 | 2026-11-13 | 3D 地球仪/WebGL 全球可视化 | 📄 文档核查（1.147，2026-11-02） |
| 22 | TerriaJS | TerriaJS/TerriaJS | Apache-2.0 | 1,380 | 2026-11-13 | 目录驱动的 2D/3D 地理数据浏览器框架 | 📄 文档核查（未本地构建） |
| 23 | GeoLibre | opengeos/GeoLibre | MIT | 8,601 | 2026-11-13 | 云原生 GIS：浏览器/桌面/移动/Jupyter 同体 | 📄 文档核查（v3.7.0，2026-11-08） |
| 24 | PMTiles | protomaps/PMTiles | BSD-3-Clause（仓库 LICENSE 头实测；API 返回 NOASSERTION） | 3,110 | 2026-09-16 | 单文件静态瓦片格式与参考实现 | 📄 文档核查（基础设施，不直接出图） |
| 25 | Bertin.js | riatelab/bertin | MIT | 319 | 2023-10-23 | D3 之上的专题制图库（分级/比例/注记分层） | ⚠️ 部分验证（15 HTML 演示，语法校验通过，未浏览器截图）；**注意：2023-10 后无推送，疑似停更；仓库已由 neocarto/bertin 迁移至 riatelab/bertin（2026-11-14 补验核实，旧地址返回 Moved Permanently）** |
| 26 | Observable Plot | observablehq/plot | ISC（npm package.json 实测） | 5,425 | 2026-11-05 | D3 团队的声明式可视化语法，含地理投影 | ⚠️ 部分验证（16 HTML 演示，语法校验通过，未浏览器截图） |
| 27 | mapsf（R） | riatelab/mapsf | GPL-3.0 | 249 | 2026-11-09（API）；本地 HEAD 提交 2026-10-09 | R 的专题制图包（图例/比例尺/指北针原生） | 📄 文档核查（本机无 R，未运行；仓库 README/API 已读） |
| 28 | map3d | cartesiancs/map3d | MIT | 2,690 | 2026-11-07 | OSM 数据一键生成 3D 城市白模并导出 GLB | 📄 文档核查（未本地构建 npm 应用） |
| 29 | 3D-Geo-Vis 2 | jakubzejdlik/3d_geo_vis_2 | 未查到（仓库无 LICENSE 文件，API 亦无） | 0 | 2026-05-21 | 3D 专题可视化实验应用（7 种 3D 方法） | 📄 文档核查（仓库 0 star，见“发现的主要问题”） |
| 30 | MapStore2 | geosolutions-it/MapStore2 | 未查到（仓库未见 LICENSE 文件，API 返回 NOASSERTION） | 670 | 2026-11-13 | 地图/dashboard/地理故事的开源框架（3D 支持） | 📄 文档核查（未本地构建） |

注：
- geoplot：API `pushed_at` 为 2024-06-08，但本地 `git log -1` 的 HEAD 提交日期为 2023-07-04——推送时间晚于 HEAD 提交，可能因分支/标签推送导致；按 API 口径仍算“2024 年后有活动”，但实质代码提交停留在 2023 年，见“发现的主要问题”。
- mapsf：同理，API 推送 2026-11-09，本地 HEAD 提交 2026-10-09。
- GeoLibre：API 记录仓库创建于 2026-05-27，约半年内获 8,601 stars，增速异常高（与 v2.4–v3.7 高频发版与 leafmap/geemap 作者的既有受众有关，见深挖）。
- 3D-Geo-Vis 2：API 返回 stars 0、description 为空、2025-10-20 创建；其存在性依据为 ICA EuroCarto 2026 摘要（doi:10.5194/ica-abs-12-160-2026）中给出的同名 GitHub 链接，见深挖与问题节。
- 本表 stars 为快照值，不同日期查询会有波动；MapLibre、PMTiles、Folium、MapStore2 的许可证以仓库文件/npm 为准，不以 API 的 NOASSERTION 为准。

## 重点项目深挖（5 个）

### 1. lonboard —— 2024–2026 年 Python 地理可视化最值得跟进的新旗舰

- **定位**：Development Seed 的 Kyle Barron 主导，Jupyter 里的 deck.gl 前端 + GeoArrow/GeoParquet 数据层。2023-08 建库，stars 仅 977（2026-11-14），但发版极密：v0.13.0（2025-11-05）、v0.14.0（2026-02-11）、v0.15.0（2026-03-13）、v0.16.0（2026-04-02）、v0.17.0（2026-10-02），最近推送 2026-11-13。
- **2024–2026 的关键变化**：0.13 引入两种渲染模式（deck.gl-first 与 MapboxOverlay）、富 `Basemap` 类、H3/A5/geohash/S2 图层、地图控件；0.17 改用上游 deck.gl-raster 的 `RasterTileLayer`。另有 DuckDB、Overture Maps、PMTiles 栅格、MovingPandas（TripsLayer）等官方示例。
- **实测**：本地装 0.17.0；`PolygonLayer.from_geopandas` + `Map.to_html()` 出图 07（4.8 MB HTML）。实测踩坑两处，均已定位并绕过：（a）本机 venv 起初未装 pyarrow，lonboard 0.17 把 pyarrow 列为可选依赖，pandas 的 `convert_dtypes` 路径因此报 `NameError: name 'pa' is not defined`——补装 pyarrow 26.0.1 后解决；（b）`get_fill_color` 不接受列名字符串，须用 `lonboard.colormap.apply_continuous_cmap` 先算出逐要素 RGB 数组再传入（官方 data-filter 示例同款用法）。这两点是新手最容易卡住的地方，文档未在显眼处提示。
- **采用者**：README/示例中未列出具名机构采用者；生态位是 Development Seed 的云原生地理栈（配合 DuckDB、Overture、GeoParquet），属于“工程师与研究者正在迁移过去”的工具，而非已有大规模部署的产品。
- **期刊标杆对照**：交互渲染锐利、GPU 性能好，但默认无图例/比例尺/指北针，`Map` 的控件是 0.13 才补的；要做投稿图仍需另行出图例与版式。结论：**分析探索首选，出版图需二次加工**。

### 2. GeoLibre —— 2026 年窜升最快的云原生 GIS（需警惕“新”与“稳”的落差）

- **定位**：opengeos（Qiusheng Wu，leafmap/geemap 作者）的新作：浏览器里的轻量 GIS，同一代码库出 Web/桌面（Tauri 2）/Android/Jupyter widget；浏览器内跑 DuckDB-WASM + 空间扩展，数据不出本机；另有行星底图（月球、火星等，OpenPlanetaryMap/USGS）。
- **数字**：API 记录创建于 2026-05-27，至 2026-11-14 已 8,601 stars、961 forks、最近推送 2026-11-13；v3.7.0 发布于 2026-11-08（室内地图 IMDF/IndoorGML、ArcGIS I3S 建筑场景层、JAXA Earth 119 个数据集插件、打印布局改进），v2.5.0 在 2026-08-05。第三方报道称 v2.4.0 单版本约 1,300 次安装下载。
- **为什么值得深挖**：它是本表唯一同时覆盖“WebGIS 前端 + dashboard + 打印出图 + Jupyter”的项目，且把 QGIS/ArcGIS Pro 工程导入、离散全球格网（A5/DGGRID/DGGAL）、高光谱数据立方、自托管服务器都排进了 2026 年的路线图；打印布局（暗色地图页背景、页脚）直接回应期刊标杆里的“版式”要求。
- **实测限度**：本次只做了文档与元数据核查，**未本地构建**（TypeScript + Rust + Tauri 构建链超出本机共享 VM 的合理工作量）；其 Web 端可直接访问 `web.geolibre.app`，但本次未做浏览器实测——报告使用者如需采用，建议先在线试用再决定。
- **风险提示**：半年 8.6k stars 的增速与作者既有受众（leafmap 3.8k stars、geemap 4k stars）高度相关，不宜直接解读为生产环境占有率；open issues 仅 18 条（2026-11-14），对如此体量的项目偏低，可能反映 issue 管理方式而非零缺陷。

### 3. MapLibre GL JS —— 开源矢量地图的事实标准接班人

- **定位**：Mapbox GL JS 最后一个开源版（v1.x）的社区分叉，现为独立基金会项目；WebGL 矢量瓦片、3D 地形/建筑、地球仪视图（v4+）、WebGL2。
- **数字**：12,084 stars；v6.18.0 发布于 2026-11-11（最近推送 2026-11-13）；第三方报道称 2025 年周下载 50 万+。许可证 BSD-3-Clause（以 npm `package.json` 为准；GitHub API 未识别）。
- **2024–2026 的关键变化**：v5 地球仪视图、与 deck.gl 的三种底图集成模式、v6 的持续迭代；deck.gl 9.4（2026-09）为其单独立了 `@deck.gl/maplibre` 模块，支持 MapLibre v4/v5/v6 的叠加与交错渲染——两者已互相成为默认搭档。
- **实测**：生成 12 号 HTML 演示（demotiles 官方样式 + 内嵌世界 GeoJSON + `interpolate` 分级设色 + 点击弹窗），Node 语法校验通过；**未浏览器截图**（本机无 headless 浏览器），渲染效果以代码与官方 demo 为据。本地 shallow clone 已于 2026-11-14 补验完成（maplibre-gl-js，366 MB）。
- **采用者**：未查到官方采用者名录；生态信号是“被 deck.gl/lonboard/GeoLibre 等上游项目默认集成”，属于基础设施型采用。
- **期刊标杆对照**：矢量底图精美、样式语言（MapLibre Style Spec）可控性强，期刊级与否取决于样式设计投入；默认 demotiles 样式只是起点，须另配图例与注记。结论：**做交互底图的首选底座，专题表达要靠上层图层与样式**。

### 4. Kepler.gl —— 无代码仪表盘的标杆，但 2026 年在“换引擎”

- **定位**：Uber 开源的无代码大规模地理数据分析工具（拖放 CSV/GeoJSON 即出交互地图与仪表盘），现为 kepler.gl 组织维护。
- **数字**：12,091 stars；最近推送 2026-11-13；最新发版为 v3.3.0-alpha.21（2026-11-13，仍处 alpha）。
- **2024–2026 的关键变化**：v3.1（2025-01）新增矢量瓦片层、Mapbox/MapLibre 双底图；v3.2（2025-08）新增栅格瓦片层（PMTiles/COG via STAC）；v3.3 把整个渲染栈从 deck.gl 8/luma.gl 8 升级到 deck.gl 9.2/luma.gl 9.2，编辑层迁移到 `@deck.gl-community/editable-layers`，TypeScript 升到 5.6。**这意味着 2026 年的 Kepler.gl 正处在大版本换引擎期**，alpha 标签与频繁推送并存。
- **实测限度**：未本地构建（npm 构建链 + 大体积，超出本次资源）；以 release notes 与仓库元数据为准。Python 侧有 `keplergl` 包（Jupyter widget），本次未另行安装验证。
- **期刊标杆对照**：默认 UI（图例、过滤、时间轴、分层控制）是本表交互工具中最 polished 的之一，接近“分析仪表盘”的期刊/报告配图要求；但静态导出仍需版式收尾，且 3D/动画表达偏重探索而非论证。结论：**给非程序员做探索与汇报演示的首选；投稿图仍需导出后加工**。


## 逐图美学评价（实测出图 20 幅）

> 口径：PNG 图（01、05、06、09、18、19、20）已**目视检查**；HTML 图（02–04、07、08、10–17）为本地运行官方 API 生成，**未做浏览器截图**（本机无 headless 浏览器），评价以生成代码、输出文件结构与各库默认样式为据，并在条目中注明。01–17 号图共用同一份 Natural Earth 110m 人口数据（datashader 除外，用合成点），因此配色与信息密度的差异主要来自库的默认值，而非数据；18 号与 01–17 同数据，19 号为巴黎 OSM 实取数据，20 号为合成正弦场。

- **01_geopandas_plot.png（GeoPandas `.plot`）**：YlGnBu 顺序配色干净、灰色国界线克制；但 `log10(人口)` 的连续映射使绝大多数国家挤在深蓝段（7–8.5），中段对比度弱，格陵兰等小人口国家反而最显眼，信息传达失真。版式上、下留白过大（约占画面三分之一），无经纬网、无比例尺/指北针；图例为纵向色带+竖排标签，字体为 Noto Sans CJK SC（已手动注册，否则中文成方框——这是本机 matplotlib 默认字体的坑）。结论：**能出图，但默认版式离期刊要求远**。
- **02_geopandas_explore.html（GeoPandas `.explore`）**：Leaflet 交互底图 + 分级设色 + 悬停 tooltip（国家名、POP_EST），图例自动生成；底图为 CartoDB Positron 浅色，数据层清晰。缺点是探索型默认：无比例尺控件之外的出版要素，导出静态图需另行截图；HTML 约 1.0 MB。结论：**探索体验好，出版需二次加工**。
- **03_folium_choropleth.html（Folium）**：CartoDB Positron 底图 + YlGnBu 分级 + 图例 + 图层控制，配色与 02 同源但控制更完整；字体与弹窗为 Leaflet 默认 sans，干净但无特色。信息密度适中（国家级设色 + 悬停数值）。结论：**最省事的交互分级图，审美天花板取决于底图与配色选择**。
- **04_plotly_choropleth.html（Plotly.py）**：Natural Earth 投影 + YlGnBu + 右侧连续色带，标题/色带标签字体规整，是本批 HTML 中版式最“报告化”的一幅；交互（悬停、缩放）流畅。不足：默认色带与地图比例偏大、国家边界偏细；PNG 导出因缺 kaleido 未出（`pip install kaleido` 可补，见验证小结）。结论：**默认出图最接近期刊/报告风的交互图之一**。
- **05_cartopy_robinson.png（Cartopy）**：本批静态图最佳构图：Robinson 投影椭圆边框、浅蓝海洋、灰色经纬网、YlGnBu 分级、右侧色带，字体清晰；但与 01 同病——对数人口的中段对比度弱，且无比例尺/指北针（Cartopy 需手工加）。另注：首次运行自动从 naturalearth S3 下载了海洋/陆地数据（110m），离线环境会失败。结论：**静态制图的底子最好，收尾靠手工**。
- **06_geoplot_choropleth.png（geoplot）**：Robinson 投影正确、国家填充与 01/05 一致；但**无海洋底色、无经纬网**，地图悬在白底上，色带无标签文字（`legend=True` 只给了色带），标题字号偏小。信息密度与 05 相同，视觉完成度低一档。结论：**投影能力在，版式细节缺失；且项目已停滞，慎作新选型**。
- **07_lonboard_world.html（lonboard）**：deck.gl GPU 渲染 + `apply_continuous_cmap` 的 YlGnBu 逐要素着色，文件 4.8 MB（含内嵌 GeoArrow 数据）；默认底图为 MapLibre 控制的浅色底图（0.13 起），悬停/缩放流畅。不足：默认无图例（须自己配色带说明），图例缺失是交互分析转出版的最大缺口。结论：**渲染质感与性能最佳，图例要自己补**。
- **08_pydeck_world.html（pydeck）**：GeoJsonLayer + YlGnBu 填充 + 悬停高亮（`auto_highlight`）+ tooltip（国家名与 log10 人口），深色 deck.gl 默认底色使设色对比鲜明；但无底图瓦片时地理参照弱（海岸线即国界线本身），且 tooltip 字体为 deck.gl 默认。结论：**大数据交互的质感标杆，底图与图例需另配**。
- **09_datashader_density.png（Datashader）**：本批最具视觉冲击的静态图：20 万合成点经 log 着色，紫—橙—黄渐变密度核层次分明，点簇边缘的稀疏点仍可见，坐标轴与标题干净。缺点同样明显：**无海岸线/底图**，密度团悬在经纬度空白框里，读者须自行对应大洲；且默认无色带图例（本图未加）。结论：**密度表达满分，地理上下文零分——必须叠加底图才可用**。
- **10_leafmap_world.html（leafmap，folium 后端）**：与 03 同源的 Leaflet 渲染 + 手工图例，leafmap 的价值不在本图（单图层设色），而在“换后端/加工具条/加 COG/STAC 图层”的 GUI 能力；本图版式与 03 接近，图例为自定义的单色块说明（非分级色带），信息量偏弱。结论：**图本身平庸，强在交互工具箱**。
- **11_leaflet_world.html（Leaflet 演示）**：CartoDB Positron 浅底 + YlGnBu 分级 + 右下角自定义图例 + 点击弹窗；Leaflet 默认字体与控件朴素、留白得当，是“干净但无个性”的典型。信息密度低（仅设色+弹窗），胜在加载快、代码短。结论：**轻量交互的审美下限有保障，上限靠样式**。
- **12_maplibre_world.html（MapLibre 演示）**：demotiles 矢量底图 + `interpolate` 分级填充 + 点击弹窗；矢量瓦片的文字注记与道路网使地图“像地图”，而非色块拼贴，这是与 Leaflet 栅格底图的最大观感差异。未截图，评价以样式与代码为据。结论：**底图质感本批最佳，专题层仍需设计**。
- **13_openlayers_world.html（OpenLayers 演示）**：OSM 栅格底图 + 矢量设色层；功能最全（投影、格式、控件），但默认样式最“工程”：控件、字体、配色均无修饰，与 Leaflet/MapLibre 的“开箱即好看”有差距。结论：**能力最强、默认最素**。
- **14_deckgl_world.html（deck.gl 演示）**：无底图瓦片的纯 GeoJsonLayer 渲染 + 悬停 tooltip；GPU 图层的边缘锐利、悬停高亮即时，是本批“数据层本身”质感最好的演示之一；但无底图时地理参照完全依赖读者对世界轮廓的熟悉。结论：**图层质感满分，底图是必选项而非可选项**。
- **15_bertin_world.html（Bertin.js 演示）**：本批唯一**原生带齐标题/脚注/比例尺/图例**的 JS 演示：NaturalEarth1 投影 + 5 级分位数 YlGnBu + 图例标题“人口估计 POP_EST”+ 公里比例尺，版式思路最接近期刊专题图。配色为 ColorBrewer 式，字体为 D3 默认 sans。未截图，评价以 bertin 官方 README 的图层语义与代码为据。结论：**专题图取向最正的 JS 库，可惜 2023 年后停更**。
- **16_observable_plot_world.html（Observable Plot 演示）**：Equal Earth 投影 + 球体浅蓝底 + 经纬网 + 5 级分位 YlGnBu + 图例，SVG 渲染线条干净、字体层级清晰，是本批静态观感最“出版化”的 JS 图；缺点是交互仅悬停标题，无缩放/过滤控件。结论：**静态专题图的默认审美最佳，交互需另写**。
- **17_hvplot_world.html（hvPlot）**：CartoLight 瓦片底图 + YlGnBu 多边形设色，Bokeh 输出的字体与工具条（平移/缩放/悬停）规整；但瓦片底图的道路/注记与设色层叠加后信息密度偏高，小国标签易淹没，且须另装 geoviews 才能用地理功能（本次实测的坑）。结论：**一行代码的性价比高，底图与设色的层次需调**。
- **18_pygmt_world.png（PyGMT，补验重渲）**：Robinson 投影 + viridis 分级 + 浅蓝海洋 + 30° 经纬网 + 右侧色带（log10 人口），标题与色带标签齐全，是本批静态图中“四件套”最接近齐全的一幅——只缺比例尺与指北针；字体为 GMT 默认无衬线，干净但无中文。配色与 01/05 同数据，但 viridis 比 YlGnBu 的中段对比更均匀。注：第二位补验员 2026-11-13 留下的 18 号原图为 1007×3883 的异常高画布（地图只占顶部约四分之一，右上角有杂散圆圈），本次已用正确图幅重渲（1063×651），原图备份于 `tmpdata/18_pygmt_world_orig_20261113.png`。结论：**静态制图的出版底子最好，补上比例尺/指北针即接近期刊要求**。
- **19_prettymaps_paris.png（prettymaps，补验新增）**：本批唯一真实 OSM 数据的艺术地图：巴黎市中心 800 m，塞纳河浅蓝点纹、建筑珊瑚红、绿地点纹、街道深灰、米白底，卢浮宫—杜乐丽一带的街区肌理与水岸转折都清晰可辨，左上角自带 OSM 署名框；3510×3510 高分辨率，印刷海报质感。信息密度极高但无图例/比例尺/指北针/标题，色彩是装饰性的而非数据编码。结论：**全场默认美感最佳，封面/海报首选；论证图需另加四件套**。
- **20_geovista_world.png（GeoVista，补验新增）**：本批唯一 3D 球体图：viridis 正弦场覆于球面 + 白色海岸线 + 底部横向色带（-1.00 至 1.00），球体明暗与海岸线走向清晰，视觉冲击强。缺点：36×18 粗网格导致色带呈明显横向条纹/面片感，色带标题“data”与 0.00 刻度重叠，无标题、无经纬网、无图例说明，背面半球全黑。结论：**封面图路线成立，专题表达需更细网格与版式收尾**。


## 期刊标杆（高权重评判尺度）

> 方法：选 3 本领域权威期刊（CaGIS、IEEE TVCG、Journal of Maps），各抽样 2024–2026 年代表性文章；优先开放获取、能看到全文和图的。Journal of Maps 4 篇读了全文 PDF（图注与方法节逐段核对）；CaGIS 2 篇见全文/预印本、2 篇仅见摘要与题录；TVCG 3 篇中 2 篇见作者版预印本/课程复现页、1 篇见 arXiv。另有 1 篇《The Cartographic Journal》的手机地图文作为旁证（检索中发现，非原定三刊，单独标注）。**只记录方法与风格层面的观察，不复制原文与图片；引用仅给标题与 DOI。** 查不到的写“未查到”，不编造图数与软件。

### 抽样文章一览

**Cartography and Geographic Information Science（CaGIS）**
| 文章 | 年份 | 图的类型与数量 | 图的组织方式 | 方法提到的制图软件/库 | 代码/数据链接 |
|---|---|---|---|---|---|
| Stachoň et al.《A comparison of performance using extrinsic and intrinsic bivariate cartographic visualizations…》DOI: 10.1080/15230406.2023.2264752 | 2025（52卷1期） | 双变量制图实验图（外在/内在两种编码）；图数未查到（全文付费墙） | 用户实验对照设计 | 未查到（仅见摘要与题录） | 未查到 |
| Guo & Jin《XFlowMap: cross-scale generalization and mapping of massive origin-destination data》DOI: 10.1080/15230406.2026.2738731；arXiv:2605.18777 | 2026-10-16 | 流图多幅（合成数据、美国县际迁移、出租车 OD）+ 分层对比图；未逐幅编号清点 | 跨尺度流簇先检测、再综合；新流符号把位置/方向/强度/OD 尺度合进单一符号 | 文中未点名绘图库（方法为扫描统计+聚类算法） | 有：Figshare doi:10.6084/m9.figshare.31702921（数据与软件） |
| Zhang et al.《MapGPT: an autonomous framework for mapping by integrating LLM and cartographic tools》DOI: 10.1080/15230406.2024.2404868 | 2024（51卷6期） | 案例地图多幅；未逐图清点 | 地图拆为符号/版式/注记等图元，LLM 按序调用工具生成 | MapGPT 框架本身；演示视频 | 有：github.com/AGI-GIS/MapGPT + 视频演示 |
| 《Cartographically representing emotions: a review of visualization approaches to emotion mapping…》DOI: 10.1080/15230406.2026.2653849 | 2026（在线首发） | 综述分类图；图数未查到 | 四类：离散点式（点图/emoji 图/饼图地图）、聚合式（热力/格网）、线/路径式、认知式（心智/草图地图） | 未查到（仅见摘要） | 未查到 |

**IEEE Transactions on Visualization and Computer Graphics（TVCG）**
| 文章 | 年份 | 图的类型与数量 | 图的组织方式 | 方法提到的制图软件/库 | 代码/数据链接 |
|---|---|---|---|---|---|
| Deng et al.《Multilevel Visual Analysis of Aggregate Geo-Networks》TVCG 30(7):3135–3150 | 2024-07 | 地铁式地理网络图多幅 + 交互截图/视频（TU Wien 课程复现页可见） | 多网络叠放：共享边如地铁线并排、k 着色自动区分、贝塞尔路由 | 复现实现未点名绘图库（课程页为学生实现）；方法本身为布局算法 | DOI 未查到（卷期页码已核实）；复现仓库见 TU Wien 课程页（GitLab 链接） |
| Nagel, Huber & Eder《Toward a Design Space for Embedded Urban Data Visualizations》IEEE VIS 2025 / TVCG 特刊（作者版预印本） | 2025 | Fig.1 设计空间总览、Fig.2 四步方法流程、Fig.3 尺度×真实度四象限 + 思辨示例图 | 内在维（空间数据/参照物/空间密度）在上、外在维（邻近度/尺度/真实度）在下 | 未查到（概念框架论文） | 预印本中未见公开仓库 |
| Schöttler et al.《Constraint-Based Breakpoints for Responsive Visualization Design and Development》TVCG 31(9):4593–4604，DOI: 10.1109/TVCG.2024.3410097；arXiv:2409.01339 | 2025 | 12 页 9 图；分级设色/比例圆/Dorling cartogram/六边形格网等多视图 | 同一数据多视图按（数据集，目标尺寸）确定性切换；约束=最小符号尺寸、元素重叠、长宽比 | D3.js 自制四组件（分级设色图、六边形图、比例圆图/cartogram、华夫图；d3-hexjson） | 有：responsive-vis.github.io/breakpoints（交互演示与补充材料） |

**Journal of Maps（均为 OA 全文已读）**
| 文章 | 年份 | 图的类型与数量 | 图的组织方式 | 方法提到的制图软件/库 | 代码/数据链接 |
|---|---|---|---|---|---|
| La Vigna et al.《Groundwater of Italy: hydrogeological mapping at 1:500,000 scale》DOI: 10.1080/17445647.2026.2666964 | 2026 | 主图 4 幅分幅（1:500,000）+ 在线 WebGIS；正文 Fig.1 方法流程、Fig.2 色盲对照色板、Fig.3 面积占比、Fig.4 流域分面（a/b/c） | 19 个水文地质综合体纯色（不用晕线）；图例对应历史分类与国家法规 | 文中只写“GIS platforms”（全文检索 QGIS 无命中）；另有 WebGIS 参与式平台 | 有：Open Science“Open Data”徽章，补充数据见 DOI 页 |
| Man et al.《Geology of the Borealis quadrangle (H01), Mercury》DOI: 10.1080/17445647.2026.2718817 | 2026 | 主图 1:3,000,000（制图 1:300,000–1:700,000）；正文 Fig.1 六面板数据产品（A–F）、Fig.2 位置图（A/B） | 极射投影（标准纬线 90°N），65°N 处比例失真如实标注为 1:2,860,000；两个版本（陨石坑三分级/五分级） | ArcGIS Pro + 地理数据库（6 个要素类），线 densify 间距 600 m | 有：补充材料含主图、shapefile 与底图栅格 |
| Tassetti et al.《High-resolution mapping of artificial reefs… Central Adriatic Sea》DOI: 10.1080/17445647.2025.2597814 | 2025 | 主图 0.20 m 格网水深图（54.5 公顷，252 座金字塔+506 根立柱）；Fig.1 左为 ADRIREEF WebGIS 主界面、右为研究区 inset | 主界面 + inset 的双框组织；多波束测深（MBES）+ 选区 ROV 视频 | ADRIREEF 项目 WebGIS（adrireef.github.io/sandbox3） | 有：补充图见 DOI 页 |
| Machado《Types of forest dynamics in Europe (2000–2018)》DOI: 10.1080/17445647.2026.2622821 | 2026 | 主图为欧盟 NUTS 森林动态类型图；正文 Fig.1 研究区与分析单元、Fig.2、Fig.3 LDT 预测方案图 | 708 个多边形/689 个 NUTS（马耳他因尺度与单元不兼容剔除，并在方法中说明） | QGIS 3.22 Białowieża + LDT4QGIS（Python/QGIS 工具） | 有：补充图见 DOI 页 |

**旁证（非原定三刊）**：《The Cartographic Journal》“Thematic World Maps in the News: How Effective are They on Smartphones?”DOI: 10.1080/00087041.2024.2447628。Fig.1 三家报纸手机屏占比（NZZ 21%、NYT 30%、Economist 26%，小国如瑞士仅约 7 个着色像素）；Fig.2 2023-01 至少 66% 读者经移动端访问。设计：按洲拆分+放大欧洲小国的分级设色图、东西半球拆分的 graduated circle 图；333 名 NZZ 读者用户研究。软件：早期人工 QGIS + Adobe Illustrator，疫情高频后自研新闻室工具 Q；文中点评 Plotly/Datawrapper/D3 只做缩放适配、不做“换设计”的响应式。

### 跨刊共性：美化特征

- **主图即成果**：Journal of Maps 的主图带比例尺/投影/数据源/版本说明，补充数据与 shapefile 同行；CaGIS/TVCG 则图 + 代码/演示链接并重，图不是装饰，是论证。
- **分面与小多图是默认组织**：六面板数据产品、a/b/c 分面、东西半球拆分、按洲拆分——不用单幅大图硬塞信息。
- **配色先讲语义与可及性**：顺序/发散/定性分开；意大利地下水文图专设 Fig.2 做色盲（protanopia）对照；高/中/低有固定色相家族。
- **底图克制**：水星图用单色马赛克与增强彩色各司其职；TVCG 地铁式网络用可开关底图/地名，数据层永远在底图之上。
- **标注与图例是论证的一部分**：图例对应法规/历史分类；比例尺变形如实标注（水星图 65°N 处比例失真写明）；字体层级分明，标题、图例、脚注（数据来源）三级齐全。
- **响应式不是缩放**：小屏要换设计（拆分、换符号、cartogram），最小符号尺寸/重叠/长宽比是硬约束（Schöttler 2025）。
- **交互要有可发现的 affordance**：权重过滤、悬停高亮、图层开关，而不是“可缩放”一句带过（Deng 2024；Nagel 2025）。
- **方法可复现**：软件 + 版本 + 参数写进方法（QGIS 3.22、ArcGIS Pro 六要素类、densify 600 m、D3 自制组件），数据/代码给 DOI 或仓库。

### 8 条期刊级制图规范（可执行）

1. **分面先行**：一幅图只讲一个结论；多变量/多时相用 a/b/c 分面或小多图，不用单图硬塞；每个分面共用同一图例与比例尺。
2. **配色讲语义**：顺序数据用顺序色、双向数据用发散色、类别用定性色；分级不超过 5–7 级；成图后做一次色盲模拟检查（至少 protanopia/deuteranopia），并在图注中说明。
3. **底图退后**：底图用浅色/单色（CartoDB Positron 类），注记与道路只作参照；数据层颜色饱和度须高于底图；交互图须提供底图开关。
4. **四件套齐全**：每幅投稿图必须有图例、比例尺（或比例说明）、指北针（非正北投影时尤甚）、数据来源与投影说明；比例变形要如实标注（如“65°N 处约 1:2,860,000”）。
5. **字体三级**：标题 ≥12 pt、图例/轴注 9–10 pt、脚注（来源）8 pt；同一图内不超过两种字体；中文图须显式指定中文字体（如 Noto Sans CJK SC），不得依赖 matplotlib 默认 DejaVu（中文会成方框，本次实测已验证）。
6. **小屏换设计**：移动端不是等比缩小——按洲/半球拆分、或改用比例圆/cartogram；并设定最小符号尺寸与不重叠约束，达不到就换视图（Schöttler 的约束断点法）。
7. **交互可发现**：每个交互都要有可见入口（滑块、开关、悬停高亮），并说明默认状态；只写“可交互”而无入口的，视为未完成。
8. **复现信息进图注**：图注或方法中写清软件与版本、关键参数（如分级方法、投影、densify 间距）、数据与代码链接（DOI/仓库）；缺失则降级为“示意图”，不作论证图。

### 用期刊规范反向评判实测工具（逐个一句话）

| 工具 | 一句话结论 |
|---|---|
| GeoPandas `.plot` | 默认有图例、无四件套其余三项，版式留白大，需手工补齐后可接近期刊静态图。 |
| GeoPandas `.explore` | 交互探索合格，但出版要素缺失，属“分析图”而非“投稿图”。 |
| Folium | 底图主导、图例靠插件、无打印导出，离期刊静态水准最远，适合探索而非投稿。 |
| leafmap | 浅色底图干净、图层开关齐全，但图例与打印版式需另做，交互接近、出版待打磨。 |
| lonboard | 渲染锐利、性能好，但默认无图例/比例尺/指北针，交互分析接近期刊级，静态投稿需截图后再加工。 |
| pydeck / deck.gl | 默认深色炫酷风与期刊克制风相反，需换浅色底图+自配图例，否则只是“好看的演示”。 |
| Plotly.py | 字体与图例干净、支持无底图分级设色，调好投影与配色后最容易出期刊风格静态图之一。 |
| Datashader | 密度渲染是强项，但无底图、无图例、无标注，默认出图只是“数据底图”，必须叠加地理上下文。 |
| hvPlot | 默认尚体面，瓦片底图+小字图例偏 web 风，投稿需放大字体、另配图例。 |
| Cartopy | 离期刊最近的 Python 静态库之一：投影、海岸线、经纬网原生，缺的是图例与比例尺的手工收尾。 |
| geoplot | 默认分级设色体面、投影正确，但无底图/经纬网、图例无标签，且项目已停滞。 |
| PyGMT | GMT 血统使出版级海岸线/比例尺/指北针原生，补验重渲的 18 号图是本批静态图中四件套最接近齐全的，确认是理论上最接近期刊规范的库。 |
| GeoVista | 3D 球体视觉冲击强，属“封面图”路线，不适合二维专题投稿图；补验装 OSMesa 后已出图（20 号），粗网格条纹与色带标题重叠是收尾问题。 |
| prettymaps / prettymapp | 默认美感按实测出图（19 号）为全场最佳，但无图例/比例尺/数据标注，是“地图艺术”而非“专题论证”（补验已成功渲染巴黎 800 m 真实 OSM 图；pip 安装仍失败，见深挖第 5 节）。 |
| ipyleaflet | 纯交互底图工具，无出版图能力，不参与期刊对标。 |
| MapLibre GL JS | 矢量底图精美、样式可控，期刊级取决于样式设计投入，默认样式只是起点。 |
| Leaflet | 默认标记与配色朴素，需大量样式打磨才接近期刊水准。 |
| OpenLayers | 功能最全、默认样式最“工程”，美学需自定义。 |
| Kepler.gl | 仪表盘默认 UI 最 polished 的交互工具之一，图例/过滤原生，导出静态图后仍需版式收尾。 |
| CesiumJS | 3D 地球电影感，专题投稿图不是它的赛道。 |
| TerriaJS | 目录式数据浏览器，界面工整但偏政府门户风。 |
| GeoLibre | 打印布局功能是亮点，默认 UI 按官网与 README 截图已接近现代期刊/报告风，值得跟踪（未本地构建）。 |
| PMTiles | 瓦片基础设施，不直接出图，不参与美学评判。 |
| Bertin.js | JS 中最“期刊专题图”取向的库（标题/脚注/比例尺/图例原生），但 2023 年后停更。 |
| Observable Plot | 声明式 SVG、Equal Earth 等投影与图例原生，调好字体后最接近期刊静态图。 |
| mapsf（R） | 为期刊专题图而生，图例/比例尺/指北针/分面原生，R 生态内最接近标杆。 |
| map3d | 白模 3D 城市，无专题制图能力，不参与期刊对标。 |
| 3D-Geo-Vis 2 | 七种 3D 专题方法学术性强，属实验性 3D 表达，未见期刊级版式。 |
| MapStore2 | 仪表盘框架默认偏企业 GIS 风，需主题定制。 |


### 5. prettymaps / prettymapp —— 美学导向制图的代表，但安装与许可证是两道坎

- **定位**：prettymaps（marceloprates，2021-03）从 OpenStreetMap 拉取街道/建筑/水体/绿地/等高线，用 matplotlib 画成海报级艺术地图，支持预设（`preset`，如 `default`/`barcelona`）、vsketch 绘图仪模式、圆形裁切与多子图；prettymapp（chrieke）是其 Streamlit 网页版与重写版，PyPI 0.6.0 发布于 2025-12-25。
- **数字**：prettymaps 14,339 stars（本表 Python 静态制图最高）、最近推送 2026-07-30；prettymapp 2,838 stars、最近推送 2026-07-08、PyPI 0.6.0（2025-12-25）。
- **源码实读**：入口为 `prettymaps/draw.py:1106` 的 `plot(query, layers={}, style={}, preset="default", radius=None, save_as=None, mode="matplotlib", multiplot=False, ...)`；图层经 OSMnx 取数（`graph_to_shapely`、`geometries_to_shapely`），另有 `plot_gdf`（:296，接受已有 GeoDataFrame，可绕开联网取数）、`plot_legends`（:427）、`draw_hillshade`（:515）与预设管理（`read_preset`/`presets`）。README 明确：**禁止 NFT 用途，要求保留 OSM 与本仓库署名**。
- **许可证警示**：AGPL-3.0（仓库 LICENSE 文件全文为 GNU AGPL v3；早期博客曾称 CC-BY-NC-4.0，已过时）。AGPL 意味着把 prettymaps 嵌进网络服务要开源衍生代码——与 MIT/BSD 的其它工具不可同日而语，商用选型须先过法务。
- **实测（2026-11-14 补验跑通）**：`pip install prettymaps` 两次失败——第一次构建子进程报错，根因为 setuptools 的 `pkgutil.ImpImporter` 在 Python 3.12 已移除；第二次（`--no-build-isolation`）缺 `mesonpy`。上游打包老化未修，pip 路线至今仍不可行。改走“装运行时依赖 + `PYTHONPATH` 引用已克隆源码”路线后跑通：补验装上 osmnx 2.1.1、vsketch 1.2.0，并按 `requirements.txt` 补齐 opencv-python-headless 5.0.0.93、thefuzz、scikit-learn、scikit-image、elevation、tqdm、rioxarray 0.23.0 后，`from prettymaps.draw import plot, plot_gdf` 导入成功（注：`plot_gdf` 不在包顶层导出，须从 `prettymaps.draw` 引；源码已适配 osmnx 2.x 的 `features_from_polygon` 等 API）。随后 `plot("Paris, France", radius=800, preset="default")` 真实联网取数成功：Nominatim 地理编码 + Overpass 取数耗时 267.57 秒，出图 19（3510×3510，4.0 MB），塞纳河、卢浮宫—杜乐丽一带建筑/绿地/街道分层清晰。`plot_gdf` 读本地 GeoDataFrame 的退路最终未用上（真实取数已跑通）。prettymapp（Streamlit）本次仍未尝试本地运行。
- **期刊标杆对照**：默认出图按 README 示例与口碑为全表最佳（配色、留白、字体层次），但**无图例/比例尺/数据来源标注**，是“地图艺术”而非“专题论证”；想用于投稿须另加四件套。结论：**封面/海报首选，论证图需手工补齐**。

## 验证小结

### 数字总览（核验日 2026-11-14）

| 口径 | 数量 |
|---|---|
| 项目总数 | 30（29 个仓库；pydeck 与 deck.gl 同库） |
| 实际出图 | **20 幅**（7 PNG + 13 HTML），覆盖 **19 个项目** |
| 其中 PNG 目视检查过 | 7 幅（01、05、06、09、18、19、20） |
| 其中 HTML 仅 Node 语法校验、未浏览器截图 | 6 幅 JS 演示（11–16 号中的 Leaflet/MapLibre/OpenLayers/deck.gl/Bertin/Observable Plot） |
| 代码验证通过（无出图） | 1 个（ipyleaflet：Map + GeoJSON 图层对象创建通过） |
| 文档/元数据核查（未本地运行） | 8 个（Kepler.gl、CesiumJS、TerriaJS、GeoLibre、PMTiles、map3d、3D-Geo-Vis 2、MapStore2）+ mapsf（R）+ prettymapp |
| 未跑通 | **0 个**（补验后 PyGMT、prettymaps、GeoVista 三项全部跑通，见下） |
| 克隆完成 | **29 个仓库全部完成**（2.2 GB；第一批 15 个 + MapLibre GL JS + 补验第二批 13 个全部完成，见附录） |

### 出图清单（`geovis/figures/`）

1. `01_geopandas_plot.png`（GeoPandas `.plot`，PNG）
2. `02_geopandas_explore.html`（GeoPandas `.explore`）
3. `03_folium_choropleth.html`（Folium）
4. `04_plotly_choropleth.html`（Plotly.py；PNG 因缺 kaleido 未出）
5. `05_cartopy_robinson.png`（Cartopy，PNG）
6. `06_geoplot_choropleth.png`（geoplot，PNG）
7. `07_lonboard_world.html`（lonboard）
8. `08_pydeck_world.html`（pydeck）
9. `09_datashader_density.png`（Datashader，PNG）
10. `10_leafmap_world.html`（leafmap）
11. `11_leaflet_world.html`（Leaflet，语法校验）
12. `12_maplibre_world.html`（MapLibre GL JS，语法校验）
13. `13_openlayers_world.html`（OpenLayers，语法校验）
14. `14_deckgl_world.html`（deck.gl，语法校验）
15. `15_bertin_world.html`（Bertin.js，语法校验）
16. `16_observable_plot_world.html`（Observable Plot，语法校验）
17. `17_hvplot_world.html`（hvPlot）
18. `18_pygmt_world.png`（PyGMT，补验重渲，1063×651；第二位补验员 2026-11-13 的原图为 1007×3883 异常画布，备份于 `tmpdata/18_pygmt_world_orig_20261113.png`）
19. `19_prettymaps_paris.png`（prettymaps，补验新增，巴黎 800 m 真实 OSM 取数，3510×3510）
20. `20_geovista_world.png`（GeoVista，补验新增，1024×768）

### 曾未跑通的三项与仍未完成（原因逐条，2026-11-14 补验后更新）

- **PyGMT（2026-11-14 补验跑通）**：pip 装的 pygmt 只是封装层，原先 `import pygmt` 报 `GMTCLibNotFoundError: libgmt.so` 缺失。补验发现 apt 缓存中已有第二位补验员下载的 GMT 6.5.0 全套 deb（`gmt`/`gmt-common`/`gmt-dcw`/`gmt-gshhg-high`/`libgmt6t64`/`libgmt-dev` 及其依赖共 72 个包），`dpkg -i /var/cache/apt/archives/*.deb` 一次装齐，`gmt --version` 为 6.5.0，`import pygmt` 通过（0.19.0）。18 号图用正确图幅重渲（1063×651；原 1007×3883 异常画布图已备份）。**结论：PyGMT 在本机已跑通，之前只是缺系统级 GMT 库，不是 pygmt 本身的问题。**
- **prettymaps（2026-11-14 补验跑通，pip 安装仍失败）**：见深挖第 5 节。根本原因仍是上游 `setup.py` 用了 Python 3.12 已移除的 `pkgutil.ImpImporter`，属**上游打包老化**，不是本机问题；但源码导入路线已跑通并出了真实 OSM 图（19 号）。
- **GeoVista（2026-11-14 补验跑通，有残留）**：`pip install geovista` 装上 0.5.3，`gv.Transform.from_1d` 建网格与 `add_coastlines` 均成功。补验过程：`add_base_layer(texture=gv.natural_earth_1())` 仍报 `AttributeError: 'ActiveArrayInfoTuple' object has no attribute '_namedtuple'`（geovista 0.5.3 与 PyVista 0.49.2 不兼容，跳过底图后继续）；`show()` 在 Xvfb 下阻塞于交互窗口等待关闭（4 分钟以上无出图，CPU 约 2%），`screenshot()` 不经 `show()` 则报 `Nothing to screenshot`；`off_screen=True` 在装 EGL（libegl-mesa0 25.2.8）后仍段错误 139，VTK 明确提示 `libOSMesa not found`。**装上 libosmesa6 25.1.7 后离屏渲染一次跑通**，出图 20（1024×768）。残留：`add_base_layer` 的版本不兼容未解（须固定 PyVista 旧版或等 geovista 修复），本次出图无底图纹理。**结论：GeoVista 在本机已跑通，代价是系统级 OSMesa；底图纹理仍是已知缺口。**
- **prettymapp（未尝试本地运行）**：Streamlit 应用，未在本机启动；只做了仓库克隆与元数据核查。
- **mapsf（未运行）**：本机无 R（`which R` 无结果），R 包未安装；只做了仓库克隆与 README/API 核查。
- **JS 重型项目未本地构建**：Kepler.gl、CesiumJS、TerriaJS、GeoLibre、MapStore2、map3d、3D-Geo-Vis 2 未跑 npm 构建（构建链重、共享 VM 资源紧张）；只做了元数据与 release notes 核查。PMTiles 为瓦片格式基础设施，不直接出图。
- **JS 演示未浏览器截图**：本机无 Chromium/Playwright，11–16 号 HTML 仅做 `node --check` 语法校验；HTML 需联网加载 CDN 脚本/瓦片后在浏览器打开查看，渲染效果以代码与官方 demo 为据。
- **第二批克隆已全部完成（2026-11-14 补验）**：Leaflet、OpenLayers、deck.gl、Kepler.gl、CesiumJS、TerriaJS、GeoLibre、PMTiles、Bertin.js、Observable Plot、map3d、3D-Geo-Vis 2、MapStore2 共 13 个仓库逐个 `--depth 1` 克隆完成（另补克隆了第二位补验员留下的空目录 deck-gl）；本地现为 29 个仓库目录、2.2 GB，逐个 `git rev-parse HEAD` 核验通过。**本报告对这些项目的结论仍以 GitHub API 元数据 + README（在线）+ release notes 为据**（克隆只用于存档核查，未据此改写结论）。
- **Plotly PNG 导出**：缺 kaleido（`pip install -U kaleido` 可解，未装），故 04 号只有 HTML；不影响交互验证。
- **apt 权限与中断（补验已解决）**：`apt-get update && apt-get install gmt` 的后台任务最初因系统权限确认而挂起；确认随后获批，但任务在执行中被运行时重启以 SIGTERM 终止，未产生输出。补验时发现：GMT 6.5.0 的 deb 其实已下载在 apt 缓存中，`dpkg -i` 直接装齐；系统级 os-intent replay 进程的 `apt-get update` 也已跑完，apt 源恢复正常，随后 `apt-get install -y libegl-mesa0 libosmesa6` 正常完成。GMT、EGL、OSMesa 现均已安装。

### 实测中踩到的坑（可复用）

1. **matplotlib 中文成方框**：默认 DejaVu 无中文。须 `font_manager.addfont("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc")` 并设 `rcParams["font.family"]="Noto Sans CJK SC"`（第一版 01/05 图已验证此问题，重跑后修复）。
2. **lonboard 0.17 的 pyarrow 可选依赖**：未装 pyarrow 时 `convert_dtypes` 路径报 `NameError: name 'pa' is not defined`；补装 pyarrow 26.0.1 解决。`get_fill_color` 不接受列名，须先用 `lonboard.colormap.apply_continuous_cmap` 算 RGB 数组。
3. **pydeck 的 MultiPolygon**：`row.geometry.to_json()` 对 MultiPolygon 失效，改用 `shapely.geometry.mapping`。
4. **datashader 的 cmap**：`cmap="fire"` 在 0.19.1 不存在，改用自定义色标列表。
5. **hvPlot 需 geoviews**：无 geoviews 时报 `The geoviews package must be installed…`，补装 geoviews 1.16.0 后成功。
6. **numpy 冲突警告**：pip 装 geopandas 后 numpy 升至 2.5.4，与系统 scipy 1.11.4（要求 numpy<1.28）冲突；2D 制图未受影响，但 3D（Axes3D）不可用。
7. **Cartopy 首次运行会联网下载 Natural Earth 数据**（naturalearth.s3.amazonaws.com），离线环境会失败；本次已自动下载 ocean/land（110m）。

## 发现的主要问题（给 orchestrator 的摘要）

1. **“仍被引用但已停更”的项目不少**：Bertin.js（2023-10-23 后无推送，319 stars）与 geoplot（实质提交停于 2023-07-04，API 推送 2024-06-08）仍在教程与论文中出现，选型时须标注停更风险；Bertin 的后继生态在 R（`berti`n 包）与 geotoolbox，不在 JS。
2. **许可证有坑**：prettymaps 是 AGPL-3.0（非早年博客说的 CC-BY-NC），商用/服务化须过法务；MapStore2 与 3D-Geo-Vis 2 **无许可证**（仓库无 LICENSE 文件，API 亦 NOASSERTION/空），后者还是 0 stars 的实验仓库——引用前须先确认授权。
3. **2026 年的新星是 GeoLibre 与 lonboard**：GeoLibre 半年 8.6k stars（API 记录创建于 2026-05-27），lonboard 发版密度最高（0.13→0.17 一年五版），两者都代表“云原生 + DuckDB/GeoArrow + 打印/桌面一体化”的方向；但 GeoLibre 未本地构建，增速与作者既有受众有关，不宜直接等同于生产占有率。
4. **默认出图离期刊水准的距离是系统性的**：19 个出图项目中，**无一默认带齐“图例+比例尺+指北针+数据来源”四件套**；最接近的是 Bertin.js（原生标题/脚注/比例尺/图例）、Observable Plot（投影+图例原生）与补验的 PyGMT 18 号图（标题+色带+经纬网，只缺比例尺/指北针），而渲染性能最好的 lonboard/deck.gl 默认连图例都没有。期刊标杆的 8 条规范（见上节）是后续选型的硬尺子。
5. **PyGMT、prettymaps、GeoVista 的失败都是“环境/打包老化”，不是功能问题——补验已全部跑通**：PyGMT 缺系统 GMT 库（补验装 GMT 6.5.0 后出图）；prettymaps 的 `setup.py` 用了 Python 3.12 已移除的 API（pip 安装至今仍失败，改走源码导入后出了真实 OSM 图）；GeoVista 卡在无头 GL（装 libosmesa6 后离屏渲染跑通）与 geovista/PyVista 版本不兼容（`add_base_layer` 仍失败，是唯一残留）。三者在有对应环境的机器上仍是强项。
6. **JS 类工具的验证天花板是本机无浏览器**：6 幅 JS 演示只做了语法校验，未截图；Kepler.gl 等重型项目未本地构建。结论的可信度分级已在总表与验证小结中逐项标明，不可把“文档核查”读作“实测通过”。
7. **共享 VM 的资源争用是本次最大外部瓶颈**：内存常 <500 MB 可用、网络极慢，第二批 13 个仓库克隆与 3 个后台安装在报告时均未完成；补验（2026-11-14）时网络有所恢复，13 个克隆与全部安装均已完成，但仍很慢（prettymaps 一次 Overpass 取数 268 秒，mapstore2 单个克隆约 9 分钟，cesium 219 MB、mapstore2 392 MB）。

## 附录：文件清单

- 本报告：`geovis/REPORT.md`
- 出图：`geovis/figures/`（20 幅，见验证小结清单）
- 克隆仓库：`geovis/repos/`（**29 个全部完成**，共 2.2 GB，逐个 `git rev-parse HEAD` 核验通过：3d-geo-vis-2、bertin、cartopy、cesium、datashader、deck-gl、folium、geolibre、geopandas、geoplot、geovista、hvplot、ipyleaflet、kepler-gl、leaflet、leafmap、lonboard、map3d、maplibre-gl-js、mapsf、mapstore2、observable-plot、openlayers、plotly-py、pmtiles、prettymapp、prettymaps、pygmt、terriajs；第二批 13 个于 2026-11-14 补验完成，其中最大的是 mapstore2 392 MB、cesium 219 MB、deck-gl 171 MB）
- 实测环境：`geovis/venv/`（Python 3.12，见文首版本清单）；系统级 GMT 6.5.0、libegl-mesa0 25.2.8、libosmesa6 25.1.7
- 渲染脚本（/tmp，临时）：`/tmp/geovis_render1.py`、`/tmp/geovis_render2.py`、`/tmp/geovis_render3.py`、`/tmp/geovis_js_demos.py`、`/tmp/geovis_geovista.py` 与 `/tmp/geovis_geovista2.py`（GeoVista 离屏渲染尝试，均未出图）
- 补验渲染脚本（`geovis/tmpdata/`，持久）：`geovis_pygmt_rerun.py`（18 号重渲）、`geovis_prettymaps_run.py`（19 号巴黎 OSM 图）、`geovis_geovista_rerun.py` / `geovis_geovista_rerun2.py` / `geovis_geovista_rerun3.py` / `geovis_geovista_rerun4.py`（GeoVista 四次尝试，前三次未出图，第四次装 OSMesa 后出图 20 号；日志 `geovista_run*.log`、克隆日志 `clone_log_20261114.txt`、`prettymaps_run.log` 同目录）；18 号原图备份 `tmpdata/18_pygmt_world_orig_20261113.png`
- 元数据快照（/tmp，临时）：`/tmp/geovis_meta.json`（GitHub API，2026-11-14）
- 期刊抽样笔记（/tmp，临时）：`/tmp/journal_notes.md`、`/tmp/reverse_eval_draft.md`（反向评判草稿，已按实测核对后写入本报告）


## 补验说明（2026-11-14）

本次补验由第三位补验研究员执行，接手时状态：报告 51,149 字节、30 个项目、17 幅出图，内容完整；`repos/` 19 个目录、`figures/` 18 幅；GMT 未装，osmnx/vsketch 未装。以下为补验结果（全部在已获授权的验证范围内，不花钱、不注册、不提交表单）。

### 盘点纠正

- 接手时 `repos/` 实为 19 个目录，但其中 `deck-gl` 为空目录（`git log` 报 `No commits yet`，系第二位补验员克隆中途被重启中断所致），有效仓库 18 个；相对报告附录的 16 个名单，实际新增只有 Leaflet、OpenLayers、deck-gl（空）3 个，并非任务简述中的 4 个。
- 接手时 `figures/` 18 幅，新增的 18 号 `18_pygmt_world.png`（2026-11-13 23:42，第二位补验员留下）确为真实 PyGMT 出图（标题注明 PyGMT 0.19.0 / GMT 6.5.0），但画布为 1007×3883 的异常高幅，地图只占顶部约四分之一，右上角有杂散圆圈；本次已重渲并备份原图（见下）。

### 三项重试结果

- **PyGMT ✅ 跑通**：apt 缓存中已有第二位补验员下载的 GMT 6.5.0 全套 deb（72 个包），`dpkg -i /var/cache/apt/archives/*.deb` 一次装齐，`gmt --version` 6.5.0，`import pygmt`（0.19.0）通过；18 号图重渲为 1063×651（Robinson 投影、viridis、色带、经纬网），目视检查通过。原 1007×3883 图备份于 `tmpdata/18_pygmt_world_orig_20261113.png`。
- **prettymaps ✅ 跑通**：`pip install osmnx vsketch` 成功（osmnx 2.1.1、vsketch 1.2.0，TMPDIR 指到 workspace 下），再按 `requirements.txt` 补齐 opencv-python-headless 5.0.0.93、thefuzz、scikit-learn、scikit-image、elevation、tqdm、rioxarray 0.23.0 后，`PYTHONPATH=repos/prettymaps` 源码导入成功；`plot("Paris, France", radius=800, preset="default")` 真实联网取数 267.57 秒，出图 19（3510×3510，4.0 MB），目视检查通过。pip 安装本身仍失败（上游 `setup.py` 的 `pkgutil.ImpImporter` 问题未修）。
- **GeoVista ✅ 跑通（有残留）**：网格与海岸线构建均成功；`add_base_layer(texture=...)` 仍报 `AttributeError: 'ActiveArrayInfoTuple' object has no attribute '_namedtuple'`（geovista 0.5.3 与 PyVista 0.49.2 不兼容）；`show()` 在 Xvfb 下阻塞于交互窗口（300 秒与 900 秒两次尝试均无出图），`screenshot()` 不经 `show()` 则报错；装 libegl-mesa0 后离屏仍段错误 139（VTK 提示 `libOSMesa not found`）；**装上 libosmesa6 25.1.7 后离屏渲染一次跑通**，出图 20（1024×768，3D 球体 + 海岸线 + 色带），目视检查通过。残留：`add_base_layer` 的版本不兼容未解，本次出图无底图纹理。

### 新增克隆

- 第二批 13 个仓库全部逐个 `--depth 1` 克隆完成（deck-gl 重克隆 171 MB；bertin 43 MB、pmtiles 25 MB、map3d 2.6 MB、3D-Geo-Vis 2 41 MB、observable-plot 121 MB、kepler-gl 41 MB、cesium 219 MB、terriajs 100 MB、geolibre 89 MB、mapstore2 392 MB；另 Leaflet、OpenLayers 为第二位补验员已克隆）。本地现为 **29 个仓库目录、共 2.2 GB**，逐个 `git rev-parse HEAD` 核验通过，覆盖 30 个项目对应的全部 29 个仓库（pydeck 与 deck.gl 同库）。

### 新增出图

- 新增 2 幅：19 号 prettymaps 巴黎图、20 号 GeoVista 球体图；18 号 PyGMT 图重渲（不计新增）。出图总数 **17 → 20 幅**（7 PNG + 13 HTML），覆盖项目 **16 → 19 个**；未跑通项目 **3 → 0 个**。

### 报告修正点

- 仓库计数改为磁盘实际数：29 个目录全部完成（原“16 个完成、其余 13 个未新增”已作废）。
- PyGMT / prettymaps / GeoVista 三个条目的验证状态由 ❌ 改为 ✅，并更新深挖第 5 节、逐图美学评价（新增 18/19/20 号评价）、期刊反向评判三行、数字总览、出图清单、附录。
- Bertin.js 仓库地址由 `neocarto/bertin` 改为 **`riatelab/bertin`**：GitHub API 核实新地址 319 stars、最近推送 2023-10-23T13:26:50Z、MIT，旧地址返回 `Moved Permanently`；stars 与推送时间与原记录一致。

### 仍未完成项及原因

- **prettymaps 的 pip 安装**：上游 `setup.py` 仍用 Python 3.12 已移除的 `pkgutil.ImpImporter`，`pip install prettymaps` 不可行，只能源码导入；须等上游修打包。
- **GeoVista 的 `add_base_layer` 底图纹理**：geovista 0.5.3 与 PyVista 0.49.2 的 `ActiveArrayInfoTuple._namedtuple` 不兼容未解；退路是固定 PyVista 旧版或等 geovista 修复，本次未再降级重装（避免破坏已跑通的环境）。
- **JS 演示仍无浏览器截图**：本机无 Chromium/Playwright，11–16 号 HTML 仍只有 Node 语法校验；Kepler.gl、CesiumJS、TerriaJS、GeoLibre、MapStore2、map3d、3D-Geo-Vis 2 仍未本地构建（构建链重，超出本次补验范围）；Plotly PNG 导出仍缺 kaleido；prettymapp、mapsf（R）仍未本地运行。
