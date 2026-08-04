---
name: file_name_insert_content
description: 在文件名中间指定位置插入字符。当用户提到文件名插入、重命名插入字符时使用。
---

# file_name_insert_content Skill

> 批量重命名：在文件名中间插入字符

## 功能描述

在指定文件的文件名中间指定位置插入新的字符。

## 所属分类

`office/skills/file/file_name_insert_content/`

## 调用方式

```python
from skills.file import file_name_insert_content

file_name_insert_content(
    file_path='./test.txt',
    insert_position=2,
    insert_content='_new'
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `file_path` | str | 是 | - | 文件路径 |
| `insert_position` | int | 是 | - | 插入位置 |
| `insert_content` | str | 是 | - | 插入的内容 |

## 返回值

`None`

## 使用示例

```python
from skills.file import file_name_insert_content
file_name_insert_content(file_path='./report.txt', insert_position=2, insert_content='_2024')
```

## 原始函数

`office.api.file.file_name_insert_content`
