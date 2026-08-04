---
name: pencil4img
description: 将输入的图片转换为铅笔画风格。当用户提到铅笔画、素描、画风转换、图片转素描时使用。
---

# pencil4img Skill

> 使用 pencil4img 算法处理图像

## 功能描述

将输入的图像转换为铅笔画风格的图像。

## 所属分类

`office/skills/image/pencil4img/`

## 调用方式

```python
from skills.image import pencil4img

pencil4img(
    input_img='./test.jpg',
    output_path='./',
    output_name='pencil4img.jpg'
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `input_img` | str | 是 | - | 输入的图像文件路径 |
| `output_path` | str | 否 | `'./'` | 输出图像的路径 |
| `output_name` | str | 否 | `'pencil4img.jpg'` | 转换后的图像文件名 |

## 返回值

`None`

## 使用示例

```python
from skills.image import pencil4img
pencil4img(input_img='./photo.jpg')
```

## 原始函数

`office.api.image.pencil4img`
