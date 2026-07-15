# -*- coding: utf-8 -*-
"""
跨平台兼容性检查模块
当检测到用户在非Windows系统上首次运行时，提供兼容性提示
"""

import os
import sys
import platform
from pathlib import Path
from typing import Dict, List


class CrossPlatformCompatibility:
    """跨平台兼容性检查器。"""
    
    def __init__(self):
        self.is_windows = platform.system() == 'Windows'
        self.is_macos = platform.system() == 'Darwin'
        self.is_linux = platform.system() == 'Linux'
        self.mark_file = Path.home() / '.python-office' / 'first_run_mark'
        self.is_first_run = self._check_first_run()
    
    def _check_first_run(self) -> bool:
        """检查是否是首次运行。
        
        Returns:
            bool: 如果是首次运行返回True，否则返回False
        """
        try:
            # 创建标记目录
            self.mark_file.parent.mkdir(exist_ok=True)
            
            # 如果标记文件不存在，则是首次运行
            if not self.mark_file.exists():
                # 创建标记文件
                self.mark_file.write_text(f"First run on {platform.system()} at {platform.platform()}")
                return True
        except OSError:
            # 兼容性提示不应影响主包导入；HOME 只读或不可写时跳过首次运行提示。
            return False
        return False
    
    def get_compatibility_info(self) -> Dict[str, List[str]]:
        """获取兼容性信息。
        
        Returns:
            Dict[str, List[str]]: 包含兼容性信息的字典
        """
        return {
            "fully_supported": [
                "Excel处理 (poexcel)",
                "PDF处理 (popdf)", 
                "图片处理 (poimage)",
                "文件管理 (pofile)",
                "邮件发送 (poemail)",
                "OCR识别 (poocr)",
                "视频处理 (povideo)",
                "进度条工具 (poprogress)",
                "代码管理 (pocode)",
                "Markdown处理 (pomarkdown)",
                "网络爬虫 (pospider)"
            ],
            "windows_only": [
                "PPT处理 (poppt) - 需要Microsoft PowerPoint",
                "Word处理 (poword) - 需要Microsoft Word",
                "微信机器人 (PyOfficeRobot) - 需要桌面微信客户端",
                "文件搜索 (search4file) - 使用Windows特定API"
            ],
            "workarounds": [
                "PPT处理: 可以使用LibreOffice或在线转换工具",
                "Word处理: 可以使用LibreOffice Writer或Google Docs",
                "微信机器人: 可以使用网页版微信API或第三方机器人框架",
                "文件搜索: 可以使用系统自带的搜索工具或find命令"
            ]
        }
    
    def display_warning(self):
        """显示兼容性警告信息。"""
        if self.is_windows:
            return  # Windows系统不需要警告
        
        if not self.is_first_run:
            return  # 非首次运行不需要重复显示
        
        compat_info = self.get_compatibility_info()
        
        # 使用rich库进行彩色输出（如果可用）
        try:
            from rich.console import Console
            from rich.panel import Panel
            from rich.table import Table
            from rich.text import Text
            from rich import print as rprint
            
            console = Console()
            
            # 标题
            title = Text("⚠️ Python-Office 跨平台兼容性提示", style="bold red")
            
            # 创建兼容性表格
            table = Table(title="功能兼容性概览", show_header=True, header_style="bold magenta")
            table.add_column("状态", style="cyan", width=12)
            table.add_column("功能模块", style="white")
            
            # 添加完全支持的功能
            for func in compat_info["fully_supported"]:
                table.add_row("✅ 完全支持", func)
            
            # 添加仅Windows支持的功能
            for func in compat_info["windows_only"]:
                table.add_row("❌ 仅Windows", func)
            
            # 创建解决方案表格
            solution_table = Table(title="替代解决方案", show_header=True, header_style="bold green")
            solution_table.add_column("Windows功能", style="yellow")
            solution_table.add_column("替代方案", style="white")
            
            for workaround in compat_info["workarounds"]:
                parts = workaround.split(": ")
                if len(parts) == 2:
                    solution_table.add_row(parts[0], parts[1])
            
            # 输出面板
            console.print(Panel(
                title,
                style="bright_yellow",
                width=80
            ))
            
            console.print(f"\n📋 检测到您正在使用: {platform.system()} {platform.release()}")
            console.print("💡 这是您首次在此系统上运行python-office库\n")
            
            console.print(table)
            console.print("\n")
            console.print(solution_table)
            
            # 资源链接
            resources_text = Text("\n🔗 相关资源链接:")
            resources_text.append("\n• 官方文档: https://www.python-office.com")
            resources_text.append("\n• 问题反馈: https://github.com/CoderWanFeng/python-office/issues")
            resources_text.append("\n• 交流群: https://www.python4office.cn/wechat-group")
            
            console.print(Panel(
                resources_text,
                title="💬 获取帮助",
                style="blue"
            ))
            
        except ImportError:
            # 如果rich不可用，使用普通输出
            self._display_plain_warning(compat_info)
    
    def _display_plain_warning(self, compat_info: Dict[str, List[str]]):
        """使用普通文本显示警告。
        
        Args:
            compat_info (Dict[str, List[str]]): 兼容性信息字典
        """
        print("=" * 80)
        print("⚠️  Python-Office 跨平台兼容性提示")
        print("=" * 80)
        print(f"\n📋 检测到您正在使用: {platform.system()} {platform.release()}")
        print("💡 这是您首次在此系统上运行python-office库\n")
        
        print("📊 功能兼容性概览:")
        print("-" * 40)
        
        print("\n✅ 完全支持的功能:")
        for func in compat_info["fully_supported"]:
            print(f"   • {func}")
        
        print("\n❌ 仅Windows支持的功能:")
        for func in compat_info["windows_only"]:
            print(f"   • {func}")
        
        print("\n🛠️ 替代解决方案:")
        print("-" * 40)
        for workaround in compat_info["workarounds"]:
            print(f"   • {workaround}")
        
        print("\n🔗 相关资源链接:")
        print("-" * 40)
        print("   • 官方文档: https://www.python-office.com")
        print("   • 问题反馈: https://github.com/CoderWanFeng/python-office/issues")
        print("   • 交流群: https://www.python4office.cn/wechat-group")
        print("\n" + "=" * 80)
    
    def check_module_compatibility(self, module_name: str) -> bool:
        """检查特定模块的兼容性。
        
        Args:
            module_name (str): 模块名称
        
        Returns:
            bool: 如果模块兼容返回True，否则返回False
        """
        windows_only_modules = {
            'poppt', 'poword', 'search4file', 'PyOfficeRobot',
            'ppt', 'word', 'wechat'
        }
        
        if module_name in windows_only_modules and not self.is_windows:
            return False
        return True
    
    def get_platform_specific_advice(self) -> str:
        """获取平台特定的建议。
        
        Returns:
            str: 平台特定的建议信息
        """
        if self.is_macos:
            return """
💻 macOS 用户建议:
• 可以使用Homebrew安装LibreOffice: brew install --cask libreoffice
• 对于Office文件处理，可以考虑使用在线转换服务
• 微信机器人功能需要使用网页版微信API替代
"""
        elif self.is_linux:
            return """
🐧 Linux 用户建议:
• 可以使用包管理器安装LibreOffice: sudo apt install libreoffice (Ubuntu/Debian)
• 对于批量文件处理，可以使用shell脚本配合python-office的跨平台功能
• 微信机器人功能需要使用网页版微信API或第三方框架
"""
        else:
            return ""


def check_compatibility():
    """检查兼容性的主函数。
    
    Returns:
        CrossPlatformCompatibility: 兼容性检查器实例
    """
    checker = CrossPlatformCompatibility()
    checker.display_warning()
    return checker


if __name__ == "__main__":
    # 测试代码
    checker = CrossPlatformCompatibility()
    print(f"系统: {platform.system()}")
    print(f"首次运行: {checker.is_first_run}")
    print(f"标记文件: {checker.mark_file}")
    
    # 显示警告（仅在非Windows且首次运行时）
    checker.display_warning()
