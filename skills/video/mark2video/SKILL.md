---
name: mark2video
description: 给视频添加文字水印，支持自定义字体大小、类型、颜色。当用户提到视频水印、视频加 logo、视频字幕时使用。
---

# mark2video Skill

> 给视频添加水印

## 功能描述

向视频添加文字水印，支持自定义字体大小、字体类型、颜色等参数。

## 所属分类

`office/skills/video/mark2video/`

## 调用方式

```python
from skills.video import mark2video

mark2video(
    video_path='./test.mp4',
    output_path='./',
    output_name='marked.mp4',
    mark_str='python-office',
    font_size=28,
    font_type='Arial',
    font_color='white'
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `video_path` | str | 是 | - | 视频地址 |
| `output_path` | str | 否 | `'./'` | 输出地址 |
| `output_name` | str | 否 | `'mark2video.mp4'` | 输出名称，记得带 `.mp4` |
| `mark_str` | str | 否 | `'www.python-office.com'` | 水印内容，**只支持英文** |
| `font_size` | int | 否 | `28` | 水印字体大小 |
| `font_type` | str | 否 | `'Arial'` | 水印字体类型 |
| `font_color` | str | 否 | `'white'` | 水印颜色 |

## 返回值

`None`

## 使用示例

```python
from skills.video import mark2video
mark2video(video_path='./demo.mp4', mark_str='My Channel')
```

## 原始函数

`office.api.video.mark2video`
