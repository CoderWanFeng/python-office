---
name: file_name_add_prefix
description: 给文件名批量增加指定前缀。当用户提到加前缀、文件名前缀、批量加前缀时使用。
---

# file_name_add_prefix Skill

> 批量重命名：给文件名增加前缀

## 功能描述

给指定文件的文件名增加指定的前缀。

## 所属分类

`office/skills/file/file_name_add_prefix/`

## 调用方式

```python
from skills.file import file_name_add_prefix

file_name_add_prefix(
    file_path='./test.txt',
    prefix_content='prefix_'
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `file_path` | str | 是 | - | 文件路径 |
| `prefix_content` | str | 是 | - | 前缀内容 |

## 返回值

`None`

## 使用示例

```python
from skills.file import file_name_add_prefix
file_name_add_prefix(file_path='./doc.txt', prefix_content='backup_')
```

## 原始函数

`office.api.file.file_name_add_prefix`
