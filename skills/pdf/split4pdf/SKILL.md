---
name: split4pdf
description: 按指定页码范围拆分 PDF 文件。当用户提到 PDF 拆分、PDF 分割、PDF 切分、拆 PDF 时使用。
---

# split4pdf Skill

> 拆分 PDF 文件

## 功能描述

按指定页码范围拆分 PDF 文件。

## 所属分类

`office/skills/pdf/split4pdf/`

## 调用方式

```python
from skills.pdf import split4pdf

split4pdf(
    input_file='./test.pdf',
    output_file='./split.pdf',
    from_page=0,
    to_page=5
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `input_file` | str | 否 | - | PDF 文件路径 |
| `output_file` | str | 否 | `'./output_path/split_pdf.pdf'` | 输出拆分后的 PDF 文件路径 |
| `from_page` | int | 否 | `-1` | 起始页码（-1 表示从第一页开始） |
| `to_page` | int | 否 | `-1` | 结束页码（-1 表示到最后一页结束） |

## 返回值

`None`

## 使用示例

```python
from skills.pdf import split4pdf
# 拆分第 1-5 页
split4pdf(input_file='./report.pdf', output_file='./part1.pdf', from_page=0, to_page=4)
```

## 视频教程

https://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/4-split4pdf/

## 原始函数

`office.api.pdf.split4pdf`
