# 数据说明：Gapminder

## 来源
- 名称：Gapminder
- 文件：`data/raw/gapminder.tsv`
- 格式：TSV（Tab 分隔）
- 说明：该数据集记录了 1952-2007 年间全球 140+ 个国家的预期寿命、人口和人均 GDP。

## 字段字典
| 字段 | 类型 | 含义 | 取值示例 | 清洗/处理方式 |
|---|---|---|---|---|
| country | str | 国家名称 | "China" | 去除首尾空格 |
| continent | category | 大洲 | "Asia" | 转为 category 类型 |
| year | int | 年份 | 1952 | 转为 int32 |
| lifeExp | float | 预期寿命 | 43.8 | 重命名为 life_exp，保留两位小数 |
| pop | int | 人口 | 556263527 | 重命名为 pop，转为 int64 |
| gdpPercap | float | 人均 GDP | 400.0 | 重命名为 gdp_percap，保留两位小数 |

## 清洗规则
1. **列名规范化**：统一转小写，用下划线连接（如 `lifeExp` -> `life_exp`, `gdpPercap` -> `gdp_percap`）。
2. **类型转换**：`year` 转整数；`life_exp`、`gdp_percap` 转浮点数；`pop` 转整数。
3. **派生新列**：计算 `gdp_total = gdp_percap * pop`（国家总 GDP）。
4. **逻辑一致性检查**：
   - `life_exp` 和 `gdp_percap` 必须 > 0。
   - `year` 必须在 1952 到 2007 之间。
5. **缺失值与重复值**：该数据集非常干净，但仍需执行 `isnull().sum()` 和 `drop_duplicates()` 确认没有异常。
6. **保存**：输出为 `data/clean/gapminder_clean.csv`。

## 清洗前后对比
- 清洗前行数：[1704]
- 清洗后行数：[1704]
- 缺失值数量：[0]
- 重复值数量：[0]