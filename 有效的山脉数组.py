#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 有效的山脉数组.py
Author: fangeng
Date: 2020/3/19 22:05
"""


class Solution:
    """
    题目：
    给定一个整数数组 A，如果它是有效的山脉数组就返回 true，否则返回 false。
    让我们回顾一下，如果 A 满足下述条件，那么它是一个山脉数组：

    A.length >= 3
    在 0 < i < A.length - 1 条件下，存在 i 使得：
    A[0] < A[1] < ... A[i-1] < A[i]
    A[i] > A[i+1] > ... > A[B.length - 1]
    """

    def validMountainArray(self, a: 'List of int') -> bool:
        if not a or len(a) < 3 or a[0] >= a[1]:
            return False
        length = len(a)
        pre = a[0]
        bigger = True
        for i in range(1, length):
            if a[i] == pre:
                return False
            if bigger:
                if a[i] < pre:
                    pre = a[i]
                    bigger = False
                else:
                    pre = a[i]
            else:
                if a[i] > pre:
                    return False
                else:
                    pre = a[i]
        return not bigger
