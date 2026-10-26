# 贡献声明 / Declaration

本文件声明 `contributors/my12yyds/` 目录下代码的作者、维护范围、许可与边界。

---

## 1. 作者与维护者

| 项目 | 内容 |
| --- | --- |
| 作者 | **my12yyds**（GitHub: [@my12yyds](https://github.com/my12yyds)） |
| 身份 | 本目录代码的**作者与核心维护者** |
| 维护范围 | `contributors/my12yyds/` 下的全部源码、测试与文档，以及 `skills/excel/` 下由本目录提供的 5 个 Skill 包装 |
| 联系方式 | 通过 GitHub Issue / Pull Request @my12yyds |

「核心维护者」在本文件中指**本贡献模块的维护责任人**：这部分代码的设计、缺陷修复、
向后兼容和文档由 my12yyds 负责。它不表示、也不应被理解为对 `python-office`
上游项目的维护权、发布权或决策权。

## 2. 与上游项目的关系

`python-office` 项目由 **CoderWanFeng** 创建并维护，项目主页为
<https://www.python-office.com>，仓库为 <https://github.com/CoderWanFeng/python-office>。

本目录是该项目开放给贡献者的代码目录，遵循仓库的贡献约定：

- 所有实现放在 `contributors/my12yyds/`，不改动 `office/` 等核心目录；
- 新增方法按约定在 `skills/<分类>/<方法>/` 下提供 Skill 包装；
- 对既有代码的意见通过 Issue 提出，不直接修改他人代码。

本声明**不改变**上游项目的版权归属、维护权与发布权。上游维护者仍可基于项目规则
对本目录代码提出修改要求或不予合并。

## 3. 贡献清单

### 3.1 本次新增（v1）

| 方法 | 作用 | 与既有方法的区别 |
| --- | --- | --- |
| `excel_diff` | 比对两份 Excel，按位置或按主键输出单元格级差异，可导出差异表 | `merge2excel` 是合并，本方法是找差异 |
| `excel_dedupe` | 按指定列或整行去重，返回重复行与保留行的对应关系 | 既有方法没有重复检测能力 |
| `excel_column_stats` | 逐列统计填充率、类型、唯一值数量与数值分布 | `find_excel_data` 是按关键词找内容，本方法是按列做画像 |
| `excel2json` | 工作表转 JSON，支持 records / columns / values 三种结构 | `excel2markdown` 输出给人看，本方法输出给程序读 |
| `excel2csv` | 工作表导出 CSV，默认 utf-8-sig 解决中文乱码，支持多表批量 | `excel2pdf` 输出 PDF，本方法输出纯文本 |

### 3.2 此前贡献

| 方法 | 作用 |
| --- | --- |
| `batch_rename_by_excel` | 按 Excel 中记录的新旧文件名映射批量重命名文件 |

### 3.3 配套文件

| 文件 | 说明 |
| --- | --- |
| `test_excel_toolkit.py` | 上述 5 个方法的单元测试，共 39 个用例 |
| `test_batch_rename_by_excel.py` | `batch_rename_by_excel` 的单元测试 |
| `skills/excel/<方法>/SKILL.md` | 每个方法的参数表、返回值说明与调用示例 |
| `skills/excel/<方法>/__init__.py` | Skill 包装，含安装包环境的兜底提示 |

## 4. 许可

本目录代码以 **Apache License 2.0** 授权，与 `python-office` 项目保持一致。
你可以自由使用、修改和分发，但需保留版权与许可声明。

## 5. 边界声明

为避免误解，明确以下事实：

1. **只处理本地文件。** 全部方法只读写本机路径，不发起网络请求，不上传任何数据。
2. **不修改原文件。** 除显式指定 `output_path` 写出新文件外，方法不会改动输入文件。
3. **不做格式转换之外的事。** 方法只做数据读取、比对、统计和格式转换，
   不评估数据业务含义，也不做任何合规判断。
4. **依赖最小化。** 仅依赖 `openpyxl`（`python-office` 已有依赖链中包含），
   不引入新的第三方包。
5. **兼容性目标。** 支持 Python 3.6 及以上版本，与仓库 `setup.cfg` 的声明保持一致。

## 6. 维护承诺

- 对与本目录代码相关的 Issue 和 Pull Request，由 my12yyds 负责响应与修复；
- 修复缺陷时优先保持函数签名与返回结构不变，确需变更时在提交说明中标注；
- 新增能力沿用同样的注释规范：每个函数记录参数、返回值与可能抛出的异常。

---

*Last updated: 2026-10-26*
