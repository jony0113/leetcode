#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    """
    给你两个二进制字符串，返回它们的和（用二进制表示）。

    输入为 非空 字符串且只包含数字 1 和 0。
    """

    def addBinary(self, a: str, b: str) -> str:
        if not a or not b:
            return ""
        index_a = len(a) - 1
        index_b = len(b) - 1

        ans = ""

        temp = 0

        while index_a >= 0 and index_b >= 0:
            num_a = int(a[index_a])
            num_b = int(b[index_b])
            sum_ = num_a + num_b + temp
            temp = sum_ // 2
            sum_ = sum_ % 2
            ans = str(sum_) + ans
            index_a -= 1
            index_b -= 1

        if index_b >= 0:
            index_a = index_b
            a = b

        while index_a >= 0:
            num_a = int(a[index_a])
            sum_ = num_a + temp
            temp = sum_ // 2
            sum_ = sum_ % 2
            ans = str(sum_) + ans
            index_a -= 1

        if temp > 0:
            ans = str(temp) + ans
        return ans
