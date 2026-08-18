# -*- coding: UTF-8 -*-
"""OCR 光学字符识别功能模块。

本模块按 https://www.python-office.com/modules/ocr/api 官方文档定义，
共 1 个函数，对应子包 ``poocr``：

    1. VatInvoiceOCR2Excel - 增值税发票识别 → Excel

调用百度智能云 OCR API，需在 [百度智能云](https://ai.baidu.com/) 注册并
创建「文字识别 OCR」应用获取 API Key / Secret Key。

Author:
    程序员晚枫

Project:
    https://www.python-office.com
"""

from __future__ import annotations

from typing import Optional

from poocr.api.ocr2excel import VatInvoiceOCR2Excel as _VatInvoiceOCR2Excel_impl


__all__ = ["VatInvoiceOCR2Excel"]


# =====================================================================
# 1. VatInvoiceOCR2Excel - 增值税发票识别 → Excel
# =====================================================================

def VatInvoiceOCR2Excel(
    input_path: str,
    output_path: str = "./",
    output_excel: str = "VatInvoiceOCR2Excel.xlsx",
    img_url: Optional[str] = None,
    id: Optional[str] = None,
    key: Optional[str] = None,
    file_name: bool = False,
    trans: bool = False,
) -> str:
    """Recognize VAT invoice and export to Excel.

    使用 OCR 技术识别增值税发票（图片 / PDF / 在线 URL），提取关键字段
    并导出为 Excel。

    Excel 中自动包含：
        - 发票代码、发票号码、开票日期
        - 销售方 / 购买方信息（名称、纳税人识别号）
        - 金额、税额、不含税金额、税率

    Documentation: https://www.python-office.com/modules/ocr/api#VatInvoiceOCR2Excel

    Args:
        input_path: 发票图片 / PDF 的路径，或包含多张发票的目录
        output_path: 输出 Excel 的保存目录。Default: ``'./'``
        output_excel: 输出 Excel 文件名。Default: ``'VatInvoiceOCR2Excel.xlsx'``
        img_url: 可选：在线图片 URL（与 ``input_path`` 二选一）。
        id: 百度智能云 OCR API 的 Access Key ID。
            在百度智能云控制台 → 文字识别 OCR 应用创建后获取。
        key: 百度智能云 OCR API 的 Secret Key。
        file_name: True=用图片文件名作为 Sheet 名。Default: ``False``
        trans: True=同时把识别结果翻译为英文。Default: ``False``

    Returns:
        str: 生成的 Excel 文件完整路径
    """
    _VatInvoiceOCR2Excel_impl(
        input_path=input_path,
        output_path=output_path,
        output_excel=output_excel,
        img_url=img_url,
        configPath=None,
        id=id,
        key=key,
        file_name=file_name,
        trans=trans,
    )
    from pathlib import Path
    out = str(Path(output_path) / output_excel)
    print(f"[python-office] VatInvoiceOCR2Excel  输出：{out}  trans={trans}")
    return out
