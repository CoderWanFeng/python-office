# -*- coding: UTF-8 -*-
"""Convert Word to PDF example.

将Word转换为PDF示例。

This example demonstrates how to use python-office library to convert Word documents to PDF format.

该示例演示如何使用python-office库将Word文档转换为PDF格式。

Example:
    >>> import office
    >>> office.word.docx2pdf(
    ...     path='your_word_file_path',
    ...     output_path='your_output_path'
    ... )

Note:
    - Supports batch conversion of Word files in a folder / 支持批量转换文件夹中的Word文件
    - Output path will be created automatically if not exists / 输出路径不存在时会自动创建
"""


# pip install python-office
import office

office.word.docx2pdf(
    path=r'D:\workplace\code\github\python-office\demo\poword\test_files',
    output_path=r'D:\workplace\code\github\python-office\demo\poword\test_files\docx2pdf')
