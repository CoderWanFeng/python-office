# PDF转Word GUI工具

一个基于PyQt5的PDF转Word转换桌面应用程序，提供简洁易用的图形界面。

## 功能特性

- ✅ 单个PDF文件转换
- ✅ 批量PDF文件转换
- ✅ 拖拽文件支持
- ✅ 实时转换进度显示
- ✅ 自定义输出路径
- ✅ 转换结果反馈

## 系统要求

- Python 3.6+
- Windows/Linux/Mac OS

## 安装依赖

```bash
pip install -r requirements.txt
```

## 使用方法

### 启动应用

```bash
cd gui/pdf2word
python main.py
```

### 基本操作

1. **添加文件**
   - 点击"选择PDF文件"按钮选择单个文件
   - 点击"批量选择"按钮选择多个文件
   - 直接拖拽PDF文件到窗口

2. **设置输出路径**
   - 在输出路径框中输入目录路径
   - 点击"浏览..."按钮选择目录
   - 留空则使用源文件所在目录

3. **开始转换**
   - 点击"开始转换"按钮
   - 查看实时转换进度
   - 等待转换完成提示

4. **管理文件列表**
   - 右键点击文件可删除
   - 点击"清空列表"清除所有文件

## 文件状态说明

| 状态 | 颜色 | 说明 |
|------|------|------|
| 等待 | 灰色 | 文件等待转换 |
| 转换中 | 蓝色 | 文件正在转换 |
| 成功 | 绿色 | 转换成功 |
| 失败 | 红色 | 转换失败，查看错误信息 |

## 技术架构

本应用采用MVC架构模式：

- **Model (模型层)**: `models/converter.py` - 封装PDF转Word转换逻辑
- **View (视图层)**: `views/main_window.py` - 提供图形界面
- **Controller (控制层)**: `controllers/converter_controller.py` - 协调模型和视图

## 项目结构

```
pdf2word/
├── models/              # 业务逻辑层
│   ├── __init__.py
│   └── converter.py     # PDF转换核心
├── views/               # 界面视图层
│   ├── __init__.py
│   └── main_window.py   # 主窗口
├── controllers/         # 控制器层
│   ├── __init__.py
│   └── converter_controller.py  # 转换控制器
├── utils/               # 工具模块
│   ├── __init__.py
│   └── file_manager.py  # 文件管理器
├── main.py              # 应用程序入口
├── requirements.txt     # 依赖清单
└── README.md            # 说明文档
```

## 注意事项

1. 确保安装了所有依赖库
2. PDF文件需要有读取权限
3. 输出目录需要有写入权限
4. 大文件转换可能需要较长时间

## 常见问题

**Q: 转换失败怎么办？**
A: 检查PDF文件是否损坏，确保有足够的磁盘空间和权限。

**Q: 支持加密的PDF吗？**
A: 目前不支持加密的PDF文件，请先解密后再转换。

**Q: 转换速度慢怎么办？**
A: PDF转Word转换是计算密集型操作，大文件需要较长时间，请耐心等待。

## 开发者

本工具基于 [python-office](https://github.com/CoderWanFeng/python-office) 项目开发。

## 许可证

本项目遵循 python-office 项目的许可证。
# PDF转Word GUI工具

一个基于PyQt5的PDF转Word转换桌面应用程序，提供简洁易用的图形界面。

## 功能特性

- ✅ 单个PDF文件转换
- ✅ 批量PDF文件转换
- ✅ 拖拽文件支持
- ✅ 实时转换进度显示
- ✅ 自定义输出路径
- ✅ 转换结果反馈

## 系统要求

- Python 3.6+
- Windows/Linux/Mac OS

## 安装依赖

```bash
pip install -r requirements.txt
```

## 使用方法

### 启动应用

```bash
cd gui/pdf2word
python main.py
```

### 基本操作

1. **添加文件**
   - 点击"选择PDF文件"按钮选择单个文件
   - 点击"批量选择"按钮选择多个文件
   - 直接拖拽PDF文件到窗口

2. **设置输出路径**
   - 在输出路径框中输入目录路径
   - 点击"浏览..."按钮选择目录
   - 留空则使用源文件所在目录

3. **开始转换**
   - 点击"开始转换"按钮
   - 查看实时转换进度
   - 等待转换完成提示

4. **管理文件列表**
   - 右键点击文件可删除
   - 点击"清空列表"清除所有文件

## 文件状态说明

| 状态 | 颜色 | 说明 |
|------|------|------|
| 等待 | 灰色 | 文件等待转换 |
| 转换中 | 蓝色 | 文件正在转换 |
| 成功 | 绿色 | 转换成功 |
| 失败 | 红色 | 转换失败，查看错误信息 |

## 技术架构

本应用采用MVC架构模式：

- **Model (模型层)**: `models/converter.py` - 封装PDF转Word转换逻辑
- **View (视图层)**: `views/main_window.py` - 提供图形界面
- **Controller (控制层)**: `controllers/converter_controller.py` - 协调模型和视图

## 项目结构

```
pdf2word/
├── models/              # 业务逻辑层
│   ├── __init__.py
│   └── converter.py     # PDF转换核心
├── views/               # 界面视图层
│   ├── __init__.py
│   └── main_window.py   # 主窗口
├── controllers/         # 控制器层
│   ├── __init__.py
│   └── converter_controller.py  # 转换控制器
├── utils/               # 工具模块
│   ├── __init__.py
│   └── file_manager.py  # 文件管理器
├── main.py              # 应用程序入口
├── requirements.txt     # 依赖清单
└── README.md            # 说明文档
```

## 注意事项

1. 确保安装了所有依赖库
2. PDF文件需要有读取权限
3. 输出目录需要有写入权限
4. 大文件转换可能需要较长时间

## 常见问题

**Q: 转换失败怎么办？**
A: 检查PDF文件是否损坏，确保有足够的磁盘空间和权限。

**Q: 支持加密的PDF吗？**
A: 目前不支持加密的PDF文件，请先解密后再转换。

**Q: 转换速度慢怎么办？**
A: PDF转Word转换是计算密集型操作，大文件需要较长时间，请耐心等待。

## 开发者

本工具基于 [python-office](https://github.com/CoderWanFeng/python-office) 项目开发。

## 许可证

本项目遵循 python-office 项目的许可证。
