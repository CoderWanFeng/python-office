---
name: audio2txt
description: 从音频文件中提取文字（语音转文字），需要腾讯云 API 凭据。当用户提到音频转文字、语音识别、ASR、音频转字幕时使用。
---

# audio2txt Skill

> 从音频里提取文字

## 功能描述

使用语音识别 API 从音频中提取文字。

> ⚠️ 注意：本地语音文件不能大于 5MB。

## 所属分类

`office/skills/video/audio2txt/`

## 调用方式

```python
from office.skills.video import audio2txt

audio2txt(
    audio_path='./test.mp3',
    appid='your_appid',
    secret_id='your_secret_id',
    secret_key='your_secret_key'
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `audio_path` | str | 是 | - | 音频文件路径 |
| `appid` | str | 是 | - | 语音识别 API 的应用 ID |
| `secret_id` | str | 是 | - | 语音识别 API 的密钥 ID |
| `secret_key` | str | 是 | - | 语音识别 API 的密钥 |

## 返回值

`None`

## 使用示例

```python
from office.skills.video import audio2txt
audio2txt(
    audio_path='./audio.mp3',
    appid='your_appid',
    secret_id='your_secret_id',
    secret_key='your_secret_key'
)
```

## 原始函数

`office.api.video.audio2txt`
