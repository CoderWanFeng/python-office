# -*- coding: UTF-8 -*-
"""Finance functionality module.

金融功能模块。

This module provides financial calculation capabilities, especially for stock T+0 trading calculations.

该模块提供了金融计算功能，尤其是股票T+0交易计算。

Author:
    程序员晚枫

Project:
    https://www.python-office.com
"""

from decimal import Decimal
RATE_LINE = 10000 * 2


def t0(buy_price: float, sale_price: float, shares: int, w_rate: float = 2.5 / 10000, min_rate: int = 5,
       stamp_tax=1 / 1000, ) -> float:
    """Calculate T+0 trading profit.
    
    计算做T的收益。
    
    Args:
        buy_price (float): buy cost / 买入成本
        sale_price (float): sale price / 卖出价格
        shares (int): quantity per transaction / 单笔数量
        w_rate (float, optional): commission rate / 手续费。Default / 默认: 2.5/10000 (0.025% / 万0.25)
        min_rate (int, optional): minimum commission per transaction / 单笔最低手续费。Default / 默认: 5 CNY / 5元
        stamp_tax (float, optional): stamp tax rate / 印花税。Default / 默认: 1/1000 (0.1% / 千分之一)
    
    Returns:
        float: profit after T+0 trading / 做T后的收益金额
    """
    buy_money = Decimal(str(buy_price)) * shares  # 买入的价格
    base_rate = min_rate if buy_money <= RATE_LINE else buy_money * w_rate

    sale_money = Decimal(str(sale_price))   * shares
    sale_rate = min_rate if sale_money <= RATE_LINE else sale_money * w_rate

    sale_tax = sale_money * Decimal(str(stamp_tax))
    stock_returns = sale_money - buy_money - base_rate - sale_rate - sale_tax
    return stock_returns


if __name__ == '__main__':
    print(t0(11.99, 12.26, 700))
