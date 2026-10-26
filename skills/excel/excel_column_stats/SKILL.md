---
name: excel_column_stats
description: 统计 Excel 每一列的填充率、类型、唯一值数量和数值分布，用于数据质量初筛。当用户提到 Excel 列统计、数据质量、缺失率、列画像时使用。
---

# excel_column_stats Skill

> 给 Excel 每一列做一次「体检」：填充率、类型、唯一值、数值分布

## 功能描述

逐列统计非空数量、空值占比、去重后的取值个数，并推断列类型
（number / text / date / mixed / empty）。数值列额外给出最小值、最大值、
均值、中位数和样本标准差；文本列给出出现次数最多的前 N 个值。

适合在正式处理数据之前先看一眼：哪列缺失严重、哪列数字里混了文本、数值量级是否合理。

## 所属分类

`skills/excel/excel_column_stats/`

## 调用方式

```python
from skills.excel import excel_column_stats

excel_column_stats(excel_path='销售明细.xlsx', top_n=3)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `excel_path` | str | 是 | - | 需要统计的 Excel 路径 |
| `sheet_name` | str | 否 | `None` | 工作表名，默认取第一个 |
| `top_n` | int | 否 | `5` | 文本列返回前 N 个高频值，0 表示不返回 |

## 返回值

`dict`，包含 `sheet`、`row_count`、`column_count`、`fill_rate`、`columns`。
`columns` 是列表，每项含 `name`、`index`、`filled`、`empty`、`empty_ratio`、
`unique`、`type`，并按类型附带 `numeric`、`date_range` 或 `top`。

## 使用示例

```python
from skills.excel import excel_column_stats

stats = excel_column_stats('销售明细.xlsx')
print('整体填充率：{:.1%}'.format(stats['fill_rate']))
for column in stats['columns']:
    print('{}（{}）：空值 {} 个'.format(column['name'], column['type'], column['empty']))
    if column['type'] == 'number':
        print('  均值 {mean}，中位数 {median}'.format(**column['numeric']))
```

## 原始函数

`contributors/my12yyds/excel_column_stats.py`
