import unittest
from tests.test_utils.comm_utils import *
from office.api.video import *


class TestVideo(unittest.TestCase):
    def test_txt2mp3(self):
        txt2mp3()
        self.assertTrue(file_exist('./程序员晚枫.mp3'))
