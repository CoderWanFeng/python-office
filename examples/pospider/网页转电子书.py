# -*- coding: utf-8 -*-
"""
网页转电子书功能演示
作者：程序员晚枫
项目官网：https://www.python-office.com
"""

import office

def url_to_ebook_demo():
    """
    演示如何将网页内容转换为电子书
    """
    print("🌐 网页转电子书功能演示 - 程序员晚枫")
    print("=" * 50)
    
    # 示例URL（使用python-office官网）
    sample_url = "https://www.python-office.com"
    ebook_title = "Python-Office自动化办公指南"
    
    print(f"📋 转换信息：")
    print(f"   网页URL：{sample_url}")
    print(f"   电子书标题：{ebook_title}")
    
    print("\n🚀 开始转换...")
    
    try:
        # 执行网页转电子书
        office.web.url2ebook(
            url=sample_url,
            tile=ebook_title
        )
        print("✅ 网页转电子书转换成功！")
        
    except Exception as e:
        print(f"❌ 转换失败：{e}")
        print("💡 提示：请检查网络连接和URL有效性")
    
    print("\n💡 功能特点：")
    print("• 支持多种网页格式转换")
    print("• 自动提取网页主要内容")
    print("• 生成标准电子书格式")
    
    print("\n📚 适用场景：")
    print("• 技术文档归档")
    print("• 学习资料整理")
    print("• 网页内容离线阅读")
    
    print("\n🔗 相关资源：")
    print("• 项目官网：https://www.python-office.com")
    print("• 交流群：http://www.python4office.cn/wechat-group")
    print("• 开发者：程序员晚枫")

if __name__ == "__main__":
    url_to_ebook_demo()