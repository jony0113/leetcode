#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 三个数的最大乘积.py
Author: fangeng
Date: 2020/3/25 22:17
"""
import sys


class Solution:
    """
    题目：
    给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

    [1,2,3] -> 6
    [1,2,3,4] -> 24
    """

    def maximumProduct(self, nums: 'List[int]') -> int:
        if not nums or len(nums) < 3:
            return 0
        elif len(nums) == 3:
            return nums[0] * nums[1] * nums[2]
        max_1 = max_2 = max_3 = -sys.maxsize
        min_1 = min_2 = sys.maxsize
        for num in nums:
            if num > max_1:
                max_3 = max_2
                max_2 = max_1
                max_1 = num
            elif num > max_2:
                max_3 = max_2
                max_2 = num
            elif num > max_3:
                max_3 = num

            if num < min_1:
                min_2 = min_1
                min_1 = num
            elif num < min_2:
                min_2 = num
        return max(max_1 * max_2 * max_3, min_1 * min_2 * max_1)
