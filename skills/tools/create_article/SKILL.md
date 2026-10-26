---
name: create_article
description: 根据给定主题自动生成指定行数的文章。当用户提到 AI 写作、自动写文章、生成稿子、AI 写稿时使用。
---

# create_article Skill

> 创建文章

## 功能描述

根据给定的主题，自动创建指定行数的文章。

## 所属分类

`office/skills/tools/create_article/`

## 调用方式

```python
from skills.tools import create_article

create_article(
    theme='人工智能的发展',
    line_num=300
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `theme` | str | 是 | - | 文章的主题 |
| `line_num` | int | 否 | `200` | 文章的行数 |

## 返回值

`None`

## 使用示例

```python
from skills.tools import create_article
create_article(theme='Python 自动化办公', line_num=500)
```

## 原始函数

`office.api.tools.create_article`
