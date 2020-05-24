#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 交点.py
Author: fangeng
Date: 2020/4/12 17:37
"""


class Solution:
    """
    题目：
    给定两条线段（表示为起点start = {X1, Y1}和终点end = {X2, Y2}），如果它们有交点，请计算其交点，没有交点则返回空值。
    要求浮点型误差不超过10^-6。若有多个交点（线段重叠）则返回 X 值最小的点，X 坐标相同则返回 Y 值最小的点。
    """

    def intersection(self, start1: 'List[int]', end1: 'List[int]', start2: 'List[int]',
                     end2: 'List[int]') -> 'List[float]':
        res = []

        def inside(x1, y1, x2, y2, m, n):
            return min(x1, x2) <= m <= max(x1, x2) and min(y1, y2) <= n <= max(y1, y2)

        def update(res, x, y):
            if len(res) < 1:
                res = [x, y]
            else:
                x0, y0 = res
                if x < x0 or (x == x0 and y < y0):
                    res = [x, y]
            return res

        x1, y1 = start1
        x2, y2 = end1
        x3, y3 = start2
        x4, y4 = end2

        # 线段平行
        if (x2 - x1) * (y4 - y3) == (x4 - x3) * (y2 - y1):
            # 线段在同一条直线上
            if (x3 - x1) * (y2 - y1) == (x2 - x1) * (y3 - y1):
                if inside(x1, y1, x2, y2, x3, y3):
                    res = update(res, x3, y3)
                if inside(x1, y1, x2, y2, x4, y4):
                    res = update(res, x4, y4)
                if inside(x3, y3, x4, y4, x1, y1):
                    res = update(res, x1, y1)
                if inside(x3, y3, x4, y4, x2, y2):
                    res = update(res, x2, y2)
        else:
            x = ((x1 - x2) * (x3 * y4 - x4 * y3) - (x3 - x4) * (x1 * y2 - x2 * y1)) \
                / ((x3 - x4) * (y1 - y2) - (x1 - x2) * (y3 - y4))
            if min(x1, x2) <= x <= max(x1, x2) and min(x3, x4) <= x <= max(x3, x4):
                # 兼容与y轴平行的情况
                if x3 == x4:
                    y = ((y1 - y2) * x + (x1 * y2 - x2 * y1)) / (x1 - x2)
                else:
                    y = ((y3 - y4) * x + (x3 * y4 - x4 * y3)) / (x3 - x4)
                res = [x, y]
        return res
