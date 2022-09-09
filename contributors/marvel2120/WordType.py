import os
from win32com import client
from win32com.client import constants


# requirements
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pypiwin32

class MainWord():
    def __init__(self):
        self.doc = ".doc"
        self.docx = ".docx"
        self.pdf = ".pdf"
        # 打开word应用程序
        self.word = client.Dispatch("Word.Application")


    def file2pdf(self, path):
        # 保存待转换的word文件
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

        # 保存待删除的中间文件
        remove_files = []

        for file in word_files:
            # 源文件
            file_path = os.path.abspath(file)
            # 目标文件
            pdf_path = os.path.abspath(file_path.split(".")[0] + self.pdf)

            # 如果是doc文件，转换为docx文件
            if file_path.endswith(self.doc):
                doc = self.word.Documents.Open(file_path)  # 打开word文件
                doc.SaveAs("{}x".format(file_path), 12)  # 另存为后缀为".docx"的文件，其中参数12或16指docx文件
                doc.Close()  # 关闭原来word文件
                file_path = file_path.split(".")[0] + self.docx
                remove_files.append(file_path)
                self.createpdf(file_path, pdf_path)
                continue
            self.createpdf(file_path, pdf_path)
        self.word.Quit()
        for f in remove_files:
            os.remove(f)

    def createpdf(self, word_path, pdf_path):
        print(word_path)
        try:
            doc = self.word.Documents.Open(word_path, ReadOnly=1)
            doc.ExportAsFixedFormat(pdf_path, constants.wdExportFormatPDF,
                                    Item=constants.wdExportDocumentWithMarkup,
                                    CreateBookmarks=constants.wdExportCreateHeadingBookmarks)
            doc.Close()
        except:
            print(f"文档{word_path}转换失败")
        finally:
            pass


m = MainWord()
m.file2pdf(r"C:\Users\PHL\Desktop\测试文档")
