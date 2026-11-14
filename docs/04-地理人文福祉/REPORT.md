# 领域三：地理人文福祉（geo-human well-being）开源调研报告

- **核验日期（快照）**：2026-11-14（星期六）
- **范围**：空间不平等与福祉/幸福感测度、可达性分析（医疗、教育、公共服务）、公共服务均等化、健康地理、社会脆弱性指数、15 分钟城市/生活圈、环境正义与空间公平相关工具
- **项目总数**：30 个（GitHub API 核查 30 个，其中 2 个返回 404，见表内说明）
- **实测**：见第 4 节“验证小结”（目标 ≥8 个重点项目实测）
- **报告位置**：`~/workspace/your_files/geography-research/wellbeing/REPORT.md`
- **仓库克隆**：`~/workspace/your_files/geography-research/wellbeing/repos/<项目名>/`（`git clone --depth 1`）
- **出图**：`~/workspace/your_files/geography-research/wellbeing/figures/`

## 1. 方法与核验说明

### 1.1 检索与核验方法

- 先以 GitHub API（未认证）批量核查 30 个候选仓库的 stars、许可证（SPDX）、最后推送时间（快照 2026-11-14）；随后逐个浅克隆（`git clone --depth 1`），读 README、LICENSE 与关键代码，核对许可证与最近提交（本地 `git log -1` 的提交时间与 API 的推送时间可能相差 1–2 天，二者都记录）。
- 轻量 Python 包在一个独立 venv（`~/workspace/.wb-venv`，Python 3.12）中用合成数据实测官方示例/核心函数；R 包与 Java 引擎本机无法运行（见 1.2），只做代码审读，绝不谎称跑通过。
- 所有数字与用例均有来源；查不到的写“未查到”。注意区分“项目本身”与“同名无关项目”（例如 `access` 须是 PySAL 的 `pysal/access`，`r2sfca` 须是 Liu & Wang 的 2SFCA 包）。

### 1.2 本机环境限制（实测前已确认）

- 共享虚拟机：内存总量 7.7 GiB，任务期间可用内存常低于 1 GiB；磁盘 150 GiB，约 145 GiB 可用。
- Python 3.12.3、git 2.43.0；系统已装 numpy 1.26.4、pandas 2.1.4、SciPy 1.11.4、matplotlib 3.6.3。
- **无 R、无 Java**（`which R Rscript java` 均无结果），无 mvn、docker；有 node/npm。
  - 影响：R 包（`accessibility`、`fca`、`findSVI`、`inAccessMod`、`devPTIpack`、EJAM）与 Java 引擎（OTP、R5、`r5r`、`r5py`、GOAT 后端）**均无法在本机实测**，记为“未实测（环境缺 R/Java），仅代码审读”。
  - `r5r` 需 JDK 21；OTP 需 Java + Maven 构建；GOAT 需 Node/pnpm + Docker 部署，均超出本机能力。
- `/tmp` 为 512 MiB tmpfs（任务期间一度仅剩 95 MiB），pip 安装曾因此报 `No space left on device` 而失败一次；后改用磁盘上的 venv（`~/workspace/.wb-venv`）与 `TMPDIR=~/workspace/.wb-tmp` 重新安装。
- 多个领域克隆任务同时在跑，GitHub 克隆多次断开（`fetch-pack: unexpected disconnect`）。最终 29 个克隆目标全部取回（`repos/` 下 29 个目录，约 3.2 GiB），其中 citychrone、cities、EJAM-PEDP、EJAM-ejanalysis 四个仓库经历中断后以对象库核实/针对性恢复方式修复（工作区完整度不一，见 4.3）。

### 1.3 许可证注记

GitHub API 对 8 个仓库返回 `NOASSERTION`（未识别），但 8 个在仓库内均有明确 LICENSE 文件，均已核实：OTP 为 LGPL-3.0，`r5py`/`r5r` 为 GPL-3.0-or-later/MIT 双许可，`accessibility`（R）为 MIT 模板，`cities` 为 MIT（Copyright 2025 cities），`devPTIpack` 为 MIT，`findSVI` 为 MIT，EJAM-PEDP 为 MIT（Copyright 2025 EJAM authors）。报告以**仓库 LICENSE 文件为准**，API 结果仅作对照。另：accessmod 的许可证文本在仓库根目录的 `COPYING` 文件（LGPL-3.0），而非惯常的 `LICENSE` 文件。

## 2. 项目总表（快照 2026-11-14）

stars 为 GitHub API 快照值；“最近更新”优先写本地克隆的最近提交时间，括号内为 API 最后推送时间（两者不一致时并列）。

| # | 项目 | 仓库 | 许可证 | stars | 最近更新 | 用途一句话 | 验证状态 |
|---|---|---|---|---|---|---|---|
| 1 | OpenTripPlanner（OTP） | opentripplanner/OpenTripPlanner | LGPL-3.0（仓库 LICENSE 核实） | 2776 | 2026-11-13（本地提交 a529a76） | GTFS+OSM 多模式公交出行规划引擎，可达性计算底座 | 未实测（缺 Java），代码审读 |
| 2 | R5 | conveyal/r5 | MIT | 405 | 2026-11-11（本地提交 500ce26） | Conveyal 的快速现实路由引擎（Java），r5r/r5py 的后端 | 未实测（缺 Java），代码审读 |
| 3 | r5py | r5py/r5py | GPL-3.0-or-later / MIT 双许可（仓库 LICENSE 核实） | 195 | 2026-09-20 | Python 调用 R5，算出行时间矩阵与可达性 | 未实测（缺 Java），代码审读 |
| 4 | r5r | ipea/r5r | GPL-3.0-or-later / MIT 双许可（仓库 LICENSE 核实） | 246 | 2026-11-09 | R 调用 R5，需 JDK 21；Ipea 巴西城市可达性研究主力 | 未实测（缺 R/Java），代码审读 |
| 5 | accessibility（R） | ipea/accessibility | MIT（仓库 LICENSE 模板，API 未识别） | 72 | 2026-11-08（本地提交 f54fd4f；CRAN 1.6.0 发布于 2026-10-30） | 给定出行成本矩阵算累积机会/重力/2SFCA/BFCA 及 Palma/Theil/FGT 不平等与贫困测度 | 未实测（缺 R），代码审读 |
| 6 | access（PySAL） | pysal/access | BSD-3-Clause | 31 | 2026-10-15 | 经典与新颖空间可达性测度（2SFCA、E2SFCA、RAAM 等） | 实测（见 4.1） |
| 7 | pandana | UDST/pandana | AGPL-3.0 | 432 | 2026-09-30（本地提交 e070217；API 推送 2026-10-01） | 收缩层次（C++）路网可达性与最短路径库，现为 LTS 兼容维护状态 | 实测（见 4.1） |
| 8 | urbanaccess | UDST/urbanaccess | AGPL-3.0 | 266 | 2026-09-03（本地提交 2fd3045；API 推送 2026-10-10） | GTFS 公交 + OSM 步行整合成多模式路网，供 Pandana 做可达性分析 | 实测 import 级（见 4.1） |
| 9 | GOAT | goat-community/goat | GPL-3.0 | 180 | 2026-11-13（本地提交 f3fd43c） | 步行/骑行可达性 WebGIS（TUM/Plan4Better，现为订阅 SaaS，代码仍开源） | 未实测（需 Node/pnpm+Docker 部署），代码审读 |
| 10 | citychrone | CityChrone/citychrone | MIT（对象库 LICENSE 核实，Copyright 2017 indaco biazzo） | 3 | 2023-11-03（本地提交 eda2b04，偏旧） | Meteor 框架的 X 分钟城市时空可达性 Web 应用（等时线 + 公交可达性交互地图） | 未实测（2023 年后无更新；对象库已核实，工作区未完全检出，见 4.3） |
| 11 | accessX | TransformTransport/accessX | MIT | 28 | 2026-11-09（本地提交 c971f08） | 基于 GeoPandas/OSMnx/NetworkX/H3/rasterio 的 X 分钟城市近邻可达性 Python 库 | 实测（见 4.1） |
| 12 | UCID | ucid-foundation/ucid | EUPL-1.2 | 2 | 2026-01-16（本地提交 e77c69f；API 推送 2026-11-09） | 城市上下文评分：15MIN（15 分钟城市）、EQUITY、WALK 等 | 实测 import 级（见 4.1） |
| 13 | coaccessibility（CTwalk 后端） | MiliasV/coaccessibility | MIT | 3 | 2023-09-22（本地提交 171b375；API 推送 2024-02-14） | 荷兰五大城市分年龄组（儿童/成人/老人）5/15 分钟步行共可达性 + Shannon 均等指数 | 未实测（需荷兰数据），代码与数据审读 |
| 14 | personalised-urban-accessibility | GPrabhanjana/personalised-urban-accessibility | MIT | 0 | 2026-10-21 | 个性化步行可达性评分框架（班加罗尔 198 选区；配论文与在线 demo） | 实测（见 4.1） |
| 15 | cities | mirkolai/cities | MIT（仓库 LICENSE 核实，Copyright 2025 cities） | 3 | 2026-02-12（本地提交 b301f91） | 城市隔离与可达性研究代码（Lai 等，网络分析度量步行可达性与隔离的相互作用） | 代码已恢复（31 个 .py 全在），未实测（需 GTFS/Infomap 数据；484 张输出图缺失，见 4.3） |
| 16 | segregation（PySAL） | pysal/segregation | BSD-3-Clause | 124 | 2026-11-13 | 40+ 种空间隔离指数（Dissimilarity、Isolation 等） | 实测（见 4.1） |
| 17 | inequality（PySAL） | pysal/inequality | BSD-3-Clause | 37 | 2026-10-13（本地提交 77d802d；API 推送 2026-10-14） | Gini、Theil 等空间不平等测度 | 实测（见 4.1） |
| 18 | spopt（PySAL） | pysal/spopt | BSD-3-Clause | 387 | 2026-10-12 | 空间优化：p-median、p-center、最大覆盖等设施选址模型 | 实测（见 4.1） |
| 19 | huff | geowieland/huff_official | MIT | 6 | 2026-11-10 | Huff/MCI 市场区分析 + Hansen 可达性 + 2SFCA（经济地理与健康地理） | 实测（见 4.1） |
| 20 | geometrics | quarcs-lab/geometrics | MIT | 0 | 2026-07-02 | 区域增长/收敛/不平等（PySAL 栈），配 Streamlit 应用与教学沙盒 | 实测（见 4.1） |
| 21 | devPTIpack | wbPTI/devPTIpack | MIT（World Bank 2026，仓库 LICENSE.md 核实） | 1 | 2026-05-18 | 世界银行 Project Targeting Index（PTI）交互仪表盘（Shiny/golem R 包），支撑 30+ 国家 PTI 分析 | 未实测（缺 R），代码审读 |
| 22 | r2sfca | urbananalytics/r2sfca（GitHub 404，见说明） | MIT（PyPI 元数据） | —（GitHub 404，无 stars） | PyPI 1.1.3 发布于 2025-10-14 | 以距离衰减参数统一 2SFCA 与 i2SFCA 的可达性测度 | 实测（PyPI 安装，见 4.1） |
| 23 | fca（R） | egrueebler/fca | GPL-3.0 | 8 | 2021-12-06（偏旧） | 浮动 catchment（FCA）方法：高斯/重力/指数/logistic 距离衰减 | 未实测（缺 R），代码审读 |
| 24 | findSVI | heli-xu/findSVI | MIT（CRAN；仓库 LICENSE.md 核实） | 18 | 2025-07-02（CRAN 0.2.0 发布于 2025-02-08） | 算 CDC/ATSDR 社会脆弱性指数（SVI），支持 2012–2022 年与 ZCTA/places 等地理层级 | 未实测（缺 R，需 Census API 数据），代码审读 |
| 25 | EJAM（PEDP fork） | Public-Environmental-Data-Partners/EJAM | MIT（仓库 LICENSE.md 核实，Copyright 2025 EJAM authors） | 2 | 2026-11-09（本地提交 f852f50） | 环境正义分析（EJScreen 的继承者，R 包；EPA 原版 2025 年中归档后由非 EPA 组织继续开发） | 未实测（缺 R），代码审读 |
| 26 | ejscreen | ejanalysis/ejscreen（GitHub 404） | 未查到 | —（GitHub 404） | 未查到 | EPA EJScreen 旧代码库，疑似已并入 EJAM 仓库；EJScreen 官网与 CEJST 官网 2025 年初下线，数据靠镜像存续 | 未实测（仓库不存在） |
| 27 | justice40-tool | usds/justice40-tool | CC0-1.0（仓库 LICENSE.md 核实） | 145 | 2025-03-25（本地提交 980ace3） | 美国 Justice40 弱势社区识别工具（CEJST v1.0 数据方法） | 已克隆核实，未实测（需全栈部署；注：v1.0 已移交 DOI-DO/j40-cejst-2，即 v2） |
| 28 | accessmod | unige-geohealth/accessmod | LGPL-3.0（仓库 COPYING 文件核实） | 50 | 2026-06-05（本地提交 65ec817，v5.9.1；API 推送 2026-09-04） | 医疗可达性分析（WHO/UNICEF/世界银行采用，40+ 国家卫生部使用） | 已克隆核实，未实测（缺 R/Java 环境） |
| 29 | inAccessMod | unige-geohealth/inAccessMod | GPL-3.0 | 12 | 2025-11-07 | AccessMod 的 R 接口（2026 年土耳其西部 11 省基层医疗研究使用） | 未实测（缺 R），代码审读 |
| 30 | TSGI | MIT-SUL-Team/Twitter-Sentiment-Geographical-Index | MIT（仓库 LICENSE 核实） | 5 | 2022-10-03（本地提交 cb5dd50，偏旧） | 4.3B 条地理推文、164 国 admin-2 级日度情感指数（主观福祉的社交媒体代理指标） | 已克隆核实，未实测（2022 年后无更新；需 4.3B 推文数据） |

> **r2sfca 与 ejscreen 的 404 说明**：2026-11-14 实测 `github.com/urbananalytics/r2sfca` 与 `github.com/ejanalysis/ejscreen` 均返回 404，`git ls-remote` 亦失败。r2sfca 仍可通过 PyPI（主页仍指向该 GitHub 地址，版本 1.1.3，MIT）安装验证，论文为 Liu & Wang (2025) "Reconciling 2SFCA and i2SFCA via distance decay parameterization", *IJGIS*, DOI 10.1080/13658816.2025.2562255。ejscreen 代码疑似已并入 EJAM 仓库（`ejanalysis/EJAM` 的 ls-remote 成功，HEAD `f852f508`，与 PEDP fork 的 HEAD 一致）。
>
> **城市与福祉主观测度的缺口**：主观福祉/幸福感方向**未查到足够专用开源项目**——TSGI（2022 年后未更新）是唯一进入清单的社交媒体情感指数工具；另有 WWBP 县级词汇库（`wwbp/county_tweet_lexical_bank`，未纳入本次克隆）可作补充。除 TSGI 外，幸福感测度在开源工具层面基本是空白，顶刊工作多用专有调查或商业移动数据（见第 5 节）。

## 3. 重点项目深挖（5 个）

### 3.1 OpenTripPlanner（OTP）——公交可达性事实上的标准底座

- **仓库**：https://github.com/opentripplanner/OpenTripPlanner ；**许可证** LGPL-3.0；**stars** 2776（2026-11-14 快照）；**最新提交** 2026-11-13（`a529a76`，v2.10.0 发布于 2026-09-09）；克隆 82 MiB，5281 个文件。
- **用途**：开源多模式出行规划器，以 GTFS（公交时刻表）+ OpenStreetMap 路网建图，提供 GraphQL API；可达性研究用它批量算“从某点出发 X 分钟内能到哪里/能到多少机会”。
- **真实用例**：全球多城部署（官网 Deployments 页列出各城市与地区实例，含 Porto Digital 等公共实例）；研究中常用作公交可达性计算的底座——例如一篇 PNAS Nexus 纽约公交可达性研究的补充材料明确写道用 OTP（OSM 路网 + GTFS）构建公交网络；2026 年 GISRUK 论文用 R5 引擎 + 英国 BODS 实时公交数据做全国公交可达性，属同一技术路线。
- **安装运行难度**：高。需 Java + Maven 全量构建（本机无 Java，未实测）；生产部署一般走官方 Docker 镜像 `opentripplanner/opentripplanner`，需自备研究区 GTFS 与 OSM 数据。
- **验证状态**：未实测（环境缺 Java）。代码审读确认：README 明确 OTP 2 为当前唯一受支持主线（自 2018 年开发）；仓库含完整文档与部署指南；许可证文件为 LGPL-3.0（GitHub API 未识别，以仓库文件为准）。
- **选型意义**：若研究需要“真实公交时刻表约束下的可达性”，OTP 是顶刊与业界共同的默认选择；但它本身不输出福祉/不平等指标，须与 `accessibility`（R）、PySAL `access` 等测度层工具搭配。

### 3.2 R5 生态（r5 + r5r + r5py）——研究级出行时间矩阵的快车道

- **仓库**：https://github.com/conveyal/r5 （MIT，405★，最新提交 2026-11-11）；https://github.com/ipea/r5r （GPL-3.0-or-later/MIT 双许可，246★，2026-11-09，CRAN 2.5.0 发布于 2026-11-07，需 JDK 21）；https://github.com/r5py/r5py （同双许可，195★，2026-09-20）。
- **用途**：R5 是 Conveyal 的 Java 路由引擎（步行/骑行/公交/驾车多模式）；`r5r`（R）、`r5py`（Python）是它的友好封装，可并行算大规模 OD 出行时间矩阵与可达性。`r5r` 另有姊妹包 `accessibility`（R）做测度层。
- **真实用例**：Ipea 的巴西城市可达性研究长期用 `r5r`；`r5py` 用于赫尔辛基 2023 出行时间矩阵公开数据集（13,132×13,132 个 OD 对，约 22 亿行结果）；一篇比较 12 种可达性测度的加拿大学习用 `r5r` + GTFS + OSM（ScienceDirect 摘要级证据）。
- **安装运行难度**：中高。核心是 Java：`r5r` 要求 JDK 21（官方推荐 Adoptium Temurin，R 包 `rJavaEnv` 可一键装）；`r5py` 可 pip/conda 安装但运行时仍需本地 Java 与 R5 jar；本机无 Java，未实测。
- **验证状态**：未实测（环境缺 R/Java）。代码审读确认三仓库均活跃（2026-09 至 2026-11 均有提交），README 与 vignette 完整，`r5r` 论文 DOI 10.32866/001c.21262。
- **选型意义**：顶刊抽样中明确点名本清单工具的少数案例之一就是 R5/`r5r`（见第 5 节）。做“时刻表敏感 + 大规模 OD”的可达性研究时，R5 生态是首选；做“方法测度比较”时，`r5r` + `accessibility`（R）是一套完整链条。

### 3.3 PySAL access——可达性测度的方法箱

- **仓库**：https://github.com/pysal/access ；**许可证** BSD-3-Clause；**stars** 31（2026-11-14 快照）；**最新提交** 2026-10-15（`c58aea7`）；克隆 9.4 MiB。
- **用途**：提供经典与新颖的空间可达性测度：累积机会、重力模型、2SFCA、E2SFCA、RAAM（理性代理人可达性模型）等；属 PySAL 家族，与 `segregation`、`inequality`、`spopt` 同源。
- **真实用例**：PySAL 文档与 CyberGIS 案例用 `access` 做芝加哥医生可达性；RAAM 方法源自 Saxon & Snow (2019)，2025 年 *Applied Geography* 的 Kim 等首尔急救可达性论文以 RAAM 对比 G2SFCA（方法来源关联，非本文直接采用）。
- **安装运行难度**：低。`pip install access`（或 `pip install pysal`），依赖 libpysal/geopandas/networkx；纯 Python，无需编译。
- **验证状态**：实测（见 4.1，合成数据跑通核心函数）。
- **选型意义**：测度层最轻量的入门选择：一个包覆盖从 Hansen 重力到 2SFCA 再到 RAAM 的谱系，适合教学与方法比较；缺点是 stars 仅 31，社区规模小，文档以 API 参考为主，示例较少。

### 3.4 r2sfca——把 2SFCA 与 i2SFCA 统一成一个参数

- **仓库**：https://github.com/urbananalytics/r2sfca （**2026-11-14 实测 GitHub 404**）；PyPI：https://pypi.org/project/r2sfca/ ，版本 1.1.3（2025-10-14），MIT，作者 Lingbo Liu、Fahui Wang；文档 https://r2sfca.readthedocs.io 。
- **用途**：以距离衰减参数化调和经典 2SFCA 与逆向 i2SFCA（后者衡量设施拥挤度），把两者统一进同一框架；论文 Liu & Wang (2025), *IJGIS*, DOI 10.1080/13658816.2025.2562255。
- **真实用例**：未查到除论文外的公开采用者记录（新包，2025 年发表）。
- **安装运行难度**：低。`pip install r2sfca`，纯 Python。
- **验证状态**：实测（PyPI 安装，见 4.1）。**风险提示**：GitHub 仓库 404（可能改名/转私有/删除），PyPI 主页仍指向该地址；采用前应确认代码托管现状，或改用 PySAL `access` 的 2SFCA/E2SFCA 实现作为替代。
- **选型意义**：方法上最新颖的 2SFCA 实现；但仓库不可达是硬伤，生产研究引用时须留档 PyPI 版本与论文。

### 3.5 GOAT——15 分钟城市的 WebGIS 工作台

- **仓库**：https://github.com/goat-community/goat ；**许可证** GPL-3.0；**stars** 180（2026-11-14 快照）；**最新提交** 2026-11-13（`f3fd43c`）；克隆 242 MiB（`apps/` 前端占 116 MiB）。
- **用途**：Geo Open Accessibility Tool（TUM / Plan4Better）：步行/骑行可达性 WebGIS 与综合规划平台，含等时圈、设施可达性、情景对比；云端试用 https://goat.plan4better.de ，代码仍在 GitHub 开源。
- **真实用例**：Plan4Better 的规划咨询项目与慕尼黑等城市应用（官网案例）；学术引用见 GOAT 相关论文。注意：现为订阅 SaaS 模式，免费云端为试用性质；自部署需完整前后端栈。
- **安装运行难度**：高。pnpm monorepo（`apps/` + `packages/`）+ Python 后端 + PostGIS，需 Docker Compose 部署；本机内存紧张且无 Docker，未实测。
- **验证状态**：未实测（环境与部署成本所限）。代码审读确认：仓库活跃（2026-11-13 仍有提交），含 `compose.yaml`、`deploy/` 与 Playwright 测试；README 徽章链接已指向 `plan4better/goat`（组织名迁移迹象，克隆地址仍为 `goat-community/goat`）。
- **选型意义**：唯一进入清单的“开箱即用 15 分钟城市工作台”；适合规划机构直接试用云端版，学术研究若需自部署或二次开发，成本显著高于 Python 库路线（`accessX`/`access`）。

## 4. 验证小结

### 4.1 实测结果（12 项，12 项通过，0 项失败）

实测环境：独立 venv（`~/workspace/.wb-venv`，Python 3.12），全部用**合成数据**完成，零下载、零注册、零费用。测试脚本见 `~/workspace/.wb-tmp/test_all.py`（任务结束后的临时文件，不在交付目录内；数值已全部记录在本节）。首次运行为 4/12 通过，其余 8 项失败均为**测试代码的 API 用法错误**（如 `Access` 构造参数位置、`PMedian.solve()` 需显式传求解器），对照官方示例与源码修正后全部通过——失败原因见下文“实测中的 API 教训”一段，包本身无一报错。

| # | 项目（版本） | 实测内容 | 结果（合成数据） | 深度 |
|---|---|---|---|---|
| 1 | inequality 1.2.0 | Gini + Theil | Gini=0.4000，Theil=0.2764（向量 [10,20,30,40,100]） | 核心函数 |
| 2 | segregation 2.6.0 | Dissimilarity | Dissim=0.7000（4 个合成 tract） | 核心函数 |
| 3 | access 1.1.10.post3 | 2SFCA + E2SFCA | 2SFCA=[0.0176, 0.0321, 0.0202, 0.0202, 0.0265]；E2SFCA=[0.0177, 0.0243, 0.0277, 0.0167, 0.0324]（5 需求区 × 3 供给点，30 分钟阈值） | 核心函数 |
| 4 | r2sfca 1.1.3 | R2SFCA access + crowd | 300 条 OD 行，100 个需求格，β=0.1 指数衰减，access ∈ [0.0015, 0.0056]；crowd 3 行 | 核心函数 |
| 5 | spopt 0.8.0 | p-median（p=2） | 选中设施 [1, 2]，平均距离 3.65，目标值 2700.0（6 需求点 × 4 候选点，PuLP/CBC 求解） | 核心函数 |
| 6 | huff 1.9.16 | 2SFCA + Hansen | 15 条交互记录（5 需求点 × 3 供给点，欧氏距离离线模式），2SFCA 与 Hansen 均完成 | 核心函数 |
| 7 | geometrics 0.1.3 | analyze_inequality_over_time | 返回 InequalityOverTimeResult（4 区域 × 2 年合成面板，Gini/Theil） | 核心函数 |
| 8 | accessx 0.1.1 | count_accessible_pois + 2SFCA | 计数 [1, 2]，2SFCA=[0.0033, 0.0133]（4×4 合成路网，2 个诊所） | 核心函数 |
| 9 | pandana 0.8 | 最短路径 + 聚合 | 0→4 最短路径 3.5；2.0 半径线性衰减聚合 [20.0, 50.0, 40.0, 70.0, 70.0]（5 节点合成路网） | 核心函数 |
| 10 | urbanaccess 0.2.2 | import | 导入成功；未下载 GTFS/OSM（无真实数据不做网络构建） | import 级 |
| 11 | UCID 1.0.3 | import + API 签名 | 导入成功；`create_ucid(city, lat, lon, timestamp, context, ...)` 与 `parse_ucid` 签名已核查；未做真实城市评分（需 OSM 数据） | import 级 |
| 12 | personalised-urban-accessibility | score_preset（仓库自带预处理数据） | 预设 'non_worker_local' 评出 20,155 个网格，分数 ∈ [0.000, 0.835]，均值 0.015（班加罗尔数据，纯标准库评分引擎） | 核心函数 |

**实测中的 API 教训**（已写入 6.2）：`spopt` 的 `facility_client_array()`/`get_mean_distance()` 返回 None、结果写在 `fac2cli`/`mean_dist` 属性上；`PMedian.solve()` 须显式传求解器；`access` 的结果列名为 `2sfca_beds`（方法名 + 供给值列名）而非 `2sfca`；`access` 构造须用关键字参数并提供 `demand_index`/`supply_index` 列名与 `neighbor_cost_df`；`r2sfca` 的 `access_score(beta)`/`crowd_score(beta)` 须传衰减参数 β（本次取 β=0.1）；huff 离线模式须先 `define_weightings` 定义 `t_ij` 权重；`accessx` 要求 OSMnx 风格整数节点 ID 与图的 `crs`；personalised 的 `DEFAULT_PRESETS` 指向不存在的 `presets_v2.json`，当前为 `presets_v3.json`。

**出图评价**：

![图 1：28 个仓库 stars 对数条形图](figures/fig1_stars.png)

![图 2：r2sfca 合成网格 2SFCA 可达性热力图](figures/fig2_r2sfca_synthetic.png)

- 图 1（`figures/fig1_stars.png`）：28 个 GitHub 仓库 stars 对数条形图（快照 2026-11-14；r2sfca 与 ejscreen 404，无 stars 值未列入）。**评价**：OTP（2776）断层领先，次高 pandana（432）仅为其约 1/6；中段 100–450 星的 9 个项目为可达性引擎主力；14 个项目不足 30 星，其中 2 个为 0 星——stars 分布极不均衡，不能只看头部。局限：stars 只反映关注度，不反映质量与适用性。
- 图 2（`figures/fig2_r2sfca_synthetic.png`）：r2sfca 在合成 10×10 网格上的 2SFCA 可达性热力图（β=0.1，3 个设施标红星，供给量 100/60/80）。**评价**：可达性高值区围绕设施呈距离衰减分布，设施 s=100 所在格（2,2）为全局最高 0.0056，边缘格最低 0.0015，符合 2SFCA 预期；验证了 r2sfca 在合成数据上能正确跑出空间分异。局限：合成网格、欧氏距离、均匀需求，非真实城市数据，不可外推为任何城市的结论。
- 图 3（`figures/fig3_journal_sample.png`）：期刊标杆抽样构成（见 5 节首）。

### 4.2 未实测的项目与原因

| 原因 | 项目 |
|---|---|
| 本机无 R（5 个 R 包 + 1 个 R 接口） | `accessibility`（R）、`fca`（R）、findSVI、inAccessMod、devPTIpack、EJAM（含 PEDP fork 与 ejanalysis 上游）——仅代码审读 |
| 本机无 Java（引擎与封装） | OpenTripPlanner、R5、`r5r`（需 JDK 21）、`r5py`、GOAT 后端——仅代码审读 |
| 需外部数据/部署，超出本机能力 | coaccessibility（需荷兰五城数据）、justice40-tool（需全栈部署）、TSGI（需 4.3B 推文数据）、accessmod（需 R/Java 运行时） |
| 仓库偏旧/停滞，未投入实测 | citychrone（2023-11 后无更新）、cities（代码已恢复，未尝试运行；其脚本需 GTFS/Infomap 数据） |
| 仓库不存在 | `r2sfca`（GitHub 404，改走 PyPI 实测通过）、ejscreen（GitHub 404，无代码可测） |

### 4.3 克隆与环境问题记录

- **批量克隆**：29 个克隆目标（30 个项目中 r2sfca 与 ejscreen GitHub 404 无仓库；EJAM 计两个仓库），最终 29 个目录齐全（`repos/` 下 29 个目录，总计约 3.2 GiB）。其中 GOAT 242 MiB、EJAM-PEDP 554 MiB、justice40-tool 169 MiB、cities 1.4 GiB（含恢复的对象库）、coaccessibility 102 MiB、geometrics 83 MiB——大体积主要来自前端代码、数据与输出文件。
- **多次断开与修复**（多领域任务同时跑造成的网络争用；`git clone` 多次报 `fetch-pack: unexpected disconnect`）：
  - citychrone：两次完整克隆失败；第三次取回对象库后以 `git show HEAD:README.md` / `HEAD:LICENSE` 核实（MIT，Meteor 等时线 Web 应用），工作区未完全检出——HEAD 树含 54,897 个文件（含已提交的 `node_modules/`），全量检出不值得，已如实记录。
  - cities：三次克隆中断；最终以 `--filter=blob:none` 取回对象库 + `git fetch --no-filter` + 针对性 `git restore` 恢复全部 31 个 `.py` 文件、README/LICENSE 与 JSON 数据；仍缺失 484 张 `plots/` 输出图（生成物，不影响代码审读）。
  - EJAM-PEDP：首次克隆中断后本地只剩 `.git` 对象目录，以 `git fetch --depth 1 origin main` + checkout 修复，最新提交 2026-11-09 `f852f50`，MIT。
  - EJAM-ejanalysis：克隆中断后对象库完整（HEAD `f852f50`，与 PEDP fork 一致），删除残留 `index.lock` 后针对性恢复 README/LICENSE/DESCRIPTION 等核心文件。
  - 其余 25 个仓库一次克隆成功。
- **pip 安装两次失败后成功**：`/tmp` 为 512 MiB tmpfs，首次安装因 `No space left on device` 失败；改用磁盘 venv（`~/workspace/.wb-venv`）+ `TMPDIR=~/workspace/.wb-tmp` 后成功。两批安装共 206.6 MiB 依赖：第一批 `r2sfca inequality segregation access spopt huff geometrics`；第二批 `accessx pandana urbanaccess UCID`（此批把 pandas 从 3.1.1 降为 2.3.3，以满足 pandana 的版本要求；降级后 12 项实测全部重新跑过并通过）。
- **GitHub API 限额**：未认证 core 限额 60/小时，30 个仓库核查后余量充足；后续以本地克隆核对为主，未再批量调用。
- **/tmp 被清空**：任务中途运行时重启清空了 512 MiB tmpfs（`/tmp/clone.log`、`/tmp/wb_tests/` 丢失）；工作文件已全部转存磁盘（`~/workspace/.wb-tmp/`），报告与仓库未受影响。

## 5. 期刊标杆：顶刊文章实际在用什么技术栈、图幅如何组织

> **抽样方法**：四个期刊各抽样 3 篇 2024–2026 年相关文章，共 12 篇（见图 3）。优先开放获取、能看到全文和图的文章；全文级指读到全文 PDF/HTML 并核对方法与图注，摘要/记录级指仅读到摘要或书目记录页。只记录方法与风格层面的观察，不复制原文大段文字或图片；引用给文章标题与 DOI 链接。
>
> ![图 3：期刊标杆抽样构成](figures/fig3_journal_sample.png)
>
> **图 3 评价**：12 篇抽样按阅读深度分布。Nature Human Behaviour 3 篇均为全文级；Journal of Transport Geography 2 篇全文级、1 篇摘要级；Applied Geography 1 篇全文级、1 篇部分全文、1 篇摘要级；Health & Place 3 篇均为摘要级——该刊 2024–2025 年相关论文多为 Elsevier 付费墙，本次未找到 OA 全文，这是本节明确的方法局限：Health & Place 的图幅观察缺失，相关结论只来自其余三刊的全文样本。

### 5.1 抽样文章一览（技术栈、图、代码/数据公开情况）

#### Nature Human Behaviour（综合顶刊，3 篇全文级）

| 文章 | 技术栈（方法部分提及） | 图的类型与数量 | 代码/数据公开 |
|---|---|---|---|
| Abbiasov 等 (2024) "The 15-minute city quantified using human mobility data", *Nat. Hum. Behav.* 8:445–455. DOI: 10.1038/s41562-023-01770-y | SafeGraph 专有 GPS/POI 数据（约 4000 万美国移动设备，136 亿次 POI 访问，2019 年）；15 分钟步行等时圈用 Openrouteservice API 按行人路网生成；未见具名 GIS/统计软件 | 多面板地图 + 统计图组合；图 1 为 15 分钟测度示意；精确图数未逐图清点 | 数据不可分享（SafeGraph 许可限制）；代码“可向作者索取”，无公开仓库链接 |
| Xu 等 (2025) "Using human mobility data to quantify experienced urban inequalities", Perspective, *Nat. Hum. Behav.* 9:654–664. DOI: 10.1038/s41562-024-02079-0 | 框架型 Perspective，未见具名软件栈；数据源列于表 1（共享单车、网约车、电动滑板、公交、社交媒体、移动设备，如 SafeGraph、GeoLife） | 共 5 幅（图 1–图 5）；图 1 为概念图（多面板 a–d：数据示例、共位网络、场所访问网络、适应性）；图 5 将移动数据测度与城市 SDG 关联；表 1 为数据源对照表 | 本次提取全文中未见 "Code availability"/"Data availability" 声明，未查到 |
| Tu 等 (2025) "Inequality in infrastructure access and its association with health disparities", *Nat. Hum. Behav.* 9:1669–1682. DOI: 10.1038/s41562-025-02208-3 | 多源地理空间数据融合生成 2020 年 0.1°×0.1° 全球经济/社会/环境三类基础设施格网图；人口加权暴露模型；Gini 系数；混合效应回归关联健康调整寿命期望（HALE）；夜间灯光 + 众包基础设施数据库校准缺失数据；未见具名软件栈 | 至少 4 幅（图 1 概念框架与研究设计 a–b；图 4 按基础设施类型分面的 Gini/HALE 图；另有补充图 1 研究设计流程图） | 本次提取未见公开代码/数据链接，未查到 |

核心发现（供选型参考，不复制原文）：Abbiasov 等发现中位居民仅 14% 的日常消费出行在 15 分钟步行内，本地设施可达性能解释跨城 84%、城内 74% 的 15 分钟使用率变异；Tu 等发现全球南方国家基础设施可达仅为全球北方 50–80%，不平等水平高 9–44%，社会类基础设施不平等最高（平均 Gini 0.83±0.12），经济类 0.55±0.12，环境类 0.35±0.14。

#### Journal of Transport Geography（2 篇全文级 + 1 篇摘要级）

| 文章 | 技术栈 | 图的类型与数量 | 代码/数据公开 |
|---|---|---|---|
| Araujo、Saraiva 等 (2025) "Unveiling inequalities: The intersection of gender and income in accessibility in Curitiba, Brazil", *J. Transp. Geogr.* 123:104136. DOI: 10.1016/j.jtrangeo.2025.104136 | AxS 智能体模型（Agent-based model），开源 NetLogo 实现（模型见 mvpsaraiva.com/thesis）；OD 调查聚合数据 + 栅格路网寻路；未提及 ArcGIS | 至少 8 幅（图 1 AxS 概念图；图 8 按性别/收入的分位可达性差距地图；另有多面板地图） | 数据声明为 "on request"，无公开代码仓库链接（仅模型主页） |
| Aravind、Mishra 等 (2024) "Equity and accessibility assessment of fixed route transit systems integrated with on-demand feeder services", *J. Transp. Geogr.* 121:104028. DOI: 10.1016/j.jtrangeo.2024.104028 | 智能体仿真框架（引自 Aravind 等 2023，未具名平台）；TCQSM 覆盖法；400 m 步行缓冲；Transit Coverage Gap；Lorenz 曲线与 Gini 指数（整合后 Gini 0.88→0.71，多 29.6% 人口获得公交）；未提及 ArcGIS | 至少 10 幅（图 1 情景示意图；图 6 出行分布；图 10 孟菲斯四面板地图 a–d） | Data availability 声明为 "Data will be made available on request"，无公开代码仓库链接 |
| Braga 等 (2026), *J. Transp. Geogr.* 131:104526. DOI: 10.1016/j.jtrangeo.2025.104526 | 摘要/记录级：仅确认卷期与 DOI（出行时间变异与岗位竞争可达性不平等主题），全文未获开放获取，方法细节与图未查到 | 未查到 | 未查到 |

#### Applied Geography（1 篇全文级 + 1 篇部分全文 + 1 篇摘要级）

| 文章 | 技术栈 | 图的类型与数量 | 代码/数据公开 |
|---|---|---|---|
| Yang、Bai、Zou (2026) "Spatial inequities in urban resource access, neighborhood social capital, and late-life depression", *Applied Geography* 188:103920. DOI: 10.1016/j.apgeog.2026.103920 | 香港 5007 名 50 岁以上老人、1746 个 LSUG、18 区；指数距离衰减模型（α=0.001，路网最短路径）算四类设施（公园、公交、医疗、老年服务）可达性；区内 Gini 衡量不平等；PCA 得 RA/RI 两因子；R 4.5.0 的 `lm()` 做带区固定效应的加权线性回归；Moran's I 检验残差（I=0.069, p=0.165）；路网距离计算工具未具名，统计软件仅明确 R | 图 1 理论框架概念图；图 2 研究区地图；图 3 四类设施 Gini 分位数 choropleth 多面板；另有交互效应图 | 未找到代码/数据公开链接 |
| Kim、Kwon、Horner (2025) "Introducing rational agent access model to enhance scene-to-hospital accessibility of emergency medical services", *Applied Geography* 182:103721. DOI: 10.1016/j.apgeog.2025.103721 | 摘要/记录级：RAAM（源自 Saxon & Snow 2019）对比 G2SFCA，首尔急救场景—医院可达性，以真实患者转运数据验证；RAAM 与实际转运时间、候诊时间、患者分配模式的相关性优于 G2SFCA | 未查到 | 未查到 |
| Zhong 等 (2024) "Intercity patient mobility can improve healthcare accessibility and equality in metropolitan areas: A case study of Shenzhen metropolitan area, China", *Applied Geography* 171:103383. DOI: 10.1016/j.apgeog.2024.103383 | 部分全文级（机构库全文 PDF，摘要与方法片段已读）：2SFCA + 考虑效率与公平的两步优化；Lorenz 曲线（图 3）与 Gini 系数量化公平；跨市患者流动使既有服务可达效率/公平提升 8%/6%，优化后较现状提升 37%/19% | 图 3 为 Lorenz 曲线；其余图未系统清点 | 软件栈未查到 |

#### Health & Place（3 篇，均为摘要级）

2024–2025 年相关论文多为 Elsevier 付费墙，本次未找到 OA 全文；以下三篇仅读到摘要/记录页，方法细节与图未查到。

| 文章 | 已知内容 | 未查到 |
|---|---|---|
| Zumelzu、Fierro、Herrmann-Lunecke (2025) "Mental wellbeing and aging in place", *Health & Place* 93:103471. DOI: 10.1016/j.healthplace.2025.103471 | 质性 go-along 步行访谈 50 人；高度步行友好 + 本地商铺提升社区联结与安宁；无 GIS/软件栈 | 方法细节与图 |
| Kong、Han、Chi、Zhan (2025) "The association between neighborhood built environment and mental health among older adults in Hangzhou, China", *Health & Place*. DOI: 10.1016/j.healthplace.2025.103415 | 1405 名杭州老人，10 项建成环境指标，结构方程模型 | 方法细节与图 |
| Kawaguchi 等 (2025) "Neighborhood Walkability and Subsequent Health and Well-Being in Urban and Rural Japan", *Health & Place* 96:103549 | 纵向研究 | 方法细节、图与 DOI（本次检索未确认） |

### 5.2 顶刊实际在用什么技术栈：清单对照

**抽样结论**：顶刊实证主流是“方法自述 + 通用统计/GIS”，而非本清单的专用可达性引擎。

- **被顶刊明确点名的清单工具**（4 项，均非本次 12 篇抽样正文直接采用，而是方法来源或关联证据）：
  - **OpenTripPlanner**：一篇 PNAS Nexus 纽约公交可达性研究的补充材料明确用 OTP（OSM 路网 + GTFS）构建公交网络。
  - **R5**：GISRUK 2026 论文用 R5 引擎 + 英国 BODS 实时公交数据做全国公交可达性（会议论文语境）。
  - **r5r**：一篇比较 12 种可达性测度的加拿大学习用 `r5r` + GTFS + OSM（ScienceDirect 摘要级证据）。
  - **PySAL access 的 RAAM**：Kim 等 (2025) 的方法来源（RAAM 源自 Saxon & Snow 2019，`access` 包亦实现该方法），非本文直接采用。
- **在抽样顶刊全文中未见直接点名采用的清单工具**：`access`、`segregation`、`inequality`、Pandana、UrbanAccess、GOAT、`accessX`、`r2sfca`、EJAM、findSVI、AccessMod、huff、geometrics、UCID 等。
- **顶刊实际高频出现的栈**：R（`lm`、PCA、Moran's I）、NetLogo（AxS 智能体模型）、自研 ABM、Openrouteservice API、SafeGraph 等专有移动数据；2SFCA/G2SFCA/Lorenz/Gini 是方法层通用语言，但实现多为作者自研代码而非点名引用专用包。
- **方法语境补充**（非四刊抽样，仅作对照）：Soukhov 等 (2025) "A family of accessibility measures derived from spatial interaction principles", *PLOS ONE* 20(11):e0335951, DOI: 10.1371/journal.pone.0335951（PMC 全文）：理论型，Hansen 型/总量约束/单约束（≈2SFCA）/双约束四成员，仅 2 幅图，数据与分析代码在 `github.com/soukhova/Family-of-accessibility-measures`；中国 1 km 医院可达性全国数据集（*Scientific Data* 2024, 11:1130, DOI: 10.1038/s41597-024-03981-y）：Ga2SFCA，OSM + Contraction Hierarchies 路径算法，WorldPop 人口，数据在 figshare，文中称“全部输入数据开放获取、代码公开”；2SFCA/E2SFCA ArcGIS Pro 工具箱（*JMIR Form Res* 2024;8:e51727, DOI: 10.2196/51727）：Python 脚本工具，ArcGIS Online 免费提供。

**对工具选型的指导意义**：顶刊点名率低不等于工具无用——抽样同时显示顶刊代码/数据公开率很低：12 篇抽样中没有一篇给出公开代码仓库（GitHub 等）链接，最接近的是 Araujo 等的 AxS 模型主页（个人网站）与 Abbiasov 等的“可向作者索取”；作为对照，语境补充的两篇（PLOS ONE 方法论文、Scientific Data 数据论文）给出了公开代码/数据链接。专用开源工具的价值正在于可复现性：做研究时，用 OTP/R5/`r5r` 做时刻表敏感的出行时间矩阵（顶刊认可的底座），用 `access`/`r2sfca`/`accessibility`（R）做测度层并公开代码，是兼顾顶刊惯例与可复现性的组合；不要以“顶刊没点名”否定一个工具，也不要以“顶刊点名”作为唯一选型依据。

### 5.3 从顶刊图幅提炼的可视化规范（5 条）

以下规范只写本次抽样全文中**实际见到**的组织层面事实；配色方案、字体、字号、线宽等细节因本次抽样为 PDF 文本层提取，无法可靠判断具体色值与字号，**写“未查到”，不编造**。

1. **图 1 定调：概念框架或研究区地图**。几乎每篇全文的图 1 都是理论框架概念图（Yang 图 1、Tu 图 1 a–b、Xu 图 1、Araujo 图 1）或研究设计/情景示意图（Aravind 图 1），而不是直接上结果图。做法：先用一幅图把“概念—数据—方法”讲清楚，再出结果。
2. **结果图用多面板 choropleth 按变量分面**。Yang 图 3 按四类设施分面的 Gini 分位数 choropleth、Aravind 图 10 孟菲斯四面板地图 a–d、Araujo 图 8 按性别/收入分位的差距地图、Tu 图 4 按基础设施类型分面的 Gini/HALE 图，都是同一范式：一个图内并列多个同尺度小地图，面板间只换一个变量。做法：分面变量取设施类型、情景或人群分组，保持色标与分级一致。
3. **图例用分位数/等值色带 + 数值标注**。结果地图的图例多为分位数色带（Yang 图 3）或等值色标，配合统计图中的具体数值（如 Gini 0.88→0.71、Gini 均值 0.83±0.12）。做法： choropleth 优先用分位数分级并在图注中写明分级方法与数值范围。
4. **统计图与地图分工明确**。Lorenz 曲线（Zhong 图 3、Aravind）、折线图（Soukhov 图 1 文献趋势）、交互效应图（Yang）与地图分开成图，不把统计曲线塞进地图面板。做法：一幅图只承担一种信息类型；分布/不平等类结论用 Lorenz/Gini 图，空间格局用地图。
5. **多面板用字母编号 + 每面板小标题**。Xu 图 1 a–d、Aravind 图 10 a–d、Tu 图 1 a–b 均用字母编号区分面板并配小标题。做法：面板编号 a、b、c、d，正文按编号引用；每面板加一行小标题说明该面板的变量。
6. **配色、字体、底图风格：未查到（本次抽样）**。文本层提取无法判断具体色值、字体与字号；底图风格亦未做逐图统计。作为通用学术惯例建议（**非本次抽样结论**，仅供参考）：用色盲友好的顺序色标做单变量 choropleth、用发散色标做差距图、底图用浅色行政区划线划、不在底图上叠加强饱和度商业底图。采用前请以目标期刊的制图指南为准。

### 5.4 本节局限

- Health & Place 抽样为摘要级，未能看到全文和图；图幅观察主要来自 Applied Geography、JTG 与 NHB 的全文样本（6 篇全文级 + 1 篇部分全文）。
- 期刊抽样量小（每刊 3 篇），结论为抽样观察而非期刊全貌统计；“未见点名采用”指本次抽样未见，不等于该工具从未被顶刊采用。
- 配色/字体/线宽/底图风格未查到，见 5.3 第 6 条。

## 6. 主要发现与问题

### 6.1 结构性发现

1. **可达性引擎强、福祉测度弱**。30 个项目中约三分之二是可达性/路网/选址工具（OTP、R5 生态、Pandana、UrbanAccess、GOAT、`accessX`、`access`、`r2sfca`、huff、spopt 等），而福祉/幸福感主观测度方向**未查到足够专用开源项目**：唯一进入清单的 TSGI（地理推文情感指数）自 2022-10 后无更新；主观福祉在开源工具层面基本空白，顶刊工作多用专有调查或商业移动数据（见第 5 节）。
2. **2SFCA 是方法层通用语言，但实现分散**。2SFCA/E2SFCA/G2SFCA/RAAM/BFCA 同时出现在 `access`（PySAL）、`r2sfca`、`accessibility`（R）、`fca`（R）、huff、`accessX` 六个包里，API 与距离衰减约定各不相同；`r2sfca` 试图以单一衰减参数统一 2SFCA 与 i2SFCA，是方法上最新颖的实现，但其 GitHub 仓库已 404（见 6.2）。
3. **R 与 Python 两条链并行，Java 引擎居底座**。测度层：R 有 `accessibility` + `fca`，Python 有 PySAL 家族；路由层：Java 的 OTP/R5 是共同底座，`r5r`（R）与 `r5py`（Python）只是封装。选型时先定路由底座（OTP 或 R5），再定测度层语言。
4. **环境正义工具正在经历机构断代**。EPA EJScreen 官网与 CEJST 官网 2025 年初下线；EPA 原版 EJAM 2025 年中归档，后续开发转入非 EPA 的 PEDP fork（MIT，2026-11-09 仍有提交）；CEJST v1.0（`justice40-tool`）已移交 DOI-DO/j40-cejst-2（v2）。用这些工具须认准当前维护方，旧官网链接多已失效。
5. **新包活跃、老包分化**。2026 年新包 `accessX`（1 月建库，9 月仍有提交）、geometrics（7 月 v0.1.3）与 UCID 快速迭代；另一边 Pandana 已声明进入 LTS 兼容维护、后续开发转至 Pandarm（`oturns/pandarm`），`fca`（R）停在 2021 年，TSGI 停在 2022 年，citychrone 停在 2023 年。

### 6.2 逐项风险提示

- **r2sfca GitHub 404**：`github.com/urbananalytics/r2sfca` 2026-11-14 实测返回 404（`git ls-remote` 亦失败），但 PyPI 1.1.3（2025-10-14，MIT）与 ReadTheDocs 文档仍可访问。采用前应确认代码托管现状，或改用 PySAL `access` 的 2SFCA/E2SFCA 实现作为替代；引用时留档 PyPI 版本与论文（Liu & Wang 2025, *IJGIS*）。
- **ejscreen GitHub 404**：`github.com/ejanalysis/ejscreen` 同日实测 404；代码疑似已并入 EJAM 仓库（`ejanalysis/EJAM` ls-remote 成功，HEAD `f852f50`，与 PEDP fork 一致）。
- **personalised-urban-accessibility 默认路径过期**：`src/analysis/scoring.py` 的 `DEFAULT_PRESETS` 指向不存在的 `presets_v2.json`，当前预设文件为 `presets_v3.json`（实测时须显式传路径）；另有注释说明旧 pickle 为已废弃的插值版本，不得再作默认。
- **GOAT 组织名迁移**：克隆地址仍为 `goat-community/goat`，但 README 徽章链接已指向 `plan4better/goat`；另其云端现为订阅 SaaS，免费版为试用性质。
- **accessmod 许可证位置特殊**：许可证文本在仓库根目录的 `COPYING` 文件（LGPL-3.0），而非惯常的 `LICENSE` 文件；GitHub API 显示 LGPL-3.0 与之一致。
- **r5r/r5py 双许可**：仓库 LICENSE 文件写明 "GPL-3.0-or-later or MIT"，GitHub API 未识别（NOASSERTION），以仓库文件为准。
- **spopt API 易误用**：`facility_client_array()` 与 `get_mean_distance()` 返回 None，结果写在 `m.fac2cli` 与 `m.mean_dist` 属性上（0.8.0 实测确认）；`PMedian.solve()` 须显式传入 pulp 求解器（如 `PULP_CBC_CMD(msg=False)`）。
- **accessx 要求 OSMnx 风格图**：`count_accessible_pois` 等函数内部调用 OSMnx 的 `nearest_nodes`，节点 ID 须为整数 osmid（元组 ID 会触发 `TypeError: Must pass list-like as 'names'`）；图须带 `graph['crs']`。
- **huff 需离线声明**：官方示例默认用 OpenRouteService 联网算车行时间（需 API token）；离线可用 `transport_costs(network=False)` 算欧氏距离，但须先 `define_weightings` 定义 `t_ij` 权重，否则 `floating_catchment` 报 `WeightingError`（实测确认）。

### 6.3 选型建议（按任务类型）

| 任务 | 首选 | 备选/搭配 |
|---|---|---|
| 真实公交时刻表约束的可达性 | OTP（部署）或 R5 + `r5r`/`r5py`（研究） | 测度层配 `accessibility`（R）或 PySAL `access` |
| 2SFCA 类医疗/公共服务可达性 | PySAL `access`（2SFCA/E2SFCA/RAAM） | `r2sfca`（方法新但仓库 404，留档版本）；`accessibility`（R，含 BFCA 与不平等测度） |
| 15 分钟城市/生活圈快速分析 | `accessX`（Python 库，2026 新） | GOAT 云端试用（零部署）；citychrone（已停滞，不推荐新项目） |
| 空间不平等/隔离测度 | `inequality`（Gini/Theil）+ `segregation`（Dissim 等） | geometrics（区域收敛/不平等，教学友好） |
| 设施选址（公共服务均等化） | `spopt`（p-median/p-center/最大覆盖） | — |
| 社会脆弱性指数 | findSVI（CDC/ATSDR SVI，需 R + Census API） | devPTIpack（世行 PTI，需 R/Shiny）；`justice40-tool`（美国 CEJST，需认准 v2 维护方） |
| 环境正义 | EJAM（PEDP fork，R） | EJScreen 数据镜像（官网已下线） |
| 主观福祉/幸福感 | 未查到足够专用开源项目；TSGI（2022 年后未更新）仅可作历史参考 | 建议用调查数据 + 通用统计栈（R/Python），不要硬套本清单工具 |

### 6.4 未查到清单

- 主观福祉/幸福感专用开源测度工具：除 TSGI 外**未查到足够项目**（另有 WWBP 县级词汇库 `wwbp/county_tweet_lexical_bank` 未纳入本次克隆，仅作线索）。
- 健康地理专用 R/Java 之外的轻量 Python 医疗可达性包：除 huff（市场区兼健康地理）与 `access` 的 RAAM 外，未查到更多。
- Health & Place 期刊的 OA 全文：2024–2025 年相关论文未找到 OA 全文（见 5.1、5.4）。
- Kawaguchi 等 (2025) *Health & Place* 96:103549 的 DOI：本次检索未确认。
- `ejanalysis/EJAM` 上游仓库与 PEDP fork 的分工细节：二者 HEAD 一致（`f852f50`，2026-11-09），上游核心文件已恢复核实（MIT，与 PEDP fork 相同）；两仓库 README 相同，未见分工说明，分工未查到。
