# from office.core.VideoType import MainVideo
# mainVideo = MainVideo()
import povideo


# 从视频里提取音频
from office.lib.decorator_utils.instruction_url import instruction

@instruction
def video2mp3(path, mp3_name=None, output_path=r'./'):
    povideo.video2mp3(path, mp3_name, output_path)


# 从音频里，提取文字
# 本地语音文件不能大于5MB
@instruction
def audio2txt(audio_path, appid, secret_id, secret_key):
    povideo.audio2txt(audio_path, appid, secret_id, secret_key)

@instruction
def mark2video(video_path, output_path=r'./', output_name=r'mark2video.mp4', mark_str: str = "www.python-office.com",
               font_size=28,
               font_type='Arial', font_color='white'):
    """
    给视频添加水印
    :param video_path: 必填，视频地址
    :param output_path: 输出地址
    :param output_name: 输出名称，记得带‘.mp4’
    :param mark_str: 水印内容，只支持英文
    :param font_size: 水印字体大小
    :param font_color: 水印颜色
    :param font_type: 水印字体类型
    :return:
    """
    povideo.mark2video(video_path, output_path, output_name, mark_str, font_size, font_type, font_color)