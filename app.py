import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Output, Input, no_update
import dash_bootstrap_components as dbc
from pathlib import Path
from functools import lru_cache

# ============================================================
# 1. 数据加载与准备（使用 lru_cache 避免重复读取）
# ============================================================
@lru_cache(maxsize=None)
def load_data():
    # 使用 Path(__file__) 确保在任何环境下都能找到数据
    data_path = Path(__file__).parent / 'data' / 'clean' / 'gapminder_clean.csv'
    df = pd.read_csv(data_path)
    return df

df = load_data()
years = sorted(df['year'].unique().tolist())
continents = sorted(df['continent'].unique().tolist())

# ============================================================
# 2. 初始化 Dash 应用
# ============================================================
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Gapminder 全球发展看板"
server = app.server  # 为 M4 部署做准备（Render/Railway 需要）

# ============================================================
# 3. 布局结构（对照 DASHBOARD.md 第 1 节）
# ============================================================
app.layout = dbc.Container([
    # --- 顶部：标题 + 筛选器 ---
    dbc.Row([
        dbc.Col(html.H1("Gapminder 全球发展看板", className="text-center mt-4 mb-4"), width=12)
    ]),
    
    dbc.Row([
        # 年份滑块
        dbc.Col([
            html.Label("选择年份", className="fw-bold"),
            dcc.Slider(
                id='year-slider',
                min=1952, max=2007, step=5, value=2007,
                marks={str(y): str(y) for y in range(1952, 2008, 5)},
                tooltip={"placement": "bottom", "always_visible": True}
            )
        ], width=6),
        
        # 大洲多选
        dbc.Col([
            html.Label("选择大洲", className="fw-bold"),
            dcc.Dropdown(
                id='continent-dropdown',
                options=[{'label': c, 'value': c} for c in continents],
                value=continents,  # 默认全选
                multi=True,
                clearable=False
            )
        ], width=3),
        
        # 指标切换
        dbc.Col([
            html.Label("指标切换", className="fw-bold"),
            dcc.RadioItems(
                id='metric-radio',
                options=[
                    {'label': '预期寿命', 'value': 'life_exp'},
                    {'label': '人均 GDP', 'value': 'gdp_percap'},
                    {'label': '人口', 'value': 'pop'}
                ],
                value='life_exp',
                inline=True
            )
        ], width=3)
    ], className="mb-4"),

    # --- 第一行：3 个 KPI 卡片 ---
    dbc.Row([
        dbc.Col(dbc.Card([dbc.CardBody([html.H6("平均预期寿命", className="card-title text-muted"), html.H4(id="kpi-life", className="card-text")])]), width=4),
        dbc.Col(dbc.Card([dbc.CardBody([html.H6("总人口", className="card-title text-muted"), html.H4(id="kpi-pop", className="card-text")])]), width=4),
        dbc.Col(dbc.Card([dbc.CardBody([html.H6("国家数量", className="card-title text-muted"), html.H4(id="kpi-count", className="card-text")])]), width=4),
    ], className="mb-4"),

    # --- 第二行：趋势折线图 ---
    dbc.Row([
        dbc.Col(dcc.Graph(id='trend-line-chart'), width=12)
    ], className="mb-4"),

    # --- 第三行：排名柱状图 + 散点图 ---
    dbc.Row([
        dbc.Col(dcc.Graph(id='top10-bar-chart'), width=6),
        dbc.Col(dcc.Graph(id='scatter-plot'), width=6)
    ], className="mb-4"),

    # --- 第四行：Choropleth 地图 ---
    dbc.Row([
        dbc.Col(dcc.Graph(id='world-map'), width=12)
    ], className="mb-5")

], fluid=True)

# ============================================================
# 4. 回调逻辑（对照 DASHBOARD.md 第 3 节）
# ============================================================
@app.callback(
    [
        Output('kpi-life', 'children'),
        Output('kpi-pop', 'children'),
        Output('kpi-count', 'children'),
        Output('trend-line-chart', 'figure'),
        Output('top10-bar-chart', 'figure'),
        Output('scatter-plot', 'figure'),
        Output('world-map', 'figure')
    ],
    [
        Input('year-slider', 'value'),
        Input('continent-dropdown', 'value'),
        Input('metric-radio', 'value')
    ],
    prevent_initial_call=True
)
def update_dashboard(selected_year, selected_continents, selected_metric):
    # 过滤数据
    if not selected_continents:
        return no_update, no_update, no_update, no_update, no_update, no_update, no_update
    
    df_filtered = df[df['continent'].isin(selected_continents)]
    df_year = df_filtered[df_filtered['year'] == selected_year]
    
    # 1. 更新 KPI 卡片
    avg_life = f"{df_year['life_exp'].mean():.1f} 岁"
    total_pop = f"{df_year['pop'].sum() / 1e9:.2f} B"  # 十亿单位
    country_count = f"{df_year['country'].nunique()} 个"
    
    # 2. 更新趋势折线图（注意：趋势图不需要 year 过滤，展示全时段）
    df_trend = df_filtered.groupby(['year', 'continent'], as_index=False)['life_exp'].mean()
    fig_line = px.line(
        df_trend, x='year', y='life_exp', color='continent',
        title='各大洲平均预期寿命趋势 (1952-2007)',
        labels={'life_exp': '预期寿命', 'year': '年份', 'continent': '大洲'},
        template='plotly_white'
    )
    
    # 3. 更新排名柱状图（使用选中的指标进行排名）
    df_top10 = df_year.nlargest(10, selected_metric)
    fig_bar = px.bar(
        df_top10, x=selected_metric, y='country', orientation='h',
        title=f'{selected_year}年 {selected_metric} Top 10 国家',
        labels={selected_metric: selected_metric, 'country': '国家'},
        color=selected_metric, color_continuous_scale='Blues',
        template='plotly_white'
    )
    fig_bar.update_layout(yaxis={'categoryorder': 'total ascending'})
    
    # 4. 更新散点图
    fig_scatter = px.scatter(
        df_year, x='gdp_percap', y='life_exp', size='pop', color='continent',
        hover_name='country', log_x=True,
        title=f'{selected_year}年人均GDP vs 预期寿命（气泡=人口）',
        labels={'gdp_percap': '人均GDP（对数轴）', 'life_exp': '预期寿命', 'continent': '大洲'},
        template='plotly_white'
    )
    
    # 5. 更新地图
    fig_map = px.choropleth(
        df_year, locations='country', locationmode='country names',
        color='life_exp', hover_name='country',
        color_continuous_scale='Viridis',
        title=f'{selected_year}年全球预期寿命分布地图',
        labels={'life_exp': '预期寿命'},
        template='plotly_white'
    )
    
    return avg_life, total_pop, country_count, fig_line, fig_bar, fig_scatter, fig_map


# ============================================================
# 5. 运行应用
# ============================================================
if __name__ == '__main__':
    app.run(debug=True)