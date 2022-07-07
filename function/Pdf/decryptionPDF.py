# coding:utf-8

from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter
from customizeWindowPyfile.ProgressBarDialog import ProgressBar

def decryptionPDF(pdfPath, password):
    src_folder = Path(pdfPath)
    file_list = list(src_folder.glob('*加密.pdf'))
    print(file_list)
    totalTaskNum = len(file_list)
    doneTaskNum = 0
    currentTaskNum = 1
    bar = ProgressBar()
    bar.show()
    for pdf in file_list:
        inputfile = PdfFileReader(str(pdf))
        outputfile = PdfFileWriter()


        bar.setProcessOnTiTle(currentTaskNum, totalTaskNum)

        if inputfile.isEncrypted:
            inputfile.decrypt(password)
            pageCount = inputfile.getNumPages()
            for page in range(pageCount):
                outputfile.addPage(inputfile.getPage(page))

            des_name = f'{pdf.stem}_解密.pdf'
            des_file = src_folder / des_name

            with open(des_file, 'wb') as f_out:
                outputfile.write(f_out)

            doneTaskNum = doneTaskNum + 1
            currentTaskNum = currentTaskNum + 1
            print(currentTaskNum)
            print(100 * doneTaskNum / totalTaskNum)
            bar.setValue(100 * doneTaskNum / totalTaskNum, 100 * (doneTaskNum - 1) / totalTaskNum,
                         100 * totalTaskNum / totalTaskNum)



if __name__ == '__main__':
    decryptionPDF('D:\Desktop\功能测试\PDF文件', '12345')

