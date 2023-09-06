# -*- coding: UTF-8 -*-
'''
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@微信     ：CoderWanFeng : https://mp.weixin.qq.com/s/B1V6KeXc7IOEB8DgXLWv3g
@个人网站      ：www.python-office.com
@代码日期    ：2023/8/22 23:28
'''

import PyOfficeRobot

from office.lib.decorator_utils.instruction_url import instruction



@instruction
def send_message(who: str, message: str):
    PyOfficeRobot.chat.send_message(who, message)


@instruction
def send_message_by_time(who, message, time):
    PyOfficeRobot.chat.send_message_by_time(who, message, time)


@instruction
def chat_by_keywords(who, keywords):
    PyOfficeRobot.chat.chat_by_keywords(who, keywords)


@instruction
def send_file(who, file):
    print(single_video)
    # PyOfficeRobot.file.send_file(who, file)


# 保存指定人的消息
# BY：盖飞
@instruction
def receive_message(who='文件传输助手', txt='userMessage.txt', output_path='./'):
    PyOfficeRobot.chat.receive_message(who, txt, output_path)


@instruction
def chat_robot(who='程序员晚枫'):
    """
    智能聊天
    Args:
        who: 指定聊天对象，可以是备注名称。不支持特殊字符。 

    Returns:

    """
    PyOfficeRobot.chat.chat_robot(who)
