# -*- coding: UTF-8 -*-
"""
统计Excel打印页数示例

该示例演示如何使用poexcel库统计Excel文件的打印页数。

Args:
    folder_path: 包含Excel文件的目录路径

Example:
    >>> import poexcel
    >>> folder_path = r"D:\\程序员晚枫的文件夹\\code\\github\\poexcel\\dev"
    >>> poexcel.count4page(folder_path)

Returns:
    dict: 包含每个Excel文件打印页数的字典

Author:
    程序员晚枫

Project:
    https://www.python-office.com
"""

import poexcel

# 存放Excel文件的目录
folder_path = r"D:\程序员晚枫的文件夹\code\github\poexcel\dev"

poexcel.count4page(folder_path)
