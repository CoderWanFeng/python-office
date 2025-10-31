# -*- coding: UTF-8 -*-
"""
合并多个Excel文件内容到一个sheet中示例

该示例演示如何使用poexcel库将多个Excel文件的内容合并到一个sheet中。

Args:
    dir_path: 包含要合并Excel文件的目录路径
    output_sheet_name: 输出sheet的名称
    output_excel_name: 输出Excel文件的名称

Example:
    >>> import poexcel
    >>> poexcel.merge2sheet(dir_path=r'D:\\workplace\\code\\github\\python-office\\tests\\test_files\\excel\\merge2sheet',
    ...                     output_sheet_name=r'platform', output_excel_name=r'./output/merge2sheet')

Author:
    程序员晚枫

Project:
    https://www.python-office.com
"""

import poexcel

poexcel.merge2sheet(dir_path=r'D:\workplace\code\github\python-office\tests\test_files\excel\merge2sheet',
                    output_sheet_name=r'platform', output_excel_name=r'./output/merge2sheet')
