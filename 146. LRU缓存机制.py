#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None


class LRUCache:
    """
    运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。
    它应该支持以下操作： 获取数据 get 和 写入数据 put 。

    获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
    写入数据 put(key, value) - 如果密钥已经存在，则变更其数据值；如果密钥不存在，则插入该组「密钥/数据值」。
    当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。

    你是否可以在 O(1) 时间复杂度内完成这两种操作？

    """

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache.get(key)
            self._move_to_head(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache.get(key)
            node.value = value
            self._move_to_head(node)
        else:
            if len(self.cache) == self.capacity:
                node = self.tail.pre
                self.cache.pop(node.key)
                node.pre.next = self.tail
                self.tail.pre = node.pre

            node = Node(key, value)
            self.cache[key] = node

            node.pre = self.head
            node.next = self.head.next
            self.head.next.pre = node
            self.head.next = node

    def _move_to_head(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

        node.pre = self.head
        node.next = self.head.next
        self.head.next.pre = node
        self.head.next = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
