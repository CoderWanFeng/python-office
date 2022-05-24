"""
功能：实现MP4与gif格式的互相转换
"""

from warnings import warn
warn("this folder will be removed, use offce.video.* instead", DeprecationWarning)


# 需要安装moviepy包
# pip install moviepy
from warnings import warn
from moviepy.editor import VideoFileClip


def mp4_to_gif(mp4_path, gif_path):

    warn("use office.image.mp4_to_gif instead" ,DeprecationWarning)
    """
    功能：mp4文件转gif文件
    参数：
        mp4_path: mp4文件所在路径
        gif_path: gif文件保存路径
    """
    clip = (VideoFileClip(mp4_path))
    clip.write_gif(gif_path)

def gif_to_mp4(gif_path, mp4_path):
    """
    gif文件转mp4文件
    参数：
        gif_path: gif文件所在路径
        mp4_path: mp4文件保存路径
    """
    clip = VideoFileClip(gif_path)
    clip.write_videofile(mp4_path)

if __name__ == '__main__':

    # mp4文件转gif
    mp4_to_gif('1.mp4', 'a.gif')

    # gif文件转mp4
    # gif_to_mp4('a.gif', 'a.mp4')

