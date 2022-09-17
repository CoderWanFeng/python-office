# from office.core.WeChatType import MainWeChat
#
# mainwx = MainWeChat()

import PyOfficeRobot


def send_message(who, message):
    PyOfficeRobot.chat.send_message(who, message)


def send_file(who, file):
    PyOfficeRobot.file.send_file(who, file)
