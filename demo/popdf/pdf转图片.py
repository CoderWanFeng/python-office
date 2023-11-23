# -*- coding: UTF-8 -*-
'''
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@微信     ：CoderWanFeng : https://mp.weixin.qq.com/s/Nt8E8vC-ZsoN1McTOYbY2g
@个人网站      ：www.python-office.com
@代码日期    ：2023/7/18 22:09 
@本段代码的视频说明     ：
'''
# 导入这个库：python-office，简写为office
import office

# 一行代码，实现转换
office.pdf.pdf2imgs(
    pdf_path='D://程序员晚枫的文件夹//程序员晚枫.pdf',
    out_dir='./点赞+关注文件夹'
)
# 参数说明：
# pdf_path = 你的PDF文件的地址
# out_dir = 转换后的图片存放地址，可以不填，默认是PDF的地址