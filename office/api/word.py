# -*- coding: UTF-8 -*-
"""Word processing functionality module.

Word处理功能模块。

This module provides Word document processing capabilities including format conversion,
file merging, image extraction, and more.

该模块提供了Word文档处理功能，包括格式转换、文件合并、图片提取等。

Author:
    程序员晚枫

Project:
    https://www.python-office.com
"""
from pathlib import Path


def _load_poword():
    try:
        import poword
    except ModuleNotFoundError as exc:
        if exc.name != "poword":
            raise
        raise ModuleNotFoundError(
            "Word处理功能依赖 poword，该功能仅支持安装了 Microsoft Word "
            "和 poword 的 Windows 环境。"
        ) from exc
    return poword


def docx2pdf(path: str, output_path: str = None):
    """Convert Word to PDF.
    
    将Word转换为PDF。
    
    Args:
        path (str): Word file location / Word文件的位置。Supports batch processing / 支持批量处理: fill in folder location / 填写文件夹位置
        output_path (str, optional): output location after conversion / 转换后的输出位置。Will be created automatically if not exists / 如果不存在会自动创建
    
    Returns:
        None
    """
    if output_path is None:
        output_path = path
    poword = _load_poword()
    poword.docx2pdf(path=path, output_path=output_path)

def merge4docx(input_path: str, output_path: str, new_word_name: str = 'merge4docx'):
    """Merge multiple Docx files into one file.
    
    合并多个Docx文件为一个文件。
    
    Args:
        input_path (str): input file path / 输入文件的路径。Can be a single file or folder path / 可以是单个文件或文件夹路径
        output_path (str): output path for merged file / 输出合并后文件的路径
        new_word_name (str, optional): name of merged new file / 合并后新文件的名称。Default / 默认: 'merge4docx'
    
    Returns:
        None
    """
    poword = _load_poword()
    poword.merge4docx(input_path=input_path, output_path=output_path, new_word_name=new_word_name)


def doc2docx(input_path: str, output_path: str = r'./', output_name: str = None):
    """Convert Doc file to Docx file.
    
    将Doc文件转换为Docx文件。
    
    Args:
        input_path (str): input Doc file path / 输入Doc文件的路径
        output_path (str, optional): output Docx file path / 输出Docx文件的路径。Can be a directory or a .docx file path / 可以是目录或 .docx 文件路径。Default / 默认: current directory / 当前目录
        output_name (str, optional): output Docx file name / 输出Docx文件的名称。Default / 默认: original filename / 原文件名
    
    Returns:
        None
    """
    if output_name is None and Path(output_path).suffix.lower() == ".docx":
        output_file = Path(output_path)
        output_path = str(output_file.parent)
        output_name = output_file.name

    poword = _load_poword()
    poword.doc2docx(input_path=input_path, output_path=output_path, output_name=output_name)


def docx2doc(input_path: str, output_path: str = r'./', output_name: str = None):
    """Convert Docx file to Doc file.
    
    将Docx文件转换为Doc文件。
    
    Args:
        input_path (str): input Docx file path / 输入Docx文件的路径
        output_path (str, optional): output Doc file path / 输出Doc文件的路径。Default / 默认: current directory / 当前目录
        output_name (str, optional): output Doc file name / 输出Doc文件的名称。Default / 默认: original filename / 原文件名
    
    Returns:
        None
    """
    poword = _load_poword()
    poword.docx2doc(input_path=input_path, output_path=output_path, output_name=output_name)

def docx4imgs(word_path, img_path):
    """Extract images from Word document.
    
    从Word里提取图片。
    
    Args:
        word_path (str): Word document path / Word文档的路径
        img_path (str): storage location for extracted images / 提取图片的存储位置。Will automatically generate a subdirectory / 会自动根据word名称在指定文件夹下生成一个子目录
    
    Returns:
        None
    """
    poword = _load_poword()
    poword.docx4imgs(word_path=word_path, img_path=img_path)
