---
name: fake2excel
description: 自动创建 Excel 并模拟数据。当用户提到生成测试数据、mock 数据、造数据、Excel 模板、模拟数据时使用。
---

# fake2excel Skill

> 自动创建 Excel 文件并模拟数据

## 功能描述

自动生成一个 Excel 文件，并填充指定列的模拟数据。支持多种字段类型（如姓名、电话、地址等），支持中英文两种语言环境。

## 所属分类

`office/skills/excel/fake2excel/`

## 调用方式

```python
from office.skills.excel import fake2excel

fake2excel(
    columns=['name', 'phone'],
    rows=100,
    path='./fake2excel.xlsx',
    language='zh_CN'
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `columns` | list | 否 | `['name']` | 需要生成的列名。可模拟的字段参考：https://www.python4office.cn/python-office/fake2excel/ |
| `rows` | int | 否 | `1` | 生成的行数 |
| `path` | str | 否 | `'./fake2excel.xlsx'` | 生成的 Excel 文件路径和名称 |
| `language` | str | 否 | `'zh_CN'` | 数据语言。`'zh_CN'` 为中文，`'english'` 为英文 |

## 返回值

`None`

## 使用示例

```python
# 示例 1：生成中文测试数据
from office.skills.excel import fake2excel
fake2excel(columns=['name', 'phone', 'address'], rows=1000, path='./test_cn.xlsx')

# 示例 2：生成英文测试数据
fake2excel(columns=['name', 'email'], rows=500, language='english', path='./test_en.xlsx')
```

## 视频教程

https://www.bilibili.com/video/BV1wr4y1b7uk/

## 原始函数

`office.api.excel.fake2excel`
