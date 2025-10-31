#-*- coding:utf-8 -*-

#############################################
# File Name: docx2doc.py
# Author: 刘运超
# Mail: chaodreaming@gmail.com
# Created Time:  2022-5-23 13:41:34
# Description: docx转doc
#############################################

from win32com.client import constants, gencache
import win32com
import os  # 目录的操作



def createdoc(wordPath: str, docxPath: str) -> None:
    """将Word文档转换为DOC格式。
    
    Args:
        wordPath (str): 源Word文档路径
        docxPath (str): 目标DOC文档路径
    
    Returns:
        None
    """
    # word = gencache.EnsureDispatch('Word.Application')
    # doc = word.Documents.Open(wordPath, ReadOnly=1)
    # # 转换方法
    # doc.ExportAsFixedFormat(docxPath, constants.wdExportFormatPDF)
    # word.Quit()

    word = win32com.client.DispatchEx('Word.Application')
    doc = word.Documents.Open(wordPath)
    doc.SaveAs(docxPath, FileFormat=11)
    doc.Close()
    word.Quit()


def docx2doc(path: str, docxSuffix: str = ".docx") -> None:
    """批量将DOCX文档转换为DOC格式。
    
    Args:
        path (str): 文件路径或目录路径
        docxSuffix (str, optional): DOCX文件后缀名，默认为".docx"
    
    Returns:
        None
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
            if file.endswith(docxSuffix):
                wordFiles.append(path + file)
    print(wordFiles)
    for file in wordFiles:
        filepath = os.path.abspath(file)
        index = filepath.rindex('.')
        docPath = filepath[:index] + '.doc'
        print(docPath)
        createdoc(filepath, docPath)