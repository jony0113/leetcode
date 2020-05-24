#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 车的可用捕获量.py
Author: fangeng
Date: 2020/3/26 21:54
"""


class Solution:
    """
    题目：
    在一个 8 x 8 的棋盘上，有一个白色车（rook）。也可能有空方块，
    白色的象（bishop）和黑色的卒（pawn）。它们分别以字符 “R”，“.”，“B” 和 “p” 给出。
    大写字符表示白棋，小写字符表示黑棋。

    车按国际象棋中的规则移动：它选择四个基本方向中的一个（北，东，西和南），
    然后朝那个方向移动，直到它选择停止、到达棋盘的边缘或移动到同一方格来捕获该方格上颜色相反的卒。
    另外，车不能与其他友方（白色）象进入同一个方格。

    返回车能够在一次移动中捕获到的卒的数量。
    """

    def numRookCaptures(self, board: 'List[List[str]]') -> int:
        i = 0
        j = 0
        found = False
        while i < 8:
            j = 0
            while j < 8:
                if board[i][j] == "R":
                    found = True
                    break
                j += 1
            if found:
                break
            i += 1
        count = 0
        for y in range(i - 1, -1, -1):
            if y < 0 or board[y][j] == "B":
                break
            if board[y][j] == "p":
                count += 1
                break

        for y in range(i + 1, 8):
            if y > 7 or board[y][j] == "B":
                break
            if board[y][j] == "p":
                count += 1
                break

        for x in range(j - 1, -1, -1):
            if x < 0 or board[i][x] == "B":
                break
            if board[i][x] == "p":
                count += 1
                break
        for x in range(j + 1, 8):
            if x > 7 or board[i][x] == "B":
                break
            if board[i][x] == "p":
                count += 1
                break
        return count
