#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: ppt2pptx.py
# Author: 刘运超
# Mail: chaodreaming@gmail.com
# Created Time:  2022-5-23 14:11
# Description: ppt转pptx
#############################################

from win32com.client import constants
import win32com
import os  # 目录的操作

def createpptx(pptPath, pptxPath):
    powerpoint = win32com.client.Dispatch('PowerPoint.Application')
    win32com.client.gencache.EnsureDispatch('PowerPoint.Application')
    # powerpoint.Visible = 1
    ppt = powerpoint.Presentations.Open(pptPath)
    ppt.SaveAs(pptxPath)
    ppt.Close()
    powerpoint.Quit()


# 1、文件的批量转换
# 自己指定路径，
# 转换ppt到pptx
def ppt2pptx(path, docxSuffix=".ppt"):
    pptFiles = []
    # 如果不存在，则不做处理
    if not os.path.exists(path):
        print("path does not exist path = " + path)
        return
    # 判断是否是文件
    elif os.path.isfile(path):
        print("path file type is file " + path)
        pptFiles.append(path)
    # 如果是目录，则遍历目录下面的文件
    elif os.path.isdir(path):
        print(os.listdir(path))
        # 填充路径，补充完整路径
        if not path.endswith("/") or not path.endswith("\\"):
            path = path + "/"
        for file in os.listdir(path):
            if file.endswith(docxSuffix):
                pptFiles.append(path + file)
    print(pptFiles)
    for file in pptFiles:
        filepath = os.path.abspath(file)
        index = filepath.rindex('.')
        pptxPath = filepath[:index] + '.pptx'
        print(pptxPath)
        createpptx(filepath, pptxPath)