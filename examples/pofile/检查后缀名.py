# -*- coding: UTF-8 -*-
'''
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：CoderWanFeng
@读者群     ：http://www.python4office.cn/wechat-group/
@学习网站      ：https://www.python-office.com
@代码日期    ：2023/8/9 22:27 
@本段代码的视频说明     ：
'''

import pofile

is_valid = pofile.check_suffix(file_name='程序员晚枫.pdf',suffix_list=['pdf'])
print(is_valid)
