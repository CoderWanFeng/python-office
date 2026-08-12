# PR #154 代码审查报告 — feat(word): 支持隐藏 doc2docx 转换进度条

> 审查方式：基于 PR diff 静态分析 + 本地仓库 `develop` 分支（HEAD `c8f263d`）交叉核对
> 注：`gh` CLI 未登录 GitHub，本报告未发布为 PR 评论。如需发布，请先 `gh auth login`。

## 一、PR 元数据

| 项 | 内容 |
|----|------|
| **标题** | feat(word): 支持隐藏 doc2docx 转换进度条 |
| **作者** | [@forever-ivy](https://github.com/forever-ivy) |
| **源分支** | `forever-ivy:feat/doc2docx-progress-toggle` |
| **目标分支** | `CoderWanFeng:develop` |
| **变更文件** | 3 个（`office/api/word.py`、`skills/word/doc2docx/SKILL.md`、`tests/test_code/test_word_api_parameters.py`） |
| **提交数** | 1（67 additions, 3 deletions） |
| **修复 Issue** | #139 |
| **底层依赖** | `CoderWanFeng/poword#3`（**当前状态：OPEN，未合并**） |

## 二、提交列表

- `feat(word): 支持隐藏 doc2docx 转换进度条`（1 commit）

## 三、变更概览

| 文件 | 类型 | 关键改动 |
|------|------|----------|
| `office/api/word.py` | 修改 | `doc2docx` 新增 `show_progress: bool = True`；`show_progress=False` 时向 `poword.doc2docx` 转发 `show_progress=False`，否则不传该键保持兼容 |
| `skills/word/doc2docx/SKILL.md` | 修改 | 示例与参数表补充 `show_progress` |
| `tests/test_code/test_word_api_parameters.py` | 新增 | mock `poword`，验证默认调用与显式隐藏两种参数转发 |

## 四、自动化发现

### 🟠 BLOCKER — PR 基于过时 develop，合入将冲突并覆盖 #157 的改进
**文件**：`office/api/word.py`（`doc2docx`）

本地 `develop` 当前 HEAD（`c8f263d`）历史包含提交 `5e8318b Support full output path in doc2docx (#157)`，该提交已为 `doc2docx` 带来两处关键改动，**而 PR #154 的 diff 上下文里完全没有这些**：

1. `output_name` 自动解析（#157 引入）：
   ```python
   if output_name is None and Path(output_path).suffix.lower() == ".docx":
       output_file = Path(output_path)
       output_path = str(output_file.parent)
       output_name = output_file.name
   ```
2. 全模块已改为 `_load_poword()` **延迟加载**（仅在调用时 `import poword`），避免 Windows 专用依赖在 `import office` 时触发 `ModuleNotFoundError`：
   ```python
   poword = _load_poword()
   poword.doc2docx(input_path=input_path, output_path=output_path, output_name=output_name)
   ```

PR #154 的改动却是直接把调用替换为 `poword.doc2docx(**kwargs)`（无 `_load_poword()`、无 `output_name` 解析）。

**后果（若直接合入）**：
- ❌ 丢失 #157 的 `output_name` 自动解析能力；
- ❌ 把延迟加载退回为直接调用 `poword`，**回归「非 Windows 环境 `import office` 因缺 poword 而崩溃」的已知风险**（这正是之前引入 `_load_poword` 要修的）。

**要求**：**rebase 到最新 `develop` 后再合入**，将 `show_progress` 逻辑叠加在现有 `doc2docdocx`（含 `_load_poword()` + `output_name` 解析）之上，例如：
```python
def doc2docx(input_path, output_path=r'./', output_name=None, show_progress=True):
    if output_name is None and Path(output_path).suffix.lower() == ".docx":
        ...
    poword = _load_poword()
    kwargs = {'input_path': input_path, 'output_path': output_path, 'output_name': output_name}
    if not show_progress:
        kwargs['show_progress'] = False
    poword.doc2docx(**kwargs)
```

### 🟠 BLOCKER — 底层依赖 `poword#3` 未合并发布
**依赖链**：`office.word.doc2docx(show_progress=False)` → `poword.doc2docx(show_progress=False)`（需 poword#3 提供）

- 经核查，poword#3 页面仍为 `wants to merge ... into main` 措辞，**表明其处于 OPEN 状态、尚未合并到 `poword/main`，更未发布到 PyPI**。
- `setup.cfg` 对 poword 的约束为 `poword;platform_system=='Windows'`，**无版本下限**。
- **后果**：当前用户装到的 poword（旧版）`doc2docx` 大概率**不接受 `show_progress` 关键字**。本 PR 仅在 `show_progress=False` 时转发该键，因此：
  - 默认调用（`show_progress=True`，不转发该键）✅ 仍兼容所有版本；
  - 显式 `show_progress=False` ⚠️ 在旧版 poword 上极可能抛 `TypeError: unexpected keyword argument 'show_progress'`（除非旧版用 `**kwargs` 吞参，未验证）。
- **要求**：至少满足其一再合入：(a) 等待 poword#3 合并并发布，且在 `setup.cfg` 提高 poword 版本下限（如 `poword>=x.y.z;platform_system=='Windows'`）；或 (b) 在 `word.py` 内对 `show_progress=False` 做防御性转发（如先探测 poword 是否支持该参数，或对 `TypeError` 降级）。

### 🔵 实现质量（正面）
- `show_progress` 转发逻辑正确：默认不传键（兼容旧调用），仅 `False` 时传 `show_progress=False`。✅
- 用 `kwargs` 构建参数，清晰且易维护。✅
- `docstring` 与 `skills/word/doc2docx/SKILL.md` 同步更新（参数表 + 示例），文档一致性好。✅

### 📊 测试覆盖
**新增** `tests/test_code/test_word_api_parameters.py`：`load_word_api()` 动态加载 `word.py` 并 mock `poword`，验证：
- 默认调用 → `poword.doc2docx(input_path, output_path, output_name)`（不含 `show_progress`）✅
- `show_progress=False` → 含 `show_progress=False` ✅

覆盖到位，但**有缺口**：
- 测试基于 PR 改动后的 `doc2docx` 签名，未涉及 `output_name` 解析 + `show_progress` 的组合（rebase 到含 #157 的 develop 后建议补充，防止回归 #157 行为）；
- 白盒加载方式依赖 `word.py` 顶部无顶层 `import poword`（当前满足），rebase 后若引入新顶层 import 需同步调整 mock。

### 安全与高危调用
- 无硬编码凭据 / 密钥泄露 ✅
- 无 `panic()` / `os._exit()` 等高危调用 ✅
- 测试内 `print` 仅出现在 `if __name__ == "__main__":`，非生产路径 ✅

## 五、整体裁决

### 🟡 NEEDS ATTENTION（含两个 BLOCKER，合入前必须处理）

**合入前置条件（缺一不可）**：
1. **Rebase 到最新 `develop`**：解决与 #157 的冲突，保留 `output_name` 解析与 `_load_poword()` 延迟加载，将 `show_progress` 叠加其上（否则会覆盖已有功能并回归 import 崩溃）。
2. **落实底层依赖**：等待 `poword#3` 合并发布，并在 `setup.cfg` 设 poword 版本下限；或在 `word.py` 内做 `show_progress=False` 的防御性转发。

**次要建议**：
- 补充 `output_name` + `show_progress` 组合的单测；
- PR 描述已声明依赖 poword#3，建议在描述中标注其当前 OPEN 状态与预计合入节奏，便于维护者排期。

**优先级**：① rebase（阻断性，最高）→ ② 底层依赖落地 / 防御性转发 → ③ 测试补充。

---
*生成时间：2026-08-04 | 审查人：PR 代码审查专家（本地静态分析，未发布 GitHub 评论）*
