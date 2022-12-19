import PyOfficeRobot
from office.lib.decorator_utils.instruction_url import instruction


@instruction
def send_message(who, message):
    PyOfficeRobot.chat.send_message(who, message)


@instruction
def send_message_by_time(who, message, time):
    PyOfficeRobot.chat.send_message_by_time(who, message, time)


@instruction
def chat_by_keywords(who, keywords):
    PyOfficeRobot.chat.chat_by_keywords(who, keywords)


@instruction
def send_file(who, file):
    PyOfficeRobot.file.send_file(who, file)


# 保存指定人的消息
# BY：盖飞
@instruction
def receive_message(who='文件传输助手', txt='userMessage.txt', output_path='./'):
    PyOfficeRobot.chat.receive_message(who, txt, output_path)
