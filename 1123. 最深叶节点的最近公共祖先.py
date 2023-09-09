#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    给你一个有根节点 root 的二叉树，返回它 最深的叶节点的最近公共祖先 。
    回想一下：
    叶节点 是二叉树中没有子节点的节点
    树的根节点的 深度 为 0，如果某一节点的深度为 d，那它的子节点的深度就是 d+1
    如果我们假定 A 是一组节点 S 的 最近公共祖先，S 中的每个节点都在以 A 为根节点
    的子树中，且 A 的深度达到此条件下可能的最大值。
    '''
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.lcaHeight(root)[0]
    
    
    def lcaHeight(self, root: Optional[TreeNode]) -> (Optional[TreeNode],int):
        if root is None:
            return root,0
        ll,hl = self.lcaHeight(root.left)
        lr,hr = self.lcaHeight(root.right)
        if hl > hr:
            return ll,hl + 1
        if hl < hr:
            return lr,hr + 1
        return root, hl + 1