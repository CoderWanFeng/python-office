# -*- coding: UTF-8 -*-
"""
批量模拟数据生成Excel示例

该示例演示如何使用poexcel库批量生成模拟数据并保存到Excel文件。

Args:
    columns: 要生成的列名列表
    rows: 要生成的行数

Example:
    >>> import poexcel
    >>> poexcel.fake2excel(columns=['name', 'text'], rows=20)

Author:
    程序员晚枫

Project:
    https://www.python-office.com
"""

import poexcel

poexcel.fake2excel(columns=['name', 'text'], rows=20)
