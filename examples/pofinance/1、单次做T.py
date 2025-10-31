# -*- coding: UTF-8 -*-
"""
单次做T（股票交易）计算示例

该示例演示如何使用pofinance库计算单次股票交易的收益。

Args:
    买入价: 股票的买入价格
    卖出价: 股票的卖出价格  
    数量: 交易股票的数量

Example:
    >>> import pofinance
    >>> print(pofinance.t0(11.06, 11.23, 500))
    >>> print(pofinance.t0(11.06, 35.57, 2000))
    >>> print(pofinance.t0(14, 14.5, 300))

Returns:
    float: 交易的总收益金额

Author:
    程序员晚枫

Project:
    https://www.python-office.com
"""

import pofinance

print(pofinance.t0(11.06, 11.23, 500))
print(pofinance.t0(11.06, 35.57, 2000))
print(pofinance.t0(14, 14.5, 300))
