# -*- coding: UTF-8 -*-
"""Word 处理功能模块。

本模块按 https://www.python-office.com/modules/word/api 官方文档定义，
共 5 个函数，对应子包 ``poword``：

    1. docx2pdf    - Word 转 PDF（支持单个文件或整个文件夹批量）
    2. merge4docx  - 合并多个 Word
    3. doc2docx    - 旧版 .doc 转为 .docx
    4. docx2doc    - .docx 转回旧版 .doc
    5. docx4imgs   - 从 Word 提取图片

所有函数依赖 Microsoft Word / WPS / LibreOffice，**仅 Windows / macOS / Linux 桌面环境**可用。
CI / 无头服务器调用会失败。

Author:
    程序员晚枫

Project:
    https://www.python-office.com
"""

from __future__ import annotations

import os
from typing import Optional

import poword


# =====================================================================
# 1. docx2pdf - Word 转 PDF
# =====================================================================

def docx2pdf(path: str, output_path: Optional[str] = None) -> str:
    """Convert Word to PDF.

    将 Word 文档转换为 PDF。**支持单个文件或整个文件夹批量转换**。

    - 输入 ``path`` 是文件 → 转换该文件
    - 输入 ``path`` 是目录 → 批量转换目录下所有 .docx / .doc

    平台要求：依赖 Microsoft Word / WPS / LibreOffice。
    - Windows：装 Office 或 WPS
    - macOS：``brew install --cask libreoffice``
    - Linux：``sudo apt install libreoffice``

    Documentation: https://www.python-office.com/modules/word/api#docx2pdf

    Args:
        path: Word 文件路径，或包含多个 Word 文件的目录路径
        output_path: 转换后的 PDF 输出目录；不存在会自动创建。
            留空则输出到 ``path`` 所在目录。

    Returns:
        str: 实际输出目录路径
    """
    if output_path is None:
        output_path = path
    poword.docx2pdf(path=path, output_path=output_path)
    print(f"[python-office] docx2pdf  输出目录：{output_path}")
    return output_path


# =====================================================================
# 2. merge4docx - 合并多个 Word
# =====================================================================

def merge4docx(
    input_path: str,
    output_path: str,
    new_word_name: str = "merge4docx",
) -> str:
    """Merge multiple Word files into one.

    合并多个 .docx 文件为一个文件。

    Documentation: https://www.python-office.com/modules/word/api#merge4docx

    Args:
        input_path: 包含多个 .docx 的目录路径
        output_path: 合并后文件保存目录
        new_word_name: 合并后新文件的名称（不含 .docx 后缀）。Default: ``'merge4docx'``

    Returns:
        str: 合并后新文件的完整路径
    """
    poword.merge4docx(
        input_path=input_path,
        output_path=output_path,
        new_word_name=new_word_name,
    )
    out_dir = output_path.rstrip("/\\")
    full = f"{out_dir}/{new_word_name}.docx"
    print(f"[python-office] merge4docx  输出文件：{full}")
    return full


# =====================================================================
# 3. doc2docx - .doc 转为 .docx
# =====================================================================

def doc2docx(
    input_path: str,
    output_path: str = "./",
    output_name: Optional[str] = None,
) -> str:
    """Convert legacy .doc to .docx.

    将旧版 .doc 文档转换为新版 .docx。

    Documentation: https://www.python-office.com/modules/word/api#doc2docx

    Args:
        input_path: 要转换的 .doc 文件路径
        output_path: 输出的 .docx 保存目录。Default: ``'./'``
        output_name: 输出的 .docx 文件名（不含后缀），留空则与原文件同名。Default: ``None``

    Returns:
        str: 转换后的 .docx 完整路径
    """
    poword.doc2docx(
        input_path=input_path, output_path=output_path, output_name=output_name,
    )
    base = output_name or os.path.basename(input_path).rsplit(".", 1)[0]
    out_dir = output_path.rstrip("/\\")
    full = f"{out_dir}/{base}.docx"
    print(f"[python-office] doc2docx  输出文件：{full}")
    return full


# =====================================================================
# 4. docx2doc - .docx 转回 .doc
# =====================================================================

def docx2doc(
    input_path: str,
    output_path: str = "./",
    output_name: Optional[str] = None,
) -> str:
    """Convert .docx back to legacy .doc.

    将 .docx 文档转回旧版 .doc。

    Documentation: https://www.python-office.com/modules/word/api#docx2doc

    Args:
        input_path: 要转换的 .docx 文件路径
        output_path: 输出的 .doc 保存目录。Default: ``'./'``
        output_name: 输出的 .doc 文件名（不含后缀），留空则与原文件同名。Default: ``None``

    Returns:
        str: 转换后的 .doc 完整路径
    """
    poword.docx2doc(
        input_path=input_path, output_path=output_path, output_name=output_name,
    )
    base = output_name or os.path.basename(input_path).rsplit(".", 1)[0]
    out_dir = output_path.rstrip("/\\")
    full = f"{out_dir}/{base}.doc"
    print(f"[python-office] docx2doc  输出文件：{full}")
    return full


# =====================================================================
# 5. docx4imgs - 从 Word 提取图片
# =====================================================================

def docx4imgs(word_path: str, img_path: str) -> str:
    """Extract images from a Word document.

    从 Word 文档中提取所有图片到指定目录。
    会在 ``img_path`` 下自动按 Word 名称生成一个子目录。

    Documentation: https://www.python-office.com/modules/word/api#docx4imgs

    Args:
        word_path: .docx 文件路径
        img_path: 图片输出根目录

    Returns:
        str: 实际图片输出目录（``img_path/<word 文件名>``）
    """
    poword.docx4imgs(word_path=word_path, img_path=img_path)
    from pathlib import Path
    out = str(Path(img_path) / Path(word_path).stem)
    print(f"[python-office] docx4imgs  输出目录：{out}")
    return out


__all__ = [
    "docx2pdf",
    "merge4docx",
    "doc2docx",
    "docx2doc",
    "docx4imgs",
]
