# 任务清单

## M1 数据清洗
- [x] 读取 `gapminder.tsv` 并执行 `df.info()` 和 `df.describe()`
- [x] 重命名列：`lifeExp` -> `life_exp`, `gdpPercap` -> `gdp_percap`
- [x] 类型转换：`year` 转 int，`life_exp` 转 float
- [x] 派生新列：`gdp_total = gdp_percap * pop`
- [x] 检查并处理缺失值与重复值（记录到 DATA.md）
- [x] 输出 `data/clean/gapminder_clean.csv`
- [x] 更新 `DATA.md` 的“清洗前后对比”部分

## M2 可视化
- [x] 在 notebook 中画出折线图（各大洲预期寿命趋势）
- [x] 画出柱状图（某年 Top 10 国家）
- [x] 画出散点图（人均 GDP vs 预期寿命，气泡=人口）
- [x] 画出地图（某年全球预期寿命分布）
- [x] 保存 4 张图到 `assets/` 文件夹
- [x] 更新 `DASHBOARD.md` 中的图表清单

## M3 Dash 看板
- [x] 编写 `app.py`，搭建基础布局（`html.Div`, `dbc.Container`）
- [x] 添加筛选器组件（`dcc.Slider`, `dcc.Dropdown`, `dcc.RadioItems`）
- [x] 添加 KPI 卡片（`dbc.Card`）
- [x] 添加 4 个图表容器（`dcc.Graph`）
- [x] 编写回调函数 `@app.callback`，实现联动
- [x] 本地运行 `python app.py` 测试成功
- [x] 检查是否有重复读取 CSV 的性能问题（使用 `lru_cache`）

## M4 部署
- [x] 创建 `.gitignore` 文件
- [x] 编写 `requirements.txt`（含 dash, plotly, pandas, gunicorn, waitress）
- [x] 在 `app.py` 中添加 `server = app.server`
- [x] 本地 Windows 测试 `waitress-serve --port=8050 app:server`
- [x] 配置 Render 部署（Build Command, Start Command）
- [x] 部署成功，获取在线链接
- [x] 将在线链接和截图填入 `README.md`
- [x] 编写 `DEPLOY.md` 记录部署过程和排错

## M5 博客
- [x] 编写 `BLOG.md` 大纲
- [x] 撰写博客正文（问题 -> 数据 -> 清洗 -> 可视化 -> Dash -> 部署）
- [x] 发布博客到掘金/知乎/个人站
- [x] 将博客链接填入 `README.md`