# -*- coding: UTF-8 -*-
'''
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@微信     ：CoderWanFeng : https://mp.weixin.qq.com/s/HYOWV7ImvTXImyYWtwADog
@个人网站      ：www.python-office.com
@代码日期    ：2023/7/17 22:37 
@本段代码的视频说明     ：
'''

import office

office.pdf.add_mark(pdf_file=r'./test_files/add_mark/程序员晚枫（没加水印）.pdf', mark_str='程序员晚枫',
                    output_path=r'./test_files/add_mark/output', output_file_name='程序员晚枫（加了水印）.pdf')
