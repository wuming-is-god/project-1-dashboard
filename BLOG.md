# 博客：用 Pandas + Dash 做一个 Gapminder 全球发展看板

## 目标读者
想入门数据分析、可视化、Dash 交互开发或部署的初学者。

## 文章大纲

### 1. 为什么选 Gapminder 数据集？
- 数据背景：1952-2007 年，140+ 个国家的预期寿命、人口、人均 GDP
- 为什么适合做第一个项目：维度全、数据干净、天然适合做趋势图/地图/散点图
- 项目目标：做一个可交互看板，展示全球发展差异

### 2. 数据清洗：Pandas 实战
- 读取 TSV 的坑（`sep='\t'`）
- 列名重命名：`lifeExp` -> `life_exp`, `gdpPercap` -> `gdp_percap`
- 类型转换：`year` 转 int，`life_exp` 转 float
- 派生新列：`gdp_total = gdp_percap * pop`
- 缺失值与重复值检查（结果：0 缺失，0 重复）
- 代码片段（从 `01_clean.ipynb` 复制）

### 3. 可视化：用 Plotly 画出 4 类图
- 折线图：各大洲预期寿命趋势
- 柱状图：Top 10 国家排名
- 散点图：GDP vs 寿命，气泡=人口
- 地图：全球预期寿命分布
- 每张图的代码和截图

### 4. Dash 看板：从静态图到交互应用
- 布局搭建：顶部筛选器 → KPI 卡片 → 4 个图表
- 筛选器：年份滑块、大洲多选、指标切换
- 回调函数：`@app.callback` 实现联动
- 踩坑记录：`prevent_initial_call=True` 避免回调循环；`lru_cache` 避免重复读 CSV

### 5. 部署：绕过 GitHub 网络限制与 Render 绑卡
- 为什么选 Hugging Face Spaces：免费、无需绑卡、国内可访问
- 关键配置：`Dockerfile` + `server = app.server` + `README.md` 元数据
- 部署步骤简述
- 在线链接：[填写你的 HF 链接]

### 6. 总结与展望
- 我学到了什么：Pandas 清洗、Plotly 可视化、Dash 回调、Docker 部署
- 如果重做会改进什么：加上更多指标、尝试更复杂的图表（如 K 线图）
- 在线链接和 GitHub 仓库

## 发布计划
- 平台：掘金 / 知乎 / 个人博客
- 发布日期：[2026/10/16]
- 链接：[https://blog.example.com/2026/10/16/pandas-dash-gapminder-dashboard/]