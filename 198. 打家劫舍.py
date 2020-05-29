#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import lru_cache


class Solution:
    """
    你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，
    影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
    如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
    给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，
    一夜之内能够偷窃到的最高金额。
    """

    def rob(self, nums: 'List[int]') -> int:
        if not nums:
            return 0
        if len(nums) < 3:
            return max(nums)

        @lru_cache
        def f(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0],nums[1])
            return max(f(i - 2) + nums[i], f(i - 1))

        return f(len(nums) - 1)
