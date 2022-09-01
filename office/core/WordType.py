import os
from win32com.client import constants, gencache


class MainWord():

    def file2pdf(self, path, docxSuffix=".docx"):
        wordFiles = []
        # 如果不存在，则不做处理
        if not os.path.exists(path):
            print("path does not exist path = " + path)
            return
        # 判断是否是文件
        elif os.path.isfile(path):
            print("path file type is file " + path)
            wordFiles.append(path)
        # 如果是目录，则遍历目录下面的文件
        elif os.path.isdir(path):
            print(os.listdir(path))
            # 填充路径，补充完整路径
            if not path.endswith("/") or not path.endswith("\\"):
                path = path + "/"
            for file in os.listdir(path):
                if file.endswith(docxSuffix):
                    wordFiles.append(path + file)
        print(wordFiles)
        for file in wordFiles:
            filepath = os.path.abspath(file)
            index = filepath.rindex('.')
            pdfPath = os.path.abspath(filepath[:index] + '.pdf')
            print(pdfPath)
            self.createpdf(filepath, pdfPath)


    def createpdf(self,wordPath, pdfPath):
        word = gencache.EnsureDispatch('Word.Application')
        doc = word.Documents.Open(wordPath, ReadOnly=1)
        # 转换方法
        doc.ExportAsFixedFormat(pdfPath, constants.wdExportFormatPDF)
        word.Quit()
