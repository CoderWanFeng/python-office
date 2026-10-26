---
name: url2ebook
description: 将网页 URL 转换为电子书。当用户提到网页转电子书、URL 转 ebook、网页转 EPUB、离线阅读网页、pospider 时使用。
---

# url2ebook Skill

> 将指定网页转换为电子书

## 功能描述

抓取网页主要内容，生成可离线阅读的电子书。依赖可选包 `pospider`。

## 所属分类

`office/skills/web/url2ebook/`

## 调用方式

```python
from skills.web import url2ebook

url2ebook(
    url='https://www.python-office.com',
    tile='Python-Office自动化办公指南'
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `url` | str | 是 | - | 要转换的网页地址 |
| `tile` | str | 是 | - | 电子书标题（参数名是 `tile`，不是 `title`） |

## 返回值

`None`（成功后生成电子书文件）

## 使用示例

```python
from skills.web import url2ebook
url2ebook(url='https://www.python-office.com', tile='Python-Office自动化办公指南')
```

## 原始函数

`office.api.web.url2ebook`

## 示例代码

`examples/pospider/网页转电子书.py`
