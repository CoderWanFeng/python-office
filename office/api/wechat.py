import PyOfficeRobot


def send_message(who, message):
    PyOfficeRobot.chat.send_message(who, message)


def chat_by_keywords(who, keywords):
    PyOfficeRobot.chat.chat_by_keywords(who, keywords)


def send_file(who, file):
    PyOfficeRobot.file.send_file(who, file)
