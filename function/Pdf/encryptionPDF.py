# coding:utf-8

from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter
from customizeWindowPyfile.ProgressBarDialog import ProgressBar


def encryptionPDF(pdfPath, password):
    src_folder = Path(pdfPath)
    file_list = list(src_folder.glob('*.pdf'))
    totalTaskNum = len(file_list)
    doneTaskNum = 0
    currTaskNum = 1
    bar = ProgressBar()
    bar.show()

    for pdf in file_list:
        inputfile = PdfFileReader(str(pdf))
        bar.setProcessOnTiTle(currTaskNum, totalTaskNum)
        outputfile = PdfFileWriter()
        pageCount = inputfile.getNumPages()

        for page in range(pageCount):
            outputfile.addPage(inputfile.getPage(page))
        outputfile.encrypt(password)
        des_name = f'{pdf.stem}_加密.pdf'
        des_file = src_folder / des_name

        doneTaskNum = doneTaskNum + 1
        currTaskNum = currTaskNum + 1
        print(100 * doneTaskNum / totalTaskNum)
        bar.setValue(100 * doneTaskNum / totalTaskNum, 100 * (doneTaskNum - 1) / totalTaskNum,
                     100 * totalTaskNum / totalTaskNum)

        with open(des_file, 'wb') as f_out:
            outputfile.write(f_out)

if __name__ == '__main__':
    encryptionPDF('D:\Desktop\功能测试\PDF文件', '12345')
