# -*- coding: UTF-8 -*-
import poimage


def compress_image(input_file: str, output_file: str, quality: int):
    poimage.compress_image(input_file, output_file, quality)


def image2gif():
    poimage.image2gif()


# todo：输出文件路径

def add_watermark(file, mark, output_path='./', color="#eaeaea", size=30, opacity=0.35, space=200,
                  angle=30):
    """
    给图片加水印
    Args:
        file: 图片位置
        mark: 水印内容
        output_path: 输出位置
        color: 水印颜色
        size: 水印大小
        opacity: 不透明度，0.01~1
        space: 水印间距
        angle: 水印角度

    Returns:

    """
    poimage.add_watermark(file, mark, output_path, color, size, opacity, space, angle)
    # mainImage.add_watermark(file, mark, out, color, size, opacity, space, angle)


# todo：输入文件路径

def img2Cartoon(path, client_api='OVALewIvPyLmiNITnceIhrYf', client_secret='rpBQH8WuXP4ldRQo5tbDkv3t0VgzwvCN'):
    poimage.img2Cartoon(path, client_api, client_secret)
    # mainImage.img2Cartoon(path, client_api, client_secret)


def down4img(url, output_path='.', output_name='down4img', type='jpg'):
    poimage.down4img(url, output_path, output_name, type)
    # mainImage.down4img(url, output_name, type)


def txt2wordcloud(filename, color="white", result_file="your_wordcloud.png"):
    poimage.txt2wordcloud(filename, color, result_file)


def pencil4img(input_img, output_path='./', output_name='pencil4img.jpg'):
    poimage.pencil4img(input_img, output_path, output_name)


def decode_qrcode(qrcode_path):
    """
    解析二维码
    :param qrcode_path: 二维码图片的路径
    :return:
    """
    poimage.decode_qrcode(qrcode_path)


def del_watermark(input_image, output_image=r'./del_water_mark.jpg'):
    poimage.del_watermark(input_image, output_image)
