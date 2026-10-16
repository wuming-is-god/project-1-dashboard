# 项目计划：Gapminder 全球发展 Dash 看板

## 1. 一句话
用 Gapminder 全球发展数据集做一个可交互 Dash 看板，展示各国预期寿命、人均GDP和人口在 1952-2007 年间的趋势与对比。

## 2. 目标
- 练习 Pandas 清洗（类型转换、缺失值处理、派生新列）
- 用 Plotly 做 4 类图：折线图、柱状图、散点图、地图
- 用 Dash 实现筛选和回调（年份滑块、大洲多选、指标切换）
- 部署到 Render/Railway
- 发布 1 篇博客

## 3. 非目标
- 不做实时抓取
- 不做用户登录
- 不做机器学习预测
- 不涉及中国以外的非国家实体（如需地图，使用国家代码或名称匹配）

## 4. 成功标准
- [x] GitHub 有完整代码和 README
- [x] 在线链接可访问
- [x] 数据清洗可复现（notebook + DATA.md）
- [x] 看板至少 5 个图表/组件，且与数据匹配
- [x] 博客发布并链接到 README

## 5. 数据
**来源**：书籍《Pandas》附带数据集 `project-1-dashboard/data/gapminder.tsv`
**类型**：面板数据（时间序列 + 截面数据结合，包含多个国家在多个年份的数据）
**字段**：
country, continent, year, lifeExp, pop, gdpPercap
**清洗规则**：
1. **列名规范化**：去除空格，统一转小写，用下划线连接（如 `lifeExp` -> `life_exp`）。
2. **类型转换**：
   - `year` 转为整数年份。
   - `life_exp`、`gdp_percap`、`pop` 转为浮点数。
3. **缺失值处理**：检查是否有缺失值（通常该数据集很干净），若有则删除或填充。
4. **重复值处理**：使用 `drop_duplicates()` 删除完全重复的行。
5. **派生新列**：
   - 计算 `gdp_total = gdp_percap * pop`（国家总 GDP）。
   - 可以通过 `pd.cut` 给 `gdp_percap` 划分收入等级（如低收入、中等收入、高收入）。
6. **保存清洗后数据**：输出为 `gapminder_clean.csv`，便于后续分析。

## 6. 看板设计
**布局**：顶部筛选器 → KPI 卡片 → 趋势图 → 排名图 → 地图/散点

**交互设计**：
- **年份滑块**（Slider）：选择 1952 到 2007 之间的年份（用于地图和排名图）。
- **大洲多选**（Dropdown/Multi-select）：选择亚洲、欧洲等（影响所有图表）。
- **指标切换**（RadioItems）：在预期寿命、人均GDP、人口之间切换。
- **国家多选/下拉**（可选）：对比特定国家的趋势。

**图表清单**：
| 区域 | 图表 | 回答的问题 | 字段 | 交互 |
|---|---|---|---|---|
| KPI | 卡片 x3 | 当前筛选下的平均寿命、总人口、国家数量 | life_exp, pop, country | 受年份和大洲影响 |
| 趋势 | 折线图 | 各大洲平均预期寿命如何随时间变化？ | year, life_exp, continent | 大洲多选 |
| 排名 | 水平条形图 | 某一年预期寿命最高的 10 个国家？ | country, life_exp | 年份滑块 |
| 关系 | 散点图 | 人均GDP与预期寿命的关系？ | gdp_percap, life_exp, pop | 颜色=大洲，大小=人口 |
| 地图 | Choropleth 地图 | 某一年全球预期寿命的分布？ | country, life_exp | 年份滑块 |

## 7. 里程碑（带完成定义）
### M1 数据清洗
- [x] `data/raw/gapminder.tsv` 存在，正确读取
- [x] `notebooks/01_clean.ipynb` 可从头跑到尾无报错
- [x] 输出 `data/clean/gapminder_clean.csv`
- [x] `DATA.md` 字段字典、清洗规则、缺失处理决策全部填写
- [x] 清洗前后对比：行数、列数、缺失值数量

### M2 可视化
- [x] 至少 4 类图：折线图、柱状图、散点图、地图
- [x] 每张图保存 PNG 到 `assets/`
- [x] `DASHBOARD.md` 图表清单填写完整
- [x] 每张图能一句话说明“回答什么问题”

### M3 Dash 看板
- [x] `app.py` 本地 `python app.py` 可运行
- [x] 至少 3 个筛选器（年份、大洲、指标） + 5 个图表/组件
- [x] 回调联动正常，无循环报错
- [x] 启动时读一次 CSV，不重复读

### M4 部署
- [x] `requirements.txt` 包含 dash/plotly/pandas/gunicorn
- [x] `app.py` 有 `server = app.server`
- [x] 本地 `gunicorn app:server` 测试通过
- [x] Render/Railway 在线链接可访问
- [x] 链接填进 `README.md`
- [x] `DEPLOY.md` 记录部署命令和排错

### M5 博客
- [x] `BLOG.md` 大纲完成
- [x] 博客发布（掘金/知乎/个人站）
- [x] 博客链接填进 `README.md`

## 8. 风险
| 风险 | 概率 | 影响 | 应对 |
|---|---|---|---|
| 地图国家名称不匹配 | 中 | 高 | 使用 `plotly.express.choropleth` 并指定 `locations` 和 `locationmode='country names'`，测试异常值 |
| 数据太大 | 低 | 中 | 该数据集仅约 1700 行，无需采样 |
| 部署失败 | 中 | 高 | 本地 gunicorn 先测 |
| 缺失值填充造成偏差 | 低 | 中 | 该数据集非常干净，但仍需记录决策 |
| 回调循环/性能差 | 中 | 中 | 启动读一次数据，用 lru_cache |
| 部署后路径找不到文件 | 中 | 高 | 用 `Path(__file__).parent` |
| 博客写成流水账 | 中 | 低 | 按“问题→数据→清洗→图→Dash→部署”写 |