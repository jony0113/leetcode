#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 括号生成.py
Author: fangeng
Date: 2020/4/9 21:18
"""


class Solution:
    """
    数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
    """

    def generateParenthesis(self, n: int) -> 'List[str]':
        def generate(s):
            r = []
            for j in range(0, len(s) + 1):
                t = list(s)
                t.insert(j, '()')
                r.append(''.join(t))
            return r

        if n == 0:
            return []
        res = {'()'}
        for i in range(2, n + 1):
            nex = []
            for item in res:
                temp = generate(item)
                nex.extend(temp)
            res = set(nex)

        return list(res)
