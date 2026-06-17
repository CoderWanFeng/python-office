# -*- coding: UTF-8 -*-
"""Tools Skills 包 - 统一暴露工具类相关的所有 Skills"""
from office.skills.tools.transtools import transtools
from office.skills.tools.qrcodetools import qrcodetools
from office.skills.tools.passwordtools import passwordtools
from office.skills.tools.weather import weather
from office.skills.tools.url2ip import url2ip
from office.skills.tools.lottery8ticket import lottery8ticket
from office.skills.tools.create_article import create_article
from office.skills.tools.pwd4wifi import pwd4wifi
from office.skills.tools.net_speed_test import net_speed_test
from office.skills.tools.course import course

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
