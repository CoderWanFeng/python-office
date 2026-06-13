# -*- coding: UTF-8 -*-
"""PDF to Word conversion functionality example.

PDF转Word功能示例。

This example demonstrates how to use python-office library to convert PDF files to Word documents.

该示例演示如何使用python-office库将PDF文件转换为Word文档。

Args:
    file_path (str): input PDF file path / 输入的PDF文件路径
    output_path (str): output Word document save path / 输出的Word文档保存路径

Example:
    >>> import office
    >>> office.pdf.pdf2docx(
    ...     file_path=r'D:\pdf\程序员晚枫.pdf',
    ...     output_path=r'D:\download'
    ... )

Note:
    - Windows users: use python-office library / Windows用户：使用python-office库
    - Mac/Linux users: use popdf library (see commented example) / Mac/Linux用户：使用popdf库（注释中的示例）
    - This function supports converting PDF files to editable Word document format / 该功能支持将PDF文件转换为可编辑的Word文档格式。
"""

# pip install python-office
import office # Import third-party library / 导入第三方库

office.pdf.pdf2docx(file_path=r'D:\pdf\程序员晚枫.pdf',
                    output_path=r'D:\download')


# Above is for Windows users / 上面这种是Windows用户
# Honorable Mac and Linux users / 尊贵的Mac和Linux用户
# pip install popdf
# import popdf
# popdf.pdf2docx(file_path=r'D:\workplace\code\github\python-office\examples\popdf\test_files\pdf2docx\程序员晚枫.pdf',
#                output_path=r'./test_files/pdf2docx/output')
