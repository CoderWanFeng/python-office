# -*- coding: UTF-8 -*-
'''
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@微信     ：CoderWanFeng : https://mp.weixin.qq.com/s/B1V6KeXc7IOEB8DgXLWv3g
@个人网站      ：www.python-office.com
@代码日期    ：2023/8/22 23:28
'''

import pofile
import search4file

# todo：输入文件路径
# @except_dec()
from office.lib.decorator_utils.instruction_url import instruction


@instruction
def replace4filename(path: str, del_content, replace_content='', dir_rename: bool = True,
                     file_rename: bool = True, suffix=None):
    """
    批量修改文件/文件夹名称
    :param path: 必填，需要修改文件夹/文件名称的根目录，注意：该根目录名称不会被修改
    :param del_content: 必填，需要替换/删除的内容
    :param replace_content: 选填，替换后的内容，不填则实现删除效果
    :param dir_rename: 选填，是否修改文件夹名称，默认：修改
    :param file_rename: 选填，是否修改文件名称，默认：修改
    :param suffix: 选填，指定修改的文件类型，默认：所有
    :return:
    """
    pofile.replace4filename(path, del_content, replace_content, dir_rename, file_rename, suffix)


# todo：输入文件路径
# @except_dec()
@instruction
def search_by_content(search_path: str, content: str):
    """
    通过内容搜索文件
    Args:
        search_path: 需要搜索的目录
        content: 搜索的内容

    Returns:

    """
    search4file.search_by_content(search_path=search_path, search_content=content)


# author：https://github.com/CoderWanFeng/python-office/pull/72
# @except_dec()
@instruction
def file_name_insert_content(file_path: str, insert_position: int, insert_content: str):
    pofile.file_name_insert_content(file_path, insert_position, insert_content)


# author：https://github.com/CoderWanFeng/python-office/pull/72
# @except_dec()
@instruction
def file_name_add_prefix(file_path: str, prefix_content: str):
    pofile.file_name_add_prefix(file_path, prefix_content)


# author：https://github.com/CoderWanFeng/python-office/pull/72
# @except_dec()
@instruction
def file_name_add_postfix(file_path, postfix_content):
    pofile.file_name_add_postfix(file_path, postfix_content)


# author：https://github.com/CoderWanFeng/python-office/pull/74
# @except_dec()
@instruction
def search_specify_type_file(file_path, file_type):
    pofile.search_specify_type_file(file_path, file_type)


# @except_dec()
@instruction
def output_file_list_to_excel(dir_path):
    pofile.output_file_list_to_excel(dir_path)


@instruction
def add_line_by_type(add_line_dict: dict, file_path, file_type='.py', output_path=r'add_line'):
    pofile.add_line_by_type(add_line_dict, file_path, file_type, output_path)


@instruction
def group_by_name(path, output_path=None, del_old_file=None):
    pofile.group_by_name(path, output_path, del_old_file)


@instruction
def get_files(path: str, name: str = '', suffix: str = None, sub: bool = False, level: int = 0) -> list:
    return pofile.get_files(path, name, suffix, sub, level)
