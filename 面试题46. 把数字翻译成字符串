#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    """
    给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，
    1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。
    一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。
    """

    def translateNum(self, num: int) -> int:
        """
        分两种情况考虑：
            前两位数可以合在一起翻译：11~25，这种情况下f(n)=f(n-1)+f(n-2)
            前两位数不能合在一起翻译：f(n)=f(n-1)
        """
        if num < 10:
            return 1
        num_str = str(num)
        if len(num_str) == 2:
            if num_str[0] > '2' or (num_str[0] == '2' and num_str[1] > '5'):
                return 1
            else:
                return 2
        else:
            if num_str[0] > '2' or (num_str[0] == '2' and num_str[1] > '5'):
                return self.translateNum(int(num_str[1:]))
            else:
                return self.translateNum(int(num_str[1:])) + self.translateNum(int(num_str[2:]))
