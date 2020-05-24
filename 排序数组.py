#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 排序数组.py
Author: fangeng
Date: 2020/3/31 21:04
"""


class Solution:
    """
    题目：给你一个整数数组 nums，请你将该数组升序排列。
    """

    def sortArray(self, nums: 'List[int]') -> 'List[int]':
        self.f(nums, 0, len(nums) - 1)
        return nums

    def f(self, nums, begin, end):
        if begin >= end:
            return
        index = self.quick_sort(nums, begin, end)
        self.f(nums, begin, index - 1)
        self.f(nums, index + 1, end)

    def quick_sort(self, nums, begin, end):
        k = begin
        for i in range(begin, end):
            if nums[i] < nums[end]:
                nums[i], nums[k] = nums[k], nums[i]
                k += 1
        if begin <= k < end:
            nums[k], nums[end] = nums[end], nums[k]
            return k
        else:
            return end


if __name__ == '__main__':
    a = [2, 4, 3, 2, 5, 6, 4, 1, 8, 0, 7, 6, 5]
    print(Solution().sortArray(a))
