# -*- coding: UTF-8 -*-
"""Image Skills 包 - 统一暴露图像处理相关的所有 Skills"""
from office.skills.image.compress_image import compress_image
from office.skills.image.image2gif import image2gif
from office.skills.image.add_watermark import add_watermark
from office.skills.image.img2Cartoon import img2Cartoon
from office.skills.image.down4img import down4img
from office.skills.image.txt2wordcloud import txt2wordcloud
from office.skills.image.pencil4img import pencil4img
from office.skills.image.decode_qrcode import decode_qrcode
from office.skills.image.del_watermark import del_watermark

__all__ = [
    'compress_image',
    'image2gif',
    'add_watermark',
    'img2Cartoon',
    'down4img',
    'txt2wordcloud',
    'pencil4img',
    'decode_qrcode',
    'del_watermark',
]
