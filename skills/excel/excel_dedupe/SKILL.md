---
name: excel_dedupe
description: 按指定列或整行给 Excel 去重，返回重复行与保留行的对应关系，可导出干净数据。当用户提到 Excel 去重、删除重复项、重复数据、查重时使用。
---

# excel_dedupe Skill

> 按指定列给 Excel 去重，并说明哪一行和哪一行重复

## 功能描述

按一个列、多个列或整行判断重复，保留第一次（或最后一次）出现的记录，
同时返回重复明细：重复的是第几行、和保留的第几行重复、去重键是什么。
只给「去重后剩多少行」往往不够排查问题，所以重复明细是重点。

## 所属分类

`skills/excel/excel_dedupe/`

## 调用方式

```python
from skills.excel import excel_dedupe

excel_dedupe(
    excel_path='客户名单.xlsx',
    key_columns=['手机号'],
    output_path='去重后.xlsx',
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `excel_path` | str | 是 | - | 需要去重的 Excel 路径 |
| `key_columns` | str \| list | 否 | `None` | 去重列，单个列名或列名列表；默认整行 |
| `sheet_name` | str | 否 | `None` | 工作表名，默认取第一个 |
| `keep` | str | 否 | `'first'` | 重复时保留 `'first'` 或 `'last'` |
| `case_sensitive` | bool | 否 | `True` | 文本是否区分大小写 |
| `output_path` | str | 否 | `None` | 去重结果输出路径 |

## 返回值

`dict`，包含 `sheet`、`key_columns`、`total`、`unique`、`duplicate_count`、
`duplicates`、`output_path`。`duplicates` 每项含 `row`、`kept_row`、`key`。

## 使用示例

```python
from skills.excel import excel_dedupe

result = excel_dedupe('客户名单.xlsx', key_columns='手机号')
print('共 {} 行，去重后 {} 行'.format(result['total'], result['unique']))
for item in result['duplicates']:
    print('第 {} 行与第 {} 行重复：{}'.format(item['row'], item['kept_row'], item['key']))
```

## 原始函数

`contributors/my12yyds/excel_dedupe.py`
