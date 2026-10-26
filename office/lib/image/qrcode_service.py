# -*- coding: utf-8 -*-
"""二维码解析服务。

背景：``poimage`` 至今（0.0.22）未提供 ``decode_qrcode``，因此这里基于
OpenCV 的 ``QRCodeDetector`` 自行实现。OpenCV 由 ``poimage`` 的依赖
``opencv-python`` 提供，无需用户额外安装。
"""

from PIL import Image


def _load_cv2():
    """按需加载 cv2，缺失时给出可操作的报错。"""
    try:
        import cv2
    except ImportError as exc:
        raise ModuleNotFoundError(
            "二维码解析依赖 opencv-python，请先安装：pip install opencv-python"
        ) from exc
    return cv2


def decode_qrcode(qrcode_path: str) -> str:
    """解析二维码图片，提取其中的文本内容。

    Args:
        qrcode_path (str): 二维码图片的路径 / QR code image path

    Returns:
        str: 二维码中的文本内容；未识别到二维码时返回空字符串

    Raises:
        FileNotFoundError: 二维码图片不存在
        ModuleNotFoundError: 未安装 opencv-python
    """
    cv2 = _load_cv2()
    import numpy as np

    with Image.open(qrcode_path) as im:
        rgb = np.array(im.convert("RGB"))

    # OpenCV 期望 BGR 顺序且内存连续的三通道数组
    bgr = np.ascontiguousarray(rgb[:, :, ::-1])

    detector = cv2.QRCodeDetector()
    data, _, _ = detector.detectAndDecode(bgr)
    return data
