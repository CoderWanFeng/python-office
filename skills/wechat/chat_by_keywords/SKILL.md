---
name: chat_by_keywords
description: 通过微信按关键词列表与指定联系人自动聊天。当用户提到微信自动回复、关键词回复、微信机器人聊天时使用。
---

# chat_by_keywords Skill

> 根据关键词与指定联系人聊天

## 功能描述

通过微信自动化，根据关键词与指定联系人进行自动聊天。

## 所属分类

`office/skills/wechat/chat_by_keywords/`

## 调用方式

```python
from office.skills.wechat import chat_by_keywords

chat_by_keywords(who='文件传输助手', keywords=['你好', '在吗'])
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `who` | str | 是 | - | 进行聊天的联系人名称 |
| `keywords` | list | 是 | - | 触发聊天的关键词列表 |

## 返回值

`None`

## 使用示例

```python
from office.skills.wechat import chat_by_keywords
chat_by_keywords(who='文件传输助手', keywords=['你好', 'hello', 'hi'])
```

## 原始函数

`office.api.wechat.chat_by_keywords`
