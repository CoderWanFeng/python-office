---
name: receive_message
description: 通过微信接收消息并保存到本地文件。当用户提到微信收消息、接收微信消息、微信消息保存时使用。
---

# receive_message Skill

> 接收微信机器人消息并保存到指定路径

## 功能描述

通过微信自动化接收消息，并保存到指定文件中。

## 所属分类

`office/skills/wechat/receive_message/`

## 调用方式

```python
from skills.wechat import receive_message

receive_message(
    who='文件传输助手',
    txt='userMessage.txt',
    output_path='./'
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `who` | str | 否 | `'文件传输助手'` | 发送消息的微信联系人 |
| `txt` | str | 否 | `'userMessage.txt'` | 消息内容的文本文件名 |
| `output_path` | str | 否 | `'./'` | 消息内容的保存路径 |

## 返回值

`None`：将消息保存到指定的文件和路径中

## 使用示例

```python
from skills.wechat import receive_message
receive_message(who='文件传输助手', txt='messages.txt', output_path='./received/')
```

## 原始函数

`office.api.wechat.receive_message`
