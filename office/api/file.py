# -*- coding: UTF-8 -*-
"""File processing functionality module.

文件处理功能模块。

This module provides rich file management capabilities including batch renaming,
file searching, directory organizing, and more.

该模块提供了丰富的文件管理功能，包括批量重命名、文件搜索、目录整理等。

Main Features:
- replace4filename: Batch modify file/folder names
- file_name_insert_content: Insert characters in the middle of filename
- file_name_add_prefix: Add prefix to filename
- file_name_add_postfix: Add postfix to filename
- output_file_list_to_excel: Organize filenames to Excel
- search_specify_type_file: Search for files of specified type
- group_by_name: Group and organize files by name
- get_files: Search for files of specified type and return list

主要功能：
- replace4filename: 批量修改文件/文件夹名称
- file_name_insert_content: 在文件名中间插入字符
- file_name_add_prefix: 给文件名增加前缀
- file_name_add_postfix: 给文件名增加后缀
- output_file_list_to_excel: 整理文件名到Excel
- search_specify_type_file: 搜索指定类型文件
- group_by_name: 按名称分组整理文件
- get_files: 搜索指定类型文件并返回列表

Author:
    程序员晚枫

Project:
    https://www.python-office.com
"""

import pofile


# todo：输入文件路径


def replace4filename(path: str, del_content, replace_content='', dir_rename: bool = True,
                     file_rename: bool = True, suffix=None):
    """Batch rename: batch modify file/folder names.
    
    批量重命名：批量修改文件/文件夹名称。
    
    Args:
        path (str): root directory for files/folders to be renamed / 需要修改文件夹/文件名称的根目录。Note / 注意: the root directory name will not be modified / 该根目录名称不会被修改
        del_content (str): content to be replaced/deleted / 需要替换/删除的内容
        replace_content (str, optional): replacement content / 替换后的内容。If empty, implements deletion / 不填则实现删除效果
        dir_rename (bool, optional): whether to rename directories / 是否修改文件夹名称。Default / 默认: True / 修改
        file_rename (bool, optional): whether to rename files / 是否修改文件名称。Default / 默认: True / 修改
        suffix (str, optional): specify file type to modify / 指定修改的文件类型。Default / 默认: all / 所有
    
    Returns:
        None
    """
    pofile.replace4filename(path=path, del_content=del_content, replace_content=replace_content, dir_rename=dir_rename, file_rename=file_rename, suffix=suffix)


# author：https://github.com/CoderWanFeng/python-office/pull/72
def file_name_insert_content(file_path: str, insert_position: int, insert_content: str):
    """Batch rename: insert characters in the middle of filename.
    
    批量重命名：在文件名中间插入字符。
    
    Args:
        file_path (str): file path / 文件路径
        insert_position (int): insert position / 插入位置
        insert_content (str): content to insert / 插入的内容
    
    Returns:
        None
    """
    pofile.file_name_insert_content(file_path=file_path, insert_position=insert_position, insert_content=insert_content)


# author：https://github.com/CoderWanFeng/python-office/pull/72
def file_name_add_prefix(file_path: str, prefix_content: str):
    """Batch rename: add prefix to filename.
    
    批量重命名：给文件名增加前缀。
    
    Args:
        file_path (str): file path / 文件路径
        prefix_content (str): prefix content / 前缀内容
    
    Returns:
        None
    """
    pofile.file_name_add_prefix(file_path=file_path, prefix_content=prefix_content)


# author：https://github.com/CoderWanFeng/python-office/pull/72
def file_name_add_postfix(file_path, postfix_content):
    """Batch rename: add postfix to filename.
    
    批量重命名：给文件名增加后缀。
    
    Args:
        file_path (str): file path / 文件路径
        postfix_content (str): postfix content / 后缀内容
    
    Returns:
        None
    """
    pofile.file_name_add_postfix(file_path=file_path, postfix_content=postfix_content)


def output_file_list_to_excel(dir_path):
    """Organize filenames in current folder into an Excel file.
    
    整理当前文件夹下的文件名到一个Excel里。
    
    Args:
        dir_path (str): directory path / 目录路径
    
    Returns:
        None
    """
    pofile.output_file_list_to_excel(dir_path=dir_path)


def add_line_by_type(add_line_dict: dict, file_path, file_type='.py', output_path=r'add_line'):
    """Add lines by type.
    
    根据类型添加行。
    
    TODO: Forgotten functionality, needs testing.
    TODO：忘记功能了，待测试。
    
    Args:
        add_line_dict (dict): dictionary of lines to add / 添加行的字典
        file_path (str): file path / 文件路径
        file_type (str, optional): file type / 文件类型。Default / 默认: '.py'
        output_path (str, optional): output path / 输出路径。Default / 默认: 'add_line'
    
    Returns:
        None
    """
    pofile.add_line_by_type(add_line_dict=add_line_dict, file_path=file_path, file_type=file_type, output_path=output_path)


# author：https://github.com/CoderWanFeng/python-office/pull/74
def search_specify_type_file(file_path, file_type):
    """Search for files of specified type in current path.
    
    在当前路径下搜索指定类型的文件。
    
    Args:
        file_path (str): file path / 文件路径
        file_type (str): file type / 文件类型
    
    Returns:
        None
    """
    pofile.search_specify_type_file(file_path=file_path, file_type=file_type)


def group_by_name(path, output_path=None, del_old_file=None):
    """Group by name.
    
    按名称分组。
    
    TODO: Forgotten functionality, needs testing.
    TODO：忘记功能了，待测试。
    
    Args:
        path (str): path / 路径
        output_path (str, optional): output path / 输出路径
        del_old_file (bool, optional): whether to delete old files / 是否删除旧文件
    
    Returns:
        None
    """
    pofile.group_by_name(path=path, output_path=output_path, del_old_file=del_old_file)


def get_files(path: str, name: str = '', suffix: str = None, sub: bool = False, level: int = 0) -> list:
    """Search all files of specified type in current path and return as list.
    
    搜索当前路径下所有指定类型的文件，并以列表形式返回。
    
    Args:
        path (str): path / 路径
        name (str, optional): filename / 文件名
        suffix (str, optional): file suffix / 文件后缀
        sub (bool, optional): whether to search subdirectories / 是否搜索子目录
        level (int, optional): search level / 搜索层级
    
    Returns:
        list: list of file paths / 文件路径列表
    """
    return pofile.get_files(path=path, name=name, suffix=suffix, sub=sub, level=level)
