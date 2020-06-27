#!/usr/bin/env python
# -*- coding: utf-8 -*-
from queue import PriorityQueue


class Solution:
    """
    给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。
    你的算法的时间复杂度应为O(n)，并且只能使用常数级别的额外空间。
    """

    def firstMissingPositive(self, nums: 'List[int]') -> int:
        sets = set([x for x in nums if x > 0])
        n = len(sets)
        ans = 1

        for i in range(n + 1):
            if ans not in sets:
                break
            ans += 1

        return ans

    def firstMissingPositive1(self, nums: 'List[int]') -> int:
        """
        分析题意，可知结果只能是[1,n+1]
        可以使用nums数组存储，对于在[1,n]范围内的数，打上标记，不在这个范围内的数存储这个位置上的数的绝对值的负数
        """
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1

        for i in range(n):
            num = abs(nums[i])
            if 0 < num < n + 1:
                # 将这个位置的数字标记为负数
                nums[num - 1] = -abs(nums[num - 1])

        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1
