---
name: add_line_by_type
description: 根据文件类型向指定文件中添加代码行。当用户提到批量添加代码、按类型插入行、自动加 import 时使用。
---

# add_line_by_type Skill

> 根据类型添加行

## 功能描述

根据文件类型，向指定文件中添加对应的代码行。

> ⚠️ TODO: 该功能为历史功能，行为待测试。

## 所属分类

`office/skills/file/add_line_by_type/`

## 调用方式

```python
from office.skills.file import add_line_by_type

add_line_by_type(
    add_line_dict={'import': 'import os'},
    file_path='./test.py',
    file_type='.py',
    output_path='add_line'
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `add_line_dict` | dict | 是 | - | 添加行的字典 |
| `file_path` | str | 是 | - | 文件路径 |
| `file_type` | str | 否 | `'.py'` | 文件类型 |
| `output_path` | str | 否 | `'add_line'` | 输出路径 |

## 返回值

`None`

## 原始函数

`office.api.file.add_line_by_type`
