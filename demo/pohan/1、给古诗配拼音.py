# -*- coding: UTF-8 -*-
'''
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@微信     ：CoderWanFeng : https://mp.weixin.qq.com/s/B1V6KeXc7IOEB8DgXLWv3g
@个人网站      ：www.python-office.com
@代码日期    ：2023/7/30 2:59 
@本段代码的视频说明     ：
'''

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
