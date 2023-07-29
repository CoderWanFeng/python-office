# -*- coding: UTF-8 -*-
'''
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@微信     ：CoderWanFeng : https://mp.weixin.qq.com/s/yFcocJbfS9Hs375NhE8Gbw
@个人网站      ：www.python-office.com
@Date    ：2023/2/13 21:19
@本段代码的视频说明     ：https://www.bilibili.com/video/BV1m8411b7LZ
'''
import PyOfficeRobot

keywords = {
    "我要报名": "你好，这是报名链接：www.python-office.com",
    "点赞了吗？": "点了",
    "关注了吗？": "必须的",
    "投币了吗？": "三连走起",
}
PyOfficeRobot.chat.chat_by_keywords(who='抖音：程序员晚枫', keywords=keywords)
