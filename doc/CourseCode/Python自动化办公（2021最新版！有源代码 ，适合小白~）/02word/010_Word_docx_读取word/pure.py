# -*- coding: utf-8 -*-

# @公众号 :Python自动化办公社区 
# @File : pure.py
# @Software: PyCharm
# @Description:

from docx import Document

document = Document('pure.docx')
all_paragraphs = document.paragraphs
for p in all_paragraphs:
    print(p.text)


# excel写入