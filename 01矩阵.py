#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 01矩阵.py
Author: fangeng
Date: 2020/4/15 21:04
"""


class Solution:
    """
    给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。

    两个相邻元素间的距离为 1 。

    1. 广度优先遍历
    2.

    """

    def updateMatrix(self, matrix: 'List[List[int]]') -> 'List[List[int]]':
        """
        广度优先
        :param matrix:
        :return:
        """
        if not matrix or len(matrix) < 1:
            return []

        row = len(matrix)
        col = len(matrix[0])
        res = [[row + col] * col for _ in range(row)]

        direction = [(-1, 0), (0, -1), (0, 1), (1, 0)]

        # 存放所有元素为0的点的坐标
        now = set()
        nex = set()
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    res[i][j] = 0
                    now.add((i, j))

        while len(now) > 0 or len(nex) > 0:
            # now中没有坐标，说明最小距离为这些值的坐标已经遍历完成，开始遍历下一组
            if len(now) == 0:
                now = nex
                nex = set()
            i, j = now.pop()
            temp = [(i + x, j + y) for x, y in direction if
                    0 <= i + x < row and 0 <= j + y < col]
            for m, n in temp:
                # 相邻的节点如果现在的距离比通过当前节点的距离小，则更新，并放入下一次遍历
                val = res[i][j] + 1
                if val < res[m][n]:
                    res[m][n] = val
                    nex.add((m, n))
        return res
