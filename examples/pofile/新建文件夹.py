# -*- coding: UTF-8 -*-
"""新建文件夹功能示例。

该示例演示如何使用pofile库创建新文件夹。

Args:
    path (str): 要创建的文件夹路径

Example:
    >>> import pofile
    >>> path = r'd://程序员晚枫-新文件夹'
    >>> pofile.mkdir(path)

Note:
    该功能会创建指定路径的文件夹，如果路径已存在则不会重复创建。
"""

import pofile

path = r'd://程序员晚枫-新文件夹'
pofile.mkdir((path))
