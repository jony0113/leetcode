#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 最小的k个数.py
Author: fangeng
Date: 2020/3/20 21:31
"""


class Solution:
    """
    题目：
    输入整数数组 arr ，找出其中最小的 k 个数。
    例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。
    本题不要求输出的k个数是按顺序排列的，所以可以使用类似于快排的方法
    """

    def getLeastNumbers(self, arr: 'List[int]', k: int) -> 'List[int]':
        if not arr or len(arr) < 1 or k < 1 or k > len(arr):
            return []
        return sorted(arr)[0:k]

    def getLeastNumbers1(self, arr: 'List[int]', k: int) -> 'List[int]':
        if not arr or len(arr) < 1 or k < 1 or k > len(arr):
            return []
        self.quick_search(arr, 0, len(arr) - 1, k)
        return arr[:k]

    def quick_search(self, arr, l, r, k):
        """
        找到数组中最小的k个元素，并使它们全部位于数组的最左边
        """
        pos = self.partition(arr, l, r)
        width = pos - l + 1
        if k < width:
            self.quick_search(arr, l, pos - 1, k)
        elif k > width:
            self.quick_search(arr, pos + 1, r, k - width)

    def partition(self, arr, l, r):
        """
        选取第r个元素作为标志，该函数能够使比r小的元素全部位于该元素左边（不保证完全排序），
        并且返回该元素在数组中的位置
        """
        num = arr[r]
        i = l - 1
        for j in range(l, r):
            if arr[j] <= num:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[r], arr[i + 1] = arr[i + 1], arr[r]
        return i + 1
