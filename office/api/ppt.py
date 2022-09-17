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
def ppt2pdf(path: str):
    poppt.ppt2pdf(path)
