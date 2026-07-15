---
name: ppt2img
description: 将 PowerPoint 转换为图片，可合并为一张长图或多张图。当用户提到 PPT 转图片、PPT 截图、PPT 转长图、幻灯片截图时使用。
---

# ppt2img Skill

> 将 PPT 转换为图片，可以转为长图

## 功能描述

将 PowerPoint 文件转换为图片，支持合并为一张长图或多张图片。

## 所属分类

`office/skills/ppt/ppt2img/`

## 调用方式

```python
from skills.ppt import ppt2img

ppt2img(
    input_path='./test.pptx',
    output_path='./',
    merge=False
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `input_path` | str | 是 | - | 存放 PPT 的位置。转换单个文件可以写文件路径，转换文件夹可以写文件夹路径 |
| `output_path` | str | 否 | `'./'` | 结果图片的存储位置 |
| `merge` | bool | 否 | `False` | `True` 转为 1 张图片，`False` 转为多张图片 |

## 返回值

`None`

## 使用示例

```python
from skills.ppt import ppt2img
# 转为多张图片
ppt2img(input_path='./presentation.pptx', output_path='./images/')
# 转为一张长图
ppt2img(input_path='./presentation.pptx', merge=True)
```

## 原始函数

`office.api.ppt.ppt2img`
