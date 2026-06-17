---
name: ppt2pdf
description: 将 PowerPoint 文件转换为 PDF。当用户提到 PPT 转 PDF、幻灯片转 PDF、PPTX 转 PDF 时使用。
---

# ppt2pdf Skill

> 将 PPT 转换为 PDF

## 功能描述

将 PowerPoint 文件转换为 PDF 格式。

## 所属分类

`office/skills/ppt/ppt2pdf/`

## 调用方式

```python
from office.skills.ppt import ppt2pdf

ppt2pdf(
    path='./test.pptx',
    output_path='./'
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `path` | str | 是 | - | PPT 文件路径 |
| `output_path` | str | 否 | `'./'` | 输出 PDF 文件路径 |

## 返回值

`None`

## 使用示例

```python
from office.skills.ppt import ppt2pdf
ppt2pdf(path='./presentation.pptx', output_path='./output/')
```

## 原始函数

`office.api.ppt.ppt2pdf`
