# -*- coding: UTF-8 -*-
'''
@作者 ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@读者群     ：http://www.python4office.cn/wechat-group/
@个人网站 ：www.python-office.com
@Date    ：2023/4/27 21:19
@Description     ：
'''

"""
批量加好友，1行代码实现
"""
# pip install PyOfficeRobot>=0.1.5
import PyOfficeRobot

msg = "你好，我是程序员晚枫，全网同名。"
num_notes = {
    # '微信号/手机号': '你给Ta的备注',
    # '1366666': '公众号-晚枫',
    'CoderWanFeng': '小红书-晚枫',
}
PyOfficeRobot.friend.add(msg=msg, num_notes=num_notes)

# TODO:控件改变了，有BUG
