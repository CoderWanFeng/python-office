# -*- coding: utf-8 -*-
import reportlab
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFont
from tqdm import tqdm


def create_watermark(content):
    """创建PDF水印模板
    """
    # 创建一个PDF文件来作为一个水印文件
    c = canvas.Canvas('watermark.pdf')
    reportlab.pdfbase.pdfmetrics.registerFont(
        reportlab.pdfbase.ttfonts.TTFont('simfang', 'C:/Windows/Fonts/simfang.ttf'))
    c.setFont('simfang', 20)
    c.saveState()
    c.translate(305, 505)
    c.rotate(45)
    c.drawCentredString(0, 0, content)
    c.restoreState()
    c.save()
    pdf_watermark = PdfReader('watermark.pdf')
    return pdf_watermark


def pdf_add_watermark(pdf_file_in, pdf_file_mark, pdf_file_out):
    # print(pdf_file_out)
    pdf_output = PdfWriter()
    input_stream = open(pdf_file_in, 'rb')
    pdf_input = PdfReader(input_stream, strict=False)
    # 获取PDF文件的页数
    if pdf_input.is_encrypted:
        print("文件已被加密")
        PDF_Passwd = input("请输入PDF密码：")
        # 尝试用空密码解密
        try:
            pdf_input.decrypt(PDF_Passwd)
        except Exception:
            print(f"尝试用密码{PDF_Passwd}解密失败.")
            return False
    pageNum = len(pdf_input.pages)
    # 读入水印pdf文件
    # print(pdf_file_mark)
    mark_stream = open(pdf_file_mark, mode='rb')
    pdf_watermark = PdfReader(mark_stream, strict=False)
    # 给每一页打水印
    for pageNumber in tqdm(range(pageNum)):
        page = pdf_input.pages[pageNumber]
        page.merge_page(pdf_watermark.pages[0])
        page.compress_content_streams()  # 压缩内容
        pdf_output.add_page(page)
    with open(pdf_file_out, 'wb') as pdf_file_out_f:
        pdf_output.write(pdf_file_out_f)
