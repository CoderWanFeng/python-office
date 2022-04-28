#!/usr/bin/env python
# -*- coding:utf-8 -*-

#############################################
# File Name: 图片.py
# Mail: 1957875073@qq.com
# Created Time:  2022-4-25 10:17:34
# Description: 有关 图片 的自动化操作
#############################################


# 自动生成gif
def image2gif():
    im = Image.open("1.jpg")
    images = []
    images.append(Image.open('2.jpg'))
    images.append(Image.open('3.jpg'))
    im.save('gif.gif', save_all=True, append_images=images, loop=1, duration=1, comment=b"aaabb")


# 生成词云需要使用的类库
from PIL import Image
from wordcloud import WordCloud
import jieba


def txt2wordcloud(filename, color="white", result_file="your_wordcloud.png"):
    """
    @Author & Date  : CoderWanFeng 2022/4/28 9:26
    @Desc  : 生成词云的代码，可以添加更多个性化功能
    @Return  ：
    """
    with open(filename, encoding='utf8') as fp:
        text = fp.read()
        # 将读取的中文文档进行分词
        # 接收分词的字符串
        word_list = jieba.cut(text)
        # 分词后在单独个体之间加上空格
        cloud_text = " ".join(word_list)

        # 生成wordcloud对象
        wc = WordCloud(background_color=color,
                       max_words=200,
                       min_font_size=15,
                       max_font_size=50,
                       width=400,
                       font_path="msyh.ttc",  # 默认的简体中文字体，没有会报错
                       )
        wc.generate(cloud_text)
        wc.to_file(result_file)
