---
name: replace4filename
description: 批量修改文件/文件夹名称，替换或删除指定内容。当用户提到批量重命名、批量改名、文件替换、文件名替换时使用。
---

# replace4filename Skill

> 批量重命名：批量修改文件/文件夹名称

## 功能描述

在指定目录下，批量将文件/文件夹名称中包含的指定内容替换为新内容。如果不填替换内容则实现删除效果。

## 所属分类

`office/skills/file/replace4filename/`

## 调用方式

```python
from skills.file import replace4filename

replace4filename(
    path='./my_folder',
    del_content='old',
    replace_content='new',
    dir_rename=True,
    file_rename=True,
    suffix=None
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `path` | str | 是 | - | 需要修改文件夹/文件名称的根目录。**注意：该根目录名称不会被修改** |
| `del_content` | str | 是 | - | 需要替换/删除的内容 |
| `replace_content` | str | 否 | `''` | 替换后的内容。不填则实现删除效果 |
| `dir_rename` | bool | 否 | `True` | 是否修改文件夹名称 |
| `file_rename` | bool | 否 | `True` | 是否修改文件名称 |
| `suffix` | str | 否 | `None` | 指定修改的文件类型。默认所有 |

## 返回值

`None`

## 使用示例

```python
from skills.file import replace4filename
# 批量替换文件名中的"old"为"new"
replace4filename(path='./data', del_content='old', replace_content='new')
# 批量删除文件名中的"tmp"
replace4filename(path='./data', del_content='tmp', replace_content='')
```

## 原始函数

`office.api.file.replace4filename`
