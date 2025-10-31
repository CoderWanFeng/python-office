# -*- coding: UTF-8 -*-
"""PDF加密功能示例。

该示例演示如何使用python-office库对PDF文件进行加密保护。

Args:
    path (str): 要加密的PDF文件路径
    password (str): 设置的加密密码

Example:
    >>> import office
    >>> office.pdf.encrypt4pdf(
    ...     path='./test_files/encrypt4pdf/程序员晚枫（作品合集）.pdf',
    ...     password='你想添加的密码'
    ... )

Note:
    - 加密后的PDF文件需要输入密码才能打开
    - 密码不能为空，建议设置强密码
    - 支持对单个PDF文件进行加密保护
"""

# 导入这个库
import office

# PDF加密：填写你的文件位置和密码
office.pdf.encrypt4pdf(path='./test_files/encrypt4pdf/程序员晚枫（作品合集）.pdf', password='你想添加的密码')