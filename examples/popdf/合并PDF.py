# -*- coding: UTF-8 -*-

# 导入这个库：python-office，简写为office
import office

#一行代码，合并pdf
office.pdf.merge2pdf(one_by_one=['程序员晚枫.pdf', '一键三连.pdf'], output='走起.pdf')

#参数作用：
# one_by_one = 是个列表，里面是2个pdf文件，合并后，a在前面，b在后面
# output = 合并后的pdf名字，不能为空