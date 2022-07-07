# coding:utf-8

from pathlib import Path
from zipfile import ZipFile
import win32com.client as win32
import shutil
from customizeWindowPyfile.ProgressBarDialog import ProgressBar

def ppt2pptx(ppt_path):
    ppt_app = win32.gencache.EnsureDispatch('PowerPoint.Application')
    ppt = ppt_app.Presentations.Open(ppt_path)
    pptx_path = ppt_path.with_suffix('.pptx')
    ppt.SaveAs(pptx_path, 24)
    ppt.Close()
    ppt_app.Quit()
    return pptx_path


def extract_img(ppt_path, img_folder):
    if ppt_path.suffix == '.ppt':
        ppt_path = ppt2pptx(ppt_path)
    with ZipFile(ppt_path) as zf:
        for name in zf.namelist():
            if name.startswith('ppt/media/image'):
                zf.extract(name, img_folder)
    filelist =img_folder.rglob('*')
    for i in filelist:
        print(type(i))
        print(i)
        if i.is_file():
            i.replace(img_folder / i.name)
    toDeleteDir = str(img_folder/'ppt')
    shutil.rmtree(toDeleteDir)


def pptImageExtration(pptPath):
    pptx_file = Path(pptPath)
    img_folder = Path(str(pptx_file.resolve()).strip('.pptx')+'提取的图片')
    if not img_folder.exists():
        img_folder.mkdir(parents=True)
    extract_img(pptx_file, img_folder)

    bar = ProgressBar()
    bar.show()
    bar.setValue(100, 0, 100)


if __name__ =='__main__':
    pptImageExtration('D:\Desktop\功能测试\ppt文件\故宫建筑介绍.pptx')

