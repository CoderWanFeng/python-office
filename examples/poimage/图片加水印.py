# -*- coding: UTF-8 -*-

# 给图片加水印
import office

office.image.add_watermark(file='./test_files/add_watermark/程序员晚枫-2.jpg',
                           mark='程序员晚枫',
                           output_path=r'./test_files/add_watermark/mark_img')
