# -*- coding: UTF-8 -*-
'''
@作者 ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@读者群     ：http://www.python4office.cn/wechat-group/
@个人网站 ：www.python-office.com
@Date    ：2023/7/3 23:46 
@Description     ：
'''
import office

office.image.compress_image(input_file=r'D:\workplace\code\github\poimage\tests\头像.jpg',
                            output_file="compressed.jpg",
                            quality=50)  # 质量，1-100之间，数值越低压缩率越高
