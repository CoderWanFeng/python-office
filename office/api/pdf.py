# -*- coding: UTF-8 -*-
"""PDF processing functionality module.

PDF处理功能模块。

This module provides rich PDF file processing capabilities including format conversion,
encryption/decryption, watermark addition, and more.

该模块提供了丰富的PDF文件处理功能，包括格式转换、加密解密、水印添加等。

Main Features:
- pdf2docx: Convert PDF to Word document
- pdf2imgs: Convert PDF to images
- txt2pdf: Convert text file to PDF
- split4pdf: Split PDF file
- encrypt4pdf: Encrypt PDF file
- decrypt4pdf: Decrypt PDF file
- add_text_watermark: Add text watermark
- merge2pdf: Merge multiple PDF files
- del4pdf: Delete specific pages from PDF
- add_watermark_by_parameters: Add watermark with parameters

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

import warnings
from pathlib import Path

import popdf


def pdf2docx(input_file=None, output_file=None, input_path=None, output_path=None, file_path=None):
    """Convert PDF to Word document.

    将PDF转换为Word文档。

    Documentation: https://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/1-pdf2docx/

    Args:
        input_file (str): path to the PDF file / PDF文件路径
        output_path (str, optional): output path for Word file / 输出Word文件路径。Default / 默认: current directory / 当前目录
        file_path (str, optional): [已弃用] 请使用 input_file 参数代替 / [Deprecated] Use input_file instead

    Returns:
        None

    Note:
        参数 file_path 已被弃用，不再推荐使用。为保持向后兼容性，
        如果您使用了 file_path 参数，它将自动映射到 input_file。
        请在新代码中使用 input_file 参数。
    """
    # 处理已弃用的 file_path 参数
    if file_path is not None:
        warnings.warn(
            "参数 'file_path' 已被弃用，不再推荐使用。请改用 'input_file' 参数。",
            DeprecationWarning,
            stacklevel=2
        )
        # 为了向后兼容，使用 file_path 的值作为 input_file
        if input_file is None:
            input_file = file_path

    if input_file is not None and output_path is not None:  # 兼容1.0.1版本
        # 从 input_file 中提取文件名（不含扩展名），组合成输出文件路径
        input_path_obj = Path(input_file)
        output_file = str(Path(output_path) / f"{input_path_obj.stem}.docx")
        popdf.pdf2docx(input_file=input_file, output_file=output_file)
    elif input_file is not None and output_file is not None:  # 优先单个识别
        popdf.pdf2docx(input_file=input_file, output_file=output_file)
    elif input_path is not None and output_path is not None:
        popdf.pdf2docx(input_path=input_path, output_path=output_path)


def pdf2imgs(input_file=None, output_file=None, merge=False, pdf_path=None, out_dir=None):
    """Convert PDF to images.

    将PDF转换为图片。

    Documentation: https://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/2-pdf2imgs/

    Args:
        input_file (str, optional): path to the PDF file / PDF文件路径
        output_file (str, optional): output path for images / 输出图片路径
        merge (bool, optional): whether to merge into one image / 是否合并为一张图片。Default / 默认: False
        pdf_path (str, optional): [已弃用] 请使用 input_file 参数代替 / [Deprecated] Use input_file instead
        out_dir (str, optional): [已弃用] 请使用 output_file 参数代替 / [Deprecated] Use output_file instead

    Returns:
        None
    """
    # 处理已弃用的参数
    if pdf_path is not None:
        warnings.warn(
            "参数 'pdf_path' 已被弃用，不再推荐使用。请改用 'input_file' 参数。",
            DeprecationWarning,
            stacklevel=2
        )
        if input_file is None:
            input_file = pdf_path
    if out_dir is not None:
        warnings.warn(
            "参数 'out_dir' 已被弃用，不再推荐使用。请改用 'output_file' 参数。",
            DeprecationWarning,
            stacklevel=2
        )
        if output_file is None:
            output_file = out_dir

    popdf.pdf2imgs(input_file=input_file, output_path=output_file, merge=merge)


def txt2pdf(input_file=None, output_file=None):
    """Convert text file to PDF file.

    将文本文件转换为PDF文件。

    Documentation: https://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/3-txt2pdf/

    Args:
        input_file (str, optional): path to the text file / 文本文件路径
        output_file (str, optional): output PDF file path / 输出PDF文件路径。Default / 默认: 'txt2pdf.pdf'

    Returns:
        None
    """
    if output_file is None:
        output_file = 'txt2pdf.pdf'

    popdf.txt2pdf(input_file=input_file, output_file=output_file)


def split4pdf(input_file=None, output_file=None, from_page=-1, to_page=-1):
    """Split PDF file.

    拆分PDF文件。

    Documentation: https://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/4-split4pdf/

    Args:
        input_file (str, optional): path to the PDF file / PDF文件路径
        output_file (str, optional): output path for split PDF file / 输出拆分后的PDF文件路径。Default / 默认: './output_path/split_pdf.pdf'
        from_page (int, optional): starting page number / 起始页码。Default / 默认: -1 (from first page / 从第一页开始)
        to_page (int, optional): ending page number / 结束页码。Default / 默认: -1 (to last page / 到最后一页结束)

    Returns:
        None
    """
    if output_file is None:
        output_file = r'./output_path/split_pdf.pdf'

    popdf.split4pdf(input_file=input_file, output_file=output_file,
                    from_page=from_page, to_page=to_page)


def encrypt4pdf(password, input_file=None, output_file=None, input_path=None, output_path=None):
    """Encrypt PDF file.

    加密PDF文件。

    This function encrypts PDF files by setting a user password to protect the PDF.

    该函数用于对PDF文件进行加密处理，支持设置用户密码保护PDF文件。

    Documentation: https://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/5-encrypt4pdf/

    Args:
        password (str): encryption password for the PDF file / PDF文件的加密密码
        input_file (str, optional): input PDF file name (with path) / 输入的PDF文件名（包含路径）
        output_file (str, optional): output encrypted PDF file name (with path) / 输出的加密PDF文件名（包含路径）
        input_path (str, optional): full path to input file / 输入文件的完整路径
        output_path (str, optional): full path for output file / 输出文件的完整路径

    Returns:
        None
    """

    popdf.encrypt4pdf(password=password, input_file=input_file, output_file=output_file, input_path=input_path,
                      output_path=output_path)


def decrypt4pdf(password, input_file=None, output_file=None, input_path=None, output_path=None):
    """Decrypt PDF file.

    解密PDF文件。

    Documentation: https://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/6-decrypt4pdf

    Args:
        password (str): decryption password for the PDF file / PDF文件的解密密码
        input_file (str, optional): input PDF file name (with path) / 输入的PDF文件名（包含路径）
        output_file (str, optional): output decrypted PDF file name (with path) / 输出的解密PDF文件名（包含路径）
        input_path (str, optional): full path to input file / 输入文件的完整路径
        output_path (str, optional): full path for output file / 输出文件的完整路径

    Returns:
        None
    """
    popdf.decrypt4pdf(password=password, input_file=input_file, output_file=output_file, input_path=input_path,
                      output_path=output_path)


def add_text_watermark(input_file=None, point=None, text='python-office',
                       output_file=None, fontname="Helvetica", fontsize=12, color=(1, 0, 0)) -> None:
    """Add text watermark to PDF document.

    在PDF文档中添加文本水印。

    Documentation: https://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/7-add_watermark

    Args:
        input_file (str, optional): path to the PDF file / PDF文件路径
        point (tuple, optional): coordinates for watermark position / 水印位置坐标
        text (str, optional): watermark text content / 水印文本内容。Default / 默认: 'python-office'
        output_file (str, optional): output PDF file path / 输出PDF文件路径。Default / 默认: './pdf_watermark.pdf'
        fontname (str, optional): font name / 字体名称。Default / 默认: 'Helvetica'
        fontsize (int, optional): font size / 字体大小。Default / 默认: 12
        color (tuple, optional): font color / 字体颜色。Default / 默认: red / 红色 (1, 0, 0)

    Returns:
        None
    """
    if output_file is None:
        output_file = './pdf_watermark.pdf'

    popdf.add_watermark(input_file=input_file, point=point, text=text,
                        output_file=output_file, fontname=fontname, fontsize=fontsize, color=color)


def merge2pdf(input_file_list=None, output_file=None, one_by_one=None, output=None):
    """Merge multiple PDF files.

    合并多个PDF文件。

    Documentation: https://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/8-merge2pdf

    Args:
        input_file_list (list, optional): list of PDF file paths / PDF文件路径列表
        output_file (str, optional): output merged PDF file path / 合并后的PDF文件路径
        one_by_one (list, optional): [已弃用] 请使用 input_file_list 参数代替 / [Deprecated] Use input_file_list instead
        output (str, optional): [已弃用] 请使用 output_file 参数代替 / [Deprecated] Use output_file instead

    Returns:
        None
    """
    # 处理已弃用的参数
    if one_by_one is not None:
        warnings.warn(
            "参数 'one_by_one' 已被弃用，不再推荐使用。请改用 'input_file_list' 参数。",
            DeprecationWarning,
            stacklevel=2
        )
        if input_file_list is None:
            input_file_list = one_by_one
    if output is not None:
        warnings.warn(
            "参数 'output' 已被弃用，不再推荐使用。请改用 'output_file' 参数。",
            DeprecationWarning,
            stacklevel=2
        )
        if output_file is None:
            output_file = output

    popdf.merge2pdf(input_file_list=input_file_list, output_file=output_file)


def del4pdf(input_file=None, output_file=None, page_nums=None):
    """Delete specific pages from PDF file.

    删除PDF文件中的指定页面。

    Documentation: https://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/9-del4pdf

    Args:
        input_file (str, optional): path to the PDF file / PDF文件路径
        output_file (str, optional): output PDF file path / 输出PDF文件路径
        page_nums (list, optional): list of page numbers to delete / 要删除的页码列表

    Returns:
        None
    """
    popdf.del4pdf(page_nums=page_nums, input_file=input_file,
                  output_file=output_file)


def add_img_water(input_file=None, mark_file=None, output_file=None, pdf_file_in=None, pdf_file_mark=None, pdf_file_out=None):
    """Add image watermark to PDF file.

    给PDF文件添加图片水印。

    Args:
        input_file (str, optional): input PDF file path / 输入PDF文件路径
        mark_file (str, optional): watermark image file path / 水印图片文件路径
        output_file (str, optional): output PDF file path / 输出PDF文件路径
        pdf_file_in (str, optional): [已弃用] 请使用 input_file 参数代替 / [Deprecated] Use input_file instead
        pdf_file_mark (str, optional): [已弃用] 请使用 mark_file 参数代替 / [Deprecated] Use mark_file instead
        pdf_file_out (str, optional): [已弃用] 请使用 output_file 参数代替 / [Deprecated] Use output_file instead

    Returns:
        None
    """
    # 处理已弃用的参数
    if pdf_file_in is not None:
        warnings.warn(
            "参数 'pdf_file_in' 已被弃用，不再推荐使用。请改用 'input_file' 参数。",
            DeprecationWarning,
            stacklevel=2
        )
        if input_file is None:
            input_file = pdf_file_in
    if pdf_file_mark is not None:
        warnings.warn(
            "参数 'pdf_file_mark' 已被弃用，不再推荐使用。请改用 'mark_file' 参数。",
            DeprecationWarning,
            stacklevel=2
        )
        if mark_file is None:
            mark_file = pdf_file_mark
    if pdf_file_out is not None:
        warnings.warn(
            "参数 'pdf_file_out' 已被弃用，不再推荐使用。请改用 'output_file' 参数。",
            DeprecationWarning,
            stacklevel=2
        )
        if output_file is None:
            output_file = pdf_file_out

    popdf.add_img_water(pdf_file_in=input_file, pdf_file_mark=mark_file, pdf_file_out=output_file)


def add_watermark() -> None:
    """Add watermark to PDF (interactive mode).

    给PDF添加水印（交互模式）。

    Returns:
        None
    """


# 给pdf加水印-有参数

def add_mark(input_file=None, mark_str=None, output_path=None, output_file=None, pdf_file=None, output_file_name=None) -> None:
    """Add watermark to PDF.

    给PDF添加水印。

    Args:
        input_file (str, optional): path to PDF file / PDF文件的位置，e.g. / 例如：d:/code/programmer.pdf
        mark_str (str, optional): watermark content to add / 需要添加的水印内容，e.g. / 例如："python-office"
        output_path (str, optional): save directory path / 保存文件的位置
        output_file (str, optional): name for output file with watermark / 指定添加了水印的文件名称。Default / 默认: watermarked file.pdf / 添加了水印的文件.pdf
        pdf_file (str, optional): [已弃用] 请使用 input_file 参数代替 / [Deprecated] Use input_file instead
        output_file_name (str, optional): [已弃用] 请使用 output_file 参数代替 / [Deprecated] Use output_file instead

    Returns:
        None
    """
    # 处理已弃用的参数
    if pdf_file is not None:
        warnings.warn(
            "参数 'pdf_file' 已被弃用，不再推荐使用。请改用 'input_file' 参数。",
            DeprecationWarning,
            stacklevel=2
        )
        if input_file is None:
            input_file = pdf_file
    if output_file_name is not None:
        warnings.warn(
            "参数 'output_file_name' 已被弃用，不再推荐使用。请改用 'output_file' 参数。",
            DeprecationWarning,
            stacklevel=2
        )
        if output_file is None:
            output_file = output_file_name

    popdf.add_watermark_by_parameters(pdf_file=input_file, mark_str=mark_str, output_path=output_path,
                                      output_file_name=output_file)


# 给pdf加水印-有参数

def add_watermark_by_parameters(input_file=None, mark_str=None, output_path=None, output_file=None, pdf_file=None, output_file_name=None) -> None:
    """Add watermark to PDF with parameters.

    给PDF添加水印（带参数）。

    Args:
        input_file (str, optional): path to PDF file / PDF文件的位置，e.g. / 例如：d:/code/programmer.pdf
        mark_str (str, optional): watermark content to add / 需要添加的水印内容，e.g. / 例如："python-office"
        output_path (str, optional): save directory path / 保存文件的位置
        output_file (str, optional): name for output file with watermark / 指定添加了水印的文件名称。Default / 默认: watermarked file.pdf / 添加了水印的文件.pdf
        pdf_file (str, optional): [已弃用] 请使用 input_file 参数代替 / [Deprecated] Use input_file instead
        output_file_name (str, optional): [已弃用] 请使用 output_file 参数代替 / [Deprecated] Use output_file instead

    Returns:
        None
    """
    # 处理已弃用的参数
    if pdf_file is not None:
        warnings.warn(
            "参数 'pdf_file' 已被弃用，不再推荐使用。请改用 'input_file' 参数。",
            DeprecationWarning,
            stacklevel=2
        )
        if input_file is None:
            input_file = pdf_file
    if output_file_name is not None:
        warnings.warn(
            "参数 'output_file_name' 已被弃用，不再推荐使用。请改用 'output_file' 参数。",
            DeprecationWarning,
            stacklevel=2
        )
        if output_file is None:
            output_file = output_file_name

    popdf.add_watermark_by_parameters(pdf_file=input_file, mark_str=mark_str, output_path=output_path,
                                      output_file_name=output_file)
