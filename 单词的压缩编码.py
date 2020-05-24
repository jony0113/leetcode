#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 单词的压缩编码.py
Author: fangeng
Date: 2020/3/28 20:47
"""
import collections
from functools import reduce


class Solution:
    """
    题目：

    给定一个单词列表，我们将这个列表编码成一个索引字符串 S 与一个索引列表 A。
    例如，如果这个列表是 ["time", "me", "bell"]，
    我们就可以将其表示为 S = "time#bell#" 和 indexes = [0, 2, 5]。
    对于每一个索引，我们可以通过从字符串 S 中索引的位置开始读取字符串，直到 "#" 结束，来恢复我们之前的单词列表。
    那么成功对给定单词列表进行编码的最小字符串长度是多少呢？
    """

    def minimumLengthEncoding(self, words: 'List[str]') -> int:
        res_words = sorted(list(set(words)), key=lambda x: len(x), reverse=True)
        res = []
        for word in res_words:
            flag = False
            for target in res:
                if target.endswith(word):
                    flag = True
                    break
            if not flag:
                res.append(word)

        return sum(len(x) + 1 for x in res)

    def minimumLengthEncoding1(self, words: 'List[str]') -> int:
        """
        字典树
        :param words:
        :return:
        """
        words = list(set(words))
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        nodes = [reduce(dict.__getitem__, word[::-1], trie)
                 for word in words]

        return sum(len(word) + 1
                   for i, word in enumerate(words)
                   if len(nodes[i]) == 0)


if __name__ == '__main__':
    print(Solution().minimumLengthEncoding1(['lo', 'hello']))
