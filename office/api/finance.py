# -*- coding: UTF-8 -*-
"""金融工具功能模块。

本模块按 https://www.python-office.com/modules/finance/api 官方文档定义，
共 1 个函数：

    1. t0 - 计算股票 T+0 交易收益

计算公式：``收益 = 卖出金额 - 买入金额 - 买入手续费 - 卖出手续费 - 印花税``

Author:
    程序员晚枫

Project:
    https://www.python-office.com
"""

from __future__ import annotations

from decimal import Decimal
from typing import Union


__all__ = ["t0"]


# 单笔交易额 ≤ 10000*2=20000 元时按最低手续费 5 元收取
_RATE_LINE = 10000 * 2


def t0(
    buy_price: float,
    sale_price: float,
    shares: int,
    w_rate: float = 2.5 / 10000,
    min_rate: int = 5,
    stamp_tax: float = 1 / 1000,
) -> float:
    """Calculate T+0 trading profit.

    计算股票 T+0 交易收益。

    计算公式：
        收益 = 卖出金额 − 买入金额 − 买入手续费 − 卖出手续费 − 印花税

    手续费规则：单笔交易额 ≤ 20000 元时按 ``min_rate`` 元收取，超过则按
    ``w_rate`` 比例收取；卖出时再扣 ``stamp_tax`` 印花税。

    Documentation: https://www.python-office.com/modules/finance/api#t0

    Args:
        buy_price: 买入价格（元 / 股）
        sale_price: 卖出价格（元 / 股）
        shares: 交易股数
        w_rate: 手续费率（默认 ``2.5/10000`` = 万 2.5 = 0.025%）
        min_rate: 单笔最低手续费（元，默认 ``5``）
        stamp_tax: 印花税率（默认 ``1/1000`` = 千 1 = 0.1%）

    Returns:
        float: 做 T 后的净收益金额（正数 = 盈利，负数 = 亏损）
    """
    buy_money = Decimal(str(buy_price)) * shares
    base_rate = min_rate if buy_money <= _RATE_LINE else buy_money * Decimal(str(w_rate))

    sale_money = Decimal(str(sale_price)) * shares
    sale_rate = min_rate if sale_money <= _RATE_LINE else sale_money * Decimal(str(w_rate))

    sale_tax = sale_money * Decimal(str(stamp_tax))
    stock_returns = sale_money - buy_money - base_rate - sale_rate - sale_tax
    return float(stock_returns)


if __name__ == "__main__":
    print(t0(11.99, 12.26, 700))
