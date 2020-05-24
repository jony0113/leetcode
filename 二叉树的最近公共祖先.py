#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 二叉树的最近公共祖先.py
Author: fangeng
Date: 2020/5/10 21:15
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
    最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，
    满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
    例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]
    """

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == p or root == q:
            return root

        if root:
            l = self.lowestCommonAncestor(root.left, p, q)
            r = self.lowestCommonAncestor(root.right, p, q)
            if l and r:
                return root
            if not l:
                return self.lowestCommonAncestor(r, p, q)
            if not r:
                return self.lowestCommonAncestor(l, p, q)
        return None
