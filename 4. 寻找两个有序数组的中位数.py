#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 4. 寻找两个有序数组的中位数.py
Author: fangeng
Date: 2020/4/18 15:34
"""


class Solution:
    """
    题目：
    给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
    请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
    你可以假设 nums1 和 nums2 不会同时为空。
    """

    def findMedianSortedArrays(self, nums1: 'List[int]', nums2: 'List[int]') -> float:
        def find(num1, start1, end1, num2, start2, end2, k):
            len1 = end1 - start1 + 1
            len2 = end2 - start2 + 1
            if len1 == 0:
                return num2[start2 + k - 1]
            if len2 == 0:
                return num1[start1 + k - 1]
            if k == 1:
                return min(num1[start1], num2[start2])
            i = start1 + min(len1, k // 2) - 1
            j = start2 + min(len2, k // 2) - 1

            # 二分法缩减区间
            if num1[i] < num2[j]:
                return find(num1, i + 1, end1, num2, start2, end2, k - (i - start1 + 1))
            else:
                return find(num1, start1, end1, num2, j + 1, end2, k - (j - start2 + 1))

        m = len(nums1)
        n = len(nums2)
        if (m + n) % 2 == 0:
            return (find(nums1, 0, m - 1, nums2, 0, n - 1, (m + n) // 2)
                    + find(nums1, 0, m - 1, nums2, 0, n - 1, (m + n) // 2 + 1)) / 2
        else:
            return find(nums1, 0, m - 1, nums2, 0, n - 1, (m + n) // 2 + 1)

