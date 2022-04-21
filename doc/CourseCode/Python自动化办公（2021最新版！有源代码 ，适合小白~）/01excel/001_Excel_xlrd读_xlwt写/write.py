# -*- coding: utf-8 -*-
# @公众号 :Python自动化办公社区 
# @File : write.py
# @Software: PyCharm
# @Description:

import xlwt
#安装：pip install xlwt
# 打开terminal

# 新建工作簿
new_workbook = xlwt.Workbook()
# 新建sheet
worksheet = new_workbook.add_sheet('new_test')
# 新建单元格，并写入内容-行列
worksheet.write(1, 2, 'test')
# 保存
new_workbook.save('test.xls')