---
name: excel2json
description: 把 Excel 工作表转换成 JSON，支持 records、columns、values 三种结构，日期自动转 ISO 字符串。当用户提到 Excel 转 JSON、表格转接口数据、Excel 生成 mock 数据时使用。
---

# excel2json Skill

> 把 Excel 转成程序能直接消费的 JSON

## 功能描述

把工作表转换成 JSON 兼容的 Python 对象，可直接写入文件或当接口数据使用。
三种结构：`records`（每行一个对象）、`columns`（每列一个数组）、`values`（纯二维数组）。
空单元格转 `null`，日期时间转 ISO 字符串，重复的列名自动加 `_2`、`_3` 后缀避免覆盖。

## 所属分类

`skills/excel/excel2json/`

## 调用方式

```python
from skills.excel import excel2json

data = excel2json('商品表.xlsx', orient='records', output_path='goods.json')
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `excel_path` | str | 是 | - | Excel 文件路径 |
| `sheet_name` | str | 否 | `None` | 工作表名，默认取第一个 |
| `orient` | str | 否 | `'records'` | `records`、`columns` 或 `values` |
| `output_path` | str | 否 | `None` | JSON 输出路径，指定后同时写文件 |
| `indent` | int | 否 | `2` | 写文件时的缩进，`None` 表示压缩 |
| `ensure_ascii` | bool | 否 | `False` | 是否把中文转成 `\uXXXX` |

## 返回值

`list | dict`：`records` 和 `values` 返回列表，`columns` 返回字典。

## 使用示例

```python
from skills.excel import excel2json

rows = excel2json('商品表.xlsx')
print(rows[0])            # {'商品名': '苹果', '价格': 5.5}

by_column = excel2json('商品表.xlsx', orient='columns')
print(by_column['价格'])   # [5.5, 3.0, ...]

excel2json('商品表.xlsx', output_path='goods.json', ensure_ascii=False)
```

## 原始函数

`contributors/my12yyds/excel2json.py`
