#!/usr/bin/env python
# -*- coding:utf-8 -*-

#############################################
# File Name: ppt.py
# Mail: 1957875073@qq.com
# Created Time:  2022-4-25 10:17:34
# Description: 有关 ppt 的自动化操作
#############################################
from office.core.PPTType import MainPPT

mainPPT = MainPPT()


def ppt2pdf(path):
    mainPPT.ppt2pdf(path)
