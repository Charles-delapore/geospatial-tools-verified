# Geospatial Tools Verified / 地学开源工具核验

独立核验的地学 Python 开源工具清单：仓库是否真实存在、是否还在维护、许可证是什么，以及重点工具的实际用例与社区评价。不做“照单全收”的搬运，只记录查到的事实。

## 来源

- 微信公众号“地学万事屋”2026-10-01《总结了100个地学Python工具/模型/代码，直接喂给AI，爽完了！》（标题称 100 个，正文实际列出 133 条，含重复条目）
- 扩展调研：复杂网络与优化、景观生态、地理人文福祉、复杂空间分析与相关性建模、地理信息可视化、skills 与 MCP

## 核验方法

- 逐个抓取 GitHub 仓库页面解析星标、许可证、归档状态与描述，再抓 commits Atom feed 取默认分支最近提交日期；异常值用 GitHub REST API 单独复核。
- 22 个核心工具另做实际用例与社区评价调研；原文未给链接的 11 个工具全网追查。
- 星标与提交时间为 **2026-11-14 快照**，不是实时值；GitHub 随时会变，长期引用请以仓库页面为准。
- 本仓库只核验“仓库是否存在、是否维护、许可证是什么”以及重点工具的用例口碑，未对每个工具做安装实测；安装兼容性需使用前自行验证。

## 主要结论

- 122 个有链接的仓库**全部有效，无一 404**；11 个无链接工具追查到 9 个，未找到 2 个（PyStream、PyRecharge）。
- **已归档 6 个，超过 2 年无提交 46 个（占 38%），超过 5 年无提交 23 个**；仍在活跃维护的 74 个，占 61%。
- 底座工具（GeoPandas、Shapely、Rasterio、ObsPy、MetPy、FloPy、PySAL）全部健康；水文、气象、气候各节里小众停更项目很多，照单全收会踩坑。

## 目录结构

- `docs/`：核验报告与各域调研报告
- `data/`：核验数据表（TSV）

## 内容

| 文件 | 说明 | 状态 |
|---|---|---|
| `docs/地学Python开源工具核验报告-20261114.md` | 微信文章 133 个工具的完整核验报告 | 已入库 |
| `data/repos.tsv` | 133 条清单（序号、分类、名称、仓库） | 已入库 |
| `data/repo_status.tsv` | 122 个有链接仓库的状态表 | 已入库 |
| `data/use_cases.md` | 22 个核心工具的实际用例与社区评价 | 已入库 |
| `data/nolink_findings.md` | 11 个无链接工具的追查结论 | 已入库 |
| `docs/complex-networks-REPORT.md` | 复杂网络与优化调研 | 待入库 |
| `docs/landscape-ecology-REPORT.md` | 景观生态调研 | 待入库 |
| `docs/wellbeing-REPORT.md` | 地理人文福祉调研 | 待入库 |
| `docs/spatial-analysis-REPORT.md` | 复杂空间分析与相关性建模调研 | 待入库 |
| `docs/geovis-REPORT.md` | 地理信息可视化调研 | 待入库 |
| `docs/skills-mcp-REPORT.md` | skills 与 MCP 调研 | 待入库 |
| `docs/revival-assessment.md` | 停更库复活评估（分叉重发 vs 交 PR） | 待入库 |
| `docs/README-index.md` | 五域总索引 | 待入库 |

## 联系

（待作者补充）
