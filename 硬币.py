#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 硬币.py
Author: fangeng
Date: 2020/4/23 21:36
"""


class Solution:
    """
    题目：
    硬币。给定数量不限的硬币，币值为25分、10分、5分和1分，编写代码计算n分有几种表示法。
    (结果可能会很大，你需要将结果模上1000000007)
    """

    def waysToChange(self, n: int) -> int:
        mod = 10 ** 9 + 7
        coins = [25, 10, 5, 1]

        f = [1] + [0] * n
        for coin in coins:
            for i in range(coin, n + 1):
                f[i] += f[i - coin]
        return f[n] % mod

