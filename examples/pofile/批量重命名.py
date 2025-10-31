# -*- coding: UTF-8 -*-
"""
批量重命名文件示例

该示例演示如何使用python-office库批量重命名文件。

Args:
    path: 包含要重命名文件的目录路径
    del_content: 要从文件名中删除的内容

Example:
    >>> import office
    >>> office.file.replace4filename(path=r'./test_files/replace4filename', 
    ...                             del_content='程序员晚枫')
    
    >>> import pofile
    >>> pofile.replace4filename(path=r'./test_files/replace4filename', 
    ...                         del_content='程序员晚枫')
"""

import office

office.file.replace4filename(path=r'./test_files/replace4filename', del_content='程序员晚枫')

import pofile

pofile.replace4filename(path=r'./test_files/replace4filename', del_content='程序员晚枫')
