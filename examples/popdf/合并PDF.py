# -*- coding: UTF-8 -*-
"""
合并PDF文件示例

该示例演示如何使用python-office库合并多个PDF文件。

Args:
    one_by_one: PDF文件列表，合并后按列表顺序排列
    output: 合并后的PDF文件名

Example:
    >>> import office
    >>> office.pdf.merge2pdf(one_by_one=['程序员晚枫.pdf', '一键三连.pdf'], 
    ...                     output='走起.pdf')

Note:
    one_by_one参数是一个列表，包含要合并的PDF文件，合并后按列表顺序排列
    output参数是合并后的PDF文件名，不能为空
"""

# 导入这个库：python-office，简写为office
import office

#一行代码，合并pdf
office.pdf.merge2pdf(one_by_one=['程序员晚枫.pdf', '一键三连.pdf'], output='走起.pdf')