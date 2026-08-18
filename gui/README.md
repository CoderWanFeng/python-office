# python-office Windows GUI

这是一个面向普通办公用户的 `python-office` 图形界面入口，基于 PySide6 构建。

它保留 CLI 的自动化能力，同时把常用功能整理成可点击、可填写、可查看日志的桌面窗口。对不熟悉命令行的用户来说，可以直接选择文件、填写参数并点击运行。

## 主要特点

- 左侧按模块展示功能，右侧按需生成参数表单
- 启动时默认折叠左侧分类，减少界面干扰
- 参数通过 `inspect.signature` 反射生成，并在打开功能页时懒加载
- 使用 `QThread` 执行业务函数，避免界面卡死
- 运行日志集中显示，方便截图和排错
- 对必须 CLI 交互的功能显示命令提示，不在 GUI 中直接执行
- 附带 Nuitka 目录模式打包脚本，方便生成离线运行版本

## 安装依赖

```bash
pip install PySide6
```

如需打包 Windows 离线版本，还需要安装 Nuitka：

```bash
pip install nuitka
```

## 启动方式

在项目根目录运行：

```bash
python -m gui
```

也可以使用：

```bash
python -m gui.run
```

## 打包方式

Windows PowerShell 中运行：

```powershell
.\scripts\build-gui-nuitka.ps1
```

脚本会使用 Nuitka 目录模式生成 `dist-nuitka/run.dist`，并复制运行所需依赖，方便离线使用。

## 目录结构

```text
gui/
├── __main__.py
├── app.py
├── run.py
├── main_window.py
├── panels.py
├── registry.py
├── styles.py
├── workers.py
├── assets/
├── widgets/
└── tests/
```

## 当前重点场景

试用反馈中，PDF 转 Word 和 PDF 合并是最受欢迎的功能。GUI 版本重点降低这些高频办公能力的使用门槛，让用户不用记命令，也不用提前配置复杂环境。
