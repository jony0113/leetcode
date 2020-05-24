#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 卡牌分组.py
Author: fangeng
Date: 2020/3/27 21:23
"""
import math


class Solution:
    """
    题目：
    给定一副牌，每张牌上都写着一个整数。

    此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：

    每组都有 X 张牌。
    组内所有的牌上都写着相同的整数。
    仅当你可选的 X >= 2 时返回 true。
    """

    def hasGroupsSizeX(self, deck: 'List[int]') -> bool:
        if not deck or len(deck) < 2:
            return False

        deck_dict = {}

        for item in deck:
            deck_dict[item] = deck_dict.get(item, 0) + 1

        x_values = list(set(deck_dict.values()))

        x = x_values[0]
        if x == 1:
            return False
        for item in x_values[1:]:
            x = math.gcd(x, item)
            if x == 1:
                return False
        return True
