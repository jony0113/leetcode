#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 快乐数.py
Author: fangeng
Date: 2020/3/21 22:32
"""


class Solution:
    """
    题目：
    编写一个算法来判断一个数是不是“快乐数”。

    一个“快乐数”定义为：对于一个正整数，
    每一次将该数替换为它每个位置上的数字的平方和，
    然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。
    如果可以变为 1，那么这个数就是快乐数。

    输入: 19
    输出: true
    解释:
    12 + 92 = 82
    82 + 22 = 68
    62 + 82 = 100
    12 + 02 + 02 = 1
    """

    def isHappy(self, n: int) -> bool:
        already = set()
        while n not in already:
            if n == 1:
                return True
            already.add(n)
            temp = n
            n = 0
            while temp != 0:
                n += ((temp % 10) ** 2)
                temp = int(temp / 10)
        return False

    def get_next(self, n: int) -> int:
        temp = n
        res = 0
        while temp != 0:
            res += ((temp % 10) ** 2)
            temp = int(temp / 10)
        return res

    def isHappy(self, n: int) -> bool:
        slow = n
        quick = self.get_next(n)
        while slow != quick:
            if slow == 1 or quick == 1:
                return True
            slow = self.get_next(slow)
            quick = self.get_next(self.get_next(quick))
        return slow == 1
