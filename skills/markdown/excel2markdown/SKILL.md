---
name: excel2markdown
description: 将 Excel 文件转换为 Markdown 格式的文档。当用户提到 Excel 转 Markdown、表格转 MD、Excel 文档化时使用。
---

# excel2markdown Skill

> 将 Excel 文件转换为 Markdown 格式的文件

## 功能描述

将 Excel 文件转换为 Markdown 格式的文件，支持选择转换指定工作表。

## 所属分类

`office/skills/markdown/excel2markdown/`

## 调用方式

```python
from skills.markdown import excel2markdown

excel2markdown(
    input_file='./data.xlsx',
    output_file='./output.md',
    sheet_name=None
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `input_file` | str | 是 | - | 输入 Excel 文件的路径 |
| `output_file` | str | 否 | `'./excel2markdown.md'` | 输出 Markdown 文件的路径 |
| `sheet_name` | str | 否 | `None` | 需要转换的 Excel 工作表名称。默认转换所有工作表 |

## 返回值

`None`

## 使用示例

```python
from skills.markdown import excel2markdown
excel2markdown(input_file='./report.xlsx', output_file='./report.md')
```

## 原始函数

`office.api.markdown.excel2markdown`
