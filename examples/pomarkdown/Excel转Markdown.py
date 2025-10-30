# -*- coding: utf-8 -*-
"""
Excel转Markdown功能演示
作者：程序员晚枫
项目官网：https://www.python-office.com
"""

import office
import os

def excel_to_markdown_demo():
    """
    演示如何将Excel文件转换为Markdown格式
    """
    print("📊 Excel转Markdown功能演示 - 程序员晚枫")
    print("=" * 50)
    
    # 创建示例Excel文件（如果不存在）
    sample_excel = "sample_data.xlsx"
    
    # 检查是否需要创建示例文件
    if not os.path.exists(sample_excel):
        print("📝 创建示例Excel文件...")
        
        # 使用python-office创建示例Excel
        office.excel.save_as(
            file_path=sample_excel,
            sheets={
                "员工信息": [
                    ["姓名", "部门", "工资", "入职时间"],
                    ["张三", "技术部", 15000, "2020-01-15"],
                    ["李四", "市场部", 12000, "2019-08-20"],
                    ["王五", "人事部", 10000, "2021-03-10"]
                ],
                "项目统计": [
                    ["项目名称", "负责人", "进度", "预算"],
                    ["OA系统开发", "张三", "80%", 500000],
                    ["官网改版", "李四", "60%", 200000],
                    ["移动端App", "王五", "30%", 300000]
                ]
            }
        )
        print(f"✅ 示例文件已创建：{sample_excel}")
    
    # 输出文件路径
    output_md = "converted_data.md"
    
    print(f"\n📋 转换信息：")
    print(f"   输入文件：{sample_excel}")
    print(f"   输出文件：{output_md}")
    
    # 执行转换
    try:
        office.markdown.excel2markdown(
            input_file=sample_excel,
            output_file=output_md
        )
        print("✅ Excel转Markdown转换成功！")
        
        # 显示转换后的内容预览
        if os.path.exists(output_md):
            print("\n📄 转换结果预览：")
            with open(output_md, 'r', encoding='utf-8') as f:
                content = f.read()
                print(content[:500] + "..." if len(content) > 500 else content)
        
    except Exception as e:
        print(f"❌ 转换失败：{e}")
    
    print("\n💡 功能特点：")
    print("• 支持多工作表转换")
    print("• 自动生成Markdown表格格式")
    print("• 保持数据结构和格式")
    
    print("\n🔗 相关资源：")
    print("• 项目官网：https://www.python-office.com")
    print("• 视频教程：https://space.bilibili.com/259649365")
    print("• 开发者：程序员晚枫")

if __name__ == "__main__":
    excel_to_markdown_demo()