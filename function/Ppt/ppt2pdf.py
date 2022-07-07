from pathlib import Path
from comtypes.client import CreateObject
from customizeWindowPyfile.ProgressBarDialog import ProgressBar

def ppt2pdf(PPTpath):
    src_folder = Path(PPTpath)
    des_folder = Path(PPTpath) / 'ppt转pdf'

    if not des_folder.exists():
        des_folder.mkdir(parents=True)


    ppt_app = CreateObject('PowerPoint.Application')
    ppt_app.Visible = 1
    file_list = list(src_folder.glob('*.ppt*'))
    print('debug0')

    totalTaskNum = len(file_list)
    doneTaskNum = 0
    currTaskNum = 1
    bar = ProgressBar()
    bar.show()


    for ppt_path in file_list:

        ppt = ppt_app.Presentations.Open(str(ppt_path))
        bar.setProcessOnTiTle(currTaskNum, totalTaskNum)
        pdf_path = des_folder / ppt_path.with_suffix('.pdf').name
        if pdf_path.exists():
            ppt.Close()
            doneTaskNum = doneTaskNum + 1
            currTaskNum = currTaskNum + 1
            print(str(100 * doneTaskNum / totalTaskNum) + '       ' + str(100 * (doneTaskNum - 1) / totalTaskNum))
            bar.setValue(100 * doneTaskNum / totalTaskNum, 100 * (doneTaskNum - 1) / totalTaskNum,
                         100 * totalTaskNum / totalTaskNum)
            continue
        else:
            ppt.SaveAs(str(pdf_path), 32)
            ppt.Close()
            doneTaskNum = doneTaskNum + 1
            currTaskNum = currTaskNum + 1
            bar.setValue(100 * doneTaskNum / totalTaskNum, 100 * (doneTaskNum-1) / totalTaskNum, 100*totalTaskNum/totalTaskNum)

    ppt_app.Quit()


if __name__ == "__main__":
    ppt2pdf('D:\Desktop\功能测试\ppt文件')
