# -*- coding: UTF-8 -*-
"""PDF encryption functionality example.

PDF加密功能示例。

This example demonstrates how to use python-office library to encrypt PDF files for protection.

该示例演示如何使用python-office库对PDF文件进行加密保护。

Args:
    path (str): path to PDF file to encrypt / 要加密的PDF文件路径
    password (str): encryption password to set / 设置的加密密码

Example:
    >>> import office
    >>> office.pdf.encrypt4pdf(
    ...     path='./test_files/encrypt4pdf/程序员晚枫（作品合集）.pdf',
    ...     password='你想添加的密码'
    ... )

Note:
    - Encrypted PDF files require password input to open / 加密后的PDF文件需要输入密码才能打开
    - Password cannot be empty, strong password recommended / 密码不能为空，建议设置强密码
    - Supports encryption protection for single PDF file / 支持对单个PDF文件进行加密保护
"""

# Import this library / 导入这个库
import office

# PDF encryption: fill in your file location and password / PDF加密：填写你的文件位置和密码
office.pdf.encrypt4pdf(path='./test_files/encrypt4pdf/程序员晚枫（作品合集）.pdf', password='你想添加的密码')