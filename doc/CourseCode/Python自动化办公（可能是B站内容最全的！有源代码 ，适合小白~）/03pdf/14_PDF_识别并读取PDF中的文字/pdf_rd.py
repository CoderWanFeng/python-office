# -*- coding: utf-8 -*-
# @Time : 2020/8/21 20:04
# @公众号 :Python自动化办公社区 
# @File : pdf_rd.py
# @Software: PyCharm
# @Description:


# pip install pdfminer3k
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager,process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams

# 打开pdf文件
pdf_file = open('静夜思.pdf', 'rb')

########默认操作#######
rsrcmgr = PDFResourceManager()
retstr = StringIO()
laparams = LAParams()
device = TextConverter(rsrcmgr=rsrcmgr,outfp=retstr,laparams=laparams)
process_pdf(rsrcmgr=rsrcmgr,device=device,fp=pdf_file)
device.close()
content = retstr.getvalue()
retstr.close()
pdf_file.close()
########默认操作#######

print(content)
