# -*- coding:utf-8 -*-
"""Optical Character Recognition (OCR) functionality module.

光学字符识别（OCR）功能模块。

This module provides OCR capabilities for extracting text from images,
especially for VAT invoice recognition.

该模块提供了OCR功能，用于从图像中提取文本，尤其是增值税发票识别。

Author:
    程序员晚枫

Project:
    https://www.python-office.com
"""

import os

import poocr

def VatInvoiceOCR2Excel(input_path, output_path=r'./', output_excel='VatInvoiceOCR2Excel.xlsx', img_url=None,
                        id=None, key=None, file_name=False, trans=False):
    """Extract VAT invoice information using OCR technology and export to Excel file.
    
    使用光学字符识别（OCR）技术将增值税发票信息提取并导出到Excel文件中。
    
    Args:
        input_path (str): invoice image file path or folder path containing multiple invoice images / 发票图片文件的路径或包含多个发票图片的文件夹路径
        output_path (str, optional): output Excel file folder path / 输出Excel文件的文件夹路径。Default / 默认: current directory / 当前目录
        output_excel (str, optional): output Excel filename / 输出Excel文件的名称。Default / 默认: 'VatInvoiceOCR2Excel.xlsx'
        img_url (str, optional): URL of online invoice image, ignored if input_path is provided / 网络发票图片的URL。如果提供了input_path，则此参数将被忽略
        id (str, optional): Baidu OCR API recognition ID / 百度OCR API的识别ID。Not needed if configured in configPath / 如果在configPath中已配置，则不需要提供
        key (str, optional): Baidu OCR API key / 百度OCR API的密钥。Not needed if configured in configPath / 如果在configPath中已配置，则不需要提供
        file_name (bool, optional): whether to use image filename as Sheet name / 是否使用图片文件名作为Sheet名称。Default / 默认: False
        trans (bool, optional): whether to translate recognition result to English / 是否将识别结果翻译成英文。Default / 默认: False
    
    Returns:
        None: function writes result directly to specified Excel file / 函数将结果直接写入到指定的Excel文件中
    """
    poocr.ocr2excel.VatInvoiceOCR2Excel(input_path=input_path, output_path=output_path,
                                        output_excel=output_excel,
                                        img_url=img_url,
                                        configPath=None,
                                        id=id, key=key, file_name=file_name, trans=trans)

