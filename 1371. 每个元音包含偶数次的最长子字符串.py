#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 1371. 每个元音包含偶数次的最长子字符串.py
Author: fangeng
Date: 2020/5/20 21:37
"""


class Solution:
    """
    给你一个字符串 s ，请你返回满足以下条件的最长子字符串的长度：每个元音字母，即 'a'，'e'，'i'，'o'，'u' ，在子字符串中都恰好出现了偶数次。

    "eleetminicoworoep" -> "leetminicowor" 13
    "leetcodeisgreat" -> "leetc" 5
    "bcbcbc" 6
    """

    def findTheLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        state = [-1] * (1 << 5)
        cur_stat = 0
        ans = 0
        for i in range(len(s)):
            if s[i] == 'a':
                cur_stat ^= (1 << 0)
            elif s[i] == 'e':
                cur_stat ^= (1 << 1)
            elif s[i] == 'i':
                cur_stat ^= (1 << 2)
            elif s[i] == 'o':
                cur_stat ^= (1 << 3)
            elif s[i] == 'u':
                cur_stat ^= (1 << 4)
            if state[cur_stat] == -1:
                state[cur_stat] = i
            else:
                ans = max(ans, i - state[cur_stat])
        return ans
