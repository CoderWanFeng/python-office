---
name: txt2wordcloud
description: 根据文本文件生成词云图片，支持自定义背景色。当用户提到词云、生成词云、文字云、词频可视化时使用。
---

# txt2wordcloud Skill

> 根据指定的文本文件生成词云图像

## 功能描述

根据指定的文本文件内容，生成词云图片。

## 所属分类

`office/skills/image/txt2wordcloud/`

## 调用方式

```python
from office.skills.image import txt2wordcloud

txt2wordcloud(
    filename='./text.txt',
    color='white',
    result_file='wordcloud.png'
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `filename` | str | 是 | - | 文本文件的路径 |
| `color` | str | 否 | `"white"` | 词云的背景颜色 |
| `result_file` | str | 否 | `"your_wordcloud.png"` | 生成的词云图像文件名 |

## 返回值

`None`

## 使用示例

```python
from office.skills.image import txt2wordcloud
txt2wordcloud(filename='./article.txt', result_file='./my_wordcloud.png')
```

## 原始函数

`office.api.image.txt2wordcloud`
