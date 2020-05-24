#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 跳跃游戏II.py
Author: fangeng
Date: 2020/4/17 21:33
"""


class Solution:
    """
    题目：
    给定一个非负整数数组，你最初位于数组的第一个位置。
    数组中的每个元素代表你在该位置可以跳跃的最大长度。
    你的目标是使用最少的跳跃次数到达数组的最后一个位置
    """

    def jump(self, nums: 'List[int]') -> int:
        if not nums or len(nums) < 2:
            return 0
        length = len(nums)

        step = 0
        last_max = 0
        cur_max = 0

        for i in range(length):

            # 不断更新最远距离
            cur_max = max(cur_max, i + nums[i])
            if i == length - 1:
                break

            # 当到达上一次的最远距离时，步数增加，当前步数下最远能到的距离
            if i == last_max:
                last_max = cur_max
                step += 1

        return step
