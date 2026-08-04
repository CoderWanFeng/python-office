---
name: merge2excel
description: 将多个 Excel 文件合并到一个 Excel 的不同 sheet 中。当用户提到合并 Excel、合并多个表格、多个 Excel 合并时使用。
---

# merge2excel Skill

> 将多个 Excel 文件合并到一个 Excel 的不同 sheet 中

## 功能描述

将指定目录下的所有 Excel 文件合并到一个新的 Excel 文件中，每个原始文件对应一个新 sheet。

## 所属分类

`office/skills/excel/merge2excel/`

## 调用方式

```python
from skills.excel import merge2excel

merge2excel(
    dir_path='./excel_files',
    output_file='./merge2excel.xlsx'
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `dir_path` | str | 是 | - | 包含多个 Excel 文件的目录路径 |
| `output_file` | str | 否 | `'merge2excel.xlsx'` | 合并后的 Excel 文件路径 |

## 返回值

`None`

## 使用示例

```python
from skills.excel import merge2excel
merge2excel(dir_path='./excels', output_file='./all_in_one.xlsx')
```

## 视频教程

https://www.bilibili.com/video/BV1Th4y1Y7kd/

## 原始函数

`office.api.excel.merge2excel`
