#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 两数相加.py
Author: fangeng
Date: 2020/4/16 22:02
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，
    并且它们的每个节点只能存储 一位 数字。
    如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
    您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

    (2 -> 4 -> 3) + (5 -> 6 -> 4) -> (7 -> 0 -> 8)
    """

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def generate(val):
            if val < 10:
                return 0, ListNode(val)
            else:
                return val // 10, ListNode(val % 10)

        ans = ListNode(0)
        tail = ans
        pop = 0
        while l1 or l2:
            val = pop
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            pop, node = generate(val)
            tail.next = node
            tail = tail.next

        if pop:
            pop, node = generate(pop)
            tail.next = node
        return ans.next
