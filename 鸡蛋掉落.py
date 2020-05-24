#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 鸡蛋掉落.py
Author: fangeng
Date: 2020/4/11 20:53
"""


class Solution:
    """
    题目：
    你将获得 K 个鸡蛋，并可以使用一栋从 1 到 N  共有 N 层楼的建筑。

    每个蛋的功能都是一样的，如果一个蛋碎了，你就不能再把它掉下去。

    你知道存在楼层 F ，满足 0 <= F <= N 任何从高于 F 的楼层落下的鸡蛋都会碎，
    从 F 楼层或比它低的楼层落下的鸡蛋都不会破。

    每次移动，你可以取一个鸡蛋（如果你有完整的鸡蛋）并把它从任一楼层 X 扔下（满足 1 <= X <= N）。

    你的目标是确切地知道 F 的值是多少。

    无论 F 的初始值如何，你确定 F 的值的最小移动次数是多少？
    """

    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[N] * (N + 1) for _ in range(K + 1)]

        for i in range(N + 1):
            dp[0][i] = 0
            dp[1][i] = i

        for j in range(K + 1):
            dp[j][0] = 0
            dp[j][1] = 1

        for i in range(2, K + 1):
            for j in range(2, N + 1):
                left = 1
                right = j
                while left + 1 < right:
                    mid = (left + right) // 2
                    t1 = dp[i][j - mid]  # 单调递减
                    t2 = dp[i - 1][mid - 1]  # 单调递增
                    if t1 > t2:
                        left = mid + 1
                    else:
                        right = mid

                dp[i][j] = max(dp[i][j - left], dp[i - 1][left - 1]) + 1

        return dp[K][N]


if __name__ == '__main__':
    print(Solution().superEggDrop(9, 7813))
