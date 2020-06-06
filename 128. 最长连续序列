#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    """
    给定一个未排序的整数数组，找出最长连续序列的长度。

    要求算法的时间复杂度为 O(n)。
    """

    def longestConsecutive(self, nums: 'List[int]') -> int:
        """
        1. 使用set存储数组里面的数，判断一个数是否在set里面，时间复杂度为O(1)
        2. 对于每个在数组里面的数x，查看x+1,x+2... 是否在set里
        3. 为了降低时间复杂度，要确保每次内层循环时，起始的元素都是这个序列的第一个元素
        """
        nums_set = set(nums)

        ans = 0
        for num in nums:
            if num - 1 not in nums_set and num in nums_set:
                temp = 1
                while num + temp in nums_set:
                    temp += 1
                ans = max(ans, temp)
        return ans
