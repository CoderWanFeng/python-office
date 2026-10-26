---
name: excel2csv
description: 把 Excel 工作表导出为 CSV，默认 utf-8-sig 编码解决中文乱码，支持多工作表批量导出。当用户提到 Excel 转 CSV、表格转文本、CSV 乱码时使用。
---

# excel2csv Skill

> 把 Excel 导出成 CSV，中文不乱码

## 功能描述

把一个或多个工作表导出为 CSV。默认使用 `utf-8-sig`（带 BOM），
双击用 Excel 打开中文不会乱码；需要给 Linux 工具链消费时可以改成 `utf-8`。
多工作表时会按 `<文件名>_<工作表名>.csv` 分别导出。

## 所属分类

`skills/excel/excel2csv/`

## 调用方式

```python
from skills.excel import excel2csv

excel2csv(excel_path='报表.xlsx', output_dir='./csv')
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `excel_path` | str | 是 | - | Excel 文件路径 |
| `output_dir` | str | 否 | `None` | 输出目录，默认与 Excel 同目录 |
| `sheet_name` | str | 否 | `None` | 只导出指定工作表，默认全部 |
| `encoding` | str | 否 | `'utf-8-sig'` | 输出编码 |
| `delimiter` | str | 否 | `','` | 分隔符，可用 `';'` 或 `'\t'` |

## 返回值

`dict`，包含 `files`（CSV 绝对路径列表）、`rows`（工作表名 -> 数据行数）、
`encoding`、`delimiter`。

## 使用示例

```python
from skills.excel import excel2csv

result = excel2csv('报表.xlsx', output_dir='./csv')
for path in result['files']:
    print('已导出', path)
print('行数统计', result['rows'])
```

## 原始函数

`contributors/my12yyds/excel2csv.py`
