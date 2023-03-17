#!/usr/bin/env python
# -*- coding:utf-8 -*-

#############################################
# File Name: word.py
# 公众号/B站/小红书/抖音: 程序员晚枫
# Mail: 1957875073@qq.com
# Created Time:  2022-4-25 10:17:34
# Description: 有关word的自动化操作
#############################################
# from office.lib.utils.except_utils import except_dec
# from office.core.WordType import MainWord

# 创建对象
# mainWord = MainWord()
import poword

# 1、文件的批量转换
# 自己指定路径，
# 为了适配wps不能转换doc的问题，这里限定：只能转换docx
# @except_dec()
from office.lib.decorator_utils.instruction_url import instruction
import win32com.client as win32
from pathlib import Path


@instruction
def docx2pdf(path):
    poword.docx2pdf(path)


@instruction
def merge4docx(input_path, output_path, new_word_name='merge4docx'):
    folder_path = input_path
    save_path = output_path + '\\' + new_word_name
    print('-' * 10 + '开始合并!' + '-' * 10)
    word = win32.gencache.EnsureDispatch('Word.Application')  # 打开word程序
    word.Visible = False  # 是否可视化
    folder = Path(folder_path)
    files = [path for path in folder.iterdir()]
    output = word.Documents.Add()  # 新建合并后的文档
    for file in files:
        output.Application.Selection.InsertFile(file)  # 拼接文档
    output.SaveAs(save_path)  # 保存
    output.Close()
    print('-' * 10 + '合并完成!' + '-' * 10)
