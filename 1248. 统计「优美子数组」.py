#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 1248. 统计「优美子数组」.py
Author: fangeng
Date: 2020/4/21 21:44
"""


class Solution:
    """
    题目：给你一个整数数组 nums 和一个整数 k。
    如果某个 连续 子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。
    请返回这个数组中「优美子数组」的数目。
    """

    def numberOfSubarrays(self, nums: 'List[int]', k: int) -> int:
        odd = [-1]

        # 将奇数全部插入数组
        for index, num in enumerate(nums):
            if num % 2 == 1:
                odd.append(index)

        odd.append(len(nums))
        odd_len = len(odd)

        ans = 0
        for i in range(1, odd_len - k):
            ans += (odd[i] - odd[i - 1]) * (odd[i + k] - odd[i + k - 1])
        return ans

    def numberOfSubarrays1(self, nums: 'List[int]', k: int) -> int:
        """
        双指针
        """
        start = end = 0
        odd_cnt = 0
        ans = 0
        while end < len(nums):
            if nums[end] & 1:
                odd_cnt += 1
            end += 1

            if odd_cnt == k:
                temp_end = end
                while end < len(nums) and nums[end] & 1 == 0:
                    end += 1
                right_cnt = end - temp_end + 1

                temp_start = start
                while nums[start] & 1 == 0:
                    start += 1
                left_cnt = start - temp_start + 1

                ans += right_cnt * left_cnt

                start += 1
                odd_cnt -= 1

        return ans
