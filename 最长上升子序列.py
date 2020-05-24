#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 最长上升子序列.py
Author: fangeng
Date: 2020/4/30 21:57
"""


class Solution:
    """
    给定一个无序的整数数组，找到其中最长上升子序列的长度。

    [10,9,2,5,3,7,101,18]

    最长的上升子序列是 [2,3,7,101]，它的长度是 4。
    """

    def lengthOfLIS(self, nums: 'List[int]') -> int:
        if not nums or len(nums) < 1:
            return 0
        length = len(nums)
        dp = [1] * length
        _max = 1
        for i in range(length):
            temp = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    temp = max(temp, dp[j] + 1)
            dp[i] = temp
            _max = max(temp, _max)
        return _max
