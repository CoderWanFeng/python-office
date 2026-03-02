# -*- coding: utf-8 -*-
"""Email sending functionality demonstration.

Author:
    程序员晚枫

Project:
    https://www.python-office.com
"""

import office

# 发送邮件示例
def send_email_demo():
    """Demonstrate how to send emails using python-office.
    
    Note: SMTP service configuration is required for email functionality.
    This example shows the code structure with placeholder values that need
    to be replaced with actual email credentials before use.
    
    Returns:
        None
    """
    print("📧 邮件发送功能演示 - 程序员晚枫")
    print("=" * 50)
    
    # 由于邮件功能需要配置SMTP，这里只展示代码结构
    # 实际使用时需要填写真实的邮箱配置
    
    # 示例配置（需要替换为真实信息）
    key = "your_email_password"  # 邮箱授权码
    msg_from = "your_email@qq.com"  # 发件人邮箱
    msg_to = "recipient@example.com"  # 收件人邮箱
    msg_subject = "来自python-office的测试邮件"
    content = """
    这是一封来自python-office库的测试邮件。
    
    项目由程序员晚枫开发，致力于Python自动化办公。
    更多功能请访问：https://www.python-office.com
    
    祝使用愉快！
    """
    
    print("📝 邮件配置信息：")
    print(f"   发件人：{msg_from}")
    print(f"   收件人：{msg_to}")
    print(f"   主题：{msg_subject}")
    print(f"   内容：{content[:100]}...")
    
    print("\n💡 使用说明：")
    print("1. 需要先配置邮箱的SMTP服务")
    print("2. 获取邮箱授权码（非登录密码）")
    print("3. 取消注释下面的代码并填写真实信息")
    
    # 实际发送代码（需要取消注释并配置真实信息）
    """
    try:
        office.email.send_email(
            key=key,
            msg_from=msg_from,
            msg_to=msg_to,
            msg_subject=msg_subject,
            content=content
        )
        print("✅ 邮件发送成功！")
    except Exception as e:
        print(f"❌ 邮件发送失败：{e}")
    """
    
    print("\n🔗 相关资源：")
    print("• 项目官网：https://www.python-office.com")
    print("• 交流群：https://www.python4office.cn/wechat-group")
    print("• 开发者：程序员晚枫")

if __name__ == "__main__":
    send_email_demo()