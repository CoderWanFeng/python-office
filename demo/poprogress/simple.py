# -*- coding: UTF-8 -*-
'''
@Author  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@WeChat     ：CoderWanFeng
@Blog      ：www.python-office.com
@Date    ：2023/3/25 17:38 
@Description     ：
'''

from poprogress import simple_progress

for i in simple_progress(range(10000000), desc='当前进度'):
    pass
