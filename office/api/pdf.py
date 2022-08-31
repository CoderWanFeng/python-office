# -*- coding: utf-8 -*-

from office.core.PDFType import MainPDF
from office.lib.utils.except_utils import except_dec

mainPDF = MainPDF()


# 给pdf加水印-无参数
@except_dec()
def add_watermark() -> None:
    mainPDF.add_watermark()


# 给pdf加水印-有参数
@except_dec()
def add_watermark_by_parameters(pdf_file, mark_str, output_file_name='添加了水印的文件.pdf') -> None:
    """
    必填参数：
    pdf_file:pdf的位置，例如：d:/code/程序员晚枫.pdf
    mark_str:需要添加的水印内容，例如：百度一下：程序员晚枫
    选填参数：
    output_file_name：指定添加了水印的文件名称，可以不指定，默认是：添加了水印的文件.pdf
    """
    mainPDF.add_watermark_by_parameters(pdf_file, mark_str, output_file_name)


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
def pdf2docx(file_path, output_path='.'):
    mainPDF.pdf2docx(file_path, output_path)


@except_dec()
def pdf2imgs(pdf_path, out_dir):
    mainPDF.pdf2imgs(pdf_path, out_dir)


@except_dec()
def add_img_water(pdf_file_in, pdf_file_mark, pdf_file_out):
    mainPDF.add_img_watermark(pdf_file_in, pdf_file_mark, pdf_file_out)
