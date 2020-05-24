#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 最大正方形.py
Author: fangeng
Date: 2020/5/8 21:18
"""


class Solution:
    """
    在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

    1 0 1 0 0
    1 0 1 1 1
    1 1 1 1 1
    1 0 0 1 0     ->      4
    """

    def maximalSquare(self, matrix: 'List[List[str]]') -> int:
        """
        dp[i][j]表示以i,j为右下角的正方形最大边长，
        dp[i][j] = min (dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
        """
        if not matrix or len(matrix) < 1:
            return 0

        row = len(matrix)
        col = len(matrix[0])

        ans = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == '1' and i - 1 >= 0 and j - 1 >= 0:
                    matrix[i][j] = min(int(matrix[i - 1][j - 1]), int(matrix[i - 1][j]),
                                       int(matrix[i][j - 1])) + 1
                ans = max(ans, int(matrix[i][j]))

        return ans * ans
