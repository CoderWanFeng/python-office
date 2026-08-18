# -*- coding: UTF-8 -*-
"""视频处理功能模块。

本模块按 https://www.python-office.com/modules/video/api 官方文档定义，
共 4 个函数，对应子包 ``povideo``：

    1. video2mp3   - 视频提取音频
    2. audio2txt   - 音频转文字（调用腾讯云语音识别）
    3. mark2video  - 视频加文字水印
    4. txt2mp3     - 文本转语音

Author:
    程序员晚枫

Project:
    https://www.python-office.com
"""

from __future__ import annotations

from typing import Optional

import povideo


__all__ = ["video2mp3", "audio2txt", "mark2video", "txt2mp3"]


# =====================================================================
# 1. video2mp3 - 视频提取音频
# =====================================================================

def video2mp3(
    path: str,
    mp3_name: Optional[str] = None,
    output_path: str = "./",
) -> str:
    """Extract audio from video and save as MP3.

    将视频文件提取为 MP3 音频。

    Documentation: https://www.python-office.com/modules/video/api#video2mp3

    Args:
        path: 输入视频文件路径
        mp3_name: 输出 MP3 文件名（不含后缀），留空则用原视频文件名。Default: ``None``
        output_path: 输出目录。Default: ``'./'``

    Returns:
        str: 输出 MP3 文件路径
    """
    povideo.video2mp3(path=path, mp3_name=mp3_name, output_path=output_path)
    from pathlib import Path
    name = mp3_name or Path(path).stem
    out = str(Path(output_path) / f"{name}.mp3")
    print(f"[python-office] video2mp3  输出：{out}")
    return out


# =====================================================================
# 2. audio2txt - 音频转文字
# =====================================================================

def audio2txt(audio_path: str, appid: str, secret_id: str, secret_key: str) -> None:
    """Convert audio to text using Tencent Cloud ASR.

    调用腾讯云语音识别 API，把音频文件转为文字。

    注意：本地音频文件不能大于 5MB。

    Documentation: https://www.python-office.com/modules/video/api#audio2txt

    Args:
        audio_path: 输入音频文件路径
        appid: 腾讯云语音识别应用的 appid
        secret_id: 腾讯云 API SecretId
        secret_key: 腾讯云 API SecretKey
    """
    povideo.audio2txt(
        audio_path=audio_path,
        appid=appid,
        secret_id=secret_id,
        secret_key=secret_key,
    )
    print(f"[python-office] audio2txt  源：{audio_path}")


# =====================================================================
# 3. mark2video - 视频加文字水印
# =====================================================================

def mark2video(
    video_path: str,
    output_path: str = "./",
    output_name: str = "mark2video.mp4",
    mark_str: str = "www.python-office.com",
    font_size: int = 28,
    font_type: str = "Arial",
    font_color: str = "white",
) -> str:
    """Add text watermark to video.

    给视频添加文字水印（默认滚动）。

    Documentation: https://www.python-office.com/modules/video/api#mark2video

    Args:
        video_path: 输入视频文件路径
        output_path: 输出目录。Default: ``'./'``
        output_name: 输出文件名（**记得带 .mp4 后缀**）。Default: ``'mark2video.mp4'``
        mark_str: 水印文字内容。Default: ``'www.python-office.com'``
        font_size: 水印字号。Default: ``28``
        font_type: 字体名称或字体文件路径。Default: ``'Arial'``
        font_color: 字体颜色。Default: ``'white'``

    Returns:
        str: 完整输出文件路径
    """
    povideo.mark2video(
        video_path=video_path,
        output_path=output_path,
        output_name=output_name,
        mark_str=mark_str,
        font_size=font_size,
        font_type=font_type,
        font_color=font_color,
    )
    from pathlib import Path
    out = str(Path(output_path) / output_name)
    print(f"[python-office] mark2video  输出：{out}  水印：{mark_str!r}")
    return out


# =====================================================================
# 4. txt2mp3 - 文本转语音
# =====================================================================

def txt2mp3(
    content: str = "程序员晚枫",
    file: Optional[str] = None,
    mp3: str = "./程序员晚枫.mp3",
    speak: bool = True,
) -> str:
    """Convert text to speech and save as MP3.

    调用本地 TTS 引擎把文本转为 MP3 语音。

    Documentation: https://www.python-office.com/modules/video/api#txt2mp3

    Args:
        content: 要朗读的文本内容。Default: ``'程序员晚枫'``
        file: 可选：从指定文件读取文本（优先级最高）。Default: ``None``
        mp3: 输出 MP3 文件路径。Default: ``'./程序员晚枫.mp3'``
        speak: True=边合成边朗读，False=只生成文件。Default: ``True``

    Returns:
        str: 输出 MP3 文件路径
    """
    result = povideo.txt2mp3(content=content, file=file, mp3=mp3, speak=speak)
    print(f"[python-office] txt2mp3  输出：{mp3}  speak={speak}")
    return result if isinstance(result, str) else mp3
