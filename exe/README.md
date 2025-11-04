# Python-Office Excel GUI 应用集合

这个文件夹包含了python-office库Excel功能的PySide6图形界面应用。

## Excel功能模块

- **fake2excel.py** - 自动创建Excel并模拟数据
- **merge2excel.py** - 多个Excel合并到一个文件的不同sheet中
- **sheet2excel.py** - 同一个Excel的不同sheet拆分为不同文件
- **merge2sheet.py** - 多个Excel的多个sheet自动合并
- **find_excel_data.py** - 搜索Excel中指定内容
- **split_excel_by_column.py** - 按指定列拆分Excel
- **excel2pdf.py** - Excel转PDF格式

## 使用说明

每个文件都是独立的PySide6 GUI应用，可以直接运行：

```bash
python fake2excel.py
```

## 依赖

- PySide6
- python-office库
- poexcel模块