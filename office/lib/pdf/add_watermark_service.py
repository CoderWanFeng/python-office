# -*- coding: utf-8 -*-
"""PDF 水印底层实现（遗留模块）。

说明：
* 本模块未被 ``office.api`` 的公开接口引用，对外的水印能力由
  ``office.api.pdf.add_text_watermark``（基于 popdf）提供，此处保留以兼容
  历史用法。
* reportlab / PyPDF2 / tqdm 均为可选依赖且未列入 install_requires，因此
  改为按需加载：导入本模块不再因缺依赖而直接失败。
"""

import os

# 系统中文字体的候选路径（按平台顺序尝试）
_FONT_CANDIDATES = (
    'C:/Windows/Fonts/simfang.ttf',                    # Windows
    '/System/Library/Fonts/Supplemental/Songti.ttc',   # macOS
    '/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc',    # Linux
)


def _load_deps():
    """按需加载 reportlab / PyPDF2 / tqdm，缺失时给出可操作的报错。"""
    try:
        from reportlab.pdfgen import canvas
        from reportlab.pdfbase.ttfonts import TTFont
        from reportlab.pdfbase.pdfmetrics import registerFont
        from PyPDF2 import PdfReader, PdfWriter
        from tqdm import tqdm
    except ImportError as exc:
        raise ModuleNotFoundError(
            "PDF 水印功能依赖 reportlab、PyPDF2 和 tqdm，请先安装："
            "pip install reportlab PyPDF2 tqdm"
        ) from exc
    return canvas, TTFont, registerFont, PdfReader, PdfWriter, tqdm


def _register_watermark_font(TTFont, registerFont) -> str:
    """注册水印字体，返回可用的字体名。

    优先使用系统中的中文字体；找不到时退回 reportlab 内置字体
    （可正常渲染，但不支持中文）。
    """
    for path in _FONT_CANDIDATES:
        if not os.path.exists(path):
            continue
        try:
            registerFont(TTFont('simfang', path))
            return 'simfang'
        except Exception:
            continue
    return 'Helvetica'


def create_watermark(content: str):
    """创建PDF水印模板。

    Args:
        content (str): 水印文字内容

    Returns:
        PdfReader: 水印PDF文件对象
    """
    canvas, TTFont, registerFont, PdfReader, _, _ = _load_deps()
    # 创建一个PDF文件来作为一个水印文件
    c = canvas.Canvas('watermark.popdf')
    font_name = _register_watermark_font(TTFont, registerFont)
    c.setFont(font_name, 20)
    c.saveState()
    c.translate(305, 505)
    c.rotate(45)
    c.drawCentredString(0, 0, content)
    c.restoreState()
    c.save()
    pdf_watermark = PdfReader('watermark.popdf')
    return pdf_watermark


def pdf_add_watermark(pdf_file_in: str, pdf_file_mark: str, pdf_file_out: str) -> bool:
    """给PDF文件添加水印。

    Args:
        pdf_file_in (str): 输入PDF文件路径
        pdf_file_mark (str): 水印PDF文件路径
        pdf_file_out (str): 输出PDF文件路径

    Returns:
        bool: 操作是否成功
    """
    _, _, _, PdfReader, PdfWriter, tqdm = _load_deps()
    # print(pdf_file_out)
    pdf_output = PdfWriter()
    input_stream = None
    mark_stream = None
    try:
        input_stream = open(pdf_file_in, 'rb')
        pdf_input = PdfReader(input_stream, strict=False)
        # 获取PDF文件的页数
        if pdf_input.is_encrypted:
            print("文件已被加密")
            PDF_Passwd = input("请输入PDF密码：")
            # 尝试用空密码解密
            try:
                pdf_input.decrypt(PDF_Passwd)
            except Exception:
                print(f"尝试用密码{PDF_Passwd}解密失败.")
                return False
        pageNum = len(pdf_input.pages)
        # 读入水印pdf文件
        # print(pdf_file_mark)
        mark_stream = open(pdf_file_mark, mode='rb')
        pdf_watermark = PdfReader(mark_stream, strict=False)
        # 检查水印PDF是否有效（至少包含一页）
        if len(pdf_watermark.pages) == 0:
            print(f"水印文件不包含任何页面：{pdf_file_mark}")
            return False
        # 给每一页打水印
        for pageNumber in tqdm(range(pageNum)):
            page = pdf_input.pages[pageNumber]
            page.merge_page(pdf_watermark.pages[0])
            page.compress_content_streams()  # 压缩内容
            pdf_output.add_page(page)
        with open(pdf_file_out, 'wb') as pdf_file_out_f:
            pdf_output.write(pdf_file_out_f)
        return True
    finally:
        # 无论成功失败，都确保输入流和水印流被关闭，避免批量处理时文件句柄泄漏
        if input_stream is not None:
            input_stream.close()
        if mark_stream is not None:
            mark_stream.close()
