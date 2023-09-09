#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    """
    给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
    使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

    注意：答案中不可以包含重复的三元组。
    """

    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        length = len(nums)
        nums.sort()
        ans = []

        for first in range(length):
            # 确保第一个数不重复
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            third = length - 1
            target = -nums[first]

            for second in range(first + 1, length):
                # 确保第二个数不重复
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue

                # 如果加和太大，需要将第三个数减小
                while second < third and nums[second] + nums[third] > target:
                    third -= 1

                if second == third:
                    break

                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])

        return ans
