# from office.core.VideoType import MainVideo
# mainVideo = MainVideo()
import povideo

# 从视频里提取音频
def video2mp3(path, mp3_name=None):
    povideo.video2mp3(path,mp3_name)