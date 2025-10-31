# -*- coding: UTF-8 -*-
"""
批量获取文件列表示例

该示例演示如何使用pofile库批量获取指定目录下特定类型的文件列表。

Args:
    path: 要搜索的目录路径
    name: 要搜索的文件名或扩展名

Example:
    >>> import pofile
    >>> files_list = pofile.get_files(path=r'D:\\workplace\\code\\github\\pofile\\tests', name='pdf')
    >>> print(files_list)

Returns:
    list: 包含匹配文件路径的列表

Author:
    程序员晚枫

Project:
    https://www.python-office.com
"""

# pip install pofile
import pofile

files_list = pofile.get_files(path=r'D:\workplace\code\github\pofile\tests', name='pdf')
print(files_list)
