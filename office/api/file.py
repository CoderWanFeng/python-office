# -*- coding: UTF-8 -*-
"""文件管理功能模块。

本模块按 https://www.python-office.com/modules/file/api 官方文档定义，
共 9 个函数，对应子包 ``pofile``：

    1.  replace4filename             - 批量替换重命名
    2.  file_name_insert_content     - 文件名中间插入内容
    3.  file_name_add_prefix         - 文件名加前缀
    4.  file_name_add_postfix        - 文件名加后缀
    5.  output_file_list_to_excel    - 文件名清单导出到 Excel
    6.  search_specify_type_file     - 按扩展名搜索文件
    7.  get_files                    - 搜索并返回文件列表
    8.  add_line_by_type             - 按类型给文件插入行
    9.  group_by_name                - 按名称分组整理

Author:
    程序员晚枫

Project:
    https://www.python-office.com
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import List, Optional

import pofile


# =====================================================================
# 1. replace4filename - 批量替换重命名
# =====================================================================

def replace4filename(
    path: str,
    del_content: str,
    replace_content: str = "",
    dir_rename: bool = True,
    file_rename: bool = True,
    suffix: Optional[str] = None,
) -> None:
    """Batch rename files/folders by replacing part of their names.

    批量重命名：按关键字替换文件名 / 文件夹名。``replace_content`` 留空则删除 ``del_content``。

    注意：根目录 ``path`` 本身的名称不会被修改。

    Documentation: https://www.python-office.com/modules/file/api#replace4filename

    Args:
        path: 要批量重命名的根目录
        del_content: 文件名中要替换 / 删除的内容
        replace_content: 替换成的新内容，留空则等于删除。Default: ``''``
        dir_rename: 是否同时修改子文件夹名。Default: ``True``
        file_rename: 是否同时修改文件名。Default: ``True``
        suffix: 只处理特定后缀的文件，如 ``'.txt'``；留空处理所有。Default: ``None``
    """
    pofile.replace4filename(
        path=path,
        del_content=del_content,
        replace_content=replace_content,
        dir_rename=dir_rename,
        file_rename=file_rename,
        suffix=suffix,
    )
    print(
        f"[python-office] replace4filename  目录：{path}  "
        f"{del_content!r} → {replace_content!r}"
    )


# =====================================================================
# 2. file_name_insert_content - 文件名中间插入内容
# =====================================================================

def file_name_insert_content(
    file_path: str,
    insert_position: int,
    insert_content: str,
) -> None:
    """Insert characters at a specific position in filename.

    批量重命名：在文件名中间插入字符串。

    Documentation: https://www.python-office.com/modules/file/api#file_name_insert_content

    Args:
        file_path: 文件路径
        insert_position: 插入位置（1 起，3 表示在第 3 个字符后插入）
        insert_content: 要插入的字符串
    """
    pofile.file_name_insert_content(
        file_path=file_path,
        insert_position=insert_position,
        insert_content=insert_content,
    )
    print(
        f"[python-office] file_name_insert_content  "
        f"在位置 {insert_position} 插入 {insert_content!r}"
    )


# =====================================================================
# 3. file_name_add_prefix - 文件名加前缀
# =====================================================================

def file_name_add_prefix(file_path: str, prefix_content: str) -> None:
    """Add prefix to filename.

    批量重命名：给文件名前加前缀。

    Documentation: https://www.python-office.com/modules/file/api#file_name_add_prefix

    Args:
        file_path: 文件路径
        prefix_content: 要添加的前缀字符串
    """
    pofile.file_name_add_prefix(file_path=file_path, prefix_content=prefix_content)
    print(f"[python-office] file_name_add_prefix  前缀：{prefix_content!r}")


# =====================================================================
# 4. file_name_add_postfix - 文件名加后缀
# =====================================================================

def file_name_add_postfix(file_path: str, postfix_content: str) -> None:
    """Add postfix to filename.

    批量重命名：给文件名后加后缀。

    Documentation: https://www.python-office.com/modules/file/api#file_name_add_postfix

    Args:
        file_path: 文件路径
        postfix_content: 要添加的后缀字符串
    """
    pofile.file_name_add_postfix(
        file_path=file_path, postfix_content=postfix_content,
    )
    print(f"[python-office] file_name_add_postfix  后缀：{postfix_content!r}")


# =====================================================================
# 5. output_file_list_to_excel - 文件名清单导出到 Excel
# =====================================================================

def output_file_list_to_excel(dir_path: str) -> str:
    """Write filename list under a directory into an Excel file.

    整理目录下的文件名到一个 Excel 文件。

    Documentation: https://www.python-office.com/modules/file/api#output_file_list_to_excel

    Args:
        dir_path: 目标目录

    Returns:
        str: 生成的 Excel 文件路径
    """
    pofile.output_file_list_to_excel(dir_path=dir_path)
    out = str(Path(dir_path) / "output_file_list_to_excel.xlsx")
    print(f"[python-office] output_file_list_to_excel  输出：{out}")
    return out


# =====================================================================
# 6. search_specify_type_file - 按扩展名搜索
# =====================================================================

def search_specify_type_file(file_path: str, file_type: str) -> None:
    """Search files of a given extension under a directory.

    按扩展名搜索文件。

    Documentation: https://www.python-office.com/modules/file/api#search_specify_type_file

    Args:
        file_path: 搜索的目录
        file_type: 要搜索的扩展名，如 ``'.pdf'`` / ``'.docx'``
    """
    pofile.search_specify_type_file(file_path=file_path, file_type=file_type)
    print(
        f"[python-office] search_specify_type_file  目录：{file_path}  类型：{file_type!r}"
    )


# =====================================================================
# 7. get_files - 搜索并返回文件列表
# =====================================================================

def get_files(
    path: str,
    name: str = "",
    suffix: Optional[str] = None,
    sub: bool = False,
    level: int = 0,
) -> List[str]:
    """Search files under a directory and return a list.

    搜索目录下符合条件的文件并以列表形式返回。

    Documentation: https://www.python-office.com/modules/file/api#get_files

    Args:
        path: 搜索的目录
        name: 文件名关键字（留空匹配所有）
        suffix: 文件后缀，如 ``'.pdf'``（留空匹配所有）
        sub: True=递归搜索子目录
        level: 递归深度（0 表示无限）

    Returns:
        list[str]: 匹配的文件路径列表
    """
    result = pofile.get_files(
        path=path, name=name, suffix=suffix, sub=sub, level=level,
    )
    if isinstance(result, list):
        return [str(p) for p in result]
    if isinstance(result, str):
        return [result] if result else []
    return list(result) if result else []


# =====================================================================
# 8. add_line_by_type - 按类型给文件插入行
# =====================================================================

def add_line_by_type(
    add_line_dict: dict,
    file_path: str,
    file_type: str = ".py",
    output_path: str = "add_line",
) -> None:
    """Add lines to all files of a given type under a directory.

    按文件后缀批量给文件插入行。

    Documentation: https://www.python-office.com/modules/file/api#add_line_by_type

    Args:
        add_line_dict: ``{内容: [文件名, ...]}`` 形式的字典；指定要插入哪些内容到哪些文件
        file_path: 目标目录
        file_type: 要处理的文件后缀（默认 ``.py``）
        output_path: 新文件输出目录（默认 ``add_line``）
    """
    pofile.add_line_by_type(
        add_line_dict=add_line_dict,
        file_path=file_path,
        file_type=file_type,
        output_path=output_path,
    )
    print(
        f"[python-office] add_line_by_type  目录：{file_path}  类型：{file_type!r}  "
        f"输出：{output_path!r}"
    )


# =====================================================================
# 9. group_by_name - 按名称分组整理
# =====================================================================

def group_by_name(
    path: str,
    output_path: Optional[str] = None,
    del_old_file: Optional[bool] = None,
) -> None:
    """Group files under a directory by name into subdirectories.

    按名称把目录下的文件分组整理到子文件夹。

    Documentation: https://www.python-office.com/modules/file/api#group_by_name

    Args:
        path: 源目录
        output_path: 分组后的输出目录。留空则在 ``path`` 同级创建 ``group_by_name`` 子目录
        del_old_file: True=删除原文件，False=保留，None=默认行为
    """
    pofile.group_by_name(
        path=path, output_path=output_path, del_old_file=del_old_file,
    )
    out = output_path or os.path.join(path, "group_by_name")
    print(f"[python-office] group_by_name  输出：{out}")


__all__ = [
    "replace4filename",
    "file_name_insert_content",
    "file_name_add_prefix",
    "file_name_add_postfix",
    "output_file_list_to_excel",
    "search_specify_type_file",
    "get_files",
    "add_line_by_type",
    "group_by_name",
]
