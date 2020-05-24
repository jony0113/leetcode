#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 152. 乘积最大子数组.py
Author: fangeng
Date: 2020/5/18 21:28
"""


class Solution:
    """
    给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），
    并返回该子数组所对应的乘积。
    """

    def maxProduct(self, nums: 'List[int]') -> int:
        if not nums:
            return 0

        length = len(nums)

        ans = nums[0]
        _max = nums[0]
        _min = nums[0]
        for i in range(1, length):
            i_max = _max
            i_min = _min
            _max = max(i_max * nums[i], i_min * nums[i], nums[i])
            _min = min(i_max * nums[i], i_min * nums[i], nums[i])
            ans = max(_max, ans)

        return ans
