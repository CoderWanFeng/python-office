"""
1. 如何设置编辑器字体的大小?
File(文件)-> Settings(设置) -> Editor(编辑器) -> Font(字体), 修改字体的大小
2. 注释: 代码的解释说明
"""

# 1). 导入需要的模块(打开应用程序的模块)
import win32com.client
import os


def ppt2pdf_single(filename, output_filename):
    """
    PPT文件导出为pdf格式
    :param filename: PPT文件的名称
    :param output_filename: 导出的pdf文件的名称
    :return:
    """
    # 2). 打开PPT程序
    ppt_app = win32com.client.Dispatch('PowerPoint.Application')
    # ppt_app.Visible = True  # 程序操作应用程序的过程是否可视化

    # 3). 通过PPT的应用程序打开指定的PPT文件
    # filename = "C:/Users/Administrator/Desktop/PPT办公自动化/ppt/PPT素材1.pptx"
    # output_filename = "C:/Users/Administrator/Desktop/PPT办公自动化/ppt/PPT素材1.pdf"
    ppt = ppt_app.Presentations.Open(filename)

    # 4). 打开的PPT另存为pdf文件。17数字是ppt转图片，32数字是ppt转pdf。
    ppt.SaveAs(output_filename, 32)
    # 退出PPT程序
    ppt_app.Quit()


