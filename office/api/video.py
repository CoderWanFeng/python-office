"""Video processing functionality module.

视频处理功能模块。

This module provides video processing capabilities including format conversion,
audio extraction, watermark addition, text-to-speech, and more.

该模块提供了视频处理功能，包括格式转换、音频提取、水印添加、文本转语音等。

Author:
    程序员晚枫

Project:
    https://www.python-office.com
"""

import povideo

# 从视频里提取音频




def video2mp3(path, mp3_name=None, output_path=r'./'):
    """Convert video file to mp3 audio file.
    
    将视频文件转换为mp3音频文件。
    
    Args:
        path (str): video file path / 视频文件的路径
        mp3_name (str, optional): output mp3 filename / 输出mp3文件的名称。If not provided, defaults to original video filename / 如果未提供，默认为原视频文件名
        output_path (str, optional): output mp3 file path / 输出mp3文件的路径。Default / 默认: current directory / 当前目录
    
    Returns:
        None: generates mp3 file in specified output path / 在指定输出路径下生成mp3文件
    """
    povideo.video2mp3(path, mp3_name, output_path)

def audio2txt(audio_path, appid, secret_id, secret_key):
    """Extract text from audio.
    
    从音频里提取文字。
    
    Note: Local audio file cannot exceed 5MB.
    注意：本地语音文件不能大于5MB。
    
    Args:
        audio_path (str): audio file path / 音频文件路径
        appid (str): speech recognition API application ID / 语音识别API的应用ID
        secret_id (str): speech recognition API secret ID / 语音识别API的密钥ID
        secret_key (str): speech recognition API secret key / 语音识别API的密钥
    
    Returns:
        None
    """
    povideo.audio2txt(audio_path, appid, secret_id, secret_key)



def mark2video(video_path, output_path=r'./', output_name=r'mark2video.mp4', mark_str: str = "www.python-office.com",
               font_size=28,
               font_type='Arial', font_color='white'):
    """Add watermark to video.
    
    给视频添加水印。
    
    Args:
        video_path (str): video file path / 视频地址
        output_path (str, optional): output path / 输出地址。Default / 默认: current directory / 当前目录
        output_name (str, optional): output filename, remember to include '.mp4' / 输出名称，记得带'.mp4'。Default / 默认: 'mark2video.mp4'
        mark_str (str, optional): watermark content, only supports English / 水印内容，只支持英文。Default / 默认: 'www.python-office.com'
        font_size (int, optional): watermark font size / 水印字体大小。Default / 默认: 28
        font_type (str, optional): watermark font type / 水印字体类型。Default / 默认: 'Arial'
        font_color (str, optional): watermark color / 水印颜色。Default / 默认: 'white'
    
    Returns:
        None
    """
    povideo.mark2video(video_path, output_path, output_name, mark_str, font_size, font_type, font_color)



def txt2mp3(content='程序员晚枫', file=None, mp3=r'./程序员晚枫.mp3', speak=True):
    """Convert text to speech.
    
    文本转语音。
    
    Args:
        content (str, optional): content to convert / 需要转换的内容。Default / 默认: '程序员晚枫'
        file (str, optional): specify file to read, highest priority / 指定读取的文件，优先级最高
        mp3 (str, optional): mp3 save location and name / 需要保存的mp3位置和名称。Fill None to not save / 填None不保存。Default / 默认: './程序员晚枫.mp3'
        speak (bool, optional): whether to read aloud / 是否阅读。Default / 默认: True
    
    Returns:
        None
    """
    return povideo.txt2mp3(content, file, mp3, speak)
