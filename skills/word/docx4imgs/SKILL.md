---
name: docx4imgs
description: 从 Word 文档中提取所有图片并保存到指定目录。当用户提到 Word 提取图片、docx 抠图、Word 取图时使用。
---

# docx4imgs Skill

> 从 Word 里提取图片

## 功能描述

从 Word 文档中提取所有图片，并保存到指定目录。会自动根据 word 名称在指定文件夹下生成一个子目录。

## 所属分类

`office/skills/word/docx4imgs/`

## 调用方式

```python
from office.skills.word import docx4imgs

docx4imgs(
    word_path='./test.docx',
    img_path='./images/'
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `word_path` | str | 是 | - | Word 文档的路径 |
| `img_path` | str | 是 | - | 提取图片的存储位置。会根据 word 名称在指定文件夹下自动生成一个子目录 |

## 返回值

`None`

## 使用示例

```python
from office.skills.word import docx4imgs
docx4imgs(word_path='./document.docx', img_path='./extracted_images/')
```

## 原始函数

`office.api.word.docx4imgs`
