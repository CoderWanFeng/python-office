# -*- coding: utf-8 -*-
# @Time : 2020/8/18 18:35
# @公众号 :Python自动化办公社区 
# @File : read.py
# @Software: PyCharm
# @Description:

import xlrd

xlsx = xlrd.open_workbook('7月下旬入库表.xlsx')

sheet = xlsx.sheet_by_index(0)
# 通过sheet名查找：xlsx.sheet_by_name("7月下旬入库表")
# 通过索引查找：xlsx.sheet_by_index(3)
# print(table.cell_value(0, 0))

# print(sheet.cell_value(1, 2))
# print(sheet.cell(0, 0).value)
# print(sheet.row(0)[0].value)


# for i in range(0, xlsx.nsheets):
#     sheet = xlsx.sheet_by_index(i)
#     print(sheet.name)
    # print(sheet.cell_value(0, 0))
#
# # 获取所有sheet名字：xlsx.sheet_names()
# # 获取sheet数量：xlsx.nsheets
#
for i in xlsx.sheet_names():
    print(i)
    # table = xlsx.sheet_by_name(i)
    # print(table.cell_value(3, 3))