#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    """
    序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，
    同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

    请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，
    你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。
    """

    def serialize(self, root):
        """
        Encodes a tree to a single string. 前序遍历，用None顶替空节点
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        nodes = []
        stack = []
        node = root
        while len(stack) > 0 or node:
            if not node:
                node = stack.pop().right
            while node:
                nodes.append(str(node.val))
                stack.append(node)
                node = node.left
            nodes.append("None")

        return ",".join(nodes)

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        vals = data.split(",")

        def deserialize_internal(vals):
            val = vals.pop(0)
            if val == "None":
                return None
            node = TreeNode(int(val))
            node.left = deserialize_internal(vals)
            node.right = deserialize_internal(vals)
            return node

        return deserialize_internal(vals)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
