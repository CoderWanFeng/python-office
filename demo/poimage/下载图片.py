# -*- coding: UTF-8 -*-
'''
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：CoderWanFeng
@读者群     ：http://www.python4office.cn/wechat-group/
@学习网站      ：www.python-office.com
@代码日期    ：2023/8/9 22:30 
@本段代码的视频说明     ：
'''

# 导入这个库：python-office，简写为office
import office

office.image.down4img(
    url='https://python-office-1300615378.cos.ap-chongqing.myqcloud.com/icon2.jpg',
    output_name='./test_files/下载图片/B站：程序员晚枫',
    type='jpg')
# 参数说明：
# url：你要下载的图片链接
# output_name：下载后的图片名称，可以不填，默认：down4img
# type：下载后的图片类型，可以不填，默认：jpg
