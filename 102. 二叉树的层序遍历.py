#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 102. 二叉树的层序遍历.py
Author: fangeng
Date: 2020/5/13 21:13
"""

# Definition for a binary tree node.
import copy


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
      3
     / \
    9  20
      /  \
     15   7

    ->

    [
        [3],
        [9,20],
        [15,7]
    ]
    """

    def levelOrder(self, root: TreeNode) -> 'List[List[int]]':
        ans = []
        if root:
            queue = [root]
            cur = 1
            nex = 0
            nodes = []
            while len(queue) > 0:
                if cur == 0:
                    ans.append(copy.deepcopy(nodes))
                    nodes = []
                    cur = nex
                    nex = 0
                node = queue.pop(0)
                cur -= 1
                nodes.append(node.val)
                if node.left:
                    nex += 1
                    queue.append(node.left)
                if node.right:
                    nex += 1
                    queue.append(node.right)
            ans.append(nodes)
        return ans