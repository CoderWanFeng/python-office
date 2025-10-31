# -*- coding: UTF-8 -*-
"""
下载图片示例

该示例演示如何使用python-office库下载网络图片。

Args:
    url: 要下载的图片链接
    output_name: 下载后的图片名称（可选，默认：down4img）
    type: 下载后的图片类型（可选，默认：jpg）

Example:
    >>> import office
    >>> office.image.down4img(
    ...     url='https://cos.python-office.com/icon2.jpg',
    ...     output_name='./test_files/下载图片/B站：程序员晚枫',
    ...     type='jpg')

Author:
    程序员晚枫

Project:
    https://www.python-office.com
"""

# 导入这个库：python-office，简写为office
import office

office.image.down4img(
    url='https://cos.python-office.com/icon2.jpg',
    output_name='./test_files/下载图片/B站：程序员晚枫',
    type='jpg')
# 参数说明：
# url：你要下载的图片链接
# output_name：下载后的图片名称，可以不填，默认：down4img
# type：下载后的图片类型，可以不填，默认：jpg
