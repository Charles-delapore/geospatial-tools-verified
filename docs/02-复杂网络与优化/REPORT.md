# 复杂网络及其优化（Complex Networks）——开源项目调研报告

**领域一 · 地理开源调研** | 核验日期：**2026-11-14** | 报告语言：中文

> 本报告覆盖网络构建、社区发现、中心性、网络优化与韧性、时空网络、图分析库、网络可视化六个子域，共 **28 个项目**，其中 **17 个通过实测**（见第 6 节）。所有星数、提交时间、版本号均为 2026-11-13/14 的快照，查不到的写“未查到”，不编造。

---

## 1. 概述与方法

### 1.1 检索与核验方法

- **检索**：公开 web 检索 + GitHub API（stars、`pushed_at`）+ PyPI JSON API + npm registry 交叉核验。先定 28 个项目清单，兼顾经典旗舰与近两年新活跃项目。
- **拉代码验证**：27 个仓库 `git clone --depth 1` 到 `repos/`（community_TAU 的 GitHub 仓库不可达，未能克隆，见 7.2）。克隆前先读 README 与关键代码，不盲目执行陌生脚本。
- **实测**：两个 Python venv（`venv-test/` 带系统包、`venv2/` 隔离环境），以 Zachary 空手道俱乐部图（34 节点 / 78 边）为统一基准做中心性、社区发现等对照测试；OSMnx、WNTR、pandana/pandarm 用自建小数据离线测试；JS/Java 工具因需 npm/Java 环境，改为源码与文档核查。
- **期刊标杆**：抽样 Nature Communications（4 篇）、Network Science（3 篇）、Applied Network Science（4 篇）共 11 篇 2024–2026 年文章，记录方法节技术栈与图幅组织（见第 5 节）。

### 1.2 重要口径说明

- **星数**：GitHub API 快照（2026-11-14）。`igraph` 取 python-igraph 仓库（1,465）；C 核心在 igraph/igraph 另有仓库，未计入。graph-tool 托管于自有 Git（git.skewed.de），无 GitHub 星数；community_TAU 仓库不可达，星数未查到。
- **最近更新**：总表用 GitHub API `pushed_at`（全仓库任意分支最新推送）；克隆到的默认分支 HEAD 日期往往早于它（例如 pathpyG：API 2026-11-06 vs HEAD 2026-07-09），差异源于向非默认分支的推送，报告中两种口径并列。
- **许可证**：以仓库内 LICENSE/COPYING 文件实测为准，API 的 `NOASSERTION` 处已用文件核对（见总表备注）。
- **“未查到”**：凡写“未查到”，指本次检索与抽样中未找到可信来源，不等于不存在。

### 1.3 一句话结论

- **图分析通用库**：NetworkX 仍是事实标准；igraph 1.0（2025-10-23）与 rustworkx 是高性能替代；NetworKit 适合大规模并行。
- **社区发现**：Leiden/Infomap/Louvain 三足鼎立；TAU（遗传算法 + Louvain/Leiden）是 2024–2026 年出现的新选手，但仓库链接已失效，需谨慎。
- **时空与高阶网络**：NetworkX-Temporal（2025 年 SoftwareX 发表）与 XGI（超图）、Reticula、pathpyG 是近两年最活跃的新方向，但后两者规模小、生态尚浅。
- **空间网络**：OSMnx 是街道网络事实标准；Pandana 原版 0.8（2026-08-24）已可在 NumPy 2 下运行，pandarm 仍是更稳妥的 fork。
- **可视化**：桌面用 Gephi 0.11.4、浏览器用 Gephi Lite（基于 sigma.js）；sigma.js / Cytoscape.js / vis-network 三者分工明确。
- **顶刊标杆**：11 篇抽样中明确点名的清单内工具只有 igraph（R）与 NetworkX（Python 2.6.3 旧版）；多数理论/方法论文自带代码存档而不依赖通用图库（见第 5 节）。

---

## 2. 项目总表（28 个）

星数与最近更新为 2026-11-14 快照；最新发版为 PyPI / npm / GitHub Releases 核验值。

| # | 项目 | 仓库 | 许可证 | Stars | 最近更新（API） | 最新发版 | 用途一句话 | 验证状态 |
|---|---|---|---|---|---|---|---|---|
| 1 | NetworkX | networkx/networkx | BSD-3-Clause | 17,392 | 2026-11-12 | 3.7（2026-09-21） | Python 图分析事实标准：建图、算法、中心性、社区、绘图 | ✅ 通过（3.7） |
| 2 | igraph（python-igraph） | igraph/python-igraph | GPL-2.0 | 1,465 | 2026-11-03 | 1.0.0（2025-10-23） | C 核心的高性能图库，Python/R/Mathematica 接口 | ✅ 通过（1.0.0） |
| 3 | graph-tool | git.skewed.de/count0/graph-tool.git | LGPL-3.0 | 未查到（非 GitHub 托管） | 2026-11-11（HEAD） | 未查到（滚动发布，conda/Debian） | C++/Boost 大规模图分析与统计推断（SBM） | ⚠️ 未实测（需编译 C++ 核心） |
| 4 | NetworKit | networkit/networkit | MIT | 886 | 2026-11-11 | 11.3（2026-11-06） | 并行大规模网络分析（中心性、社区、图生成） | ✅ 通过（11.3） |
| 5 | rustworkx | Qiskit/rustworkx | Apache-2.0 | 1,780 | 2026-11-12 | 0.18.1（2026-07-30） | Rust 核心的高速图库，Qiskit 生态，NetworkX 兼容 API | ✅ 通过（0.18.1） |
| 6 | graspologic | graspologic-org/graspologic | MIT | 1,021 | 2026-06-18 | 3.4.4（2025-09-08） | 统计图分析：谱嵌入、图匹配、聚类（源自微软研究院 graspologic） | ✅ 通过（3.4.4） |
| 7 | scikit-network | sknetwork-team/scikit-network | BSD | 633 | 2026-11-03 | 0.33.5（2025-11-19） | scikit-learn 风格的图机器学习：聚类、嵌入、分类 | ✅ 通过（实装 0.33.0） |
| 8 | CDlib | GiulioRossetti/cdlib | BSD-2-Clause | 430 | 2026-08-16 | 0.4.1（2026-07-25） | 社区发现算法大一统接口（数十种算法 + 评估） | ✅ 通过（0.4.1） |
| 9 | leidenalg | vtraag/leidenalg | GPL-3.0 | 804 | 2026-11-02 | 0.12.0（2026-05-24） | Leiden 社区发现算法（igraph 配套，优于 Louvain） | ✅ 通过（0.12.0） |
| 10 | Infomap | mapequation/infomap | GPL-3.0 | 492 | 2026-11-11 | 2.16.0（2026-10-27） | 基于信息流（map equation）的多层社区发现 | ✅ 通过（2.16.0） |
| 11 | cuGraph | rapidsai/cugraph | Apache-2.0 | 2,259 | 2026-11-13 | cugraph-cu12 26.10.0（2026-10-08） | NVIDIA RAPIDS 的 GPU 图分析，兼容 NetworkX API（nx-cugraph） | ⚠️ 未实测（需 NVIDIA GPU + CUDA/RAPIDS） |
| 12 | PyTorch Geometric | pyg-team/pytorch_geometric | MIT | 24,142 | 2026-11-06 | 2.8.1（2026-10-12） | 图神经网络标准库（GNN、图学习） | ⚠️ 未实测（需 PyTorch，体积大） |
| 13 | EasyGraph | easy-graph/Easy-Graph | BSD-3-Clause | 484 | 2026-10-12 | 1.6.3（2026-10-12） | 复旦 DataNET 的图分析库，含超图、GPU 与 GNN 模块 | ✅ 通过（1.6.3，基础图功能；见备注） |
| 14 | GRAPE | AnacletoLAB/grape | MIT | 644 | 2024-02-24 | PyPI grape 0.2.5（2025-09-28，与仓库提交不一致，见 7.3） | 大规模图嵌入与图机器学习 | ⚠️ 未实测（仓库已停滞 2 年以上） |
| 15 | NetworkX-Temporal | nelsonaloysio/networkx-temporal | BSD-3-Clause | 20 | 2026-11-13 | 1.4.5（2026-11-09） | NetworkX 的时序网络扩展：切片、快照、时序指标与绘图 | ✅ 通过（1.4.5） |
| 16 | Reticula | reticula-network/reticula | MIT | 26 | 2025-10-01 | PyPI reticula 0.13.0（2024-11-14，Python 绑定） | C++ 静态/时序/超图网络分析（Python 绑定） | ⚠️ 未实测（需编译 C++ 核心） |
| 17 | XGI | xgi-org/xgi | BSD-3-Clause | 263 | 2026-11-13 | 1.1（2026-11-13） | 高阶网络：超图与单纯复形分析 | ✅ 通过（1.1） |
| 18 | pathpyG | pathpy/pathpyG | AGPL-3.0 | 62 | 2026-11-06 | 未查到（无 PyPI） | GPU 加速的时序网络高阶 De Bruijn 图模型 | ⚠️ 未实测（需 torch + torch-geometric） |
| 19 | community_TAU（TAU） | PyPI 称 github.com/HillelCharbit/community_TAU，但 2026-11-14 实测不可达 | MIT（PyPI 标注） | 未查到（仓库不可达） | 未查到 | PyPI tau-community-detection 1.4.7（2026-07-14） | 遗传算法 + Louvain/Leiden 的社区发现（特拉维夫大学） | ✅ 通过（PyPI 1.4.7；仓库不可达，见 7.2） |
| 20 | OSMnx | gboeing/osmnx | MIT | 5,899 | 2026-11-07 | 2.1.1（2026-07-21） | 从 OpenStreetMap 下载、建模、分析街道网络 | ✅ 通过（2.1.1，离线 XML） |
| 21 | Pandana | UDST/pandana | AGPL-3.0 | 432 | 2026-10-01 | 0.8（2026-08-24） | 街道网络可达性分析（聚合、POI、等时线） | ✅ 通过（0.8，NumPy 2 下可用，见 7.4） |
| 22 | pandarm | oturns/pandarm | AGPL-3.0 | 25 | 2026-10-23 | 0.0.7.post1（2026-10-23） | Pandana 的友好 fork，修复 NumPy 2.0 兼容 | ✅ 通过（0.0.7.post1） |
| 23 | WNTR | USEPA/WNTR | BSD（Revised BSD） | 476 | 2026-11-11 | 1.5.0（2026-07-01） | 美国环保署的供水管网建模、模拟与韧性分析 | ✅ 通过（1.5.0） |
| 24 | Gephi | gephi/gephi | GPL-3.0 / CDDL-1.0 双许可 | 6,704 | 2026-11-08 | 0.11.4（2026-11-01） | 桌面网络可视化与探索事实标准 | ⚠️ 未实测（本机无 Java 环境） |
| 25 | Gephi Lite | gephi/gephi-lite | GPL-3.0 | 358 | 2026-11-06 | v1.1.1（2026-11-06） | 浏览器版 Gephi（免安装，约 1 万节点/2 万边上限） | ⚠️ 未实测（Web 应用，仅文档/源码核查） |
| 26 | sigma.js | jacomyal/sigma.js | MIT | 12,240 | 2026-11-10 | npm 4.0.6 | WebGL 大规模网络图渲染（Gephi Lite 底层） | ⚠️ 未实测（未装 npm 依赖，仅源码核查） |
| 27 | Cytoscape.js | cytoscape/cytoscape.js | MIT | 11,289 | 2026-11-10 | npm 3.35.0 | 浏览器图论可视化与分析库 | ⚠️ 未实测（未装 npm 依赖，仅源码核查） |
| 28 | vis-network | visjs/vis-network | Apache-2.0 | 3,641 | 2026-11-13 | npm 10.1.5 | 浏览器交互网络图（vis.js 生态） | ⚠️ 未实测（未装 npm 依赖，仅源码核查） |

**表注：**
- Gephi 的仓库 COPYING.txt 写明双许可 CDDL 1.0 + GPL；GitHub API 仅标注 GPL-3.0。
- graph-tool 的仓库 COPYING 为 GPL-3.0 文本，但另有 COPYING.LESSER，README 明确为 LGPL v3；以 LGPL-3.0 为准。
- EasyGraph 实测为 `--no-deps` 安装 + 补装 fastjsonschema、tqdm 后的基础图功能；官方全量依赖含 PyTorch（README 要求 1.12.1 ≤ torch < 2.0）与 numpy<2，本次未全量安装（见 6.3）。
- scikit-network：PyPI 最新 0.33.5，但 pip 在本环境解析为 0.33.0；实测版本以 0.33.0 为准。

![各项目 GitHub 星数（2026-11-14 快照，对数轴）](figures/stars-2026-11-14.png)

> 图 1：28 个项目中 26 个有 GitHub 星数的分布（graph-tool 与 TAU 无星数，未入图）。PyTorch Geometric 与 NetworkX 断层领先；可视化库 sigma.js、Cytoscape.js 紧随其后；时序/高阶新项目（NetworkX-Temporal 20、Reticula 26、pandarm 25）星数仍很小。

---

## 3. 分域小结

### 3.1 图分析库（通用）

NetworkX、igraph、graph-tool、NetworKit、rustworkx、graspologic、scikit-network、EasyGraph 共 8 个。分层清晰：**NetworkX** 是教学与原型事实标准；**igraph 1.0**（C 核心约 1,100 个用户函数，PLOS ONE 2026 论文称月下载超百万）与 **rustworkx**（Rust 核心）是性能路线；**NetworKit**（KIT）面向超大规模并行；**graspologic** 专精谱方法与统计推断；**scikit-network** 把图算法装进 scikit-learn 接口；**EasyGraph** 是国内（复旦 DataNET）的新生力量，2025-09-29 官方称达 90 万下载，但全量依赖较重且要求 numpy<2、torch<2.0，版本约束偏旧。

### 3.2 社区发现

CDlib（大一统接口）、leidenalg（Leiden）、Infomap（map equation）、community_TAU（遗传算法）共 4 个。Leiden 已取代 Louvain 成为默认推荐（修复了 Louvain 的断连社区问题）；Infomap 在有向/多层网络上仍有独特优势；CDlib 适合算法横评，一次调用可跑数十种方法；TAU 是 2024–2026 年的新算法，Karate 图上 4 社区、模块度 0.4449，效果与 Leiden 相当，但仓库链接失效是硬伤。

### 3.3 中心性、网络优化与韧性

本域无独立单功能库，能力分散在通用库与行业库中：中心性（betweenness、PageRank）由 NetworkX / igraph / NetworKit / rustworkx 覆盖，实测四库在 Karate 图上结果一致（节点 0、33、32 居前）；**cuGraph** 提供 GPU 加速（NVIDIA 博客称 GPU Leiden 比 CPU 快可达 47 倍，H100 + NetworkX 3.5 + cugraph 25.10），但需 GPU；**WNTR** 是供水管网韧性分析的行业标准（美国环保署），Net1 案例实测通过；**GRAPE** 曾是图嵌入方向的活跃项目，但仓库已停滞 2 年以上，不推荐新项目采用。

### 3.4 时空网络与高阶网络

NetworkX-Temporal、Reticula、XGI、pathpyG 共 4 个，是近两年最活跃的新方向：**NetworkX-Temporal** 2025 年发表于 SoftwareX（DOI 10.1016/j.softx.2025.102277），1.4.5 刚于 2026-11-09 发布，切片/快照 API 简单；**XGI** 是超图与单纯复形的标准库（JOSS 论文 DOI 10.21105/joss.05162，另有 XGI-DATA 数据集仓），1.1 于 2026-11-13 发布；**Reticula**（C++，SoftwareX 论文）覆盖静态+时序+超图，但星数仅 26，生态尚浅；**pathpyG** 是 pathpy 的 GPU 继任者（ETH Zürich 等），需 torch + torch-geometric，门槛高。另有极新极小项目 temporal-networks（1 star，2026-10-28 发布 0.1.0）与 STM-Graph（5 stars，CIKM '25 论文），未列入正表，仅作動向注记。

### 3.5 空间网络

OSMnx、Pandana、pandarm、WNTR 共 4 个。**OSMnx** 是街道网络事实标准（Boeing 2025, *Geographical Analysis* 57(4):567–577, DOI 10.1111/gean.70009），可下载步行/驾车/骑行网络及 POI、建筑、海拔、路向、速度/通行时间；**Pandana** 是 UrbanSim 生态的可达性分析库；**pandarm** 是其 NumPy 2 兼容 fork；**WNTR** 面向供水管网。空间网络是本领域与地理研究结合最紧的一域。

### 3.6 网络可视化

Gephi、Gephi Lite、sigma.js、Cytoscape.js、vis-network 共 5 个。**Gephi** 0.11 于 2026-05-05 重大性能升级，0.11.4 于 2026-11-01 发布；**Gephi Lite** v1.0 于 2025-10-08 发布（浏览器免安装，上限约 1 万节点/2 万边），v1.1 于 2026-10-06 发布（MapLibre 地图底图、后台布局、改进调色板），底层基于 sigma.js；**sigma.js**（WebGL 渲染，大规模）、**Cytoscape.js**（图论分析 + 可视化一体）、**vis-network**（轻量交互）三者按规模与分析需求分工。Python 侧绘图仍以 NetworkX + matplotlib 为主，出版级图需按第 5 节规范手工打磨。

---

## 4. 重点项目深挖（5 个）

### 4.1 NetworkX 3.7 —— 通用图分析的事实标准

- **定位**：Python 图分析的默认选择；算法最全、文档最完善、与 pandas / NumPy / SciPy / matplotlib 生态无缝衔接。
- **实测**（venv-test，3.7）：Karate Club 图 34 节点 / 78 边；betweenness 前三为节点 0（0.4376）、33（0.3041）、32（0.1452）；Louvain 社区规模 [6, 10, 4, 14]；平均聚类系数 0.5706；连通分量 1。结果与 igraph、NetworKit、rustworkx 交叉一致。
- **采用者**：未逐一核查具体机构；作为 Python 生态的默认图库，被绝大多数图分析教程、论文复现代码与下游库（OSMnx、CDlib、graspologic 等）依赖。
- **局限**：纯 Python 实现，大规模图（百万边以上）性能明显弱于 igraph / NetworKit / rustworkx；3.x 要求 Python 3.10+。
- **安装难度**：低，`pip install networkx` 即可。

![Karate 图 Louvain 社区划分（NetworkX 3.7 实测，spring 布局，seed=42）](figures/karate-louvain-networkx.png)

> 图 2：实测输出。4 个社区分别着色，节点编号标注。注意：同一算法在不同库中划分略有差异（igraph+Leiden 得 [5,6,11,12]，Infomap 得 [5,11,18]），比较研究应固定算法与随机种子并报告模块度。

### 4.2 igraph 1.0.0 + leidenalg 0.12.0 —— 高性能与社区发现的黄金组合

- **定位**：C 核心的高性能图库（Python/R/Mathematica 三接口），1.0.0 于 2025-10-23 发布；配套 leidenalg 提供 Leiden 算法。
- **实测**（venv-test）：igraph 1.0.0：Zachary 图 34/78，betweenness（未归一化）前三 0（231.07）、33（160.55）、32（76.69），与 NetworkX 归一化值成比例一致；leidenalg：Leiden Modularity 分区 4 个社区，规模 [5, 6, 11, 12]，模块度 0.4198。
- **学术背书**：igraph 1.0 论文发表于 PLOS ONE 2026（Antonov et al., DOI 10.1371/journal.pone.0355108），称月下载超百万；顶刊抽样中，igraph（R 包 2.1.4）是唯一被 Nature Communications 方法节明确点名的清单内工具（见 5.2）。
- **局限**：GPL-2.0 许可证对商业闭源集成有限制；API 风格较 NetworkX 底层，学习曲线稍陡。
- **安装难度**：低，`pip install igraph leidenalg` 有预编译 wheel。

### 4.3 Infomap 2.16.0 —— 信息流社区发现

- **定位**：基于 map equation（信息论压缩）的社区发现，擅长有向网络与多层网络；mapequation 团队维护。
- **实测**（venv-test）：`infomap.find_communities(karate, seed=123, num_trials=5)` 得 3 个社区，规模 [5, 11, 18]——与 Louvain/Leiden 的 4 社区不同，体现了算法假设的差异（信息流 vs 模块度），不是错误。
- **采用者**：未查到具体机构名单；算法本身是网络科学经典方法，被大量论文引用。
- **安装难度**：低，`pip install infomap` 有 wheel；2.16.0 于 2026-10-27 发布（PyPI 旧页曾显示 2.12.0，注意区分）。

### 4.4 OSMnx 2.1.1 —— 空间网络的事实标准

- **定位**：从 OpenStreetMap 下载、建模、分析、绘图街道网络；支持步行/驾车/骑行网络、POI、建筑、公交站、海拔、路向、速度/通行时间与路径规划。
- **实测**（venv2，离线）：手写 3 节点 OSM XML（一条 residential 道路），`ox.graph_from_xml` 解析得 3 节点 / 4 有向边，CRS epsg:4326；`simplify=True` 后合并为 2 节点 / 2 边，边长 122.2 m；`to_graph` 等核心路径正常。另发现：`ox.stats.basic_stats` 在此 3 节点退化玩具图上报错 `ValueError: max() iterable argument is empty`（`streets_per_node_counts` 为空），属小图边界情况，未在真实路网复现，记为“核心通过、统计函数小图异常”。
- **学术背书**：Boeing 2025, *Geographical Analysis* 57(4):567–577, DOI 10.1111/gean.70009。
- **安装难度**：中，依赖 geopandas / shapely / pyproj 等地理栈，`pip install osmnx` 可装，但体积较大；在线下载需访问 OSM 服务，本次实测全程离线。

### 4.5 NetworkX-Temporal 1.4.5 —— 时序网络的新兴标准件

- **定位**：NetworkX 的时序网络扩展：时序图对象、按时间属性切片、快照序列、时序指标与绘图。2025 年发表于 SoftwareX（DOI 10.1016/j.softx.2025.102277）。
- **实测**（venv2，1.4.5）：示例时序图 6 节点 / 8 边，切片得 4 个快照，节点数 [1, 1, 3, 3]；`pip install 'networkx-temporal[draw]'`，依赖 networkx>=2.1、numpy、pandas、scipy。
- **局限**：星数仅 20，生态刚起步；功能聚焦切片与快照，深度时序模型（如 pathpyG 的高阶 De Bruijn）不在其范围。
- **安装难度**：低。

---

## 5. 期刊标杆

### 5.1 抽样说明

- **期刊**：Nature Communications（4 篇）、Network Science（Cambridge，3 篇）、Applied Network Science（Springer，全 OA，4 篇），共 11 篇 2024–2026 年文章。
- **方法**：公开 web 检索 + 全文页面读取（Nature Communications 与 Springer 全文可读；Network Science 多篇仅见 Cambridge 摘要/PDF 片段，部分信息记“未查到”）。只记录方法与风格层面的观察，不复制原文大段文字与图片。
- **口径**：“未点名”指在已读正文与方法节中未出现通用库名称，不等于作者未使用。

### 5.2 抽样文章一览（11 篇）

| # | 期刊 | 文章（标题 / DOI） | 方法节提到的技术栈 | 代码/数据公开 |
|---|---|---|---|---|
| 1 | Nat Commun 2024 | Kojaku et al., Network community detection via neural embeddings. 15, 9446. DOI 10.1038/s41467-024-52355-w | node2vec / DeepWalk / LINE + K-means + 信念传播（BP）+ 随机块模型（SBM）；通用图库未点名 | 数据 Figshare 10.6084/m9.figshare.26808775；代码 Zenodo 10.5281/zenodo.13362073（另有 GitHub 最新版） |
| 2 | Nat Commun 2026 | Randhawa et al., The changing surface of the world's roads. 17, 9345. DOI 10.1038/s41467-026-76234-8 | PlanetScope 3–4 m 影像 + 深度学习，全球 920 万公里主干路网；OSM 仅作对照数据源（表面标签覆盖仅 30–40%，准确率 64.7% vs 模型 89.2%）；通用图库未点名 | 在已读全文提取中未见独立 Data/Code availability 小节，未查到 |
| 3 | Nat Commun 2026 | Multiple local PfDHFR I164L haplotype expansions drive *Plasmodium falciparum* antifolate resistance in Uganda. 17, 9552. DOI 10.1038/s41467-026-76826-4 | **igraph R 包 2.1.4** 做 IBD 网络社区检测，阈值 IBD ≥ 0.9 / ≥ 0.5，算规模、平均度/强度、内外边数、内部边密度 | 数据 NCBI SRA（PRJNA880926 等）；代码 github.com/victorasua/Antifolate_Resistance_Evolution |
| 4 | Nat Commun 2026（在压） | Vestergaard et al., Multimodal analysis disentangles the genetic and microbial associations between inflammatory bowel disease and other immune-mediated diseases. DOI 10.1038/s41467-026-68564-4 | **Python networkx v2.6.3**（连通家系数量与规模、有向无环图、最低共同祖先与最短路径）与 pyAGH v0.3.3（亲缘系数） | 未查到 |
| 5 | Network Science 2025 | Lubold et al., Spectral goodness-of-fit tests for complete and partial network data. 13, e11. DOI 10.1017/nws.2025.10005 | 随机矩阵理论谱拟合优度检验（SBM/潜空间模型）；R 包 latentnet 与 ergm | 代码链接未查到 |
| 6 | Network Science 2025 | Angst et al., Automated extraction of discourse networks from large volumes of media data. 13, e4. DOI 10.1017/nws.2025.4 | 话语网络建模为组织–信念二分图；NER + 实体链接 + 有监督文本分类 + 大语言模型立场检测；通用图库未查到 | 未查到 |
| 7 | Network Science 2025 | Gwee et al., Model-based clustering for network data via a latent shrinkage position cluster model. 13, e19. DOI 10.1017/nws.2025.10014 | 潜收缩位置聚类模型（LSPCM），贝叶斯非参数收缩先验；R 代码，lspm GitLab 仓库；应用于两个真实 Twitter 网络 | 代码在 GitLab（lspm） |
| 8 | Appl Netw Sci 2025 | Janca et al., Augmented visualization of class–cluster match in patient similarity networks. 10:52. DOI 10.1007/s41109-025-00741-8 | LRNet 构建患者相似网络 + Louvain 社区检测；提出 rMCC 与 Connection Purity（cPurity）评估簇–类匹配；全文 13 幅图 | 代码独立声明未查到 |
| 9 | Appl Netw Sci 2025 | Fushimi & Koike, Iterative finetuning … based on proximity segmentation for image geolocalization. 10:40. DOI 10.1007/s41109-025-00734-7 | Delaunay 三角剖分 / Gabriel 图 / 相对邻域图构建邻近图，边权为 ViT 图像特征余弦相似度，Louvain 划分作地理聚类标签 + ViT 微调迭代；实现库未查到 | 未查到 |
| 10 | Appl Netw Sci 2025 | ARLClustering: an R package for community detection in social networks based on user interaction and association rule learning. DOI 10.1007/s41109-025-00715-w | R 4.1.2，关联规则学习（Apriori）做社区检测，对标 Louvain、标签传播、谱聚类；CRAN + GitHub 开源；七个基准网络（Karate Club、Dolphins、Les Misérables、Word-adjacency、Facebook-Friends、NetScience、Facebook L1 Organization）；图 6 幅以上 | CRAN + GitHub 开源 |
| 11 | Appl Netw Sci 2025 | Cakmak & Agarwal, Influence of symbolic content on recommendation bias: YouTube's algorithm during Taiwan's 2024 election. 10:23. DOI 10.1007/s41109-025-00713-y | YouTube 推荐网络（15,600 视频），社区检测揭示符号内容促进的群组形成；软件栈未查到 | 未查到 |

### 5.3 顶刊实际在用的技术栈

- **明确采用的清单内工具（本抽样）**：只有 **igraph（R 包 2.1.4，第 3 篇）**与 **NetworkX（Python v2.6.3，第 4 篇）**。注意 NetworkX 被点名的是 2021 年的 2.6.3 旧版——顶刊作者倾向用稳定旧版，而非追新。
- **被反复点名但常不指明实现库的算法**：**Louvain**（第 8、9、10 篇均点名）是社区发现的默认算法；SBM、谱方法、标签传播亦然。工具选型时“算法名”比“库名”更常出现在方法节。
- **R 生态占显著地位**：Network Science 与应用统计类工作中，igraph、latentnet、ergm、lspm 等 R 包是主流；Python 生态以 NetworkX 为代表。
- **多数理论/方法论文自带代码**：Zenodo / GitLab / GitHub 存档是常态（第 1、3、7、10 篇），而不依赖通用图库；图分析库更多出现在应用型与数据型论文的方法节。
- **本抽样中未被点名的清单内工具**：OSMnx、Gephi、cdlib、leidenalg、NetworKit、rustworkx、cuGraph、PyG、XGI 等在 11 篇中均未见点名。**这只是“本抽样中未见”，不是“顶刊不用”**——例如第 2 篇道路网络工作用 OSM 作对照而非 OSMnx，反映的是数据源与工具的区分，不是对工具的否定。

### 5.4 从顶刊图幅提炼的可视化规范（5 条）

1. **多面板按逻辑分组，单图讲清一个对比**：性能曲线按平均度/社区数条件分面板（第 1 篇 Fig.1–4）；地图 + 变化图并置（第 2 篇 Fig.1 全球铺装率地图 + 2020–2024 变化图）；网络图 + 每簇两侧的指标条形图并置（第 8 篇：左 rMCC、右 cPurity）。**规范：每幅主图只回答一个问题，面板之间是“条件—结果”或“全貌—局部”的逻辑关系，不是堆砌。**
2. **颜色与类别严格一一对应，且语义有序**：第 8 篇 Fig.1 按疾病严重程度绿（轻）/黄（中）/橙（重）/红（严重）编码，图例与颜色逐一对应；第 2 篇 Fig.2 用品红=未铺装、白=已铺装，卫星影像与预测叠加对照。**规范：类别色板须在图例中逐项说明；有序变量用顺序色（sequential），不用无序彩虹色；同一类别在全文所有图中保持同一颜色。**
3. **阈值与判断标准直接标在图上**：第 8 篇明确标注 MCC > 0.4 为强匹配、> 0.7 为很强；第 3 篇在方法与图中同时标注 IBD ≥ 0.9 / ≥ 0.5 两档阈值。**规范：关键阈值、显著性线、参考线要画在图内并在图注中复述，不要只写在正文。**
4. **大网络坦承二维布局的局限**：第 8 篇 Fig.12（N=1080，8 类、5 簇）作者明确指出二维可视化困难（teal 簇穿过 lime 簇），交互式 3D 可改善可读性但超出范围。**规范：节点数上千的网络图不要硬画全图——应做抽样、聚合（超节点）、分簇子图或交互式呈现，并在图注中说明呈现方式与局限。**
5. **图注自足（self-contained）**：顶刊图注普遍包含样本量 N、方法、阈值与数据来源，读者不读正文也能理解图意。**规范：每幅图的图注至少写清：数据（N、来源）、方法（布局算法、社区算法与参数）、颜色/符号编码、结论指向。字体与版式上，正文图多用无衬线字体、字号不小于 7 pt，线宽与点径在印刷缩小后仍可分辨；配色优先考虑色盲友好（如 ColorBrewer / Okabe-Ito）与灰度打印可区分。**

---

## 6. 验证小结

### 6.1 验证环境

- Linux VM（Python 3.12.3，git 2.43.0），内存 7.7 GiB（任务期间空闲仅约 166–558 MiB），磁盘 150G（可用 139G）。
- `venv-test/`：`python3 -m venv --system-site-packages`（系统 numpy 1.26.4 / SciPy 1.11.4 / pandas 2.1.4 / matplotlib 3.6.3，pip 安装后 numpy 升至 2.5.4）；`venv2/`：隔离 venv（numpy 2.5.4、matplotlib 3.11.2）。
- 克隆：27 个仓库 shallow clone，共约 1.1G；测试 venv 合计约 2.2G。`/tmp` 为 tmpfs 仅 512M，pip 默认缓存曾因此报 `No space left on device`，改用工作区内 `tmp-pip/` 作 TMPDIR 后解决（已清理）。
- 统一基准：Zachary 空手道俱乐部图（34 节点 / 78 边），除注明者外均以此图测试。

### 6.2 实测通过（17 个）

| 项目 | 实测版本 | 关键结果 |
|---|---|---|
| NetworkX | 3.7 | betweenness 前三 0（0.4376）、33（0.3041）、32（0.1452）；Louvain [6,10,4,14]；平均聚类系数 0.5706 |
| igraph | 1.0.0 | betweenness（未归一化）前三 0（231.07）、33（160.55）、32（76.69），与 NetworkX 成比例一致 |
| leidenalg | 0.12.0 | Leiden 4 社区 [5,6,11,12]，模块度 0.4198 |
| rustworkx | 0.18.1 | betweenness 与 NetworkX 一致；Dijkstra 0→33 距离 2.0 |
| Infomap | 2.16.0 | 3 社区 [5,11,18]（seed=123, num_trials=5） |
| CDlib | 0.4.1 | Louvain 4 社区 [5,5,11,13]，模块度 0.4402 |
| scikit-network | 0.33.0 | Louvain 4 社区（注意：0.33.0 拒绝 SciPy sparse array，须传 ndarray 或 csr_matrix） |
| graspologic | 3.4.4 | 谱嵌入 ASE 输出 (34, 2) |
| NetworKit | 11.3 | betweenness 前三 0（462.14）、33（321.10）、32（153.38）（未归一化有序对计数，约为 igraph 值的 2 倍）；PageRank 前二 33（0.1009）、0（0.0970） |
| XGI | 1.1 | 超图示例 12 节点 / 6 超边，边大小 [2,2,3,3,4,5] |
| NetworkX-Temporal | 1.4.5 | 时序图 6 节点 / 8 边，4 快照，节点数 [1,1,3,3] |
| community_TAU | 1.4.7（PyPI） | 4 社区 [5,6,11,12]，模块度 0.4449（导入名已改为 `tau_community_detection`，旧名 `community_TAU` 不可用） |
| OSMnx | 2.1.1 | 离线 XML 解析 3 节点 / 4 有向边，简化后 2 节点 / 2 边，边长 122.2 m；`basic_stats` 在 3 节点玩具图上报错（见 4.4） |
| Pandana | 0.8 | 合成 4 节点路网聚合结果 [84.0, 92.0, 88.0, 90.0]，与 pandarm 一致 |
| pandarm | 0.0.7.post1 | 同上 [84.0, 92.0, 88.0, 90.0]；最近节点查询正常 |
| WNTR | 1.5.0 | Net1 案例：9 个 junction、12 根管道、11 个节点、13 条连接；`to_graph` 得 11/13；节点 '10' 高程 216.408 |
| EasyGraph | 1.6.3 | 基础图功能通过：4 节点 / 4 边，度 {0:2,1:2,2:3,3:1}，直径 2，平均聚类系数 0.5833（`--no-deps` 安装 + 补装 fastjsonschema、tqdm；全量依赖未装） |

**测试脚本说明**：测试中的 API 用法错误（如 rustworkx `pagerank` 要求有向图、sknetwork 拒绝 sparse array、pandana/pandarm 的 `aggregate` 须传 `name` 参数、WNTR 的 `junctions()` 返回生成器）均已在脚本中修正，**不计为库故障**；报告中的数值均为修正后的最终运行结果。

### 6.3 未跑通 / 未实测（11 个）及原因

| 项目 | 状态 | 原因 |
|---|---|---|
| graph-tool | 未实测 | 需编译 C++ 核心（Boost），本机内存紧张未全量编译；已核查源码与 LGPL-3.0 许可证 |
| cuGraph | 未实测 | 需 NVIDIA GPU + CUDA/RAPIDS 环境，本机无 GPU；已核查源码结构 |
| PyTorch Geometric | 未实测 | 需 PyTorch（数百 MB），本机带宽与内存紧张未全量安装；已核查源码（`torch_geometric/nn/conv/`） |
| Reticula | 未实测 | C++ 核心 + Python 绑定需编译；已核查源码 |
| pathpyG | 未实测 | 需 torch + torch-geometric；已核查源码与 README |
| GRAPE | 未实测 | 仓库最后提交 2024-02-24，已停滞 2 年以上；PyPI 0.2.5（2025-09-28）与仓库提交不一致，未证实二者对应关系 |
| Gephi | 未实测 | 本机无 Java 环境，桌面应用无法运行；已核查源码与发版（0.11.4，2026-11-01） |
| Gephi Lite | 未实测 | Web 应用，需 npm 构建/部署；已核查 README 与发版（v1.1.1，2026-11-06） |
| sigma.js | 未实测 | 未装 npm 依赖；已核查 package.json（npm 4.0.6）与源码；本机 Node v24.22.1 可用 |
| Cytoscape.js | 未实测 | 未装 npm 依赖；已核查 package.json（npm 3.35.0）与源码 |
| vis-network | 未实测 | 未装 npm 依赖；已核查 package.json（npm 10.1.5）与源码 |
| community_TAU | 仓库未克隆（但 PyPI 实测通过） | GitHub 仓库不可达（见 7.2）；PyPI wheel 1.4.7 实测通过 |

**环境性失败（已修复，不计入未通过）**：XGI 首次实测失败源于本机环境冲突——pip 把 venv 内 numpy 升至 2.5.4，而 `--system-site-packages` 引入的系统 matplotlib 3.6.3 针对 NumPy 1.x 编译，`import xgi` 时报 `numpy.core.multiarray failed to import`。改用隔离 venv2（numpy 2.5.4 + matplotlib 3.11.2）后通过。这是环境问题，不是 XGI 的故障。

---

## 7. 发现的主要问题

### 7.1 停滞与衰落的项目

- **GRAPE**：GitHub 最后提交 2024-02-24，已停滞 2 年以上；PyPI 上却有 2025-09-28 的 grape 0.2.5，二者对应关系未证实。**新项目不应采用。**
- **DGL**（未列入正表）：RAPIDS 25.06 已移除 cuGraph-DGL 支持，生态在收缩；SNAP.py（PyPI 最后发布 2020 年）已停滞，均不推荐新项目。

### 7.2 community_TAU：PyPI 活跃、仓库失联

PyPI 称其主页为 https://github.com/HillelCharbit/community_TAU.git，但 2026-11-14 实测 `git ls-remote` 失败、GitHub API 与搜索均无匹配，克隆失败。PyPI 包 tau-community-detection 1.4.7（2026-07-14，MIT）仍可安装且实测通过，但**导入名已由 `community_TAU` 改为 `tau_community_detection`，旧文档的导入示例失效**；PyPI 描述称“积极维护”与仓库不可达的事实矛盾。**采用前须先确认源码托管去向；当前只建议通过 PyPI wheel 使用，不建议作为长期依赖。**

### 7.3 版本号与仓库状态不一致

- GRAPE：PyPI 0.2.5（2025-09-28）vs 仓库最后提交 2024-02-24，未证实二者对应关系。
- API `pushed_at` 与默认分支 HEAD 日期存在系统性差异（scikit-network、leidenalg、infomap、cugraph、pathpyG、reticula 均有），源于向非默认分支的推送；评估活跃度时应以默认分支 HEAD 与发版日期为准，`pushed_at` 仅作参考。
- Infomap 的 PyPI 旧页曾显示 2.12.0，实际最新为 2.16.0（2026-10-27）；scikit-network 的 pip 在本环境解析为 0.33.0 而非 PyPI 最新 0.33.5。

### 7.4 NumPy 2 兼容性仍是分水岭

- **Pandana 原版 0.8（2026-08-24）已可在 NumPy 2.5.4 下运行**，与 pandarm 结果完全一致——“原版不兼容 NumPy 2”的说法对 0.8 已过时；但 pandarm（0.0.7.post1）仍是更明确的兼容 fork，二者任选其一均可，优先试原版 0.8。
- **EasyGraph 1.6.3 仍要求 numpy<2**（元数据硬约束），且全量依赖含 torch<2.0、gensim、pandas 3 等，依赖解析会把 numpy 降级至 1.26.4；本次仅 `--no-deps` + 补装小依赖验证了基础图功能，GNN/GPU 模块未验证。
- XGI 的首次失败亦源于 NumPy 1.x/2.x 混装（见 6.3）。**建议：新环境统一用 NumPy 2 + 各库最新版；混用系统包与 pip 包时优先用隔离 venv。**

### 7.5 顶刊抽样中通用图库点名率低

11 篇抽样中仅 2 篇点名清单内工具（igraph R、NetworkX 2.6.3 旧版），其余或自带代码存档，或只点名算法（Louvain、SBM）而不指明实现库。**含义**：选型时不应只看“顶刊用不用”，而要看算法是否被顶刊方法论认可、以及库本身是否可复现（代码/数据存档、版本固定、随机种子）。Louvain/Leiden/Infomap 的算法地位比任何单一库的点名更稳固。

### 7.6 其他注意点

- **许可证风险**：igraph（GPL-2.0）、leidenalg/Infomap（GPL-3.0）、pathpyG/Pandana/pandarm（AGPL-3.0）、Gephi（GPL-3.0/CDDL）为 copyleft 许可，商业闭源集成需评估；其余多为 MIT/BSD/Apache-2.0 宽松许可。
- **小众新库生态浅**：NetworkX-Temporal（20 stars）、Reticula（26）、pandarm（25）、pathpyG（62）星数与用户基数都很小，API 仍在变动，采用时应固定版本并留好替代方案。
- **同名区分**：graspologic 当前主仓为 graspologic-org/graspologic（旧地址 graspologic/graspologic 与 microsoft/graspologic 非当前主仓）；scikit-network 主仓为 sknetwork-team/scikit-network（旧地址 sknetwork/scikit-network 404）；XGI 主仓为 xgi-org/xgi（旧地址 ComplexGroupInteractions/xgi 已迁移）；pandarm 主仓为 oturns/pandarm（foti/pandarm 404）。引用时务必用当前地址。

---

## 8. 选型建议

| 场景 | 首选 | 备选 / 说明 |
|---|---|---|
| 通用图分析、教学、原型 | **NetworkX 3.7** | 大规模时换 igraph / NetworKit / rustworkx |
| 大规模图、高性能 | **igraph 1.0.0**（GPL-2.0 注意许可）或 **rustworkx 0.18.1** | NetworKit 适合并行批处理；cuGraph 需 GPU |
| 社区发现 | **leidenalg + igraph**（默认）；有向/多层用 **Infomap** | 横评算法用 CDlib；新算法可试 TAU（先确认源码去向） |
| 图机器学习 / GNN | **PyTorch Geometric 2.8.1** | 传统谱方法用 graspologic；scikit-learn 风格用 scikit-network |
| 时序网络 | **NetworkX-Temporal 1.4.5** | 深度时序模型看 pathpyG（门槛高）；超图用 XGI 1.1 |
| 街道网络（地理研究） | **OSMnx 2.1.1** | 可达性分析用 Pandana 0.8 或 pandarm；供水管网用 WNTR 1.5.0 |
| 网络可视化 | 桌面 **Gephi 0.11.4**；浏览器 **Gephi Lite** / **sigma.js** | 分析+可视化一体用 Cytoscape.js；轻量交互用 vis-network |
| 出版级图幅 | 按 5.4 的 5 条规范手工打磨 | 颜色与类别一一对应、阈值标在图上、图注自足、大网络不硬画全图 |

---

## 附录 A. 复现说明

- **仓库克隆**：`complex-networks/repos/` 下 27 个子目录（shallow clone，`--depth 1`），共约 1.1G；缺 community_TAU（仓库不可达）。克隆 HEAD 哈希（抽样）：networkx 2026-11-11 `6855cd5`、igraph 2026-11-03 `1fff572`、networkit 2026-11-11 `2bac2b3`、rustworkx 2026-11-08 `e32b4d3`、graspologic 2026-06-18 `ccf1458`、infomap 2026-11-01 `39e7876`、leidenalg 2026-10-13 `9890a99`、cugraph 2026-11-10 `c17377f`、pytorch-geometric 2026-11-05 `d1f2f86`、easygraph 2026-10-12 `a81b5df`、osmnx 2026-11-07 `5f3b46f`、wntr 2026-11-11 `39e6b34`、pathpyG 2026-07-09 `02c0dc6`、pandana 2026-09-30 `e070217`、pandarm 2026-10-23 `fda3676`、gephi-lite 2026-11-06 `9570b9c`、sigma.js 2026-11-10 `e7748c8`、xgi 2026-11-13 `e218543`、networkx-temporal 2026-11-09 `ec27161`、graph-tool 2026-11-11 `50e5353`、grape 2024-02-24 `f7f84b4`、reticula 2025-07-26 `e2af9b6`、vis-network 2026-11-13 `62fb913`、cytoscape.js 2026-11-10 `b768734`、gephi 2026-11-08 `e2ecd45`。
- **测试环境**：`venv-test/`（约 1.4G）、`venv2/`（约 750M）保留供复核；测试脚本曾存于 `/tmp/t_*.py`（临时文件，未保留，关键命令与输出已记入第 6 节）。
- **配图**：`figures/stars-2026-11-14.png`（星数分布）、`figures/karate-louvain-networkx.png`（Karate 图 Louvain 划分实测输出）。

## 附录 B. 未列入正表、仅作動向注记的项目

- **temporal-networks**（cadrianas/temporal_networks，1 star，GPL-3.0，2026-10-28 发布 0.1.0）：极新极小，待观察。
- **STM-Graph**（Ahghaffari/stm_graph，5 stars，MIT，CIKM '25 论文，2025-09-03）：时空图方向新工作，待观察。
- **DGL**：RAPIDS 25.06 已移除 cuGraph-DGL 支持，生态收缩，不推荐新项目。
- **SNAP.py**：PyPI 最后发布 2020 年，已停滞，不推荐新项目。
