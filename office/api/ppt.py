# -*- coding: UTF-8 -*-
"""PPT 处理功能模块。

本模块按 https://www.python-office.com/modules/ppt/api 官方文档定义，
共 3 个函数，对应子包 ``poppt``：

    1. ppt2pdf    - PPT 转 PDF
    2. ppt2img    - PPT 转图片（可合成一张长图）
    3. merge4ppt  - 合并多个 PPT

Author:
    程序员晚枫

Project:
    https://www.python-office.com
"""

from __future__ import annotations

from typing import Optional

import poppt


# =====================================================================
# 1. ppt2pdf - PPT 转 PDF
# =====================================================================

def ppt2pdf(path: str, output_path: str = "./") -> str:
    """Convert PowerPoint to PDF.

    将 PPT / PPTX 文档转换为 PDF。

    Documentation: https://www.python-office.com/modules/ppt/api#ppt2pdf

    Args:
        path: PPT / PPTX 文件路径
        output_path: PDF 输出目录。Default: ``'./'``

    Returns:
        str: 输出目录路径
    """
    poppt.ppt2pdf(path=path, output_path=output_path)
    print(f"[python-office] ppt2pdf  输出目录：{output_path}")
    return output_path


# =====================================================================
# 2. ppt2img - PPT 转图片
# =====================================================================

def ppt2img(
    input_path: str,
    output_path: str = "./",
    merge: bool = False,
) -> str:
    """Convert PowerPoint to images.

    将 PPT 转换为图片。
    - ``merge=False``（默认）：每页一张图，输出到 ``output_path`` 目录
    - ``merge=True``：所有页拼成一张长图，输出到 ``output_path`` 单文件

    同时支持：
    - 单个文件：传 ``input_path='xxx.pptx'``
    - 批量目录：传 ``input_path='./ppt_dir/'``，转换目录下所有 PPT

    Documentation: https://www.python-office.com/modules/ppt/api#ppt2img

    Args:
        input_path: PPT / PPTX 文件路径，或包含多个 PPT 的目录
        output_path: 图片输出目录（merge=False）或单张长图文件路径（merge=True）。Default: ``'./'``
        merge: True=合并为一张长图，False=每页一张图。Default: ``False``

    Returns:
        str: 实际输出目录 / 文件路径
    """
    poppt.ppt2img(input_path=input_path, output_path=output_path, merge=merge)
    print(f"[python-office] ppt2img  输出：{output_path}  merge={merge}")
    return output_path


# =====================================================================
# 3. merge4ppt - 合并多个 PPT
# =====================================================================

def merge4ppt(
    input_path: str,
    output_path: str = "./",
    output_name: str = "merge4ppt.pptx",
) -> str:
    """Merge multiple PowerPoint files into one.

    将多个 PPT / PPTX 合并为一个文件。

    Documentation: https://www.python-office.com/modules/ppt/api#merge4ppt

    Args:
        input_path: 包含多个 PPT / PPTX 的目录
        output_path: 合并后文件保存目录。Default: ``'./'``
        output_name: 合并后文件名（含 .pptx 后缀）。Default: ``'merge4ppt.pptx'``

    Returns:
        str: 合并后文件完整路径
    """
    poppt.merge4ppt(
        input_path=input_path, output_path=output_path, output_name=output_name,
    )
    out_dir = output_path.rstrip("/\\")
    full = f"{out_dir}/{output_name}"
    print(f"[python-office] merge4ppt  输出文件：{full}")
    return full


__all__ = [
    "ppt2pdf",
    "ppt2img",
    "merge4ppt",
]
