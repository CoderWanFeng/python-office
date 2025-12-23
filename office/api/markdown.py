"""Markdown processing functionality module.

Markdown处理功能模块。

This module provides Markdown file processing capabilities including format conversion.

该模块提供了Markdown文件处理功能，包括格式转换。

Author:
    程序员晚枫

Project:
    https://www.python-office.com
"""

import pomarkdown


def excel2markdown(input_file, output_file=r'./excel2markdown.md', sheet_name=None):
    """Convert Excel file to Markdown format file.
    
    将Excel文件转换为Markdown格式的文件。
    
    This function uses the excel2markdown function in the pomarkdown library to perform conversion.
    It is mainly responsible for defining the input/output paths and worksheet names for conversion.
    
    本函数利用pomarkdown库中的excel2markdown函数执行转换操作。
    主要负责定义转换的输入输出路径及工作表名称。
    
    Args:
        input_file (str): input Excel file path / 输入Excel文件的路径
        output_file (str, optional): output Markdown file path / 输出Markdown文件的路径。Default / 默认: './excel2markdown.md' in current directory / 当前目录下的'excel2markdown.md'
        sheet_name (str, optional): Excel worksheet name to convert / 需要转换的Excel工作表名称。Default / 默认: None (convert all worksheets / 转换所有工作表)
    
    Returns:
        None
    """
    # 调用pomarkdown库中的excel2markdown函数执行Excel到Markdown的转换
    pomarkdown.excel2markdown(input_file, output_file, sheet_name)

