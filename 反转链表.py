#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 反转链表.py
Author: fangeng
Date: 2020/4/30 21:30
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    反转一个单链表。

    输入: 1->2->3->4->5->NULL
    输出: 5->4->3->2->1->NULL
    """

    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        temp = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return temp

    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre
