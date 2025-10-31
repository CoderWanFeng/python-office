# -*- coding: UTF-8 -*-
"""
根据内容查找文件示例

该示例演示如何使用search4file库根据文件内容查找文件。

Args:
    path: 要搜索的文件夹路径
    content: 要查找的文件内容

Example:
    >>> import search4file
    >>> search4file.search_by_content(r'd:\\程序员晚枫的文件夹', 
    ...                              content="所有平台都叫-程序员晚枫")
"""

# 导入这个库：python-office，简写为office
import search4file

# 1行代码，实现
search4file.search_by_content(r'你的文件夹，例如：d:\\程序员晚枫的文件夹' , content="你需要查找的文件里面的内容，例如：所有平台都叫-程序员晚枫")