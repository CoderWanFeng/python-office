# -*- coding: UTF-8 -*-
"""微信机器人功能模块。

本模块按 https://www.python-office.com/modules/wechat/api 官方文档定义，
共 7 个函数，对应子包 ``PyOfficeRobot``：

    1. send_message            - 发送消息         (chat.send_message)
    2. send_message_by_time    - 定时发送         (chat.send_message_by_time)
    3. chat_by_keywords        - 关键词自动回复   (chat.chat_by_keywords)
    4. send_file               - 发送文件         (file.send_file)
    5. group_send              - 群发消息         (group.send)
    6. receive_message         - 接收消息         (chat.receive_message)
    7. chat_robot              - 智能聊天         (chat.chat_robot)

注意：微信 API 不是 ``office.wechat.*``，而是 ``PyOfficeRobot.*``。

使用提醒：
    1. 不要频繁发消息（建议间隔 1 秒以上）
    2. 不要群发广告（容易被封号）
    3. 个人微信慎用，推荐用企业微信
    4. 依赖 PC 微信客户端，仅 Windows

Author:
    程序员晚枫

Project:
    https://www.python-office.com
"""

from __future__ import annotations

from typing import Dict, Optional

import PyOfficeRobot


__all__ = [
    "send_message",
    "send_message_by_time",
    "chat_by_keywords",
    "send_file",
    "group_send",
    "receive_message",
    "chat_robot",
]


# =====================================================================
# 1. send_message - 发送消息
# =====================================================================

def send_message(who: str, message: str) -> None:
    """Send message to specified contact.

    发送消息给指定好友 / 文件传输助手 / 群。

    Documentation: https://www.python-office.com/modules/wechat/api#send_message

    Args:
        who: 好友昵称 / 群名（如 ``'文件传输助手'`` / ``'家人'``）
        message: 要发送的消息内容
    """
    PyOfficeRobot.chat.send_message(who=who, message=message)
    print(f"[python-office] send_message  → {who}: {message[:30]!r}")


# =====================================================================
# 2. send_message_by_time - 定时发送
# =====================================================================

def send_message_by_time(who: str, message: str, time: str) -> None:
    """Send message to specified contact at specified time.

    在指定时间自动发送消息给好友 / 群。

    Documentation: https://www.python-office.com/modules/wechat/api#send_message_by_time

    Args:
        who: 好友昵称 / 群名
        message: 要发送的消息内容
        time: 定时发送时间，格式 ``'YYYY-MM-DD HH:MM:SS'``，如 ``'2026-06-15 09:00:00'``
    """
    PyOfficeRobot.chat.send_message_by_time(who=who, message=message, time=time)
    print(
        f"[python-office] send_message_by_time  → {who} @ {time}: {message[:30]!r}"
    )


# =====================================================================
# 3. chat_by_keywords - 关键词自动回复
# =====================================================================

def chat_by_keywords(who: str, keywords: Dict[str, str]) -> None:
    """Auto-reply to a contact based on keyword mapping.

    根据关键词字典自动回复好友 / 群。

    Documentation: https://www.python-office.com/modules/wechat/api#chat_by_keywords

    Args:
        who: 要监听的好友 / 群名
        keywords: ``{关键词: 回复内容}`` 字典，匹配到任一关键词时自动回复
    """
    PyOfficeRobot.chat.chat_by_keywords(who=who, keywords=keywords)
    print(
        f"[python-office] chat_by_keywords  {who}: "
        f"{len(keywords)} 条规则"
    )


# =====================================================================
# 4. send_file - 发送文件
# =====================================================================

def send_file(who: str, file: str) -> None:
    """Send a file to specified contact.

    发送本地文件给好友 / 群。

    Documentation: https://www.python-office.com/modules/wechat/api#send_file

    Args:
        who: 好友昵称 / 群名
        file: 要发送的文件路径
    """
    PyOfficeRobot.file.send_file(who=who, file=file)
    print(f"[python-office] send_file  → {who}: {file}")


# =====================================================================
# 5. group_send - 群发消息
# =====================================================================

def group_send() -> None:
    """Send group messages to multiple contacts at once.

    群发消息（按预设的群组列表）。

    Documentation: https://www.python-office.com/modules/wechat/api#group_send
    """
    PyOfficeRobot.group.send()
    print("[python-office] group_send  群发消息完成")


# =====================================================================
# 6. receive_message - 接收消息
# =====================================================================

def receive_message(
    who: str = "文件传输助手",
    txt: str = "userMessage.txt",
    output_path: str = "./",
) -> str:
    """Receive WeChat messages and save to file.

    接收指定好友 / 群的消息并保存到文件。

    Documentation: https://www.python-office.com/modules/wechat/api#receive_message

    Args:
        who: 要监听的好友 / 群名。Default: ``'文件传输助手'``
        txt: 消息保存的文本文件名。Default: ``'userMessage.txt'``
        output_path: 消息文件保存目录。Default: ``'./'``

    Returns:
        str: 实际保存路径（``output_path/txt``）
    """
    PyOfficeRobot.chat.receive_message(who=who, txt=txt, output_path=output_path)
    from pathlib import Path
    out = str(Path(output_path) / txt)
    print(f"[python-office] receive_message  {who} → {out}")
    return out


# =====================================================================
# 7. chat_robot - 智能聊天
# =====================================================================

def chat_robot(who: str = "程序员晚枫") -> None:
    """Enable intelligent chat with specified contact.

    启动与指定好友的智能聊天（需配置 OpenAI Key 等模型凭据）。

    Documentation: https://www.python-office.com/modules/wechat/api#chat_robot

    Args:
        who: 聊天对象（备注名称，不支持特殊字符）。Default: ``'程序员晚枫'``
    """
    PyOfficeRobot.chat.chat_robot(who=who)
    print(f"[python-office] chat_robot  已启动智能聊天：{who}")
