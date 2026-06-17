---
name: split_excel_by_column
description: 按指定列的内容拆分 Excel 文件，每个唯一值一个文件。当用户提到按列拆分 Excel、按字段拆分表格时使用。
---

# split_excel_by_column Skill

> 按指定列的内容拆分 Excel 文件

## 功能描述

根据指定列的内容，将一个 Excel 文件拆分为多个 Excel 文件，每个唯一值对应一个新文件。

## 所属分类

`office/skills/excel/split_excel_by_column/`

## 调用方式

```python
from office.skills.excel import split_excel_by_column

split_excel_by_column(
    filepath='./data.xlsx',
    column=0,
    worksheet_name=None
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `filepath` | str | 是 | - | 需要拆分的 Excel 文件路径 |
| `column` | int | 是 | - | 按哪一列的内容进行拆分（列索引） |
| `worksheet_name` | str | 否 | `None` | 指定工作表名称。默认处理第一个工作表 |

## 返回值

`None`

## 使用示例

```python
from office.skills.excel import split_excel_by_column
# 按第 0 列拆分
split_excel_by_column(filepath='./orders.xlsx', column=0)
```

## 原始函数

`office.api.excel.split_excel_by_column`
