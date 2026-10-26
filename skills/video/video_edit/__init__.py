# -*- coding: UTF-8 -*-
"""video_edit Skill - 音视频剪辑集合（截取、画面裁剪、音视频拼接、合成/替换音频）"""
from office.api.video import (
    cut_video,
    cut_audio,
    crop_video,
    concat_videos,
    concat_audios,
    add_audio_to_video,
)

__all__ = [
    'cut_video',
    'cut_audio',
    'crop_video',
    'concat_videos',
    'concat_audios',
    'add_audio_to_video',
]
