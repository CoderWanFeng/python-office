# -*- coding: UTF-8 -*-
'''
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@微信     ：CoderWanFeng : https://mp.weixin.qq.com/s/yFcocJbfS9Hs375NhE8Gbw
@个人网站      ：www.python-office.com
@代码日期    ：2023/7/16 5:38 
@本段代码的视频说明     ：https://mp.weixin.qq.com/s/PjQJ3s4Arr872NDfcr-7YA
'''

# 下载方式：pip install python-office
import office

office.word.merge4docx(input_path=r'D:\程序员晚枫的文件夹\word-in',
                        output_path=r'D:\程序员晚枫的文件夹\word-out')