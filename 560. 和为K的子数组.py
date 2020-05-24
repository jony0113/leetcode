#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 560. 和为K的子数组.py
Author: fangeng
Date: 2020/5/15 21:54
"""


class Solution:
    """
    给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
    """

    def subarraySum(self, nums: 'List[int]', k: int) -> int:
        if not nums or len(nums) < 1:
            return 0
        count = 0
        for i in range(len(nums)):
            _sum = 0
            for j in range(i, -1, -1):
                _sum += nums[j]
                if _sum == k:
                    count += 1

        return count

    def subarraySum1(self, nums: 'List[int]', k: int) -> int:
        if not nums or len(nums) < 1:
            return 0
        count = 0
        pre = 0
        mp = {0: 1}
        for i in range(len(nums)):
            pre += nums[i]
            if pre - k in mp:
                count += mp.get(pre - k)
            mp[pre] = mp.get(pre, 0) + 1

        return count
