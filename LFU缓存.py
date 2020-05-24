#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: LFU缓存.py
Author: fangeng
Date: 2020/4/5 21:09
"""
import time


class LFUCache:
    """
    题目：
    请你为 最不经常使用（LFU）缓存算法设计并实现数据结构。它应该支持以下操作：get 和 put。

    get(key) - 如果键存在于缓存中，则获取键的值（总是正数），否则返回 -1。
    put(key, value) - 如果键不存在，请设置或插入值。当缓存达到其容量时，则应该在插入新项之前，
    使最不经常使用的项无效。在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，应该去除 最近 最少使用的键。
    「项的使用次数」就是自插入该项以来对其调用 get 和 put 函数的次数之和。使用次数会在对应项被移除后置为 0 。
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.container = {}

    def get(self, key: int) -> int:
        data = self.container.get(key)
        if data:
            value = data[0]
            count = data[1]
            self.container[key] = (value, count + 1, time.time())
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        data = self.container.get(key)
        if data:
            self.container[key] = (value, data[1] + 1, time.time())
        else:
            size = len(self.container)
            if size == self.capacity:
                k = self._find1()
                self.container.pop(k)
            self.container[key] = (value, 1, time.time())

    def _find1(self) -> int:
        sort_f = sorted(self.container.items(), key=lambda x: x[1][1])
        f = [(x[0], x[1][2]) for x in sort_f if x[1][1] == sort_f[0][1][1]]
        f.sort(key=lambda x: x[1])
        return f[0][0]

    def _find(self) -> int:
        freq = 0
        freq_list = []
        for k, v in self.container.items():
            f = v[1]
            t = v[2]
            if freq == 0 or f == freq:
                freq = f
                freq_list.append((k, t))
            if f < freq:
                freq_list.clear()
                freq = f
                freq_list.append((k, t))
        tm = 0
        key = -1
        for k, t in freq_list:
            if tm == 0:
                tm = t
                key = k
            elif t < tm:
                tm = t
                key = k
        return key


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == '__main__':
    cache = LFUCache(2)
    cache.put(2, 1)
    cache.put(3, 2)
    cache.get(3)
    cache.get(2)
    cache.put(4, 3)
