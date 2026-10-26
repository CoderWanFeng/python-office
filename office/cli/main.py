# -*- coding: UTF-8 -*-
"""`po` 命令入口：argparse 构建、平台守卫与延迟分发。

用法::

    po [--json] <module> <command> [args...]
    po --version

设计要点：

- 注册表（office.cli.commands）自包含参数信息，构建解析器零 import；
- 只有分发时才 ``importlib.import_module`` 对应的 ``office.api`` 模块，
  并把导入期输出重定向到 stderr，避免污染 ``--json`` 的 stdout；
- 分发前按平台守卫拦截 Windows-only 模块，给出干净报错；
- 传参前用 ``inspect.signature`` 过滤，注册表多写的参数不会传进 api。
"""

import argparse
import contextlib
import importlib
import inspect
import sys

from office.cli import commands, output


class CliError(Exception):
    """CLI 层的可预期错误（平台不符、命令缺失等），报给用户而非 traceback。"""


def _kebab(name):
    return name.replace("_", "-")


def _str2bool(value):
    """支持 ``--flag true/false/1/0/yes/no/on/off``，用于 api 默认值为 True 的参数。"""
    if isinstance(value, bool):
        return value
    text = str(value).strip().lower()
    if text in ("1", "true", "t", "yes", "y", "on"):
        return True
    if text in ("0", "false", "f", "no", "n", "off"):
        return False
    raise argparse.ArgumentTypeError("expect true/false, got %r" % value)


def _add_params(cmd_parser, params):
    for param in params:
        name = param["name"]
        help_text = param.get("help", "")
        if param.get("positional"):
            kwargs = {"help": help_text}
            for key in ("nargs", "metavar", "type", "choices"):
                if key in param:
                    kwargs[key] = param[key]
            if param.get("type") == "bool":
                kwargs["type"] = _str2bool
                kwargs["metavar"] = "BOOL"
            cmd_parser.add_argument(name, **kwargs)
        else:
            kwargs = {"dest": name, "help": help_text}
            if param.get("flag"):
                kwargs["action"] = "store_true"
            else:
                for key in ("default", "nargs", "choices", "type"):
                    if key in param:
                        kwargs[key] = param[key]
                if param.get("type") == "bool":
                    kwargs["type"] = _str2bool
                    kwargs["metavar"] = "BOOL"
                if param.get("required"):
                    kwargs["required"] = True
            cmd_parser.add_argument("--" + _kebab(name), **kwargs)


def build_parser(registry=None):
    """由注册表构建完整 argparse 解析器。"""
    registry = commands.MODULES if registry is None else registry
    parser = argparse.ArgumentParser(
        prog="po",
        description="python-office CLI — office automation from the terminal",
    )
    parser.add_argument("-V", "--version", action="store_true",
                        help="show version and exit")
    parser.add_argument("--json", action="store_true",
                        help="machine readable output (stdout is a single JSON line)")
    module_sub = parser.add_subparsers(dest="module", metavar="<module>")
    for module_name in sorted(registry):
        module = registry[module_name]
        module_parser = module_sub.add_parser(module_name, help=module.get("help", ""))
        command_sub = module_parser.add_subparsers(dest="command", metavar="<command>",
                                                   required=True)
        for command_name in sorted(module.get("commands", {})):
            command = module["commands"][command_name]
            command_parser = command_sub.add_parser(command_name, help=command.get("help", ""))
            _add_params(command_parser, command.get("params", []))
    return parser


def _version():
    try:
        from importlib.metadata import version
        return version("python-office")
    except Exception:
        try:
            import office
            return getattr(office, "__version__", "unknown")
        except Exception:
            return "unknown"


def dispatch(module_name, command_name, namespace, registry, as_json=False):
    """延迟导入目标模块并调用 api 函数，返回其返回值。"""
    module = registry[module_name]
    allowed = module.get("platforms")
    if allowed and sys.platform not in allowed:
        raise CliError(
            "module '%s' is only available on: %s (current: %s)"
            % (module_name, ", ".join(allowed), sys.platform))
    # office 包导入期可能打印横幅（首次运行提示），重定向到 stderr 保持 stdout 干净
    with contextlib.redirect_stdout(sys.stderr):
        target = importlib.import_module(module["module"])
    func = getattr(target, command_name, None)
    if func is None:
        raise CliError("command not found: %s.%s" % (module_name, command_name))
    accepted = inspect.signature(func).parameters
    kwargs = {key: value for key, value in vars(namespace).items()
              if key in accepted and value is not argparse.SUPPRESS}
    if as_json:
        with contextlib.redirect_stdout(sys.stderr):
            return func(**kwargs)
    return func(**kwargs)


def main(argv=None, registry=None):
    """`po` 入口，返回进程退出码。"""
    registry = commands.MODULES if registry is None else registry
    parser = build_parser(registry)
    args = parser.parse_args(argv)
    if args.version:
        print("po %s (python-office)" % _version())
        return 0
    if not args.module:
        parser.print_help(sys.stderr)
        return 2
    try:
        result = dispatch(args.module, args.command, args, registry, as_json=args.json)
    except CliError as exc:
        return output.emit_error(exc, as_json=args.json)
    except KeyboardInterrupt:
        return output.emit_error("interrupted", as_json=args.json) or 130
    except Exception as exc:
        return output.emit_error("%s: %s" % (type(exc).__name__, exc),
                                 as_json=args.json)
    output.emit_result(result, as_json=args.json)
    return 0
