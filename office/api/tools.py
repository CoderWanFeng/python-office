import wftools
from pocode.api.color import random_color_print

from office.lib.conf.CONST import SPLIT_LINE


#
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


def passwordtools(len=8):
    """
    生成一个指定长度的密码。

    参数：
    len (int): 密码长度，默认为8。

    返回值：
    str: 生成的密码。
    """
    return wftools.passwordtools(len)


def weather():
    wftools.weather()


# 通过url，获取ip地址
# 
def url2ip(url: str) -> str:
    return wftools.url2ip(url)


# 通过url，获取ip地址

def lottery8ticket():
    wftools.lottery8ticket()


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


def pwd4wifi(len_pwd: int = 8, pwd_list=[]):
    wftools.pwd4wifi(len_pwd, pwd_list)


# 测试网速

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


def course():
    random_color_print(SPLIT_LINE)
    random_color_print('【python-office库】，功能持续更新中')
    random_color_print('使用有问题 or 提交你的功能需求 or 参与项目开发')
    random_color_print('1、给小白的【50讲Python自动化办公】：https://www.python-office.com/course/50-python-office.html')
    random_color_print('2、请+【项目交流群】：http://www.python4office.cn/wechat-group/')
    random_color_print('3、本开源项目的【源代码】：https://github.com/CoderWanFeng/python-office')
    random_color_print(SPLIT_LINE)
