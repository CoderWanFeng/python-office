# -*- coding: UTF-8 -*-
"""File Skills 包 - 统一暴露文件处理相关的所有 Skills"""
from office.skills.file.replace4filename import replace4filename
from office.skills.file.file_name_insert_content import file_name_insert_content
from office.skills.file.file_name_add_prefix import file_name_add_prefix
from office.skills.file.file_name_add_postfix import file_name_add_postfix
from office.skills.file.output_file_list_to_excel import output_file_list_to_excel
from office.skills.file.add_line_by_type import add_line_by_type
from office.skills.file.search_specify_type_file import search_specify_type_file
from office.skills.file.group_by_name import group_by_name
from office.skills.file.get_files import get_files

__all__ = [
    'replace4filename',
    'file_name_insert_content',
    'file_name_add_prefix',
    'file_name_add_postfix',
    'output_file_list_to_excel',
    'add_line_by_type',
    'search_specify_type_file',
    'group_by_name',
    'get_files',
]
