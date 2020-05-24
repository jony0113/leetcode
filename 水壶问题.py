#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 水壶问题.py
Author: fangeng
Date: 2020/3/21 21:57
"""
import math


class Solution:
    """
    题目：
    有两个容量分别为 x升 和 y升 的水壶以及无限多的水。请判断能否通过使用这两个水壶，从而可以得到恰好 z升 的水？

    如果可以，最后请用以上水壶中的一或两个来盛放取得的 z升 水。

    你允许：

    装满任意一个水壶
    清空任意一个水壶
    从一个水壶向另外一个水壶倒水，直到装满或者倒空
    """

    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        stack = [(0, 0)]
        already = set()
        while stack:
            remain_x, remain_y = stack.pop()
            if remain_x == z or remain_y == z or remain_x + remain_y == z:
                return True
            if (remain_x, remain_y) in already:
                continue
            already.add((remain_x, remain_y))

            # 把x装满
            stack.append((x, remain_y))
            # 把y装满
            stack.append((remain_x, y))
            # 把x全部倒掉
            stack.append((0, remain_y))
            # 把y全部倒掉
            stack.append((remain_x, 0))
            # 把x中的水倒入y
            stack.append((0, remain_x + remain_y) if remain_x + remain_y < y
                         else (remain_x + remain_y - y, y))

            # 把y中的水倒入x
            stack.append((remain_x + remain_y, 0) if remain_x + remain_y < x
                         else (x, remain_x + remain_y - x))
        return False

    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x + y < z:
            return False
        if x == 0 or y == 0:
            return z == 0 or x + y == z
        return z % math.gcd(x, y) == 0
