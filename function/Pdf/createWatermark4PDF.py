# coding:utf-8

from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
import reportlab.pdfbase.ttfonts
from customizeWindowPyfile.ProgressBarDialog import ProgressBar



def create_watermark(content, angle, alpha, color):
    file_name = 'watermark.pdf'
    a = canvas.Canvas(file_name, pagesize=(50 * cm, 50 * cm))
    a.translate(0 * cm, 0 * cm)
    print('debug9')
    reportlab.pdfbase.pdfmetrics.registerFont(reportlab.pdfbase.ttfonts.TTFont('站酷高端黑', 'font/圆体-简繁 细体.ttc'))
    print('debug10')
    a.setFont('站酷高端黑', 26)
    a.rotate(angle)#旋转角度
    a.setFillColorRGB(color[0],color[1], color[2])#选择颜色
    print('color 0:'+str(color[0]))
    print('color 1:'+str(color[1]))
    print('color 2:'+str(color[2]))
    a.setFillAlpha(alpha)#透明度
    for i in range(0, 50, 5):
        for j in range(0, 50, 5):
            a.drawString(i * cm, j * cm, content)
    a.save()
    return file_name

def add_watermark(pdf_file_in, pdf_file_mark, pdf_file_out):
    outputfile = PdfFileWriter()
    inputfile = PdfFileReader(pdf_file_in)
    pageCount = inputfile.getNumPages()
    markfile = PdfFileReader(pdf_file_mark)
    for i in range(pageCount):
        page = inputfile.getPage(i)
        page.mergePage(markfile.getPage(0))
        outputfile.addPage(page)
    with open(pdf_file_out, 'wb') as f_out:
        outputfile.write(f_out)

def createWatermark4PDF(content,pdfPath, color=[139,105,105], angle=10, alpha=0.5):
    print('debug3')
    color = [color[0]/255, color[1]/255, color[2]/255]
    src_folder = Path(pdfPath)
    des_folder = src_folder/'水印'

    if not des_folder.exists():
        des_folder.mkdir(parents=True)
    file_list = list(src_folder.glob('*.pdf'))
    totalTaskNum = len(file_list)
    doneTaskNum = 0
    currTaskNum = 1
    bar = ProgressBar()
    bar.show()
    for pdf in file_list:
        pdf_file_in = str(pdf)
        pdf_file_mark = create_watermark(content, angle, alpha, color)
        pdf_file_out = str(des_folder / pdf.name)
        bar.setProcessOnTiTle(currTaskNum, totalTaskNum)
        add_watermark(pdf_file_in, pdf_file_mark, pdf_file_out)
        doneTaskNum = doneTaskNum + 1
        currTaskNum = currTaskNum + 1
        bar.setValue(100 * doneTaskNum / totalTaskNum, 100 * (doneTaskNum - 1) / totalTaskNum,
                     100 * totalTaskNum / totalTaskNum)


if __name__ == '__main__':
    color = [139, 105, 105]
    createWatermark4PDF('天才制造','D:\Desktop\功能测试\PDF文件')





