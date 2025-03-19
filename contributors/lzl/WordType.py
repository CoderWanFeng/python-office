import os
from win32com import client
from win32com.client import constants


# requirements
# pip install -i https://mirrors.aliyun.com/pypi/simple/ pypiwin32

class MainWord():
    def __init__(self):
        self.doc = ".doc"
        self.docx = ".docx"
        self.pdf = ".pdf"
        # Open Word application
        self.word = client.Dispatch("Word.Application")


    def file2pdf(self, path):
        # Save Word files to be converted
        word_files = []

        # Traverse all docx, doc files under the path and add them to word_files
        for dir_path, _, files in os.walk(path):
            for f in files:
                if f.endswith(self.doc) or f.endswith(self.docx):
                    word_files.append(os.path.join(dir_path, f))

        # No valid files exist
        if len(word_files) == 0:
            print("No valid Word files found")
            return

        # Save intermediate files to be deleted
        remove_files = []

        for file in word_files:
            # Source file
            file_path = os.path.abspath(file)
            # Target file
            pdf_path = os.path.abspath(file_path.split(".")[0] + self.pdf)

            # If it is a doc file, convert it to a docx file
            if file_path.endswith(self.doc):
                doc = self.word.Documents.Open(file_path)  # Open Word file
                doc.SaveAs("{}x".format(file_path), 12)  # Save as a file with the suffix ".docx", where parameter 12 or 16 refers to a docx file
                doc.Close()  # Close the original Word file
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
            print(f"Failed to convert document {word_path}")
        finally:
            pass


m = MainWord()
m.file2pdf(r"C:\Users\lzl\Desktop\test")
