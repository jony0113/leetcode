#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 跳跃游戏.py
Author: fangeng
Date: 2020/4/17 20:42
"""


class Solution:
    """
    题目：给定一个非负整数数组，你最初位于数组的第一个位置。
    数组中的每个元素代表你在该位置可以跳跃的最大长度。
    判断你是否能够到达最后一个位置。
    """

    def canJump(self, nums: 'List[int]') -> bool:
        if not nums or len(nums) < 2:
            return True
        length = len(nums)

        # 最远能到达的距离
        _max = 0

        for i in range(length):

            # 如果循环已经超过了最远距离，则不可能到达了
            if i > _max:
                return False

            # 更新最远能到达的距离
            _max = max(_max, i + nums[i])

            # 如果最远能到达的距离大于等于数组的长度，说明能到达
            if _max >= length - 1:
                return True
