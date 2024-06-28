import time


def time_count_dec(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        res = func(*args, **kwargs)
        t2 = time.time()
        print(func.__name__ + "执行耗时" + str(t2 - t1))
        return res

    return wrapper
