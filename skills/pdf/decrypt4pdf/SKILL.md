---
name: decrypt4pdf
description: 对加密的 PDF 文件进行解密。当用户提到 PDF 解密、解除 PDF 密码、解 PDF 时使用。
---

# decrypt4pdf Skill

> 解密 PDF 文件

## 功能描述

对加密的 PDF 文件进行解密处理。

## 所属分类

`office/skills/pdf/decrypt4pdf/`

## 调用方式

```python
from office.skills.pdf import decrypt4pdf

decrypt4pdf(
    password='123456',
    input_file='./encrypted.pdf',
    output_file='./decrypted.pdf'
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `password` | str | 是 | - | 解密密码 |
| `input_file` | str | 否 | - | 输入 PDF 文件名（包含路径） |
| `output_file` | str | 否 | - | 输出的解密 PDF 文件名（包含路径） |
| `input_path` | str | 否 | - | 输入文件的完整路径 |
| `output_path` | str | 否 | - | 输出文件的完整路径 |

## 返回值

`None`

## 使用示例

```python
from office.skills.pdf import decrypt4pdf
decrypt4pdf(password='mypassword', input_file='./encrypted.pdf', output_file='./decrypted.pdf')
```

## 视频教程

https://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/6-decrypt4pdf

## 原始函数

`office.api.pdf.decrypt4pdf`
