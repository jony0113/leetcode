#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    """
    编写一个函数来查找字符串数组中的最长公共前缀。
    如果不存在公共前缀，返回空字符串 ""。
    """

    def longestCommonPrefix(self, strs: 'List[str]') -> str:
        if not strs or len(strs) < 1:
            return ""

        ans = strs[0]

        for s in strs:
            if not s.startswith(ans):
                length = min(len(ans), len(s))
                temp = ""
                for i in range(length):
                    if ans[i] == s[i]:
                        temp += ans[i]
                    else:
                        break
                ans = temp
            if ans == "":
                break
        return ans

    def longestCommonPrefix1(self, strs: 'List[str]') -> str:
        """
        字典树
        """

        class TrieNode:
            def __init__(self, val):
                self.val = val
                self.last = False
                self.next = {}

            def insert(self, s):
                if s == "":
                    self.last = True

                node = self
                length = len(s)
                for i in range(length):
                    next_node = node.next.get(s[i], None)
                    if not next_node:
                        next_node = TrieNode(s[i])
                        node.next[s[i]] = next_node
                    node = next_node
                    if i == length - 1:
                        node.last = True

        root = TrieNode("")

        for s in strs:
            root.insert(s)

        ans = ""
        while not root.last and len(root.next) == 1:
            root = root.next.popitem()[1]
            ans += root.val
        return ans
