#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: word.py
# Author: 程序员晚枫
# Mail: 1957875073@qq.com
# Created Time:  2022-4-25 10:17:34
# Description: 有关word的自动化操作
#############################################

from win32com.client import constants, gencache
import os  # 目录的操作


def createpdf(wordPath, pdfPath):
    word = gencache.EnsureDispatch('Word.Application')
    doc = word.Documents.Open(wordPath, ReadOnly=1)
    # 转换方法
    doc.ExportAsFixedFormat(pdfPath, constants.wdExportFormatPDF)
    word.Quit()



# 1、文件的批量转换
# 自己指定路径，
# 为了适配wps不能转换doc的问题，这里限定：只能转换docx
def docx2pdf(path, docxSuffix=".docx"):
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
        pdfPath = filepath[:index] + '.pdf'
        print(pdfPath)
        createpdf(filepath, pdfPath)
