# -*- coding: UTF-8 -*-
"""
给古诗配拼音示例

该示例演示如何使用pohan库给中文文本添加拼音。

Args:
    text: 要添加拼音的中文文本
    style: 拼音样式（NORMAL: 不带声调, TONE: 带声调, TONE3: 带数字声调）

Example:
    >>> import pohan
    >>> from pohan.pinyin.pinyin import Style
    >>> line1 = "床前明月光"
    >>> 
    >>> # 不带声调的
    >>> pinyin_list = pohan.pinyin.han2pinyin(line1, style=Style.NORMAL)
    >>> print(f'不带声调的结果：{pinyin_list}')
    >>> 
    >>> # 带声调的
    >>> pinyin_list = pohan.pinyin.han2pinyin(line1, style=Style.TONE)
    >>> print(f'带声调的结果：{pinyin_list}')
    >>> 
    >>> # 带数字声调的
    >>> pinyin_list = pohan.pinyin.han2pinyin(line1, style=Style.TONE3)
    >>> print(f'带数字声调的结果：{pinyin_list}')
"""

# pip install pohan
import pohan
from pohan.pinyin.pinyin import Style

line1 = "床前明月光"

# 不带声调的
pinyin_list = pohan.pinyin.han2pinyin(line1, style=Style.NORMAL)
print(f'不带声调的结果：{pinyin_list}')

# 带声调的
pinyin_list = pohan.pinyin.han2pinyin(line1, style=Style.TONE)
print(f'带声调的结果：{pinyin_list}')

# 带数字声调的
pinyin_list = pohan.pinyin.han2pinyin(line1, style=Style.TONE3)
print(f'带数字声调的结果：{pinyin_list}')
