# -*- coding: UTF-8 -*-
"""Excel 处理功能模块。

本模块按 https://www.python-office.com/modules/excel/api 官方文档定义，
共 7 个函数，对应子包 ``poexcel``：

    1. fake2excel               - 自动生成模拟数据
    2. merge2excel              - 合并多个 Excel（不同 sheet）
    3. sheet2excel              - 按 sheet 拆分 Excel
    4. merge2sheet              - 合并多个 Excel 的多个 sheet
    5. find_excel_data          - 在 Excel 中搜索内容
    6. split_excel_by_column    - 按指定列拆分
    7. excel2pdf                - Excel 转 PDF

Author:
    程序员晚枫

Project:
    https://www.python-office.com
"""

from __future__ import annotations

from typing import List, Optional

import poexcel


# =====================================================================
# 1. fake2excel - 自动生成模拟数据
# =====================================================================

def fake2excel(
    columns: Optional[List[str]] = None,
    rows: int = 1,
    path: str = "./fake2excel.xlsx",
    language: str = "zh_CN",
) -> str:
    """Automatically create Excel file with mock data.

    自动创建 Excel 文件并模拟数据。

    可用字段：name, phone, email, address, company, job, country, city,
    postcode, ssn, credit_card_number, user_agent, text, sentence。

    Documentation: https://www.python-office.com/modules/excel/api#fake2excel

    Args:
        columns: 列名列表。Default: ``['name']``
        rows: 生成行数。Default: ``1``
        path: 输出 Excel 文件路径。Default: ``'./fake2excel.xlsx'``
        language: 数据语言，``'zh_CN'`` 或 ``'english'``。Default: ``'zh_CN'``

    Returns:
        str: 实际写入的文件路径
    """
    if columns is None or len(columns) == 0:
        columns = ["name"]
    if rows < 1:
        rows = 1
    poexcel.fake2excel(columns=columns, rows=rows, path=path, language=language)
    print(f"[python-office] fake2excel  输出文件：{path}")
    return path


# =====================================================================
# 2. merge2excel - 合并多个 Excel（不同 sheet）
# =====================================================================

def merge2excel(dir_path: str, output_file: str = "merge2excel.xlsx") -> str:
    """Merge multiple Excel files into different sheets.

    将多个 Excel 文件合并到一个 Excel 的不同 sheet 中。

    Documentation: https://www.python-office.com/modules/excel/api#merge2excel

    Args:
        dir_path: 包含多个 Excel 文件的目录路径
        output_file: 合并后的 Excel 文件路径。Default: ``'merge2excel.xlsx'``

    Returns:
        str: 合并后的文件路径
    """
    poexcel.merge2excel(dir_path=dir_path, output_file=output_file)
    print(f"[python-office] merge2excel  输出文件：{output_file}")
    return output_file


# =====================================================================
# 3. sheet2excel - 按 sheet 拆分 Excel
# =====================================================================

def sheet2excel(file_path: str, output_path: str = "./") -> str:
    """Split an Excel into multiple files by sheet.

    将同一个 Excel 里的不同 sheet 拆分为不同的 Excel 文件。

    Documentation: https://www.python-office.com/modules/excel/api#sheet2excel

    Args:
        file_path: 要拆分的 Excel 文件路径
        output_path: 拆分后文件输出目录。Default: ``'./'``

    Returns:
        str: 输出目录
    """
    poexcel.sheet2excel(file_path=file_path, output_path=output_path)
    print(f"[python-office] sheet2excel  输出目录：{output_path}")
    return output_path


# =====================================================================
# 4. merge2sheet - 合并多个 Excel 的多个 sheet
# =====================================================================

def merge2sheet(
    dir_path: str,
    output_sheet_name: str = "Sheet1",
    output_excel_name: str = "merge2sheet",
) -> str:
    """Merge multiple sheets from multiple Excel files into one.

    自动合并多个 Excel 文件的多个 sheet 到一个 Excel 中。

    Documentation: https://www.python-office.com/modules/excel/api#merge2sheet

    Args:
        dir_path: 包含多个 Excel 文件的目录路径
        output_sheet_name: 合并后的 sheet 名称。Default: ``'Sheet1'``
        output_excel_name: 合并后的 Excel 文件名（不含后缀）。Default: ``'merge2sheet'``

    Returns:
        str: 合并后的 Excel 文件名
    """
    poexcel.merge2sheet(
        dir_path=dir_path,
        output_sheet_name=output_sheet_name,
        output_excel_name=output_excel_name,
    )
    print(f"[python-office] merge2sheet  输出文件：{output_excel_name}")
    return output_excel_name


# =====================================================================
# 5. find_excel_data - 在 Excel 中搜索内容
# =====================================================================

def find_excel_data(search_key: str, target_dir: str) -> None:
    """Search for specific content in Excel files.

    在 Excel 文件中搜索指定内容，输出匹配的文件名、行号、内容详情。

    Documentation: https://www.python-office.com/modules/excel/api#find_excel_data

    Args:
        search_key: 要搜索的关键词
        target_dir: 搜索的目录路径
    """
    poexcel.find_excel_data(search_key=search_key, target_dir=target_dir)
    print(f"[python-office] find_excel_data  搜索 {search_key!r} 完成")


# =====================================================================
# 6. split_excel_by_column - 按指定列拆分
# =====================================================================

def split_excel_by_column(
    filepath: str,
    column: int,
    worksheet_name: Optional[str] = None,
) -> List[str]:
    """Split an Excel file by a specified column's content.

    按指定列的内容拆分 Excel 文件，每组独立输出一个 Excel。

    实现说明：``poexcel`` 较新版本已不再提供 ``split_excel_by_column``，
    本函数改用 :mod:`openpyxl` 直接实现，保证可用。

    Documentation: https://www.python-office.com/modules/excel/api#split_excel_by_column

    Args:
        filepath: 要拆分的 Excel 文件路径
        column: 按哪一列的内容进行拆分（1-indexed）
        worksheet_name: 要处理的工作表名称。Default: 第一个工作表

    Returns:
        list[str]: 生成的拆分文件路径列表
    """
    try:
        from openpyxl import Workbook, load_workbook  # noqa: F401
    except ImportError as e:
        raise ImportError(
            "split_excel_by_column 需要 openpyxl，请 pip install openpyxl"
        ) from e

    from openpyxl import Workbook, load_workbook
    from pathlib import Path

    wb = load_workbook(filepath, read_only=True, data_only=True)
    try:
        ws = wb[worksheet_name] if worksheet_name else wb.active
        rows = list(ws.iter_rows(values_only=True))
    finally:
        wb.close()

    if not rows:
        raise ValueError(f"文件 {filepath} 为空，无数据可拆分")

    header = list(rows[0])
    if column < 1 or column > len(header):
        raise ValueError(f"列号 {column} 超出范围（文件共 {len(header)} 列）")

    col_idx = column - 1
    # 按 col_idx 不同的值分组
    groups: dict = {}
    for row in rows[1:]:
        # 用元组化整个 row 作 fallback 防止可变对象做 key
        if col_idx < len(row):
            key = row[col_idx]
        else:
            key = None
        groups.setdefault(key, []).append(list(row))

    in_path = Path(filepath)
    out_dir = in_path.parent
    base = in_path.stem
    outputs: List[str] = []

    for key, group_rows in groups.items():
        safe_key = str(key) if key is not None else "blank"
        # 文件名安全 + sheet 名最大 31 字符
        safe_filename = safe_key.replace("/", "_").replace("\\", "_").replace(":", "_")
        out_path = out_dir / f"{base}_Split_{safe_filename}.xlsx"

        new_wb = Workbook()
        try:
            new_ws = new_wb.active
            new_ws.title = safe_filename[:31] or "Sheet"
            new_ws.append(header)
            for r in group_rows:
                new_ws.append(r)
            new_wb.save(out_path)
        finally:
            new_wb.close()
        outputs.append(str(out_path))

    print(
        f"[python-office] split_excel_by_column  按第 {column} 列拆分为 "
        f"{len(outputs)} 个文件"
    )
    for p in outputs:
        print(f"  - {p}")
    return outputs


# =====================================================================
# 7. excel2pdf - Excel 转 PDF
# =====================================================================

def excel2pdf(excel_path: str, pdf_path: str, sheet_id: int = 0) -> str:
    """Convert specified worksheet from Excel to PDF.

    将 Excel 文件的指定工作表转换为 PDF 格式。

    Documentation: https://www.python-office.com/modules/excel/api#excel2pdf

    Args:
        excel_path: Excel 文件路径
        pdf_path: 转换后 PDF 的保存路径
        sheet_id: 工作表索引（0-indexed）。Default: ``0``

    Returns:
        str: 生成的 PDF 文件路径
    """
    poexcel.excel2pdf(excel_path=excel_path, pdf_path=pdf_path, sheet_id=sheet_id)
    print(f"[python-office] excel2pdf  输出文件：{pdf_path}")
    return pdf_path


__all__ = [
    "fake2excel",
    "merge2excel",
    "sheet2excel",
    "merge2sheet",
    "find_excel_data",
    "split_excel_by_column",
    "excel2pdf",
]
