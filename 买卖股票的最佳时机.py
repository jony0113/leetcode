#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 买卖股票的最佳时机.py
Author: fangeng
Date: 2020/4/13 20:55
"""


class Solution:
    """
    给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

    如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。

    注意：你不能在买入股票前卖出股票。
    """

    def maxProfit(self, prices: 'List[int]') -> int:
        if not prices or len(prices) < 2:
            return 0

        _min = prices[0]
        res = 0
        for item in prices:
            if item <= _min:
                _min = item
                continue
            temp_res = item - _min
            if temp_res > res:
                res = temp_res
        return res