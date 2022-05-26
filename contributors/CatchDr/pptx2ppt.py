#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: pptx2ppt.py
# Author: 刘运超
# Mail: chaodreaming@gmail.com
# Created Time:  2022-5-23 14:15
# Description: pptx转ppt
#############################################

from win32com.client import constants
import win32com
import os  # 目录的操作

def createppt(pptxPath, pptPath):
    powerpoint = win32com.client.Dispatch('PowerPoint.Application')
    win32com.client.gencache.EnsureDispatch('PowerPoint.Application')
    # powerpoint.Visible = 1
    ppt = powerpoint.Presentations.Open(pptxPath)
    ppt.SaveAs(pptPath)
    ppt.Close()
    powerpoint.Quit()


# 1、文件的批量转换
# 自己指定路径，
# 转换pptx到ppt
def pptx2ppt(path, docxSuffix=".pptx"):
    pptxFiles = []
    # 如果不存在，则不做处理
    if not os.path.exists(path):
        print("path does not exist path = " + path)
        return
    # 判断是否是文件
    elif os.path.isfile(path):
        print("path file type is file " + path)
        pptxFiles.append(path)
    # 如果是目录，则遍历目录下面的文件
    elif os.path.isdir(path):
        print(os.listdir(path))
        # 填充路径，补充完整路径
        if not path.endswith("/") or not path.endswith("\\"):
            path = path + "/"
        for file in os.listdir(path):
            if file.endswith(docxSuffix):
                pptxFiles.append(path + file)
    print(pptxFiles)
    for file in pptxFiles:
        filepath = os.path.abspath(file)
        index = filepath.rindex('.')
        pptPath = filepath[:index] + '.ppt'
        print(pptPath)
        createppt(filepath, pptPath)