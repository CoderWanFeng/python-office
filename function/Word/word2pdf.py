from pathlib import Path
from comtypes.client import CreateObject
from customizeWindowPyfile.ProgressBarDialog import ProgressBar


def word2pdf(wordPath):
    src_folder = Path(wordPath)
    des_folder = Path(wordPath)/'pdf'
    if not des_folder.exists():
        des_folder.mkdir(parents=True)
    file_list = list(src_folder.glob('*.doc*'))
    totalTaskNum = len(file_list)
    doneTaskNum = 0
    currTaskNum = 1
    bar = ProgressBar()
    bar.show()

    word = CreateObject('Word.Application')
    for word_path in file_list:
        bar.setProcessOnTiTle(currTaskNum, totalTaskNum)
        pdf_path = des_folder / word_path.with_suffix('.pdf').name
        if pdf_path.exists():
            doc.Close()
            doneTaskNum = doneTaskNum + 1
            currTaskNum = currTaskNum + 1
            bar.setValue(100 * doneTaskNum / totalTaskNum, 100 * (doneTaskNum - 1) / totalTaskNum,
                         100 * totalTaskNum / totalTaskNum)
            continue
        else:
            doc = word.Documents.Open(str(word_path))
            doc.SaveAs(str(pdf_path), FileFormat=17)
            doc.Close()
            doneTaskNum = doneTaskNum + 1
            currTaskNum = currTaskNum + 1
            bar.setValue(100 * doneTaskNum / totalTaskNum, 100 * (doneTaskNum-1) / totalTaskNum, 100*totalTaskNum/totalTaskNum)

    word.Quit()

if __name__ == '__main__':
    word2pdf("D:\Desktop\功能测试\word文件")

