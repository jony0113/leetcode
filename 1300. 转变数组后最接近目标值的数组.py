#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    """
    给你一个整数数组 arr 和一个目标值 target ，请你返回一个整数 value ，
    使得将数组中所有大于 value 的值变成 value 后，数组的和最接近  target （最接近表示两者之差的绝对值最小）。

    如果有多种使得和最接近 target 的方案，请你返回这些整数中的最小值。

    请注意，答案不一定是 arr 中的数字。
    """

    def findBestValue(self, arr: 'List[int]', target: int) -> int:
        """
        先排序，然后遍历，当遍历的值大于target-当前累加和除以剩余个数时，返回剩余的平均值
        """
        arr.sort()
        sum_ = 0
        length = len(arr)

        for i in range(length):
            avg = (target - sum_) // (length - i)
            if arr[i] > avg:
                x = (target - sum_) / (length - i)
                # 找最接近的
                if x - avg > 0.5:
                    return avg + 1
                else:
                    return avg
            sum_ += arr[i]
        return arr[-1]
