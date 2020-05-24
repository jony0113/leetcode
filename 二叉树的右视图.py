#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 二叉树的右视图.py
Author: fangeng
Date: 2020/4/22 21:48
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

    [1,2,3,null,5,null,4] -> [1,3,4]
    """

    def rightSideView(self, root: TreeNode) -> 'List[int]':
        if not root:
            return []
        res = []
        queue = [root]
        cur = 1
        nex = 0
        while len(queue) > 0:
            if cur == 0:
                cur = nex
                nex = 0
                continue
            node = queue.pop(0)
            if node.left:
                nex += 1
                queue.append(node.left)
            if node.right:
                nex += 1
                queue.append(node.right)

            if cur == 1:
                res.append(node.val)
            cur -= 1
        return res
