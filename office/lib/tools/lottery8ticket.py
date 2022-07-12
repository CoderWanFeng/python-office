import random


def SSL():
    red_ball = random.sample(range(1, 34), 6)
    blue_ball = random.sample(range(1, 17), 1)
    return f'双色球的号码是：红色球{red_ball}，蓝色球{blue_ball}'


def D3():
    pass


def SLC():
    pass


def CCDLT():
    pass


def QXC():
    pass


def PL3():
    pass


def PL5():
    pass


def KL8():
    pass


def QWS():
    pass


def X_22_5():
    res = random.sample(range(1, 33), 5)  # 1到22，不重复的5个数
    return res


def X_36_7():
    res = random.sample(range(1, 37), 7)  # 1到36，不重复的7个数
    return res


def X_26_5():
    res = random.sample(range(1, 27), 5)
    return res


ticket_kinds = {
    "0": ["退出", None],
    "1": ["双色球", SSL],
    "2": ["福彩3D", D3],
    "3": ["七乐彩", SLC],
    "4": ["超级大乐透", CCDLT],
    "5": ["七星彩", QXC],
    "6": ["排列3", PL3],
    "7": ["排列5", PL5],
    "8": ["快乐8", KL8],
    "9": ["七位数", QWS],
    "10": ["22选5", X_22_5],
    "11": ["36选7", X_36_7],
    "12": ["25选5", X_26_5],
}
