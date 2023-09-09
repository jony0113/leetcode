#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    """
    假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

    每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
    """

    def climbStairs(self, n: int) -> int:
        """
        动态规划，f(n) = f(n-1) + f(n-2)
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        a = 1
        b = 2

        for i in range(3, n + 1):
            a, b = b, a + b
        return b
