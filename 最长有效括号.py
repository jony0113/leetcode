#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 最长有效括号.py
Author: fangeng
Date: 2020/4/25 20:52
"""


class Solution:
    """
    给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
    "(()" -> 2
    ")()())" -> 4
    """

    def longestValidParentheses(self, s: str) -> int:
        if not s or len(s) < 2:
            return 0

        stack = [-1]
        max_length = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            if s[i] == ')':
                stack.pop()
                if len(stack) > 0:
                    max_length = max(max_length, i - stack[-1])
                else:
                    stack.append(i)

        return max_length
