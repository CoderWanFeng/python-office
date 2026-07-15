"""Tests for the instruction URL decorator."""

import importlib.util
from pathlib import Path
import sys
import types
import unittest


class TestInstructionUrl(unittest.TestCase):
    def setUp(self):
        self._original_modules = {
            name: sys.modules.get(name)
            for name in (
                "pocode",
                "pocode.api",
                "pocode.api.color",
                "office",
                "office.api",
                "office.lib",
                "office.lib.conf",
                "office.lib.conf.CONST",
                "office.lib.decorator_utils.instruction_url",
            )
        }

        sys.modules["pocode"] = types.ModuleType("pocode")
        sys.modules["pocode.api"] = types.ModuleType("pocode.api")
        color_module = types.ModuleType("pocode.api.color")
        color_module.random_color_print = lambda *args, **kwargs: None
        sys.modules["pocode.api.color"] = color_module
        const_module = types.ModuleType("office.lib.conf.CONST")
        const_module.SPLIT_LINE = "-" * 20
        api_module = types.ModuleType("office.api")
        office_module = types.ModuleType("office")
        office_module.api = api_module
        sys.modules["office"] = office_module
        sys.modules["office.api"] = api_module
        sys.modules["office.lib"] = types.ModuleType("office.lib")
        sys.modules["office.lib.conf"] = types.ModuleType("office.lib.conf")
        sys.modules["office.lib.conf.CONST"] = const_module
        sys.modules.pop("office.lib.decorator_utils.instruction_url", None)

    def tearDown(self):
        for name in (
            "pocode",
            "pocode.api",
            "pocode.api.color",
            "office",
            "office.api",
            "office.lib",
            "office.lib.conf",
            "office.lib.conf.CONST",
            "office.lib.decorator_utils.instruction_url",
        ):
            sys.modules.pop(name, None)

        for name, module in self._original_modules.items():
            if module is not None:
                sys.modules[name] = module

    def test_missing_method_link_does_not_block_wrapped_function(self):
        module_path = (
            Path(__file__).resolve().parents[2]
            / "office"
            / "lib"
            / "decorator_utils"
            / "instruction_url.py"
        )
        spec = importlib.util.spec_from_file_location(
            "office.lib.decorator_utils.instruction_url",
            module_path,
        )
        instruction_url = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = instruction_url
        spec.loader.exec_module(instruction_url)
        namespace = {}
        exec(
            compile("def undocumented_feature():\n    return 'ok'\n", "/tmp/excel.py", "exec"),
            namespace,
        )

        wrapped = instruction_url.instruction(namespace["undocumented_feature"])

        self.assertEqual("ok", wrapped())


if __name__ == "__main__":
    unittest.main()
