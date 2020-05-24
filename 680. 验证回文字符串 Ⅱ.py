#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 680. 验证回文字符串 Ⅱ.py
Author: fangeng
Date: 2020/5/19 21:39
"""


class Solution:
    """
    给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
    """

    def validPalindrome(self, s: str) -> bool:
        if not s or len(s) < 3:
            return True
        left = 0
        right = len(s) - 1

        def check(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        while left < right:
            if s[left] != s[right]:
                return check(left, right - 1) or check(left + 1, right)
            left += 1
            right -= 1

        return True
