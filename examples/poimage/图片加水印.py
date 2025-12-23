# -*- coding: UTF-8 -*-
"""Add watermark to image example.

图片加水印示例。

This example demonstrates how to use python-office library to add watermark to images.

该示例演示如何使用python-office库给图片添加水印。

Args:
    file: image file path to add watermark / 要添加水印的图片文件路径
    mark: watermark text content / 水印文本内容
    output_path: output image save path / 输出图片的保存路径

Example:
    >>> import office
    >>> office.image.add_watermark(file='./test_files/add_watermark/程序员晚枫-2.jpg',
    ...                           mark='程序员晚枫',
    ...                           output_path=r'./test_files/add_watermark/mark_img')
"""

# Add watermark to image / 给图片加水印
import office

office.image.add_watermark(file='./test_files/add_watermark/程序员晚枫-2.jpg',
                           mark='程序员晚枫',
                           output_path=r'./test_files/add_watermark/mark_img')
