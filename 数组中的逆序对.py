#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 数组中的逆序对.py
Author: fangeng
Date: 2020/4/24 20:54
"""
import copy


class Solution:
    """
    在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
    输入一个数组，求出这个数组中的逆序对的总数。

    [7,5,6,4] -> 5
    """

    def reversePairs(self, nums: 'List[int]') -> int:
        if not nums or len(nums) < 2:
            return 0

        return self.count_nums(nums, 0, len(nums) - 1)

    def count_nums(self, nums, start, end):
        if start == end:
            return 0

        mid = (start + end) // 2
        ans = self.count_nums(nums, start, mid)
        ans += self.count_nums(nums, mid + 1, end)
        i, j = start, mid + 1
        temp = []
        while i <= mid and j <= end:
            if nums[j] < nums[i]:
                ans += (mid - i + 1)
                temp.append(nums[j])
                j += 1
            else:
                temp.append(nums[i])
                i += 1
        if i <= mid:
            temp.extend(nums[i: mid + 1])
        if j <= end:
            temp.extend(nums[j: end + 1])

        k = start
        for item in temp:
            nums[k] = item
            k += 1

        return ans
