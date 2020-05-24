#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 使数组唯一的最小增量.py
Author: fangeng
Date: 2020/3/22 20:21
"""


class Solution:
    """
    题目：
    给定整数数组 A，每次 move 操作将会选择任意 A[i]，并将其递增 1。
    返回使 A 中的每个值都是唯一的最少操作次数。

    输入：[1,2,2]
    输出：1
    解释：经过一次 move 操作，数组将变为 [1, 2, 3]。

    输入：[3,2,1,2,1,7]
    输出：6
    解释：经过 6 次 move 操作，数组将变为 [3, 4, 1, 2, 5, 7]。
    可以看出 5 次或 5 次以下的 move 操作是不能让数组的每个值唯一的。
    """

    def minIncrementForUnique(self, A: 'List[int]') -> int:
        if not A or len(A) < 2:
            return 0
        A.sort()
        length = len(A)
        cur_max = A[0]
        sum_ = 0
        for i in range(1, length):
            if A[i] > A[i - 1]:
                cur_max = A[i]
            else:
                cur_max += 1
                sum_ += (cur_max - A[i])
                A[i] = cur_max
        return sum_