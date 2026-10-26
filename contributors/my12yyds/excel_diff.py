# -*- coding: UTF-8 -*-
"""比对两份 Excel 表格的差异。

适用场景：同一张表被两个人分别改过，或者需要确认「这周的报表和上周比改了什么」。
手工逐行看既慢又容易漏，本方法把差异整理成结构化结果，需要时还能导出成一张差异表。

两种比对方式：
    1. 按位置比对（默认）：逐单元格比较，适合行顺序固定的表。
    2. 按主键比对（指定 key_column）：先按主键配对，再比较同一主键下的字段，
       适合行顺序会变、但每行有唯一编号的表（订单号、学号、工号等）。

与 office.api.excel.merge2excel 的区别：merge2excel 是「把多张表合并成一张」，
本方法是「找出两张表哪里不一样」，两者互补。

Author:
    my12yyds

Project:
    https://www.python-office.com
"""

import os

import openpyxl


def excel_diff(
    before_path: str,
    after_path: str,
    sheet_name: str = None,
    key_column: str = None,
    ignore_case: bool = False,
    output_path: str = None,
) -> dict:
    """比对两份 Excel，返回差异明细，可导出为差异表。

    Args:
        before_path (str): 变更前的 Excel 文件路径，支持 .xlsx。
        after_path (str): 变更后的 Excel 文件路径，支持 .xlsx。
        sheet_name (str, optional): 要比对的工作表名称，两份文件使用同名工作表。
            默认 None，表示各取第一个工作表。
        key_column (str, optional): 主键列名。指定后按主键配对行再比对，适合行顺序会变的表。
            默认 None，表示按行号位置逐单元格比对。
        ignore_case (bool, optional): 为 True 时文本比较忽略大小写。默认 False，精确比较。
        output_path (str, optional): 差异报告的输出路径。指定后会写出一张 .xlsx 差异表，
            包含「差异」和「汇总」两个工作表。默认 None，不写文件。

    Returns:
        dict: 比对结果，包含以下键：
            - mode (str): 比对方式，'position'（按位置）或 'key'（按主键）。
            - sheet (str): 实际比对的工作表名称。
            - header (dict): 表头差异，含 'added' 和 'removed' 两个列表。
            - summary (dict): 汇总，含 changed（变更单元格数）、added_rows（新增行数）、
              removed_rows（删除行数）、identical（是否完全一致）。
            - changes (list): 单元格级变更，每项为 dict，含 row（行号，按位置比对时）、
              key（主键值，按主键比对时）、column（列名）、before、after 五个键。
            - added_rows (list): 新增行，每项含 row 和 key。
            - removed_rows (list): 删除行，每项含 row 和 key。
            - output_path (str): 差异表路径；未导出时为 None。

    Raises:
        FileNotFoundError: 任一 Excel 文件不存在。
        ValueError: 工作表不存在、表格为空、主键列不存在，或主键存在重复值。
    """
    _require_file(before_path)
    _require_file(after_path)

    before_header, before_rows = _load_sheet(before_path, sheet_name)
    after_header, after_rows = _load_sheet(after_path, sheet_name)
    if not before_header or not after_header:
        raise ValueError('表格为空，至少需要一行表头：{} / {}'.format(before_path, after_path))

    mode = 'key' if key_column else 'position'
    changes = []
    added_rows = []
    removed_rows = []

    if mode == 'position':
        column_count = max(len(before_header), len(after_header))
        for index in range(max(len(before_rows), len(after_rows))):
            before_row = before_rows[index] if index < len(before_rows) else None
            after_row = after_rows[index] if index < len(after_rows) else None
            excel_row = index + 2  # 表头占第 1 行

            if before_row is None:
                added_rows.append({'row': excel_row, 'key': None})
                continue
            if after_row is None:
                removed_rows.append({'row': excel_row, 'key': None})
                continue
            for column in range(column_count):
                name = _column_name(before_header, after_header, column)
                old = before_row[column] if column < len(before_row) else None
                new = after_row[column] if column < len(after_row) else None
                if not _same(old, new, ignore_case):
                    changes.append({
                        'row': excel_row,
                        'key': None,
                        'column': name,
                        'before': old,
                        'after': new,
                    })
    else:
        if key_column not in before_header:
            raise ValueError('变更前的表格中没有主键列：{}'.format(key_column))
        if key_column not in after_header:
            raise ValueError('变更后的表格中没有主键列：{}'.format(key_column))

        before_map = _index_by_key(before_rows, before_header, key_column, ignore_case, before_path)
        after_map = _index_by_key(after_rows, after_header, key_column, ignore_case, after_path)

        for key in before_map:
            if key not in after_map:
                removed_rows.append({'row': before_map[key]['row'], 'key': before_map[key]['value']})
        for key in after_map:
            if key not in before_map:
                added_rows.append({'row': after_map[key]['row'], 'key': after_map[key]['value']})

        for key, before_item in before_map.items():
            after_item = after_map.get(key)
            if after_item is None:
                continue
            for column in range(max(len(before_header), len(after_header))):
                name = _column_name(before_header, after_header, column)
                if name == key_column:
                    continue
                old = before_item['cells'].get(name)
                new = after_item['cells'].get(name)
                if not _same(old, new, ignore_case):
                    changes.append({
                        'row': after_item['row'],
                        'key': after_item['value'],
                        'column': name,
                        'before': old,
                        'after': new,
                    })

    header_diff = {
        'added': [name for name in after_header if name not in before_header],
        'removed': [name for name in before_header if name not in after_header],
    }
    summary = {
        'changed': len(changes),
        'added_rows': len(added_rows),
        'removed_rows': len(removed_rows),
        'identical': not changes and not added_rows and not removed_rows and not any(header_diff.values()),
    }

    result = {
        'mode': mode,
        'sheet': _sheet_label(before_path, sheet_name),
        'header': header_diff,
        'summary': summary,
        'changes': changes,
        'added_rows': added_rows,
        'removed_rows': removed_rows,
        'output_path': None,
    }

    if output_path:
        result['output_path'] = _write_report(result, output_path)
    return result


def _require_file(path):
    """校验文件存在。

    Args:
        path (str): 待校验的文件路径。

    Raises:
        FileNotFoundError: 文件不存在。
    """
    if not os.path.isfile(path):
        raise FileNotFoundError('文件不存在：{}'.format(path))


def _load_sheet(path, sheet_name):
    """读取工作表，返回（表头列表，数据行列表）。

    Args:
        path (str): Excel 文件路径。
        sheet_name (str): 工作表名称，None 表示第一个工作表。

    Returns:
        tuple: (header, rows)。header 为列名字符串列表；rows 为二维列表，已去掉末尾空行。

    Raises:
        ValueError: 指定的工作表不存在。
    """
    workbook = openpyxl.load_workbook(path, read_only=True, data_only=True)
    try:
        if sheet_name is None:
            worksheet = workbook.worksheets[0]
        else:
            if sheet_name not in workbook.sheetnames:
                raise ValueError('工作表不存在：{}，可选：{}'.format(sheet_name, workbook.sheetnames))
            worksheet = workbook[sheet_name]
        raw_rows = [list(row) for row in worksheet.iter_rows(values_only=True)]
    finally:
        workbook.close()

    while raw_rows and all(cell is None or cell == '' for cell in raw_rows[-1]):
        raw_rows.pop()
    if not raw_rows:
        return [], []

    header = []
    for index, cell in enumerate(raw_rows[0]):
        text = str(cell).strip() if cell is not None else ''
        header.append(text or '列{}'.format(index + 1))
    return header, raw_rows[1:]


def _sheet_label(path, sheet_name):
    """返回用于结果展示的工作表名称。

    Args:
        path (str): Excel 文件路径，仅在未指定工作表时用于读取默认工作表名。
        sheet_name (str): 用户指定的工作表名称。

    Returns:
        str: 工作表名称。
    """
    if sheet_name:
        return sheet_name
    workbook = openpyxl.load_workbook(path, read_only=True)
    try:
        return workbook.sheetnames[0]
    finally:
        workbook.close()


def _column_name(before_header, after_header, index):
    """取第 index 列的列名，两侧表头不一致时以变更后为准。

    Args:
        before_header (list): 变更前的表头。
        after_header (list): 变更后的表头。
        index (int): 列的序号，从 0 开始。

    Returns:
        str: 列名；两侧都没有该列时返回列号占位符。
    """
    if index < len(after_header):
        return after_header[index]
    if index < len(before_header):
        return before_header[index]
    return '列{}'.format(index + 1)


def _same(before, after, ignore_case):
    """判断两个单元格的值是否相同。

    Args:
        before (object): 变更前的值。
        after (object): 变更后的值。
        ignore_case (bool): 为 True 时文本忽略大小写比较。

    Returns:
        bool: 相同返回 True。
    """
    if isinstance(before, str) and isinstance(after, str) and ignore_case:
        return before.strip().lower() == after.strip().lower()
    return before == after


def _index_by_key(rows, header, key_column, ignore_case, path):
    """按主键列给数据行建立索引。

    Args:
        rows (list): 二维数据行列表。
        header (list): 表头列表。
        key_column (str): 主键列名。
        ignore_case (bool): 为 True 时主键忽略大小写。
        path (str): 文件路径，仅用于错误提示。

    Returns:
        dict: 主键映射到 {'row': Excel 行号, 'value': 原始主键, 'cells': {列名: 值}}。

    Raises:
        ValueError: 主键存在空值或重复值。
    """
    position = header.index(key_column)
    indexed = {}
    for offset, row in enumerate(rows):
        raw = row[position] if position < len(row) else None
        if raw is None or raw == '':
            raise ValueError('{} 第 {} 行的主键「{}」为空'.format(path, offset + 2, key_column))
        key = str(raw).strip().lower() if ignore_case else str(raw).strip()
        if key in indexed:
            raise ValueError(
                '{} 的主键「{}」存在重复值（第 {} 行和第 {} 行）'.format(
                    path, key_column, indexed[key]['row'], offset + 2
                )
            )
        indexed[key] = {
            'row': offset + 2,
            'value': raw,
            'cells': {name: (row[i] if i < len(row) else None) for i, name in enumerate(header)},
        }
    return indexed


def _write_report(result, output_path):
    """把比对结果写成差异 Excel。

    Args:
        result (dict): excel_diff 的返回结果。
        output_path (str): 输出文件路径。

    Returns:
        str: 实际写入的文件路径。

    Raises:
        OSError: 输出目录不存在或不可写。
    """
    directory = os.path.dirname(os.path.abspath(output_path))
    if not os.path.isdir(directory):
        raise OSError('输出目录不存在：{}'.format(directory))

    workbook = openpyxl.Workbook()
    detail = workbook.active
    detail.title = '差异'
    detail.append(['类型', '行号', '主键', '列名', '变更前', '变更后'])

    for item in result['changes']:
        detail.append(['修改', item['row'], item['key'], item['column'], _cell_text(item['before']), _cell_text(item['after'])])
    for item in result['added_rows']:
        detail.append(['新增', item['row'], item['key'], '', '', ''])
    for item in result['removed_rows']:
        detail.append(['删除', item['row'], item['key'], '', '', ''])
    for name in result['header']['added']:
        detail.append(['新增列', '', '', name, '', ''])
    for name in result['header']['removed']:
        detail.append(['删除列', '', '', name, '', ''])

    summary = workbook.create_sheet('汇总')
    summary.append(['项目', '数值'])
    summary.append(['比对方式', result['mode']])
    summary.append(['工作表', result['sheet']])
    summary.append(['变更单元格', result['summary']['changed']])
    summary.append(['新增行', result['summary']['added_rows']])
    summary.append(['删除行', result['summary']['removed_rows']])
    summary.append(['是否一致', '是' if result['summary']['identical'] else '否'])

    workbook.save(output_path)
    return os.path.abspath(output_path)


def _cell_text(value):
    """把单元格值转成适合写入报表的文本。

    Args:
        value (object): 任意单元格值。

    Returns:
        str: 文本形式；None 转为空字符串。
    """
    if value is None:
        return ''
    if isinstance(value, (str, int, float, bool)):
        return value
    return str(value)
