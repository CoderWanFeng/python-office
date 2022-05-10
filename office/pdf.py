# -*- coding: utf-8 -*-
import os
from fpdf import FPDF
from service.pdf import add_watermark_service
import pikepdf


#给pdf加水印
def add_watermark():
    pdf_file_in = input("请输入需要添加水印的文件位置：")  # 需要添加水印的文件
    Watermark_Str = input("请输入需要添加的水印内容：")
    print('=' * 20)
    print('正在按要求，给你的PDF文件添加水印，请让程序飞一会儿~')
    print('=' * 20)
    pdf_file_mark = 'watermark.pdf'  # 水印文件
    add_watermark_service.create_watermark(str(Watermark_Str))
    pdf_file_out = '添加了水印的文件.pdf'  # 添加PDF水印后的文件
    add_watermark_service.pdf_add_watermark(pdf_file_in, pdf_file_mark, pdf_file_out)
    print("水印添加结束，请打开电脑上的这个位置，查看结果文件：{path}".format(path=os.getcwd()))


# txt转pdf
def txt2pdf():
    pdf = FPDF()
    pdf.add_page()  # Add a page
    pdf.set_font("Arial", size=15)  # set style and size of font
    f = open(
        'D:\\workplace\\code\\BaiduNetdiskWorkspace\\personal\\linux\\workplace\\pro\\git\\gitee\\python-office\\test\\allpackages.txt',
        "r")  # open the text file in read mode
    # insert the texts in pdf
    for x in f:
        pdf.cell(50, 5, txt=x, ln=1, align='C')
    # pdf.output("path where you want to store pdf file\\file_name.pdf")
    pdf.output("game_notes.pdf")


# PDF加密
def encrypt4pdf(path, password, res_pdf='encrypt.pdf'):
    """
    @Author & Date  : CoderWanFeng 2022/5/9 18:27
    @Desc  : path: 存放文件的路径
            password: 你的密码
            res_pdf: 结果文件的名称 ，可以为空，默认是：encrypt.pdf
    """
    pdf = pikepdf.open(path)
    pdf.save(res_pdf, encryption=pikepdf.Encryption(owner=password,  user=password,R=4))
    pdf.close()


# PDF解密
def decrypt4pdf(path, password, res_pdf='decrypt.pdf'):
    pdf = pikepdf.open(path, password=password)
    pdf.save(res_pdf)
    pdf.close()
