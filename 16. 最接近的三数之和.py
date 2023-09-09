#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    """
    给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
    找出 nums 中的三个整数，使得它们的和与 target 最接近。
    返回这三个数的和。假定每组输入只存在唯一答案。
    """

    def threeSumClosest(self, nums: 'List[int]', target: int) -> int:
        if not nums or len(nums) < 3:
            return 0
        n = len(nums)
        nums.sort()

        ans = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, n - 1

            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return target

                if abs(s - target) < abs(ans - target):
                    ans = s

                if s < target:
                    j += 1
                else:
                    k -= 1

        return ans
