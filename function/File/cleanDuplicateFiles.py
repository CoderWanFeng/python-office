# coding:utf-8

from pathlib import Path
from filecmp import cmp
from customizeWindowPyfile.ProgressBarDialog import ProgressBar

def cleanDuplicateFiles(folderPath):
    src_folder = Path(folderPath)
    des_folder = src_folder/'冗余文件'
    if not des_folder.exists():
        des_folder.mkdir(parents=True)
    result = list(src_folder.glob('*'))
    file_list = []

    for i in result:
        if i.is_file():
            file_list.append(i)

    for m in file_list:
        for n in file_list:
            if m != n and m.exists() and n.exists():
                if cmp(m, n):
                    n.replace(des_folder / n.name)
    bar = ProgressBar()
    bar.show()
    bar.setValue(100,0,100)

if __name__ =='__main__':
    cleanDuplicateFiles('D:\Desktop\功能测试\检测重复文件功能展示')

