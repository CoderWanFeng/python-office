"""Utility tools functionality module.

工具类功能模块。

This module provides various utility tools including translation, QR code generation,
password generation, weather query, URL to IP conversion, article generation, and more.

该模块提供了各种工具类功能，包括翻译、二维码生成、密码生成、天气查询、URL转IP、文章生成等。

Author:
    程序员晚枫

Project:
    https://www.python-office.com
"""

import wftools
from pocode.api.color import random_color_print

from office.lib.conf.CONST import SPLIT_LINE


#
def transtools(to_lang: str, content: str, from_lang: str = 'zh'):
    """Translate content from one language to another.
    
    将内容从一种语言翻译为另一种语言。
    
    Args:
        to_lang (str): target language / 目标语言
        content (str): content to translate / 待翻译的内容
        from_lang (str, optional): source language / 源语言。Default / 默认: 'zh' (Chinese / 中文)
    
    Returns:
        str: translated result / 翻译后的结果
    """
    return wftools.transtools(to_lang=to_lang, content=content, from_lang=from_lang)


def qrcodetools(url: str, output: str = r'./qrcode_img.png'):
    """Generate QR code image.
    
    生成二维码图片。
    
    Args:
        url (str): URL address for generating QR code / 用于生成二维码的URL地址
        output (str, optional): save path for generated QR code image / 生成的二维码图片保存路径。Default / 默认: './qrcode_img.png' in current directory / 当前目录下的'./qrcode_img.png'
    
    Returns:
        None
    """
    wftools.qrcodetools(url, output)


def passwordtools(len=8):
    """Generate password of specified length.
    
    生成一个指定长度的密码。
    
    Args:
        len (int, optional): password length / 密码长度。Default / 默认: 8
    
    Returns:
        str: generated password / 生成的密码
    """
    return wftools.passwordtools(len)

def weather():
    """Get current weather information.
    
    获取当前天气信息。
    
    This function calls the weather method in wftools library to get current weather information.
    Note that this function has no parameters and returns no value. It depends on external library wftools to complete actual weather information retrieval.
    
    该函数调用了wftools库中的weather方法，以获取当前的天气信息。
    请注意，此函数内部无参数且不返回任何值。它依赖于外部库wftools来完成实际的天气信息获取。
    
    Returns:
        None
    """
    wftools.weather()



# 通过url，获取ip地址
#
def url2ip(url: str) -> str:
    """Convert URL to IP address.
    
    将URL转换为IP地址。
    
    This function calls url2ip method in wftools library to parse given URL and return corresponding IP address.
    
    此函数调用了wftools库中的url2ip方法，用于解析给定的URL并返回相应的IP地址。
    
    Args:
        url (str): URL string to convert / 需要转换的URL字符串
    
    Returns:
        str: parsed IP address string / 解析得到的IP地址字符串
    """
    return wftools.url2ip(url)



# 通过url，获取ip地址

def lottery8ticket():
    """Generate 8-digit lottery ticket number.
    
    生成一张8位彩票号码。
    
    Calls lottery8ticket method in `wftools` library to generate lottery ticket number in specified format.
    This function requires no parameters and has no return value, all logic is completed internally.
    
    调用了`wftools`库中的lottery8ticket方法，用于生成指定格式的彩票号码。
    该函数不需要任何参数，也无返回值，所有逻辑都在内部完成。
    
    Returns:
        None
    """
    wftools.lottery8ticket()



def create_article(theme, line_num=200):
    """Create article.
    
    创建文章。
    
    Args:
        theme (str): article theme / 文章的主题
        line_num (int, optional): number of lines in article / 文章的行数。Default / 默认: 200 lines / 200行
    
    Returns:
        None
    """
    wftools.create_article(theme, line_num)


def pwd4wifi(len_pwd: int = 8, pwd_list=[]):
    """Generate WiFi password list.
    
    生成WiFi密码列表。
    
    This function calls pwd4wifi function in wftools module to generate WiFi password list of specified length.
    If no password list provided, function will use empty list as default parameter.
    
    该函数调用wftools模块中的pwd4wifi函数，以生成指定长度的WiFi密码列表。
    如果没有提供密码列表，函数将使用空列表作为默认参数。
    
    Args:
        len_pwd (int, optional): password length / 密码长度。Default / 默认: 8
        pwd_list (list, optional): password list / 密码列表。Default / 默认: empty list / 空列表
    
    Returns:
        None
    """
    # 调用wftools模块中的pwd4wifi函数，传递密码长度和密码列表参数
    wftools.pwd4wifi(len_pwd, pwd_list)

# 测试网速

def net_speed_test():
    """Network speed test function.
    
    网络速度测试函数。
    
    This function is used to test network upload and download speed.
    
    该函数用于测试网络的上传和下载速度。
    
    Returns:
        None
    """
    wftools.net_speed_test()


def course():
    """Display information and resource links for python-office library.
    
    显示python-office库的相关信息和资源链接。
    
    Returns:
        None
    """
    random_color_print(SPLIT_LINE)
    random_color_print('【python-office库】，功能持续更新中')
    random_color_print('使用有问题 or 提交你的功能需求 or 参与项目开发')
    random_color_print('1、给小白的【50讲Python自动化办公】：https://www.python-office.com/course/50-python-office.html')
    random_color_print('2、请+【项目交流群】：http://www.python4office.cn/wechat-group/')
    random_color_print('3、本开源项目的【源代码】：https://github.com/CoderWanFeng/python-office')
    random_color_print(SPLIT_LINE)
