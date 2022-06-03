#!/usr/bin/env python
# -*- coding:utf-8 -*-

#############################################
# File Name: 文件.py
# Mail: 1957875073@qq.com
# Created Time:  2022-4-25 10:17:34
# Description: 有关 文件 的自动化操作
#############################################


import os
from alive_progress import alive_bar


def replace4filename(path, del_content, replace_content=None):
    """
    :param path: 需要替换的文件夹路径
    :param del_content: 需要删除/替换的内容
    :param replace_content: 替换后的内容，可以不填 = 直接删除
    :return: 
    """
    # 获取该目录下所有文件，存入列表中；不包含子文件夹
    fileList = os.listdir(path)
    work_count = 0
    with alive_bar(len(fileList)) as bar:
        for old_file_name in fileList:  # 依次读取该路径下的文件名
            bar()  # 进度条
            if del_content in old_file_name:

                if replace_content:
                    new_file_name = old_file_name.replace(del_content, replace_content)
                else:
                    new_file_name = old_file_name.replace(del_content, '')
                os.rename(path + os.sep + old_file_name, path + os.sep + new_file_name)
                work_count = work_count + 1
    print("当前目录下，共有{}个文件/文件夹，本次运行共进行了{}个文件/文件夹的重命名".format(len(fileList), work_count))
    

def search_by_content(search_path, content):  # 定义 search() 函数，传入 "path" 文件路径， "target" 要查找的目标文件
    """
    获取当前路径下所有内容
    判断每个内容的类型（文件夹还是文件）
    若是文件夹则继续递归查找
    """
    glob_path = glob.glob(search_path)
    for file_path in glob_path:  # for 循环判断递归查到的内容是文件夹还是文件
        if glob.os.path.isdir(file_path):  # 若是文件夹，继续将该文件夹的路径传给 search() 函数继续递归查找
            _path = glob.os.path.join(file_path, '*')
            search_by_content(_path, content)
        else:  # 若是文件，则将该查询到的文件所在路径插入 final_result 空列表
            try:
                with open(file_path, 'r') as file:  # 利用 open() 函数读取文件，并通过 try...except... 捕获不可读的文件格式（.zip 格式）
                    if content in file.read():
                        print('该文件内，包含：【{}】'.format(content) +' | '*2+ file_path)
            except:
                continue

