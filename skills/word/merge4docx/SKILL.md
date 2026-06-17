---
name: merge4docx
description: 将多个 Word 文档合并为一个文件。当用户提到 Word 合并、合并 docx、合并多个 Word 时使用。
---

# merge4docx Skill

> 合并多个 Docx 文件为一个文件

## 功能描述

将多个 Word 文档合并为一个文件，可以是单个文件列表或文件夹下所有 docx 文件。

## 所属分类

`office/skills/word/merge4docx/`

## 调用方式

```python
from office.skills.word import merge4docx

merge4docx(
    input_path='./word_files',
    output_path='./output/',
    new_word_name='merged.docx'
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `input_path` | str | 是 | - | 输入文件的路径。可以是单个文件或文件夹路径 |
| `output_path` | str | 是 | - | 输出合并后文件的路径 |
| `new_word_name` | str | 否 | `'merge4docx'` | 合并后新文件的名称 |

## 返回值

`None`

## 使用示例

```python
from office.skills.word import merge4docx
merge4docx(
    input_path='./word_files',
    output_path='./output/',
    new_word_name='all_merged'
)
```

## 原始函数

`office.api.word.merge4docx`
