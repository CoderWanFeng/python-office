# -*- coding: utf-8 -*-
# @Time : 2021/3/16 18:02
# @公众号 :Python自动化办公社区
# @File : pdf_python.py
# @Software: PyCharm
# @Description:

import PyPDF2
import pdfplumber

def extract_content(pdf_path):
    # 内容提取，使用 pdfplumber 打开 PDF，用于提取文本
    with pdfplumber.open(pdf_path) as pdf_file:
        # 使用 PyPDF2 打开 PDF 用于提取图片
        pdf_image_reader = PyPDF2.PdfFileReader(open(pdf_path, "rb"))
        print(pdf_image_reader.getNumPages())

        content = ''
        # len(pdf.pages)为PDF文档页数，一页页解析
        for i in range(len(pdf_file.pages)):
            print("当前第 %s 页" % i)
            # pdf.pages[i] 是读取PDF文档第i+1页
            page_text = pdf_file.pages[i]
            # page.extract_text()函数即读取文本内容
            page_content = page_text.extract_text()
            if page_content:
                content = content + page_content + "\n"
                print(page_content)

extract_content('静夜思.pdf')

