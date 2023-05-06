# mail_sent模块

参数如下

    :param _sender: 必填，字符串，服务邮件账号
    :param _passwd: 必填，字符串，服务邮件密码
    :param receiver: 必填，列表，发送邮件目的地
    :param content: 默认空，字符串，发送文本
    :param subject: 默认空，字符串，邮件主题
    :param files: 可选，列表，发送附件时候使用，支持多文件
    :param types: 默认’plain‘，字符串，邮件发送类型，常见类型：'plain'常用文本, 'html'超文本
    :param log_options: 默认False，布尔值
    :param host: 邮件服务器地址
    :return:

**main.py**
```python
import mail_sent

_sender = '*******@outlook.com'  # 邮箱账号
_passwd = '******'  # 邮箱账号密码
receiver = ['******']  # 多个收件人放在一个list里面  # 接收邮箱
text = '''
文本内容（可根据send_mail的types参数发送内容为html或者正常文本内容）
'''

mail_sent.send_mail(_sender, _passwd, receiver, content=text, subject='青年大学习完成名单情况(测试)', types='plain')
```

> 邮件发送模块  
> 由于outlook邮箱发送和其他国内邮箱有些不一样，目前仅支持outlook邮箱，后续添加跟多邮箱

编程菜鸟，如有不足请指正
