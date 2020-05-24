#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 零钱兑换.py
Author: fangeng
Date: 2020/5/1 17:30
"""


class Solution:
    """
    给定不同面额的硬币 coins 和一个总金额 amount。
    编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
    如果没有任何一种硬币组合能组成总金额，返回 -1。
    """

    def coinChange(self, coins: 'List[int]', amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1

        for i in range(1, amount + 1):
            if dp[i] > 0:
                continue
            temp = -1
            for coin in coins:
                if i - coin > 0 and dp[i - coin] > 0:
                    if temp == -1:
                        temp = dp[i - coin] + 1
                    else:
                        temp = min(temp, dp[i - coin] + 1)
            dp[i] = temp
        return dp[amount]


if __name__ == '__main__':
    Solution().coinChange([1, 2, 5], 11)
