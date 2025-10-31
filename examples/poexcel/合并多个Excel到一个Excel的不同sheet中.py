# -*- coding: UTF-8 -*-
"""
合并多个Excel到一个Excel的不同sheet中示例

该示例演示如何使用python-office库将多个Excel文件合并到一个Excel文件的不同sheet中。

Args:
    dir_path: 包含Excel文件的目录路径
    output_file: 合并后的Excel文件名

Example:
    >>> import office
    >>> office.excel.merge2excel(dir_path=r'../../contributors/bulabean', 
    ...                         output_file='test_merge2excel.xlsx')
"""

import office

office.excel.merge2excel(dir_path=r'../../contributors/bulabean', output_file='test_merge2excel.xlsx', )
