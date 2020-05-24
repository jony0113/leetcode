#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 另一个树的子树.py
Author: fangeng
Date: 2020/5/7 22:07
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。
    s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。
    """

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return not t
        if not t:
            return True

        queue = [s]
        while len(queue) > 0:
            node = queue.pop(0)
            if self.equal(node, t):
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False

    def equal(self, n1: TreeNode, n2: TreeNode) -> bool:
        if not n1:
            return not n2
        if not n2:
            return not n1
        if n1.val != n2.val:
            return False
        return self.equal(n1.left, n2.left) and self.equal(n1.right, n2.right)
