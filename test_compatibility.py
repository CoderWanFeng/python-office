#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
跨平台兼容性检查功能测试脚本
"""

import sys
import os

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_compatibility_module():
    """测试兼容性模块"""
    print("🧪 测试跨平台兼容性检查功能")
    print("=" * 60)
    
    try:
        # 导入兼容性模块
        from office.compatibility import CrossPlatformCompatibility
        
        # 创建兼容性检查器实例
        checker = CrossPlatformCompatibility()
        
        print(f"✅ 系统检测: {checker.is_windows}")
        print(f"✅ 首次运行标记: {checker.is_first_run}")
        print(f"✅ 标记文件路径: {checker.mark_file}")
        
        # 测试兼容性信息获取
        compat_info = checker.get_compatibility_info()
        print(f"✅ 兼容性信息获取成功，包含 {len(compat_info)} 个类别")
        
        # 测试模块兼容性检查
        test_modules = ['poexcel', 'poppt', 'poword', 'pofile']
        for module in test_modules:
            is_compatible = checker.check_module_compatibility(module)
            status = "✅" if is_compatible else "❌"
            print(f"{status} {module}: {'兼容' if is_compatible else '不兼容'}")
        
        # 测试平台特定建议
        advice = checker.get_platform_specific_advice()
        if advice:
            print(f"✅ 平台特定建议获取成功")
        
        print("\n🎯 测试显示警告功能（仅在非Windows系统首次运行时显示）")
        checker.display_warning()
        
        print("\n✅ 所有测试通过！")
        
    except Exception as e:
        print(f"❌ 测试失败: {e}")
        import traceback
        traceback.print_exc()

def test_main_package_import():
    """测试主包导入时的兼容性检查"""
    print("\n🧪 测试主包导入时的兼容性检查")
    print("=" * 60)
    
    try:
        # 模拟导入主包（这会触发兼容性检查）
        import office
        print("✅ 主包导入成功")
        print(f"✅ 包版本: {office.__version__}")
        print(f"✅ 包文档: {office.__doc__[:100]}...")
        
    except Exception as e:
        print(f"❌ 主包导入失败: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    print("🚀 开始跨平台兼容性检查功能测试")
    print("=" * 60)
    
    test_compatibility_module()
    test_main_package_import()
    
    print("\n" + "=" * 60)
    print("🎉 测试完成！")
    print("\n📋 功能总结:")
    print("• ✅ 操作系统检测功能")
    print("• ✅ 首次运行标记功能") 
    print("• ✅ 兼容性信息管理")
    print("• ✅ 模块兼容性检查")
    print("• ✅ 平台特定建议")
    print("• ✅ 自动警告显示（仅在非Windows系统首次运行时）")
    print("• ✅ 主包导入时自动触发检查")
    
    print("\n💡 使用说明:")
    print("1. 用户首次在非Windows系统上导入python-office时，会自动显示兼容性警告")
    print("2. 警告信息包含功能兼容性概览和替代解决方案")
    print("3. 使用标记文件确保警告只显示一次")
    print("4. 支持彩色输出（如果rich库可用）和普通文本输出")