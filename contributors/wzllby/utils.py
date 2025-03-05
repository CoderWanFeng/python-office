"""
    此类为通用工具类
"""

import zipfile
import base64
import os
import shutil
import pandas as pd


def process_zip(zip_path, target_path='./file'):
    """
    解压zip文件,获取解压后的文件路径

    Args:
        zip_path: 需要解压的zip文件
        target_path: 解压后的文件  默认是当前文件
    """
    # 创建临时文件夹
    temp_dir = "./temp"
    os.makedirs(temp_dir, exist_ok=True)
    # 解压zip文件
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for file in zip_ref.namelist():
            # 处理乱码
            fixed_name = file.encode('cp437').decode('gbk')
            fixed_path = os.path.join(temp_dir, fixed_name)
            if file.endswith('/'):
                os.makedirs(fixed_path, exist_ok=True)
            else:
                with open(fixed_path, 'wb') as f:
                    f.write(zip_ref.read(file))
    items = os.listdir(temp_dir)
    if len(items) != 1 or not os.path.isdir(os.path.join(temp_dir, items[0])):
        raise ValueError("zip文件格式有误")
        # 获取唯一的文件夹名称
    single_folder = items[0]
    folder_path = os.path.join(temp_dir, single_folder)

    # 移动到目标目录
    target_folder = os.path.join(target_path, single_folder)
    shutil.move(folder_path, target_folder)

    # 清理临时目录
    os.rmdir(temp_dir)
    return target_folder


def get_base64_by_img(img_path):
    """
    根据文件路径获取base64编码

    Args:
        img_path: 图片路径
    """
    with open(img_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def get_tencent_secret(csv_path):
    """
    获取密钥信息

    Args:
        csv_path: 密钥csv信息csv文件
    """
    df = pd.read_csv(csv_path)
    secret_id = df["SecretId"][0]
    secret_key = df["SecretKey"][0]
    return [secret_id, secret_key]
