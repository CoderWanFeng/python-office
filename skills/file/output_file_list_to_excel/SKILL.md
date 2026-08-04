---
name: output_file_list_to_excel
description: 将文件夹下的所有文件名整理到一个 Excel 表格中。当用户提到文件名清单、文件名导出 Excel、文件名汇总时使用。
---

# output_file_list_to_excel Skill

> 整理当前文件夹下的文件名到一个 Excel 里

## 功能描述

将指定目录下的所有文件名整理到一个 Excel 文件中。

## 所属分类

`office/skills/file/output_file_list_to_excel/`

## 调用方式

```python
from skills.file import output_file_list_to_excel

output_file_list_to_excel(dir_path='./data')
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `dir_path` | str | 是 | - | 目录路径 |

## 返回值

`None`

## 使用示例

```python
from skills.file import output_file_list_to_excel
output_file_list_to_excel(dir_path='./我的文件夹')
```

## 原始函数

`office.api.file.output_file_list_to_excel`
