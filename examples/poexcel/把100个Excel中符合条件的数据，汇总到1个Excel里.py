# -*- coding: UTF-8 -*-
"""
从多个Excel中查询并汇总数据示例

该示例演示如何使用poexcel库从多个Excel文件中查询符合条件的数据并汇总到一个Excel中。

Args:
    query_content: 要查询的内容
    query_path: 包含Excel文件的目录路径
    output_path: 输出查询结果Excel的位置（可选，默认为query_path）
    output_name: 输出文件名（可选，默认为query4excel.xlsx）

Example:
    >>> import poexcel
    >>> poexcel.query4excel(query_content='程序员晚枫',
    ...                     query_path=r'必填，放Excel文件的位置')
"""

import poexcel

poexcel.query4excel(query_content='程序员晚枫',
                    query_path=r'必填，放Excel文件的位置')
