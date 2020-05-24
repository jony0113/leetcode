#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 将数组分成和相等的三个部分.py
Author: fangeng
Date: 2020/5/2 22:35
"""


class Solution:
    """
    给你一个整数数组 A，只有可以将其划分为三个和相等的非空部分时才返回 true，否则返回 false。
    形式上，如果可以找出索引 i+1 < j 且满足 
    (A[0] + A[1] + ... + A[i]
     == A[i+1] + A[i+2] + ... + A[j-1]
     == A[j] + A[j-1] + ... + A[A.length - 1]) 就可以将数组三等分。
    """

    def canThreePartsEqualSum(self, A: 'List[int]') -> bool:
        if not A or len(A) < 3:
            return False
        _sum = sum(A)
        if _sum % 3 != 0:
            return False

        target = _sum // 3
        _sum = 0

        x = -1
        y = -1

        for i in range(len(A)):
            _sum += A[i]
            if x == -1 and _sum == target:
                x = i
                continue
            if x >= 0 and _sum == 2 * target:
                y = i
                break

        if 0 <= x < y < len(A) - 1:
            return True
        return False


if __name__ == '__main__':
    print(Solution().canThreePartsEqualSum([10, -10, 10, -10, 10, -10, 10, -10]))
