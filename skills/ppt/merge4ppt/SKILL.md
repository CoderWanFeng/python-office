---
name: merge4ppt
description: 将多个 PowerPoint 文件合并为一个 PPT。当用户提到 PPT 合并、合并幻灯片、合并 PPTX 时使用。
---

# merge4ppt Skill

> 合并多个 PPT 文件

## 功能描述

将多个 PPT 文件合并为一个 PPT 文件。

## 所属分类

`office/skills/ppt/merge4ppt/`

## 调用方式

```python
from office.skills.ppt import merge4ppt

merge4ppt(
    input_path='./ppt_files',
    output_path='./',
    output_name='merged.pptx'
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `input_path` | str | 是 | - | 输入 PPT 文件路径 |
| `output_path` | str | 否 | `'./'` | 输出 PPT 文件路径 |
| `output_name` | str | 否 | `'merge4ppt.pptx'` | 合并后的 PPT 文件名 |

## 返回值

`None`

## 使用示例

```python
from office.skills.ppt import merge4ppt
merge4ppt(input_path='./ppt_files', output_name='all_merged.pptx')
```

## 原始函数

`office.api.ppt.merge4ppt`
