---
name: merge2pdf
description: 将多个 PDF 文件合并为一个 PDF。当用户提到 PDF 合并、合并 PDF 文件、PDF 拼接时使用。
---

# merge2pdf Skill

> 合并多个 PDF 文件

## 功能描述

将多个 PDF 文件合并为一个 PDF 文件。

## 所属分类

`office/skills/pdf/merge2pdf/`

## 调用方式

```python
from skills.pdf import merge2pdf

merge2pdf(
    input_file_list=['./1.pdf', './2.pdf', './3.pdf'],
    output_file='./merged.pdf'
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `input_file_list` | list | 否 | - | PDF 文件路径列表 |
| `output_file` | str | 否 | - | 合并后的 PDF 文件路径 |
| `one_by_one` | list | 否 | - | **[已弃用]** 请使用 `input_file_list` |
| `output` | str | 否 | - | **[已弃用]** 请使用 `output_file` |

## 返回值

`None`

## 使用示例

```python
from skills.pdf import merge2pdf
merge2pdf(
    input_file_list=['./part1.pdf', './part2.pdf'],
    output_file='./all.pdf'
)
```

## 视频教程

https://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/8-merge2pdf

## 原始函数

`office.api.pdf.merge2pdf`
