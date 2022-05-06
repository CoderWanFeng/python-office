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

"""
图片添加水印，参考：
"""

import math
import os

from PIL import Image, ImageFont, ImageDraw, ImageEnhance, ImageChops

TTF_FONT = os.path.dirname(__file__) + "/font/msyh.ttc"


def crop_image(im):
    '''裁剪图片边缘空白'''
    bg = Image.new(mode='RGBA', size=im.size)
    bbox = ImageChops.difference(im, bg).getbbox()
    if bbox:
        return im.crop(bbox)
    return im


def set_opacity(im, opacity):
    '''设置水印透明度'''
    assert 0 <= opacity <= 1
    alpha = im.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    im.putalpha(alpha)
    return im


def get_mark_img(text, color="#8B8B1B", size=30, opacity=0.15):
    """生成水印图片"""
    width = len(text) * size
    mark = Image.new(mode='RGBA', size=(width, size + 20))
    draw_table = ImageDraw.Draw(im=mark)
    draw_table.text(xy=(0, 0),
                    text=text,
                    fill=color,
                    font=ImageFont.truetype(TTF_FONT, size=size))
    del draw_table
    # 裁剪空白
    mark = crop_image(mark)
    # 透明度
    set_opacity(mark, opacity)
    return mark


def im_add_mark(im, text, color="#8B8B1B", size=30, opacity=0.15, space=75, angle=30):
    """给图片对象添加水印"""
    # 获取水印图片对象
    mark = get_mark_img(text, color, size, opacity)
    # 将水印图片扩展并旋转生成水印大图
    w, h = im.size
    c = int(math.sqrt(w ** 2 + h ** 2))
    mark2 = Image.new(mode='RGBA', size=(c, c))
    y, idx = 0, 0
    mark_w, mark_h = mark.size
    while y < c:
        x = -int((mark_w + space) * 0.5 * idx)
        idx = (idx + 1) % 2
        while x < c:
            mark2.paste(mark, (x, y))
            x = x + mark_w + space
        y = y + mark_h + space
    # 将水印大图旋转一定角度
    mark2 = mark2.rotate(angle)
    # 在原图上添加水印大图
    if im.mode != 'RGBA':
        im = im.convert('RGBA')
    im.paste(mark2, (int((w - c) / 2), int((h - c) / 2)),  # 坐标
             mask=mark2.split()[3])
    return im


def add_mark2file(imageFile, text, out="output", color="#8B8B1B", size=30, opacity=0.15, space=75, angle=30):
    '''
    添加水印，然后保存图片
    '''
    name = os.path.basename(imageFile)
    new_name = os.path.join(out, name)
    try:
        im = Image.open(imageFile)
        image = im_add_mark(im, text, color, size, opacity, space, angle)
        if not os.path.exists(out):
            os.mkdir(out)
        if os.path.splitext(new_name)[1] != '.png':
            image = image.convert('RGB')
        image.save(new_name)
        print(new_name, "保存成功。")
    except Exception as e:
        print(new_name, "保存失败。错误信息：", e)


# 给图片添加水印
def add_watermark(file, mark, out="output", color="#8B8B1B", size=30, opacity=0.15, space=75, angle=30):
    if os.path.isdir(file):
        names = os.listdir(file)
        for name in names:
            image_file = os.path.join(file, name)
            add_mark2file(image_file, mark, out, color, size, opacity, space, angle)
    else:
        add_mark2file(file, mark, out, color, size, opacity, space, angle)
