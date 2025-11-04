#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
简化版打包脚本
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def build_with_pyinstaller():
    """使用 PyInstaller 直接打包"""
    print("🚀 开始打包 fake2excel.py...")
    
    # 使用 PyInstaller 直接打包
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "fake2excel.py",
        "--onefile",           # 打包成单个文件
        "--noconsole",         # 不显示控制台窗口
        "--name", "fake2excel", # 输出文件名
        "--clean",             # 清理临时文件
        "--noconfirm",         # 不确认覆盖
        "--hidden-import=office.api.excel",
        "--hidden-import=PySide6",
        "--hidden-import=PySide6.QtCore",
        "--hidden-import=PySide6.QtGui",
        "--hidden-import=PySide6.QtWidgets",
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=os.getcwd())
        
        if result.returncode == 0:
            print("✓ 打包成功！")
            
            # 检查生成的文件
            dist_dir = Path("dist")
            if dist_dir.exists():
                exe_file = dist_dir / "fake2excel.exe"
                if exe_file.exists():
                    # 复制到当前目录
                    shutil.copy2(exe_file, ".")
                    print(f"✓ 可执行文件已生成: {exe_file.name}")
                    
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
            print("❌ 打包失败:")
            print("STDOUT:", result.stdout)
            print("STDERR:", result.stderr)
            return False
            
    except Exception as e:
        print(f"❌ 打包过程中出错: {e}")
        return False

def cleanup():
    """清理临时文件"""
    temp_dirs = ["build", "dist", "__pycache__"]
    
    for dir_name in temp_dirs:
        dir_path = Path(dir_name)
        if dir_path.exists():
            try:
                shutil.rmtree(dir_path)
                print(f"🗑️  已清理目录: {dir_name}")
            except Exception as e:
                print(f"⚠️  清理 {dir_name} 失败: {e}")

def main():
    """主函数"""
    print("=" * 60)
    print("📦 Excel数据模拟器 - 简化打包工具")
    print("=" * 60)
    
    # 检查当前目录
    current_dir = Path(__file__).parent
    os.chdir(current_dir)
    print(f"📁 工作目录: {current_dir}")
    
    # 检查源文件是否存在
    if not Path("fake2excel.py").exists():
        print("❌ fake2excel.py 文件不存在")
        return
    
    # 打包
    if build_with_pyinstaller():
        print("\n🎉 打包完成！")
        print("✅ 可执行文件已生成在当前目录")
    else:
        print("\n❌ 打包失败")
    
    # 清理临时文件
    cleanup()
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()