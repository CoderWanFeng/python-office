---
name: video_edit
description: 音视频剪辑工具箱。包含视频剪辑截取、音频剪辑截取、视频画面裁剪、视频拼接合并、音频拼接合并、视频合成/替换音频。当用户提到音视频剪辑、裁剪视频、合并视频、音频剪辑、视频配音时使用。
---

# video_edit Skill

> 音视频剪辑功能集（截取、裁剪、拼接、配音/音轨替换）

## 功能描述

本 Skill 将所有音视频剪辑相关功能合并为一个统一的 API 模块，包含以下 6 个核心剪辑功能：

1. `cut_video`: 截取视频指定时间段片段
2. `cut_audio`: 截取音频指定时间段片段
3. `crop_video`: 裁剪视频画面的坐标区域与尺寸
4. `concat_videos`: 多个视频文件顺序拼接合并
5. `concat_audios`: 多个音频文件顺序拼接合并
6. `add_audio_to_video`: 视频合成/替换背景音乐或音频

## 所属分类

`office/skills/video/video_edit/`

## 调用方式

```python
from skills.video.video_edit import (
    cut_video,
    cut_audio,
    crop_video,
    concat_videos,
    concat_audios,
    add_audio_to_video,
)
```

或从 `skills.video` 模块导入：
```python
from skills.video import video_edit

video_edit.cut_video(video_path='./test.mp4', start_time='00:00:10', end_time='00:00:30')
```

## 功能与参数说明

### 1. 视频截取 `cut_video`
| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `video_path` | str | 是 | - | 视频文件路径 |
| `start_time` | float/str | 否 | `0` | 开始时间（秒数或格式如 `'00:01:10'`） |
| `end_time` | float/str | 否 | `None` | 结束时间（秒数或格式如 `'00:02:30'`，默认结尾） |
| `output_path` | str | 否 | `'./'` | 输出目录 |
| `output_name` | str | 否 | `None` | 输出文件名（默认原名后加 `_cut`） |

### 2. 音频截取 `cut_audio`
| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `audio_path` | str | 是 | - | 音频文件路径 |
| `start_time` | float/str | 否 | `0` | 开始时间（秒数或格式如 `'00:00:05'`） |
| `end_time` | float/str | 否 | `None` | 结束时间 |
| `output_path` | str | 否 | `'./'` | 输出目录 |
| `output_name` | str | 否 | `None` | 输出文件名 |

### 3. 画面裁剪 `crop_video`
| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `video_path` | str | 是 | - | 视频文件路径 |
| `x1` | int | 否 | `0` | 左上角 x 坐标 |
| `y1` | int | 否 | `0` | 左上角 y 坐标 |
| `x2` | int | 否 | `None` | 右下角 x 坐标 |
| `y2` | int | 否 | `None` | 右下角 y 坐标 |
| `width` | int | 否 | `None` | 裁剪宽度（可代替 x2） |
| `height` | int | 否 | `None` | 裁剪高度（可代替 y2） |
| `output_path` | str | 否 | `'./'` | 输出目录 |
| `output_name` | str | 否 | `None` | 输出文件名 |

### 4. 视频拼接 `concat_videos`
| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `video_list` | list[str] | 是 | - | 视频路径列表 |
| `output_path` | str | 否 | `'./'` | 输出目录 |
| `output_name` | str | 否 | `'concat_video.mp4'` | 输出文件名 |

### 5. 音频拼接 `concat_audios`
| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `audio_list` | list[str] | 是 | - | 音频路径列表 |
| `output_path` | str | 否 | `'./'` | 输出目录 |
| `output_name` | str | 否 | `'concat_audio.mp3'` | 输出文件名 |

### 6. 合成音频/配音 `add_audio_to_video`
| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `video_path` | str | 是 | - | 视频文件路径 |
| `audio_path` | str | 是 | - | 音频文件路径 |
| `output_path` | str | 否 | `'./'` | 输出目录 |
| `output_name` | str | 否 | `None` | 输出文件名 |

## 使用示例

```python
from skills.video import video_edit

# 视频截取
video_edit.cut_video(video_path='./input.mp4', start_time=0, end_time=10)

# 视频合成音频
video_edit.add_audio_to_video(video_path='./input.mp4', audio_path='./music.mp3')
```

## 原始函数

- `office.api.video.cut_video`
- `office.api.video.cut_audio`
- `office.api.video.crop_video`
- `office.api.video.concat_videos`
- `office.api.video.concat_audios`
- `office.api.video.add_audio_to_video`
