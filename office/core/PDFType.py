import os
from fpdf import FPDF
from office.lib.pdf import add_watermark_service
import pikepdf
from PyPDF2 import PdfFileReader, PdfFileWriter
from pdf2docx import Converter


class MainPDF():

    def add_watermark(self):
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

    def file2pdf(self, file_type, path, res_pdf='file2pdf.pdf'):
        if file_type == 'txt':
            pdf = FPDF()
            pdf.add_page()  # Add a page
            pdf.set_font("Arial", size=15)  # set style and size of font
            f = open(path, "r")  # open the text file in read mode
            # insert the texts in pdf
            for x in f:
                pdf.cell(50, 5, txt=x, ln=1, align='C')
            # pdf.output("path where you want to store pdf file\\file_name.pdf")
            pdf.output(res_pdf)

    def pdf2docx(self, file_path):
        try:
            pdf_name = file_path.split('.')[0]
            word_name = pdf_name + '.docx'
            cv = Converter(file_path)
            cv.convert(word_name)
            cv.close()
        except:
            print('这个文件有问题~！')

    # 合并pdf
    def merge2pdf(self, one_by_one, output):
        """
        @Author & Date  : CoderWanFeng 2022/5/16 23:33
        @Desc  : merge_pdfs(paths=['开篇词.pdf', '中国元宇宙白皮书 (送审稿).pdf'], output='merge.pdf')
        """
        pdf_writer = PdfFileWriter()

        for path in one_by_one:
            pdf_reader = PdfFileReader(path)
            for page in range(pdf_reader.getNumPages()):
                # 把每张PDF页面加入到这个可读取对象中
                pdf_writer.addPage(pdf_reader.getPage(page))

        # 把这个已合并了的PDF文档存储起来
        with open(output, 'wb') as out:
            pdf_writer.write(out)

    # PDF加密
    def encrypt4pdf(self, path, password, res_pdf='encrypt.pdf'):
        """
        @Author & Date  : CoderWanFeng 2022/5/9 18:27
        @Desc  : path: 存放文件的路径
                password: 你的密码
                res_pdf: 结果文件的名称 ，可以为空，默认是：encrypt.pdf
        """
        pdf = pikepdf.open(path)
        pdf.save(res_pdf, encryption=pikepdf.Encryption(owner=password, user=password, R=4))
        pdf.close()

    # PDF解密
    def decrypt4pdf(self, path, password, res_pdf='decrypt.pdf'):
        pdf = pikepdf.open(path, password=password)
        pdf.save(res_pdf)
        pdf.close()
