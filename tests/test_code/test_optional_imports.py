"""Tests for optional dependency imports."""

from contextlib import contextmanager
import importlib
import os
import sys
import tempfile
import types
import unittest
from unittest import mock


SUPPORTED_DEPENDENCIES = [
    "poexcel",
    "popdf",
    "poimage",
    "pofile",
    "povideo",
    "poocr",
    "pomarkdown",
    "wftools",
]

OPTIONAL_DEPENDENCIES = [
    "poppt",
    "poword",
    "PyOfficeRobot",
    "pospider",
]

MANAGED_MODULE_PREFIXES = (
    "office",
    "pocode",
)

OPTIONAL_LOADERS = [
    (
        "office.api.word",
        "_load_poword",
        "poword",
        "win32com",
        "Word处理功能依赖 poword",
    ),
    (
        "office.api.ppt",
        "_load_poppt",
        "poppt",
        "comtypes",
        "PPT处理功能依赖 poppt",
    ),
    (
        "office.api.wechat",
        "_load_py_office_robot",
        "PyOfficeRobot",
        "uiautomation",
        "微信自动化功能依赖 PyOfficeRobot",
    ),
    (
        "office.api.web",
        "_load_pospider",
        "pospider",
        "requests",
        "网页转电子书功能依赖 pospider",
    ),
]


def _is_managed_module(name):
    return any(name == prefix or name.startswith(f"{prefix}.") for prefix in MANAGED_MODULE_PREFIXES)


class TestOptionalImports(unittest.TestCase):
    """Check that optional dependencies do not break package imports."""

    @contextmanager
    def _optional_import_test_environment(self):
        module_names = (
            SUPPORTED_DEPENDENCIES
            + OPTIONAL_DEPENDENCIES
            + ["pocode", "pocode.api", "pocode.api.color"]
        )
        original_modules = {
            name: sys.modules.get(name)
            for name in list(sys.modules)
            if name in module_names or _is_managed_module(name)
        }
        original_home = os.environ.get("HOME")

        try:
            with tempfile.TemporaryDirectory() as temp_home:
                mark_dir = os.path.join(temp_home, ".python-office")
                os.makedirs(mark_dir)
                with open(os.path.join(mark_dir, "first_run_mark"), "w", encoding="utf-8") as mark_file:
                    mark_file.write("already checked")

                os.environ["HOME"] = temp_home

                for name in list(sys.modules):
                    if _is_managed_module(name):
                        sys.modules.pop(name, None)

                for name in SUPPORTED_DEPENDENCIES:
                    sys.modules[name] = types.ModuleType(name)

                sys.modules["pocode"] = types.ModuleType("pocode")
                sys.modules["pocode.api"] = types.ModuleType("pocode.api")
                color_module = types.ModuleType("pocode.api.color")
                color_module.random_color_print = lambda *args, **kwargs: None
                sys.modules["pocode.api.color"] = color_module

                for name in OPTIONAL_DEPENDENCIES:
                    sys.modules.pop(name, None)

                yield
        finally:
            if original_home is None:
                os.environ.pop("HOME", None)
            else:
                os.environ["HOME"] = original_home

            for name in list(sys.modules):
                if name in module_names or _is_managed_module(name):
                    sys.modules.pop(name, None)

            for name, module in original_modules.items():
                if module is not None:
                    sys.modules[name] = module

    def test_import_office_without_optional_dependencies(self):
        with self._optional_import_test_environment():
            office = importlib.import_module("office")

            self.assertIsNotNone(office.web)

    def test_loader_preserves_dependency_internal_import_errors(self):
        with self._optional_import_test_environment():
            importlib.import_module("office")
            original_import = __import__

            for module_name, loader_name, dependency_name, internal_name, message in OPTIONAL_LOADERS:
                with self.subTest(dependency_name=dependency_name):
                    api_module = importlib.import_module(module_name)
                    loader = getattr(api_module, loader_name)

                    def import_with_missing_internal_dependency(
                        name, globals=None, locals=None, fromlist=(), level=0
                    ):
                        if name == dependency_name:
                            raise ModuleNotFoundError(
                                f"No module named '{internal_name}'",
                                name=internal_name,
                            )
                        return original_import(name, globals, locals, fromlist, level)

                    with mock.patch("builtins.__import__", side_effect=import_with_missing_internal_dependency):
                        with self.assertRaises(ModuleNotFoundError) as error:
                            loader()

                    self.assertEqual(internal_name, error.exception.name)
                    self.assertNotIn(message, str(error.exception))

    def test_loader_reports_missing_optional_dependency(self):
        with self._optional_import_test_environment():
            importlib.import_module("office")

            for module_name, loader_name, dependency_name, _, message in OPTIONAL_LOADERS:
                with self.subTest(dependency_name=dependency_name):
                    api_module = importlib.import_module(module_name)
                    loader = getattr(api_module, loader_name)

                    with self.assertRaises(ModuleNotFoundError) as error:
                        loader()

                    self.assertIn(message, str(error.exception))


if __name__ == "__main__":
    unittest.main()
