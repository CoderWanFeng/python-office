# -*- coding: UTF-8 -*-
'''
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：CoderWanFeng
@读者群     ：http://www.python4office.cn/wechat-group/
@学习网站      ：https://www.python-office.com
@代码日期    ：2023/8/9 23:25 
@本段代码的视频说明     ：
'''
import pydatav

if __name__ == '__main__':
    filename = r'.\txt2wordcloud\test.txt'
    color = 'black'
    result_file = r'.\txt2wordcloud\res.jpg'
    pydatav.image.txt2wordcloud(filename, color, result_file)
