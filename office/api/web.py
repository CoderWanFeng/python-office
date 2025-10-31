# -*- coding:utf-8 -*-

import pospider

def url2ebook(url, tile):
    """将指定的URL转换为电子书格式。
    
    本函数通过调用pospider模块的url2ebook方法，将给定的URL转换为电子书。
    
    Args:
        url (str): 需要转换为电子书的网页URL
        tile (str): 电子书的标题
    
    Returns:
        None，但会生成电子书文件
    """
    pospider.url.url2ebook(url, tile)
