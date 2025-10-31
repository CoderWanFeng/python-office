# -*- coding: UTF-8 -*-
"""PDF处理功能模块。

该模块提供了丰富的PDF文件处理功能，包括格式转换、加密解密、水印添加等。

主要功能：
- pdf2docx: PDF转Word文档
- pdf2imgs: PDF转图片
- txt2pdf: 文本文件转PDF
- split4pdf: 拆分PDF文件
- encrypt4pdf: 加密PDF文件
- decrypt4pdf: 解密PDF文件
- add_text_watermark: 添加文本水印
- merge2pdf: 合并多个PDF文件
- del4pdf: 删除PDF指定页面
- add_watermark_by_parameters: 参数化添加水印

Author:
    程序员晚枫

Project:
    https://www.python-office.com
"""

import popdf


def pdf2docx(input_file, output_path='.'):
    """PDF转Word。
    
    文档：http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/1-pdf2docx/
    
    Args:
        input_file (str): PDF文件路径
        output_path (str, optional): 输出Word文件路径，默认为当前目录
    
    Returns:
        None
    """
    popdf.pdf2docx(input_file, output_path)


def pdf2imgs(input_file, output_path, merge=False):
    """PDF转图片。
    
    文档：http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/2-pdf2imgs/
    
    Args:
        input_file (str): PDF文件路径
        output_path (str): 输出图片路径
        merge (bool, optional): 是否合并为一张图片，默认为False
    
    Returns:
        None
    """
    popdf.pdf2imgs(input_file, output_path, merge)


def txt2pdf(input_file: str, output_file='txt2pdf.pdf'):
    """将文本文件转换为PDF文件。
    
    文档：http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/3-txt2pdf/
    
    Args:
        input_file (str): 文本文件路径
        output_file (str, optional): 输出PDF文件路径，默认为'txt2pdf.pdf'
    
    Returns:
        None
    """

    popdf.txt2pdf(input_file, output_file)


def split4pdf(input_file, output_file=r'./output_path/split_pdf.pdf', from_page=-1, to_page=-1):
    """拆分PDF文件。
    
    文档：http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/4-split4pdf/
    
    Args:
        input_file (str): PDF文件路径
        output_file (str, optional): 输出拆分后的PDF文件路径
        from_page (int, optional): 起始页码，默认为-1（从第一页开始）
        to_page (int, optional): 结束页码，默认为-1（到最后一页结束）
    
    Returns:
        None
    """
    popdf.split4pdf(input_file, output_file, from_page, to_page)


def encrypt4pdf(password, input_file=None, output_file=None, input_path=None, output_path=None):
    """加密PDF文件。
    
    该函数用于对PDF文件进行加密处理，支持设置用户密码保护PDF文件。
    
    文档：http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/5-encrypt4pdf/
    
    Args:
        password (str): PDF文件的加密密码
        input_file (str, optional): 输入的PDF文件名（包含路径）
        output_file (str, optional): 输出的加密PDF文件名（包含路径）
        input_path (str, optional): 输入文件的完整路径
        output_path (str, optional): 输出文件的完整路径
    
    Returns:
        None
    """

    popdf.encrypt4pdf(password=password, input_file=input_file, output_file=output_file, input_path=input_path,
                      output_path=output_path)


def decrypt4pdf(password, input_file=None, output_file=None, input_path=None, output_path=None):
    """解密PDF文件。
    
    文档：http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/6-decrypt4pdf
    
    Args:
        password (str): PDF文件的解密密码
        input_file (str, optional): 输入的PDF文件名（包含路径）
        output_file (str, optional): 输出的解密PDF文件名（包含路径）
        input_path (str, optional): 输入文件的完整路径
        output_path (str, optional): 输出文件的完整路径
    
    Returns:
        None
    """
    popdf.decrypt4pdf(password=password, input_file=input_file, output_file=output_file, input_path=input_path,
                      output_path=output_path)


def add_text_watermark(input_file, point, text='python-office',
                       output_file='./pdf_watermark.pdf', fontname="Helvetica", fontsize=12, color=(1, 0, 0)) -> None:
    """在PDF文档中添加文本水印。
    
    文档：http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/7-add_watermark
    
    Args:
        input_file (str): PDF文件路径
        point (tuple): 水印位置坐标
        text (str, optional): 水印文本内容，默认为'python-office'
        output_file (str, optional): 输出PDF文件路径
        fontname (str, optional): 字体名称，默认为'Helvetica'
        fontsize (int, optional): 字体大小，默认为12
        color (tuple, optional): 字体颜色，默认为红色(1, 0, 0)
    
    Returns:
        None
    """
    popdf.add_watermark(input_file, point, text,
                        output_file, fontname, fontsize, color)


def merge2pdf(input_file_list, output_file):
    """合并多个PDF文件。
    
    文档：http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/8-merge2pdf
    
    Args:
        input_file_list (list): PDF文件路径列表
        output_file (str): 合并后的PDF文件路径
    
    Returns:
        None
    """
    popdf.merge2pdf(input_file_list, output_file)


def del4pdf(input_file, output_file, page_nums):
    """删除PDF文件中的指定页面。
    
    文档：http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/9-del4pdf
    
    Args:
        input_file (str): PDF文件路径
        output_file (str): 输出PDF文件路径
        page_nums (list): 要删除的页码列表
    
    Returns:
        None
    """
    popdf.del4pdf(input_file, output_file, page_nums)


def add_img_water(pdf_file_in, pdf_file_mark, pdf_file_out):
    popdf.add_img_water(pdf_file_in, pdf_file_mark, pdf_file_out)


def add_watermark() -> None:
    popdf.add_watermark()


# 给pdf加水印-有参数

def add_mark(pdf_file, mark_str, output_path=None, output_file_name=None) -> None:
    """给PDF添加水印。
    
    Args:
        pdf_file (str): PDF文件的位置，例如：d:/code/程序员晚枫.popdf
        mark_str (str): 需要添加的水印内容，例如：百度一下：程序员晚枫
        output_path (str, optional): 保存文件的位置
        output_file_name (str, optional): 指定添加了水印的文件名称，可以不指定，默认是：添加了水印的文件.popdf
    
    Returns:
        None
    """
    popdf.add_watermark_by_parameters(pdf_file, mark_str, output_path, output_file_name)


# 给pdf加水印-有参数

def add_watermark_by_parameters(pdf_file, mark_str, output_path=None, output_file_name=None) -> None:
    """给PDF添加水印。
    
    Args:
        pdf_file (str): PDF文件的位置，例如：d:/code/程序员晚枫.popdf
        mark_str (str): 需要添加的水印内容，例如：百度一下：程序员晚枫
        output_path (str, optional): 保存文件的位置
        output_file_name (str, optional): 指定添加了水印的文件名称，可以不指定，默认是：添加了水印的文件.popdf
    
    Returns:
        None
    """
    popdf.add_watermark_by_parameters(pdf_file, mark_str, output_path, output_file_name)
