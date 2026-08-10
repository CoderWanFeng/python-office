# -*- coding: utf-8 -*-
"""Video and Audio editing services.

音视频剪辑服务模块（截取、画面裁剪、音视频拼接、合成/替换音频）。
"""

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
        start_time (float|str, optional): start time in seconds or "HH:MM:SS" / 开始时间。Default / 默认: 0
        end_time (float|str, optional): end time in seconds or "HH:MM:SS" / 结束时间。Default / 默认: None
        output_path (str, optional): output directory / 输出目录。Default / 默认: './'
        output_name (str, optional): output filename / 输出文件名。Default / 默认: None
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
        end_time (float|str, optional): end time in seconds or "HH:MM:SS" / 结束时间。Default / 默认: None
        output_path (str, optional): output directory / 输出目录。Default / 默认: './'
        output_name (str, optional): output filename / 输出文件名。Default / 默认: None
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
        output_name (str, optional): output filename / 输出文件名。Default / 默认: None
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
        output_name (str, optional): output filename / 输出文件名。Default / 默认: None
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
