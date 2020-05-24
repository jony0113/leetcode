#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 编辑距离.py
Author: fangeng
Date: 2020/4/6 22:03
"""


class Solution:
    """
    给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

    你可以对一个单词进行如下三种操作：
        插入一个字符
        删除一个字符    等价于在另一个字符串插入一个字符
        替换一个字符
    """

    def minDistance(self, word1: str, word2: str) -> int:
        if not word1:
            return len(word2) if word2 else 0
        if not word2:
            return len(word1) if word1 else 0

        m = len(word1)
        n = len(word2)

        # dp[i][j] 代表word1的前i个字符转换为word2的前j个字符需要的最少操作次数
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 当有一个字符串为空串时，需要的最少操作次数是另一个字符串的长度
        for i in range(m + 1):
            dp[i][0] = i

        for i in range(n + 1):
            dp[0][i] = i

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 末尾插入一个字符
                x = dp[i - 1][j] + 1
                # 第二个字符末尾插入一个字符，等价于删除一个字符
                y = dp[i][j - 1] + 1
                # 注意i，j代表两个字符串的长度，所以此时两个字符的子序列为i-1，j-1
                # z代表替换末尾的字符
                if word1[i - 1] == word2[j - 1]:
                    z = dp[i - 1][j - 1]
                else:
                    z = dp[i - 1][j - 1] + 1
                dp[i][j] = min(x, y, z)

        return dp[m][n]
