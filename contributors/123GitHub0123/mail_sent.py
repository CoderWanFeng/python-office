# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : mail_sent.py
# @Time      : 2023/2/10 13:11




import smtplib
import winsound

# 发送文字
from email.mime.text import MIMEText

# 发送文件
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication



def send_mail(_sender, _passwd, receiver: list, files: list = None, content=None, subject=None, types='plain' or 'html',
              log_options=False, host='smtp.office365.com', port=587):
    """

    :param _sender: 必填，字符串，服务邮件账号
    :param _passwd: 必填，字符串，服务邮件密码
    :param receiver: 必填，列表，发送邮件目的地
    :param content: 默认空，字符串，发送文本
    :param subject: 默认空，字符串，邮件主题
    :param files: 可选，列表，发送附件时候使用，支持多文件
    :param types: 默认’plain‘，字符串，邮件发送类型，常见类型：'plain'常用文本, 'html'超文本
    :param log_options: 默认False，布尔值
    :param host: 邮件服务器地址
    :return:
    """
    ret = True
    try:
        # 重要的4行代码
        server = smtplib.SMTP(host, port)  # 这里容易遗漏host，切记
        # server.connect(host, 587)
        server.set_debuglevel(log_options)  # 打印登录日志
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(_sender, _passwd)  # 如果程序需要先花很多时间去获取各种信息然后把信息发出来，那么千万别在程序开启的时候就login，要不然断开连接了，要发信的时候再login比较好

        msg = MIMEMultipart()
        msg["Accept-Charset"] = "ISO-8859-1,utf-8"
        msg["Accept-Language"] = "zh-CN"
        msg['Subject'] = subject
        msg['From'] = _sender
        msg['To'] = ','.join(receiver)  # 这里必须要把多个邮箱按照逗号拼接为字符串

        # 文本

        message = MIMEText(content, types, 'utf-8')
        msg.attach(message)

        # 多个文件，for循环attach
        try:
            for fileName in files:
                with open(fileName, 'rb') as f:
                    part = MIMEApplication(f.read())
                    part.add_header('Content-Disposition', 'attachment', filename=fileName)
                    msg.attach(part)
        except:
            pass

        server.sendmail(_sender, receiver, msg.as_string())

        server.quit()
        print('email sent')
        winsound.MessageBeep()
    except:
        ret = False

    if ret:
        print('sent to')
    else:
        print('erron')
