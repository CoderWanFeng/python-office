# python-office 代码审计报告

审计方式：多 agent 并行工作流（survey → 4 路并行查找 → 对抗式验证 → 用户视角缺口分析，共 42 个 agent），
对 `office/lib/**`、`office/api/**`、`office/compatibility.py`、`setup.cfg`、`tests/**` 做了逐行验证。
所有条目均已通过独立的"对抗式验证"agent 复核（默认不信任发现者，要求验证者亲自读代码定位到具体行才能确认），
未通过验证的 6 条已剔除。以下按严重程度排列，每条给出文件、行号、具体触发场景，可直接据此实现修复。

---

## 已修复（本次会话完成）

### `office/api/pdf.py` — `add_img_water()` 是完全的空操作（no-op）
- **文件**：`office/api/pdf.py:301-341`
- **问题**：该函数解析完弃用参数别名后，直接结束，**从未调用 `popdf.add_img_water(...)`**。对比同文件里其他所有函数（`pdf2docx`、`merge2pdf`、`del4pdf` 等）都以 `popdf.xxx(...)` 结尾，这个函数是唯一的例外。
- **后果**：调用 `add_img_water(input_file=..., mark_file=..., output_file=...)` 静默返回 `None`，不生成任何文件，不抛异常，用户完全无法感知失败。
- **修复**：补上委托调用，注意 `popdf.add_img_water` 的真实签名是旧式参数名 `(pdf_file_in, pdf_file_mark, pdf_file_out)`（已通过 `pip install popdf` 安装后用 `inspect.signature` 验证），不是新参数名：
  ```python
  popdf.add_img_water(pdf_file_in=input_file, pdf_file_mark=mark_file, pdf_file_out=output_file)
  ```
- **验证**：直接加载模块并调用，确认参数正确传递到 `popdf` 内部（`popdf` 自身另有一个独立 bug——`popdf.lib.pdf.add_watermark_service` 缺失 `pdf_add_watermark`，这是 `popdf` 包自己的问题，与本仓库无关，`popdf/__init__.py` 也已将 `add_img_water` 标记为 `__deprecated__`）。
- **状态**：已在本地修改，未提交。

---

## 待修复：高严重度（崩溃 / 挂起 / 常规用法下出错）

### 1. `office/lib/excel/SplitExcel.py:53` — 使用了未导入的 `tqdm`
```python
for r in tqdm(range(rows)):
```
文件顶部只 `import os, xlrd, xlwt, openpyxl, datetime`，没有 `import tqdm`。任何调用 `process_xls`（即 `.xls` 文件走 `split_excel_by_column`）都会立刻 `NameError: name 'tqdm' is not defined`，包括文件自己 `__main__` 里的示例调用。
**修复**：加 `from tqdm import tqdm`。

### 2. `office/lib/excel/SplitExcel.py:100` — 使用已被移除的 openpyxl API
```python
worksheet = workbook.get_sheet_by_name(worksheet_name)
```
`get_sheet_by_name` 在 openpyxl 2.x 就已弃用，3.x 完全移除。只要调用 `split_excel_by_column(..., worksheet_name='Sheet2')`（函数签名明确支持的合法用法），就会 `AttributeError: 'Workbook' object has no attribute 'get_sheet_by_name'`。
**修复**：改为 `workbook[worksheet_name]`。

### 3. `office/lib/image/eliminate_background.py:42-45` — 非 `.jpg`/`.png` 扩展名时 `r,g,b` 未定义
```python
if src_img_path.endswith('.jpg'):
    r, g, b = pix[...]
elif src_img_path.endswith('.png'):
    r, g, b, _ = pix[...]
# 无 else 分支
```
没有 `bc_color` 且文件名是 `.jpeg`（常见的 JPEG 备用扩展名）或大写 `.JPG` 时（`.endswith` 大小写敏感），两个分支都不走，`r/g/b` 从未赋值，后续第 52-55 行使用时直接 `NameError`。
**修复**：加 `else` 分支统一处理，或调用前先 `img.convert('RGBA')` 再取像素，不依赖扩展名字符串判断格式。

### 4. `office/lib/image/eliminate_background.py:43` — 非 RGB 模式 JPEG 导致解包错误
```python
r, g, b = pix[int(width / 20), int(height / 20)]
```
这行在 `img.convert("RGBA")`（第 47 行）**之前**执行，此时如果图片是灰度模式 `'L'`（单通道，合法的 JPEG），`pix[x,y]` 返回单个 int，解包报 `TypeError: cannot unpack non-iterable int object`；CMYK 模式则返回 4 元组报 `ValueError: too many values to unpack`。
**修复**：取像素前先 `img.convert('RGB')` 规范化模式。

### 5. `office/lib/pdf/add_watermark_service.py:3` — import 已移除的 PyPDF2 旧 API，模块直接无法加载
```python
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfReader, PdfWriter
```
`PdfFileWriter`/`PdfFileReader` 在 PyPDF2 3.0+ 完全移除；即使代码里只用到 `PdfReader`/`PdfWriter`，Python 的 `from X import a, b, c, d` 是原子操作，任何一个名字不存在就整行失败。**只要装的是现代 PyPDF2，这个模块连 import 都会报 `ImportError`**，导致整个模块（包括写得对的 `pdf_add_watermark`）完全不可用。
**修复**：删掉未使用的 `PdfFileWriter, PdfFileReader`。

### 6. `office/lib/tools/pwd4wifi_service.py:80` 和 `:101` — 库函数里调用 `exit(0)`
```python
if interface.status() == 4:
    print(f'连接成功！密码为：{pwd}')
    exit(0)
```
`wifi_password_crack()` 是普通函数，不在 `__main__` guard 内。`exit(0)` 抛 `SystemExit`（继承自 `BaseException`，外层 `except Exception` 捕不到）。如果任何 Web 服务/GUI 程序 import 这个模块并调用它，破解成功的那一刻会直接**杀死整个宿主进程**，而不是把密码返回给调用者。
**修复**：把两处 `exit(0)` 改成 `return pwd`（并调整函数返回值设计，让调用者能拿到结果）。

### 7. `office/lib/tools/pwd4wifi_service.py:52` — 无超时的忙等待循环
```python
while interface.status() == 4:
    pass
```
纯自旋等待，没有 `sleep`、没有超时。如果网卡状态因为驱动/虚拟环境等原因一直停在 4（已连接），会无限占满一个 CPU 核心且永不返回。
**修复**：加 `time.sleep(0.1)` 和最大重试次数/超时时间。

### 8. `office/lib/tools/pwd4wifi_service.py:64-84` — pwd_list 全部试错后死循环
```python
while True:
    if pwd_list:
        for pwd in pwd_list:
            ...
        print(f'{pwd_list}中，没有合适的密码')
    # 没有 break，会再次回到 while True 顶部，重复同样的列表
```
提供的密码列表全部尝试失败后，没有 `break`/`return`，会带着同一份列表无限重试，函数永不返回。
**修复**：for 循环结束后加 `break` 或 `return None`。

### 9. `office/lib/tools/weather_service.py:12-13` — 正则匹配失败时下标越界
```python
weather = pat_weather.findall(content)
print(weather[0])          # 12
print('更新时间：', up_time[0])  # 13
```
目标网页结构变化、URL 错误或被重定向时 `findall` 返回 `[]`，`[0]` 直接 `IndexError`，两处都没有任何保护。爬虫类代码这是最常见的失败模式，不是极端情况。
**修复**：判空后再取，取不到时给出明确的错误信息而不是裸 `IndexError`。

### 10. `office/lib/decorator_utils/instruction_url.py:123` — 装饰器里字典漏配就整个函数报错
```python
if func_filename in instruction_file_dict.keys() and instruction_file_dict[func_filename][func.__name__]:
```
新增一个被 `@instruction` 装饰的函数，但忘了在对应的 `xxx_dict` 里加它的 key，调用这个新函数直接 `KeyError`，**函数体根本不会执行**（这行代码在真正调用 `func(*args, **kwargs)` 之前）。
**修复**：改成 `instruction_file_dict.get(func_filename, {}).get(func.__name__)`。

### 11. `office/compatibility.py:36` + 239 — import 期无保护的文件系统写入
```python
# 第239行，模块级别，import 时无条件执行：
compatibility_checker = check_compatibility()
```
内部调用链最终会 `mark_file.write_text(...)`，没有任何 try/except。只读 HOME 目录（常见于部分 CI 容器、锁定的企业 Windows 账户）下 `import office` 会直接抛 `PermissionError`/`OSError`，**导致整个包无法导入**，不仅仅是兼容性提示功能失效。
**修复**：给这段包裹 try/except，写入失败时静默跳过提示，不应该影响正常导入。

### 12. `office/api/pdf.py:301`（历史bug，已修复，见上方"已修复"章节）

---

## 待修复：中等严重度（边界情况崩溃 / 静默错误吞掉 / 资源泄漏）

### 13. `office/lib/excel/SplitExcel.py:42-45, 95-98` — 裸 `except:` 吞掉所有异常
两处（`.xls` 和 `.xlsx` 分支）都用裸 `except:` 把权限错误、文件损坏、内部解析 bug 全部压成同一句 `"文件读取异常：{filepath}"`，调用者无法区分"文件不存在"和"文件被占用"和"文件损坏"。
**修复**：改成 `except Exception as e:`，并把 `e` 的信息带进返回消息。

### 14. `office/lib/excel/SplitExcel.py:96` — `openpyxl.load_workbook(..., read_only=True)` 从不 `close()`
read_only 模式下 openpyxl 官方文档要求显式 `close()` 释放文件句柄；批量处理很多文件时会逐渐耗尽文件描述符，最终 `OSError: Too many open files`。
**修复**：用 `with` 或 `try/finally` 确保 `workbook.close()`。

### 15. `office/lib/pdf/add_watermark_service.py:47,62` — 输入流从不关闭
`input_stream`/`mark_stream` 用 `open()` 打开后从未 `close()`，加密文件解密失败时的 `return False`（第58行）更是直接跳过后续所有清理。批量处理场景下会泄漏文件句柄。
**修复**：用 `with open(...)` 或 `try/finally`。

### 16. `office/lib/pdf/add_watermark_service.py:67` — 水印 PDF 页数为 0 时下标越界
```python
page.merge_page(pdf_watermark.pages[0])
```
没有检查水印 PDF 至少有一页，如果调用者传入一个 0 页的水印文件，直接 `IndexError`，没有任何友好提示。
**修复**：调用前检查 `len(pdf_watermark.pages) > 0`。

### 17. `office/lib/image/add_watermark_service.py:41` — `set_opacity()` 假设图片一定有 alpha 通道
```python
alpha = im.split()[3]
```
这是一个导出的公共函数，文档没写"必须是 RGBA"，直接传 RGB 图片进来会 `IndexError: tuple index out of range`。当前内部唯一调用点碰巧总是传 RGBA，但作为公共 API 缺少防护。
**修复**：函数开头 `im = im.convert('RGBA')` 或在文档里明确注明前置条件并加断言。

### 18. `office/lib/image/add_watermark_service.py:138` — 批量水印失败时静默吞掉所有异常
```python
except Exception as e:
    print(new_name, "保存失败。错误信息：", e)
```
`add_mark2file` 返回类型标注是 `-> None`，任何失败（字体文件缺失、磁盘满、权限错误）都只是 print，调用者拿到的返回值和成功时完全一样（都是 `None`），批处理脚本无法判断真的成功了没有。
**修复**：至少改为返回 `bool` 表示成功/失败，或重新抛出异常让调用者决定怎么处理。

### 19. `office/lib/ppt/ppt2pdf_service.py:26-31` — PowerPoint COM 对象失败时永不 `Quit()`
```python
ppt = ppt_app.Presentations.Open(filename)
ppt.SaveAs(output_filename, 32)
ppt_app.Quit()   # 前面任何一步抛异常，这行就永远不会执行
```
没有 try/except/finally。`SaveAs` 因为路径不存在等原因失败时，`ppt_app.Quit()` 被跳过，后台留下一个隐藏的、看不见窗口的 PowerPoint.exe 进程，Python 垃圾回收也不保证真正结束这个进程。批量处理失败文件会累积多个孤儿进程。
**修复**：整个函数体包 try/finally，finally 里调用 `ppt_app.Quit()`。

### 20. `office/lib/tools/pwd4wifi_service.py:14, 48` — 硬编码取第一个无线网卡，无边界检查
```python
interface = wifi.interfaces()[0]
```
没有无线网卡（无头服务器、网卡被禁用）时 `wifi.interfaces()` 返回空列表，`[0]` 直接 `IndexError`。
**修复**：判空后给出"未检测到无线网卡"的明确提示。

### 21. `office/lib/image/eliminate_background.py:36` — `_hex_to_rgb` 返回 `None` 时解包崩溃
```python
r, g, b = _hex_to_rgb(bc_color)
```
`_hex_to_rgb` 对格式不对的颜色字符串（比如漏了开头的 `#`）只是 print 警告然后 `return None`，这里直接解包 `None` 会报一个和真实原因毫无关系的 `TypeError: cannot unpack non-iterable NoneType object`。
**修复**：`_hex_to_rgb` 改成抛 `ValueError` 并带上清晰的错误信息，而不是返回 `None` 再让调用方莫名其妙崩溃。

### 22. `office/api/finance.py:22` — 返回类型标注与实际返回值不符
```python
def t0(...) -> float:
    ...
    return stock_returns  # 实际是 Decimal 对象
```
函数内部全程用 `Decimal` 计算，标注却是 `float`。调用者如果用 `isinstance(result, float)` 判断或 `json.dumps({'profit': t0(...)})` 序列化，会直接 `TypeError: Object of type Decimal is not JSON serializable`。
**修复**：函数末尾 `return float(stock_returns)`，或把标注改成 `-> Decimal`（如果希望保留精度，后者更合理，但要同步更新文档）。

### 23. `office/__init__.py` — `office/api/web.py` 被遗漏，未在包初始化时导入
`office/__init__.py` 第 7-19 行导入了 email/excel/file/finance/image/pdf/ppt/tools/video/wechat/word/markdown/ocr，唯独漏了 `web`。`office/api/web.py` 里的 `url2ebook()` 实际存在且 `pospider` 依赖也已在 `setup.cfg` 声明，但 `import office; office.web.url2ebook(...)` 会报 `AttributeError: module 'office' has no attribute 'web'`，跟其他模块的使用方式不一致。
**修复**：在 `office/__init__.py` 里加一行 `from office.api import web`。

---

## 待修复：低严重度 / 测试与流程问题

### 24. `tests/test_code/test_tools/` 缺少 `__init__.py`
`tests/test_code/test_tools.py`（文件）和 `tests/test_code/test_tools/`（目录）同名，Python 优先解析成模块而不是包，导致目录下的 `test_trans.py` 对 `unittest discover()` 完全不可见（`python -m unittest discover` 静默报 0 个测试，退出码 5）。已用隔离环境实测复现，加上 `__init__.py` 后确认修复。pytest 默认配置不受影响（其收集机制不依赖这个）。
**修复**：新增 `tests/test_code/test_tools/__init__.py`（空文件即可）。

### 25. 测试文件之间工作目录（CWD）约定不一致，没有单一 CWD 能让所有测试都通过
`test_excel.py`/`test_file.py`/`test_image.py`/`test_ruiming.py` 等用 `'../test_files/...'`（相对 `tests/test_code/`），而 `test_pdf.py` 用 `'./tests/test_files/pdf/...'`（相对仓库根目录）。两种约定互斥：CWD 设为 `tests/test_code/` 时 `test_pdf.py` 失败，CWD 设为仓库根目录时其他测试失败。且仓库里没有 `conftest.py`/`pytest.ini` 统一配置。
**修复**：统一所有测试文件的路径基准（建议都改成基于 `os.path.dirname(__file__)` 的相对路径，不依赖进程 CWD），或补一个 `conftest.py` 固定 CWD。

### 26. `tests/test_code/test_ppt.py:22-25` — 已知会失败的测试没有标记 skip
```python
# todo: 文件打开有异常
def test_ppt2img(self):
    ppt2img(...)
```
作者已经在注释里承认这个测试有已知异常，但没有用 `@unittest.skip("原因")` 标记，导致每次跑全量测试都会看到一个"预期内"的失败，和真正的新增回归无法区分。
**修复**：加 `@unittest.skip("文件打开有异常，待修复")` 装饰器，或修复根本问题后去掉注释。

---

## 用户视角的功能缺口（按 影响 × 实现难度 排序，均可在本仓库单个 PR 内完成，不涉及外部 po* 包）

### 1. 非 Windows 首次 `import office` 时兼容性提示可能打印两次，且无法关闭
`office/compatibility.py` 的 `check_compatibility()` 在模块级别（import 时）执行一次，`office/__init__.py` 又显式调用了一次，非 Windows 用户第一次 `import office` 可能看到两遍完整的 rich 表格输出。没有任何环境变量或参数可以关闭它，唯一的"开关"是 `~/.python-office/first_run_mark` 标记文件，且这个文件的写入本身还有前面提到的 bug 11（无保护写入可能直接让 import 失败）。
**建议修复**：去重两处调用（只保留 `__init__.py` 里的），加一个 `PYTHON_OFFICE_NO_BANNER` 环境变量在 `display_warning()` 开头判断并直接 return。
**影响**：高——所有非 Windows 新用户的第一印象都会被这段意外的 stdout 输出干扰，在 CI/notebook 场景下更是噪音污染。
**难度**：低——只涉及 2 个文件。

### 2. `except_dec` 装饰器统一吞异常、只 print、从不重新抛出
`office/lib/utils/except_utils.py` 的 `except_dec` 捕获所有异常，打印一段装饰性文字后返回 `None`，从不 `raise`，也不走 `logging`/`loguru`（`loguru` 已经是 `setup.cfg` 里声明的依赖，但完全没用上）。调用者没法区分"函数本来就该返回 None"和"函数内部出错了"。
**建议修复**：把 `print()` 换成 `logging.getLogger('office').exception(...)` 或用已声明的 `loguru`，并把原始异常重新抛出（或提供一个可选参数控制是否吞掉）。
**影响**：高——这是个跨多个模块使用的公共装饰器，行为改一次全局受益，但需要先排查所有调用点确认没有依赖"吞异常返回 None"这个行为。
**难度**：中高——单文件改动，但要审计所有 `@except_dec` 使用点。

### 3. 没有统一的异常体系，调用者无法用一个 `except` 兜住所有 python-office 自己抛出的错误
`word.py` 的 `_load_poword()` 会抛一个写得很好的自定义 `ModuleNotFoundError`，但没有一个 `office.exceptions.OfficeError` 基类。用户想统一捕获"python-office 抛出的任何错误"时，必须枚举 `ModuleNotFoundError`/`ImportError`/`AttributeError` 等各种底层异常类型。
**建议修复**：新增 `office/exceptions.py`，定义 `OfficeError(Exception)` 及若干子类（如 `MissingDependencyError(OfficeError)`），让现有的 `_load_poword` 等函数改用子类抛出（因为是继承关系，现有 `except ModuleNotFoundError` 的代码不受影响）。
**影响**：中高——纯增量修改，向后兼容。
**难度**：低——新增一个文件加几处 import 改动。

### 4. 没有 `py.typed` 标记，IDE 自动补全体验差，与"一行代码"的产品定位矛盾
`office/` 下没有 `py.typed` 文件。按 PEP 561，没有这个标记的包，类型检查器（mypy/pyright）会把整个包当作无类型对待，即使代码里已经写了一部分类型标注。这个库自我定位是"零基础一行代码搞定办公自动化"，恰恰是最依赖 IDE 参数提示的用户群体，却得不到任何补全支持。
**建议修复**：新增空文件 `office/py.typed`，在 `setup.cfg` 的 `package_data`/`include_package_data` 里注册，同时把 `office/api/*.py` 里已经部分标注类型的函数补全返回类型标注（比如很多写了 `Returns: None` 文档但函数签名没有 `-> None`）。
**影响**：高——直接影响目标用户群体的核心体验（IDE 自动补全）。
**难度**：低——加文件 + 打包配置一行 + 机械性补标注，不涉及外部包。

### 5. 没有 CLI 入口，与"办公自动化工具"的产品定位不符
`setup.cfg` 的 `[options]` 里没有 `[options.entry_points]`/`console_scripts` 配置。尽管官网宣传"73个即用型 Skill，一行代码搞定办公自动化"，非开发者用户（README 自己列的"使用场景"里包括办公室职员、学生）仍然必须先写一个 `.py` 文件才能跑任何一个转换功能，无法直接在终端/批处理脚本里一条命令调用。
**建议修复**：新增 `office/cli.py`，用标准库 `argparse`（避免引入新的重依赖）暴露最高频的几个 skill 作为子命令（如 `pdf2docx`、`docx2pdf`、图片压缩等），在 `setup.cfg` 新增 `[options.entry_points]` 注册 `office = office.cli:main`。
**影响**：中——显著降低非开发者用户的上手门槛，但属于增量能力，不修复现有断裂的工作流。
**难度**：中——需要决定覆盖哪些 skill（避免一次性想覆盖全部 73 个导致范围失控），建议先选 5-10 个高频功能，单个 PR 内可完成。

---

## 附：验证方法说明

- 每条"已确认"的问题都经过独立的对抗式验证 agent 复核：验证者被要求默认不信任发现者的结论，必须自己读取对应文件的确切行号，找到问题代码原文引用后才能给出 `confirmed: true`。
- 有 6 条最初被发现者提出、但未通过对抗式验证的候选问题已被剔除，不在本文档中（多为对 `setup.cfg` 平台标记的误报，验证后确认标记是正确的）。
- 涉及外部 PyPI 包（`poexcel`/`poword`/`popdf`/`poimage` 等，均不在本仓库内）内部的 bug 不在本次审计范围内，除非该 bug 是本仓库 wrapper 层代码直接导致的（如条目 1 的 `add_img_water`，问题出在 wrapper 层缺失调用，而不是 `popdf` 内部逻辑）。
