# -*- coding: UTF-8 -*-
"""Merge multiple Excel files into different sheets of one Excel file example.

合并多个Excel到一个Excel的不同sheet中示例。

This example demonstrates how to use python-office library to merge multiple Excel files into different sheets of one Excel file.

该示例演示如何使用python-office库将多个Excel文件合并到一个Excel文件的不同sheet中。

Args:
    dir_path: directory path containing Excel files / 包含Excel文件的目录路径
    output_file: merged Excel filename / 合并后的Excel文件名

Example:
    >>> import office
    >>> office.excel.merge2excel(dir_path=r'../../contributors/bulabean', 
    ...                         output_file='test_merge2excel.xlsx')
"""

import office

office.excel.merge2excel(dir_path=r'../../contributors/bulabean', output_file='test_merge2excel.xlsx', )
