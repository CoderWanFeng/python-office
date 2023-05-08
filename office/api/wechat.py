from office.lib.decorator_utils.instruction_url import instruction

single_video = "该方法目前已经独立出去，详情请看视频：https://www.bilibili.com/video/BV1SY411y7Uh"


@instruction
def send_message(who, message):
    print(single_video)
    # PyOfficeRobot.chat.send_message(who, message)


@instruction
def send_message_by_time(who, message, time):
    print(single_video)
    # PyOfficeRobot.chat.send_message_by_time(who, message, time)


@instruction
def chat_by_keywords(who, keywords):
    print(single_video)
    # PyOfficeRobot.chat.chat_by_keywords(who, keywords)


@instruction
def send_file(who, file):
    print(single_video)
    # PyOfficeRobot.file.send_file(who, file)


# 保存指定人的消息
# BY：盖飞
@instruction
def receive_message(who='文件传输助手', txt='userMessage.txt', output_path='./'):
    print(single_video)
    # PyOfficeRobot.chat.receive_message(who, txt, output_path)
