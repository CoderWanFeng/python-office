import unittest
from tests.test_utils.comm_utils import *
from office.api.video import *


class TestVideo(unittest.TestCase):
    def test_txt2mp3(self):
        txt2mp3()
        self.assertTrue(file_exist('./程序员晚枫.mp3'))

    def test_video2mp3(self):
        video2mp3(path=r'D:\software\obs\vedio\1-引入.mp4', mp3_name=r'1-引入')
