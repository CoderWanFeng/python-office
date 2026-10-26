# -*- coding:utf-8 -*-


def _load_pospider():
    try:
        import pospider
    except ModuleNotFoundError as exc:
        if exc.name != "pospider":
            raise
        raise ModuleNotFoundError(
            "网页转电子书功能依赖 pospider，请先安装 pospider。"
        ) from exc
    try:
        pospider.url.url2ebook
    except AttributeError as exc:
        raise ImportError(
            "当前 pospider 版本不提供 url.url2ebook，请安装兼容版本。"
        ) from exc
    return pospider


def url2ebook(url, tile):
    """将指定的URL转换为电子书格式。
    
    本函数通过调用pospider模块的url2ebook方法，将给定的URL转换为电子书。
    
    Args:
        url (str): 需要转换为电子书的网页URL
        tile (str): 电子书的标题
    
    Returns:
        None，但会生成电子书文件
    """
    pospider = _load_pospider()
    pospider.url.url2ebook(url=url, tile=tile)
