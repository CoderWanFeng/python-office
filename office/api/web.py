# -*- coding:utf-8 -*-

import pospider

def url2ebook(url, tile):
    """
    将指定的URL转换为电子书格式。

    本函数通过调用pospider模块的url2ebook方法，将给定的URL转换为电子书。
    这里的tile参数用于指定电子书的标题。

    参数:
    url (str): 需要转换为电子书的网页URL。
    tile (str): 电子书的标题。

    返回:
    无直接返回值，但会生成电子书文件。
    """
    # 调用pospider模块中的url2ebook方法进行URL到电子书的转换
    pospider.url.url2ebook(url, tile)
