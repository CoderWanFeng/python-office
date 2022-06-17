import moviepy.editor as mp


class MainVideo():

    # 从视频里提取音频
    def video2mp3(self, path, mp3_name):
        """
        :param path: 视频文件的路径
        :param mp3_name: mp3的名字，可以为空
        :return:
        """
        # specify the mp4 file here(mention the file path if it is in different directory)
        clip = mp.VideoFileClip(path)
        if mp3_name:
            clip.audio.write_audiofile(str(mp3_name) + '.mp3')
        else:
            # specify the name for mp3 extracted
            clip.audio.write_audiofile('Audio.mp3')
            # you will notice mp3 file will be created at the specified location.
