# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 按摩师.py
Author: fangeng
Date: 2020/3/24 21:58
"""


class Solution:
    """
    题目：
    一个有名的按摩师会收到源源不断的预约请求，每个预约都可以选择接或不接。
    在每次预约服务之间要有休息时间，因此她不能接受相邻的预约。给定一个预约请求序列，
    替按摩师找到最优的预约集合（总预约时间最长），返回总的分钟数。

    输入： [1,2,3,1]
    输出： 4
    解释： 选择 1 号预约和 3 号预约，总时长 = 1 + 3 = 4。

    输入： [2,7,9,3,1]
    输出： 12
    解释： 选择 1 号预约、 3 号预约和 5 号预约，总时长 = 2 + 9 + 1 = 12。

    输入： [2,1,4,5,3,1,1,3]
    输出： 12
    解释： 选择 1 号预约、 3 号预约、 5 号预约和 8 号预约，总时长 = 2 + 4 + 3 + 3 = 12。
    """

    def massage(self, nums: 'List[int]') -> int:
        if not nums or len(nums) < 1:
            return 0
        length = len(nums)
        a = 0
        b = nums[0]
        flag = True
        for i in range(1, length):
            if flag:
                temp = max(b, a + nums[i])
            else:
                temp = a + nums[i]
            if temp > b:
                flag = True
                a, b = b, temp
            else:
                flag = False
                a = b
        return b


if __name__ == '__main__':
    print(Solution().massage([2, 7, 6, 3, 1]))
