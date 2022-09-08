import os
import aspose.words as aw
from win32com.client import constants, gencache


# requirements
# ppypiwin32==223
# aspose-words==22.8.0

class MainWord():
    def __init__(self):
        self.doc = ".doc"
        self.docx = ".docx"
        self.pdf = ".pdf"

    def file2pdf(self, path):
        # 保存word文件路径
        word_files = []
        # 遍历path下所有的docx, doc文件，加入到word_files中
        for dir_path, _, files in os.walk(path):
            for f in files:
                if f.endswith(self.doc) or f.endswith(self.docx):
                    word_files.append(os.path.join(dir_path, f))
        # 不存在有效的文件
        if len(word_files) == 0:
            print("不存在有效的word文件")
            return
        print(word_files)
        remove_files = []
        for file in word_files:
            # 源文件
            file_path = os.path.abspath(file)
            # 目标文件
            pdf_path = os.path.abspath(file_path.split(".")[0] + self.pdf)
            # 如果是doc文件，转换为docx文件
            if file_path.endswith(self.doc):
                docx = aw.Document(file_path)
                file_path = file_path.split(".")[0] + self.docx
                docx.save(file_path)
                remove_files.append(file_path)
                self.createpdf(file_path, pdf_path)
                continue
            self.createpdf(file_path, pdf_path)
        for f in remove_files:
            os.remove(f)

    def createpdf(self, word_path, pdf_path):
        print(word_path)
        word = gencache.EnsureDispatch('Word.Application')
        doc = word.Documents.Open(word_path, ReadOnly=1)
        # 转换方法
        doc.ExportAsFixedFormat(pdf_path, constants.wdExportFormatPDF)
        word.Quit()


m = MainWord()
m.file2pdf(r"C:\Users\PHL\Desktop\测试文档")
