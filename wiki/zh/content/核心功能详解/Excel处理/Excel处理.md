# Excel 处理

<cite>
**本文档中引用的文件**
- [office/api/excel.py](file://office/api/excel.py)
- [examples/poexcel/批量模拟数据.py](file://examples/poexcel/批量模拟数据.py)
- [examples/poexcel/合并多个Excel到一个Excel的不同sheet中.py](file://examples/poexcel/合并多个Excel到一个Excel的不同sheet中.py)
- [examples/poexcel/同一个excel里的不同sheet，拆分为不同的excel文件.py](file://examples/poexcel/同一个excel里的不同sheet，拆分为不同的excel文件.py)
- [examples/poexcel/Excel转PDF.py](file://examples/poexcel/Excel转PDF.py)
</cite>

## 目录
1. [简介](#简介)
2. [功能列表](#功能列表)
3. [数据模拟](#数据模拟)
4. [文件合并与拆分](#文件合并与拆分)
5. [内容搜索](#内容搜索)
6. [格式转换](#格式转换)

## 简介

python-office 的 Excel 处理模块（`office.excel`）基于 poexcel 库，提供 7 个功能，覆盖 Excel 数据模拟、文件合并拆分、内容搜索、格式转换等场景。

## 功能列表

| 功能 | 函数名 | 说明 |
|------|--------|------|
| 模拟数据 | `fake2excel` | 自动创建 Excel 并填充模拟数据 |
| 合并到不同 Sheet | `merge2excel` | 多个 Excel 合并到一个文件的不同 sheet |
| Sheet 拆分 | `sheet2excel` | 同一 Excel 不同 sheet 拆分为不同文件 |
| 合并到同一 Sheet | `merge2sheet` | 多个 Excel 的多个 sheet 自动合并 |
| 内容搜索 | `find_excel_data` | 搜索 Excel 中指定内容 |
| 按列拆分 | `split_excel_by_column` | 按指定列的内容拆分 Excel |
| Excel 转 PDF | `excel2pdf` | 将 Excel 工作表转换为 PDF |

## 数据模拟

### fake2excel
自动创建 Excel 文件并填充模拟数据，基于 Faker 库实现。

```python
import office

office.excel.fake2excel(
    columns=['name', 'phone', 'email'],
    rows=1000,
    path='test.xlsx',
    language='zh_CN'
)
```

**参数说明：**
- `columns`: 列名列表，支持 name、phone、email、address 等多种类型
- `rows`: 生成的行数
- `path`: 输出 Excel 文件路径
- `language`: 数据语言（`zh_CN` 中文 / `english` 英文）

## 文件合并与拆分

### merge2excel — 合并到不同 Sheet
将目录下多个 Excel 文件合并到一个 Excel 文件的不同 sheet 中。

```python
office.excel.merge2excel(dir_path='./my_excels', output_file='all.xlsx')
```

### sheet2excel — Sheet 拆分
将同一个 Excel 里的不同 sheet 拆分为不同的 Excel 文件。

```python
office.excel.sheet2excel(file_path='multi_sheet.xlsx', output_path='./output/')
```

### merge2sheet — 合并到同一 Sheet
将多个 Excel 文件的多个 sheet 自动合并到同一个 sheet。

```python
office.excel.merge2sheet(
    dir_path='./my_excels',
    output_sheet_name='Sheet1',
    output_excel_name='merge2sheet'
)
```

### split_excel_by_column — 按列拆分
按指定列的内容拆分 Excel 文件。

```python
office.excel.split_excel_by_column(
    filepath='data.xlsx',
    column=2,
    worksheet_name='Sheet1'
)
```

## 内容搜索

### find_excel_data
搜索 Excel 中指定内容的文件、行数、内容详情。

```python
office.excel.find_excel_data(
    search_key='张三',
    target_dir='./excels/'
)
```

## 格式转换

### excel2pdf
将 Excel 文件的指定工作表转换为 PDF 格式。

```python
office.excel.excel2pdf(
    excel_path='report.xlsx',
    pdf_path='report.pdf',
    sheet_id=0
)
```

**Section sources**
- [office/api/excel.py](file://office/api/excel.py#L1-L163)
