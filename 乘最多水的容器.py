#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 乘最多水的容器.py
Author: fangeng
Date: 2020/4/18 13:47
"""


class Solution:
    """
    题目：
    给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
    在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
    找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
    """

    def maxArea(self, height: 'List[int]') -> int:
        if not height or len(height) < 2:
            return 0
        low = 0
        high = len(height) - 1
        area = 0
        while low < high:
            area = max(area, (high - low) * min(height[low], height[high]))
            if height[low] < height[high]:
                low += 1
            else:
                high -= 1

        return area
