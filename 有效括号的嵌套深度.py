#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 有效括号的嵌套深度.py
Author: fangeng
Date: 2020/4/1 21:53
"""


class Solution:
    """
    题目：
    有效括号字符串 定义：对于每个左括号，都能找到与之对应的右括号，反之亦然。
    嵌套深度 depth 定义：即有效括号字符串嵌套的层数，depth(A) 表示有效括号字符串 A 的嵌套深度。

    给你一个「有效括号字符串」 seq，请你将其分成两个不相交的有效括号字符串，A 和 B，并使这两个字符串的深度最小。
        不相交：每个 seq[i] 只能分给 A 和 B 二者中的一个，不能既属于 A 也属于 B 。
        A 或 B 中的元素在原字符串中可以不连续。
        A.length + B.length = seq.length
        深度最小：max(depth(A), depth(B)) 的可能取值最小。 

    划分方案用一个长度为 seq.length 的答案数组 answer 表示，编码规则如下：
        answer[i] = 0，seq[i] 分给 A 。
        answer[i] = 1，seq[i] 分给 B 。
        如果存在多个满足要求的答案，只需返回其中任意 一个 即可。

    (()()) -> [0,1,1,1,1,0]
    ()(())() -> [0,0,0,1,1,0,1,1]

    解析：需要匹配括号，要用到栈，只需要把(放入栈中，并且把栈的深度平分成两部分就好，
    分别将栈的深度是奇数/偶数的的分别分给两部分就好

    """

    def maxDepthAfterSplit(self, seq: str) -> 'List[int]':
        res = []

        # 记录当前栈的深度
        count = 0
        for ch in seq:
            if ch == '(':
                count += 1
                res.append(count % 2)
            if ch == ')':
                res.append(count % 2)
                count -= 1
        return res
