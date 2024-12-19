# -*- coding: UTF-8 -*-
'''
@作者 ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@读者群     ：http://www.python4office.cn/wechat-group/
@个人网站 ：www.python-office.com
@Date    ：2023/5/25 23:34 
@Description     ：
'''

# 集成使用
import office

input_path = r"./test_files/merge4ppt"
office.ppt.merge4ppt(input_path)

# 独立使用
# import poppt
#
# poppt.merge4ppt(input_path, output_path=r'./output')
