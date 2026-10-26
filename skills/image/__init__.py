# -*- coding: UTF-8 -*-
"""Image Skills 包 - 统一暴露图像处理相关的所有 Skills"""
from .compress_image import compress_image
from .image2gif import image2gif
from .add_watermark import add_watermark
from .img2Cartoon import img2Cartoon
from .down4img import down4img
from .txt2wordcloud import txt2wordcloud
from .pencil4img import pencil4img
from .decode_qrcode import decode_qrcode
from .del_watermark import del_watermark

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
