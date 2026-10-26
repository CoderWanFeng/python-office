---
name: txt2pdf
description: 将文本文件转换为 PDF 文件。当用户提到文本转 PDF、txt 转 PDF、TXT 生成 PDF 时使用。
---

# txt2pdf Skill

> 将文本文件转换为 PDF 文件

## 功能描述

将文本文件（.txt）转换为 PDF 格式。

## 所属分类

`office/skills/pdf/txt2pdf/`

## 调用方式

```python
from skills.pdf import txt2pdf

txt2pdf(
    input_file='./test.txt',
    output_file='./test.pdf'
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `input_file` | str | 否 | - | 文本文件路径 |
| `output_file` | str | 否 | `'txt2pdf.pdf'` | 输出 PDF 文件路径 |

## 返回值

`None`

## 使用示例

```python
from skills.pdf import txt2pdf
txt2pdf(input_file='./article.txt', output_file='./article.pdf')
```

## 视频教程

https://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/3-txt2pdf/

## 原始函数

`office.api.pdf.txt2pdf`
