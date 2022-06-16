# -*- coding: utf-8 -*-

from core.PDFType import MainPDF

mainPDF = MainPDF()


# 给pdf加水印
def add_watermark():
    mainPDF.add_watermark()


# txt转pdf
def txt2pdf(path, res_pdf='txt2pdf.pdf'):
    mainPDF.file2pdf(path, res_pdf)


# PDF加密
def encrypt4pdf(path, password, res_pdf='encrypt.pdf'):
    mainPDF.encrypt4pdf(path, password, res_pdf)


# PDF解密
def decrypt4pdf(path, password, res_pdf='decrypt.pdf'):
    mainPDF.decrypt4pdf(path, password, res_pdf)


# 合并pdf
def merge2pdf(one_by_one, output):
    mainPDF.merge2pdf(one_by_one, output)


def pdf2docx(file_path):
    mainPDF.pdf2docx(file_path)
