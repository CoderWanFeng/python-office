# -*- coding: UTF-8 -*-
"""实用工具功能模块。

本模块按 https://www.python-office.com/modules/tools/api 官方文档定义，
共 10 个函数，对应子包 ``wftools``（随主包自动安装）：

    1.  transtools        - 多语言翻译
    2.  qrcodetools       - 生成二维码
    3.  passwordtools     - 随机密码
    4.  weather           - 天气查询（CLI 交互式）
    5.  url2ip            - URL 转 IP
    6.  lottery8ticket    - 彩票号码（CLI 交互式）
    7.  create_article    - AI 生成文章
    8.  pwd4wifi          - WiFi 密码（仅 Windows）
    9.  net_speed_test    - 网速测试（CLI 交互式）
    10. course            - 项目信息展示

Author:
    程序员晚枫

Project:
    https://www.python-office.com
"""

from __future__ import annotations

from typing import List, Optional

import wftools

try:
    from pocode.api.color import random_color_print
except ImportError:  # 兜底：pocode 不可用时退化为普通 print
    def random_color_print(text: str) -> None:  # type: ignore[no-redef]
        print(text)


# =====================================================================
# 1. transtools - 多语言翻译
# =====================================================================

def transtools(to_lang: str, content: str, from_lang: str = "zh") -> str:
    """Translate text between languages.

    将内容从一种语言翻译为另一种语言（调用 libretranslate）。

    Documentation: https://www.python-office.com/modules/tools/api#transtools

    Args:
        to_lang: 目标语言代码（en / zh / ja / ...）
        content: 待翻译的内容
        from_lang: 源语言代码。Default: ``'zh'``（中文）

    Returns:
        str: 翻译后的结果
    """
    result = wftools.transtools(
        to_lang=to_lang, content=content, from_lang=from_lang,
    )
    print(f"[python-office] transtools  {from_lang}→{to_lang}: {content[:20]!r}")
    return result


# =====================================================================
# 2. qrcodetools - 生成二维码
# =====================================================================

def qrcodetools(url: str, output: str = "./qrcode_img.png") -> str:
    """Generate QR code image from URL.

    把 URL 编码为二维码图片。

    Documentation: https://www.python-office.com/modules/tools/api#qrcodetools

    Args:
        url: 要编码的网址或文本
        output: 二维码图片保存路径。Default: ``'./qrcode_img.png'``

    Returns:
        str: 生成的二维码图片路径
    """
    wftools.qrcodetools(url=url, output=output)
    print(f"[python-office] qrcodetools  → {output}")
    return output


# =====================================================================
# 3. passwordtools - 随机密码
# =====================================================================

def passwordtools(len: int = 8) -> str:
    """Generate random password of specified length.

    生成指定长度的随机密码。

    Documentation: https://www.python-office.com/modules/tools/api#passwordtools

    Args:
        len: 密码长度。Default: ``8``

    Returns:
        str: 生成的随机密码字符串
    """
    password = wftools.passwordtools(len=len)
    print(f"[python-office] passwordtools  长度={len}  密码={password!r}")
    return password


# =====================================================================
# 4. weather - 天气查询（CLI 交互式）
# =====================================================================

def weather() -> None:
    """Get current weather information（CLI 交互式）.

    获取当前天气信息（CLI 场景会引导用户输入城市；GUI 中标占位即可）。

    Documentation: https://www.python-office.com/modules/tools/api#weather
    """
    try:
        city = input("请输入要查询的城市: ").strip()
    except EOFError:
        print("\n[python-office] 非交互式环境，请在 GUI 中使用天气查询。")
        return
    wftools.weather()
    print(f"[python-office] weather  查询：{city}")


# =====================================================================
# 5. url2ip - URL 转 IP
# =====================================================================

def url2ip(url: str) -> str:
    """Resolve URL to IP address.

    把 URL / 域名解析为 IP 地址。

    Documentation: https://www.python-office.com/modules/tools/api#url2ip

    Args:
        url: 要查询的网址或域名

    Returns:
        str: 解析得到的 IP 地址字符串
    """
    ip = wftools.url2ip(url=url)
    print(f"[python-office] url2ip  {url} → {ip}")
    return ip


# =====================================================================
# 6. lottery8ticket - 彩票号码（CLI 交互式）
# =====================================================================

def lottery8ticket() -> None:
    """Generate an 8-digit lottery ticket number（CLI 交互式）.

    生成一张 8 位彩票号码（CLI 场景）。

    Documentation: https://www.python-office.com/modules/tools/api#lottery8ticket
    """
    wftools.lottery8ticket()
    print("[python-office] lottery8ticket  已生成彩票号码")


# =====================================================================
# 7. create_article - AI 生成文章
# =====================================================================

def create_article(theme: str, line_num: int = 200) -> None:
    """Create an article around the given theme.

    围绕主题自动生成文章。

    Documentation: https://www.python-office.com/modules/tools/api#create_article

    Args:
        theme: 文章主题
        line_num: 目标字数。Default: ``200``
    """
    wftools.create_article(theme=theme, line_num=line_num)
    print(f"[python-office] create_article  主题：{theme!r}  字数：{line_num}")


# =====================================================================
# 8. pwd4wifi - WiFi 密码（仅 Windows）
# =====================================================================

def pwd4wifi(len_pwd: int = 8, pwd_list: Optional[List[str]] = None) -> None:
    """Generate WiFi password list (Windows only).

    生成 WiFi 密码字典列表（仅 Windows，依赖 pywifi）。

    Documentation: https://www.python-office.com/modules/tools/api#pwd4wifi

    Args:
        len_pwd: 密码长度。Default: ``8``
        pwd_list: 自定义字符集，留空用默认。Default: ``None``
    """
    if pwd_list is None:
        pwd_list = []
    wftools.pwd4wifi(len_pwd=len_pwd, pwd_list=pwd_list)
    print(f"[python-office] pwd4wifi  长度={len_pwd}  字符集={len(pwd_list)} 项")


# =====================================================================
# 9. net_speed_test - 网速测试（CLI 交互式）
# =====================================================================

def net_speed_test() -> None:
    """Test network upload and download speed（CLI 交互式）.

    测试网络上传和下载速度（CLI 场景）。

    Documentation: https://www.python-office.com/modules/tools/api#net_speed_test
    """
    wftools.net_speed_test()
    print("[python-office] net_speed_test  测试完成")


# =====================================================================
# 10. course - 项目信息
# =====================================================================

def course() -> None:
    """Display project info and resource links for python-office.

    显示 python-office 库的相关信息和资源链接。

    Documentation: https://www.python-office.com/modules/tools/api#course
    """
    random_color_print("=" * 60)
    random_color_print("【python-office 库】，功能持续更新中")
    random_color_print("使用有问题 or 提交功能需求 or 参与项目开发")
    random_color_print("1、给小白的【50 讲 Python 自动化办公】: https://www.python-office.com/course/50-python-office.html")
    random_color_print("2、请+【项目交流群】: https://www.python4office.cn/wechat-group/")
    random_color_print("3、本开源项目的【源代码】: https://github.com/CoderWanFeng/python-office")
    random_color_print("=" * 60)


__all__ = [
    "transtools",
    "qrcodetools",
    "passwordtools",
    "weather",
    "url2ip",
    "lottery8ticket",
    "create_article",
    "pwd4wifi",
    "net_speed_test",
    "course",
]
