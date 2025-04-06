# -*- coding: UTF-8 -*-
'''
@作者 ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@读者群     ：http://www.python4office.cn/wechat-group/
@个人网站 ：www.python-office.com
@Date    ：2023/3/25 17:38 
@Description     ：
'''

from poprogress import simple_progress

for i in simple_progress(range(10000000), desc='当前进度'):
    pass
