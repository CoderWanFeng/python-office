# -*- coding: UTF-8 -*-


import popdf


# todo：输入文件路径
def pdf2docx(input_file, output_path='.'):
    """
    PDF转Word
    文档：http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/1-pdf2docx/
    """
    popdf.pdf2docx(input_file, output_path)


def pdf2imgs(input_file, output_path, merge=False):
    """
    pdf转图片
    文档：http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/2-pdf2imgs/
    """
    popdf.pdf2imgs(input_file, output_path, merge)


def txt2pdf(input_file: str, output_file='txt2pdf.pdf'):
    """
    将文本文件转换为PDF文件。
    文档：http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/3-txt2pdf/
    """

    popdf.txt2pdf(input_file, output_file)


def split4pdf(input_file, output_file=r'./output_path/split_pdf.pdf', from_page=-1, to_page=-1):
    """
    拆分PDF文件
    文档：http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/4-split4pdf/
    """
    popdf.split4pdf(input_file, output_file, from_page, to_page)


def encrypt4pdf(password, input_file=None, output_file=None, input_path=None, output_path=None):
    """
    加密PDF文件

    该函数用于对PDF文件进行加密处理，支持设置用户密码保护PDF文件

    参数:
        password (str): PDF文件的加密密码
        input_file (str, optional): 输入的PDF文件名（包含路径）
        output_file (str, optional): 输出的加密PDF文件名（包含路径）
        input_path (str, optional): 输入文件的完整路径
        output_path (str, optional): 输出文件的完整路径

    返回值:
        None: 该函数不返回任何值，直接生成加密后的PDF文件

    文档：http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/5-encrypt4pdf/
    """

    popdf.encrypt4pdf(password=password, input_file=input_file, output_file=output_file, input_path=input_path,
                      output_path=output_path)


def decrypt4pdf(password, input_file=None, output_file=None, input_path=None, output_path=None):
    """
    解密pdf
    文档：http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/6-decrypt4pdf
    演示代码：
    """
    popdf.decrypt4pdf(password=password, input_file=input_file, output_file=output_file, input_path=input_path,
                      output_path=output_path)


def add_text_watermark(input_file, point, text='python-office',
                       output_file='./pdf_watermark.pdf', fontname="Helvetica", fontsize=12, color=(1, 0, 0)) -> None:
    """
    在PDF文档中添加文本水印。
    文档：http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/7-add_watermark
    """
    popdf.add_watermark(input_file, point, text,
                        output_file, fontname, fontsize, color)


def merge2pdf(input_file_list, output_file):
    """
    合并pdf
    文档：http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/8-merge2pdf
    演示代码：
    """
    popdf.merge2pdf(input_file_list, output_file)


def del4pdf(input_file, output_file, page_nums):
    """
    删除pdf页面
    文档：http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/9-del4pdf
    演示代码：
    """
    popdf.del4pdf(input_file, output_file, page_nums)


def add_img_water(pdf_file_in, pdf_file_mark, pdf_file_out):
    popdf.add_img_water(pdf_file_in, pdf_file_mark, pdf_file_out)


def add_watermark() -> None:
    popdf.add_watermark()


# 给pdf加水印-有参数

def add_mark(pdf_file, mark_str, output_path=None, output_file_name=None) -> None:
    """
    必填参数：
    pdf_file:pdf的位置，例如：d:/code/程序员晚枫.popdf
    mark_str:需要添加的水印内容，例如：百度一下：程序员晚枫
    选填参数：
    output_file_name：指定添加了水印的文件名称，可以不指定，默认是：添加了水印的文件.popdf
    """
    popdf.add_watermark_by_parameters(pdf_file, mark_str, output_path, output_file_name)


# 给pdf加水印-有参数

def add_watermark_by_parameters(pdf_file, mark_str, output_path=None, output_file_name=None) -> None:
    """
    给PDF添加水印
    Args:
        pdf_file: pdf的位置，例如：d:/code/程序员晚枫.popdf
        mark_str: 需要添加的水印内容，例如：百度一下：程序员晚枫
        output_path: 保存文件的位置
        output_file_name: 指定添加了水印的文件名称，可以不指定，默认是：添加了水印的文件.popdf

    Returns:

    """
    popdf.add_watermark_by_parameters(pdf_file, mark_str, output_path, output_file_name)
