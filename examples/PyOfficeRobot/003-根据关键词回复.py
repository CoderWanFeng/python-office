# -*- coding: UTF-8 -*-

import PyOfficeRobot

keywords = {
    "我要报名": "你好，这是报名链接：www.python-office.com",
    "点赞了吗？": "点了",
    "关注了吗？": "必须的",
    "投币了吗？": "三连走起",
}
# keywords 中 前面一个引号里的内容是好友发来的消息，后面一个引号里的内容是回复给好友的消息
PyOfficeRobot.chat.chat_by_keywords(who='抖音：程序员晚枫', keywords=keywords)
# PyOfficeRobot.chat.chat_by_keywords(who='每天进步一点点', keywords=keywords)
