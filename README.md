# Gapminder 全球发展 Dash 看板

![Dashboard 截图](assets/screenshot.png)

一个基于 Pandas + Plotly + Dash 构建的可交互数据看板，用于探索 1952-2007 年间全球各国的预期寿命、人均 GDP 和人口变化。

## 🔗 在线体验
- **在线看板**：[https://project-1-dashboard-2026.onrender.com]
- **博客文章**：[https://blog.example.com/2026/10/16/pandas-dash-gapminder-dashboard/]

## ✨ 功能特性
- 年份滑块：动态切换 1952-2007 年数据
- 大洲筛选：多选亚洲、欧洲、非洲等
- 指标切换：在预期寿命、人均 GDP、人口间切换
- 4 类图表：趋势折线图、排名柱状图、关系散点图、世界地图
- KPI 卡片：实时显示筛选后的平均值

## 🛠️ 技术栈
- Python 3.10.10
- Pandas（数据清洗）
- Plotly / Plotly Express（可视化）
- Dash / Dash Bootstrap Components（看板交互）
- Gunicorn + Render（部署）

## 🚀 本地运行
```bash
git clone https://github.com/wuming-is-god/project-1-dashboard.git
cd project-1-dashboard
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py