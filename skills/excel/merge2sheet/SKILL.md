---
name: merge2sheet
description: 将多个 Excel 文件的多个 sheet 合并到同一个 sheet。当用户提到合并 sheet、跨表合并、汇总多个表格时使用。
---

# merge2sheet Skill

> 自动合并多个 Excel 文件的多个 sheet

## 功能描述

将多个 Excel 文件中的所有 sheet 合并到同一个 Excel 文件的同一个 sheet 中。

## 所属分类

`office/skills/excel/merge2sheet/`

## 调用方式

```python
from skills.excel import merge2sheet

merge2sheet(
    dir_path='./excels',
    output_sheet_name='Sheet1',
    output_excel_name='merge2sheet'
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `dir_path` | str | 是 | - | 包含多个 Excel 文件的目录路径 |
| `output_sheet_name` | str | 否 | `'Sheet1'` | 合并后的 sheet 名称 |
| `output_excel_name` | str | 否 | `'merge2sheet'` | 合并后的 Excel 文件名 |

## 返回值

`None`

## 使用示例

```python
from skills.excel import merge2sheet
merge2sheet(dir_path='./my_excels', output_sheet_name='AllData', output_excel_name='all_merged')
```

## 原始函数

`office.api.excel.merge2sheet`
