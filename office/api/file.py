#!/usr/bin/env python
# -*- coding:utf-8 -*-

#############################################
# File Name: 文件.py
# Mail: 1957875073@qq.com
# Created Time:  2022-4-25 10:17:34
# Description: 有关 文件 的自动化操作
#############################################
# from office.lib.utils.except_utils import except_dec
# from office.core.FileType import pofile
# from office.core.SearchByContentType import MainSearchByContent

# pofile = pofile()
# mainSearchByContent = MainSearchByContent()
import pofile

# todo：输入文件路径
# @except_dec()
def replace4filename(path, del_content, replace_content=None):
    pofile.replace4filename(path, del_content, replace_content)


# todo：输入文件路径
# @except_dec()
def search_by_content(search_path, content):  # 定义 search() 函数，传入 "path" 文件路径， "target" 要查找的目标文件
    pofile.search_by_content(search_path, content)


# author：https://github.com/CoderWanFeng/python-office/pull/72
# @except_dec()
def file_name_insert_content(file_path, insert_position: int, insert_content: str):
    pofile.file_name_insert_content(file_path, insert_position, insert_content)


# author：https://github.com/CoderWanFeng/python-office/pull/72
# @except_dec()
def file_name_add_prefix(file_path, prefix_content):
    pofile.file_name_add_prefix(file_path, prefix_content)


# author：https://github.com/CoderWanFeng/python-office/pull/72
# @except_dec()
def file_name_add_postfix(file_path, postfix_content):
    pofile.file_name_add_postfix(file_path, postfix_content)


# author：https://github.com/CoderWanFeng/python-office/pull/74
# @except_dec()
def search_specify_type_file(file_path, file_type):
    pofile.search_specify_type_file(file_path, file_type)


# @except_dec()
def output_file_list_to_excel(dir_path):
    pofile.output_file_list_to_excel(dir_path)
