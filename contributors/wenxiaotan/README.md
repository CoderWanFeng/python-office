# 贡献说明 / README

本目录（`contributors/wenxiaotan/`）提供两个**修正版实现**，用于规避 python-office
当前版本中已复现的两个缺陷。

- 作者：**wenxiaotan**（GitHub: [@wenxiaotan](https://github.com/wenxiaotan)）
- 基准版本：`develop` 分支 HEAD `549bdc9`（v1.1.2，2026-10-29）
- 许可：Apache License 2.0，与 `python-office` 项目保持一致

按仓库贡献约定，本目录**不改动 `office/` 等核心目录**，只提供可独立调用的实现。

---

## 1. 文件清单

| 文件 | 说明 |
| --- | --- |
| `finance_t0_fix.py` | 修正版 T+0 收益计算，解决 `Decimal` / `float` 混算与返回类型不一致 |
| `split_excel_fix.py` | 修正版 Excel 按列拆分，解决输出路径损坏、列号校验缺失、工作表异常外泄 |
| `test_contribution.py` | 上述两个模块的单元测试，共 26 个用例 |

运行测试：

```bash
cd contributors/wenxiaotan
python -m unittest test_contribution -v
# 或
python -m pytest test_contribution.py -q
```

---

## 2. 缺陷一：`t0` 的 `min_rate` 未做 `Decimal` 规范化

### 现象

`office.api.finance.t0` 把 `w_rate`、`buy_price`、`sale_price`、`stamp_tax` 都转成了
`Decimal`，**唯独漏了 `min_rate`**。当买卖金额低于 `RATE_LINE` 时，手续费直接取
`min_rate`（此时仍是 `int` / `float`），随后与 `Decimal` 相减即抛异常。

CLI（`office/cli/commands.py`）把 `min_rate` 声明为 `type: float`，因此下面这条命令
**必然失败**：

```bash
$ python -m office finance t0 11.99 12.26 700 --min-rate 5
po: error: TypeError: unsupported operand type(s) for -:
            'decimal.Decimal' and 'float'

$ python -m office finance t0 11.99 12.26 700     # 不带该参数则正常
170.41800
```

### 附带问题

函数签名与文档均标注 `-> float`，实际返回 `Decimal`：

```bash
$ python -c "import office; print(type(office.finance.t0(11.99,12.26,700)))"
<class 'decimal.Decimal'>
```

这会让调用方的 `isinstance` 判断、`json.dumps` 序列化、与 `float` 混算出现与文档
不符的行为。

### 修正版用法

```python
import sys
sys.path.insert(0, 'contributors/wenxiaotan')

from finance_t0_fix import t0, t0_safe

t0(11.99, 12.26, 700)                  # 170.418，返回 float
t0(11.99, 12.26, 700, min_rate=5.0)    # 上游此处抛 TypeError
t0(100, 110, 700)                      # 6886.25，超过起征线按比例计佣

t0_safe("脏数据", 12.26, 700)           # None，不抛异常
```

### 建议的上游修复

```diff
     w_rate = Decimal(str(w_rate))
+    min_rate = Decimal(str(min_rate))
     ...
     stock_returns = sale_money - buy_money - base_rate - sale_rate - sale_tax
-    return stock_returns
+    return float(stock_returns)
```

---

## 3. 缺陷二：Excel 按列拆分的 4 个问题

### 前置事实

`office.api.excel.split_excel_by_column` 会先尝试 `poexcel.split_excel_by_column`，
取不到则回退到内置实现 `office/lib/excel/SplitExcel.py`。经核实**当前发布的 poexcel
并未导出该函数**：

```bash
$ python -c "import poexcel; print(hasattr(poexcel,'split_excel_by_column'))"
False
```

因此**回退实现就是实际执行的那份代码**，它的问题会直接影响用户。

### 3.1 输出路径被字符串替换破坏

生成输出文件名用的是 `filepath.replace('.xls', ...)`，会命中路径中**任意位置**的
`.xls`，包括目录名：

```bash
# 输入 .../archive.xls.v2/demo.xls
FileNotFoundError: [Errno 2] No such file or directory:
  '...\archive_Split_2026-11-11_151700.xls.v2\demo_Split_2026-11-11_151700.xls'
```

`.xlsx` 分支（原 `:110`）同样写法、同样问题。

### 3.2 错误的工作表名会抛异常

`.xls` 分支只把「打开文件」包在 `try` 里，工作表查找在 `try` 之外：

```bash
$ process_xls('demo.xls', 1, 'Nope')
xlrd.biffh.XLRDError: No sheet named <'Nope'>
```

而 `.xlsx` 分支会返回提示字符串，两个格式行为不一致。

### 3.3 `.xls` 分支缺少列号越界检查

```bash
process_xls(xls, 99)    → IndexError: list index out of range
process_xlsx(xlsx, 99)  → 最大列数是3，取不到第99列
```

### 3.4 `column=0` 静默拆错列

实现是 1-based（`row_data[column - 1]`），但 CLI 帮助写的是
`column index (0-based)`。传 0 时通过检查后被 Python 负索引解释为**最后一列**：

| 输入 | 实际分组列 |
| --- | --- |
| `column=1` | 第 1 列（正确） |
| `column=3` | 第 3 列（正确） |
| **`column=0`** | **第 3 列（错误，应是非法输入）** |

这是「不报错但结果错误」，排查成本最高。

### 修正版用法

```python
import sys
sys.path.insert(0, 'contributors/wenxiaotan')

from split_excel_fix import split_excel_by_column

# 列号从 1 开始
split_excel_by_column('./orders.xlsx', column=1)
# → 输出到 ./orders_Split_<时间戳>.xlsx
```

对上述 4 个缺陷的行为变化：

| 场景 | 上游行为 | 修正版行为 |
| --- | --- | --- |
| 目录名含 `.xls` | `FileNotFoundError` | 正常拆分到原目录 |
| 工作表名错误 | 抛 `XLRDError` | 返回「工作表读取异常：...」 |
| `column` 越界 | 抛 `IndexError` | 返回「最大列数是 N，取不到第 M 列」 |
| `column=0` | **静默按最后一列拆分** | 返回「列号从 1 开始」 |
| 文件不存在 | 抛异常 | `FileNotFoundError`（明确提示） |

### 建议的上游修复

```diff
-def generate_xls(filepath, worksheet_data):
-    datetime_str = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')
-    new_filepath = filepath.replace('.xls', '_Split_{}.xls'.format(datetime_str))
+def _build_split_path(filepath):
+    root, ext = os.path.splitext(filepath)
+    datetime_str = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')
+    return '{}_Split_{}{}'.format(root, datetime_str, ext)
```

并列号校验（`.xls` / `.xlsx` 共用）：

```diff
+def _validate_column(column, max_column):
+    if column < 1:
+        return "列号从1开始，取不到第{}列".format(column)
+    if max_column < column:
+        return "最大列数是{}，取不到第{}列".format(max_column, column)
+    return ''
```

> 注意：`column=0` 从「静默拆错」变为「明确报错」是**有意的行为变更**。现有测试与
> 文档示例都用 `column >= 1`，合法列号的输出结果完全不变。

---

## 4. 重要说明：本目录代码不会被 `pip install` 安装

`contributors/` 目录**不随 python-office 包发布**（该目录没有 `__init__.py`，
`setup.cfg` 的 `packages = find:` 不会收录它）。已实测确认：

```python
>>> from setuptools import find_packages
>>> 'contributors' in [p.split('.')[0] for p in find_packages()]
False
```

这意味着：

- 本目录代码**不会自动修复**已安装的 `office` 包，用户需按下文方式显式导入；
- 若希望修复直接惠及 `pip install python-office` 的用户，需要在 `office/` 内改动
  （参考已合并的 #161、#180 等修复类 PR）。

本贡献因此定位为：**可立即使用的修正实现 + 给维护者的修复参考**。

### 显式导入方式

```python
import sys
sys.path.insert(0, 'path/to/python-office/contributors/wenxiaotan')

from finance_t0_fix import t0
from split_excel_fix import split_excel_by_column
```

---

## 5. 边界声明

1. **只处理本地文件。** 两个模块都不发起网络请求，不上传任何数据。
2. **不修改上游代码。** 本目录只新增文件，未改动 `office/`、`skills/` 等任何目录。
3. **不引入新依赖。** 仅使用 `openpyxl`、`xlrd`、`xlwt`、`tqdm`，均为 python-office
   现有依赖链中的包。
4. **兼容性。** 支持 Python 3.6 及以上，与仓库 `setup.cfg` 声明一致。
5. **测试。** 26 个用例覆盖两个模块的正常路径与上述全部缺陷场景。

---

*Last updated: 2026-11-11*
