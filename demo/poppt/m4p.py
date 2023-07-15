# -*- coding: UTF-8 -*-
'''
@作者 ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@微信 ：CoderWanFeng : https://mp.weixin.qq.com/s/HYOWV7ImvTXImyYWtwADog
@个人网站 ：www.python-office.com
@Date    ：2023/5/25 23:34 
@Description     ：
'''

# 集成使用
import office

input_path = r"D:\workplace\code\github\poppt\dev\docs"
office.ppt.merge4ppt(input_path)

# 独立使用
import poppt

input_path = r"D:\小破站\程序员晚枫\github\poppt\dev\docs"
poppt.merge4ppt(input_path)
