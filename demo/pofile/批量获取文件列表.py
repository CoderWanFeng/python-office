# -*- coding: UTF-8 -*-
'''
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@微信     ：CoderWanFeng : https://mp.weixin.qq.com/s/yFcocJbfS9Hs375NhE8Gbw
@个人网站      ：www.python-office.com
@代码日期    ：2023/7/20 0:05 
@本段代码的视频说明     ：https://www.bilibili.com/video/BV1ua4y1M7ya/
'''

# pip install pofile
import pofile

files_list = pofile.get_files(path=r'D:\workplace\code\github\pofile\tests', name='pdf')
print(files_list)
