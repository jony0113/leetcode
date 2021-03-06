#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 最低票价.py
Author: fangeng
Date: 2020/5/6 21:25
"""
from functools import lru_cache


class Solution:
    """
    在一个火车旅行很受欢迎的国度，你提前一年计划了一些火车旅行。
    在接下来的一年里，你要旅行的日子将以一个名为 days 的数组给出。每一项是一个从 1 到 365 的整数。
    火车票有三种不同的销售方式：
        一张为期一天的通行证售价为 costs[0] 美元；
        一张为期七天的通行证售价为 costs[1] 美元；
        一张为期三十天的通行证售价为 costs[2] 美元。
        通行证允许数天无限制的旅行。 例如，如果我们在第 2 天获得一张为期 7 天的通行证，
        那么我们可以连着旅行 7 天：第 2 天、第 3 天、第 4 天、第 5 天、第 6 天、第 7 天和第 8 天。

    返回你想要完成在给定的列表 days 中列出的每一天的旅行所需要的最低消费。
    """

    def mincostTickets(self, days: 'List[int]', costs: 'List[int]') -> int:
        """
        dp[i]表示从第i天到最后一天的最小花费，
        若第i天必须出行，那么dp[i] = min(dp[i+1]+cost[0],dp[i+7]+cost[1],dp[i+30]+cost[i+30])
        若第i天不必出行，那么dp[i] = dp[i+1]
        """
        days_set = set(days)

        @lru_cache(None)
        def dp(i):
            if i > 365:
                return 0
            if i in days_set:
                return min(dp(i + d) + c for d, c in zip([1, 7, 30], costs))
            else:
                return dp(i + 1)

        return dp(1)

    def mincostTickets1(self, days: 'List[int]', costs: 'List[int]') -> int:
        """
        dp[i]表示从第days[i]天到最后一天的最小花费，
        那么dp[i] = min(dp[j1]+cost[0],dp[j7]+cost[1],dp[j30]+cost[i+30])
        """
