---
name: encrypt4pdf
description: 对 PDF 文件设置密码进行加密保护。当用户提到 PDF 加密、PDF 密码、PDF 保护、加 PDF 密码时使用。
---

# encrypt4pdf Skill

> 加密 PDF 文件

## 功能描述

对 PDF 文件进行加密处理，设置用户密码保护 PDF 文件。

## 所属分类

`office/skills/pdf/encrypt4pdf/`

## 调用方式

```python
from office.skills.pdf import encrypt4pdf

encrypt4pdf(
    password='123456',
    input_file='./test.pdf',
    output_file='./encrypted.pdf'
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `password` | str | 是 | - | 加密密码 |
| `input_file` | str | 否 | - | 输入 PDF 文件名（包含路径） |
| `output_file` | str | 否 | - | 输出的加密 PDF 文件名（包含路径） |
| `input_path` | str | 否 | - | 输入文件的完整路径（另一种传入方式） |
| `output_path` | str | 否 | - | 输出文件的完整路径（另一种传入方式） |

## 返回值

`None`

## 使用示例

```python
from office.skills.pdf import encrypt4pdf
encrypt4pdf(password='mypassword', input_file='./report.pdf', output_file='./encrypted.pdf')
```

## 视频教程

https://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/5-encrypt4pdf/

## 原始函数

`office.api.pdf.encrypt4pdf`
