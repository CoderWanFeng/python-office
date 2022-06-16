from office.core.VideoType import MainVideo

mainVideo = MainVideo()


# 从视频里提取音频
def video2mp3(path, mp3_name=None):
    mainVideo.video2mp3(path,mp3_name)