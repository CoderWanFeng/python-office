---
name: down4img
description: 从指定 URL 下载图片并保存到本地。当用户提到下载图片、抓图、图片下载、网络图片保存时使用。
---

# down4img Skill

> 下载图片并保存到指定路径

## 功能描述

从给定的 URL 下载图片，并将其保存到指定路径。

## 所属分类

`office/skills/image/down4img/`

## 调用方式

```python
from office.skills.image import down4img

down4img(
    url='https://example.com/image.png',
    output_path='./images',
    output_name='my_image',
    type='jpg'
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `url` | str | 是 | - | 图片的 URL 地址 |
| `output_path` | str | 否 | `'.'` | 保存图片的路径 |
| `output_name` | str | 否 | `'down4img'` | 保存图片时使用的文件名 |
| `type` | str | 否 | `'jpg'` | 图片的文件类型 |

## 返回值

`None`

## 使用示例

```python
from office.skills.image import down4img
down4img(url='https://example.com/photo.jpg')
```

## 原始函数

`office.api.image.down4img`
