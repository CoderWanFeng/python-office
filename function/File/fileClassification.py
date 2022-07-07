# coding:utf-8
from pathlib import Path
from customizeWindowPyfile.ProgressBarDialog import ProgressBar
def fileClasscation(folderPath):
    src_folder = Path(folderPath)
    des_folder = src_folder/'分类后的文件'

    files = src_folder.glob('*')

    for i in files:
        if i.is_file():
            des_path = des_folder / i.suffix.strip('.')
            if not des_path.exists():
                des_path.mkdir(parents=True)
            i.replace(des_path / i.name)
    bar = ProgressBar()
    bar.show()
    bar.setValue(100, 0, 100)



if __name__ == '__main__':
    fileClasscation('D:\Desktop\功能测试\文件分类功能展示')