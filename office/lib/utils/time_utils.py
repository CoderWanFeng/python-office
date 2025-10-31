import time


def time_count_dec(func):
    """时间统计装饰器，用于测量函数执行时间。
    
    Args:
        func: 被装饰的函数
    
    Returns:
        function: 装饰后的函数
    """
    def wrapper(*args, **kwargs):
        t1 = time.time()
        res = func(*args, **kwargs)
        t2 = time.time()
        print(func.__name__ + "执行耗时" + str(t2 - t1))
        return res

    return wrapper
