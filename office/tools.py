from core.ToolsType import MainTools

mainTools = MainTools()


def transtools(to_lang, content):
    mainTools.transtools(to_lang, content)


def qrcodetools(url):
    mainTools.qrcodetools(url)


def passwordtools(len=8):
    mainTools.passwordtools(len)


def weather():
    mainTools.weather()


# 通过url，获取ip地址
def url2ip(url):
    mainTools.url2ip(url)
