# -*- coding: UTF-8 -*-
"""Word Skills 包 - 统一暴露 Word 处理相关的所有 Skills"""
from .docx2pdf import docx2pdf
from .merge4docx import merge4docx
from .doc2docx import doc2docx
from .docx2doc import docx2doc
from .docx4imgs import docx4imgs

__all__ = [
    'docx2pdf',
    'merge4docx',
    'doc2docx',
    'docx2doc',
    'docx4imgs',
]
