---
name: pdf2docx
description: 将 PDF 文件转换为 Word 文档（.docx），支持单文件和批量转换。当用户提到 PDF 转 Word、PDF 转 docx 时使用。
---

# pdf2docx Skill

> 将 PDF 转换为 Word 文档

## 功能描述

将一个或多个 PDF 文件转换为 Word（.docx）格式。

## 所属分类

`office/skills/pdf/pdf2docx/`

## 调用方式

```python
from office.skills.pdf import pdf2docx

# 单个文件
pdf2docx(input_file='./test.pdf', output_file='./test.docx')

# 批量转换（指定输入输出文件夹）
pdf2docx(input_path='./pdfs/', output_path='./docs/')
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `input_file` | str | 否* | - | PDF 文件路径 |
| `output_file` | str | 否 | - | 输出 Word 文件路径 |
| `input_path` | str | 否* | - | 输入文件夹路径（批量转换时使用） |
| `output_path` | str | 否 | - | 输出文件夹路径（批量转换时使用） |
| `file_path` | str | 否 | - | **[已弃用]** 请使用 `input_file` |

> 至少需要提供 `input_file`+`output_file` 或 `input_path`+`output_path` 之一

## 返回值

`None`

## 使用示例

```python
from office.skills.pdf import pdf2docx
pdf2docx(input_file='./report.pdf', output_file='./report.docx')
```

## 视频教程

https://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/1-pdf2docx/

## 原始函数

`office.api.pdf.pdf2docx`
