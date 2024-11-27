# -*- coding: UTF-8 -*-
'''
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：CoderWanFeng
@读者群     ：http://www.python4office.cn/wechat-group/
@学习网站      ：https://www.python-office.com
@代码日期    ：2023/7/15 0:40 
@本段代码的视频说明     ：
'''

# pip install python-office
import office # 导入第三方库

office.pdf.pdf2docx(file_path=r'D:\pdf\程序员晚枫.pdf',
                    output_path=r'D:\download')


# 上面这种是Windows用户
# 尊贵的Mac和Linux用户
# pip install popdf
# import popdf
# popdf.pdf2docx(file_path=r'D:\workplace\code\github\python-office\demo\popdf\test_files\pdf2docx\程序员晚枫.pdf',
#                output_path=r'./test_files/pdf2docx/output')
