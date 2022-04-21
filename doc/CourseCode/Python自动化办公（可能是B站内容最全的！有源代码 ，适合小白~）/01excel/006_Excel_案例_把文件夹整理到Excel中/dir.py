# -*- coding: utf-8 -*-
# @Time : 2020/8/20 17:42
# @公众号 :Python自动化办公社区 
# @File : dir.py
# @Software: PyCharm
# @Description:

import os
import xlwt

# 目标文件夹
file_path = 'd:/'
# 取出目标文件夹下的文件名
os.listdir(file_path)

new_workbook = xlwt.Workbook()
sheet = new_workbook.add_sheet('new_dir')

n = 0
for i in os.listdir(file_path):
    sheet.write(n,0,i)
    n+=1
new_workbook.save('dir.xls')