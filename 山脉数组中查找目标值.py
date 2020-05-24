#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 山脉数组中查找目标值.py
Author: fangeng
Date: 2020/4/29 22:22
"""


# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    """
    给你一个 山脉数组 mountainArr，请你返回能够使得 
    mountainArr.get(index) 等于 target 最小 的下标 index 值。
    如果不存在这样的下标 index，就请返回 -1。

    何为山脉数组？如果数组 A 是一个山脉数组的话，那它满足如下条件：

    首先，A.length >= 3
    其次，在 0 < i < A.length - 1 条件下，存在 i 使得：
    A[0] < A[1] < ... A[i-1] < A[i]
    A[i] > A[i+1] > ... > A[A.length - 1]
 
    你将 不能直接访问该山脉数组，必须通过 MountainArray 接口来获取数据：
    MountainArray.get(k) - 会返回数组中索引为k 的元素（下标从 0 开始）
    MountainArray.length() - 会返回该数组的长度
    """

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length()
        l = 0
        r = length - 1

        while l < r:
            mid = (l + r) // 2
            # 在递减序列
            if mountain_arr.get(mid) > mountain_arr.get(mid + 1):
                r = mid
            else:
                l = mid + 1

        mx = l
        l, r = 0, mx
        while l <= r:
            mid = (l + r) // 2
            num = mountain_arr.get(mid)
            if num == target:
                return mid
            elif num > target:
                r = mid - 1
            else:
                l = mid + 1

        l, r = mx, length - 1
        while l <= r:
            mid = (l + r) // 2
            num = mountain_arr.get(mid)
            if num == target:
                return mid
            elif num > target:
                l = mid + 1
            else:
                r = mid - 1
        return -1
