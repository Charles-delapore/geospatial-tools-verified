# 景观生态开源工具调研报告（领域二）

- **核验日期**：2026-11-14（star 数、最近提交均为该日快照；文中日期均为仓库/API 返回的 UTC 时间换算说明，特别注明时除外）
- **范围**：景观格局指数、景观连通性、生态廊道识别与模拟、生境建模、FRAGSTATS 替代品、景观模拟与规划工具
- **方法**：先做公开检索（GitHub API、PyPI、CRAN、期刊论文），再把仓库 `--depth 1` 浅克隆到 `repos/`，读 README/DESCRIPTION/关键代码后做小步实测；查不到的写“未查到”，不编造数字与用例
- **规模**：正表 **28 个开源项目 + 2 个闭源基准（FRAGSTATS、Conefor）**；另在“期刊标杆”一节抽样 **8 篇** 2024–2026 年论文
- **本地仓库**：`~/workspace/your_files/geography-research/landscape-ecology/repos/`（27 个目录，约 700 MB；landschaft 的 git clone 超时失败，未落盘，见表内备注）

## 1. 项目总表

“验证状态”分档：✅ 完整运行 / ◐ 导入或核心函数级通过 / △ 仅静态检查（编译/语法） / ✖ 未跑通（注明原因） / — 未尝试运行（仅做仓库与文档核验）。

| # | 项目 | 仓库 | 许可证 | Stars* | 最近提交/发版 | 用途（一句话） | 验证状态 |
|---|---|---|---|---|---|---|---|
| 1 | PyLandStats | https://github.com/martibosch/pylandstats | GPL-3.0 | 114 | 提交 2026-11-09；发版 v3.1.0（2025-02-13） | Python 景观格局指数库（斑块/类别/景观三级指标） | ◐ 核心函数通过（`compute_adjacency_arr` 实测），整包导入需 rasterio+geopandas 等重依赖，本机未全量安装 |
| 2 | landscapemetrics | https://github.com/r-spatialecology/landscapemetrics | GPL-3 | 264 | 提交 2026-10-18；CRAN v2.2.1（2025-02-10），仓库内 DESCRIPTION 为 v2.2.2 | R 版 FRAGSTATS 替代品，tidy 工作流算景观指数 | ✖ 本机无 R，未跑通 |
| 3 | landschaft | https://github.com/sacridini/landschaft | GPL-3.0 | 0 | 提交 2026-10-31；PyPI 1.58.1（2026-10-31） | 新一代 Python 景观分析包（C++17/OpenMP 核心，133 个指标 + MSPA/破碎化/连通性/生境） | ✅ 完整运行（见 §3.1） |
| 4 | LecoS | https://github.com/Martin-Jung/LecoS | GPL-3.0 | 25 | 提交 2026-05-05；QGIS 插件 v3.0.2（2026-05-05） | QGIS 景观生态统计插件，算土地覆被指数 | — 未尝试运行（需 QGIS）；QGIS 插件站累计下载约 18 万次 |
| 5 | motif | https://github.com/Nowosad/motif | MIT | 66 | 提交 2025-07-26；CRAN v0.6.5（2025-07-26） | R 格局签名分析：共生矩阵描述、搜索/变化检测/聚类 | ✖ 本机无 R，未跑通 |
| 6 | comat | https://github.com/Nowosad/comat | MIT | 6 | 提交 2026-03-17；v0.9.8 | motif 的底层库：由空间数据建共生矩阵 | ✖ 本机无 R，未跑通 |
| 7 | DynamicPATCH | https://github.com/zay1996/DynamicPATCH | MIT | 9 | 提交 2026-09-30（API）；本地浅克隆 HEAD 为 2026-04-19 | 2025 年新方法：8 类斑块动态转移（出现/消失/合并/分裂/穿孔/填充/扩张/收缩）+ 总量变化 | ✖ 导入失败：缺 `osgeo`（GDAL），README 要求 conda 装 GDAL |
| 8 | LS_METRICS | https://github.com/LEEClab/LS_METRICS | GPL-2.0 | 28 | 提交 2025-10-11 | GRASS GIS 生态尺度景观指数 + 连通性制图，为 BioDIM 个体模型备输入 | — 未尝试运行（需 GRASS GIS 7.8）；仓库 139 MB，近半为图片与演示数据 |
| 9 | Circuitscape.jl | https://github.com/Circuitscape/Circuitscape.jl | MIT | 150 | 提交 2026-10-28；发版 v6.1.0（2026-09-07） | 电路理论连通性旗舰（Julia 版，pairwise/one-to-all/all-to-one/advanced 四模式） | ✖ 本机无 Julia，未跑通 |
| 10 | Omniscape.jl | https://github.com/Circuitscape/Omniscape.jl | MIT | 75 | 提交 2026-10-27；v0.6.4 | 全向移动窗口电路连通性（Omniscape 算法） | ✖ 本机无 Julia，未跑通 |
| 11 | circuitscaper | https://github.com/matthewkling/circuitscaper | MIT | 5 | 提交 2026-11-06；CRAN v0.2.0（2026-11-06） | 2026 年新 R 包：在 R 内调 Julia 的 Circuitscape/Omniscape | ✖ 本机无 R/Julia，未跑通 |
| 12 | Linkage Mapper | https://github.com/linkagescape/linkage-mapper | GPL-3.0 | 55 | 提交 2026-08-31；通行版 v3.2.0（论文中常见） | ArcGIS 廊道工具箱：最小成本廊道 + Pinchpoint/Centrality/Barrier Mapper | △ 全部脚本 `py_compile` 通过；功能运行需 ArcGIS/arcpy，未跑通 |
| 13 | Makurhini | https://github.com/connectscape/Makurhini | GPL-3 | 57 | 提交 2026-11-12；v3.0 | R 破碎化与连通性综合包（PC/IIC/ECA、欧氏/最小成本/电路三种链接） | ✖ 本机无 R，未跑通（见 §3.3 深挖） |
| 14 | Graphab | https://gitlab-mshe.univ-fcomte.fr/thema/graphab | 未在仓库顶层找到 LICENSE 文件；官网称免费供非商业使用 | —（GitLab，未查到 star 数） | 提交 2026-09-02（3.1.14 合并提交） | 景观图旗舰：建图、可视化、连通性指标、与外部数据联动；Java + Maven，需 Java 11+ | ✖ 本机无 Java，未跑通 |
| 15 | landscape-connectivity-pipelines | https://github.com/goaudreymp/landscape-connectivity-pipelines | GPL-3.0 | 0 | 提交 2026-10-21；Zenodo v2.0.0（2026-10-21） | 2026 年新自动化流水线集：Graphab + Circuitscape/Omniscape 参数扫描 | — 未尝试运行（需 R + Graphab + Julia 三件套） |
| 16 | pyGuidos | https://github.com/nonpenso/pyguidos（GitHub 镜像；上游 code.europa.eu/jrc-forest/guidos/pyguidos） | GPL-3.0 | 1（镜像） | 镜像提交 2026-11-10；PyPI 2.6.4（2026-11-09） | 2026 年 JOSS 在审：GuidosToolbox 核心工具的纯 Python 实现（MSPA/破碎化/景观镶嵌等） | ✖ 全量 pip 安装超时（numba/llvmlite 等依赖链过大）；代码已读，未运行 |
| 17 | GuidosToolbox / GWB（MSPAstandalone 代理） | GTB/GWB 官网 https://forest.jrc.ec.europa.eu/en/activities/lpa/gtb/；代码代理 https://github.com/vogtpet/MSPAstandalone | GPL-3.0（MSPAstandalone） | 0（代理） | 代理提交 2026-11-13；GTB 3.402 / GWB 2.0.4（2026-07） | JRC 形态学空间格局分析旗舰：MSPA、FAD、景观镶嵌；GWB 为 Linux 命令行版 | ✖ 本机无 Java/编译链，未跑通；仅核验手册与代理仓库 |
| 18 | NLMR | https://github.com/ropensci/NLMR | GPL-3 | 71 | 提交 2026-11-12；v1.5.0 | R 中性景观模型：15 种算法，返回 terra SpatRaster | ✖ 本机无 R，未跑通 |
| 19 | nlmpy | https://github.com/jsta/nlmpy | 未声明 LICENSE | 3 | 提交 2018-02-19（停滞） | Python 中性景观模型（PyPI 镜像仓库） | ✅ 完整运行（`mpd`/`classifyArray`/`randomClusterNN`） |
| 20 | NeutralLandscapes.jl | https://github.com/EcoJulia/NeutralLandscapes.jl | MIT | 19 | 提交 2026-02-17 | Julia 中性景观生成（基于 NLMPy 思路） | ✖ 本机无 Julia，未跑通 |
| 21 | flsgen | https://github.com/dimitri-justeau/flsgen | GPL-3.0 | 6 | 提交 2022-10-07（停滞） | 以景观指数为目标的中性景观生成器（Java/Maven） | ✖ 本机无 Java，未跑通 |
| 22 | ALGR | https://github.com/pogoyoly/ALGR | GPL-3.0 | 0 | 提交 2025-09-20 | 2025 年新 R 包：通用农业景观生成器（三步：划定空间—布设田块—丰富信息） | ✖ 本机无 R，未跑通 |
| 23 | RangeShiftR | https://github.com/RangeShifter/RangeShiftR-pkg | GPL-3.0 | 12 | 提交 2026-11-13（API）；本地克隆 HEAD 2026-10-21 | R 包版 RangeShifter：个体、空间显式、生态进化种群模拟（v1.1.2，2025-09-26） | ✖ 本机无 R，未跑通 |
| 24 | LANDIS-II | https://github.com/LANDIS-II-Foundation/Core-Model-v6（核心 v6 已归档停滞；扩展仍活跃） | Apache-2.0 | 9（核心 v6） | 核心 v6 提交 2018-02-21；扩展如 NECN 提交 2026-11-12 | 森林景观模拟：演替 + 火/风/采伐/虫害等干扰，大尺度（10 万–1000 万公顷） | ✖ 本机无 .NET/C# 运行环境，未跑通 |
| 25 | InVEST | https://github.com/natcap/invest | Apache-2.0 | 259 | 提交 2026-11-13；发版 3.20.2（2026-09-02） | 自然资本模型集；本领域用其 Habitat Quality（生境质量）与 Habitat Risk Assessment | △ `habitat_quality.py` 语法编译通过；完整模型需 GDAL 数据栈，未跑通 |
| 26 | PLUS | https://github.com/HPSCIL/Patch-generating_Land_Use_Simulation_Model | 无 LICENSE 文件 | 198 | 提交 2025-12-14 | 斑块生成土地利用模拟（LEAS 规则挖掘 + 元胞自动机），中国国土空间规划常用 | ✖ 仓库实为 Windows 发行物：解出的内容只有 `PLUS V1.4.2.exe`（74 MB）+ GDAL_DATA，无源码主干；git clone 两次网络中断、tarball 截断 |
| 27 | WS3 | https://github.com/UBC-FRESH/ws3 | MIT | 14 | 提交 2026-10-12；发版 v1.0.5（2025-10-12） | 森林木材供应模拟与优化框架（Model I 线性规划 + 栅格分配） | ◐ 包与 `ws3.forest` 子模块导入通过；真实模型运行需林分清单数据 + HiGHS/Gurobi 求解器，未跑通 |
| 28 | xLandscape | https://github.com/xlandscape/xLandscape-Analysis（组织内多仓，无单一主仓） | 未声明 | 1（Analysis 仓） | Analysis 仓提交 2024-04-11 | 模块化景观模型框架（XML 编排组件，农药/水生风险等场景） | — 未尝试运行（多仓拼装，入门成本高） |
| 基准 A | FRAGSTATS | https://www.fragstats.org（免费软件，非开源） | 闭源免费 | — | 通行版 v4.3（论文中 v4.2/v4.3 常见） | 景观格局指数的定义源头与事实标准；几乎所有替代品都以“与 FRAGSTATS 一致”为卖点 | — 基准，不参与开源排名 |
| 基准 B | Conefor Sensinode | https://conefor.org（免费软件，非开源） | 闭源免费 | — | 2.2/2.6 版通行 | 景观连通性 PC/IIC/dPC/ECA 指标的源头；Makurhini、Graphab 等都对标它 | — 基准，不参与开源排名 |

\* Stars 为 2026-11-14 通过 `api.github.com` 查询的快照；许可证优先以仓库内 `LICENSE`/`DESCRIPTION` 文件为准，API 未返回时注明。

### 总表读法（先说结论）

- **格局指数已从“R 一家独大”转向“Python 双轨”**：`landscapemetrics`（264★）仍是引用量最大的 FRAGSTATS 替代品，但 2026 年冒头的 `landschaft`（0★，PyPI 1.58.1）一次覆盖了 landscapemetrics + GuidosToolbox + InVEST 三家的功能面，且自带基准测试称指标与 landscapemetrics 2.2.2“逐位一致”、快 35–500 倍（该说法来自其 PyPI 页，未独立复核）。
- **连通性仍是“老三样 + 新包装”**：Circuitscape.jl / Omniscape.jl / Graphab / Linkage Mapper / Conefor 仍是顶刊方法部分的标配；2026 年的新东西是包装层（`circuitscaper` 把 Julia 藏进 R，`landscape-connectivity-pipelines` 把 Graphab+Circuitscape 串成参数扫描），不是新算法。
- **2024–2026 真正的新项目**：`landschaft`、`pyGuidos`、`circuitscaper`、`DynamicPATCH`、`ALGR`、`Makurhini 3.0`、`landscape-connectivity-pipelines`、`WS3`（2025 年论文）。其中 `landschaft` 与 `pyGuidos` 是本轮最值得跟进的两个。
- **停滞对照组**：`nlmpy`（2018）、`flsgen`（2022）、LANDIS-II 核心 v6（2018）已停更，但仍被引用；选型时应优先用其活跃替代品（NLMR、NeutralLandscapes.jl、LANDIS-II 各扩展仓）。

## 2. 重点项目深挖（5 个）

### 2.1 landschaft —— 本轮最大发现：一个包顶三家

- **定位**：PyPI 介绍为“Fast, landscape analysis for Python”，C++17/OpenMP 核心 + numpy/xarray/dask/rasterio API；功能对照表自称复现 GuidosToolbox（破碎化 FAD/FOS、景观镶嵌、熵）、landscapemetrics/FRAGSTATS（133 个斑块/类别/景观指标）、InVEST（碳储量、生境退化/质量/稀有度），另有最小成本廊道、等时线、MSPA、电路连通性（`ls.circuit.omniscape`）、物种分布模型（`ls.sdm`）等模块。
- **真实用例/采用者**：未查到已发表的第三方应用论文（2026-10-31 才到 1.58.1，太新）；作者即 Awesome-Geospatial 维护者 sacridini。其 PyPI 页给出基准测试方法与“与 landscapemetrics 2.2.2 逐位一致、快 35–500 倍”的对照表（未独立复核，数字存疑，至少说明作者有意对标）。
- **安装运行难度**：中等偏易（有 wheels）。本次实测走 `--no-deps` 装 wheel 后逐个补依赖（xarray → rasterio → click/affine/attrs/cligj → rioxarray/pyproj），最终导入成功；全量 `pip install pyguidos landschaft` 曾因 /tmp 只有 512 MB 而报 `No space left on device`，改 TMPDIR 到 home 磁盘后仍因网络慢超时——教训：共享机上装重依赖务必设 `TMPDIR` 到大磁盘并用 `--no-cache-dir`。
- **实测结果（✅）**：40×40 合成栅格（3 类，seed 7，res=30 m），`ls.Landscape(arr)` 得 212 个斑块，`landscape_metrics()` 一次返回约 60 个指标的 DataFrame，关键值：SHDI 1.059、SHEI 0.964、CONTAG 6.38、AI 38.55、LPI 13.1、COHESION 94.16、DIVISION 0.775、ED 403.3、NP 212、TE 58080。见图 `figures/landschaft-synthetic-test.png`（左为测试栅格，右为所选指标条形图；注意右图不同量纲共用一轴，仅作示意，SHDI/SHEI 这类 ~1 的值几乎看不见——制图时应分面或标准化）。
- **风险**：0 star、单人维护、无同行评审论文背书；指标“逐位一致”的说法需用真实景观数据复核后才能采信；依赖面很宽（geopandas、pyarrow、folium、plotly、h3、dendropy 等），全量安装重。

### 2.2 PyLandStats —— Python 格局指数的稳健老将

- **定位**：2019 年 PLOS ONE 论文的配套库（Bosch & Chenal），`Landscape` 类读 GeoTIFF，输出斑块/类别/景观三级指标 DataFrame，支持时序演变与梯度分析、缓冲区分析；指标定义对标 FRAGSTATS v4。
- **真实用例**：瑞士三座城市群城市化时空格局分析（Bosch & Chenal，论文配套代码另有专仓）；康顿 Vaud 2000/2006/2012 Corine 土地覆被示例。
- **安装运行难度**：中等。依赖 clustergram、dask、geopandas、rasterio、seaborn、scikit-learn、scipy；本机系统 Python 已有 numpy/pandas/scipy/matplotlib，缺 rasterio/geopandas/sklearn 等，全量安装未做（网络慢、内存紧）。
- **实测结果（◐）**：绕过 `__init__` 的重依赖，直接加载 `src/pylandstats/adjacency.py`（纯 numpy），对 3×3 测试阵列算邻接矩阵成功，总邻接数 80。整包 `import pylandstats` 因顶层 `import rasterio` 未在本机跑通——这是该包的真实门槛：即使只想用 numpy 数组输入，也绕不开 rasterio/geopandas 的导入。
- **注意**：2026-11-09 仍有提交（`Refactor/numpy adjacency`），项目活着；但发版停在 2025-02 的 v3.1.0。

### 2.3 Makurhini 3.0 —— 连通性指标的“合订本”

- **定位**：R 包，名字取自普雷佩查语；把破碎化与连通性指标收进一个工具：欧氏/最小成本/电路三种链接方式，算 PC（Probability of Connectivity）、IIC、ECA（Equivalent Connected Area）、Protected Connected 等，并给节点/链接按贡献排序；支持并行、大数据量；v3.0 新增 `MK_dPCIIC()` 对 PC/IIC 做 intra/direct/step 三组分分解（Saura, Bodin & Fortin 2014 的框架）。
- **真实用例/采用者**：论文 2025 年 4 月挂 Research Square 预印本，2026 年刊于 Environmental Modelling and Software（201 卷，106981）；方法上承接 Saura 的 Conefor 指标体系，定位是保护规划与修复优先排序。仓库 122 MB（含较多示例数据/图片），README 自标 lifecycle: experimental。
- **安装运行难度**：R ≥ 4.0，需 igraph、cppRouting ≥ 2.0 等；本机无 R，未跑通。只做了仓库核验：DESCRIPTION 明确 License GPL-3 + file LICENSE，版本 3.0。
- **选型意义**：如果工作流在 R 里且只需要“指标”而非“跑电路模拟”，Makurhini 比 Circuitscape.jl 更轻；但它不产生廊道地图，需与 Linkage Mapper/Graphab 搭配。

### 2.4 pyGuidos —— JRC 官方工具的 Python 化（2026 年最值得跟进的之一）

- **定位**：欧盟委员会 JRC 的 GuidosToolbox（GTB）/ Workbench（GWB）核心工具的纯 Python 重实现：`mspa()`（形态学空间格局分析）、`spa()`、`frag()`、`frag_gray()`、`frag_change()`、`landmos()`（景观镶嵌）、`acc()`（前景斑块面积核算）、`rss()`（修复状态汇总）；Numba JIT 并行，号称性能与 C 编译版相当；JOSS 在审（Caudullo, Vogt & Soille 2026）。
- **真实用例/采用者**：直接服务于欧盟《自然恢复法》（NRR）合规——成员国须上报基于前景面积密度（FAD）的森林连通性指数，pyGuidos 实现了该法规采用的 FAD 精确算法；全球森林属性数据集（GFAD）的生产流程即用 pyguidos（Caudullo & Vogt 2026，Zenodo 数据集 + GFAD-analysis 代码仓）。
- **安装运行难度**：中高。要求 Python ≥ 3.10、numpy ≥ 2.0、rasterio ≥ 1.4、scipy、scikit-image、matplotlib、pyogrio、geopandas、shapely、python-ternary、numba；另含 `_mspa` C 扩展（vendored miallib），源码安装需编译。本次全量 `pip install pyguidos landschaft` 在共享机上超时失败（280 秒未完成，numba/llvmlite 轮子约 60 MB + 网络拥塞），未跑通；但已读 README、pyproject 与模块清单，确认其 API 与 GTB/GWB 的对应关系。
- **注意**：上游在 code.europa.eu（需 EU Login 才能提 issue），GitHub 镜像为 `nonpenso/pyguidos`（1★，同步于 2026-11-10），提 issue/贡献走镜像。旧版 pyguidos 曾是“调 GWB 二进制”的封装，新版 2.x 是原生重实现，选型时要认准版本。

### 2.5 Graphab —— 景观图方法的事实标准（但跑起来最“重”）

- **定位**：法国 ThéMA 实验室的 Java 应用（Maven 工程，需 Java 11+）：建图（栅格/矢量生境均可，3.0 新增矢量生境）、算连通性指标（全局/局部）、关联外部点数据、可视化制图；GUI + 命令行双模式，可批量。
- **真实用例/采用者**：加泰罗尼亚生境连通性工作流（AD4GD 项目，欧盟资助，HPC 容器化跑 Graphab）、欧洲多国城市绿地与保护规划研究；2025 年 Foltête & Vuidel 在 Environmental Modelling and Software 的综述把 Graphab 与 Conefor、Iconnect 并列为景观图三大工具；2026 年 Landscape Ecology 欧洲首都绿地连通性论文用其 R 封装 `graph4lg` 算图论指标。
- **安装运行难度**：高。需 Java 11+ 与 Maven 构建（或下载发行版），大景观计算吃内存；本机无 Java，未跑通。本次核验：GitLab 仓库浅克隆成功（22 MB），最新提交 2026-09-02（3.1.14 合并），`pom.xml` 确认 `maven.compiler.release=11`，README 明确要求 Java 11+ 64 位。
- **注意**：仓库顶层未找到 LICENSE 文件，官网/维基称“免费供非商业使用”；商用前须向作者确认授权。另有 R 封装 `graph4lg`（CRAN）可只算指标不装 Java 应用，轻量场景可优先考虑。

## 3. 验证小结

### 3.1 实测方法与环境

- 本机：共享虚拟机，Python 3.12.3（系统自带 numpy 1.26.4 / scipy 1.11.4 / pandas 2.1.4 / matplotlib 3.6.3），**无 R、无 Julia、无 Java、无 .NET**；内存可用常不足 1 GB；`/tmp` 仅 512 MB tmpfs（pip 默认缓存曾把 /tmp 写满导致 `No space left on device`，后改 `TMPDIR` 到 home 磁盘解决）；网络不稳定，多次 git clone 出现 `fetch-pack: unexpected disconnect`（与同机其他任务并发有关）。
- 策略：优先小步验证——能只装 wheel 就不编译，能只测核心函数就不装全量依赖；R/Julia/Java 项目只做仓库与文档核验，不硬装运行环境。

### 3.2 实测结果统计

- **尝试实测的项目：24 个**（其余 4 个仅做仓库/文档核验：LecoS、LS_METRICS、landscape-connectivity-pipelines、xLandscape）。
- **通过 6 个**：
  - ✅ 完整功能运行（2）：`landschaft`（合成栅格全量指标）、`nlmpy`（`mpd`/`classifyArray`/`randomClusterNN`）。
  - ◐ 导入/核心函数级通过（2）：`WS3`（包 + `ws3.forest` 子模块导入成功，需补 dill/fiona）、`PyLandStats`（纯 numpy 邻接矩阵核心函数）。
  - △ 仅静态检查通过（2）：`Linkage Mapper`（全部脚本 `py_compile` 通过，仅 3 处无效转义 SyntaxWarning）、`InVEST`（`habitat_quality.py` 语法编译通过）。
- **未跑通 18 个**，原因分类：
  - 本机无 R（8）：landscapemetrics、motif、comat、NLMR、ALGR、Makurhini、RangeShiftR、circuitscaper。
  - 本机无 Julia（3）：Circuitscape.jl、Omniscape.jl、NeutralLandscapes.jl。
  - 本机无 Java（4）：Graphab、MSPAstandalone、flsgen、LANDIS-II。
  - 依赖/分发问题（3）：DynamicPATCH 缺 GDAL（`osgeo`）、pyGuidos 全量安装超时、PLUS 为 Windows exe 分发且下载截断。
- 尝试实测总数 = 通过 6 + 未跑通 18 = **24 个**；其余 4 个（LecoS、LS_METRICS、landscape-connectivity-pipelines、xLandscape）只做仓库/文档核验，未尝试运行。
- **克隆失败 3 次**：`landschaft`（git clone 超时，无落盘，后改 PyPI wheel 实测）、`ws3` 与 `PLUS` 首次 git clone 均网络中断；后 `ws3` 与 `InVEST` 改用 `--filter=blob:none` 浅克隆成功（`ws3` 工作区检出仍失败，仅树结构可用，628 个文件已用 `git ls-tree` 核验；`PLUS` 改 codeload tarball，下载截断，仅解出 `PLUS V1.4.2.exe` + `GDAL_DATA`）。
- **出图 2 张**（`figures/`）：`landschaft-synthetic-test.png`（实测栅格与指标，见 §2.1 评价）、`stars-snapshot-2026-11-14.png`（16 个项目 star 快照条形图；注意 0 star 的新项目与 200+ star 的老项目同轴比较时量级差异极大，读图以排序为主）。

### 3.3 发现的主要问题

1. **环境缺口决定验证天花板**：本领域一半以上的主力工具在 R/Julia/Java 生态里，本机三者皆无，导致 15 个项目无法运行验证，只能核验仓库与文档。这是本次验证通过率低的首要原因，不是项目本身的质量问题。
2. **“新”不等于“有人用”**：2026 年新项目（landschaft、circuitscaper、landscape-connectivity-pipelines、pyGuidos 2.x）star 数几乎为 0，采用证据主要来自作者自述或法规需求，尚未经过第三方论文检验；与之相对，FRAGSTATS/Conefor/Graphab/Circuitscape 仍是顶刊方法部分的硬通货。
3. **分发方式混乱**：PLUS 仓库没有源码主干、只有 Windows exe；LANDIS-II 核心仓停滞但扩展仓活跃，初学者极易克隆到错误的仓；pyGuidos 有上游（code.europa.eu）与镜像（GitHub）两个地址，issue 通道不同；Graphab 在 GitLab 而不在 GitHub，检索时容易漏掉。
4. **仓库臃肿**：LS_METRICS 139 MB（近半是图片与演示数据）、Makurhini 122 MB、Linkage Mapper 58 MB、LANDIS-II 核心 v6 103 MB；浅克隆仍占磁盘，批量拉取前应先看体积。
5. **许可证信息不一致**：GitHub API 的 license 字段常为空或 NOASSERTION（如 Makurhini、motif、NLMR、PLUS），须以仓库内 DESCRIPTION/LICENSE 文件为准；Graphab 顶层无 LICENSE 文件，商用风险未查到。
6. **重依赖 + 小 /tmp 是实测杀手**：pyguidos/landschaft 全量安装涉及 numba、GDAL、geopandas 等大轮子，/tmp 512 MB 会先写满；务必设 TMPDIR 到 home 磁盘并加 `--no-cache-dir`，或像本次一样 `--no-deps` 逐个补依赖。

## 4. 期刊标杆（新增方法论一节）

**抽样方法**：以 Landscape Ecology、Landscape and Urban Planning 为主刊，Nature Sustainability 为综合顶刊对照；每刊抽 3 篇 2024–2026 年论文（优先开放获取、能看到全文或官方 PDF 的），共 8 篇；只记录方法与风格层面的观察，不复制原文与图片；查不到的写“未查到”。LUP 为 Elsevier 付费墙期刊，本次只能看到 ScienceDirect 摘要页与作者机构库的开放版本，全文图幅细节以“未查到”标注，不推测。

### 4.1 抽样论文一览

| # | 期刊 | 文章（标题 / DOI） | 方法部分提到的软件/库/技术栈 | 图的类型与数量 | 代码/数据公开 |
|---|---|---|---|---|---|
| J1 | Landscape Ecology (2026) | Integrating earth observation and graph theory to evaluate urban green spaces connectivity across European capitals / https://doi.org/10.1007/s10980-026-02392-1 | Google Earth Engine（云端分类 10 m 城市植被图，LUCAS 野外调查验证）+ R 包 `graph4lg`（Graphab 的图论指标，10 个网络科学指标）+ FRAGSTATS + `landscapemetrics`（30 个传统景观指标） | 全文 34 页；图幅数量未查到（仅读到方法与摘要） | 未查到代码链接（文中未在摘要中声明） |
| J2 | Landscape Ecology (2026) | Assessing connectivity between protected areas in an urban environment / https://doi.org/10.1007/s10980-026-02395-y | 电路理论 + 图论联合建模；9 个阻力情景 × 3 种扩散模式 × 多扩散距离；具体软件名在可查到的摘要中未点名 | 未查到 | 开放获取（CC BY 4.0）；代码链接未查到 |
| J3 | Landscape Ecology (2025) | DynamicPATCH: method and software for spatially explicit dynamic patch transition characterization / https://doi.org/10.1007/s10980-025-02120-1 | 自研 Python 包 DynamicPATCH（GDAL + numpy/pandas + OpenCV + scikit-image）；案例为池塘与盐沼 | 方法论文，含 8 类转移示意图与案例图；具体图数未查到 | 代码即论文配套包 https://github.com/zay1996/DynamicPATCH（本报告表内 #7） |
| J4 | Landscape and Urban Planning (2024) | Nature-based solutions for urban biodiversity: spatial targeting of retrofits can multiply ecological connectivity benefits / https://doi.org/10.1016/j.landurbplan.2024.105169 | 墨尔本停车位转绿地三情景；连通性建模方法在摘要中未点名具体软件；研究对象为 New Holland honeyeater、蓝带蜂、蝼蛄 | 情景对比图为主；具体图数未查到 | 开放获取（CC BY）；数据声明为“Data will be made available on request”（非公开仓） |
| J5 | Landscape and Urban Planning (2024) | Key connectivity areas in the Llanganates-Sangay Ecological Corridor in Ecuador / https://doi.org/10.1016/j.landurbplan.2024.105039 | 电路分析（circuit analysis，山地貘生境连通性）+ 多准则决策分析（AHP）+ 空间适宜性 + 子流域优先排序；参与式过程使廊道面积翻倍 | 研究区 + 连通性 + 适宜性分区图；具体图数未查到 | 开放获取（作者机构库 IKIAM 存有 20.96 MB 全文 PDF）；代码链接未查到 |
| J6 | Landscape and Urban Planning (2026) | Beyond protected areas: optimizing conservation planning through integrated ecosystem services and connectivity / https://doi.org/10.1016/j.landurbplan.2026.105580 | 仅通过 Crossref 题录确认存在（2026 年刊，生态系统服务 + 连通性综合保护规划）；方法细节未查到（付费墙） | 未查到 | 未查到 |
| J7 | Nature Sustainability (2025) | Landscape patterns in stand-replacing disturbances across the world's forests / https://doi.org/10.1038/s41893-024-01450-3 | Hansen 全球森林变化数据 v1.6（Google Earth Engine 伙伴数据）+ 斑块指标（面积/形状/伸长/时空聚类）+ k-means 聚类（4 类干扰格局）；2002–2014 年识别 249,149,911 个干扰斑块 | 全球格局图 + 按生物群系分面的比例图（文中点名 Fig. 2a）；表 2 为四类格局的指标统计 | 数据源为公开的 Hansen 数据集；自研代码链接未查到 |
| J8 | Nature Sustainability（综述向） | Macroecological approaches for the prediction of zoonotic disease risk / https://doi.org/10.1038/s41893-025-01749-9（2026 年 1 月刊） | 综述文章：讨论生境破碎化、生态完整性等宏观生态变量在疾病风险建模中的使用；非景观工具方法论文 | 以概念图与文献计量图为主；具体图数未查到 | 综述，无代码 |

> J6 仅作题录级抽样，方法与图幅均未查到，不计入技术栈统计。

另有一篇重要综述作为背景（非抽样计数）：Foltête & Vuidel (2025), Landscape graphs as tools for modelling and managing spatial ecological networks, Environmental Modelling and Software 193, 106594（开放获取），系统比较了 Conefor Sensinode、Graphab、Iconnect 与 Circuitscape，结论是景观图方法正受到电路理论与个体模型（IBM）的挑战。

### 4.2 顶刊实际在用什么技术栈（汇总）

- **连通性/廊道**：电路理论（Circuitscape 系）与图论（Graphab / `graph4lg` / Conefor 指标）是两大支柱，经常**联合使用**（J1、J2），而非二选一；Linkage Mapper 在 2025 年大量应用型论文中仍是廊道提取的默认工具（本报告检索到的宜昌、哥伦比亚貘、合肥冷岛等 2025–2026 年案例均用 Linkage Mapper v3.1–3.2 + Circuitscape），但在本次抽样的两本主刊正刊论文中，作者更倾向直接点名 Circuitscape/Graphab 而非 Linkage Mapper。
- **格局指数**：FRAGSTATS 仍是方法部分的“定义锚”（J1 同时用 FRAGSTATS 与 landscapemetrics，且以 FRAGSTATS 的指标定义为准）；`landscapemetrics` 是唯一在顶刊方法中被反复点名的开源替代品；PyLandStats、LecoS、motif 在本次抽样中**未被采用**。
- **生境/生态系统服务**：InVEST Habitat Quality 是中国生态安全格局类论文的标配（检索到的 2025 年应用论文几乎每篇都用），但在本次抽样的 Landscape Ecology / LUP 正刊论文中出现频率低于连通性工具；PLUS 在国土空间规划类应用中高频出现，多与 InVEST 耦合。
- **遥感与云平台**：Google Earth Engine 已成标配（J1、J7），ArcGIS 仍是应用型论文的主力 GIS 平台（Linkage Mapper 依赖它）；R（terra/sf/igraph 生态）与 Python（GDAL/栅格栈）并存，Julia 只在 Circuitscape/Omniscape 的方法引用中出现，作者本人多半不直接写 Julia。
- **中性景观与模拟**：NLMR、RangeShifter、LANDIS-II 在本次 8 篇抽样中**未被采用**；它们出现在更专门的模拟类期刊与方法论文中，而非主刊的实证连通性论文。

### 4.3 清单对照：哪些被顶刊采用、哪些没被采用

| 采用情况 | 项目 |
|---|---|
| 顶刊方法中明确采用 | Circuitscape.jl、Omniscape.jl、Graphab（及 R 封装 graph4lg）、FRAGSTATS（基准）、Conefor（基准/指标源）、landscapemetrics、Linkage Mapper（应用型论文高频）、InVEST、PLUS、Google Earth Engine（平台，非本表项目） |
| 本次抽样中未被采用，但有其他证据支持 | PyLandStats（有 PLOS ONE 方法论文与瑞士案例）、Makurhini（2026 年 EMS 方法论文）、NLMR（rOpenSci 同行评审包）、RangeShiftR（2025 年多篇应用）、LANDIS-II（森林模拟领域标准）、GuidosToolbox/MSPA（欧盟法规与 GFAD 生产流程采用）、DynamicPATCH（本刊方法论文 J3 自带） |
| 本次抽样中未被采用，且尚无顶刊采用证据 | landschaft、pyGuidos（除 GFAD 生产流程外）、circuitscaper、ALGR、NeutralLandscapes.jl、flsgen、nlmpy（老）、LS_METRICS、landscape-connectivity-pipelines、WS3、xLandscape、motif/comat（方法论文自引为主） |

### 4.4 从顶刊图幅提炼的可视化规范（3–5 条，附可信度）

以下规范的依据强度不一，逐条标注。总体限制：LUP 付费墙导致两篇 LUP 论文只能看到摘要页，图幅细节未逐图核对；J7（Nature Sustainability）全文 PDF 可读，是图幅观察的主要来源。

1. **多面板“证据链”版式（可信度：高）**：典型组织是“研究区图 → 阻力/电流密度图 → 情景对比图 → 指标统计图/表”的递进链；同一图内用 a/b/c/d 分面并列不同情景或物种（J1 对 28 个首都城市、J7 对全球生物群系分面、J4 对三情景并列）。**规范：每张图只讲一个递进环节，分面之间用同一底图、同一比例尺、同一图例。**
2. **廊道/电流图用顺序色带、类别图用定性色板（可信度：中）**：电流密度、连通性优先级等连续量用单色顺序渐变（低→高），土地覆被/格局类别用互不混淆的定性色；J7 的四类干扰格局在全球图上以类别色区分，并在分面条形图中复用同一配色。**规范：连续量不套彩虹色；类别色在全篇固定、图例与正文一致。**
3. **地图要素齐全是投稿硬门槛（可信度：中，基于期刊通用要求与可读到的图注）**：每幅地图带比例尺、指北针、图例与坐标参考说明；研究区图须标出行政/生态边界与关键地名。**规范：出图检查清单须含这四项，缺一不可；底图用浅灰地形或无底图，避免彩色卫星底图抢夺主题信息。**
4. **图与表分工明确（可信度：高，J7 表 2 为证）**：数值比较进表格（均值 ± 标准差、四类格局的指标统计），地图只表达空间分布；不在地图上堆数值标注。**规范：指标对比用表，空间格局用图；图注写清数据来源与年份（如 Hansen v1.6、2002–2014）。**
5. **开放获取与可复现声明（可信度：高）**：本次抽样 8 篇中有 5 篇开放获取（J1、J2、J3、J4、J5）；但“数据可应要求提供”（J4）仍多于公开代码仓，只有方法论文（J3）真正公开了代码。**规范：投稿时优先选 CC BY 开放获取，把代码与处理后数据挂公开仓（而非“on request”），这是顶刊正在收紧的方向。**

### 4.5 对工具选型的指导（高权重结论）

- **发顶刊优先选“方法部分点名率最高”的组合**：连通性用 Circuitscape.jl/Omniscape.jl + Graphab（或 graph4lg），格局指数用 FRAGSTATS 定义 + landscapemetrics 实现，生境用 InVEST，廊道应用用 Linkage Mapper——这套组合在抽样中零学习成本地被审稿人接受。
- **新工具要证明“与标杆一致”才能进顶刊**：landschaft、pyGuidos 的卖点恰好是“复现 FRAGSTATS/GuidosToolbox 的结果”，这是正确的进场策略；但在有独立第三方复核之前，不建议把它作为顶刊投稿的唯一计算链，可作交叉验证的第二链。
- **R 与 Python 不是对立面**：顶刊实证论文多为“GEE（分类）+ R（指标/图论）+ ArcGIS（制图/廊道）”的混合链；选型应按环节选工具，而不是按语言站队。

## 5. 选型建议与后续工作

1. **立即能用（Python，低门槛）**：`landschaft`（格局指数 + MSPA + 连通性一站式，但须先用真实数据复核指标一致性）、`PyLandStats`（稳健，需 GDAL 栈）、`nlmpy`/`NLMR`（中性景观对照实验）。
2. **R 工作流**：`landscapemetrics` + `Makurhini` + `graph4lg`（Graphab 的 R 封装）+ `motif`（格局签名）；连通性模拟再接 Circuitscape.jl。
3. **廊道规划实务**：Linkage Mapper（需 ArcGIS）+ Circuitscape.jl + Graphab；无 ArcGIS 时用 `circuitscaper`（R 调 Julia）或 landschaft 的电路模块作替代验证。
4. **生境与土地利用模拟**：InVEST（生境质量）+ PLUS（土地利用变化；注意其仓库只有 Windows exe，须从官网/论文渠道确认版本）+ WS3（森林木材供应，需林分数据与求解器）。
5. **形态学/法规合规**：pyGuidos（FAD/NRR 合规）+ GuidosToolbox/GWB（MSPA 标准实现）。
6. **后续验证缺口**：本机补装 R、Julia、Java 三大运行环境后，应优先补测 landscapemetrics、Makurhini、Circuitscape.jl、Graphab 四个旗舰；另需用真实景观（如 Corine 土地覆被子集）复核 landschaft 与 landscapemetrics 的指标一致性，验证其“逐位一致”宣传。

---
*报告生成方式：公开检索 + GitHub API（2026-11-14 快照）+ 本地浅克隆与实测；未查到的事实均已标注“未查到”，未编造数字与用例；期刊部分只记录方法与风格层面的观察，未复制原文或图片，引用仅给标题与 DOI。*
