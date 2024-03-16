# -*- coding: UTF-8 -*-
'''
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：CoderWanFeng
@读者群     ：http://www.python4office.cn/wechat-group/
@学习网站      ：www.python-office.com
@代码日期    ：2023/7/15 0:35 
@本段代码的视频说明     ：
'''

# pip install python-office
import office

office.word.docx2pdf(
    path=r'D:\workplace\code\github\python-office\demo\poword\test_files',
    output_path=r'D:\workplace\code\github\python-office\demo\poword\test_files\docx2pdf')
