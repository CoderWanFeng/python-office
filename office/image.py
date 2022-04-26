#!/usr/bin/env python
# -*- coding:utf-8 -*-

#############################################
# File Name: 图片.py
# Mail: 1957875073@qq.com
# Created Time:  2022-4-25 10:17:34
# Description: 有关 图片 的自动化操作
#############################################


from PIL import Image


# 自动生成gif
def image2gif():
    im = Image.open("1.jpg")
    images = []
    images.append(Image.open('2.jpg'))
    images.append(Image.open('3.jpg'))
    im.save('gif.gif', save_all=True, append_images=images, loop=1, duration=1, comment=b"aaabb")
