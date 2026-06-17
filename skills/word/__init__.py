# -*- coding: UTF-8 -*-
"""Word Skills 包 - 统一暴露 Word 处理相关的所有 Skills"""
from office.skills.word.docx2pdf import docx2pdf
from office.skills.word.merge4docx import merge4docx
from office.skills.word.doc2docx import doc2docx
from office.skills.word.docx2doc import docx2doc
from office.skills.word.docx4imgs import docx4imgs

__all__ = [
    'docx2pdf',
    'merge4docx',
    'doc2docx',
    'docx2doc',
    'docx4imgs',
]
