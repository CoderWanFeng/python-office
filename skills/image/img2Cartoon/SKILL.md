---
name: img2Cartoon
description: 通过百度 API 将图片转换为卡通风格。当用户提到卡通化、图片转卡通、卡通风、漫画风时使用。
---

# img2Cartoon Skill

> 将图片转换为卡通风格

## 功能描述

通过调用百度 API，将指定图片转换为卡通风格的图片。需要提供百度 AI 的 client_api 和 client_secret。

## 所属分类

`office/skills/image/img2Cartoon/`

## 调用方式

```python
from office.skills.image import img2Cartoon

img2Cartoon(
    path='./test.png',
    client_api='your_api_key',
    client_secret='your_secret'
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `path` | str | 是 | - | 图片文件的路径 |
| `client_api` | str | 否 | `''` | 客户端的 API 密钥 |
| `client_secret` | str | 否 | `''` | 客户端的密钥 |

## 返回值

`None`

## 使用示例

```python
from office.skills.image import img2Cartoon
img2Cartoon(path='./photo.jpg')
```

## 原始函数

`office.api.image.img2Cartoon`
