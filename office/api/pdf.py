# -*- coding: utf-8 -*-

from office.core.PDFType import MainPDF
from office.lib.utils.except_utils import except_dec

mainPDF = MainPDF()


# 给pdf加水印
@except_dec()
def add_watermark() -> None:
    mainPDF.add_watermark()


# txt转pdf
@except_dec()
def txt2pdf(path: str, res_pdf='txt2pdf.pdf'):
    mainPDF.file2pdf(path, res_pdf)


# PDF加密
@except_dec()
def encrypt4pdf(path, password, res_pdf='encrypt.pdf'):
    mainPDF.encrypt4pdf(path, password, res_pdf)


# PDF解密
@except_dec()
def decrypt4pdf(path, password, res_pdf='decrypt.pdf'):
    mainPDF.decrypt4pdf(path, password, res_pdf)


# 合并pdf
@except_dec()
def merge2pdf(one_by_one, output):
    mainPDF.merge2pdf(one_by_one, output)


# todo：输入文件路径
@except_dec()
def pdf2docx(file_path):
    mainPDF.pdf2docx(file_path)


@except_dec()
def pdf2imgs(pdf_path, out_dir):
    mainPDF.pdf2imgs(pdf_path, out_dir)
