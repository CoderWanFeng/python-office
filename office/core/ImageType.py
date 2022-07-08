import os
# from lib.image import add_watermark_service
# 生成词云需要使用的类库
from PIL import Image
from alive_progress import alive_bar

from office.lib.image import add_watermark_service
import base64
import requests


class MainImage():

    # 自动生成gif
    def image2gif(self):
        im = Image.open("1.jpg")
        images = []
        images.append(Image.open('2.jpg'))
        images.append(Image.open('3.jpg'))
        im.save('gif.gif', save_all=True, append_images=images, loop=1, duration=1, comment=b"aaabb")

    # from wordcloud import WordCloud
    # import jieba

    # def txt2wordcloud(filename, color="white", result_file="your_wordcloud.png"):
    #     """
    #     @Author & Date  : CoderWanFeng 2022/4/28 9:26
    #     @Desc  : 生成词云的代码，可以添加更多个性化功能
    #     @Return  ：
    #     """
    #     with open(filename, encoding='utf8') as fp:
    #         text = fp.read()
    #         # 将读取的中文文档进行分词
    #         # 接收分词的字符串
    #         word_list = jieba.cut(text)
    #         # 分词后在单独个体之间加上空格
    #         cloud_text = " ".join(word_list)
    #
    #         # 生成wordcloud对象
    #         wc = WordCloud(background_color=color,
    #                        max_words=200,
    #                        min_font_size=15,
    #                        max_font_size=50,
    #                        width=400,
    #                        font_path="msyh.ttc",  # 默认的简体中文字体，没有会报错
    #                        )
    #         wc.generate(cloud_text)
    #         wc.to_file(result_file)

    def add_watermark(self, file, mark, out="output", color="#8B8B1B", size=30, opacity=0.15, space=75, angle=30):
        """
        @Author & Date  : demo 2022/5/6 14:33
        @Desc  : 给图片添加水印
        @Return  ： 添加了水印的图片，输出到out指定的文件夹
        """
        if os.path.isdir(file):
            names = os.listdir(file)
            with alive_bar(len(names)) as bar:
                for name in names:
                    bar()
                    image_file = os.path.join(file, name)
                    add_watermark_service.add_mark2file(image_file, mark, out, color, size, opacity, space, angle)
        else:
            add_watermark_service.add_mark2file(file, mark, out, color, size, opacity, space, angle)

    def get_access_token(self, client_api, client_secret):

        # 获取token的API
        url = 'https://aip.baidubce.com/oauth/2.0/token'
        # 获取access_token需要的参数
        params = {
            # 固定参数
            'grant_type': 'client_credentials',
            # 必选参数，传入你的API Key
            'client_id': client_api,
            # 必选参数，传入你的Secret Key
            'client_secret': client_secret
        }
        # 发送请求，获取响应数据

        response = requests.post(url, params)
        # 将响应的数据转成字典类型，然后取出access_token
        access_token = eval(response.text)['access_token']
        # 将access_token返回
        return access_token

    def img2Cartoon(self, path, client_api, client_secret):
        print('=' * 30)
        print('正在进行动漫头像的转换')
        print('本仓库的视频教程：http://t.cn/A6aAvu47')
        print('这个接口调用的是百度AI平台的免费试用接口（200次），如果代码报错，大概率是试用次数没有了')
        print('获取免费使用次数的教程，我整理在这个文档里了：https://python-office.com/office/image.html')
        print('=' * 30)

        # 头像动漫化的API
        url = 'https://aip.baidubce.com/rest/2.0/image-process/v1/selfie_anime'
        # 以二进制的方式读取原始图片
        origin_im = open(path, 'rb')
        # 将图片进行base64编码
        path = base64.b64encode(origin_im.read())
        # 关闭原图片
        origin_im.close()
        # 请求的headers信息，固定写法
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        # 请求的参数
        params = {
            # 开始获取的access_token
            'access_token': self.get_access_token(client_api, client_secret),
            # 图片的base64编码
            'image': path,
        }
        # 发送请求
        response = requests.post(url, data=params, headers=headers)
        # 对响应结果进行处理
        if response:
            # 打开一个文件
            f = open('result.jpg', 'wb')
            try:
                # 获取动漫头像
                anime = response.json()['image']
            except:
                raise Exception('你没有开通百度AI账号，错误原因以及【免费】开通方式，见：https://mp.weixin.qq.com/s/5Eyk2j20jzSaVcr1DTsfvw')
            # 对返回的头像进行解码
            anime = base64.b64decode(anime)
            # 将头像写入文件当中
            f.write(anime)
            f.close()
        print('*' * 20 + "{}".format('动漫头像名称：result.jpg') + '*' * 20)
        print('*' * 20 + "{}".format('您的动漫头像转换完毕，请在本代码运行的文档里查看') + '*' * 20)

    def down4img(self, url, output_name, type):
        """
        下载指定url的一张图片，支持所有格式:jpg\png\gif .etc
        """
        response = requests.get(url, stream=True)
        with open('.'.join((output_name, type)), 'wb') as output_img:
            for chunk in response:
                output_img.write(chunk)
            output_img.close()
            print(f"下载成功，图片名称：{'.'.join((output_name, type))}")
