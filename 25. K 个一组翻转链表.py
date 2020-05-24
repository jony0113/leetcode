#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 25. K 个一组翻转链表.py
Author: fangeng
Date: 2020/5/16 20:16
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
    k 是一个正整数，它的值小于或等于链表的长度。
    如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

    给你这个链表：1->2->3->4->5
        当 k = 2 时，应当返回: 2->1->4->3->5
        当 k = 3 时，应当返回: 3->2->1->4->5
    """

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k < 2:
            return head

        tail = head
        for i in range(k - 1):
            if tail.next:
                tail = tail.next
            else:
                return head

        # 下一轮的开始
        n_head = tail.next

        pre = head
        cur = head.next
        while cur != n_head:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        head.next = self.reverseKGroup(n_head, k)
        return pre
