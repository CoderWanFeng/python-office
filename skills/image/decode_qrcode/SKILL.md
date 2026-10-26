---
name: decode_qrcode
description: 解析二维码图片并提取其中的文本内容。当用户提到二维码识别、扫二维码、读二维码、解码 QR 时使用。
---

# decode_qrcode Skill

> 解析二维码

## 功能描述

解析二维码图片，提取二维码中的内容。

## 所属分类

`office/skills/image/decode_qrcode/`

## 调用方式

```python
from skills.image import decode_qrcode

decode_qrcode(qrcode_path='./qrcode.png')
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `qrcode_path` | str | 是 | - | 二维码图片的路径 |

## 返回值

`str`（二维码中的文本内容；同时也会直接打印输出；未识别到二维码时为空字符串）

## 使用示例

```python
from skills.image import decode_qrcode
decode_qrcode(qrcode_path='./my_qrcode.png')
```

## 原始函数

`office.api.image.decode_qrcode`
