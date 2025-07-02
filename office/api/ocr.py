# -*- coding:utf-8 -*-

import poocr


def VatInvoiceOCR2Excel(input_path, output_path=r'./', output_excel='VatInvoiceOCR2Excel.xlsx', img_url=None,
                        id=None, key=None, file_name=False, trans=False):
    """
    发票识别
    Args:
        input_path:
        output_path:
        output_excel:
        img_url:
        id:
        key:
        file_name:
        trans:

    Returns:

    """
    poocr.ocr2excel.VatInvoiceOCR2Excel(input_path=input_path, output_path=output_path,
                                        output_excel=output_excel,
                                        img_url=img_url,
                                        configPath=None,
                                        id=id, key=key, file_name=file_name, trans=trans)
