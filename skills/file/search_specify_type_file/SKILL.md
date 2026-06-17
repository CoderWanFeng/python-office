---
name: search_specify_type_file
description: 在指定路径下搜索指定类型的文件（如 .txt、.pdf）。当用户提到按类型搜索文件、找某类文件、检索文件时使用。
---

# search_specify_type_file Skill

> 在当前路径下搜索指定类型的文件

## 功能描述

在指定路径下搜索指定类型的文件。

## 所属分类

`office/skills/file/search_specify_type_file/`

## 调用方式

```python
from office.skills.file import search_specify_type_file

search_specify_type_file(
    file_path='./data',
    file_type='.txt'
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `file_path` | str | 是 | - | 文件路径 |
| `file_type` | str | 是 | - | 文件类型（如 `.txt`、`.py`） |

## 返回值

`None`（结果直接打印输出）

## 使用示例

```python
from office.skills.file import search_specify_type_file
search_specify_type_file(file_path='./docs', file_type='.pdf')
```

## 原始函数

`office.api.file.search_specify_type_file`
