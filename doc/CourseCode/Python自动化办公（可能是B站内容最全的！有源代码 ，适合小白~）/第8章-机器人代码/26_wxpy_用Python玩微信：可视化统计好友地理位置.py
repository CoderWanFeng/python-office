# -*- coding: utf-8 -*-
# @Time : 2020/8/23 2:24
# @公众号 :Python自动化办公社区 
# @File : 26_wxpy_用Python玩微信：可视化统计好友地理位置.py
# @Software: PyCharm
# @Description:

# pip install wxpy
from wxpy import *

# 初始化一个机器人对象
# cache_path缓存路径，给定值为第一次登录生成的缓存文件路径
bot = Bot()
# 获取好友列表(包括自己)
my_friends = bot.friends(update=False)
'''
stats_text 函数：帮助我们简单统计微信好友基本信息
简单的统计结果的文本    
:param total: 总体数量    
:param sex: 性别分布    
:param top_provinces: 省份分布    
:param top_cities: 城市分布    
:return: 统计结果文本
'''
print(my_friends.stats_text())
