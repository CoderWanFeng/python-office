from office.lib.utils.except_utils import except_dec

from office.core.ToolsType import MainTools

mainTools = MainTools()


@except_dec()
def transtools(to_lang, content):
    mainTools.transtools(to_lang, content)


@except_dec()
def qrcodetools(url):
    mainTools.qrcodetools(url)


@except_dec()
def passwordtools(len=8):
    mainTools.passwordtools(len)


@except_dec()
def weather():
    mainTools.weather()


# 通过url，获取ip地址
@except_dec()
def url2ip(url):
    mainTools.url2ip(url)


# 通过url，获取ip地址
@except_dec()
def lottery8ticket():
    mainTools.lottery8ticket()
