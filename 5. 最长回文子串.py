#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 5. 最长回文子串.py
Author: fangeng
Date: 2020/3/17 21:25
"""


class Solution:
    """
    题目：给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

    思路：
    一个字符串为回文，只需要两边的两个字符相等，并且中间的为回文。

    给定i,j分别为子串的起始、结束索引，p(i,j)为判断该子串是否为回文的函数，则可以得到以下函数关系
    p(i,j)= p(i) == p(j) and ( p(i+1,j-1) or j-i-2<=0 ) 不要忽略中间字符数只有一个的情况
    """
    def longestPalindrome(self, s: str) -> str:
        if s is None or len(s) < 2:
            return s

        length = len(s)
        dp = [[False for _ in range(length)] for _ in range(length)]

        # 第一个字符一定是回文
        left = 0
        right = 0
        for i in range(length - 1, -1, -1):
            for j in range(i + 1, length):
                dp[i][j] = s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1])
                if dp[i][j] and j - i > right - left:
                    left = i
                    right = j

        return s[left:right + 1]

