import wftools

from office.lib.decorator_utils.instruction_url import instruction


# from office.core.ToolsType import wftools
# wftools = wftools()

# @except_dec()
# # @instruction
def transtools(to_lang: str, content: str, from_lang: str = 'zh'):
    """
    将内容从一种语言翻译为另一种语言。

    参数:
    to_lang (str): 目标语言，用字符串表示。
    content (str): 待翻译的内容。
    from_lang (str, 可选): 源语言，默认为'zh'（中文）。

    返回:
    str: 翻译后的结果。

    """
    return wftools.transtools(to_lang=to_lang, content=content, from_lang=from_lang)



# @except_dec()
# @instruction
def qrcodetools(url: str, output: str = r'./qrcode_img.png'):
    """
    生成二维码图片。

    参数:
    url (str): 用于生成二维码的URL地址。
    output (str, 可选): 生成的二维码图片保存路径，默认为当前目录下的 './qrcode_img.png'。

    返回:
    无

    """
    wftools.qrcodetools(url, output)



# @except_dec()
# @instruction
def passwordtools(len=8):
    """
    生成一个指定长度的密码。

    参数：
    len (int): 密码长度，默认为8。

    返回值：
    str: 生成的密码。
    """
    return wftools.passwordtools(len)


# @except_dec()
# @instruction
def weather():
    wftools.weather()



# 通过url，获取ip地址
# # @except_dec()
# @instruction
def url2ip(url: str) -> str:
    return wftools.url2ip(url)


# 通过url，获取ip地址
# @except_dec()
# @instruction
def lottery8ticket():
    wftools.lottery8ticket()



# @except_dec()
# @instruction
def create_article(theme, line_num=200):
    """
    创建文章

    参数:
    theme (str): 文章的主题
    line_num (int): 文章的行数，默认为200行

    返回:
    无

    """
    wftools.create_article(theme, line_num)



# @except_dec()
# @instruction
def pwd4wifi(len_pwd: int = 8, pwd_list=[]):
    wftools.pwd4wifi(len_pwd, pwd_list)


# 测试网速
# @instruction
def net_speed_test():
    """
    网络速度测试函数

    该函数用于测试网络的上传和下载速度

    参数:
        无

    返回:
        无
    """
    wftools.net_speed_test()

