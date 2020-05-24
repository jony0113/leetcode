#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 合并K个排序链表.py
Author: fangeng
Date: 2020/3/23 22:24
"""
from queue import PriorityQueue


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    题目：
    合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
    输入:
        [
            1->4->5,
            1->3->4,
            2->6
        ]
    输出: 1->1->2->3->4->4->5->6
    """

    def mergeKLists(self, lists) -> ListNode:
        """
        优先队列：先把lists里面的每个列表都放进优先队列中，
        在优先队列中按照头节点的值排序(为了在有相同元素时也能够进行排序，加入一个递增的count值进行区分)，
        然后依次从优先队列中取出一个元素
        :param lists:
        :return:
        """
        head = ListNode(0)
        tail = head
        queue = PriorityQueue()
        count = 0
        for item in lists:
            if item:
                queue.put((item.val, count, item))
                count += 1
        while not queue.empty():
            val, count, node = queue.get()
            tail.next = node
            tail = tail.next
            node = node.next
            if node:
                queue.put((node.val, count, node))
        return head.next

    def mergeKLists1(self, lists) -> ListNode:
        """
        每次拿出一个链表和已有的链表进行合并
        :param lists:
        :return:
        """
        if not lists or len(lists) < 1:
            return None

        node = lists.pop(0)
        for item in lists:
            node = self.mergeTwo(node, item)
        return node

    def mergeTwo(self, node1, node2):
        """
        合并两个链表
        :param node1:
        :param node2:
        :return:
        """
        head = tail = ListNode(0)
        while node1 and node2:
            if node1.val < node2.val:
                tail.next = node1
                node1 = node1.next
            else:
                tail.next = node2
                node2 = node2.next
            tail = tail.next
        if node1:
            tail.next = node1
        if node2:
            tail.next = node2
        return head.next

    def mergeKLists2(self, lists) -> ListNode:
        """
        分治：每次找两个进行合并，合并的结果再找两个合并(相当于合并了4个)，直到合并完成
        :param lists:
        :return:
        """
        if not lists or len(lists) < 1:
            return None
        length = len(lists)
        if length == 1:
            return lists[0]
        else:
            return self.mergeTwo(self.mergeKLists2(lists[:length // 2]),
                                 self.mergeKLists2(lists[length / 2:]))
