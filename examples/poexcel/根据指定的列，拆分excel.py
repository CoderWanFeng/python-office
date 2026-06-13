# -*- coding: UTF-8 -*-
"""
根据指定的列拆分Excel文件示例

该示例演示如何使用poexcel库根据指定的列拆分Excel文件。

Args:
    filepath: 要拆分的Excel文件路径
    column: 要拆分的列索引（从1开始）
    worksheet_name: 工作表名称

Example:
    >>> import poexcel
    >>> poexcel.split_excel_by_column(
    ...     filepath=r'D:\\workplace\\code\\github\\python-office\\demo\\poexcel\\excel\\split_excel_by_column.xlsx',
    ...     column=1,
    ...     worksheet_name='platform')

Author:
    程序员晚枫

Project:
    https://www.python-office.com
"""

import poexcel

poexcel.split_excel_by_column(
    filepath=r'D:\workplace\code\github\python-office\demo\poexcel\excel\split_excel_by_column.xlsx',
    column=1,
    worksheet_name='platform')

