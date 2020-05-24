#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 链表的中间结点.py
Author: fangeng
Date: 2020/3/23 22:07
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    题目:
    给定一个带有头结点 head 的非空单链表，返回链表的中间结点。
    如果有两个中间结点，则返回第二个中间结点。

    [1,2,3,4,5] -> [3,4,5]
    [1,2,3,4,5,6] -> [4,5,6]
    """
    def middleNode(self, head: ListNode) -> ListNode:
        if not head or head.next is None:
            return head
        if head.next.next is None:
            return head.next
        slow = head
        quick = head
        while quick and quick.next:
            slow = slow.next
            quick = quick.next.next
        return slow
