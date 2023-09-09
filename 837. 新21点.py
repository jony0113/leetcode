#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    """
    爱丽丝参与一个大致基于纸牌游戏 “21点” 规则的游戏，描述如下：

    爱丽丝以 0 分开始，并在她的得分少于 K 分时抽取数字。
    抽取时，她从 [1, W] 的范围中随机获得一个整数作为分数进行累计，
    其中 W 是整数。 每次抽取都是独立的，其结果具有相同的概率。

    当爱丽丝获得不少于 K 分时，她就停止抽取数字。 爱丽丝的分数不超过 N 的概率是多少？
    """

    def new21Game(self, N: int, K: int, W: int) -> float:
        # 最大能到K+W-1，最小为0，存储累积的数为x时每个数成功的概率
        dp = [0] * (K + W)

        # 记录下一轮开始时右侧的概率和
        temp = 0
        # 当累积到数字在[K,N]时，获胜的概率为1
        for i in range(K, min(N + 1, K + W)):
            dp[i] = 1
            temp += 1

        for i in range(K - 1, -1, -1):
            dp[i] = temp / W
            temp = temp + dp[i] - dp[i + W]

        return dp[0]
