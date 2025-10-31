#-*- coding:utf-8 -*-

#############################################
# File Name: Baidu_Text_transApi.py
# Author: 刘运超
# Mail: chaodreaming@gmail.com
# Created Time:  2022-5-23 14:45
# Description: 调用百度翻译接口进行翻译
#############################################
import requests
import random
from hashlib import md5
def make_md5(s: str, encoding: str = 'utf-8') -> str:
    """生成字符串的MD5哈希值。
    
    Args:
        s (str): 要哈希的字符串
        encoding (str, optional): 编码格式，默认为'utf-8'
        
    Returns:
        str: MD5哈希值
    """
    return md5(s.encode(encoding)).hexdigest()
def baidu_trans(query, from_lang, to_lang, appid, appkey):
    """调用百度翻译接口进行翻译。
    
    Args:
        query (str): 需要翻译的文本
        from_lang (str): 源语言代码
        to_lang (str): 目标语言代码
        appid (str): 百度翻译API的应用ID
        appkey (str): 百度翻译API的密钥
    
    Returns:
        str: 翻译后的文本
    """


    # For list of language codes, please refer to `https://api.fanyi.baidu.com/doc/21`
    # from_lang = 'en'
    # to_lang = 'zh'

    endpoint = 'http://api.fanyi.baidu.com'
    path = '/api/trans/vip/translate'
    url = endpoint + path

    # query = 'Hello World! This is 1st paragraph.\nThis is 2nd paragraph.'

    # Generate salt and sign

    salt = random.randint(32768, 65536)
    sign = make_md5(appid + query + str(salt) + appkey)

    # Build request
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'appid': appid, 'q': query, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}

    # Send request
    r = requests.post(url, params=payload, headers=headers)
    result = r.json()
    if len(result)==3:
        return result['trans_result'][0]['dst']
    else:
        return result

# if __name__ == '__main__':
#     # 百度官方通用翻译api
#     # 可参考这些链接申请 https://superdoctranslator.com/appidkey
#     # https://jingyan.baidu.com/article/3f16e00305bb552591c10304.html
#     appid = 'xxxxxxxxxxxxx'
#     appkey = 'xxxxxxxxxxxx'
#     res=baidu_trans("good","en","zh",appid,appkey)
#     print(res)