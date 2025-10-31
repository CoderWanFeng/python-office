# -*- coding: UTF-8 -*-


import PyOfficeRobot

def send_message(who: str, message: str):
    """发送消息给指定联系人。
    
    Args:
        who (str): 接收消息的联系人名称
        message (str): 要发送的消息内容
    
    Returns:
        None
    """
    PyOfficeRobot.chat.send_message(who, message)


def send_message_by_time(who, message, time):
    """在指定时间发送消息给指定联系人。
    
    Args:
        who (str): 接收消息的联系人名称
        message (str): 要发送的消息内容
        time (str): 发送消息的预定时间
    
    Returns:
        None
    """
    PyOfficeRobot.chat.send_message_by_time(who, message, time)


def chat_by_keywords(who, keywords):
    """根据关键词与指定联系人聊天。
    
    Args:
        who (str): 进行聊天的联系人名称
        keywords (list): 触发聊天的关键词列表
    
    Returns:
        None
    """
    PyOfficeRobot.chat.chat_by_keywords(who, keywords)


def send_file(who, file):
    """发送文件给指定联系人。
    
    Args:
        who (str): 接收文件的联系人名称
        file (str): 要发送的文件路径
    
    Returns:
        None
    """
    PyOfficeRobot.file.send_file(who, file)


def group_send():
    """群发消息。
    
    Returns:
        None
    """
    PyOfficeRobot.group.send()


def receive_message(who='文件传输助手', txt='userMessage.txt', output_path='./'):
    """接收微信机器人消息并保存到指定路径。
    
    该函数通过调用PyOfficeRobot库中的receive_message函数来接收微信机器人的消息，
    并将接收到的消息保存到指定的文件中。这是实现微信消息接收自动化的一种方式。
    
    Args:
        who (str, optional): 发送消息的微信联系人，默认为'文件传输助手'
        txt (str, optional): 消息内容的文本文件名，默认为'userMessage.txt'
        output_path (str, optional): 消息内容的保存路径，默认为当前目录
    
    Returns:
        None，该函数的执行结果是将消息保存到指定的文件和路径中
    """
    PyOfficeRobot.chat.receive_message(who, txt, output_path)


def chat_robot(who='程序员晚枫'):
    """智能聊天。
    
    Args:
        who (str, optional): 指定聊天对象，可以是备注名称，不支持特殊字符，默认为'程序员晚枫'
    
    Returns:
        None
    """
    PyOfficeRobot.chat.chat_robot(who)
