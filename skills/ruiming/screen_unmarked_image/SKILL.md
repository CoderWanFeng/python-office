---
name: screen_unmarked_image
description: 在指定目录下筛选没有对应标注文件（.xml）的图片，并移动到「未标注图片」子目录。当用户提到筛选未标注图片、未标数据、清洗图片数据集时使用。
---

# screen_unmarked_image Skill

> 筛选未标注的图像

## 功能描述

在指定目录下，筛选出没有对应标注文件（如 .xml）的图片，并将其移动到 `未标注图片` 子目录中。

## 所属分类

`office/skills/ruiming/screen_unmarked_image/`

## 调用方式

```python
from skills.ruiming import screen_unmarked_image

screen_unmarked_image(dir_path='./dataset')
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `dir_path` | str | 是 | - | 图片及标注文件的存放路径 |
| `image_name_extension` | str | 否 | `'.jpg'` | 图片文件的后缀 |
| `marked_file_name_extension` | str | 否 | `'.xml'` | 标注文件的后缀 |

## 返回值

`None`（结果直接打印输出）

## 使用示例

```python
from skills.ruiming import screen_unmarked_image
screen_unmarked_image(dir_path='./my_dataset')
```

## 原始函数

`office.api.testApi.ruiming.screen_unmarked_image`
