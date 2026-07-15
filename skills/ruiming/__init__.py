# -*- coding: UTF-8 -*-
"""Ruiming Skills 包 - 统一暴露 Ruiming（testApi）相关的所有 Skills"""
from .screen_unmarked_image import screen_unmarked_image
from .change_label_in_xml import change_label_in_xml
from .screen_without_label_json_file import screen_without_label_json_file

__all__ = [
    'screen_unmarked_image',
    'change_label_in_xml',
    'screen_without_label_json_file',
]
