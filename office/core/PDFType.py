from fpdf import FPDF
from office.lib.pdf import add_watermark_service
import pikepdf
from PyPDF2 import PdfFileReader, PdfFileWriter
from pdf2docx import Converter
import os
import datetime

import fitz  # fitz就是pip install PyMuPDF


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

    # def pdf2imgs(self, pdf_path: str, out_dir=".") -> None:
    #     print('PDF开始转换，你可以加入交流群唠唠嗑：http://www.python4office.cn/wechat-group/')
    #     pdfDoc = fitz.open(pdf_path)
    #     if pdfDoc.pageCount > 50:
    #         print('少年，你的PDF页数有点多哟，请耐心等待~')
    #     for pg in range(pdfDoc.pageCount):
    #         page = pdfDoc[pg]
    #         rotate = int(0)
    #         # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像。
    #         # 此处若是不做设置，默认图片大小为：792X612, dpi=96
    #         zoom_x = 1.33333333  # (1.33333333-->1056x816)   (2-->1584x1224)
    #         zoom_y = 1.33333333
    #         mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
    #         pix = page.getPixmap(matrix=mat, alpha=False)

    #         if not os.path.exists(out_dir):  # 判断存放图片的文件夹是否存在
    #             os.makedirs(out_dir)  # 若图片文件夹不存在就创建

    #         pix.writePNG(out_dir + '/' + 'images_%s.png' % pg)  # 将图片写入指定的文件夹内
    #     print(f'PDF转换Image完成，图片在你指定的output文件夹{out_dir}，如果没有指定，默认是PDF同一个文件夹')

    def pdf2imgs(self,pdf_path: str, out_dir=".") -> None:
        print('PDF开始转换，你可以加入交流群唠唠嗑：http://www.python4office.cn/wechat-group/')
        pdfDoc = fitz.open(pdf_path)
        if pdfDoc.page_count > 50:
            print('少年，你的PDF页数有点多哟，请耐心等待~')
        for pg in range(pdfDoc.page_count):
            page = pdfDoc[pg]
            rotate = int(0)
            # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像。
            # 此处若是不做设置，默认图片大小为：792X612, dpi=96
            zoom_x = 1.33333333  # (1.33333333-->1056x816)   (2-->1584x1224)
            zoom_y = 1.33333333
            mat = fitz.Matrix(zoom_x, zoom_y).prerotate(rotate)
            pix = page.get_pixmap(matrix=mat, alpha=False)

            if not os.path.exists(out_dir):  # 判断存放图片的文件夹是否存在
                os.makedirs(out_dir)  # 若图片文件夹不存在就创建

            pix.save(out_dir + '/' + 'images_%s.png' % pg)  # 将图片写入指定的文件夹内
        print(f'PDF转换Image完成，图片在你指定的output文件夹{out_dir}，如果没有指定，默认是PDF同一个文件夹')