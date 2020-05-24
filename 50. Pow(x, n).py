#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 50. Pow(x, n).py
Author: fangeng
Date: 2020/5/11 20:42
"""


class Solution:
    """
    实现 pow(x, n) ，即计算 x 的 n 次幂函数。
    """

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n > 0:
            if n % 2 == 0:
                return self.myPow(x * x, n // 2)
            if n % 2 == 1:
                return x * self.myPow(x * x, n // 2)
