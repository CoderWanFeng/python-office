# -*- coding: UTF-8 -*-
"""Ruiming Skills 包 - 统一暴露 Ruiming（testApi）相关的所有 Skills"""
from office.skills.ruiming.screen_unmarked_image import screen_unmarked_image
from office.skills.ruiming.change_label_in_xml import change_label_in_xml
from office.skills.ruiming.screen_without_label_json_file import screen_without_label_json_file

__all__ = [
    'screen_unmarked_image',
    'change_label_in_xml',
    'screen_without_label_json_file',
]
