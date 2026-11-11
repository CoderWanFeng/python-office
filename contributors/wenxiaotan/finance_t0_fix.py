# -*- coding: UTF-8 -*-
"""修正版的 T+0 收益计算，解决 Decimal / float 混算与返回类型不一致的问题。

背景
----
`office.api.finance.t0`（python-office 1.1.2）有两个缺陷，都会影响正常使用：

1. **`min_rate` 未做 Decimal 规范化。** 该函数把 `w_rate`、`buy_price`、
   `sale_price`、`stamp_tax` 都转成了 `Decimal`，唯独漏了 `min_rate`。
   当买入/卖出金额低于 `RATE_LINE` 时，手续费直接取 `min_rate`（此时还是
   `int` 或 `float`），随后与 `Decimal` 相减即抛：

       TypeError: unsupported operand type(s) for -:
                  'decimal.Decimal' and 'float'

   而 CLI（`office/cli/commands.py`）把 `min_rate` 声明为 `type: float`，
   所以下面这条命令**必然失败**：

       po finance t0 11.99 12.26 700 --min-rate 5

2. **返回值类型与签名不符。** 函数签名与文档都写 `-> float`，实际返回的是
   `Decimal`。调用方做 `isinstance` 判断、`json.dumps` 序列化，或与 `float`
   混算时，会得到与文档承诺不一致的结果。

本模块提供一个行为一致、类型正确的实现，可独立于上游修复直接使用。

Author:
    wenxiaotan

Project:
    https://www.python-office.com
"""

from decimal import Decimal

# 与上游保持一致：佣金按比例计算的起征线
RATE_LINE = 10000 * 2


def t0(
    buy_price: float,
    sale_price: float,
    shares: int,
    w_rate: float = 2.5 / 10000,
    min_rate: int = 5,
    stamp_tax=1 / 1000,
) -> float:
    """计算做 T 的收益。

    与 `office.api.finance.t0` 的计算逻辑一致，但修复了两个问题：
    所有参与运算的参数统一转为 `Decimal`（含此前被遗漏的 `min_rate`），
    并在返回前显式转换为 `float`，使返回值与类型标注一致。

    Args:
        buy_price (float): 买入成本。
        sale_price (float): 卖出价格。
        shares (int): 单笔数量。
        w_rate (float, optional): 手续费率。默认 2.5/10000（万 0.25）。
        min_rate (int, optional): 单笔最低手续费。默认 5 元。
            可传 `int` 或 `float`，都会先转成 `Decimal` 再参与计算。
        stamp_tax (float, optional): 印花税率。默认 1/1000（千分之一）。

    Returns:
        float: 做 T 后的收益金额，保留与上游一致的 5 位小数精度。

    Raises:
        TypeError: 任一价格或数量无法转换为数字时。
        ValueError: `shares` 为负数时。

    Example:
        >>> t0(11.99, 12.26, 700)
        170.418
        >>> t0(11.99, 12.26, 700, min_rate=5.0)   # 上游此处会抛 TypeError
        170.418
        >>> t0(100, 110, 700)                    # 超过费率起征线，按比例计佣
        6886.25
    """
    if shares < 0:
        raise ValueError("shares 不能为负数，收到：{!r}".format(shares))

    # 统一转 Decimal：Decimal 与 float 直接运算会抛 TypeError，
    # min_rate 正是上游漏掉的那一个。
    w_rate = Decimal(str(w_rate))
    min_rate = Decimal(str(min_rate))

    buy_money = Decimal(str(buy_price)) * shares
    base_rate = min_rate if buy_money <= RATE_LINE else buy_money * w_rate

    sale_money = Decimal(str(sale_price)) * shares
    sale_rate = min_rate if sale_money <= RATE_LINE else sale_money * w_rate

    sale_tax = sale_money * Decimal(str(stamp_tax))
    stock_returns = sale_money - buy_money - base_rate - sale_rate - sale_tax

    # 标注是 -> float，就返回 float，避免调用方拿到 Decimal。
    return float(stock_returns)


def t0_safe(*args, **kwargs):
    """`t0` 的容错包装：参数非法时返回 None，而不是抛异常。

    适合在批量计算、报表生成等不希望被单条脏数据中断的场景使用。

    Returns:
        float | None: 计算成功返回收益金额，失败返回 None。

    Example:
        >>> t0_safe(11.99, 12.26, 700)
        170.418
        >>> t0_safe("不是数字", 12.26, 700) is None
        True
    """
    try:
        return t0(*args, **kwargs)
    except (TypeError, ValueError, ArithmeticError):
        return None


if __name__ == "__main__":
    # 简单自检：覆盖小于/大于 RATE_LINE、float 型 min_rate 三种情况
    print("小额（用最低手续费）      :", t0(11.99, 12.26, 700))
    print("小额 + float min_rate     :", t0(11.99, 12.26, 700, min_rate=5.0))
    print("大额（按比例计佣）        :", t0(100, 110, 700))
    print("返回类型                  :", type(t0(11.99, 12.26, 700)).__name__)
    print("容错包装（脏数据）        :", t0_safe("abc", 12.26, 700))
