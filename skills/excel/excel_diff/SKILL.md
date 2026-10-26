---
name: excel_diff
description: 比对两份 Excel 表格的差异，按位置或按主键找出修改、新增、删除的行，可导出差异表。当用户提到对比 Excel、Excel 差异、两份表格有什么不同、核对表格时使用。
---

# excel_diff Skill

> 比对两份 Excel，输出单元格级差异，可导出差异表

## 功能描述

把两份 Excel 的同一张工作表做对比，返回每个变化的单元格、新增行、删除行和表头变化。
支持两种模式：按行号逐格比对（适合行顺序固定的表），或按主键配对后再比对
（适合行顺序会变、但每行有唯一编号的表）。

## 所属分类

`skills/excel/excel_diff/`

## 调用方式

```python
from skills.excel import excel_diff

excel_diff(
    before_path='上周报表.xlsx',
    after_path='本周报表.xlsx',
    key_column='订单号',
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `before_path` | str | 是 | - | 变更前的 Excel 路径 |
| `after_path` | str | 是 | - | 变更后的 Excel 路径 |
| `sheet_name` | str | 否 | `None` | 工作表名，默认取第一个 |
| `key_column` | str | 否 | `None` | 主键列名；指定后按主键配对行 |
| `ignore_case` | bool | 否 | `False` | 文本比较是否忽略大小写 |
| `output_path` | str | 否 | `None` | 差异表输出路径，指定后写出 .xlsx |

## 返回值

`dict`，包含 `mode`、`sheet`、`header`、`summary`、`changes`、`added_rows`、
`removed_rows`、`output_path` 八个键。`summary` 中的 `identical` 表示两份表是否完全一致。

## 使用示例

```python
from skills.excel import excel_diff

result = excel_diff('v1.xlsx', 'v2.xlsx', key_column='编号', output_path='差异.xlsx')
print(result['summary'])
for item in result['changes']:
    print(item['key'], item['column'], item['before'], '->', item['after'])
```

## 原始函数

`contributors/my12yyds/excel_diff.py`
