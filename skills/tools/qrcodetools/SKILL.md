---
name: qrcodetools
description: 根据 URL 生成对应的二维码图片。当用户提到生成二维码、做二维码、QR 码、生二维码时使用。
---

# qrcodetools Skill

> 生成二维码图片

## 功能描述

根据给定的 URL 生成对应的二维码图片。

## 所属分类

`office/skills/tools/qrcodetools/`

## 调用方式

```python
from skills.tools import qrcodetools

qrcodetools(
    url='https://www.python-office.com',
    output='./qrcode.png'
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `url` | str | 是 | - | 用于生成二维码的 URL 地址 |
| `output` | str | 否 | `'./qrcode_img.png'` | 生成的二维码图片保存路径 |

## 返回值

`None`

## 使用示例

```python
from skills.tools import qrcodetools
qrcodetools(url='https://www.python-office.com', output='./my_qrcode.png')
```

## 原始函数

`office.api.tools.qrcodetools`
