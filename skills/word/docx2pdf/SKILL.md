---
name: docx2pdf
description: 将 Word 文档（.docx）转换为 PDF，支持单文件和整个文件夹批量转换。当用户提到 Word 转 PDF、docx 转 PDF 时使用。
---

# docx2pdf Skill

> 将 Word 转换为 PDF

## 功能描述

将 Word 文档（.docx）转换为 PDF 格式，支持单个文件或整个文件夹批量转换。

## 所属分类

`office/skills/word/docx2pdf/`

## 调用方式

```python
from skills.word import docx2pdf

# 单个文件
docx2pdf(path='./test.docx', output_path='./output/')

# 批量转换（path 传入文件夹）
docx2pdf(path='./word_files/', output_path='./pdfs/')
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `path` | str | 是 | - | Word 文件位置。支持批量处理：填写文件夹位置 |
| `output_path` | str | 否 | `None` | 转换后的输出位置。如果不存在会自动创建 |

## 返回值

`None`

## 使用示例

```python
from skills.word import docx2pdf
docx2pdf(path='./report.docx', output_path='./output/')
```

## 原始函数

`office.api.word.docx2pdf`
