# -*- coding:utf-8 -*-
import os

import poocr

def VatInvoiceOCR2Excel(input_path, output_path=r'./', output_excel='VatInvoiceOCR2Excel.xlsx', img_url=None,
                        id=None, key=None, file_name=False, trans=False):
    """
    使用光学字符识别（OCR）技术将增值税发票信息提取并导出到Excel文件中。

    Args:
        input_path: str, 发票图片文件的路径或包含多个发票图片的文件夹路径。
        output_path: str, 可选，输出Excel文件的文件夹路径，默认为当前目录。
        output_excel: str, 可选，输出Excel文件的名称，默认为'VatInvoiceOCR2Excel.xlsx'。
        img_url: str, 可选，如果提供了input_path，则此参数将被忽略。用于指定网络发票图片的URL。
        id: str, 可选，百度OCR API的识别ID，如果在configPath中已配置，则不需要提供。
        key: str, 可选，百度OCR API的密钥，如果在configPath中已配置，则不需要提供。
        file_name: bool, 可选，是否使用图片文件名作为Sheet名称，默认为False。
        trans: bool, 可选，是否将识别结果翻译成英文，默认为False。

    Returns:
        None，函数将结果直接写入到指定的Excel文件中。
    """
    poocr.ocr2excel.VatInvoiceOCR2Excel(input_path=input_path, output_path=output_path,
                                        output_excel=output_excel,
                                        img_url=img_url,
                                        configPath=None,
                                        id=id, key=key, file_name=file_name, trans=trans)

