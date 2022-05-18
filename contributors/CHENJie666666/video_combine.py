"""
功能：实现视频拼接功能
"""
# 需要安装moviepy包
# pip install moviepy

from moviepy.editor import VideoFileClip, concatenate_videoclips

def video_combine(video_list, save_path):
    """
    视频拼接
    """
    clips = []
    
    # 导入第一个视频
    clip1 = VideoFileClip(video_list[0])
    clips.append(clip1)
    
    # 获取视频帧宽高、帧率信息
    clip_size = clip1.size
    fps = clip1.fps

    # 导入其他需要合并的视频
    try:
        for video in video_list[1:]:
            _clip = VideoFileClip(video).resize(clip_size)
            clips.append(_clip)
    except:
        print('The number of video was less than two, no need to combine')
        return None
    
    # 合并视频并导出
    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile(save_path, fps=fps)
    print(f'The combined video has been saved as {save_path}')


if __name__ == '__main__':

    video_combine(['1.mp4', '2.mp4'], 'combine.mp4')

