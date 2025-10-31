# -*- coding: UTF-8 -*-
"""文件处理功能模块。

该模块提供了丰富的文件管理功能，包括批量重命名、文件搜索、目录整理等。

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
    """批量重命名 1：批量修改文件/文件夹名称。
    
    Args:
        path (str): 需要修改文件夹/文件名称的根目录，注意：该根目录名称不会被修改
        del_content (str): 需要替换/删除的内容
        replace_content (str, optional): 替换后的内容，不填则实现删除效果
        dir_rename (bool, optional): 是否修改文件夹名称，默认：修改
        file_rename (bool, optional): 是否修改文件名称，默认：修改
        suffix (str, optional): 指定修改的文件类型，默认：所有
    
    Returns:
        None
    """
    pofile.replace4filename(path, del_content, replace_content, dir_rename, file_rename, suffix)


# author：https://github.com/CoderWanFeng/python-office/pull/72
def file_name_insert_content(file_path: str, insert_position: int, insert_content: str):
    """批量重命名 2：在文件名中间插入字符。
    
    Args:
        file_path (str): 文件路径
        insert_position (int): 插入位置
        insert_content (str): 插入的内容
    
    Returns:
        None
    """
    pofile.file_name_insert_content(file_path, insert_position, insert_content)


# author：https://github.com/CoderWanFeng/python-office/pull/72
def file_name_add_prefix(file_path: str, prefix_content: str):
    """批量重命名 3：给文件名给增加前缀。
    
    Args:
        file_path (str): 文件路径
        prefix_content (str): 前缀内容
    
    Returns:
        None
    """
    pofile.file_name_add_prefix(file_path, prefix_content)


# author：https://github.com/CoderWanFeng/python-office/pull/72
def file_name_add_postfix(file_path, postfix_content):
    """批量重命名 4：给文件名给增加后缀。
    
    Args:
        file_path (str): 文件路径
        postfix_content (str): 后缀内容
    
    Returns:
        None
    """
    pofile.file_name_add_postfix(file_path, postfix_content)


def output_file_list_to_excel(dir_path):
    """整理当前文件夹下的文件名，到一个Excel里。
    
    Args:
        dir_path (str): 目录路径
    
    Returns:
        None
    """
    pofile.output_file_list_to_excel(dir_path)


def add_line_by_type(add_line_dict: dict, file_path, file_type='.py', output_path=r'add_line'):
    """根据类型添加行。
    
    TODO：忘记功能了，待测试
    
    Args:
        add_line_dict (dict): 添加行的字典
        file_path (str): 文件路径
        file_type (str, optional): 文件类型，默认为'.py'
        output_path (str, optional): 输出路径，默认为'add_line'
    
    Returns:
        None
    """
    pofile.add_line_by_type(add_line_dict, file_path, file_type, output_path)


# author：https://github.com/CoderWanFeng/python-office/pull/74
def search_specify_type_file(file_path, file_type):
    """当前路径下，搜索指定类型的文件。
    
    Args:
        file_path (str): 文件路径
        file_type (str): 文件类型
    
    Returns:
        None
    """
    pofile.search_specify_type_file(file_path, file_type)


def group_by_name(path, output_path=None, del_old_file=None):
    """按名称分组。
    
    TODO：忘记功能了，待测试
    
    Args:
        path (str): 路径
        output_path (str, optional): 输出路径
        del_old_file (bool, optional): 是否删除旧文件
    
    Returns:
        None
    """
    pofile.group_by_name(path, output_path, del_old_file)


def get_files(path: str, name: str = '', suffix: str = None, sub: bool = False, level: int = 0) -> list:
    """搜索当前路径下，所有指定类型的文件，并以列表的形式返回。
    
    Args:
        path (str): 路径
        name (str, optional): 文件名
        suffix (str, optional): 文件后缀
        sub (bool, optional): 是否搜索子目录
        level (int, optional): 搜索层级
    
    Returns:
        list: 文件路径列表
    """
    return pofile.get_files(path, name, suffix, sub, level)
