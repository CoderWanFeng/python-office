# -*- coding: UTF-8 -*-
'''
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：CoderWanFeng
@读者群     ：http://www.python4office.cn/wechat-group/
@学习网站      ：https://www.python-office.com
@代码日期    ：2023/7/20 0:08 
@本段代码的视频说明     ：
'''
# 给图片加水印
import office

office.image.add_watermark(file='./test_files/add_watermark/程序员晚枫-2.jpg',
                           mark='程序员晚枫',
                           output_path=r'./test_files/add_watermark/mark_img')
