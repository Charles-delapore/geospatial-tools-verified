# 领域六：跨领域 Skills 与 MCP —— GIS / 地理分析相关的 Claude Skills、Agent Skills 与 MCP 服务器

**报告日期：2026-11-14（快照日）｜研究员：接续研究员（从头接手，前任被运行时重启中断三次，未留 REPORT.md）**

> 本报告基于本地已克隆的 26 个仓库、`figures/` 下 14 个验证日志文本（任务交接时称 7 个，接手盘点时为 13 个，本次复跑新增 1 个）与 `tmp/` 下的复跑脚本写成。GitHub stars / 最近推送时间取自 GitHub API 快照（2026-11-14，见 `tmp/gh_snapshot_2026-11-14.json`）。所有“未查到 / 未验证”均为如实标注，不作推测性补全。

---

## 1. 方法与口径

### 1.1 收录范围

本域收录与 GIS / 地理分析相关的三类东西，统一按“项目”计数：

- **MCP 服务器**：把地理工具、数据或服务暴露给 AI 助手（如 QGIS MCP、PostGIS MCP、OSM MCP、STAC MCP、GeoServer MCP、Mapbox MCP 等）；
- **Agent Skills / Claude Skills**：以 `SKILL.md` + 参考文档形式给 agent 的工作流、规范与检查清单（如 GIS-Development-Skills、openmapstack-skills、GeoLibre skill）；
- **注册表 / 元项目**：本身不是服务器，而是收录、编目 MCP 服务器的清单（如 sparkgeo/geo-mcp-servers，114 条）。

### 1.2 逐项核查方法

1. 对 `repos/` 下 26 个目录逐个读 README 头部、LICENSE 文件、目录结构，确认“这是什么、给谁用、靠什么外部服务”；
2. 许可证优先以仓库内 LICENSE / LICENSE.md 文件为准，再与 GitHub API 的 `license.spdx_id` 对照；两者不一致时以仓库文件为准并在表中注明；
3. stars 与最近推送（pushed_at）取 GitHub API 快照（2026-11-14 一次性拉取 26 条，未逐条刷 API；限额使用前余量 59/60）。**注意**：本地克隆的 HEAD 提交日期在个别仓库上落后于 API 的 pushed_at（如 gdal-mcp、stac-mcp），说明本地克隆不是最新；表中“最近更新”以 API pushed_at 为准，并在备注中标出本地 HEAD 日期；
4. 验证状态只认 `figures/` 下的日志文本：日志中出现 `TOOLS_COUNT=N` 且无致命启动错误，才算“工具列表实测通过”；只有报错堆栈的算“未跑通”；没有任何日志的算“未验证”。**日志中的推测、README 宣称的工具数、第三方榜单分数，一律不写成实测通过**；
5. 同名项目严格区分：两个 `geoserver-mcp`（acupai / mahdin75）、两个 `qgis-mcp`（nkarasiak / jjsantos01）、三个 `osm-mcp`（jagan / ni-c / GRABOSM）、两个 `stac-mcp`（BnJam / bbrauzzi）分别立项；`pg-mcp`（stuzero）实为文档站，其源码已迁出，不与 `pg-mcp-server` 混淆；`server-google-maps` 只是 `modelcontextprotocol/servers` 单体仓库中的一个参考实现，其 91,976 stars 是整个单体仓库的数，不是 Google Maps 服务器的数。

### 1.3 验证口径（重要限定）

- **“实测通过”在本报告中仅指：服务器进程能以 stdio 方式启动，并成功返回工具列表（`list_tools`）**。前任研究员的 9 次成功验证全部是这一口径：**没有一次日志显示真实调用了某个地理工具并核对了计算结果**（如真的做一次 buffer、真的查一次 STAC、真的连上 QGIS 改一个图层）。因此“通过”≠“功能正确”，≠“生产可用”。
- QGIS MCP（nkarasiak）的 125 个工具是在**未连接 QGIS** 的情况下列出的（日志首行即说明“will connect on first call”）；`ping`、`get_qgis_info` 等工具的真实连通性本次未验证，需要一台装有 QGIS + 插件的机器才能验证。
- GeoServer / STAC / OSM 类服务器的工具列表本身不需要连上后端服务即可列出；真实调用是否成功、是否要 key、配额如何，本次均未验证。

### 1.4 数字口径

- stars 量级按快照值分档：0–10 为“个位数 / 刚起步”，11–100 为“两位数”，101–1,000 为“三位数”，1,001–10,000 为“四位数”，10,000+ 为“五位数以上”。表中同时给出精确快照值。
- 凡 stars 属于“整个单体仓库 / 整个技能合集”而非本项目本身的（如 `modelcontextprotocol/servers`、K-Dense scientific-agent-skills），表中明确标注，不把合集热度算到单个地理项目头上。

---

## 2. 项目总表（26 个，快照日 2026-11-14）

| # | 项目 / 仓库 | 许可证 | Stars（快照） | 最近推送 | 用途一句话 | 验证状态 | 传输方式 | 外部服务依赖 |
|---|---|---|---|---|---|---|---|---|
| 1 | Axion-MCP — `Dhenenjay/Axion-MCP` | MIT | 5 | 2025-11-08 | Google Earth Engine 的 MCP 接入，把 Claude Desktop 变成遥感分析工作站；自称 6 个“超级工具” | 未验证 | stdio / SSE（仓库含两种配置） | Google Earth Engine 账号与凭证 |
| 2 | cesium-ai-integrations — `CesiumGS/cesium-ai-integrations` | Apache-2.0 | 94 | 2026-08-19 | Cesium 官方的 AI 集成旧仓：CesiumJS MCP 与 agent skills | 未验证 | 未查到（仓库已声明弃用） | Cesium ion 等（按迁移目标而定） |
| 3 | cesium-mcp — `gaopengbin/cesium-mcp` | MIT | 151 | 2026-11-13 | 个人维护的 Cesium MCP：浏览器 / MCP runtime 四种接入，宣称 60+ 工具 | 未验证 | stdio（MCP runtime）；另有 WebMCP / 浏览器 agent 路径 | CesiumJS 运行环境；**注意：用量统计默认开启**，需 `CESIUM_TELEMETRY_DISABLED=1` 关闭 |
| 4 | gdal-mcp — `Wayfinder-Foundry/gdal-mcp` | MIT | 85 | 2026-05-25（本地 HEAD 2026-05-21，克隆滞后） | 把 GDAL / Rasterio 的栅格、矢量操作暴露为 MCP 工具，带“方法论自证”中间件 | ✅ 工具列表实测通过（13 个） | stdio | 无（本地 GDAL / Rasterio；可选 Docker） |
| 5 | gee-mcp — `FrontierDevelopmentLab/gee-mcp` | MIT | 9 | 2026-06-02 | Google Earth Engine MCP：数据集发现、元数据、分析原语与 GEE 代码生成 | 未验证 | stdio | Google Earth Engine 账号与凭证 |
| 6 | geo-mcp-servers（注册表）— `sparkgeo/geo-mcp-servers` | MIT | 248 | 2026-11-05 | 地理 MCP 服务器编目：114 条，含健康状态与部署 / 访问分级，附一个 Claude skill | 未验证（注册表本身不是服务器） | 不适用 | 不适用 |
| 7 | GeoClaw-Claude — `whuyao/GeoClaw_Claude` | **未声明**（README 自称 MIT，但仓库无 LICENSE 文件，API 亦返回 null） | 34 | 2026-03-11 | UrbanComp Lab 的自然语言城市地理分析 agent 框架（v3.2.0），文件系统 + 代码执行 + 网络请求 | 未验证 | 未查到（非 MCP 服务器，是 agent 框架） | LLM API；作者明确警告应在沙箱 / 虚拟机中运行 |
| 8 | GeoLibre — `opengeos/GeoLibre` | MIT | 8,602 | 2026-11-13 | 云原生开源 GIS 平台（桌面 / Web / Jupyter），以 `.geolibre.json` 工程文件为 agent 接口，附 1 个 skill 与 `geolibre-mcp` | 未验证（仅核查到 skill 文件存在） | 未查到（skill 提及 `geolibre-mcp`，但本仓库内未核查其服务器实现） | 可本地运行；分享 / 插件服务为可选在线服务 |
| 9 | scientific-agent-skills（Geomaster）— `K-Dense-AI/scientific-agent-skills` | MIT | 57,064（整个技能合集，非地理单项） | 2026-11-09 | 科学 agent 技能合集，宣称 177 个 skills；其中地理相关为 `geomaster` 一个 skill 目录 | 未验证；**本地克隆仅见 `skills/geomaster/` 一个 skill 目录，README 宣称的 177 个未在本地核实** | 不适用（skill 文件，非服务器） | 按各 skill 而定，未查到 |
| 10 | geoserver-mcp — `acupai/geoserver-mcp` | MIT | 0 | 2026-07-12 | GeoServer REST API 的 MCP 封装（与 mahdin75 版同源分叉倾向明显，见 §3.4） | 未验证 | stdio / Streamable HTTP / SSE（README 明示三种） | 自有 GeoServer 实例 + 账号密码 |
| 11 | geoserver-mcp — `mahdin75/geoserver-mcp` | MIT | 97 | 2026-08-16 | 同上：GeoServer 工作区、图层、样式、用户与系统操作的 MCP 封装 | ✅ 工具列表实测通过（56 个） | stdio（实测）；README 另有 Docker / Smithery 部署 | 自有 GeoServer 实例（仅列工具不需连接；真实调用需连接） |
| 12 | GIS-Development-Skills — `ahmadibrahim4geo/GIS-Development-Skills` | MIT | 6 | 2026-10-30 | 35 个 GIS 开发 skills：QGIS / ArcGIS 插件、空间数据库、遥感管线、制图等 | 未验证（仅清点到 35 个 `SKILL.md`） | 不适用（skill 文件） | 按各 skill 而定 |
| 13 | gis-mcp — `mahdin75/gis-mcp` | MIT | 205 | 2026-08-21 | 通用 GIS MCP：矢量 / 栅格 / 坐标 / 空间统计 / 卫星影像，宣称 92+ 工具 | ✅ 工具列表实测通过（91 个，**带警告**，见 §4） | stdio | 部分工具依赖 Microsoft Planetary Computer、气候 / 生态等可选模块与外部服务 |
| 14 | gis-mcp-server（LocuSync）— `matbel91765/gis-mcp-server` | MIT | 4 | 2026-07-08 | 地理编码、路径、空间分析 MCP（PyPI 名 `locusync-server`，仓库 README 即以 LocuSync 为标题） | ✅ 工具列表实测通过（46 个） | stdio | Nominatim、OSRM 公共服务（日志明示）；高程等亦走在线服务 |
| 15 | mapbox-mcp-server — `mapbox/mcp-server` | MIT | 370 | 2026-11-13 | **官方** Mapbox MCP：地理编码、POI、路径、等时线、地图匹配、渲染 | 未验证 | stdio；另有 hosted HTTP 指南 | Mapbox API token（必需）、Mapbox 平台服务 |
| 16 | open-streetmap-mcp — `jagan-shanmugam/open-streetmap-mcp` | MIT | 234 | 2025-07-12（本地 HEAD 2025-06-30，克隆滞后） | OSM MCP：地理编码、周边、路径、聚会点优化、区域画像 | ✅ 工具列表实测通过（12 个） | stdio | Nominatim / Overpass / OSRM 等 OSM 生态公共服务 |
| 17 | openmapstack-skills — `jaakla/openmapstack-skills` | MIT | 78 | 2026-11-10 | 4 个 skills：可复现 GIS 工程（数据发现、空间 SQL、项目规范、仪表盘交付） | 未验证（仅清点到 4 个 `SKILL.md`） | 不适用（skill 文件） | STAC、GeoParquet / COG、DuckDB / PostGIS、QGIS 等（按 skill 而定） |
| 18 | osm-mcp — `GRABOSM/osm-mcp` | MIT | 6 | 2026-01-23 | Grab 社区 OSM MCP，宣称 30 个工具（地理编码、路径、质检、分析） | 未验证 | 未查到（README 未在核查范围内明示传输方式） | OSM / OSRM 等公共服务（按 README 描述推断，未实测） |
| 19 | osm-mcp — `ni-c/osm-mcp` | MIT | 6 | 2026-11-10 | OSM MCP：地理编码、路径矩阵、TSP 优化、等时线、POI | ✅ 工具列表实测通过（11 个） | stdio（实测）；另有 HTTP（经 mcp-hub）与容器镜像 | 公共 OSRM / Valhalla（日志首行明示） |
| 20 | pg-mcp — `stuzero/pg-mcp` | **未声明**（无 LICENSE 文件） | 28 | 2025-04-15 | **仅为文档站**：源码已迁至 `stuzero/pg-mcp-server` 与 `pg-mcp-client`，本仓库无服务器代码 | 未验证（不适用：无可运行物） | 不适用 | 不适用 |
| 21 | postgis-mcp — `receptopalak/postgis-mcp` | **未声明**（无 LICENSE 文件） | 21 | 2026-04-21 | TypeScript PostGIS MCP：以 MCP 连接 PostGIS 数据库 | 未验证 | 未查到（未在核查范围内确认传输方式） | 自有 PostGIS 数据库 |
| 22 | qgis-mcp — `nkarasiak/qgis-mcp` | **GPL-2.0** | 436 | 2026-11-11 | QGIS MCP：125 个工具，图层、要素编辑、处理算法、渲染、布局、跨层 SQL | ✅ 工具列表实测通过（125 个，两次日志一致） | stdio（MCP 服务器）＋ TCP socket（连 QGIS 内插件，默认 localhost:9876） | QGIS 3.28–4.x + 插件（真实操作必需；仅列工具不需要） |
| 23 | qgis_mcp — `jjsantos01/qgis_mcp` | **未声明**（无 LICENSE 文件） | 1,152 | 2025-10-01 | 较早的 QGIS MCP（BlenderMCP 思路，socket 双向通信），QGIS 项目 / 图层 / 处理算法 / 代码执行 | ❌ 未跑通（3 次失败日志，见 §4） | stdio（设计上）；实测未能启动 | QGIS + 插件（未能启动到需要 QGIS 的阶段） |
| 24 | server-google-maps（单体仓库内）— `modelcontextprotocol/servers` | 过渡中：MIT → Apache-2.0（API 返回 NOASSERTION） | 91,976（**整个单体仓库**，非 Google Maps 服务器） | 2026-11-12（整个仓库） | 官方 MCP 参考实现合集；其中 Google Maps 服务器提供地点、路线与地点详情 | 未验证；**且该服务器已移至 `servers-archived`，本仓库 `src/` 下已无 google-maps 目录** | stdio（参考实现惯例，未实测） | Google Maps API key（必需） |
| 25 | stac-eo-mcp — `bbrauzzi/stac-eo-mcp` | MIT | 0 | 2026-10-29 | STAC MCP：搜 Sentinel-2 场景并算 NDVI / NDWI / NBR，不下载整景 | ✅ 工具列表实测通过（5 个） | stdio | 默认 Microsoft Planetary Computer STAC |
| 26 | stac-mcp — `BnJam/stac-mcp`（Wayfinder-Foundry 组织下亦有同名） | MIT | 20 | 2026-11-05（本地 HEAD 2026-08-07，克隆滞后） | 通用 STAC MCP：目录、集合、单品检索，text / JSON 双输出 | ✅ 工具列表实测通过（11 个） | stdio | 任意 STAC API（由调用方指定） |

**小计**：26 个项目中，MCP 服务器 19 个（含 1 个已弃用、1 个仅文档站、1 个已归档）、纯 skills 合集 6 个（#9、#12、#17 及 #6 注册表附带的 skill、#8 的 1 个 skill、#2 的 skills 目录——按主形态计入上表）、注册表 1 个。许可证：MIT 19 个、Apache-2.0 1 个、GPL-2.0 1 个、过渡中 1 个、**未声明 4 个**（#7、#20、#21、#23）。

---

## 3. 重点项目深挖

### 3.1 QGIS MCP：两条路线，一条能跑、一条已断（#22 vs #23）

这是本域最重要、也是最容易混淆的一对。

**nkarasiak/qgis-mcp（#22，GPL-2.0，436 stars，2026-11-11 更新）——本域唯一达到“活跃 + 可验证 + 工具最全”的项目。**

- 架构：MCP 服务器（FastMCP，stdio）←→ TCP socket ←→ QGIS 内插件（QTimer 事件循环内处理 JSON 命令）。README 宣称 125 个工具，覆盖图层管理、要素增删改、处理算法、渲染、样式、布局与图集、跨层 SQL、插件开发、系统管理，兼容 QGIS 3.28–4.x，客户端不限（Claude Code、Codex CLI、Gemini CLI、Cursor、VS Code 等）。
- 验证：两次日志（`verify-qgis-nkarasiak-tools.txt` 与 `-rerun.txt`）内容完全一致，均为 `TOOLS_COUNT=125`，与 README 宣称吻合。**但两次都是在未连接 QGIS 的情况下列出的工具**（日志首行：“will connect on first call to: default=localhost:9876”）。也就是说，125 这个数字验证的是“服务器能启动、工具已注册”，不是“能在 QGIS 里干活”。
- 采用者线索：第三方博客 terra-lab.ai（2026-11-07 实测文）称 QGIS 插件库中该插件 v0.15.2 下载量 77,002 次（截至 2026-11-07）。**该数字未独立核实**，仅作线索记录；本报告未访问 QGIS 插件库核对。
- 许可证注意：**GPL-2.0**，是本域 26 个项目里唯一的 copyleft 许可证；若把它的代码并入闭源产品，需要法务评估。QGIS 插件本身也受 QGIS 的 GPL 约束，这一点与 MIT 为主的其他项目不同。
- 安装难度：中等。需要 QGIS 3.28+ 与 uv；插件与服务器分开装；真实使用还要处理端口、QGIS 版本匹配（日志提到版本匹配诊断）。

**jjsantos01/qgis_mcp（#23，无许可证声明，1,152 stars，2025-10-01 后无更新）—— star 最多的 QGIS MCP，却是本域唯一“三次都跑不起来”的项目。**

- 它是 2025 年 3 月的老项目，思路源自 BlenderMCP，socket 双向通信，功能包括项目操作、图层操作、处理算法与“在 QGIS 里执行任意 Python 代码”（README 自己提醒“非常强大，但要非常谨慎”）。
- 三次失败日志各不相同，说明前任研究员换了两种环境仍未解决：
1. `verify-qgis-jjsantos-tools.txt`（venv_mcp，mcp 2.x）：`No module named 'mcp.server.fastmcp'`——mcp 2.x 已把 FastMCP 改名为 MCPServer，旧 import 直接失效；
2. `verify-qgis-jjsantos-tools-rerun.txt`（venv_mcp1x，mcp 1.x）：`FastMCP.__init__() got an unexpected keyword argument 'description'`——1.x 的 FastMCP 构造参数与代码写法不匹配；
3. `verify-qgis-jjsantos-tools-rerun2.txt`：同样未跑通（0 个工具，日志以连接关闭告终）。
- 结论：**该项目在 2026-11-13 的 Python MCP SDK（1.x 与 2.x）下均无法启动，属于“代码已落后于 SDK”的状态**，不是环境配错。它的 1,152 stars 是历史积累（2025 年上半年 QGIS MCP 几乎只有它），不能作为今天可用的依据。最后提交 2025-10-01，之后 13 个月无更新。
- 安全提示：即使修好，它“执行任意 Python 代码”的设计意味着接上 QGIS 后 agent 能在桌面环境执行任意代码，**只能在受控机器上用**，与 GeoClaw 的沙箱警告同理。

**两条路线的取舍**：新用 QGIS MCP，选 nkarasiak 版；jjsantos 版只作为历史参考。不要因为 star 数（1,152 vs 436）选错。

### 3.2 通用 GIS MCP：mahdin75/gis-mcp（#13）——工具最多，但“全功能”要打折扣

- 规模：README 宣称 92+ 工具；实测 `TOOLS_COUNT=91`（一次成功日志）。工具覆盖 geopandas 矢量、shapely 几何、rasterio 栅格、pyproj 坐标、PySAL 空间统计（Moran's I、Getis-Ord、空间 Markov、空间回归等）、可视化与卫星影像下载。
- **实测中的三个折扣**（都在 `verify-gis-mcp-mahdin75-tools.txt` 里）：
1. 启动时 5 个可选模块导入失败：`pygadm`（行政区划）、`cdsapi`（气候）、`pygbif`（生态）、`osmnx`（移动）、`folium`（可视化），日志明确提示需 `pip install gis-mcp[administrative-boundaries]` 等 extras。也就是说，**默认安装下 91 个工具里有一批是“挂名但不可用”的**，具体多少个工具受影响，日志未逐项标出，未查到；
2. 日志中段出现一次 `Failed to parse JSONRPC message from server`，原因是服务器往 stdout 打印了一行 `Starting GIS MCP server with STDIO transport...`，破坏了 JSON-RPC 流，随后客户端抛 pydantic 校验错。工具列表最终仍打印完整，但这说明**该服务器的 stdio 实现有 stdout 污染问题**，在有的客户端上可能直接断连；
3. 卫星影像类工具（`download_satellite_imagery`、`compute_s2_ndvi` 等）依赖 Microsoft Planetary Computer（STAC + SAS），需要联网与上游可用性。
- 活跃度：205 stars，PyPI 有包（`gis-mcp`），有官网 gis-mcp.com；但最近推送 2026-08-21，距快照日近 3 个月无更新。安装难度中等偏上：Python 3.11+，geopandas / rasterio 等重型依赖，extras 按需装。

### 3.3 OSM MCP：三个同名项目，实测分出高下（#16、#19、#18）

- **jagan-shanmugam/open-streetmap-mcp（#16，234 stars）**：12 个工具实测通过。亮点是两个“场景化”工具：`suggest_meeting_point`（多人聚会点优化）与 `explore_area`（区域画像），README 配有三张演示动图。依赖 OSM 生态公共服务。最后推送 2025-07-12，之后 4 个月无更新，但工具列表仍能跑。
- **ni-c/osm-mcp（#19，6 stars）**：11 个工具实测通过，日志首行即说明“routing via public OSRM/Valhalla”。工具设计最“产品化”：`route_matrix`（多对多耗时矩阵）、`optimize_route`（TSP）、`isochrone`、`poi_details`（取 OSM 全部 tag，含营业时间、电话、网址）。2026-11-10 仍在更新（当天有 Dependabot 升 Node 的提交），是三者中唯一仍活跃的；另有 HTTP 接入（经 mcp-hub）与容器镜像。star 只有 6 个，**热度与质量在此处是反的**。
- **GRABOSM/osm-mcp（#18，6 stars）**：宣称 30 个工具，Grab 社区项目，2026-01-23 后无更新，**本次未验证**。不要因为“30 个工具”的宣称就把它排在前两位之前。
- 共同外部依赖：三者都依赖 OSM 公共服务（Nominatim 地理编码、Overpass、OSRM/Valhalla 路径），都要遵守公共服务的使用政策（Nominatim 有速率限制），不适合高频批量调用。

### 3.4 GeoServer MCP：同源双生，选有验证的那个（#11 vs #10）

- mahdin75 版（#11，97 stars）与 acupai 版（#10，0 stars）README 高度相似，LICENSE 均为 “Copyright (c) 2025 GeoServer MCP Contributors”，acupai 版明确写“移除不再需要的边界框重计算功能”等重构记录，**两者极可能是同源分叉**，但本次未做逐文件 diff，未查到分叉关系声明，不作定论。
- 只有 mahdin75 版有实测日志：56 个工具，覆盖工作区、图层、数据存储、样式（SLD 生成）、图层组、用户与系统操作（`reload_geoserver`、`reset_geoserver` 这种危险操作也在内）。acupai 版的优势只在 README 层面：明示支持 stdio / Streamable HTTP / SSE 三种传输与 Docker、1Panel 部署，但**未经实测**。
- 共同点：都要求自有 GeoServer 实例 + 账号密码；MCP 侧不存数据。采用前必须想好：**把 GeoServer 管理员凭证交给 agent，等于把“删图层、改样式、建用户”的权限交给模型**，生产实例务必用最小权限账号。

### 3.5 STAC MCP：小而实的两个（#25、#26）与注册表（#6）

- **stac-eo-mcp（#25，0 stars，2026-10-29 新建）**：5 个工具实测通过，是本域最小的服务器。定位精准：搜 Sentinel-2 场景、在 bbox 窗口内算 NDVI / NDWI / NBR、做时序均值，**不下载整景**。默认接 Microsoft Planetary Computer。0 stars 不代表不能用——它是 2026-10-29 才建的仓库，新是主因。
- **stac-mcp（#26，20 stars）**：11 个工具实测通过，通用 STAC 目录检索（root、conformance、collections、item），text / JSON 双输出，可接任意 STAC API。注意本地克隆 HEAD（2026-08-07）落后于 API 推送（2026-11-05），本地核查基于旧版。
- **geo-mcp-servers 注册表（#6，248 stars，114 条）**：本域的“地图”。它把 114 个地理 MCP 服务器按语言、部署（本地 / 托管 / 自托管）、类型（官方 / 社区）、健康度（🟢 活跃 / 🟡 沉寂 / 🔴 死亡）、访问（开放 / 免费 / 商业 / 付费墙）分级，并用 `health.json` 跟踪。Sparkgeo 维护，2026-11-05 仍在更新。**本报告的 26 个项目只是它的一个子集**；要找 PostGIS、天气、商业位置平台等本报告未覆盖的服务器，应先查它。它的 ANALYSIS.md 另有市场与缺口分析，本次未深入。

### 3.6 官方与商业：Mapbox MCP 与 Google Maps 参考实现（#15、#24）

- **mapbox/mcp-server（#15，370 stars，2026-11-13 更新）**：本域唯一的**大厂官方**地理 MCP（Mapbox）。功能最全：地理编码、POI、海量路径、等时线、路径优化、地图匹配、实时渲染（`render_map_tool`）。代价是**必须有 Mapbox API token**，用量按 Mapbox 计费；另有 hosted HTTP 接入指南与 evals。未实测（无 token，不注册账号）。
- **server-google-maps（#24）**：官方参考实现，但**已归档迁移**：README 指引到 `servers-archived` 的 google-maps 目录，本地单体仓库 `src/` 下已无该目录。把它当“怎么写一个地点类 MCP 服务器”的范例可以，当现成可用的服务器不行。需要 Google Maps API key。

### 3.7 Skills 侧：四种不同的“技能”形态（#12、#17、#8、#9）

- **GIS-Development-Skills（#12，35 个 skills）**：本域 skills 数量最多且全部可清点（35 个 `SKILL.md`）。覆盖 QGIS 插件开发、ArcGIS 工具箱、空间数据库、遥感管线、制图、移动端 GIS、阿拉伯语国际化等，另有 `mcp-integration-and-tool-orchestration` 与 `geospatial-ai-agents` 两个直接讲 agent 的 skill。缺点是 2026-10-24 才建仓、仅 6 stars，无采用者证据；质量只能逐个读，未逐个验证。
- **openmapstack-skills（#17，4 个 skills）**：最讲究“可复现”：以 `project.yaml` + `pipeline.py` + 仪表盘交付，强调 pinned 数据源、显式 CRS、来源可追溯，带 evals 与示例站。适合“要交出可复核成果”的场景，而非随手问答。
- **GeoLibre skill（#8，1 个）**：只有一个 skill，但定位清晰——“交付物是地图而不是数字时用它”，教 agent 写 `.geolibre.json` 工程文件，再由桌面 / Web / Notebook 三端渲染。
- **Geomaster（#9，1 个本地可见）**：K-Dense 177-skill 合集里的地理 skill。README 宣称 177 个 skills、100+ 数据库，但**本地克隆 `skills/` 下只有一个 `geomaster` 目录**，其余 176 个未在本地出现（可能与克隆方式或仓库结构有关，未查到原因）。引用“177”时必须注明是 README 宣称、本地未核实。

---

## 4. 验证小结

### 4.1 验证总账

| 类别 | 数量 | 项目 |
|---|---|---|
| 工具列表实测通过（stdio 启动 + `list_tools` 成功） | **9** | gdal-mcp（13）、geoserver-mcp-mahdin75（56）、gis-mcp-mahdin75（91）、gis-mcp-server/LocuSync（46）、open-streetmap-mcp-jagan（12）、osm-mcp-ni-c（11）、qgis-mcp-nkarasiak（125）、stac-eo-mcp（5）、stac-mcp（11） |
| 未跑通 | **1** | qgis_mcp-jjsantos01（3 次失败日志，两种 SDK 版本下均失败） |
| 未验证 | **16** | 其余全部（含 6 个纯 skills、1 个注册表、1 个文档站、1 个已弃用、1 个已归档） |

**合计工具数（仅实测通过的 9 个相加）：370 个**（13+56+91+46+12+11+125+5+11）。其中 gis-mcp 的 91 个含 5 个缺失可选模块对应的工具，实际可用数低于 91。

> 注：复跑结果见 §4.3（2026-11-14 复跑一致，125 个工具）。

### 4.2 未跑通与受限原因

| 项目 | 原因（以日志原文为准） |
|---|---|
| qgis_mcp-jjsantos01 | mcp 2.x 下 `mcp.server.fastmcp` 模块已更名，import 失败；mcp 1.x 下 `FastMCP(description=...)` 参数不被接受。代码落后于 SDK，非环境问题 |
| gis-mcp-mahdin75（通过但带病） | 5 个可选模块缺失（pygadm、cdsapi、pygbif、osmnx、folium）；stdout 打印污染 JSON-RPC 流，一度导致客户端解析失败 |
| qgis-mcp-nkarasiak（通过但有限） | 工具列表在未连 QGIS 时列出；真实操作需 QGIS + 插件，本次无 QGIS 环境，未验证 |
| 其余 16 个未验证 | 原因各不相同：无验证日志（大多数）；需要外部账号 / token（Mapbox、Google Maps、GEE、GeoServer、PostGIS）；需要桌面软件（QGIS、GeoLibre 桌面端）；或本身不是可运行物（skills、注册表、文档站、已弃用 / 已归档） |

### 4.3 复跑记录（2026-11-14）

2026-11-14 00:16（UTC 约 11-13 16:16），复用前任研究员留下的 `tmp/venv_mcp`（mcp 2.3.0 + fastmcp 4.2.0，内含 editable 安装的 qgis-mcp 0.15.3）与 `tmp/mcp_list2.py`，对 qgis-mcp（nkarasiak）重做一次 stdio 工具列表调用，TMPDIR 设到 workspace 下，未新建虚拟环境、未安装新依赖。结果：**`TOOLS_COUNT=125`，工具名与 2026-11-13 的两次日志逐项比对完全一致**（diff 无差异），新日志存为 `figures/verify-qgis-nkarasiak-tools-rerun-2026-11-14.txt`。结论：**复跑一致**，125 这个数字在两天、同一环境下可复现。仍需注意：本次复跑同样未连接 QGIS，仅验证工具注册，不验证真实操作。

### 4.4 验证方法复盘：前任研究员留下的东西哪些可信

- **可信**：9 个成功日志都有明确的 `TOOLS_COUNT` 与逐项工具名、描述，可与 README 宣称交叉核对（如 qgis 125、gis-mcp 91 与 README 的 92+ 基本吻合、gdal 13、stac 11/5）。日志时间戳集中在 2026-11-13 22:30–23:13，是一次连续的验证会话。
- **不可直接当结论用的**：日志里没有任何一次真实工具调用；`figures/` 下 12 个文件全是 `.txt` 日志，**没有一张图片**，不要把它们当“截图证据”引用；qgis-nkarasiak 的两个日志内容完全相同（一次是 rerun 复制），只能算一次独立验证 + 一次重复确认，不能算两次独立验证。
- **残留物**：`tmp/` 下有 `venv_mcp`、`venv_mcp1x` 两个虚拟环境与 `mcp_list2.py`、`run_*.py` 三个启动脚本（`run_geoserver_mahdin.py`、`run_jagan.py`、`run_jjsantos.py`），以及 pip 缓存；`tmp/` 总计约 1.3 GB，`repos/` 约 393 MB。复跑应优先复用已有 venv，不要重复建大环境。

---

## 5. 期刊核查（轻量）

本域与期刊关联较弱，按任务要求只做轻量核查，不硬套抽样。

**查到的直接证据（1 篇期刊论文明确以 Skills + MCP 为方法）：**

- **Agentic SWMM**（2026，*AI for Engineering*，MDPI，第 1 期）：加拿大维多利亚大学团队，提出 aiswmm 运行时 + Agentic SWMM 工作流，把 Agent Skills 与 MCP 工具嵌进 SWMM 水文建模，自动完成 QGIS 预处理、SWMM 配置、执行与后处理；案例为 Tod Creek 流域（约 17 km²），QGIS 分水岭出水口检测与商业 PCSWMM 方法的差异在流域周长 0.88% 以内；v0.6.4 含 14 个 Skills、11 个 MCP 服务器、45 个 MCP 工具；主模型为 GPT-5.5 Thinking，QGIS 4.0.2 做 GIS 工作。这是本次核查中**唯一一篇把 MCP、Skills、QGIS 三者同时作为方法核心的期刊论文**。但它是一篇 2026 年新刊（MDPI *AI for Engineering* 创刊号）论文，且作者自述项目仍为 pre-1.0、部分记忆层功能未经验证，证据强度有限。

**查到的相关但未点名 MCP 的期刊工作：**

- Pierdicca 等（2025，*ISPRS International Journal of Geo-Information* 14, 401）：用 GPT-4 与 DeepSeek-R1 把自然语言转成 GIS 工作流（动态生成 Python 脚本），与 10 名资深 GIS 分析师对比，任务时间从约 1 小时 45 分降至约 27 分。**用的是 LLM 生成代码，不是 MCP**。
- Li & Ning（2023，*International Journal of Digital Earth*）“Autonomous GIS”及后续研究议程（*Annals of GIS* 2025, 31(4)）：提出自主 GIS 的五级自主、五大目标与概念框架，有 4 个 GIS agent 概念验证。**属于愿景与框架论文，未采用 MCP**。
- van de Weghe 等（2025，*Journal of Spatial Information Science* 30）：GIScience 与 LLM 整合的机遇与挑战。**综述 / 观点性质，未涉及 MCP 部署**。
- 第 32 届国际制图大会（ICC 2025）摘要：多智能体 GeoAI 系统的开发与案例。**会议摘要，非期刊论文**。

**结论：期刊层面采用证据不足。** 在 2024–2026 年的 GIS / 地理顶刊（IJGIS、IJDE、IJGI、Annals of GIS、JOSIS 等）中，LLM 驱动的 GIS 自动化已有若干论文，但**明确采用 MCP / QGIS MCP / agent skills 作为方法并给出可复现验证的，只有上述 2026 年 Agentic SWMM 一篇**；其余均为 LLM 生成代码或自主 GIS 框架层面的讨论。也就是说，MCP 在地理领域的期刊证据目前处于“萌芽、个案”阶段，远未形成顶刊层面的采纳共识。本报告不把博客、播客（如 Mapscaping 2026-11-12 的 agentic coding 访谈、terra-lab.ai 的 QGIS 实测）算作期刊证据，它们只在正文作线索引用。

---

## 6. 谨慎采用清单

### 6.1 可以试（有实测工具列表 + 活跃 + 依赖可控）

| 场景 | 首选 | 提醒 |
|---|---|---|
| 在 QGIS 里让 agent 干活 | qgis-mcp（nkarasiak，GPL-2.0） | 先在测试工程上试；注意 GPL-2.0；`ping` 等真实连通性仍需在有 QGIS 的机器上验证 |
| 通用矢量 / 栅格 / 空间统计（本地文件） | gis-mcp（mahdin75） | 默认安装缺 5 个可选模块；注意 stdout 污染 JSON-RPC 的问题；卫星影像工具要联网 |
| 栅格 / 矢量格式转换与统计 | gdal-mcp | 最干净的一次验证（13 个工具，无外部依赖）；但 2026-05-25 后无更新 |
| STAC 影像检索 + 指数计算 | stac-eo-mcp（小而专）或 stac-mcp（通用） | 都要联网到 STAC 服务；stac-eo 默认 Planetary Computer |
| OSM 地理编码 / 路径 / POI | osm-mcp（ni-c，仍活跃）或 open-streetmap-mcp（jagan，场景化工具） | 遵守 Nominatim / OSRM 公共服务速率限制；不要批量刷 |
| 自有 GeoServer 的管理 | geoserver-mcp（mahdin75，有验证） | 用最小权限账号；`delete_*`、`reset_geoserver` 类工具先在测试实例上试 |

### 6.2 暂缓 / 有条件采用

- **jjsantos01/qgis_mcp**：不要在新项目采用；代码已落后于 MCP SDK，修好之前不可用；star 数是历史遗留。
- **cesium-ai-integrations**：官方已声明弃用，按 README 迁移到 cesiumjs-ai-starter-app / cesiumjs-skills（**这两个迁移目标不在本次 26 个之内，未核查**）。
- **GeoClaw-Claude**：作者明确要求沙箱运行；无 LICENSE 文件，商用前先确认授权；2026-03-11 后无更新。
- **Axion-MCP / gee-mcp**：都要 GEE 凭证；Axion 仓库庞杂（大量测试报告 JSON 与多个 mcp-*.js 变体），先读 README 再决定用哪一个入口，不要盲目运行。
- **cesium-mcp（gaopengbin）**：功能最全的个人 Cesium MCP，但**用量统计默认开启**，采用前先按 README 关闭遥测；作者在 README 求职，属个人项目，持续性依赖个人维护。
- **mapbox-mcp-server**：官方、可信，但要 Mapbox token 与按量计费；先在免费额度内试。
- **scientific-agent-skills（K-Dense）**：57,064 stars 是合集热度；地理部分本地只见到 1 个 skill，引用前先确认你要的 skill 是否在其中。
- **server-google-maps**：已归档迁移，不要当作现成服务器采用；需要 Google Maps API key。

### 6.3 不要做的事

- **不要把“工具列表能列出”当成“算得对”**：9 个“通过”都只是 list_tools，没有一次真实调用核对结果；做空间分析、制图出图前，必须自己设计对照验证。
- **不要把 agent 直接连生产数据库 / 生产 GeoServer / 生产 QGIS 工程**：PostGIS MCP、GeoServer MCP、QGIS MCP 都有删、改、重置类工具；先用最小权限账号与测试实例。
- **不要在无 LICENSE 的 4 个仓库上做商用分发**（GeoClaw-Claude、pg-mcp、postgis-mcp、jjsantos01/qgis_mcp）；无许可证 = 未授权，不是“可以随便用”。
- **不要运行来路不明的安装脚本**：本次核查只读了 README 与关键代码、只跑了 `list_tools`；`install.sh`（GeoClaw）、`start-mcp-server.ps1`（Axion）等脚本未执行。
- **不要把博客下载量、合集 stars 当作项目采用证据**：如 QGIS MCP 插件 77,002 下载（博客称，未独立核实）、`modelcontextprotocol/servers` 91,976 stars（整个单体仓库）、K-Dense 57,064 stars（整个技能合集），都不能直接折算到单个地理项目上。

---

## 7. 主要问题与缺口

1. **验证深度不足**：9/26 的“通过”只是工具列表，没有一次真实工具调用；QGIS、GeoServer、PostGIS、Mapbox、GEE 五类最需要真实后端的项目，恰恰都没有端到端验证。后续工作应在有 QGIS / 测试用 GeoServer 的环境下补一次真实调用。
2. **一个项目已断代**：jjsantos01/qgis_mcp 在 mcp 1.x 与 2.x 下均无法启动，是 26 个里唯一确认“现在不能用”的；它的高 star 数具有误导性。
3. **许可证缺口**：4/26 无 LICENSE 文件声明；1 个（GeoClaw）README 自称 MIT 但无文件；1 个（server-google-maps）处于 MIT→Apache-2.0 过渡期。合规采用前需逐个确认。
4. **同名混淆严重**：geoserver-mcp ×2、qgis-mcp ×2、osm-mcp ×3、stac-mcp ×2、pg-mcp（文档站）vs pg-mcp-server（源码，已不在本次范围内）。引用时必须带作者 / 组织名，不能只写项目名。
5. **本地克隆滞后**：gdal-mcp、stac-mcp、open-streetmap-mcp-jagan 的本地 HEAD 落后于 GitHub 推送；geomaster 本地仅见 1 个 skill，与 README 宣称的 177 个不符。后续应 `git pull` 后复核。
6. **期刊证据稀薄**：2024–2026 年顶刊中明确采用 MCP/Skills 的地理论文仅检索到 1 篇（Agentic SWMM，2026，新刊），其余为 LLM 生成代码或自主 GIS 框架讨论。学术采纳远落后于 GitHub 上的工程热度。
7. **遥测与凭证风险**：cesium-mcp 默认开启用量统计；GeoServer / PostGIS / Mapbox / GEE 类项目都要把凭证交给 agent 运行环境；GeoClaw 与 jjsantos 的“任意代码执行”能力只应在沙箱中使用。

---

## 附录 A. 素材与复现说明

- 仓库目录：`skills-mcp/repos/`（26 个，约 393 MB）
- 验证日志：`skills-mcp/figures/verify-*.txt`（14 个文本日志，**不是图片**；接手时 12 个，本次复跑新增 1 个 qgis-nkarasiak 日志）
- 成功 11 个日志对应 9 个项目：`verify-gdal-mcp-tools.txt`（13）、`verify-geoserver-mcp-mahdin75-tools.txt`（56）、`verify-gis-mcp-mahdin75-tools.txt`（91）、`verify-locusync-tools.txt`（46）、`verify-osm-mcp-jagan-tools.txt`（12）、`verify-osm-mcp-ni-c-tools.txt`（11）、`verify-qgis-nkarasiak-tools.txt`（125）、`verify-qgis-nkarasiak-tools-rerun.txt`（125，与前者内容一致）、`verify-qgis-nkarasiak-tools-rerun-2026-11-14.txt`（125，本次复跑，工具名逐项一致）、`verify-stac-eo-mcp-tools.txt`（5）、`verify-stac-mcp-tools.txt`（11）
- 失败 3 个：`verify-qgis-jjsantos-tools.txt`、`verify-qgis-jjsantos-tools-rerun.txt`、`verify-qgis-jjsantos-tools-rerun2.txt`（均为 0 个工具）
- 注：任务交接时称 figures 下有 7 个日志，实际盘点为 12 个；另有 `verify-geoserver-mcp-mahdin75-tools.txt` 与 `verify-gis-mcp-mahdin75-tools.txt` 在交接清单中未列出
- 复跑脚本：`skills-mcp/tmp/mcp_list2.py`（通用 stdio list_tools 客户端）、`run_jjsantos.py`、`run_jagan.py`、`run_geoserver_mahdin.py`；虚拟环境 `tmp/venv_mcp`（mcp 2.x）、`tmp/venv_mcp1x`（mcp 1.x）
- GitHub 快照：`skills-mcp/tmp/gh_snapshot_2026-11-14.json`（2026-11-14 一次性 API 拉取，26 条；API 限额使用前余量 59/60）
- 期刊核查：2026-11-14 两次公开检索（MCP+GIS+顶刊；GeoAI+LLM agent+GIScience），未做系统性文献抽样（本域与期刊关联较弱，见 §5）

## 附录 B. 未查到事项清单

- 26 个项目中 16 个无真实用例 / 采用者证据（README 未给出来源可查的采用者，GitHub 亦无公开引用统计）；报告中凡“采用者”一栏未写的，即未查到，不作推测。
- Mapbox / Google Maps / GEE / GeoServer / PostGIS 类项目的真实调用成本、配额与速率限制：未验证（需要账号 / 实例，未注册）。
- cesium-mcp（gaopengbin）的 60+ 工具清单、osm-mcp（GRABOSM）的 30 个工具清单：仅为 README 宣称，未逐项核对。
- GeoLibre 的 `geolibre-mcp` 服务器实现细节：skill 文件提及，但本仓库内未核查到服务器代码位置。
- acupai/geoserver-mcp 与 mahdin75/geoserver-mcp 的分叉关系：未做逐文件 diff，未查到声明。
- K-Dense 合集本地仅见 1 个 skill 的原因：未查到。
