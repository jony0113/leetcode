#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: x的平方根.py
Author: fangeng
Date: 2020/5/9 20:46
"""


class Solution:
    """
    实现 int sqrt(int x) 函数。
    计算并返回 x 的平方根，其中 x 是非负整数。
    由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
    """

    def mySqrt(self, x: int) -> int:
        if x <= 0:
            return 0

        start = 1
        end = x
        while start <= end:
            mid = (start + end) // 2
            if mid * mid == x:
                return mid
            if mid * mid > x:
                end = mid - 1
            else:
                start = mid + 1

        if start * start > x:
            return start - 1

        return start
