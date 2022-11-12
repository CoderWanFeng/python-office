#!/usr/bin/env python
# -*- coding:utf-8 -*-

#############################################
# File Name: 图片.py
# Mail: 1957875073@qq.com
# Created Time:  2022-4-25 10:17:34
# Description: 有关 图片 的自动化操作
#############################################
import poimage


# from office.core.ImageType import MainImage
# from office.lib.utils.except_utils import except_dec

# mainImage = MainImage()


# @except_dec()
def image2gif():
    poimage.image2gif()


# todo：输出文件路径
# @except_dec()
def add_watermark(file, mark, output_path=r'./', out="mark_img", color="#8B8B1B", size=30, opacity=0.15, space=75,
                  angle=30):
    poimage.add_watermark(file, mark, output_path, out, color, size, opacity, space, angle)
    # mainImage.add_watermark(file, mark, out, color, size, opacity, space, angle)


# todo：输入文件路径
# @except_dec()
def img2Cartoon(path, client_api='OVALewIvPyLmiNITnceIhrYf', client_secret='rpBQH8WuXP4ldRQo5tbDkv3t0VgzwvCN'):
    poimage.img2Cartoon(path, client_api, client_secret)
    # mainImage.img2Cartoon(path, client_api, client_secret)


# @except_dec()
def down4img(url, output_path='.', output_name='down4img', type='jpg'):
    poimage.down4img(url, output_path, output_name, type)
    # mainImage.down4img(url, output_name, type)


def txt2wordcloud(filename, color="white", result_file="your_wordcloud.png"):
    poimage.txt2wordcloud(filename, color, result_file)


def pencil4img(input_img, output_path='./', output_name='pencil4img.jpg'):
    poimage.pencil4img(input_img, output_path, output_name)


def decode_qrcode(qrcode_path):
    """
    解析二维码
    :param qrcode_path: 二维码图片的路径
    :return:
    """
    poimage.decode_qrcode(qrcode_path)
