#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Desc:
File: 两数相加 II.py
Author: fangeng
Date: 2020/4/14 21:24
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    题目：给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。
    它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。
    你可以假设除了数字 0 之外，这两个数字都不会以零开头。

    进阶：
    如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。

    (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4) -> (7 -> 8 -> 0 -> 7)
    """

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        遍历，转换成数字，相加，转换成链表
        :param l1:
        :param l2:
        :return:
        """
        if not l1:
            return l2
        if not l2:
            return l1

        a = 0
        b = 0
        while l1:
            a = (a * 10) + l1.val
            l1 = l1.next
        while l2:
            b = (b * 10) + l2.val
            l2 = l2.next
        res = a + b
        ans = None
        if res == 0:
            ans = ListNode(0)
        else:
            while res:
                nx = ListNode(res % 10)
                nx.next = ans
                ans = nx
                res //= 10
        return ans

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        放入栈中，依次相加，处理较长的链表，处理最后的进位
        :param l1:
        :param l2:
        :return:
        """
        if not l1:
            return l2
        if not l2:
            return l1

        stack1 = list()
        stack2 = list()
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        def generate(temp, ans):
            if temp >= 10:
                val = temp % 10
                pop = temp // 10
            else:
                val = temp
                pop = 0
            nx = ListNode(val)
            nx.next = ans
            ans = nx
            return ans, pop

        pop = 0
        ans = None
        while len(stack1) > 0 and len(stack2) > 0:
            temp = pop + stack1.pop() + stack2.pop()
            ans, pop = generate(temp, ans)
        while len(stack1) > 0:
            temp = pop + stack1.pop()
            ans, pop = generate(temp, ans)
        while len(stack2) > 0:
            temp = pop + stack2.pop()
            ans, pop = generate(temp, ans)
        if pop > 0:
            ans, pop = generate(pop, ans)
        return ans
