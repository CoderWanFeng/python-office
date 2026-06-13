# -*- coding: UTF-8 -*-
"""OCR功能测试模块。

该模块包含对python-office库中OCR相关功能的单元测试。

@学习网站      ：https://www.python-office.com
@读者群     ：https://www.python4office.cn/wechat-group/
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：wfdev7
@代码日期    ：2025/7/2 22:45 
@本段代码的视频说明     ：
"""

import os
import unittest

from loguru import logger

from office.api.ocr import VatInvoiceOCR2Excel


class TestPDF(unittest.TestCase):
    """OCR功能测试类。
    
    该类包含对OCR相关API的单元测试方法。
    """
    def setUp(self):
        self.id = os.getenv("SecretId", None)
        self.key = os.getenv("SecretKey", None)

    def test_VatInvoiceOCR2Excel(self):
        logger.info(self.id)
        logger.info(self.key)
        VatInvoiceOCR2Excel(input_path=r'..\test_files\ocr\img.png', output_path=r'./output/ocr',
                            id=self.id, key=self.key)
