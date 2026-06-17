---
name: add_watermark
description: 通过交互方式给 PDF 添加水印。当用户提到 PDF 互动加水印时使用。
---

# add_watermark Skill

> 给图片加水印

## 功能描述

向图片添加文字水印，支持自定义颜色、大小、透明度、间距、角度等参数。

## 所属分类

`office/skills/image/add_watermark/`

## 调用方式

```python
from office.skills.image import add_watermark

add_watermark(
    file='./test.png',
    mark='python-office',
    output_path='./',
    color="#eaeaea",
    size=30,
    opacity=0.35,
    space=200,
    angle=30
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `file` | str | 是 | - | 图片位置 |
| `mark` | str | 是 | - | 水印内容 |
| `output_path` | str | 否 | `'./'` | 输出位置 |
| `color` | str | 否 | `"#eaeaea"` | 水印颜色 |
| `size` | int | 否 | `30` | 水印大小 |
| `opacity` | float | 否 | `0.35` | 不透明度，范围 0.01~1 |
| `space` | int | 否 | `200` | 水印间距 |
| `angle` | int | 否 | `30` | 水印角度 |

## 返回值

`None`

## 使用示例

```python
from office.skills.image import add_watermark
add_watermark(file='./photo.jpg', mark='我的水印')
```

## 原始函数

`office.api.image.add_watermark`
