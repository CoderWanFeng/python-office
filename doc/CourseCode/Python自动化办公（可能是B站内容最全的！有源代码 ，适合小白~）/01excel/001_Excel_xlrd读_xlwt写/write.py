# -*- coding: utf-8 -*-
# @Time : 2020/8/18 19:04
# @公众号 :Python自动化办公社区 
# @File : write.py
# @Software: PyCharm
# @Description:

import xlwt
# 新建工作簿
new_workbook = xlwt.Workbook()
# 新建sheet
worksheet = new_workbook.add_sheet('new_test')
# 新建单元格，并写入内容
worksheet.write(0, 0, 'test')
# 保存
new_workbook.save('test.xls')