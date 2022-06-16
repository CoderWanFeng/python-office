#!/usr/bin/env python
# -*- coding:utf-8 -*-

#############################################
# File Name: 图片.py
# Mail: 1957875073@qq.com
# Created Time:  2022-4-25 10:17:34
# Description: 有关 图片 的自动化操作
#############################################
from core.ImageType import MainImage

mainImage = MainImage()


def image2gif():
    mainImage.image2gif()


def add_watermark(file, mark, out="output", color="#8B8B1B", size=30, opacity=0.15, space=75, angle=30):
    mainImage.add_watermark(file, mark, out, color, size, opacity, space, angle)
