# -*- coding: UTF-8 -*-
"""WeChat Skills 包 - 统一暴露微信自动化相关的所有 Skills"""
from .send_message import send_message
from .send_message_by_time import send_message_by_time
from .chat_by_keywords import chat_by_keywords
from .send_file import send_file
from .group_send import group_send
from .receive_message import receive_message
from .chat_robot import chat_robot

__all__ = [
    'send_message',
    'send_message_by_time',
    'chat_by_keywords',
    'send_file',
    'group_send',
    'receive_message',
    'chat_robot',
]
