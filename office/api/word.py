# -*- coding: UTF-8 -*-

import poword


def docx2pdf(path: str, output_path: str = None):
    """
    word转pdf
    Args:
        path: word文件的位置。支持批量处理：填写文件夹位置。
        output_path: 转换后的输出位置，如果不存在会自动创建。

    Returns:

    """
    if output_path is None:
        output_path = path
    poword.docx2pdf(path, output_path)

def merge4docx(input_path: str, output_path: str, new_word_name: str = 'merge4docx'):
    """
    合并多个Docx文件为一个文件。

    参数:
    input_path: str - 输入文件的路径，可以是单个文件或文件夹路径。
    output_path: str - 输出合并后文件的路径。
    new_word_name: str - 合并后新文件的名称，默认为'merge4docx'。

    返回:
    无返回值。
    """
    poword.merge4docx(input_path, output_path, new_word_name)


def doc2docx(input_path: str, output_path: str = r'./', output_name: str = None):
    """
    将Doc文件转换为Docx文件。

    参数:
    input_path: str - 输入Doc文件的路径。
    output_path: str - 输出Docx文件的路径，默认为当前目录。
    output_name: str - 输出Docx文件的名称，默认为原文件名。

    返回:
    无返回值。
    """
    poword.doc2docx(input_path, output_path, output_name)


def docx2doc(input_path: str, output_path: str = r'./', output_name: str = None):
    """
    将Docx文件转换为Doc文件。

    参数:
    input_path: str - 输入Docx文件的路径。
    output_path: str - 输出Doc文件的路径，默认为当前目录。
    output_name: str - 输出Doc文件的名称，默认为原文件名。

    返回:
    无返回值。
    """
    poword.docx2doc(input_path, output_path, output_name)

def docx4imgs(word_path, img_path):
    """
    从Word里提取图片
    Args:
        word_path:word文档的路径
        img_path: 提取图片的存储位置，会自动根据word名称，在指定文件夹下，生成一个子目录

    Returns:

    """
    poword.docx4imgs(word_path, img_path)
