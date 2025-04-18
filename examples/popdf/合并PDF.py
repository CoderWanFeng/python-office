# -*- coding: UTF-8 -*-
'''
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：CoderWanFeng
@读者群     ：http://www.python4office.cn/wechat-group/
@学习网站      ：https://www.python-office.com
@代码日期    ：2023/7/18 22:08 
@本段代码的视频说明     ：
'''
# 导入这个库：python-office，简写为office
import office

#一行代码，合并pdf
office.pdf.merge2pdf(one_by_one=['程序员晚枫.pdf', '一键三连.pdf'], output='走起.pdf')

#参数作用：
# one_by_one = 是个列表，里面是2个pdf文件，合并后，a在前面，b在后面
# output = 合并后的pdf名字，不能为空