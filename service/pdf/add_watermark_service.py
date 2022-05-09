# -*- coding: utf-8 -*-
import reportlab
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFont

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
    pdf_watermark = PdfFileReader('watermark.pdf')
    return pdf_watermark


def pdf_add_watermark(pdf_file_in, pdf_file_mark, pdf_file_out):
    # print(pdf_file_out)
    pdf_output = PdfFileWriter()
    input_stream = open(pdf_file_in, 'rb')
    pdf_input = PdfFileReader(input_stream, strict=False)
    # 获取PDF文件的页数
    if pdf_input.getIsEncrypted():
        print("文件已被加密")
        PDF_Passwd = input("请输入PDF密码：")
        # 尝试用空密码解密
        try:
            pdf_input.decrypt(PDF_Passwd)
        except Exception:
            print(f"尝试用密码{PDF_Passwd}解密失败.")
            return False
    pageNum = pdf_input.getNumPages()
    # 读入水印pdf文件
    # print(pdf_file_mark)
    mark_stream = open(pdf_file_mark, mode='rb')
    pdf_watermark = PdfFileReader(mark_stream, strict=False)
    # 给每一页打水印
    for i in range(pageNum):
        page = pdf_input.getPage(i)
        page.mergePage(pdf_watermark.getPage(0))
        page.compressContentStreams()  # 压缩内容
        pdf_output.addPage(page)
    pdf_output.write(open(pdf_file_out, 'wb'))

