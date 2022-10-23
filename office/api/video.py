# from office.core.VideoType import MainVideo
# mainVideo = MainVideo()
import povideo


# 从视频里提取音频
def video2mp3(path, mp3_name=None, output_path=r'./'):
    povideo.video2mp3(path, mp3_name, output_path)


# 从音频里，提取文字
# 本地语音文件不能大于5MB
def audio2txt(audio_path, appid, secret_id, secret_key):
    povideo.audio2txt(audio_path, appid, secret_id, secret_key)
