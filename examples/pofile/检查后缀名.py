# -*- coding: UTF-8 -*-
"""
检查文件后缀名示例

该示例演示如何使用pofile库检查文件后缀名是否在允许的列表中。

Args:
    file_name: 要检查的文件名
    suffix_list: 允许的后缀名列表

Example:
    >>> import pofile
    >>> is_valid = pofile.check_suffix(file_name='程序员晚枫.pdf', suffix_list=['pdf'])
    >>> print(is_valid)

Returns:
    bool: 如果文件后缀名在允许列表中返回True，否则返回False

Author:
    程序员晚枫

Project:
    https://www.python-office.com
"""

import pofile

is_valid = pofile.check_suffix(file_name='程序员晚枫.pdf',suffix_list=['pdf'])
print(is_valid)
