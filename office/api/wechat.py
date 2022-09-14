from office.core.WeChatType import MainWeChat

mainwx = MainWeChat()


def send_message(who, message):
    mainwx.send_message(who, message)


def send_file(who, file):
    mainwx.send_file(who, file)
