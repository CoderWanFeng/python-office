# -*- coding: utf-8 -*-
# @Time : 2020/8/20 20:47
# @公众号 :Python自动化办公社区 
# @File : word2pdf.py
# @Software: PyCharm
# @Description:

from win32com.client import Dispatch,constants,gencache

doc_path = 'test.docx'
pdf_path = 'test.pdf'

gencache.EnsureModule('{00020905-0000-0000-C000-000000000046}',0,8,4)
wd = Dispatch("Word.Application")
doc = wd.Documents.Open(doc_path,ReadOnly=1)
doc.ExportAsFixedFormat(pdf_path,constants.wdExportFormatPDF,Item=constants.wdExportDocumentWithMarkup,CreateBookmarks=constants.wdExportCreateHeadingBookmarks)
wd.Quit(constants.wdDoNotSaveChanges)