# -*- coding: utf-8 -*-
"""二维码解析的回归测试。

背景：``poimage`` 至今未提供 ``decode_qrcode``，``office.api.image`` 曾直接
调用 ``poimage.decode_qrcode(...)``，必然抛出 AttributeError。现已改为调用
内置的 ``office.lib.image.qrcode_service``。

本测试不依赖真实 opencv：通过 stub 注入假的 cv2。
"""

import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest import mock

from PIL import Image


def _make_fake_cv2(decoded="https://example.com"):
    """构造一个假的 cv2 模块，其 QRCodeDetector 返回固定解码结果。"""
    fake = types.ModuleType("cv2")

    class FakeDetector:
        def __init__(self, *args, **kwargs):
            pass

        def detectAndDecode(self, image):  # noqa: N802 - 保持与 OpenCV 一致
            # 记录收到的图像形状，便于断言颜色通道已转换为 BGR
            fake.last_shape = getattr(image, "shape", None)
            return decoded, None, None

    fake.QRCodeDetector = FakeDetector
    return fake


class TestQrcodeService(unittest.TestCase):
    def setUp(self):
        self._original_cv2 = sys.modules.get("cv2")
        self._original_poimage = sys.modules.get("poimage")

    def tearDown(self):
        for name, original in (("cv2", self._original_cv2), ("poimage", self._original_poimage)):
            if original is not None:
                sys.modules[name] = original
            else:
                sys.modules.pop(name, None)

    def _make_image(self, tmpdir):
        path = Path(tmpdir) / "qr.png"
        Image.new("RGB", (10, 10), (255, 255, 255)).save(path)
        return str(path)

    def test_decode_qrcode_returns_text(self):
        from office.lib.image.qrcode_service import decode_qrcode

        fake_cv2 = _make_fake_cv2("hello-qrcode")
        sys.modules["cv2"] = fake_cv2

        with tempfile.TemporaryDirectory() as tmpdir:
            path = self._make_image(tmpdir)
            result = decode_qrcode(path)

        self.assertEqual(result, "hello-qrcode")
        # PIL 读出的是 RGB，转 BGR 后宽高不变
        self.assertEqual(fake_cv2.last_shape[:2], (10, 10))

    def test_decode_qrcode_without_opencv_raises_actionable_error(self):
        from office.lib.image.qrcode_service import decode_qrcode

        # sys.modules 中置为 None 时 import 会失败，用于模拟 cv2 缺失
        with mock.patch.dict(sys.modules, {"cv2": None}):
            with self.assertRaises(ImportError) as ctx:
                decode_qrcode("whatever.png")

        self.assertIn("opencv-python", str(ctx.exception))

    def test_api_image_decode_qrcode_delegates_to_service(self):
        """office.api.image.decode_qrcode 不得再调用不存在的 poimage.decode_qrcode。"""
        poimage = types.ModuleType("poimage")
        poimage.__path__ = []
        poimage.decode_qrcode = mock.Mock(
            side_effect=AssertionError("不应调用 poimage.decode_qrcode"))
        sys.modules["poimage"] = poimage

        sys.modules.pop("office.api.image", None)
        import office.api.image as image_api

        with mock.patch("office.lib.image.qrcode_service.decode_qrcode",
                        return_value="decoded-text") as service:
            with mock.patch("builtins.print") as printed:
                result = image_api.decode_qrcode("qr.png")

        service.assert_called_once_with(qrcode_path="qr.png")
        self.assertEqual(result, "decoded-text")
        printed.assert_called_once_with("decoded-text")


if __name__ == "__main__":
    unittest.main()
