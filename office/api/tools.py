from office.lib.utils.except_utils import except_dec

# from office.core.ToolsType import wftools

# wftools = wftools()

import wftools

# @except_dec()
def transtools(to_lang, content):
    wftools.transtools(to_lang, content)


# @except_dec()
def qrcodetools(url):
    wftools.qrcodetools(url)


# @except_dec()
def passwordtools(len=8):
    wftools.passwordtools(len)


# @except_dec()
def weather():
    wftools.weather()


# 通过url，获取ip地址
# # @except_dec()
def url2ip(url):
    wftools.url2ip(url)


# 通过url，获取ip地址
# @except_dec()
def lottery8ticket():
    wftools.lottery8ticket()


# @except_dec()
def create_article(theme, line_num=200):
    wftools.create_article(theme, line_num)


# @except_dec()
def pwd4wifi(len_pwd=8, pwd_list=[]):
    wftools.pwd4wifi(len_pwd, pwd_list)

# 测试网速
def net_speed_test():
    wftools.net_speed_test()