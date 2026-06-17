---
name: passwordtools
description: 生成指定长度的随机密码。当用户提到生成密码、随机密码、强密码、密码生成器时使用。
---

# passwordtools Skill

> 生成一个指定长度的密码

## 功能描述

生成指定长度的随机密码。

## 所属分类

`office/skills/tools/passwordtools/`

## 调用方式

```python
from office.skills.tools import passwordtools

pwd = passwordtools(len=12)
print(pwd)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `len` | int | 否 | `8` | 密码长度 |

## 返回值

`str`：生成的密码

## 使用示例

```python
from office.skills.tools import passwordtools
pwd = passwordtools(len=16)
print(f"生成的密码: {pwd}")
```

## 原始函数

`office.api.tools.passwordtools`
