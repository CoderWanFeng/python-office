# -*- coding: UTF-8 -*-
import poimage


def compress_image(input_file: str, output_file: str, quality: int):
    """
    压缩图像文件，以减小其文件大小，同时尽量保持视觉质量。

    参数:
    input_file (str): 需要压缩的输入图像文件的路径。
    output_file (str): 压缩后的图像文件保存路径。
    quality (int): 压缩质量等级，取值范围为 0 到 95。数值越高，表示图像质量越好，但文件体积也越大。

    返回值:
    None
    """

    poimage.compress_image(input_file, output_file, quality)


def image2gif():
    """
    将图像转换为 GIF 格式。

    本函数通过调用 poimage 模块的 image2gif 方法来实现图像到 GIF 格式的转换。
    该方法负责处理图像数据，将其编码为 GIF 格式，并保存或输出转换后的 GIF 文件。
    """
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

def img2Cartoon(path, client_api='', client_secret=''):
    """
    将图片转换为卡通风格。

    本函数通过调用百度的API，将给定路径下的图片转换成卡通风格的图片。客户端的API密钥和密钥秘密用于认证。

    参数:
    - path (str): 图片文件的路径。
    - client_api (str): 客户端的API密钥，默认值为'OVALewIvPyLmiNITnceIhrYf'。
    - client_secret (str): 客户端的密钥秘密，默认值为'rpBQH8WuXP4ldRQo5tbDkv3t0VgzwvCN'。

    返回:
    无直接返回值，但会生成或显示转换后的卡通风格图片。
    """
    # 调用img2Cartoon函数处理图片，参数包括图片路径、API密钥和密钥秘密
    poimage.img2Cartoon(path, client_api, client_secret)



def down4img(url, output_path='.', output_name='down4img', type='jpg'):
    """
    下载图片并保存到指定路径。

    调用此函数以从给定的URL下载图片，并将其保存在指定的输出路径中。如果没有指定输出路径和名称，将使用默认值。

    参数:
    - url (str): 图片的URL地址。
    - output_path (str, optional): 保存图片的路径，默认为当前目录('.')。
    - output_name (str, optional): 保存图片时使用的文件名，默认为'output_name'。
    - type (str, optional): 图片的文件类型，默认为'jpg'。

    返回:
    无返回值。图片将直接保存到指定的路径中。
    """
    # 调用poimage模块中的down4img函数执行图片下载和保存操作
    poimage.down4img(url, output_path, output_name, type)


def txt2wordcloud(filename, color="white", result_file="your_wordcloud.png"):
    """
    根据指定的文本文件生成词云图像。

    参数:
    filename (str): 文本文件的路径。
    color (str, optional): 词云的背景颜色。默认为 "white"。
    result_file (str, optional): 生成的词云图像文件名。默认为 "your_wordcloud.png"。

    返回:
    无返回值，但会生成一个词云图像文件。
    """
    # 调用poimage模块的txt2wordcloud方法生成词云
    poimage.txt2wordcloud(filename, color, result_file)



def pencil4img(input_img, output_path='./', output_name='pencil4img.jpg'):
    """
    使用pencil4img算法处理图像。

    该函数接受一个输入图像，并将其转换为铅笔画风格的图像。转换后的图像将保存在指定的输出路径下，文件名为output_name。

    参数:
    - input_img: 输入的图像文件路径。必须是一个字符串，表示图像文件的路径。
    - output_path: 输出图像的路径。这是一个可选参数，默认值为当前目录('./')。
    - output_name: 转换后的图像文件名。这是一个可选参数，默认值为'pencil4img.jpg'。

    返回值:
    无返回值。函数将处理后的图像保存在指定路径下。
    """
    # 调用poimage库中的pencil4img函数处理图像
    poimage.pencil4img(input_img, output_path, output_name)



def decode_qrcode(qrcode_path):
    """
    解析二维码
    :param qrcode_path: 二维码图片的路径
    :return:
    """
    poimage.decode_qrcode(qrcode_path)


def del_watermark(input_image, output_image=r'./del_water_mark.jpg'):
    """
    从输入的图片中删除水印，并保存处理后的图片到指定路径。

    参数:
    input_image (str): 输入图片的路径，这是需要进行水印删除处理的图片。
    output_image (str, optional): 处理后图片的保存路径。默认为当前目录下的'del_water_mark.jpg'。

    返回:
    无返回值。该函数直接将处理后的图片文件保存到指定路径。
    """
    # 调用poimage库中的del_watermark函数来删除图片中的水印
    poimage.del_watermark(input_image, output_image)

