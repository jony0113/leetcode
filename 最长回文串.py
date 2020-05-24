#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 最长回文串.py
Author: fangeng
Date: 2020/5/1 18:03
"""
import collections


class Solution:
    """
    给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
    在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

    "abccccdd" -> "dccaccd" 7
    """

    def longestPalindrome(self, s: str) -> int:
        counter = collections.Counter(s)
        ans = 0
        for v in counter.values():
            ans += (v // 2) * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans
