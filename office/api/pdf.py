# -*- coding: UTF-8 -*-
"""PDF 处理功能模块。

本模块按 https://www.python-office.com/modules/pdf/api 官方文档定义，
共 13 个函数，对应子包 ``popdf``：

    1.  pdf2docx                   - PDF 转 Word
    2.  pdf2imgs                   - PDF 转图片
    3.  txt2pdf                    - 文本转 PDF
    4.  split4pdf                  - 拆分 PDF
    5.  encrypt4pdf                - 加密 PDF
    6.  decrypt4pdf                - 解密 PDF
    7.  merge2pdf                  - 合并 PDF
    8.  add_text_watermark         - 文本水印
    9.  add_img_water              - 图片水印
    10. add_mark                   - 旧版水印（保留兼容）
    11. add_watermark_by_parameters- 参数化水印（推荐）
    12. del4pdf                    - 删除页面
    13. add_watermark              - 交互式水印（CLI 场景，GUI 中可忽略）

Author:
    程序员晚枫

Project:
    https://www.python-office.com
"""

from __future__ import annotations

import warnings
from ast import literal_eval
from pathlib import Path
from typing import List, Optional, Tuple

import popdf

from office.lib.decorator_utils import deprecated_params


# =====================================================================
# 1. PDF 转 Word
# =====================================================================

def _resolve_pdf2docx_output(input_file: str, output_file: str = None) -> str:
    """推导 PDF 转 Word 的最终输出文件路径。

    规则：
        1. ``output_file`` 为空 → ``<input 同目录>/<同名>.docx``；
        2. ``output_file`` 是已存在目录或以 / \\ 结尾 → 在该目录下按 input stem 拼接；
        3. ``output_file`` 是文件路径但后缀不是 .docx → 自动补 .docx；
        4. 其它情况 → 视为已指定的完整文件路径。
    """
    in_path = Path(input_file).resolve()
    if output_file is None or str(output_file).strip() == "":
        return str(in_path.with_suffix(".docx"))

    out_path = Path(output_file)
    if out_path.is_dir() or str(out_path).endswith(("/", "\\")):
        return str(out_path / f"{in_path.stem}.docx")
    if out_path.suffix.lower() != ".docx":
        return str(out_path.with_suffix(".docx"))
    return str(out_path)


def pdf2docx(input_file: str = None, output_file: str = None,
             input_path: str = None, output_path: str = None) -> str:
    """Convert PDF to Word document.

    将PDF转换为Word文档。

    支持两种调用风格：

    * **新风格（推荐）**: 直接传 ``input_file`` + ``output_file``；
      若 ``output_file`` 留空，自动取输入文件同目录、同 stem、扩展名 .docx。
    * **兼容风格**: ``input_path`` + ``output_path`` 一起给（1.0.1 行为）。

    实际输出文件路径会通过 stdout 打印，GUI 日志可捕获。

    Documentation: https://www.python4office.cn/python-office/popdf/1-pdf2docx/

    Args:
        input_file (str, optional): PDF 文件路径（新风格）
        output_file (str, optional): 输出 .docx 文件路径；留空时懒人模式自动派生
        input_path (str, optional): 输入目录（兼容风格）
        output_path (str, optional): 输出目录（兼容风格）

    Returns:
        str: 最终落盘的 .docx 文件绝对路径
    """
    if input_file is not None:
        resolved = _resolve_pdf2docx_output(input_file, output_file)
        print(f"[python-office] PDF → Word  输出文件：{resolved}")
        popdf.pdf2docx(input_file=str(input_file), output_file=resolved)
        return resolved

    if input_path is not None and output_path is not None:
        out_file = str(Path(output_path) / f"{Path(input_path).stem}.docx") \
            if not str(output_path).endswith(".docx") else output_path
        print(f"[python-office] PDF → Word  输出文件：{out_file}")
        popdf.pdf2docx(input_path=input_path, output_path=output_path)
        return out_file

    raise ValueError(
        "pdf2docx 需要传 (input_file) 或 (input_path + output_path) 之一。"
    )


# =====================================================================
# 2. PDF 转图片
# =====================================================================

@deprecated_params({"pdf_path": "input_file", "out_dir": "output_file"})
def pdf2imgs(input_file: str = None, output_file: str = None,
             merge: bool = False,
             pdf_path: str = None, out_dir: str = None) -> None:
    """Convert PDF to images.

    将PDF转换为图片。

    每页一张图，或通过 ``merge=True`` 合并为一张长图。

    Documentation: https://www.python4office.cn/python-office/popdf/2-pdf2imgs/

    Args:
        input_file (str): PDF 文件路径
        output_file (str): 输出图片路径（合并模式下为单张长图文件名，如 ``./long.png``；
            不合并时为输出目录）
        merge (bool): 是否合并为一张长图。Default: False
        pdf_path (str): [已弃用] 请使用 input_file
        out_dir (str): [已弃用] 请使用 output_file
    """
    popdf.pdf2imgs(input_file=input_file, output_file=output_file, merge=merge)


def _coerce_number_tuple(value, default: tuple[float, ...]) -> tuple[float, ...]:
    """把 GUI 文本框里的元组字符串转成底层库需要的数字 tuple。"""
    if value in (None, ""):
        return default
    if isinstance(value, tuple):
        return tuple(float(item) for item in value)
    if isinstance(value, list):
        return tuple(float(item) for item in value)
    if isinstance(value, str):
        try:
            parsed = literal_eval(value)
        except (SyntaxError, ValueError):
            return default
        if isinstance(parsed, (tuple, list)):
            return tuple(float(item) for item in parsed)
    return default


# =====================================================================
# 3. 文本转 PDF
# =====================================================================

def txt2pdf(input_file: str = "text.txt", output_file: str = "output.pdf") -> None:
    """Convert text file to PDF.

    将文本文件转换为PDF。

    Documentation: https://www.python4office.cn/python-office/popdf/3-txt2pdf/

    Args:
        input_file (str): 文本文件路径
        output_file (str): 输出 PDF 文件路径
    """
    popdf.txt2pdf(input_file=input_file, output_file=output_file)


# =====================================================================
# 4. 拆分 PDF
# =====================================================================

def split4pdf(input_file: str = None, output_file: str = "./output/split_pdf.pdf",
              from_page: int = 1, to_page: int = -1) -> None:
    """Split PDF file.

    拆分PDF文件。

    Documentation: https://www.python4office.cn/python-office/popdf/4-split4pdf/

    Args:
        input_file (str): PDF 文件路径
        output_file (str): 输出拆分后的 PDF 文件路径
        from_page (int): 起始页码（1-indexed，-1 表示首页）。Default: 1
        to_page (int): 结束页码（-1 表示末页）。Default: -1
    """
    popdf.split4pdf(input_file=input_file, output_file=output_file,
                    from_page=from_page, to_page=to_page)


# =====================================================================
# 5 / 6. 加密 / 解密 PDF
# =====================================================================

def encrypt4pdf(password: str, input_file: str = None, output_file: str = None,
                input_path: str = None, output_path: str = None) -> None:
    """Encrypt PDF file.

    加密PDF文件。

    Documentation: https://www.python4office.cn/python-office/popdf/5-encrypt4pdf/

    Args:
        password (str): 加密密码
        input_file (str): 输入 PDF 文件名（含路径）
        output_file (str): 输出加密 PDF 文件名（含路径）
        input_path (str): [已弃用] 旧版兼容，请用 input_file
        output_path (str): [已弃用] 旧版兼容，请用 output_file
    """
    if password is None or str(password) == "":
        raise ValueError("encrypt4pdf: password 不能为空")
    popdf.encrypt4pdf(password=password, input_file=input_file, output_file=output_file,
                      input_path=input_path, output_path=output_path)


def decrypt4pdf(password: str, input_file: str = None, output_file: str = None,
                input_path: str = None, output_path: str = None) -> None:
    """Decrypt PDF file.

    解密PDF文件。

    Documentation: https://www.python4office.cn/python-office/popdf/6-decrypt4pdf

    Args:
        password (str): 解密密码
        input_file (str): 输入加密 PDF 文件名（含路径）
        output_file (str): 输出解密后 PDF 文件名（含路径）
        input_path (str): [已弃用] 旧版兼容，请用 input_file
        output_path (str): [已弃用] 旧版兼容，请用 output_file
    """
    if password is None or str(password) == "":
        raise ValueError("decrypt4pdf: password 不能为空")
    popdf.decrypt4pdf(password=password, input_file=input_file, output_file=output_file,
                      input_path=input_path, output_path=output_path)


# =====================================================================
# 7. 合并 PDF
# =====================================================================

@deprecated_params({"one_by_one": "input_file_list", "output": "output_file"})
def merge2pdf(input_file_list: List[str] = None, output_file: str = None,
              one_by_one: List[str] = None, output: str = None) -> None:
    """Merge multiple PDF files.

    合并多个PDF文件。

    Documentation: https://www.python4office.cn/python-office/popdf/8-merge2pdf

    Args:
        input_file_list (list[str]): PDF 文件路径列表
        output_file (str): 合并后的 PDF 文件路径
        one_by_one (list[str]): [已弃用] 请使用 input_file_list
        output (str): [已弃用] 请使用 output_file
    """
    popdf.merge2pdf(input_file_list=input_file_list, output_file=output_file)


# =====================================================================
# 8. 文本水印
# =====================================================================

def add_text_watermark(input_file: str = None, text: str = "python-office",
                       output_file: str = None,
                       point: Tuple[float, float] = None,
                       fontname: str = "Helvetica",
                       fontsize: int = 48,
                       color: Tuple[float, float, float] = (0.45, 0.50, 0.55),
                       opacity: float = 0.16,
                       angle: int = -35) -> None:
    """Add text watermark to PDF document.

    在PDF文档中添加文本水印。

    Documentation: https://www.python4office.cn/python-office/popdf/7-add_watermark

    Args:
        input_file (str): PDF 文件路径
        text (str): 水印文本内容。Default: "python-office"
        output_file (str): 输出 PDF 文件路径；留空时自动用输入文件同目录 + "_watermark" 后缀
        point (tuple): 起始位置坐标 (x, y)，留空时自动铺满页面
        fontname (str): 字体名称。Default: "Helvetica"
        fontsize (int): 字体大小。Default: 48
        color (tuple): RGB 颜色三元组，每个分量 0~1。Default: 浅灰色
        opacity (float): 水印透明度，0~1。Default: 0.16
        angle (int): 水印倾斜角度。Default: -35
    """
    if output_file is None and input_file:
        in_path = Path(input_file)
        output_file = str(in_path.parent / f"{in_path.stem}_watermark.pdf")
    start_point = _coerce_number_tuple(point, ())
    color = _coerce_number_tuple(color, (0.45, 0.50, 0.55))
    opacity = max(0.01, min(float(opacity), 1.0))
    angle = int(angle)

    import pymupdf

    print(f"[python-office] 文本水印  输出文件：{output_file}")
    doc = pymupdf.open(input_file)
    for page in doc:
        rect = page.rect
        matrix = pymupdf.Matrix(1, 1).prerotate(angle)
        if len(start_point) == 2:
            positions = [pymupdf.Point(start_point[0], start_point[1])]
        else:
            x_step = max(fontsize * max(len(str(text)), 4) * 0.65, 220)
            y_step = max(fontsize * 3.0, 150)
            positions = [
                pymupdf.Point(x, y)
                for y in range(int(-rect.height), int(rect.height * 2), int(y_step))
                for x in range(int(-rect.width), int(rect.width * 2), int(x_step))
            ]
        for pos in positions:
            page.insert_text(
                pos,
                str(text),
                fontsize=fontsize,
                fontname=fontname,
                color=color,
                fill_opacity=opacity,
                overlay=True,
                morph=(pos, matrix),
            )
    Path(output_file).parent.mkdir(parents=True, exist_ok=True)
    doc.save(output_file)
    doc.close()


# =====================================================================
# 9. 图片水印（官方 API 真实存在）
# =====================================================================

def add_img_water(input_file: str, mark_file: str, output_file: str) -> None:
    """Add image watermark to PDF.

    在 PDF 上叠加图片水印。

    Documentation: https://www.python-office.com/modules/pdf/api#add_img_water

    Args:
        input_file (str): 输入 PDF 文件路径
        mark_file (str): 水印图片文件路径（建议 PNG / JPG）
        output_file (str): 输出带水印的 PDF 文件路径
    """
    if not input_file:
        raise ValueError("add_img_water: input_file 必填")
    if not mark_file:
        raise ValueError("add_img_water: mark_file 必填")
    if not output_file:
        # 懒人模式：输入文件 + "_watermarked" 后缀
        in_path = Path(input_file)
        output_file = str(in_path.parent / f"{in_path.stem}_watermarked.pdf")
    print(f"[python-office] 图片水印  输出文件：{output_file}")
    popdf.add_img_water(
        pdf_file_in=str(input_file),
        pdf_file_mark=str(mark_file),
        pdf_file_out=str(output_file),
    )


# =====================================================================
# 10 / 11. 旧版 + 参数化水印
# =====================================================================

@deprecated_params({"pdf_file": "input_file", "output_file_name": "output_file"})
def add_mark(input_file: str = None, mark_str: str = None,
             output_path: str = "./output/",
             output_file: str = None,
             pdf_file: str = None, output_file_name: str = None) -> None:
    """旧版水印接口，保留兼容。

    推荐使用 :func:`add_watermark_by_parameters`，参数更明确。

    Args:
        input_file (str): PDF 文件路径
        mark_str (str): 水印文本
        output_path (str): 输出目录
        output_file (str): 输出文件名
        pdf_file (str): [已弃用] 请使用 input_file
        output_file_name (str): [已弃用] 请使用 output_file
    """
    popdf.add_watermark_by_parameters(
        pdf_file=input_file, mark_str=mark_str,
        output_path=output_path, output_file_name=output_file,
    )


@deprecated_params({"pdf_file": "input_file", "output_file_name": "output_file"})
def add_watermark_by_parameters(input_file: str = None, mark_str: str = None,
                                output_path: str = "./output/",
                                output_file: str = None,
                                pdf_file: str = None,
                                output_file_name: str = None) -> None:
    """Add watermark to PDF with parameters（推荐使用）。

    给PDF添加水印（带参数）。

    Documentation: https://www.python-office.com/modules/pdf/api#add_watermark_by_parameters

    Args:
        input_file (str): PDF 文件路径
        mark_str (str): 水印文本
        output_path (str): 输出目录
        output_file (str): 输出文件名
        pdf_file (str): [已弃用] 请使用 input_file
        output_file_name (str): [已弃用] 请使用 output_file
    """
    popdf.add_watermark_by_parameters(
        pdf_file=input_file, mark_str=mark_str,
        output_path=output_path, output_file_name=output_file,
    )


# =====================================================================
# 12. 删除页面
# =====================================================================

def del4pdf(input_file: str = None, output_file: str = None,
            page_nums: List[int] = None) -> None:
    """Delete specific pages from PDF file.

    删除PDF文件中的指定页面。

    Documentation: https://www.python4office.cn/python-office/popdf/9-del4pdf

    Args:
        input_file (str): PDF 文件路径
        output_file (str): 输出 PDF 文件路径
        page_nums (list[int]): 要删除的页码列表（1-indexed）
    """
    popdf.del4pdf(page_nums=page_nums, input_file=input_file,
                  output_file=output_file)


# =====================================================================
# 13. 交互式水印
# =====================================================================

def add_watermark() -> None:
    """交互式水印入口（CLI 场景）。

    在命令行场景下调用 ``office.pdf.add_watermark()`` 会进入交互问答，
    由用户逐步输入参数后调用 :func:`add_text_watermark`。

    在 GUI 场景下请直接使用「PDF 加文字水印」面板，无需调用此函数。

    Documentation: https://www.python-office.com/modules/pdf/api#add_watermark
    """
    print("=" * 60)
    print("python-office 交互式水印")
    print("=" * 60)
    try:
        input_file = input("请输入 PDF 文件路径: ").strip()
        text = input("请输入水印文本 [python-office]: ").strip() or "python-office"
        output_file = input("请输入输出文件路径 [留空自动派生]: ").strip() or None
    except EOFError:
        print("\n[python-office] 检测到非交互式环境，请在 GUI 中使用「PDF 加文字水印」。")
        return
    print()
    add_text_watermark(
        input_file=input_file,
        text=text,
        output_file=output_file,
    )


# =====================================================================
# __all__
# =====================================================================

__all__ = [
    "pdf2docx",
    "pdf2imgs",
    "txt2pdf",
    "split4pdf",
    "encrypt4pdf",
    "decrypt4pdf",
    "merge2pdf",
    "add_text_watermark",
    "add_img_water",
    "add_mark",
    "add_watermark_by_parameters",
    "del4pdf",
    "add_watermark",
]
