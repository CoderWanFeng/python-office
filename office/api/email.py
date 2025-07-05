# -*- coding:utf-8 -*-
"""
关于这个功能的使用说明，见课程：
"""
import poemail
from poemail.lib.Const import Mail_Type


def send_email(key, msg_from, msg_to, msg_cc=None, attach_files=[], msg_subject='', content='', host=Mail_Type['qq'],
               port=465):
    """
    自动发送邮件

    参数:
    key (str): 邮箱账户密钥
    msg_from (str): 发件人邮箱地址
    msg_to (str): 收件人邮箱地址
    file_path (str, 可选): 邮件附件路径，默认为None
    msg_subject (str, 可选): 邮件主题，默认为空字符串
    content (str, 可选): 邮件内容，默认为空字符串
    host (str, 可选): 邮箱服务器地址，默认为'qq'
    port (int, 可选): 邮箱服务器端口号，默认为465

    返回:
    无

    """
    poemail.send.send_email(key=key,
                            msg_from=msg_from,
                            msg_to=msg_to,
                            msg_cc=msg_cc,
                            msg_subject=msg_subject,
                            host=host,
                            port=port)


def receive_email(key, msg_from, msg_to, output_path=r'./', status="UNSEEN", msg_subject='', content='',
                  host=Mail_Type['qq'], port=465):
    poemail.receive.receive_email(key=key,
                                  msg_from=msg_from,
                                  msg_to=msg_to,
                                  msg_subject=msg_subject,
                                  host=host,
                                  port=port, output_path=output_path, status=status)
