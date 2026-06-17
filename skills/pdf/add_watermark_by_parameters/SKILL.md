---
name: add_watermark_by_parameters
description: 通过参数化方式给 PDF 添加水印。当用户提到参数化 PDF 水印、批量 PDF 水印时使用。
---

# add_watermark_by_parameters Skill

> 给 PDF 添加水印（带参数）

## 功能描述

通过参数化方式给 PDF 添加水印，与 `add_mark` 类似。

## 所属分类

`office/skills/pdf/add_watermark_by_parameters/`

## 调用方式

```python
from office.skills.pdf import add_watermark_by_parameters

add_watermark_by_parameters(
    input_file='./test.pdf',
    mark_str='python-office',
    output_path='./',
    output_file='watermarked.pdf'
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `input_file` | str | 否 | - | PDF 文件路径 |
| `mark_str` | str | 否 | - | 水印内容 |
| `output_path` | str | 否 | - | 输出路径 |
| `output_file` | str | 否 | - | 输出文件名 |
| `pdf_file` | str | 否 | - | **[已弃用]** 请使用 `input_file` |
| `output_file_name` | str | 否 | - | **[已弃用]** 请使用 `output_file` |

## 返回值

`None`

## 使用示例

```python
from office.skills.pdf import add_watermark_by_parameters
add_watermark_by_parameters(input_file='./report.pdf', mark_str='机密')
```

## 原始函数

`office.api.pdf.add_watermark_by_parameters`
