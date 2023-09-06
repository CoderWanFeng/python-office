# -*- coding: UTF-8 -*-
'''
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@微信     ：CoderWanFeng : https://mp.weixin.qq.com/s/B1V6KeXc7IOEB8DgXLWv3g
@个人网站      ：www.python-office.com
@代码日期    ：2023/8/9 22:36 
@本段代码的视频说明     ：
'''

# pip install poimage，可以使用清华大学的仓库下载：https://www.bilibili.com/video/BV1SM411y7vw
import poimage

# 支持jpg、png等所有图片格式
# 注意：图片的路径和名称，都不能有中文！
poimage.del_watermark(
    input_image=r"D:\workplace\code\github\python-office\demo\poimage\test_files\del_watermark\img.png",
    output_image=r'./test_files/del_watermark/del_watermark.jpg')
