# -*- coding: UTF-8 -*-

import pofile


# todo：输入文件路径


def replace4filename(path: str, del_content, replace_content='', dir_rename: bool = True,
                     file_rename: bool = True, suffix=None):
    """
    批量重命名 1：批量修改文件/文件夹名称
    :param path: 必填，需要修改文件夹/文件名称的根目录，注意：该根目录名称不会被修改
    :param del_content: 必填，需要替换/删除的内容
    :param replace_content: 选填，替换后的内容，不填则实现删除效果
    :param dir_rename: 选填，是否修改文件夹名称，默认：修改
    :param file_rename: 选填，是否修改文件名称，默认：修改
    :param suffix: 选填，指定修改的文件类型，默认：所有
    :return:
    """
    pofile.replace4filename(path, del_content, replace_content, dir_rename, file_rename, suffix)


# author：https://github.com/CoderWanFeng/python-office/pull/72
def file_name_insert_content(file_path: str, insert_position: int, insert_content: str):
    """
    批量重命名 2：在文件名中间插入字符
    Args:
        file_path:
        insert_position:
        insert_content:

    Returns:

    """
    pofile.file_name_insert_content(file_path, insert_position, insert_content)


# author：https://github.com/CoderWanFeng/python-office/pull/72
def file_name_add_prefix(file_path: str, prefix_content: str):
    """
    批量重命名 3：给文件名给增加前缀
    Args:
        file_path:
        prefix_content:

    Returns:

    """
    pofile.file_name_add_prefix(file_path, prefix_content)


# author：https://github.com/CoderWanFeng/python-office/pull/72
def file_name_add_postfix(file_path, postfix_content):
    """
    批量重命名 4：给文件名给增加后缀
    Args:
        file_path:
        postfix_content:

    Returns:

    """
    pofile.file_name_add_postfix(file_path, postfix_content)


def output_file_list_to_excel(dir_path):
    """
    整理当前文件夹下的文件名，到一个Excel里
    Args:
        dir_path:

    Returns:

    """
    pofile.output_file_list_to_excel(dir_path)


def add_line_by_type(add_line_dict: dict, file_path, file_type='.py', output_path=r'add_line'):
    """
    #TODO：忘记功能了，待测试
    Args:
        add_line_dict:
        file_path:
        file_type:
        output_path:

    Returns:

    """
    pofile.add_line_by_type(add_line_dict, file_path, file_type, output_path)


# author：https://github.com/CoderWanFeng/python-office/pull/74
def search_specify_type_file(file_path, file_type):
    """
    当前路径下，搜索指定类型的文件
    Args:
        file_path:
        file_type:

    Returns:

    """
    pofile.search_specify_type_file(file_path, file_type)


def group_by_name(path, output_path=None, del_old_file=None):
    """
    #TODO：忘记功能了，待测试
    Args:
        path:
        output_path:
        del_old_file:

    Returns:

    """
    pofile.group_by_name(path, output_path, del_old_file)


def get_files(path: str, name: str = '', suffix: str = None, sub: bool = False, level: int = 0) -> list:
    """
    搜索当前路径下，所有指定类型的文件，并以列表的形式返回
    Args:
        path:
        name:
        suffix:
        sub:
        level:

    Returns:

    """
    return pofile.get_files(path, name, suffix, sub, level)
