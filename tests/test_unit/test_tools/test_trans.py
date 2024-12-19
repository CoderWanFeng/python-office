# -*- coding: UTF-8 -*-
'''
@学习网站      ：https://www.python-office.com
@读者群     ：http://www.python4office.cn/wechat-group/
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：CoderWanFeng
@代码日期    ：2024/6/15 13:36 
@本段代码的视频说明     ：
'''
# test_tools1.py
import unittest

from office.api.tools import transtools


class TestTranstools(unittest.TestCase):

    def test_translation_to_english(self):
        # 测试从中文翻译到英文
        translated = transtools(to_lang='en', content='你好')
        self.assertIn('hello', translated.lower())  # 假设翻译包含"hello"

    def test_translation_to_chinese(self):
        # 测试从英文翻译到中文
        translated = transtools(to_lang='zh', content='hello')
        self.assertIn('你好', translated)  # 假设翻译包含"你好"

    def test_translation_with_default_language(self):
        # 测试默认的源语言（中文）是否生效
        translated = transtools(to_lang='en', content='你好')
        self.assertIn('hello', translated.lower())  # 假设翻译包含"hello"

    def test_translation_with_specific_language(self):
        # 测试指定源语言是否生效
        translated = transtools(to_lang='en', content='Bonjour', from_lang='fr')
        self.assertIn('hello', translated.lower())  # 假设翻译包含"hello"

    def test_empty_content(self):
        # 测试空内容是否返回空字符串
        translated = transtools(to_lang='en', content='')
        self.assertEqual(translated, '')

    def test_none_content(self):
        # 测试None内容是否引发异常
        with self.assertRaises(TypeError):
            transtools(to_lang='en', content=None)

# 这将使得测试可以通过命令行执行
if __name__ == '__main__':
    unittest.main()
