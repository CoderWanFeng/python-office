# -*- coding: UTF-8 -*-
"""File Skills 包 - 统一暴露文件处理相关的所有 Skills"""
from .replace4filename import replace4filename
from .file_name_insert_content import file_name_insert_content
from .file_name_add_prefix import file_name_add_prefix
from .file_name_add_postfix import file_name_add_postfix
from .output_file_list_to_excel import output_file_list_to_excel
from .add_line_by_type import add_line_by_type
from .search_specify_type_file import search_specify_type_file
from .group_by_name import group_by_name
from .get_files import get_files

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
