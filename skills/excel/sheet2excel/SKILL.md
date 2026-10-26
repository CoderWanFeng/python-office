---
name: sheet2excel
description: 将同一个 Excel 文件的多个 sheet 拆分为独立文件。当用户提到拆分 sheet、Excel 按表拆分、拆 sheet 时使用。
---

# sheet2excel Skill

> 将同一个 Excel 里的不同 sheet 拆分为不同的 Excel 文件

## 功能描述

将一个包含多个 sheet 的 Excel 文件，按 sheet 拆分为多个独立的 Excel 文件。

## 所属分类

`office/skills/excel/sheet2excel/`

## 调用方式

```python
from skills.excel import sheet2excel

sheet2excel(
    file_path='./multi_sheet.xlsx',
    output_path='./output/'
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `file_path` | str | 是 | - | 需要拆分的 Excel 文件路径 |
| `output_path` | str | 否 | `'./'` | 拆分后文件的输出目录 |

## 返回值

`None`

## 使用示例

```python
from skills.excel import sheet2excel
sheet2excel(file_path='./data.xlsx', output_path='./split_output/')
```

## 视频教程

https://www.bilibili.com/video/BV1714y147Ao/

## 原始函数

`office.api.excel.sheet2excel`
