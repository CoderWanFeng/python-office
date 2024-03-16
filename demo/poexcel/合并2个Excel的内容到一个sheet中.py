# -*- coding: UTF-8 -*-
'''
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：CoderWanFeng
@读者群     ：http://www.python4office.cn/wechat-group/
@学习网站      ：www.python-office.com
@代码日期    ：2023/8/6 20:17 
@本段代码的视频说明     ：
'''
import poexcel

poexcel.merge2sheet(dir_path=r'D:\workplace\code\github\python-office\tests\test_files\excel\merge2sheet',
                    output_sheet_name=r'platform', output_excel_name=r'./output/merge2sheet')
