#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 回文数.py
Author: fangeng
Date: 2020/4/20 22:24
"""


class Solution:
    """
    题目：
    判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
    不转换成字符串，解答
    """

    def isPalindrome(self, x: int) -> bool:
        """
        取出后一半的数进行翻转
        """

        # 负数以及末位为0(200) 这样的数字返回False
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverse_num = 0
        while x > reverse_num:
            reverse_num = reverse_num * 10 + x % 10
            x //= 10

        # 原来的数字是偶数位，判断是否相等；原来的数字是奇数位，判断反转后的数字除以10
        return x == reverse_num or x == reverse_num // 10

if __name__ == '__main__':
    Solution().isPalindrome(121)