# -*- coding: UTF-8 -*-
"""Video Skills 包 - 统一暴露视频处理相关的所有 Skills"""
from .video2mp3 import video2mp3
from .audio2txt import audio2txt
from .mark2video import mark2video
from .txt2mp3 import txt2mp3

__all__ = [
    'video2mp3',
    'audio2txt',
    'mark2video',
    'txt2mp3',
]
