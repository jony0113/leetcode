#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 53. 最大子序和.py
Author: fangeng
Date: 2020/3/19 21:30
"""


class Solution(object):
    """
    题目：
    给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
    """

    def maxSubArray(self, nums: 'List of int') -> int:
        if not nums or len(nums) < 1:
            return 0
        length = len(nums)
        _ans = nums[0]
        _sum = nums[0]
        for i in range(1, length):
            if _sum > 0:
                _sum += nums[i]
            else:
                _sum = nums[i]
            _ans = max(_sum, _ans)
        return _ans


if __name__ == '__main__':
    print(Solution().maxSubArray([1, 2, 3]))
