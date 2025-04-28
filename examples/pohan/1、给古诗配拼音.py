# -*- coding: UTF-8 -*-


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
