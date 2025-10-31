# -*- coding: UTF-8 -*-
"""PDF转Word功能示例。

该示例演示如何使用python-office库将PDF文件转换为Word文档。

Args:
    file_path (str): 输入的PDF文件路径
    output_path (str): 输出的Word文档保存路径

Example:
    >>> import office
    >>> office.pdf.pdf2docx(
    ...     file_path=r'D:\pdf\程序员晚枫.pdf',
    ...     output_path=r'D:\download'
    ... )

Note:
    - Windows用户：使用python-office库
    - Mac/Linux用户：使用popdf库（注释中的示例）
    - 该功能支持将PDF文件转换为可编辑的Word文档格式。
"""

# pip install python-office
import office # 导入第三方库

office.pdf.pdf2docx(file_path=r'D:\pdf\程序员晚枫.pdf',
                    output_path=r'D:\download')


# 上面这种是Windows用户
# 尊贵的Mac和Linux用户
# pip install popdf
# import popdf
# popdf.pdf2docx(file_path=r'D:\workplace\code\github\python-office\examples\popdf\test_files\pdf2docx\程序员晚枫.pdf',
#                output_path=r'./test_files/pdf2docx/output')
