# coding:utf-8
from pathlib import Path
import win32com.client as win32
from customizeWindowPyfile.ProgressBarDialog import ProgressBar



def wordReplaceKeyword(wordPath,replace_dict):
    src_folder = Path(wordPath)
    des_folder = src_folder/'替换后的文件'
    if not des_folder.exists():
        des_folder.mkdir(parents=True)
    file_list = list(src_folder.glob('*.doc*'))
    totalTaskNum = len(file_list)
    doneTaskNum = 0
    currTaskNum = 1
    bar = ProgressBar()
    bar.show()
    word = win32.gencache.EnsureDispatch('Word.Application')
    word.Visible = False
    cs = win32.constants
    for i in file_list:
        doc = word.Documents.Open(str(i))
        bar.setProcessOnTiTle(currTaskNum, totalTaskNum)

        print(i.name)
        for old_txt, new_txt in replace_dict.items():
            findobj = word.Selection.Find
            findobj.ClearFormatting()
            findobj.Text = old_txt
            findobj.Replacement.ClearFormatting()
            findobj.Replacement.Text = new_txt
            if findobj.Execute(Replace=cs.wdReplaceAll):
                print(f'{old_txt}-->{new_txt}')
        new_file = des_folder / i.name
        doc.SaveAs(str(new_file))
        doc.Close()
        doneTaskNum = doneTaskNum + 1
        currTaskNum = currTaskNum + 1
        bar.setValue(100 * doneTaskNum / totalTaskNum, 100 * (doneTaskNum - 1) / totalTaskNum,
                     100 * totalTaskNum / totalTaskNum)

    word.Quit()

if __name__ == '__main__':
    dict = {'20201786': '20201772', '唐葆程': '小镇小船们'}
    wordReplaceKeyword('D:\Desktop\替换关键字', dict)
