# -*- coding: UTF-8 -*-
"""
自动整理文件夹示例

该示例演示如何使用python-office库自动整理文件夹中的文件。

Args:
    path: 要整理的文件夹路径

Example:
    >>> import office
    >>> path = 'd://程序员晚枫需要整理的文件夹//'
    >>> office.file.group_by_name(path)

Author:
    程序员晚枫

Project:
    https://www.python-office.com
"""

import office

path = 'd://程序员晚枫需要整理的文件夹//'
office.file.group_by_name(path)