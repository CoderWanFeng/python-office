#-*- coding:utf-8 -*-

#############################################
# File Name: doc2docx.py
# Author: 刘运超
# Mail: chaodreaming@gmail.com
# Created Time:  2022-5-23 13:41:34
# Description: doc转docx
#############################################

from win32com.client import constants, gencache
import win32com
import os  # 目录的操作


def createdocx(wordPath: str, docxPath: str) -> None:
    """将Word文档转换为docx格式。
    
    Args:
        wordPath (str): 原始Word文档路径
        docxPath (str): 转换后的docx文件路径
    """
    # word = gencache.EnsureDispatch('Word.Application')
    # doc = word.Documents.Open(wordPath, ReadOnly=1)
    # # 转换方法
    # doc.ExportAsFixedFormat(docxPath, constants.wdExportFormatPDF)
    # word.Quit()

    word = win32com.client.DispatchEx('Word.Application')
    doc = word.Documents.Open(wordPath)
    doc.SaveAs(docxPath, FileFormat=12)
    doc.Close()
    word.Quit()


def doc2docx(path: str, docSuffix: str = ".doc") -> None:
    """批量将doc文件转换为docx格式。
    
    Args:
        path (str): 文件路径或目录路径
        docSuffix (str, optional): doc文件后缀，默认为".doc"
    """
    wordFiles = []
    # 如果不存在，则不做处理
    if not os.path.exists(path):
        print("path does not exist path = " + path)
        return
    # 判断是否是文件
    elif os.path.isfile(path):
        print("path file type is file " + path)
        wordFiles.append(path)
    # 如果是目录，则遍历目录下面的文件
    elif os.path.isdir(path):
        print(os.listdir(path))
        # 填充路径，补充完整路径
        if not path.endswith("/") or not path.endswith("\\"):
            path = path + "/"
        for file in os.listdir(path):
            if file.endswith(docSuffix):
                wordFiles.append(path + file)
    print(wordFiles)
    for file in wordFiles:
        filepath = os.path.abspath(file)
        index = filepath.rindex('.')
        docxPath = filepath[:index] + '.docx'
        print(docxPath)
        createdocx(filepath, docxPath)

