---
name: transtools
description: 将内容从一种语言翻译为另一种语言。当用户提到翻译、中英互译、多语言翻译、自动翻译时使用。
---

# transtools Skill

> 将内容从一种语言翻译为另一种语言

## 功能描述

使用翻译引擎将内容从源语言翻译为目标语言。

## 所属分类

`office/skills/tools/transtools/`

## 调用方式

```python
from office.skills.tools import transtools

result = transtools(
    to_lang='en',
    content='你好世界',
    from_lang='zh'
)
print(result)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `to_lang` | str | 是 | - | 目标语言 |
| `content` | str | 是 | - | 待翻译的内容 |
| `from_lang` | str | 否 | `'zh'` | 源语言（默认中文） |

## 返回值

`str`：翻译后的结果

## 使用示例

```python
from office.skills.tools import transtools
result = transtools(to_lang='en', content='你好，世界！')
print(result)  # Hello, world!
```

## 原始函数

`office.api.tools.transtools`
