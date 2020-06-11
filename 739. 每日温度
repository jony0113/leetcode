#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    """
    请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，
    至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0 来代替。

    例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，
    你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。
    """

    def dailyTemperatures(self, T: 'List[int]') -> 'List[int]':
        ans = [0] * len(T)

        # 存储当前还没找到更高温度的index，栈里面存储的index对应的温度一定是单调递减，否则应该找到了比它高的温度
        stack = []
        for i in range(len(T)):

            # 如果栈里面有比当前温度低的，那么这些元素就已经找到了比它们高的温度
            while len(stack) > 0 and T[i] > T[stack[-1]]:
                index = stack[-1]
                ans[index] = i - index
                stack.pop()
            stack.append(i)
        return ans
