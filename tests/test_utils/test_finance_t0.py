"""Tests for office.api.finance.t0."""

import pytest

from office.api.finance import t0


def test_t0_large_trade_does_not_raise_type_error():
    """买入金额超过 RATE_LINE 时，佣金按比例计算，不应抛 TypeError。

    回归用例：此前 buy_money 是 Decimal，w_rate 是 float，两者相乘会报
    TypeError: unsupported operand type(s) for *: 'decimal.Decimal' and 'float'。
    """
    result = t0(buy_price=100, sale_price=110, shares=700)

    # 77000 - 70000 - 70000*0.00025 - 77000*0.00025 - 77000*0.001
    assert float(result) == pytest.approx(6886.25)


def test_t0_small_trade_uses_min_commission():
    """金额低于 RATE_LINE 时，买卖两边都按最低手续费 min_rate 计算。"""
    result = t0(buy_price=11.99, sale_price=12.26, shares=700)

    # 8582 - 8393 - 5 - 5 - 8582*0.001
    assert float(result) == pytest.approx(170.418)


def test_t0_respects_custom_commission_rate():
    """自定义 w_rate 时按比例计算佣金，且不受 float/Decimal 混算影响。"""
    result = t0(buy_price=100, sale_price=110, shares=700, w_rate=1 / 10000)

    # 77000 - 70000 - 70000*0.0001 - 77000*0.0001 - 77000*0.001
    assert float(result) == pytest.approx(6908.3)
