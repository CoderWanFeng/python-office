# -*- coding: UTF-8 -*-
"""PPT Skills 包 - 统一暴露 PPT 处理相关的所有 Skills"""
from office.skills.ppt.ppt2pdf import ppt2pdf
from office.skills.ppt.ppt2img import ppt2img
from office.skills.ppt.merge4ppt import merge4ppt

__all__ = [
    'ppt2pdf',
    'ppt2img',
    'merge4ppt',
]
