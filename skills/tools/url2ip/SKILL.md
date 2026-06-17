---
name: url2ip
description: 将 URL 解析为对应的 IP 地址。当用户提到 URL 转 IP、域名解析 IP、查 IP 时使用。
---

# url2ip Skill

> 将 URL 转换为 IP 地址

## 功能描述

解析给定的 URL 并返回对应的 IP 地址。

## 所属分类

`office/skills/tools/url2ip/`

## 调用方式

```python
from office.skills.tools import url2ip

ip = url2ip(url='https://www.python-office.com')
print(ip)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `url` | str | 是 | - | 需要转换的 URL 字符串 |

## 返回值

`str`：解析得到的 IP 地址字符串

## 使用示例

```python
from office.skills.tools import url2ip
ip = url2ip(url='https://www.baidu.com')
print(f"百度 IP: {ip}")
```

## 原始函数

`office.api.tools.url2ip`
