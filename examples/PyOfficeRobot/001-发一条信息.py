# -*- coding: UTF-8 -*- 

# 首先，将PyOfficeRobot模块导入到我们的代码块中。
import PyOfficeRobot


def send_with_emoji(who, message):
    """
    支持Emoji符号的微信消息发送方法（优化版）
    :param who: 接收人
    :param message: 要发送的消息(支持Emoji)
    """
    import time
    import pyautogui
    import pyperclip
    # 确保微信窗口在前台
    try:
        # 复制消息到剪贴板（支持Emoji）
        pyperclip.copy(message)

        # 打开微信窗口（这里简化处理，实际使用时可能需要调整）
        PyOfficeRobot.chat.send_message(who=who, message='')  # 先激活微信

        time.sleep(2)  # 等待微信窗口激活

        # 粘贴内容
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.5)

        # 发送消息
        pyautogui.press('enter')

    except Exception as e:
        print(f"发送失败: {e}")
        # 备用方案：分段发送
        for char in message:
            try:
                pyperclip.copy(char)
                pyautogui.hotkey('ctrl', 'v')
                time.sleep(0.1)
            except:
                continue
        pyautogui.press('enter')


if __name__ == '__main__':
    # who 后面写的微信好友的昵称/备注名，message是发送的内容
    PyOfficeRobot.chat.send_message(who='小红书：程序员晚枫', message='你好')
    # PyOfficeRobot.chat.send_message(who='每天进步一点点', message='你好')

    # 支持emoji符号的消息发送
    send_with_emoji(who='文件传输助手', message='🌤️ ​​午安！咖啡时间到☕，休息一下吧～')