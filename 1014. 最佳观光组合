#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    """
    给定正整数数组 A，A[i] 表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的距离为 j - i。

    一对景点（i < j）组成的观光组合的得分为（A[i] + A[j] + i - j）：景点的评分之和减去它们两者之间的距离。

    返回一对观光景点能取得的最高分。
    """

    def maxScoreSightseeingPair(self, A: 'List[int]') -> int:
        """
        A[i] + A[j] + i - j = (A[i] + i) + (A[j] - j)
        
        """
        if not A or len(A) < 2:
            return 0
        ans = 0

        # 存储当前为止最大的 A[i] + i 的值
        temp = A[0]
        length = len(A)

        for j in range(1, length):
            ans = max(ans, A[j] - j + temp)

            # 更新temp的值
            temp = max(temp, A[j] + j)

        return ans
