# -*- coding: UTF-8 -*-
# Author: 程序员晚枫

import PyOfficeRobot

import office

keywords = {
    "我要报名": "你好，这是报名链接：www.python-office.com",
    "来个密码": office.tools.passwordtools(),
}
# PyOfficeRobot.chat.chat_by_keywords(who='每天进步一点点', keywords=keywords)
# office.tools.passwordtools() 会生成一个随机的8位数密码
PyOfficeRobot.chat.chat_by_keywords(who='知乎：程序员晚枫', keywords=keywords)