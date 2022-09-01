from datetime import datetime
# import traceback
from functools import wraps


# 统一的异常输出
def except_dec(msg='异常原因'):
    # msg用于自定义函数的提示信息
    def except_execute(func):
        @wraps(func)
        def execept_print(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                sign = '=' * 60 + '\n'
                print(f'{sign}>>>异常时间：\t{datetime.now()}\n>>>异常函数：\t{func.__name__}\n>>>{msg}：\t{e}\n>>>异常反馈：\thttp://www.python4office.cn/wechat-group/')

                print(f'{sign}')
                # print(f'{sign}{traceback.format_exc()}{sign}')

        return execept_print

    return except_execute

@except_dec()
def lig(a = 5,b = 0):
    print(a/b)
lig()