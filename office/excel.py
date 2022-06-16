#!/usr/bin/env python
# -*- coding:utf-8 -*-

#############################################
# File Name: excel.py
# Mail: 1957875073@qq.com
# Created Time:  2022-4-25 10:17:34
# Description: 有关 excel 的自动化操作
#############################################
from core.ExcelType import MainExcel

mainExcel = MainExcel()


def fake2excel(columns=['name'], rows=1, language='zh_CN', path='./fake2excel.xlsx'):
    mainExcel.fake2excel(columns, rows, language, path)
