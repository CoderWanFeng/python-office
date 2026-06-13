# -*- coding: UTF-8 -*-
"""Add watermark to video example.

给视频添加水印示例。

This example demonstrates how to use python-office library to add watermark to videos.

该示例演示如何使用python-office库给视频添加水印。

Args:
    video_path (str): input video file path / 输入视频文件路径
    output_path (str): output video save path / 输出视频保存路径

Example:
    >>> import office
    >>> office.video.mark2video(
    ...     video_path=r'D:\download\video.mp4',
    ...     output_path=r'D:\download\out'
    ... )

Note:
    - Watermark content can be customized through parameters / 水印内容可通过参数自定义
    - Supports various video formats / 支持多种视频格式
"""

import office

office.video.mark2video(video_path=r'D:\download\baiduyun\图片添加水印.mp4', output_path=r'D:\download\baiduyun\out')
