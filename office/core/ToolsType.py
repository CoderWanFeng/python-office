from translate import Translator
import qrcode
import string
import random
import socket
import time
from office.lib.tools.lottery8ticket import ticket_kinds

from office.lib.tools.weather_city_code import WEATHER_CITY_CODE_DIC
from office.lib.tools.weather_service import weather_spider


# from utils.tools.weather_city_code import WEATHER_CITY_CODE_DIC


class MainTools():

    def transtools(self, to_lang, content):
        # specifying the language
        translator = Translator(to_lang)
        # typing the message
        translation = translator.translate(content)
        # print the translated message
        print(translation)

    def qrcodetools(self, url):
        # Creating object
        # version: defines size of image from integer(1 to 40), box_size = size of each box in pixels, border = thickness of the border.
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        # add_date :  pass the input text
        qr.add_data(url)
        # converting into image
        qr.make(fit=True)
        # specify the foreground and background color for the img
        img = qr.make_image(fill='black', back_color='white')
        # store the image
        img.save('qrcode_img.png')

    def passwordtools(self, len):
        """
        @Author & Date  : CoderWanFeng 2022/5/9 11:54
        @Desc  : 随机密码生成器，默认是8位
        @Return  ：
        """
        chars = string.digits + string.ascii_letters
        return ''.join(random.sample(chars * 10, len))

    def weather(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7'
        }
        while (True):
            try:
                cityName = input('请输入城市名称(按q/Q键退出)：')
                if cityName == 'q' or cityName == 'Q':
                    break
                cityCode = WEATHER_CITY_CODE_DIC[cityName]  # 得到城市代码
                url = 'http://www.weather.com.cn/weather1d/%d.shtml' % cityCode  # 得到城市天气网址
                weather_spider(url, headers)
            except:
                print('未查到%s城市，请重新输入：' % cityName)

    # 通过url，获取ip地址
    def url2ip(self, url):
        socket_list = socket.getaddrinfo(url, None, 0, socket.SOCK_STREAM)
        ip_info = socket_list[0][4][0]
        print('【{}】 这个网址对应的IP地址是：{}'.format(url, ip_info))

    def lottery8ticket(self):
        '''
        自动生成彩票
        种类代码：

        '''
        while True:
            for num, name_def in ticket_kinds.items():
                print(num, name_def[0])
            kind = input("选择一个种类：")
            if kind == str(0):
                break
            print('*' * 20)
            if not ticket_kinds.get(kind)[1]():
                print('这个规则太复杂了，我们正在开发。如果可以提供建议，请私信：http://t.cn/A6XVQXAk')
            else:
                print(f'{ticket_kinds.get(kind)[0]}的号码是 -->> {ticket_kinds.get(kind)[1]()}')
            print('*' * 20)
