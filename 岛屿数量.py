#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 岛屿数量.py
Author: fangeng
Date: 2020/4/20 21:16
"""


class Solution:
    """
    给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
    岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
    此外，你可以假设该网格的四条边均被水包围。

    11110
    11010
    11000
    00000   ->   1

    11000
    11000
    00100
    00011   ->   3
    """

    def numIslands(self, grid: 'List[List[str]]') -> int:
        if not grid or len(grid) < 1:
            return 0

        row = len(grid)
        col = len(grid[0])

        ans = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    ans += 1
                    grid[i][j] = '0'
                    temp = [(i, j)]
                    while len(temp) > 0:
                        r, c = temp.pop(0)
                        for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                            if 0 <= x < row and 0 <= y < col and grid[x][y] == '1':
                                grid[x][y] = '0'
                                temp.append((x, y))
        return ans
