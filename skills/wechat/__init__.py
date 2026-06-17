# -*- coding: UTF-8 -*-
"""WeChat Skills 包 - 统一暴露微信自动化相关的所有 Skills"""
from office.skills.wechat.send_message import send_message
from office.skills.wechat.send_message_by_time import send_message_by_time
from office.skills.wechat.chat_by_keywords import chat_by_keywords
from office.skills.wechat.send_file import send_file
from office.skills.wechat.group_send import group_send
from office.skills.wechat.receive_message import receive_message
from office.skills.wechat.chat_robot import chat_robot

__all__ = [
    'send_message',
    'send_message_by_time',
    'chat_by_keywords',
    'send_file',
    'group_send',
    'receive_message',
    'chat_robot',
]
