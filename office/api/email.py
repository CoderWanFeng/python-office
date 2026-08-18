# -*- coding: UTF-8 -*-
"""邮件发送 / 接收功能模块。

本模块按 https://www.python-office.com/modules/email/api 官方文档定义，
共 2 个函数，对应子包 ``poemail``：

    1. send_email     - 发送邮件（支持附件 / 抄送）
    2. receive_email  - 接收邮件

邮箱配置：

    | 邮箱  | host            | port |
    |-------|-----------------|------|
    | QQ    | smtp.qq.com     | 465  |
    | 163   | smtp.163.com    | 465  |
    | Gmail | smtp.gmail.com  | 587  |

注意：``key`` 是**邮箱授权码**，不是登录密码。

Author:
    程序员晚枫

Project:
    https://www.python-office.com
"""

from __future__ import annotations

from typing import List, Optional

from poemail.api.send import send_email as _send_email_impl
from poemail.api.receive import receive_email as _receive_email_impl


__all__ = ["send_email", "receive_email"]


# =====================================================================
# 1. send_email - 发送邮件
# =====================================================================

def send_email(
    key: str,
    msg_from: str,
    msg_to: str,
    msg_cc: Optional[str] = None,
    attach_files: Optional[List[str]] = None,
    msg_subject: str = "",
    content: str = "",
    host: str = "smtp.qq.com",
    port: int = 465,
) -> None:
    """Send an email.

    自动发送邮件，支持附件和抄送。

    Documentation: https://www.python-office.com/modules/email/api#send_email

    Args:
        key: 邮箱授权码（**不是登录密码**）
        msg_from: 发件人邮箱地址
        msg_to: 收件人邮箱地址
        msg_cc: 抄送地址（多个用逗号分隔）。Default: ``None``
        attach_files: 附件文件路径列表。Default: ``None``
        msg_subject: 邮件主题。Default: ``''``
        content: 邮件正文。Default: ``''``
        host: SMTP 服务器地址，常见值 ``'smtp.qq.com'`` / ``'smtp.163.com'`` / ``'smtp.gmail.com'``。Default: ``'smtp.qq.com'``
        port: SMTP 服务器端口。Default: ``465``

    Returns:
        None
    """
    if attach_files is None:
        attach_files = []
    _send_email_impl(
        key=key,
        msg_from=msg_from,
        msg_to=msg_to,
        msg_cc=msg_cc,
        attach_files=attach_files,
        msg_subject=msg_subject,
        content=content,
        host=host,
        port=port,
    )
    print(
        f"[python-office] send_email  {msg_from} → {msg_to}  "
        f"主题：{msg_subject!r}  附件：{len(attach_files)} 个"
    )


# =====================================================================
# 2. receive_email - 接收邮件
# =====================================================================

def receive_email(
    key: str,
    msg_from: str,
    output_path: str = "./",
    status: str = "UNSEEN",
    msg_subject: str = "",
    host: str = "smtp.qq.com",
    port: int = 465,
) -> str:
    """Receive emails.

    接收邮件并保存到指定目录。

    Documentation: https://www.python-office.com/modules/email/api#receive_email

    Args:
        key: 邮箱授权码
        msg_from: 发件人邮箱地址
        output_path: 邮件保存目录。Default: ``'./'``
        status: 邮件状态过滤，常用 ``'UNSEEN'``（未读）/ ``'SEEN'``（已读）。Default: ``'UNSEEN'``
        msg_subject: 邮件主题过滤（留空匹配所有）。Default: ``''``
        host: 邮件服务器地址。Default: ``'smtp.qq.com'``
        port: 邮件服务器端口。Default: ``465``

    Returns:
        str: 邮件保存目录
    """
    _receive_email_impl(
        key=key,
        msg_from=msg_from,
        output_path=output_path,
        status=status,
        msg_subject=msg_subject,
        host=host,
        port=port,
    )
    print(
        f"[python-office] receive_email  账户：{msg_from}  "
        f"状态：{status!r}  输出：{output_path}"
    )
    return output_path
