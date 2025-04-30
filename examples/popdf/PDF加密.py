# -*- coding: UTF-8 -*-


# 导入这个库
import office

# PDF加密：填写你的文件位置和密码
office.pdf.encrypt4pdf(path='./test_files/encrypt4pdf/程序员晚枫（作品合集）.pdf', password='你想添加的密码')

# 参数说明：
# path：你的文件位置，例如：D:\work\参考.pdf
# password：你的密码，可以随意设置，不能为空