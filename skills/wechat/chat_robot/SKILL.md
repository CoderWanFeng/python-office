---
name: chat_robot
description: 通过微信与指定联系人进行智能聊天（基于 AI 回复）。当用户提到微信智能聊天、微信 AI 对话、微信机器人时使用。
---

# chat_robot Skill

> 智能聊天

## 功能描述

通过微信自动化与指定联系人进行智能聊天。

## 所属分类

`office/skills/wechat/chat_robot/`

## 调用方式

```python
from office.skills.wechat import chat_robot

chat_robot(who='程序员晚枫')
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `who` | str | 否 | `'程序员晚枫'` | 指定聊天对象。**可以是备注名称，不支持特殊字符** |

## 返回值

`None`

## 使用示例

```python
from office.skills.wechat import chat_robot
chat_robot(who='文件传输助手')
```

## 原始函数

`office.api.wechat.chat_robot`
