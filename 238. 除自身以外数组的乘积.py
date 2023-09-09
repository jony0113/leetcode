#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    """
    给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，
    其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

    提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。

    说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。
    """

    def productExceptSelf(self, nums: 'List[int]') -> 'List[int]':
        length = len(nums)
        left = [1] * length
        right = [1] * length

        for i in range(1, length):
            left[i] = left[i - 1] * nums[i - 1]

        for i in range(length - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        ans = []
        for i in range(length):
            ans.append(left[i] * right[i])
        return ans
