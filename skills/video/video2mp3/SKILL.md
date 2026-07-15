---
name: video2mp3
description: 从视频文件中提取音频并保存为 MP3。当用户提到视频转音频、提取音频、抽 MP3、视频提取声音时使用。
---

# video2mp3 Skill

> 将视频文件转换为 mp3 音频文件

## 功能描述

从视频中提取音频，保存为 mp3 格式。

## 所属分类

`office/skills/video/video2mp3/`

## 调用方式

```python
from skills.video import video2mp3

video2mp3(
    path='./test.mp4',
    mp3_name='test.mp3',
    output_path='./'
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `path` | str | 是 | - | 视频文件的路径 |
| `mp3_name` | str | 否 | `None` | 输出 mp3 文件的名称。如果未提供，默认为原视频文件名 |
| `output_path` | str | 否 | `'./'` | 输出 mp3 文件的路径 |

## 返回值

`None`：在指定输出路径下生成 mp3 文件

## 使用示例

```python
from skills.video import video2mp3
video2mp3(path='./movie.mp4', mp3_name='movie_audio.mp3')
```

## 原始函数

`office.api.video.video2mp3`
