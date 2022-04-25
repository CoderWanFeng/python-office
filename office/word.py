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
def docx2pdf(path):
    print(os.listdir(path))  # 当前文件夹下的所有文件
    wordfiles = []
    for file in os.listdir('.'):
        if file.endswith(('.docx')):  # 通过后缀找出所有的workd文件
            wordfiles.append(file)
    print(wordfiles)

    for file in wordfiles:
        # 获取文件路径
        filepath = os.path.abspath(file)
        index = filepath.rindex('.')
        # 通过截取获取pdfpath
        pdfpath = filepath[:index] + '.pdf'
        print(pdfpath)
        createpdf(filepath, pdfpath)
