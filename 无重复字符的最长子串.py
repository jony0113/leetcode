#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 无重复字符的最长子串.py
Author: fangeng
Date: 2020/4/18 14:03
"""


class Solution:
    """
    给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s or len(s) < 1:
            return 0
        length = len(s)

        map = {}

        _max = 0
        start, end = 0, 0
        while end < length:
            if s[end] in map:
                # 当前字符如果没有出现在区间内，则不用更新区间的起始位置
                start = max(map[s[end]] + 1, start)
            map[s[end]] = end
            _max = max(_max, end - start + 1)
            end += 1
        return _max
