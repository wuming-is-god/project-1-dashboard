# 部署指南：Render / Railway

## 1. 准备工作
- 确保 `app.py` 中包含：`server = app.server`
- 确保 `requirements.txt` 包含：`dash`, `plotly`, `pandas`, `gunicorn`, `waitress`
- 确保数据文件 `data/clean/gapminder_clean.csv` 已提交到 GitHub

## 2. Render 部署步骤
1. 登录 [Render](https://render.com/)
2. 点击 "New" -> "Web Service"
3. 连接你的 GitHub 仓库
4. 配置：
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:server`
   - **Python Version**: 3.11 (在 Environment 中添加 `PYTHON_VERSION=3.11`)
5. 点击 "Deploy Web Service"

## 3. Railway 部署步骤（备选）
1. 登录 [Railway](https://railway.app/)
2. 点击 "New Project" -> "Deploy from GitHub repo"
3. 添加 `Procfile`，内容：`web: gunicorn app:server`
4. 等待自动部署完成

## 4. 排错记录
- **502 Bad Gateway**：检查 Start Command 是否为 `gunicorn app:server`
- **ModuleNotFoundError**：检查 `requirements.txt` 是否拼写正确
- **FileNotFoundError**：检查数据路径是否使用了 `Path(__file__).parent / "data/clean/gapminder_clean.csv"`
- **应用运行但无数据**：检查 CSV 文件是否已提交到 Git，Render 构建时是否包含该文件

## 5. 部署信息
- 在线链接：[部署后填写]
- 部署日期：[部署后填写]
- 耗时：[部署后填写]