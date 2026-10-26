---
name: find_excel_data
description: 在 Excel 文件中搜索指定关键词并返回文件、行号、详情。当用户提到搜索 Excel、Excel 查找、Excel 搜索内容时使用。
---

# find_excel_data Skill

> 搜索 Excel 中指定内容的文件、行数、内容详情

## 功能描述

在指定目录下的所有 Excel 文件中搜索包含特定关键词的内容，并返回匹配的文件名、行号和详情。

## 所属分类

`office/skills/excel/find_excel_data/`

## 调用方式

```python
from skills.excel import find_excel_data

find_excel_data(
    search_key='python',
    target_dir='./data'
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `search_key` | str | 是 | - | 需要搜索的关键词 |
| `target_dir` | str | 是 | - | 搜索的目录路径 |

## 返回值

`None`（结果直接打印输出）

## 使用示例

```python
from skills.excel import find_excel_data
find_excel_data(search_key='订单', target_dir='./订单数据')
```

## 视频教程

https://www.bilibili.com/video/BV1Bd4y1B7yr/

## 原始函数

`office.api.excel.find_excel_data`
