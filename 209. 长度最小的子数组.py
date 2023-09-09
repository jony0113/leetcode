#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    """
    给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组，
    并返回其长度。如果不存在符合条件的连续子数组，返回 0。
    """

    def minSubArrayLen(self, s: int, nums: 'List[int]') -> int:
        if not nums:
            return 0
        n = len(nums)
        left, right = 0, 0
        _sum = 0
        ans = n + 1
        while right < n:
            _sum += nums[right]
            while _sum >= s:
                ans = min(ans, right - left + 1)
                _sum -= nums[left]
                left += 1
            right += 1

        if ans == n+1:
            return 0
        else:
            return ans


if __name__ == '__main__':
    print(Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
