---
name: add_mark
description: 给 PDF 添加文字水印（简化接口）。当用户提到 PDF 加文字、PDF 标记时使用。
---

# add_mark Skill

> 给 PDF 添加水印

## 功能描述

向 PDF 文件添加文字水印。

## 所属分类

`office/skills/pdf/add_mark/`

## 调用方式

```python
from skills.pdf import add_mark

add_mark(
    input_file='./test.pdf',
    mark_str='python-office',
    output_path='./',
    output_file='watermarked.pdf'
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `input_file` | str | 否 | - | PDF 文件的位置，例如 `d:/code/programmer.pdf` |
| `mark_str` | str | 否 | - | 需要添加的水印内容，例如 `"python-office"` |
| `output_path` | str | 否 | - | 保存文件的位置 |
| `output_file` | str | 否 | - | 指定添加了水印的文件名称 |
| `pdf_file` | str | 否 | - | **[已弃用]** 请使用 `input_file` |
| `output_file_name` | str | 否 | - | **[已弃用]** 请使用 `output_file` |

## 返回值

`None`

## 使用示例

```python
from skills.pdf import add_mark
add_mark(input_file='./report.pdf', mark_str='机密')
```

## 原始函数

`office.api.pdf.add_mark`
