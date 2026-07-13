---
name: doc2docx
description: 将旧版 Word 文档（.doc）转换为新版（.docx）。当用户提到 doc 转 docx、旧 Word 转新 Word 时使用。
---

# doc2docx Skill

> 将 Doc 文件转换为 Docx 文件

## 功能描述

将旧版 Word 文档（.doc）转换为新版 Word 文档（.docx）。

## 所属分类

`office/skills/word/doc2docx/`

## 调用方式

```python
from office.skills.word import doc2docx

doc2docx(
    input_path='./old.doc',
    output_path='./',
    output_name='new.docx'
)
```

也可以直接把目标文件路径传给 `output_path`：

```python
from office.skills.word import doc2docx

doc2docx(
    input_path='./old.doc',
    output_path='./new/new.docx'
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `input_path` | str | 是 | - | 输入 Doc 文件的路径 |
| `output_path` | str | 否 | `'./'` | 输出 Docx 文件的路径，可以是输出目录，也可以是完整的 `.docx` 文件路径 |
| `output_name` | str | 否 | `None` | 输出 Docx 文件的名称。默认原文件名 |

## 返回值

`None`

## 使用示例

```python
from office.skills.word import doc2docx
doc2docx(input_path='./old.doc', output_path='./new/')
```

```python
from office.skills.word import doc2docx
doc2docx(input_path='./old.doc', output_path='./new/new.docx')
```

## 原始函数

`office.api.word.doc2docx`
