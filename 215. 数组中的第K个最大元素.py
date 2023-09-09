#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    """
    在未排序的数组中找到第 k 个最大的元素。
    请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

    输入: [3,2,1,5,6,4] 和 k = 2
    输出: 5

    输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
    输出: 4
    """

    def findKthLargest(self, nums: 'List[int]', k: int) -> int:
        n = len(nums)
        target = n - k

        def partition(start, end):
            if start == end:
                return start

            pivot = nums[end]
            l, r = start, end - 1
            while l < r:
                while nums[l] < pivot and l < r:
                    l += 1
                while nums[r] >= pivot and l < r:
                    r -= 1
                if l < r:
                    nums[l], nums[r] = nums[r], nums[l]

            if nums[l] >= pivot:
                nums[l], nums[end] = pivot, nums[l]
                return l
            else:
                return end

        left, right = 0, n - 1
        while True:
            index = partition(left, right)
            if index == target:
                return nums[index]
            elif index > target:
                right = index - 1
            else:
                left = index + 1
