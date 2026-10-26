# -*- coding: UTF-8 -*-
"""PPT Skills 包 - 统一暴露 PPT 处理相关的所有 Skills"""
from .ppt2pdf import ppt2pdf
from .ppt2img import ppt2img
from .merge4ppt import merge4ppt

__all__ = [
    'ppt2pdf',
    'ppt2img',
    'merge4ppt',
]
