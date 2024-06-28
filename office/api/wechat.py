# -*- coding: UTF-8 -*-
'''
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：CoderWanFeng
@读者群     ：http://www.python4office.cn/wechat-group/
@学习网站      ：https://www.python-office.com
@代码日期    ：2023/8/22 23:28
'''

"""
🤖10讲Python微信机器人，小白也能学会
https://www.bilibili.com/video/BV1S84y1m7xd/
"""

import PyOfficeRobot

from office.lib.decorator_utils.instruction_url import instruction


# @instruction
def send_message(who: str, message: str):
    PyOfficeRobot.chat.send_message(who, message)


# @instruction
def send_message_by_time(who, message, time):
    PyOfficeRobot.chat.send_message_by_time(who, message, time)


# @instruction
def chat_by_keywords(who, keywords):
    PyOfficeRobot.chat.chat_by_keywords(who, keywords)


# @instruction
def send_file(who, file):
    PyOfficeRobot.file.send_file(who, file)


def group_send():
    PyOfficeRobot.group.send()


# 保存指定人的消息
# BY：盖飞
# @instruction
def receive_message(who='文件传输助手', txt='userMessage.txt', output_path='./'):
    PyOfficeRobot.chat.receive_message(who, txt, output_path)


# @instruction
def chat_robot(who='程序员晚枫'):
    """
    智能聊天
    Args:
        who: 指定聊天对象，可以是备注名称。不支持特殊字符。 

    Returns:

    """
    PyOfficeRobot.chat.chat_robot(who)
