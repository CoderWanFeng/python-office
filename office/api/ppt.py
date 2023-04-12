#!/usr/bin/env python
# -*- coding:utf-8 -*-

#############################################
# File Name: ppt.py
# Mail: 1957875073@qq.com
# Created Time:  2022-4-25 10:17:34
# Description: 有关 ppt 的自动化操作
#############################################
# from office.lib.utils.except_utils import except_dec
# from office.core.PPTType import MainPPT

# mainPPT = MainPPT()

import poppt

# todo：输入文件路径
# @except_dec()
from office.lib.decorator_utils.instruction_url import instruction


@instruction
def ppt2pdf(path: str, output_path=r'./'):
    poppt.ppt2pdf(path, output_path)


@instruction
def ppt2img(input_path, output_path=r'./', img_type='jpg'):
    poppt.ppt2img(input_path, output_path, img_type)
