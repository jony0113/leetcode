#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 圆圈中最后剩下的数字.py
Author: fangeng
Date: 2020/3/30 21:12
"""


class Solution:
    """
    题目：
    0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。
    例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，
    则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。

    约瑟夫环问题 当n=1, f(n,m)=0;当n>1时, f(n,m)=(f(n-1,m)+m)%n。
    可以用倒推的方法得出上述结论。
    """

    def lastRemaining(self, n: int, m: int) -> int:
        return 0 if n == 1 else (m + self.lastRemaining(n - 1, m)) % n

    def lastRemaining1(self, n: int, m: int) -> int:
        res = 0
        for i in range(2, n + 1):
            res = (m + res) % i
        return res
