#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 136. 只出现一次的数字.py
Author: fangeng
Date: 2020/5/14 21:21
"""
from functools import reduce


class Solution:
    """
    给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
    """

    def singleNumber(self, nums: 'List[int]') -> int:
        """
        异或运算
        a ^ 0 = a
        a ^ a = 0
        """
        return reduce(lambda a, b: a ^ b, nums)
