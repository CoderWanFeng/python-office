---
name: add_img_water
description: 给 PDF 添加图片水印（logo 等）。当用户提到 PDF 图片水印、PDF 加 logo 时使用。
---

# add_img_water Skill

> 给 PDF 文件添加图片水印

## 功能描述

向 PDF 文件添加图片作为水印。

## 所属分类

`office/skills/pdf/add_img_water/`

## 调用方式

```python
from skills.pdf import add_img_water

add_img_water(
    input_file='./test.pdf',
    mark_file='./watermark.png',
    output_file='./with_watermark.pdf'
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `input_file` | str | 否 | - | 输入 PDF 文件路径 |
| `mark_file` | str | 否 | - | 水印图片文件路径 |
| `output_file` | str | 否 | - | 输出 PDF 文件路径 |
| `pdf_file_in` | str | 否 | - | **[已弃用]** 请使用 `input_file` |
| `pdf_file_mark` | str | 否 | - | **[已弃用]** 请使用 `mark_file` |
| `pdf_file_out` | str | 否 | - | **[已弃用]** 请使用 `output_file` |

## 返回值

`None`

## 使用示例

```python
from skills.pdf import add_img_water
add_img_water(
    input_file='./report.pdf',
    mark_file='./logo.png',
    output_file='./with_watermark.pdf'
)
```

## 原始函数

`office.api.pdf.add_img_water`
