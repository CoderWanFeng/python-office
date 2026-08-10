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
    povideo.video2mp3(path=path, mp3_name=mp3_name, output_path=output_path)

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
    povideo.audio2txt(audio_path=audio_path, appid=appid, secret_id=secret_id, secret_key=secret_key)



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
    povideo.mark2video(video_path=video_path, output_path=output_path, output_name=output_name, mark_str=mark_str, font_size=font_size, font_type=font_type, font_color=font_color)



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
    return povideo.txt2mp3(content=content, file=file, mp3=mp3, speak=speak)


import os
from moviepy import VideoFileClip, AudioFileClip, concatenate_videoclips, concatenate_audioclips


def _parse_time(t):
    if t is None:
        return None
    if isinstance(t, (int, float)):
        return float(t)
    if isinstance(t, str):
        t = t.strip()
        parts = t.split(':')
        if len(parts) == 1:
            return float(parts[0])
        elif len(parts) == 2:
            return float(parts[0]) * 60 + float(parts[1])
        elif len(parts) == 3:
            return float(parts[0]) * 3600 + float(parts[1]) * 60 + float(parts[2])
    return float(t)


def cut_video(video_path, start_time=0, end_time=None, output_path=r'./', output_name=None):
    """Cut / trim a video file to specified time range.
    
    剪辑/截取视频指定时间段。
    
    Args:
        video_path (str): video file path / 视频文件路径
        start_time (float|str, optional): start time in seconds or "HH:MM:SS" / 开始时间（秒数或格式如 '00:01:10'）。Default / 默认: 0
        end_time (float|str, optional): end time in seconds or "HH:MM:SS" / 结束时间（秒数或格式如 '00:02:30'）。Default / 默认: None (end of video)
        output_path (str, optional): output directory / 输出目录。Default / 默认: './'
        output_name (str, optional): output filename / 输出文件名。Default / 默认: None (auto-generated)
    
    Returns:
        None
    """
    os.makedirs(output_path, exist_ok=True)
    if not output_name:
        base_name = os.path.basename(video_path)
        name, ext = os.path.splitext(base_name)
        output_name = f"{name}_cut{ext if ext else '.mp4'}"
    out_file = os.path.join(output_path, output_name)

    st = _parse_time(start_time)
    et = _parse_time(end_time)

    clip = VideoFileClip(video_path)
    try:
        if hasattr(clip, 'subclipped'):
            sub = clip.subclipped(st, et)
        else:
            sub = clip.subclip(st, et)
        sub.write_videofile(out_file)
    finally:
        clip.close()


def cut_audio(audio_path, start_time=0, end_time=None, output_path=r'./', output_name=None):
    """Cut / trim an audio file to specified time range.
    
    剪辑/截取音频指定时间段。
    
    Args:
        audio_path (str): audio file path / 音频文件路径
        start_time (float|str, optional): start time in seconds or "HH:MM:SS" / 开始时间。Default / 默认: 0
        end_time (float|str, optional): end time in seconds or "HH:MM:SS" / 结束时间。Default / 默认: None (end of audio)
        output_path (str, optional): output directory / 输出目录。Default / 默认: './'
        output_name (str, optional): output filename / 输出文件名。Default / 默认: None (auto-generated)
    
    Returns:
        None
    """
    os.makedirs(output_path, exist_ok=True)
    if not output_name:
        base_name = os.path.basename(audio_path)
        name, ext = os.path.splitext(base_name)
        output_name = f"{name}_cut{ext if ext else '.mp3'}"
    out_file = os.path.join(output_path, output_name)

    st = _parse_time(start_time)
    et = _parse_time(end_time)

    clip = AudioFileClip(audio_path)
    try:
        if hasattr(clip, 'subclipped'):
            sub = clip.subclipped(st, et)
        else:
            sub = clip.subclip(st, et)
        sub.write_audiofile(out_file)
    finally:
        clip.close()


def crop_video(video_path, x1=0, y1=0, x2=None, y2=None, width=None, height=None, output_path=r'./', output_name=None):
    """Crop video screen region.
    
    裁剪视频画面坐标和尺寸。
    
    Args:
        video_path (str): video file path / 视频文件路径
        x1 (int, optional): left x coordinate / 左上角 x 坐标。Default / 默认: 0
        y1 (int, optional): top y coordinate / 左上角 y 坐标。Default / 默认: 0
        x2 (int, optional): right x coordinate / 右下角 x 坐标。Default / 默认: None
        y2 (int, optional): bottom y coordinate / 右下角 y 坐标。Default / 默认: None
        width (int, optional): crop width / 裁剪宽度。Default / 默认: None
        height (int, optional): crop height / 裁剪高度。Default / 默认: None
        output_path (str, optional): output directory / 输出目录。Default / 默认: './'
        output_name (str, optional): output filename / 输出文件名。Default / 默认: None (auto-generated)
    
    Returns:
        None
    """
    os.makedirs(output_path, exist_ok=True)
    if not output_name:
        base_name = os.path.basename(video_path)
        name, ext = os.path.splitext(base_name)
        output_name = f"{name}_cropped{ext if ext else '.mp4'}"
    out_file = os.path.join(output_path, output_name)

    clip = VideoFileClip(video_path)
    try:
        if hasattr(clip, 'cropped'):
            cropped = clip.cropped(x1=x1, y1=y1, x2=x2, y2=y2, width=width, height=height)
        elif hasattr(clip, 'crop'):
            cropped = clip.crop(x1=x1, y1=y1, x2=x2, y2=y2, width=width, height=height)
        else:
            import moviepy.video.fx.all as vfx
            cropped = vfx.crop(clip, x1=x1, y1=y1, x2=x2, y2=y2, width=width, height=height)
        cropped.write_videofile(out_file)
    finally:
        clip.close()


def concat_videos(video_list, output_path=r'./', output_name=r'concat_video.mp4'):
    """Concatenate multiple video files in sequence.
    
    多个视频顺序拼接合并为一个视频文件。
    
    Args:
        video_list (list[str]): list of video file paths / 视频文件路径列表
        output_path (str, optional): output directory / 输出目录。Default / 默认: './'
        output_name (str, optional): output filename / 输出文件名。Default / 默认: 'concat_video.mp4'
    
    Returns:
        None
    """
    os.makedirs(output_path, exist_ok=True)
    out_file = os.path.join(output_path, output_name)

    clips = [VideoFileClip(v) for v in video_list]
    try:
        final_clip = concatenate_videoclips(clips)
        final_clip.write_videofile(out_file)
    finally:
        for c in clips:
            c.close()


def concat_audios(audio_list, output_path=r'./', output_name=r'concat_audio.mp3'):
    """Concatenate multiple audio files in sequence.
    
    多个音频顺序拼接合并为一个音频文件。
    
    Args:
        audio_list (list[str]): list of audio file paths / 音频文件路径列表
        output_path (str, optional): output directory / 输出目录。Default / 默认: './'
        output_name (str, optional): output filename / 输出文件名。Default / 默认: 'concat_audio.mp3'
    
    Returns:
        None
    """
    os.makedirs(output_path, exist_ok=True)
    out_file = os.path.join(output_path, output_name)

    clips = [AudioFileClip(a) for a in audio_list]
    try:
        final_clip = concatenate_audioclips(clips)
        final_clip.write_audiofile(out_file)
    finally:
        for c in clips:
            c.close()


def add_audio_to_video(video_path, audio_path, output_path=r'./', output_name=None):
    """Add or replace audio track in a video file.
    
    将音频合成/替换到视频文件中。
    
    Args:
        video_path (str): video file path / 视频文件路径
        audio_path (str): audio file path / 音频文件路径
        output_path (str, optional): output directory / 输出目录。Default / 默认: './'
        output_name (str, optional): output filename / 输出文件名。Default / 默认: None (auto-generated)
    
    Returns:
        None
    """
    os.makedirs(output_path, exist_ok=True)
    if not output_name:
        base_name = os.path.basename(video_path)
        name, ext = os.path.splitext(base_name)
        output_name = f"{name}_with_audio{ext if ext else '.mp4'}"
    out_file = os.path.join(output_path, output_name)

    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)
    try:
        if hasattr(video_clip, 'with_audio'):
            final_clip = video_clip.with_audio(audio_clip)
        else:
            final_clip = video_clip.set_audio(audio_clip)
        final_clip.write_videofile(out_file)
    finally:
        video_clip.close()
        audio_clip.close()

