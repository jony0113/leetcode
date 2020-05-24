#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 机器人的运动范围.py
Author: fangeng
Date: 2020/4/8 21:25
"""


class Solution:
    """
    题目：
    地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。
    一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），
    也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，
    因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？
    """

    def movingCount(self, m: int, n: int, k: int) -> int:
        if m < 1 or n < 1:
            return 0
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        reached = set()
        queue = [(0, 0)]

        def num_sum(num):
            res = 0
            while num > 0:
                res += (num % 10)
                num //= 10
            return res

        while len(queue) > 0:
            i, j = queue.pop(0)
            if (i, j) in reached:
                continue
            reached.add((i, j))
            node_list = [(i + x, j + y) for x, y in direction if
                         0 <= i + x < m and 0 <= j + y < n and
                         num_sum(i + x) + num_sum(j + y) <= k]
            queue.extend(node_list)

        return len(reached)


if __name__ == '__main__':
    print(Solution().movingCount(1, 2, 1))
