---
name: pdf2imgs
description: 将 PDF 文件转换为图片，可合并为一张长图或多张图。当用户提到 PDF 转图片、PDF 截图、PDF 转长图 时使用。
---

# pdf2imgs Skill

> 将 PDF 转换为图片

## 功能描述

将 PDF 文件转换为图片，支持合并为一张大图或多张图片。

## 所属分类

`office/skills/pdf/pdf2imgs/`

## 调用方式

```python
from skills.pdf import pdf2imgs

pdf2imgs(
    input_file='./test.pdf',
    output_file='./images/',
    merge=False
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `input_file` | str | 否 | - | PDF 文件路径 |
| `output_file` | str | 否 | - | 输出图片路径 |
| `merge` | bool | 否 | `False` | 是否合并为一张图片 |
| `pdf_path` | str | 否 | - | **[已弃用]** 请使用 `input_file` |
| `out_dir` | str | 否 | - | **[已弃用]** 请使用 `output_file` |

## 返回值

`None`

## 使用示例

```python
from skills.pdf import pdf2imgs
pdf2imgs(input_file='./report.pdf', output_file='./images/', merge=True)
```

## 视频教程

https://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/2-pdf2imgs/

## 原始函数

`office.api.pdf.pdf2imgs`
