#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 三维形体的表面积.py
Author: fangeng
Date: 2020/3/25 21:53
"""


class Solution:
    """
    题目：
    在 N * N 的网格上，我们放置一些 1 * 1 * 1  的立方体。
    每个值 v = grid[i][j] 表示 v 个正方体叠放在对应单元格 (i, j) 上。
    输入为一个二维数组，表示在该网格上各个位置有几个正方体
    请你返回最终形体的表面积。

    [[2]] -> 10
    [[1,2],[3,4]] -> 34
    [[1,0],[0,2]] -> 16
    [[1,1,1],[1,0,1],[1,1,1]] - > 32

    """

    def surfaceArea(self, grid: 'List[List[int]]') -> int:
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        length = len(grid)
        res = 0
        for i in range(length):
            for j in range(length):
                res += (grid[i][j] * 4 + 2 if grid[i][j] != 0 else 0)
                if i - 1 >= 0:
                    res -= (min(grid[i][j], grid[i - 1][j]) * 2)
                if j - 1 >= 0:
                    res -= (min(grid[i][j], grid[i][j - 1]) * 2)
        return res


if __name__ == '__main__':
    print(Solution().surfaceArea([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
