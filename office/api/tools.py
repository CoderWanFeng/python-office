from office.lib.decorator_utils.instruction_url import instruction

from office.lib.utils.except_utils import except_dec

# from office.core.ToolsType import wftools

# wftools = wftools()

import wftools

# @except_dec()
@instruction
def transtools(to_lang, content):
    wftools.transtools(to_lang, content)


# @except_dec()
@instruction
def qrcodetools(url):
    wftools.qrcodetools(url)


# @except_dec()
@instruction
def passwordtools(len=8):
    return wftools.passwordtools(len)


# @except_dec()
@instruction
def weather():
    wftools.weather()


# 通过url，获取ip地址
# # @except_dec()
@instruction
def url2ip(url):
    wftools.url2ip(url)


# 通过url，获取ip地址
# @except_dec()
@instruction
def lottery8ticket():
    wftools.lottery8ticket()


# @except_dec()
@instruction
def create_article(theme, line_num=200):
    wftools.create_article(theme, line_num)


# @except_dec()
@instruction
def pwd4wifi(len_pwd=8, pwd_list=[]):
    wftools.pwd4wifi(len_pwd, pwd_list)

# 测试网速
@instruction
def net_speed_test():
    wftools.net_speed_test()