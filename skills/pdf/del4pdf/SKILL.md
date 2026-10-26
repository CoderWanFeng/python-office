---
name: del4pdf
description: 删除 PDF 文件中指定的页面。当用户提到 PDF 删除页、PDF 删页、删 PDF 页 时使用。
---

# del4pdf Skill

> 删除 PDF 文件中的指定页面

## 功能描述

从 PDF 文件中删除指定的页面。

## 所属分类

`office/skills/pdf/del4pdf/`

## 调用方式

```python
from skills.pdf import del4pdf

del4pdf(
    input_file='./test.pdf',
    output_file='./deleted.pdf',
    page_nums=[0, 2]
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `input_file` | str | 否 | - | PDF 文件路径 |
| `output_file` | str | 否 | - | 输出 PDF 文件路径 |
| `page_nums` | list | 否 | - | 要删除的页码列表 |

## 返回值

`None`

## 使用示例

```python
from skills.pdf import del4pdf
# 删除第 1 页和第 3 页
del4pdf(input_file='./report.pdf', output_file='./new.pdf', page_nums=[0, 2])
```

## 视频教程

https://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/9-del4pdf

## 原始函数

`office.api.pdf.del4pdf`
