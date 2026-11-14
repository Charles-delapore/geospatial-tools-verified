# 领域四：复杂空间分析与相关性建模（Advanced Spatial Analysis & Correlation Modeling）

**开源项目调研报告 · 核验日期：2026-11-14**

## 0. 方法与口径

- **范围**：多尺度 GWR 与地理加权回归、空间计量经济学、贝叶斯空间模型、空间因果推断、空间机器学习、地理加权方法、空间交互模型、空间自相关与聚类、地理探测器、地统计。
- **收录标准**：2024–2026 年仍活跃的项目优先，兼顾仍是行业标准的经典旗舰；最终收录 **28 个项目**（Python 18 + R 10），在任务目标 15–30 个之内。另有 2 个仓库 404、2 个已停滞项目记入第 7 节“存疑与未查到”，不计入 28 个。
- **元数据来源**：stars / forks / 许可证 / 最近推送均为 **2026-11-14 的 GitHub API 快照**（未认证接口）；许可证以仓库内 `LICENSE` / `DESCRIPTION` / `setup.py` 文件为准，API 返回 `NOASSERTION` / `None` 的已逐一按仓库文件纠正并在表中注明；PyPI / CRAN 发版号为同日查询。
- **代码验证**：28 个收录项目中 **27 个已 `git clone --depth 1` 到本报告配套目录 `repos/`**（r-inla 的 `devel` 分支克隆失败两次，见第 5 节；`repos/` 下实为 27 个目录，无 r-inla 副本——原草稿“全部 28 个均已 clone”的说法有误，已由接续核查修正）。Python 项目在独立 venv（Python 3.12，numpy 2.5.4 / scipy 1.16.3 / pandas 3.1.1 / scikit-learn 1.9.1 / matplotlib 3.11.2）中从克隆源码安装并运行合成数据小例子；**本机无 R / Rscript**，10 个 R 项目只能做克隆 + 读代码 + CRAN 元数据核验，报告中如实记为“未实测（无 R 环境）”。
- **不编造原则**：所有数字与用例均有来源；查不到的写“未查到”。同名项目已区分（如 `opengeos/geoai` 是通用 GeoAI 框架，与空间统计核心仅部分相关；`geoshapley` 以 `Ziqi-Li/geoshapley` 为准，另有他人 fork）。
- **期刊标杆**：见第 6 节。抽样 4 本期刊、11 篇 2024–2026 年文章（优先开放获取全文），只记录方法与风格层面的观察，不复制原文大段文字或图片；引用仅给标题与 DOI。

## 1. 总览与选型地图

| 子领域 | 项目（★= 2024–2026 新活跃 / 新发现） | 选型要点 |
|---|---|---|
| 地理加权回归（GWR/MGWR） | mgwr、GWmodel（停滞，CRAN 仍在）、mgwnbr、stgam★、PyGALAX★ | 经典统计路线用 mgwr / GWmodel；计数数据用 mgwnbr；GAM 路线用 stgam |
| 空间自相关与聚类 | esda、spdep、spatialreg | Python 用 esda（PySAL），R 用 spdep + spatialreg |
| 空间计量经济学 | spreg、spatialreg、geocausal★（因果） | spreg 是 PySAL 的空间回归主力；geocausal 是 2024–2026 新兴的空间因果 R 包 |
| 贝叶斯空间模型 | r-inla、inlabru（注脚）、ST-HCMs★（论文配套代码） | INLA 仍是贝叶斯空间模型事实标准，但本机未克隆成功 |
| 空间因果推断 | geocausal★、ST-HCMs★ | 2024–2026 最活跃的新方向，但工具仍少且多为论文配套代码 |
| 空间机器学习 | spml★、PyGRF、PyGALAX★、geoshapley★、geoai | spml（PySAL 2025 改名）是官方新旗舰；geoshapley 是解释性工具 |
| 空间交互模型 | spint、PyTDLM★ | spint 是经典引力模型库；PyTDLM（2025）是出行分布定律的系统比较工具 |
| 地理探测器 | gdverse、GD（geodetector 后继） | R 生态；gdverse 是整合包，GD 是核心算法包 |
| 地统计 | GSTools、PyKrige、pyinterpolate、scikit-gstat、verde、spatialize★ | GSTools + PyKrige 是双旗舰；spatialize 是 2024–2026 新活跃的并行克里金 |
| 空间交叉验证 | blockCV | R 包，2026-09 发 4.0-1，空间分块 CV 的标准工具 |
| 图神经网络 / 空间网络 | City2Graph★ | CEUS 2026 论文配套 Python 库，1985 stars，增长最快的新工具 |

**一句话结论**：经典旗舰（mgwr / esda / spreg / GSTools / PyKrige / spdep / INLA）仍是顶刊与生产环境的默认选择；2024–2026 的新增长集中在三处——**空间机器学习**（spml、geoshapley、PyGALAX）、**空间因果推断**（geocausal、ST-HCMs）与**图方法**（City2Graph）；地统计出现并行化新选手 spatialize；地理探测器已完成向 gdverse 的整合。

## 2. 项目总表

stars / 最近推送为 2026-11-14 GitHub API 快照；许可证以仓库文件为准；“验证”栏见第 5 节。

| # | 项目 | 仓库 | 语言 | 许可证 | Stars | 最近推送 | 最新发版 | 用途一句话 | 验证状态 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | mgwr | [pysal/mgwr](https://github.com/pysal/mgwr) | Python | BSD-3 | 438 | 2026-10-14 | PyPI 2.2.1 (2024-01-06) | 多尺度地理加权回归（MGWR/GWR） | ✅ 通过（接续复跑，见 §5） |
| 2 | esda | [pysal/esda](https://github.com/pysal/esda) | Python | BSD-3 | 263 | 2026-11-13 | PyPI 2.10.0 (2026-06-19) | 探索性空间数据分析：Moran's I、LISA、Geary 等 | ✅ 通过（接续复跑，见 §5） |
| 3 | spreg | [pysal/spreg](https://github.com/pysal/spreg) | Python | BSD-3（仓库 LICENSE.txt；API 误标 NOASSERTION） | 89 | 2026-11-11 | PyPI 1.9.2 (2026-11-09) | 空间回归：空间滞后/误差、GMM、内生性检验 | 未实测（无存档记录） |
| 4 | spint | [pysal/spint](https://github.com/pysal/spint) | Python | BSD-3 | 58 | 2026-10-13 | PyPI 1.1.0 (2026-06-17) | 空间交互：引力模型、辐射模型、PWO 等 | 未实测（无存档记录） |
| 5 | spml | [pysal/spml](https://github.com/pysal/spml)（曾用名 gwlearn） | Python | BSD-3 | 50 | 2026-11-12 | PyPI 0.2.2 (2026-06-25) | PySAL 官方空间机器学习：地理加权 RF/GBM/线性模型、空间 CV | ⚠️ 部分通过（fit 可跑，predict 报错，见 §5） |
| 6 | PyGRF | [geoai-lab/PyGRF](https://github.com/geoai-lab/PyGRF) | Python | GPL-3.0 | 68 | 2025-08-19 | 未上 PyPI（单文件包 + 笔记本） | 地理随机森林（GRF）的改进 Python 实现 | 未实测（无存档记录） |
| 7 | PyGALAX | [Pingping9/PyGALAX](https://github.com/Pingping9/PyGALAX) | Python | BSD-3 | 7 | 2026-07-27 | 未上 PyPI | 地理加权 AutoML（FLAML 驱动的局部模型搜索） | 未实测（无存档记录） |
| 8 | geoshapley | [Ziqi-Li/geoshapley](https://github.com/Ziqi-Li/geoshapley) | Python | MIT（setup.py；仓库无 LICENSE 文件） | 219 | 2026-10-21 | PyPI 0.2.1.1 (2026-10-21) | 用 Shapley 值度量任意 ML 模型的空间效应与空间变系数 | 未实测（无存档记录） |
| 9 | GSTools | [GeoStat-Framework/GSTools](https://github.com/GeoStat-Framework/GSTools) | Python | LGPL-3.0 | 664 | 2026-10-13 | PyPI 1.7.0 (2025-04-28) | 地统计：随机场生成、变差函数、克里金、条件模拟 | ✅ 通过（接续复跑确认，见 §5） |
| 10 | PyKrige | [GeoStat-Framework/PyKrige](https://github.com/GeoStat-Framework/PyKrige) | Python | BSD-3 | 869 | 2025-10-16 | PyPI 1.7.3 (2025-10-16) | 克里金插值工具箱（普通/泛/回归克里金） | 未实测（无存档记录） |
| 11 | pyinterpolate | [DataverseLabs/pyinterpolate](https://github.com/DataverseLabs/pyinterpolate) | Python | 存疑：LICENSE.md 条款文本与 BSD-3 一致，但 pyproject 分类标 MIT（接续核查，见 §7） | 175 | 2026-05-23（仓库内最新提交 2025-12-26） | PyPI 1.2.1 (2025-12-26) | 空间插值：变差函数、克里金、面积-点插值 | 未实测 |
| 12 | verde | [fatiando/verde](https://github.com/fatiando/verde) | Python | BSD-3 | 677 | 2026-11-11 | PyPI 1.9.0 (2026-03-19) | 空间数据处理与插值（样条、块均值、网格化） | 未实测（无存档记录） |
| 13 | spatialize | [alges/spatialize](https://github.com/alges/spatialize) | Python (+C++) | Apache-2.0 | 6 | 2026-10-27 | PyPI 1.3.0 (2026-10-23) | 并行空间插值：ESI/克里金，C++ 内核 | 未实测（无存档记录） |
| 14 | scikit-gstat | [mmaelicke/scikit-gstat](https://github.com/mmaelicke/scikit-gstat) | Python | MIT | 254 | 2026-10-28 | PyPI 1.0.27 (2026-10-28) | 变差函数估计与地统计建模（scikit-learn 风格 API） | 未实测（无存档记录） |
| 15 | PyTDLM | [RTDLM/PyTDLM](https://github.com/RTDLM/PyTDLM) | Python | GPL-3.0（仓库 LICENSE 为 GPL v3 全文） | 1 | 2026-09-22 | PyPI 0.2.2 (2026-03-24) | 出行分布定律与模型的系统比较（引力/辐射/机会模型） | 未实测（无存档记录） |
| 16 | geoai | [opengeos/geoai](https://github.com/opengeos/geoai) | Python | MIT | 3473 | 2026-11-09 | 仓库 pyproject 标 0.43.1（PyPI 未单独复核） | 通用 GeoAI 框架（遥感深度学习、分割、检测等） | 仅静态核查 |
| 17 | ST-HCMs | [CAMELLIAxt/ST-HCMs](https://github.com/CAMELLIAxt/ST-HCMs) | Python | 未查到（仓库无 LICENSE 文件） | 2 | 2025-10-15 | 无发版（论文配套代码） | 时空分层因果模型（论文仿真 + 芝加哥事故案例） | 仅静态核查 |
| 18 | City2Graph | [c2g-dev/city2graph](https://github.com/c2g-dev/city2graph) | Python | BSD-3 | 1985 | 2026-11-08 | PyPI 1.1.0 (2026-11-08) | 把地理空间关系转为图，供 GNN 与空间网络分析 | 仅静态核查 |
| 19 | gdverse | [stscl/gdverse](https://github.com/stscl/gdverse) | R | GPL-3（DESCRIPTION） | 104 | 2026-06-09 | CRAN 1.6 | 地理探测器整合包（geodetector/GD 的后继） | 未实测（无 R） |
| 20 | GD | [ausgis/GD](https://github.com/ausgis/GD) | R | GPL-3（DESCRIPTION；CRAN 标 GPL-3，v10.9，2026-02-27） | 20 | 2026-02-27 | CRAN 10.9 (2026-02-27) | 地理探测器核心算法（因子/交互/风险/生态探测器） | 未实测（无 R） |
| 21 | GWmodel | [lbb220/GWmodel](https://github.com/lbb220/GWmodel) | R | GPL ≥2（DESCRIPTION） | 26 | 2022-06-15（GitHub 已停滞；克隆 master 最新提交 2021-04-12） | CRAN 2.4-1 (2024-09-07) | R 的地理加权模型全家桶（GWR/GW PCA/判别等） | 未实测（无 R） |
| 22 | mgwnbr | [julianamrosa/mgwnbr](https://github.com/julianamrosa/mgwnbr) | R | GPL-3（DESCRIPTION） | 0 | 2025-10-01 | CRAN 0.3.0 | 多尺度地理加权负二项回归（计数数据） | 未实测（无 R） |
| 23 | geocausal | [mmukaigawara/geocausal](https://github.com/mmukaigawara/geocausal) | R | MIT（DESCRIPTION 标 MIT + file LICENSE） | 73 | 2026-11-02 | CRAN 0.4.2 (2026-06-26) | 时空数据因果推断（干预效应、政策学习） | 未实测（无 R） |
| 24 | blockCV | [rvalavi/blockCV](https://github.com/rvalavi/blockCV) | R | GPL ≥3（DESCRIPTION） | 149 | 2026-10-13 | CRAN 4.0-1 (2026-09-22) | 空间与环境分块交叉验证 | 未实测（无 R） |
| 25 | spdep | [r-spatial/spdep](https://github.com/r-spatial/spdep) | R | GPL ≥2（DESCRIPTION） | 151 | 2026-11-03 | CRAN 1.4-2 (2026-02-13) | 空间依赖：权重矩阵、Moran's I、LISA 等 | 未实测（无 R） |
| 26 | spatialreg | [r-spatial/spatialreg](https://github.com/r-spatial/spatialreg) | R | GPL-2（DESCRIPTION） | 55 | 2026-11-03 | CRAN 1.4-3 (2026-03-20) | 空间回归分析（SAR/SEM/SDM 等） | 未实测（无 R） |
| 27 | r-inla | [hrue/r-inla](https://github.com/hrue/r-inla) | R | MIT | 132 | 2026-11-13 | 非 CRAN 发行（官网 inla.r-inla-download.org） | 贝叶斯潜高斯模型的 INLA 近似推断 | 未克隆，未实测 |
| 28 | stgam | [lexcomber/stgam](https://github.com/lexcomber/stgam) | R | MIT（DESCRIPTION 标 MIT + file LICENSE） | 7 | 2026-08-19 | CRAN 1.2.1 | 用 GAM 平滑项做时空变系数模型（GGP-GAM 的配套包） | 未实测（无 R） |

> 注：`pysal/libpysal`（294 stars，2026-11-12 推送）是 PySAL 的基础设施（权重、IO、CG），不单独计入 28 个；`inlabru`（132 stars，2026-10-23 推送，CRAN 2.15.0）是 r-inla 的配套前端，同样作注脚。`FastGWR`（64 stars，最后推送 2022-03-17）已停滞，仅作对比，不计入。

## 3. 重点项目深挖

> 本节为接续补写（2026-11-14）。每个项目写清用途、采用者与实测情况；未查到的写“未查到”，不推断。

### 3.1 mgwr（`pysal/mgwr`，Python，BSD-3，438 stars）

- **用途**：多尺度地理加权回归（MGWR）与传统 GWR 的 Python 实现。支持高斯 / Poisson / 二项模型的 GWR 校准（迭代加权最小二乘）、黄金分割或等距搜索选带宽、GWR 诊断（含多重假设检验校正与局部共线性）、空间变异性 Monte Carlo 检验、GWR 空间预测；MGWR 用 GAM 迭代 backfitting 校准（仅高斯模型），提供协变量专属推断与带宽置信区间，支持并行计算。基于 `spglm` 模块。
- **方法论文**：Oshan, Li, Kang, Wolf & Fotheringham (2019), *ISPRS International Journal of Geo-Information* 8(6):269，DOI 10.3390/ijgi8060269。
- **采用者**：PySAL 官方旗舰之一；顶刊抽样中 IJGIS 2026 的 TabPFN-GSA 研究把 MGWR 列为最强基线之一（合成数据上 MGWR 表现最好），见 §6.1。注意 §6.3 的提醒：顶刊作者常用 MGWR 思想，但不一定用 `pysal/mgwr` 这个包实现。
- **实测情况**：✅ 通过（接续复跑，见 §5.1）。5×5 合成格网、自适应带宽 8 近邻的 GWR 拟合 R²=0.974。**注意**：`y` 须为 `(n,1)` 形状；传一维 `(n,)` 会在 `_local_fit` 的 `np.dot(self.X[i], betas)[0]` 处报 `IndexError: invalid index to scalar variable`（本轮初次复跑即因此报错，改形状后通过；属调用方式问题，非包本身缺陷）。

### 3.2 GSTools + PyKrige（地统计双旗舰）

**GSTools**（`GeoStat-Framework/GSTools`，Python，LGPL-3.0，664 stars）：

- **用途**：地统计全流程——随机场生成（SRF）、变差函数估计与拟合、普通/泛克里金、条件模拟、时空模型。配套论文发表于 *Geoscientific Model Development*（GMD 15:3161–2022，DOI 10.5194/gmd-15-3161-2022）。
- **采用者**：GeoStat-Framework 生态的核心库；与 PyKrige、scikit-gstat 同为地统计领域的 Python 事实标准（本报告 §1 选型要点）。顶刊抽样中克里金思想被 Geographical Analysis 2025 的半变差函数克里金研究采用，但实现为 R 的 `gstat`，而非本清单的 Python 包（见 §6.3）。
- **实测情况**：✅ 通过（原轮已通过，接续复跑确认，见 §5.1）。40 个随机点合成高斯随机场：变差函数拟合 var≈1.30、len_scale≈3.42（真值 1.0 / 3.0），5×5 网格普通克里金正常输出。

**PyKrige**（`GeoStat-Framework/PyKrige`，Python，BSD-3，869 stars）：

- **用途**：克里金插值工具箱，支持 2D/3D 普通与泛克里金；内置线性、幂、球状、高斯、指数等标准变差函数模型，也支持自定义变差函数；2D 泛克里金支持区域线性、点对数与外部漂移项，3D 支持三维区域线性漂移。是本清单中 stars 最高的纯地统计包（869）。
- **采用者**：未查到顶刊抽样文章点名采用本包的记录（抽样中克里金实现为 R 的 gstat，见 §6.3）；作为 GeoStat-Framework 的老牌工具箱，在教学与工程插值中广泛使用（具体采用者名录未在本轮逐一核查，记“未查到”）。
- **实测情况**：未实测（无存档记录）。仓库已克隆，代码已读；未在本轮运行——PyKrige 未装入 venv，如需复跑需另行安装。

### 3.3 spml（`pysal/spml`，曾用名 gwlearn，Python，BSD-3，50 stars）

- **用途**：PySAL 官方空间机器学习包（2025 年由 gwlearn 改名，README 自述当前为 beta，核心 API 不应大变）。基于 scikit-learn 与 `libpysal.graph`，提供地理加权扩展的回归/分类模型原型框架：地理加权线性回归、地理加权随机森林/梯度提升等，以及空间交叉验证。README 示例用 `GWLinearRegression(bandwidth=25, fixed=False, kernel="bisquare")` 在 Guerry 数据上拟合。
- **采用者**：PySAL 官方新旗舰定位，但 stars 仅 50、PyPI 0.2.2（2026-06-25），属 2024–2026 新兴工具；顶刊抽样中未出现（见 §6.3），存在采用滞后。Zenodo DOI 10.5281/zenodo.18173180。
- **实测情况**：⚠️ 部分通过（接续复跑，见 §5.2）。40 个合成点上 `GWLinearRegression.fit()` 可正常运行、无报错，但拟合后未生成局部系数（`coef_` 为空、`_local_models` 属性缺失），随后 `predict()` 报 `AttributeError: 'GWLinearRegression' object has no attribute '_local_models'`。疑似开发版（0.1.dev1+g85151c9b，从克隆源码安装）未完成或本轮调用方式与文档示例有出入；**不记为完全通过**，生产使用前应以 PyPI 发版 0.2.2 或官方 Guerry 示例复核。

### 3.4 City2Graph（`c2g-dev/city2graph`，Python，BSD-3，1985 stars）

- **用途**：把建筑、街道、公共交通（GTFS/GBFS）、OD 矩阵、分区与 POI 等地理空间数据转为空间图与异构图，桥接 GeoPandas、NetworkX 与 PyTorch Geometric，服务空间网络分析、城市分析与图神经网络（GNN）。功能包括城市形态图（OSM / Overture Maps）、合成 GTFS 生成与 DuckDB 存取、KNN / Delaunay / Gilbert / Waxman 图、queen/rook 邻接、异构图与元路径、GNN 张量往返转换。支持 Python 3.12–3.14。
- **方法论文**：CEUS 2026，Sato 等，DOI 10.1016/j.compenvurbsys.2026.102492（本报告 §6 抽样衍生纳入）。
- **采用者**：本清单中增长最快的新工具（1985 stars，2026-11-08 刚发 1.1.0）；顶刊抽样中其配套论文本身即为 CEUS 2026 文章（见 §6.1 抽样说明）。其对位趋势是 §6.3 指出的顶刊前沿——把空间结构（图、位置编码、空间 CV）放进深度学习 pipeline。
- **实测情况**：仅静态核查。仓库已克隆、README 已读；未运行——完整功能依赖 PyTorch / PyTorch Geometric，未在本机 venv 安装（体积大、耗时长），仅 `pip install city2graph` 的基础安装亦未在本轮执行。

### 3.5 esda（`pysal/esda`，Python，BSD-3，263 stars）

- **用途**：PySAL 的探索性空间数据分析包：全局/局部 Moran's I、Geary's C、Getis-Ord、LISA 聚类等空间自相关与聚类方法，是 Python 空间统计的基础设施。
- **采用者**：PySAL 生态通用基础设施；顶刊抽样中 Moran's I 类方法未作为核心方法出现（见 §6.3），但为领域通用工具。
- **实测情况**：✅ 通过（接续复跑，见 §5.1）。5×5 合成格网（带空间趋势）Moran's I=0.185，p=0.070（99 次置换）。另注意：本轮运行时出现 `DeprecationWarning`——下一大版本将把置换检验的默认备择假设改为 `'two-sided'`（会使 p 值翻倍），建议显式设置 `alternative='two-sided'` 或 `'directed'`。

## 4. 选型建议与使用路线

> 本节为接续补写（2026-11-14），综合 §1、§3、§6 的证据给出路线建议，不引入未核查的新项目。

| 任务 | 首选 | 备选 / 说明 |
|---|---|---|
| 空间变系数回归（连续因变量） | mgwr（Python）或 GWmodel（R，CRAN 为准） | 计数数据用 mgwnbr（R）；GAM 路线用 stgam（R） |
| 空间自相关 / LISA 探索 | esda（Python） | R 用 spdep |
| 空间回归（SAR/SEM/SDM、内生性） | spreg（Python） | R 用 spatialreg；两者均未在本轮实测，选型以文档与生态为准 |
| 贝叶斯空间模型 | r-inla（R，官网发行） | 本机未克隆成功、无 R 实测；部署前须在有 R 的环境复核 |
| 地统计 / 克里金 | GSTools（已实测通过）+ PyKrige | 变差函数建模可用 scikit-gstat；并行插值看 spatialize（仅 6 stars，尚新） |
| 空间机器学习 | spml（PySAL 官方，beta） | 注意 §5.2 的部分通过结论：先用 PyPI 发版 0.2.2 与官方示例复核再上生产；解释性工具配 geoshapley |
| 空间因果推断 | geocausal（R） | 工具少且多为论文配套代码（ST-HCMs）；方法新、生态未稳 |
| 地理探测器 | gdverse（R，整合包） | 核心算法 GD；均为 R 生态 |
| 空间交叉验证 | blockCV（R，CRAN 4.0-1） | 做空间 ML 时必配，避免随机 CV 高估 |
| 图 / GNN 的空间图构建 | City2Graph | 仅静态核查；需 PyTorch Geometric 环境 |

**三条路线**：(1) **经典统计路线**：esda + spreg + mgwr + GSTools/PyKrige（Python）或 spdep + spatialreg + GWmodel + gstat（R），顶刊与生产环境的默认选择；(2) **空间 ML 路线**：spml + geoshapley + blockCV，配 City2Graph 做图输入；(3) **贝叶斯 / 因果前沿路线**：r-inla + geocausal + ST-HCMs，工具最新但验证最少，适合方法学探索而非生产。

## 5. 验证小结

### 5.1 本轮复跑（接续核查，2026-11-14）

复跑环境与附录 A 一致（Python 3.12.3，venv 内 numpy 2.5.4 / scipy 1.16.3 / pandas 3.1.1 / scikit-learn 1.9.1 / matplotlib 3.11.2；scipy 现为 1.16.3，系 scikit-gstat 要求 scipy<1.17、pip 自动降级所致）。复跑脚本已改存于报告配套目录 `verify/`（`test_gstools.py`、`test_esda_only.py`、`test_mgwr_only.py`、`test_spml.py`、`test_spml_fitonly.py`），不再放在 `/tmp`（原 `/tmp/verify_tests/` 已随运行时重启丢失，见接续说明）。全部使用合成小数据（n=25–40），不依赖外部数据文件。

| 项目 | 结果 | 证据 |
|---|---|---|
| GSTools | ✅ 通过 | 40 点合成高斯随机场：变差函数拟合 var≈1.30、len_scale≈3.42（真值 1.0/3.0）；5×5 网格普通克里金正常输出，均值 0.682 |
| esda | ✅ 通过 | 5×5 合成格网 Moran's I=0.185，p=0.070（99 次置换）；附 DeprecationWarning（备择假设默认值将变，见 §3.5） |
| mgwr | ✅ 通过 | 5×5 合成格网、自适应带宽 8 近邻 GWR 拟合 R²=0.974；初次复跑因 `y` 传一维形状报错，改 `(n,1)` 后通过（见 §3.1） |
| spml | ⚠️ 部分通过 | 见 §5.2 |

### 5.2 未通过 / 部分通过

| 项目 | 状态 | 原因 |
|---|---|---|
| spml | ⚠️ 部分通过 | `GWLinearRegression.fit()` 可运行，但拟合后无局部系数（`coef_` 为空、`_local_models` 缺失），`predict()` 报 `AttributeError: 'GWLinearRegression' object has no attribute '_local_models'`。从克隆源码安装的开发版 0.1.dev1+g85151c9b；疑似开发版未完成或调用方式与文档示例有出入，未以 PyPI 发版 0.2.2 复核 |
| r-inla | ❌ 未克隆，未实测 | `git clone --depth 1 --branch devel` 两次重试均失败（网络超时），`repos/` 下无本地副本；元数据以 GitHub API（132 stars，2026-11-13 推送，MIT）与官网发行渠道为准 |

### 5.3 验证总账（28 个项目）

| 类别 | 数量 | 项目 |
|---|---|---|
| ✅ 实测通过 | 3 | mgwr、esda、GSTools（本轮复跑；GSTools 原轮已通过，本轮复跑确认） |
| ⚠️ 部分通过 | 1 | spml |
| 仅静态核查（克隆 + 读代码/README，未运行） | 3 | geoai、ST-HCMs、City2Graph |
| 未实测（无存档记录） | 10 | spreg、spint、PyGRF、PyGALAX、geoshapley、PyKrige、pyinterpolate、verde、spatialize、scikit-gstat（Python；原轮“待填”状态无存档测试记录可核，统一改记为未实测） |
| 未实测（无 R 环境） | 9 | gdverse、GD、GWmodel、mgwnbr、geocausal、blockCV、spdep、spatialreg、stgam（R，已克隆） |
| 未克隆，未实测 | 1 | r-inla（R；另计入“未实测无 R”类则 R 未实测共 10 个） |
| **合计** | **28** | Python 18 + R 10（与 §0 收录口径一致；本地克隆副本为 27 个） |

**重要说明**：venv 中已从源码安装的包有 esda、geoshapley、gstools、mgwr、scikit-gstat、spint、spml、verde（另 spreg 为 PyPI 版 1.9.2），但**安装成功 ≠ 功能通过**；本轮仅对其中的 4 个做了复跑（3 通过 + spml 部分通过），其余已安装未复跑的仍记“未实测”。R 项目 10 个均未实测的根本原因是本机无 R/Rscript（附录 A），非项目本身问题；GWmodel 另有 GitHub 停滞但 CRAN 仍在发版的情况（见 §7），R 用户应以 CRAN 为准。

## 6. 期刊标杆：顶刊在用什么、图怎么画

**抽样方法**：4 本期刊（IJGIS、Geographical Analysis、Computers, Environment and Urban Systems、Nature Communications），各抽 2–3 篇 2024–2026 年代表性文章，共 11 篇，优先开放获取全文。只记录方法与风格层面的观察，不复制原文与图片。

### 6.1 抽样文章一览

| 期刊 | 文章（年份） | 技术栈 | 图幅 | 代码/数据 |
|---|---|---|---|---|
| IJGIS | Deng, Li & Wang (2026)《Do foundation models work for geospatial tabular data? An investigation of TabPFN and a proposed enhancement based on geospatial sparse attention》，DOI [10.1080/13658816.2026.2691066](https://doi.org/10.1080/13658816.2026.2691066) | TabPFN（PriorLabs）+ 自研 TabPFN-GSA；7 个基线：MLR、GWR、MGWR、XGBoost、PyGRF、GCNNWR、GeoAggregator；合成 DGP 含 Lin/GWR/SLX/SL/SD | 正文 8 幅（架构图、R² 性能曲线、注意力权重分布/热图、GSA 示意图、超参数敏感性曲线）+ 附录系数地图 A1/A2；多为折线/散点性能图，非地图 | 代码 GitHub `ruid7181/TabPFN-GSA`；数据 figshare DOI 10.6084/m9.figshare.31123945 |
| IJGIS | Wu, Du, Wei & Xiao (2026)《An efficient calibration algorithm for multiscale geographically and temporally weighted regression》，DOI [10.1080/13658816.2026.2623155](https://doi.org/10.1080/13658816.2026.2623155) | MGTWR_2SCALL（基于局部线性拟合的两步校准，替代 backfitting）；案例 2014–2021 年中国碳排放 | 未查到（全文细节未获） | 未查到 |
| IJGIS | Comber, Harris & Brunsdon (2024)《Multiscale spatially varying coefficient modelling using a Geographical Gaussian Process GAM》，IJGIS 38(1):27–47，DOI [10.1080/13658816.2023.2270285](https://doi.org/10.1080/13658816.2023.2270285) | R 的 mgcv 包（GAM + 高斯过程样条）+ 自研 R 包 stgam；与 MGWR 对比，GGP-GAM 多项拟合指标优于 MGWR | 未逐一统计 | R 包 stgam（本报告第 28 号） |
| Geogr. Anal. | Boeing (2025)《Modeling and Analyzing Urban Networks and Amenities With OSMnx》，DOI [10.1111/gean.70009](https://doi.org/10.1111/gean.70009) | OSMnx（纯 Python，NetworkX / GeoPandas 生态） | 仅 3 幅：图 1 街道网络简化前后对比、图 2 极坐标直方图 + 对应街道地图、图 3 一平方英里 figure-ground 图；图 2、图 3 为转载旧图 | OSMnx 为开源 Python 包 |
| Geogr. Anal. | Finne & Sauzet (2025)《Feasibility of Using Survey Data and Semi-variogram Kriging to Obtain Bespoke Indices of Neighborhood Characteristics》，57(1):3–26，DOI [10.1111/gean.12401](https://doi.org/10.1111/gean.12401) | 半变差函数克里金（仿真 + RECORD 研究案例）；配套 R 包 EgoCor（基于 gstat） | 未读全文，图幅未统计 | R 包 EgoCor（CRAN 1.3.4，MIT） |
| CEUS | Wang 等 (2025)《Multi-modal contrastive learning of urban space representations from POI data》（CaLLiPer），120:102299，DOI [10.1016/j.compenvurbsys.2025.102299](https://doi.org/10.1016/j.compenvurbsys.2025.102299) | PyTorch 2.2.2、Gensim（TF-IDF/LDA/Doc2Vec）、Sentence-Transformers（all-MiniLM-L6-v2）、Llama3-8B；基线 Place2Vec、SPPE、SpaBERT、Urban2Vec、HGI、Space2Vec；下游 Linear + MLP | 已确认图 3 为伦敦六边形网格 K-Means 聚类地图；全文图幅总数未完全核对 | 代码 GitHub `xlwang233/CaLLiPer` |
| CEUS | Liang, Zhu, Ye & Gao (2025)《GeoAI-enhanced community detection on spatial networks with graph deep learning》（region2vec），117:102228，DOI [10.1016/j.compenvurbsys.2024.102228](https://doi.org/10.1016/j.compenvurbsys.2024.102228) | GCN/GAT 图神经网络 + 凝聚聚类；基线 Louvain、Leiden、Node2vec、DeepWalk、LINE、K-Means；SafeGraph + 美国社区调查（ACS），Rook 邻接 | 共 5 幅：图 1 方法流程、图 2 三指标 3D 图、图 3 敏感性分布、图 4 各方法社区地图（14 个社区，分色）、图 5 威斯康星 HPSA 缺医地区图（绿色 + 透明度表征得分） | 代码 GitHub `GeoDS/region2vec-GAT` |
| CEUS | Zhao 等 (2026)《UST-GNN: A unified spatial–topological graph neural network framework for urban analytics》，129:102466，DOI [10.1016/j.compenvurbsys.2026.102466](https://doi.org/10.1016/j.compenvurbsys.2026.102466) | GNN（GCN/GIN/GraphSAGE/GATv2）+ 位置/地点编码（Laplacian、随机游走位置编码、SatCLIP）+ 严格空间交叉验证；基线含梯度提升树、空间滞后模型、GWR 与 geo-informed ML；数据 MedSAT（大伦敦 4835 个邻里、150+ 变量、6 种处方结局）；R² 提升 8.4–13.2% | 正文至少 6 幅（图 1 方法总览 A–E 五步、图 5 邻接构建消融、图 6 抑郁处方预测 vs 观测 + 折叠稳定性、图 8 PCA 嵌入解释地图）+ 附录图 B.11/B.12 | 未查到公开代码仓库（Data availability 段称作者在审稿回复中分享了 figshare 数据/代码链接，未在正文中给出公开链接） |
| Nat. Commun. | Zhang 等 (2025)《High frequency of moraine-dammed lake outburst floods driven by global warming》，16:11173，DOI [10.1038/s41467-025-67650-3](https://doi.org/10.1038/s41467-025-67650-3) | **GWR 在 ArcGIS 中实现**（自适应高斯核，AICc 选带宽），Poisson GAM 做趋势分析；数据 1°×1° 格网聚合 | 图 1 全球分布图（1° 瓦片圆圈按数量缩放 + 饼图分来源，底图 Natural Earth 公共领域）、图 2 灾害等级地图 + 十年趋势、图 3 GWR 局部系数图（系数 0–1.5 量级） | 仅趋势分析的 PoissonGAM 代码公开（GitHub `Taigang1/GLOF`）；GWR 本身无开源代码链接；数据 Zenodo DOI 10.5281/zenodo.14643434 |
| Nat. Commun. | Zhu 等 (2026)《Optimized spatial planning offers a dual solution for managing urban heat and air pollution in humid subtropical climates》，DOI [10.1038/s41467-026-73855-x](https://doi.org/10.1038/s41467-026-73855-x) | GWR（连接土地利用与目标函数）+ NSGA-III 多目标优化 + WRF-GC 气候化学耦合模型；GWR 具体实现软件未提及 | 正文 4 幅：图 1 散点密度图（红拟合线 + 黑 1:1 线，n=9967）、图 2 六面板地图（无规划 A/C/E vs 优化 B/D/F：开发频率、建成密度、绿地比例，红框标两处重点开发区）、图 3 箱线图（T2/PM2.5/O₃/ESV，400 个方案散点）+ 图 4 | 代码 GitHub `LiuhuaZhu1/urban_planning_optimization` + WRF-GC 官方仓库；源数据随文提供 |
| Nat. Commun. | Xu 等 (2025)《Predicting human mobility flows in cities using deep learning on satellite imagery》，16:10372，DOI [10.1038/s41467-025-65373-z](https://doi.org/10.1038/s41467-025-65373-z) | Imagery2Flow：自监督深度学习编码卫星影像 + 图注意力网络；基线含传统物理模型、XGBoost、LGBM；Sentinel-2 / Landsat-8，美国十大都会区，人口普查 tract 为单元，LODES 通勤流为真值 | 图 1 架构总览；多幅预测 vs 观测对比图 | 代码 GitHub `GeoDS/Imagery2Flow` |

> 抽样说明：Geographical Analysis 的 Finne & Sauzet (2025) 未读全文，方法细节以摘要与配套 EgoCor 包说明为准；IJGIS 的 Wu (2026) 未获全文细节，代码/数据记“未查到”。另发现两项期刊衍生的新工具候选已纳入主清单：City2Graph（CEUS 2026，Sato 等，DOI 10.1016/j.compenvurbsys.2026.102492）与 stgam（IJGIS 2024，Comber 等）。

### 6.2 顶刊实际在用的空间分析技术栈

1. **统计基线仍是 GWR/MGWR，但实现方式分裂**：IJGIS 的 TabPFN-GSA 研究把 MGWR 当作最强基线之一（合成数据上 MGWR 表现最好）；Nature Communications 的两篇应用文章直接用 GWR（其一在 ArcGIS 中实现，其一未注明实现）。这意味着 **MGWR 的方法地位高于其软件地位**——顶刊作者用 MGWR 思想，但不一定用 `pysal/mgwr` 这个包。
2. **空间机器学习已成标配基线**：XGBoost、随机森林、GCNNWR、GeoAggregator、PyGRF 在 IJGIS 2026 的基准测试中与 TabPFN 同台；CEUS 的三篇文章全部以 GNN/对比学习为主方法，传统模型只作基线。
3. **图方法崛起**：CEUS 2025–2026 的 region2vec 与 UST-GNN、Nature Communications 的 Imagery2Flow 均以图神经网络为核心；City2Graph（GeoPandas + NetworkX + PyTorch Geometric）正是为这类工作提供图构建基础设施。
4. **R 生态在方法学期刊仍占一半**：IJGIS 的 GGP-GAM（mgcv + stgam）、Geographical Analysis 的半变差函数克里金（gstat / EgoCor）均以 R 为主；Python 阵地在 CEUS 与 Nature Communications 的应用型文章中更强。
5. **代码公开率约 8/11**：11 篇中有 8 篇给出公开代码仓库（GitHub 为主），2 篇未查到（Wu 2026 MGTWR；Zhao 2026 UST-GNN，仅提及审稿阶段 figshare 链接），1 篇仅部分公开（GLOF 的 GWR 部分无代码）。数据公开以 figshare / Zenodo 为主。

### 6.3 清单工具的顶刊采用对照

| 采用情况 | 项目 |
|---|---|
| **被顶刊抽样文章直接采用** | mgwr（MGWR 作基线，IJGIS 2026）、PyGRF（基线，IJGIS 2026）、City2Graph（CEUS 2026 论文配套库）、stgam（IJGIS 2024 论文配套包）、GWR 思想（Nat. Commun. 2025/2026 两篇，ArcGIS 实现或未注明） |
| **同类方法被采用，但未点名本包** | esda/spdep（Moran's I 类方法在抽样中未作为核心方法出现，但为领域通用基础设施）、GSTools/PyKrige/scikit-gstat（克里金思想被 Geogr. Anal. 2025 采用，实现为 R 的 gstat，而非本清单的 Python 包）、blockCV（空间交叉验证思想被 UST-GNN 采用，实现方式未注明）、spint/PyTDLM（空间交互思想被 Imagery2Flow 采用，但以深度学习重构） |
| **抽样中未出现** | spreg、spatialreg、geocausal、ST-HCMs、gdverse/GD、GWmodel、mgwnbr、spml、PyGALAX、geoshapley、verde、spatialize、geoai、r-inla |

> 解读：未出现 ≠ 不重要。spreg / spatialreg / INLA 是教科书级基础设施，抽样文章的方法部分常默认读者已知而不展开；geoshapley、spml、geocausal 是 2024–2026 年的新工具，顶刊采用存在滞后。真正值得注意的信号是：**顶刊前沿正在从“用某个包跑 GWR”转向“把空间结构（图、位置编码、空间 CV）放进深度学习 pipeline”**，而本清单中只有 City2Graph 与 spml 直接对位这一趋势。

### 6.4 从顶刊图幅提炼的可视化规范（5 条）

1. **性能图与地图分工明确**：方法学文章（IJGIS TabPFN-GSA）正文以折线/散点性能图为主（R² 曲线、注意力热图、敏感性曲线），地图只出现在附录；应用型文章（Nat. Commun.、CEUS）则以地图为主图。选图类型先问“这篇文章要证明什么”——比方法用性能图，比空间格局用地图。
2. **多面板按“对照逻辑”组织，而非按变量堆叠**：Zhu 等 (2026) 图 2 用 A/C/E（无规划）vs B/D/F（优化后）六面板，两两对照；region2vec 图 4 把 Louvain/Leiden/Node2vec 等方法并排放在同一地理底图上。面板的组织单位是“可比的方案”，不是“更多的变量”。
3. **配色克制、语义优先**：抽样文章的地图普遍用单色系顺序色阶表示连续量（系数、得分、密度），用 2–4 色分类色表示类别（社区、等级）；HPSA 图用绿色 + 透明度双重编码得分。避免彩虹色；同一篇文章内同一变量的色阶保持一致。
4. **底图极简、标注只给必要信息**：Nat. Commun. GLOF 图用 Natural Earth 公共领域底图，仅保留海岸线与国界轮廓；城市级地图（伦敦 LSOA、威斯康星）多用浅灰底图 + 深色边界。比例尺与指北针在小比例尺全球图上出现，城市级多面板图常省略，改以图注说明投影与单位。
5. **每幅图自带“可复现锚点”**：顶刊图注普遍包含样本量（n=9967）、方法参数（自适应高斯核、AICc 选带宽）、数据来源（LODES、ACS、SafeGraph）三类信息中的至少两类；代码/数据链接放在 Data/Code availability 段而非图注。作图时把 n、带宽/核函数、数据源写进图注，是成本最低的可信度提升。

## 7. 存疑、停滞与未查到

| 项目 / 事项 | 状态（2026-11-14 核验） |
|---|---|
| `retailgravity`（PyPI 称 2026 年新包，MIT） | GitHub 仓库 404，无法核验仓库与代码；**已排除出主清单** |
| `geoai2analytics-sdk` | GitHub 仓库 404，无法核验；**已排除出主清单** |
| `RTDLM/PyTDLM`（与第 15 号同名注意） | 搜索 API 曾返回 1 star、2026-09-22 推送；后成功克隆，仓库内 LICENSE 为 GPL v3，确认为同一项目，已计入主清单 |
| `lbelzile/spflow` | GitHub 404（空间流模型 R 包，疑似已迁移或改名）；未计入 |
| `YusufEminoglu/retailgravity_sdk` | 404；未计入 |
| FastGWR（`Ziqi-Li/FastGWR`，64 stars，MIT，最后推送 2022-03-17） | 已停滞，仅作对比提及；其快速 GWR 思想已被 mgwr / PyGALAX 等吸收 |
| GWmodel GitHub（`lbb220/GWmodel`） | GitHub 最后推送 2022-06-15，克隆 master 最新提交 2021-04-12；但 CRAN 版 2.4-1 发布于 2024-09-07，R 用户应以 CRAN 为准 |
| pyinterpolate 的推送日期出入 | GitHub API pushed 显示 2026-05-23，但仓库内 CHANGELOG 最新为 2025-12-26（v1.2.1）；报告以仓库内记录为准并注明出入 |
| pyinterpolate 许可证 | 接续核查已部分解决：仓库 LICENSE.md 条款文本与 BSD-3 一致（含“Neither the name of the author…”第三条），但 pyproject 分类标 MIT License；两者出入未完全消除，记“存疑（BSD-3 文本 / MIT 分类）”，许可证栏已同步更新 |
| geoai 的 PyPI 版本号 | 接续核查：仓库 `pyproject.toml` 标版本 0.43.1；PyPI 未单独复核，总表已按仓库版本更新 |
| Wu (2026) MGTWR 全文细节与代码 | 未获全文（Otago S3 链接 403 过期），记“未查到”，未重复请求该链接 |
| Geographical Analysis 除 Boeing (2025) 与 Finne & Sauzet (2025) 外的抽样 | 多为 Wiley 付费墙，未读全文；记“未查到” |
| R 项目的运行实测 | 本机无 R/Rscript，10 个 R 项目均未实测；结论仅基于克隆代码 + CRAN 元数据 |
| r-inla 的克隆 | `git clone --depth 1 --branch devel` 两次重试均失败（网络超时），未取得本地副本；元数据以 GitHub API（132 stars，2026-11-13 推送，MIT）与官网发行渠道为准 |

## 附录 A. 验证环境

- 虚拟机：共享 VM，内存 7.7 GB（实测时可用约 1.4 GB），磁盘 149 GB 可用。
- Python 3.12.3；实测 venv：numpy 2.5.4、scipy 1.16.3（scikit-gstat 要求 scipy<1.17，安装时 pip 自动降级，见第 5 节）、pandas 3.1.1、scikit-learn 1.9.1、matplotlib 3.11.2。
- 克隆方式：`git clone --depth 1`（r-inla 指定 `--branch devel`）；克隆目录 `repos/`（实有 27 个目录，r-inla 未克隆成功，见第 5 节）。
- 实测脚本：合成小数据（n=20–100），不依赖外部数据文件；接续复跑脚本见报告配套目录 `verify/`（原 `/tmp/verify_tests/` 已随运行时重启丢失，见接续说明）。
- 同一时段有多个并行调研任务在克隆与安装，网络拥堵是部分克隆/安装缓慢的原因之一。

## 附录 B. 仓库地址速查

见第 2 节总表。补充注脚：PySAL 基础设施 `pysal/libpysal`（https://github.com/pysal/libpysal）；INLA 配套前端 `inlabru-org/inlabru`（https://github.com/inlabru-org/inlabru）；INLA 官网发行渠道 https://inla.r-inla-download.org/。

## 接续说明（2026-11-14，原研究员中断后由接续研究员收尾）

1. **章节缺失已补齐**：原草稿章节编号从第 2 节直接跳到第 6 节，第 3/4/5 节确实缺失。本轮补写第 3 节（重点项目深挖：mgwr、GSTools+PyKrige、spml、City2Graph、esda）、第 4 节（选型建议与使用路线）、第 5 节（验证小结）；原草稿中所有指向“第 5 节”的引用（总表表头、§0、附录 A）现均有对应内容。
2. **克隆数修正**：原草稿 §0 称“全部 28 个仓库均已 clone”，与事实不符。核查 `repos/` 实为 **27 个目录**，r-inla 无本地副本（`devel` 分支两次克隆失败）。收录总数仍为 28 个项目（r-inla 以 GitHub API 元数据计入），本地克隆副本为 27 个；§0、附录 A 已修正措辞。
3. **验证状态修正**：原总表除 GSTools 外其余 Python 项目均为“待填”，且原实测脚本存放于 `/tmp/verify_tests/`，已随运行时重启丢失（tmpfs 清空），无存档记录可核。本轮将无记录的 10 个 Python 项目统一改记为“未实测（无存档记录）”，并用现有 venv 对 4 个项目做了复跑确认：GSTools ✅、esda ✅、mgwr ✅、spml ⚠️ 部分通过（fit 可跑，predict 报 `_local_models` 缺失）。复跑脚本改存于报告配套目录 `verify/`，不再放 `/tmp`。
4. **许可证与版本补查**：pyinterpolate 的 LICENSE.md 条款文本与 BSD-3 一致，但 pyproject 分类标 MIT，出入未完全消除，记“存疑（BSD-3 文本 / MIT 分类）”，总表与 §7 已同步；geoai 版本由仓库 `pyproject.toml` 补为 0.43.1（PyPI 未单独复核）。
5. **环境数字修正**：附录 A 的 scipy 由 1.18.1 修正为 venv 实际的 1.16.3（scikit-gstat 要求 scipy<1.17，pip 自动降级所致）；其余 numpy 2.5.4 / pandas 3.1.1 / scikit-learn 1.9.1 / matplotlib 3.11.2 与 venv 实测一致。
6. **出图核查**：`figures/` 下 2 幅图均已目视核对——`stars_2026-11-14.png`（28 条，数值与总表一致）与 `recency_2026-11-14.png`（28 条，天数与总表推送日期一致，如 GWmodel 1613 天、esda 1 天）；两图均含 r-inla（API 快照口径），与克隆缺失不矛盾。
7. **期刊标杆核查（第 6 节完整）**：逐项核对——抽样确为 4 本期刊 11 篇（IJGIS 3、Geographical Analysis 2、CEUS 3、Nature Communications 3）；方法栈、技术栈、图类型与数量、组织方式、配色/底图等美化特征、代码与数据公开情况均已覆盖（§6.1 表、§6.2、§6.3、§6.4）；代码公开率“8/11（2 未查到、1 仅部分公开）” recount 一致（8 篇完全公开：Deng、Comber、Boeing、Finne、Wang、Liang、Zhu、Xu；部分公开：Zhang 的 GLOF；未查到：Wu、Zhao）；引用仅给标题与 DOI，未复制原文大段文字或图片。本节未做改动。
8. **未复核项**：stars / forks / 最近推送等 GitHub API 快照（2026-11-14）未在本轮逐条重新调 API 复核，仅做了总表与两幅图的内部一致性核对；PyKrige、verde、scikit-gstat 等 10 个 Python 项目仍未实测，R 项目 10 个均未实测（本机无 R），如需补测应在有 R 的环境进行。
