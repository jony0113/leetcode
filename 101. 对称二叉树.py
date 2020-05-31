#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    给定一个二叉树，检查它是否是镜像对称的。
    """

    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        def check(p: TreeNode, q: TreeNode) -> bool:
            if not p and not q:
                return True
            if not p or not q:
                return False

            return p.val == q.val and check(p.left, q.right) and check(p.right, q.left)

        return check(root.left, root.right)
