import wftools
from pocode.api.color import random_color_print

from office.lib.conf.CONST import SPLIT_LINE


#
def transtools(to_lang: str, content: str, from_lang: str = 'zh'):
    """将内容从一种语言翻译为另一种语言。
    
    Args:
        to_lang (str): 目标语言
        content (str): 待翻译的内容
        from_lang (str, optional): 源语言，默认为'zh'（中文）
    
    Returns:
        str: 翻译后的结果
    """
    return wftools.transtools(to_lang=to_lang, content=content, from_lang=from_lang)


def qrcodetools(url: str, output: str = r'./qrcode_img.png'):
    """生成二维码图片。
    
    Args:
        url (str): 用于生成二维码的URL地址
        output (str, optional): 生成的二维码图片保存路径，默认为当前目录下的'./qrcode_img.png'
    
    Returns:
        None
    """
    wftools.qrcodetools(url, output)


def passwordtools(len=8):
    """生成一个指定长度的密码。
    
    Args:
        len (int, optional): 密码长度，默认为8
    
    Returns:
        str: 生成的密码
    """
    return wftools.passwordtools(len)

def weather():
    """获取当前天气信息。
    
    该函数调用了wftools库中的weather方法，以获取当前的天气信息。
    请注意，此函数内部无参数且不返回任何值。它依赖于外部库wftools来完成实际的天气信息获取。
    
    Returns:
        None
    """
    wftools.weather()



# 通过url，获取ip地址
#
def url2ip(url: str) -> str:
    """将URL转换为IP地址。
    
    此函数调用了wftools库中的url2ip方法，用于解析给定的URL并返回相应的IP地址。
    
    Args:
        url (str): 需要转换的URL字符串
    
    Returns:
        str: 解析得到的IP地址字符串
    """
    return wftools.url2ip(url)



# 通过url，获取ip地址

def lottery8ticket():
    """生成一张8位彩票号码。
    
    调用了 `wftools` 库中的 lottery8ticket 方法，用于生成指定格式的彩票号码。
    该函数不需要任何参数，也无返回值，所有逻辑都在内部完成。
    
    Returns:
        None
    """
    wftools.lottery8ticket()



def create_article(theme, line_num=200):
    """创建文章。
    
    Args:
        theme (str): 文章的主题
        line_num (int, optional): 文章的行数，默认为200行
    
    Returns:
        None
    """
    wftools.create_article(theme, line_num)


def pwd4wifi(len_pwd: int = 8, pwd_list=[]):
    """生成WiFi密码列表。
    
    该函数调用wftools模块中的pwd4wifi函数，以生成指定长度的WiFi密码列表。
    如果没有提供密码列表，函数将使用空列表作为默认参数。
    
    Args:
        len_pwd (int, optional): 密码长度，默认为8
        pwd_list (list, optional): 密码列表，默认为空列表
    
    Returns:
        None
    """
    # 调用wftools模块中的pwd4wifi函数，传递密码长度和密码列表参数
    wftools.pwd4wifi(len_pwd, pwd_list)

# 测试网速

def net_speed_test():
    """网络速度测试函数。
    
    该函数用于测试网络的上传和下载速度
    
    Returns:
        None
    """
    wftools.net_speed_test()


def course():
    """显示python-office库的相关信息和资源链接。
    
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
