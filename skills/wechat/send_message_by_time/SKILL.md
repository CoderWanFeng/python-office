---
name: send_message_by_time
description: 通过微信在指定时间向联系人发送定时消息。当用户提到定时发微信、微信定时消息、预约发微信时使用。
---

# send_message_by_time Skill

> 在指定时间发送消息给指定联系人

## 功能描述

通过微信自动化，在指定时间向联系人发送一条消息（定时消息）。

## 所属分类

`office/skills/wechat/send_message_by_time/`

## 调用方式

```python
from office.skills.wechat import send_message_by_time

send_message_by_time(
    who='文件传输助手',
    message='该起床了',
    time='08:00:00'
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `who` | str | 是 | - | 接收消息的联系人名称 |
| `message` | str | 是 | - | 要发送的消息内容 |
| `time` | str | 是 | - | 发送消息的预定时间 |

## 返回值

`None`

## 使用示例

```python
from office.skills.wechat import send_message_by_time
send_message_by_time(who='文件传输助手', message='早安', time='08:00:00')
```

## 原始函数

`office.api.wechat.send_message_by_time`
