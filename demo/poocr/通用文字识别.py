# -*- coding: UTF-8 -*-
'''
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@微信     ：CoderWanFeng : https://mp.weixin.qq.com/s/B1V6KeXc7IOEB8DgXLWv3g
@个人网站      ：www.python-office.com
@代码日期    ：2023/7/25 22:52 
@本段代码的视频说明     ：
'''
# pip install poocr
import poocr

# 获取id和key的地址：https://cloud.tencent.com/act/cps/redirect?redirect=36394&cps_key=ca76be5a2293ba3906d6d5407aea15ee
id = '获取方式👆'
key = '获取方式👆'

# 全部功能 的文档：https://mp.weixin.qq.com/s/WxICBZZSgkm-OrvXB82hbg
result = poocr.ocr.GeneralBasicOCR(
    # 可以填写本地图片的地址：img_path，也可以填写在线图片的地址：img_url ，如果2个都填，则只用在线图片img_url
    img_path=r'D:\workplace\code\程序员晚枫\全网同名\普通照片.jpg',
    id=id, key=key)
print(result)  # 输出json格式的识别结果
