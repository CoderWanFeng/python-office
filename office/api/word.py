# -*- coding: UTF-8 -*-
'''
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@微信     ：CoderWanFeng : https://mp.weixin.qq.com/s/B1V6KeXc7IOEB8DgXLWv3g
@个人网站      ：www.python-office.com
@代码日期    ：2023/8/22 23:28
'''

import poword

from office.lib.decorator_utils.instruction_url import instruction


@instruction
def docx2pdf(path: str, output_path: str = None):
    """
    word转pdf
    Args:
        path: word文件的位置。支持批量处理：填写文件夹位置。
        output_path: 转换后的输出位置，如果不存在会自动创建。

    Returns:

    """
    if output_path == None:
        output_path = path
    poword.docx2pdf(path, output_path)


@instruction
def merge4docx(input_path: str, output_path: str, new_word_name: str = 'merge4docx'):
    poword.merge4docx(input_path, output_path, new_word_name)


@instruction
def doc2docx(input_path: str, output_path: str = r'./'):
    poword.doc2docx(input_path, output_path)


@instruction
def docx2doc(input_path: str, output_path: str = r'./'):
    poword.docx2doc(input_path, output_path)
