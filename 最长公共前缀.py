#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 最长公共前缀.py
Author: fangeng
Date: 2020/4/20 23:00
"""


class Solution:
    """
    编写一个函数来查找字符串数组中的最长公共前缀。
    如果不存在公共前缀，返回空字符串 ""。
    """

    def longestCommonPrefix(self, strs: 'List[str]') -> str:
        if not strs or len(strs) < 1:
            return ""
        if len(strs) == 1:
            return strs[0]

        length = len(strs[0])
        longest = strs[0]
        strs.remove(strs[0])
        n = 0

        def match(p, s):
            for item in s:
                if not item.startswith(p):
                    return False
            return True

        while n <= length - 1:
            prefix = longest[:n + 1]
            if not match(prefix, strs):
                break
            n += 1

        return longest[:n]

