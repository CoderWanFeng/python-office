# -*- coding: utf-8 -*-
# @Time : 2020/8/19 19:03
# @公众号 :Python自动化办公社区 
# @File : 0701SUM.py
# @Software: PyCharm
# @Description:

import xlrd
import xlwt

# 读取excel文件
xlsx = xlrd.open_workbook('三年二班（各科成绩单）.xls')
# 选择指定sheet
sheet = xlsx.sheet_by_index(0)
# 依次单元格数据，并统计总分
all_data = []
# 统计共有多少学生，并去重
num_set = set()
for row_i in range(1, sheet.nrows):
    num = sheet.cell_value(row_i, 0)
    name = sheet.cell_value(row_i, 1)
    grade = sheet.cell_value(row_i, 3)

    student = {
        'num': num,
        'name': name,
        'grade': grade,
    }
    all_data.append(student)
    num_set.add(num)
# print(all_data)
# print(len(all_data))
# print(len(num_set))

# 计算总分
sum_list = []
for num in num_set:
    name = ''
    sum = 0
    for student in all_data:
        # print(student['num'])
        # print(num)
        if num == student['num']:
            sum += student['grade']
            name = student['name']
    sum_stu = {
        'num': num,
        'name': name,
        'sum': sum
    }
    sum_list.append(sum_stu)
print(sum_list)

# 写入新的excel

# 新建工作簿
new_workbook = xlwt.Workbook()
# 新建sheet
worksheet = new_workbook.add_sheet('2班')
# 新建单元格，并写入内容
# 写入第一列的内容
worksheet.write(0, 0, '学号')
worksheet.write(0, 1, '姓名')
worksheet.write(0, 2, '总分')
# 自动写入后面的内容
for row in range(0,len(sum_list)):
    worksheet.write(row+1,0,sum_list[row]['num'])
    worksheet.write(row+1,1,sum_list[row]['name'])
    worksheet.write(row+1,2,sum_list[row]['sum'])
# 保存
new_workbook.save('2班学生总分.xls')
