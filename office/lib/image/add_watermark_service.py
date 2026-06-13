
"""
图片添加水印，参考：
"""

import math
import os

from PIL import Image, ImageFont, ImageDraw, ImageEnhance, ImageChops

TTF_FONT = os.path.dirname(__file__) + "/font/msyh.ttc"


def crop_image(im: Image.Image) -> Image.Image:
    """裁剪图片边缘空白。
    
    Args:
        im (Image.Image): 图片对象
    
    Returns:
        Image.Image: 裁剪后的图片对象
    """
    bg = Image.new(mode='RGBA', size=im.size)
    bbox = ImageChops.difference(im, bg).getbbox()
    if bbox:
        return im.crop(bbox)
    return im


def set_opacity(im: Image.Image, opacity: float) -> Image.Image:
    """设置水印透明度。
    
    Args:
        im (Image.Image): 图片对象
        opacity (float): 透明度值，范围0-1
    
    Returns:
        Image.Image: 设置透明度后的图片对象
    """
    assert 0 <= opacity <= 1
    alpha = im.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    im.putalpha(alpha)
    return im


def get_mark_img(text: str, color: str = "#8B8B1B", size: int = 30, opacity: float = 0.15) -> Image.Image:
    """生成水印图片。
    
    Args:
        text (str): 水印文字
        color (str, optional): 水印颜色，默认为"#8B8B1B"
        size (int, optional): 字体大小，默认为30
        opacity (float, optional): 透明度，默认为0.15
    
    Returns:
        Image.Image: 生成的水印图片对象
    """
    width = len(text) * size
    mark = Image.new(mode='RGBA', size=(width, size + 20))
    draw_table = ImageDraw.Draw(im=mark)
    draw_table.text(xy=(0, 0),
                    text=text,
                    fill=color,
                    font=ImageFont.truetype(TTF_FONT, size=size))
    del draw_table
    # 裁剪空白
    mark = crop_image(mark)
    # 透明度
    set_opacity(mark, opacity)
    return mark


def im_add_mark(im: Image.Image, text: str, color: str = "#8B8B1B", size: int = 30, opacity: float = 0.15, space: int = 75, angle: int = 30) -> Image.Image:
    """给图片对象添加水印。
    
    Args:
        im (Image.Image): 原始图片对象
        text (str): 水印文字
        color (str, optional): 水印颜色，默认为"#8B8B1B"
        size (int, optional): 字体大小，默认为30
        opacity (float, optional): 透明度，默认为0.15
        space (int, optional): 水印间距，默认为75
        angle (int, optional): 旋转角度，默认为30
    
    Returns:
        Image.Image: 添加水印后的图片对象
    """
    # 获取水印图片对象
    mark = get_mark_img(text, color, size, opacity)
    # 将水印图片扩展并旋转生成水印大图
    w, h = im.size
    c = int(math.sqrt(w ** 2 + h ** 2))
    mark2 = Image.new(mode='RGBA', size=(c, c))
    y, idx = 0, 0
    mark_w, mark_h = mark.size
    while y < c:
        x = -int((mark_w + space) * 0.5 * idx)
        idx = (idx + 1) % 2
        while x < c:
            mark2.paste(mark, (x, y))
            x = x + mark_w + space
        y = y + mark_h + space
    # 将水印大图旋转一定角度
    mark2 = mark2.rotate(angle)
    # 在原图上添加水印大图
    if im.mode != 'RGBA':
        im = im.convert('RGBA')
    im.paste(mark2, (int((w - c) / 2), int((h - c) / 2)),  # 坐标
             mask=mark2.split()[3])
    return im


def add_mark2file(imageFile: str, text: str, out: str = "output", color: str = "#8B8B1B", size: int = 30, opacity: float = 0.15, space: int = 75, angle: int = 30) -> None:
    """添加水印，然后保存图片。
    
    Args:
        imageFile (str): 原始图片文件路径
        text (str): 水印文字
        out (str, optional): 输出目录，默认为"output"
        color (str, optional): 水印颜色，默认为"#8B8B1B"
        size (int, optional): 字体大小，默认为30
        opacity (float, optional): 透明度，默认为0.15
        space (int, optional): 水印间距，默认为75
        angle (int, optional): 旋转角度，默认为30
    """
    name = os.path.basename(imageFile)
    new_name = os.path.join(out, name)
    try:
        im = Image.open(imageFile)
        image = im_add_mark(im, text, color, size, opacity, space, angle)
        if not os.path.exists(out):
            os.mkdir(out)
        if os.path.splitext(new_name)[1] != '.png':
            image = image.convert('RGB')
        image.save(new_name)
        print(new_name, "保存成功。")
    except Exception as e:
        print(new_name, "保存失败。错误信息：", e)
