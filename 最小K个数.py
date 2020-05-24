#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 最小K个数.py
Author: fangeng
Date: 2020/5/13 22:06
"""
from queue import PriorityQueue


class Solution:
    """
    设计一个算法，找出数组中最小的k个数。以任意顺序返回这k个数均可。

    arr = [1,3,5,7,2,4,6,8], k = 4   ->   [1,2,3,4]
    """

    def smallestK(self, arr: 'List[int]', k: int) -> 'List[int]':
        if k < 1:
            return []
        heap = arr[:k]

        # 最后一个非叶子节点
        last = (k - 2) // 2

        # 将序号为j的元素和它的子元素比较，只到将其放到正确的位置
        def change(j):
            while j <= last:
                if 2 * j + 2 >= k:
                    if heap[j] < heap[2 * j + 1]:
                        heap[j], heap[2 * j + 1] = heap[2 * j + 1], heap[j]
                    break
                else:
                    _max = max(heap[j], heap[2 * j + 1], heap[2 * j + 2])
                    if heap[j] == _max:
                        break
                    else:
                        temp, heap[j] = heap[j], _max
                        if heap[2 * j + 1] == _max:
                            heap[2 * j + 1] = temp
                            j = 2 * j + 1
                        else:
                            heap[2 * j + 2] = temp
                            j = 2 * j + 2

        # 构建大顶堆
        for i in range(last, -1, -1):
            j = i
            change(j)

        length = len(arr)
        for i in range(k, length):
            if arr[i] >= heap[0]:
                continue
            else:
                heap[0] = arr[i]
                j = 0
                change(j)

        return heap

    def smallestK1(self, arr: 'List[int]', k: int) -> 'List[int]':
        if k < 1:
            return []

        heap = PriorityQueue(k)
        for i in range(k):
            heap.put((-arr[i], arr[i]))

        for i in range(k, len(arr)):
            _, v = heap.get()
            if arr[i] < v:
                heap.put((-arr[i], arr[i]))
            else:
                heap.put((-v, v))

        ans = []
        while not heap.empty():
            ans.append(heap.get()[1])

        return ans
