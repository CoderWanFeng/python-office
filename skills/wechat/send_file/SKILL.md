---
name: send_file
description: 通过微信向指定联系人发送文件。当用户提到微信发文件、微信传文件、微信机器人传文件时使用。
---

# send_file Skill

> 发送文件给指定联系人

## 功能描述

通过微信自动化，向指定联系人发送一个文件。

## 所属分类

`office/skills/wechat/send_file/`

## 调用方式

```python
from skills.wechat import send_file

send_file(who='文件传输助手', file='./test.txt')
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `who` | str | 是 | - | 接收文件的联系人名称 |
| `file` | str | 是 | - | 要发送的文件路径 |

## 返回值

`None`

## 使用示例

```python
from skills.wechat import send_file
send_file(who='文件传输助手', file='./report.pdf')
```

## 原始函数

`office.api.wechat.send_file`
