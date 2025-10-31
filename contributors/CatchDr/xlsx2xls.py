#-*- coding:utf-8 -*-

#############################################
# File Name: xlsx2xls.py
# Author: 刘运超
# Mail: chaodreaming@gmail.com
# Created Time:  2022-5-23 14:30
# Description: xlsx转xls
#############################################

from win32com.client import constants, gencache
import win32com
import os  # 目录的操作

def createxls(xlsxPath: str, xlsPath: str) -> None:
    """将XLSX文档转换为XLS格式。
    
    Args:
        xlsxPath (str): 源XLSX文档路径
        xlsPath (str): 目标XLS文档路径
    
    Returns:
        None
    """
    excel = win32com.client.DispatchEx('Excel.Application')
    wb = excel.Workbooks.Open(xlsxPath)

    wb.SaveAs(xlsPath, FileFormat=56)  # FileFormat = 51 is for .xlsx extension
    wb.Close()  # FileFormat = 56 is for .xls extension
    excel.Application.Quit()


def xlsx2xls(path: str, docxSuffix: str = ".xlsx") -> None:
    """批量将XLSX文档转换为XLS格式。
    
    Args:
        path (str): 文件路径或目录路径
        docxSuffix (str, optional): XLSX文件后缀名，默认为".xlsx"
    
    Returns:
        None
    """
    excelFiles = []
    # 如果不存在，则不做处理
    if not os.path.exists(path):
        print("path does not exist path = " + path)
        return
    # 判断是否是文件
    elif os.path.isfile(path):
        print("path file type is file " + path)
        excelFiles.append(path)
    # 如果是目录，则遍历目录下面的文件
    elif os.path.isdir(path):
        print(os.listdir(path))
        # 填充路径，补充完整路径
        if not path.endswith("/") or not path.endswith("\\"):
            path = path + "/"
        for file in os.listdir(path):
            if file.endswith(docxSuffix):
                excelFiles.append(path + file)
    print(excelFiles)
    for file in excelFiles:
        filepath = os.path.abspath(file)
        index = filepath.rindex('.')
        xlsxPath = filepath[:index] + '.xls'
        print(xlsxPath)
        createxls(filepath, xlsxPath)