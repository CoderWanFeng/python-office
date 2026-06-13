# -*- coding: UTF-8 -*-
"""Excel转PDF功能示例。

该示例演示如何使用python-office库将Excel文件转换为PDF格式。

Args:
    excel_path (str): 输入的Excel文件路径
    pdf_path (str): 输出的PDF文件路径

Example:
    >>> import office
    >>> office.excel.excel2pdf(
    ...     excel_path=r"D:\test\程序员晚枫.xlsx",
    ...     pdf_path=r"D:\test\程序员晚枫.pdf"
    ... )

Note:
    该功能需要安装python-office库，支持将Excel文件转换为PDF格式。
"""

import office

office.excel.excel2pdf(excel_path=r"D:\test\程序员晚枫.xlsx",
                       pdf_path=r"D:\test\程序员晚枫.pdf")
