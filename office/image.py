#!/usr/bin/env python
# -*- coding:utf-8 -*-

#############################################
# File Name: 图片.py
# Mail: 1957875073@qq.com
# Created Time:  2022-4-25 10:17:34
# Description: 有关 图片 的自动化操作
#############################################

import os
# from service.image import add_watermark_service
# 生成词云需要使用的类库
from PIL import Image
from alive_progress import alive_bar




# 自动生成gif
from service.image import add_watermark_service


def image2gif():
    im = Image.open("1.jpg")
    images = []
    images.append(Image.open('2.jpg'))
    images.append(Image.open('3.jpg'))
    im.save('gif.gif', save_all=True, append_images=images, loop=1, duration=1, comment=b"aaabb")

# from wordcloud import WordCloud
# import jieba

# def txt2wordcloud(filename, color="white", result_file="your_wordcloud.png"):
#     """
#     @Author & Date  : CoderWanFeng 2022/4/28 9:26
#     @Desc  : 生成词云的代码，可以添加更多个性化功能
#     @Return  ：
#     """
#     with open(filename, encoding='utf8') as fp:
#         text = fp.read()
#         # 将读取的中文文档进行分词
#         # 接收分词的字符串
#         word_list = jieba.cut(text)
#         # 分词后在单独个体之间加上空格
#         cloud_text = " ".join(word_list)
#
#         # 生成wordcloud对象
#         wc = WordCloud(background_color=color,
#                        max_words=200,
#                        min_font_size=15,
#                        max_font_size=50,
#                        width=400,
#                        font_path="msyh.ttc",  # 默认的简体中文字体，没有会报错
#                        )
#         wc.generate(cloud_text)
#         wc.to_file(result_file)


def add_watermark(file, mark, out="output", color="#8B8B1B", size=30, opacity=0.15, space=75, angle=30):
    """
    @Author & Date  : demo 2022/5/6 14:33
    @Desc  : 给图片添加水印
    @Return  ： 添加了水印的图片，输出到out指定的文件夹
    """
    if os.path.isdir(file):
        names = os.listdir(file)
        with alive_bar(len(names)) as bar:
            for name in names:
                bar()
                image_file = os.path.join(file, name)
                add_watermark_service.add_mark2file(image_file, mark, out, color, size, opacity, space, angle)
    else:
        add_watermark_service.add_mark2file(file, mark, out, color, size, opacity, space, angle)
