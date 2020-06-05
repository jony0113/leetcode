#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    """
    输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

    matrix = [[1,2,3],[4,5,6],[7,8,9]] -> [1,2,3,6,9,8,7,4,5]
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]] -> [1,2,3,4,8,12,11,10,9,5,6,7]
    """

    def spiralOrder(self, matrix: 'List[List[int]]') -> 'List[int]':
        if not matrix or len(matrix) < 1:
            return []

        row = len(matrix)
        col = len(matrix[0])

        ans = []

        top, bottom, left, right = 0, row - 1, 0, col - 1

        while top <= bottom and left <= right:
            if top <= bottom and left <= right:
                for i in range(left, right + 1):
                    ans.append(matrix[top][i])
                top += 1

            if top <= bottom and left <= right:
                for i in range(top, bottom + 1):
                    ans.append(matrix[i][right])
                right -= 1

            if top <= bottom and left <= right:
                for i in range(right, left - 1, -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1

            if top <= bottom and left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1
        return ans
