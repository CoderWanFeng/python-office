---
name: change_label_in_xml
description: 批量修改指定目录下所有 XML 标注文件中的标签名（old_label 替换为 new_label）。当用户提到改 XML 标签、修改标注、批量改 label 时使用。
---

# change_label_in_xml Skill

> 修改 XML 标注文件中的 label

## 功能描述

批量修改指定目录下所有 XML 标注文件中的标签名（old_label 替换为 new_label）。

## 所属分类

`office/skills/ruiming/change_label_in_xml/`

## 调用方式

```python
from skills.ruiming import change_label_in_xml

change_label_in_xml(
    dir_path='./dataset',
    old_label='cat',
    new_label='dog'
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `dir_path` | str | 是 | - | 图片及标注文件的存放路径 |
| `old_label` | str | 是 | - | 需要修改的标签 |
| `new_label` | str | 是 | - | 修改后的标签 |

## 返回值

`None`

## 使用示例

```python
from skills.ruiming import change_label_in_xml
change_label_in_xml(dir_path='./annotations', old_label='person', new_label='human')
```

## 原始函数

`office.api.testApi.ruiming.change_label_in_xml`
