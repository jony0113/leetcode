#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 两数之和.py
Author: fangeng
Date: 2020/4/16 21:29
"""


class Solution:
    """
    给定一个整数数组 nums 和一个目标值 target，
    请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
    你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
    """

    def twoSum(self, nums: 'List[int]', target: int) -> 'List[int]':
        temp = {}
        for index, item in enumerate(nums):
            another = target - item
            if another in temp:
                return [temp.get(another), index]
            temp[item] = index
