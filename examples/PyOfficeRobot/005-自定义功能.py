# -*- coding: UTF-8 -*-
'''
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：CoderWanFeng
@读者群     ：http://www.python4office.cn/wechat-group/
@学习网站      ：https://www.python-office.com
@代码日期    ：2023/7/9 23:22 
@本段代码的视频说明     ：https://www.bilibili.com/video/BV14R4y127h6
'''
import PyOfficeRobot

import office

keywords = {
    "我要报名": "你好，这是报名链接：www.python-office.com",
    "来个密码": office.tools.passwordtools(),
}
# PyOfficeRobot.chat.chat_by_keywords(who='每天进步一点点', keywords=keywords)
PyOfficeRobot.chat.chat_by_keywords(who='知乎：程序员晚枫', keywords=keywords)