---
name: txt2mp3
description: 将文本内容转换为 MP3 语音文件，可选择直接朗读。当用户提到文字转语音、TTS、文本朗读、AI 配音时使用。
---

# txt2mp3 Skill

> 文本转语音

## 功能描述

将文本内容转换为 mp3 语音文件，并可选择是否直接播放。

## 所属分类

`office/skills/video/txt2mp3/`

## 调用方式

```python
from office.skills.video import txt2mp3

txt2mp3(
    content='你好，世界',
    file=None,
    mp3='./hello.mp3',
    speak=True
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `content` | str | 否 | `'程序员晚枫'` | 需要转换的内容 |
| `file` | str | 否 | `None` | 指定读取的文件，优先级最高 |
| `mp3` | str | 否 | `'./程序员晚枫.mp3'` | 需要保存的 mp3 位置和名称。填 `None` 不保存 |
| `speak` | bool | 否 | `True` | 是否直接朗读 |

## 返回值

`None`

## 使用示例

```python
from office.skills.video import txt2mp3
# 直接朗读
txt2mp3(content='你好，世界', mp3=None, speak=True)
# 保存为 mp3 文件
txt2mp3(content='你好，世界', mp3='./hello.mp3', speak=False)
```

## 原始函数

`office.api.video.txt2mp3`
