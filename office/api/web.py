#!/usr/bin/env python
# -*- coding:utf-8 -*-

#############################################
# File Name: 网站开发.py
# Mail: 1957875073@qq.com
# Created Time:  2022-4-25 10:17:34
# Description: 有关 网站开发 的自动化操作
#############################################

import pospider


def url2ebook(url, tile):
    pospider.url.url2ebook(url, tile)
