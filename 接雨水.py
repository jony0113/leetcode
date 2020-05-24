#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 接雨水.py
Author: fangeng
Date: 2020/4/4 21:49
"""


class Solution:
    """
    给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

    输入: [0,1,0,2,1,0,1,3,2,1,2,1]
    输出: 6
    """

    def trap(self, height: 'List[int]') -> int:
        if not height or len(height) < 2:
            return 0
        length = len(height)
        left_max = height[0]
        left_height = [0] * length
        for i in range(1, length):
            left_max = max(left_max, height[i - 1])
            left_height[i] = left_max

        right_max = height[length - 1]
        right_height = [0] * length
        for i in range(length - 2, -1, -1):
            right_max = max(right_max, height[i + 1])
            right_height[i] = right_max

        res = 0
        for i in range(1, length - 1):
            h = min(left_height[i], right_height[i]) - height[i]
            if h > 0:
                res += h
        return res
