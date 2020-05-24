#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 105. 从前序与中序遍历序列构造二叉树.py
Author: fangeng
Date: 2020/5/22 20:08
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    根据一棵树的前序遍历与中序遍历构造二叉树。
    """

    def buildTree(self, preorder: 'List[int]', inorder: 'List[int]') -> TreeNode:
        if not preorder or not inorder or len(preorder) != len(inorder):
            return None
        length = len(preorder)
        return self.build(preorder, inorder, 0, length - 1, 0, length - 1)

    def build(self, pre_order, in_order, pre_left, pre_right, in_left, in_right):
        if not (0 <= pre_left <= pre_right < len(pre_order) and 0 <= in_left <= in_right < len(
                in_order)):
            return None
        if pre_left == pre_right:
            return TreeNode(pre_order[pre_left])

        def findIndex(li, left, right, target):
            while left <= right:
                if li[left] == target:
                    return left
                left += 1

        root_val = pre_order[pre_left]
        index = findIndex(in_order, in_left, in_right, root_val)
        left_count = index - in_left
        root = TreeNode(root_val)
        root.left = self.build(pre_order, in_order, pre_left + 1, pre_left + left_count,
                               in_left, index - 1)
        root.right = self.build(pre_order, in_order, pre_left + left_count + 1, pre_right,
                                index + 1, in_right)
        return root


if __name__ == '__main__':
    Solution().buildTree([1, 2], [2, 1])
