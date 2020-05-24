#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 整数反转.py
Author: fangeng
Date: 2020/4/17 22:45
"""


class Solution:
    """
    题目：给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
    """

    def reverse(self, x: int) -> int:

        MAX = (2 << 30) - 1
        MIN = - 2 << 30

        symbol = 1
        if x < 0:
            x = -x
            symbol = -1

        temp = 0
        res = 0
        while x > 0:
            temp = (temp * 10 + x % 10)
            x //= 10
            res = symbol * temp
            if res > MAX or res < MIN:
                return 0
        return res
