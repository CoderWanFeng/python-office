# -*- coding: UTF-8 -*-
'''
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@微信     ：CoderWanFeng : https://mp.weixin.qq.com/s/yFcocJbfS9Hs375NhE8Gbw
@个人网站      ：www.python-office.com
@代码日期    ：2023/7/9 23:22 
@本段代码的视频说明     ：https://www.bilibili.com/video/BV14R4y127h6
'''
import office

import PyOfficeRobot

keywords = {
    "我要报名": "你好，这是报名链接：www.python-office.com",
    "来个密码": office.tools.passwordtools(),
}
PyOfficeRobot.chat.chat_by_keywords(who='知乎：程序员晚枫', keywords=keywords)
