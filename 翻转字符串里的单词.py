#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 翻转字符串里的单词.py
Author: fangeng
Date: 2020/4/10 20:59
"""


class Solution:
    """
    题目：
    给定一个字符串，逐个翻转字符串中的每个单词。
    the sky is blue -> blue is sky the
    """

    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))
