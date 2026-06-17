---
name: excel2pdf
description: 将 Excel 文件的指定工作表转换为 PDF 格式。当用户提到 Excel 转 PDF、表格转 PDF、导出 Excel 为 PDF 时使用。
---

# excel2pdf Skill

> 将 Excel 文件的指定工作表转换为 PDF 格式

## 功能描述

将 Excel 文件的指定工作表转换为 PDF 文件。

## 所属分类

`office/skills/excel/excel2pdf/`

## 调用方式

```python
from office.skills.excel import excel2pdf

excel2pdf(
    excel_path='./data.xlsx',
    pdf_path='./data.pdf',
    sheet_id=0
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `excel_path` | str | 是 | - | Excel 文件的路径 |
| `pdf_path` | str | 是 | - | 转换后生成的 PDF 文件的路径 |
| `sheet_id` | int | 否 | `0` | 工作表的索引（默认第一个工作表） |

## 返回值

`None`

## 使用示例

```python
from office.skills.excel import excel2pdf
excel2pdf(excel_path='./report.xlsx', pdf_path='./report.pdf', sheet_id=0)
```

## 视频教程

https://www.bilibili.com/video/BV1A84y1N7or/

## 原始函数

`office.api.excel.excel2pdf`
