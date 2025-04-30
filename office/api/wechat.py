# -*- coding: UTF-8 -*-


import PyOfficeRobot


def send_message(who: str, message: str):
    PyOfficeRobot.chat.send_message(who, message)


def send_message_by_time(who, message, time):
    PyOfficeRobot.chat.send_message_by_time(who, message, time)


def chat_by_keywords(who, keywords):
    PyOfficeRobot.chat.chat_by_keywords(who, keywords)


def send_file(who, file):
    PyOfficeRobot.file.send_file(who, file)


def group_send():
    PyOfficeRobot.group.send()


# 保存指定人的消息
# BY：盖飞

def receive_message(who='文件传输助手', txt='userMessage.txt', output_path='./'):
    PyOfficeRobot.chat.receive_message(who, txt, output_path)


def chat_robot(who='程序员晚枫'):
    """
    智能聊天
    Args:
        who: 指定聊天对象，可以是备注名称。不支持特殊字符。 

    Returns:

    """
    PyOfficeRobot.chat.chat_robot(who)
