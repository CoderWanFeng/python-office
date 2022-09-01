#!/usr/bin/env python
# -*- coding:utf-8 -*-

#############################################
# File Name: word.py
# Author: 程序员晚枫
# Mail: 1957875073@qq.com
# Created Time:  2022-4-25 10:17:34
# Description: 有关word的自动化操作
#############################################
from office.lib.utils.except_utils import except_dec

from office.core.WordType import MainWord

# 创建对象
mainWord = MainWord()


# 1、文件的批量转换
# 自己指定路径，
# 为了适配wps不能转换doc的问题，这里限定：只能转换docx
@except_dec()
def docx2pdf(path):
    mainWord.file2pdf(path)
