#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: video_time_statistics.py
# Author: 刘运超
# Mail: chaodreaming@gmail.com
# Created Time:  2022-5-23 14:58
# Description: 统计视频时长
#############################################
import os
import datetime
from moviepy.editor import VideoFileClip
from tqdm import tqdm
def video_time_statistics(path):
    filelist = []
    for a, b, c in os.walk(path):
        for name in c:
            fname = os.path.join(a, name)
            if fname.endswith(".mp4"):
                filelist.append(fname)
    ftime = 0.0
    for item in tqdm(filelist):
        clip = VideoFileClip(item)
        ftime += clip.duration
    print("%d seconds: " % ftime, str(datetime.timedelta(seconds=ftime)))


# if __name__ == "__main__":
#
#     path=r"D:\BaiduNetdiskDownload\07-阶段七 \第三章"
#     video_time_statistics(path)