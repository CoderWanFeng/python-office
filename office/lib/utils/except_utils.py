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
                print('*' * 20 + "{}".format('糟糕，你的程序出现了异常') + '*' * 20)
                print(
                    f'>>>异常时间：\t{datetime.now()}\n>>>异常函数：\t{func.__name__}\n>>>{msg}：\t{e}')

                print('*' * 20 + "{}".format('别慌，你的异常我来解决→http://t.cn/A6XVQXAk') + '*' * 20)

                # print(f'{sign}{traceback.format_exc()}{sign}')

        return execept_print

    return except_execute
