#!/usr/bin/env python
# -*- coding:utf-8 -*-

#############################################
# File Name: excel.py
# Mail: 1957875073@qq.com
# Created Time:  2022-4-25 10:17:34
# Description: 有关 excel 的自动化操作
#############################################
from office.core.ExcelType import MainExcel
from office.lib.utils.except_utils import except_dec

mainExcel = MainExcel()


# todo:输出文件路径
@except_dec()
def fake2excel(columns=['name'], rows=1, path='./fake2excel.xlsx', language='zh_CN'):
    mainExcel.fake2excel(columns, rows, path, language)


# 多个excel，合并到一个excel的不同sheet中
@except_dec()
def merge2excel(dir_path, output_file='merge2excel.xlsx'):
    """
    :param dir_path:
    :param output_file:
    :return:
    """
    mainExcel.merge2excel(dir_path, output_file)


# 同一个excel里的不同sheet，拆分为不同的excel文件
@except_dec()
def sheet2excel(file_path):
    mainExcel.sheet2excel(file_path)


@except_dec()
def merge2sheet(dir_path, output_sheet_name: str = 'Sheet1', output_excel_name: str = 'merge2sheet'):
    mainExcel.merge2sheet(dir_path, output_sheet_name, output_excel_name)


# 搜索excel中指定内容的文件、行数、内容详情
# 作者：https://gitee.com/bulabean
# @except_dec()
def find_excel_data(search_key: str, target_dir: str):
    mainExcel.find_excel_data(search_key, target_dir)
