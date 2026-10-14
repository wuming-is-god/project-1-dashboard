# 看板设计：Gapminder Dashboard

## 1. 布局结构
1. **顶部**：标题 + 筛选器（年份滑块、大洲多选、指标切换）
2. **第一行**：3 个 KPI 卡片（平均预期寿命、总人口、国家数量）
3. **第二行**：趋势折线图（大洲平均预期寿命随时间变化）
4. **第三行**：排名柱状图（某年 Top 10 国家）+ 散点图（人均GDP vs 预期寿命）
5. **第四行**：Choropleth 世界地图（某年全球预期寿命分布）

## 2. 图表与组件清单
| 区域 | 图表类型 | 回答的问题 | 涉及字段 | 交互/回调输入 |
|---|---|---|---|---|
| KPI | 卡片 x3 | 当前筛选下的整体情况如何？ | life_exp, pop, country | 年份 + 大洲 |
| 趋势 | 折线图 | 各大洲预期寿命如何随时间变化？ | year, life_exp, continent | 大洲多选 |
| 排名 | 水平条形图 | 某一年预期寿命最高的 10 个国家？ | country, life_exp | 年份滑块 |
| 关系 | 散点图 | 人均 GDP 与预期寿命的关系？ | gdp_percap, life_exp, pop | 颜色=大洲，大小=人口 |
| 地图 | Choropleth | 某一年全球预期寿命的地理分布？ | country, life_exp | 年份滑块 |

## 3. 交互逻辑（Dash 回调设计）
- **Input**：
  - `year-slider` (dcc.Slider): 范围 1952-2007，步长 5
  - `continent-dropdown` (dcc.Dropdown): 多选，默认全选
  - `metric-radio` (dcc.RadioItems): 选择 life_exp / gdp_percap / pop
- **Output**：
  - KPI 卡片数值
  - 折线图、柱状图、散点图、地图
- **逻辑**：
  - 所有图表都受 `year-slider` 和 `continent-dropdown` 约束。
  - 散点图和折线图的 Y 轴受 `metric-radio` 控制。
  - 使用 `prevent_initial_call=True` 避免初次加载时的循环。

## 4. 视觉规范
- 使用 Plotly 的 `plotly_white` 或 `simple_white` 模板。
- 颜色映射：大洲使用 `px.colors.qualitative.Set2`。
- 地图：使用 `px.choropleth`，`locationmode='country names'`。