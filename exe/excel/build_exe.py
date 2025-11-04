#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
打包脚本 - 将 fake2excel.py 打包成可执行文件
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def check_pyinstaller():
    """检查是否安装了 PyInstaller"""
    try:
        import PyInstaller
        print("✓ PyInstaller 已安装")
        return True
    except ImportError:
        print("❌ PyInstaller 未安装，正在安装...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
            print("✓ PyInstaller 安装成功")
            return True
        except subprocess.CalledProcessError:
            print("❌ PyInstaller 安装失败")
            return False

def create_spec_file():
    """创建 PyInstaller spec 文件"""
    spec_content = """# -*- mode: python ; coding: utf-8 -*-

import sys
from PyInstaller.utils.hooks import collect_data_files, collect_submodules
from PyInstaller.utils.hooks import logger

block_cipher = None

a = Analysis(
    ['fake2excel.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[
        'office.api.excel',
        'PySide6',
        'PySide6.QtCore',
        'PySide6.QtGui', 
        'PySide6.QtWidgets',
        'PySide6.QtNetwork',
        'PySide6.QtOpenGL',
        'PySide6.QtOpenGLWidgets',
        'PySide6.QtPrintSupport',
        'PySide6.QtQml',
        'PySide6.QtQuick',
        'PySide6.QtSvg',
        'PySide6.QtUiTools',
        'PySide6.QtXml',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

# 添加 PySide6 相关文件
pyside6_data = collect_data_files('PySide6')
for data in pyside6_data:
    a.datas.append(data)

# 添加 office 相关模块
for module in ['office', 'office.api', 'office.api.excel']:
    try:
        hidden_imports = collect_submodules(module)
        for imp in hidden_imports:
            a.hiddenimports.append(imp)
    except Exception as e:
        logger.warning(f"Failed to collect submodules for {module}: {e}")

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='fake2excel',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # 设置为 False 以隐藏控制台窗口
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
"""
    
    with open('fake2excel.spec', 'w', encoding='utf-8') as f:
        f.write(spec_content)
    print("✓ Spec 文件创建成功")

def build_executable():
    """构建可执行文件"""
    print("🚀 开始构建可执行文件...")
    
    # 使用 PyInstaller 构建
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "fake2excel.spec",
        "--noconfirm",  # 不确认覆盖
        "--clean",      # 清理临时文件
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=os.getcwd())
        
        if result.returncode == 0:
            print("✓ 可执行文件构建成功！")
            
            # 检查生成的文件
            dist_dir = Path("dist")
            if dist_dir.exists():
                exe_files = list(dist_dir.glob("fake2excel*.exe"))
                if exe_files:
                    exe_file = exe_files[0]
                    print(f"📁 生成的可执行文件: {exe_file}")
                    
                    # 复制到当前目录
                    shutil.copy2(exe_file, ".")
                    print("✓ 可执行文件已复制到当前目录")
                    
                    # 显示文件大小
                    size_mb = exe_file.stat().st_size / (1024 * 1024)
                    print(f"📊 文件大小: {size_mb:.2f} MB")
                    
                    return True
                else:
                    print("❌ 未找到生成的可执行文件")
                    return False
            else:
                print("❌ dist 目录不存在")
                return False
                
        else:
            print("❌ 构建失败:")
            print("STDOUT:", result.stdout)
            print("STDERR:", result.stderr)
            return False
            
    except Exception as e:
        print(f"❌ 构建过程中出错: {e}")
        return False

def cleanup():
    """清理临时文件"""
    temp_dirs = ["build", "dist", "__pycache__"]
    temp_files = ["fake2excel.spec"]
    
    for dir_name in temp_dirs:
        dir_path = Path(dir_name)
        if dir_path.exists():
            shutil.rmtree(dir_path)
            print(f"🗑️  已清理目录: {dir_name}")
    
    for file_name in temp_files:
        file_path = Path(file_name)
        if file_path.exists():
            file_path.unlink()
            print(f"🗑️  已清理文件: {file_name}")

def main():
    """主函数"""
    print("=" * 60)
    print("📦 Excel数据模拟器 - 打包工具")
    print("=" * 60)
    
    # 检查当前目录
    current_dir = Path(__file__).parent
    os.chdir(current_dir)
    print(f"📁 工作目录: {current_dir}")
    
    # 检查源文件是否存在
    if not Path("fake2excel.py").exists():
        print("❌ fake2excel.py 文件不存在")
        return
    
    # 检查 PyInstaller
    if not check_pyinstaller():
        return
    
    # 创建 spec 文件
    create_spec_file()
    
    # 构建可执行文件
    if build_executable():
        print("\n🎉 打包完成！")
        print("✅ 可执行文件已生成在当前目录")
        print("✅ 临时文件已自动清理")
    else:
        print("\n❌ 打包失败")
    
    # 清理临时文件
    cleanup()
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()