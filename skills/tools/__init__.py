# -*- coding: UTF-8 -*-
"""Tools Skills 包 - 统一暴露工具类相关的所有 Skills"""
from .transtools import transtools
from .qrcodetools import qrcodetools
from .passwordtools import passwordtools
from .weather import weather
from .url2ip import url2ip
from .lottery8ticket import lottery8ticket
from .create_article import create_article
from .pwd4wifi import pwd4wifi
from .net_speed_test import net_speed_test
from .course import course

__all__ = [
    'transtools',
    'qrcodetools',
    'passwordtools',
    'weather',
    'url2ip',
    'lottery8ticket',
    'create_article',
    'pwd4wifi',
    'net_speed_test',
    'course',
]
