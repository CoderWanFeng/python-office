---
name: get_files
description: 在指定路径下搜索文件并返回路径列表，支持按后缀、子目录、层级过滤。当用户提到获取文件列表、查找某类文件、列出所有文件时使用。
---

# get_files Skill

> 搜索当前路径下所有指定类型的文件，并以列表形式返回

## 功能描述

在指定路径下搜索文件，支持按文件名、后缀、子目录等条件过滤，返回文件路径列表。

## 所属分类

`office/skills/file/get_files/`

## 调用方式

```python
from office.skills.file import get_files

files = get_files(
    path='./data',
    name='report',
    suffix='.txt',
    sub=False,
    level=0
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `path` | str | 是 | - | 路径 |
| `name` | str | 否 | `''` | 文件名 |
| `suffix` | str | 否 | `None` | 文件后缀 |
| `sub` | bool | 否 | `False` | 是否搜索子目录 |
| `level` | int | 否 | `0` | 搜索层级 |

## 返回值

`list`：文件路径列表

## 使用示例

```python
from office.skills.file import get_files
# 获取所有 .txt 文件
txt_files = get_files(path='./docs', suffix='.txt', sub=True)
# 获取所有名为 report 的文件
reports = get_files(path='./data', name='report', sub=True)
```

## 原始函数

`office.api.file.get_files`
