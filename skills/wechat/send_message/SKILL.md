---
name: send_message
description: 通过微信自动化向指定联系人发送消息。当用户提到微信发消息、微信机器人、给某人发微信时使用。
---

# send_message Skill

> 发送消息给指定联系人

## 功能描述

通过微信自动化，向指定联系人发送一条消息。

## 所属分类

`office/skills/wechat/send_message/`

## 调用方式

```python
from office.skills.wechat import send_message

send_message(who='文件传输助手', message='Hello, World!')
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `who` | str | 是 | - | 接收消息的联系人名称 |
| `message` | str | 是 | - | 要发送的消息内容 |

## 返回值

`None`

## 使用示例

```python
from office.skills.wechat import send_message
send_message(who='文件传输助手', message='Hello, World!')
```

## 原始函数

`office.api.wechat.send_message`
