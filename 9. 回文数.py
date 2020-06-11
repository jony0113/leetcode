#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    """
    判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
    """

    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        low = 0
        high = len(x_str) - 1
        while low < high:
            if x_str[low] != x_str[high]:
                return False
            low += 1
            high -= 1
        return True

    def isPalindrome1(self, x: int) -> bool:
        """
        不转换成字符串解答，取出后一半数字，反向组成新的数字，和前半段比较是否相同
        """

        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverse = 0
        while x > reverse:
            reverse = reverse * 10 + x % 10
            x //= 10

        # 注意数字位数为奇数时，reverse最终会比x多一位
        return x == reverse or x == reverse // 10
