# -*- coding: UTF-8 -*-
"""Markdown 处理功能模块。

本模块按 https://www.python-office.com/modules/markdown/api 官方文档定义，
共 1 个函数，对应子包 ``pomarkdown``：

    1. excel2markdown - Excel 转 Markdown 表格

Author:
    程序员晚枫

Project:
    https://www.python-office.com
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Optional

from openpyxl import load_workbook


__all__ = ["excel2markdown"]


def _sheet_to_markdown(ws) -> str:
    """把 openpyxl 的工作表转 Markdown 文档，表格部分用 HTML（支持 colspan/rowspan）。

    修复了 ``pomarkdown.excel2markdown`` 的 6 个 bug：
    1. 合并单元格：第 1 行若合并 → 当作 h2 标题，不进表头
    2. 合并单元格：表头/数据中出现合并 → 用 HTML <td colspan/rowspan> 正确表达
       （不再"重复值"或"留空"模拟 —— 用 HTML 表格，原貌保留）
    3. 不再用 pandas.read_excel（pandas 把合并空列命名为 "Unnamed: N"，导致后续被错误跳过）
    4. 空值 → 空 <td></td>
    5. 自动找第一个非空行当表头（用 <th> 标签）
    6. 多个 sheet → 同一文件，每个 sheet 用 h2 标题分隔

    Args:
        ws: openpyxl 的 Worksheet 对象

    Returns:
        str: 包含 h2 标题和 HTML 表格的 Markdown 文本
    """
    rows = list(ws.iter_rows(values_only=False))
    if not rows:
        return ""

    # 1) 检测第 1 行是否整行合并（标题行）：若合并 → 用合并值作 h2 标题，跳过该行
    #    否则用 sheet 名作 h2 标题（保持每个 sheet 独立、可读）
    first_row_idx = 0
    yield_str = ""
    has_merged_title = False
    if rows and len(ws.merged_cells.ranges) > 0:
        for merge in ws.merged_cells.ranges:
            if (merge.min_row == 1 and merge.max_row == 1
                    and merge.min_col == 1 and merge.max_col == ws.max_column):
                first_row_idx = 1
                title = rows[0][0].value
                if title:
                    yield_str = f"## {title}\n\n"
                    has_merged_title = True
                break

    # 1.5) 没有合并标题时，用 sheet 名当 h2 标题
    if not has_merged_title:
        sheet_title = ws.title
        if sheet_title:
            yield_str = f"## {sheet_title}\n\n"

    if first_row_idx >= len(rows):
        return yield_str

    # 2) 找第一个非全空行作为表头（跳过空行）
    header_row_idx = first_row_idx
    while header_row_idx < len(rows):
        if any(cell.value not in (None, "") for cell in rows[header_row_idx]):
            break
        header_row_idx += 1
    if header_row_idx >= len(rows):
        return yield_str

    n_cols = ws.max_column

    # 3) 构建合并信息表：(r, c) → (min_r, min_c, rowspan, colspan)
    #    只有 anchor（左上角）保留输出；其他合并位置被"合并掉"（colspan/rowspan 自动扩展）
    merge_info: dict[tuple[int, int], tuple[int, int, int, int]] = {}
    for merge in ws.merged_cells.ranges:
        span_r = merge.max_row - merge.min_row + 1
        span_c = merge.max_col - merge.min_col + 1
        for r in range(merge.min_row, merge.max_row + 1):
            for c in range(merge.min_col, merge.max_col + 1):
                merge_info[(r, c)] = (merge.min_row, merge.min_col, span_r, span_c)

    def cell_tag(r_idx_1based: int, c_idx_1based: int, is_header_row: bool) -> str:
        """生成单个单元格的 HTML 标签（<th> 或 <td>），含 colspan/rowspan。"""
        # 1. 合并处理：非 anchor 直接返回空串（由 anchor 的 colspan/rowspan 覆盖）
        if (r_idx_1based, c_idx_1based) in merge_info:
            min_r, min_c, span_r, span_c = merge_info[(r_idx_1based, c_idx_1based)]
            if (r_idx_1based, c_idx_1based) != (min_r, min_c):
                return ""  # 被合并的格子，不输出
            attrs = []
            if span_r > 1:
                attrs.append(f'rowspan="{span_r}"')
            if span_c > 1:
                attrs.append(f'colspan="{span_c}"')
            attr = (" " + " ".join(attrs)) if attrs else ""
        else:
            attr = ""

        # 2. 取值（None → ""）
        v = ws.cell(row=r_idx_1based, column=c_idx_1based).value
        text = "" if v is None else str(v).replace("|", "\\|").replace("\n", " ")

        # 3. 表头用 <th>，数据用 <td>
        tag = "th" if is_header_row else "td"
        return f"<{tag}{attr}>{text}</{tag}>"

    # 4) 写表头
    head_cells = [cell_tag(header_row_idx + 1, c + 1, is_header_row=True)
                  for c in range(n_cols)]
    if not any("</th>" in h for h in head_cells):
        return yield_str

    # 5) 写数据行
    body_rows_html = []
    for r_idx in range(header_row_idx + 1, len(rows)):
        r_1based = r_idx + 1
        row_cells = [cell_tag(r_1based, c + 1, is_header_row=False)
                     for c in range(n_cols)]
        # 整行都是空（合并除外）→ 跳过
        visible = [c for c in row_cells if c]
        if not visible:
            continue
        body_rows_html.append("<tr>" + "".join(row_cells) + "</tr>")

    # 6) 拼成完整 HTML 表格
    head_row = "<tr>" + "".join(head_cells) + "</tr>"
    body = "".join(body_rows_html)
    table = (
        "<table>\n"
        "<thead>\n" + head_row + "\n</thead>\n"
        + ("<tbody>\n" + body + "\n</tbody>\n" if body else "")
        + "</table>\n"
    )
    return yield_str + table


def excel2markdown(
    input_file: str,
    output_file: str = "./excel2markdown.md",
    sheet_name: Optional[str] = None,
) -> str:
    """Convert Excel file to Markdown format.

    将 Excel 表格转换为 Markdown 格式。

    使用场景：
        - 文档编写：把 Excel 数据嵌入 Markdown 文档
        - 博客发布：将表格数据发布到支持 Markdown 的平台
        - README 制作：为 GitHub 项目自动生成表格文档

    Documentation: https://www.python-office.com/modules/markdown/api#excel2markdown

    Args:
        input_file: 输入 Excel 文件路径（.xlsx / .xls）
        output_file: 输出 Markdown 文件路径。Default: ``'./excel2markdown.md'``
        sheet_name: 要转换的工作表名称，留空则转换所有工作表。Default: ``None``

    Returns:
        str: 生成的 Markdown 文件路径
    """
    if not os.path.isfile(input_file):
        raise FileNotFoundError(f"找不到 Excel 文件：{input_file}")

    # 输出目录不存在则创建
    out_dir = Path(output_file).parent
    if str(out_dir) and not out_dir.exists():
        out_dir.mkdir(parents=True, exist_ok=True)

    wb = load_workbook(input_file, data_only=True)
    target_sheets = wb.sheetnames if sheet_name is None else [sheet_name]

    with open(output_file, "w", encoding="utf-8") as md_file:
        first = True
        for name in target_sheets:
            if name not in wb.sheetnames:
                print(f"[python-office] excel2markdown  跳过（无此 sheet）：{name}")
                continue
            ws = wb[name]
            md_text = _sheet_to_markdown(ws)
            if not first:
                md_file.write("\n")
            md_file.write(md_text)
            first = False
    print(f"[python-office] excel2markdown  输出：{output_file}  sheet={sheet_name!r}")
    return output_file
