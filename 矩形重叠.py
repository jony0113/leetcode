#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 矩形重叠.py
Author: fangeng
Date: 2020/5/2 21:45
"""


class Solution:
    """
    矩形以列表 [x1, y1, x2, y2] 的形式表示，其中 (x1, y1) 为左下角的坐标，(x2, y2) 是右上角的坐标。
    如果相交的面积为正，则称两矩形重叠。需要明确的是，只在角或边接触的两个矩形不构成重叠。
    给出两个矩形，判断它们是否重叠并返回结果。
    """

    def isRectangleOverlap(self, rec1: 'List[int]', rec2: 'List[int]') -> bool:
        """
        如果重叠，那么x轴和y轴，两个都应该有交集
        """

        return max(rec1[0], rec2[0]) < min(rec1[2], rec2[2]) \
               and max(rec1[1], rec2[1]) < min(rec1[3], rec2[3])
