# -*- coding: UTF-8 -*-
"""修正版的 Excel 按列拆分，解决输出路径、列号校验与工作表异常处理问题。

背景
----
`office.api.excel.split_excel_by_column` 在拿不到 `poexcel.split_excel_by_column`
时会回退到内置实现 `office/lib/excel/SplitExcel.py`（经核实，当前发布的 poexcel
并未导出该函数，因此**回退实现就是实际执行的那份**）。该实现有 4 个缺陷：

1. **输出路径被字符串替换破坏。** 生成输出文件名时用的是
   ``filepath.replace('.xls', ...)``，它会命中路径中**任意位置**的 ``.xls``，
   包括目录名。例如输入 ``.../archive.xls.v2/demo.xls``，会得到
   ``.../archive_Split_时间戳.xls.v2/demo_Split_时间戳.xls`` —— 一个不存在的
   目录，xlwt 保存时抛 FileNotFoundError。``.xlsx`` 分支同样写法、同样问题。

2. **错误的工作表名会抛异常。** ``.xls`` 分支只把「打开文件」包在 try 里，
   工作表查找在 try 之外。表名写错时直接把 ``XLRDError`` 抛给调用者，
   而 ``.xlsx`` 分支却会返回提示字符串，两个格式行为不一致。

3. **缺少列号越界检查。** ``.xls`` 分支没有校验列号，``column`` 超过总列数时
   抛 ``IndexError``；``.xlsx`` 分支会返回「最大列数是 N」的友好提示。

4. **``column=0`` 静默拆错列。** 实现是 1-based（``row_data[column - 1]``），
   但 CLI 帮助写的是 ``column index (0-based)``。传 0 时通过检查后被 Python
   负索引解释为**最后一列**，产生「不报错但结果错误」的输出。

本模块提供一个行为更稳健的实现，可独立使用。

Author:
    wenxiaotan

Project:
    https://www.python-office.com
"""

import datetime
import os

import openpyxl
import xlrd
import xlwt
from tqdm import tqdm

# Excel 对 sheet 名的限制：最长 31 个字符，且不能包含 : \ / ? * [ ]
_SHEET_NAME_MAX_LEN = 31
_SHEET_NAME_INVALID_CHARS = ':\\/?*[]'


def _to_valid_sheet_name(value, used_names: set) -> str:
    """把分组值转换成合法的 sheet 名。

    拆分依据的列内容可能包含 Excel 不允许的字符（例如日期 2026/10/22、
    文件路径、网址），也可能超过 31 个字符，直接用作 sheet 名会抛异常，
    导致整个拆分失败。这里统一替换非法字符并截断。

    Args:
        value: 分组依据的单元格内容。
        used_names (set): 已被占用的 sheet 名，用于避免截断后重名。

    Returns:
        str: 合法的 sheet 名。
    """
    name = str(value)
    for char in _SHEET_NAME_INVALID_CHARS:
        name = name.replace(char, '_')
    name = name.strip()[:_SHEET_NAME_MAX_LEN] or 'Sheet'
    candidate = name
    index = 1
    while candidate in used_names:
        suffix = '_{}'.format(index)
        candidate = name[:_SHEET_NAME_MAX_LEN - len(suffix)] + suffix
        index += 1
    used_names.add(candidate)
    return candidate


def build_split_path(filepath: str) -> str:
    """按原文件扩展名生成拆分后的输出路径。

    修复点 1：不能用 ``str.replace`` 拼接输出名，因为它会命中路径中任意
    位置的扩展名（含目录名）。这里用 ``os.path.splitext`` 精确切分。

    Args:
        filepath (str): 原始文件路径。

    Returns:
        str: 拆分后的输出文件路径，形如 ``<主文件名>_Split_<时间戳><原扩展名>``。

    Example:
        >>> build_split_path('/data/archive.xls.v2/demo.xls').endswith('.xls')
        True
        >>> 'archive_Split' in build_split_path('/data/archive.xls.v2/demo.xls')
        False
    """
    root, ext = os.path.splitext(filepath)
    datetime_str = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')
    return '{}_Split_{}{}'.format(root, datetime_str, ext)


def validate_column(column: int, max_column: int) -> str:
    """校验拆分列号。

    修复点 4：列号是**从 1 开始**的（内部实现为 ``row_data[column - 1]``）。
    ``column=0`` 会因 Python 负索引悄悄取到最后一列，产生「不报错但拆错列」
    的结果，因此这里一并拦截。

    Args:
        column (int): 用户传入的列号。
        max_column (int): 工作表最大列数。

    Returns:
        str: 校验通过时返回空字符串，否则返回错误提示。
    """
    if column < 1:
        return "列号从1开始，取不到第{}列".format(column)
    if max_column < column:
        return "最大列数是{}，取不到第{}列".format(max_column, column)
    return ''


def generate_xls(filepath: str, worksheet_data: dict) -> str:
    """生成 XLS 格式的拆分文件。

    Args:
        filepath (str): 原始文件路径。
        worksheet_data (dict): 工作表数据字典，键为分组名，值为行数据列表。

    Returns:
        str: 新生成的文件路径。
    """
    new_filepath = build_split_path(filepath)
    new_workbook = xlwt.Workbook(encoding='utf-8')
    used_names = set()
    for worksheet_name, row_data_list in worksheet_data.items():
        title = _to_valid_sheet_name(worksheet_name, used_names)
        new_worksheet = new_workbook.add_sheet(title)
        for row_index, row_data in enumerate(row_data_list):
            for column_index, data in enumerate(row_data):
                new_worksheet.write(row_index, column_index, data)
    new_workbook.save(new_filepath)
    return new_filepath


def process_xls(filepath: str, column: int, worksheet_name: str = None) -> str:
    """处理 XLS 格式的 Excel 文件拆分。

    修复点 2（工作表异常）与修复点 3（列号越界）。

    Args:
        filepath (str): Excel 文件路径。
        column (int): 拆分依据的列号，从 1 开始。
        worksheet_name (str, optional): 工作表名称，默认为 None（第一个工作表）。

    Returns:
        str: 处理结果信息（成功时为保存路径提示，失败时为错误提示）。
    """
    try:
        workbook = xlrd.open_workbook(filepath, formatting_info=True)
    except Exception as e:
        return "文件读取异常：{}，错误信息：{}".format(filepath, str(e))

    # 修复点 2：工作表查找也要纳入异常保护，与 .xlsx 分支行为对齐
    try:
        if worksheet_name:
            worksheet = workbook.sheet_by_name(worksheet_name)
        else:
            worksheet = workbook.sheet_by_index(0)
    except Exception as e:
        return "工作表读取异常：{}，错误信息：{}".format(worksheet_name, str(e))

    rows = worksheet.nrows
    cols = worksheet.ncols

    # 修复点 3：补上列号校验
    column_error = validate_column(column, cols)
    if column_error:
        return column_error

    split_data_dict = {}
    for r in tqdm(range(rows)):
        row_data = [worksheet.cell(r, c).value if worksheet.cell(r, c).value != '' else ' '
                    for c in range(cols)]
        temp_data = row_data[column - 1]
        temp_data_list = split_data_dict.get(temp_data, [])
        temp_data_list.append(row_data)
        split_data_dict[temp_data] = temp_data_list

    new_filepath = generate_xls(filepath, split_data_dict)
    return "数据保存在新文件中，文件名：{}".format(new_filepath)


def generate_xlsx(filepath: str, worksheet_data: dict) -> str:
    """生成 XLSX 格式的拆分文件。

    Args:
        filepath (str): 原始文件路径。
        worksheet_data (dict): 工作表数据字典，键为分组名，值为行数据列表。

    Returns:
        str: 新生成的文件路径。
    """
    new_filepath = build_split_path(filepath)
    new_workbook = openpyxl.Workbook()
    # openpyxl 新建工作簿时会自带一个空白 sheet，这里直接复用给第一个分组，
    # 避免拆分结果里多出一个没有内容的 Sheet
    default_worksheet = new_workbook.active
    used_names = set()
    for index, (worksheet_name, row_data_list) in enumerate(worksheet_data.items()):
        title = _to_valid_sheet_name(worksheet_name, used_names)
        if index == 0:
            new_worksheet = default_worksheet
            new_worksheet.title = title
        else:
            new_worksheet = new_workbook.create_sheet(title)
        for row_data in row_data_list:
            new_worksheet.append(row_data)
    new_workbook.save(new_filepath)
    return new_filepath


def process_xlsx(filepath: str, column: int, worksheet_name: str = None) -> str:
    """处理 XLSX 格式的 Excel 文件拆分。

    Args:
        filepath (str): Excel 文件路径。
        column (int): 拆分依据的列号，从 1 开始。
        worksheet_name (str, optional): 工作表名称，默认为 None（第一个工作表）。

    Returns:
        str: 处理结果信息（成功时为保存路径提示，失败时为错误提示）。
    """
    try:
        workbook = openpyxl.load_workbook(filepath, read_only=True, data_only=True)
        try:
            if worksheet_name:
                worksheet = workbook[worksheet_name]
            else:
                worksheet = workbook.active

            column_error = validate_column(column, worksheet.max_column)
            if column_error:
                return column_error

            split_data_dict = {}
            for row in worksheet.rows:
                row_data = [cell.value if cell.value is not None else ' ' for cell in row]
                temp_data = row_data[column - 1]
                temp_data_list = split_data_dict.get(temp_data, [])
                temp_data_list.append(row_data)
                split_data_dict[temp_data] = temp_data_list
        finally:
            workbook.close()
    except Exception as e:
        return "处理异常：{}，错误信息：{}".format(filepath, str(e))

    new_filepath = generate_xlsx(filepath, split_data_dict)
    return "数据保存在新文件中，文件名：{}".format(new_filepath)


def split_excel_by_column(filepath: str, column: int, worksheet_name: str = None) -> str:
    """根据指定列拆分 Excel 文件。

    与 `office.api.excel.split_excel_by_column` 用法一致，但修复了上述 4 个缺陷。

    Args:
        filepath (str): Excel 文件路径，支持 .xls 与 .xlsx。
        column (int): 拆分依据的列号，**从 1 开始**。
        worksheet_name (str, optional): 工作表名称，默认为 None（第一个工作表）。

    Returns:
        str: 处理结果信息（成功时为保存路径提示，失败时为错误提示）。

    Raises:
        FileNotFoundError: 输入文件不存在。

    Example:
        >>> split_excel_by_column('./orders.xlsx', column=1)   # doctest: +SKIP
        '数据保存在新文件中，文件名：./orders_Split_20260101_120000.xlsx'
    """
    if not os.path.isfile(filepath):
        raise FileNotFoundError("文件不存在：{}".format(filepath))

    if filepath.endswith('.xlsx'):
        result = process_xlsx(filepath, column, worksheet_name)
    elif filepath.endswith('.xls'):
        result = process_xls(filepath, column, worksheet_name)
    else:
        return "文件格式不对，不进行处理（仅支持 .xls / .xlsx）：{}".format(filepath)

    print(result)
    return result


if __name__ == "__main__":
    print(__doc__.split('背景')[0].strip())
    print()
    print("输出路径示例（目录名含 .xls 也不会被破坏）：")
    print("  ", build_split_path(os.path.join('data', 'archive.xls.v2', 'demo.xls')))
    print()
    print("列号校验示例：")
    print("   column=0  ->", repr(validate_column(0, 3)))
    print("   column=99 ->", repr(validate_column(99, 3)))
