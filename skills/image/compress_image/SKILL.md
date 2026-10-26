---
name: compress_image
description: 压缩图片文件大小，通过调整质量参数控制输出体积。当用户提到压缩图片、图片减肥、缩小图片体积、降低图片质量时使用。
---

# compress_image Skill

> 压缩图像文件，以减小其文件大小，同时尽量保持视觉质量

## 功能描述

将图像文件压缩为更小的体积，通过调整压缩质量参数控制输出文件大小。

## 所属分类

`office/skills/image/compress_image/`

## 调用方式

```python
from skills.image import compress_image

compress_image(
    input_file='./test.png',
    output_file='./test_compressed.jpg',
    quality=50
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `input_file` | str | 是 | - | 需要压缩的输入图像文件的路径 |
| `output_file` | str | 是 | - | 压缩后的图像文件保存路径 |
| `quality` | int | 是 | - | 压缩质量等级，取值范围 0 到 95。值越高，质量越好，文件越大 |

## 返回值

`None`

## 使用示例

```python
from skills.image import compress_image
compress_image(input_file='./photo.jpg', output_file='./photo_small.jpg', quality=30)
```

## 原始函数

`office.api.image.compress_image`
