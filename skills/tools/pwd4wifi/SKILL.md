---
name: pwd4wifi
description: 生成 WiFi 密码字典列表。当用户提到 WiFi 密码字典、WiFi 破解字典、密码字典时使用。
---

# pwd4wifi Skill

> 生成 WiFi 密码列表

## 功能描述

生成指定长度的 WiFi 密码列表，可用于 WiFi 密码字典。

## 所属分类

`office/skills/tools/pwd4wifi/`

## 调用方式

```python
from skills.tools import pwd4wifi

pwd4wifi(len_pwd=8, pwd_list=[])
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `len_pwd` | int | 否 | `8` | 密码长度 |
| `pwd_list` | list | 否 | `[]` | 密码列表 |

## 返回值

`None`

## 使用示例

```python
from skills.tools import pwd4wifi
pwd4wifi(len_pwd=10)
```

## 原始函数

`office.api.tools.pwd4wifi`
