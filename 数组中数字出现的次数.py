#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 数组中数字出现的次数.py
Author: fangeng
Date: 2020/4/28 21:08
"""


class Solution:
    """
    一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。
    要求时间复杂度是O(n)，空间复杂度是O(1)。
    """

    def singleNumbers(self, nums: 'List[int]') -> 'List[int]':

        # temp的最终结果是两个不同数字异或的结果
        temp = 0
        for num in nums:
            temp = temp ^ num

        # 接下来考虑需要把两个不同数字分开，这两个数字的区别是啥呢，他们肯定有至少1位上的数字不同
        # 怎么找这个数呢，他们这一位上异或的结果肯定是1，所以只要找到temp里面为1的那一位，
        # 然后根据这一位是不是1来进行区分就行了
        index = 0
        while True:
            if (temp >> index) & 1:
                break
            index += 1

        a = 0
        b = 0

        for num in nums:
            if (num >> index) & 1:
                a ^= num
            else:
                b ^= num
        return [a, b]

if __name__ == '__main__':
    print(Solution().singleNumbers([7,1,7,2,6,6,3,1]))