#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 旋转矩阵.py
Author: fangeng
Date: 2020/4/7 21:35
"""


class Solution:
    """
    给你一幅由 N × N 矩阵表示的图像，其中每个像素的大小为 4 字节。请你设计一种算法，将图像顺时针旋转 90 度。
    不占用额外内存空间能否做到？

    1. 第一行和最后一行互换，第二行和倒数第二行互换...
    2. 对角互换

    """

    def rotate(self, matrix: 'List[List[int]]') -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or len(matrix) <= 1:
            return

        n = len(matrix)
        i = 0
        j = n - 1
        while i < j:
            matrix[i], matrix[j] = matrix[j], matrix[i]
            i += 1
            j -= 1

        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
