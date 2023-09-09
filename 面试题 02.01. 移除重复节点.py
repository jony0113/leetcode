#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。
    """

    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head:
            return head
        nodes = {head.val}
        pre = head
        while pre.next:
            now = pre.next
            if now.val in nodes:
                pre.next = now.next
            else:
                nodes.add(now.val)
                pre = now
        return head
