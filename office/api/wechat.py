# -*- coding: UTF-8 -*-
"""WeChat automation functionality module.

微信自动化功能模块。

This module provides WeChat automation capabilities including sending messages,
sending files, scheduled messages, keyword-based chat, and more.

该模块提供了微信自动化功能，包括发送消息、发送文件、定时消息、关键词聊天等。

Author:
    程序员晚枫

Project:
    https://www.python-office.com
"""


import PyOfficeRobot

def send_message(who: str, message: str):
    """Send message to specified contact.
    
    发送消息给指定联系人。
    
    Args:
        who (str): contact name to receive message / 接收消息的联系人名称
        message (str): message content to send / 要发送的消息内容
    
    Returns:
        None
    """
    PyOfficeRobot.chat.send_message(who=who, message=message)


def send_message_by_time(who, message, time):
    """Send message to specified contact at specified time.
    
    在指定时间发送消息给指定联系人。
    
    Args:
        who (str): contact name to receive message / 接收消息的联系人名称
        message (str): message content to send / 要发送的消息内容
        time (str): scheduled time to send message / 发送消息的预定时间
    
    Returns:
        None
    """
    PyOfficeRobot.chat.send_message_by_time(who=who, message=message, time=time)


def chat_by_keywords(who, keywords):
    """Chat with specified contact based on keywords.
    
    根据关键词与指定联系人聊天。
    
    Args:
        who (str): contact name for chatting / 进行聊天的联系人名称
        keywords (list): keyword list to trigger chat / 触发聊天的关键词列表
    
    Returns:
        None
    """
    PyOfficeRobot.chat.chat_by_keywords(who=who, keywords=keywords)


def send_file(who, file):
    """Send file to specified contact.
    
    发送文件给指定联系人。
    
    Args:
        who (str): contact name to receive file / 接收文件的联系人名称
        file (str): file path to send / 要发送的文件路径
    
    Returns:
        None
    """
    PyOfficeRobot.file.send_file(who=who, file=file)


def group_send():
    """Send group messages.
    
    群发消息。
    
    Returns:
        None
    """
    PyOfficeRobot.group.send()


def receive_message(who='文件传输助手', txt='userMessage.txt', output_path='./'):
    """Receive WeChat robot messages and save to specified path.
    
    接收微信机器人消息并保存到指定路径。
    
    This function receives messages from WeChat robot by calling receive_message function in PyOfficeRobot library,
    and saves received messages to specified file. This is a way to automate WeChat message reception.
    
    该函数通过调用PyOfficeRobot库中的receive_message函数来接收微信机器人的消息，
    并将接收到的消息保存到指定的文件中。这是实现微信消息接收自动化的一种方式。
    
    Args:
        who (str, optional): WeChat contact who sent message / 发送消息的微信联系人。Default / 默认: '文件传输助手'
        txt (str, optional): message content text filename / 消息内容的文本文件名。Default / 默认: 'userMessage.txt'
        output_path (str, optional): message content save path / 消息内容的保存路径。Default / 默认: current directory / 当前目录
    
    Returns:
        None: function result is saving messages to specified file and path / 函数的执行结果是将消息保存到指定的文件和路径中
    """
    PyOfficeRobot.chat.receive_message(who=who, txt=txt, output_path=output_path)


def chat_robot(who='程序员晚枫'):
    """Intelligent chat.
    
    智能聊天。
    
    Args:
        who (str, optional): specify chat target / 指定聊天对象。Can be remark name, does not support special characters / 可以是备注名称，不支持特殊字符。Default / 默认: '程序员晚枫'
    
    Returns:
        None
    """
    PyOfficeRobot.chat.chat_robot(who=who)
