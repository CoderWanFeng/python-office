---
name: batch_rename_by_excel
description: 按 Excel 中记录的新旧文件名映射批量重命名文件。当用户提到按表格/清单批量改名、按 Excel 对照表重命名文件、批量修改文件名但改名规则已列在表格里时使用。
---

# batch_rename_by_excel Skill

> 按 Excel 映射批量重命名文件

## 功能描述

用户手里有一批需要改名的文件，改名前后的对应关系已经整理在 Excel 里。本 Skill 读取
Excel 中的「原文件名 → 新文件名」映射，批量重命名指定目录下的文件。

和 `replace4filename` 的区别：`replace4filename` 是「按规则批量替换文件名中的字符」，
本 Skill 是「按 Excel 中逐行指定的映射改名」，适合改名规则不统一、只能逐个列出的场景。

## 所属分类

`skills/file/batch_rename_by_excel/`

## 调用方式

```python
from skills.file.batch_rename_by_excel import batch_rename_by_excel
```

实现代码位于贡献者目录，也可以直接引用：

```python
from contributors.my12yyds.batch_rename_by_excel import batch_rename_by_excel
```

> 注意：`contributors/` 不随 `pip install python-office` 一起发布，安装包环境中请直接
> 复制 `contributors/my12yyds/batch_rename_by_excel.py` 到自己的项目里使用。

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `excel_path` | str | 是 | - | 记录新旧文件名映射的 Excel 文件路径，支持 `.xlsx` |
| `folder_path` | str | 是 | - | 需要重命名文件所在的目录路径，只处理该目录第一层的文件 |
| `old_name_column` | str | 否 | `'原文件名'` | Excel 中存放原文件名的列名 |
| `new_name_column` | str | 否 | `'新文件名'` | Excel 中存放新文件名的列名 |
| `sheet_name` | str | 否 | `None` | 工作表名称，默认使用第一个工作表 |
| `dry_run` | bool | 否 | `False` | 为 `True` 时只返回重命名计划，不真正修改文件 |

## 返回值

`dict`，包含 4 个键：

| 键 | 类型 | 说明 |
|----|------|------|
| `renamed` | list | 已重命名的记录，元素为 `(原文件名, 新文件名)` 元组；`dry_run=True` 时为计划重命名的记录 |
| `skipped` | list | 未执行重命名的记录，元素为 `(文件名, 原因)` 元组，例如新旧文件名相同、原文件名或新文件名为空 |
| `missing` | list | Excel 中有记录、但目录下找不到的原文件名 |
| `conflicts` | list | 目标文件名已存在，为避免覆盖而跳过的原文件名 |

## 使用示例

Excel 内容（表头必须是这两列）：

| 原文件名 | 新文件名 |
|---|---|
| a.txt | 2026年1月报表.txt |
| b.txt | 2026年2月报表.txt |

```python
from skills.file.batch_rename_by_excel import batch_rename_by_excel

# 先预览，确认映射没问题
result = batch_rename_by_excel(
    excel_path='./rename_list.xlsx',
    folder_path='./files',
    dry_run=True,
)
print(result['renamed'])

# 确认无误后再真正执行
result = batch_rename_by_excel(
    excel_path='./rename_list.xlsx',
    folder_path='./files',
)
print('成功', len(result['renamed']), '个')
print('找不到', result['missing'])
print('目标已存在', result['conflicts'])
```

## 原始函数

`contributors/my12yyds/batch_rename_by_excel.py::batch_rename_by_excel`
