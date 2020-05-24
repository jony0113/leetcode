#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 岛屿的最大面积.py
Author: fangeng
Date: 2020/5/2 21:23
"""


class Solution:
    """
    给定一个包含了一些 0 和 1 的非空二维数组 grid 。
    一个 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，
    这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。
    你可以假设 grid 的四个边缘都被 0（代表水）包围着。
    找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 0 。)
    """

    def maxAreaOfIsland(self, grid: 'List[List[int]]') -> int:
        if not grid or len(grid) < 1:
            return 0
        row = len(grid)
        col = len(grid[0])

        ans = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    temp = 1
                    grid[i][j] = 0
                    queue = [(i, j)]
                    while len(queue) > 0:
                        x, y = queue.pop(0)
                        for a, b in [(x + m, y + n) for m, n in [(-1, 0), (1, 0), (0, -1), (0, 1)]]:
                            if 0 <= a < row and 0 <= b < col and grid[a][b] == 1:
                                grid[a][b] = 0
                                temp += 1
                                queue.append((a, b))
                    ans = max(ans, temp)

        return ans


if __name__ == '__main__':
    print(Solution().maxAreaOfIsland(
        [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]))
