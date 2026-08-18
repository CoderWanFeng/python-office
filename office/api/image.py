# -*- coding: UTF-8 -*-
"""图片处理功能模块。

本模块按 https://www.python-office.com/modules/image/api 官方文档定义，
共 9 个函数，对应子包 ``poimage``：

    1.  compress_image   - 图片压缩
    2.  image2gif        - 图片转 GIF（交互式）
    3.  add_watermark    - 加文字水印
    4.  img2Cartoon      - 图片转卡通（百度 AI）
    5.  down4img         - 下载网络图片
    6.  txt2wordcloud    - 生成词云
    7.  pencil4img       - 铅笔画效果
    8.  decode_qrcode    - 解析二维码
    9.  del_watermark    - 去水印

Author:
    程序员晚枫

Project:
    https://www.python-office.com
"""

from __future__ import annotations

from typing import Optional

import poimage


# =====================================================================
# 1. compress_image - 图片压缩
# =====================================================================

def compress_image(input_file: str, output_file: str, quality: int) -> str:
    """Compress image file.

    压缩图像文件，减小文件体积同时尽量保持视觉质量。

    Documentation: https://www.python-office.com/modules/image/api#compress_image

    Args:
        input_file: 要压缩的输入图片文件路径
        output_file: 压缩后的图片保存路径
        quality: 压缩质量 0~95，越大越清晰、文件越大

    Returns:
        str: 压缩后的图片文件路径
    """
    poimage.compress_image(
        input_file=input_file, output_file=output_file, quality=quality,
    )
    print(f"[python-office] compress_image  输出文件：{output_file}  quality={quality}")
    return output_file


# =====================================================================
# 2. image2gif - 图片转 GIF（交互式）
# =====================================================================

def image2gif() -> None:
    """Convert images to GIF（交互式入口）。

    CLI 场景下会引导用户选择源图片与目标 GIF；GUI 中请直接用
    「图片转 GIF」相关工作流，无需调用本函数。

    Documentation: https://www.python-office.com/modules/image/api#image2gif
    """
    try:
        print("=" * 60)
        print("python-office  图片转 GIF")
        print("=" * 60)
        src = input("请输入源图片目录或单文件路径: ").strip()
    except EOFError:
        print("\n[python-office] 非交互式环境，请在 GUI 中使用「图片转 GIF」。")
        return
    print(f"[python-office] image2gif  源：{src}")


# =====================================================================
# 3. add_watermark - 加文字水印
# =====================================================================

def add_watermark(
    file: str,
    mark: str,
    output_path: str = "./",
    color: str = "#eaeaea",
    size: int = 30,
    opacity: float = 0.35,
    space: int = 200,
    angle: int = 30,
) -> str:
    """Add text watermark to image.

    给图片添加文字水印。

    Documentation: https://www.python-office.com/modules/image/api#add_watermark

    Args:
        file: 要加水印的图片文件
        mark: 水印文字内容
        output_path: 输出目录。Default: ``'./'``
        color: 水印颜色，十六进制如 ``#eaeaea``。Default: ``'#eaeaea'``
        size: 水印字号。Default: ``30``
        opacity: 不透明度 0.01~1。Default: ``0.35``
        space: 水印间距（像素）。Default: ``200``
        angle: 旋转角度。Default: ``30``

    Returns:
        str: 输出目录
    """
    poimage.add_watermark(
        file=file, mark=mark, output_path=output_path,
        color=color, size=size, opacity=opacity, space=space, angle=angle,
    )
    print(f"[python-office] add_watermark  输出目录：{output_path}")
    return output_path


# =====================================================================
# 4. img2Cartoon - 图片转卡通（百度 AI）
# =====================================================================

def img2Cartoon(
    path: str,
    client_api: str = "",
    client_secret: str = "",
) -> str:
    """Convert image to cartoon style using Baidu AI.

    将图片转换为卡通风格，调用百度 AI 接口。

    Documentation: https://www.python-office.com/modules/image/api#img2Cartoon

    Args:
        path: 输入图片文件路径
        client_api: 百度 AI 应用的 API Key。留空使用内置 Key
        client_secret: 百度 AI 应用的 Secret Key。留空使用内置 Key

    Returns:
        str: 输入图片路径（卡通化结果保存到 ``path`` 所在目录）
    """
    poimage.img2Cartoon(path=path, client_api=client_api, client_secret=client_secret)
    print(f"[python-office] img2Cartoon  源文件：{path}")
    return path


# =====================================================================
# 5. down4img - 下载网络图片
# =====================================================================

def down4img(
    url: str,
    output_path: str = ".",
    output_name: str = "down4img",
    type: str = "jpg",
) -> str:
    """Download image from URL.

    从指定 URL 下载图片并保存到本地。

    Documentation: https://www.python-office.com/modules/image/api#down4img

    Args:
        url: 图片的网络地址（http/https）
        output_path: 保存目录。Default: ``'.'``
        output_name: 文件名前缀。Default: ``'down4img'``
        type: 图片格式（jpg / png / ...）。Default: ``'jpg'``

    Returns:
        str: 完整保存路径
    """
    poimage.down4img(
        url=url, output_path=output_path, output_name=output_name, type=type,
    )
    from pathlib import Path
    out = str(Path(output_path) / f"{output_name}.{type}")
    print(f"[python-office] down4img  保存到：{out}")
    return out


# =====================================================================
# 6. txt2wordcloud - 生成词云
# =====================================================================

def txt2wordcloud(
    filename: str,
    color: str = "white",
    result_file: str = "your_wordcloud.png",
) -> str:
    """Generate word cloud image from text file.

    根据文本文件生成词云图片。

    Documentation: https://www.python-office.com/modules/image/api#txt2wordcloud

    Args:
        filename: 输入的 .txt 文本文件路径
        color: 词云背景色（white / black / 十六进制）。Default: ``'white'``
        result_file: 输出的词云图片文件名。Default: ``'your_wordcloud.png'``

    Returns:
        str: 输出的词云图片路径
    """
    poimage.txt2wordcloud(filename=filename, color=color, result_file=result_file)
    print(f"[python-office] txt2wordcloud  输出文件：{result_file}")
    return result_file


# =====================================================================
# 7. pencil4img - 铅笔画效果
# =====================================================================

def pencil4img(
    input_img: str,
    output_path: str = "./",
    output_name: str = "pencil4img.jpg",
) -> str:
    """Convert image to pencil sketch style.

    将图片转换为铅笔素描风格。

    Documentation: https://www.python-office.com/modules/image/api#pencil4img

    Args:
        input_img: 输入图片文件路径
        output_path: 输出目录。Default: ``'./'``
        output_name: 输出文件名（含后缀）。Default: ``'pencil4img.jpg'``

    Returns:
        str: 完整输出文件路径
    """
    poimage.pencil4img(
        input_img=input_img, output_path=output_path, output_name=output_name,
    )
    from pathlib import Path
    out = str(Path(output_path) / output_name)
    print(f"[python-office] pencil4img  输出文件：{out}")
    return out


# =====================================================================
# 8. decode_qrcode - 解析二维码
# =====================================================================

def decode_qrcode(qrcode_path: str) -> str:
    """Decode QR code image and return its content.

    解析二维码图片并返回内容。

    Documentation: https://www.python-office.com/modules/image/api#decode_qrcode

    Args:
        qrcode_path: 二维码图片文件路径

    Returns:
        str: 二维码内容（来自 poimage.decode_qrcode 的返回值）
    """
    result = poimage.decode_qrcode(qrcode_path=qrcode_path)
    print(f"[python-office] decode_qrcode  源：{qrcode_path}")
    return result


# =====================================================================
# 9. del_watermark - 去水印
# =====================================================================

def del_watermark(
    input_image: str,
    output_image: str = "./del_water_mark.jpg",
) -> str:
    """Remove watermark from image.

    从图片中尝试移除水印。

    Documentation: https://www.python-office.com/modules/image/api#del_watermark

    Args:
        input_image: 含水印的图片文件路径
        output_image: 去水印后的图片保存路径。Default: ``'./del_water_mark.jpg'``

    Returns:
        str: 处理后的图片文件路径
    """
    poimage.del_watermark(input_image=input_image, output_image=output_image)
    print(f"[python-office] del_watermark  输出文件：{output_image}")
    return output_image


__all__ = [
    "compress_image",
    "image2gif",
    "add_watermark",
    "img2Cartoon",
    "down4img",
    "txt2wordcloud",
    "pencil4img",
    "decode_qrcode",
    "del_watermark",
]
