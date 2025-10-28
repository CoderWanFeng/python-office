# -*- coding: utf-8 -*-
"""
测试API功能演示
作者：程序员晚枫
项目官网：https://www.python-office.com
"""

import office
import os
import json

def create_test_files(test_dir):
    """创建测试所需的文件"""
    # 创建测试图片文件
    with open(os.path.join(test_dir, "image1.jpg"), 'w') as f:
        f.write("# 模拟图片文件")
    with open(os.path.join(test_dir, "image2.jpg"), 'w') as f:
        f.write("# 模拟图片文件")
    
    # 创建XML标注文件（只标注image1）
    xml_content = """<?xml version="1.0" ?>
<annotation>
    <object>
        <name>person</name>
        <bndbox>
            <xmin>100</xmin>
            <ymin>100</ymin>
            <xmax>200</xmax>
            <ymax>200</ymax>
        </bndbox>
    </object>
</annotation>"""
    with open(os.path.join(test_dir, "image1.xml"), 'w', encoding='utf-8') as f:
        f.write(xml_content)
    
    # 创建JSON标注文件
    json_content = {
        "shapes": [
            {
                "label": "car",
                "points": [[100, 100], [200, 200]]
            }
        ]
    }
    with open(os.path.join(test_dir, "labeled.json"), 'w', encoding='utf-8') as f:
        json.dump(json_content, f, ensure_ascii=False)
    
    # 创建无标签的JSON文件
    empty_json = {"shapes": []}
    with open(os.path.join(test_dir, "empty.json"), 'w', encoding='utf-8') as f:
        json.dump(empty_json, f, ensure_ascii=False)

def ruiming_api_demo():
    """
    演示测试API功能
    """
    print("🧪 测试API功能演示 - 程序员晚枫")
    print("=" * 50)
    
    # 创建测试目录
    test_dir = "test_images"
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)
        print(f"✅ 创建测试目录：{test_dir}")
    
    # 创建测试文件
    print("📁 创建测试文件...")
    create_test_files(test_dir)
    print("✅ 测试文件创建完成")
    
    # 1. 筛选无标记图片
    print("\n🖼️ 筛选无标记图片演示：")
    print(f"   测试目录：{test_dir}")
    
    try:
        office.ruiming.screen_unmarked_image(dir_path=test_dir)
        print("   ✅ 无标记图片筛选完成")
        print("   💡 功能说明：自动识别并筛选没有标记的图片文件")
        print("   📊 结果：image2.jpg 被移动到'未标注图片'文件夹")
    except Exception as e:
        print(f"   ❌ 功能执行失败：{e}")
    
    # 2. 修改XML标签
    print("\n📝 修改XML标签演示：")
    old_label = "person"
    new_label = "human"
    
    try:
        office.ruiming.change_label_in_xml(
            dir_path=test_dir,
            old_label=old_label,
            new_label=new_label
        )
        print(f"   ✅ XML标签修改完成")
        print(f"   旧标签：{old_label} → 新标签：{new_label}")
        print("   💡 功能说明：批量修改XML文件中的标签名称")
    except Exception as e:
        print(f"   ❌ 功能执行失败：{e}")
    
    # 3. 筛选无标签JSON文件
    print("\n📄 筛选无标签JSON文件演示：")
    
    try:
        office.ruiming.screen_without_label_json_file(dir_path=test_dir)
        print("   ✅ 无标签JSON文件筛选完成")
        print("   💡 功能说明：识别并筛选没有标签的JSON文件")
        print("   📊 结果：empty.json 被移动到'无标签json文件'文件夹")
    except Exception as e:
        print(f"   ❌ 功能执行失败：{e}")
    
    print("\n💡 功能特点：")
    print("• 图片处理：自动识别无标记图片")
    print("• XML操作：批量修改标签内容")
    print("• JSON处理：智能筛选文件")
    print("• 批量操作：支持目录级处理")
    
    print("\n🎯 适用场景：")
    print("• 机器学习数据预处理")
    print("• 图像识别项目数据整理")
    print("• 自动化测试数据管理")
    print("• 批量文件格式转换")
    
    print("\n🔗 相关资源：")
    print("• 项目官网：https://www.python-office.com")
    print("• 开发者博客：http://www.python4office.cn")
    print("• 交流群：http://www.python4office.cn/wechat-group")
    print("• 开发者：程序员晚枫")
    
    print("\n📌 注意事项：")
    print("• 需要特定的文件格式支持（JPG图片、XML标注、JSON标注）")
    print("• 文件命名需要对应（image.jpg 对应 image.xml）")
    print("• 功能主要用于机器学习数据预处理")

if __name__ == "__main__":
    ruiming_api_demo()