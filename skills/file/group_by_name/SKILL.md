---
name: group_by_name
description: 按文件名的规则将文件分组整理到不同目录。当用户提到按名称分组文件、整理文件、自动归类时使用。
---

# group_by_name Skill

> 按名称分组整理文件

## 功能描述

按文件名的前缀或规则，将文件分组整理到不同目录中。

> ⚠️ TODO: 该功能为历史功能，行为待测试。

## 所属分类

`office/skills/file/group_by_name/`

## 调用方式

```python
from skills.file import group_by_name

group_by_name(
    path='./data',
    output_path=None,
    del_old_file=None
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `path` | str | 是 | - | 路径 |
| `output_path` | str | 否 | `None` | 输出路径 |
| `del_old_file` | bool | 否 | `None` | 是否删除旧文件 |

## 返回值

`None`

## 原始函数

`office.api.file.group_by_name`
