---
name: t0
description: 计算股票 T+0 交易的收益，考虑买入价、卖出价、手数、佣金、印花税。当用户提到做 T、T+0、股票做 T、短线做 T 时使用。
---

# t0 Skill

> 计算做 T 的收益

## 功能描述

计算股票 T+0 交易的收益，考虑买入价、卖出价、手数、佣金、印花税等因素。

## 所属分类

`office/skills/finance/t0/`

## 调用方式

```python
from office.skills.finance import t0

profit = t0(
    buy_price=11.99,
    sale_price=12.26,
    shares=700
)
print(profit)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `buy_price` | float | 是 | - | 买入成本 |
| `sale_price` | float | 是 | - | 卖出价格 |
| `shares` | int | 是 | - | 单笔数量（手数） |
| `w_rate` | float | 否 | `2.5/10000` | 佣金费率（万 0.25） |
| `min_rate` | int | 否 | `5` | 单笔最低手续费（元） |
| `stamp_tax` | float | 否 | `1/1000` | 印花税（千分之一） |

## 返回值

`float`：做 T 后的收益金额

## 使用示例

```python
from office.skills.finance import t0
# 买 11.99 卖 12.26，700 股
profit = t0(buy_price=11.99, sale_price=12.26, shares=700)
print(f"本次做T收益: {profit} 元")
```

## 原始函数

`office.api.finance.t0`
