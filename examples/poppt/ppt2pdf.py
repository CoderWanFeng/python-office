# -*- coding: UTF-8 -*-
"""Convert PowerPoint to PDF example.

将PowerPoint转换为PDF示例。

This example demonstrates how to use python-office library to convert PowerPoint files to PDF format.

该示例演示如何使用python-office库将PowerPoint文件转换为PDF格式。

Args:
    path (str): PowerPoint file path / PowerPoint文件路径
    output_path (str): output PDF save path / 输出PDF保存路径

Example:
    >>> import office
    >>> office.ppt.ppt2pdf(
    ...     path=r'./test_files/ppt2pdf/程序员晚枫.pptx',
    ...     output_path=r'./test_files/ppt2pdf/output'
    ... )

Note:
    - Supports batch conversion / 支持批量转换
    - Output directory will be created automatically / 输出目录会自动创建
"""

# Import library: python-office, abbreviated as: office / 导入库：python-office，简写为：office
import office

# Fill in your ppt directory / 填入你的ppt目录
office.ppt.ppt2pdf(path=r'./test_files/ppt2pdf/程序员晚枫.pptx',
                   output_path=r'./test_files/ppt2pdf/output')
