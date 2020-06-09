#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    """
    给定一个由表示变量之间关系的字符串方程组成的数组，每个字符串方程 equations[i] 的长度为 4，
    并采用两种不同的形式之一："a==b" 或 "a!=b"。在这里，a 和 b 是小写字母（不一定不同），表示单字母变量名。

    只有当可以将整数分配给变量名，以便满足所有给定的方程时才返回 true，否则返回 false。 

    """

    def equationsPossible(self, equations: 'List[str]') -> bool:
        class UnionFind:
            def __init__(self, capacity):
                self.parent = list(range(capacity))

            def find(self, x):
                """
                获取x的根节点
                """
                if self.parent[x] == x:
                    return x
                else:
                    # 路径压缩
                    self.parent[x] = self.find(self.parent[x])
                    return self.parent[x]

            def union(self, x, y):
                """
                让x的父节点指向y的根节点
                """
                self.parent[self.find(x)] = self.find(y)

        uf = UnionFind(26)
        # 初始化并查集
        for s in equations:
            if s[1] == '=':
                uf.union(ord(s[0]) - ord('a'), ord(s[3]) - ord('a'))

        for s in equations:
            if s[1] == '!' and uf.find(ord(s[0]) - ord('a')) == uf.find(ord(s[3]) - ord('a')):
                return False

        return True
