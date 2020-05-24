#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 全排列.py
Author: fangeng
Date: 2020/4/25 19:49
"""
import copy


class Solution:
    """
    给定一个 没有重复 数字的序列，返回其所有可能的全排列。
    """

    def permute(self, nums: 'List[int]') -> 'List[List[int]]':
        """
        维护一个数组保存前面k个数字的全排列，当加入第k+1个数字的时候，
        只需要对每个全排列的每一个list所有能插入数字的地方插入当前数字
        """
        if not nums or len(nums) < 1:
            return [[]]
        ans = [[nums[0]]]

        for i in range(1, len(nums)):
            temp = ans
            ans = []
            for item in temp:
                length = len(item)
                for j in range(length + 1):
                    li = copy.copy(item)  # 注意这里要使用copy方法，否则会在item上进行修改
                    li.insert(j, nums[i])
                    ans.append(li)

        return ans
