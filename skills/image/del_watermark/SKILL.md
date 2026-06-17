---
name: del_watermark
description: 从图片中删除水印并保存。当用户提到去水印、去除水印、消水印、清除图片水印时使用。
---

# del_watermark Skill

> 从输入的图片中删除水印

## 功能描述

从输入的图片中删除水印，并保存处理后的图片到指定路径。

## 所属分类

`office/skills/image/del_watermark/`

## 调用方式

```python
from office.skills.image import del_watermark

del_watermark(
    input_image='./with_watermark.jpg',
    output_image='./no_watermark.jpg'
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `input_image` | str | 是 | - | 输入图片的路径 |
| `output_image` | str | 否 | `'./del_water_mark.jpg'` | 处理后图片的保存路径 |

## 返回值

`None`

## 使用示例

```python
from office.skills.image import del_watermark
del_watermark(input_image='./photo.jpg')
```

## 原始函数

`office.api.image.del_watermark`
