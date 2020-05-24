#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 76. 最小覆盖子串.py
Author: fangeng
Date: 2020/5/23 19:53
"""
import collections


class Solution:
    """
    给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字符的最小子串。
    S = "ADOBECODEBANC", T = "ABC"  ->   "BANC"
    """

    def minWindow(self, s: str, t: str) -> str:
        if not s:
            return ""
        t_counter = collections.Counter(t).items()
        s_dict = {}

        def check():
            for k, v in t_counter:
                if s_dict.get(k, 0) < v:
                    return False
            return True

        low = 0
        high = 0
        ans_l = -1
        ans_r = -1
        length = len(s)
        ans_length = length + 1
        while high < length:
            val = s[high]
            s_dict[val] = s_dict.get(val, 0) + 1
            high += 1

            while check() and low <= high:
                if high - low < ans_length:
                    ans_length = high - low
                    ans_l = low
                    ans_r = high
                low_val = s[low]
                s_dict[low_val] = s_dict.get(low_val) - 1
                low += 1

        return "" if ans_l == -1 else s[ans_l:ans_r]


if __name__ == '__main__':
    print(Solution().minWindow("cabwefgewcwaefgcf", "cae"))
