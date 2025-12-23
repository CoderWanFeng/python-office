# -*- coding: UTF-8 -*-
"""Image processing functionality module.

图像处理功能模块。

This module provides rich image processing capabilities including compression,
format conversion, watermark addition/removal, style conversion, and more.

该模块提供了丰富的图像处理功能，包括压缩、格式转换、水印添加/去除、风格转换等。

Author:
    程序员晚枫

Project:
    https://www.python-office.com
"""

import poimage


def compress_image(input_file: str, output_file: str, quality: int):
    """Compress image file to reduce size while maintaining visual quality.
    
    压缩图像文件，以减小其文件大小，同时尽量保持视觉质量。
    
    Args:
        input_file (str): path to input image file to compress / 需要压缩的输入图像文件的路径
        output_file (str): save path for compressed image file / 压缩后的图像文件保存路径
        quality (int): compression quality level, range 0 to 95 / 压缩质量等级，取值范围0到95。Higher value means better quality but larger file size / 数值越高，表示图像质量越好，但文件体积也越大
    
    Returns:
        None
    """

    poimage.compress_image(input_file, output_file, quality)


def image2gif():
    """Convert images to GIF format.
    
    将图像转换为GIF格式。
    
    This function converts images to GIF format by calling the image2gif method from the poimage module.
    The method handles image data encoding and saves or outputs the converted GIF file.
    
    本函数通过调用poimage模块的image2gif方法来实现图像到GIF格式的转换。
    该方法负责处理图像数据，将其编码为GIF格式，并保存或输出转换后的GIF文件。
    
    Returns:
        None
    """
    poimage.image2gif()



# todo：输出文件路径

def add_watermark(file, mark, output_path='./', color="#eaeaea", size=30, opacity=0.35, space=200,
                  angle=30):
    """Add watermark to image.
    
    给图片加水印。
    
    Args:
        file (str): image file location / 图片位置
        mark (str): watermark content / 水印内容
        output_path (str, optional): output location / 输出位置。Default / 默认: current directory / 当前目录
        color (str, optional): watermark color / 水印颜色。Default / 默认: "#eaeaea"
        size (int, optional): watermark size / 水印大小。Default / 默认: 30
        opacity (float, optional): opacity, 0.01~1 / 不透明度，0.01~1。Default / 默认: 0.35
        space (int, optional): watermark spacing / 水印间距。Default / 默认: 200
        angle (int, optional): watermark angle / 水印角度。Default / 默认: 30
    
    Returns:
        None
    """
    poimage.add_watermark(file, mark, output_path, color, size, opacity, space, angle)
    # mainImage.add_watermark(file, mark, out, color, size, opacity, space, angle)


# todo：输入文件路径

def img2Cartoon(path, client_api='', client_secret=''):
    """Convert image to cartoon style.
    
    将图片转换为卡通风格。
    
    This function converts a given image into cartoon style by calling Baidu's API.
    Client API key and secret are used for authentication.
    
    本函数通过调用百度的API，将给定路径下的图片转换成卡通风格的图片。
    客户端的API密钥和密钥秘密用于认证。
    
    Args:
        path (str): image file path / 图片文件的路径
        client_api (str, optional): client API key / 客户端的API密钥。Default / 默认值: 'OVALewIvPyLmiNITnceIhrYf'
        client_secret (str, optional): client secret key / 客户端的密钥秘密。Default / 默认值: 'rpBQH8WuXP4ldRQo5tbDkv3t0VgzwvCN'
    
    Returns:
        None
    """
    # 调用img2Cartoon函数处理图片，参数包括图片路径、API密钥和密钥秘密
    poimage.img2Cartoon(path, client_api, client_secret)



def down4img(url, output_path='.', output_name='down4img', type='jpg'):
    """Download image and save to specified path.
    
    下载图片并保存到指定路径。
    
    Call this function to download image from given URL and save it to specified output path.
    If no output path and name specified, default values will be used.
    
    调用此函数以从URL下载图片，并将其保存在指定的输出路径中。
    如果没有指定输出路径和名称，将使用默认值。
    
    Args:
        url (str): image URL address / 图片的URL地址
        output_path (str, optional): path to save image / 保存图片的路径。Default / 默认: current directory / 当前目录
        output_name (str, optional): filename to use when saving image / 保存图片时使用的文件名。Default / 默认: 'down4img'
        type (str, optional): image file type / 图片的文件类型。Default / 默认: 'jpg'
    
    Returns:
        None
    """
    # 调用poimage模块中的down4img函数执行图片下载和保存操作
    poimage.down4img(url, output_path, output_name, type)


def txt2wordcloud(filename, color="white", result_file="your_wordcloud.png"):
    """Generate word cloud image from specified text file.
    
    根据指定的文本文件生成词云图像。
    
    Args:
        filename (str): text file path / 文本文件的路径
        color (str, optional): word cloud background color / 词云的背景颜色。Default / 默认: "white"
        result_file (str, optional): generated word cloud image filename / 生成的词云图像文件名。Default / 默认: "your_wordcloud.png"
    
    Returns:
        None
    """
    # 调用poimage模块的txt2wordcloud方法生成词云
    poimage.txt2wordcloud(filename, color, result_file)



def pencil4img(input_img, output_path='./', output_name='pencil4img.jpg'):
    """Process image using pencil4img algorithm.
    
    使用pencil4img算法处理图像。
    
    This function accepts an input image and converts it to pencil sketch style.
    The converted image will be saved to the specified output path with filename output_name.
    
    该函数接受一个输入图像，并将其转换为铅笔画风格的图像。
    转换后的图像将保存在指定的输出路径下，文件名为output_name。
    
    Args:
        input_img (str): input image file path / 输入的图像文件路径
        output_path (str, optional): output image path / 输出图像的路径。Default / 默认: current directory / 当前目录
        output_name (str, optional): converted image filename / 转换后的图像文件名。Default / 默认: 'pencil4img.jpg'
    
    Returns:
        None
    """
    # 调用poimage库中的pencil4img函数处理图像
    poimage.pencil4img(input_img, output_path, output_name)



def decode_qrcode(qrcode_path):
    """Decode QR code.
    
    解析二维码。
    
    Args:
        qrcode_path (str): QR code image path / 二维码图片的路径
    
    Returns:
        None
    """
    poimage.decode_qrcode(qrcode_path)


def del_watermark(input_image, output_image=r'./del_water_mark.jpg'):
    """Remove watermark from input image and save processed image to specified path.
    
    从输入的图片中删除水印，并保存处理后的图片到指定路径。
    
    Args:
        input_image (str): input image path / 输入图片的路径。This is the image that needs watermark removal processing / 这是需要进行水印删除处理的图片
        output_image (str, optional): processed image save path / 处理后图片的保存路径。Default / 默认: './del_water_mark.jpg' in current directory / 当前目录下的'del_water_mark.jpg'
    
    Returns:
        None
    """
    # 调用poimage库中的del_watermark函数来删除图片中的水印
    poimage.del_watermark(input_image, output_image)

