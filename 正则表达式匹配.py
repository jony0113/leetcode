#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 正则表达式匹配.py
Author: fangeng
Date: 2020/3/18 21:14
"""


class Solution:
    """
    题目：
    给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
    '.' 匹配任意单个字符
    '*' 匹配零个或多个前面的那一个元素
    所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
    """

    def isMatch(self, s: str, p: str) -> bool:
        memo = {}  # key: (i,j) value: True/False
        s_len = len(s)
        p_len = len(p)

        def dp(i, j):
            # 已经在备忘录中，直接返回
            if (i, j) in memo:
                return memo[(i, j)]

            # 模式串到达末尾
            if j == p_len:
                return i == s_len

            # 当前字符是否匹配
            cur = i < s_len and p[j] in [s[i], '.']

            # 如果接下来的字符是*，则可以直接把模式串后移2位(相当于略过当前字符和*)
            # 或者在当前字符匹配的情况下把匹配串后移一位
            if j < p_len - 1 and p[j + 1] == '*':
                res = dp(i, j + 2) or cur and dp(i + 1, j)
            else:
                # 接下来不是*，则只能在当前字符匹配的情况下，将匹配串和模式串都后移一位
                res = cur and dp(i + 1, j + 1)

            # 记录到备忘录中
            memo[(i, j)] = res
            return res

        return dp(0, 0)
