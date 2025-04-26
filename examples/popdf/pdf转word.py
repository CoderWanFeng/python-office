# -*- coding: UTF-8 -*-


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
