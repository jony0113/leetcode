#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 合并区间.py
Author: fangeng
Date: 2020/4/16 21:05
"""


class Solution:
    """
    题目：给出一个区间的集合，请合并所有重叠的区间。

    [[1,4],[4,5]] -> [[1,5]]
    """

    def merge(self, intervals: 'List[List[int]]') -> 'List[List[int]]':
        if not intervals or len(intervals) < 1:
            return intervals
        intervals.sort(key=lambda x: x[0])

        def extend(list1, list2):
            ans = []
            a, b = list1
            c, d = list2
            if b < c:
                ans = [list1, list2]
            elif b >= c:
                ans = [[a, max(b, d)]]
            return ans

        res = [intervals[0]]
        length = len(intervals)
        for i in range(1, length):
            pre = res.pop()
            item = intervals[i]
            res.extend(extend(pre, item))
        return res
