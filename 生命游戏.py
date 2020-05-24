#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 生命游戏.py
Author: fangeng
Date: 2020/4/2 21:31
"""


class Solution:
    """
    题目：
    生命游戏，简称为生命，是英国数学家约翰·何顿·康威在 1970 年发明的细胞自动机。
    给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。
    每个细胞都具有一个初始状态：1 即为活细胞（live），或 0 即为死细胞（dead）。
    每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：
        如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
        如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
        如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
        如果死细胞周围正好有三个活细胞，则该位置死细胞复活；

    根据当前状态，写一个函数来计算面板上所有细胞的下一个（一次更新后的）状态。
    下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。

    0,1,0               0,0,0
    0,0,1       ——>     1,0,1
    1,1,1               0,1,1
    0,0,0               0,1,0

    """

    def gameOfLife(self, board: 'List[List[int]]') -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        row = len(board)
        col = len(board[0])
        neighbor = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        def calculate(x, y):
            count = 0
            for p, q in [(x + m, y + n) for m, n in neighbor if
                         0 <= x + m < row and 0 <= y + n < col]:
                # -1：由活到死 0：死 1：活 2：由死到活
                count += (1 if board[p][q] in (1, -1) else 0)
            if board[x][y] == 1:
                return 1 if count in (2, 3) else -1
            if board[x][y] == 0:
                return 2 if count == 3 else 0

        for i in range(0, row):
            for j in range(0, col):
                board[i][j] = calculate(i, j)

        for i in range(0, row):
            for j in range(0, col):
                board[i][j] = (1 if board[i][j] > 0 else 0)
