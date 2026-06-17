---
name: add_text_watermark
description: 给 PDF 添加文字水印，支持自定义字体、字号、颜色、位置。当用户提到 PDF 文字水印、PDF 加水印 时使用。
---

# add_text_watermark Skill

> 在 PDF 文档中添加文本水印

## 功能描述

向 PDF 文档添加文本水印，可自定义位置、字体、字号、颜色等参数。

## 所属分类

`office/skills/pdf/add_text_watermark/`

## 调用方式

```python
from office.skills.pdf import add_text_watermark

add_text_watermark(
    input_file='./test.pdf',
    point=(100, 200),
    text='python-office',
    output_file='./with_watermark.pdf',
    fontname='Helvetica',
    fontsize=12,
    color=(1, 0, 0)
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `input_file` | str | 否 | - | PDF 文件路径 |
| `point` | tuple | 否 | - | 水印位置坐标 |
| `text` | str | 否 | `'python-office'` | 水印文本内容 |
| `output_file` | str | 否 | `'./pdf_watermark.pdf'` | 输出 PDF 文件路径 |
| `fontname` | str | 否 | `'Helvetica'` | 字体名称 |
| `fontsize` | int | 否 | `12` | 字体大小 |
| `color` | tuple | 否 | `(1, 0, 0)` | 字体颜色（RGB） |

## 返回值

`None`

## 使用示例

```python
from office.skills.pdf import add_text_watermark
add_text_watermark(input_file='./report.pdf', text='机密文件')
```

## 视频教程

https://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/7-add_watermark

## 原始函数

`office.api.pdf.add_text_watermark`
