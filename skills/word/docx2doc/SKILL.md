---
name: docx2doc
description: 将新版 Word 文档（.docx）转换为旧版（.doc）。当用户提到 docx 转 doc、新 Word 转旧 Word 时使用。
---

# docx2doc Skill

> 将 Docx 文件转换为 Doc 文件

## 功能描述

将新版 Word 文档（.docx）转换为旧版 Word 文档（.doc）。

## 所属分类

`office/skills/word/docx2doc/`

## 调用方式

```python
from office.skills.word import docx2doc

docx2doc(
    input_path='./new.docx',
    output_path='./',
    output_name='old.doc'
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `input_path` | str | 是 | - | 输入 Docx 文件的路径 |
| `output_path` | str | 否 | `'./'` | 输出 Doc 文件的路径 |
| `output_name` | str | 否 | `None` | 输出 Doc 文件的名称。默认原文件名 |

## 返回值

`None`

## 使用示例

```python
from office.skills.word import docx2doc
docx2doc(input_path='./new.docx', output_path='./old/')
```

## 原始函数

`office.api.word.docx2doc`
