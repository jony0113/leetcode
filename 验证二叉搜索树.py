#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 验证二叉搜索树.py
Author: fangeng
Date: 2020/5/5 15:00
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    给定一个二叉树，判断其是否是一个有效的二叉搜索树。

    假设一个二叉搜索树具有如下特征：
        节点的左子树只包含小于当前节点的数。
        节点的右子树只包含大于当前节点的数。
        所有左子树和右子树自身必须也是二叉搜索树。

    """

    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = []
        pre = float('-inf')

        cur = root

        while len(stack) > 0 or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if pre < cur.val:
                pre = cur.val
            else:
                return False
            cur = cur.right
        return True
