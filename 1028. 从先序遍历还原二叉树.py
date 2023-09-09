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
    我们从二叉树的根节点 root 开始进行深度优先搜索。

    在遍历中的每个节点处，我们输出 D 条短划线（其中 D 是该节点的深度），然后输出该节点的值。
    （如果节点的深度为 D，则其直接子节点的深度为 D + 1。根节点的深度为 0）。

    如果节点只有一个子节点，那么保证该子节点为左子节点。

    给出遍历输出 S，还原树并返回其根节点 root。
    """

    def recoverFromPreorder(self, S: str) -> TreeNode:
        if not S:
            return None

        path = []
        length = len(S)

        # 当前遍历到哪个位置
        i = 0
        while i < length:

            # 下一个节点的层级
            level = 0
            while i < length and S[i] == '-':
                level += 1
                i += 1

            # 节点的值
            val = 0
            while i < length and S[i].isdigit():
                val = val * 10 + ord(S[i]) - ord('0')
                i += 1
            node = TreeNode(val)

            # 层级和路径中的节点个数相同，则说明当前节点是上一个节点的左孩子
            if level == len(path):
                if path:
                    path[-1].left = node
            # 层级和路径中的节点个数不同，则一定小于路径中节点的个数
            else:
                # 将路径中大于层级的节点删除，因为它们都是右子节点为空的节点
                path = path[:level]
                # 当前节点是路径中最后一个节点的右子节点
                path[-1].right = node
            # 将当前节点加入到路径中
            path.append(node)
        return path[0]
