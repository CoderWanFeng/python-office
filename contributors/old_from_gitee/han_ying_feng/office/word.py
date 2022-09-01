#!/usr/bin/env python
# -*- coding:utf-8 -*-

#############################################
# File Name: word.py
# Author: han_ying_feng
# Mail: gyuanhao@163.com
# Created Time:  2022年05月24日23:52:13
# Description: macOS下有关word的自动化操作
#############################################
from pypandoc import convert_file


def createpdf(wordPath, pdfPath):
    convert_file(wordPath, 'pdf', pdfPath)
