---
name: file_name_add_postfix
description: 给文件名批量增加指定后缀。当用户提到加后缀、文件名后缀、批量加后缀时使用。
---

# file_name_add_postfix Skill

> 批量重命名：给文件名增加后缀

## 功能描述

给指定文件的文件名增加指定的后缀。

## 所属分类

`office/skills/file/file_name_add_postfix/`

## 调用方式

```python
from office.skills.file import file_name_add_postfix

file_name_add_postfix(
    file_path='./test.txt',
    postfix_content='_backup'
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `file_path` | str | 是 | - | 文件路径 |
| `postfix_content` | str | 是 | - | 后缀内容 |

## 返回值

`None`

## 使用示例

```python
from office.skills.file import file_name_add_postfix
file_name_add_postfix(file_path='./data.txt', postfix_content='_v1')
```

## 原始函数

`office.api.file.file_name_add_postfix`
