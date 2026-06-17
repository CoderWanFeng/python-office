---
name: screen_without_label_json_file
description: 筛选 shapes 字段为空的 JSON 标注文件，并移动到「无标签json文件」子目录。当用户提到筛选空标签 JSON、清洗 JSON 标注时使用。
---

# screen_without_label_json_file Skill

> 筛选无标签内容的 JSON 文件

## 功能描述

在指定目录下，筛选出 shapes 字段为空的 JSON 文件，并将其移动到 `无标签json文件` 子目录中。常用于数据清洗场景。

## 所属分类

`office/skills/ruiming/screen_without_label_json_file/`

## 调用方式

```python
from office.skills.ruiming import screen_without_label_json_file

screen_without_label_json_file(dir_path='./jsons')
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `dir_path` | str | 是 | - | JSON 文件的存放路径 |

## 返回值

`None`（结果直接打印输出）

## 使用示例

```python
from office.skills.ruiming import screen_without_label_json_file
screen_without_label_json_file(dir_path='./annotations')
```

## 原始函数

`office.api.testApi.ruiming.screen_without_label_json_file`
