#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 多数元素.py
Author: fangeng
Date: 2020/4/13 21:17
"""


class Solution:
    """
    给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

    你可以假设数组是非空的，并且给定的数组总是存在多数元素。
    """

    def majorityElement(self, nums: 'List[int]') -> int:
        return sorted(nums)[nums // 2]
