#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: xls2xlsx.py
# Author: 刘运超
# Mail: chaodreaming@gmail.com
# Created Time:  2022-5-23 14:24
# Description: xls转xlsx
#############################################

from win32com.client import constants, gencache
import win32com
import os  # 目录的操作



def createxlsx(xlsPath, xlsxPath):

    excel = win32com.client.DispatchEx('Excel.Application')
    wb = excel.Workbooks.Open(xlsPath)

    wb.SaveAs(xlsxPath, FileFormat=51)  # FileFormat = 51 is for .xlsx extension
    wb.Close()  # FileFormat = 56 is for .xls extension
    excel.Application.Quit()



# 1、文件的批量转换
# 自己指定路径，
# 转换xls到xlsx
def xls2xlsx(path, docxSuffix=".xls"):
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
        xlsPath = filepath[:index] + '.xlsx'
        print(xlsPath)
        createxlsx(filepath, xlsPath)