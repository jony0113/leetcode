#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 最小栈.py
Author: fangeng
Date: 2020/5/12 20:55
"""


class MinStack:
    """
    设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
    push(x) —— 将元素 x 推入栈中。
    pop() —— 删除栈顶的元素。
    top() —— 获取栈顶元素。
    getMin() —— 检索栈中的最小元素。
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.sort_list = []

    def _binary_find(self, x) -> int:
        left = 0
        right = len(self.sort_list) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.sort_list[mid] == x:
                return mid
            if self.sort_list[mid] > x:
                right = mid - 1
            if self.sort_list[mid] < x:
                left = mid + 1
        return left

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.sort_list.insert(self._binary_find(x), x)

    def pop(self) -> None:
        if len(self.stack) > 0:
            x = self.stack.pop()
            index = self._binary_find(x)
            for i in range(index + 1, len(self.sort_list)):
                self.sort_list[i - 1] = self.sort_list[i]
            self.sort_list.pop()
        else:
            raise IndexError

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            raise IndexError

    def getMin(self) -> int:
        if len(self.sort_list) > 0:
            return self.sort_list[0]
        else:
            raise IndexError


class MinStack_with_stack:
    """
    设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
    push(x) —— 将元素 x 推入栈中。
    pop() —— 删除栈顶的元素。
    top() —— 获取栈顶元素。
    getMin() —— 检索栈中的最小元素。
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.sort_list = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.sort_list) == 0 or x < self.getMin():
            self.sort_list.append(x)
        else:
            self.sort_list.append(self.getMin())

    def pop(self) -> None:
        if len(self.stack) > 0:
            self.stack.pop()
            self.sort_list.pop()
        else:
            raise IndexError

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            raise IndexError

    def getMin(self) -> int:
        if len(self.sort_list) > 0:
            return self.sort_list[-1]
        else:
            raise IndexError

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
